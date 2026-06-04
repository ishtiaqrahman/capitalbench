from __future__ import annotations

import csv
import os
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Callable

from .io import load_manifest, load_options
from .prices import _price_rows_for_date, _write_price_csv
from .run_store import get_run_paths, list_run_ids, read_run_manifest
from .universe import TIINGO_API_KEY_ENV, TiingoFetcher, fetch_tiingo_eod_prices
from .web_sync import optional_sync_round
from .weekly import WeeklyPerformanceOutput, update_weekly_performance


DEFAULT_SNAPSHOTS_DIR = Path("market_data/daily_price_snapshots")
DEFAULT_MIN_SNAPSHOT_ROWS = 20


@dataclass(frozen=True)
class PriceSnapshotFile:
    target_date: str
    path: Path
    row_count: int
    source: str


@dataclass(frozen=True)
class InterimRoundSummary:
    round_id: str
    run_id: str | None
    status: str
    message: str
    snapshot_count: int = 0
    latest_snapshot_date: str | None = None
    weekly_prices_path: Path | None = None
    weekly_performance_path: Path | None = None
    performance_row_count: int = 0
    sync_status: str | None = None
    sync_message: str = ""


@dataclass(frozen=True)
class InterimPerformanceOutput:
    snapshot_date: str
    snapshot_path: Path
    snapshot_status: str
    discovered_snapshot_count: int
    updated_rounds: list[InterimRoundSummary] = field(default_factory=list)
    skipped_rounds: list[InterimRoundSummary] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


SyncFunc = Callable[[Path, str], Any]


def update_interim_performance(
    *,
    rounds_dir: Path,
    snapshot_date: str,
    snapshots_dir: Path = DEFAULT_SNAPSHOTS_DIR,
    universe_round: Path | None = None,
    track: str = "monthly",
    skip_fetch: bool = False,
    overwrite_snapshot: bool = False,
    sync: bool = True,
    soft_fail: bool = False,
    min_snapshot_rows: int = DEFAULT_MIN_SNAPSHOT_ROWS,
    fetcher: TiingoFetcher | None = None,
    sync_func: SyncFunc | None = None,
) -> InterimPerformanceOutput:
    """Update interim performance charts for active rounds from reusable price snapshots."""

    _validate_iso_date(snapshot_date, "snapshot date")
    if track not in {"weekly", "monthly", "all"}:
        raise ValueError("track must be one of: weekly, monthly, all")

    snapshot_path = snapshots_dir / f"{snapshot_date}.csv"
    snapshot_status = "missing"
    warnings: list[str] = []
    try:
        snapshot_status = _ensure_daily_snapshot(
            rounds_dir=rounds_dir,
            snapshots_dir=snapshots_dir,
            snapshot_date=snapshot_date,
            universe_round=universe_round,
            skip_fetch=skip_fetch,
            overwrite_snapshot=overwrite_snapshot,
            fetcher=fetcher,
        )
    except Exception as exc:
        if not soft_fail:
            raise
        snapshot_status = "failed"
        warnings.append(f"daily snapshot fetch failed for {snapshot_date}: {exc}")

    snapshots = discover_price_snapshots(
        rounds_dir=rounds_dir,
        snapshots_dir=snapshots_dir,
        min_snapshot_rows=min_snapshot_rows,
    )
    updated: list[InterimRoundSummary] = []
    skipped: list[InterimRoundSummary] = []
    for round_path in _round_paths(rounds_dir):
        try:
            round_summary = _update_interim_round(
                round_path,
                snapshots=snapshots,
                track=track,
                snapshot_date=snapshot_date,
                sync=sync,
                sync_func=sync_func,
            )
        except Exception as exc:
            manifest_id = _safe_round_id(round_path)
            round_summary = InterimRoundSummary(
                round_id=manifest_id,
                run_id=None,
                status="failed",
                message=str(exc),
            )
            warnings.append(f"{manifest_id}: {exc}")
        if round_summary.status == "updated":
            updated.append(round_summary)
        else:
            skipped.append(round_summary)
            if round_summary.status == "failed":
                warnings.append(f"{round_summary.round_id}: {round_summary.message}")

    return InterimPerformanceOutput(
        snapshot_date=snapshot_date,
        snapshot_path=snapshot_path,
        snapshot_status=snapshot_status,
        discovered_snapshot_count=len(snapshots),
        updated_rounds=updated,
        skipped_rounds=skipped,
        warnings=warnings,
    )


def discover_price_snapshots(
    *,
    rounds_dir: Path,
    snapshots_dir: Path = DEFAULT_SNAPSHOTS_DIR,
    min_snapshot_rows: int = DEFAULT_MIN_SNAPSHOT_ROWS,
) -> list[PriceSnapshotFile]:
    snapshots: list[PriceSnapshotFile] = []
    for path in sorted(snapshots_dir.glob("*.csv")) if snapshots_dir.exists() else []:
        snapshot = _read_price_snapshot(path, fallback_date=path.stem, source="daily_snapshot")
        if snapshot is not None and snapshot.row_count >= min_snapshot_rows:
            snapshots.append(snapshot)

    for round_path in _round_paths(rounds_dir):
        for filename, source in [("entry_prices.csv", "round_entry_prices"), ("exit_prices.csv", "round_exit_prices")]:
            path = round_path / "prices" / filename
            snapshot = _read_price_snapshot(path, fallback_date=None, source=source)
            if snapshot is not None and snapshot.row_count >= min_snapshot_rows:
                snapshots.append(snapshot)

    return _dedupe_snapshots(snapshots)


def _ensure_daily_snapshot(
    *,
    rounds_dir: Path,
    snapshots_dir: Path,
    snapshot_date: str,
    universe_round: Path | None,
    skip_fetch: bool,
    overwrite_snapshot: bool,
    fetcher: TiingoFetcher | None,
) -> str:
    snapshot_path = snapshots_dir / f"{snapshot_date}.csv"
    existed = snapshot_path.exists()
    if snapshot_path.exists() and not overwrite_snapshot:
        return "reused"
    if skip_fetch:
        return "missing"

    api_key = os.environ.get(TIINGO_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError("TIINGO_API_KEY is required unless --skip-fetch is passed")

    selected_round = universe_round or _latest_universe_round(rounds_dir)
    options = load_options(selected_round)
    fetch = fetcher or fetch_tiingo_eod_prices
    rows = _price_rows_for_date(options, snapshot_date, api_key, fetch)
    snapshots_dir.mkdir(parents=True, exist_ok=True)
    _write_price_csv(snapshot_path, rows)
    return "overwritten" if overwrite_snapshot and existed else "created"


def _latest_universe_round(rounds_dir: Path) -> Path:
    candidates: list[tuple[date, str, Path]] = []
    for round_path in _round_paths(rounds_dir):
        if not (round_path / "options.yaml").exists():
            continue
        try:
            manifest = load_manifest(round_path)
            key = date.fromisoformat(manifest.entry_date or manifest.decision_date or "0001-01-01")
        except Exception:
            continue
        candidates.append((key, round_path.name, round_path))
    if not candidates:
        raise FileNotFoundError(f"no round with options.yaml found under {rounds_dir}")
    return sorted(candidates, key=lambda item: (item[0], item[1]))[-1][2]


def _update_interim_round(
    round_path: Path,
    *,
    snapshots: list[PriceSnapshotFile],
    track: str,
    snapshot_date: str,
    sync: bool,
    sync_func: SyncFunc | None,
) -> InterimRoundSummary:
    manifest = load_manifest(round_path)
    round_id = manifest.round_id
    if not manifest.entry_date or not manifest.exit_date:
        return InterimRoundSummary(round_id, None, "skipped", "missing entry_date or exit_date")
    if not _track_matches(track, manifest.entry_date, manifest.exit_date, manifest.horizon):
        return InterimRoundSummary(round_id, None, "skipped", f"not a {track} round")
    if _parse_date(snapshot_date) >= _parse_date(manifest.exit_date):
        return InterimRoundSummary(round_id, None, "skipped", "snapshot date is on or after exit_date")
    if not (round_path / "prices" / "entry_prices.csv").exists():
        return InterimRoundSummary(round_id, None, "skipped", "missing entry_prices.csv")

    run_id = _selected_public_official_run_id(round_path)
    if run_id is None:
        return InterimRoundSummary(round_id, None, "skipped", "no selected public official run")

    selected_snapshots = [
        snapshot
        for snapshot in snapshots
        if _parse_date(manifest.entry_date) < _parse_date(snapshot.target_date) < _parse_date(manifest.exit_date)
    ]
    selected_snapshots.sort(key=lambda item: item.target_date)
    if not selected_snapshots:
        return InterimRoundSummary(round_id, run_id, "skipped", "no reusable interim snapshots after entry_date")

    try:
        output = update_weekly_performance(
            round_path,
            run_id,
            snapshot_price_files=[snapshot.path for snapshot in selected_snapshots],
            snapshot_dates=[snapshot.target_date for snapshot in selected_snapshots],
        )
    except Exception as exc:
        return InterimRoundSummary(round_id, run_id, "failed", f"weekly performance update failed: {exc}")

    sync_status: str | None = None
    sync_message = ""
    if sync:
        try:
            if sync_func is not None:
                sync_result = sync_func(round_path, run_id)
            else:
                sync_result = optional_sync_round(round_path, run_id=run_id, event_type="update_interim_performance")
            sync_status = str(getattr(sync_result, "status", "success"))
            sync_message = str(getattr(sync_result, "message", "") or "")
        except Exception as exc:
            sync_status = "failed"
            sync_message = str(exc)

    return _updated_summary(
        round_id=round_id,
        run_id=run_id,
        output=output,
        selected_snapshots=selected_snapshots,
        sync_status=sync_status,
        sync_message=sync_message,
    )


def _updated_summary(
    *,
    round_id: str,
    run_id: str,
    output: WeeklyPerformanceOutput,
    selected_snapshots: list[PriceSnapshotFile],
    sync_status: str | None,
    sync_message: str,
) -> InterimRoundSummary:
    message = f"updated through {selected_snapshots[-1].target_date}"
    if sync_status == "failed":
        message += f"; Supabase sync failed: {sync_message}"
    return InterimRoundSummary(
        round_id=round_id,
        run_id=run_id,
        status="updated",
        message=message,
        snapshot_count=output.snapshot_count,
        latest_snapshot_date=selected_snapshots[-1].target_date,
        weekly_prices_path=output.weekly_prices_path,
        weekly_performance_path=output.weekly_performance_path,
        performance_row_count=output.performance_row_count,
        sync_status=sync_status,
        sync_message=sync_message,
    )


def _selected_public_official_run_id(round_path: Path) -> str | None:
    candidates: list[tuple[int, str]] = []
    for run_id in list_run_ids(round_path):
        run_paths = get_run_paths(round_path, run_id)
        manifest = read_run_manifest(run_paths)
        if manifest.get("mock") is True:
            continue
        if str(manifest.get("run_type") or "") != "official":
            continue
        if not bool(manifest.get("official_score_eligible")):
            continue
        if _int_or_zero(manifest.get("invalid_submissions")) != 0:
            continue
        if _int_or_zero(manifest.get("valid_submissions")) <= 0:
            continue
        selected = 0 if bool(manifest.get("operator_selected_official")) else 1
        candidates.append((selected, run_id))
    if not candidates:
        return None
    return sorted(candidates)[0][1]


def _read_price_snapshot(path: Path, *, fallback_date: str | None, source: str) -> PriceSnapshotFile | None:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            return None
        if "option_id" not in reader.fieldnames:
            return None
        dates: set[str] = set()
        option_ids: set[str] = set()
        row_count = 0
        for row in reader:
            row_count += 1
            option_id = str(row.get("option_id") or "").strip()
            if option_id:
                option_ids.add(option_id)
            raw_date = str(row.get("date") or "").strip()
            if raw_date:
                dates.add(raw_date[:10])
    if not option_ids:
        return None
    target_date = _single_date(dates, fallback_date)
    if target_date is None:
        return None
    return PriceSnapshotFile(target_date=target_date, path=path, row_count=row_count, source=source)


def _single_date(dates: set[str], fallback_date: str | None) -> str | None:
    valid_dates = {item for item in dates if _looks_like_iso_date(item)}
    if len(valid_dates) == 1:
        return next(iter(valid_dates))
    if not valid_dates and fallback_date and _looks_like_iso_date(fallback_date):
        return fallback_date
    return None


def _dedupe_snapshots(snapshots: list[PriceSnapshotFile]) -> list[PriceSnapshotFile]:
    priority = {"daily_snapshot": 0, "round_entry_prices": 1, "round_exit_prices": 2}
    selected: dict[str, PriceSnapshotFile] = {}
    for snapshot in snapshots:
        existing = selected.get(snapshot.target_date)
        if existing is None:
            selected[snapshot.target_date] = snapshot
            continue
        current_key = (-snapshot.row_count, priority.get(snapshot.source, 9), snapshot.path.as_posix())
        existing_key = (-existing.row_count, priority.get(existing.source, 9), existing.path.as_posix())
        if current_key < existing_key:
            selected[snapshot.target_date] = snapshot
    return [selected[key] for key in sorted(selected)]


def _round_paths(rounds_dir: Path) -> list[Path]:
    if not rounds_dir.exists():
        return []
    return sorted(path.parent for path in rounds_dir.glob("*/manifest.yaml"))


def _is_monthly_round(entry_date: str, exit_date: str, horizon: str) -> bool:
    days = (_parse_date(exit_date) - _parse_date(entry_date)).days
    return days >= 28 or "month" in horizon.lower()


def _is_weekly_round(entry_date: str, exit_date: str, horizon: str) -> bool:
    days = (_parse_date(exit_date) - _parse_date(entry_date)).days
    return days < 28 and "week" in horizon.lower()


def _track_matches(track: str, entry_date: str, exit_date: str, horizon: str) -> bool:
    if track == "all":
        return _is_weekly_round(entry_date, exit_date, horizon) or _is_monthly_round(entry_date, exit_date, horizon)
    if track == "weekly":
        return _is_weekly_round(entry_date, exit_date, horizon)
    return _is_monthly_round(entry_date, exit_date, horizon)


def _safe_round_id(round_path: Path) -> str:
    try:
        return load_manifest(round_path).round_id
    except Exception:
        return round_path.name


def _parse_date(value: str) -> date:
    return date.fromisoformat(value)


def _validate_iso_date(value: str, label: str) -> None:
    try:
        _parse_date(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be YYYY-MM-DD: {value}") from exc


def _looks_like_iso_date(value: str) -> bool:
    try:
        _parse_date(value)
    except ValueError:
        return False
    return True


def _int_or_zero(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0

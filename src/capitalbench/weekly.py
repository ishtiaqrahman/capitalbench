from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .io import load_manifest, load_options, read_json
from .portfolio import allocation_views, primary_option_id, score_portfolio_return
from .run_store import get_run_paths, read_run_manifest
from .schemas import MarketOption, ModelSubmission, PriceRecord
from .scoring import (
    _find_sp500_option,
    _is_cash_option,
    _lookup_price,
    calculate_option_returns,
    read_price_records,
)
from .validation import iter_submission_files, validate_submission_payload


@dataclass(frozen=True)
class WeeklyPerformanceOutput:
    weekly_prices_path: Path
    weekly_performance_path: Path
    snapshot_count: int
    model_count: int
    price_row_count: int
    performance_row_count: int


@dataclass(frozen=True)
class PriceSnapshot:
    target_date: str
    price_file: Path
    price_records: dict[str, PriceRecord]


def update_weekly_performance(
    round_path: Path,
    run_id: str,
    *,
    snapshot_price_files: list[Path] | None = None,
    snapshot_dates: list[str] | None = None,
) -> WeeklyPerformanceOutput:
    manifest = load_manifest(round_path)
    options = load_options(round_path)
    run_paths = get_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    submissions = _load_valid_submissions(round_path, run_paths.parsed_dir, run_manifest, options)
    if not submissions:
        raise ValueError(f"no valid parsed submissions found for run_id: {run_id}")
    if not manifest.entry_date:
        raise ValueError("round manifest must define entry_date before weekly performance can be calculated")

    snapshot_price_files = snapshot_price_files or []
    snapshot_dates = snapshot_dates or []
    if len(snapshot_price_files) != len(snapshot_dates):
        raise ValueError("--snapshot-price-file and --snapshot-date must be provided the same number of times")

    entry_prices_path = round_path / "prices" / "entry_prices.csv"
    entry_prices = read_price_records(entry_prices_path)
    snapshots = [
        PriceSnapshot(
            target_date=manifest.entry_date,
            price_file=entry_prices_path,
            price_records=entry_prices,
        )
    ]
    seen_dates = {manifest.entry_date}
    for price_file, target_date in zip(snapshot_price_files, snapshot_dates):
        _validate_iso_date(target_date, "snapshot date")
        if target_date in seen_dates:
            raise ValueError(f"duplicate weekly snapshot target_date: {target_date}")
        snapshots.append(
            PriceSnapshot(
                target_date=target_date,
                price_file=price_file,
                price_records=read_price_records(price_file),
            )
        )
        seen_dates.add(target_date)
    snapshots.sort(key=lambda snapshot: snapshot.target_date)

    sp500_option = _find_sp500_option(options)
    selected_ids = set().union(*(set(allocation.option_id for allocation in allocation_views(item)) for item in submissions))
    required_option_ids = {sp500_option.option_id} | selected_ids
    required_option_ids.update(option.option_id for option in options if _is_cash_option(option))
    options_by_id = {option.option_id: option for option in options}

    weekly_price_rows: list[dict[str, object]] = []
    weekly_performance_rows: list[dict[str, object]] = []
    entry_date = date.fromisoformat(manifest.entry_date)

    for snapshot in snapshots:
        target = date.fromisoformat(snapshot.target_date)
        option_returns = calculate_option_returns(
            options,
            entry_prices,
            snapshot.price_records,
            selected_ids,
            required_option_ids=required_option_ids,
        )
        if sp500_option.option_id not in option_returns:
            raise ValueError(f"missing return for SP500 benchmark option_id: {sp500_option.option_id}")
        sp500_return = option_returns[sp500_option.option_id]

        for option_id in sorted(required_option_ids):
            option = options_by_id.get(option_id)
            if option is None:
                raise ValueError(f"selected option_id is not present in options.yaml: {option_id}")
            price_record = _price_record_for_required_option(snapshot.price_records, option)
            weekly_price_rows.append(
                {
                    "round_id": manifest.round_id,
                    "target_date": snapshot.target_date,
                    "price_date": price_record.date or snapshot.target_date,
                    "option_id": option.option_id,
                    "symbol": option.symbol or "",
                    "price": "" if price_record.price is None else price_record.price,
                    "price_source": price_record.source or price_record.price_source,
                    "published": True,
                }
            )

        for submission in sorted(submissions, key=lambda item: (item.provider, item.model_id, item.replicate_index or 1)):
            model_return = score_portfolio_return(submission, option_returns)
            allocations = allocation_views(submission)
            weekly_performance_rows.append(
                {
                    "round_id": manifest.round_id,
                    "run_id": run_id,
                    "model_id": submission.model_id,
                    "provider": submission.provider,
                    "target_date": snapshot.target_date,
                    "price_date": _snapshot_price_date(snapshot, sp500_option),
                    "days_elapsed": (target - entry_date).days,
                    "run_type": run_type,
                    "submission_format": "portfolio" if submission.portfolio is not None else "single_pick",
                    "selected_option_id": primary_option_id(submission),
                    "holding_count": len(allocations),
                    "model_return": model_return,
                    "sp500_return": sp500_return,
                    "alpha_vs_sp500": model_return - sp500_return,
                    "price_status": "complete",
                    "published": True,
                }
            )

    prices_path = round_path / "prices" / "weekly_prices.csv"
    performance_path = run_paths.results_dir / "weekly_performance.csv"
    _write_csv(
        prices_path,
        [
            "round_id",
            "target_date",
            "price_date",
            "option_id",
            "symbol",
            "price",
            "price_source",
            "published",
        ],
        weekly_price_rows,
    )
    _write_csv(
        performance_path,
        [
            "round_id",
            "run_id",
            "model_id",
            "provider",
            "target_date",
            "price_date",
            "days_elapsed",
            "run_type",
            "submission_format",
            "selected_option_id",
            "holding_count",
            "model_return",
            "sp500_return",
            "alpha_vs_sp500",
            "price_status",
            "published",
        ],
        weekly_performance_rows,
    )
    return WeeklyPerformanceOutput(
        weekly_prices_path=prices_path,
        weekly_performance_path=performance_path,
        snapshot_count=len(snapshots),
        model_count=len(submissions),
        price_row_count=len(weekly_price_rows),
        performance_row_count=len(weekly_performance_rows),
    )


def _load_valid_submissions(
    round_path: Path,
    parsed_dir: Path,
    run_manifest: dict[str, object],
    options: list[MarketOption],
) -> list[ModelSubmission]:
    manifest = load_manifest(round_path)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)
    submissions: list[ModelSubmission] = []
    for submission_path in iter_submission_files(parsed_dir):
        payload = read_json(submission_path)
        submissions.append(
            validate_submission_payload(
                payload,
                options,
                manifest.round_id,
                run_type=run_type,
                replicate_count=replicate_count,
                require_run_metadata=run_type in {"official", "stability", "retrospective"},
                submission_format=manifest.submission_format,
                portfolio_constraints=manifest.portfolio_constraints,
            )
        )
    return submissions


def _price_record_for_required_option(prices: dict[str, PriceRecord], option: MarketOption) -> PriceRecord:
    record = _lookup_price(prices, option)
    if record is not None:
        return record
    if _is_cash_option(option):
        return PriceRecord(option_id=option.option_id, symbol=option.symbol, price=1.0, date=None, source="cash")
    raise ValueError(f"missing weekly snapshot price for option_id: {option.option_id}")


def _snapshot_price_date(snapshot: PriceSnapshot, sp500_option: MarketOption) -> str:
    record = _price_record_for_required_option(snapshot.price_records, sp500_option)
    return record.date or snapshot.target_date


def _validate_iso_date(value: str, label: str) -> None:
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be YYYY-MM-DD: {value}") from exc


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

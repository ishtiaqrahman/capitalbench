from __future__ import annotations

import csv
import json
import mimetypes
import os
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Protocol

from .cumulative import (
    TRACKS,
    Track,
    build_cumulative_official,
    build_cumulative_stability,
    cumulative_status,
    latest_status,
    latest_selection_sort_key,
)
from .hashing import round_hashes_match, sha256_file
from .io import load_manifest, load_options, read_json, read_yaml
from .portfolio import allocation_views, portfolio_metrics, primary_option_id
from .run_store import get_run_paths, list_run_ids, read_run_manifest, resolve_run_id
from .schemas import ModelSubmission
from .validation import iter_submission_files

SUPABASE_SKIP_MESSAGE = "Supabase sync skipped: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not configured."
PUBLIC_ARTIFACT_BUCKET = "capitalbench-public-artifacts"
MODEL_DISPLAY_NAMES = {
    "anthropic-claude-fable-5": "Claude Fable 5",
    "anthropic-claude-opus-4-7": "Claude Opus 4.7",
    "anthropic-claude-opus-4-8": "Claude Opus 4.8",
    "google-gemini-3-1-pro": "Gemini 3.1 Pro",
    "openai-gpt-5-5": "GPT-5.5",
    "xai-grok-4-3": "Grok 4.3",
}


class WebSyncSink(Protocol):
    def upsert(self, table: str, rows: list[dict[str, Any]], *, on_conflict: str) -> None: ...

    def insert(self, table: str, rows: list[dict[str, Any]]) -> None: ...

    def delete_eq(self, table: str, filters: dict[str, Any]) -> None: ...

    def upload_public_artifact(self, local_path: Path, storage_path: str) -> None: ...


@dataclass(frozen=True)
class SyncSummary:
    event_type: str
    round_id: str | None = None
    run_id: str | None = None
    status: str = "success"
    message: str = ""
    row_counts: dict[str, int] = field(default_factory=dict)


class SupabaseWebSyncSink:
    def __init__(self, url: str, service_role_key: str) -> None:
        try:
            from supabase import create_client
        except ImportError as exc:  # pragma: no cover - exercised only without optional dependency.
            raise RuntimeError(
                "Supabase sync requires the optional supabase client. "
                "Install with `pip install 'capitalbench[web-sync]'` or `pip install supabase>=2,<3`."
            ) from exc
        self.client = create_client(url, service_role_key)

    def upsert(self, table: str, rows: list[dict[str, Any]], *, on_conflict: str) -> None:
        if not rows:
            return
        self.client.table(table).upsert(rows, on_conflict=on_conflict).execute()

    def insert(self, table: str, rows: list[dict[str, Any]]) -> None:
        if not rows:
            return
        self.client.table(table).insert(rows).execute()

    def delete_eq(self, table: str, filters: dict[str, Any]) -> None:
        query = self.client.table(table).delete()
        for column, value in filters.items():
            query = query.eq(column, value)
        query.execute()

    def upload_public_artifact(self, local_path: Path, storage_path: str) -> None:
        content_type = mimetypes.guess_type(local_path.name)[0] or "application/octet-stream"
        payload = local_path.read_bytes()
        bucket = self.client.storage.from_(PUBLIC_ARTIFACT_BUCKET)
        try:
            bucket.upload(
                path=storage_path,
                file=payload,
                file_options={"content-type": content_type, "upsert": "true"},
            )
        except Exception:
            bucket.update(
                path=storage_path,
                file=payload,
                file_options={"content-type": content_type},
            )


def configured_sink_from_env() -> WebSyncSink | None:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        return None
    return SupabaseWebSyncSink(url, key)


def optional_sync_round(
    round_path: Path,
    *,
    run_id: str | None = None,
    event_type: str = "sync_round",
    sink: WebSyncSink | None = None,
) -> SyncSummary:
    configured_sink = sink or configured_sink_from_env()
    if configured_sink is None:
        print(SUPABASE_SKIP_MESSAGE)
        return SyncSummary(event_type=event_type, status="skipped", message=SUPABASE_SKIP_MESSAGE)
    return sync_round(round_path, run_id=run_id, event_type=event_type, sink=configured_sink)


def optional_sync_latest(
    rounds_dir: Path,
    *,
    selection_path: Path | None = None,
    event_type: str = "publish_latest",
    sink: WebSyncSink | None = None,
    track: Track | None = None,
) -> SyncSummary:
    configured_sink = sink or configured_sink_from_env()
    if configured_sink is None:
        print(SUPABASE_SKIP_MESSAGE)
        return SyncSummary(event_type=event_type, status="skipped", message=SUPABASE_SKIP_MESSAGE)
    return sync_latest_leaderboard(
        rounds_dir,
        selection_path=selection_path,
        event_type=event_type,
        sink=configured_sink,
        track=track,
    )


def optional_sync_cumulative(
    rounds_dir: Path,
    *,
    selection_path: Path | None = None,
    event_type: str = "publish_cumulative",
    sink: WebSyncSink | None = None,
    track: Track | None = None,
) -> SyncSummary:
    configured_sink = sink or configured_sink_from_env()
    if configured_sink is None:
        print(SUPABASE_SKIP_MESSAGE)
        return SyncSummary(event_type=event_type, status="skipped", message=SUPABASE_SKIP_MESSAGE)
    return sync_cumulative_leaderboards(
        rounds_dir,
        selection_path=selection_path,
        event_type=event_type,
        sink=configured_sink,
        track=track,
    )


def sync_round(
    round_path: Path,
    *,
    run_id: str | None = None,
    event_type: str = "sync_round",
    sink: WebSyncSink,
) -> SyncSummary:
    manifest = load_manifest(round_path)
    selected_run_ids = [resolve_run_id(round_path, run_id)] if run_id else _public_run_ids(round_path)
    if run_id and not selected_run_ids:
        raise ValueError(f"run_id is not syncable public benchmark data: {run_id}")

    run_payloads: list[dict[str, Any]] = []
    model_rows: dict[str, dict[str, Any]] = {}
    submission_rows: list[dict[str, Any]] = []
    allocation_rows: list[dict[str, Any]] = []
    official_rows: list[dict[str, Any]] = []
    stability_rows: list[dict[str, Any]] = []
    option_return_rows: list[dict[str, Any]] = []
    weekly_price_rows: list[dict[str, Any]] = []
    weekly_performance_rows: list[dict[str, Any]] = []
    audit_rows: list[dict[str, Any]] = []
    uploaded_paths: list[Path] = []

    for selected_run_id in selected_run_ids:
        run_paths = get_run_paths(round_path, selected_run_id)
        run_manifest = read_run_manifest(run_paths)
        syncable = _validate_public_run(round_path, selected_run_id, run_manifest)
        if not syncable:
            continue
        run_payloads.append(_run_row(manifest.round_id, run_paths, run_manifest))
        for model_row in _model_rows(run_paths):
            model_rows[model_row["model_id"]] = model_row
        submission_rows.extend(_submission_rows(run_paths, published=True))
        allocation_rows.extend(_submission_allocation_rows(run_paths, published=True))
        if (run_paths.results_dir / "leaderboard.csv").exists():
            official_rows.extend(_official_result_rows(manifest.round_id, selected_run_id, run_paths))
            option_return_rows.extend(_option_return_rows(manifest.round_id, selected_run_id, run_paths))
        if (run_paths.results_dir / "stability.csv").exists():
            stability_rows.extend(_stability_result_rows(manifest.round_id, selected_run_id, run_paths))
        weekly_performance_rows.extend(_weekly_performance_rows(manifest.round_id, selected_run_id, run_paths))
        run_audit_rows, run_uploads = _run_audit_artifact_rows(manifest.round_id, run_paths)
        audit_rows.extend(run_audit_rows)
        uploaded_paths.extend(run_uploads)

    if run_id and not run_payloads:
        raise ValueError(f"run_id is not syncable public benchmark data: {run_id}")
    if not run_payloads and not _round_has_public_metadata(round_path):
        return _record_event(
            sink,
            SyncSummary(
                event_type=event_type,
                round_id=manifest.round_id,
                status="skipped",
                message="round has no public non-mock benchmark run",
            ),
        )

    round_row = _round_row(round_path, selected_run_ids)
    option_rows = _option_rows(round_path, published=True)
    weekly_price_rows.extend(_weekly_price_rows(manifest.round_id, round_path))
    research_rows, research_uploads = _research_artifact_rows(manifest.round_id, round_path)
    audit_rows.extend(_round_audit_artifact_rows(manifest.round_id, round_path))
    uploaded_paths.extend(research_uploads)

    if run_id is None:
        _clear_round_public_run_rows(sink, manifest.round_id)

    sink.upsert("rounds", [round_row], on_conflict="round_id")
    sink.upsert("options", option_rows, on_conflict="round_id,option_id")
    sink.upsert("models", list(model_rows.values()), on_conflict="model_id")
    sink.upsert("runs", run_payloads, on_conflict="round_id,run_id")
    sink.upsert("submissions", submission_rows, on_conflict="round_id,run_id,model_id,replicate_index")
    sink.upsert(
        "submission_allocations",
        allocation_rows,
        on_conflict="round_id,run_id,model_id,replicate_index,option_id",
    )
    sink.upsert("official_results", official_rows, on_conflict="round_id,run_id,model_id")
    sink.upsert("stability_results", stability_rows, on_conflict="round_id,run_id,model_id")
    sink.upsert("option_returns", option_return_rows, on_conflict="round_id,run_id,option_id")
    sink.upsert("round_weekly_prices", weekly_price_rows, on_conflict="round_id,target_date,option_id")
    sink.upsert(
        "round_weekly_performance",
        weekly_performance_rows,
        on_conflict="round_id,run_id,model_id,target_date",
    )
    sink.upsert("research_artifacts", research_rows, on_conflict="round_id,path")
    sink.upsert("audit_artifacts", audit_rows, on_conflict="round_id,run_id,path")

    for path in uploaded_paths:
        sink.upload_public_artifact(path, _artifact_storage_path(manifest.round_id, round_path, path))

    summary = SyncSummary(
        event_type=event_type,
        round_id=manifest.round_id,
        run_id=run_id,
        row_counts={
            "rounds": 1,
            "options": len(option_rows),
            "models": len(model_rows),
            "runs": len(run_payloads),
            "submissions": len(submission_rows),
            "submission_allocations": len(allocation_rows),
            "official_results": len(official_rows),
            "stability_results": len(stability_rows),
            "option_returns": len(option_return_rows),
            "round_weekly_prices": len(weekly_price_rows),
            "round_weekly_performance": len(weekly_performance_rows),
            "research_artifacts": len(research_rows),
            "audit_artifacts": len(audit_rows),
        },
    )
    return _record_event(sink, summary)


def sync_rounds_dir(
    rounds_dir: Path,
    *,
    include_cumulative: bool = False,
    selection_path: Path | None = None,
    event_type: str = "sync_rounds_dir",
    sink: WebSyncSink,
) -> list[SyncSummary]:
    summaries: list[SyncSummary] = []
    for round_path in sorted(path for path in rounds_dir.iterdir() if path.is_dir() and (path / "manifest.yaml").exists()):
        summaries.append(sync_round(round_path, event_type=event_type, sink=sink))
    if include_cumulative:
        for track in TRACKS:
            summaries.append(sync_latest_leaderboard(rounds_dir, selection_path=selection_path, sink=sink, track=track))
            summaries.append(sync_cumulative_leaderboards(rounds_dir, selection_path=selection_path, sink=sink, track=track))
    return summaries


def sync_latest_leaderboard(
    rounds_dir: Path,
    *,
    selection_path: Path | None = None,
    event_type: str = "sync_latest_leaderboard",
    sink: WebSyncSink,
    track: Track | None = None,
) -> SyncSummary:
    status = latest_status(rounds_dir, selection_path, track=track)
    slot = _latest_slot(track)
    if not status.selections:
        sink.delete_eq("latest_leaderboard", {"slot": slot})
        return _record_event(
            sink,
            SyncSummary(
                event_type=event_type,
                status="skipped",
                message="no resolved official rounds found",
                row_counts={"latest_leaderboard": 0},
            ),
        )
    selected = max(status.selections, key=latest_selection_sort_key)
    rows = [_latest_row(selected.round_id, selected.official_run_id or "", row, slot=slot) for row in selected.official_rows]
    sink.delete_eq("latest_leaderboard", {"slot": slot})
    sink.upsert("latest_leaderboard", rows, on_conflict="slot,model_id")
    return _record_event(
        sink,
        SyncSummary(
            event_type=event_type,
            round_id=selected.round_id,
            run_id=selected.official_run_id,
            row_counts={"latest_leaderboard": len(rows)},
        ),
    )


def sync_cumulative_leaderboards(
    rounds_dir: Path,
    *,
    selection_path: Path | None = None,
    event_type: str = "sync_cumulative_leaderboards",
    sink: WebSyncSink,
    track: Track | None = None,
) -> SyncSummary:
    status = cumulative_status(rounds_dir, selection_path, track=track)
    slot = _cumulative_slot(track)
    official_input_rows: list[dict[str, str]] = []
    stability_input_rows: list[dict[str, str]] = []
    for selected in status.selections:
        for row in selected.official_rows:
            official_input_rows.append({**row, "round_id": selected.round_id})
        for row in selected.stability_rows:
            stability_input_rows.append({**row, "round_id": selected.round_id})

    official_rows = [_published_row({**row, "slot": slot}) for row in build_cumulative_official(official_input_rows)]
    stability_rows = [_published_row({**row, "slot": slot}) for row in build_cumulative_stability(stability_input_rows)]
    sink.delete_eq("cumulative_official_leaderboard", {"slot": slot})
    sink.delete_eq("cumulative_stability_leaderboard", {"slot": slot})
    sink.upsert("cumulative_official_leaderboard", official_rows, on_conflict="slot,model_id")
    sink.upsert("cumulative_stability_leaderboard", stability_rows, on_conflict="slot,model_id")
    return _record_event(
        sink,
        SyncSummary(
            event_type=event_type,
            row_counts={
                "cumulative_official_leaderboard": len(official_rows),
                "cumulative_stability_leaderboard": len(stability_rows),
            },
        ),
    )


def _public_run_ids(round_path: Path) -> list[str]:
    official_runs: list[str] = []
    selected_official_runs: list[str] = []
    other_public_runs: list[str] = []
    for run_id in list_run_ids(round_path):
        manifest = read_run_manifest(get_run_paths(round_path, run_id))
        if _run_is_public_candidate(manifest):
            if str(manifest.get("run_type") or "") == "official":
                official_runs.append(run_id)
                if bool(manifest.get("operator_selected_official")):
                    selected_official_runs.append(run_id)
            else:
                other_public_runs.append(run_id)
    return (selected_official_runs or official_runs) + other_public_runs


def _clear_round_public_run_rows(sink: WebSyncSink, round_id: str) -> None:
    for table in [
        "submission_allocations",
        "submissions",
        "official_results",
        "stability_results",
        "option_returns",
        "round_weekly_prices",
        "round_weekly_performance",
        "audit_artifacts",
        "runs",
    ]:
        sink.delete_eq(table, {"round_id": round_id})


def _run_is_public_candidate(run_manifest: dict[str, Any]) -> bool:
    run_type = str(run_manifest.get("run_type") or "")
    if run_manifest.get("mock") is True or run_type in {"mock", "retrospective", "provider_smoke"}:
        return False
    if run_type == "official":
        return bool(run_manifest.get("official_score_eligible"))
    return run_type == "stability"


def _round_has_public_metadata(round_path: Path) -> bool:
    return any(_run_is_public_candidate(read_run_manifest(get_run_paths(round_path, run_id))) for run_id in list_run_ids(round_path))


def _validate_public_run(round_path: Path, run_id: str, run_manifest: dict[str, Any]) -> bool:
    run_paths = get_run_paths(round_path, run_id)
    run_type = str(run_manifest.get("run_type") or "")
    if not _run_is_public_candidate(run_manifest):
        return False
    if not round_hashes_match(round_path):
        raise ValueError(f"round hashes do not match current files: {round_path}")
    invalid_count = _invalid_submission_count(run_paths, run_manifest)
    if invalid_count != 0:
        raise ValueError(f"cannot sync public run with invalid parsed submissions: {run_id}")
    if run_type == "official":
        if not (run_paths.parsed_dir.exists() and list(iter_submission_files(run_paths.parsed_dir))):
            raise FileNotFoundError(f"official run has no parsed submissions: {run_id}")
        if (run_paths.results_dir / "leaderboard.csv").exists():
            _require_files(
                run_paths.results_dir,
                ["leaderboard.csv", "returns.csv"],
                f"official scored run {run_id}",
            )
    if run_type == "stability":
        _require_files(run_paths.results_dir, ["stability.csv"], f"stability run {run_id}")
    return True


def _invalid_submission_count(run_paths: Any, run_manifest: dict[str, Any]) -> int:
    if run_paths.validation_summary_path.exists():
        validation = read_json(run_paths.validation_summary_path)
        return int(validation.get("invalid_count") or 0)
    return int(run_manifest.get("invalid_submissions") or 0)


def _require_files(directory: Path, filenames: list[str], label: str) -> None:
    missing = [filename for filename in filenames if not (directory / filename).exists()]
    if missing:
        raise FileNotFoundError(f"missing required files for {label}: {', '.join(missing)}")


def _round_row(round_path: Path, selected_run_ids: list[str]) -> dict[str, Any]:
    manifest = load_manifest(round_path)
    run_manifests = [read_run_manifest(get_run_paths(round_path, run_id)) for run_id in selected_run_ids]
    methodology_version = next(
        (str(item.get("methodology_version")) for item in run_manifests if item.get("methodology_version")),
        str(manifest.methodology_version or ""),
    )
    has_scored_results = any(
        (get_run_paths(round_path, run_id).results_dir / "leaderboard.csv").exists()
        or (get_run_paths(round_path, run_id).results_dir / "stability.csv").exists()
        for run_id in selected_run_ids
    )
    return {
        "round_id": manifest.round_id,
        "title": manifest.title,
        "description": manifest.description,
        "decision_date": manifest.decision_date,
        "decision_deadline_utc": manifest.decision_deadline,
        "horizon": manifest.horizon,
        "horizon_days": _horizon_days(manifest.entry_date, manifest.exit_date),
        "entry_rule": manifest.entry_rule,
        "exit_rule": manifest.exit_rule,
        "entry_date": manifest.entry_date,
        "exit_date": manifest.exit_date,
        "status": "resolved" if has_scored_results else "pending",
        "methodology_version": methodology_version,
        "universe_version": _round_universe_version(round_path, manifest.universe_version),
        "submission_format": manifest.submission_format,
        "portfolio_constraints": _jsonable(manifest.portfolio_constraints.model_dump(mode="json")),
        "published": True,
        "notes": manifest.notes,
        "created_at_utc": manifest.created_at,
    }


def _run_row(round_id: str, run_paths: Any, run_manifest: dict[str, Any]) -> dict[str, Any]:
    report_path = run_paths.results_dir / "report.md"
    return {
        "round_id": round_id,
        "run_id": run_paths.run_id,
        "run_type": str(run_manifest.get("run_type") or ""),
        "mode": str(run_manifest.get("mode") or ""),
        "mock": bool(run_manifest.get("mock")),
        "official_score_eligible": bool(run_manifest.get("official_score_eligible")),
        "operator_selected_official": bool(run_manifest.get("operator_selected_official")),
        "methodology_version": str(run_manifest.get("methodology_version") or ""),
        "replicates": int(run_manifest.get("replicates") or 1),
        "model_count": _int_or_none(run_manifest.get("model_count")),
        "valid_submissions": _int_or_none(run_manifest.get("valid_submissions")),
        "invalid_submissions": _int_or_none(run_manifest.get("invalid_submissions")),
        "created_at_utc": run_manifest.get("created_at_utc"),
        "completed_at_utc": run_manifest.get("completed_at_utc"),
        "report_path": _relative_to_round(run_paths.round_path, report_path) if report_path.exists() else None,
        "report_sha256": sha256_file(report_path) if report_path.exists() else None,
        "published": True,
        "metadata": _jsonable(
            {
                key: value
                for key, value in run_manifest.items()
                if key
                not in {
                    "run_id",
                    "round_id",
                    "run_type",
                    "mode",
                    "mock",
                    "official_score_eligible",
                    "operator_selected_official",
                    "methodology_version",
                    "replicates",
                    "model_count",
                    "valid_submissions",
                    "invalid_submissions",
                    "created_at_utc",
                    "completed_at_utc",
                }
            }
        ),
    }


def _option_rows(round_path: Path, *, published: bool) -> list[dict[str, Any]]:
    manifest = load_manifest(round_path)
    entry_prices = _read_csv_by_key(round_path / "prices" / "entry_prices.csv", "option_id")
    rows: list[dict[str, Any]] = []
    for sort_order, option in enumerate(load_options(round_path), start=1):
        price_row = _price_row_for_option(entry_prices, option)
        rows.append(
            {
                "round_id": manifest.round_id,
                "option_id": option.option_id,
                "sort_order": sort_order,
                "name": option.name,
                "symbol": option.symbol,
                "tiingo_symbol": option.tiingo_symbol,
                "asset_class": option.asset_class,
                "category": option.category,
                "option_group": option.option_group,
                "risk_bucket": option.risk_bucket,
                "exposure_description": option.exposure_description,
                "currency": option.currency,
                "is_cash": option.is_cash,
                "is_benchmark": option.is_benchmark or option.option_id.upper() == "SP500",
                "include_in_universe": option.include_in_universe,
                "entry_price": _price_value(price_row),
                "entry_price_source": _price_source(price_row),
                "entry_price_date": price_row.get("date") if price_row else None,
                "published": published,
            }
        )
    return rows


def _round_universe_version(round_path: Path, manifest_version: str | None) -> str | None:
    if manifest_version:
        return manifest_version
    options_path = round_path / "options.yaml"
    if not options_path.exists():
        return None
    options_text = options_path.read_text(encoding="utf-8").strip()
    configs_dir = Path(__file__).resolve().parents[2] / "configs" / "universes"
    if not configs_dir.exists():
        return None
    for config_path in sorted(configs_dir.glob("capitalbench_universe_*.yaml"), reverse=True):
        if config_path.read_text(encoding="utf-8").strip() == options_text:
            return config_path.stem
    return None


def _model_rows(run_paths: Any) -> list[dict[str, Any]]:
    configs = _model_configs_by_id(run_paths)
    rows: dict[str, dict[str, Any]] = {}
    for submission_path in iter_submission_files(run_paths.parsed_dir):
        payload = read_json(submission_path)
        model_id = str(payload["model_id"])
        provider = str(payload["provider"])
        config = configs.get(model_id, {})
        rows[model_id] = {
            "model_id": model_id,
            "provider": provider,
            "display_name": str(config.get("display_name") or _display_model_name(model_id)),
            "api_model_name": config.get("api_model_name"),
            "first_eligible_round": config.get("first_eligible_round"),
            "first_eligible_date_utc": config.get("first_eligible_date_utc"),
            "model_release_date": config.get("model_release_date"),
            "official_score_eligible": None,
            "metadata": _jsonable(config.get("metadata") or {}),
            "published": True,
        }
    return list(rows.values())


def _model_configs_by_id(run_paths: Any) -> dict[str, dict[str, Any]]:
    run_manifest = read_run_manifest(run_paths)
    models_path_raw = run_manifest.get("models_path") or run_manifest.get("models_config_file")
    if not models_path_raw:
        return {}
    models_path = Path(str(models_path_raw))
    if not models_path.is_absolute():
        candidate = run_paths.round_path.parent.parent / models_path
        models_path = candidate if candidate.exists() else models_path
    if not models_path.exists():
        return {}
    data = read_yaml(models_path)
    raw_models = data.get("models") if isinstance(data, dict) else None
    if not isinstance(raw_models, list):
        return {}
    return {
        str(item.get("model_id")): item
        for item in raw_models
        if isinstance(item, dict) and item.get("model_id")
    }


def _submission_rows(run_paths: Any, *, published: bool) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    options_by_id = {option.option_id: option for option in load_options(run_paths.round_path)}
    for submission_path in iter_submission_files(run_paths.parsed_dir):
        payload = read_json(submission_path)
        submission = ModelSubmission.model_validate(payload)
        replicate_index = int(payload.get("replicate_index") or 1)
        usage = payload.get("usage")
        cost_usd = payload.get("cost_usd")
        if cost_usd is None and isinstance(usage, dict):
            cost_usd = usage.get("cost_usd")
        metrics = portfolio_metrics(submission, options_by_id)
        rows.append(
            {
                "round_id": payload["round_id"],
                "run_id": run_paths.run_id,
                "model_id": payload["model_id"],
                "provider": payload["provider"],
                "mode": payload["mode"],
                "run_type": payload.get("run_type") or read_run_manifest(run_paths).get("run_type"),
                "replicate_index": replicate_index,
                "replicate_count": int(payload.get("replicate_count") or 1),
                "is_official_score": bool(payload.get("is_official_score")),
                "submission_format": "portfolio" if payload.get("portfolio") else "single_pick",
                "selected_option_id": primary_option_id(submission),
                "holding_count": metrics.holding_count,
                "max_allocation_bps": metrics.max_allocation_bps,
                "cash_allocation_bps": metrics.cash_allocation_bps,
                "benchmark_allocation_bps": metrics.benchmark_allocation_bps,
                "concentration_hhi": _decimal(metrics.concentration_hhi),
                "portfolio": _jsonable(_submission_portfolio_payload(submission)),
                "portfolio_rationale": payload.get("portfolio_rationale") or None,
                "confidence": _decimal(payload.get("confidence")),
                "rationale_summary": payload["rationale_summary"],
                "key_risks": payload.get("key_risks") or [],
                "usage": _jsonable(usage) if usage is not None else None,
                "cost_usd": _decimal(cost_usd),
                "metadata": _jsonable(payload.get("metadata") or {}),
                "submission_sha256": sha256_file(submission_path),
                "published": published,
            }
        )
    return rows


def _submission_portfolio_payload(submission: ModelSubmission) -> list[dict[str, Any]]:
    return [
        {
            "option_id": allocation.option_id,
            "allocation_bps": allocation.allocation_bps,
            "allocation_pct": allocation.allocation_bps / 100,
            "rationale": allocation.rationale,
        }
        for allocation in allocation_views(submission)
    ]


def _submission_allocation_rows(run_paths: Any, *, published: bool) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for submission_path in iter_submission_files(run_paths.parsed_dir):
        payload = read_json(submission_path)
        submission = ModelSubmission.model_validate(payload)
        replicate_index = int(payload.get("replicate_index") or 1)
        for allocation in allocation_views(submission):
            rows.append(
                {
                    "round_id": payload["round_id"],
                    "run_id": run_paths.run_id,
                    "model_id": payload["model_id"],
                    "replicate_index": replicate_index,
                    "option_id": allocation.option_id,
                    "allocation_bps": allocation.allocation_bps,
                    "allocation_rank": allocation.allocation_rank,
                    "rationale_summary": allocation.rationale,
                    "published": published,
                }
            )
    return rows


def _official_result_rows(round_id: str, run_id: str, run_paths: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    submissions_by_model = _parsed_submission_payloads_by_model(run_paths)
    for row in _read_csv(run_paths.results_dir / "leaderboard.csv"):
        submission_payload = submissions_by_model.get(row["model_id"], {})
        rows.append(
            {
                "round_id": round_id,
                "run_id": run_id,
                "model_id": row["model_id"],
                "provider": row["provider"],
                "mode": row["mode"],
                "submission_format": row.get("submission_format") or "single_pick",
                "selected_option_id": row["selected_option_id"],
                "confidence": _decimal(row.get("confidence")),
                "selected_asset_return": _decimal(row.get("selected_asset_return")),
                "portfolio_return": _decimal(row.get("portfolio_return")),
                "sp500_return": _decimal(row.get("sp500_return")),
                "alpha_vs_sp500": _decimal(row.get("alpha_vs_sp500")),
                "regret_vs_best_option": _decimal(row.get("regret_vs_best_option")),
                "rank_among_options": _int_or_none(row.get("rank_among_options")),
                "holding_count": _int_or_none(row.get("holding_count")) or 1,
                "max_allocation_bps": _int_or_none(row.get("max_allocation_bps")) or 10000,
                "cash_allocation_bps": _int_or_none(row.get("cash_allocation_bps")) or 0,
                "benchmark_allocation_bps": _int_or_none(row.get("benchmark_allocation_bps")) or 0,
                "concentration_hhi": _decimal(row.get("concentration_hhi")),
                "beats_sp500": _bool(row.get("beats_sp500")),
                "beats_cash": _bool(row.get("beats_cash")),
                "cost_usd": _decimal(row.get("cost_usd")),
                "alpha_per_dollar": _decimal(row.get("alpha_per_dollar")),
                "rationale_summary": submission_payload.get("rationale_summary") or row.get("rationale_summary") or "",
                "key_risks": submission_payload.get("key_risks") or _key_risks(row.get("key_risks")),
                "published": True,
            }
        )
    return rows


def _parsed_submission_payloads_by_model(run_paths: Any) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for submission_path in iter_submission_files(run_paths.parsed_dir):
        payload = read_json(submission_path)
        if payload.get("model_id"):
            rows[str(payload["model_id"])] = payload
    return rows


def _stability_result_rows(round_id: str, run_id: str, run_paths: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in _read_csv(run_paths.results_dir / "stability.csv"):
        rows.append(
            {
                "round_id": round_id,
                "run_id": run_id,
                "model_id": row["model_id"],
                "provider": row["provider"],
                "replicate_count": _int_or_none(row.get("replicate_count")) or 1,
                "valid_replicates": _int_or_none(row.get("valid_replicates")) or 0,
                "invalid_replicates": _int_or_none(row.get("invalid_replicates")) or 0,
                "selected_option_ids": _json_value(row.get("selected_option_ids"), []),
                "pick_distribution": _json_value(row.get("pick_distribution"), {}),
                "modal_pick": row.get("modal_pick") or None,
                "modal_pick_count": _int_or_none(row.get("modal_pick_count")),
                "consistency_rate": _decimal(row.get("consistency_rate")),
                "average_repeated_return": _decimal(row.get("average_repeated_return")),
                "average_repeated_alpha_vs_sp500": _decimal(row.get("average_repeated_alpha_vs_sp500")),
                "best_replicate_return": _decimal(row.get("best_replicate_return")),
                "worst_replicate_return": _decimal(row.get("worst_replicate_return")),
                "best_replicate_option_id": row.get("best_replicate_option_id") or None,
                "worst_replicate_option_id": row.get("worst_replicate_option_id") or None,
                "modal_pick_return": _decimal(row.get("modal_pick_return")),
                "modal_pick_alpha_vs_sp500": _decimal(row.get("modal_pick_alpha_vs_sp500")),
                "total_cost_usd": _decimal(row.get("total_cost_usd")),
                "average_cost_usd": _decimal(row.get("average_cost_usd")),
                "notes": row.get("notes") or "",
                "published": True,
            }
        )
    return rows


def _option_return_rows(round_id: str, run_id: str, run_paths: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in _read_csv(run_paths.results_dir / "returns.csv"):
        if "option_id" not in row:
            continue
        rows.append(
            {
                "round_id": round_id,
                "run_id": run_id,
                "option_id": row["option_id"],
                "label": row.get("label") or "",
                "asset_symbol": row.get("asset_symbol") or "",
                "entry_price": _decimal(row.get("entry_price")),
                "exit_price": _decimal(row.get("exit_price")),
                "entry_price_source": row.get("entry_price_source") or None,
                "exit_price_source": row.get("exit_price_source") or None,
                "realized_return": _decimal(row.get("return")),
                "rank": _int_or_none(row.get("rank")),
                "is_benchmark": _bool(row.get("is_benchmark")),
                "is_cash": _bool(row.get("is_cash")),
                "published": True,
            }
        )
    return rows


def _weekly_price_rows(round_id: str, round_path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in _read_csv(round_path / "prices" / "weekly_prices.csv"):
        rows.append(
            {
                "round_id": round_id,
                "target_date": row["target_date"],
                "price_date": row.get("price_date") or row["target_date"],
                "option_id": row["option_id"],
                "symbol": row.get("symbol") or None,
                "price": _decimal(row.get("price")),
                "price_source": row.get("price_source") or None,
                "published": _bool(row.get("published") or True),
            }
        )
    return rows


def _weekly_performance_rows(round_id: str, run_id: str, run_paths: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in _read_csv(run_paths.results_dir / "weekly_performance.csv"):
        rows.append(
            {
                "round_id": round_id,
                "run_id": run_id,
                "model_id": row["model_id"],
                "provider": row["provider"],
                "target_date": row["target_date"],
                "price_date": row.get("price_date") or row["target_date"],
                "days_elapsed": _int_or_none(row.get("days_elapsed")) or 0,
                "run_type": row.get("run_type") or "official",
                "submission_format": row.get("submission_format") or "single_pick",
                "selected_option_id": row["selected_option_id"],
                "holding_count": _int_or_none(row.get("holding_count")) or 1,
                "model_return": _decimal(row.get("model_return")),
                "sp500_return": _decimal(row.get("sp500_return")),
                "alpha_vs_sp500": _decimal(row.get("alpha_vs_sp500")),
                "price_status": row.get("price_status") or "complete",
                "published": _bool(row.get("published") or True),
            }
        )
    return rows


def _research_artifact_rows(round_id: str, round_path: Path) -> tuple[list[dict[str, Any]], list[Path]]:
    paths: list[Path] = []
    if (round_path / "briefing.md").exists():
        paths.append(round_path / "briefing.md")
    research_dir = round_path / "research"
    if research_dir.exists():
        paths.extend(sorted(path for path in research_dir.iterdir() if path.is_file()))
    rows = [
        _artifact_row(
            round_id=round_id,
            run_id=None,
            round_path=round_path,
            path=path,
            artifact_type=_artifact_type(path),
            model_facing=path.name in {"briefing.md", "final_briefing.md"},
        )
        for path in paths
    ]
    return rows, paths


def _round_audit_artifact_rows(round_id: str, round_path: Path) -> list[dict[str, Any]]:
    paths = [round_path / "hashes.json"]
    paths.extend(sorted(path for path in (round_path / "prices").glob("*.csv") if path.exists()))
    return [
        _artifact_row(
            round_id=round_id,
            run_id="",
            round_path=round_path,
            path=path,
            artifact_type=_artifact_type(path),
            model_facing=False,
        )
        for path in paths
        if path.exists()
    ]


def _run_audit_artifact_rows(round_id: str, run_paths: Any) -> tuple[list[dict[str, Any]], list[Path]]:
    paths = [run_paths.run_manifest_path, run_paths.validation_summary_path, run_paths.run_log_path]
    if run_paths.results_dir.exists():
        paths.extend(sorted(path for path in run_paths.results_dir.iterdir() if path.is_file()))
    existing_paths = [path for path in paths if path.exists()]
    rows = [
        _artifact_row(
            round_id=round_id,
            run_id=run_paths.run_id,
            round_path=run_paths.round_path,
            path=path,
            artifact_type=_artifact_type(path),
            model_facing=False,
        )
        for path in existing_paths
    ]
    return rows, existing_paths


def _artifact_row(
    *,
    round_id: str,
    run_id: str | None,
    round_path: Path,
    path: Path,
    artifact_type: str,
    model_facing: bool,
) -> dict[str, Any]:
    storage_path = _artifact_storage_path(round_id, round_path, path)
    row = {
        "round_id": round_id,
        "path": _relative_to_round(round_path, path),
        "artifact_type": artifact_type,
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
        "storage_bucket": PUBLIC_ARTIFACT_BUCKET,
        "storage_path": storage_path,
        "published": True,
    }
    if run_id is None:
        row["model_facing"] = model_facing
    else:
        row["run_id"] = run_id
        row["validation_summary"] = read_json(path) if path.name == "validation_summary.json" else None
        row["warnings"] = []
    return row


def _latest_row(round_id: str, run_id: str, row: dict[str, str], *, slot: str = "latest") -> dict[str, Any]:
    return {
        "slot": slot,
        "round_id": round_id,
        "run_id": run_id,
        "model_id": row["model_id"],
        "provider": row["provider"],
        "submission_format": row.get("submission_format") or "single_pick",
        "selected_option_id": row["selected_option_id"],
        "confidence": _decimal(row.get("confidence")),
        "selected_asset_return": _decimal(row.get("selected_asset_return")),
        "portfolio_return": _decimal(row.get("portfolio_return")),
        "sp500_return": _decimal(row.get("sp500_return")),
        "alpha_vs_sp500": _decimal(row.get("alpha_vs_sp500")),
        "regret_vs_best_option": _decimal(row.get("regret_vs_best_option")),
        "rank_among_options": _int_or_none(row.get("rank_among_options")),
        "holding_count": _int_or_none(row.get("holding_count")) or 1,
        "max_allocation_bps": _int_or_none(row.get("max_allocation_bps")) or 10000,
        "cash_allocation_bps": _int_or_none(row.get("cash_allocation_bps")) or 0,
        "benchmark_allocation_bps": _int_or_none(row.get("benchmark_allocation_bps")) or 0,
        "concentration_hhi": _decimal(row.get("concentration_hhi")),
        "beats_sp500": _bool(row.get("beats_sp500")),
        "beats_cash": _bool(row.get("beats_cash")),
        "published": True,
    }


def _latest_slot(track: Track | None) -> str:
    return f"latest_{track}" if track else "latest"


def _cumulative_slot(track: Track | None) -> str:
    return f"cumulative_{track}" if track else "cumulative_all"


def _record_event(sink: WebSyncSink, summary: SyncSummary) -> SyncSummary:
    sink.insert(
        "sync_events",
        [
            {
                "event_type": summary.event_type,
                "round_id": summary.round_id,
                "run_id": summary.run_id,
                "status": summary.status,
                "message": summary.message,
                "row_counts": summary.row_counts,
            }
        ],
    )
    return summary


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_csv_by_key(path: Path, key: str) -> dict[str, dict[str, str]]:
    rows = _read_csv(path)
    return {row[key]: row for row in rows if row.get(key)}


def _price_row_for_option(rows: dict[str, dict[str, str]], option: Any) -> dict[str, str] | None:
    for key in [option.option_id, option.symbol, option.tiingo_symbol, option.asset_symbol]:
        if key and key in rows:
            return rows[key]
    return None


def _price_value(row: dict[str, str] | None) -> float | None:
    if row is None:
        return None
    for key in ["price", "adj_close", "adjClose", "close"]:
        value = row.get(key)
        if value not in {None, ""}:
            return _decimal(value)
    return None


def _price_source(row: dict[str, str] | None) -> str | None:
    if row is None:
        return None
    if row.get("price_source"):
        return row["price_source"]
    if row.get("price") not in {None, ""}:
        return "price"
    if row.get("adj_close") not in {None, ""} or row.get("adjClose") not in {None, ""}:
        return "adj_close"
    if row.get("close") not in {None, ""}:
        return "close"
    return None


def _artifact_storage_path(round_id: str, round_path: Path, path: Path) -> str:
    return f"{round_id}/{_relative_to_round(round_path, path)}"


def _relative_to_round(round_path: Path, path: Path) -> str:
    return path.relative_to(round_path).as_posix()


def _artifact_type(path: Path) -> str:
    name = path.name
    if name in {"briefing.md", "final_briefing.md"}:
        return "briefing"
    if name == "hashes.json" or name.endswith("_hashes.json"):
        return "hash_manifest"
    if name == "validation_summary.json":
        return "validation_summary"
    if name == "report.md":
        return "report"
    if name.endswith(".csv"):
        return "csv"
    if name.endswith(".yaml") or name.endswith(".yml"):
        return "yaml"
    return "artifact"


def _display_model_name(model_id: str) -> str:
    if model_id in MODEL_DISPLAY_NAMES:
        return MODEL_DISPLAY_NAMES[model_id]
    replacements = {"gpt": "GPT", "xai": "xAI", "openai": "OpenAI"}
    words = []
    for word in model_id.replace("_", "-").split("-"):
        words.append(replacements.get(word.lower(), word.upper() if len(word) <= 3 else word.capitalize()))
    return " ".join(words)


def _published_row(row: dict[str, Any]) -> dict[str, Any]:
    return {**row, "published": True}


def _jsonable(value: Any) -> Any:
    return json.loads(json.dumps(value, default=str))


def _json_value(raw: str | None, default: Any) -> Any:
    if raw is None or raw == "":
        return default
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return default


def _key_risks(raw: str | None) -> list[str]:
    if not raw:
        return []
    parsed = _json_value(raw, None)
    if isinstance(parsed, list):
        return [str(item) for item in parsed]
    return [item.strip() for item in raw.split(";") if item.strip()]


def _decimal(value: Any) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


def _int_or_none(value: Any) -> int | None:
    if value is None or value == "":
        return None
    return int(float(value))


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def _horizon_days(entry_date: str | None, exit_date: str | None) -> int | None:
    if not entry_date or not exit_date:
        return None
    try:
        return (date.fromisoformat(exit_date) - date.fromisoformat(entry_date)).days
    except ValueError:
        return None

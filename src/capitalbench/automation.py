from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Protocol

from .cumulative import publish_cumulative, publish_latest, track_for_horizon_days
from .hashing import round_hashes_match
from .io import load_manifest, read_json, read_yaml, write_yaml
from .prices import fetch_selected_prices
from .report import publish_report
from .run_store import get_run_paths, read_run_manifest, update_run_manifest
from .scoring import score_round
from .web_sync import (
    SUPABASE_SKIP_MESSAGE,
    optional_sync_cumulative,
    optional_sync_latest,
    optional_sync_round,
)


AUTOMATION_DIRNAME = "automation"
RESOLUTION_JOB_FILENAME = "resolution_job.yaml"
AUTOMATION_JOB_TYPE = "resolve_round"
DEFAULT_RESOLUTION_TIME_UTC = time(hour=23, minute=30, tzinfo=timezone.utc)


@dataclass(frozen=True)
class AutomationSummary:
    status: str
    round_id: str
    run_id: str
    job_id: str | None = None
    message: str = ""
    due_at_utc: str | None = None
    outputs: dict[str, str] = field(default_factory=dict)


class AutomationStore(Protocol):
    def upsert_job(self, row: dict[str, Any]) -> None: ...

    def claim_due_job(self, *, due_before_utc: str, worker_id: str) -> dict[str, Any] | None: ...

    def update_job(self, job_id: str, updates: dict[str, Any]) -> None: ...


class SupabaseAutomationStore:
    def __init__(self, url: str, service_role_key: str) -> None:
        try:
            from supabase import create_client
        except ImportError as exc:  # pragma: no cover - exercised only without optional dependency.
            raise RuntimeError(
                "Automation requires the optional supabase client. "
                "Install with `pip install 'capitalbench[web-sync]'` or `pip install supabase>=2,<3`."
            ) from exc
        self.client = create_client(url, service_role_key)

    def upsert_job(self, row: dict[str, Any]) -> None:
        self.client.table("automation_jobs").upsert(row, on_conflict="round_id,run_id,job_type").execute()

    def claim_due_job(self, *, due_before_utc: str, worker_id: str) -> dict[str, Any] | None:
        response = self.client.rpc(
            "claim_due_automation_job",
            {
                "due_before": due_before_utc,
                "worker": worker_id,
            },
        ).execute()
        data = response.data
        if isinstance(data, list):
            return data[0] if data else None
        return data if isinstance(data, dict) and data else None

    def update_job(self, job_id: str, updates: dict[str, Any]) -> None:
        self.client.table("automation_jobs").update(updates).eq("job_id", job_id).execute()


def configured_automation_store_from_env() -> AutomationStore | None:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        return None
    return SupabaseAutomationStore(url, key)


def accept_run(
    round_path: Path,
    *,
    run_id: str,
    schedule_resolution: bool = True,
    due_at_utc: str | None = None,
    store: AutomationStore | None = None,
    sync_pending: bool = True,
) -> AutomationSummary:
    manifest = load_manifest(round_path)
    run_paths = get_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    _validate_acceptance_gate(round_path, run_manifest)

    accepted_at_utc = _utc_now()
    due_at = due_at_utc or _default_due_at_utc(manifest.exit_date)
    updates: dict[str, Any] = {
        "operator_selected_official": True,
        "accepted_at_utc": accepted_at_utc,
    }
    if schedule_resolution:
        updates["resolution_due_at_utc"] = due_at
    update_run_manifest(run_paths, updates)

    job_id: str | None = None
    if schedule_resolution:
        row = _automation_job_row(
            round_id=manifest.round_id,
            run_id=run_id,
            due_at_utc=due_at,
            status="scheduled",
            metadata={
                "round_path": str(round_path),
                "accepted_at_utc": accepted_at_utc,
            },
        )
        job_id = str(row["job_id"])
        write_yaml(_local_job_path(round_path), _local_job_file(row))
        selected_store = store if store is not None else configured_automation_store_from_env()
        if selected_store is None:
            print(SUPABASE_SKIP_MESSAGE)
        else:
            selected_store.upsert_job(row)

    if sync_pending:
        optional_sync_round(round_path, run_id=run_id, event_type="accept_run")

    return AutomationSummary(
        status="scheduled" if schedule_resolution else "accepted",
        round_id=manifest.round_id,
        run_id=run_id,
        job_id=job_id,
        due_at_utc=due_at if schedule_resolution else None,
        message="accepted official run" + (" and scheduled resolution" if schedule_resolution else ""),
    )


def automation_status(rounds_dir: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(rounds_dir.glob(f"*/{AUTOMATION_DIRNAME}/{RESOLUTION_JOB_FILENAME}")):
        rows.append(read_yaml(path))
    return rows


def retry_local_job(round_path: Path, *, next_attempt_at_utc: str | None = None) -> AutomationSummary:
    job_path = _local_job_path(round_path)
    if not job_path.exists():
        raise FileNotFoundError(f"no local automation job found: {job_path}")
    job = read_yaml(job_path)
    job["status"] = "scheduled"
    job["next_attempt_at_utc"] = next_attempt_at_utc
    job["last_error"] = ""
    write_yaml(job_path, job)
    return AutomationSummary(
        status="scheduled",
        round_id=str(job["round_id"]),
        run_id=str(job["run_id"]),
        job_id=str(job.get("job_id") or ""),
        due_at_utc=str(job.get("due_at_utc") or ""),
        message="local automation job marked for retry",
    )


def cancel_local_job(round_path: Path) -> AutomationSummary:
    job_path = _local_job_path(round_path)
    if not job_path.exists():
        raise FileNotFoundError(f"no local automation job found: {job_path}")
    job = read_yaml(job_path)
    job["status"] = "cancelled"
    job["cancelled_at_utc"] = _utc_now()
    write_yaml(job_path, job)
    return AutomationSummary(
        status="cancelled",
        round_id=str(job["round_id"]),
        run_id=str(job["run_id"]),
        job_id=str(job.get("job_id") or ""),
        message="local automation job cancelled",
    )


def automation_run(
    rounds_dir: Path,
    *,
    due_before_utc: str | None = None,
    max_jobs: int = 3,
    latest_output: Path = Path("latest"),
    cumulative_output: Path = Path("cumulative"),
    selection_path: Path | None = None,
    worker_id: str | None = None,
) -> list[AutomationSummary]:
    selected_store = configured_automation_store_from_env()
    due_before = due_before_utc or _utc_now()
    if selected_store is not None:
        return _automation_run_supabase(
            rounds_dir,
            store=selected_store,
            due_before_utc=due_before,
            max_jobs=max_jobs,
            latest_output=latest_output,
            cumulative_output=cumulative_output,
            selection_path=selection_path,
            worker_id=worker_id or f"local-{os.getpid()}",
        )
    return _automation_run_local(
        rounds_dir,
        due_before_utc=due_before,
        max_jobs=max_jobs,
        latest_output=latest_output,
        cumulative_output=cumulative_output,
        selection_path=selection_path,
    )


def resolve_accepted_round(
    rounds_dir: Path,
    *,
    round_id: str,
    run_id: str,
    latest_output: Path = Path("latest"),
    cumulative_output: Path = Path("cumulative"),
    selection_path: Path | None = None,
    fetch_exit_prices: bool = True,
    overwrite_prices: bool = False,
    full_universe_prices: bool = True,
    sync: bool = True,
) -> AutomationSummary:
    round_path = _round_path_for_id(rounds_dir, round_id)
    manifest = load_manifest(round_path)
    if manifest.round_id != round_id:
        raise ValueError(f"round_id mismatch: expected {round_id}, manifest has {manifest.round_id}")
    if not manifest.exit_date:
        raise ValueError(f"round {round_id} has no exit_date")

    today = datetime.now(timezone.utc).date()
    exit_date = datetime.fromisoformat(manifest.exit_date).date()
    if today < exit_date:
        raise ValueError(f"round {round_id} is not due yet: exit_date is {manifest.exit_date}")

    run_paths = get_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    _validate_resolution_gate(round_path, run_manifest)

    if fetch_exit_prices:
        fetch_selected_prices(
            round_path=round_path,
            run_id=run_id,
            entry_date=None,
            exit_date=manifest.exit_date,
            overwrite_prices=overwrite_prices,
            full_universe=full_universe_prices,
            price_side="exit",
        )
    elif not (round_path / "prices" / "exit_prices.csv").exists():
        raise FileNotFoundError("missing exit prices and fetch_exit_prices is false")

    scores = score_round(round_path, run_id=run_id)
    report_path = publish_report(round_path, run_id=run_id)
    track = track_for_horizon_days(_horizon_days(manifest.entry_date, manifest.exit_date))
    latest = publish_latest(rounds_dir, latest_output, selection_path=selection_path, track=track)
    cumulative = publish_cumulative(rounds_dir, cumulative_output, selection_path=selection_path, track=track)

    if sync:
        optional_sync_round(round_path, run_id=run_id, event_type="automation_resolve")
        optional_sync_latest(rounds_dir, selection_path=selection_path, event_type="automation_publish_latest", track=track)
        optional_sync_cumulative(
            rounds_dir,
            selection_path=selection_path,
            event_type="automation_publish_cumulative",
            track=track,
        )

    completed_at_utc = _utc_now()
    update_run_manifest(run_paths, {"resolved_at_utc": completed_at_utc})
    _mark_local_job(round_path, status="succeeded", completed_at_utc=completed_at_utc, last_error="")

    return AutomationSummary(
        status="succeeded",
        round_id=round_id,
        run_id=run_id,
        message=f"resolved {len(scores)} official scores",
        outputs={
            "report": str(report_path),
            "latest_leaderboard": str(latest.latest_leaderboard_path),
            "latest_report": str(latest.latest_report_path),
            "cumulative_official": str(cumulative.official_leaderboard_path),
            "cumulative_stability": str(cumulative.stability_leaderboard_path),
            "cumulative_report": str(cumulative.cumulative_report_path),
        },
    )


def _automation_run_supabase(
    rounds_dir: Path,
    *,
    store: AutomationStore,
    due_before_utc: str,
    max_jobs: int,
    latest_output: Path,
    cumulative_output: Path,
    selection_path: Path | None,
    worker_id: str,
) -> list[AutomationSummary]:
    summaries: list[AutomationSummary] = []
    for _ in range(max_jobs):
        job = store.claim_due_job(due_before_utc=due_before_utc, worker_id=worker_id)
        if job is None:
            break
        job_id = str(job["job_id"])
        try:
            summary = resolve_accepted_round(
                rounds_dir,
                round_id=str(job["round_id"]),
                run_id=str(job["run_id"]),
                latest_output=latest_output,
                cumulative_output=cumulative_output,
                selection_path=selection_path,
                overwrite_prices=True,
            )
        except Exception as exc:
            next_attempt = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()
            store.update_job(
                job_id,
                {
                    "status": "failed",
                    "last_error": str(exc),
                    "next_attempt_at_utc": next_attempt,
                    "locked_at_utc": None,
                    "locked_by": None,
                },
            )
            summaries.append(
                AutomationSummary(
                    status="failed",
                    round_id=str(job["round_id"]),
                    run_id=str(job["run_id"]),
                    job_id=job_id,
                    message=str(exc),
                )
            )
            continue
        store.update_job(
            job_id,
            {
                "status": "succeeded",
                "last_error": "",
                "completed_at_utc": _utc_now(),
                "locked_at_utc": None,
                "locked_by": None,
                "metadata": {"outputs": summary.outputs},
            },
        )
        summaries.append(summary)
    return summaries


def _automation_run_local(
    rounds_dir: Path,
    *,
    due_before_utc: str,
    max_jobs: int,
    latest_output: Path,
    cumulative_output: Path,
    selection_path: Path | None,
) -> list[AutomationSummary]:
    due_before = _parse_utc(due_before_utc)
    jobs: list[dict[str, Any]] = []
    for path in sorted(rounds_dir.glob(f"*/{AUTOMATION_DIRNAME}/{RESOLUTION_JOB_FILENAME}")):
        job = read_yaml(path)
        job["_path"] = path
        if _job_is_due(job, due_before):
            jobs.append(job)
    summaries: list[AutomationSummary] = []
    for job in jobs[:max_jobs]:
        path = Path(job["_path"])
        round_path = path.parents[1]
        try:
            _mark_local_job(round_path, status="running", locked_at_utc=_utc_now(), last_error="")
            summaries.append(
                resolve_accepted_round(
                    rounds_dir,
                    round_id=str(job["round_id"]),
                    run_id=str(job["run_id"]),
                    latest_output=latest_output,
                    cumulative_output=cumulative_output,
                    selection_path=selection_path,
                    overwrite_prices=True,
                )
            )
        except Exception as exc:
            next_attempt = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()
            _mark_local_job(
                round_path,
                status="failed",
                last_error=str(exc),
                next_attempt_at_utc=next_attempt,
                locked_at_utc=None,
            )
            summaries.append(
                AutomationSummary(
                    status="failed",
                    round_id=str(job["round_id"]),
                    run_id=str(job["run_id"]),
                    job_id=str(job.get("job_id") or ""),
                    message=str(exc),
                )
            )
    return summaries


def _validate_acceptance_gate(round_path: Path, run_manifest: dict[str, Any]) -> None:
    if str(run_manifest.get("run_type") or "") != "official":
        raise ValueError("only official runs can be accepted for automated resolution")
    if run_manifest.get("mock") is True:
        raise ValueError("mock runs cannot be accepted for public automation")
    if not bool(run_manifest.get("official_score_eligible")):
        raise ValueError("run is not official_score_eligible")
    model_count = _int_or_zero(run_manifest.get("model_count"))
    valid_submissions = _int_or_zero(run_manifest.get("valid_submissions"))
    invalid_submissions = _int_or_zero(run_manifest.get("invalid_submissions"))
    if model_count <= 0:
        raise ValueError("run has no model_count")
    if valid_submissions != model_count:
        raise ValueError(f"valid submissions do not match model_count: {valid_submissions} != {model_count}")
    if invalid_submissions != 0:
        raise ValueError(f"run has invalid submissions: {invalid_submissions}")
    if not round_hashes_match(round_path):
        raise ValueError("round hashes do not match current round files")
    for filename in ["manifest.yaml", "briefing.md", "options.yaml", "prompt.md", "hashes.json"]:
        if not (round_path / filename).exists():
            raise FileNotFoundError(f"missing required round file: {filename}")


def _validate_resolution_gate(round_path: Path, run_manifest: dict[str, Any]) -> None:
    _validate_acceptance_gate(round_path, run_manifest)
    if not bool(run_manifest.get("operator_selected_official")):
        raise ValueError("official run has not been accepted by operator")
    if not (round_path / "prices" / "entry_prices.csv").exists():
        raise FileNotFoundError("missing entry prices")


def _automation_job_row(
    *,
    round_id: str,
    run_id: str,
    due_at_utc: str,
    status: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    job_id = f"{round_id}:{run_id}:{AUTOMATION_JOB_TYPE}"
    return {
        "job_id": job_id,
        "round_id": round_id,
        "run_id": run_id,
        "job_type": AUTOMATION_JOB_TYPE,
        "due_at_utc": due_at_utc,
        "next_attempt_at_utc": due_at_utc,
        "status": status,
        "attempts": 0,
        "max_attempts": 30,
        "metadata": metadata or {},
    }


def _local_job_file(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "job_id": row["job_id"],
        "round_id": row["round_id"],
        "run_id": row["run_id"],
        "job_type": row["job_type"],
        "due_at_utc": row["due_at_utc"],
        "next_attempt_at_utc": row["next_attempt_at_utc"],
        "status": row["status"],
        "attempts": row["attempts"],
        "max_attempts": row["max_attempts"],
        "last_error": "",
        "created_at_utc": _utc_now(),
    }


def _job_is_due(job: dict[str, Any], due_before: datetime) -> bool:
    if str(job.get("status") or "") not in {"scheduled", "failed"}:
        return False
    next_attempt_raw = job.get("next_attempt_at_utc") or job.get("due_at_utc")
    if not next_attempt_raw:
        return False
    attempts = _int_or_zero(job.get("attempts"))
    max_attempts = _int_or_zero(job.get("max_attempts")) or 30
    return attempts < max_attempts and _parse_utc(str(next_attempt_raw)) <= due_before


def _mark_local_job(round_path: Path, **updates: Any) -> None:
    job_path = _local_job_path(round_path)
    if not job_path.exists():
        return
    job = read_yaml(job_path)
    if "status" in updates and updates["status"] == "running":
        job["attempts"] = _int_or_zero(job.get("attempts")) + 1
    for key, value in updates.items():
        job[key] = value
    write_yaml(job_path, job)


def _local_job_path(round_path: Path) -> Path:
    return round_path / AUTOMATION_DIRNAME / RESOLUTION_JOB_FILENAME


def _round_path_for_id(rounds_dir: Path, round_id: str) -> Path:
    direct = rounds_dir / round_id
    if (direct / "manifest.yaml").exists():
        return direct
    for candidate in rounds_dir.iterdir() if rounds_dir.exists() else []:
        if candidate.is_dir() and (candidate / "manifest.yaml").exists():
            try:
                if load_manifest(candidate).round_id == round_id:
                    return candidate
            except Exception:
                continue
    raise FileNotFoundError(f"round_id not found under {rounds_dir}: {round_id}")


def _default_due_at_utc(exit_date: str | None) -> str:
    if not exit_date:
        raise ValueError("round exit_date is required to schedule automated resolution")
    day = datetime.fromisoformat(exit_date).date()
    due = datetime.combine(day, DEFAULT_RESOLUTION_TIME_UTC)
    return due.isoformat()


def _horizon_days(entry_date: str | None, exit_date: str | None) -> int | None:
    if not entry_date or not exit_date:
        return None
    try:
        return (datetime.fromisoformat(exit_date).date() - datetime.fromisoformat(entry_date).date()).days
    except ValueError:
        return None


def _parse_utc(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _int_or_zero(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0

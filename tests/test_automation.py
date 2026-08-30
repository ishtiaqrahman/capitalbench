import csv
from pathlib import Path
from shutil import copytree
from types import SimpleNamespace
from typing import Any

import pytest
import yaml

from capitalbench.automation import (
    AutomationSummary,
    accept_run,
    automation_run,
    cancel_local_job,
    resolve_accepted_round,
    retry_local_job,
)
from capitalbench.hashing import write_round_hashes
from capitalbench.roster import portfolio_v2_roster_version


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROUND_1 = PROJECT_ROOT / "rounds" / "CB-2026-05-10-1M"


class FakeAutomationStore:
    def __init__(self) -> None:
        self.jobs: list[dict[str, Any]] = []
        self.updates: list[tuple[str, dict[str, Any]]] = []

    def upsert_job(self, row: dict[str, Any]) -> None:
        self.jobs.append(row)

    def claim_due_job(self, *, due_before_utc: str, worker_id: str) -> dict[str, Any] | None:
        return None

    def update_job(self, job_id: str, updates: dict[str, Any]) -> None:
        self.updates.append((job_id, updates))


def _copy_due_round(tmp_path: Path) -> Path:
    round_path = tmp_path / "CB-2026-05-10-1M"
    copytree(ROUND_1, round_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["exit_date"] = "2026-05-11"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    write_round_hashes(round_path)
    return round_path


def _write_exit_prices(round_path: Path) -> None:
    (round_path / "prices" / "exit_prices.csv").write_text(
        "\n".join(
            [
                "option_id,symbol,date,close,adj_close,source",
                "CASH,,2026-05-11,1.0,1.0,cash",
                "SP500,SPY,2026-05-11,740.00,740.00,test",
                "SEMICONDUCTORS,SMH,2026-05-11,580.00,580.00,test",
                "SOFTWARE,IGV,2026-05-11,93.00,93.00,test",
                "",
            ]
        ),
        encoding="utf-8",
    )


def test_accept_run_schedules_resolution_job(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    store = FakeAutomationStore()

    summary = accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=store,
        sync_pending=False,
    )

    assert summary.status == "scheduled"
    assert summary.job_id == "CB-2026-05-10-1M:official-round-1-clean:resolve_round"
    assert store.jobs[0]["round_id"] == "CB-2026-05-10-1M"
    assert store.jobs[0]["run_id"] == "official-round-1-clean"
    assert store.jobs[0]["status"] == "scheduled"
    local_job = yaml.safe_load((round_path / "automation" / "resolution_job.yaml").read_text(encoding="utf-8"))
    assert local_job["status"] == "scheduled"
    run_manifest = yaml.safe_load(
        (round_path / "runs" / "official-round-1-clean" / "run_manifest.yaml").read_text(encoding="utf-8")
    )
    assert run_manifest["operator_selected_official"] is True
    assert run_manifest["resolution_due_at_utc"] == "2026-05-11T23:30:00+00:00"


def test_cancel_and_retry_job_keep_remote_store_in_sync(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )

    cancel_store = FakeAutomationStore()
    cancelled = cancel_local_job(round_path, store=cancel_store)

    assert cancelled.status == "cancelled"
    assert cancel_store.updates == [
        (
            "CB-2026-05-10-1M:official-round-1-clean:resolve_round",
            {
                "status": "cancelled",
                "last_error": "cancelled by operator",
                "locked_at_utc": None,
                "locked_by": None,
            },
        )
    ]
    local_job = yaml.safe_load((round_path / "automation" / "resolution_job.yaml").read_text(encoding="utf-8"))
    assert local_job["status"] == "cancelled"
    assert local_job["last_error"] == "cancelled by operator"

    retry_store = FakeAutomationStore()
    retried = retry_local_job(round_path, next_attempt_at_utc="2026-05-12T00:00:00+00:00", store=retry_store)

    assert retried.status == "scheduled"
    assert retry_store.updates == [
        (
            "CB-2026-05-10-1M:official-round-1-clean:resolve_round",
            {
                "status": "scheduled",
                "next_attempt_at_utc": "2026-05-12T00:00:00+00:00",
                "last_error": "",
                "locked_at_utc": None,
                "locked_by": None,
                "completed_at_utc": None,
            },
        )
    ]
    local_job = yaml.safe_load((round_path / "automation" / "resolution_job.yaml").read_text(encoding="utf-8"))
    assert local_job["status"] == "scheduled"
    assert "cancelled_at_utc" not in local_job


def test_accept_run_syncs_round_selection_to_clear_superseded_rows(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    round_path = _copy_due_round(tmp_path)
    calls: list[tuple[Path, dict[str, Any]]] = []

    def fake_sync(path: Path, **kwargs: Any) -> None:
        calls.append((path, kwargs))

    monkeypatch.setattr("capitalbench.automation.optional_sync_round", fake_sync)

    accept_run(
        round_path,
        run_id="official-round-1-clean",
        store=FakeAutomationStore(),
        sync_pending=True,
    )

    assert calls == [(round_path, {"event_type": "accept_run"})]


def test_accept_legacy_v2_freezes_roster_from_decision_date(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    expected_model_ids = [
        "openai-gpt-5-5",
        "openai-gpt-5-6-sol",
        "anthropic-claude-opus-4-7",
        "anthropic-claude-opus-4-8",
        "anthropic-claude-fable-5",
        "google-gemini-3-1-pro",
        "xai-grok-4-3",
        "xai-grok-4-5",
    ]
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "round_id": "CB-2026-07-20-1W",
            "decision_date": "2026-07-20",
            "methodology_version": "portfolio-v2.0",
            "submission_format": "portfolio",
        }
    )
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    run_manifest_path = round_path / "runs" / "official-round-1-clean" / "run_manifest.yaml"
    run_manifest = yaml.safe_load(run_manifest_path.read_text(encoding="utf-8"))
    run_manifest.update(
        {
            "round_id": "CB-2026-07-20-1W",
            "model_count": len(expected_model_ids),
            "valid_submissions": len(expected_model_ids),
            "invalid_submissions": 0,
            "model_ids": expected_model_ids,
        }
    )
    run_manifest.pop("expected_model_ids", None)
    run_manifest.pop("model_roster_version", None)
    run_manifest_path.write_text(yaml.safe_dump(run_manifest, sort_keys=False), encoding="utf-8")
    write_round_hashes(round_path)

    accept_run(
        round_path,
        run_id="official-round-1-clean",
        store=FakeAutomationStore(),
        sync_pending=False,
    )

    frozen = yaml.safe_load(run_manifest_path.read_text(encoding="utf-8"))
    assert frozen["expected_model_ids"] == expected_model_ids
    assert frozen["model_roster_version"] == portfolio_v2_roster_version(expected_model_ids)
    assert frozen["model_roster_frozen_at_utc"]


def test_accept_run_rejects_invalid_official_run(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    run_manifest_path = round_path / "runs" / "official-round-1-clean" / "run_manifest.yaml"
    manifest = yaml.safe_load(run_manifest_path.read_text(encoding="utf-8"))
    manifest["invalid_submissions"] = 1
    manifest["official_score_eligible"] = False
    run_manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="not official_score_eligible"):
        accept_run(round_path, run_id="official-round-1-clean", sync_pending=False)


def test_accept_run_supersedes_previous_selected_run_and_cancels_job(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    original_path = round_path / "runs" / "official-round-1-clean"
    replacement_path = round_path / "runs" / "official-round-1-replacement"
    copytree(original_path, replacement_path)
    replacement_manifest_path = replacement_path / "run_manifest.yaml"
    replacement_manifest = yaml.safe_load(replacement_manifest_path.read_text(encoding="utf-8"))
    replacement_manifest["run_id"] = "official-round-1-replacement"
    replacement_manifest["operator_selected_official"] = False
    replacement_manifest_path.write_text(yaml.safe_dump(replacement_manifest, sort_keys=False), encoding="utf-8")
    store = FakeAutomationStore()

    accept_run(
        round_path,
        run_id="official-round-1-replacement",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=store,
        sync_pending=False,
    )

    original_manifest = yaml.safe_load((original_path / "run_manifest.yaml").read_text(encoding="utf-8"))
    assert original_manifest["operator_selected_official"] is False
    assert original_manifest["superseded_by_run_id"] == "official-round-1-replacement"
    assert store.updates == [
        (
            "CB-2026-05-10-1M:official-round-1-clean:resolve_round",
            {
                "status": "cancelled",
                "locked_at_utc": None,
                "locked_by": None,
                "last_error": "superseded by accepted run official-round-1-replacement",
            },
        )
    ]


def test_resolve_accepted_round_scores_publishes_and_marks_job(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    _write_exit_prices(round_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )

    summary = resolve_accepted_round(
        tmp_path,
        round_id="CB-2026-05-10-1M",
        run_id="official-round-1-clean",
        latest_output=tmp_path / "latest",
        cumulative_output=tmp_path / "cumulative",
        fetch_exit_prices=False,
        sync=False,
    )

    assert summary.status == "succeeded"
    assert (round_path / "runs" / "official-round-1-clean" / "results" / "leaderboard.csv").exists()
    assert (round_path / "runs" / "official-round-1-clean" / "results" / "report.md").exists()
    assert (tmp_path / "latest" / "latest_round_leaderboard.csv").exists()
    assert (tmp_path / "cumulative" / "official_leaderboard.csv").exists()
    local_job = yaml.safe_load((round_path / "automation" / "resolution_job.yaml").read_text(encoding="utf-8"))
    assert local_job["status"] == "succeeded"


def test_manual_resolution_marks_remote_job_succeeded(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    round_path = _copy_due_round(tmp_path)
    _write_exit_prices(round_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )
    monkeypatch.setattr("capitalbench.automation.optional_sync_round", lambda *args, **kwargs: None)
    monkeypatch.setattr("capitalbench.automation.optional_sync_latest", lambda *args, **kwargs: None)
    monkeypatch.setattr("capitalbench.automation.optional_sync_cumulative", lambda *args, **kwargs: None)
    store = FakeAutomationStore()

    summary = resolve_accepted_round(
        tmp_path,
        round_id="CB-2026-05-10-1M",
        run_id="official-round-1-clean",
        latest_output=tmp_path / "latest",
        cumulative_output=tmp_path / "cumulative",
        fetch_exit_prices=False,
        sync=True,
        store=store,
    )

    assert summary.status == "succeeded"
    assert len(store.updates) == 1
    job_id, updates = store.updates[0]
    assert job_id == "CB-2026-05-10-1M:official-round-1-clean:resolve_round"
    assert updates["status"] == "succeeded"
    assert updates["last_error"] == ""
    assert updates["completed_at_utc"]
    assert updates["metadata"]["outputs"] == summary.outputs


def test_resolve_accepted_round_preserves_entry_and_fetches_exit_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    round_path = _copy_due_round(tmp_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )
    calls: list[dict[str, Any]] = []
    original_entry = (round_path / "prices" / "entry_prices.csv").read_text(encoding="utf-8")

    def fake_fetch_selected_prices(**kwargs: Any) -> Any:
        calls.append(kwargs)
        prices_dir = round_path / "prices"
        prices_dir.mkdir(exist_ok=True)
        exit_path = prices_dir / "exit_prices.csv"
        exit_path.write_text(
            "\n".join(
                [
                    "option_id,symbol,date,close,adj_close,source",
                    "CASH,,2026-05-11,1.0,1.0,cash",
                    "SP500,SPY,2026-05-11,101.0,101.0,test",
                    "SEMICONDUCTORS,SMH,2026-05-11,110.0,110.0,test",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(exit_prices_path=exit_path)

    monkeypatch.setattr("capitalbench.automation.fetch_selected_prices", fake_fetch_selected_prices)

    summary = resolve_accepted_round(
        tmp_path,
        round_id="CB-2026-05-10-1M",
        run_id="official-round-1-clean",
        latest_output=tmp_path / "latest",
        cumulative_output=tmp_path / "cumulative",
        fetch_exit_prices=True,
        sync=False,
    )

    assert summary.status == "succeeded"
    assert len(calls) == 1
    assert calls[0]["entry_date"] is None
    assert calls[0]["exit_date"] == "2026-05-11"
    assert calls[0]["price_side"] == "exit"
    assert calls[0]["overwrite_prices"] is True
    assert calls[0]["full_universe"] is True
    assert calls[0]["allow_previous_trading_day_exit"] is True
    assert (round_path / "prices" / "entry_prices.csv").read_text(encoding="utf-8") == original_entry
    assert (tmp_path / "market_data" / "daily_price_snapshots" / "2026-05-11.csv").exists()


def test_resolve_accepted_round_reuses_shared_exit_snapshot(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    round_path = _copy_due_round(tmp_path)
    source_exit = round_path / "prices" / "exit_prices.csv"
    snapshot_path = tmp_path / "market_data" / "daily_price_snapshots" / "2026-05-11.csv"
    snapshot_path.parent.mkdir(parents=True)
    entry_snapshot = (round_path / "prices" / "entry_prices.csv").read_text(encoding="utf-8")
    snapshot_path.write_text(entry_snapshot.replace("2026-05-08", "2026-05-11"), encoding="utf-8")
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )

    def unexpected_fetch(**_kwargs: Any) -> Any:
        raise AssertionError("shared snapshot should avoid a provider fetch")

    monkeypatch.setattr("capitalbench.automation.fetch_selected_prices", unexpected_fetch)

    summary = resolve_accepted_round(
        tmp_path,
        round_id="CB-2026-05-10-1M",
        run_id="official-round-1-clean",
        latest_output=tmp_path / "latest",
        cumulative_output=tmp_path / "cumulative",
        sync=False,
    )

    assert summary.status == "succeeded"
    assert source_exit.exists()
    assert "2026-05-11" in source_exit.read_text(encoding="utf-8")


def test_resolve_accepted_round_repairs_incomplete_entry_from_shared_snapshot(
    tmp_path: Path,
) -> None:
    round_path = _copy_due_round(tmp_path)
    entry_path = round_path / "prices" / "entry_prices.csv"
    full_entry = entry_path.read_text(encoding="utf-8")
    (round_path / "prices" / "exit_prices.csv").write_text(
        full_entry.replace("2026-05-08", "2026-05-11"),
        encoding="utf-8",
    )
    snapshot_path = tmp_path / "market_data" / "daily_price_snapshots" / "2026-05-08.csv"
    snapshot_path.parent.mkdir(parents=True)
    snapshot_path.write_text(full_entry, encoding="utf-8")
    entry_path.write_text(
        "\n".join(line for line in full_entry.splitlines() if not line.startswith("SOFTWARE,")) + "\n",
        encoding="utf-8",
    )
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )

    summary = resolve_accepted_round(
        tmp_path,
        round_id="CB-2026-05-10-1M",
        run_id="official-round-1-clean",
        latest_output=tmp_path / "latest",
        cumulative_output=tmp_path / "cumulative",
        fetch_exit_prices=False,
        sync=False,
    )

    assert summary.status == "succeeded"
    with entry_path.open("r", encoding="utf-8", newline="") as handle:
        repaired_ids = {row["option_id"] for row in csv.DictReader(handle)}
    expected_ids = {
        line.split(",", 1)[0]
        for line in full_entry.splitlines()[1:]
        if line
    }
    assert repaired_ids == expected_ids
    leaderboard_path = round_path / "runs" / "official-round-1-clean" / "results" / "leaderboard.csv"
    with leaderboard_path.open("r", encoding="utf-8", newline="") as handle:
        leaderboard = list(csv.DictReader(handle))
    assert leaderboard
    assert all(row["regret_vs_best_option"] for row in leaderboard)


def test_resolve_accepted_round_stops_before_fetch_when_entry_snapshot_is_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    round_path = _copy_due_round(tmp_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )
    (round_path / "prices" / "entry_prices.csv").unlink()

    def unexpected_fetch(**_kwargs: Any) -> Any:
        raise AssertionError("provider fetch must not start without frozen entry prices")

    monkeypatch.setattr("capitalbench.automation.fetch_selected_prices", unexpected_fetch)

    with pytest.raises(FileNotFoundError, match="stopped before fetching exit prices"):
        resolve_accepted_round(
            tmp_path,
            round_id="CB-2026-05-10-1M",
            run_id="official-round-1-clean",
            latest_output=tmp_path / "latest",
            cumulative_output=tmp_path / "cumulative",
            sync=False,
        )


def test_automation_run_falls_back_to_due_local_jobs_when_supabase_has_none(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    round_path = _copy_due_round(tmp_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )
    calls: list[dict[str, Any]] = []

    def fake_resolve_accepted_round(*args: Any, **kwargs: Any) -> AutomationSummary:
        calls.append(kwargs)
        return AutomationSummary(
            status="succeeded",
            round_id=str(kwargs["round_id"]),
            run_id=str(kwargs["run_id"]),
            message="resolved by local fallback",
        )

    monkeypatch.setattr("capitalbench.automation.configured_automation_store_from_env", lambda: FakeAutomationStore())
    monkeypatch.setattr("capitalbench.automation.resolve_accepted_round", fake_resolve_accepted_round)

    summaries = automation_run(
        tmp_path,
        due_before_utc="2026-05-12T00:00:00+00:00",
        max_jobs=1,
        latest_output=tmp_path / "latest",
        cumulative_output=tmp_path / "cumulative",
    )

    assert len(summaries) == 1
    assert summaries[0].round_id == "CB-2026-05-10-1M"
    assert calls[0]["round_id"] == "CB-2026-05-10-1M"
    assert calls[0]["run_id"] == "official-round-1-clean"

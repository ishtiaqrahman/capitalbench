from pathlib import Path
from shutil import copytree
from types import SimpleNamespace
from typing import Any

import pytest
import yaml

from capitalbench.automation import AutomationSummary, accept_run, automation_run, resolve_accepted_round
from capitalbench.hashing import write_round_hashes


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROUND_1 = PROJECT_ROOT / "rounds" / "CB-2026-05-10-1M"


class FakeAutomationStore:
    def __init__(self) -> None:
        self.jobs: list[dict[str, Any]] = []

    def upsert_job(self, row: dict[str, Any]) -> None:
        self.jobs.append(row)

    def claim_due_job(self, *, due_before_utc: str, worker_id: str) -> dict[str, Any] | None:
        return None

    def update_job(self, job_id: str, updates: dict[str, Any]) -> None:
        raise AssertionError("not used")


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


def test_accept_run_rejects_invalid_official_run(tmp_path: Path) -> None:
    round_path = _copy_due_round(tmp_path)
    run_manifest_path = round_path / "runs" / "official-round-1-clean" / "run_manifest.yaml"
    manifest = yaml.safe_load(run_manifest_path.read_text(encoding="utf-8"))
    manifest["invalid_submissions"] = 1
    manifest["official_score_eligible"] = False
    run_manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="not official_score_eligible"):
        accept_run(round_path, run_id="official-round-1-clean", sync_pending=False)


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


def test_resolve_accepted_round_refreshes_entry_and_exit_prices(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    round_path = _copy_due_round(tmp_path)
    accept_run(
        round_path,
        run_id="official-round-1-clean",
        due_at_utc="2026-05-11T23:30:00+00:00",
        store=FakeAutomationStore(),
        sync_pending=False,
    )
    calls: list[dict[str, Any]] = []

    def fake_fetch_selected_prices(**kwargs: Any) -> Any:
        calls.append(kwargs)
        prices_dir = round_path / "prices"
        prices_dir.mkdir(exist_ok=True)
        (prices_dir / "entry_prices.csv").write_text(
            "\n".join(
                [
                    "option_id,symbol,date,close,adj_close,source",
                    "CASH,,2026-05-08,1.0,1.0,cash",
                    "SP500,SPY,2026-05-08,100.0,100.0,test",
                    "SEMICONDUCTORS,SMH,2026-05-08,100.0,100.0,test",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (prices_dir / "exit_prices.csv").write_text(
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
        return SimpleNamespace()

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
    assert calls[0]["entry_date"] == "2026-05-08"
    assert calls[0]["exit_date"] == "2026-05-11"
    assert calls[0]["price_side"] == "both"
    assert calls[0]["overwrite_prices"] is True
    assert calls[0]["full_universe"] is True
    assert calls[0]["allow_previous_trading_day_exit"] is True


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

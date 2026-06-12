import csv
import json
from pathlib import Path
from shutil import copytree, rmtree
from typing import Any

import yaml

from capitalbench.cli import main
from capitalbench.hashing import write_round_hashes
from capitalbench.scoring import score_round
from capitalbench.web_sync import (
    SUPABASE_SKIP_MESSAGE,
    _display_model_name,
    sync_cumulative_leaderboards,
    sync_latest_leaderboard,
    sync_round,
)
from capitalbench.weekly import update_weekly_performance


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROUND_1 = PROJECT_ROOT / "rounds" / "CB-2026-05-10-1M"


class FakeSink:
    def __init__(self) -> None:
        self.upserts: dict[str, list[dict[str, Any]]] = {}
        self.inserts: dict[str, list[dict[str, Any]]] = {}
        self.deletes: list[tuple[str, dict[str, Any]]] = []
        self.uploads: list[tuple[Path, str]] = []

    def upsert(self, table: str, rows: list[dict[str, Any]], *, on_conflict: str) -> None:
        self.upserts.setdefault(table, []).extend(rows)

    def insert(self, table: str, rows: list[dict[str, Any]]) -> None:
        self.inserts.setdefault(table, []).extend(rows)

    def delete_eq(self, table: str, filters: dict[str, Any]) -> None:
        self.deletes.append((table, filters))

    def upload_public_artifact(self, local_path: Path, storage_path: str) -> None:
        self.uploads.append((local_path, storage_path))


def test_claude_fable_uses_public_display_name() -> None:
    assert _display_model_name("anthropic-claude-fable-5") == "Claude Fable 5"


def _write_resolved_round(
    rounds_dir: Path,
    round_id: str,
    *,
    entry_date: str,
    exit_date: str,
    horizon: str,
    decision_deadline: str = "2026-01-01T20:00:00Z",
) -> None:
    round_path = rounds_dir / round_id
    results_dir = round_path / "runs" / "official" / "results"
    results_dir.mkdir(parents=True)
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": round_id,
                "title": round_id,
                "decision_deadline": decision_deadline,
                "entry_date": entry_date,
                "exit_date": exit_date,
                "horizon": horizon,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "runs" / "official" / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "official",
                "round_id": round_id,
                "run_type": "official",
                "mode": "closed_capability",
                "replicates": 1,
                "mock": False,
                "official_score_eligible": True,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    with (results_dir / "leaderboard.csv").open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "model_id",
            "provider",
            "mode",
            "selected_option_id",
            "confidence",
            "selected_asset_return",
            "sp500_return",
            "alpha_vs_sp500",
            "regret_vs_best_option",
            "rank_among_options",
            "beats_sp500",
            "beats_cash",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "SP500",
                "confidence": 0.5,
                "selected_asset_return": 0.03,
                "sp500_return": 0.02,
                "alpha_vs_sp500": 0.01,
                "regret_vs_best_option": "",
                "rank_among_options": 1,
                "beats_sp500": True,
                "beats_cash": True,
            }
        )


def test_sync_web_skips_when_supabase_env_is_missing(monkeypatch, capsys) -> None:
    monkeypatch.delenv("SUPABASE_URL", raising=False)
    monkeypatch.delenv("SUPABASE_SERVICE_ROLE_KEY", raising=False)

    exit_code = main(["sync-web", "--round", str(ROUND_1), "--run-id", "official-round-1-clean"])

    assert exit_code == 0
    assert SUPABASE_SKIP_MESSAGE in capsys.readouterr().out


def test_sync_round_publishes_pending_round_without_leaderboard(tmp_path: Path) -> None:
    round_path = tmp_path / "CB-2026-05-10-1M"
    copytree(ROUND_1, round_path)
    rmtree(round_path / "runs" / "official-round-1-clean" / "results")
    sink = FakeSink()

    summary = sync_round(round_path, run_id="official-round-1-clean", sink=sink)

    assert summary.status == "success"
    assert sink.upserts["rounds"][0]["status"] == "pending"
    assert sink.upserts["rounds"][0]["universe_version"] == "capitalbench_universe_v1_5"
    assert sink.upserts["runs"][0]["run_id"] == "official-round-1-clean"
    assert len(sink.upserts["submissions"]) == 4
    assert len(sink.upserts["submission_allocations"]) == 4
    assert {row["option_id"] for row in sink.upserts["submission_allocations"]} == {"SEMICONDUCTORS"}
    assert {row["allocation_bps"] for row in sink.upserts["submission_allocations"]} == {10000}
    assert all(len(row["portfolio"]) == 1 for row in sink.upserts["submissions"])
    assert all(row["portfolio"][0]["allocation_bps"] == 10000 for row in sink.upserts["submissions"])
    assert all(row["portfolio"][0]["rationale"] == row["rationale_summary"] for row in sink.upserts["submissions"])
    assert len(sink.upserts["official_results"]) == 0
    assert any(row["option_id"] == "SEMICONDUCTORS" and row["entry_price"] for row in sink.upserts["options"])
    assert any(row["path"] == "hashes.json" for row in sink.upserts["audit_artifacts"])
    assert sink.inserts["sync_events"][0]["status"] == "success"


def test_sync_round_publishes_resolved_single_pick_result_fields(tmp_path: Path) -> None:
    round_path = tmp_path / "CB-2026-05-10-1M"
    copytree(ROUND_1, round_path)
    sink = FakeSink()

    summary = sync_round(round_path, run_id="official-round-1-clean", sink=sink)

    assert summary.status == "success"
    assert sink.upserts["rounds"][0]["status"] == "resolved"
    assert len(sink.upserts["official_results"]) == 4
    assert all(row["portfolio_return"] == row["selected_asset_return"] for row in sink.upserts["official_results"])
    sp500_return = next(row for row in sink.upserts["option_returns"] if row["option_id"] == "SP500")
    assert sp500_return["is_benchmark"] is True


def test_sync_round_uses_operator_selected_official_run_and_clears_stale_public_rows(tmp_path: Path) -> None:
    round_path = tmp_path / "CB-2026-06-02-1W"
    copytree(PROJECT_ROOT / "rounds" / "CB-2026-06-02-1W", round_path)
    sink = FakeSink()

    summary = sync_round(round_path, sink=sink)

    assert summary.status == "success"
    assert {row["run_id"] for row in sink.upserts["runs"]} == {"official-20260602-clean"}
    assert {row["run_id"] for row in sink.upserts["submissions"]} == {"official-20260602-clean"}
    assert len(sink.upserts["submissions"]) == 5
    weekly_performance_path = (
        round_path / "runs" / "official-20260602-clean" / "results" / "weekly_performance.csv"
    )
    with weekly_performance_path.open(encoding="utf-8", newline="") as handle:
        expected_weekly_rows = list(csv.DictReader(handle))
    assert len(sink.upserts["round_weekly_performance"]) == len(expected_weekly_rows)
    assert ("submissions", {"round_id": "CB-2026-06-02-1W"}) in sink.deletes
    assert ("round_weekly_performance", {"round_id": "CB-2026-06-02-1W"}) in sink.deletes
    assert ("runs", {"round_id": "CB-2026-06-02-1W"}) in sink.deletes


def test_sync_round_refuses_mock_official_public_result(tmp_path: Path) -> None:
    round_path = tmp_path / "CB-2026-05-10-1M"
    copytree(ROUND_1, round_path)
    run_manifest_path = round_path / "runs" / "official-round-1-clean" / "run_manifest.yaml"
    manifest = yaml.safe_load(run_manifest_path.read_text(encoding="utf-8"))
    manifest["mock"] = True
    run_manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    sink = FakeSink()

    try:
        sync_round(round_path, run_id="official-round-1-clean", sink=sink)
    except ValueError as exc:
        assert "not syncable public benchmark data" in str(exc)
    else:
        raise AssertionError("mock official run was synced")


def test_sync_round_publishes_portfolio_allocations(tmp_path: Path) -> None:
    round_path = tmp_path / "portfolio-round"
    (round_path / "runs" / "official" / "submissions" / "parsed").mkdir(parents=True)
    (round_path / "prices").mkdir(parents=True)
    (round_path / "briefing.md").write_text("Briefing.", encoding="utf-8")
    (round_path / "prompt.md").write_text("Prompt.", encoding="utf-8")
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "portfolio-round",
                "title": "Portfolio Round",
                "description": "Portfolio test.",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_date": "2026-01-02",
                "exit_date": "2026-02-02",
                "methodology_version": "portfolio-v1.0",
                "universe_version": "test-v2.0",
                "submission_format": "portfolio",
                "portfolio_constraints": {
                    "min_holdings": 1,
                    "max_holdings": 5,
                    "allocation_increment_pct": 5,
                    "min_allocation_pct": 5,
                    "max_total_allocation_pct": 100,
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "options.yaml").write_text(
        yaml.safe_dump(
            {
                "options": [
                    {"option_id": "opt_a", "label": "Option A", "asset_symbol": "AAA"},
                    {"option_id": "sp500", "label": "S&P 500", "asset_symbol": "SPY", "is_benchmark": True},
                    {"option_id": "cash", "label": "Cash", "asset_symbol": "USD", "is_cash": True},
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    for name in ["entry_prices.csv", "exit_prices.csv"]:
        price = 100 if name.startswith("entry") else 110
        (round_path / "prices" / name).write_text(
            "option_id,price\nopt_a,{price}\nsp500,105\ncash,1\n".format(price=price),
            encoding="utf-8",
        )
    (round_path / "runs" / "official" / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "official",
                "round_id": "portfolio-round",
                "run_type": "official",
                "mode": "closed_capability",
                "replicates": 1,
                "mock": False,
                "official_score_eligible": True,
                "model_count": 1,
                "valid_submissions": 1,
                "invalid_submissions": 0,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "runs" / "official" / "validation_summary.json").write_text(
        json.dumps({"invalid_count": 0}),
        encoding="utf-8",
    )
    (round_path / "runs" / "official" / "run_log.jsonl").write_text("", encoding="utf-8")
    (round_path / "runs" / "official" / "submissions" / "parsed" / "model-a.json").write_text(
        json.dumps(
            {
                "round_id": "portfolio-round",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "run_type": "official",
                "replicate_index": 1,
                "replicate_count": 1,
                "is_official_score": True,
                "portfolio": [
                    {"option_id": "opt_a", "allocation_pct": 60, "rationale": "Upside."},
                    {"option_id": "sp500", "allocation_pct": 40, "rationale": "Benchmark."},
                ],
                "confidence": 0.5,
                "portfolio_rationale": "Portfolio rationale.",
                "rationale_summary": "Summary.",
                "key_risks": ["Risk clause; still one risk."],
            }
        ),
        encoding="utf-8",
    )
    score_round(round_path, run_id="official")
    update_weekly_performance(
        round_path,
        "official",
        snapshot_price_files=[round_path / "prices" / "exit_prices.csv"],
        snapshot_dates=["2026-01-09"],
    )
    write_round_hashes(round_path)
    sink = FakeSink()

    sync_round(round_path, run_id="official", sink=sink)

    assert sink.upserts["rounds"][0]["methodology_version"] == "portfolio-v1.0"
    assert sink.upserts["rounds"][0]["universe_version"] == "test-v2.0"
    assert sink.upserts["rounds"][0]["submission_format"] == "portfolio"
    assert sink.upserts["options"][0]["sort_order"] == 1
    assert sink.upserts["submissions"][0]["submission_format"] == "portfolio"
    assert sink.upserts["submissions"][0]["holding_count"] == 2
    assert sink.upserts["submissions"][0]["portfolio"] == [
        {"option_id": "opt_a", "allocation_bps": 6000, "allocation_pct": 60.0, "rationale": "Upside."},
        {"option_id": "sp500", "allocation_bps": 4000, "allocation_pct": 40.0, "rationale": "Benchmark."},
    ]
    assert len(sink.upserts["submission_allocations"]) == 2
    assert {row["allocation_bps"] for row in sink.upserts["submission_allocations"]} == {6000, 4000}
    assert len(sink.upserts["round_weekly_prices"]) == 6
    assert len(sink.upserts["round_weekly_performance"]) == 2
    assert sink.upserts["round_weekly_performance"][1]["submission_format"] == "portfolio"
    assert sink.upserts["official_results"][0]["key_risks"] == ["Risk clause; still one risk."]


def test_sync_latest_clears_stale_rows_when_no_public_resolved_round(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    copytree(PROJECT_ROOT / "rounds" / "example-round-2", rounds_dir / "example-round-2")
    sink = FakeSink()

    summary = sync_latest_leaderboard(rounds_dir, sink=sink)

    assert summary.status == "skipped"
    assert summary.row_counts == {"latest_leaderboard": 0}
    assert ("latest_leaderboard", {"slot": "latest"}) in sink.deletes
    assert "latest_leaderboard" not in sink.upserts


def test_sync_latest_and_cumulative_use_track_slots(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _write_resolved_round(
        rounds_dir,
        "CB-2026-01-01-1W",
        entry_date="2026-01-02",
        exit_date="2026-01-09",
        horizon="one week",
    )
    _write_resolved_round(
        rounds_dir,
        "CB-2026-01-01-1M",
        entry_date="2026-01-02",
        exit_date="2026-02-02",
        horizon="one month",
    )
    sink = FakeSink()

    sync_latest_leaderboard(rounds_dir, sink=sink, track="weekly")
    sync_cumulative_leaderboards(rounds_dir, sink=sink, track="weekly")

    assert ("latest_leaderboard", {"slot": "latest_weekly"}) in sink.deletes
    assert sink.upserts["latest_leaderboard"][0]["slot"] == "latest_weekly"
    assert sink.upserts["latest_leaderboard"][0]["round_id"] == "CB-2026-01-01-1W"
    assert ("cumulative_official_leaderboard", {"slot": "cumulative_weekly"}) in sink.deletes
    assert sink.upserts["cumulative_official_leaderboard"][0]["slot"] == "cumulative_weekly"
    assert sink.upserts["cumulative_official_leaderboard"][0]["rounds_included"] == "CB-2026-01-01-1W"


def test_sync_latest_uses_scoring_end_date_for_hydrated_latest_table(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _write_resolved_round(
        rounds_dir,
        "CB-2026-03-01-1W",
        entry_date="2026-03-02",
        exit_date="2026-03-09",
        horizon="one week",
        decision_deadline="2026-03-01T20:00:00Z",
    )
    _write_resolved_round(
        rounds_dir,
        "CB-2026-02-01-1W",
        entry_date="2026-03-10",
        exit_date="2026-03-17",
        horizon="one week",
        decision_deadline="2026-02-01T20:00:00Z",
    )
    sink = FakeSink()

    sync_latest_leaderboard(rounds_dir, sink=sink, track="weekly")

    assert sink.upserts["latest_leaderboard"][0]["slot"] == "latest_weekly"
    assert sink.upserts["latest_leaderboard"][0]["round_id"] == "CB-2026-02-01-1W"

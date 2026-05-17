import json
from pathlib import Path
from shutil import copytree
from typing import Any

import yaml

from capitalbench.cli import main
from capitalbench.hashing import write_round_hashes
from capitalbench.scoring import score_round
from capitalbench.web_sync import SUPABASE_SKIP_MESSAGE, sync_latest_leaderboard, sync_round


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


def test_sync_web_skips_when_supabase_env_is_missing(monkeypatch, capsys) -> None:
    monkeypatch.delenv("SUPABASE_URL", raising=False)
    monkeypatch.delenv("SUPABASE_SERVICE_ROLE_KEY", raising=False)

    exit_code = main(["sync-web", "--round", str(ROUND_1), "--run-id", "official-round-1-clean"])

    assert exit_code == 0
    assert SUPABASE_SKIP_MESSAGE in capsys.readouterr().out


def test_sync_round_publishes_pending_round_without_leaderboard(tmp_path: Path) -> None:
    round_path = tmp_path / "CB-2026-05-10-1M"
    copytree(ROUND_1, round_path)
    sink = FakeSink()

    summary = sync_round(round_path, run_id="official-round-1-clean", sink=sink)

    assert summary.status == "success"
    assert sink.upserts["rounds"][0]["status"] == "pending"
    assert sink.upserts["rounds"][0]["universe_version"] == "capitalbench_universe_v1_5"
    assert sink.upserts["runs"][0]["run_id"] == "official-round-1-clean"
    assert len(sink.upserts["submissions"]) == 4
    assert len(sink.upserts["official_results"]) == 0
    assert any(row["option_id"] == "SEMICONDUCTORS" and row["entry_price"] for row in sink.upserts["options"])
    assert any(row["path"] == "hashes.json" for row in sink.upserts["audit_artifacts"])
    assert sink.inserts["sync_events"][0]["status"] == "success"


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
                "key_risks": ["Risk"],
            }
        ),
        encoding="utf-8",
    )
    score_round(round_path, run_id="official")
    write_round_hashes(round_path)
    sink = FakeSink()

    sync_round(round_path, run_id="official", sink=sink)

    assert sink.upserts["rounds"][0]["universe_version"] == "test-v2.0"
    assert sink.upserts["rounds"][0]["submission_format"] == "portfolio"
    assert sink.upserts["options"][0]["sort_order"] == 1
    assert sink.upserts["submissions"][0]["submission_format"] == "portfolio"
    assert sink.upserts["submissions"][0]["holding_count"] == 2
    assert len(sink.upserts["submission_allocations"]) == 2
    assert {row["allocation_bps"] for row in sink.upserts["submission_allocations"]} == {6000, 4000}


def test_sync_latest_clears_stale_rows_when_no_public_resolved_round(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    copytree(PROJECT_ROOT / "rounds" / "example-round-2", rounds_dir / "example-round-2")
    sink = FakeSink()

    summary = sync_latest_leaderboard(rounds_dir, sink=sink)

    assert summary.status == "skipped"
    assert summary.row_counts == {"latest_leaderboard": 0}
    assert ("latest_leaderboard", {"slot": "latest"}) in sink.deletes
    assert "latest_leaderboard" not in sink.upserts

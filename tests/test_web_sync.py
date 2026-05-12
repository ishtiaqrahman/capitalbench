from pathlib import Path
from shutil import copytree
from typing import Any

import yaml

from capitalbench.cli import main
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


def test_sync_latest_clears_stale_rows_when_no_public_resolved_round(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    copytree(PROJECT_ROOT / "rounds" / "example-round-2", rounds_dir / "example-round-2")
    sink = FakeSink()

    summary = sync_latest_leaderboard(rounds_dir, sink=sink)

    assert summary.status == "skipped"
    assert summary.row_counts == {"latest_leaderboard": 0}
    assert ("latest_leaderboard", {"slot": "latest"}) in sink.deletes
    assert "latest_leaderboard" not in sink.upserts

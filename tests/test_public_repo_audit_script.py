import importlib.util
import sys
from datetime import date
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "public_repo_audit.py"
SPEC = importlib.util.spec_from_file_location("public_repo_audit", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
public_repo_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = public_repo_audit
SPEC.loader.exec_module(public_repo_audit)
entry_prices_are_due = public_repo_audit.entry_prices_are_due


def _round_with_entry_date(tmp_path: Path, entry_date: str) -> Path:
    round_path = tmp_path / "round"
    round_path.mkdir()
    (round_path / "manifest.yaml").write_text(
        f"round_id: test-round\nentry_date: '{entry_date}'\n",
        encoding="utf-8",
    )
    return round_path


def test_entry_prices_are_not_due_before_or_on_entry_date(tmp_path: Path) -> None:
    round_path = _round_with_entry_date(tmp_path, "2026-08-17")

    assert entry_prices_are_due(round_path, today_utc=date(2026, 8, 16)) is False
    assert entry_prices_are_due(round_path, today_utc=date(2026, 8, 17)) is False


def test_entry_prices_are_due_after_entry_date(tmp_path: Path) -> None:
    round_path = _round_with_entry_date(tmp_path, "2026-08-17")

    assert entry_prices_are_due(round_path, today_utc=date(2026, 8, 18)) is True

from pathlib import Path
from shutil import copytree

from capitalbench.audit import audit_round
from capitalbench.cli import main
from capitalbench.io import read_yaml, write_yaml
from capitalbench.report import publish_report
from capitalbench.run_store import get_selected_run_paths
from capitalbench.scoring import score_round
from capitalbench.validation import validate_submissions


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROUND = PROJECT_ROOT / "rounds" / "example-round"


def _copy_example_round(tmp_path: Path) -> Path:
    target = tmp_path / "example-round"
    copytree(EXAMPLE_ROUND, target)
    return target


def test_sample_round_end_to_end(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)

    validation = validate_submissions(round_path, run_id="legacy-run")
    scores = score_round(round_path, run_id="legacy-run")
    report_path = publish_report(round_path, run_id="legacy-run")
    audit = audit_round(round_path)

    assert validation.valid_count >= 4
    assert validation.invalid_count == 0
    assert len(scores) >= 4
    assert {"openai", "anthropic", "google", "xai"}.issubset({score.provider for score in scores})
    run_paths = get_selected_run_paths(round_path, "legacy-run")
    assert (run_paths.results_dir / "leaderboard.csv").exists()
    assert report_path.exists()
    assert audit.ok is True


def test_audit_command_reports_pass(tmp_path: Path, capsys) -> None:
    round_path = _copy_example_round(tmp_path)

    exit_code = main(["audit-round", "--round", str(round_path)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Audit status: PASS" in captured.out
    assert "hashes.json matches current files: yes" in captured.out


def test_audit_accepts_disclosed_legacy_sha_only_raw_responses(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_paths = get_selected_run_paths(round_path, "legacy-run")
    run_paths.raw_responses_dir.mkdir(parents=True, exist_ok=True)
    manifest = read_yaml(run_paths.run_manifest_path)
    manifest["raw_response_text_preservation"] = "sha_only_for_this_run"
    write_yaml(run_paths.run_manifest_path, manifest)

    audit = audit_round(round_path, run_id="legacy-run")

    assert audit.ok is True
    assert any("legacy SHA-only run disclosed" in line for line in audit.lines)


def test_hash_mismatch_detection(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    briefing = round_path / "briefing.md"
    briefing.write_text(briefing.read_text(encoding="utf-8") + "\nChanged after hashing.\n", encoding="utf-8")

    audit = audit_round(round_path)

    assert audit.ok is False
    assert any("hashes.json matches current files: no" in line for line in audit.lines)


def test_audit_flags_weekly_prompt_with_one_month_wording(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = read_yaml(manifest_path)
    manifest["horizon"] = "one week"
    write_yaml(manifest_path, manifest)
    (round_path / "prompt.md").write_text("Optimize for this one-month scoring window.\n", encoding="utf-8")
    assert main(["hash-round", "--round", str(round_path)]) == 0

    audit = audit_round(round_path)

    assert audit.ok is False
    assert any("Weekly prompt has no one-month wording: no" in line for line in audit.lines)

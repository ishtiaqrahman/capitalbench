import hashlib
from pathlib import Path
from shutil import copytree

import pytest

from capitalbench.audit import audit_round
from capitalbench.cli import main
from capitalbench.hashing import sha256_file
from capitalbench.prompting import build_prompt
from capitalbench.report import publish_report, publish_round_summary
from capitalbench.research import import_research_artifacts


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROUND = PROJECT_ROOT / "rounds" / "example-round"


def _copy_example_round(tmp_path: Path) -> Path:
    target = tmp_path / "example-round"
    copytree(EXAMPLE_ROUND, target)
    return target


def _write_research_files(tmp_path: Path, final_text: str = "Final model-facing facts.\n") -> tuple[Path, Path, Path]:
    market = tmp_path / "market_fact_report.md"
    audit = tmp_path / "briefing_audit_report.md"
    final = tmp_path / "final_briefing.md"
    market.write_text("Market fact source ledger.\nAudit-only detail.\n", encoding="utf-8")
    audit.write_text("Briefing audit gap-check report.\nAudit-only correction notes.\n", encoding="utf-8")
    final.write_text(final_text, encoding="utf-8")
    return market, audit, final


def test_import_research_creates_folder_and_copies_files(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path)

    summary = import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )

    research_dir = round_path / "research"
    assert summary.research_dir == research_dir
    assert (research_dir / "market_fact_report.md").exists()
    assert (research_dir / "briefing_audit_report.md").exists()
    assert (research_dir / "final_briefing.md").exists()
    assert (research_dir / "research_manifest.yaml").exists()
    assert (research_dir / "research_hashes.json").exists()
    assert (round_path / "briefing.md").read_text(encoding="utf-8") == final.read_text(encoding="utf-8")


def test_final_briefing_hash_equals_briefing_hash_after_import(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path)

    import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )

    assert sha256_file(round_path / "research" / "final_briefing.md") == sha256_file(round_path / "briefing.md")


def test_prompt_builder_excludes_audit_only_reports(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path, final_text="Only this briefing reaches the model.\n")

    import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )
    prompt = build_prompt(round_path)

    assert "Only this briefing reaches the model." in prompt
    assert "Market fact source ledger" not in prompt
    assert "Briefing audit gap-check report" not in prompt
    assert "research_manifest.yaml" not in prompt
    assert "research_hashes.json" not in prompt


def test_prompt_builder_rejects_prohibited_benchmark_allocation_instruction(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    prohibited = (
        "The S&P 500 benchmark asset is an allowed holding. Allocate to it when expected active edge is weak "
        "or when the benchmark case is more robust than available active alternatives. Do not add active risk "
        "only because this is a benchmark contest."
    )
    (round_path / "prompt.md").write_text(prohibited, encoding="utf-8")

    with pytest.raises(ValueError, match="prohibited benchmark-allocation instruction"):
        build_prompt(round_path)


def test_import_research_fails_on_empty_final_briefing(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path, final_text="")

    with pytest.raises(ValueError, match="cannot be empty"):
        import_research_artifacts(
            round_path=round_path,
            market_fact_report=market,
            audit_report=audit,
            final_briefing=final,
            research_cutoff_utc="2026-05-09T21:00:00Z",
        )


def test_import_research_fails_on_recommendation_language(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path, final_text="The best pick is SP500.\n")

    with pytest.raises(ValueError, match="best pick"):
        import_research_artifacts(
            round_path=round_path,
            market_fact_report=market,
            audit_report=audit,
            final_briefing=final,
            research_cutoff_utc="2026-05-09T21:00:00Z",
        )


def test_import_research_fails_on_subjective_analysis_language(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path, final_text="Scenario analysis: conditions vary.\n")

    with pytest.raises(ValueError, match="scenario analysis"):
        import_research_artifacts(
            round_path=round_path,
            market_fact_report=market,
            audit_report=audit,
            final_briefing=final,
            research_cutoff_utc="2026-05-09T21:00:00Z",
        )


def test_import_research_fails_on_market_impact_language(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path, final_text="This event has clear market impact.\n")

    with pytest.raises(ValueError, match="market impact"):
        import_research_artifacts(
            round_path=round_path,
            market_fact_report=market,
            audit_report=audit,
            final_briefing=final,
            research_cutoff_utc="2026-05-09T21:00:00Z",
        )


def test_import_research_warns_on_urls(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(
        tmp_path,
        final_text="Facts are summarized here. See https://example.com for a source.\n",
    )

    summary = import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )

    assert any("URLs found" in warning for warning in summary.warnings)


def test_import_research_cli_prints_url_warning(tmp_path: Path, capsys) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(
        tmp_path,
        final_text="Facts are summarized here. Source: https://example.com\n",
    )

    exit_code = main(
        [
            "import-research",
            "--round",
            str(round_path),
            "--market-fact-report",
            str(market),
            "--audit-report",
            str(audit),
            "--final-briefing",
            str(final),
            "--research-cutoff-utc",
            "2026-05-09T21:00:00Z",
        ]
    )
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "warning: URLs found" in captured.err


def test_audit_round_reports_research_artifacts(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path)
    import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )

    audit_result = audit_round(round_path)
    lines = "\n".join(audit_result.lines)

    assert "research/market_fact_report.md exists: yes" in lines
    assert "research/briefing_audit_report.md exists: yes" in lines
    assert "research/final_briefing.md exists: yes" in lines
    assert "final_briefing.md hash matches briefing.md: yes" in lines
    assert "only final_briefing is model-facing: yes" in lines


def test_publish_report_includes_research_artifact_hashes(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path)
    import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )

    report_path = publish_report(round_path, run_id="official-mock")
    report = report_path.read_text(encoding="utf-8")
    final_hash = hashlib.sha256(final.read_bytes()).hexdigest()

    assert "## Research Artifacts" in report
    assert "research/market_fact_report.md" in report
    assert "research/briefing_audit_report.md" in report
    assert "research/final_briefing.md" in report
    assert final_hash in report


def test_publish_round_summary_includes_research_artifact_hashes(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    market, audit, final = _write_research_files(tmp_path)
    import_research_artifacts(
        round_path=round_path,
        market_fact_report=market,
        audit_report=audit,
        final_briefing=final,
        research_cutoff_utc="2026-05-09T21:00:00Z",
    )

    summary_path = publish_round_summary(round_path, "official-mock", "stability-mock")
    summary = summary_path.read_text(encoding="utf-8")
    final_hash = hashlib.sha256(final.read_bytes()).hexdigest()

    assert "## Research Artifacts" in summary
    assert "research/final_briefing.md" in summary
    assert final_hash in summary

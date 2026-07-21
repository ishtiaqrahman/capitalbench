import csv
import json
from datetime import date, timedelta
from pathlib import Path

import pytest
import yaml

from capitalbench.decision_context import (
    DECISION_CONTEXT_TITLE,
    QUALITY_EVIDENCE_TITLE,
    fetch_universe_decision_context,
)
from capitalbench.prompting import build_prompt


def _write_round(tmp_path: Path, *, horizon: str = "one week") -> Path:
    round_path = tmp_path / "round"
    round_path.mkdir()
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "CB-2026-01-30-V2-1W",
                "title": "V2 test",
                "decision_date": "2026-01-30",
                "decision_deadline": "2026-01-31T07:30:00Z",
                "horizon": horizon,
                "entry_date": "2026-01-30",
                "exit_date": "2026-02-06" if horizon == "one week" else "2026-03-02",
                "methodology_version": "portfolio-v2.0-pilot",
                "submission_format": "portfolio",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "options.yaml").write_text(
        yaml.safe_dump(
            {
                "options": [
                    {"option_id": "ASSET", "label": "Asset", "asset_symbol": "AAA"},
                    {
                        "option_id": "SP500",
                        "label": "S&P 500",
                        "asset_symbol": "SPY",
                        "is_benchmark": True,
                    },
                    {"option_id": "CASH", "label": "Cash", "asset_symbol": "USD", "is_cash": True},
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "prompt.md").write_text("Return the required V2 portfolio JSON.", encoding="utf-8")
    (round_path / "briefing.md").write_text("Fixed facts-only briefing.", encoding="utf-8")
    return round_path


def _history(symbol: str, start: date, end: date):
    rows = []
    cursor = start
    index = 0
    slope = 0.0015 if symbol == "AAA" else 0.0005
    while cursor <= end:
        rows.append(
            {
                "date": cursor.isoformat(),
                "adjClose": 100.0 * (1.0 + slope * index),
                "adjVolume": 1_000_000 + index * 2_500,
            }
        )
        cursor += timedelta(days=1)
        index += 1
    return rows, "fixture_adjusted_price_and_volume"


def test_weekly_decision_context_is_complete_and_replaces_v1_appendix(tmp_path: Path) -> None:
    round_path = _write_round(tmp_path)

    output = fetch_universe_decision_context(
        round_path=round_path,
        as_of_date="2026-01-30",
        fetcher=_history,
    )

    assert output.profile == "weekly"
    assert output.failed_options == []
    with output.csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 3
    assert len(rows[0]) == 15
    assert float(rows[0]["active_return_5s"]) > 0
    prompt = build_prompt(round_path)
    assert prompt.count(DECISION_CONTEXT_TITLE) == 1
    assert "Full-Universe Price, Risk, And Benchmark Context" not in prompt
    assert "single-turn, non-agentic" in prompt


def test_monthly_decision_context_uses_monthly_profile_without_live_calls(tmp_path: Path) -> None:
    round_path = _write_round(tmp_path, horizon="one month")

    output = fetch_universe_decision_context(
        round_path=round_path,
        as_of_date="2026-01-30",
        fetcher=_history,
    )

    with output.csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    row = rows[0]
    cash = next(item for item in rows if item["option_id"] == "CASH")
    assert output.profile == "monthly"
    assert "active_return_21s" in row
    assert cash["active_return_21s"] != ""
    assert "prior_105s_active_return" in row
    assert "active_return_5s" not in row


def test_production_v2_decision_context_is_compact_and_clustered(tmp_path: Path) -> None:
    round_path = _write_round(tmp_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["methodology_version"] = "portfolio-v2.0"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    output = fetch_universe_decision_context(
        round_path=round_path,
        as_of_date="2026-01-30",
        fetcher=_history,
    )

    with output.csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    row = rows[0]
    cash = next(item for item in rows if item["option_id"] == "CASH")
    assert len(row) == 12
    assert "economic_exposure_cluster" in row
    assert cash["economic_exposure_cluster"] == "capital_preservation"
    assert "return_5s" not in row
    assert "as_of_price_date" not in row
    assert "status" not in row


def test_portfolio_v2_2_adds_q1_evidence_without_forcing_selection(tmp_path: Path) -> None:
    round_path = _write_round(tmp_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["methodology_version"] = "portfolio-v2.2"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    output = fetch_universe_decision_context(
        round_path=round_path,
        as_of_date="2026-01-30",
        fetcher=_history,
    )

    assert output.quality_json_path is not None
    assert output.quality_markdown_path is not None
    report = json.loads(output.quality_json_path.read_text(encoding="utf-8"))
    assert report["coverage"] == 1.0
    assert report["weights"] == {
        "low_volatility_rank": 0.15,
        "prior_active_rank": 0.45,
        "recent_active_reversal_rank": 0.30,
        "shallow_drawdown_rank": 0.10,
    }
    assert len(report["rows"]) == 1
    assert report["rows"][0]["option_id"] == "ASSET"
    assert report["rows"][0]["quality_evidence_score"] == 0.5

    prompt = build_prompt(round_path)
    assert prompt.count(QUALITY_EVIDENCE_TITLE) == 1
    assert prompt.index(QUALITY_EVIDENCE_TITLE) < prompt.index("## Briefing")
    assert "Use or reject this evidence as you judge appropriate." in prompt
    assert "ten highest scores" not in prompt
    assert "final five must include at least two" not in prompt


def test_portfolio_v2_2_rejects_incomplete_q1_evidence_at_prompt_time(tmp_path: Path) -> None:
    round_path = _write_round(tmp_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["methodology_version"] = "portfolio-v2.2"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    options_path = round_path / "options.yaml"
    options = yaml.safe_load(options_path.read_text(encoding="utf-8"))
    options["options"].insert(
        1,
        {"option_id": "ASSET_B", "label": "Asset B", "asset_symbol": "BBB"},
    )
    options_path.write_text(yaml.safe_dump(options, sort_keys=False), encoding="utf-8")

    def partial_history(symbol: str, start: date, end: date):
        if symbol == "BBB":
            raise ValueError("fixture unavailable")
        return _history(symbol, start, end)

    fetch_universe_decision_context(
        round_path=round_path,
        as_of_date="2026-01-30",
        fetcher=partial_history,
    )

    with pytest.raises(ValueError, match="coverage is below"):
        build_prompt(round_path)

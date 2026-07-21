from __future__ import annotations

from datetime import date

import pytest

from scripts.analyze_v2_resolution_diagnostics import (
    candidate_overlap,
    construction_counterfactuals,
    construction_rules,
    model_diagnostic,
    yahoo_rows_for_options,
)


class Option:
    def __init__(self, option_id: str, symbol: str = "") -> None:
        self.option_id = option_id
        self.tiingo_symbol = symbol
        self.symbol = symbol
        self.asset_symbol = symbol


def submission() -> dict:
    return {
        "model_id": "model-a",
        "candidate_ledger": [
            {"option_id": "SP500", "decision": "rejected", "forecast_low_pct": -1, "forecast_base_pct": 0.5, "forecast_high_pct": 2},
            {"option_id": "A", "decision": "selected", "forecast_low_pct": -1, "forecast_base_pct": 2, "forecast_high_pct": 4},
            {"option_id": "B", "decision": "rejected", "forecast_low_pct": -2, "forecast_base_pct": 1, "forecast_high_pct": 3},
        ],
        "portfolio": [{"option_id": "A", "allocation_pct": 100}],
    }


def test_regret_decomposition_sums_to_total() -> None:
    row = model_diagnostic(
        submission(),
        {"portfolio_return": "0.04"},
        {"SP500": 0.02, "A": 0.04, "B": 0.08, "C": 0.10},
        {"A", "B", "C"},
        {"C"},
        0.02,
    )
    assert row["search_regret"] == pytest.approx(0.02)
    assert row["ranking_regret"] == pytest.approx(0.04)
    assert row["construction_regret"] == pytest.approx(0.0)
    assert row["search_regret"] + row["ranking_regret"] + row["construction_regret"] == pytest.approx(
        row["total_oracle_regret"]
    )


def test_forecast_metrics_use_every_ledger_candidate() -> None:
    row = model_diagnostic(
        submission(),
        {"portfolio_return": "0.03"},
        {"SP500": 0.01, "A": 0.03, "B": -0.01},
        {"SP500", "A", "B"},
        {"A"},
        0.01,
    )
    assert row["candidate_forecast_rank_ic"] is not None
    assert row["candidate_interval_coverage"] == pytest.approx(1.0)
    assert row["rejected_candidates_beating_spy"] == 0


def test_legacy_submission_reports_only_measurable_regret() -> None:
    legacy_submission = {
        "model_id": "model-a",
        "portfolio": [
            {"option_id": "A", "allocation_pct": 60},
            {"option_id": "B", "allocation_pct": 40},
        ],
    }
    row = model_diagnostic(
        legacy_submission,
        {"portfolio_return": "0.04"},
        {"SP500": 0.02, "A": 0.06, "B": 0.01, "C": 0.10},
        {"A", "B", "C"},
        {"C"},
        0.02,
    )
    assert row["candidate_ledger_available"] is False
    assert row["search_regret"] is None
    assert row["ranking_regret"] is None
    assert row["preselection_regret"] == pytest.approx(0.04)
    assert row["construction_regret"] == pytest.approx(0.02)
    assert row["preselection_regret"] + row["construction_regret"] == pytest.approx(
        row["total_oracle_regret"]
    )
    assert row["candidate_forecast_rank_ic"] is None
    assert row["candidate_interval_coverage"] is None


def test_candidate_overlap_is_average_jaccard() -> None:
    assert candidate_overlap([{"A", "B"}, {"B", "C"}]) == pytest.approx(1 / 3)
    assert candidate_overlap([{"A"}]) is None


def test_construction_rules_keep_selected_assets_and_redirect_caps_to_sp500() -> None:
    rules = construction_rules({"A": 60.0, "B": 40.0})
    assert rules["equal_selected"] == {"A": 50.0, "B": 50.0}
    assert rules["cap_50_to_sp500"] == {"A": 50.0, "B": 40.0, "SP500": 10.0}
    assert sum(rules["cap_35_to_sp500"].values()) == pytest.approx(100.0)


def test_construction_counterfactuals_compare_with_submitted_result() -> None:
    rows, summaries = construction_counterfactuals(
        [{"model_id": "model-a", "portfolio": [{"option_id": "A", "allocation_pct": 60}, {"option_id": "B", "allocation_pct": 40}]}],
        {"model-a": {"portfolio_return": "0.04"}},
        {"SP500": 0.02, "A": 0.06, "B": 0.01},
    )
    equal = next(row for row in rows if row["rule"] == "equal_selected")
    assert equal["counterfactual_return"] == pytest.approx(0.035)
    assert equal["improvement_vs_submitted"] == pytest.approx(-0.005)
    assert len(summaries) == 3


def test_yahoo_rows_are_built_for_both_dates(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_fetch(symbol: str, start: date, end: date) -> list[dict]:
        assert symbol == "AAA"
        return [
            {"date": start.isoformat(), "close": 100, "adjClose": 99},
            {"date": end.isoformat(), "close": 110, "adjClose": 109},
        ]

    monkeypatch.setattr("scripts.analyze_v2_resolution_diagnostics._fetch_yahoo_chart_adjclose", fake_fetch)
    entry, exit_rows = yahoo_rows_for_options(
        [Option("CASH"), Option("A", "AAA")],
        "2026-07-13",
        "2026-07-20",
    )
    assert entry[0]["source"] == "cash"
    assert entry[1]["adj_close"] == 99
    assert exit_rows[1]["adj_close"] == 109
    assert exit_rows[1]["source"] == "yahoo_chart_adjclose"

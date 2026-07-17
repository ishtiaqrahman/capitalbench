from __future__ import annotations

import sys
from datetime import date
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import analyze_model_predictability as base
import analyze_v2_improvements as research


def test_equal_weight_preserves_selected_set() -> None:
    result = research.equal_weight({"A": 70.0, "B": 20.0, "SP500": 10.0})

    assert result == {"A": 100.0 / 3.0, "B": 100.0 / 3.0, "SP500": 100.0 / 3.0}
    assert sum(result.values()) == 100.0


def test_active_cap_redirects_excess_to_spy() -> None:
    result = research.cap_active_holding({"OIL": 70.0, "ENERGY": 20.0, "SP500": 10.0}, 35.0)

    assert result == {"OIL": 35.0, "ENERGY": 20.0, "SP500": 45.0}
    assert sum(result.values()) == 100.0


def test_spy_blend_is_exact_portfolio_blend() -> None:
    allocation = {"OIL": 60.0, "SP500": 40.0}
    result = research.blend_with_spy(allocation, 25.0)

    assert result == {"OIL": 45.0, "SP500": 55.0}
    returns = {"OIL": 0.10, "SP500": 0.02}
    submitted = research.portfolio_return(allocation, returns)
    blended = research.portfolio_return(result, returns)
    expected = 0.75 * submitted + 0.25 * returns["SP500"]
    assert abs(blended - expected) < 1e-12


def test_allocation_turnover_and_overlap_are_consistent() -> None:
    left = {"OIL": 70.0, "SP500": 30.0}
    right = {"OIL": 20.0, "ENERGY": 50.0, "SP500": 30.0}

    assert research.allocation_turnover(left, right) == 50.0
    assert research.allocation_overlap(left, right) == 50.0


def test_failure_decomposition_identity() -> None:
    record = base.RoundRecord(
        round_id="CB-2026-01-01-1W",
        track="weekly",
        decision_date=date(2026, 1, 1),
        entry_date=date(2026, 1, 1),
        exit_date=date(2026, 1, 8),
        decision_deadline=None,
        run_id="official",
        assets=[
            {"option_id": "SP500", "future_return": 0.02, "is_cash": False},
            {"option_id": "A", "future_return": 0.10, "is_cash": False},
            {"option_id": "B", "future_return": -0.02, "is_cash": False},
        ],
        models=[
            base.ModelRecord(
                model_id="model",
                allocation={"SP500": 50.0, "B": 50.0},
                text="",
                portfolio_return=0.0,
                alpha_vs_sp500=-0.02,
            )
        ],
        sp500_return=0.02,
        oracle_return=0.10,
        winner_ids=("A",),
    )

    rows, summary = research.analyze_historical_failures([record])

    assert len(rows) == 1
    row = rows[0]
    assert abs(row["portfolio_return"] - 0.0) < 1e-12
    assert abs(row["search_regret"] - 0.08) < 1e-12
    assert abs(row["sizing_regret"] - 0.02) < 1e-12
    assert row["regret_identity_error"] < 1e-12
    assert abs(summary[0]["search_share_of_regret"] - 0.8) < 1e-12


def test_portfolio_rule_set_is_frozen() -> None:
    rules = research.portfolio_rule_allocations({"A": 100.0})

    assert set(rules) == {
        "submitted",
        "equal_selected",
        "cap_active_50_to_spy",
        "cap_active_35_to_spy",
        "spy_reserve_25",
        "spy_reserve_50",
    }
    assert rules["cap_active_35_to_spy"] == {"A": 35.0, "SP500": 65.0}

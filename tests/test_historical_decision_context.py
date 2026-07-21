from __future__ import annotations

from datetime import date, timedelta

from scripts.analyze_historical_decision_context import (
    add_ranks,
    feature_row,
    nonoverlap,
    selection_probabilities,
    signal_score,
)


def history(start: date, count: int, daily_gain: float, volume: float = 100.0):
    price = 100.0
    rows = []
    for index in range(count):
        price *= 1.0 + daily_gain + (0.0004 if index % 2 else -0.0003)
        rows.append({"date": (start + timedelta(days=index)).isoformat(), "adj_close": price, "volume": volume + index})
    return rows


def config():
    return {
        "weekly_metrics": {
            "recent_sessions": 5,
            "prior_sessions": 16,
            "volatility_sessions": 21,
            "correlation_sessions": 20,
            "volume_recent_sessions": 5,
            "volume_baseline_sessions": 20,
        },
        "monthly_metrics": {
            "recent_sessions": 21,
            "prior_sessions": 40,
            "volatility_sessions": 30,
            "correlation_sessions": 40,
            "volume_recent_sessions": 10,
            "volume_baseline_sessions": 20,
        },
    }


def test_feature_row_ignores_prices_after_entry_date():
    start = date(2025, 1, 1)
    asset_history = history(start, 100, 0.002)
    spy_history = history(start, 100, 0.001)
    entry = start + timedelta(days=79)
    asset = {
        "round_id": "R1",
        "track": "weekly",
        "split": "discovery",
        "entry_date": entry.isoformat(),
        "exit_date": (entry + timedelta(days=7)).isoformat(),
        "option_id": "TEST",
        "symbol": "TEST",
        "future_return": "0.02",
    }
    before = feature_row(asset, asset_history, spy_history, config())
    asset_history[-1]["adj_close"] *= 100
    after = feature_row(asset, asset_history, spy_history, config())
    assert before == after
    assert before is not None
    assert before["recent_active_return"] > 0


def test_fractional_selection_probability_preserves_count():
    probabilities = selection_probabilities([3.0, 2.0, 2.0, 1.0], 2)
    assert probabilities == [1.0, 0.5, 0.5, 0.0]
    assert sum(probabilities) == 2.0


def test_signal_score_uses_frozen_component_weights():
    rows = [
        {"recent_active_return": 1.0, "prior_active_return": 1.0, "volatility": 1.0, "max_drawdown": -0.2, "volume_zscore": 0.0, "beta_spy": 1.2},
        {"recent_active_return": 2.0, "prior_active_return": 0.0, "volatility": 0.5, "max_drawdown": -0.1, "volume_zscore": 1.0, "beta_spy": 0.8},
    ]
    add_ranks(rows)
    score = signal_score(rows[1], {"recent_active_rank": 0.4, "prior_active_rank": 0.6})
    assert score == 0.4


def test_nonoverlap_keeps_first_available_window():
    rows = [
        {"round_id": "A", "entry_date": "2026-01-01", "exit_date": "2026-01-08"},
        {"round_id": "B", "entry_date": "2026-01-04", "exit_date": "2026-01-11"},
        {"round_id": "C", "entry_date": "2026-01-08", "exit_date": "2026-01-15"},
    ]
    assert [row["round_id"] for row in nonoverlap(rows)] == ["A", "C"]

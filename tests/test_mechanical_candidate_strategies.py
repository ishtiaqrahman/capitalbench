from __future__ import annotations

from datetime import date

import pytest

from scripts.analyze_mechanical_candidate_strategies import (
    advancement_rows,
    classify_regime,
    maximal_non_overlapping,
    path_quality,
    weighted_rank,
)
from scripts.analyze_model_predictability import RoundRecord


def make_round(round_id: str, entry: date, exit_date: date, spy_return_30d: float, breadth: list[float]) -> RoundRecord:
    assets = [
        {
            "option_id": "SP500",
            "is_cash": False,
            "is_benchmark": True,
            "return_30d": spy_return_30d,
        }
    ]
    assets.extend(
        {
            "option_id": f"A{index}",
            "is_cash": False,
            "is_benchmark": False,
            "return_30d": value,
        }
        for index, value in enumerate(breadth)
    )
    return RoundRecord(
        round_id=round_id,
        track="weekly",
        decision_date=entry,
        entry_date=entry,
        exit_date=exit_date,
        decision_deadline=None,
        run_id="official",
        assets=assets,
        models=[],
        sp500_return=0.0,
        oracle_return=0.0,
        winner_ids=("A0",),
    )


def config() -> dict:
    return {
        "minimum_non_overlapping_rounds": 6,
        "minimum_mean_top5_alpha": 0.005,
        "minimum_sp500_beat_rate": 0.6,
        "strategies": {
            "regime_router": {"positive_breadth_threshold": 0.5},
        },
    }


def test_weighted_rank_and_reversal() -> None:
    asset = {"rank_return_7d": 0.8, "rank_return_30d": 0.2}
    weights = {"return_7d": 0.75, "return_30d": 0.25}
    assert weighted_rank(asset, weights) == pytest.approx(0.65)
    assert weighted_rank(asset, weights, reverse=True) == pytest.approx(0.35)


def test_path_quality_rewards_low_volatility_and_orderly_path() -> None:
    asset = {
        "rank_volatility_30d": 0.1,
        "rank_max_drawdown_30d": 0.8,
        "rank_up_day_share_30d": 0.7,
        "rank_distance_from_52w_high": 0.6,
        "rank_distance_from_52w_low": 0.9,
    }
    assert path_quality(asset) == pytest.approx(0.78)
    assert path_quality({**asset, "rank_volatility_30d": None}) is None


@pytest.mark.parametrize(
    ("spy", "breadth", "expected"),
    [
        (0.02, [0.01, 0.03, -0.01, 0.02], "bullish"),
        (-0.02, [-0.01, -0.03, 0.01, -0.02], "bearish"),
        (0.02, [-0.01, -0.03, 0.01, -0.02], "mixed"),
    ],
)
def test_regime_classification(spy: float, breadth: list[float], expected: str) -> None:
    round_record = make_round("R", date(2026, 1, 1), date(2026, 1, 8), spy, breadth)
    assert classify_regime(round_record, config()) == expected


def test_non_overlapping_sequence_is_chronological_and_deterministic() -> None:
    rounds = [
        make_round("R1", date(2026, 1, 1), date(2026, 1, 8), 0.0, [0.0] * 4),
        make_round("R2", date(2026, 1, 2), date(2026, 1, 9), 0.0, [0.0] * 4),
        make_round("R3", date(2026, 1, 9), date(2026, 1, 16), 0.0, [0.0] * 4),
    ]
    assert maximal_non_overlapping(rounds) == {"R1", "R3"}


def test_advancement_requires_every_gate() -> None:
    scopes = {
        "non_overlapping": {"rounds": 6, "mean_top5_alpha": 0.006, "sp500_beat_rate": 2 / 3},
        "non_overlapping_discovery": {"rounds": 4, "mean_top5_alpha": 0.004, "sp500_beat_rate": 0.75},
        "non_overlapping_holdout": {"rounds": 2, "mean_top5_alpha": 0.002, "sp500_beat_rate": 0.5},
    }
    aggregates = [
        {"track": track, "strategy": strategy, "scope": scope, **values}
        for track in ("weekly", "monthly")
        for strategy in ("continuation", "reversal", "quality_pullback", "regime_router")
        for scope, values in scopes.items()
    ]
    decisions = advancement_rows(aggregates, {
        **config(),
        "strategies": {name: {} for name in ("continuation", "reversal", "quality_pullback", "regime_router")},
    })
    assert all(row["eligible_for_model_shadow"] for row in decisions)
    aggregates[0]["mean_top5_alpha"] = 0.004
    decisions = advancement_rows(aggregates, {
        **config(),
        "strategies": {name: {} for name in ("continuation", "reversal", "quality_pullback", "regime_router")},
    })
    weekly_continuation = next(
        row for row in decisions if row["track"] == "weekly" and row["strategy"] == "continuation"
    )
    assert not weekly_continuation["eligible_for_model_shadow"]
    assert "alpha_below_threshold" in weekly_continuation["reasons"]

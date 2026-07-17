from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from scripts.analyze_model_predictability import (
    RoundRecord,
    eligibility,
    evaluate_scores,
    fit_ridge,
    mention_count,
    percentile_ranks,
    predict_ridge,
    purged_training_rounds,
    selection_probabilities,
)


def make_round(
    round_id: str,
    decision_date: date,
    entry_date: date,
    exit_date: date,
    assets: list[dict] | None = None,
) -> RoundRecord:
    rows = assets or []
    risky = [row for row in rows if not row.get("is_cash")]
    oracle = max((float(row["future_return"]) for row in risky), default=0.0)
    winners = tuple(row["option_id"] for row in risky if float(row["future_return"]) == oracle)
    return RoundRecord(
        round_id=round_id,
        track="weekly",
        decision_date=decision_date,
        entry_date=entry_date,
        exit_date=exit_date,
        decision_deadline=None,
        run_id="official",
        assets=rows,
        models=[],
        sp500_return=0.02,
        oracle_return=oracle,
        winner_ids=winners,
    )


def test_percentile_ranks_average_ties_and_preserve_missing() -> None:
    assert percentile_ranks([1.0, 2.0, 2.0, None]) == [0.0, 0.75, 0.75, None]


def test_selection_probabilities_do_not_break_ties_by_option_order() -> None:
    assert selection_probabilities([1.0, 1.0, 0.0], 1) == [0.5, 0.5, 0.0]
    assert selection_probabilities([1.0, 1.0, 0.0], 2) == [1.0, 1.0, 0.0]


def test_evaluate_scores_uses_fractional_tie_outcomes() -> None:
    assets = [
        {"option_id": "A", "is_cash": False, "future_return": 0.10},
        {"option_id": "SP500", "is_cash": False, "future_return": 0.05},
        {"option_id": "C", "is_cash": False, "future_return": -0.02},
        {"option_id": "CASH", "is_cash": True, "future_return": 0.0},
    ]
    round_record = make_round(
        "CB-2026-01-01-1W",
        date(2026, 1, 1),
        date(2026, 1, 1),
        date(2026, 1, 8),
        assets,
    )
    round_record.sp500_return = 0.05
    result = evaluate_scores(
        round_record,
        "tied",
        "test",
        {"A": 1.0, "SP500": 1.0, "C": 0.0},
    )
    assert result is not None
    assert result["exact_winner_hit"] == pytest.approx(0.5)
    assert result["top1_return"] == pytest.approx(0.075)
    assert result["top3_capture"] == pytest.approx(1.0)


def test_purged_training_excludes_rounds_whose_outcomes_overlap_test_entry() -> None:
    completed = make_round(
        "CB-2026-01-01-1W",
        date(2026, 1, 1),
        date(2026, 1, 1),
        date(2026, 1, 8),
    )
    overlapping = make_round(
        "CB-2026-01-05-1W",
        date(2026, 1, 5),
        date(2026, 1, 5),
        date(2026, 1, 12),
    )
    test_round = make_round(
        "CB-2026-01-10-1W",
        date(2026, 1, 10),
        date(2026, 1, 10),
        date(2026, 1, 17),
    )
    assert purged_training_rounds([completed, overlapping], test_round) == [completed]


def test_ridge_learns_positive_rank_relationship() -> None:
    assets = [
        {
            "option_id": "LOW",
            "is_cash": False,
            "future_return": -0.02,
            "rank_future_return": 0.0,
            "rank_return_7d": 0.0,
        },
        {
            "option_id": "MID",
            "is_cash": False,
            "future_return": 0.01,
            "rank_future_return": 0.5,
            "rank_return_7d": 0.5,
        },
        {
            "option_id": "HIGH",
            "is_cash": False,
            "future_return": 0.05,
            "rank_future_return": 1.0,
            "rank_return_7d": 1.0,
        },
    ]
    round_record = make_round(
        "CB-2026-01-01-1W",
        date(2026, 1, 1),
        date(2026, 1, 1),
        date(2026, 1, 8),
        assets,
    )
    model = fit_ridge([round_record])
    assert predict_ridge(model, assets[2]) > predict_ridge(model, assets[0])


def test_mentions_require_distinctive_aliases() -> None:
    option = {"id": "SEMICONDUCTORS", "name": "Semiconductors", "symbol": "SMH"}
    assert mention_count("SMH rose as semiconductor demand improved.", option) == 1
    assert mention_count("Broad equities rose.", option) == 0


def test_v2_round_id_is_ineligible_before_file_checks(tmp_path: Path) -> None:
    round_dir = tmp_path / "CB-2026-07-13-V2-1W"
    round_dir.mkdir()
    run, row = eligibility(round_dir)
    assert run is None
    assert row["reason"] == "non_v1_round_id"

from pathlib import Path

import pytest

from capitalbench.portfolio_v3 import (
    build_portfolio_v3_allocation,
    build_portfolio_v3_candidate_slate,
    materialize_portfolio_v3_submission,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _assessment(option_id: str, rank: int, interpretation: str, probability: float) -> dict:
    return {
        "option_id": option_id,
        "rank": rank,
        "recent_return_interpretation": interpretation,
        "p_beat_spy_pct": probability,
    }


def test_v3_selects_confident_overreactions_in_model_rank_order() -> None:
    result = build_portfolio_v3_allocation(
        [
            _assessment("CONTINUATION", 1, "supported_continuation", 90),
            _assessment("OVERREACTION_B", 3, "overreaction", 70),
            _assessment("OVERREACTION_A", 2, "overreaction", 55),
            _assessment("LOW_CONFIDENCE", 4, "overreaction", 54.9),
        ]
    )

    assert result["selected_active_option_ids"] == ["OVERREACTION_A", "OVERREACTION_B"]
    assert result["allocation_pct"] == {
        "OVERREACTION_A": 35.0,
        "OVERREACTION_B": 35.0,
        "SP500": 30.0,
    }


def test_v3_uses_spy_for_every_unused_slot() -> None:
    result = build_portfolio_v3_allocation(
        [
            _assessment("CONTINUATION", 1, "supported_continuation", 90),
            _assessment("NO_EDGE", 2, "no_edge", 80),
            _assessment("SP500", 3, "overreaction", 99),
        ]
    )

    assert result["selected_active_option_ids"] == []
    assert result["allocation_pct"] == {"SP500": 100.0}


def test_v3_limits_active_positions_to_available_slots() -> None:
    result = build_portfolio_v3_allocation(
        [_assessment(f"OPTION_{index}", index, "overreaction", 60) for index in range(1, 5)]
    )

    assert result["selected_active_option_ids"] == ["OPTION_1", "OPTION_2", "OPTION_3"]
    fourth = next(row for row in result["decisions"] if row["option_id"] == "OPTION_4")
    assert fourth["eligible"] is True
    assert fourth["selected"] is False
    assert fourth["reason"] == "outside_available_slots"


@pytest.mark.parametrize(
    "assessments, message",
    [
        (
            [
                _assessment("A", 1, "overreaction", 60),
                _assessment("A", 2, "overreaction", 70),
            ],
            "option_id",
        ),
        (
            [
                _assessment("A", 1, "overreaction", 60),
                _assessment("B", 1, "overreaction", 70),
            ],
            "rank",
        ),
    ],
)
def test_v3_rejects_ambiguous_assessments(assessments: list[dict], message: str) -> None:
    with pytest.raises(ValueError, match=message):
        build_portfolio_v3_allocation(assessments)


def test_v3_rejects_invalid_slot_weights() -> None:
    with pytest.raises(ValueError, match="sum to 100"):
        build_portfolio_v3_allocation(
            [_assessment("A", 1, "overreaction", 60)],
            slot_weights_pct=(40, 40, 10),
        )


def test_v3_candidate_slate_is_deterministic_and_includes_spy() -> None:
    round_path = PROJECT_ROOT / "rounds" / "CB-2026-08-04-1W"

    first = build_portfolio_v3_candidate_slate(round_path)
    second = build_portfolio_v3_candidate_slate(round_path)

    assert first == second
    assert 10 <= len(first) <= 16
    assert first[-1]["option_id"] == "SP500"
    assert first[-1]["origin_lanes"] == ["benchmark"]


def test_v3_candidate_slate_supports_monthly_context() -> None:
    round_path = PROJECT_ROOT / "rounds" / "CB-2026-08-05-1M"

    slate = build_portfolio_v3_candidate_slate(round_path)

    assert 10 <= len(slate) <= 16
    assert {row["metric_profile"] for row in slate} == {"monthly"}
    assert slate[-1]["option_id"] == "SP500"


def test_v3_materializes_model_judgment_into_scored_portfolio() -> None:
    slate = [
        {"option_id": "A", "origin_lanes": ["shock_reversal"]},
        {"option_id": "B", "origin_lanes": ["medium_strength"]},
        {"option_id": "C", "origin_lanes": ["short_continuation"]},
        {"option_id": "SP500", "origin_lanes": ["benchmark"]},
    ]
    assessments = []
    for rank, row in enumerate(slate, start=1):
        assessments.append(
            {
                "option_id": row["option_id"],
                "origin_lanes": row["origin_lanes"],
                "mechanism": "reversal" if row["option_id"] in {"A", "B"} else "no_edge",
                "p_beat_spy_pct": 60 if row["option_id"] in {"A", "B"} else 50,
                "p_top3_pct": 25,
                "excess_return_p10_pct": -1.0,
                "excess_return_p50_pct": 1.0,
                "excess_return_p90_pct": 3.0,
                "recent_return_interpretation": (
                    "overreaction" if row["option_id"] in {"A", "B"} else "no_edge"
                ),
                "evidence": ["Frozen input evidence."],
                "rank": rank,
            }
        )
    payload = {
        "round_id": "CB-V3-TEST",
        "model_id": "google-test",
        "provider": "google",
        "mode": "closed_capability",
        "dispersion_state": "normal",
        "dominant_pattern": "mixed",
        "market_rationale": "Mixed conditions.",
        "candidate_assessments": assessments,
        "top3_option_ids": ["A", "B", "C"],
        "prefer_spy": False,
        "portfolio_rationale": "A and B pass the frozen V3 rule.",
        "key_risks": ["Reversal does not occur.", "SPY accelerates."],
    }

    result = materialize_portfolio_v3_submission(
        payload,
        round_id="CB-V3-TEST",
        model_id="google-test",
        provider="google",
        mode="closed_capability",
        candidate_slate=slate,
        allowed_option_ids=["A", "B", "C", "SP500", "CASH"],
    )

    assert [(row["option_id"], row["allocation_pct"]) for row in result["portfolio"]] == [
        ("A", 35),
        ("B", 35),
        ("SP500", 30),
    ]
    assert result["metadata"]["portfolio_v3"]["candidate_assessments"] == assessments

    invalid = {**payload, "prefer_spy": "false"}
    with pytest.raises(ValueError, match="prefer_spy must be a boolean"):
        materialize_portfolio_v3_submission(
            invalid,
            round_id="CB-V3-TEST",
            model_id="google-test",
            provider="google",
            mode="closed_capability",
            candidate_slate=slate,
            allowed_option_ids=["A", "B", "C", "SP500", "CASH"],
        )

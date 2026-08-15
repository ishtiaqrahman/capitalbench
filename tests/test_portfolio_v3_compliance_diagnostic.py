from scripts.analyze_portfolio_v3_compliance import eligible_assessments


def _row(rank: int, interpretation: str, probability: float) -> dict:
    return {
        "option_id": f"OPTION_{rank}",
        "rank": rank,
        "recent_return_interpretation": interpretation,
        "p_beat_spy_pct": probability,
    }


def test_gate_requires_overreaction_and_confidence_margin() -> None:
    rows = [
        _row(1, "supported_continuation", 80),
        _row(2, "no_edge", 70),
        _row(3, "overreaction", 55),
        _row(4, "overreaction", 54.9),
    ]

    eligible = eligible_assessments(rows)

    assert [row["option_id"] for row in eligible] == ["OPTION_3"]


def test_gate_preserves_model_rank_among_eligible_candidates() -> None:
    rows = [
        _row(4, "overreaction", 70),
        _row(1, "supported_continuation", 90),
        _row(3, "overreaction", 60),
        _row(2, "no_edge", 80),
    ]

    eligible = eligible_assessments(rows)

    assert [row["rank"] for row in eligible] == [3, 4]

from scripts.analyze_model_quality_hybrids import (
    nonoverlap_round_ids,
    normalize,
    quality_sleeve,
    union_rerank,
    within_holdings_tilt,
)


def test_quality_sleeve_preserves_frozen_weights():
    allocation = quality_sleeve(
        {"A": 100.0},
        {"B": 50.0, "C": 50.0},
        original_weight=0.75,
        quality_weight=0.25,
    )
    assert allocation == {"A": 75.0, "B": 12.5, "C": 12.5}


def test_union_rerank_selects_five_and_normalizes():
    allocation = union_rerank(
        {"A": 100.0},
        {"B": 20.0, "C": 20.0, "D": 20.0, "E": 20.0, "F": 20.0},
        {"A": 0.1, "B": 1.0, "C": 0.9, "D": 0.8, "E": 0.7, "F": 0.6},
        model_weight=0.5,
        quality_weight=0.5,
        count=5,
    )
    assert len(allocation) == 5
    assert sum(allocation.values()) == 100.0
    assert "B" in allocation


def test_within_holdings_tilt_cannot_add_candidates():
    allocation = within_holdings_tilt(
        {"A": 50.0, "B": 50.0},
        {"A": 1.0, "B": 0.0, "C": 1.0},
        minimum_multiplier=0.5,
        quality_multiplier=1.0,
        cash_multiplier=1.0,
    )
    assert set(allocation) == {"A", "B"}
    assert allocation["A"] == 75.0
    assert allocation["B"] == 25.0


def test_nonoverlap_round_ids_clusters_by_round():
    rows = [
        {"round_id": "A", "entry_date": "2026-01-01", "exit_date": "2026-01-08"},
        {"round_id": "A", "entry_date": "2026-01-01", "exit_date": "2026-01-08"},
        {"round_id": "B", "entry_date": "2026-01-04", "exit_date": "2026-01-11"},
        {"round_id": "C", "entry_date": "2026-01-08", "exit_date": "2026-01-15"},
    ]
    assert nonoverlap_round_ids(rows) == ["A", "C"]


def test_normalize_drops_zero_weights():
    assert normalize({"A": 2.0, "B": 0.0}) == {"A": 100.0}

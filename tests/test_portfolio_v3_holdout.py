from scripts.run_portfolio_v3_holdout import aggregate


def _config() -> dict:
    return {
        "models": ["m1", "m2", "m3", "m4"],
        "episodes": [{"replay_id": "p1"}, {"replay_id": "p2"}, {"replay_id": "p3"}],
        "gate": {
            "minimum_valid_pairs": 10,
            "minimum_mean_treatment_alpha_pct": 0.0,
            "minimum_mean_paired_improvement_pct": 1.0,
            "minimum_nonnegative_alpha_cells": 8,
            "minimum_positive_models": 3,
            "minimum_positive_periods": 2,
            "minimum_worst_period_alpha_pct": -0.5,
            "minimum_selected_top3_capture_change": 0,
        },
    }


def _row(model: str, period: str, alpha: float, improvement: float) -> dict:
    return {
        "model_id": model,
        "replay_id": period,
        "valid": True,
        "treatment_return_pct": alpha + 1.0,
        "treatment_alpha_pct": alpha,
        "control_return_pct": alpha + 1.0 - improvement,
        "control_alpha_pct": alpha - improvement,
        "paired_improvement_pct": improvement,
        "treatment_top3_capture": True,
        "control_top3_capture": False,
        "active_slots": 1,
    }


def test_holdout_gate_passes_only_when_every_frozen_check_passes() -> None:
    rows = [
        _row(model, period, 1.0, 1.2)
        for model in _config()["models"]
        for period in ("p1", "p2", "p3")
    ]
    result = aggregate(_config(), rows)
    assert result["passes_gate"] is True
    assert all(result["gate_checks"].values())


def test_holdout_gate_rejects_positive_alpha_without_v2_improvement() -> None:
    rows = [
        _row(model, period, 1.0, 0.2)
        for model in _config()["models"]
        for period in ("p1", "p2", "p3")
    ]
    result = aggregate(_config(), rows)
    assert result["gate_checks"]["positive_treatment_alpha"] is True
    assert result["gate_checks"]["paired_improvement"] is False
    assert result["passes_gate"] is False

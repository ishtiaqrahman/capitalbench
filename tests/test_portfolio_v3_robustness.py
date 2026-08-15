import pytest

from scripts.analyze_portfolio_v3_robustness import summarize_rows


def _row(period: str, model: str, alpha: float) -> dict:
    return {
        "replay_id": period,
        "model_id": model,
        "alpha_pct": alpha,
        "paired_improvement_pct": alpha + 1.0,
        "active_positions": int(alpha != 0),
        "top3_capture": alpha > 1,
    }


def test_summary_reports_breadth_and_removal_robustness() -> None:
    rows = [
        _row("P1", "M1", 1.0),
        _row("P1", "M2", 0.0),
        _row("P2", "M1", 2.0),
        _row("P2", "M2", -0.5),
    ]

    summary = summarize_rows(rows)

    assert summary["mean_alpha_pct"] == pytest.approx(0.625)
    assert summary["spy_beats"] == 2
    assert summary["nonnegative_alpha_cells"] == 3
    assert summary["positive_models"] == 1
    assert summary["positive_periods"] == 2
    assert summary["worst_period_alpha_pct"] == pytest.approx(0.5)
    assert min(summary["leave_one_model_out_alpha_pct"].values()) == pytest.approx(-0.25)
    assert min(summary["leave_one_period_out_alpha_pct"].values()) == pytest.approx(0.5)
    assert summary["minimum_leave_one_cell_out_alpha_pct"] == pytest.approx(1 / 6)

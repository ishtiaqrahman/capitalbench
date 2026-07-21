from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_vnext_historical_replay_stage1c.py"
SPEC = importlib.util.spec_from_file_location("vnext_replay_stage1c", SCRIPT)
assert SPEC and SPEC.loader
stage1c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stage1c)


def _config() -> dict:
    return stage1c.load_config(stage1c.DEFAULT_CONFIG)


def _episode(replay_id: str = "D1") -> dict:
    return next(item for item in _config()["episodes"] if item["replay_id"] == replay_id)


def _top5(ids: list[str]) -> list[dict]:
    roles = ["continuation", "quality_pullback", "capitulation_rebound", "free", "free"]
    return [
        {
            "rank": index + 1,
            "option_id": option_id,
            "forecast_return_pct": 1.5 - index * 0.1,
            "expected_alpha_vs_spy_pct": 1.0 - index * 0.1,
            "signal_type": "mixed",
            "evidence": "Frozen entry-time evidence.",
            "invalidation": "The entry-time signal reverses.",
            "selection_role": roles[index],
        }
        for index, option_id in enumerate(ids[:5])
    ]


def _assessments(ids: list[str]) -> list[dict]:
    ranking = ["continuation", "quality_pullback", "capitulation_rebound"] + ["other"] * 7
    return [
        {
            "option_id": option_id,
            "ranking_lane": ranking[index],
            "probability_beats_spy_pct": 60 - index,
            "probability_top_decile_pct": 30 - index,
            "downside_probability_pct": 20 + index,
            "assessment": "Entry-time probability assessment.",
        }
        for index, option_id in enumerate(ids)
    ]


def test_stage_call_counts_are_gated() -> None:
    config = _config()
    assert len(stage1c.diagnostic_calls(config)) == 12
    assert len(stage1c.integrated_calls(config)) == 12
    assert len(stage1c.confirmation_calls(config)) == 24


def test_diagnostic_payload_preserves_frozen_h4_shortlist() -> None:
    config = _config()
    episode = _episode()
    record = stage1c._load_prior_record(config, "D1", config["models"][0], "H4")
    shortlist = stage1c._h4_shortlist(record)
    ids = [item["option_id"] for item in shortlist]
    payload = {
        "replay_id": "D1",
        "treatment_id": "R1",
        "spy_forecast_return_pct": 0.5,
        "prefer_spy": False,
        "shortlist": shortlist,
        "candidate_assessments": _assessments(ids),
        "top5": _top5(ids),
    }
    assert stage1c.validate_payload(config, payload, episode, config["models"][0], "R1") == []


def test_changed_diagnostic_shortlist_is_rejected() -> None:
    config = _config()
    episode = _episode()
    model_id = config["models"][0]
    shortlist = stage1c._h4_shortlist(stage1c._load_prior_record(config, "D1", model_id, "H4"))
    ids = [item["option_id"] for item in shortlist]
    shortlist[0]["candidate_lane"] = "wildcard" if shortlist[0]["candidate_lane"] != "wildcard" else "context"
    payload = {
        "replay_id": "D1",
        "treatment_id": "R1",
        "spy_forecast_return_pct": 0.5,
        "prefer_spy": False,
        "shortlist": shortlist,
        "candidate_assessments": _assessments(ids),
        "top5": _top5(ids),
    }
    errors = stage1c.validate_payload(config, payload, episode, model_id, "R1")
    assert "diagnostic shortlist or H4 lane labels changed" in errors


def test_gate_requires_final_five_capture_and_broad_alpha() -> None:
    config = _config()
    pairs = []
    for model_index in range(4):
        for episode_index in range(3):
            pairs.append(
                {
                    "replay_id": f"D{episode_index + 1}",
                    "model_id": f"m{model_index}",
                    "pair_valid": True,
                    "control_top5_top2": 0,
                    "challenger_top5_top2": 1,
                    "challenger_shortlist_top2": 1,
                    "alpha_improvement": 0.01,
                }
            )
    gate = stage1c._gate(config, pairs)
    assert gate["passes_gate"] is True
    assert gate["challenger_top5_top2_captures"] == 12


def test_integrated_gate_requires_candidate_recall_floor() -> None:
    config = _config()
    pairs = []
    for model_index in range(4):
        for episode_index in range(3):
            pairs.append(
                {
                    "replay_id": f"D{episode_index + 1}",
                    "model_id": f"m{model_index}",
                    "pair_valid": True,
                    "control_top5_top2": 0,
                    "challenger_top5_top2": 1,
                    "challenger_shortlist_top2": 0,
                    "alpha_improvement": 0.01,
                }
            )
    gate = stage1c._gate(config, pairs, integrated=True)
    assert gate["passes_gate"] is False

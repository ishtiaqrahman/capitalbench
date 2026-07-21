from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_vnext_symmetric_coverage_replay.py"
SPEC = importlib.util.spec_from_file_location("vnext_symmetric_coverage", SCRIPT)
assert SPEC and SPEC.loader
replay = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replay)


def episode() -> dict[str, str]:
    return {
        "replay_id": "V1",
        "round_id": "CB-2026-06-17-1W",
        "event_register": "research/event_registers/CB-2026-06-17-1W.yaml",
    }


def valid_payload() -> dict:
    lanes = replay.option_lane_map(episode())
    events = replay.mapped_events(episode())
    selected: list[tuple[str, str]] = [("SP500", "benchmark")]
    for lane in replay.FIXED_LANES:
        lane_options = [option for option, assigned in lanes.items() if assigned == lane]
        option_id = next((option for option in lane_options if events[option]), lane_options[0])
        selected.append((option_id, lane))
    wildcard = next(
        option for option, assigned in lanes.items()
        if assigned != "benchmark" and option not in {value for value, _lane in selected} and events[option]
    )
    selected.append((wildcard, "wildcard"))
    shortlist = []
    for option_id, lane in selected:
        ids = events[option_id]
        shortlist.append(
            {
                "option_id": option_id,
                "search_lane": lane,
                "event_ids": ids[:1],
                "evidence_strength": "moderate" if ids else "none",
                "timing_fit": "inside_window" if ids else "no_direct_event",
                "forecast_return_pct": 1.0,
                "expected_alpha_vs_spy_pct": 0.5,
                "evidence_summary": "Mapped factual event." if ids else "No mapped event.",
            }
        )
    top5_ids = [
        row["option_id"]
        for row in shortlist
        if row["option_id"] != "SP500" and row["event_ids"]
    ][:5]
    assert len(top5_ids) == 5
    return {
        "replay_id": "V1",
        "treatment_id": "H9",
        "spy_forecast_return_pct": 0.5,
        "prefer_spy": False,
        "abstention_reason": "",
        "shortlist": shortlist,
        "top5": [
            {
                "rank": index,
                "option_id": option_id,
                "forecast_return_pct": 1.0,
                "expected_alpha_vs_spy_pct": 0.5,
                "evidence": "Mapped factual event.",
                "invalidation": "Event does not support the exposure.",
            }
            for index, option_id in enumerate(top5_ids, start=1)
        ],
    }


def test_lane_map_covers_every_non_cash_option_once() -> None:
    lanes = replay.option_lane_map(episode())
    assert lanes["SP500"] == "benchmark"
    assert "CASH" not in lanes
    assert set(lanes.values()) == {"benchmark", *replay.FIXED_LANES}


def test_option_evidence_table_marks_unmapped_options() -> None:
    table = replay.option_evidence_table(episode())
    assert "| SP500 | benchmark |" in table
    assert "none" in table


def test_valid_payload_passes_local_validation() -> None:
    assert replay.validate_payload(valid_payload(), episode()) == []


def test_active_finalist_without_event_fails_gate() -> None:
    payload = valid_payload()
    option_id = payload["top5"][0]["option_id"]
    row = next(item for item in payload["shortlist"] if item["option_id"] == option_id)
    row["event_ids"] = []
    row["evidence_strength"] = "none"
    row["timing_fit"] = "no_direct_event"
    errors = replay.validate_payload(payload, episode())
    assert any("failed independent-evidence gate" in error for error in errors)


def test_gate_requires_every_frozen_condition() -> None:
    gate = {
        "minimum_valid_pairs": 2,
        "minimum_mean_effective_return_improvement": 0.005,
        "require_positive_treatment_alpha": True,
        "minimum_positive_pairs": 2,
        "minimum_positive_models": 2,
        "minimum_positive_episodes": 2,
        "minimum_relative_shortlist_regret_reduction": 0.20,
        "require_nonnegative_top3_capture_change": True,
        "minimum_worst_episode_alpha_change": 0.0,
    }
    pairs = [
        {
            "pair_valid": True,
            "replay_id": "V1",
            "model_id": "M1",
            "effective_return_improvement": 0.01,
            "challenger_effective_alpha": 0.01,
            "control_regret": 0.10,
            "challenger_regret": 0.05,
            "top3_capture_change": 0,
            "challenger_abstained": False,
        },
        {
            "pair_valid": True,
            "replay_id": "V2",
            "model_id": "M2",
            "effective_return_improvement": 0.01,
            "challenger_effective_alpha": 0.01,
            "control_regret": 0.10,
            "challenger_regret": 0.05,
            "top3_capture_change": 1,
            "challenger_abstained": False,
        },
    ]
    assert replay.evaluate_gate(pairs, gate)["passes_gate"] is True
    pairs[1]["effective_return_improvement"] = -0.01
    assert replay.evaluate_gate(pairs, gate)["passes_gate"] is False

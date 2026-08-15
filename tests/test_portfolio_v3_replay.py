from __future__ import annotations

from copy import deepcopy

from scripts.run_portfolio_v3_replay import (
    DEFAULT_CONFIG,
    FORBIDDEN_PACKET_MARKERS,
    build_prompt,
    candidate_slate,
    load_config,
    planned_calls,
    aggregate,
    validate_episode_dates,
    validate_payload,
)


def config_and_episode():
    config = load_config(DEFAULT_CONFIG)
    return config, config["episodes"][0]


def valid_payload(config, episode):
    slate = candidate_slate(config, episode)
    assessments = []
    for index, row in enumerate(slate, start=1):
        assessments.append(
            {
                "option_id": row["option_id"],
                "origin_lanes": row["lanes"],
                "mechanism": "reversal" if "shock_reversal" in row["lanes"] else "no_edge",
                "p_beat_spy_pct": 50,
                "p_top3_pct": 5,
                "excess_return_p10_pct": -2.0,
                "excess_return_p50_pct": 0.1,
                "excess_return_p90_pct": 2.0,
                "recent_return_interpretation": "no_edge",
                "evidence": ["Cutoff-safe evidence."],
                "rank": index,
            }
        )
    return {
        "replay_id": episode["replay_id"],
        "treatment_id": config["treatment_id"],
        "dispersion_state": "normal",
        "dominant_pattern": "mixed",
        "market_rationale": "Mixed entry-time evidence.",
        "candidate_assessments": assessments,
        "top3_option_ids": [row["option_id"] for row in slate[:3]],
        "prefer_spy": False,
        "portfolio_rationale": "Fixed top-three construction.",
    }


def test_v3_call_budget_and_windows_are_frozen():
    config, _episode = config_and_episode()
    assert len(config["episodes"]) == 3
    assert len(planned_calls(config)) == 12
    validate_episode_dates(config)


def test_v3_candidate_slate_is_complete_and_outcome_free():
    config, episode = config_and_episode()
    slate = candidate_slate(config, episode)
    assert 10 <= len(slate) <= 16
    assert slate[-1]["option_id"] == "SP500"
    assert slate[-1]["lanes"] == ["benchmark"]
    assert len({row["option_id"] for row in slate}) == len(slate)
    assert all("realized" not in key and "future" not in key for row in slate for key in row)


def test_v3_prompt_contains_no_outcome_markers():
    config, episode = config_and_episode()
    prompt = build_prompt(config, episode).lower()
    assert all(marker not in prompt for marker in FORBIDDEN_PACKET_MARKERS)
    assert "single-turn, non-agentic" in prompt
    assert "deterministic candidate slate" in prompt


def test_v3_payload_requires_every_slate_candidate_and_ranked_top_three():
    config, episode = config_and_episode()
    payload = valid_payload(config, episode)
    assert validate_payload(payload, config, episode) == []

    reordered_lanes = deepcopy(payload)
    multi_lane = next(
        row for row in reordered_lanes["candidate_assessments"] if len(row["origin_lanes"]) > 1
    )
    multi_lane["origin_lanes"] = list(reversed(multi_lane["origin_lanes"]))
    assert validate_payload(reordered_lanes, config, episode) == []

    missing = deepcopy(payload)
    missing["candidate_assessments"].pop(3)
    missing["candidate_assessments"] = [
        {**row, "rank": index}
        for index, row in enumerate(missing["candidate_assessments"], start=1)
    ]
    missing["top3_option_ids"] = [
        row["option_id"] for row in missing["candidate_assessments"][:3]
    ]
    assert any("missing deterministic slate candidates" in error for error in validate_payload(missing, config, episode))

    wrong_top = deepcopy(payload)
    wrong_top["top3_option_ids"] = list(reversed(wrong_top["top3_option_ids"]))
    assert "top3_option_ids must equal candidate ranks 1-3" in validate_payload(wrong_top, config, episode)


def test_v3_payload_limits_wildcards_and_orders_quantiles():
    config, episode = config_and_episode()
    payload = valid_payload(config, episode)
    used = {row["option_id"] for row in payload["candidate_assessments"]}
    choices = [
        option_id
        for option_id in ("HEALTHCARE", "UTILITIES", "INDIA", "EUROPE")
        if option_id not in used
    ][:3]
    for option_id in choices:
        payload["candidate_assessments"].append(
            {
                "option_id": option_id,
                "origin_lanes": ["wildcard"],
                "mechanism": "catalyst",
                "p_beat_spy_pct": 55,
                "p_top3_pct": 8,
                "excess_return_p10_pct": -1.0,
                "excess_return_p50_pct": 0.5,
                "excess_return_p90_pct": 2.5,
                "recent_return_interpretation": "no_edge",
                "evidence": ["Specific supplied briefing evidence."],
                "rank": len(payload["candidate_assessments"]) + 1,
            }
        )
    assert "too many wildcard candidates" in validate_payload(payload, config, episode)

    quantiles = valid_payload(config, episode)
    quantiles["candidate_assessments"][0]["excess_return_p10_pct"] = 3.0
    assert any("quantiles out of order" in error for error in validate_payload(quantiles, config, episode))


def test_v3_frozen_gate_requires_positive_alpha_and_breadth():
    config, _episode = config_and_episode()
    rows = []
    for episode in config["episodes"]:
        for model_id in config["models"]:
            rows.append(
                {
                    "replay_id": episode["replay_id"],
                    "model_id": model_id,
                    "valid": True,
                    "treatment_return_pct": 2.0,
                    "treatment_alpha_pct": 1.5,
                    "control_alpha_pct": 0.0,
                    "paired_improvement_pct": 1.5,
                    "treatment_winner_capture": False,
                    "control_winner_capture": False,
                    "treatment_top3_capture": True,
                    "control_top3_capture": False,
                    "candidate_rank_spearman": 0.2,
                    "slate_winner_capture": True,
                    "slate_top3_capture_count": 1,
                }
            )
    assert aggregate(config, rows)["passes_gate"] is True
    for row in rows:
        row["treatment_alpha_pct"] = -0.1
    result = aggregate(config, rows)
    assert result["passes_gate"] is False
    assert result["gate_checks"]["positive_treatment_alpha"] is False

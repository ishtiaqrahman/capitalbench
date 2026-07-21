from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_vnext_historical_replay_stage1b.py"
SPEC = importlib.util.spec_from_file_location("vnext_replay_stage1b", SCRIPT)
assert SPEC and SPEC.loader
stage1b = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stage1b)


def _config() -> dict:
    return stage1b.load_config(stage1b.DEFAULT_CONFIG)


def _episode(replay_id: str = "D1") -> dict:
    return next(item for item in _config()["episodes"] if item["replay_id"] == replay_id)


def _active_ids(episode: dict) -> list[str]:
    return sorted(stage1b.base.allowed_active_ids(episode))


def _top5(ids: list[str], spy: float = 0.5) -> list[dict]:
    return [
        {
            "rank": index + 1,
            "option_id": option_id,
            "forecast_return_pct": 1.5 - index * 0.1,
            "expected_alpha_vs_spy_pct": 1.0 - index * 0.1,
            "signal_type": "mixed",
            "evidence": "Frozen entry-time evidence.",
            "invalidation": "The entry-time signal reverses.",
        }
        for index, option_id in enumerate(ids[:5])
    ]


def test_call_counts_reuse_controls() -> None:
    config = _config()
    assert len(stage1b.primary_calls(config)) == 24
    assert len(stage1b.fallback_calls(config)) == 12
    assert all(call["treatment"] != "H0" for call in stage1b.primary_calls(config))


def test_candidate_references_use_only_active_options() -> None:
    episode = _episode()
    active = set(_active_ids(episode))
    references = stage1b.lane_references(episode)
    assert set(references) == {"continuation", "reversal", "context", "defensive"}
    assert all(len(values) == 12 for values in references.values())
    assert all(set(values) <= active for values in references.values())


def test_h4_balanced_lane_payload_validates() -> None:
    episode = _episode()
    options = {
        str(item["id"]): item
        for item in stage1b.base.load_options(stage1b.base.source_round(episode))
        if str(item["id"]) in stage1b.base.allowed_active_ids(episode)
    }
    selected: list[str] = []
    group_counts: dict[str, int] = {}
    for option_id in sorted(options):
        group = str(options[option_id].get("option_group") or "")
        if group_counts.get(group, 0) >= 2:
            continue
        selected.append(option_id)
        group_counts[group] = group_counts.get(group, 0) + 1
        if len(selected) == 10:
            break
    lanes = ["continuation"] * 3 + ["reversal"] * 3 + ["context"] * 2 + ["defensive", "wildcard"]
    payload = {
        "replay_id": "D1",
        "treatment_id": "H4",
        "market_regime": "mixed",
        "regime_rationale": "Entry-time signals disagree.",
        "spy_forecast_return_pct": 0.5,
        "prefer_spy": False,
        "shortlist": [
            {"option_id": option_id, "candidate_lane": lane}
            for option_id, lane in zip(selected, lanes)
        ],
        "top5": _top5(selected),
    }
    assert stage1b.validate_payload(payload, episode, "H4") == []


def test_h6_requires_omitted_candidates_in_final_shortlist() -> None:
    episode = _episode()
    ids = _active_ids(episode)
    initial = ids[:10]
    omitted = ids[10:15]
    final = omitted[:2] + initial[:8]
    payload = {
        "replay_id": "D1",
        "treatment_id": "H6",
        "market_regime": "mixed",
        "regime_rationale": "Entry-time signals disagree.",
        "spy_forecast_return_pct": 0.5,
        "prefer_spy": False,
        "initial_shortlist_option_ids": initial,
        "omitted_challenge_option_ids": omitted,
        "shortlist": [{"option_id": option_id, "candidate_lane": "wildcard"} for option_id in final],
        "top5": _top5(final),
    }
    assert stage1b.validate_payload(payload, episode, "H6") == []


def test_discovery_gate_requires_broad_improvement() -> None:
    config = _config()
    rows = []
    for model_index in range(4):
        for episode_index in range(3):
            rows.append(
                {
                    "replay_id": f"D{episode_index + 1}",
                    "model_id": f"m{model_index}",
                    "challenger": "H4",
                    "pair_valid": True,
                    "control_top2_capture_count": 0,
                    "challenger_top2_capture_count": 1,
                    "control_regret": 0.10,
                    "challenger_regret": 0.05,
                    "alpha_improvement": 0.01,
                }
            )
    aggregate = stage1b._aggregate(config, rows)[0]
    assert aggregate["passes_gate"] is True
    assert aggregate["capture_episodes"] == 3
    assert aggregate["capture_models"] == 4

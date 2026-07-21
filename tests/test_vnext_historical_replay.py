from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_vnext_historical_replay.py"
SPEC = importlib.util.spec_from_file_location("vnext_replay", SCRIPT)
assert SPEC and SPEC.loader
replay = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replay)


def test_percentile_ranks_average_ties() -> None:
    assert replay.percentile_ranks([1.0, 2.0, 2.0, None]) == [0.0, 0.75, 0.75, None]


def test_sanitize_full_briefing_removes_setup_and_selected_return_table() -> None:
    text = """# Briefing
## 2. Research And Evaluation Setup
| weekly round | CB-2026-06-17-1W |
## 3. Latest Macro Datapoints
| CPI | 2.0% |
## 7. Selected Mechanical Return Context
| SPY | 3.0% |
## 8. Scheduled Events
| 2026-06-18 | Claims | BLS | scheduled |
"""
    cleaned = replay.sanitize_full_briefing(text)
    assert "Latest Macro" in cleaned
    assert "Scheduled Events" in cleaned
    assert "weekly round" not in cleaned
    assert "Selected Mechanical" not in cleaned


def test_focused_briefing_keeps_only_in_window_non_capitalbench_events() -> None:
    text = """# Briefing
## 3. Latest Macro Datapoints
| CPI | 2.0% |
## 8. Scheduled Events
| date | event | entity | status |
| --- | --- | --- | --- |
| 2026-06-18 | Claims | BLS | scheduled |
| 2026-06-24 | Weekly round exit close | CapitalBench | scheduled |
| 2026-07-01 | CPI | BLS | scheduled |
"""
    focused = replay.focused_briefing(
        text,
        replay.date(2026, 6, 17),
        replay.date(2026, 6, 24),
    )
    assert "Claims" in focused
    assert "CapitalBench" not in focused
    assert "2026-07-01" not in focused


def test_derived_market_rows_create_rank_shift_without_outcomes() -> None:
    rows = [
        {
            "option_id": "SP500",
            "symbol": "SPY",
            "option_group": "benchmark",
            "risk_bucket": "medium",
            "is_benchmark": True,
            "return_7d": 0.01,
            "return_30d": 0.02,
            "return_6m": 0.03,
            "return_1y": 0.04,
        },
        {
            "option_id": "A",
            "symbol": "AAA",
            "option_group": "sector",
            "risk_bucket": "high",
            "is_benchmark": False,
            "return_7d": 0.03,
            "return_30d": 0.01,
            "return_6m": 0.02,
            "return_1y": 0.01,
        },
    ]
    derived = replay.derived_market_rows(rows)
    asset = derived[1]
    assert asset["active_return_7d"] == pytest.approx(0.02)
    assert asset["rank_return_7d"] == 1.0
    assert asset["rank_return_30d"] == 0.0
    assert asset["recent_vs_medium_rank_shift"] == 1.0


def test_discovery_assignment_is_paired_and_balanced() -> None:
    config = replay.load_yaml(replay.DEFAULT_EXPERIMENT)
    calls = replay.discovery_calls(config)
    assert len(calls) == 24
    controls = [row for row in calls if row["treatment"] == "H0"]
    challengers = [row for row in calls if row["treatment"] != "H0"]
    assert len(controls) == len(challengers) == 12
    for model_id in config["models"]:
        model_treatments = {
            row["treatment"] for row in challengers if row["model_id"] == model_id
        }
        assert model_treatments == {"H1", "H2", "H3"}


def test_ticker_aliases_are_canonicalized_to_frozen_option_ids() -> None:
    config = replay.load_yaml(replay.DEFAULT_EXPERIMENT)
    episode = next(item for item in config["episodes"] if item["replay_id"] == "D1")
    option = next(
        item
        for item in replay.load_options(replay.source_round(episode))
        if item.get("symbol")
        and item["id"] != item["symbol"]
        and not item.get("is_cash")
        and not item.get("is_benchmark")
    )
    payload = {
        "shortlist_option_ids": [option["symbol"]],
        "top5": [{"option_id": option["symbol"]}],
    }
    normalized = replay.canonicalize_option_ids(payload, episode)
    assert normalized["shortlist_option_ids"] == [option["id"]]
    assert normalized["top5"][0]["option_id"] == option["id"]


def test_private_replay_can_override_provider_api_model() -> None:
    config = replay.load_yaml(replay.DEFAULT_EXPERIMENT)
    models = replay.model_index(config)
    assert models["google-gemini-3-1-pro"].api_model_name == "gemini-3.5-flash"


def test_confirmation_gate_requires_breadth() -> None:
    rows = []
    for model_index in range(4):
        for episode_index in range(3):
            rows.append(
                {
                    "challenger": "H1",
                    "pair_valid": True,
                    "model_id": f"m{model_index}",
                    "replay_id": f"c{episode_index}",
                    "control_top5_capture": False,
                    "challenger_top5_capture": model_index == 0 and episode_index == 0,
                    "paired_top5_alpha_improvement": 0.01,
                }
            )
    result = replay.confirmation_gate(rows, "H1")
    assert result["passes_confirmation_gate"] is True

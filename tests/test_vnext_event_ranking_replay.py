from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_vnext_event_ranking_replay.py"
SPEC = importlib.util.spec_from_file_location("vnext_event_replay_test", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
replay = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replay)
CONFIG = replay.load_config(ROOT / "experiments" / "vnext-event-ranking-replay-2026-07-21.yaml")


def test_event_registers_use_valid_option_ids_and_unique_event_ids() -> None:
    for episode in CONFIG["episodes"]:
        register = replay.event_register(episode)
        options = {
            str(row["id"])
            for row in replay.base.load_options(replay.base.source_round(episode))
        }
        events = register["events"]
        event_ids = [str(row["id"]) for row in events]
        assert len(event_ids) == len(set(event_ids))
        assert all(row["affected_options"] for row in events)
        assert not {
            option_id
            for row in events
            for option_id in row["affected_options"]
            if option_id not in options
        }


def test_event_registers_do_not_contain_direction_or_recommendation_fields() -> None:
    prohibited = {"direction", "expected_return", "recommendation", "score", "rank"}
    for episode in CONFIG["episodes"]:
        for event in replay.event_register(episode)["events"]:
            assert prohibited.isdisjoint(event)


def test_event_register_is_only_added_to_event_treatments() -> None:
    episode = CONFIG["episodes"][0]
    event_id = replay.event_register(episode)["events"][0]["id"]
    assert event_id not in replay.build_prompt(CONFIG, episode, "H4")
    assert event_id in replay.build_prompt(CONFIG, episode, "H7")
    assert event_id in replay.build_prompt(CONFIG, episode, "H8")


def test_search_and_final_call_budgets_are_frozen() -> None:
    assert len(replay.calls_for(CONFIG, "search")) == CONFIG["max_search_calls"] == 32
    assert len(replay.calls_for(CONFIG, "final")) == CONFIG["max_final_calls"] == 32
    assert CONFIG["max_total_calls"] == 64


def test_h8_schema_requires_pairwise_comparisons_and_abstention() -> None:
    schema = replay.response_schema("H8")
    assert schema["properties"]["candidate_vs_spy"]["minItems"] == 10
    assert schema["properties"]["pairwise_finalists"]["minItems"] == 10
    assert "abstention_reason" in schema["required"]

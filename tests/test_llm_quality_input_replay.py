from scripts.run_llm_quality_input_replay import (
    build_prompt,
    feature_rows,
    load_config,
    quality_table,
)


CONFIG_PATH = "experiments/llm-quality-input-replay-2026-07-21.yaml"


def config_and_episode():
    from pathlib import Path

    config = load_config(Path(CONFIG_PATH))
    return config, config["episodes"][0]


def test_evidence_snapshot_has_no_outcome_fields():
    config, episode = config_and_episode()
    rows = feature_rows(config, episode)
    assert len(rows) >= 60
    assert not ({"future_return", "winner", "realized_rank", "outcome"} & set(rows[0]))


def test_quality_table_is_complete_and_neutral():
    config, episode = config_and_episode()
    table = quality_table(config, episode)
    assert "quality evidence score" in table
    assert "future_return" not in table
    assert "winner" not in table.lower()


def test_q1_and_q2_preserve_single_turn_h4_contract():
    config, episode = config_and_episode()
    q1 = build_prompt(config, episode, "Q1")
    q2 = build_prompt(config, episode, "Q2")
    assert "Treatment identifier: Q1" in q1
    assert "Treatment identifier: Q2" in q2
    assert "three continuation candidates" in q1
    assert "at least three of the evidence table's ten highest" in q2
    assert "Complete option comparison table" in q1

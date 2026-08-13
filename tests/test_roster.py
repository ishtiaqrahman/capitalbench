from pathlib import Path

import pytest

from capitalbench.config import load_model_configs
from capitalbench.roster import (
    active_portfolio_v2_model_ids,
    canonical_portfolio_v2_model_ids,
    portfolio_v2_roster_version,
    validate_official_portfolio_v2_roster,
    validate_official_portfolio_v2_run_manifest,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PORTFOLIO_V2_MODEL_IDS = {
    "openai-gpt-5-5",
    "openai-gpt-5-6-sol",
    "anthropic-claude-opus-4-7",
    "anthropic-claude-opus-4-8",
    "anthropic-claude-opus-5",
    "anthropic-claude-fable-5",
    "google-gemini-3-1-pro",
    "xai-grok-4-3",
    "xai-grok-4-5",
    "xai-grok-4-6",
}
EXPECTED_POST_OPUS_4_7_RETIREMENT_MODEL_IDS = EXPECTED_PORTFOLIO_V2_MODEL_IDS - {
    "anthropic-claude-opus-4-7"
}
EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS = EXPECTED_POST_OPUS_4_7_RETIREMENT_MODEL_IDS - {
    "openai-gpt-5-5"
}
EXPECTED_PRE_GROK_4_6_MODEL_IDS = EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS - {
    "xai-grok-4-6"
}


def test_canonical_portfolio_v2_roster_contains_all_ten_models() -> None:
    assert set(canonical_portfolio_v2_model_ids()) == EXPECTED_PORTFOLIO_V2_MODEL_IDS


def test_active_portfolio_v2_roster_excludes_models_after_retirement() -> None:
    pre_opus_5_ids = EXPECTED_PORTFOLIO_V2_MODEL_IDS - {
        "anthropic-claude-opus-5",
        "xai-grok-4-6",
    }
    assert set(active_portfolio_v2_model_ids("2026-07-20T23:59:59Z")) == pre_opus_5_ids
    assert set(active_portfolio_v2_model_ids("2026-07-21T00:00:00Z")) == (
        EXPECTED_POST_OPUS_4_7_RETIREMENT_MODEL_IDS
        - {"anthropic-claude-opus-5", "xai-grok-4-6"}
    )
    assert set(
        active_portfolio_v2_model_ids(
            "2026-07-24T00:00:00Z",
            round_id="CB-2026-07-24-1W",
        )
    ) == (EXPECTED_POST_OPUS_4_7_RETIREMENT_MODEL_IDS - {"xai-grok-4-6"})
    assert set(
        active_portfolio_v2_model_ids(
            "2026-08-13T02:59:23Z",
            round_id="CB-2026-08-12-1W",
        )
    ) == (EXPECTED_POST_OPUS_4_7_RETIREMENT_MODEL_IDS - {"xai-grok-4-6"})
    assert set(
        active_portfolio_v2_model_ids(
            "2026-08-13T02:59:24Z",
            round_id="CB-2026-08-12-1W",
        )
    ) == EXPECTED_PRE_GROK_4_6_MODEL_IDS
    assert set(
        active_portfolio_v2_model_ids(
            "2026-08-13T03:14:52Z",
            round_id="CB-2026-08-13-1W",
        )
    ) == EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS


def test_roster_version_is_order_independent() -> None:
    model_ids = list(EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS)
    assert portfolio_v2_roster_version(model_ids) == portfolio_v2_roster_version(reversed(model_ids))


def test_official_portfolio_v2_rejects_partial_roster() -> None:
    configs = load_model_configs(PROJECT_ROOT / "configs" / "models.v2.yaml")

    with pytest.raises(ValueError, match="complete frozen model roster"):
        validate_official_portfolio_v2_roster("portfolio-v2.0", configs[:4])


def test_official_portfolio_v2_2_accepts_exact_frozen_roster() -> None:
    configs = load_model_configs(PROJECT_ROOT / "configs" / "models.v2.yaml")
    active_configs = [
        config for config in configs if config.model_id in EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS
    ]

    actual_ids = validate_official_portfolio_v2_roster(
        "portfolio-v2.2",
        active_configs,
        EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS,
    )

    assert set(actual_ids) == EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS


def test_official_portfolio_v2_2_requires_frozen_roster() -> None:
    configs = load_model_configs(PROJECT_ROOT / "configs" / "models.v2.yaml")

    with pytest.raises(ValueError, match="freeze expected_model_ids"):
        validate_official_portfolio_v2_roster("portfolio-v2.2", configs)


def test_official_portfolio_v2_acceptance_rejects_wrong_count() -> None:
    with pytest.raises(ValueError, match="model_count"):
        validate_official_portfolio_v2_run_manifest(
            "portfolio-v2.0",
            {"model_count": 4, "model_ids": sorted(EXPECTED_PORTFOLIO_V2_MODEL_IDS)[:4]},
        )


def test_official_portfolio_v2_2_acceptance_uses_frozen_roster() -> None:
    model_ids = sorted(EXPECTED_ACTIVE_PORTFOLIO_V2_MODEL_IDS)

    validate_official_portfolio_v2_run_manifest(
        "portfolio-v2.2",
        {"model_count": len(model_ids), "model_ids": model_ids},
        model_ids,
    )

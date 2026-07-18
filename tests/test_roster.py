from pathlib import Path

import pytest

from capitalbench.config import load_model_configs
from capitalbench.roster import (
    canonical_portfolio_v2_model_ids,
    validate_official_portfolio_v2_roster,
    validate_official_portfolio_v2_run_manifest,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PORTFOLIO_V2_MODEL_IDS = {
    "openai-gpt-5-5",
    "openai-gpt-5-6-sol",
    "anthropic-claude-opus-4-7",
    "anthropic-claude-opus-4-8",
    "anthropic-claude-fable-5",
    "google-gemini-3-1-pro",
    "xai-grok-4-3",
    "xai-grok-4-5",
}


def test_canonical_portfolio_v2_roster_contains_all_eight_models() -> None:
    assert set(canonical_portfolio_v2_model_ids()) == EXPECTED_PORTFOLIO_V2_MODEL_IDS


def test_official_portfolio_v2_rejects_partial_roster() -> None:
    configs = load_model_configs(PROJECT_ROOT / "configs" / "models.v2.yaml")

    with pytest.raises(ValueError, match="complete canonical model roster"):
        validate_official_portfolio_v2_roster("portfolio-v2.0", configs[:4])


def test_official_portfolio_v2_acceptance_rejects_wrong_count() -> None:
    with pytest.raises(ValueError, match="model_count"):
        validate_official_portfolio_v2_run_manifest(
            "portfolio-v2.0",
            {"model_count": 4, "model_ids": sorted(EXPECTED_PORTFOLIO_V2_MODEL_IDS)[:4]},
        )

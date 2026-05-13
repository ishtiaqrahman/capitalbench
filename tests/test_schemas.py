import pytest
from pydantic import ValidationError

from capitalbench.schemas import ModelSubmission, PortfolioConstraints, Usage


def _valid_submission() -> dict[str, object]:
    return {
        "round_id": "round-a",
        "model_id": "model-a",
        "provider": "openai",
        "mode": "closed_capability",
        "selected_option_id": "sp500",
        "confidence": 0.5,
        "rationale_summary": "A concise rationale.",
        "key_risks": ["Risk one"],
    }


def _valid_portfolio_submission() -> dict[str, object]:
    return {
        "round_id": "round-a",
        "model_id": "model-a",
        "provider": "openai",
        "mode": "closed_capability",
        "portfolio": [
            {"option_id": "sp500", "allocation_pct": 100, "rationale": "Benchmark exposure."},
        ],
        "confidence": 0.5,
        "portfolio_rationale": "Single-holding portfolio.",
        "rationale_summary": "A concise rationale.",
        "key_risks": ["Risk one"],
    }


def test_schema_validation_rejects_bad_confidence() -> None:
    payload = _valid_submission()
    payload["confidence"] = 1.2
    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_schema_validation_rejects_missing_required_field() -> None:
    payload = _valid_submission()
    del payload["selected_option_id"]
    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_schema_validation_rejects_extra_field() -> None:
    payload = _valid_submission()
    payload["selected_option_ids"] = ["sp500", "cash"]
    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_schema_validation_accepts_portfolio_submission() -> None:
    submission = ModelSubmission.model_validate(_valid_portfolio_submission())

    assert submission.selected_option_id is None
    assert submission.portfolio is not None
    assert submission.portfolio[0].allocation_pct == 100


def test_schema_validation_rejects_payload_with_pick_and_portfolio() -> None:
    payload = _valid_portfolio_submission()
    payload["selected_option_id"] = "sp500"

    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_portfolio_constraints_reject_impossible_minimum_allocation() -> None:
    with pytest.raises(ValidationError, match="min_holdings times min_allocation_pct"):
        PortfolioConstraints(min_holdings=4, min_allocation_pct=30)


def test_portfolio_constraints_require_full_allocation() -> None:
    with pytest.raises(ValidationError, match="max_total_allocation_pct must be 100"):
        PortfolioConstraints(max_total_allocation_pct=80)


def test_schema_validation_rejects_invalid_provider() -> None:
    payload = _valid_submission()
    payload["provider"] = "manual"
    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_schema_validation_rejects_unrecognized_mode() -> None:
    payload = _valid_submission()
    payload["mode"] = "portfolio"
    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_schema_validation_rejects_key_risks_that_are_not_a_list() -> None:
    payload = _valid_submission()
    payload["key_risks"] = "risk one"
    with pytest.raises(ValidationError):
        ModelSubmission.model_validate(payload)


def test_usage_validates_total_tokens() -> None:
    with pytest.raises(ValidationError):
        Usage.model_validate(
            {
                "input_tokens": 10,
                "output_tokens": 5,
                "total_tokens": 12,
            }
        )


def test_usage_allows_reasoning_tokens_within_output_tokens() -> None:
    usage = Usage.model_validate(
        {
            "input_tokens": 10,
            "output_tokens": 5,
            "reasoning_tokens": 3,
            "total_tokens": 15,
        }
    )

    assert usage.total_tokens == 15

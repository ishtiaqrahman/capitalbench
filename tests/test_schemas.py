import pytest
from pydantic import ValidationError

from capitalbench.schemas import ModelSubmission, Usage


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

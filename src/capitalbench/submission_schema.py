from __future__ import annotations

from .schemas import ModelConfig


def provider_submission_schema(model_config: ModelConfig) -> dict[str, object]:
    option_ids = [str(option_id) for option_id in model_config.metadata.get("option_ids", [])]
    if not option_ids:
        option_ids = ["CASH"]
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "round_id": {
                "type": "string",
                "enum": [str(model_config.metadata["round_id"])],
            },
            "model_id": {
                "type": "string",
                "enum": [model_config.model_id],
            },
            "provider": {
                "type": "string",
                "enum": [model_config.provider],
            },
            "mode": {
                "type": "string",
                "enum": [model_config.mode],
            },
            "selected_option_id": {
                "type": "string",
                "enum": option_ids,
            },
            "confidence": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
            },
            "rationale_summary": {
                "type": "string",
            },
            "key_risks": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": [
            "round_id",
            "model_id",
            "provider",
            "mode",
            "selected_option_id",
            "confidence",
            "rationale_summary",
            "key_risks",
        ],
    }


def prompt_for_model(prompt: str, model_config: ModelConfig) -> str:
    option_ids = ", ".join(str(option_id) for option_id in model_config.metadata.get("option_ids", []))
    return (
        f"{prompt}\n\n"
        "For this specific call, return only JSON using exactly these identifiers:\n"
        f"- round_id: {model_config.metadata['round_id']}\n"
        f"- model_id: {model_config.model_id}\n"
        f"- provider: {model_config.provider}\n"
        f"- mode: {model_config.mode}\n"
        f"- allowed selected_option_id values: {option_ids}\n"
    )

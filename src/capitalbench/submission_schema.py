from __future__ import annotations

from .schemas import ModelConfig


def provider_submission_schema(model_config: ModelConfig) -> dict[str, object]:
    option_ids = [str(option_id) for option_id in model_config.metadata.get("option_ids", [])]
    if not option_ids:
        option_ids = ["CASH"]
    submission_format = str(model_config.metadata.get("submission_format") or "single_pick")
    if submission_format == "portfolio":
        constraints = dict(model_config.metadata.get("portfolio_constraints") or {})
        min_holdings = int(constraints.get("min_holdings") or 1)
        max_holdings = int(constraints.get("max_holdings") or 5)
        increment = int(constraints.get("allocation_increment_pct") or 5)
        minimum = int(constraints.get("min_allocation_pct") or 5)
        return {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "round_id": {"type": "string", "enum": [str(model_config.metadata["round_id"])]},
                "model_id": {"type": "string", "enum": [model_config.model_id]},
                "provider": {"type": "string", "enum": [model_config.provider]},
                "mode": {"type": "string", "enum": [model_config.mode]},
                "portfolio": {
                    "type": "array",
                    "minItems": min_holdings,
                    "maxItems": max_holdings,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "option_id": {"type": "string", "enum": option_ids},
                            "allocation_pct": {
                                "type": "integer",
                                "minimum": minimum,
                                "maximum": 100,
                                "multipleOf": increment,
                            },
                            "rationale": {"type": "string"},
                        },
                        "required": ["option_id", "allocation_pct", "rationale"],
                    },
                },
                "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                "portfolio_rationale": {"type": "string"},
                "rationale_summary": {"type": "string"},
                "key_risks": {"type": "array", "items": {"type": "string"}},
            },
            "required": [
                "round_id",
                "model_id",
                "provider",
                "mode",
                "portfolio",
                "confidence",
                "portfolio_rationale",
                "rationale_summary",
                "key_risks",
            ],
        }
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
    submission_format = str(model_config.metadata.get("submission_format") or "single_pick")
    if submission_format == "portfolio":
        constraints = dict(model_config.metadata.get("portfolio_constraints") or {})
        return (
            f"{prompt}\n\n"
            "For this specific call, return only JSON using exactly these identifiers and constraints:\n"
            f"- round_id: {model_config.metadata['round_id']}\n"
            f"- model_id: {model_config.model_id}\n"
            f"- provider: {model_config.provider}\n"
            f"- mode: {model_config.mode}\n"
            f"- allowed portfolio option_id values: {option_ids}\n"
            f"- min_holdings: {constraints.get('min_holdings', 1)}\n"
            f"- max_holdings: {constraints.get('max_holdings', 5)}\n"
            f"- allocation_increment_pct: {constraints.get('allocation_increment_pct', 5)}\n"
            f"- min_allocation_pct: {constraints.get('min_allocation_pct', 5)}\n"
            f"- total_allocation_pct: {constraints.get('max_total_allocation_pct', 100)}\n"
        )
    return (
        f"{prompt}\n\n"
        "For this specific call, return only JSON using exactly these identifiers:\n"
        f"- round_id: {model_config.metadata['round_id']}\n"
        f"- model_id: {model_config.model_id}\n"
        f"- provider: {model_config.provider}\n"
        f"- mode: {model_config.mode}\n"
        f"- allowed selected_option_id values: {option_ids}\n"
    )

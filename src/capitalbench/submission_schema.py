from __future__ import annotations

from .methodology import is_portfolio_v2, is_production_portfolio_v2
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
        methodology_version = str(model_config.metadata.get("methodology_version") or "")
        v2 = is_portfolio_v2(methodology_version)
        production_v2 = is_production_portfolio_v2(methodology_version)
        holding_properties: dict[str, object] = {
            "option_id": {"type": "string", "enum": option_ids},
            "allocation_pct": {
                "type": "integer",
                "minimum": minimum,
                "maximum": 100,
                "multipleOf": increment,
            },
            "rationale": {"type": "string"},
        }
        holding_required = ["option_id", "allocation_pct", "rationale"]
        if v2:
            holding_properties.update(
                {
                    "expected_return_pct": {"type": "number"},
                    "time_window_catalyst": {"type": "string"},
                    "invalidation_condition": {"type": "string"},
                }
            )
            holding_required.extend(
                ["expected_return_pct", "time_window_catalyst", "invalidation_condition"]
            )
        properties: dict[str, object] = {
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
                    "properties": holding_properties,
                    "required": holding_required,
                },
            },
            "confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "portfolio_rationale": {"type": "string"},
            "rationale_summary": {"type": "string"},
            "key_risks": {"type": "array", "items": {"type": "string"}},
        }
        required = [
            "round_id",
            "model_id",
            "provider",
            "mode",
            "portfolio",
            "confidence",
            "portfolio_rationale",
            "rationale_summary",
            "key_risks",
        ]
        if v2:
            properties.update(
                {
                    "benchmark_expected_return_pct": {"type": "number"},
                    "portfolio_expected_return_pct": {"type": "number"},
                    "expected_alpha_vs_sp500_pct": {"type": "number"},
                }
            )
            required.extend(
                [
                    "benchmark_expected_return_pct",
                    "portfolio_expected_return_pct",
                    "expected_alpha_vs_sp500_pct",
                ]
            )
        if production_v2:
            properties["candidate_ledger"] = {
                "type": "array",
                "minItems": 6,
                "maxItems": 8,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "option_id": {"type": "string", "enum": option_ids},
                        "decision": {"type": "string", "enum": ["selected", "rejected"]},
                        "forecast_low_pct": {"type": "number"},
                        "forecast_base_pct": {"type": "number"},
                        "forecast_high_pct": {"type": "number"},
                        "evidence": {
                            "type": "array",
                            "minItems": 1,
                            "maxItems": 3,
                            "items": {"type": "string"},
                        },
                        "continuation_case": {"type": "string"},
                        "reversal_case": {"type": "string"},
                        "time_window_catalyst": {"type": "string"},
                        "invalidation_condition": {"type": "string"},
                    },
                    "required": [
                        "option_id",
                        "decision",
                        "forecast_low_pct",
                        "forecast_base_pct",
                        "forecast_high_pct",
                        "evidence",
                        "continuation_case",
                        "reversal_case",
                        "time_window_catalyst",
                        "invalidation_condition",
                    ],
                },
            }
            required.append("candidate_ledger")
        return {
            "type": "object",
            "additionalProperties": False,
            "properties": properties,
            "required": required,
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
        methodology_version = str(model_config.metadata.get("methodology_version") or "")
        v2_instructions = ""
        if is_portfolio_v2(methodology_version):
            v2_instructions = (
                f"- methodology_version: {methodology_version}\n"
                "- confidence is your probability from 0 to 1 that this portfolio beats SPY over the scoring window\n"
                "- expected return fields are percentage points, so 1.25 means +1.25%\n"
                "- expected_alpha_vs_sp500_pct must equal portfolio_expected_return_pct minus benchmark_expected_return_pct\n"
                "- each holding requires expected_return_pct, time_window_catalyst, and invalidation_condition\n"
            )
        if is_production_portfolio_v2(methodology_version):
            v2_instructions += (
                "- candidate_ledger must contain 6-8 unique options, include SP500, and span at least four economic-exposure clusters\n"
                "- selected candidate_ledger entries must exactly match portfolio holdings\n"
                "- every selected non-SP500, non-CASH candidate base forecast must exceed the SP500 base forecast\n"
                f"- max_economic_exposure_pct outside SP500 and CASH: {constraints.get('max_economic_exposure_pct', 50)}\n"
            )
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
            f"{v2_instructions}"
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

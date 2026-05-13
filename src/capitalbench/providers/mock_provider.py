from __future__ import annotations

import hashlib
import json
import time
from typing import Any

from ..schemas import ModelConfig, RuntimeSettings
from .base import ProviderResult, elapsed_usage


class MockProvider:
    provider_name = "mock"
    api_key_env_var = ""

    def run_model(
        self,
        model_config: ModelConfig,
        prompt: str,
        json_schema: dict[str, Any],
        runtime_limits: RuntimeSettings,
    ) -> ProviderResult:
        started_at = time.monotonic()
        options = model_config.metadata.get("option_ids") or ["CASH"]
        option_ids = [str(option_id) for option_id in options]
        if not option_ids:
            option_ids = ["CASH"]
        index = int(hashlib.sha256(model_config.model_id.encode("utf-8")).hexdigest(), 16) % len(option_ids)
        selected_option_id = option_ids[index]
        confidence = 0.5 + ((index % 4) * 0.08)
        base_payload = {
            "round_id": model_config.metadata["round_id"],
            "model_id": model_config.model_id,
            "provider": model_config.provider,
            "mode": model_config.mode,
            "confidence": round(confidence, 2),
            "rationale_summary": (
                f"Mock dry-run selected {selected_option_id} deterministically for "
                f"{model_config.model_id}."
            ),
            "key_risks": [
                "Mock output is not a real model decision",
                "Dry-run data must not be interpreted as benchmark evidence",
            ],
        }
        if model_config.metadata.get("submission_format") == "portfolio":
            constraints = dict(model_config.metadata.get("portfolio_constraints") or {})
            min_holdings = max(1, int(constraints.get("min_holdings") or 1))
            max_holdings = max(1, int(constraints.get("max_holdings") or 5))
            increment = max(1, int(constraints.get("allocation_increment_pct") or 5))
            minimum = max(1, int(constraints.get("min_allocation_pct") or 5))
            total = max(1, int(constraints.get("max_total_allocation_pct") or 100))
            feasible_by_minimum = max(1, total // minimum)
            holding_count = min(max_holdings, len(option_ids), feasible_by_minimum)
            holding_count = min(len(option_ids), max(min_holdings, holding_count))
            selected = [option_ids[(index + offset) % len(option_ids)] for offset in range(holding_count)]
            allocations = [minimum for _ in selected]
            remainder = total - sum(allocations)
            cursor = 0
            while remainder > 0 and selected:
                step = min(increment, remainder)
                allocations[cursor % len(allocations)] += step
                remainder -= step
                cursor += 1
            payload = {
                **base_payload,
                "portfolio": [
                    {
                        "option_id": option_id,
                        "allocation_pct": allocations[position],
                        "rationale": f"Mock portfolio allocation to {option_id}.",
                    }
                    for position, option_id in enumerate(selected)
                ],
                "portfolio_rationale": "Mock dry-run portfolio built deterministically.",
            }
        else:
            payload = {
                **base_payload,
                "selected_option_id": selected_option_id,
            }
        raw_text = json.dumps(payload, sort_keys=True)
        usage = elapsed_usage(
            started_at,
            input_tokens=len(prompt.split()),
            output_tokens=len(raw_text.split()),
        )
        return ProviderResult(
            raw_text=raw_text,
            parsed_json=payload,
            usage=usage,
            error=None,
        )

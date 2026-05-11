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
        payload = {
            "round_id": model_config.metadata["round_id"],
            "model_id": model_config.model_id,
            "provider": model_config.provider,
            "mode": model_config.mode,
            "selected_option_id": selected_option_id,
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

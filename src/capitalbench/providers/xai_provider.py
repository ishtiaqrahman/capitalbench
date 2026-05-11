from __future__ import annotations

import time
from typing import Any

from ..schemas import ModelConfig, RuntimeSettings
from .base import BaseProvider, ProviderResult, elapsed_usage, parse_json_object


class XAIProvider(BaseProvider):
    provider_name = "xai"
    api_key_env_var = "XAI_API_KEY"

    def run_model(
        self,
        model_config: ModelConfig,
        prompt: str,
        json_schema: dict[str, Any],
        runtime_limits: RuntimeSettings,
    ) -> ProviderResult:
        started_at = time.monotonic()
        payload = {
            "model": model_config.api_model_name,
            "messages": [
                {
                    "role": "system",
                    "content": "Return only valid JSON. Do not use tools or web search.",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": runtime_limits.temperature,
            "max_tokens": runtime_limits.max_output_tokens,
            "tools": [],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "capitalbench_submission",
                    "schema": json_schema,
                    "strict": True,
                },
            },
        }
        response = self._post_json(
            "https://api.x.ai/v1/chat/completions",
            {"Authorization": f"Bearer {self._api_key()}"},
            payload,
            runtime_limits.timeout_seconds,
        )
        raw_text = _extract_xai_text(response)
        usage_data = response.get("usage") or {}
        completion_details = usage_data.get("completion_tokens_details") or {}
        usage = elapsed_usage(
            started_at,
            input_tokens=usage_data.get("prompt_tokens"),
            output_tokens=usage_data.get("completion_tokens"),
            reasoning_tokens=completion_details.get("reasoning_tokens"),
            total_tokens=usage_data.get("total_tokens"),
        )
        return ProviderResult(
            raw_text=raw_text,
            parsed_json=parse_json_object(raw_text),
            usage=usage,
            error=None,
        )


def _extract_xai_text(response: dict[str, Any]) -> str:
    choices = response.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content")
    return content if isinstance(content, str) else ""

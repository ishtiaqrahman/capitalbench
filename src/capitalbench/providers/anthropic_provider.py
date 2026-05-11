from __future__ import annotations

import json
import time
from typing import Any

from ..schemas import ModelConfig, RuntimeSettings
from .base import BaseProvider, ProviderResult, elapsed_usage, parse_json_object


class AnthropicProvider(BaseProvider):
    provider_name = "anthropic"
    api_key_env_var = "ANTHROPIC_API_KEY"

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
            "max_tokens": runtime_limits.max_output_tokens,
            "temperature": runtime_limits.temperature,
            "system": (
                "Return only one JSON object that conforms to the supplied schema. "
                "Do not use tools and do not include markdown fences."
            ),
            "tool_choice": {"type": "none"},
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"{prompt}\n\n"
                        "Required JSON schema:\n"
                        f"{json.dumps(json_schema, sort_keys=True)}"
                    ),
                }
            ],
        }
        response = self._post_anthropic(payload, runtime_limits.timeout_seconds)
        raw_text = _extract_anthropic_text(response)
        usage_data = response.get("usage") or {}
        usage = elapsed_usage(
            started_at,
            input_tokens=usage_data.get("input_tokens"),
            output_tokens=usage_data.get("output_tokens"),
        )
        return ProviderResult(
            raw_text=raw_text,
            parsed_json=parse_json_object(raw_text),
            usage=usage,
            error=None,
        )


    def _post_anthropic(self, payload: dict[str, Any], timeout_seconds: int) -> dict[str, Any]:
        try:
            return self._post_json(
                "https://api.anthropic.com/v1/messages",
                {
                    "x-api-key": self._api_key(),
                    "anthropic-version": "2023-06-01",
                },
                payload,
                timeout_seconds,
            )
        except RuntimeError as exc:
            message = str(exc).lower()
            if "temperature" not in message or ("deprecated" not in message and "unsupported" not in message):
                raise
            retry_payload = dict(payload)
            retry_payload.pop("temperature", None)
            return self._post_json(
                "https://api.anthropic.com/v1/messages",
                {
                    "x-api-key": self._api_key(),
                    "anthropic-version": "2023-06-01",
                },
                retry_payload,
                timeout_seconds,
            )


def _extract_anthropic_text(response: dict[str, Any]) -> str:
    parts: list[str] = []
    for item in response.get("content", []) or []:
        text = item.get("text")
        if isinstance(text, str):
            parts.append(text)
    return "\n".join(parts)

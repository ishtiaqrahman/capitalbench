from __future__ import annotations

import time
from typing import Any

from ..schemas import ModelConfig, RuntimeSettings
from .base import BaseProvider, ProviderResult, elapsed_usage, parse_json_object


class OpenAIProvider(BaseProvider):
    provider_name = "openai"
    api_key_env_var = "OPENAI_API_KEY"

    def run_model(
        self,
        model_config: ModelConfig,
        prompt: str,
        json_schema: dict[str, Any],
        runtime_limits: RuntimeSettings,
    ) -> ProviderResult:
        started_at = time.monotonic()
        payload: dict[str, Any] = {
            "model": model_config.api_model_name,
            "input": prompt,
            "temperature": runtime_limits.temperature,
            "max_output_tokens": runtime_limits.max_output_tokens,
            "tools": [],
            "tool_choice": "none",
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "capitalbench_submission",
                    "schema": json_schema,
                    "strict": True,
                }
            },
        }
        if runtime_limits.reasoning_effort:
            payload["reasoning"] = {"effort": runtime_limits.reasoning_effort}

        response = self._post_openai(payload, runtime_limits.timeout_seconds)
        raw_text = _extract_openai_text(response)
        usage_data = response.get("usage") or {}
        output_details = usage_data.get("output_tokens_details") or {}
        usage = elapsed_usage(
            started_at,
            input_tokens=usage_data.get("input_tokens"),
            output_tokens=usage_data.get("output_tokens"),
            reasoning_tokens=output_details.get("reasoning_tokens"),
            total_tokens=usage_data.get("total_tokens"),
        )
        return ProviderResult(
            raw_text=raw_text,
            parsed_json=parse_json_object(raw_text),
            usage=usage,
            error=None,
        )


    def _post_openai(self, payload: dict[str, Any], timeout_seconds: int) -> dict[str, Any]:
        try:
            return self._post_json(
                "https://api.openai.com/v1/responses",
                {"Authorization": f"Bearer {self._api_key()}"},
                payload,
                timeout_seconds,
            )
        except RuntimeError as exc:
            message = str(exc)
            if "Unsupported parameter" not in message or "temperature" not in message:
                raise
            retry_payload = dict(payload)
            retry_payload.pop("temperature", None)
            return self._post_json(
                "https://api.openai.com/v1/responses",
                {"Authorization": f"Bearer {self._api_key()}"},
                retry_payload,
                timeout_seconds,
            )


def _extract_openai_text(response: dict[str, Any]) -> str:
    if isinstance(response.get("output_text"), str):
        return response["output_text"]
    parts: list[str] = []
    for item in response.get("output", []) or []:
        for content in item.get("content", []) or []:
            text = content.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts)

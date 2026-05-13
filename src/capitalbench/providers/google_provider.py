from __future__ import annotations

import time
import urllib.parse
from typing import Any

from ..schemas import ModelConfig, RuntimeSettings
from .base import BaseProvider, ProviderResult, elapsed_usage, parse_json_object


class GoogleProvider(BaseProvider):
    provider_name = "google"
    api_key_env_var = "GOOGLE_API_KEY"

    def run_model(
        self,
        model_config: ModelConfig,
        prompt: str,
        json_schema: dict[str, Any],
        runtime_limits: RuntimeSettings,
    ) -> ProviderResult:
        started_at = time.monotonic()
        api_key = self._api_key()
        model_name = urllib.parse.quote(model_config.api_model_name, safe="")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
        generation_config: dict[str, Any] = {
            "temperature": runtime_limits.temperature,
            "maxOutputTokens": runtime_limits.max_output_tokens,
            "responseMimeType": "application/json",
            "responseSchema": _to_google_response_schema(json_schema),
        }
        thinking_config = _google_thinking_config(runtime_limits.reasoning_effort)
        if thinking_config is not None:
            generation_config["thinkingConfig"] = thinking_config
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ],
            "generationConfig": generation_config,
            "tools": [],
            "toolConfig": {"functionCallingConfig": {"mode": "NONE"}},
        }
        response = self._post_json(url, {"x-goog-api-key": api_key}, payload, runtime_limits.timeout_seconds)
        raw_text = _extract_google_text(response)
        usage_data = response.get("usageMetadata") or {}
        usage = elapsed_usage(
            started_at,
            input_tokens=usage_data.get("promptTokenCount"),
            output_tokens=usage_data.get("candidatesTokenCount"),
            reasoning_tokens=usage_data.get("thoughtsTokenCount"),
            total_tokens=usage_data.get("totalTokenCount"),
        )
        return ProviderResult(
            raw_text=raw_text,
            parsed_json=parse_json_object(raw_text),
            usage=usage,
            error=None,
        )


def _extract_google_text(response: dict[str, Any]) -> str:
    parts: list[str] = []
    for candidate in response.get("candidates", []) or []:
        content = candidate.get("content") or {}
        for part in content.get("parts", []) or []:
            text = part.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts)


def _google_thinking_config(reasoning_effort: str | None) -> dict[str, int] | None:
    if reasoning_effort is None:
        return None
    budgets = {
        "none": 0,
        "minimal": 128,
        "low": 512,
        "medium": 1024,
        "high": 2048,
    }
    budget = budgets.get(reasoning_effort)
    if budget is None:
        return None
    return {"thinkingBudget": budget}


def _to_google_response_schema(schema: dict[str, Any]) -> dict[str, Any]:
    unsupported = {"additionalProperties", "minimum", "maximum", "multipleOf"}
    converted: dict[str, Any] = {}
    for key, value in schema.items():
        if key in unsupported:
            continue
        if key == "properties" and isinstance(value, dict):
            converted[key] = {
                property_name: _to_google_response_schema(property_schema)
                for property_name, property_schema in value.items()
                if isinstance(property_schema, dict)
            }
            continue
        if key == "items" and isinstance(value, dict):
            converted[key] = _to_google_response_schema(value)
            continue
        converted[key] = value
    return converted

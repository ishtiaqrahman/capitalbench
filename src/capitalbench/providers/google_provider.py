from __future__ import annotations

import json
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
        thinking_config = _google_thinking_config(
            model_config.api_model_name,
            runtime_limits.reasoning_effort,
        )
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
        headers = {"x-goog-api-key": api_key}
        try:
            response = self._post_json(url, headers, payload, runtime_limits.timeout_seconds)
        except RuntimeError as exc:
            if not _is_response_schema_rejection(exc):
                raise
            retry_payload = dict(payload)
            retry_generation_config = dict(generation_config)
            retry_generation_config.pop("responseSchema", None)
            retry_payload["generationConfig"] = retry_generation_config
            retry_payload["contents"] = [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                f"{prompt}\n\nRequired JSON schema:\n"
                                f"{json.dumps(json_schema, sort_keys=True)}"
                            )
                        }
                    ],
                }
            ]
            response = self._post_json(url, headers, retry_payload, runtime_limits.timeout_seconds)
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


def _google_thinking_config(
    api_model_name: str,
    reasoning_effort: str | None,
) -> dict[str, int | str] | None:
    if reasoning_effort is None:
        return None
    if api_model_name.lower().startswith("gemini-3"):
        levels = {
            "minimal": "minimal",
            "low": "low",
            "medium": "medium",
            "high": "high",
        }
        level = levels.get(reasoning_effort)
        return {"thinkingLevel": level} if level is not None else None
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


def _is_response_schema_rejection(exc: RuntimeError) -> bool:
    message = str(exc).lower()
    return "http 400" in message and ("invalid_argument" in message or "invalid argument" in message)


def _to_google_response_schema(schema: dict[str, Any]) -> dict[str, Any]:
    unsupported = {"additionalProperties", "minimum", "maximum", "multipleOf"}
    converted: dict[str, Any] = {}
    for key, value in schema.items():
        if key in unsupported:
            continue
        # Gemini rejects otherwise valid schemas when repeated option enums make
        # the structured-output grammar too large. CapitalBench validates these
        # identifiers against the frozen universe after generation.
        if key == "enum" and isinstance(value, list) and len(value) > 50:
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

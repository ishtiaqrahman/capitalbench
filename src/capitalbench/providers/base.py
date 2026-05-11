from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any, Protocol

from pydantic import Field

from ..schemas import ModelConfig, RuntimeSettings, StrictModel, Usage


class ProviderResult(StrictModel):
    raw_text: str
    parsed_json: dict[str, Any] | None = None
    usage: Usage
    error: str | None = None


class ProviderAdapter(Protocol):
    def run_model(
        self,
        model_config: ModelConfig,
        prompt: str,
        json_schema: dict[str, Any],
        runtime_limits: RuntimeSettings,
    ) -> ProviderResult:
        ...


class BaseProvider:
    provider_name: str
    api_key_env_var: str

    def _api_key(self) -> str:
        api_key = os.environ.get(self.api_key_env_var, "").strip()
        if not api_key:
            raise RuntimeError(f"{self.api_key_env_var} is required for {self.provider_name} API calls")
        return api_key

    def _post_json(
        self,
        url: str,
        headers: dict[str, str],
        payload: dict[str, Any],
        timeout_seconds: int,
    ) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=body,
            headers={
                "Content-Type": "application/json",
                **headers,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                response_body = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")[:1000]
            detail = f": {error_body}" if error_body else ""
            raise RuntimeError(f"{self.provider_name} API request failed with HTTP {exc.code}{detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"{self.provider_name} API request failed: {exc.reason}") from exc
        return json.loads(response_body)


def parse_json_object(raw_text: str) -> dict[str, Any] | None:
    try:
        parsed = json.loads(raw_text)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        pass

    start = raw_text.find("{")
    end = raw_text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        parsed = json.loads(raw_text[start : end + 1])
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def elapsed_usage(
    started_at: float,
    *,
    input_tokens: int | None = None,
    output_tokens: int | None = None,
    reasoning_tokens: int | None = None,
    total_tokens: int | None = None,
    cost_usd: float | None = None,
) -> Usage:
    return Usage(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        reasoning_tokens=reasoning_tokens,
        total_tokens=total_tokens,
        cost_usd=cost_usd,
        latency_seconds=time.monotonic() - started_at,
    )

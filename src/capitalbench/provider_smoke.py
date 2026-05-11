from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .io import load_manifest, load_options, write_json
from .prompting import build_prompt
from .runner import PROVIDER_CLASSES
from .schemas import ModelConfig, ProviderName, RuntimeSettings
from .submission_schema import prompt_for_model, provider_submission_schema
from .validation import validate_submission_payload

PROVIDER_KEY_ENV_VARS = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "google": "GOOGLE_API_KEY",
    "xai": "XAI_API_KEY",
}


@dataclass(frozen=True)
class ProviderSmokeSummary:
    provider: str
    smoke_dir: Path
    validation_status: str
    error: str | None


def check_provider_keys() -> dict[str, bool]:
    return {
        env_var: bool(os.environ.get(env_var, "").strip())
        for env_var in PROVIDER_KEY_ENV_VARS.values()
    }


def smoke_provider(
    *,
    provider: ProviderName,
    api_model_name: str,
    round_path: Path,
    allow_real_api_calls: bool = False,
) -> ProviderSmokeSummary:
    if not allow_real_api_calls:
        raise RuntimeError("refusing provider smoke test without --allow-real-api-calls")
    env_var = PROVIDER_KEY_ENV_VARS[provider]
    if not os.environ.get(env_var, "").strip():
        raise RuntimeError(f"{env_var} is required for {provider} provider smoke tests")

    manifest = load_manifest(round_path)
    options = load_options(round_path)
    prompt = build_prompt(round_path)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    smoke_dir = round_path / "provider-smoke-tests" / f"{provider}-{timestamp}"
    smoke_dir.mkdir(parents=True, exist_ok=False)

    reasoning_effort = None
    if provider == "google":
        reasoning_effort = "low"
    elif provider == "openai":
        reasoning_effort = "minimal"

    model_config = ModelConfig(
        model_id=f"{provider}-smoke",
        provider=provider,
        api_model_name=api_model_name,
        enabled=True,
        mode="closed_capability",
        temperature=0,
        max_completion_tokens=500,
        max_wall_clock_seconds=60,
        reasoning_effort=reasoning_effort,
        metadata={
            "round_id": manifest.round_id,
            "option_ids": [option.option_id for option in options],
            "run_type": "provider_smoke",
            "replicate_index": None,
            "replicate_count": None,
            "is_official_score": False,
        },
    )
    runtime_limits = RuntimeSettings(
        timeout_seconds=60,
        max_output_tokens=500,
        temperature=0,
        reasoning_effort=reasoning_effort,
    )

    started_at_time = time.monotonic()
    started_at = datetime.now(timezone.utc).isoformat()
    try:
        result = PROVIDER_CLASSES[provider]().run_model(
            model_config,
            prompt_for_model(prompt, model_config),
            provider_submission_schema(model_config),
            runtime_limits,
        )
    except Exception as exc:
        completed_at = datetime.now(timezone.utc).isoformat()
        latency_seconds = time.monotonic() - started_at_time
        error = str(exc)
        (smoke_dir / "raw_response.txt").write_text("", encoding="utf-8")
        write_json(
            smoke_dir / "smoke_log.json",
            {
                "provider": provider,
                "api_model_name": api_model_name,
                "started_at_utc": started_at,
                "completed_at_utc": completed_at,
                "latency_seconds": latency_seconds,
                "input_tokens": None,
                "output_tokens": None,
                "reasoning_tokens": None,
                "total_tokens": None,
                "cost_usd": None,
                "raw_response_sha256": hashlib.sha256(b"").hexdigest(),
                "validation_status": "invalid",
                "error": error,
            },
        )
        write_json(
            smoke_dir / "validation_result.json",
            {
                "validation_status": "invalid",
                "error": error,
            },
        )
        return ProviderSmokeSummary(
            provider=provider,
            smoke_dir=smoke_dir,
            validation_status="invalid",
            error=error,
        )
    completed_at = datetime.now(timezone.utc).isoformat()
    raw_response_sha256 = hashlib.sha256(result.raw_text.encode("utf-8")).hexdigest()

    (smoke_dir / "raw_response.txt").write_text(result.raw_text, encoding="utf-8")
    parsed_json = None
    if result.parsed_json is not None:
        parsed_json = {
            **result.parsed_json,
            "run_type": "provider_smoke",
            "replicate_index": None,
            "replicate_count": None,
            "is_official_score": False,
        }
        write_json(smoke_dir / "parsed_response.json", parsed_json)

    validation_status = "invalid"
    validation_error = result.error
    try:
        if parsed_json is None:
            raise ValueError("provider response did not contain a JSON object")
        validate_submission_payload(parsed_json, options, manifest.round_id, run_type="provider_smoke")
    except Exception as exc:
        validation_error = validation_error or str(exc)
    else:
        validation_status = "valid"

    write_json(
        smoke_dir / "smoke_log.json",
        {
            "provider": provider,
            "api_model_name": api_model_name,
            "started_at_utc": started_at,
            "completed_at_utc": completed_at,
            "latency_seconds": result.usage.latency_seconds,
            "input_tokens": result.usage.input_tokens,
            "output_tokens": result.usage.output_tokens,
            "reasoning_tokens": result.usage.reasoning_tokens,
            "total_tokens": result.usage.total_tokens,
            "cost_usd": result.usage.cost_usd,
            "raw_response_sha256": raw_response_sha256,
            "validation_status": validation_status,
            "error": validation_error,
        },
    )
    write_json(
        smoke_dir / "validation_result.json",
        {
            "validation_status": validation_status,
            "error": validation_error,
        },
    )
    return ProviderSmokeSummary(
        provider=provider,
        smoke_dir=smoke_dir,
        validation_status=validation_status,
        error=validation_error,
    )

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import PricingTable, calculate_cost_usd, load_model_configs, load_pricing_config
from .io import load_manifest, load_options, write_json
from .prompting import build_prompt
from .providers import AnthropicProvider, GoogleProvider, MockProvider, OpenAIProvider, ProviderResult, XAIProvider
from .portfolio import constraints_from_manifest, submission_format_from_manifest
from .run_store import (
    create_run_paths,
    generate_run_id,
    update_run_manifest,
    validate_run_id,
    write_initial_run_manifest,
)
from .schemas import ModelConfig, RuntimeSettings, Usage
from .submission_schema import prompt_for_model, provider_submission_schema
from .validation import validate_submission_payload

PROVIDER_CLASSES = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "google": GoogleProvider,
    "xai": XAIProvider,
}


@dataclass(frozen=True)
class RunSummary:
    run_id: str
    loaded_models: int
    skipped_models: int
    attempted_models: int
    valid_submissions: int
    invalid_submissions: int
    run_log_path: Path
    skipped_reasons: list[str] = field(default_factory=list)


def run_round(
    round_path: Path,
    models_path: Path,
    pricing_path: Path | None = None,
    mode: str = "closed_capability",
    mock: bool = False,
    allow_real_api_calls: bool = False,
    run_id: str | None = None,
    overwrite_run: bool = False,
    run_type: str | None = None,
    replicates: int | None = None,
) -> RunSummary:
    selected_run_type, selected_replicates = _normalize_run_type_and_replicates(run_type, mock, replicates)
    if not mock and not allow_real_api_calls:
        raise RuntimeError(
            "refusing to call real provider APIs without --allow-real-api-calls; "
            "use --mock for a dry run"
        )

    manifest = load_manifest(round_path)
    options = load_options(round_path)
    submission_format = submission_format_from_manifest(manifest)
    portfolio_constraints = constraints_from_manifest(manifest)
    prompt = build_prompt(round_path)
    model_configs = load_model_configs(models_path)
    pricing = load_pricing_config(pricing_path)
    enabled_models, skipped_reasons = _filter_eligible_models(model_configs, manifest.round_id, manifest.decision_deadline, mode)
    skipped_models = len(model_configs) - len(enabled_models)

    if not mock:
        _preflight_real_api_keys(enabled_models)

    selected_run_id = validate_run_id(run_id) if run_id else generate_run_id(mode, mock, selected_run_type)
    run_paths = create_run_paths(round_path, selected_run_id, overwrite=overwrite_run)
    write_initial_run_manifest(
        run_paths,
        round_id=manifest.round_id,
        mode=mode,
        run_type=selected_run_type,
        mock=mock,
        models_path=models_path,
        pricing_path=pricing_path,
        replicates=selected_replicates,
        allow_real_api_calls=allow_real_api_calls,
        official_score_eligible=False,
    )

    valid_count = 0
    invalid_count = 0
    validation_errors: dict[str, list[str]] = {}
    option_ids = [option.option_id for option in options]

    with run_paths.run_log_path.open("w", encoding="utf-8") as log_handle:
        for model_config in enabled_models:
            for replicate_index in range(1, selected_replicates + 1):
                enriched_config = _with_round_metadata(
                    model_config,
                    manifest.round_id,
                    option_ids,
                    run_type=selected_run_type,
                    replicate_index=replicate_index,
                    replicate_count=selected_replicates,
                    is_official_score=selected_run_type == "official",
                    submission_format=submission_format,
                    portfolio_constraints=portfolio_constraints.model_dump(mode="json"),
                )
                started_at = _utc_now()
                result = _run_one_model(
                    enriched_config,
                    prompt_for_model(prompt, enriched_config),
                    provider_submission_schema(enriched_config),
                    mock,
                )
                completed_at = _utc_now()
                result = _apply_pricing(result, enriched_config, pricing)
                raw_response_sha256 = hashlib.sha256(result.raw_text.encode("utf-8")).hexdigest()

                raw_payload = _raw_payload_from_result(
                    result,
                    enriched_config,
                    run_type=selected_run_type,
                    replicate_index=replicate_index,
                    replicate_count=selected_replicates,
                    is_official_score=selected_run_type == "official",
                )
                filename_stem = _submission_filename_stem(
                    enriched_config.model_id,
                    selected_run_type,
                    replicate_index,
                )
                raw_file = run_paths.raw_dir / f"{filename_stem}.json"
                parsed_file = run_paths.parsed_dir / f"{filename_stem}.json"
                raw_response_file = run_paths.raw_responses_dir / f"{filename_stem}.txt"
                raw_response_file.write_text(result.raw_text, encoding="utf-8", newline="")
                write_json(raw_file, raw_payload)

                validation_status = "invalid"
                validation_error = result.error
                try:
                    submission = validate_submission_payload(
                        raw_payload,
                        options,
                        manifest.round_id,
                        run_type=selected_run_type,
                        replicate_count=selected_replicates,
                        require_run_metadata=selected_run_type in {"official", "stability", "retrospective"},
                        submission_format=submission_format,
                        portfolio_constraints=portfolio_constraints,
                    )
                except Exception as exc:
                    invalid_count += 1
                    validation_error = validation_error or str(exc)
                    validation_errors[raw_file.name] = [validation_error]
                    if parsed_file.exists():
                        parsed_file.unlink()
                else:
                    valid_count += 1
                    validation_status = "valid"
                    write_json(parsed_file, submission.model_dump(mode="json", exclude_none=True))

                log_handle.write(
                    json.dumps(
                        _run_log_record(
                            model_config=enriched_config,
                            started_at_utc=started_at,
                            completed_at_utc=completed_at,
                            usage=result.usage,
                            raw_response_sha256=raw_response_sha256,
                            raw_response_path=raw_response_file.relative_to(run_paths.run_path).as_posix(),
                            validation_status=validation_status,
                            error=validation_error,
                            run_type=selected_run_type,
                            replicate_index=replicate_index,
                            replicate_count=selected_replicates,
                            is_official_score=selected_run_type == "official",
                        ),
                        sort_keys=True,
                    )
                    + "\n"
                )

    validation_summary = {
        "run_id": selected_run_id,
        "run_type": selected_run_type,
        "replicates": selected_replicates,
        "raw_count": len(enabled_models) * selected_replicates,
        "valid_count": valid_count,
        "invalid_count": invalid_count,
        "errors": validation_errors,
    }
    write_json(run_paths.validation_summary_path, validation_summary)
    official_score_eligible = (
        selected_run_type == "official"
        and not mock
        and len(enabled_models) > 0
        and valid_count == len(enabled_models)
        and invalid_count == 0
    )
    manifest_updates: dict[str, Any] = {
        "model_count": len(enabled_models),
        "loaded_models": len(model_configs),
        "skipped_models": skipped_models,
        "valid_submissions": valid_count,
        "invalid_submissions": invalid_count,
        "completed_at_utc": _utc_now(),
        "official_score_eligible": official_score_eligible,
    }
    if selected_run_type == "official" and not mock and not official_score_eligible:
        manifest_updates["notes"] = (
            "Official run is incomplete or contains invalid submissions; preserved for audit "
            "but not eligible for public official scoring."
        )
    update_run_manifest(
        run_paths,
        manifest_updates,
    )

    return RunSummary(
        run_id=selected_run_id,
        loaded_models=len(model_configs),
        skipped_models=skipped_models,
        attempted_models=len(enabled_models) * selected_replicates,
        valid_submissions=valid_count,
        invalid_submissions=invalid_count,
        run_log_path=run_paths.run_log_path,
        skipped_reasons=skipped_reasons,
    )


def _normalize_run_type_and_replicates(
    run_type: str | None,
    mock: bool,
    replicates: int | None,
) -> tuple[str, int]:
    selected_run_type = run_type or ("mock" if mock else "official")
    if selected_run_type not in {"official", "stability", "mock", "retrospective"}:
        raise ValueError("run_type must be one of: official, stability, mock, retrospective")

    selected_replicates = replicates if replicates is not None else (5 if selected_run_type == "stability" else 1)
    if selected_replicates < 1:
        raise ValueError("replicates must be at least 1")
    if selected_run_type == "official" and selected_replicates != 1:
        raise ValueError("official runs require exactly one replicate; do not pass --replicates > 1")
    if selected_run_type == "stability" and selected_replicates < 2:
        raise ValueError("stability runs require --replicates of at least 2")
    if selected_run_type == "mock" and selected_replicates != 1:
        raise ValueError("run_type mock requires exactly one replicate; use --run-type stability for repeated mock calls")
    if selected_run_type == "retrospective" and selected_replicates != 1:
        raise ValueError("retrospective runs require exactly one replicate; use --run-type stability for repeated calls")
    return selected_run_type, selected_replicates


def _filter_eligible_models(
    model_configs: list[ModelConfig],
    round_id: str,
    decision_deadline: str | None,
    mode: str,
) -> tuple[list[ModelConfig], list[str]]:
    enabled: list[ModelConfig] = []
    skipped: list[str] = []
    for config in model_configs:
        reason = _model_skip_reason(config, round_id, decision_deadline, mode)
        if reason is not None:
            skipped.append(reason)
            continue
        enabled.append(config)
    return enabled, skipped


def _model_skip_reason(
    model_config: ModelConfig,
    round_id: str,
    decision_deadline: str | None,
    mode: str,
) -> str | None:
    if not model_config.enabled:
        return f"Skipping {model_config.model_id}: disabled."
    if model_config.mode != mode:
        return f"Skipping {model_config.model_id}: mode {model_config.mode} does not match requested {mode}."
    if model_config.first_eligible_round and round_id < model_config.first_eligible_round:
        return f"Skipping {model_config.model_id}: not eligible until {model_config.first_eligible_round}."
    if model_config.first_eligible_date_utc and decision_deadline:
        deadline = _parse_utc_datetime(decision_deadline)
        eligible_at = _parse_utc_datetime(model_config.first_eligible_date_utc)
        if deadline is not None and eligible_at is not None and deadline < eligible_at:
            return f"Skipping {model_config.model_id}: not eligible until {model_config.first_eligible_date_utc}."
    return None


def _parse_utc_datetime(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _preflight_real_api_keys(model_configs: list[ModelConfig]) -> None:
    for config in model_configs:
        provider_class = PROVIDER_CLASSES.get(config.provider)
        if provider_class is None:
            raise ValueError(f"invalid provider: {config.provider}")
        env_var = provider_class.api_key_env_var
        if not os.environ.get(env_var, "").strip():
            raise RuntimeError(f"{env_var} is required for {config.provider} API calls")


def _with_round_metadata(
    model_config: ModelConfig,
    round_id: str,
    option_ids: list[str],
    *,
    run_type: str,
    replicate_index: int,
    replicate_count: int,
    is_official_score: bool,
    submission_format: str,
    portfolio_constraints: dict[str, Any],
) -> ModelConfig:
    metadata = {
        **model_config.metadata,
        "round_id": round_id,
        "option_ids": option_ids,
        "run_type": run_type,
        "replicate_index": replicate_index,
        "replicate_count": replicate_count,
        "is_official_score": is_official_score,
        "submission_format": submission_format,
        "portfolio_constraints": portfolio_constraints,
    }
    return model_config.model_copy(update={"metadata": metadata})


def _run_one_model(
    model_config: ModelConfig,
    prompt: str,
    json_schema: dict[str, Any],
    mock: bool,
) -> ProviderResult:
    provider = MockProvider() if mock else PROVIDER_CLASSES[model_config.provider]()
    runtime_limits = RuntimeSettings(
        timeout_seconds=model_config.max_wall_clock_seconds,
        max_output_tokens=model_config.max_completion_tokens,
        temperature=model_config.temperature,
        reasoning_effort=model_config.reasoning_effort,
    )
    try:
        return provider.run_model(model_config, prompt, json_schema, runtime_limits)
    except Exception as exc:
        return ProviderResult(
            raw_text="",
            parsed_json=None,
            usage=Usage(latency_seconds=0),
            error=str(exc),
        )


def _apply_pricing(result: ProviderResult, model_config: ModelConfig, pricing: PricingTable) -> ProviderResult:
    cost_usd = calculate_cost_usd(model_config.provider, model_config.api_model_name, result.usage, pricing)
    usage = result.usage.model_copy(update={"cost_usd": cost_usd})
    return result.model_copy(update={"usage": usage})


def _raw_payload_from_result(
    result: ProviderResult,
    model_config: ModelConfig,
    *,
    run_type: str,
    replicate_index: int,
    replicate_count: int,
    is_official_score: bool,
) -> dict[str, Any]:
    run_fields = {
        "run_type": run_type,
        "replicate_index": replicate_index,
        "replicate_count": replicate_count,
        "is_official_score": is_official_score,
    }
    if result.parsed_json is not None:
        payload = dict(result.parsed_json)
        payload.update(run_fields)
        payload["usage"] = result.usage.model_dump(mode="json", exclude_none=True)
        if result.usage.cost_usd is not None:
            payload["cost_usd"] = result.usage.cost_usd
        return payload
    return {
        "round_id": model_config.metadata.get("round_id"),
        "model_id": model_config.model_id,
        "provider": model_config.provider,
        "mode": model_config.mode,
        **run_fields,
        "raw_text": result.raw_text,
        "error": result.error,
        "usage": result.usage.model_dump(mode="json", exclude_none=True),
    }


def _run_log_record(
    *,
    model_config: ModelConfig,
    started_at_utc: str,
    completed_at_utc: str,
    usage: Usage,
    raw_response_sha256: str,
    raw_response_path: str,
    validation_status: str,
    error: str | None,
    run_type: str,
    replicate_index: int,
    replicate_count: int,
    is_official_score: bool,
) -> dict[str, Any]:
    return {
        "provider": model_config.provider,
        "model_id": model_config.model_id,
        "api_model_name": model_config.api_model_name,
        "run_type": run_type,
        "replicate_index": replicate_index,
        "replicate_count": replicate_count,
        "is_official_score": is_official_score,
        "started_at_utc": started_at_utc,
        "completed_at_utc": completed_at_utc,
        "latency_seconds": usage.latency_seconds,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "reasoning_tokens": usage.reasoning_tokens,
        "total_tokens": usage.total_tokens,
        "cost_usd": usage.cost_usd,
        "raw_response_sha256": raw_response_sha256,
        "raw_response_path": raw_response_path,
        "validation_status": validation_status,
        "error": error,
    }


def _safe_filename(value: str) -> str:
    return "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in value)


def _submission_filename_stem(model_id: str, run_type: str, replicate_index: int) -> str:
    safe_model_id = _safe_filename(model_id)
    if run_type == "stability":
        return f"{safe_model_id}__replicate_{replicate_index:03d}"
    return safe_model_id


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

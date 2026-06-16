from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import statistics
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from .cumulative import discover_rounds
from .io import load_manifest, load_options, read_json, read_yaml, write_json
from .run_store import get_run_paths, list_run_ids, read_run_manifest

INSIGHTS_VERSION = "capitalbench_insights_v1"
INSIGHTS_INPUT_VERSION = "capitalbench_insights_input_v1"
INSIGHTS_DATA_FINGERPRINT_VERSION = "capitalbench_insights_data_fingerprint_v1"
DETERMINISTIC_ENGINE_VERSION = "deterministic_insights_v1"
LLM_PROMPT_VERSION = "capitalbench_insight_llm_prompt_v1"
LLM_OUTPUT_VERSION = "insight_llm_output_v1"
LLM_ENGINE_VERSION = "nvidia_llm_rewrite_v1"
DEFAULT_NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
DEFAULT_NVIDIA_MODEL_ID = "meta/llama-3.1-8b-instruct"
DEFAULT_NVIDIA_TIMEOUT_SECONDS = 180
DEFAULT_NVIDIA_MAX_TOKENS = 2000
DEFAULT_LLM_CANDIDATE_LIMIT = 4
VALID_LLM_MODES = {"auto", "off", "required"}

AUDIENCE_ALL = ["investors", "capital_allocators", "traders", "ai_researchers"]

REGIME_LABELS = {
    "liquidity_defensive": "cash and defensive liquidity",
    "duration_credit": "rates and credit",
    "defensive_equity": "defensive equity",
    "broad_cyclical_equity": "broad and cyclical equity",
    "growth_technology": "growth and technology",
    "international_equity": "international equity",
    "real_assets_inflation": "real assets and inflation",
    "crypto": "crypto",
}


@dataclass(frozen=True)
class InsightsInputOutput:
    output_path: Path
    round_count: int
    portfolio_count: int
    result_count: int


@dataclass(frozen=True)
class InsightsGenerationOutput:
    insights_dir: Path
    run_dir: Path
    latest_path: Path
    index_path: Path
    insight_count: int
    llm_status: str
    llm_model: str | None
    published: bool
    data_fingerprint: str
    skipped_reason: str | None


@dataclass(frozen=True)
class InsightsValidationOutput:
    latest_path: Path
    insight_count: int
    run_count: int


def build_insights_input(
    *,
    rounds_dir: Path,
    output_path: Path,
    run_date: str | None = None,
    generated_at: str | None = None,
    repo_root: Path | None = None,
) -> InsightsInputOutput:
    repo_root = repo_root or Path.cwd()
    generated_at = generated_at or _utc_now()
    run_date = run_date or generated_at[:10]
    snapshot = _build_snapshot(
        rounds_dir=rounds_dir,
        repo_root=repo_root,
        generated_at=generated_at,
        run_date=run_date,
    )
    write_json(output_path, snapshot)
    return InsightsInputOutput(
        output_path=output_path,
        round_count=len(snapshot["rounds"]),
        portfolio_count=sum(len(round_item["portfolios"]) for round_item in snapshot["rounds"]),
        result_count=sum(len(round_item["results"]) for round_item in snapshot["rounds"]),
    )


def generate_insights(
    *,
    input_path: Path,
    output_dir: Path,
    generated_at: str | None = None,
    llm_mode: str = "auto",
    nvidia_api_key: str | None = None,
    nvidia_base_url: str | None = None,
    nvidia_model_id: str | None = None,
    max_llm_candidates: int = DEFAULT_LLM_CANDIDATE_LIMIT,
    llm_client: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    force: bool = False,
) -> InsightsGenerationOutput:
    if llm_mode not in VALID_LLM_MODES:
        raise ValueError(f"llm_mode must be one of: {', '.join(sorted(VALID_LLM_MODES))}")
    snapshot = read_json(input_path)
    generated_at = generated_at or str(snapshot.get("generated_at") or _utc_now())
    run_date = str(snapshot.get("run_date") or generated_at[:10])
    latest_path = output_dir / "latest.json"
    index_path = output_dir / "index.json"
    data_fingerprint = _snapshot_data_fingerprint(snapshot)
    previous_latest = _read_previous_latest(latest_path)
    if not force and _previous_data_fingerprint(previous_latest) == data_fingerprint:
        return InsightsGenerationOutput(
            insights_dir=output_dir,
            run_dir=output_dir / run_date,
            latest_path=latest_path,
            index_path=index_path,
            insight_count=len(previous_latest.get("insights") or []) if isinstance(previous_latest, dict) else 0,
            llm_status="skipped_unchanged",
            llm_model=_resolve_nvidia_model(nvidia_model_id),
            published=False,
            data_fingerprint=data_fingerprint,
            skipped_reason="data_unchanged",
        )

    candidates = build_deterministic_candidates(snapshot, generated_at=generated_at)
    llm_result = _maybe_generate_llm_rewrites(
        snapshot=snapshot,
        candidates=candidates,
        generated_at=generated_at,
        run_date=run_date,
        llm_mode=llm_mode,
        api_key=nvidia_api_key,
        base_url=nvidia_base_url,
        model_id=nvidia_model_id,
        max_candidates=max_llm_candidates,
        llm_client=llm_client,
    )
    public_insights = llm_result["insights"]
    engine_version = (
        f"{DETERMINISTIC_ENGINE_VERSION}+{LLM_ENGINE_VERSION}"
        if llm_result["status"] == "succeeded"
        else DETERMINISTIC_ENGINE_VERSION
    )
    public = {
        "version": INSIGHTS_VERSION,
        "engine_version": engine_version,
        "generated_at": generated_at,
        "run_date": run_date,
        "data_as_of": _snapshot_data_as_of(snapshot),
        "source": {
            "type": "llm_assisted" if llm_result["status"] == "succeeded" else "deterministic",
            "input_version": snapshot.get("version"),
            "capitalbench_generated_at": snapshot.get("generated_at"),
            "data_fingerprint_version": INSIGHTS_DATA_FINGERPRINT_VERSION,
            "data_fingerprint": data_fingerprint,
            "llm": _public_llm_source(llm_result),
        },
        "insight_count": len(public_insights),
        "insights": public_insights,
    }

    run_dir = output_dir / run_date
    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(run_dir / "input.json", snapshot)
    write_json(run_dir / "deterministic_candidates.json", {"insights": candidates})
    if llm_result.get("request") is not None:
        write_json(run_dir / "llm_request.redacted.json", llm_result["request"])
    if llm_result.get("response") is not None:
        write_json(run_dir / "llm_response.json", llm_result["response"])
    write_json(run_dir / "insights.json", public)
    write_json(
        run_dir / "run_manifest.json",
        {
            "version": INSIGHTS_VERSION,
            "engine_version": engine_version,
            "run_date": run_date,
            "generated_at": generated_at,
            "input_path": str(input_path),
            "published": True,
            "data_fingerprint_version": INSIGHTS_DATA_FINGERPRINT_VERSION,
            "data_fingerprint": data_fingerprint,
            "llm_status": llm_result["status"],
            "llm_provider": llm_result.get("provider"),
            "llm_model": llm_result.get("model"),
            "llm_error": llm_result.get("error"),
            "llm_prompt_version": LLM_PROMPT_VERSION if llm_result.get("request") is not None else None,
            "insight_count": len(public_insights),
            "deterministic_candidate_count": len(candidates),
        },
    )
    _write_report(run_dir / "report.md", public)

    write_json(latest_path, public)
    write_json(index_path, _build_index(output_dir, run_date, public))
    return InsightsGenerationOutput(
        insights_dir=output_dir,
        run_dir=run_dir,
        latest_path=latest_path,
        index_path=index_path,
        insight_count=len(public_insights),
        llm_status=llm_result["status"],
        llm_model=llm_result.get("model"),
        published=True,
        data_fingerprint=data_fingerprint,
        skipped_reason=None,
    )


def validate_insights(*, insights_dir: Path) -> InsightsValidationOutput:
    latest_path = insights_dir / "latest.json"
    if not latest_path.exists():
        raise FileNotFoundError(f"missing latest insights file: {latest_path}")
    latest = read_json(latest_path)
    _validate_public_insights(latest, latest_path)
    run_count = 0
    for item in insights_dir.iterdir() if insights_dir.exists() else []:
        if item.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", item.name):
            run_file = item / "insights.json"
            if not run_file.exists():
                raise ValueError(f"missing dated insights artifact: {run_file}")
            _validate_public_insights(read_json(run_file), run_file)
            run_count += 1
    return InsightsValidationOutput(
        latest_path=latest_path,
        insight_count=len(latest.get("insights") or []),
        run_count=run_count,
    )


def build_deterministic_candidates(snapshot: dict[str, Any], *, generated_at: str | None = None) -> list[dict[str, Any]]:
    generated_at = generated_at or str(snapshot.get("generated_at") or _utc_now())
    candidates: list[dict[str, Any]] = []
    candidates.extend(_active_positioning_insights(snapshot, generated_at))
    candidates.extend(_horizon_agreement_insights(snapshot, generated_at))
    candidates.extend(_momentum_exposure_insights(snapshot, generated_at))
    candidates.extend(_model_similarity_insights(snapshot, generated_at))
    candidates.extend(_latest_resolved_track_insights(snapshot, generated_at))
    candidates.extend(_confidence_calibration_insights(snapshot, generated_at))
    candidates.extend(_live_path_insights(snapshot, generated_at))
    deduped = _dedupe_insights(candidates)
    return sorted(
        deduped,
        key=lambda row: (-float(row["importance_score"]), str(row["category"]), str(row["id"])),
    )


def _maybe_generate_llm_rewrites(
    *,
    snapshot: dict[str, Any],
    candidates: list[dict[str, Any]],
    generated_at: str,
    run_date: str,
    llm_mode: str,
    api_key: str | None,
    base_url: str | None,
    model_id: str | None,
    max_candidates: int,
    llm_client: Callable[[dict[str, Any]], dict[str, Any]] | None,
) -> dict[str, Any]:
    model = _resolve_nvidia_model(model_id)
    endpoint_base = (base_url or os.environ.get("NVIDIA_BASE_URL") or DEFAULT_NVIDIA_BASE_URL).rstrip("/")
    key = api_key or os.environ.get("NVIDIA_API_KEY")
    if llm_mode == "off":
        return _llm_result(status="disabled", candidates=candidates, model=model, provider=None)
    if not key and llm_client is None:
        if llm_mode == "required":
            raise ValueError("NVIDIA_API_KEY is required when --llm required is used")
        return _llm_result(status="not_configured", candidates=candidates, model=model, provider=None)

    packet = _llm_input_packet(
        snapshot=snapshot,
        candidates=candidates,
        generated_at=generated_at,
        run_date=run_date,
        model=model,
        max_candidates=max_candidates,
    )
    request_payload = _llm_request_payload(packet=packet, model=model)
    redacted_request = _redacted_llm_request(
        endpoint_base=endpoint_base,
        model=model,
        payload=request_payload,
        packet=packet,
    )
    try:
        raw_response = llm_client(request_payload) if llm_client is not None else _call_nvidia_llm(
            request_payload=request_payload,
            api_key=str(key),
            endpoint_base=endpoint_base,
        )
        output = _extract_llm_json(raw_response)
        insights = _apply_llm_output(candidates=candidates, output=output, model=model)
        return {
            "status": "succeeded",
            "provider": "nvidia_nim",
            "model": model,
            "insights": insights,
            "request": redacted_request,
            "response": _redacted_llm_response(raw_response=raw_response, output=output, status="succeeded"),
            "selected_candidate_ids": output.get("selected_candidate_ids") or [],
            "error": None,
        }
    except Exception as exc:
        if llm_mode == "required":
            raise
        return {
            "status": "failed",
            "provider": "nvidia_nim",
            "model": model,
            "insights": candidates,
            "request": redacted_request,
            "response": _redacted_llm_response(raw_response=None, output=None, status="failed", error=str(exc)),
            "selected_candidate_ids": [],
            "error": str(exc),
        }


def _llm_result(*, status: str, candidates: list[dict[str, Any]], model: str, provider: str | None) -> dict[str, Any]:
    return {
        "status": status,
        "provider": provider,
        "model": model,
        "insights": candidates,
        "request": None,
        "response": None,
        "selected_candidate_ids": [],
        "error": None,
    }


def _resolve_nvidia_model(model_id: str | None = None) -> str:
    return model_id or os.environ.get("NVIDIA_MODEL_ID") or DEFAULT_NVIDIA_MODEL_ID


def _llm_input_packet(
    *,
    snapshot: dict[str, Any],
    candidates: list[dict[str, Any]],
    generated_at: str,
    run_date: str,
    model: str,
    max_candidates: int,
) -> dict[str, Any]:
    selected = candidates[: max(1, max_candidates)]
    latest_rounds = [
        {
            "round_id": round_item["round_id"],
            "track": round_item["track"],
            "status": round_item["status"],
            "decision_date": round_item.get("decision_date"),
            "exit_date": round_item.get("exit_date"),
            "model_count": len(round_item.get("portfolios") or []),
            "result_count": len(round_item.get("results") or []),
        }
        for round_item in sorted(snapshot.get("rounds") or [], key=_round_sort_value, reverse=True)[:8]
    ]
    return {
        "version": "capitalbench_insight_llm_input_v1",
        "prompt_version": LLM_PROMPT_VERSION,
        "run_date": run_date,
        "generated_at": generated_at,
        "data_as_of": _snapshot_data_as_of(snapshot),
        "llm_model": model,
        "benchmark_context": {
            "name": "CapitalBench",
            "description": "The live benchmark for AI capital allocation.",
            "not_financial_advice": True,
            "method": "Frontier AI models receive the same market brief, portfolios are frozen, and results are scored against real market returns.",
        },
        "style_rules": [
            "Use plain English for investors, capital allocators, traders, and AI researchers.",
            "Explain benchmark meaning, not trading advice.",
            "Do not invent facts, causes, market news, or external context.",
            "Do not introduce new numbers. Use only numbers already present in the candidate insight.",
            "Use asset names before tickers, for example Semiconductors (SMH).",
            "Avoid buy, sell, long, short, price-target, or recommendation language.",
            "Rewrite no more than four candidates.",
            "Keep titles under 80 characters.",
            "Keep summaries under 260 characters.",
            "Keep why_it_matters under 240 characters.",
            "Keep titles direct and institutional.",
            "Keep summaries one or two sentences.",
        ],
        "latest_round_context": latest_rounds,
        "candidate_insights": [_compact_candidate_for_llm(candidate) for candidate in selected],
        "required_output_schema": {
            "version": LLM_OUTPUT_VERSION,
            "selected_candidate_ids": ["candidate id strings in preferred display order"],
            "rewrites": [
                {
                    "candidate_id": "candidate id",
                    "title": "optional rewritten title",
                    "summary": "optional rewritten summary",
                    "why_it_matters": "optional rewritten why_it_matters",
                }
            ],
            "rejected_candidate_ids": ["candidate ids that should not be rewritten"],
        },
    }


def _compact_candidate_for_llm(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": candidate["id"],
        "category": candidate["category"],
        "audiences": candidate.get("audiences") or [],
        "importance_score": candidate.get("importance_score"),
        "confidence": candidate.get("confidence"),
        "data_as_of": candidate.get("data_as_of"),
        "title": candidate.get("title"),
        "summary": candidate.get("summary"),
        "why_it_matters": candidate.get("why_it_matters"),
        "calculations": candidate.get("calculations") or [],
        "evidence": candidate.get("evidence") or [],
        "related": candidate.get("related") or [],
    }


def _llm_request_payload(*, packet: dict[str, Any], model: str) -> dict[str, Any]:
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": _llm_system_prompt()},
            {
                "role": "user",
                "content": json.dumps(packet, sort_keys=True, separators=(",", ":")),
            },
        ],
        "temperature": 0,
        "top_p": 1,
        "max_tokens": DEFAULT_NVIDIA_MAX_TOKENS,
        "stream": False,
        "response_format": {"type": "json_object"},
    }


def _llm_system_prompt() -> str:
    return (
        "You are the CapitalBench insight editor. Rewrite deterministic benchmark insights for clarity. "
        "Return only valid JSON matching the requested schema. Do not use markdown. Do not add facts, "
        "causes, market commentary, or numbers that are not already present in the candidate. Do not give "
        "investment advice or trade recommendations. Keep all evidence, calculations, and benchmark meaning intact. "
        "Keep the JSON compact: at most four rewrite objects, with short title, summary, and why_it_matters strings."
    )


def _call_nvidia_llm(*, request_payload: dict[str, Any], api_key: str, endpoint_base: str) -> dict[str, Any]:
    body = json.dumps(request_payload).encode("utf-8")
    request = urllib.request.Request(
        f"{endpoint_base}/chat/completions",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=DEFAULT_NVIDIA_TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"NVIDIA LLM request failed with HTTP {exc.code}: {_truncate(detail, 500)}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"NVIDIA LLM request failed: {exc.reason}") from exc


def _extract_llm_json(raw_response: dict[str, Any]) -> dict[str, Any]:
    if raw_response.get("version") == LLM_OUTPUT_VERSION:
        output = raw_response
    else:
        choices = raw_response.get("choices")
        if not isinstance(choices, list) or not choices:
            raise ValueError("NVIDIA response did not include choices")
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str) or not content.strip():
            raise ValueError("NVIDIA response did not include message content")
        output = _parse_json_content(content)
    output = _normalize_llm_output(output)
    if output.get("version") != LLM_OUTPUT_VERSION:
        raise ValueError("LLM output version is invalid")
    if not isinstance(output.get("selected_candidate_ids"), list):
        raise ValueError("LLM output selected_candidate_ids must be a list")
    if not isinstance(output.get("rewrites"), list):
        raise ValueError("LLM output rewrites must be a list")
    if not isinstance(output.get("rejected_candidate_ids", []), list):
        raise ValueError("LLM output rejected_candidate_ids must be a list")
    return output


def _normalize_llm_output(output: dict[str, Any]) -> dict[str, Any]:
    if output.get("version") == LLM_OUTPUT_VERSION:
        return output
    rewrites = output.get("rewrites")
    if output.get("version") is not None or not isinstance(rewrites, list):
        return output
    normalized = dict(output)
    selected_ids = [
        rewrite.get("candidate_id")
        for rewrite in rewrites
        if isinstance(rewrite, dict) and isinstance(rewrite.get("candidate_id"), str)
    ]
    normalized["version"] = LLM_OUTPUT_VERSION
    normalized.setdefault("selected_candidate_ids", selected_ids)
    normalized.setdefault("rejected_candidate_ids", [])
    return normalized


def _parse_json_content(content: str) -> dict[str, Any]:
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"LLM output was not valid JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("LLM output JSON must be an object")
    return parsed


def _apply_llm_output(*, candidates: list[dict[str, Any]], output: dict[str, Any], model: str) -> list[dict[str, Any]]:
    by_id = {candidate["id"]: candidate for candidate in candidates}
    referenced = set(output.get("selected_candidate_ids") or []) | set(output.get("rejected_candidate_ids") or [])
    for rewrite in output.get("rewrites") or []:
        if not isinstance(rewrite, dict):
            raise ValueError("LLM rewrite entries must be objects")
        referenced.add(str(rewrite.get("candidate_id") or ""))
    unknown = sorted(candidate_id for candidate_id in referenced if candidate_id not in by_id)
    if unknown:
        raise ValueError(f"LLM output referenced unknown candidate ids: {', '.join(unknown)}")

    rewrites = {rewrite["candidate_id"]: rewrite for rewrite in output.get("rewrites") or [] if rewrite.get("candidate_id") in by_id}
    rewritten = []
    for candidate in candidates:
        rewrite = rewrites.get(candidate["id"])
        if not rewrite:
            rewritten.append(candidate)
            continue
        updated = dict(candidate)
        changed = False
        for field in ["title", "summary", "why_it_matters"]:
            value = rewrite.get(field)
            if value is None:
                continue
            text = str(value).strip()
            if not text:
                raise ValueError(f"LLM rewrite for {candidate['id']} has blank {field}")
            _validate_llm_rewrite_text(candidate, text, field)
            updated[field] = text
            changed = True
        if changed:
            updated["source_type"] = "llm_assisted"
            updated["llm_assisted_by"] = {
                "provider": "nvidia_nim",
                "model": model,
                "prompt_version": LLM_PROMPT_VERSION,
                "candidate_id": candidate["id"],
            }
        rewritten.append(updated)
    return rewritten


def _validate_llm_rewrite_text(candidate: dict[str, Any], text: str, field: str) -> None:
    lowered = text.lower()
    if re.search(r"\b(buy|sell|price target|trade signal|recommend(?:ed|s|ing)? buying|recommend(?:ed|s|ing)? selling|go long|go short)\b", lowered):
        raise ValueError(f"LLM rewrite for {candidate['id']} contains investment-action language")
    allowed_numbers = _allowed_candidate_numbers(candidate)
    for number in _normalized_numbers(text):
        if number not in allowed_numbers:
            raise ValueError(f"LLM rewrite for {candidate['id']} introduced unsupported number {number} in {field}")


def _allowed_candidate_numbers(candidate: dict[str, Any]) -> set[str]:
    allowed = _normalized_numbers(json.dumps(_compact_candidate_for_llm(candidate), sort_keys=True))
    for calculation in candidate.get("calculations") or []:
        value = calculation.get("value")
        if isinstance(value, (int, float)) and math.isfinite(float(value)):
            unit = str(calculation.get("unit") or "").lower()
            for digits in [0, 1, 2, 4]:
                allowed.add(_normalize_number_token(f"{float(value):.{digits}f}"))
                allowed.add(_normalize_number_token(f"{float(value):+.{digits}f}"))
                if unit in {"percent", "percentage_points"}:
                    allowed.add(_normalize_number_token(f"{float(value):.{digits}f}%"))
                    allowed.add(_normalize_number_token(f"{float(value):+.{digits}f}%"))
    return {number for number in allowed if number}


def _normalized_numbers(text: str) -> set[str]:
    return {number for number in (_normalize_number_token(match.group(0)) for match in re.finditer(r"[-+]?\d+(?:,\d{3})*(?:\.\d+)?%?", text)) if number}


def _normalize_number_token(token: str) -> str:
    value = token.strip().replace(",", "").replace("%", "")
    if value.startswith("+"):
        value = value[1:]
    if value in {"", "-", "."}:
        return ""
    try:
        number = float(value)
    except ValueError:
        return value
    if number == 0:
        number = 0.0
    formatted = f"{number:.6f}".rstrip("0").rstrip(".")
    return formatted or "0"


def _redacted_llm_request(*, endpoint_base: str, model: str, payload: dict[str, Any], packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "version": "capitalbench_llm_request_redacted_v1",
        "provider": "nvidia_nim",
        "endpoint_host": endpoint_base,
        "endpoint_path": "/chat/completions",
        "model": model,
        "prompt_version": LLM_PROMPT_VERSION,
        "system_prompt": payload["messages"][0]["content"],
        "input_packet": packet,
        "input_sha256": _sha256_json(packet),
        "request_parameters": {
            "temperature": payload.get("temperature"),
            "top_p": payload.get("top_p"),
            "max_tokens": payload.get("max_tokens"),
            "stream": payload.get("stream"),
            "response_format": payload.get("response_format"),
        },
        "authorization": "redacted",
    }


def _redacted_llm_response(
    *,
    raw_response: dict[str, Any] | None,
    output: dict[str, Any] | None,
    status: str,
    error: str | None = None,
) -> dict[str, Any]:
    payload = {
        "version": "capitalbench_llm_response_v1",
        "status": status,
        "provider": "nvidia_nim",
        "prompt_version": LLM_PROMPT_VERSION,
        "output": output,
        "error": error,
    }
    if raw_response is not None:
        payload["response"] = {
            "id": raw_response.get("id"),
            "model": raw_response.get("model"),
            "created": raw_response.get("created"),
            "usage": raw_response.get("usage"),
            "finish_reason": (raw_response.get("choices") or [{}])[0].get("finish_reason") if isinstance(raw_response.get("choices"), list) else None,
        }
    return payload


def _public_llm_source(llm_result: dict[str, Any]) -> dict[str, Any]:
    return {
        "provider": llm_result.get("provider"),
        "model": llm_result.get("model"),
        "status": llm_result.get("status"),
        "prompt_version": LLM_PROMPT_VERSION if llm_result.get("request") is not None else None,
        "selected_candidate_ids": llm_result.get("selected_candidate_ids") or [],
    }


def _sha256_json(payload: dict[str, Any]) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def _snapshot_data_fingerprint(snapshot: dict[str, Any]) -> str:
    stable_payload = {
        "version": snapshot.get("version"),
        "asset_risk_model": snapshot.get("asset_risk_model"),
        "rounds": snapshot.get("rounds") or [],
    }
    return _sha256_json(stable_payload)


def _read_previous_latest(latest_path: Path) -> dict[str, Any] | None:
    if not latest_path.exists():
        return None
    try:
        latest = read_json(latest_path)
    except Exception:
        return None
    return latest if isinstance(latest, dict) else None


def _previous_data_fingerprint(latest: dict[str, Any] | None) -> str | None:
    if not isinstance(latest, dict):
        return None
    source = latest.get("source")
    if not isinstance(source, dict):
        return None
    value = source.get("data_fingerprint")
    return value if isinstance(value, str) and value else None


def _truncate(value: str, limit: int) -> str:
    return value if len(value) <= limit else f"{value[:limit]}..."


def _build_snapshot(*, rounds_dir: Path, repo_root: Path, generated_at: str, run_date: str) -> dict[str, Any]:
    asset_risk = _load_asset_risk(repo_root)
    rounds: list[dict[str, Any]] = []
    for round_path in discover_rounds(rounds_dir):
        round_item = _round_snapshot(round_path, asset_risk)
        if round_item is not None:
            rounds.append(round_item)
    rounds.sort(key=lambda row: _round_sort_value(row))
    return {
        "version": INSIGHTS_INPUT_VERSION,
        "generated_at": generated_at,
        "run_date": run_date,
        "source": {
            "rounds_dir": str(rounds_dir),
            "repo_root": str(repo_root),
        },
        "asset_risk_model": {
            "version": asset_risk.get("version"),
            "published_at": asset_risk.get("published_at"),
            "regime_groups": asset_risk.get("regime_groups") or {},
        },
        "rounds": rounds,
    }


def _round_snapshot(round_path: Path, asset_risk: dict[str, Any]) -> dict[str, Any] | None:
    try:
        manifest = load_manifest(round_path)
    except Exception:
        return None
    selected_run_id = _select_official_run_id(round_path)
    if selected_run_id is None:
        return None
    run_paths = get_run_paths(round_path, selected_run_id)
    run_manifest = read_run_manifest(run_paths)
    leaderboard_path = run_paths.results_dir / "leaderboard.csv"
    status = "resolved" if leaderboard_path.exists() else "active"
    options = _option_rows(round_path, asset_risk)
    options_by_id = {row["option_id"]: row for row in options}
    returns = _returns_rows(run_paths, options_by_id)
    return_by_option = {row["option_id"]: row["return"] for row in returns if _finite(row.get("return"))}
    portfolios = _portfolio_rows(run_paths, options_by_id, return_by_option)
    return {
        "round_id": manifest.round_id,
        "track": _track_from_manifest(manifest),
        "status": status,
        "title": manifest.title,
        "decision_date": _text(manifest.decision_date),
        "decision_deadline_utc": _text(manifest.decision_deadline),
        "entry_date": _text(manifest.entry_date),
        "exit_date": _text(manifest.exit_date),
        "horizon": manifest.horizon,
        "methodology_version": _text(manifest.methodology_version),
        "universe_version": _text(manifest.universe_version),
        "submission_format": manifest.submission_format,
        "run_id": selected_run_id,
        "run_manifest": {
            "run_type": run_manifest.get("run_type"),
            "mock": bool(run_manifest.get("mock")),
            "operator_selected_official": bool(run_manifest.get("operator_selected_official")),
            "accepted_at_utc": _text(run_manifest.get("accepted_at_utc")),
            "resolution_due_at_utc": _text(run_manifest.get("resolution_due_at_utc")),
            "model_count": _optional_int(run_manifest.get("model_count")),
            "valid_submissions": _optional_int(run_manifest.get("valid_submissions")),
            "invalid_submissions": _optional_int(run_manifest.get("invalid_submissions")),
        },
        "options": options,
        "portfolios": portfolios,
        "results": _result_rows(run_paths, returns, portfolios, options_by_id),
        "returns": returns,
        "allocations": _result_allocation_rows(run_paths, options_by_id),
        "interim_performance": _interim_rows(run_paths),
        "trailing_returns": _trailing_return_rows(round_path, options_by_id),
    }


def _select_official_run_id(round_path: Path) -> str | None:
    candidates: list[tuple[int, str, dict[str, Any]]] = []
    for run_id in list_run_ids(round_path):
        run_paths = get_run_paths(round_path, run_id)
        manifest = read_run_manifest(run_paths)
        if manifest.get("run_type") != "official":
            continue
        if manifest.get("mock") is True:
            continue
        if not bool(manifest.get("official_score_eligible")):
            continue
        score = 0
        if manifest.get("operator_selected_official") is True:
            score += 100
        if manifest.get("accepted_at_utc"):
            score += 20
        if (run_paths.results_dir / "leaderboard.csv").exists():
            score += 10
        candidates.append((score, run_id, manifest))
    if not candidates:
        return None
    candidates.sort(key=lambda item: (-item[0], str(item[2].get("created_at_utc") or ""), item[1]))
    return candidates[0][1]


def _option_rows(round_path: Path, asset_risk: dict[str, Any]) -> list[dict[str, Any]]:
    if not (round_path / "options.yaml").exists():
        return []
    definitions = asset_risk.get("assets") or {}
    rows = []
    for option in load_options(round_path):
        definition = definitions.get(option.option_id) or {}
        rows.append(
            {
                "option_id": option.option_id,
                "label": option.label,
                "ticker": option.symbol,
                "asset_class": option.asset_class,
                "category": option.category,
                "option_group": option.option_group,
                "risk_bucket": option.risk_bucket,
                "is_cash": option.is_cash,
                "is_benchmark": option.is_benchmark or option.option_id == "SP500",
                "risk_score_1_5": _optional_float(definition.get("risk_score_1_5")),
                "risk_on_loading": _optional_float(definition.get("risk_on_loading")),
                "regime_group": _text(definition.get("regime_group")),
            }
        )
    return rows


def _portfolio_rows(
    run_paths,
    options_by_id: dict[str, dict[str, Any]],
    return_by_option: dict[str, float],
) -> list[dict[str, Any]]:
    rows = []
    if not run_paths.parsed_dir.exists():
        return rows
    for parsed_file in sorted(run_paths.parsed_dir.glob("*.json")):
        payload = read_json(parsed_file)
        allocations = _submission_allocations(payload)
        model_return = _weighted_return(allocations, return_by_option)
        rows.append(
            {
                "round_id": _text(payload.get("round_id")) or run_paths.round_path.name,
                "run_id": run_paths.run_id,
                "model_id": _text(payload.get("model_id")) or parsed_file.stem,
                "provider": _text(payload.get("provider")),
                "mode": _text(payload.get("mode")),
                "run_type": _text(payload.get("run_type")),
                "selected_option_id": _text(payload.get("selected_option_id")) or _primary_option_id(allocations),
                "holding_count": len(allocations),
                "confidence": _optional_float(payload.get("confidence")),
                "rationale_summary": _text(payload.get("rationale_summary")),
                "portfolio_rationale": _text(payload.get("portfolio_rationale")),
                "key_risks": [_text(item) for item in payload.get("key_risks") or [] if _text(item)],
                "usage": payload.get("usage") if isinstance(payload.get("usage"), dict) else {},
                "allocations": [_enrich_allocation(item, options_by_id) for item in allocations],
                "model_return": model_return,
            }
        )
    return rows


def _submission_allocations(payload: dict[str, Any]) -> list[dict[str, Any]]:
    raw_portfolio = payload.get("portfolio")
    if isinstance(raw_portfolio, list) and raw_portfolio:
        return [
            {
                "option_id": _text(item.get("option_id")),
                "allocation_pct": _optional_float(item.get("allocation_pct")) or 0.0,
                "rationale": _text(item.get("rationale")),
            }
            for item in raw_portfolio
            if _text(item.get("option_id"))
        ]
    selected = _text(payload.get("selected_option_id"))
    if not selected:
        return []
    return [
        {
            "option_id": selected,
            "allocation_pct": 100.0,
            "rationale": _text(payload.get("rationale_summary")),
        }
    ]


def _enrich_allocation(item: dict[str, Any], options_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    option = options_by_id.get(str(item["option_id"])) or {}
    allocation_pct = _optional_float(item.get("allocation_pct")) or 0.0
    option_return = _optional_float(item.get("option_return"))
    return {
        "option_id": item["option_id"],
        "label": option.get("label") or item["option_id"],
        "ticker": option.get("ticker"),
        "category": option.get("category"),
        "regime_group": option.get("regime_group"),
        "risk_on_loading": option.get("risk_on_loading"),
        "allocation_pct": allocation_pct,
        "rationale": _text(item.get("rationale")),
        "option_return": option_return,
        "return_contribution": _optional_float(item.get("return_contribution")),
    }


def _returns_rows(run_paths, options_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    path = run_paths.results_dir / "returns.csv"
    rows = []
    if not path.exists():
        return rows
    for raw in _read_csv(path):
        option_id = _text(raw.get("option_id"))
        option = options_by_id.get(option_id) or {}
        rows.append(
            {
                "option_id": option_id,
                "label": _text(raw.get("label")) or option.get("label") or option_id,
                "ticker": _text(raw.get("asset_symbol")) or option.get("ticker"),
                "return": _optional_float(raw.get("return")),
                "rank": _optional_int(raw.get("rank")),
                "is_benchmark": _bool(raw.get("is_benchmark")) or option_id == "SP500",
                "is_cash": _bool(raw.get("is_cash")),
                "category": option.get("category"),
                "regime_group": option.get("regime_group"),
            }
        )
    return rows


def _result_rows(
    run_paths,
    returns: list[dict[str, Any]],
    portfolios: list[dict[str, Any]],
    options_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    path = run_paths.results_dir / "leaderboard.csv"
    if not path.exists():
        return []
    oracle_return = _oracle_return(returns)
    portfolio_by_model = {row["model_id"]: row for row in portfolios}
    rows = []
    for raw in _read_csv(path):
        model_id = _text(raw.get("model_id"))
        portfolio_return = _optional_float(raw.get("portfolio_return"))
        if portfolio_return is None:
            portfolio_return = _optional_float(raw.get("selected_asset_return"))
        sp500_return = _optional_float(raw.get("sp500_return"))
        selected_option_id = _text(raw.get("selected_option_id"))
        option = options_by_id.get(selected_option_id) or {}
        rows.append(
            {
                "round_id": _text(raw.get("round_id")) or run_paths.round_path.name,
                "run_id": run_paths.run_id,
                "model_id": model_id,
                "provider": _text(raw.get("provider")),
                "selected_option_id": selected_option_id,
                "selected_label": option.get("label") or selected_option_id,
                "selected_ticker": option.get("ticker"),
                "confidence": _optional_float(raw.get("confidence")),
                "rationale_summary": _text(raw.get("rationale_summary")),
                "key_risks": _split_risks(raw.get("key_risks")),
                "portfolio_return": portfolio_return,
                "sp500_return": sp500_return,
                "alpha_vs_sp500": _optional_float(raw.get("alpha_vs_sp500")),
                "regret_vs_best_option": _optional_float(raw.get("regret_vs_best_option")),
                "rank_among_options": _optional_int(raw.get("rank_among_options")),
                "holding_count": _optional_int(raw.get("holding_count")),
                "concentration_hhi": _optional_float(raw.get("concentration_hhi")),
                "beats_sp500": _bool(raw.get("beats_sp500")),
                "beats_cash": _bool(raw.get("beats_cash")),
                "cost_usd": _optional_float(raw.get("cost_usd")),
                "capitalbench_score": _capitalbench_score(portfolio_return, oracle_return),
                "allocations": portfolio_by_model.get(model_id, {}).get("allocations", []),
            }
        )
    rows.sort(key=lambda row: (-(row.get("portfolio_return") or -999), row.get("model_id") or ""))
    for index, row in enumerate(rows, start=1):
        row["rank"] = index
    return rows


def _result_allocation_rows(run_paths, options_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    path = run_paths.results_dir / "allocations.csv"
    if not path.exists():
        return []
    rows = []
    for raw in _read_csv(path):
        option_id = _text(raw.get("option_id"))
        option = options_by_id.get(option_id) or {}
        rows.append(
            {
                "round_id": _text(raw.get("round_id")) or run_paths.round_path.name,
                "run_id": run_paths.run_id,
                "model_id": _text(raw.get("model_id")),
                "provider": _text(raw.get("provider")),
                "option_id": option_id,
                "label": option.get("label") or option_id,
                "ticker": option.get("ticker"),
                "category": option.get("category"),
                "regime_group": option.get("regime_group"),
                "allocation_pct": _optional_float(raw.get("allocation_pct")),
                "allocation_rank": _optional_int(raw.get("allocation_rank")),
                "option_return": _optional_float(raw.get("option_return")),
                "return_contribution": _optional_float(raw.get("return_contribution")),
                "rationale": _text(raw.get("rationale")),
            }
        )
    return rows


def _interim_rows(run_paths) -> list[dict[str, Any]]:
    path = run_paths.results_dir / "weekly_performance.csv"
    if not path.exists():
        return []
    rows = []
    for raw in _read_csv(path):
        rows.append(
            {
                "round_id": _text(raw.get("round_id")) or run_paths.round_path.name,
                "run_id": _text(raw.get("run_id")) or run_paths.run_id,
                "model_id": _text(raw.get("model_id")),
                "provider": _text(raw.get("provider")),
                "target_date": _text(raw.get("target_date")),
                "price_date": _text(raw.get("price_date")),
                "days_elapsed": _optional_int(raw.get("days_elapsed")),
                "model_return": _optional_float(raw.get("model_return")),
                "sp500_return": _optional_float(raw.get("sp500_return")),
                "alpha_vs_sp500": _optional_float(raw.get("alpha_vs_sp500")),
                "price_status": _text(raw.get("price_status")),
                "published": _bool(raw.get("published")),
            }
        )
    return rows


def _trailing_return_rows(round_path: Path, options_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    path = round_path / "market_data" / "universe_trailing_returns.json"
    if not path.exists():
        return []
    payload = read_json(path)
    rows = []
    for raw in payload.get("rows") or []:
        option_id = _text(raw.get("option_id"))
        option = options_by_id.get(option_id) or {}
        rows.append(
            {
                "option_id": option_id,
                "label": _text(raw.get("name")) or option.get("label") or option_id,
                "ticker": _text(raw.get("symbol")) or option.get("ticker"),
                "return_7d": _optional_float(raw.get("return_7d")),
                "return_30d": _optional_float(raw.get("return_30d")),
                "return_6m": _optional_float(raw.get("return_6m")),
                "return_1y": _optional_float(raw.get("return_1y")),
                "status": _text(raw.get("status")),
            }
        )
    return rows


def _active_positioning_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    current_rounds = _current_active_rounds(snapshot)
    portfolios = [portfolio for round_item in current_rounds for portfolio in round_item["portfolios"]]
    if not portfolios:
        return []
    allocation = _aggregate_allocations(portfolios)
    top_option_id, top_allocation = allocation[0]
    top_option = _find_option(current_rounds, top_option_id)
    risk_score = _average([_portfolio_risk_score(portfolio) for portfolio in portfolios])
    label = _risk_label(risk_score)
    data_as_of = max((_round_date(round_item) for round_item in current_rounds), default=_snapshot_data_as_of(snapshot))
    evidence = [
        {"label": f"{_track_label(round_item['track'])} live round", "href": f"/rounds/{round_item['round_id']}", "source": f"rounds/{round_item['round_id']}"}
        for round_item in current_rounds
    ]
    top_name = _asset_name(top_option)
    insights = [
        _insight(
            insight_id=f"active-positioning-{_slug(data_as_of)}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="current_positioning",
            audiences=["investors", "capital_allocators", "traders"],
            title=f"Live AI portfolios are concentrated in {top_name}",
            summary=(
                f"Across the newest live weekly and monthly portfolios, {top_name} is the largest aggregate "
                f"allocation at {_fmt_pct(top_allocation / 100)}."
            ),
            why=(
                "This shows the current crowding point in model capital allocation, before the open rounds receive "
                "their final market scores."
            ),
            importance=88 if top_allocation >= 30 else 78,
            calculations=[
                {
                    "name": "aggregate_live_allocation",
                    "value": round(top_allocation, 4),
                    "unit": "percentage_points",
                    "formula": "average allocation across newest live model portfolios",
                }
            ],
            evidence=evidence,
            related=[{"label": "AI Risk Appetite", "href": "/risk-appetite"}],
        )
    ]
    if risk_score is not None:
        insights.append(
            _insight(
                insight_id=f"active-risk-{_slug(data_as_of)}",
                generated_at=generated_at,
                data_as_of=data_as_of,
                category="risk_regime",
                audiences=["investors", "capital_allocators", "traders"],
                title=f"Live AI risk posture is {label.lower()}",
                summary=(
                    f"The newest live portfolios have a deterministic risk-taking score of "
                    f"{risk_score:.1f} out of 100."
                ),
                why=(
                    "The score translates allocations into a common risk scale, so readers can see whether models "
                    "are collectively leaning defensive, balanced, or aggressive."
                ),
                importance=86,
                calculations=[
                    {
                        "name": "live_risk_taking_score",
                        "value": round(risk_score, 4),
                        "unit": "points",
                        "formula": "50 + 50 * weighted average asset risk-on loading",
                    }
                ],
                evidence=evidence,
                related=[{"label": "AI Risk Appetite", "href": "/risk-appetite"}],
            )
        )
    return insights


def _horizon_agreement_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    current = _current_active_rounds(snapshot)
    by_track = {round_item["track"]: round_item for round_item in current}
    weekly = by_track.get("weekly")
    monthly = by_track.get("monthly")
    if not weekly or not monthly:
        return []
    weekly_regime = _top_regime(weekly["portfolios"])
    monthly_regime = _top_regime(monthly["portfolios"])
    if not weekly_regime or not monthly_regime:
        return []
    data_as_of = max(_round_date(weekly), _round_date(monthly))
    if weekly_regime[0] == monthly_regime[0]:
        title = f"Weekly and monthly AI portfolios both favor {REGIME_LABELS.get(weekly_regime[0], weekly_regime[0])}"
        summary = (
            f"The newest weekly portfolios allocate {_fmt_pct(weekly_regime[1] / 100)} to "
            f"{REGIME_LABELS.get(weekly_regime[0], weekly_regime[0])}, while the newest monthly portfolios allocate "
            f"{_fmt_pct(monthly_regime[1] / 100)}."
        )
        why = "Agreement across horizons signals that the current model posture is not just a short-term tactical move."
        importance = 84
    else:
        title = "Weekly and monthly AI portfolios point to different regimes"
        summary = (
            f"The newest weekly portfolios lean toward {REGIME_LABELS.get(weekly_regime[0], weekly_regime[0])}, "
            f"while the newest monthly portfolios lean toward {REGIME_LABELS.get(monthly_regime[0], monthly_regime[0])}."
        )
        why = "A horizon split helps readers separate short-window positioning from the longer one-month model view."
        importance = 82
    return [
        _insight(
            insight_id=f"horizon-agreement-{_slug(data_as_of)}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="horizon_agreement",
            audiences=["investors", "capital_allocators", "traders", "ai_researchers"],
            title=title,
            summary=summary,
            why=why,
            importance=importance,
            calculations=[
                {
                    "name": "weekly_top_regime_allocation",
                    "value": round(weekly_regime[1], 4),
                    "unit": "percentage_points",
                    "formula": "average weekly allocation by asset-risk regime",
                },
                {
                    "name": "monthly_top_regime_allocation",
                    "value": round(monthly_regime[1], 4),
                    "unit": "percentage_points",
                    "formula": "average monthly allocation by asset-risk regime",
                },
            ],
            evidence=[
                {"label": "Weekly live round", "href": f"/rounds/{weekly['round_id']}", "source": f"rounds/{weekly['round_id']}"},
                {"label": "Monthly live round", "href": f"/rounds/{monthly['round_id']}", "source": f"rounds/{monthly['round_id']}"},
            ],
            related=[{"label": "AI Risk Appetite", "href": "/risk-appetite"}],
        )
    ]


def _momentum_exposure_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    insights = []
    for round_item in _current_active_rounds(snapshot):
        trailing = [row for row in round_item["trailing_returns"] if _finite(row.get("return_30d"))]
        if len(trailing) < 10 or not round_item["portfolios"]:
            continue
        top_count = max(1, math.ceil(len(trailing) * 0.2))
        ranked_30d = sorted(trailing, key=lambda row: row["return_30d"], reverse=True)
        top_ids = {row["option_id"] for row in ranked_30d[:top_count]}
        bottom_ids = {row["option_id"] for row in ranked_30d[-top_count:]}
        top_allocation = _allocation_to_ids(round_item["portfolios"], top_ids)
        bottom_allocation = _allocation_to_ids(round_item["portfolios"], bottom_ids)
        top_asset = _asset_name(_find_option([round_item], ranked_30d[0]["option_id"]))
        data_as_of = _round_date(round_item)
        insights.append(
            _insight(
                insight_id=f"momentum-exposure-{round_item['round_id']}",
                generated_at=generated_at,
                data_as_of=data_as_of,
                category="model_behavior",
                audiences=["traders", "ai_researchers", "capital_allocators"],
                title=f"{_track_label(round_item['track'])} models are leaning into recent winners",
                summary=(
                    f"The newest {_track_label(round_item['track']).lower()} portfolios allocate "
                    f"{_fmt_pct(top_allocation / 100)} to the top 20% of assets by prior 30-day return. "
                    f"The strongest 30-day asset in the input table was {top_asset}."
                ),
                why=(
                    "This measures whether models are chasing recent momentum or allocating away from it before outcomes "
                    "are known."
                ),
                importance=80 if top_allocation >= 50 else 68,
                calculations=[
                    {
                        "name": "allocation_to_top_30d_momentum_quintile",
                        "value": round(top_allocation, 4),
                        "unit": "percentage_points",
                        "formula": "average allocation to assets in the top 20% by pre-run 30-day trailing return",
                    },
                    {
                        "name": "allocation_to_bottom_30d_momentum_quintile",
                        "value": round(bottom_allocation, 4),
                        "unit": "percentage_points",
                        "formula": "average allocation to assets in the bottom 20% by pre-run 30-day trailing return",
                    },
                ],
                evidence=[
                    {"label": f"{_track_label(round_item['track'])} round", "href": f"/rounds/{round_item['round_id']}", "source": f"rounds/{round_item['round_id']}/market_data/universe_trailing_returns.json"}
                ],
                related=[{"label": "Round list", "href": "/rounds"}],
            )
        )
    return insights


def _model_similarity_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    current = _current_active_rounds(snapshot)
    model_vectors: dict[str, dict[str, float]] = {}
    model_counts: dict[str, int] = {}
    for round_item in current:
        for portfolio in round_item["portfolios"]:
            vector = model_vectors.setdefault(portfolio["model_id"], {})
            model_counts[portfolio["model_id"]] = model_counts.get(portfolio["model_id"], 0) + 1
            for allocation in portfolio["allocations"]:
                vector[allocation["option_id"]] = vector.get(allocation["option_id"], 0.0) + float(allocation["allocation_pct"])
    if len(model_vectors) < 3:
        return []
    for model_id, vector in model_vectors.items():
        count = max(1, model_counts.get(model_id, 1))
        for option_id in list(vector):
            vector[option_id] = vector[option_id] / count
    pairs = []
    for left_id in sorted(model_vectors):
        for right_id in sorted(model_vectors):
            if left_id >= right_id:
                continue
            pairs.append((left_id, right_id, _cosine_similarity(model_vectors[left_id], model_vectors[right_id])))
    if not pairs:
        return []
    closest = max(pairs, key=lambda item: item[2])
    avg_distance = {}
    for model_id in model_vectors:
        similarities = [score for left, right, score in pairs if left == model_id or right == model_id]
        avg_distance[model_id] = 1 - _average(similarities) if similarities else 0
    outlier = max(avg_distance.items(), key=lambda item: item[1])
    data_as_of = max((_round_date(round_item) for round_item in current), default=_snapshot_data_as_of(snapshot))
    return [
        _insight(
            insight_id=f"model-similarity-{_slug(data_as_of)}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="model_similarity",
            audiences=["ai_researchers", "capital_allocators"],
            title="Live model portfolios are tightly clustered",
            summary=(
                f"The closest live allocation pair is {_model_label(closest[0])} and {_model_label(closest[1])} "
                f"with {_fmt_pct(closest[2])} cosine similarity. The current allocation outlier is {_model_label(outlier[0])}."
            ),
            why=(
                "Similarity analysis shows whether models are independently converging on the same portfolio or expressing "
                "meaningfully different capital-allocation behavior."
            ),
            importance=76,
            calculations=[
                {
                    "name": "closest_pair_cosine_similarity",
                    "value": round(closest[2], 4),
                    "unit": "ratio",
                    "formula": "cosine similarity between live allocation vectors",
                },
                {
                    "name": "outlier_average_distance",
                    "value": round(outlier[1], 4),
                    "unit": "ratio",
                    "formula": "1 - average cosine similarity versus other live model allocation vectors",
                },
            ],
            evidence=[
                {"label": "Models", "href": "/models", "source": "live parsed submissions"}
            ],
            related=[{"label": "AI Risk Appetite", "href": "/risk-appetite"}],
        )
    ]


def _latest_resolved_track_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    insights = []
    for track, round_item in _latest_resolved_by_track(snapshot).items():
        insights.extend(_consensus_performance_insight(round_item, generated_at))
        insights.extend(_benchmark_difficulty_insight(round_item, generated_at))
        insights.extend(_missed_oracle_insight(round_item, generated_at))
        insights.extend(_attribution_insight(round_item, generated_at))
    return insights


def _consensus_performance_insight(round_item: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    if not round_item["results"] or not round_item["returns"]:
        return []
    returns = {row["option_id"]: row["return"] for row in round_item["returns"] if _finite(row.get("return"))}
    consensus_allocations = _aggregate_allocations(round_item["portfolios"])
    consensus_return = sum((allocation_pct / 100) * returns.get(option_id, 0.0) for option_id, allocation_pct in consensus_allocations)
    sp500_return = _sp500_return(round_item)
    oracle_return = _oracle_return(round_item["returns"])
    avg_model_return = _average([row.get("portfolio_return") for row in round_item["results"]])
    consensus_score = _capitalbench_score(consensus_return, oracle_return)
    data_as_of = _round_date(round_item, prefer_exit=True)
    return [
        _insight(
            insight_id=f"consensus-performance-{round_item['round_id']}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="consensus_performance",
            audiences=["investors", "capital_allocators", "traders", "ai_researchers"],
            title=f"AI consensus portfolio scored {consensus_score:.1f} versus the oracle" if consensus_score is not None else "AI consensus portfolio is now measurable",
            summary=(
                f"If the {_track_label(round_item['track']).lower()} model allocations were averaged into one consensus "
                f"portfolio, it returned {_fmt_pct(consensus_return)} versus {_fmt_pct(sp500_return)} for the S&P 500 "
                f"and {_fmt_pct(oracle_return)} for the hindsight best asset."
            ),
            why=(
                "The consensus portfolio tests whether the combined AI view is more useful than any single model's "
                "portfolio or the S&P 500 benchmark."
            ),
            importance=92,
            calculations=[
                {
                    "name": "consensus_portfolio_return",
                    "value": round(consensus_return * 100, 4),
                    "unit": "percent",
                    "formula": "sum(average_model_allocation * asset_return)",
                },
                {
                    "name": "average_model_return",
                    "value": round((avg_model_return or 0) * 100, 4),
                    "unit": "percent",
                    "formula": "average resolved model portfolio return",
                },
                {
                    "name": "consensus_capitalbench_score",
                    "value": None if consensus_score is None else round(consensus_score, 4),
                    "unit": "points",
                    "formula": "100 * consensus_return / oracle_return",
                },
            ],
            evidence=[
                {"label": f"{_track_label(round_item['track'])} result", "href": f"/rounds/{round_item['round_id']}", "source": f"rounds/{round_item['round_id']}/runs/{round_item['run_id']}/results"}
            ],
            related=[{"label": f"Latest {_track_label(round_item['track']).lower()} results", "href": f"/leaderboards/latest-{round_item['track']}"}],
        )
    ]


def _benchmark_difficulty_insight(round_item: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    returns = [row for row in round_item["returns"] if _finite(row.get("return"))]
    if len(returns) < 2:
        return []
    ranked = sorted(returns, key=lambda row: row["return"], reverse=True)
    best = ranked[0]
    worst = ranked[-1]
    positive_count = sum(1 for row in returns if row["return"] > 0)
    positive_share = positive_count / len(returns)
    spread = best["return"] - worst["return"]
    sp500_rank = next((row.get("rank") for row in returns if row.get("option_id") == "SP500"), None)
    data_as_of = _round_date(round_item, prefer_exit=True)
    return [
        _insight(
            insight_id=f"benchmark-difficulty-{round_item['round_id']}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="benchmark_difficulty",
            audiences=["investors", "capital_allocators", "ai_researchers"],
            title=f"{_track_label(round_item['track'])} round had {_fmt_pct(spread)} asset dispersion",
            summary=(
                f"The best scored asset returned {_fmt_pct(best['return'])}, the worst returned {_fmt_pct(worst['return'])}, "
                f"and {_fmt_pct(positive_share)} of the universe was positive. "
                f"The S&P 500 ranked {sp500_rank or 'unranked'} out of {len(returns)} options."
            ),
            why=(
                "Benchmark difficulty matters because model scores should be interpreted against the opportunity set and "
                "the market window they faced."
            ),
            importance=90,
            calculations=[
                {"name": "oracle_return", "value": round(best["return"] * 100, 4), "unit": "percent", "formula": "max(scored asset returns)"},
                {"name": "worst_asset_return", "value": round(worst["return"] * 100, 4), "unit": "percent", "formula": "min(scored asset returns)"},
                {"name": "positive_universe_share", "value": round(positive_share * 100, 4), "unit": "percent", "formula": "positive asset count / scored asset count"},
            ],
            evidence=[
                {"label": f"{_track_label(round_item['track'])} result", "href": f"/rounds/{round_item['round_id']}", "source": f"rounds/{round_item['round_id']}/runs/{round_item['run_id']}/results/returns.csv"}
            ],
            related=[{"label": "Scoring", "href": "/scoring"}],
        )
    ]


def _missed_oracle_insight(round_item: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    returns = [row for row in round_item["returns"] if _finite(row.get("return"))]
    if not returns or not round_item["portfolios"]:
        return []
    best = max(returns, key=lambda row: row["return"])
    best_id = best["option_id"]
    holders = []
    for portfolio in round_item["portfolios"]:
        allocation = sum(float(item["allocation_pct"]) for item in portfolio["allocations"] if item["option_id"] == best_id)
        if allocation > 0:
            holders.append((portfolio["model_id"], allocation))
    avg_allocation = sum(allocation for _, allocation in holders) / len(round_item["portfolios"])
    largest_holder = max(holders, key=lambda item: item[1]) if holders else None
    best_name = _asset_name(best)
    data_as_of = _round_date(round_item, prefer_exit=True)
    summary = (
        f"The hindsight best asset was {best_name} at {_fmt_pct(best['return'])}. "
        f"{len(holders)} of {len(round_item['portfolios'])} models held it, with {_fmt_pct(avg_allocation / 100)} average allocation."
    )
    if largest_holder:
        summary += f" The largest allocation came from {_model_label(largest_holder[0])} at {_fmt_pct(largest_holder[1] / 100)}."
    return [
        _insight(
            insight_id=f"missed-oracle-{round_item['round_id']}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="oracle_comparison",
            audiences=["investors", "capital_allocators", "traders", "ai_researchers"],
            title=f"Models {'found' if holders else 'missed'} the {_track_label(round_item['track']).lower()} oracle asset",
            summary=summary,
            why=(
                "This shows whether models identified the eventual best asset before scoring, even when portfolio weights "
                "were too small to fully capture the oracle return."
            ),
            importance=89,
            calculations=[
                {"name": "oracle_asset_holder_count", "value": len(holders), "unit": "models", "formula": "count models with positive allocation to oracle asset"},
                {"name": "average_oracle_asset_allocation", "value": round(avg_allocation, 4), "unit": "percentage_points", "formula": "average allocation to oracle asset across model portfolios"},
            ],
            evidence=[
                {"label": f"{_track_label(round_item['track'])} result", "href": f"/rounds/{round_item['round_id']}", "source": f"rounds/{round_item['round_id']}/runs/{round_item['run_id']}/results"}
            ],
            related=[{"label": "Scoring", "href": "/scoring#capitalbench-score"}],
        )
    ]


def _attribution_insight(round_item: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    allocation_rows = [row for row in round_item["allocations"] if _finite(row.get("return_contribution"))]
    if not allocation_rows or not round_item["results"]:
        return []
    winner = max(round_item["results"], key=lambda row: row.get("portfolio_return") or -999)
    winner_rows = [row for row in allocation_rows if row["model_id"] == winner["model_id"]]
    if not winner_rows:
        return []
    best = max(winner_rows, key=lambda row: row["return_contribution"])
    worst = min(winner_rows, key=lambda row: row["return_contribution"])
    data_as_of = _round_date(round_item, prefer_exit=True)
    if worst["return_contribution"] < 0:
        second_clause = f"The largest drag came from {worst['label']} at {_fmt_pct(worst['return_contribution'])}."
        weakest_calculation_name = "largest_negative_contribution"
    elif worst["option_id"] == best["option_id"]:
        second_clause = "No holding detracted from the portfolio in this one-holding attribution view."
        weakest_calculation_name = "smallest_positive_contribution"
    else:
        second_clause = f"No holding detracted; the smallest positive contribution came from {worst['label']} at {_fmt_pct(worst['return_contribution'])}."
        weakest_calculation_name = "smallest_positive_contribution"
    return [
        _insight(
            insight_id=f"attribution-{round_item['round_id']}-{_slug(winner['model_id'])}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="performance_attribution",
            audiences=["traders", "capital_allocators", "ai_researchers"],
            title=f"{_model_label(winner['model_id'])}'s result was driven by {best['label']}",
            summary=(
                f"In the latest {_track_label(round_item['track']).lower()} result, {best['label']} contributed "
                f"{_fmt_pct(best['return_contribution'])} to {_model_label(winner['model_id'])}'s portfolio. "
                f"{second_clause}"
            ),
            why=(
                "Attribution turns a model score into an explanation of which holdings actually helped or hurt the "
                "frozen portfolio."
            ),
            importance=83,
            calculations=[
                {"name": "largest_positive_contribution", "value": round(best["return_contribution"] * 100, 4), "unit": "percent", "formula": "allocation weight * asset return"},
                {"name": weakest_calculation_name, "value": round(worst["return_contribution"] * 100, 4), "unit": "percent", "formula": "allocation weight * asset return"},
            ],
            evidence=[
                {"label": f"{_track_label(round_item['track'])} result", "href": f"/rounds/{round_item['round_id']}", "source": f"rounds/{round_item['round_id']}/runs/{round_item['run_id']}/results/allocations.csv"}
            ],
            related=[{"label": f"Latest {_track_label(round_item['track']).lower()} results", "href": f"/leaderboards/latest-{round_item['track']}"}],
        )
    ]


def _confidence_calibration_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    rows = [
        result
        for round_item in snapshot["rounds"]
        if round_item["status"] == "resolved"
        for result in round_item["results"]
        if _finite(result.get("confidence")) and _finite(result.get("portfolio_return"))
    ]
    if len(rows) < 6:
        return []
    median_confidence = statistics.median([row["confidence"] for row in rows])
    high = [row for row in rows if row["confidence"] >= median_confidence]
    low = [row for row in rows if row["confidence"] < median_confidence]
    if not high or not low:
        return []
    high_return = _average([row["portfolio_return"] for row in high]) or 0
    low_return = _average([row["portfolio_return"] for row in low]) or 0
    high_score = _average([row.get("capitalbench_score") for row in high])
    low_score = _average([row.get("capitalbench_score") for row in low])
    better = "outperformed" if high_return > low_return else "underperformed"
    data_as_of = _snapshot_data_as_of(snapshot)
    return [
        _insight(
            insight_id=f"confidence-calibration-{_slug(data_as_of)}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="confidence_calibration",
            audiences=["ai_researchers", "capital_allocators", "investors"],
            title=f"High-confidence model calls have {better} lower-confidence calls",
            summary=(
                f"Across resolved official results, submissions at or above the median confidence of {median_confidence:.2f} "
                f"averaged {_fmt_pct(high_return)}, while lower-confidence submissions averaged {_fmt_pct(low_return)}."
            ),
            why=(
                "Confidence calibration helps readers judge whether model self-reported confidence carries useful "
                "information about realized benchmark performance."
            ),
            importance=85,
            calculations=[
                {"name": "high_confidence_average_return", "value": round(high_return * 100, 4), "unit": "percent", "formula": "average return for confidence >= median confidence"},
                {"name": "low_confidence_average_return", "value": round(low_return * 100, 4), "unit": "percent", "formula": "average return for confidence < median confidence"},
                {"name": "high_confidence_average_capitalbench_score", "value": None if high_score is None else round(high_score, 4), "unit": "points", "formula": "average CapitalBench Score for confidence >= median confidence"},
                {"name": "low_confidence_average_capitalbench_score", "value": None if low_score is None else round(low_score, 4), "unit": "points", "formula": "average CapitalBench Score for confidence < median confidence"},
            ],
            evidence=[
                {"label": "Results", "href": "/leaderboards/latest", "source": "resolved official leaderboard rows"}
            ],
            related=[{"label": "Scoring", "href": "/scoring"}],
        )
    ]


def _live_path_insights(snapshot: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    active_rounds = [round_item for round_item in snapshot["rounds"] if round_item["status"] == "active"]
    latest_rows = []
    for round_item in active_rounds:
        grouped: dict[str, list[dict[str, Any]]] = {}
        for row in round_item["interim_performance"]:
            if row.get("published") is False:
                continue
            grouped.setdefault(row["model_id"], []).append(row)
        for model_rows in grouped.values():
            model_rows.sort(key=lambda row: (row.get("price_date") or "", row.get("target_date") or ""))
            latest_rows.append({**model_rows[-1], "track": round_item["track"], "round_id": round_item["round_id"]})
    if len(latest_rows) < 2:
        return []
    best = max(latest_rows, key=lambda row: row.get("alpha_vs_sp500") if _finite(row.get("alpha_vs_sp500")) else -999)
    worst = min(latest_rows, key=lambda row: row.get("alpha_vs_sp500") if _finite(row.get("alpha_vs_sp500")) else 999)
    data_as_of = max((_text(row.get("price_date")) for row in latest_rows), default=_snapshot_data_as_of(snapshot))
    best_context = f"{_model_label(best['model_id'])} in {best['round_id']}"
    worst_context = f"{_model_label(worst['model_id'])} in {worst['round_id']}"
    return [
        _insight(
            insight_id=f"live-path-{_slug(data_as_of)}",
            generated_at=generated_at,
            data_as_of=data_as_of,
            category="live_performance",
            audiences=["traders", "investors", "capital_allocators"],
            title=f"{_model_label(best['model_id'])} has the strongest live alpha",
            summary=(
                f"Using the latest available interim close, {best_context} is ahead of the S&P 500 by "
                f"{_fmt_pp(best['alpha_vs_sp500'])}, while {worst_context} is at {_fmt_pp(worst['alpha_vs_sp500'])}."
            ),
            why=(
                "Live alpha is provisional, but it shows how open model portfolios are moving before the final official score."
            ),
            importance=77,
            calculations=[
                {"name": "best_live_alpha", "value": round(best["alpha_vs_sp500"] * 100, 4), "unit": "percentage_points", "formula": "interim model return - interim S&P 500 return"},
                {"name": "worst_live_alpha", "value": round(worst["alpha_vs_sp500"] * 100, 4), "unit": "percentage_points", "formula": "interim model return - interim S&P 500 return"},
            ],
            evidence=[
                {"label": "Live performance", "href": "/", "source": "weekly_performance.csv"}
            ],
            related=[{"label": "Rounds", "href": "/rounds"}],
        )
    ]


def _current_active_rounds(snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    output = []
    for track in ["weekly", "monthly"]:
        candidates = [row for row in snapshot["rounds"] if row["track"] == track and row["status"] == "active" and row["portfolios"]]
        if candidates:
            output.append(max(candidates, key=_round_sort_value))
    return output


def _latest_resolved_by_track(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    output = {}
    for track in ["weekly", "monthly"]:
        candidates = [row for row in snapshot["rounds"] if row["track"] == track and row["status"] == "resolved" and row["results"]]
        if candidates:
            output[track] = max(candidates, key=lambda row: (_text(row.get("exit_date")), _round_sort_value(row)))
    return output


def _aggregate_allocations(portfolios: list[dict[str, Any]]) -> list[tuple[str, float]]:
    if not portfolios:
        return []
    totals: dict[str, float] = {}
    for portfolio in portfolios:
        for allocation in portfolio.get("allocations") or []:
            totals[allocation["option_id"]] = totals.get(allocation["option_id"], 0.0) + float(allocation["allocation_pct"])
    denominator = max(1, len(portfolios))
    return sorted(((option_id, value / denominator) for option_id, value in totals.items()), key=lambda item: (-item[1], item[0]))


def _top_regime(portfolios: list[dict[str, Any]]) -> tuple[str, float] | None:
    if not portfolios:
        return None
    totals: dict[str, float] = {}
    for portfolio in portfolios:
        for allocation in portfolio.get("allocations") or []:
            regime = _text(allocation.get("regime_group")) or "unknown"
            totals[regime] = totals.get(regime, 0.0) + float(allocation["allocation_pct"])
    if not totals:
        return None
    denominator = max(1, len(portfolios))
    return max(((key, value / denominator) for key, value in totals.items()), key=lambda item: item[1])


def _allocation_to_ids(portfolios: list[dict[str, Any]], option_ids: set[str]) -> float:
    if not portfolios:
        return 0.0
    total = 0.0
    for portfolio in portfolios:
        total += sum(float(item["allocation_pct"]) for item in portfolio.get("allocations") or [] if item["option_id"] in option_ids)
    return total / len(portfolios)


def _portfolio_risk_score(portfolio: dict[str, Any]) -> float | None:
    score = 0.0
    denominator = 0.0
    for allocation in portfolio.get("allocations") or []:
        loading = _optional_float(_find_allocation_loading(allocation))
        if loading is None:
            continue
        weight = float(allocation["allocation_pct"]) / 100
        score += weight * (50 + 50 * loading)
        denominator += weight
    return score / denominator if denominator else None


def _find_allocation_loading(allocation: dict[str, Any]) -> float | None:
    # Current allocation objects keep only regime, so recover risk-on loading
    # from option_return field only if future callers include it. Missing values
    # are intentionally ignored rather than guessed.
    return allocation.get("risk_on_loading")


def _find_option(rounds: list[dict[str, Any]], option_id: str) -> dict[str, Any]:
    for round_item in rounds:
        for option in round_item.get("options") or []:
            if option["option_id"] == option_id:
                return option
        for return_row in round_item.get("returns") or []:
            if return_row["option_id"] == option_id:
                return return_row
    return {"option_id": option_id, "label": option_id, "ticker": None}


def _sp500_return(round_item: dict[str, Any]) -> float | None:
    for row in round_item["returns"]:
        if row.get("option_id") == "SP500" and _finite(row.get("return")):
            return row["return"]
    if round_item["results"]:
        return round_item["results"][0].get("sp500_return")
    return None


def _oracle_return(returns: list[dict[str, Any]]) -> float | None:
    values = [row["return"] for row in returns if _finite(row.get("return"))]
    return max(values) if values else None


def _weighted_return(allocations: list[dict[str, Any]], return_by_option: dict[str, float]) -> float | None:
    if not return_by_option or not allocations:
        return None
    total = 0.0
    for allocation in allocations:
        option_id = allocation["option_id"]
        if option_id not in return_by_option:
            return None
        total += (float(allocation["allocation_pct"]) / 100) * return_by_option[option_id]
    return total


def _capitalbench_score(portfolio_return: float | None, oracle_return: float | None) -> float | None:
    if portfolio_return is None or oracle_return is None:
        return None
    if oracle_return == 0:
        return 100.0 if portfolio_return == 0 else None
    return 100 * portfolio_return / oracle_return


def _cosine_similarity(left: dict[str, float], right: dict[str, float]) -> float:
    keys = set(left) | set(right)
    dot = sum(left.get(key, 0.0) * right.get(key, 0.0) for key in keys)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def _insight(
    *,
    insight_id: str,
    generated_at: str,
    data_as_of: str,
    category: str,
    audiences: list[str],
    title: str,
    summary: str,
    why: str,
    importance: float,
    calculations: list[dict[str, Any]],
    evidence: list[dict[str, str]],
    related: list[dict[str, str]] | None = None,
    confidence: str = "high",
    source_type: str = "deterministic",
) -> dict[str, Any]:
    return {
        "id": insight_id,
        "date": generated_at[:10],
        "generated_at": generated_at,
        "data_as_of": data_as_of,
        "category": category,
        "audiences": audiences,
        "source_type": source_type,
        "title": title,
        "summary": summary,
        "why_it_matters": why,
        "importance_score": round(float(importance), 4),
        "confidence": confidence,
        "status": "published",
        "calculations": calculations,
        "evidence": evidence,
        "related": related or [],
    }


def _validate_public_insights(payload: dict[str, Any], path: Path) -> None:
    if payload.get("version") != INSIGHTS_VERSION:
        raise ValueError(f"{path} has invalid insights version")
    insights = payload.get("insights")
    if not isinstance(insights, list):
        raise ValueError(f"{path} must contain an insights list")
    seen_ids: set[str] = set()
    required = {
        "id",
        "date",
        "generated_at",
        "data_as_of",
        "category",
        "audiences",
        "source_type",
        "title",
        "summary",
        "why_it_matters",
        "importance_score",
        "confidence",
        "status",
        "calculations",
        "evidence",
    }
    for insight in insights:
        if not isinstance(insight, dict):
            raise ValueError(f"{path} contains a non-object insight")
        missing = required - set(insight)
        if missing:
            raise ValueError(f"{path} insight {insight.get('id')} is missing fields: {', '.join(sorted(missing))}")
        if insight["id"] in seen_ids:
            raise ValueError(f"{path} contains duplicate insight id: {insight['id']}")
        seen_ids.add(insight["id"])
        for text_field in ["title", "summary", "why_it_matters"]:
            if not str(insight.get(text_field) or "").strip():
                raise ValueError(f"{path} insight {insight['id']} has blank {text_field}")
        if not insight.get("evidence"):
            raise ValueError(f"{path} insight {insight['id']} has no evidence")
        if insight.get("source_type") not in {"deterministic", "llm_assisted", "system"}:
            raise ValueError(f"{path} insight {insight['id']} has invalid source_type")


def _write_report(path: Path, public: dict[str, Any]) -> None:
    lines = [
        "# CapitalBench Insights",
        "",
        f"Generated at: `{public['generated_at']}`",
        f"Data as of: `{public['data_as_of']}`",
        f"Engine: `{public['engine_version']}`",
        "",
    ]
    for insight in public["insights"]:
        lines.extend(
            [
                f"## {insight['title']}",
                "",
                insight["summary"],
                "",
                f"Why it matters: {insight['why_it_matters']}",
                "",
                f"Category: `{insight['category']}`",
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _build_index(output_dir: Path, run_date: str, public: dict[str, Any]) -> dict[str, Any]:
    runs = []
    if output_dir.exists():
        for item in sorted(output_dir.iterdir()):
            if item.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", item.name):
                run_file = item / "insights.json"
                if run_file.exists():
                    runs.append({"date": item.name, "href": f"{item.name}/insights.json"})
    if not any(row["date"] == run_date for row in runs):
        runs.append({"date": run_date, "href": f"{run_date}/insights.json"})
    runs = sorted(runs, key=lambda row: row["date"], reverse=True)
    return {
        "version": INSIGHTS_VERSION,
        "generated_at": public["generated_at"],
        "latest_date": run_date,
        "latest_href": "latest.json",
        "run_count": len(runs),
        "runs": runs,
    }


def _load_asset_risk(repo_root: Path) -> dict[str, Any]:
    path = repo_root / "configs" / "asset_risk_model.yaml"
    return read_yaml(path) if path.exists() else {"assets": {}, "regime_groups": {}}


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _split_risks(value: object) -> list[str]:
    if isinstance(value, list):
        return [_text(item) for item in value if _text(item)]
    text = _text(value)
    if not text:
        return []
    return [part.strip() for part in re.split(r";|\n", text) if part.strip()]


def _round_sort_value(round_item: dict[str, Any]) -> str:
    return ":".join(
        [
            _text(round_item.get("decision_deadline_utc")),
            _text(round_item.get("decision_date")),
            _text(round_item.get("entry_date")),
            _text(round_item.get("round_id")),
        ]
    )


def _round_date(round_item: dict[str, Any], *, prefer_exit: bool = False) -> str:
    if prefer_exit:
        return _text(round_item.get("exit_date")) or _text(round_item.get("decision_date")) or _snapshot_fallback_date()
    return _text(round_item.get("decision_date")) or _text(round_item.get("entry_date")) or _snapshot_fallback_date()


def _snapshot_data_as_of(snapshot: dict[str, Any]) -> str:
    dates = []
    for round_item in snapshot.get("rounds") or []:
        if round_item.get("status") == "resolved" and round_item.get("exit_date"):
            dates.append(str(round_item["exit_date"]))
        for row in round_item.get("interim_performance") or []:
            if row.get("price_date"):
                dates.append(str(row["price_date"]))
        if round_item.get("decision_date"):
            dates.append(str(round_item["decision_date"]))
    return max(dates) if dates else str(snapshot.get("generated_at") or _utc_now())[:10]


def _track_from_manifest(manifest) -> str:
    horizon = str(manifest.horizon or "").lower()
    round_id = str(manifest.round_id)
    if "week" in horizon or round_id.endswith("-1W"):
        return "weekly"
    return "monthly"


def _track_label(track: str) -> str:
    return "Weekly" if track == "weekly" else "Monthly"


def _risk_label(score: float | None) -> str:
    if score is None:
        return "Not available"
    if score < 20:
        return "Defensive"
    if score < 40:
        return "Cautious"
    if score < 60:
        return "Balanced"
    if score < 80:
        return "Risk-seeking"
    return "Aggressive"


def _asset_name(row: dict[str, Any]) -> str:
    label = _text(row.get("label")) or _text(row.get("option_id"))
    ticker = _text(row.get("ticker"))
    if ticker and ticker.upper() not in {"CASH", "USD"}:
        return f"{label} ({ticker})"
    return label


def _model_label(model_id: str) -> str:
    labels = {
        "anthropic-claude-fable-5": "Claude Fable 5",
        "anthropic-claude-opus-4-7": "Claude Opus 4.7",
        "anthropic-claude-opus-4-8": "Claude Opus 4.8",
        "google-gemini-3-1-pro": "Gemini 3.1 Pro",
        "openai-gpt-5-5": "GPT-5.5",
        "xai-grok-4-3": "Grok 4.3",
    }
    return labels.get(model_id, model_id)


def _primary_option_id(allocations: list[dict[str, Any]]) -> str:
    if not allocations:
        return ""
    return max(allocations, key=lambda row: float(row["allocation_pct"]))["option_id"]


def _average(values: list[Any]) -> float | None:
    finite = [float(value) for value in values if _finite(value)]
    return sum(finite) / len(finite) if finite else None


def _bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def _optional_float(value: object) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _optional_int(value: object) -> int | None:
    parsed = _optional_float(value)
    return int(parsed) if parsed is not None else None


def _finite(value: object) -> bool:
    return _optional_float(value) is not None


def _text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _fmt_pct(value: float | None) -> str:
    if value is None:
        return "not available"
    return f"{value * 100:+.2f}%"


def _fmt_pp(value: float | None) -> str:
    if value is None:
        return "not available"
    return f"{value * 100:+.2f} percentage points"


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _dedupe_insights(insights: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output = []
    seen = set()
    for insight in insights:
        if insight["id"] in seen:
            continue
        seen.add(insight["id"])
        output.append(insight)
    return output


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _snapshot_fallback_date() -> str:
    return _utc_now()[:10]

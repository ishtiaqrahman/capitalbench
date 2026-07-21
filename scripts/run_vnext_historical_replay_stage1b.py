from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import math
import os
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "run_vnext_historical_replay.py"
SPEC = importlib.util.spec_from_file_location("vnext_replay_base", BASE_SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load base replay runner: {BASE_SCRIPT}")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)

DEFAULT_CONFIG = ROOT / "experiments" / "vnext-historical-replay-stage1b-2026-07-21.yaml"
DEFAULT_REPORT = ROOT / "docs" / "vnext_historical_replay_stage1b_report.md"
LANES = ("continuation", "reversal", "context", "defensive", "wildcard")
REGIMES = ("trending_up", "trending_down", "range_bound", "stress_reversal", "mixed")


def load_config(path: Path) -> dict[str, Any]:
    return base.load_yaml(path)


def experiment_output(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def control_output(config: dict[str, Any]) -> Path:
    return ROOT / str(config["control_output_dir"])


def episode_index(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return base.episode_index(config)


def _active_rows(episode: dict[str, Any]) -> list[dict[str, Any]]:
    rows = base.derived_market_rows(base.common_market_rows(base.source_round(episode)))
    return [row for row in rows if not row["is_benchmark"]]


def _value(row: dict[str, Any], key: str, default: float = 0.5) -> float:
    parsed = base.as_float(row.get(key))
    return default if parsed is None else parsed


def _top_ids(scored: Sequence[tuple[float, str]], count: int = 12) -> list[str]:
    return [option_id for _score, option_id in sorted(scored, key=lambda item: (-item[0], item[1]))[:count]]


def _context_scores(episode: dict[str, Any], rows: Sequence[dict[str, Any]]) -> dict[str, float]:
    round_path = base.source_round(episode)
    briefing_path = round_path / "research" / "final_briefing.md"
    if not briefing_path.exists():
        briefing_path = round_path / "briefing.md"
    briefing = base.sanitize_full_briefing(briefing_path.read_text(encoding="utf-8"))
    lines = [line for line in briefing.splitlines() if "not provided" not in line.lower()]
    scores: dict[str, float] = {}
    for row in rows:
        option_id = str(row["option_id"])
        symbol = str(row.get("symbol") or "")
        patterns = [rf"\|\s*{re.escape(option_id)}(?:_CONTEXT)?\s*\|"]
        if len(symbol) >= 2:
            patterns.append(rf"\|\s*{re.escape(symbol)}\s*\|")
        mentions = sum(
            1
            for line in lines
            if any(re.search(pattern, line, flags=re.IGNORECASE) for pattern in patterns)
        )
        rank_shift = abs(_value(row, "recent_vs_medium_rank_shift", 0.0))
        scores[option_id] = float(mentions) + rank_shift * 0.05
    return scores


def lane_references(episode: dict[str, Any]) -> dict[str, list[str]]:
    rows = _active_rows(episode)
    continuation: list[tuple[float, str]] = []
    reversal: list[tuple[float, str]] = []
    defensive: list[tuple[float, str]] = []
    context_scores = _context_scores(episode, rows)
    risk_weight = {"low": 1.0, "medium": 0.72, "high": 0.35, "very_high": 0.10}
    for row in rows:
        option_id = str(row["option_id"])
        rank_7d = _value(row, "rank_return_7d")
        rank_30d = _value(row, "rank_return_30d")
        rank_6m = _value(row, "rank_return_6m")
        dispersion = _value(row, "trend_rank_dispersion", 0.5)
        continuation.append((0.55 * rank_7d + 0.30 * rank_30d + 0.15 * rank_6m, option_id))
        reversal.append(
            (
                0.55 * (1.0 - rank_7d)
                + 0.25 * (1.0 - rank_30d)
                + 0.20 * abs(rank_7d - rank_30d),
                option_id,
            )
        )
        defensive.append(
            (
                0.65 * risk_weight.get(str(row.get("risk_bucket") or ""), 0.45)
                + 0.35 * (1.0 - min(max(dispersion, 0.0), 1.0)),
                option_id,
            )
        )
    context = [(score, option_id) for option_id, score in context_scores.items()]
    return {
        "continuation": _top_ids(continuation),
        "reversal": _top_ids(reversal),
        "context": _top_ids(context),
        "defensive": _top_ids(defensive),
    }


def market_summary(episode: dict[str, Any]) -> str:
    rows = base.derived_market_rows(base.common_market_rows(base.source_round(episode)))
    spy = next(row for row in rows if row["is_benchmark"])
    active = [row for row in rows if not row["is_benchmark"]]
    returns_7d = [_value(row, "return_7d", 0.0) for row in active]
    returns_30d = [_value(row, "return_30d", 0.0) for row in active]
    values = [
        ["SPY 7d return", base._pct(spy.get("return_7d"))],
        ["SPY 30d return", base._pct(spy.get("return_30d"))],
        ["active median 7d", f"{median(returns_7d) * 100:.2f}%"],
        ["active median 30d", f"{median(returns_30d) * 100:.2f}%"],
        ["active positive breadth 7d", f"{sum(value > 0 for value in returns_7d) / len(returns_7d) * 100:.1f}%"],
        ["active positive breadth 30d", f"{sum(value > 0 for value in returns_30d) / len(returns_30d) * 100:.1f}%"],
        ["cross-sectional dispersion 7d", f"{pstdev(returns_7d) * 100:.2f}%"],
        ["cross-sectional dispersion 30d", f"{pstdev(returns_30d) * 100:.2f}%"],
    ]
    return base.markdown_table(["entry-time market statistic", "value"], values)


def lane_reference_table(episode: dict[str, Any]) -> str:
    references = lane_references(episode)
    return base.markdown_table(
        ["candidate lens", "mechanical reference IDs"],
        [[lane, ", ".join(references[lane])] for lane in ("continuation", "reversal", "context", "defensive")],
    )


COMMON_TASK = """
You are participating in a private, retrospective CapitalBench input experiment.
Treat this as an unknown decision point. Use only this packet. Do not use
remembered outcomes, tools, browsing, search, or external facts. The horizon is
one week.

Forecast SPY separately. Build a ten-option shortlist from the complete active
universe, then rank a final five that is a subset of that shortlist. Use exact
option_id values. Rank 1 is the highest expected one-week return.
expected_alpha_vs_spy_pct must equal the candidate forecast minus the SPY
forecast. The mechanical candidate lenses are references, not recommendations
or a reduced universe. Return only JSON matching the supplied schema.
""".strip()


TREATMENT_TEXT = {
    "H4": """
Use balanced candidate coverage. The ten-name shortlist must contain exactly
three continuation candidates, three reversal candidates, two context or
catalyst candidates, one defensive candidate, and one unrestricted wildcard.
Assign each shortlist name to exactly one lane. Do not place more than four
shortlist names in the same option group. Evaluate the complete universe before
choosing the lane representatives.
""".strip(),
    "H5": """
First classify the entry-time environment as trending_up, trending_down,
range_bound, stress_reversal, or mixed. State a concise rationale. Then route
the shortlist according to that regime while retaining at least two
continuation candidates, two reversal candidates, one context or catalyst
candidate, and one defensive candidate. Up to four remaining names may use any
lane, including wildcard. Do not place more than four shortlist names in the
same option group.
""".strip(),
    "H6": """
Create an initial ten-name shortlist. Before finalizing it, identify the five
strongest omitted candidates that could make the initial shortlist wrong.
Submit a revised final ten-name shortlist containing at least two of those five
challengers. This is a single-turn review: do all stages internally and return
one JSON object. Assign a candidate lane to each final shortlist name.
""".strip(),
}


def build_prompt(config: dict[str, Any], episode: dict[str, Any], treatment: str) -> str:
    if treatment == "H0":
        return base.build_prompt(config, episode, treatment)
    round_path = base.source_round(episode)
    briefing_path = round_path / "research" / "final_briefing.md"
    if not briefing_path.exists():
        briefing_path = round_path / "briefing.md"
    briefing = base.sanitize_full_briefing(briefing_path.read_text(encoding="utf-8"))
    table = base.derived_market_table(
        base.derived_market_rows(base.common_market_rows(round_path))
    )
    return (
        f"{COMMON_TASK}\n\n"
        f"Replay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {treatment}\n\n"
        f"Treatment instructions:\n{TREATMENT_TEXT[treatment]}\n\n"
        f"Entry-time market summary:\n{market_summary(episode)}\n\n"
        f"Mechanical candidate references:\n{lane_reference_table(episode)}\n\n"
        f"Frozen factual briefing:\n{briefing}\n\n"
        f"Complete option comparison table:\n{table}\n"
    )


def response_schema(treatment: str) -> dict[str, Any]:
    if treatment == "H0":
        return base.response_schema()
    top5_item = copy.deepcopy(base.response_schema()["properties"]["top5"]["items"])
    shortlist_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "option_id": {"type": "string"},
            "candidate_lane": {"type": "string", "enum": list(LANES)},
        },
        "required": ["option_id", "candidate_lane"],
    }
    properties: dict[str, Any] = {
        "replay_id": {"type": "string"},
        "treatment_id": {"type": "string"},
        "market_regime": {"type": "string", "enum": list(REGIMES)},
        "regime_rationale": {"type": "string"},
        "spy_forecast_return_pct": {"type": "number"},
        "prefer_spy": {"type": "boolean"},
        "shortlist": {
            "type": "array",
            "minItems": 10,
            "maxItems": 10,
            "items": shortlist_item,
        },
        "top5": {
            "type": "array",
            "minItems": 5,
            "maxItems": 5,
            "items": top5_item,
        },
    }
    required = list(properties)
    if treatment == "H6":
        properties["initial_shortlist_option_ids"] = {
            "type": "array",
            "minItems": 10,
            "maxItems": 10,
            "items": {"type": "string"},
        }
        properties["omitted_challenge_option_ids"] = {
            "type": "array",
            "minItems": 5,
            "maxItems": 5,
            "items": {"type": "string"},
        }
        required.extend(["initial_shortlist_option_ids", "omitted_challenge_option_ids"])
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": properties,
        "required": required,
    }


def _alias_map(episode: dict[str, Any]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    ambiguous: set[str] = set()
    for row in base.load_options(base.source_round(episode)):
        option_id = str(row["id"])
        if bool(row.get("is_cash")) or bool(row.get("is_benchmark")) or option_id == "SP500":
            continue
        for value in (option_id, row.get("symbol")):
            alias = str(value or "").strip().upper()
            if not alias:
                continue
            if alias in aliases and aliases[alias] != option_id:
                ambiguous.add(alias)
            else:
                aliases[alias] = option_id
    for alias in ambiguous:
        aliases.pop(alias, None)
    return aliases


def canonicalize_payload(payload: Any, episode: dict[str, Any], treatment: str) -> Any:
    if treatment == "H0":
        return base.canonicalize_option_ids(payload, episode)
    if not isinstance(payload, dict):
        return payload
    aliases = _alias_map(episode)

    def canonical(value: Any) -> str:
        text = str(value or "").strip()
        return aliases.get(text.upper(), text)

    normalized = json.loads(json.dumps(payload))
    if isinstance(normalized.get("shortlist"), list):
        for item in normalized["shortlist"]:
            if isinstance(item, dict):
                item["option_id"] = canonical(item.get("option_id"))
    if isinstance(normalized.get("top5"), list):
        for item in normalized["top5"]:
            if isinstance(item, dict):
                item["option_id"] = canonical(item.get("option_id"))
    for key in ("initial_shortlist_option_ids", "omitted_challenge_option_ids"):
        if isinstance(normalized.get(key), list):
            normalized[key] = [canonical(value) for value in normalized[key]]
    return normalized


def _shortlist_ids(payload: dict[str, Any], treatment: str) -> list[str]:
    if treatment == "H0":
        return [str(value) for value in payload.get("shortlist_option_ids", [])]
    return [
        str(item.get("option_id") or "")
        for item in payload.get("shortlist", [])
        if isinstance(item, dict)
    ]


def validate_payload(payload: Any, episode: dict[str, Any], treatment: str) -> list[str]:
    if treatment == "H0":
        return base.validate_payload(payload, episode, treatment)
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    shortlist = payload.get("shortlist")
    shortlist_ids = _shortlist_ids(payload, treatment)
    translated = copy.deepcopy(payload)
    translated["shortlist_option_ids"] = shortlist_ids
    errors = base.validate_payload(translated, episode, treatment)
    if payload.get("market_regime") not in REGIMES:
        errors.append("invalid market regime")
    if not str(payload.get("regime_rationale") or "").strip():
        errors.append("missing regime rationale")
    lanes: list[str] = []
    if not isinstance(shortlist, list) or len(shortlist) != 10:
        errors.append("shortlist must contain exactly 10 rows")
    else:
        for item in shortlist:
            if not isinstance(item, dict):
                errors.append("shortlist row is not an object")
                continue
            lane = str(item.get("candidate_lane") or "")
            lanes.append(lane)
            if lane not in LANES:
                errors.append(f"invalid candidate lane: {lane}")
    lane_counts = Counter(lanes)
    if treatment == "H4":
        required = {"continuation": 3, "reversal": 3, "context": 2, "defensive": 1, "wildcard": 1}
        if any(lane_counts[lane] != count for lane, count in required.items()):
            errors.append("H4 lane counts must be 3 continuation, 3 reversal, 2 context, 1 defensive, 1 wildcard")
    if treatment == "H5":
        required_minimums = {"continuation": 2, "reversal": 2, "context": 1, "defensive": 1}
        if any(lane_counts[lane] < count for lane, count in required_minimums.items()):
            errors.append("H5 lane minimums were not met")
    options = {str(row["id"]): row for row in base.load_options(base.source_round(episode))}
    groups = Counter(str(options.get(option_id, {}).get("option_group") or "") for option_id in shortlist_ids)
    if any(group and count > 4 for group, count in groups.items()):
        errors.append("shortlist contains more than four options from one option group")
    if treatment == "H6":
        active_ids = base.allowed_active_ids(episode)
        initial = [str(value) for value in payload.get("initial_shortlist_option_ids", [])]
        omitted = [str(value) for value in payload.get("omitted_challenge_option_ids", [])]
        if len(initial) != 10 or len(set(initial)) != 10 or set(initial) - active_ids:
            errors.append("invalid H6 initial shortlist")
        if len(omitted) != 5 or len(set(omitted)) != 5 or set(omitted) - active_ids:
            errors.append("invalid H6 omitted challenge list")
        if set(initial) & set(omitted):
            errors.append("H6 omitted challenges must be absent from the initial shortlist")
        if len(set(shortlist_ids) & set(omitted)) < 2:
            errors.append("H6 final shortlist must include at least two omitted challengers")
    return sorted(set(errors))


def primary_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"]
        if episode["phase"] == "discovery"
        for model_id in config["models"]
        for treatment in config["primary_treatments"]
    ]


def fallback_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    treatment = str(config["fallback_treatment"])
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"]
        if episode["phase"] == "discovery"
        for model_id in config["models"]
    ]


def confirmation_calls(config: dict[str, Any], selected: str) -> list[dict[str, str]]:
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"]
        if episode["phase"] == "confirmation"
        for model_id in config["models"]
        for treatment in ("H0", selected)
    ]


def response_stem(call: dict[str, str]) -> str:
    return base.response_stem(call)


def prepare(config_path: Path) -> None:
    config = load_config(config_path)
    output = experiment_output(config)
    packet_dir = output / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    packets: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        for treatment in config["treatments"]:
            prompt = build_prompt(config, episode, treatment)
            path = packet_dir / f"{episode['replay_id']}__{treatment}.txt"
            path.write_text(prompt, encoding="utf-8", newline="\n")
            packets.append(
                {
                    "replay_id": episode["replay_id"],
                    "phase": episode["phase"],
                    "treatment": treatment,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": base.sha256_text(prompt),
                    "bytes": len(prompt.encode("utf-8")),
                    "estimated_tokens": math.ceil(len(prompt) / 4),
                    "schema_sha256": base.sha256_text(json.dumps(response_schema(treatment), sort_keys=True)),
                }
            )
    controls: list[dict[str, Any]] = []
    control_dir = control_output(config) / "records" / "discovery"
    for episode in config["episodes"]:
        if episode["phase"] != "discovery":
            continue
        for model_id in config["models"]:
            call = {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": "H0"}
            path = control_dir / f"{response_stem(call)}.json"
            if not path.exists():
                raise RuntimeError(f"missing frozen control: {path}")
            record = json.loads(path.read_text(encoding="utf-8"))
            if not record.get("valid"):
                raise RuntimeError(f"control is not valid: {path}")
            controls.append(
                {
                    **call,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": base.sha256_file(path),
                    "api_model_name": record.get("api_model_name"),
                }
            )
    protocol_path = ROOT / str(config["protocol"])
    manifest = {
        "experiment_id": config["experiment_id"],
        "frozen_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "outcomes_loaded": False,
        "config_path": config_path.relative_to(ROOT).as_posix(),
        "config_sha256": base.sha256_file(config_path),
        "protocol_sha256": base.sha256_file(protocol_path),
        "runner_sha256": base.sha256_file(Path(__file__)),
        "packets": packets,
        "frozen_controls": controls,
        "planned_primary_calls": len(primary_calls(config)),
        "planned_fallback_calls": len(fallback_calls(config)),
    }
    base.write_json(output / "freeze_manifest.json", manifest)
    base.write_csv(output / "packet_manifest.csv", packets)
    print(f"prepared_packets={len(packets)}")
    print(f"frozen_controls={len(controls)}")
    print(f"primary_calls={len(primary_calls(config))}")
    print(f"fallback_calls={len(fallback_calls(config))}")


def verify_freeze(config: dict[str, Any]) -> dict[str, Any]:
    path = experiment_output(config) / "freeze_manifest.json"
    if not path.exists():
        raise RuntimeError("freeze manifest is missing; run prepare first")
    freeze = json.loads(path.read_text(encoding="utf-8"))
    if freeze.get("outcomes_loaded") is not False:
        raise RuntimeError("freeze manifest does not certify outcomes_loaded=false")
    for packet in freeze["packets"]:
        packet_path = ROOT / packet["path"]
        if base.sha256_file(packet_path) != packet["sha256"]:
            raise RuntimeError(f"packet hash mismatch: {packet_path}")
    for control in freeze["frozen_controls"]:
        control_path = ROOT / control["path"]
        if base.sha256_file(control_path) != control["sha256"]:
            raise RuntimeError(f"control hash mismatch: {control_path}")
    return freeze


def _call_provider(model: Any, prompt: str, treatment: str, retries: int) -> tuple[Any, int]:
    provider_class = base.PROVIDERS.get(model.provider)
    if provider_class is None:
        raise ValueError(f"provider not allowed: {model.provider}")
    runtime = base.RuntimeSettings(
        timeout_seconds=model.max_wall_clock_seconds,
        max_output_tokens=model.max_completion_tokens,
        temperature=model.temperature,
        reasoning_effort=model.reasoning_effort,
    )
    attempts = 0
    while True:
        attempts += 1
        try:
            result = provider_class().run_model(model, prompt, response_schema(treatment), runtime)
            return result, attempts
        except Exception as exc:
            if attempts > retries or not base._transport_error(str(exc)):
                raise
            time.sleep(2.0 * attempts)


def _selected_treatment(config: dict[str, Any]) -> str | None:
    output = experiment_output(config)
    primary = output / "primary_decision.json"
    if primary.exists():
        selected = json.loads(primary.read_text(encoding="utf-8")).get("selected_treatment")
        if selected:
            return str(selected)
    fallback = output / "fallback_decision.json"
    if fallback.exists():
        selected = json.loads(fallback.read_text(encoding="utf-8")).get("selected_treatment")
        if selected:
            return str(selected)
    return None


def run_calls(config_path: Path, phase: str) -> None:
    config = load_config(config_path)
    freeze = verify_freeze(config)
    output = experiment_output(config)
    episodes = episode_index(config)
    models = base.model_index(config)
    base.load_local_env()
    required_env = {base.PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required_env if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")
    if phase == "primary":
        calls = primary_calls(config)
    elif phase == "fallback":
        primary_path = output / "primary_decision.json"
        if not primary_path.exists():
            raise RuntimeError("score primary before fallback")
        primary = json.loads(primary_path.read_text(encoding="utf-8"))
        if primary.get("selected_treatment"):
            print("fallback_skipped=primary treatment passed")
            return
        calls = fallback_calls(config)
    elif phase == "confirmation":
        selected = _selected_treatment(config)
        if not selected:
            print("confirmation_skipped=no treatment passed discovery")
            return
        calls = confirmation_calls(config, selected)
    else:
        raise ValueError(f"unknown phase: {phase}")
    record_dir = output / "records" / phase
    response_dir = output / "responses" / phase
    record_dir.mkdir(parents=True, exist_ok=True)
    response_dir.mkdir(parents=True, exist_ok=True)
    completed = 0
    for position, call in enumerate(calls, start=1):
        stem = response_stem(call)
        record_path = record_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if not existing.get("provider_error"):
                normalized = canonicalize_payload(
                    existing.get("parsed_json"), episodes[call["replay_id"]], call["treatment"]
                )
                errors = validate_payload(normalized, episodes[call["replay_id"]], call["treatment"])
                existing["parsed_json"] = normalized
                existing["validation_errors"] = errors
                existing["valid"] = not errors
                base.write_json(record_path, existing)
                if existing["valid"] or errors != ["response is not a JSON object"]:
                    completed += 1
                    print(f"[{position}/{len(calls)}] skip_existing valid={existing['valid']} {stem}", flush=True)
                    continue
                print(f"[{position}/{len(calls)}] retry_truncated_json {stem}", flush=True)
            else:
                print(f"[{position}/{len(calls)}] retry_provider_error {stem}", flush=True)
        packet_path = output / "packets" / f"{call['replay_id']}__{call['treatment']}.txt"
        prompt = packet_path.read_text(encoding="utf-8")
        packet_hash = base.sha256_text(prompt)
        frozen = next(
            row for row in freeze["packets"]
            if row["replay_id"] == call["replay_id"] and row["treatment"] == call["treatment"]
        )
        if packet_hash != frozen["sha256"]:
            raise RuntimeError(f"packet changed after freeze: {packet_path}")
        print(f"[{position}/{len(calls)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            result, attempts = _call_provider(
                models[call["model_id"]], prompt, call["treatment"], int(config["transport_retries"])
            )
            error = result.error
        except Exception as exc:
            result = base.ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = 1
            error = str(exc)
        completed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        raw_path = response_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = canonicalize_payload(result.parsed_json, episodes[call["replay_id"]], call["treatment"])
        errors = validate_payload(parsed, episodes[call["replay_id"]], call["treatment"])
        if error:
            errors.append(f"provider_error: {error}")
        record = {
            **call,
            "provider": models[call["model_id"]].provider,
            "api_model_name": models[call["model_id"]].api_model_name,
            "started_at_utc": started,
            "completed_at_utc": completed_at,
            "attempts": attempts,
            "packet_sha256": packet_hash,
            "raw_response_sha256": base.sha256_text(result.raw_text),
            "raw_response_path": raw_path.relative_to(ROOT).as_posix(),
            "provider_parsed_json": result.parsed_json,
            "parsed_json": parsed,
            "usage": result.usage.model_dump(mode="json", exclude_none=True),
            "provider_error": error,
            "validation_errors": sorted(set(errors)),
            "valid": not errors,
        }
        base.write_json(record_path, record)
        completed += 1
        print(f"[{position}/{len(calls)}] saved valid={record['valid']} {stem}", flush=True)
        if error and not base._transport_error(error):
            raise RuntimeError(f"provider call failed for {stem}: {error}")
    print(f"{phase}_records={completed}")


def _score_record(record: dict[str, Any], episode: dict[str, Any], outcome: dict[str, Any]) -> dict[str, Any]:
    payload = record.get("parsed_json") if record.get("valid") else None
    result = {
        "phase": episode["phase"],
        "replay_id": episode["replay_id"],
        "model_id": record["model_id"],
        "treatment": record["treatment"],
        "valid": bool(record.get("valid")),
        "validation_errors": record.get("validation_errors", []),
        "spy_return": outcome["spy_return"],
        "input_tokens": (record.get("usage") or {}).get("input_tokens"),
        "output_tokens": (record.get("usage") or {}).get("output_tokens"),
        "reasoning_tokens": (record.get("usage") or {}).get("reasoning_tokens"),
        "latency_seconds": (record.get("usage") or {}).get("latency_seconds"),
    }
    if not isinstance(payload, dict):
        return result
    treatment = str(record["treatment"])
    shortlist = _shortlist_ids(payload, treatment)
    top5_rows = sorted(payload["top5"], key=lambda item: int(item["rank"]))
    top5 = [str(item["option_id"]) for item in top5_rows]
    ordered = sorted(outcome["active_returns"].items(), key=lambda item: (-item[1], item[0]))
    top2_ids = [option_id for option_id, _return in ordered[:2]]
    top2_count = len(set(shortlist) & set(top2_ids))
    shortlist_best = max(outcome["returns"][option_id] for option_id in shortlist)
    top5_return = mean(outcome["returns"][option_id] for option_id in top5)
    result.update(
        {
            "shortlist_ids": shortlist,
            "top5_ids": top5,
            "winner_ids": outcome["winner_ids"],
            "top2_ids": top2_ids,
            "winner_capture": bool(set(shortlist) & set(outcome["winner_ids"])),
            "top2_capture_count": top2_count,
            "top2_any_capture": top2_count > 0,
            "shortlist_best_return": shortlist_best,
            "shortlist_oracle_regret": outcome["best_return"] - shortlist_best,
            "top5_return": top5_return,
            "top5_alpha": top5_return - outcome["spy_return"],
        }
    )
    return result


def _control_records(config: dict[str, Any]) -> list[dict[str, Any]]:
    freeze = verify_freeze(config)
    return [json.loads((ROOT / row["path"]).read_text(encoding="utf-8")) for row in freeze["frozen_controls"]]


def _phase_records(config: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    directory = experiment_output(config) / "records" / phase
    if not directory.exists():
        return []
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.json"))]


def _score_records(config: dict[str, Any], records: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    episodes = episode_index(config)
    outcomes: dict[str, dict[str, Any]] = {}
    scored: list[dict[str, Any]] = []
    for record in records:
        replay_id = str(record["replay_id"])
        if replay_id not in outcomes:
            outcomes[replay_id] = base.load_outcomes(episodes[replay_id])
        scored.append(_score_record(record, episodes[replay_id], outcomes[replay_id]))
    return scored


def _paired_rows(scored: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in scored:
        grouped[(str(row["replay_id"]), str(row["model_id"]))][str(row["treatment"])] = row
    pairs: list[dict[str, Any]] = []
    for (replay_id, model_id), treatments in sorted(grouped.items()):
        control = treatments.get("H0")
        if control is None:
            continue
        for treatment, challenger in sorted(treatments.items()):
            if treatment == "H0":
                continue
            valid = bool(control.get("valid")) and bool(challenger.get("valid"))
            pairs.append(
                {
                    "replay_id": replay_id,
                    "model_id": model_id,
                    "challenger": treatment,
                    "pair_valid": valid,
                    "control_top2_capture_count": control.get("top2_capture_count"),
                    "challenger_top2_capture_count": challenger.get("top2_capture_count"),
                    "top2_capture_change": (
                        int(challenger["top2_capture_count"]) - int(control["top2_capture_count"])
                        if valid else None
                    ),
                    "control_regret": control.get("shortlist_oracle_regret"),
                    "challenger_regret": challenger.get("shortlist_oracle_regret"),
                    "regret_reduction": (
                        float(control["shortlist_oracle_regret"])
                        - float(challenger["shortlist_oracle_regret"])
                        if valid else None
                    ),
                    "control_top5_alpha": control.get("top5_alpha"),
                    "challenger_top5_alpha": challenger.get("top5_alpha"),
                    "alpha_improvement": (
                        float(challenger["top5_alpha"]) - float(control["top5_alpha"])
                        if valid else None
                    ),
                }
            )
    return pairs


def _aggregate(config: dict[str, Any], pairs: Sequence[dict[str, Any]], confirmation: bool = False) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in pairs:
        grouped[str(row["challenger"])].append(row)
    gates = config["gates"]
    output: list[dict[str, Any]] = []
    for treatment, subset in sorted(grouped.items()):
        valid = [row for row in subset if row["pair_valid"]]
        alpha = [float(row["alpha_improvement"]) for row in valid]
        control_regret = [float(row["control_regret"]) for row in valid]
        challenger_regret = [float(row["challenger_regret"]) for row in valid]
        control_top2 = sum(int(row["control_top2_capture_count"]) for row in valid)
        challenger_top2 = sum(int(row["challenger_top2_capture_count"]) for row in valid)
        capture_episodes = len({row["replay_id"] for row in valid if int(row["challenger_top2_capture_count"]) > 0})
        capture_models = len({row["model_id"] for row in valid if int(row["challenger_top2_capture_count"]) > 0})
        by_model: dict[str, list[float]] = defaultdict(list)
        by_episode: dict[str, list[float]] = defaultdict(list)
        for row in valid:
            by_model[str(row["model_id"])].append(float(row["alpha_improvement"]))
            by_episode[str(row["replay_id"])].append(float(row["alpha_improvement"]))
        positive_models = sum(mean(values) > 0 for values in by_model.values())
        positive_episodes = sum(mean(values) > 0 for values in by_episode.values())
        control_regret_mean = mean(control_regret) if control_regret else None
        challenger_regret_mean = mean(challenger_regret) if challenger_regret else None
        relative_regret_reduction = (
            (control_regret_mean - challenger_regret_mean) / control_regret_mean
            if control_regret_mean and challenger_regret_mean is not None else None
        )
        minimum_alpha = 0.0 if confirmation else float(gates["minimum_mean_alpha_improvement"])
        minimum_regret = 0.0 if confirmation else float(gates["minimum_relative_regret_reduction"])
        passed = bool(
            len(valid) >= int(gates["minimum_valid_pairs"])
            and challenger_top2 > control_top2
            and capture_episodes >= int(gates["minimum_capture_episodes"])
            and capture_models >= int(gates["minimum_capture_models"])
            and relative_regret_reduction is not None
            and relative_regret_reduction > minimum_regret
            and alpha
            and mean(alpha) > minimum_alpha
            and sum(value > 0 for value in alpha) >= int(gates["minimum_positive_pairs"])
            and positive_models >= int(gates["minimum_positive_models"])
            and positive_episodes >= int(gates["minimum_positive_episodes"])
        )
        output.append(
            {
                "challenger": treatment,
                "valid_pairs": len(valid),
                "control_top2_capture_count": control_top2,
                "challenger_top2_capture_count": challenger_top2,
                "top2_capture_change": challenger_top2 - control_top2,
                "capture_episodes": capture_episodes,
                "capture_models": capture_models,
                "relative_regret_reduction": relative_regret_reduction,
                "mean_alpha_improvement": mean(alpha) if alpha else None,
                "positive_pairs": sum(value > 0 for value in alpha),
                "positive_models": positive_models,
                "positive_episodes": positive_episodes,
                "passes_gate": passed,
            }
        )
    return output


def _select(aggregates: Sequence[dict[str, Any]]) -> str | None:
    passing = [row for row in aggregates if row["passes_gate"]]
    passing.sort(
        key=lambda row: (
            -int(row["top2_capture_change"]),
            -float(row["relative_regret_reduction"]),
            -float(row["mean_alpha_improvement"]),
            str(row["challenger"]),
        )
    )
    return str(passing[0]["challenger"]) if passing else None


def score_primary(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    records = _control_records(config) + _phase_records(config, "primary")
    scored = _score_records(config, records)
    pairs = _paired_rows(scored)
    aggregates = _aggregate(config, pairs)
    selected = _select(aggregates)
    decision = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "selected_treatment": selected,
        "fallback_allowed": selected is None,
        "aggregates": aggregates,
    }
    output = experiment_output(config)
    base.write_csv(output / "primary_call_metrics.csv", scored)
    base.write_csv(output / "primary_pairs.csv", pairs)
    base.write_csv(output / "primary_aggregate.csv", aggregates)
    base.write_json(output / "primary_decision.json", decision)
    print(json.dumps(decision, indent=2))
    return decision


def score_fallback(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    primary_path = experiment_output(config) / "primary_decision.json"
    if not primary_path.exists():
        raise RuntimeError("score primary first")
    primary = json.loads(primary_path.read_text(encoding="utf-8"))
    if primary.get("selected_treatment"):
        decision = {"selected_treatment": None, "skipped": "primary treatment passed"}
        base.write_json(experiment_output(config) / "fallback_decision.json", decision)
        print(json.dumps(decision, indent=2))
        return decision
    records = _control_records(config) + _phase_records(config, "fallback")
    scored = _score_records(config, records)
    pairs = _paired_rows(scored)
    aggregates = _aggregate(config, pairs)
    selected = _select(aggregates)
    decision = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "selected_treatment": selected,
        "aggregates": aggregates,
    }
    output = experiment_output(config)
    base.write_csv(output / "fallback_call_metrics.csv", scored)
    base.write_csv(output / "fallback_pairs.csv", pairs)
    base.write_csv(output / "fallback_aggregate.csv", aggregates)
    base.write_json(output / "fallback_decision.json", decision)
    print(json.dumps(decision, indent=2))
    return decision


def score_confirmation(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    selected = _selected_treatment(config)
    if not selected:
        result = {"selected_treatment": None, "skipped": "no discovery treatment passed"}
        base.write_json(experiment_output(config) / "confirmation_decision.json", result)
        print(json.dumps(result, indent=2))
        return result
    records = _phase_records(config, "confirmation")
    scored = _score_records(config, records)
    pairs = [row for row in _paired_rows(scored) if row["challenger"] == selected]
    aggregates = _aggregate(config, pairs, confirmation=True)
    result = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "selected_treatment": selected,
        "aggregates": aggregates,
        "passes_confirmation": bool(aggregates and aggregates[0]["passes_gate"]),
    }
    output = experiment_output(config)
    base.write_csv(output / "confirmation_call_metrics.csv", scored)
    base.write_csv(output / "confirmation_pairs.csv", pairs)
    base.write_csv(output / "confirmation_aggregate.csv", aggregates)
    base.write_json(output / "confirmation_decision.json", result)
    print(json.dumps(result, indent=2))
    return result


def _format_pct(value: Any) -> str:
    parsed = base.as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.2f}%"


def _aggregate_table(rows: Sequence[dict[str, Any]]) -> str:
    return base.markdown_table(
        ["Treatment", "Valid", "Top-2 challenger/control", "Capture breadth", "Regret reduction", "Alpha improvement", "Positive pairs", "Gate"],
        [
            [
                row["challenger"],
                row["valid_pairs"],
                f"{row['challenger_top2_capture_count']}/{row['control_top2_capture_count']}",
                f"{row['capture_episodes']} periods, {row['capture_models']} models",
                _format_pct(row["relative_regret_reduction"]),
                _format_pct(row["mean_alpha_improvement"]),
                row["positive_pairs"],
                "Pass" if row["passes_gate"] else "Fail",
            ]
            for row in rows
        ],
    )


def write_report(config_path: Path, report_path: Path) -> None:
    config = load_config(config_path)
    output = experiment_output(config)
    primary = json.loads((output / "primary_decision.json").read_text(encoding="utf-8"))
    fallback_path = output / "fallback_decision.json"
    fallback = json.loads(fallback_path.read_text(encoding="utf-8")) if fallback_path.exists() else None
    confirmation_path = output / "confirmation_decision.json"
    confirmation = json.loads(confirmation_path.read_text(encoding="utf-8")) if confirmation_path.exists() else None
    selected = _selected_treatment(config)
    if not selected:
        bottom_line = "No candidate-coverage treatment passed discovery. No confirmation calls were run."
    elif confirmation and confirmation.get("passes_confirmation"):
        bottom_line = f"{selected} passed historical discovery and confirmation. It qualifies only for a prospective live shadow test."
    elif confirmation:
        bottom_line = f"{selected} passed development but failed historical confirmation. It does not qualify for a live shadow test."
    else:
        bottom_line = f"{selected} passed development; confirmation has not been completed."
    lines = [
        "# VNext Historical Replay Stage 1B Results",
        "",
        f"Generated at: `{datetime.now(timezone.utc).replace(microsecond=0).isoformat()}`",
        "",
        "## Bottom Line",
        "",
        bottom_line,
        "",
        "## Primary Discovery",
        "",
        _aggregate_table(primary["aggregates"]),
        "",
    ]
    if fallback and fallback.get("aggregates"):
        lines.extend(["## Fallback Discovery", "", _aggregate_table(fallback["aggregates"]), ""])
    if confirmation and confirmation.get("aggregates"):
        lines.extend(["## Confirmation", "", _aggregate_table(confirmation["aggregates"]), ""])
    records = _phase_records(config, "primary") + _phase_records(config, "fallback") + _phase_records(config, "confirmation")
    usage = base.usage_summary(records)
    lines.extend(
        [
            "## Execution",
            "",
            f"- New logical calls saved: {usage['calls']}",
            f"- Valid responses: {usage['valid_calls']}",
            f"- Input tokens: {usage['input_tokens']:,}",
            f"- Output tokens: {usage['output_tokens']:,}",
            f"- Reported reasoning tokens: {usage['reasoning_tokens']:,}",
            "",
            "## Interpretation",
            "",
            "D1-D3 are adaptive development data. Only C1-C3 are held out, and any historical confirmation pass still requires a prospective live shadow test.",
            "",
        ]
    )
    text = "\n".join(lines)
    output_report = output / "report.md"
    output_report.write_text(text, encoding="utf-8", newline="\n")
    report_path.write_text(text, encoding="utf-8", newline="\n")
    print(text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run CapitalBench Stage 1B historical replay")
    parser.add_argument(
        "command",
        choices=(
            "prepare",
            "run-primary",
            "score-primary",
            "run-fallback",
            "score-fallback",
            "run-confirmation",
            "score-confirmation",
            "report",
        ),
    )
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    if args.command == "prepare":
        prepare(config_path)
    elif args.command == "run-primary":
        run_calls(config_path, "primary")
    elif args.command == "score-primary":
        score_primary(config_path)
    elif args.command == "run-fallback":
        run_calls(config_path, "fallback")
    elif args.command == "score-fallback":
        score_fallback(config_path)
    elif args.command == "run-confirmation":
        run_calls(config_path, "confirmation")
    elif args.command == "score-confirmation":
        score_confirmation(config_path)
    elif args.command == "report":
        write_report(config_path, args.report.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

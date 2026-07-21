"""Run the private H9 symmetric-coverage historical replay."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[1]
EVENT_RUNNER = ROOT / "scripts" / "run_vnext_event_ranking_replay.py"
DEFAULT_CONFIG = ROOT / "experiments" / "vnext-symmetric-coverage-replay-2026-07-21.yaml"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


event = _load_module("vnext_symmetric_event_base", EVENT_RUNNER)
base = event.base
stage1b = event.stage1b

from capitalbench.exposures import exposure_clusters_by_option  # noqa: E402
from capitalbench.io import load_options as load_market_options  # noqa: E402


FIXED_LANES = (
    "us_core_style",
    "growth_technology",
    "domestic_cyclicals",
    "health_defensive",
    "international_equity",
    "rates_credit",
    "real_assets",
    "alternatives_currencies",
)
SEARCH_LANES = ("benchmark", *FIXED_LANES, "wildcard")
EVIDENCE_STRENGTHS = ("strong", "moderate", "weak", "none")
TIMING_FITS = ("inside_window", "already_released", "no_direct_event", "uncertain")

LANE_CLUSTERS = {
    "us_core_style": {"diversified_us_equity"},
    "growth_technology": {"technology_and_growth"},
    "domestic_cyclicals": {
        "consumer_cyclical",
        "financials",
        "industrials_and_defense",
    },
    "health_defensive": {
        "consumer_defensive",
        "healthcare_and_biotech",
        "rate_sensitive_defensive",
    },
    "international_equity": {"international_equity"},
    "rates_credit": {"capital_preservation", "rates_and_duration", "credit"},
    "real_assets": {
        "clean_energy",
        "energy",
        "materials_and_mining",
        "non_energy_commodities",
        "precious_metals",
    },
    "alternatives_currencies": {"crypto_assets", "currencies"},
}

COMMON_TASK = """
You are participating in a private retrospective CapitalBench input experiment.
Treat this as an unknown decision point. Use only this packet. Do not use
remembered outcomes, tools, browsing, search, or external facts. The horizon is
one week.

Evaluate every non-cash option through the fixed search lanes. Build exactly one
unique finalist from each of the eight lanes, include SP500 as the benchmark,
and add one unique wildcard for a ten-option shortlist. Then rank a final five
that is a subset of the shortlist. Rank 1 has the highest expected one-week
return. Return only JSON matching the supplied schema.
""".strip()

TREATMENT_TASK = """
The option evidence matrix is exhaustive and symmetric. An event mapping is
factual context, not a directional recommendation. An option marked none has no
mapped non-price fact in this packet. Do not use mention count, row order, lane
size, or table position as evidence.

For every shortlist row, cite only event IDs actually mapped to that option.
Recent or trailing price performance alone is not independent evidence. Every
non-SP500 final-five candidate must have at least one mapped event ID, strong or
moderate evidence, timing inside the window or already released, and positive
expected alpha versus SPY. If five finalists do not clear that gate, or if the
supported basket is not expected to beat SPY, set prefer_spy=true and explain
why. The final five must still be returned for audit even when SPY is preferred.
""".strip()


def load_config(path: Path) -> dict[str, Any]:
    return base.load_yaml(path)


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def event_register(episode: dict[str, Any]) -> dict[str, Any]:
    return event.event_register(episode)


def option_lane_map(episode: dict[str, Any]) -> dict[str, str]:
    round_path = base.source_round(episode)
    options = [option for option in load_market_options(round_path) if option.include_in_universe]
    clusters = exposure_clusters_by_option(options)
    cluster_to_lane: dict[str, str] = {}
    for lane, lane_clusters in LANE_CLUSTERS.items():
        for cluster in lane_clusters:
            if cluster in cluster_to_lane:
                raise ValueError(f"duplicate lane cluster: {cluster}")
            cluster_to_lane[cluster] = lane
    result: dict[str, str] = {}
    for option in options:
        if option.is_cash:
            continue
        if option.option_id == "SP500" or option.is_benchmark:
            result[option.option_id] = "benchmark"
            continue
        cluster = clusters[option.option_id]
        lane = cluster_to_lane.get(cluster)
        if lane is None:
            raise ValueError(f"unmapped exposure cluster {cluster}: {option.option_id}")
        result[option.option_id] = lane
    return result


def mapped_events(episode: dict[str, Any]) -> dict[str, list[str]]:
    lanes = option_lane_map(episode)
    mapped = {option_id: [] for option_id in lanes}
    for row in event_register(episode).get("events", []):
        event_id = str(row["id"])
        for option_id in row.get("affected_options", []):
            option_id = str(option_id)
            if option_id in mapped:
                mapped[option_id].append(event_id)
    return {key: sorted(set(value)) for key, value in mapped.items()}


def option_evidence_table(episode: dict[str, Any]) -> str:
    lanes = option_lane_map(episode)
    events = mapped_events(episode)
    rows = [
        [option_id, lanes[option_id], ", ".join(events[option_id]) or "none"]
        for option_id in lanes
    ]
    return base.markdown_table(["option_id", "fixed search lane", "mapped event IDs"], rows)


def build_prompt(config: dict[str, Any], episode: dict[str, Any]) -> str:
    market = base.derived_market_table(
        base.derived_market_rows(base.common_market_rows(base.source_round(episode)))
    )
    return (
        f"{COMMON_TASK}\n\nReplay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {config['treatment']}\n\n{TREATMENT_TASK}\n\n"
        f"Entry-time market summary:\n{stage1b.market_summary(episode)}\n\n"
        f"Complete option evidence matrix:\n{option_evidence_table(episode)}\n\n"
        f"Frozen factual event register:\n{event.event_table(episode)}\n\n"
        f"Complete option comparison table:\n{market}\n"
    )


def response_schema() -> dict[str, Any]:
    shortlist_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "option_id": {"type": "string"},
            "search_lane": {"type": "string", "enum": list(SEARCH_LANES)},
            "event_ids": {"type": "array", "items": {"type": "string"}},
            "evidence_strength": {"type": "string", "enum": list(EVIDENCE_STRENGTHS)},
            "timing_fit": {"type": "string", "enum": list(TIMING_FITS)},
            "forecast_return_pct": {"type": "number"},
            "expected_alpha_vs_spy_pct": {"type": "number"},
            "evidence_summary": {"type": "string"},
        },
        "required": [
            "option_id",
            "search_lane",
            "event_ids",
            "evidence_strength",
            "timing_fit",
            "forecast_return_pct",
            "expected_alpha_vs_spy_pct",
            "evidence_summary",
        ],
    }
    top5_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "rank": {"type": "integer", "minimum": 1, "maximum": 5},
            "option_id": {"type": "string"},
            "forecast_return_pct": {"type": "number"},
            "expected_alpha_vs_spy_pct": {"type": "number"},
            "evidence": {"type": "string"},
            "invalidation": {"type": "string"},
        },
        "required": [
            "rank",
            "option_id",
            "forecast_return_pct",
            "expected_alpha_vs_spy_pct",
            "evidence",
            "invalidation",
        ],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "replay_id": {"type": "string"},
            "treatment_id": {"type": "string", "enum": ["H9"]},
            "spy_forecast_return_pct": {"type": "number"},
            "prefer_spy": {"type": "boolean"},
            "abstention_reason": {"type": "string"},
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
        },
        "required": [
            "replay_id",
            "treatment_id",
            "spy_forecast_return_pct",
            "prefer_spy",
            "abstention_reason",
            "shortlist",
            "top5",
        ],
    }


def _alias_map(episode: dict[str, Any]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    ambiguous: set[str] = set()
    for row in base.load_options(base.source_round(episode)):
        option_id = str(row["id"])
        if bool(row.get("is_cash")):
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


def canonicalize(payload: Any, episode: dict[str, Any]) -> Any:
    if not isinstance(payload, dict):
        return payload
    normalized = json.loads(json.dumps(payload))
    aliases = _alias_map(episode)

    def option_id(value: Any) -> str:
        text = str(value or "").strip()
        return aliases.get(text.upper(), text)

    for key in ("shortlist", "top5"):
        for row in normalized.get(key) or []:
            if isinstance(row, dict):
                row["option_id"] = option_id(row.get("option_id"))
    return normalized


def validate_payload(payload: Any, episode: dict[str, Any]) -> list[str]:
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    errors: list[str] = []
    if str(payload.get("replay_id")) != str(episode["replay_id"]):
        errors.append("replay_id mismatch")
    if payload.get("treatment_id") != "H9":
        errors.append("treatment_id must be H9")
    spy_forecast = base.as_float(payload.get("spy_forecast_return_pct"))
    if spy_forecast is None:
        errors.append("invalid SPY forecast")
        spy_forecast = 0.0

    lanes = option_lane_map(episode)
    events = mapped_events(episode)
    valid_event_ids = {str(row["id"]) for row in event_register(episode).get("events", [])}
    shortlist = payload.get("shortlist")
    shortlist_ids: list[str] = []
    lane_counts: Counter[str] = Counter()
    shortlist_by_id: dict[str, dict[str, Any]] = {}
    if not isinstance(shortlist, list) or len(shortlist) != 10:
        errors.append("shortlist must contain exactly 10 rows")
        shortlist = []
    for row in shortlist:
        if not isinstance(row, dict):
            errors.append("shortlist row is not an object")
            continue
        option_id = str(row.get("option_id") or "")
        lane = str(row.get("search_lane") or "")
        shortlist_ids.append(option_id)
        lane_counts[lane] += 1
        shortlist_by_id[option_id] = row
        if option_id not in lanes:
            errors.append(f"invalid shortlist option: {option_id}")
            continue
        if lane not in SEARCH_LANES:
            errors.append(f"invalid search lane: {lane}")
        elif lane == "benchmark" and option_id != "SP500":
            errors.append("benchmark lane must contain SP500")
        elif lane in FIXED_LANES and lanes[option_id] != lane:
            errors.append(f"option {option_id} does not belong to lane {lane}")
        elif lane == "wildcard" and option_id == "SP500":
            errors.append("wildcard must be a non-benchmark option")
        cited = [str(value) for value in row.get("event_ids") or []]
        unknown = set(cited) - valid_event_ids
        if unknown:
            errors.append(f"unknown event IDs: {sorted(unknown)}")
        unmapped = set(cited) - set(events[option_id])
        if unmapped:
            errors.append(f"events not mapped to {option_id}: {sorted(unmapped)}")
        forecast = base.as_float(row.get("forecast_return_pct"))
        alpha = base.as_float(row.get("expected_alpha_vs_spy_pct"))
        if forecast is None or alpha is None or abs((forecast - spy_forecast) - alpha) > 0.011:
            errors.append(f"forecast alpha mismatch: {option_id}")
        if row.get("evidence_strength") not in EVIDENCE_STRENGTHS:
            errors.append(f"invalid evidence strength: {option_id}")
        if row.get("timing_fit") not in TIMING_FITS:
            errors.append(f"invalid timing fit: {option_id}")
        if not str(row.get("evidence_summary") or "").strip():
            errors.append(f"missing evidence summary: {option_id}")

    if len(set(shortlist_ids)) != len(shortlist_ids):
        errors.append("shortlist options must be unique")
    if any(lane_counts[lane] != 1 for lane in SEARCH_LANES):
        errors.append("shortlist must contain benchmark, eight fixed lanes, and wildcard exactly once")

    top5 = payload.get("top5")
    top5_ids: list[str] = []
    top5_ranks: list[int] = []
    if not isinstance(top5, list) or len(top5) != 5:
        errors.append("top5 must contain exactly five rows")
        top5 = []
    for row in top5:
        if not isinstance(row, dict):
            errors.append("top5 row is not an object")
            continue
        option_id = str(row.get("option_id") or "")
        top5_ids.append(option_id)
        try:
            top5_ranks.append(int(row.get("rank")))
        except (TypeError, ValueError):
            errors.append(f"invalid top5 rank: {option_id}")
        if option_id not in shortlist_by_id:
            errors.append(f"top5 option absent from shortlist: {option_id}")
        forecast = base.as_float(row.get("forecast_return_pct"))
        alpha = base.as_float(row.get("expected_alpha_vs_spy_pct"))
        if forecast is None or alpha is None or abs((forecast - spy_forecast) - alpha) > 0.011:
            errors.append(f"top5 forecast alpha mismatch: {option_id}")
        if not str(row.get("evidence") or "").strip() or not str(row.get("invalidation") or "").strip():
            errors.append(f"top5 evidence or invalidation missing: {option_id}")
    if len(set(top5_ids)) != len(top5_ids):
        errors.append("top5 options must be unique")
    if sorted(top5_ranks) != [1, 2, 3, 4, 5]:
        errors.append("top5 ranks must be 1 through 5")

    prefer_spy = payload.get("prefer_spy")
    if not isinstance(prefer_spy, bool):
        errors.append("prefer_spy must be boolean")
    if prefer_spy and not str(payload.get("abstention_reason") or "").strip():
        errors.append("SPY preference requires an abstention reason")
    if prefer_spy is False:
        for option_id in top5_ids:
            if option_id == "SP500":
                continue
            row = shortlist_by_id.get(option_id, {})
            supported = bool(row.get("event_ids"))
            timely = row.get("timing_fit") in {"inside_window", "already_released"}
            strong = row.get("evidence_strength") in {"strong", "moderate"}
            positive = (base.as_float(row.get("expected_alpha_vs_spy_pct")) or 0.0) > 0
            if not (supported and timely and strong and positive):
                errors.append(f"active finalist failed independent-evidence gate: {option_id}")
    return sorted(set(errors))


def calls_for(config: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "replay_id": str(episode["replay_id"]),
            "model_id": str(model_id),
            "treatment": str(config["treatment"]),
        }
        for episode in config["episodes"]
        for model_id in config["models"]
    ]


def control_repair_calls(manifest: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "replay_id": str(row["replay_id"]),
            "model_id": str(row["model_id"]),
            "treatment": str(row["treatment"]),
        }
        for row in manifest["controls"]
        if row.get("repair_required")
    ]


def prepare(config_path: Path) -> None:
    config = load_config(config_path)
    output = output_dir(config)
    packet_dir = output / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    packets: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []
    controls: list[dict[str, Any]] = []
    control_dir = ROOT / str(config["control_output_dir"]) / "records" / "search"
    for episode in config["episodes"]:
        event_path = ROOT / str(episode["event_register"])
        round_path = base.source_round(episode)
        sources.append(
            {
                "replay_id": episode["replay_id"],
                "event_register": event_path.relative_to(ROOT).as_posix(),
                "event_register_sha256": base.sha256_file(event_path),
                "options": (round_path / "options.yaml").relative_to(ROOT).as_posix(),
                "options_sha256": base.sha256_file(round_path / "options.yaml"),
                "market_data": (round_path / "market_data" / "universe_trailing_returns.csv").relative_to(ROOT).as_posix(),
                "market_data_sha256": base.sha256_file(round_path / "market_data" / "universe_trailing_returns.csv"),
            }
        )
        lane_counts = Counter(option_lane_map(episode).values())
        if any(lane_counts[lane] == 0 for lane in ("benchmark", *FIXED_LANES)):
            raise ValueError(f"empty search lane in {episode['replay_id']}")
        prompt = build_prompt(config, episode)
        packet_path = packet_dir / f"{episode['replay_id']}__{config['treatment']}.txt"
        packet_path.write_text(prompt, encoding="utf-8", newline="\n")
        packets.append(
            {
                "replay_id": episode["replay_id"],
                "treatment": config["treatment"],
                "path": packet_path.relative_to(ROOT).as_posix(),
                "sha256": base.sha256_text(prompt),
                "bytes": len(prompt.encode("utf-8")),
                "schema_sha256": base.sha256_text(json.dumps(response_schema(), sort_keys=True)),
            }
        )
        for model_id in config["models"]:
            call = {
                "replay_id": str(episode["replay_id"]),
                "model_id": str(model_id),
                "treatment": str(config["control_treatment"]),
            }
            path = control_dir / f"{base.response_stem(call)}.json"
            if not path.exists():
                raise RuntimeError(f"missing H4 control: {path}")
            record = json.loads(path.read_text(encoding="utf-8"))
            if record.get("valid"):
                controls.append(
                    {
                        **call,
                        "repair_required": False,
                        "path": path.relative_to(ROOT).as_posix(),
                        "sha256": base.sha256_file(path),
                        "api_model_name": record.get("api_model_name"),
                    }
                )
                continue
            control_packet = (
                ROOT
                / str(config["control_output_dir"])
                / "packets"
                / f"{episode['replay_id']}__{config['control_treatment']}.txt"
            )
            if not control_packet.exists():
                raise RuntimeError(f"missing frozen H4 packet: {control_packet}")
            controls.append(
                {
                    **call,
                    "repair_required": True,
                    "packet_path": control_packet.relative_to(ROOT).as_posix(),
                    "packet_sha256": base.sha256_file(control_packet),
                    "schema_sha256": base.sha256_text(
                        json.dumps(event.response_schema(str(config["control_treatment"])), sort_keys=True)
                    ),
                    "prior_error": record.get("provider_error"),
                    "api_model_name": record.get("api_model_name"),
                }
            )
    planned = calls_for(config)
    repairs = [row for row in controls if row.get("repair_required")]
    if len(planned) > int(config["max_h9_calls"]):
        raise RuntimeError("planned H9 calls exceed frozen call budget")
    if len(repairs) > int(config["max_control_repair_calls"]):
        raise RuntimeError("planned control repairs exceed frozen call budget")
    if len(planned) + len(repairs) > int(config["max_calls"]):
        raise RuntimeError("planned calls exceed frozen call budget")
    manifest = {
        "experiment_id": config["experiment_id"],
        "frozen_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "outcomes_loaded": False,
        "config_path": config_path.relative_to(ROOT).as_posix(),
        "config_sha256": base.sha256_file(config_path),
        "protocol_sha256": base.sha256_file(ROOT / str(config["protocol"])),
        "runner_sha256": base.sha256_file(Path(__file__)),
        "packets": packets,
        "sources": sources,
        "controls": controls,
        "planned_h9_calls": len(planned),
        "planned_control_repair_calls": len(repairs),
        "planned_calls": len(planned) + len(repairs),
    }
    base.write_json(output / "freeze_manifest.json", manifest)
    base.write_csv(output / "packet_manifest.csv", packets)
    print(f"prepared_packets={len(packets)}")
    print(f"planned_h9_calls={len(planned)}")
    print(f"planned_control_repair_calls={len(repairs)}")
    print(f"planned_calls={len(planned) + len(repairs)}")


def verify_freeze(config: dict[str, Any]) -> dict[str, Any]:
    path = output_dir(config) / "freeze_manifest.json"
    if not path.exists():
        raise RuntimeError("freeze manifest missing; run prepare first")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("outcomes_loaded") is not False:
        raise RuntimeError("freeze does not certify outcomes_loaded=false")
    for row in manifest["packets"]:
        if base.sha256_file(ROOT / row["path"]) != row["sha256"]:
            raise RuntimeError(f"packet hash mismatch: {row['path']}")
    for row in manifest["sources"]:
        for key in ("event_register", "options", "market_data"):
            if base.sha256_file(ROOT / row[key]) != row[f"{key}_sha256"]:
                raise RuntimeError(f"source hash mismatch: {row[key]}")
    for row in manifest["controls"]:
        if row.get("repair_required"):
            if base.sha256_file(ROOT / row["packet_path"]) != row["packet_sha256"]:
                raise RuntimeError(f"control packet hash mismatch: {row['packet_path']}")
        elif base.sha256_file(ROOT / row["path"]) != row["sha256"]:
            raise RuntimeError(f"control hash mismatch: {row['path']}")
    return manifest


def _call_provider(model: Any, prompt: str, schema: dict[str, Any], retries: int) -> tuple[Any, int]:
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
            return provider_class().run_model(model, prompt, schema, runtime), attempts
        except Exception as exc:
            if attempts > retries or not base._transport_error(str(exc)):
                raise
            time.sleep(2.0 * attempts)


def _run_control_repairs(
    config: dict[str, Any],
    freeze: dict[str, Any],
    episodes: dict[str, dict[str, Any]],
    models: dict[str, Any],
) -> None:
    calls = control_repair_calls(freeze)
    records_dir = output_dir(config) / "records" / "control"
    responses_dir = output_dir(config) / "responses" / "control"
    records_dir.mkdir(parents=True, exist_ok=True)
    responses_dir.mkdir(parents=True, exist_ok=True)
    for position, call in enumerate(calls, start=1):
        stem = base.response_stem(call)
        record_path = records_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if not existing.get("provider_error"):
                parsed = event.canonicalize(
                    existing.get("parsed_json"), episodes[call["replay_id"]], str(config["control_treatment"])
                )
                errors = event.validate_payload(
                    parsed, episodes[call["replay_id"]], str(config["control_treatment"])
                )
                existing.update({"parsed_json": parsed, "validation_errors": errors, "valid": not errors})
                base.write_json(record_path, existing)
                if existing["valid"] or errors != ["response is not a JSON object"]:
                    print(f"[control {position}/{len(calls)}] skip_existing valid={existing['valid']} {stem}", flush=True)
                    continue
        control = next(
            row
            for row in freeze["controls"]
            if row["replay_id"] == call["replay_id"]
            and row["model_id"] == call["model_id"]
            and row.get("repair_required")
        )
        packet = ROOT / control["packet_path"]
        prompt = packet.read_text(encoding="utf-8")
        if base.sha256_text(prompt) != control["packet_sha256"]:
            raise RuntimeError(f"control packet changed after freeze: {packet}")
        print(f"[control {position}/{len(calls)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            result, attempts = _call_provider(
                models[call["model_id"]],
                prompt,
                event.response_schema(str(config["control_treatment"])),
                int(config["transport_retries"]),
            )
            error = result.error
        except Exception as exc:
            result = base.ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = 1
            error = str(exc)
        raw_path = responses_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = event.canonicalize(result.parsed_json, episodes[call["replay_id"]], str(config["control_treatment"]))
        errors = event.validate_payload(parsed, episodes[call["replay_id"]], str(config["control_treatment"]))
        if error:
            errors.append(f"provider_error: {error}")
        usage = result.usage.model_dump(mode="json", exclude_none=True) if hasattr(result.usage, "model_dump") else {}
        record = {
            **call,
            "provider": models[call["model_id"]].provider,
            "api_model_name": models[call["model_id"]].api_model_name,
            "started_at_utc": started,
            "completed_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "attempts": attempts,
            "packet_sha256": control["packet_sha256"],
            "raw_response_sha256": base.sha256_text(result.raw_text),
            "raw_response_path": raw_path.relative_to(ROOT).as_posix(),
            "parsed_json": parsed,
            "usage": usage,
            "provider_error": error,
            "validation_errors": sorted(set(errors)),
            "valid": not errors,
        }
        base.write_json(record_path, record)
        print(f"[control {position}/{len(calls)}] saved valid={record['valid']} {stem}", flush=True)
        if error and not base._transport_error(error):
            raise RuntimeError(f"provider call failed for {stem}: {error}")


def _run_h9_calls(
    config: dict[str, Any],
    freeze: dict[str, Any],
    episodes: dict[str, dict[str, Any]],
    models: dict[str, Any],
) -> None:
    calls = calls_for(config)
    records_dir = output_dir(config) / "records" / "h9"
    responses_dir = output_dir(config) / "responses" / "h9"
    records_dir.mkdir(parents=True, exist_ok=True)
    responses_dir.mkdir(parents=True, exist_ok=True)
    for position, call in enumerate(calls, start=1):
        stem = base.response_stem(call)
        record_path = records_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if not existing.get("provider_error"):
                parsed = canonicalize(existing.get("parsed_json"), episodes[call["replay_id"]])
                errors = validate_payload(parsed, episodes[call["replay_id"]])
                existing.update({"parsed_json": parsed, "validation_errors": errors, "valid": not errors})
                base.write_json(record_path, existing)
                if existing["valid"] or errors != ["response is not a JSON object"]:
                    print(f"[H9 {position}/{len(calls)}] skip_existing valid={existing['valid']} {stem}", flush=True)
                    continue
        packet = output_dir(config) / "packets" / f"{call['replay_id']}__{config['treatment']}.txt"
        prompt = packet.read_text(encoding="utf-8")
        frozen = next(row for row in freeze["packets"] if row["replay_id"] == call["replay_id"])
        if base.sha256_text(prompt) != frozen["sha256"]:
            raise RuntimeError(f"packet changed after freeze: {packet}")
        print(f"[H9 {position}/{len(calls)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            result, attempts = _call_provider(
                models[call["model_id"]], prompt, response_schema(), int(config["transport_retries"])
            )
            error = result.error
        except Exception as exc:
            result = base.ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = 1
            error = str(exc)
        raw_path = responses_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = canonicalize(result.parsed_json, episodes[call["replay_id"]])
        errors = validate_payload(parsed, episodes[call["replay_id"]])
        if error:
            errors.append(f"provider_error: {error}")
        usage = result.usage.model_dump(mode="json", exclude_none=True) if hasattr(result.usage, "model_dump") else {}
        record = {
            **call,
            "provider": models[call["model_id"]].provider,
            "api_model_name": models[call["model_id"]].api_model_name,
            "started_at_utc": started,
            "completed_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "attempts": attempts,
            "packet_sha256": frozen["sha256"],
            "raw_response_sha256": base.sha256_text(result.raw_text),
            "raw_response_path": raw_path.relative_to(ROOT).as_posix(),
            "parsed_json": parsed,
            "usage": usage,
            "provider_error": error,
            "validation_errors": sorted(set(errors)),
            "valid": not errors,
        }
        base.write_json(record_path, record)
        print(f"[H9 {position}/{len(calls)}] saved valid={record['valid']} {stem}", flush=True)
        if error and not base._transport_error(error):
            raise RuntimeError(f"provider call failed for {stem}: {error}")


def run_calls(config_path: Path) -> None:
    config = load_config(config_path)
    freeze = verify_freeze(config)
    episodes = base.episode_index(config)
    models = base.model_index(config)
    base.load_local_env()
    required = {base.PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")
    _run_control_repairs(config, freeze, episodes, models)
    _run_h9_calls(config, freeze, episodes, models)


def load_records(config: dict[str, Any]) -> list[dict[str, Any]]:
    path = output_dir(config) / "records" / "h9"
    return [json.loads(item.read_text(encoding="utf-8")) for item in sorted(path.glob("*.json"))]


def load_control_repair_records(config: dict[str, Any]) -> list[dict[str, Any]]:
    path = output_dir(config) / "records" / "control"
    return [json.loads(item.read_text(encoding="utf-8")) for item in sorted(path.glob("*.json"))]


def load_controls(config: dict[str, Any]) -> list[dict[str, Any]]:
    freeze = verify_freeze(config)
    repair_records = {
        (str(row["replay_id"]), str(row["model_id"])): row
        for row in load_control_repair_records(config)
    }
    controls: list[dict[str, Any]] = []
    for row in freeze["controls"]:
        if row.get("repair_required"):
            record = repair_records.get((str(row["replay_id"]), str(row["model_id"])))
            if record is None:
                raise RuntimeError(f"missing repaired control: {row['replay_id']} {row['model_id']}")
            controls.append(record)
        else:
            controls.append(json.loads((ROOT / row["path"]).read_text(encoding="utf-8")))
    return controls


def score_record(record: dict[str, Any], episode: dict[str, Any], outcome: dict[str, Any], h9: bool) -> dict[str, Any]:
    payload = record.get("parsed_json") if record.get("valid") else None
    row: dict[str, Any] = {
        "replay_id": record["replay_id"],
        "model_id": record["model_id"],
        "treatment": record["treatment"],
        "valid": bool(record.get("valid")),
        "spy_return": outcome["spy_return"],
        "validation_errors": record.get("validation_errors", []),
    }
    if not isinstance(payload, dict):
        return row
    shortlist = stage1b._shortlist_ids(payload, record["treatment"])
    top5 = [str(item["option_id"]) for item in sorted(payload["top5"], key=lambda item: int(item["rank"]))]
    ordered = sorted(outcome["active_returns"].items(), key=lambda item: (-item[1], item[0]))
    top3 = [option_id for option_id, _value in ordered[:3]]
    shortlist_best = max(outcome["returns"][option_id] for option_id in shortlist)
    top5_return = mean(outcome["returns"][option_id] for option_id in top5)
    abstained = h9 and bool(payload.get("prefer_spy"))
    effective_return = outcome["spy_return"] if abstained else top5_return
    row.update(
        {
            "shortlist_ids": shortlist,
            "top5_ids": top5,
            "top3_ids": top3,
            "shortlist_top3_capture_count": len(set(shortlist) & set(top3)),
            "final_top3_capture_count": len(set(top5) & set(top3)),
            "shortlist_oracle_regret": outcome["best_return"] - shortlist_best,
            "top5_return": top5_return,
            "top5_alpha": top5_return - outcome["spy_return"],
            "abstained": abstained,
            "effective_return": effective_return,
            "effective_alpha": effective_return - outcome["spy_return"],
        }
    )
    return row


def _breadth(rows: Sequence[dict[str, Any]], metric: str) -> tuple[int, int, int]:
    by_model: dict[str, list[float]] = defaultdict(list)
    by_episode: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        by_model[str(row["model_id"])].append(float(row[metric]))
        by_episode[str(row["replay_id"])].append(float(row[metric]))
    return (
        sum(float(row[metric]) > 0 for row in rows),
        sum(mean(values) > 0 for values in by_model.values()),
        sum(mean(values) > 0 for values in by_episode.values()),
    )


def evaluate_gate(pairs: Sequence[dict[str, Any]], gate: dict[str, Any]) -> dict[str, Any]:
    valid = [row for row in pairs if row["pair_valid"]]
    improvements = [float(row["effective_return_improvement"]) for row in valid]
    positive_pairs, positive_models, positive_episodes = _breadth(valid, "effective_return_improvement") if valid else (0, 0, 0)
    mean_improvement = mean(improvements) if improvements else None
    treatment_alpha = mean(float(row["challenger_effective_alpha"]) for row in valid) if valid else None
    control_regret = mean(float(row["control_regret"]) for row in valid) if valid else None
    challenger_regret = mean(float(row["challenger_regret"]) for row in valid) if valid else None
    relative_regret_reduction = (
        (control_regret - challenger_regret) / control_regret
        if control_regret and challenger_regret is not None else None
    )
    capture_change = sum(int(row["top3_capture_change"]) for row in valid)
    episode_changes: dict[str, list[float]] = defaultdict(list)
    for row in valid:
        episode_changes[str(row["replay_id"])].append(float(row["effective_return_improvement"]))
    worst_episode_change = min((mean(values) for values in episode_changes.values()), default=None)
    passes = bool(
        len(valid) >= int(gate["minimum_valid_pairs"])
        and mean_improvement is not None
        and mean_improvement >= float(gate["minimum_mean_effective_return_improvement"])
        and (not gate["require_positive_treatment_alpha"] or (treatment_alpha is not None and treatment_alpha > 0))
        and positive_pairs >= int(gate["minimum_positive_pairs"])
        and positive_models >= int(gate["minimum_positive_models"])
        and positive_episodes >= int(gate["minimum_positive_episodes"])
        and relative_regret_reduction is not None
        and relative_regret_reduction >= float(gate["minimum_relative_shortlist_regret_reduction"])
        and (not gate["require_nonnegative_top3_capture_change"] or capture_change >= 0)
        and worst_episode_change is not None
        and worst_episode_change >= float(gate["minimum_worst_episode_alpha_change"])
    )
    return {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passes_gate": passes,
        "valid_pairs": len(valid),
        "mean_effective_return_improvement": mean_improvement,
        "mean_treatment_alpha_vs_spy": treatment_alpha,
        "positive_pairs": positive_pairs,
        "positive_models": positive_models,
        "positive_episodes": positive_episodes,
        "relative_shortlist_regret_reduction": relative_regret_reduction,
        "top3_capture_change": capture_change,
        "worst_episode_alpha_change": worst_episode_change,
        "abstentions": sum(bool(row["challenger_abstained"]) for row in valid),
    }


def usage(records: Sequence[dict[str, Any]]) -> dict[str, int]:
    return {
        "calls": len(records),
        "valid_calls": sum(bool(row.get("valid")) for row in records),
        "input_tokens": sum(int((row.get("usage") or {}).get("input_tokens") or 0) for row in records),
        "output_tokens": sum(int((row.get("usage") or {}).get("output_tokens") or 0) for row in records),
        "reasoning_tokens": sum(int((row.get("usage") or {}).get("reasoning_tokens") or 0) for row in records),
    }


def lane_diagnostic(config: dict[str, Any], records: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    episodes = base.episode_index(config)
    outcomes = {key: base.load_outcomes(value) for key, value in episodes.items()}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if not record.get("valid"):
            continue
        payload = record.get("parsed_json") or {}
        outcome = outcomes[str(record["replay_id"])]
        top3 = {
            option_id
            for option_id, _value in sorted(
                outcome["active_returns"].items(), key=lambda item: (-item[1], item[0])
            )[:3]
        }
        top5 = {str(row["option_id"]) for row in payload.get("top5") or []}
        for row in payload.get("shortlist") or []:
            option_id = str(row["option_id"])
            grouped[str(row["search_lane"])].append(
                {
                    "alpha": outcome["returns"][option_id] - outcome["spy_return"],
                    "top3": option_id in top3,
                    "top5": option_id in top5,
                    "supported": bool(row.get("event_ids")),
                }
            )
    return [
        {
            "lane": lane,
            "observations": len(rows),
            "mean_realized_alpha": mean(float(row["alpha"]) for row in rows),
            "positive_alpha_share": sum(float(row["alpha"]) > 0 for row in rows) / len(rows),
            "top3_capture_count": sum(bool(row["top3"]) for row in rows),
            "final_selection_share": sum(bool(row["top5"]) for row in rows) / len(rows),
            "mapped_evidence_share": sum(bool(row["supported"]) for row in rows) / len(rows),
        }
        for lane, rows in sorted(grouped.items())
    ]


def _pct(value: Any) -> str:
    return "n/a" if value is None else f"{float(value) * 100:.2f}%"


def write_result(
    config: dict[str, Any],
    decision: dict[str, Any],
    pairs: Sequence[dict[str, Any]],
    records: Sequence[dict[str, Any]],
) -> None:
    result_decision = "accepted_for_prospective_shadow" if decision["passes_gate"] else "rejected"
    lanes = lane_diagnostic(config, records)
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": result_decision,
        "official_score_eligible": False,
        "production_impact": "none",
        "gate": decision,
        "usage": usage([*load_control_repair_records(config), *records]),
        "lane_diagnostic": lanes,
        "limitations": [
            "All four periods are historical development data previously used by related experiments.",
            "Current models may remember historical outcomes.",
            "A pass authorizes only a prospective private shadow, not a production change.",
        ],
    }
    base.write_json(ROOT / str(config["canonical_summary"]), summary)
    pair_rows = [
        [
            row["replay_id"],
            row["model_id"],
            _pct(row.get("control_effective_alpha")),
            _pct(row.get("challenger_effective_alpha")),
            _pct(row.get("effective_return_improvement")),
            "Yes" if row.get("challenger_abstained") else "No",
        ]
        for row in pairs
        if row["pair_valid"]
    ]
    lane_rows = [
        [
            row["lane"],
            row["observations"],
            _pct(row["mean_realized_alpha"]),
            _pct(row["positive_alpha_share"]),
            row["top3_capture_count"],
            _pct(row["mapped_evidence_share"]),
        ]
        for row in lanes
    ]
    report = "\n".join(
        [
            "# VNext Symmetric Coverage Replay Results",
            "",
            f"Decision: **{result_decision}**",
            "",
            "## Frozen Gate",
            "",
            f"- Valid pairs: {decision['valid_pairs']}",
            f"- Mean effective-return improvement over H4: {_pct(decision['mean_effective_return_improvement'])}",
            f"- Mean H9 effective alpha versus SPY: {_pct(decision['mean_treatment_alpha_vs_spy'])}",
            f"- Positive pairs/models/episodes: {decision['positive_pairs']}/{decision['positive_models']}/{decision['positive_episodes']}",
            f"- Relative shortlist-regret reduction: {_pct(decision['relative_shortlist_regret_reduction'])}",
            f"- Top-three shortlist capture change: {decision['top3_capture_change']}",
            f"- Worst episode alpha change: {_pct(decision['worst_episode_alpha_change'])}",
            f"- Abstentions: {decision['abstentions']}",
            f"- Gate: {'pass' if decision['passes_gate'] else 'fail'}",
            "",
            "## Paired Results",
            "",
            base.markdown_table(
                ["Episode", "Model", "H4 alpha", "H9 effective alpha", "Change", "SPY preferred"],
                pair_rows,
            ),
            "",
            "## Lane Diagnostics",
            "",
            base.markdown_table(
                ["Lane", "Candidates", "Mean realized alpha", "Positive alpha", "Top-three captures", "Mapped evidence"],
                lane_rows,
            ),
            "",
            "## Execution",
            "",
            f"- Provider calls: {summary['usage']['calls']}",
            f"- Valid calls: {summary['usage']['valid_calls']}",
            f"- Input tokens: {summary['usage']['input_tokens']:,}",
            f"- Output tokens: {summary['usage']['output_tokens']:,}",
            f"- Reasoning tokens: {summary['usage']['reasoning_tokens']:,}",
            "",
            "## Interpretation",
            "",
            "H9 is a historical development screen. It can reject a weak symmetric-coverage design but cannot establish prospective investment skill. Production Portfolio V2.0 remains unchanged.",
            "",
        ]
    )
    (ROOT / str(config["canonical_report"])).write_text(report, encoding="utf-8", newline="\n")


def score(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    episodes = base.episode_index(config)
    outcomes = {key: base.load_outcomes(value) for key, value in episodes.items()}
    controls = [score_record(row, episodes[row["replay_id"]], outcomes[row["replay_id"]], h9=False) for row in load_controls(config)]
    challengers_raw = load_records(config)
    challengers = [score_record(row, episodes[row["replay_id"]], outcomes[row["replay_id"]], h9=True) for row in challengers_raw]
    grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in [*controls, *challengers]:
        grouped[(str(row["replay_id"]), str(row["model_id"]))][str(row["treatment"])] = row
    pairs: list[dict[str, Any]] = []
    for (replay_id, model_id), treatments in sorted(grouped.items()):
        left = treatments.get(str(config["control_treatment"]))
        right = treatments.get(str(config["treatment"]))
        valid = bool(left and right and left.get("valid") and right.get("valid"))
        row: dict[str, Any] = {
            "replay_id": replay_id,
            "model_id": model_id,
            "pair_valid": valid,
        }
        if valid and left and right:
            row.update(
                {
                    "control_effective_alpha": left["effective_alpha"],
                    "challenger_effective_alpha": right["effective_alpha"],
                    "effective_return_improvement": right["effective_return"] - left["effective_return"],
                    "control_regret": left["shortlist_oracle_regret"],
                    "challenger_regret": right["shortlist_oracle_regret"],
                    "top3_capture_change": right["shortlist_top3_capture_count"] - left["shortlist_top3_capture_count"],
                    "challenger_abstained": right["abstained"],
                }
            )
        pairs.append(row)
    decision = evaluate_gate(pairs, config["gate"])
    output = output_dir(config)
    base.write_csv(output / "call_metrics.csv", [*controls, *challengers])
    base.write_csv(output / "pairs.csv", pairs)
    base.write_json(output / "decision.json", decision)
    write_result(config, decision, pairs, challengers_raw)
    print(json.dumps(decision, indent=2))
    return decision


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "run", "score"])
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    if args.command == "prepare":
        prepare(config_path)
    elif args.command == "run":
        run_calls(config_path)
    else:
        score(config_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

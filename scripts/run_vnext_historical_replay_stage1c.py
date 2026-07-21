from __future__ import annotations

import argparse
import copy
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


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = _load_module("vnext_replay_base_for_stage1c", ROOT / "scripts" / "run_vnext_historical_replay.py")
stage1b = _load_module("vnext_replay_stage1b_for_stage1c", ROOT / "scripts" / "run_vnext_historical_replay_stage1b.py")

DEFAULT_CONFIG = ROOT / "experiments" / "vnext-historical-replay-stage1c-2026-07-21.yaml"
DEFAULT_REPORT = ROOT / "docs" / "vnext_historical_replay_stage1c_report.md"
RANKING_LANES = ("continuation", "quality_pullback", "capitulation_rebound", "context_defensive", "other")
SELECTION_ROLES = ("continuation", "quality_pullback", "capitulation_rebound", "free")


def load_config(path: Path) -> dict[str, Any]:
    return base.load_yaml(path)


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def h4_output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["h4_output_dir"])


def h0_output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["h0_output_dir"])


def episode_index(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return base.episode_index(config)


def _prior_record_path(config: dict[str, Any], replay_id: str, model_id: str, treatment: str) -> Path:
    call = {"replay_id": replay_id, "model_id": model_id, "treatment": treatment}
    stem = base.response_stem(call)
    if treatment == "H4":
        return h4_output_dir(config) / "records" / "primary" / f"{stem}.json"
    if treatment == "H0":
        return h0_output_dir(config) / "records" / "discovery" / f"{stem}.json"
    raise ValueError(f"unsupported prior treatment: {treatment}")


def _load_prior_record(config: dict[str, Any], replay_id: str, model_id: str, treatment: str) -> dict[str, Any]:
    path = _prior_record_path(config, replay_id, model_id, treatment)
    if not path.exists():
        raise RuntimeError(f"missing prior record: {path}")
    record = json.loads(path.read_text(encoding="utf-8"))
    if not record.get("valid"):
        raise RuntimeError(f"prior record is not valid: {path}")
    return record


def _h4_shortlist(record: dict[str, Any]) -> list[dict[str, str]]:
    shortlist = record.get("parsed_json", {}).get("shortlist")
    if not isinstance(shortlist, list) or len(shortlist) != 10:
        raise RuntimeError("H4 record does not contain a ten-name shortlist")
    return [
        {
            "option_id": str(item["option_id"]),
            "candidate_lane": str(item["candidate_lane"]),
        }
        for item in shortlist
    ]


def _candidate_rows(episode: dict[str, Any], shortlist: Sequence[dict[str, str]]) -> str:
    rows = {str(row["option_id"]): row for row in stage1b._active_rows(episode)}
    data: list[list[str]] = []
    for item in shortlist:
        row = rows[item["option_id"]]
        data.append(
            [
                item["option_id"],
                str(row.get("symbol") or ""),
                item["candidate_lane"],
                str(row.get("option_group") or ""),
                str(row.get("risk_bucket") or ""),
                base._pct(row.get("active_return_7d")),
                base._pct(row.get("active_return_30d")),
                base._rank(row.get("rank_return_7d")),
                base._rank(row.get("rank_return_30d")),
                base._rank(row.get("rank_return_6m")),
                base._rank(row.get("rank_return_1y")),
                base._rank(row.get("recent_vs_medium_rank_shift")),
                base._rank(row.get("trend_rank_dispersion")),
            ]
        )
    return base.markdown_table(
        [
            "option_id",
            "symbol",
            "H4 lane",
            "group",
            "risk",
            "7d alpha",
            "30d alpha",
            "7d pctile",
            "30d pctile",
            "6m pctile",
            "1y pctile",
            "7d-30d rank shift",
            "trend dispersion",
        ],
        data,
    )


def _briefing(episode: dict[str, Any]) -> str:
    round_path = base.source_round(episode)
    path = round_path / "research" / "final_briefing.md"
    if not path.exists():
        path = round_path / "briefing.md"
    return base.sanitize_full_briefing(path.read_text(encoding="utf-8"))


RANKING_TASK = """
You are participating in a private, retrospective CapitalBench input experiment.
Treat this as an unknown decision point. Use only this packet. Do not use
remembered outcomes, tools, browsing, search, or external facts. The horizon is
one week.

Assess all ten shortlisted options before selecting a final five. For every
candidate, estimate its probability of beating SPY, probability of finishing
in the top decile of active assets, and probability of a materially negative
one-week return. Probabilities must be between 0 and 100.

Distinguish quality_pullback from capitulation_rebound. A quality pullback is a
recent decline with stronger medium- or long-horizon structure. A capitulation
rebound is an unusually sharp dislocation where a rapid rebound is plausible
despite substantial downside risk.

The final five must contain exactly one continuation role, one quality_pullback
role, one capitulation_rebound role, and two free roles. Forecast SPY separately.
expected_alpha_vs_spy_pct must equal the candidate forecast minus the SPY
forecast. Return only JSON matching the supplied schema.
""".strip()


def diagnostic_prompt(config: dict[str, Any], episode: dict[str, Any], model_id: str) -> str:
    record = _load_prior_record(config, episode["replay_id"], model_id, "H4")
    shortlist = _h4_shortlist(record)
    return (
        f"{RANKING_TASK}\n\n"
        f"Replay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {config['diagnostic_treatment']}\n\n"
        "This is a ranking-only diagnostic. Preserve the exact ten option IDs and H4 candidate-lane labels shown below. Do not add or remove candidates.\n\n"
        f"Entry-time market summary:\n{stage1b.market_summary(episode)}\n\n"
        f"Frozen ten-candidate table:\n{_candidate_rows(episode, shortlist)}\n\n"
        f"Frozen factual briefing:\n{_briefing(episode)}\n"
    )


def integrated_prompt(config: dict[str, Any], episode: dict[str, Any]) -> str:
    rows = base.derived_market_rows(base.common_market_rows(base.source_round(episode)))
    return (
        f"{RANKING_TASK}\n\n"
        f"Replay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {config['integrated_treatment']}\n\n"
        "This is a single-turn integrated test. First build a balanced ten-name shortlist from the complete universe. It must contain exactly three continuation, three reversal, two context, one defensive, and one wildcard candidate. No more than four shortlist names may share an option group. Then assess all ten and build the role-constrained final five.\n\n"
        f"Entry-time market summary:\n{stage1b.market_summary(episode)}\n\n"
        f"Mechanical candidate references:\n{stage1b.lane_reference_table(episode)}\n\n"
        f"Frozen factual briefing:\n{_briefing(episode)}\n\n"
        f"Complete option comparison table:\n{base.derived_market_table(rows)}\n"
    )


def response_schema(treatment: str) -> dict[str, Any]:
    if treatment == "H0":
        return base.response_schema()
    top5 = copy.deepcopy(base.response_schema()["properties"]["top5"]["items"])
    top5["properties"]["selection_role"] = {"type": "string", "enum": list(SELECTION_ROLES)}
    top5["required"].append("selection_role")
    shortlist_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "option_id": {"type": "string"},
            "candidate_lane": {"type": "string", "enum": list(stage1b.LANES)},
        },
        "required": ["option_id", "candidate_lane"],
    }
    assessment_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "option_id": {"type": "string"},
            "ranking_lane": {"type": "string", "enum": list(RANKING_LANES)},
            "probability_beats_spy_pct": {"type": "number", "minimum": 0, "maximum": 100},
            "probability_top_decile_pct": {"type": "number", "minimum": 0, "maximum": 100},
            "downside_probability_pct": {"type": "number", "minimum": 0, "maximum": 100},
            "assessment": {"type": "string"},
        },
        "required": [
            "option_id",
            "ranking_lane",
            "probability_beats_spy_pct",
            "probability_top_decile_pct",
            "downside_probability_pct",
            "assessment",
        ],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "replay_id": {"type": "string"},
            "treatment_id": {"type": "string"},
            "spy_forecast_return_pct": {"type": "number"},
            "prefer_spy": {"type": "boolean"},
            "shortlist": {"type": "array", "minItems": 10, "maxItems": 10, "items": shortlist_item},
            "candidate_assessments": {
                "type": "array",
                "minItems": 10,
                "maxItems": 10,
                "items": assessment_item,
            },
            "top5": {"type": "array", "minItems": 5, "maxItems": 5, "items": top5},
        },
        "required": [
            "replay_id",
            "treatment_id",
            "spy_forecast_return_pct",
            "prefer_spy",
            "shortlist",
            "candidate_assessments",
            "top5",
        ],
    }


def canonicalize_payload(payload: Any, episode: dict[str, Any], treatment: str) -> Any:
    if treatment == "H0":
        return base.canonicalize_option_ids(payload, episode)
    if not isinstance(payload, dict):
        return payload
    aliases = stage1b._alias_map(episode)

    def canonical(value: Any) -> str:
        text = str(value or "").strip()
        return aliases.get(text.upper(), text)

    normalized = json.loads(json.dumps(payload))
    for key in ("shortlist", "candidate_assessments", "top5"):
        if isinstance(normalized.get(key), list):
            for item in normalized[key]:
                if isinstance(item, dict):
                    item["option_id"] = canonical(item.get("option_id"))
    return normalized


def _shortlist_ids(payload: dict[str, Any], treatment: str) -> list[str]:
    if treatment == "H0":
        return [str(value) for value in payload.get("shortlist_option_ids", [])]
    if treatment == "H4":
        return stage1b._shortlist_ids(payload, treatment)
    return [str(item.get("option_id") or "") for item in payload.get("shortlist", []) if isinstance(item, dict)]


def validate_payload(
    config: dict[str, Any],
    payload: Any,
    episode: dict[str, Any],
    model_id: str,
    treatment: str,
) -> list[str]:
    if treatment == "H0":
        return base.validate_payload(payload, episode, treatment)
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    shortlist = payload.get("shortlist")
    shortlist_ids = _shortlist_ids(payload, treatment)
    translated = copy.deepcopy(payload)
    translated["shortlist_option_ids"] = shortlist_ids
    errors = base.validate_payload(translated, episode, treatment)
    if not isinstance(shortlist, list) or len(shortlist) != 10:
        errors.append("shortlist must contain exactly 10 rows")
        shortlist = []
    candidate_lanes = [str(item.get("candidate_lane") or "") for item in shortlist if isinstance(item, dict)]
    if any(lane not in stage1b.LANES for lane in candidate_lanes):
        errors.append("invalid candidate lane")
    diagnostic = str(config["diagnostic_treatment"])
    integrated = str(config["integrated_treatment"])
    if treatment == diagnostic:
        frozen = _h4_shortlist(_load_prior_record(config, episode["replay_id"], model_id, "H4"))
        frozen_map = {item["option_id"]: item["candidate_lane"] for item in frozen}
        response_map = {
            str(item.get("option_id") or ""): str(item.get("candidate_lane") or "")
            for item in shortlist if isinstance(item, dict)
        }
        if response_map != frozen_map:
            errors.append("diagnostic shortlist or H4 lane labels changed")
    if treatment == integrated:
        counts = Counter(candidate_lanes)
        expected = {"continuation": 3, "reversal": 3, "context": 2, "defensive": 1, "wildcard": 1}
        if any(counts[lane] != count for lane, count in expected.items()):
            errors.append("integrated shortlist lane counts are invalid")
        options = {str(row["id"]): row for row in base.load_options(base.source_round(episode))}
        groups = Counter(str(options.get(option_id, {}).get("option_group") or "") for option_id in shortlist_ids)
        if any(group and count > 4 for group, count in groups.items()):
            errors.append("integrated shortlist exceeds the option-group cap")
    assessments = payload.get("candidate_assessments")
    assessment_map: dict[str, dict[str, Any]] = {}
    if not isinstance(assessments, list) or len(assessments) != 10:
        errors.append("candidate assessments must contain exactly 10 rows")
    else:
        for item in assessments:
            if not isinstance(item, dict):
                errors.append("candidate assessment row is not an object")
                continue
            option_id = str(item.get("option_id") or "")
            assessment_map[option_id] = item
            if item.get("ranking_lane") not in RANKING_LANES:
                errors.append(f"invalid ranking lane for {option_id}")
            for key in ("probability_beats_spy_pct", "probability_top_decile_pct", "downside_probability_pct"):
                value = base.as_float(item.get(key))
                if value is None or value < 0 or value > 100:
                    errors.append(f"invalid probability {key} for {option_id}")
            if not str(item.get("assessment") or "").strip():
                errors.append(f"missing assessment for {option_id}")
        if set(assessment_map) != set(shortlist_ids):
            errors.append("candidate assessment IDs must equal shortlist IDs")
    top5 = payload.get("top5") if isinstance(payload.get("top5"), list) else []
    roles = Counter(str(item.get("selection_role") or "") for item in top5 if isinstance(item, dict))
    expected_roles = {"continuation": 1, "quality_pullback": 1, "capitulation_rebound": 1, "free": 2}
    if any(roles[role] != count for role, count in expected_roles.items()):
        errors.append("final-five selection roles are invalid")
    for item in top5:
        if not isinstance(item, dict):
            continue
        role = str(item.get("selection_role") or "")
        option_id = str(item.get("option_id") or "")
        if role != "free" and assessment_map.get(option_id, {}).get("ranking_lane") != role:
            errors.append(f"selection role does not match ranking lane for {option_id}")
    return sorted(set(errors))


def diagnostic_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    treatment = str(config["diagnostic_treatment"])
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"] if episode["phase"] == "discovery"
        for model_id in config["models"]
    ]


def integrated_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    treatment = str(config["integrated_treatment"])
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"] if episode["phase"] == "discovery"
        for model_id in config["models"]
    ]


def confirmation_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    treatment = str(config["integrated_treatment"])
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": selected}
        for episode in config["episodes"] if episode["phase"] == "confirmation"
        for model_id in config["models"]
        for selected in ("H0", treatment)
    ]


def _packet_path(config: dict[str, Any], call: dict[str, str]) -> Path:
    packet_dir = output_dir(config) / "packets"
    if call["treatment"] == str(config["diagnostic_treatment"]):
        return packet_dir / f"{call['replay_id']}__{call['model_id']}__{call['treatment']}.txt"
    return packet_dir / f"{call['replay_id']}__{call['treatment']}.txt"


def _prompt_for_call(config: dict[str, Any], call: dict[str, str]) -> str:
    episode = episode_index(config)[call["replay_id"]]
    if call["treatment"] == str(config["diagnostic_treatment"]):
        return diagnostic_prompt(config, episode, call["model_id"])
    if call["treatment"] == str(config["integrated_treatment"]):
        return integrated_prompt(config, episode)
    if call["treatment"] == "H0":
        return base.build_prompt(config, episode, "H0")
    raise ValueError(f"unsupported treatment: {call['treatment']}")


def prepare(config_path: Path) -> None:
    config = load_config(config_path)
    output = output_dir(config)
    packet_dir = output / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    planned_calls = diagnostic_calls(config) + integrated_calls(config) + confirmation_calls(config)
    unique: dict[str, dict[str, str]] = {}
    for call in planned_calls:
        unique[str(_packet_path(config, call))] = call
    packets: list[dict[str, Any]] = []
    for call in unique.values():
        prompt = _prompt_for_call(config, call)
        path = _packet_path(config, call)
        path.write_text(prompt, encoding="utf-8", newline="\n")
        packets.append(
            {
                **call,
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": base.sha256_text(prompt),
                "bytes": len(prompt.encode("utf-8")),
                "estimated_tokens": (len(prompt) + 3) // 4,
                "schema_sha256": base.sha256_text(json.dumps(response_schema(call["treatment"]), sort_keys=True)),
            }
        )
    frozen_records: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        if episode["phase"] != "discovery":
            continue
        for model_id in config["models"]:
            for treatment in ("H4", "H0"):
                path = _prior_record_path(config, episode["replay_id"], model_id, treatment)
                record = _load_prior_record(config, episode["replay_id"], model_id, treatment)
                frozen_records.append(
                    {
                        "replay_id": episode["replay_id"],
                        "model_id": model_id,
                        "treatment": treatment,
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
        "config_sha256": base.sha256_file(config_path),
        "protocol_sha256": base.sha256_file(protocol_path),
        "runner_sha256": base.sha256_file(Path(__file__)),
        "packets": packets,
        "frozen_prior_records": frozen_records,
        "planned_diagnostic_calls": len(diagnostic_calls(config)),
        "planned_integrated_calls": len(integrated_calls(config)),
        "planned_confirmation_calls": len(confirmation_calls(config)),
    }
    base.write_json(output / "freeze_manifest.json", manifest)
    base.write_csv(output / "packet_manifest.csv", packets)
    print(f"prepared_packets={len(packets)}")
    print(f"frozen_prior_records={len(frozen_records)}")
    print(f"diagnostic_calls={len(diagnostic_calls(config))}")
    print(f"integrated_calls={len(integrated_calls(config))}")
    print(f"confirmation_calls={len(confirmation_calls(config))}")


def verify_freeze(config: dict[str, Any]) -> dict[str, Any]:
    path = output_dir(config) / "freeze_manifest.json"
    if not path.exists():
        raise RuntimeError("freeze manifest is missing")
    freeze = json.loads(path.read_text(encoding="utf-8"))
    if freeze.get("outcomes_loaded") is not False:
        raise RuntimeError("freeze does not certify outcomes_loaded=false")
    for row in freeze["packets"]:
        if base.sha256_file(ROOT / row["path"]) != row["sha256"]:
            raise RuntimeError(f"packet hash mismatch: {row['path']}")
    for row in freeze["frozen_prior_records"]:
        if base.sha256_file(ROOT / row["path"]) != row["sha256"]:
            raise RuntimeError(f"prior record hash mismatch: {row['path']}")
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
            return provider_class().run_model(model, prompt, response_schema(treatment), runtime), attempts
        except Exception as exc:
            if attempts > retries or not base._transport_error(str(exc)):
                raise
            time.sleep(2.0 * attempts)


def _stage_allowed(config: dict[str, Any], phase: str) -> bool:
    output = output_dir(config)
    if phase == "diagnostic":
        return True
    diagnostic_path = output / "diagnostic_decision.json"
    if not diagnostic_path.exists():
        raise RuntimeError("score diagnostic first")
    diagnostic = json.loads(diagnostic_path.read_text(encoding="utf-8"))
    if phase == "integrated":
        return bool(diagnostic.get("passes_gate"))
    integrated_path = output / "integrated_decision.json"
    if not integrated_path.exists():
        raise RuntimeError("score integrated first")
    integrated = json.loads(integrated_path.read_text(encoding="utf-8"))
    return bool(integrated.get("passes_gate"))


def run_calls(config_path: Path, phase: str) -> None:
    config = load_config(config_path)
    freeze = verify_freeze(config)
    if not _stage_allowed(config, phase):
        print(f"{phase}_skipped=prior gate did not pass")
        return
    if phase == "diagnostic":
        calls = diagnostic_calls(config)
    elif phase == "integrated":
        calls = integrated_calls(config)
    elif phase == "confirmation":
        calls = confirmation_calls(config)
    else:
        raise ValueError(f"unknown phase: {phase}")
    models = base.model_index(config)
    episodes = episode_index(config)
    base.load_local_env()
    required_env = {base.PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required_env if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")
    records_dir = output_dir(config) / "records" / phase
    responses_dir = output_dir(config) / "responses" / phase
    records_dir.mkdir(parents=True, exist_ok=True)
    responses_dir.mkdir(parents=True, exist_ok=True)
    completed = 0
    for position, call in enumerate(calls, start=1):
        stem = base.response_stem(call)
        record_path = records_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if not existing.get("provider_error"):
                normalized = canonicalize_payload(existing.get("parsed_json"), episodes[call["replay_id"]], call["treatment"])
                errors = validate_payload(config, normalized, episodes[call["replay_id"]], call["model_id"], call["treatment"])
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
        packet_path = _packet_path(config, call)
        prompt = packet_path.read_text(encoding="utf-8")
        packet_hash = base.sha256_text(prompt)
        frozen = next(row for row in freeze["packets"] if row["path"] == packet_path.relative_to(ROOT).as_posix())
        if packet_hash != frozen["sha256"]:
            raise RuntimeError(f"packet changed after freeze: {packet_path}")
        print(f"[{position}/{len(calls)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            result, attempts = _call_provider(models[call["model_id"]], prompt, call["treatment"], int(config["transport_retries"]))
            error = result.error
        except Exception as exc:
            result = base.ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = 1
            error = str(exc)
        completed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        raw_path = responses_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = canonicalize_payload(result.parsed_json, episodes[call["replay_id"]], call["treatment"])
        errors = validate_payload(config, parsed, episodes[call["replay_id"]], call["model_id"], call["treatment"])
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


def _phase_records(config: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    directory = output_dir(config) / "records" / phase
    if not directory.exists():
        return []
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.json"))]


def _score_record(record: dict[str, Any], episode: dict[str, Any], outcome: dict[str, Any]) -> dict[str, Any]:
    payload = record.get("parsed_json") if record.get("valid") else None
    result = {
        "replay_id": episode["replay_id"],
        "model_id": record["model_id"],
        "treatment": record["treatment"],
        "valid": bool(record.get("valid")),
        "input_tokens": (record.get("usage") or {}).get("input_tokens"),
        "output_tokens": (record.get("usage") or {}).get("output_tokens"),
        "reasoning_tokens": (record.get("usage") or {}).get("reasoning_tokens"),
        "latency_seconds": (record.get("usage") or {}).get("latency_seconds"),
    }
    if not isinstance(payload, dict):
        return result
    treatment = str(record["treatment"])
    shortlist = _shortlist_ids(payload, treatment)
    top5 = [str(item["option_id"]) for item in sorted(payload["top5"], key=lambda item: int(item["rank"]))]
    ordered = sorted(outcome["active_returns"].items(), key=lambda item: (-item[1], item[0]))
    top2 = [option_id for option_id, _return in ordered[:2]]
    top5_return = mean(outcome["returns"][option_id] for option_id in top5)
    result.update(
        {
            "shortlist_ids": shortlist,
            "top5_ids": top5,
            "top2_ids": top2,
            "shortlist_top2_capture_count": len(set(shortlist) & set(top2)),
            "top5_top2_capture_count": len(set(top5) & set(top2)),
            "top5_return": top5_return,
            "top5_alpha": top5_return - outcome["spy_return"],
        }
    )
    return result


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


def _prior_records(config: dict[str, Any], treatment: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        if episode["phase"] != "discovery":
            continue
        for model_id in config["models"]:
            records.append(_load_prior_record(config, episode["replay_id"], model_id, treatment))
    return records


def _paired(scored: Sequence[dict[str, Any]], control_treatment: str, challenger_treatment: str) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in scored:
        grouped[(str(row["replay_id"]), str(row["model_id"]))][str(row["treatment"])] = row
    pairs: list[dict[str, Any]] = []
    for (replay_id, model_id), treatments in sorted(grouped.items()):
        control = treatments.get(control_treatment)
        challenger = treatments.get(challenger_treatment)
        if control is None or challenger is None:
            continue
        valid = bool(control.get("valid")) and bool(challenger.get("valid"))
        pairs.append(
            {
                "replay_id": replay_id,
                "model_id": model_id,
                "control": control_treatment,
                "challenger": challenger_treatment,
                "pair_valid": valid,
                "control_shortlist_top2": control.get("shortlist_top2_capture_count"),
                "challenger_shortlist_top2": challenger.get("shortlist_top2_capture_count"),
                "control_top5_top2": control.get("top5_top2_capture_count"),
                "challenger_top5_top2": challenger.get("top5_top2_capture_count"),
                "top5_capture_change": (
                    int(challenger["top5_top2_capture_count"]) - int(control["top5_top2_capture_count"])
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


def _gate(config: dict[str, Any], pairs: Sequence[dict[str, Any]], integrated: bool = False, confirmation: bool = False) -> dict[str, Any]:
    valid = [row for row in pairs if row["pair_valid"]]
    alpha = [float(row["alpha_improvement"]) for row in valid]
    control_captures = sum(int(row["control_top5_top2"]) for row in valid)
    challenger_captures = sum(int(row["challenger_top5_top2"]) for row in valid)
    challenger_shortlist = sum(int(row["challenger_shortlist_top2"]) for row in valid)
    capture_episodes = len({row["replay_id"] for row in valid if int(row["challenger_top5_top2"]) > 0})
    capture_models = len({row["model_id"] for row in valid if int(row["challenger_top5_top2"]) > 0})
    by_model: dict[str, list[float]] = defaultdict(list)
    by_episode: dict[str, list[float]] = defaultdict(list)
    for row in valid:
        by_model[str(row["model_id"])].append(float(row["alpha_improvement"]))
        by_episode[str(row["replay_id"])].append(float(row["alpha_improvement"]))
    positive_models = sum(mean(values) > 0 for values in by_model.values())
    positive_episodes = sum(mean(values) > 0 for values in by_episode.values())
    gates = config["gates"]
    minimum_alpha = 0.0 if confirmation else float(gates["minimum_mean_alpha_improvement"])
    passes = bool(
        len(valid) >= int(gates["minimum_valid_pairs"])
        and challenger_captures > control_captures
        and capture_episodes >= int(gates["minimum_capture_episodes"])
        and capture_models >= int(gates["minimum_capture_models"])
        and alpha and mean(alpha) > minimum_alpha
        and sum(value > 0 for value in alpha) >= int(gates["minimum_positive_pairs"])
        and positive_models >= int(gates["minimum_positive_models"])
        and positive_episodes >= int(gates["minimum_positive_episodes"])
        and (
            not integrated
            or challenger_shortlist >= int(gates["minimum_integrated_shortlist_top2_captures"])
        )
    )
    return {
        "valid_pairs": len(valid),
        "control_top5_top2_captures": control_captures,
        "challenger_top5_top2_captures": challenger_captures,
        "top5_capture_change": challenger_captures - control_captures,
        "challenger_shortlist_top2_captures": challenger_shortlist,
        "capture_episodes": capture_episodes,
        "capture_models": capture_models,
        "mean_alpha_improvement": mean(alpha) if alpha else None,
        "positive_pairs": sum(value > 0 for value in alpha),
        "positive_models": positive_models,
        "positive_episodes": positive_episodes,
        "passes_gate": passes,
    }


def _score_stage(
    config_path: Path,
    phase: str,
    control_treatment: str,
    challenger_treatment: str,
    integrated: bool = False,
    confirmation: bool = False,
) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    if phase == "diagnostic":
        records = _prior_records(config, control_treatment) + _phase_records(config, phase)
    elif phase == "integrated":
        records = _prior_records(config, control_treatment) + _phase_records(config, phase)
    else:
        records = _phase_records(config, phase)
    scored = _score_records(config, records)
    pairs = _paired(scored, control_treatment, challenger_treatment)
    gate = _gate(config, pairs, integrated=integrated, confirmation=confirmation)
    decision = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "phase": phase,
        "control_treatment": control_treatment,
        "challenger_treatment": challenger_treatment,
        **gate,
    }
    output = output_dir(config)
    base.write_csv(output / f"{phase}_call_metrics.csv", scored)
    base.write_csv(output / f"{phase}_pairs.csv", pairs)
    base.write_json(output / f"{phase}_decision.json", decision)
    print(json.dumps(decision, indent=2))
    return decision


def score_diagnostic(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    return _score_stage(config_path, "diagnostic", "H4", str(config["diagnostic_treatment"]))


def score_integrated(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    return _score_stage(config_path, "integrated", "H0", str(config["integrated_treatment"]), integrated=True)


def score_confirmation(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    if not _stage_allowed(config, "confirmation"):
        decision = {"phase": "confirmation", "passes_gate": False, "skipped": "integrated gate did not pass"}
        base.write_json(output_dir(config) / "confirmation_decision.json", decision)
        print(json.dumps(decision, indent=2))
        return decision
    return _score_stage(config_path, "confirmation", "H0", str(config["integrated_treatment"]), confirmation=True)


def _pct(value: Any) -> str:
    parsed = base.as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.2f}%"


def report(config_path: Path, report_path: Path) -> None:
    config = load_config(config_path)
    output = output_dir(config)
    decisions: list[dict[str, Any]] = []
    for phase in ("diagnostic", "integrated", "confirmation"):
        path = output / f"{phase}_decision.json"
        if path.exists():
            decisions.append(json.loads(path.read_text(encoding="utf-8")))
    final = decisions[-1] if decisions else {}
    if final.get("phase") == "confirmation" and final.get("passes_gate"):
        bottom_line = "S1 passed development and historical confirmation. It qualifies only for a prospective live shadow test."
    elif any(row.get("phase") == "integrated" and row.get("passes_gate") for row in decisions):
        bottom_line = "S1 passed development but confirmation did not pass or is incomplete."
    elif any(row.get("phase") == "diagnostic" and row.get("passes_gate") for row in decisions):
        bottom_line = "The ranking diagnostic passed, but the integrated single-turn version did not pass or is incomplete."
    else:
        bottom_line = "The ranking diagnostic did not pass. Integrated and confirmation calls were not run."
    table_rows = []
    for row in decisions:
        if row.get("skipped"):
            continue
        table_rows.append(
            [
                row["phase"],
                row["valid_pairs"],
                f"{row['challenger_top5_top2_captures']}/{row['control_top5_top2_captures']}",
                row["challenger_shortlist_top2_captures"],
                f"{row['capture_episodes']} periods, {row['capture_models']} models",
                _pct(row["mean_alpha_improvement"]),
                row["positive_pairs"],
                "Pass" if row["passes_gate"] else "Fail",
            ]
        )
    records = (
        _phase_records(config, "diagnostic")
        + _phase_records(config, "integrated")
        + _phase_records(config, "confirmation")
    )
    usage = base.usage_summary(records)
    text = "\n".join(
        [
            "# VNext Historical Replay Stage 1C Results",
            "",
            f"Generated at: `{datetime.now(timezone.utc).replace(microsecond=0).isoformat()}`",
            "",
            "## Bottom Line",
            "",
            bottom_line,
            "",
            "## Results",
            "",
            base.markdown_table(
                ["Stage", "Valid", "Top-2 final-five challenger/control", "Shortlist top-2", "Capture breadth", "Alpha improvement", "Positive pairs", "Gate"],
                table_rows,
            ),
            "",
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
            "R1 is a ranking-only diagnostic and cannot become production evidence. S1 is the single-turn implementation. C1-C3 remain the historical holdout, and any historical pass still requires a prospective live shadow test.",
            "",
        ]
    )
    (output / "report.md").write_text(text, encoding="utf-8", newline="\n")
    report_path.write_text(text, encoding="utf-8", newline="\n")
    print(text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run CapitalBench Stage 1C ranking replay")
    parser.add_argument(
        "command",
        choices=(
            "prepare",
            "run-diagnostic",
            "score-diagnostic",
            "run-integrated",
            "score-integrated",
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
    elif args.command == "run-diagnostic":
        run_calls(config_path, "diagnostic")
    elif args.command == "score-diagnostic":
        score_diagnostic(config_path)
    elif args.command == "run-integrated":
        run_calls(config_path, "integrated")
    elif args.command == "score-integrated":
        score_integrated(config_path)
    elif args.command == "run-confirmation":
        run_calls(config_path, "confirmation")
    elif args.command == "score-confirmation":
        score_confirmation(config_path)
    elif args.command == "report":
        report(config_path, args.report.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

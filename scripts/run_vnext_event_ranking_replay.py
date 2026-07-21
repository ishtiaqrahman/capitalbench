from __future__ import annotations

import argparse
import copy
import importlib.util
import itertools
import json
import os
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "scripts" / "run_vnext_historical_replay.py"
STAGE1B_PATH = ROOT / "scripts" / "run_vnext_historical_replay_stage1b.py"
DEFAULT_CONFIG = ROOT / "experiments" / "vnext-event-ranking-replay-2026-07-21.yaml"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = _load_module("vnext_event_base", BASE_PATH)
stage1b = _load_module("vnext_event_stage1b", STAGE1B_PATH)
LANE_REQUIREMENTS = {
    "continuation": 3,
    "reversal": 3,
    "context": 2,
    "defensive": 1,
    "wildcard": 1,
}
EVIDENCE_STRENGTHS = ("strong", "moderate", "weak", "none")
TIMING_FITS = ("inside_window", "already_released", "no_direct_event", "uncertain")


def load_config(path: Path) -> dict[str, Any]:
    return base.load_yaml(path)


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def event_register(episode: dict[str, Any]) -> dict[str, Any]:
    path = ROOT / str(episode["event_register"])
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"invalid event register: {path}")
    return payload


def event_table(episode: dict[str, Any]) -> str:
    rows = []
    for event in event_register(episode).get("events", []):
        rows.append(
            [
                event["id"], event["timing"], event["status"], event["fact"],
                event["comparison"], ", ".join(event["affected_options"]),
                event["directness"], event["market_already_moved"],
            ]
        )
    return base.markdown_table(
        ["event_id", "timing", "status", "fact", "comparison", "mapped option IDs", "directness", "already moved"],
        rows,
    )


COMMON_TASK = """
You are participating in a private retrospective CapitalBench input experiment.
Treat this as an unknown decision point. Use only this packet. Do not use
remembered outcomes, tools, browsing, search, or external facts. The horizon is
one week.

Forecast SPY separately. Evaluate the complete active universe, build a
ten-option shortlist, and rank a final five that is a subset of that shortlist.
Use exact option_id values. Rank 1 has the highest expected one-week return.
expected_alpha_vs_spy_pct must equal the candidate forecast minus the SPY
forecast. Mechanical lanes are search aids, not recommendations. Return only
JSON matching the supplied schema.
""".strip()


BALANCED_SEARCH = """
The shortlist must contain exactly three continuation candidates, three
reversal candidates, two context/event candidates, one defensive candidate,
and one unrestricted wildcard. Assign each name to one lane. Do not place more
than four shortlist names in one option group.
""".strip()


EVENT_SEARCH = """
Use the compact event register as factual evidence, not as a direction signal.
For every shortlist candidate, cite zero or more exact event IDs, classify the
evidence strength, and state whether timing is inside the window, already
released, uncertain, or has no direct event. A candidate with no mapped event
may still qualify through another lane, but it must be marked no_direct_event.
Do not infer an event outcome that was unknown at the cutoff.
""".strip()


PAIRWISE_RANKING = """
After the shortlist is complete, compare every shortlist candidate with SPY.
Then choose five finalists and compare every pair among those five. Make the
final rank consistent with those comparisons. Set prefer_spy=true unless at
least one finalist has strong or moderate evidence, timing that is inside the
window or already released, and positive expected alpha versus SPY. Explain an
abstention briefly. This is one single-turn decision; return one JSON object.
""".strip()


def build_prompt(config: dict[str, Any], episode: dict[str, Any], treatment: str) -> str:
    if treatment == "H0":
        return base.build_prompt(config, episode, treatment)
    if treatment == "H4":
        return stage1b.build_prompt(config, episode, treatment)
    round_path = base.source_round(episode)
    briefing_path = round_path / "research" / "final_briefing.md"
    if not briefing_path.exists():
        briefing_path = round_path / "briefing.md"
    briefing = base.sanitize_full_briefing(briefing_path.read_text(encoding="utf-8"))
    market = base.derived_market_table(base.derived_market_rows(base.common_market_rows(round_path)))
    extra = PAIRWISE_RANKING if treatment == "H8" else ""
    return (
        f"{COMMON_TASK}\n\nReplay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {treatment}\n\n{BALANCED_SEARCH}\n\n"
        f"{EVENT_SEARCH}\n\n{extra}\n\n"
        f"Entry-time market summary:\n{stage1b.market_summary(episode)}\n\n"
        f"Mechanical lane references:\n{stage1b.lane_reference_table(episode)}\n\n"
        f"Compact event register:\n{event_table(episode)}\n\n"
        f"Frozen factual briefing:\n{briefing}\n\n"
        f"Complete option comparison table:\n{market}\n"
    )


def response_schema(treatment: str) -> dict[str, Any]:
    if treatment == "H0":
        return base.response_schema()
    schema = copy.deepcopy(stage1b.response_schema("H4"))
    if treatment == "H4":
        return schema
    schema["properties"]["treatment_id"] = {"type": "string", "enum": [treatment]}
    item = schema["properties"]["shortlist"]["items"]
    item["properties"].update(
        {
            "event_ids": {"type": "array", "items": {"type": "string"}},
            "evidence_strength": {"type": "string", "enum": list(EVIDENCE_STRENGTHS)},
            "timing_fit": {"type": "string", "enum": list(TIMING_FITS)},
        }
    )
    item["required"].extend(["event_ids", "evidence_strength", "timing_fit"])
    schema["properties"]["event_use_summary"] = {"type": "string"}
    schema["required"].append("event_use_summary")
    if treatment == "H8":
        schema["properties"]["candidate_vs_spy"] = {
            "type": "array", "minItems": 10, "maxItems": 10,
            "items": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    "option_id": {"type": "string"},
                    "verdict": {"type": "string", "enum": ["candidate", "SP500", "unclear"]},
                    "reason": {"type": "string"},
                },
                "required": ["option_id", "verdict", "reason"],
            },
        }
        schema["properties"]["pairwise_finalists"] = {
            "type": "array", "minItems": 10, "maxItems": 10,
            "items": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    "left_option_id": {"type": "string"},
                    "right_option_id": {"type": "string"},
                    "preferred_option_id": {"type": "string"},
                    "reason": {"type": "string"},
                },
                "required": ["left_option_id", "right_option_id", "preferred_option_id", "reason"],
            },
        }
        schema["properties"]["abstention_reason"] = {"type": "string"}
        schema["required"].extend(["candidate_vs_spy", "pairwise_finalists", "abstention_reason"])
    return schema


def canonicalize(payload: Any, episode: dict[str, Any], treatment: str) -> Any:
    if treatment in {"H0", "H4"}:
        return stage1b.canonicalize_payload(payload, episode, treatment)
    normalized = stage1b.canonicalize_payload(payload, episode, "H4")
    if not isinstance(normalized, dict):
        return normalized
    aliases = stage1b._alias_map(episode)

    def option_id(value: Any) -> str:
        text = str(value or "").strip()
        return aliases.get(text.upper(), text)

    for row in normalized.get("candidate_vs_spy") or []:
        if isinstance(row, dict):
            row["option_id"] = option_id(row.get("option_id"))
    for row in normalized.get("pairwise_finalists") or []:
        if isinstance(row, dict):
            row["left_option_id"] = option_id(row.get("left_option_id"))
            row["right_option_id"] = option_id(row.get("right_option_id"))
            preferred = str(row.get("preferred_option_id") or "")
            row["preferred_option_id"] = preferred if preferred == "unclear" else option_id(preferred)
    return normalized


def validate_payload(payload: Any, episode: dict[str, Any], treatment: str) -> list[str]:
    if treatment in {"H0", "H4"}:
        return stage1b.validate_payload(payload, episode, treatment)
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    translated = copy.deepcopy(payload)
    translated["treatment_id"] = "H4"
    errors = stage1b.validate_payload(translated, episode, "H4")
    valid_events = {str(row["id"]) for row in event_register(episode).get("events", [])}
    shortlist = payload.get("shortlist") if isinstance(payload.get("shortlist"), list) else []
    for row in shortlist:
        if not isinstance(row, dict):
            continue
        unknown = set(str(value) for value in row.get("event_ids") or []) - valid_events
        if unknown:
            errors.append(f"unknown event IDs: {sorted(unknown)}")
        if row.get("evidence_strength") not in EVIDENCE_STRENGTHS:
            errors.append("invalid evidence strength")
        if row.get("timing_fit") not in TIMING_FITS:
            errors.append("invalid timing fit")
    if not str(payload.get("event_use_summary") or "").strip():
        errors.append("missing event use summary")
    if treatment == "H8":
        shortlist_ids = {str(row.get("option_id")) for row in shortlist if isinstance(row, dict)}
        comparisons = payload.get("candidate_vs_spy")
        if not isinstance(comparisons, list) or len(comparisons) != 10:
            errors.append("candidate_vs_spy must contain 10 rows")
            comparisons = []
        compared_ids = [str(row.get("option_id")) for row in comparisons if isinstance(row, dict)]
        if set(compared_ids) != shortlist_ids or len(set(compared_ids)) != 10:
            errors.append("candidate_vs_spy must cover each shortlist option once")
        top5 = [str(row.get("option_id")) for row in payload.get("top5") or [] if isinstance(row, dict)]
        expected_pairs = {frozenset(pair) for pair in itertools.combinations(top5, 2)}
        actual_pairs: set[frozenset[str]] = set()
        pairwise = payload.get("pairwise_finalists")
        if not isinstance(pairwise, list) or len(pairwise) != 10:
            errors.append("pairwise_finalists must contain 10 rows")
            pairwise = []
        for row in pairwise:
            if not isinstance(row, dict):
                continue
            left = str(row.get("left_option_id"))
            right = str(row.get("right_option_id"))
            preferred = str(row.get("preferred_option_id"))
            actual_pairs.add(frozenset((left, right)))
            if preferred not in {left, right, "unclear"}:
                errors.append("invalid pairwise preferred option")
        if actual_pairs != expected_pairs:
            errors.append("pairwise_finalists must cover every final-five pair once")
        if not payload.get("prefer_spy"):
            evidence_by_id = {str(row.get("option_id")): row for row in shortlist if isinstance(row, dict)}
            verdicts = {str(row.get("option_id")): row.get("verdict") for row in comparisons if isinstance(row, dict)}
            supported = any(
                evidence_by_id.get(option, {}).get("evidence_strength") in {"strong", "moderate"}
                and evidence_by_id.get(option, {}).get("timing_fit") in {"inside_window", "already_released"}
                and verdicts.get(option) == "candidate"
                for option in top5
            )
            if not supported:
                errors.append("prefer_spy=false requires a timely supported finalist that beats SPY")
        elif not str(payload.get("abstention_reason") or "").strip():
            errors.append("prefer_spy=true requires an abstention reason")
    return sorted(set(errors))


def calls_for(config: dict[str, Any], phase: str) -> list[dict[str, str]]:
    key = "search_treatments" if phase == "search" else "final_treatments"
    return [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"]
        for model_id in config["models"]
        for treatment in config[key]
    ]


def prepare(config_path: Path) -> None:
    config = load_config(config_path)
    output = output_dir(config)
    packets_dir = output / "packets"
    packets_dir.mkdir(parents=True, exist_ok=True)
    packets: list[dict[str, Any]] = []
    source_inputs: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        round_path = base.source_round(episode)
        event_path = ROOT / str(episode["event_register"])
        briefing_path = round_path / "research" / "final_briefing.md"
        source_inputs.append(
            {
                "replay_id": episode["replay_id"],
                "event_register": event_path.relative_to(ROOT).as_posix(),
                "event_register_sha256": base.sha256_file(event_path),
                "briefing": briefing_path.relative_to(ROOT).as_posix(),
                "briefing_sha256": base.sha256_file(briefing_path),
            }
        )
        register = event_register(episode)
        if str(register.get("round_id")) != str(episode["round_id"]):
            raise ValueError(f"event register round mismatch: {event_path}")
        for event in register.get("events", []):
            if not event.get("id") or not event.get("affected_options"):
                raise ValueError(f"incomplete event row in {event_path}")
        for treatment in config["treatments"]:
            prompt = build_prompt(config, episode, treatment)
            path = packets_dir / f"{episode['replay_id']}__{treatment}.txt"
            path.write_text(prompt, encoding="utf-8", newline="\n")
            packets.append(
                {
                    "replay_id": episode["replay_id"],
                    "treatment": treatment,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": base.sha256_text(prompt),
                    "bytes": len(prompt.encode("utf-8")),
                    "schema_sha256": base.sha256_text(json.dumps(response_schema(treatment), sort_keys=True)),
                }
            )
    protocol = ROOT / str(config["protocol"])
    manifest = {
        "experiment_id": config["experiment_id"],
        "frozen_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "outcomes_loaded": False,
        "config_path": config_path.relative_to(ROOT).as_posix(),
        "config_sha256": base.sha256_file(config_path),
        "protocol_sha256": base.sha256_file(protocol),
        "runner_sha256": base.sha256_file(Path(__file__)),
        "packets": packets,
        "source_inputs": source_inputs,
        "planned_search_calls": len(calls_for(config, "search")),
        "planned_final_calls": len(calls_for(config, "final")),
    }
    base.write_json(output / "freeze_manifest.json", manifest)
    base.write_csv(output / "packet_manifest.csv", packets)
    print(f"prepared_packets={len(packets)}")
    print(f"search_calls={manifest['planned_search_calls']}")
    print(f"final_calls={manifest['planned_final_calls']}")


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
    for row in manifest["source_inputs"]:
        if base.sha256_file(ROOT / row["event_register"]) != row["event_register_sha256"]:
            raise RuntimeError(f"event register hash mismatch: {row['event_register']}")
        if base.sha256_file(ROOT / row["briefing"]) != row["briefing_sha256"]:
            raise RuntimeError(f"briefing hash mismatch: {row['briefing']}")
    return manifest


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


def run_calls(config_path: Path, phase: str) -> None:
    config = load_config(config_path)
    if phase == "final":
        decision_path = output_dir(config) / "search_decision.json"
        if not decision_path.exists():
            raise RuntimeError("score search before final calls")
        decision = json.loads(decision_path.read_text(encoding="utf-8"))
        if not decision.get("passes_gate"):
            print("final_skipped=search gate failed")
            return
    freeze = verify_freeze(config)
    episodes = base.episode_index(config)
    models = base.model_index(config)
    base.load_local_env()
    required = {base.PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")
    calls = calls_for(config, phase)
    record_dir = output_dir(config) / "records" / phase
    response_dir = output_dir(config) / "responses" / phase
    record_dir.mkdir(parents=True, exist_ok=True)
    response_dir.mkdir(parents=True, exist_ok=True)
    completed = 0
    for position, call in enumerate(calls, start=1):
        stem = base.response_stem(call)
        record_path = record_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if not existing.get("provider_error"):
                parsed = canonicalize(existing.get("parsed_json"), episodes[call["replay_id"]], call["treatment"])
                errors = validate_payload(parsed, episodes[call["replay_id"]], call["treatment"])
                existing.update({"parsed_json": parsed, "validation_errors": errors, "valid": not errors})
                base.write_json(record_path, existing)
                if existing["valid"] or errors != ["response is not a JSON object"]:
                    completed += 1
                    print(f"[{position}/{len(calls)}] skip_existing valid={existing['valid']} {stem}", flush=True)
                    continue
        packet_path = output_dir(config) / "packets" / f"{call['replay_id']}__{call['treatment']}.txt"
        prompt = packet_path.read_text(encoding="utf-8")
        frozen = next(
            row for row in freeze["packets"]
            if row["replay_id"] == call["replay_id"] and row["treatment"] == call["treatment"]
        )
        if base.sha256_text(prompt) != frozen["sha256"]:
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
        raw_path = response_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = canonicalize(result.parsed_json, episodes[call["replay_id"]], call["treatment"])
        errors = validate_payload(parsed, episodes[call["replay_id"]], call["treatment"])
        if error:
            errors.append(f"provider_error: {error}")
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


def load_records(config: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    path = output_dir(config) / "records" / phase
    return [json.loads(item.read_text(encoding="utf-8")) for item in sorted(path.glob("*.json"))] if path.exists() else []


def score_record(record: dict[str, Any], episode: dict[str, Any], outcome: dict[str, Any]) -> dict[str, Any]:
    payload = record.get("parsed_json") if record.get("valid") else None
    row: dict[str, Any] = {
        "replay_id": record["replay_id"], "model_id": record["model_id"],
        "treatment": record["treatment"], "valid": bool(record.get("valid")),
        "spy_return": outcome["spy_return"], "validation_errors": record.get("validation_errors", []),
    }
    if not isinstance(payload, dict):
        return row
    shortlist = stage1b._shortlist_ids(payload, record["treatment"])
    top5 = [str(item["option_id"]) for item in sorted(payload["top5"], key=lambda item: int(item["rank"]))]
    ordered = sorted(outcome["active_returns"].items(), key=lambda item: (-item[1], item[0]))
    top3 = [option_id for option_id, _ in ordered[:3]]
    shortlist_best = max(outcome["returns"][option_id] for option_id in shortlist)
    top5_return = mean(outcome["returns"][option_id] for option_id in top5)
    abstained = record["treatment"] == "H8" and bool(payload.get("prefer_spy"))
    effective_return = outcome["spy_return"] if abstained else top5_return
    row.update(
        {
            "shortlist_ids": shortlist, "top5_ids": top5, "top3_ids": top3,
            "shortlist_top3_capture_count": len(set(shortlist) & set(top3)),
            "final_top3_capture_count": len(set(top5) & set(top3)),
            "shortlist_oracle_regret": outcome["best_return"] - shortlist_best,
            "top5_return": top5_return, "top5_alpha": top5_return - outcome["spy_return"],
            "abstained": abstained, "effective_return": effective_return,
            "effective_alpha": effective_return - outcome["spy_return"],
        }
    )
    return row


def scored_records(config: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    episodes = base.episode_index(config)
    outcomes = {key: base.load_outcomes(value) for key, value in episodes.items()}
    return [score_record(row, episodes[row["replay_id"]], outcomes[row["replay_id"]]) for row in load_records(config, phase)]


def paired(scored: Sequence[dict[str, Any]], control: str, challenger: str) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in scored:
        grouped[(str(row["replay_id"]), str(row["model_id"]))][str(row["treatment"])] = row
    rows: list[dict[str, Any]] = []
    for (replay_id, model_id), treatments in sorted(grouped.items()):
        left, right = treatments.get(control), treatments.get(challenger)
        valid = bool(left and right and left.get("valid") and right.get("valid"))
        row: dict[str, Any] = {
            "replay_id": replay_id, "model_id": model_id, "control": control,
            "challenger": challenger, "pair_valid": valid,
        }
        if valid and left and right:
            row.update(
                {
                    "control_top5_alpha": left["top5_alpha"],
                    "challenger_top5_alpha": right["top5_alpha"],
                    "top5_alpha_improvement": right["top5_alpha"] - left["top5_alpha"],
                    "control_effective_return": left["effective_return"],
                    "challenger_effective_return": right["effective_return"],
                    "effective_return_improvement": right["effective_return"] - left["effective_return"],
                    "control_effective_alpha": left["effective_alpha"],
                    "challenger_effective_alpha": right["effective_alpha"],
                    "control_shortlist_top3": left["shortlist_top3_capture_count"],
                    "challenger_shortlist_top3": right["shortlist_top3_capture_count"],
                    "top3_capture_change": right["shortlist_top3_capture_count"] - left["shortlist_top3_capture_count"],
                    "control_regret": left["shortlist_oracle_regret"],
                    "challenger_regret": right["shortlist_oracle_regret"],
                    "regret_reduction": left["shortlist_oracle_regret"] - right["shortlist_oracle_regret"],
                    "challenger_abstained": right["abstained"],
                }
            )
        rows.append(row)
    return rows


def _breadth(valid: Sequence[dict[str, Any]], metric: str) -> tuple[int, int, int]:
    values = [float(row[metric]) for row in valid]
    by_model: dict[str, list[float]] = defaultdict(list)
    by_episode: dict[str, list[float]] = defaultdict(list)
    for row in valid:
        by_model[str(row["model_id"])].append(float(row[metric]))
        by_episode[str(row["replay_id"])].append(float(row[metric]))
    return (
        sum(value > 0 for value in values),
        sum(mean(group) > 0 for group in by_model.values()),
        sum(mean(group) > 0 for group in by_episode.values()),
    )


def score_search(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    scored = scored_records(config, "search")
    pairs = paired(scored, "H4", "H7")
    valid = [row for row in pairs if row["pair_valid"]]
    positive_pairs, positive_models, positive_episodes = _breadth(valid, "top5_alpha_improvement") if valid else (0, 0, 0)
    mean_improvement = mean(float(row["top5_alpha_improvement"]) for row in valid) if valid else None
    capture_change = sum(int(row["top3_capture_change"]) for row in valid)
    regret_reduction = mean(float(row["regret_reduction"]) for row in valid) if valid else None
    gate = config["search_gate"]
    passes = bool(
        len(valid) >= int(gate["minimum_valid_pairs"])
        and mean_improvement is not None
        and mean_improvement >= float(gate["minimum_mean_alpha_improvement"])
        and positive_pairs >= int(gate["minimum_positive_pairs"])
        and positive_models >= int(gate["minimum_positive_models"])
        and positive_episodes >= int(gate["minimum_positive_episodes"])
        and (not gate["require_nonnegative_top3_capture_change"] or capture_change >= 0)
        and (not gate["require_nonnegative_regret_reduction"] or (regret_reduction is not None and regret_reduction >= 0))
    )
    decision = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passes_gate": passes, "valid_pairs": len(valid),
        "mean_top5_alpha_improvement": mean_improvement,
        "positive_pairs": positive_pairs, "positive_models": positive_models,
        "positive_episodes": positive_episodes, "top3_capture_change": capture_change,
        "mean_regret_reduction": regret_reduction,
    }
    output = output_dir(config)
    base.write_csv(output / "search_call_metrics.csv", scored)
    base.write_csv(output / "search_pairs.csv", pairs)
    base.write_json(output / "search_decision.json", decision)
    if not passes:
        write_canonical_result(config, search=decision, final=None)
    print(json.dumps(decision, indent=2))
    return decision


def score_final(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    search_path = output_dir(config) / "search_decision.json"
    if not search_path.exists():
        raise RuntimeError("score search first")
    search = json.loads(search_path.read_text(encoding="utf-8"))
    if not search.get("passes_gate"):
        result = {"passes_gate": False, "skipped": "search gate failed"}
        write_canonical_result(config, search=search, final=result)
        print(json.dumps(result, indent=2))
        return result
    scored = scored_records(config, "final")
    pairs = paired(scored, "H0", "H8")
    valid = [row for row in pairs if row["pair_valid"]]
    positive_pairs, positive_models, positive_episodes = _breadth(valid, "effective_return_improvement") if valid else (0, 0, 0)
    mean_improvement = mean(float(row["effective_return_improvement"]) for row in valid) if valid else None
    treatment_alpha = mean(float(row["challenger_effective_alpha"]) for row in valid) if valid else None
    capture_change = sum(int(row["top3_capture_change"]) for row in valid)
    regret_reduction = mean(float(row["regret_reduction"]) for row in valid) if valid else None
    by_episode_control: dict[str, list[float]] = defaultdict(list)
    by_episode_challenger: dict[str, list[float]] = defaultdict(list)
    for row in valid:
        by_episode_control[row["replay_id"]].append(float(row["control_effective_alpha"]))
        by_episode_challenger[row["replay_id"]].append(float(row["challenger_effective_alpha"]))
    worst_control = min((mean(values) for values in by_episode_control.values()), default=None)
    worst_challenger = min((mean(values) for values in by_episode_challenger.values()), default=None)
    worst_deterioration = (
        worst_challenger - worst_control
        if worst_control is not None and worst_challenger is not None else None
    )
    gate = config["final_gate"]
    passes = bool(
        len(valid) >= int(gate["minimum_valid_pairs"])
        and mean_improvement is not None
        and mean_improvement >= float(gate["minimum_mean_effective_return_improvement"])
        and (not gate["require_positive_treatment_alpha"] or (treatment_alpha is not None and treatment_alpha > 0))
        and positive_pairs >= int(gate["minimum_positive_pairs"])
        and positive_models >= int(gate["minimum_positive_models"])
        and positive_episodes >= int(gate["minimum_positive_episodes"])
        and (not gate["require_improved_capture_or_regret"] or capture_change > 0 or (regret_reduction is not None and regret_reduction > 0))
        and worst_deterioration is not None
        and worst_deterioration >= -float(gate["maximum_worst_episode_deterioration"])
    )
    result = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passes_gate": passes, "valid_pairs": len(valid),
        "mean_effective_return_improvement": mean_improvement,
        "mean_treatment_alpha_vs_spy": treatment_alpha,
        "positive_pairs": positive_pairs, "positive_models": positive_models,
        "positive_episodes": positive_episodes, "top3_capture_change": capture_change,
        "mean_regret_reduction": regret_reduction,
        "worst_episode_alpha_change": worst_deterioration,
        "abstentions": sum(bool(row["challenger_abstained"]) for row in valid),
    }
    output = output_dir(config)
    base.write_csv(output / "final_call_metrics.csv", scored)
    base.write_csv(output / "final_pairs.csv", pairs)
    base.write_json(output / "final_decision.json", result)
    write_canonical_result(config, search=search, final=result)
    print(json.dumps(result, indent=2))
    return result


def _pct(value: Any) -> str:
    return "n/a" if value is None else f"{float(value) * 100:.2f}%"


def usage(config: dict[str, Any]) -> dict[str, Any]:
    records = load_records(config, "search") + load_records(config, "final")
    return {
        "calls": len(records),
        "valid_calls": sum(bool(row.get("valid")) for row in records),
        "input_tokens": sum(int((row.get("usage") or {}).get("input_tokens") or 0) for row in records),
        "output_tokens": sum(int((row.get("usage") or {}).get("output_tokens") or 0) for row in records),
        "reasoning_tokens": sum(int((row.get("usage") or {}).get("reasoning_tokens") or 0) for row in records),
    }


def event_evidence_diagnostic(config: dict[str, Any]) -> dict[str, Any]:
    episodes = base.episode_index(config)
    outcomes = {key: base.load_outcomes(value) for key, value in episodes.items()}
    candidates: list[dict[str, Any]] = []
    for record in load_records(config, "search"):
        if record.get("treatment") != "H7" or not record.get("valid"):
            continue
        payload = record.get("parsed_json") or {}
        outcome = outcomes[str(record["replay_id"])]
        top5_ids = {str(row["option_id"]) for row in payload.get("top5") or []}
        top3_ids = {
            option_id for option_id, _ in sorted(
                outcome["active_returns"].items(), key=lambda item: (-item[1], item[0])
            )[:3]
        }
        statuses = {
            str(row["id"]): str(row["status"])
            for row in event_register(episodes[str(record["replay_id"])]).get("events", [])
        }
        for row in payload.get("shortlist") or []:
            option_id = str(row["option_id"])
            event_ids = [str(value) for value in row.get("event_ids") or []]
            candidates.append(
                {
                    "replay_id": record["replay_id"], "model_id": record["model_id"],
                    "option_id": option_id, "evidence_strength": row.get("evidence_strength"),
                    "timing_fit": row.get("timing_fit"), "event_linked": bool(event_ids),
                    "event_status": "+".join(sorted({statuses.get(value, "unknown") for value in event_ids})) if event_ids else "none",
                    "selected_final": option_id in top5_ids, "realized_top3": option_id in top3_ids,
                    "realized_alpha": outcome["returns"][option_id] - outcome["spy_return"],
                    "timely_supported": (
                        row.get("evidence_strength") in {"strong", "moderate"}
                        and row.get("timing_fit") in {"inside_window", "already_released"}
                    ),
                }
            )

    def aggregate(field: str) -> list[dict[str, Any]]:
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in candidates:
            grouped[str(row[field])].append(row)
        return [
            {
                "group": key, "candidates": len(rows),
                "mean_realized_alpha": mean(float(row["realized_alpha"]) for row in rows),
                "positive_alpha_share": sum(float(row["realized_alpha"]) > 0 for row in rows) / len(rows),
                "realized_top3_share": sum(bool(row["realized_top3"]) for row in rows) / len(rows),
                "final_selection_share": sum(bool(row["selected_final"]) for row in rows) / len(rows),
            }
            for key, rows in sorted(grouped.items())
        ]

    timely = [row for row in candidates if row["timely_supported"]]
    others = [row for row in candidates if not row["timely_supported"]]
    return {
        "candidate_observations": len(candidates),
        "valid_h7_records": sum(1 for row in load_records(config, "search") if row.get("treatment") == "H7" and row.get("valid")),
        "event_linked_share": sum(bool(row["event_linked"]) for row in candidates) / len(candidates) if candidates else None,
        "timely_supported_candidates": len(timely),
        "timely_supported_mean_alpha": mean(float(row["realized_alpha"]) for row in timely) if timely else None,
        "other_candidate_mean_alpha": mean(float(row["realized_alpha"]) for row in others) if others else None,
        "by_evidence_strength": aggregate("evidence_strength"),
        "by_timing_fit": aggregate("timing_fit"),
        "by_event_status": aggregate("event_status"),
        "interpretation_limit": "Candidate observations repeat options across models and are descriptive, not independent.",
    }


def write_canonical_result(config: dict[str, Any], search: dict[str, Any], final: dict[str, Any] | None) -> None:
    if final and "skipped" not in final:
        decision = "accepted_for_prospective_shadow" if final.get("passes_gate") else "rejected"
    elif search.get("passes_gate"):
        decision = "active"
    else:
        decision = "rejected"
    evidence = event_evidence_diagnostic(config)
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": decision,
        "official_score_eligible": False,
        "search": search,
        "final": final,
        "usage": usage(config),
        "event_evidence_diagnostic": evidence,
        "limitations": [
            "Four historical periods are insufficient to prove prospective skill.",
            "Current models may remember historical outcomes.",
            "The equal-weight top-five basket is a selection diagnostic, not the production portfolio.",
        ],
    }
    summary_path = ROOT / str(config["canonical_summary"])
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    base.write_json(summary_path, summary)
    final_lines = ["- Final stage not run."]
    if final:
        final_lines = [
            f"- Status: {final.get('skipped', 'pass' if final.get('passes_gate') else 'fail')}",
            f"- Mean effective-return improvement over H0: {_pct(final.get('mean_effective_return_improvement'))}",
            f"- Mean H8 alpha versus SPY: {_pct(final.get('mean_treatment_alpha_vs_spy'))}",
            f"- Positive pairs/models/episodes: {final.get('positive_pairs', 0)}/{final.get('positive_models', 0)}/{final.get('positive_episodes', 0)}",
            f"- Abstentions: {final.get('abstentions', 0)}",
        ]
    evidence_rows = [
        [row["group"], row["candidates"], _pct(row["mean_realized_alpha"]), _pct(row["positive_alpha_share"]), _pct(row["realized_top3_share"])]
        for row in evidence["by_evidence_strength"]
    ]
    report = "\n".join(
        [
            "# VNext Event And Pairwise Ranking Replay Results", "",
            f"Decision: **{decision}**", "", "## Search Gate", "",
            f"- H7 mean top-five alpha improvement over H4: {_pct(search.get('mean_top5_alpha_improvement'))}",
            f"- Positive pairs/models/episodes: {search.get('positive_pairs', 0)}/{search.get('positive_models', 0)}/{search.get('positive_episodes', 0)}",
            f"- Top-three shortlist capture change: {search.get('top3_capture_change', 0)}",
            f"- Mean shortlist-regret reduction: {_pct(search.get('mean_regret_reduction'))}",
            f"- Search gate: {'pass' if search.get('passes_gate') else 'fail'}", "", "## Final Gate", "",
            *final_lines, "", "## Execution", "",
            f"- Provider calls: {summary['usage']['calls']}",
            f"- Valid calls: {summary['usage']['valid_calls']}",
            f"- Input tokens: {summary['usage']['input_tokens']:,}",
            f"- Output tokens: {summary['usage']['output_tokens']:,}",
            f"- Reasoning tokens: {summary['usage']['reasoning_tokens']:,}", "", "## Interpretation", "",
            f"H7 linked {_pct(evidence['event_linked_share'])} of shortlist observations to at least one event. Timely strong/moderate candidates realized {_pct(evidence['timely_supported_mean_alpha'])} mean alpha versus {_pct(evidence['other_candidate_mean_alpha'])} for other candidates.", "",
            base.markdown_table(["Evidence strength", "Candidates", "Mean realized alpha", "Positive alpha", "Realized top-three"], evidence_rows), "",
            "Candidate observations repeat options across models and are descriptive, not independent. This private replay can reject a weak design but cannot prove live skill. Production Portfolio V2.0 remains unchanged.", "",
        ]
    )
    report_path = ROOT / str(config["canonical_report"])
    report_path.write_text(report, encoding="utf-8", newline="\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "run-search", "score-search", "run-final", "score-final"])
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    if args.command == "prepare":
        prepare(config_path)
    elif args.command == "run-search":
        run_calls(config_path, "search")
    elif args.command == "score-search":
        score_search(config_path)
    elif args.command == "run-final":
        run_calls(config_path, "final")
    elif args.command == "score-final":
        score_final(config_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

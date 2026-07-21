#!/usr/bin/env python3
"""Run paired LLM tests of compact quality evidence and use instructions."""

from __future__ import annotations

import argparse
import copy
import json
import os
import statistics
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import run_vnext_event_ranking_replay as event  # noqa: E402
from scripts import run_vnext_historical_replay_stage1b as stage1b  # noqa: E402


base = stage1b.base
DEFAULT_CONFIG = ROOT / "experiments" / "llm-quality-input-replay-2026-07-21.yaml"
DEFAULT_CANONICAL_REPORT = ROOT / "docs" / "llm_quality_input_replay_report.md"
DEFAULT_CANONICAL_SUMMARY = ROOT / "research" / "results" / "llm-quality-input-replay-2026-07-21.json"


def load_config(path: Path) -> dict[str, Any]:
    return base.load_yaml(path)


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def canonical_report(config: dict[str, Any]) -> Path:
    return ROOT / str(config["canonical_report"]) if config.get("canonical_report") else DEFAULT_CANONICAL_REPORT


def canonical_summary(config: dict[str, Any]) -> Path:
    return ROOT / str(config["canonical_summary"]) if config.get("canonical_summary") else DEFAULT_CANONICAL_SUMMARY


def feature_rows(config: dict[str, Any], episode: dict[str, Any]) -> list[dict[str, Any]]:
    rows = base.read_csv(ROOT / str(config["feature_panel"]))
    allowed = base.allowed_active_ids(episode)
    result: list[dict[str, Any]] = []
    for row in rows:
        if row.get("round_id") != episode["round_id"] or row.get("option_id") not in allowed:
            continue
        components = {
            "prior_active_rank": float(row["rank_prior_active_return"]),
            "recent_active_reversal_rank": float(row["rank_recent_active_reversal"]),
            "low_volatility_rank": float(row["rank_low_volatility"]),
            "shallow_drawdown_rank": float(row["rank_shallow_drawdown"]),
        }
        score = sum(float(config["quality_signal"][key]) * value for key, value in components.items())
        result.append({"option_id": row["option_id"], **components, "quality_score": score})
    if len(result) < int(len(allowed) * 0.9):
        raise ValueError(f"insufficient cutoff-safe quality rows for {episode['replay_id']}: {len(result)}/{len(allowed)}")
    option_order = {
        str(row["id"]): index for index, row in enumerate(base.load_options(base.source_round(episode)))
    }
    return sorted(result, key=lambda row: option_order[str(row["option_id"])])


def quality_top10(config: dict[str, Any], episode: dict[str, Any]) -> list[str]:
    return [
        str(row["option_id"])
        for row in sorted(feature_rows(config, episode), key=lambda row: (-float(row["quality_score"]), str(row["option_id"])))[:10]
    ]


def quality_table(config: dict[str, Any], episode: dict[str, Any]) -> str:
    rows = feature_rows(config, episode)
    return base.markdown_table(
        [
            "option_id",
            "prior active rank",
            "recent pullback rank",
            "low volatility rank",
            "shallow drawdown rank",
            "quality evidence score",
        ],
        [
            [
                row["option_id"],
                f"{float(row['prior_active_rank']):.3f}",
                f"{float(row['recent_active_reversal_rank']):.3f}",
                f"{float(row['low_volatility_rank']):.3f}",
                f"{float(row['shallow_drawdown_rank']):.3f}",
                f"{float(row['quality_score']):.3f}",
            ]
            for row in rows
        ],
    )


Q1_INSTRUCTION = """
Additional entry-time information follows. It is a complete cross-sectional
evidence table, not a recommendation or reduced universe. A higher quality
evidence score combines a stronger prior relative trend, a deeper recent
relative pullback, lower volatility, and shallower drawdown. Use or reject this
evidence as you judge appropriate. Preserve every original H4 requirement.
""".strip()


Q2_INSTRUCTION = """
Before finalizing the H4 shortlist, explicitly challenge each lane
representative against the highest quality-evidence options. Your ten-name
shortlist must include at least three of the evidence table's ten highest
scores, and your final five must include at least two. These are consideration
requirements, not automatic recommendations: forecast every finalist against
SPY, and rank by your own expected one-week return. Preserve the original H4
lane counts and all other response requirements.
""".strip()


def build_prompt(config: dict[str, Any], episode: dict[str, Any], treatment: str) -> str:
    prompt = stage1b.build_prompt(config, episode, "H4")
    prompt = prompt.replace("Treatment identifier: H4", f"Treatment identifier: {treatment}", 1)
    instruction = Q1_INSTRUCTION if treatment == "Q1" else Q2_INSTRUCTION
    appendix = (
        f"\n\nAdditional treatment instruction:\n{instruction}\n\n"
        "Complete option-level quality evidence table. All values are entry-date percentile ranks; no outcome data is included:\n"
        f"{quality_table(config, episode)}\n"
    )
    marker = "\n\nFrozen factual briefing:"
    if marker not in prompt:
        raise ValueError("H4 prompt structure changed")
    return prompt.replace(marker, appendix + marker, 1)


def response_schema() -> dict[str, Any]:
    return stage1b.response_schema("H4")


def canonicalize(payload: Any, episode: dict[str, Any]) -> Any:
    return stage1b.canonicalize_payload(payload, episode, "H4")


def validate_payload(payload: Any, config: dict[str, Any], episode: dict[str, Any], treatment: str) -> list[str]:
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    errors: list[str] = []
    if payload.get("treatment_id") != treatment:
        errors.append("treatment_id mismatch")
    translated = copy.deepcopy(payload)
    translated["treatment_id"] = "H4"
    errors.extend(stage1b.validate_payload(translated, episode, "H4"))
    if treatment == "Q2":
        top = set(quality_top10(config, episode))
        shortlist = set(stage1b._shortlist_ids(payload, "H4"))
        final = {
            str(row.get("option_id"))
            for row in payload.get("top5", [])
            if isinstance(row, dict)
        }
        requirements = config["q2_requirements"]
        if len(shortlist & top) < int(requirements["minimum_quality_top10_in_shortlist"]):
            errors.append("Q2 shortlist contains too few quality top-ten options")
        if len(final & top) < int(requirements["minimum_quality_top10_in_final5"]):
            errors.append("Q2 final five contains too few quality top-ten options")
    return sorted(set(errors))


def calls(config: dict[str, Any]) -> list[dict[str, str]]:
    planned = [
        {"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment}
        for episode in config["episodes"]
        for model_id in config["models"]
        for treatment in config["treatments"]
    ]
    return planned


def repair_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "replay_id": str(row["replay_id"]),
            "model_id": str(row["model_id"]),
            "treatment": "H4",
        }
        for row in config.get("control_repairs", [])
    ]


def operations(config: dict[str, Any]) -> list[dict[str, str]]:
    planned = repair_calls(config) + calls(config)
    if len(planned) > int(config["max_calls"]):
        raise ValueError("planned calls exceed frozen budget")
    return planned


def control_path(config: dict[str, Any], call: dict[str, str]) -> Path:
    model = call["model_id"].replace("/", "_")
    return ROOT / str(config["control_records_dir"]) / f"{call['replay_id']}__{model}__H4.json"


def prepare(config_path: Path) -> None:
    config_path = config_path.resolve()
    config = load_config(config_path)
    directory = output_dir(config)
    packet_dir = directory / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    packets: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        rows = feature_rows(config, episode)
        source_snapshot = directory / "evidence" / f"{episode['replay_id']}.json"
        source_snapshot.parent.mkdir(parents=True, exist_ok=True)
        base.write_json(source_snapshot, {"replay_id": episode["replay_id"], "round_id": episode["round_id"], "rows": rows})
        sources.append(
            {
                "replay_id": episode["replay_id"],
                "path": source_snapshot.relative_to(ROOT).as_posix(),
                "sha256": base.sha256_file(source_snapshot),
                "rows": len(rows),
                "forbidden_outcome_fields_present": any(
                    key in row for row in rows for key in ("future_return", "winner", "realized_rank", "outcome")
                ),
            }
        )
        for treatment in config["treatments"]:
            prompt = build_prompt(config, episode, treatment)
            lowered = prompt.lower()
            if "future_return" in lowered or "realized winner" in lowered:
                raise ValueError(f"outcome marker in packet {episode['replay_id']} {treatment}")
            path = packet_dir / f"{episode['replay_id']}__{treatment}.txt"
            path.write_text(prompt, encoding="utf-8", newline="\n")
            packets.append(
                {
                    "replay_id": episode["replay_id"],
                    "treatment": treatment,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": base.sha256_file(path),
                    "bytes": len(prompt.encode("utf-8")),
                    "schema_sha256": base.sha256_text(json.dumps(response_schema(), sort_keys=True)),
                }
            )
        if any(row["replay_id"] == episode["replay_id"] for row in repair_calls(config)):
            prompt = stage1b.build_prompt(config, episode, "H4")
            path = packet_dir / f"{episode['replay_id']}__H4.txt"
            path.write_text(prompt, encoding="utf-8", newline="\n")
            packets.append(
                {
                    "replay_id": episode["replay_id"],
                    "treatment": "H4",
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": base.sha256_file(path),
                    "bytes": len(prompt.encode("utf-8")),
                    "schema_sha256": base.sha256_text(json.dumps(response_schema(), sort_keys=True)),
                }
            )
    controls: list[dict[str, Any]] = []
    for call in calls(config):
        if call["treatment"] != config["treatments"][0]:
            continue
        path = control_path(config, call)
        if not path.exists():
            raise FileNotFoundError(path)
        record = json.loads(path.read_text(encoding="utf-8"))
        controls.append(
            {
                "replay_id": call["replay_id"],
                "model_id": call["model_id"],
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": base.sha256_file(path),
                "valid": bool(record.get("valid")),
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
        "planned_calls": len(operations(config)),
        "planned_treatment_calls": len(calls(config)),
        "planned_control_repairs": len(repair_calls(config)),
        "packets": packets,
        "evidence_sources": sources,
        "controls": controls,
    }
    base.write_json(directory / "freeze_manifest.json", manifest)
    base.write_csv(directory / "packet_manifest.csv", packets)
    if any(row["forbidden_outcome_fields_present"] for row in sources):
        raise ValueError("outcome field present in evidence snapshot")
    print(f"prepared_packets={len(packets)}")
    print(f"planned_calls={manifest['planned_calls']}")
    print(f"valid_saved_controls={sum(row['valid'] for row in controls)}/{len(controls)}")


def verify_freeze(config: dict[str, Any]) -> dict[str, Any]:
    path = output_dir(config) / "freeze_manifest.json"
    if not path.exists():
        raise RuntimeError("freeze manifest missing")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("outcomes_loaded") is not False:
        raise RuntimeError("freeze does not certify outcomes_loaded=false")
    for collection in ("packets", "evidence_sources", "controls"):
        for row in manifest[collection]:
            if base.sha256_file(ROOT / row["path"]) != row["sha256"]:
                raise RuntimeError(f"frozen file changed: {row['path']}")
    return manifest


def _call_provider(model: Any, prompt: str, retries: int) -> tuple[Any, int]:
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
            result = provider_class().run_model(model, prompt, response_schema(), runtime)
            if result.error and attempts <= retries and base._transport_error(str(result.error)):
                time.sleep(2.0 * attempts)
                continue
            return result, attempts
        except Exception as exc:
            if attempts > retries or not base._transport_error(str(exc)):
                raise
            time.sleep(2.0 * attempts)


def run(config_path: Path) -> None:
    config = load_config(config_path)
    freeze = verify_freeze(config)
    episodes = base.episode_index(config)
    models = base.model_index(config)
    base.load_local_env()
    required = {base.PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")
    record_dir = output_dir(config) / "records"
    repair_dir = output_dir(config) / "control_repairs"
    response_dir = output_dir(config) / "responses"
    record_dir.mkdir(parents=True, exist_ok=True)
    repair_dir.mkdir(parents=True, exist_ok=True)
    response_dir.mkdir(parents=True, exist_ok=True)
    planned = operations(config)
    repair_keys = {(row["replay_id"], row["model_id"], row["treatment"]) for row in repair_calls(config)}
    for position, call in enumerate(planned, start=1):
        stem = base.response_stem(call)
        is_repair = (call["replay_id"], call["model_id"], call["treatment"]) in repair_keys
        record_path = (repair_dir if is_repair else record_dir) / f"{stem}.json"
        previous_attempts = 0
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if existing.get("valid") or (existing.get("validation_errors") and not existing.get("provider_error")):
                print(f"[{position}/{len(planned)}] skip {stem} valid={existing.get('valid')}", flush=True)
                continue
            previous_attempts = int(existing.get("attempts") or 0)
            maximum_attempts = int(config["transport_retries"]) + 1
            if previous_attempts >= maximum_attempts:
                print(f"[{position}/{len(planned)}] retry_exhausted {stem}", flush=True)
                continue
        packet_path = output_dir(config) / "packets" / f"{call['replay_id']}__{call['treatment']}.txt"
        prompt = packet_path.read_text(encoding="utf-8")
        frozen = next(
            row for row in freeze["packets"]
            if row["replay_id"] == call["replay_id"] and row["treatment"] == call["treatment"]
        )
        if base.sha256_text(prompt) != frozen["sha256"]:
            raise RuntimeError(f"packet changed after freeze: {packet_path}")
        print(f"[{position}/{len(planned)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            remaining_attempts = int(config["transport_retries"]) + 1 - previous_attempts
            result, new_attempts = _call_provider(
                models[call["model_id"]], prompt, max(0, remaining_attempts - 1)
            )
            attempts = previous_attempts + new_attempts
            provider_error = result.error
        except Exception as exc:
            result = base.ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = previous_attempts + 1
            provider_error = str(exc)
        raw_path = response_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = canonicalize(result.parsed_json, episodes[call["replay_id"]])
        if is_repair:
            errors = stage1b.validate_payload(parsed, episodes[call["replay_id"]], "H4")
        else:
            errors = validate_payload(parsed, config, episodes[call["replay_id"]], call["treatment"])
        if provider_error:
            errors.append(f"provider_error: {provider_error}")
        record = {
            **call,
            "provider": models[call["model_id"]].provider,
            "api_model_name": models[call["model_id"]].api_model_name,
            "started_at_utc": started,
            "completed_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "attempts": attempts,
            "packet_sha256": frozen["sha256"],
            "raw_response_path": raw_path.relative_to(ROOT).as_posix(),
            "raw_response_sha256": base.sha256_text(result.raw_text),
            "parsed_json": parsed,
            "usage": result.usage.model_dump(mode="json", exclude_none=True),
            "provider_error": provider_error,
            "validation_errors": sorted(set(errors)),
            "valid": not errors,
        }
        base.write_json(record_path, record)
        print(f"[{position}/{len(planned)}] saved {stem} valid={record['valid']}", flush=True)
    print(f"treatment_records={len(list(record_dir.glob('*.json')))}")
    print(f"control_repairs={len(list(repair_dir.glob('*.json')))}")


def load_treatment_records(config: dict[str, Any]) -> list[dict[str, Any]]:
    directory = output_dir(config) / "records"
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.json"))]


def load_control_records(config: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for call in calls(config):
        key = (call["replay_id"], call["model_id"])
        if key in seen:
            continue
        seen.add(key)
        repair_path = output_dir(config) / "control_repairs" / f"{base.response_stem({**call, 'treatment': 'H4'})}.json"
        selected = repair_path if repair_path.exists() else control_path(config, call)
        records.append(json.loads(selected.read_text(encoding="utf-8")))
    return records


def scored_record(record: dict[str, Any], episode: dict[str, Any], outcome: dict[str, Any]) -> dict[str, Any]:
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
    shortlist = stage1b._shortlist_ids(payload, "H4")
    top5 = [str(item["option_id"]) for item in sorted(payload["top5"], key=lambda item: int(item["rank"]))]
    ordered = sorted(outcome["active_returns"].items(), key=lambda item: (-item[1], item[0]))
    top3 = {option_id for option_id, _value in ordered[:3]}
    top5_return = statistics.mean(outcome["returns"][option_id] for option_id in top5)
    row.update(
        {
            "shortlist_ids": shortlist,
            "top5_ids": top5,
            "top5_return": top5_return,
            "top5_alpha": top5_return - outcome["spy_return"],
            "shortlist_regret": outcome["best_return"] - max(outcome["returns"][option_id] for option_id in shortlist),
            "shortlist_top3_capture": len(set(shortlist) & top3),
        }
    )
    return row


def pairs_for(
    controls: Sequence[dict[str, Any]],
    treatments: Sequence[dict[str, Any]],
    treatment: str,
) -> list[dict[str, Any]]:
    control_index = {(row["replay_id"], row["model_id"]): row for row in controls}
    challenger_index = {
        (row["replay_id"], row["model_id"]): row for row in treatments if row["treatment"] == treatment
    }
    pairs: list[dict[str, Any]] = []
    for key in sorted(set(control_index) | set(challenger_index)):
        control = control_index.get(key)
        challenger = challenger_index.get(key)
        valid = bool(control and challenger and control.get("valid") and challenger.get("valid"))
        row: dict[str, Any] = {
            "replay_id": key[0],
            "model_id": key[1],
            "treatment": treatment,
            "pair_valid": valid,
        }
        if valid and control and challenger:
            row.update(
                {
                    "control_alpha": control["top5_alpha"],
                    "treatment_alpha": challenger["top5_alpha"],
                    "return_improvement": challenger["top5_return"] - control["top5_return"],
                    "regret_reduction": control["shortlist_regret"] - challenger["shortlist_regret"],
                    "top3_capture_change": challenger["shortlist_top3_capture"] - control["shortlist_top3_capture"],
                }
            )
        pairs.append(row)
    return pairs


def breadth(rows: Sequence[dict[str, Any]]) -> tuple[int, int, int]:
    by_model: dict[str, list[float]] = defaultdict(list)
    by_episode: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        by_model[row["model_id"]].append(float(row["return_improvement"]))
        by_episode[row["replay_id"]].append(float(row["return_improvement"]))
    return (
        sum(float(row["return_improvement"]) > 0 for row in rows),
        sum(statistics.mean(values) > 0 for values in by_model.values()),
        sum(statistics.mean(values) > 0 for values in by_episode.values()),
    )


def decision_for(config: dict[str, Any], treatment: str, pairs: Sequence[dict[str, Any]]) -> dict[str, Any]:
    valid = [row for row in pairs if row["pair_valid"]]
    positive_pairs, positive_models, positive_episodes = breadth(valid) if valid else (0, 0, 0)
    mean_improvement = statistics.mean(float(row["return_improvement"]) for row in valid) if valid else None
    treatment_alpha = statistics.mean(float(row["treatment_alpha"]) for row in valid) if valid else None
    regret_reduction = statistics.mean(float(row["regret_reduction"]) for row in valid) if valid else None
    control_by_episode: dict[str, list[float]] = defaultdict(list)
    challenger_by_episode: dict[str, list[float]] = defaultdict(list)
    for row in valid:
        control_by_episode[row["replay_id"]].append(float(row["control_alpha"]))
        challenger_by_episode[row["replay_id"]].append(float(row["treatment_alpha"]))
    worst_control = min((statistics.mean(values) for values in control_by_episode.values()), default=None)
    worst_challenger = min((statistics.mean(values) for values in challenger_by_episode.values()), default=None)
    worst_change = worst_challenger - worst_control if worst_control is not None and worst_challenger is not None else None
    gate = config["gate"]
    passes = bool(
        len(valid) >= int(gate["minimum_valid_pairs"])
        and mean_improvement is not None
        and mean_improvement >= float(gate["minimum_mean_return_improvement"])
        and (not gate["require_positive_treatment_alpha"] or (treatment_alpha is not None and treatment_alpha > 0))
        and positive_pairs >= int(gate["minimum_positive_pairs"])
        and positive_models >= int(gate["minimum_positive_models"])
        and positive_episodes >= int(gate["minimum_positive_episodes"])
        and (not gate["require_nonnegative_regret_reduction"] or (regret_reduction is not None and regret_reduction >= 0))
        and worst_change is not None
        and worst_change >= -float(gate["maximum_worst_episode_deterioration"])
    )
    return {
        "treatment": treatment,
        "passes_gate": passes,
        "valid_pairs": len(valid),
        "mean_return_improvement": mean_improvement,
        "mean_treatment_alpha_vs_spy": treatment_alpha,
        "positive_pairs": positive_pairs,
        "positive_models": positive_models,
        "positive_episodes": positive_episodes,
        "mean_regret_reduction": regret_reduction,
        "top3_capture_change": sum(int(row["top3_capture_change"]) for row in valid),
        "worst_episode_alpha_change": worst_change,
    }


def usage(records: Sequence[dict[str, Any]]) -> dict[str, Any]:
    return {
        "calls": len(records),
        "valid_calls": sum(bool(row.get("valid")) for row in records),
        "input_tokens": sum(int((row.get("usage") or {}).get("input_tokens") or 0) for row in records),
        "output_tokens": sum(int((row.get("usage") or {}).get("output_tokens") or 0) for row in records),
        "reasoning_tokens": sum(int((row.get("usage") or {}).get("reasoning_tokens") or 0) for row in records),
    }


def pct(value: Any) -> str:
    return "n/a" if value is None else f"{float(value) * 100:.2f}%"


def write_result(config: dict[str, Any], decisions: Sequence[dict[str, Any]], pairs: Sequence[dict[str, Any]], records: Sequence[dict[str, Any]]) -> dict[str, Any]:
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": "accepted_for_prospective_shadow" if any(row["passes_gate"] for row in decisions) else "rejected",
        "decisions": list(decisions),
        "usage": usage(records),
        "official_score_eligible": False,
        "production_impact": "none",
    }
    lines = [
        "# LLM Quality-Input Replay Results",
        "",
        f"Decision: **{summary['decision']}**",
        "",
        "| Treatment | Valid pairs | Return improvement | Treatment alpha | Positive pairs/models/periods | Regret reduction | Capture change | Worst-period change | Gate |",
        "| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in decisions:
        lines.append(
            f"| {row['treatment']} | {row['valid_pairs']} | {pct(row['mean_return_improvement'])} | {pct(row['mean_treatment_alpha_vs_spy'])} | {row['positive_pairs']}/{row['positive_models']}/{row['positive_episodes']} | {pct(row['mean_regret_reduction'])} | {row['top3_capture_change']} | {pct(row['worst_episode_alpha_change'])} | {'pass' if row['passes_gate'] else 'fail'} |"
        )
    lines.extend(
        [
            "",
            "## Execution",
            "",
            f"- New provider calls: {summary['usage']['calls']}",
            f"- Valid calls: {summary['usage']['valid_calls']}",
            f"- Input tokens: {summary['usage']['input_tokens']:,}",
            f"- Output tokens: {summary['usage']['output_tokens']:,}",
            f"- Reasoning tokens: {summary['usage']['reasoning_tokens']:,}",
            "",
            "## Interpretation",
            "",
            "The treatments change information and instructions inside the LLM call. No post-response portfolio overlay or reranking is applied. Historical reuse can reject weak treatments but cannot confirm prospective skill.",
            "",
        ]
    )
    report = "\n".join(lines)
    directory = output_dir(config)
    base.write_csv(directory / "pairs.csv", list(pairs))
    base.write_json(directory / "decision.json", summary)
    (directory / "report.md").write_text(report, encoding="utf-8")
    report_path = canonical_report(config)
    summary_path = canonical_summary(config)
    report_path.write_text(report, encoding="utf-8")
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    base.write_json(summary_path, summary)
    return summary


def score(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path)
    verify_freeze(config)
    episodes = base.episode_index(config)
    outcomes = {key: base.load_outcomes(value) for key, value in episodes.items()}
    raw_controls = load_control_records(config)
    raw_treatments = load_treatment_records(config)
    raw_repairs = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((output_dir(config) / "control_repairs").glob("*.json"))
    ] if (output_dir(config) / "control_repairs").exists() else []
    controls = [scored_record(row, episodes[row["replay_id"]], outcomes[row["replay_id"]]) for row in raw_controls]
    treatments = [scored_record(row, episodes[row["replay_id"]], outcomes[row["replay_id"]]) for row in raw_treatments]
    all_pairs: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    for treatment in config["treatments"]:
        treatment_pairs = pairs_for(controls, treatments, treatment)
        all_pairs.extend(treatment_pairs)
        decisions.append(decision_for(config, treatment, treatment_pairs))
    summary = write_result(config, decisions, all_pairs, raw_repairs + raw_treatments)
    print(json.dumps(summary, indent=2))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("prepare", "run", "score"))
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.config)
    elif args.command == "run":
        run(args.config)
    else:
        score(args.config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

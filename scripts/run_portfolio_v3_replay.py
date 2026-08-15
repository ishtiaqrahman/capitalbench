#!/usr/bin/env python3
"""Prepare, run, and score the frozen Portfolio V3A replay."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import statistics
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import run_vnext_historical_replay as base  # noqa: E402


DEFAULT_CONFIG = ROOT / "experiments" / "portfolio-v3-anti-extrapolation-replay-2026-08-13.yaml"
FORBIDDEN_PACKET_MARKERS = (
    "realized_return",
    "future_return",
    "outcome_rank",
    "winner_option_id",
    "results/returns.csv",
    "results/leaderboard.csv",
)
LANES = (
    "shock_reversal",
    "medium_strength",
    "short_continuation",
    "quality_pullback",
    "volume_dislocation",
    "benchmark",
    "wildcard",
)
MECHANISMS = ("continuation", "reversal", "catalyst", "defensive", "no_edge")
RECENT_INTERPRETATIONS = (
    "overreaction",
    "fundamental_deterioration",
    "supported_continuation",
    "no_edge",
)


def load_config(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"invalid config: {path}")
    return value


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def canonical_report(config: dict[str, Any]) -> Path:
    return ROOT / str(config["canonical_report"])


def canonical_summary(config: dict[str, Any]) -> Path:
    return ROOT / str(config["canonical_summary"])


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def episode_index(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row["replay_id"]): row for row in config["episodes"]}


def round_path(episode: dict[str, Any]) -> Path:
    return ROOT / "rounds" / str(episode["round_id"])


def option_rows(episode: dict[str, Any]) -> list[dict[str, Any]]:
    payload = base.load_yaml(round_path(episode) / "options.yaml")
    return [row for row in payload.get("options", []) if isinstance(row, dict) and row.get("id")]


def option_index(episode: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row["id"]): row for row in option_rows(episode)}


def decision_context(episode: dict[str, Any]) -> list[dict[str, str]]:
    path = round_path(episode) / "market_data" / "universe_decision_context.csv"
    rows = read_csv(path)
    if not rows:
        raise ValueError(f"empty decision context: {path}")
    return rows


def quality_scores(episode: dict[str, Any]) -> dict[str, float]:
    path = round_path(episode) / "market_data" / "universe_quality_evidence.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if float(payload.get("coverage") or 0) < 0.9:
        raise ValueError(f"insufficient quality evidence coverage: {path}")
    return {
        str(row["option_id"]): float(row["quality_evidence_score"])
        for row in payload.get("rows", [])
    }


def _number(row: dict[str, Any], key: str) -> float | None:
    value = row.get(key)
    if value in {None, ""}:
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _ranked_ids(
    rows: Sequence[dict[str, Any]], key: str, count: int, *, reverse: bool, absolute: bool = False
) -> list[str]:
    present = [row for row in rows if _number(row, key) is not None]
    ordered = sorted(
        present,
        key=lambda row: (
            abs(float(row[key])) if absolute else float(row[key]),
            str(row["option_id"]),
        ),
        reverse=reverse,
    )
    return [str(row["option_id"]) for row in ordered[:count]]


def candidate_slate(config: dict[str, Any], episode: dict[str, Any]) -> list[dict[str, Any]]:
    spec = config["candidate_slate"]
    rows = [
        row
        for row in decision_context(episode)
        if str(row.get("option_id")) not in {"CASH", "SP500"}
    ]
    quality = quality_scores(episode)
    lane_ids = {
        "shock_reversal": _ranked_ids(
            rows, "active_return_5s", int(spec["shock_reversal"]), reverse=False
        ),
        "medium_strength": _ranked_ids(
            rows, "prior_16s_active_return", int(spec["medium_strength"]), reverse=True
        ),
        "short_continuation": _ranked_ids(
            rows, "active_return_5s", int(spec["short_continuation"]), reverse=True
        ),
        "quality_pullback": [
            option_id
            for option_id in sorted(quality, key=lambda value: (-quality[value], value))
            if option_id not in {"CASH", "SP500"}
        ][: int(spec["quality_pullback"])],
        "volume_dislocation": _ranked_ids(
            rows,
            "volume_zscore_5v60",
            int(spec["volume_dislocation"]),
            reverse=True,
            absolute=True,
        ),
    }
    memberships: dict[str, list[str]] = defaultdict(list)
    ordered_ids: list[str] = []
    for lane in (
        "shock_reversal",
        "medium_strength",
        "short_continuation",
        "quality_pullback",
        "volume_dislocation",
    ):
        for option_id in lane_ids[lane]:
            memberships[option_id].append(lane)
            if option_id not in ordered_ids:
                ordered_ids.append(option_id)
    ordered_ids.append("SP500")
    memberships["SP500"] = ["benchmark"]

    context = {str(row["option_id"]): row for row in decision_context(episode)}
    options = option_index(episode)
    slate: list[dict[str, Any]] = []
    for option_id in ordered_ids:
        row = context[option_id]
        option = options[option_id]
        slate.append(
            {
                "option_id": option_id,
                "symbol": option.get("symbol") or "",
                "name": option.get("name") or option_id,
                "cluster": row.get("economic_exposure_cluster") or "",
                "risk_bucket": option.get("risk_bucket") or "",
                "lanes": memberships[option_id],
                "return_3s_pct": _pct_number(row, "return_3s"),
                "active_return_5s_pct": _pct_number(row, "active_return_5s"),
                "prior_16s_active_return_pct": _pct_number(row, "prior_16s_active_return"),
                "volatility_21s_pct": _pct_number(row, "volatility_21s"),
                "max_drawdown_21s_pct": _pct_number(row, "max_drawdown_21s"),
                "volume_zscore_5v60": _number(row, "volume_zscore_5v60"),
                "corr_spy_63s": _number(row, "corr_spy_63s"),
                "beta_spy_63s": _number(row, "beta_spy_63s"),
                "distance_52w_high_pct": _pct_number(row, "distance_52w_high"),
                "quality_evidence_score": quality.get(option_id),
            }
        )
    if not 10 <= len(slate) <= 16:
        raise ValueError(f"unexpected deterministic slate size {len(slate)} for {episode['replay_id']}")
    return slate


def _pct_number(row: dict[str, Any], key: str) -> float | None:
    value = _number(row, key)
    return None if value is None else value * 100.0


def _display(value: Any, digits: int = 2) -> str:
    if value is None or value == "":
        return "n/a"
    return f"{float(value):.{digits}f}"


def slate_table(slate: Sequence[dict[str, Any]]) -> str:
    headers = [
        "option_id",
        "symbol",
        "name",
        "lanes",
        "3s return %",
        "5s active %",
        "prior 16s active %",
        "21s vol %",
        "21s max drawdown %",
        "volume z",
        "SPY corr",
        "SPY beta",
        "52w-high distance %",
        "quality score",
    ]
    body = [
        [
            row["option_id"],
            row["symbol"],
            row["name"],
            ",".join(row["lanes"]),
            _display(row["return_3s_pct"]),
            _display(row["active_return_5s_pct"]),
            _display(row["prior_16s_active_return_pct"]),
            _display(row["volatility_21s_pct"]),
            _display(row["max_drawdown_21s_pct"]),
            _display(row["volume_zscore_5v60"]),
            _display(row["corr_spy_63s"]),
            _display(row["beta_spy_63s"]),
            _display(row["distance_52w_high_pct"]),
            _display(row["quality_evidence_score"], 3),
        ]
        for row in slate
    ]
    return base.markdown_table(headers, body)


def universe_table(episode: dict[str, Any]) -> str:
    rows = []
    for option in option_rows(episode):
        if not option.get("include_in_universe", True) or option["id"] == "CASH":
            continue
        rows.append(
            [
                option["id"],
                option.get("symbol") or "",
                option.get("name") or "",
                option.get("option_group") or "",
                option.get("risk_bucket") or "",
                str(option.get("exposure_description") or "").replace("|", "/"),
            ]
        )
    return base.markdown_table(
        ["option_id", "symbol", "name", "group", "risk", "exposure"], rows
    )


def market_summary(episode: dict[str, Any]) -> str:
    rows = decision_context(episode)
    active = [row for row in rows if row.get("option_id") not in {"CASH", "SP500"}]
    five = [float(row["active_return_5s"]) for row in active if row.get("active_return_5s")]
    prior = [float(row["prior_16s_active_return"]) for row in active if row.get("prior_16s_active_return")]
    return base.markdown_table(
        ["entry-time statistic", "value"],
        [
            ["active choices", len(active)],
            ["five-session active-return dispersion", f"{statistics.pstdev(five) * 100:.2f}%"],
            ["prior 16-session active-return dispersion", f"{statistics.pstdev(prior) * 100:.2f}%"],
            ["neutral top-three base rate", f"{3 / len(active) * 100:.2f}%"],
        ],
    )


TASK = """
You are participating in a private, offline CapitalBench replay. Treat this as
an unknown decision point. Use only this packet. Do not use remembered
outcomes, tools, browsing, retrieval, search, or facts after the research
cutoff. This is one single-turn, non-agentic decision.

Your objective is to rank assets for realized return over exactly one week and
construct a portfolio that beats SPY. The deterministic candidate slate exists
to prevent omission; it is not a recommendation. Assess every slate candidate.
You may add at most two wildcard options from the complete universe, but only
when the frozen briefing supplies a specific reason the mechanical slate
missed.

Do not extrapolate recent returns mechanically. A recent winner has no positive
edge without independent in-window support. Give extreme recent losers a fair
reversal test, but distinguish temporary price overreaction from fundamental
deterioration. Use the supplied cross-sectional dispersion, medium-horizon
relative strength, volatility, drawdown, volume, and briefing evidence. The
neutral chance that one active choice finishes in the top three is only about
4.3%, so keep top-three probabilities selective and internally comparable.

For every assessed candidate, provide probabilities and an 80% excess-return
range relative to SPY. Rank all assessments without ties. top3_option_ids must
be the options ranked 1, 2, and 3. If no active candidate has a credible edge,
set prefer_spy to true. Otherwise, the scorer will allocate 35%, 35%, and 30%
to ranks 1, 2, and 3. Do not create alternative portfolios.

Return only JSON matching the supplied schema.
""".strip()


def build_prompt(config: dict[str, Any], episode: dict[str, Any]) -> str:
    path = round_path(episode)
    briefing = (path / "briefing.md").read_text(encoding="utf-8")
    slate = candidate_slate(config, episode)
    allocation = ", ".join(str(value) for value in config["portfolio"]["rank_allocations_pct"])
    return (
        f"{TASK}\n\n"
        f"Replay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {config['treatment_id']}\n"
        f"Research cutoff and entry date: {episode['entry_date']} close\n"
        f"Exit date: {episode['exit_date']} close\n"
        f"Fixed rank allocations: {allocation}\n\n"
        f"Entry-time market summary:\n{market_summary(episode)}\n\n"
        "Deterministic candidate slate. For slate candidates, origin_lanes must exactly match this table. "
        "For an added candidate use origin_lanes=[\"wildcard\"]:\n"
        f"{slate_table(slate)}\n\n"
        f"Frozen factual briefing:\n{briefing}\n\n"
        f"Complete allowed active universe for optional wildcards:\n{universe_table(episode)}\n"
    )


def response_schema() -> dict[str, Any]:
    assessment = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "option_id": {"type": "string"},
            "origin_lanes": {
                "type": "array",
                "minItems": 1,
                "maxItems": 5,
                "items": {"type": "string", "enum": list(LANES)},
            },
            "mechanism": {"type": "string", "enum": list(MECHANISMS)},
            "p_beat_spy_pct": {"type": "integer", "minimum": 0, "maximum": 100},
            "p_top3_pct": {"type": "integer", "minimum": 0, "maximum": 100},
            "excess_return_p10_pct": {"type": "number"},
            "excess_return_p50_pct": {"type": "number"},
            "excess_return_p90_pct": {"type": "number"},
            "recent_return_interpretation": {
                "type": "string",
                "enum": list(RECENT_INTERPRETATIONS),
            },
            "evidence": {
                "type": "array",
                "minItems": 1,
                "maxItems": 3,
                "items": {"type": "string"},
            },
            "rank": {"type": "integer", "minimum": 1, "maximum": 18},
        },
        "required": [
            "option_id",
            "origin_lanes",
            "mechanism",
            "p_beat_spy_pct",
            "p_top3_pct",
            "excess_return_p10_pct",
            "excess_return_p50_pct",
            "excess_return_p90_pct",
            "recent_return_interpretation",
            "evidence",
            "rank",
        ],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "replay_id": {"type": "string"},
            "treatment_id": {"type": "string"},
            "dispersion_state": {"type": "string", "enum": ["low", "normal", "high"]},
            "dominant_pattern": {
                "type": "string",
                "enum": ["continuation", "reversal", "mixed"],
            },
            "market_rationale": {"type": "string"},
            "candidate_assessments": {
                "type": "array",
                "minItems": 10,
                "maxItems": 18,
                "items": assessment,
            },
            "top3_option_ids": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": {"type": "string"},
            },
            "prefer_spy": {"type": "boolean"},
            "portfolio_rationale": {"type": "string"},
        },
        "required": [
            "replay_id",
            "treatment_id",
            "dispersion_state",
            "dominant_pattern",
            "market_rationale",
            "candidate_assessments",
            "top3_option_ids",
            "prefer_spy",
            "portfolio_rationale",
        ],
    }


def canonicalize(payload: Any, episode: dict[str, Any]) -> Any:
    if not isinstance(payload, dict):
        return payload
    normalized = json.loads(json.dumps(payload))
    options = option_index(episode)
    aliases: dict[str, str] = {}
    for option_id, row in options.items():
        aliases[option_id.upper()] = option_id
        if row.get("symbol"):
            aliases[str(row["symbol"]).upper()] = option_id

    def canonical(value: Any) -> str:
        text = str(value or "").strip()
        return aliases.get(text.upper(), text)

    if isinstance(normalized.get("candidate_assessments"), list):
        for row in normalized["candidate_assessments"]:
            if isinstance(row, dict):
                row["option_id"] = canonical(row.get("option_id"))
    if isinstance(normalized.get("top3_option_ids"), list):
        normalized["top3_option_ids"] = [canonical(value) for value in normalized["top3_option_ids"]]
    return normalized


def expected_lane_map(config: dict[str, Any], episode: dict[str, Any]) -> dict[str, list[str]]:
    return {str(row["option_id"]): list(row["lanes"]) for row in candidate_slate(config, episode)}


def validate_payload(
    payload: Any, config: dict[str, Any], episode: dict[str, Any]
) -> list[str]:
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    errors: list[str] = []
    if payload.get("replay_id") != episode["replay_id"]:
        errors.append("replay_id mismatch")
    if payload.get("treatment_id") != config["treatment_id"]:
        errors.append("treatment_id mismatch")
    assessments = payload.get("candidate_assessments")
    if not isinstance(assessments, list):
        return errors + ["candidate_assessments must be an array"]
    expected = expected_lane_map(config, episode)
    allowed = set(option_index(episode)) - {"CASH"}
    ids = [str(row.get("option_id") or "") for row in assessments if isinstance(row, dict)]
    if len(ids) != len(assessments):
        errors.append("every candidate assessment must be an object")
    if len(ids) != len(set(ids)):
        errors.append("candidate assessment option IDs must be unique")
    missing = sorted(set(expected) - set(ids))
    if missing:
        errors.append(f"missing deterministic slate candidates: {','.join(missing)}")
    invalid = sorted(set(ids) - allowed)
    if invalid:
        errors.append(f"invalid candidate option IDs: {','.join(invalid)}")
    wildcards = sorted(set(ids) - set(expected))
    if len(wildcards) > int(config["candidate_slate"]["maximum_wildcards"]):
        errors.append("too many wildcard candidates")
    ranks: list[int] = []
    for row in assessments:
        if not isinstance(row, dict):
            continue
        option_id = str(row.get("option_id") or "")
        origins = row.get("origin_lanes")
        expected_origins = expected.get(option_id, ["wildcard"])
        if not isinstance(origins, list) or sorted(origins) != sorted(expected_origins):
            errors.append(f"origin_lanes mismatch for {option_id}")
        try:
            rank = int(row.get("rank"))
            ranks.append(rank)
        except (TypeError, ValueError):
            errors.append(f"invalid rank for {option_id}")
        try:
            low = float(row.get("excess_return_p10_pct"))
            median = float(row.get("excess_return_p50_pct"))
            high = float(row.get("excess_return_p90_pct"))
            if not low <= median <= high:
                errors.append(f"quantiles out of order for {option_id}")
        except (TypeError, ValueError):
            errors.append(f"invalid quantiles for {option_id}")
    if sorted(ranks) != list(range(1, len(assessments) + 1)):
        errors.append("candidate ranks must be contiguous and unique")
    top3 = payload.get("top3_option_ids")
    ranked = [
        str(row.get("option_id"))
        for row in sorted(
            (row for row in assessments if isinstance(row, dict)),
            key=lambda row: int(row.get("rank") or 999),
        )[:3]
    ]
    if top3 != ranked:
        errors.append("top3_option_ids must equal candidate ranks 1-3")
    return sorted(set(errors))


def planned_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    calls = [
        {
            "replay_id": str(episode["replay_id"]),
            "model_id": str(model_id),
            "treatment": str(config["treatment_id"]),
        }
        for episode in config["episodes"]
        for model_id in config["models"]
    ]
    if len(config["episodes"]) > int(config["max_test_sets"]):
        raise ValueError("configured episodes exceed the three-set limit")
    if len(calls) > int(config["max_calls"]):
        raise ValueError("planned calls exceed the frozen call budget")
    if any("anthropic" in call["model_id"] or "gpt-5-5" in call["model_id"] for call in calls):
        raise ValueError("prohibited model in V3A call plan")
    return calls


def source_paths(episode: dict[str, Any]) -> list[Path]:
    path = round_path(episode)
    return [
        path / "manifest.yaml",
        path / "options.yaml",
        path / "briefing.md",
        path / "market_data" / "universe_decision_context.csv",
        path / "market_data" / "universe_quality_evidence.json",
    ]


def validate_episode_dates(config: dict[str, Any]) -> None:
    episodes = sorted(config["episodes"], key=lambda row: row["entry_date"])
    for previous, current in zip(episodes, episodes[1:]):
        if date.fromisoformat(str(current["entry_date"])) < date.fromisoformat(str(previous["exit_date"])):
            raise ValueError("V3A replay windows overlap")
    models = base.model_index(config)
    for episode in episodes:
        entry = date.fromisoformat(str(episode["entry_date"]))
        manifest = base.load_yaml(round_path(episode) / "manifest.yaml")
        if manifest.get("methodology_version") != "portfolio-v2.2":
            raise ValueError(f"non-V2.2 source round: {episode['round_id']}")
        if str(manifest.get("entry_date")) != str(episode["entry_date"]):
            raise ValueError(f"entry date mismatch: {episode['replay_id']}")
        if str(manifest.get("exit_date")) != str(episode["exit_date"]):
            raise ValueError(f"exit date mismatch: {episode['replay_id']}")
        for model in models.values():
            eligible = model.first_eligible_date_utc
            if eligible and date.fromisoformat(str(eligible)[:10]) > entry:
                raise ValueError(f"model was not eligible before replay: {model.model_id}")


def prepare(config_path: Path) -> None:
    config_path = config_path.resolve()
    config = load_config(config_path)
    planned = planned_calls(config)
    validate_episode_dates(config)
    directory = output_dir(config)
    packets_dir = directory / "packets"
    evidence_dir = directory / "evidence"
    packets_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    packets: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        slate = candidate_slate(config, episode)
        evidence_path = evidence_dir / f"{episode['replay_id']}.json"
        base.write_json(
            evidence_path,
            {
                "replay_id": episode["replay_id"],
                "round_id": episode["round_id"],
                "outcomes_loaded": False,
                "candidate_slate": slate,
            },
        )
        sources.append(
            {
                "replay_id": episode["replay_id"],
                "path": evidence_path.relative_to(ROOT).as_posix(),
                "sha256": base.sha256_file(evidence_path),
                "slate_size": len(slate),
            }
        )
        prompt = build_prompt(config, episode)
        lowered = prompt.lower()
        found = [marker for marker in FORBIDDEN_PACKET_MARKERS if marker in lowered]
        if found:
            raise ValueError(f"forbidden outcome markers in {episode['replay_id']}: {found}")
        packet_path = packets_dir / f"{episode['replay_id']}__{config['treatment_id']}.txt"
        packet_path.write_text(prompt, encoding="utf-8", newline="\n")
        packets.append(
            {
                "replay_id": episode["replay_id"],
                "treatment": config["treatment_id"],
                "path": packet_path.relative_to(ROOT).as_posix(),
                "sha256": base.sha256_file(packet_path),
                "bytes": packet_path.stat().st_size,
                "schema_sha256": base.sha256_text(json.dumps(response_schema(), sort_keys=True)),
            }
        )
        for source in source_paths(episode):
            if not source.exists():
                raise FileNotFoundError(source)
            sources.append(
                {
                    "replay_id": episode["replay_id"],
                    "path": source.relative_to(ROOT).as_posix(),
                    "sha256": base.sha256_file(source),
                }
            )
    manifest = {
        "experiment_id": config["experiment_id"],
        "frozen_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "outcomes_loaded": False,
        "config_path": config_path.relative_to(ROOT).as_posix(),
        "config_sha256": base.sha256_file(config_path),
        "protocol_sha256": base.sha256_file(ROOT / str(config["protocol"])),
        "runner_sha256": base.sha256_file(Path(__file__)),
        "planned_calls": len(planned),
        "test_sets": len(config["episodes"]),
        "models": list(config["models"]),
        "packets": packets,
        "sources": sources,
    }
    base.write_json(directory / "freeze_manifest.json", manifest)
    print(f"prepared_packets={len(packets)}")
    print(f"planned_calls={len(planned)}")
    print(f"outcomes_loaded={manifest['outcomes_loaded']}")


def verify_freeze(config_path: Path, config: dict[str, Any]) -> dict[str, Any]:
    path = output_dir(config) / "freeze_manifest.json"
    if not path.exists():
        raise RuntimeError("freeze manifest missing; run prepare first")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("outcomes_loaded") is not False:
        raise RuntimeError("freeze does not certify outcomes_loaded=false")
    if manifest.get("config_sha256") != base.sha256_file(config_path):
        raise RuntimeError("config changed after freeze")
    if manifest.get("runner_sha256") != base.sha256_file(Path(__file__)):
        raise RuntimeError("runner changed after freeze")
    for collection in ("packets", "sources"):
        for row in manifest[collection]:
            path = ROOT / str(row["path"])
            if base.sha256_file(path) != row["sha256"]:
                raise RuntimeError(f"frozen artifact changed: {path}")
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
    config_path = config_path.resolve()
    config = load_config(config_path)
    freeze = verify_freeze(config_path, config)
    episodes = episode_index(config)
    models = base.model_index(config)
    base.load_local_env()
    required = {base.PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")
    records_dir = output_dir(config) / "records"
    responses_dir = output_dir(config) / "responses"
    records_dir.mkdir(parents=True, exist_ok=True)
    responses_dir.mkdir(parents=True, exist_ok=True)
    calls = planned_calls(config)
    for position, call in enumerate(calls, start=1):
        stem = base.response_stem(call)
        record_path = records_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if existing.get("valid") or (
                existing.get("validation_errors") and not existing.get("provider_error")
            ):
                print(f"[{position}/{len(calls)}] skip {stem} valid={existing.get('valid')}", flush=True)
                continue
        episode = episodes[call["replay_id"]]
        packet = output_dir(config) / "packets" / f"{call['replay_id']}__{config['treatment_id']}.txt"
        prompt = packet.read_text(encoding="utf-8")
        frozen = next(row for row in freeze["packets"] if row["replay_id"] == call["replay_id"])
        if base.sha256_text(prompt) != frozen["sha256"]:
            raise RuntimeError(f"packet changed after freeze: {packet}")
        model = models[call["model_id"]]
        print(f"[{position}/{len(calls)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            result, attempts = _call_provider(model, prompt, int(config["transport_retries"]))
            provider_error = result.error
        except Exception as exc:
            result = base.ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = 1
            provider_error = str(exc)
        raw_path = responses_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        parsed = canonicalize(result.parsed_json, episode)
        errors = validate_payload(parsed, config, episode)
        if provider_error:
            errors.append(f"provider_error: {provider_error}")
        usage = (
            result.usage.model_dump(mode="json", exclude_none=True)
            if hasattr(result.usage, "model_dump")
            else dict(result.usage or {})
        )
        record = {
            **call,
            "provider": model.provider,
            "api_model_name": model.api_model_name,
            "started_at_utc": started,
            "completed_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "attempts": attempts,
            "packet_sha256": frozen["sha256"],
            "raw_response_path": raw_path.relative_to(ROOT).as_posix(),
            "raw_response_sha256": base.sha256_text(result.raw_text),
            "parsed_json": parsed,
            "usage": usage,
            "provider_error": provider_error,
            "validation_errors": sorted(set(errors)),
            "valid": not errors,
        }
        base.write_json(record_path, record)
        print(f"[{position}/{len(calls)}] saved {stem} valid={record['valid']}", flush=True)
    print(f"records={len(list(records_dir.glob('*.json')))}")


def control_paths(episode: dict[str, Any]) -> tuple[Path, Path, Path]:
    run = round_path(episode) / "runs" / str(episode["control_run_id"])
    return run / "results" / "leaderboard.csv", run / "results" / "returns.csv", run


def _portfolio_return(allocation: dict[str, float], returns: dict[str, float]) -> float:
    return sum(weight / 100.0 * returns[option_id] for option_id, weight in allocation.items())


def _spearman_rank(ids: Sequence[str], returns: dict[str, float]) -> float | None:
    present = [option_id for option_id in ids if option_id in returns]
    if len(present) < 2:
        return None
    realized = sorted(present, key=lambda option_id: returns[option_id], reverse=True)
    actual = {option_id: index + 1 for index, option_id in enumerate(realized)}
    n = len(present)
    squared = sum((index + 1 - actual[option_id]) ** 2 for index, option_id in enumerate(present))
    return 1.0 - 6.0 * squared / (n * (n * n - 1))


def _control_portfolio(run: Path, model_id: str) -> list[str]:
    path = run / "submissions" / "parsed" / f"{model_id}.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [str(row["option_id"]) for row in payload.get("portfolio", [])]


def score_rows(config: dict[str, Any]) -> list[dict[str, Any]]:
    records_dir = output_dir(config) / "records"
    records = {
        (str(row["replay_id"]), str(row["model_id"])): row
        for row in (
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(records_dir.glob("*.json"))
        )
    }
    rows: list[dict[str, Any]] = []
    allocations = [float(value) for value in config["portfolio"]["rank_allocations_pct"]]
    for episode in config["episodes"]:
        leaderboard_path, returns_path, run = control_paths(episode)
        leaderboard = {row["model_id"]: row for row in read_csv(leaderboard_path)}
        return_rows = read_csv(returns_path)
        returns = {row["option_id"]: float(row["return"]) for row in return_rows}
        realized_order = [
            row["option_id"]
            for row in sorted(return_rows, key=lambda row: float(row["return"]), reverse=True)
        ]
        realized_top3 = set(realized_order[:3])
        slate = candidate_slate(config, episode)
        slate_ids = [str(row["option_id"]) for row in slate]
        for model_id in config["models"]:
            record = records.get((str(episode["replay_id"]), str(model_id)))
            control = leaderboard.get(str(model_id))
            base_row = {
                "replay_id": episode["replay_id"],
                "round_id": episode["round_id"],
                "model_id": model_id,
                "valid": bool(record and record.get("valid") and control),
                "provider_error": record.get("provider_error") if record else "missing record",
                "validation_errors": record.get("validation_errors") if record else ["missing record"],
                "spy_return_pct": returns["SP500"] * 100.0,
                "winner_option_id": realized_order[0],
                "realized_top3": realized_order[:3],
                "slate_size": len(slate_ids),
                "slate_winner_capture": realized_order[0] in slate_ids,
                "slate_top3_capture_count": len(realized_top3 & set(slate_ids)),
            }
            if not base_row["valid"]:
                rows.append(base_row)
                continue
            payload = record["parsed_json"]
            top3 = [str(value) for value in payload["top3_option_ids"]]
            if payload["prefer_spy"]:
                allocation = {"SP500": 100.0}
            else:
                allocation = {
                    option_id: allocations[index] for index, option_id in enumerate(top3)
                }
            treatment_return = _portfolio_return(allocation, returns)
            control_return = float(control["portfolio_return"])
            control_ids = _control_portfolio(run, str(model_id))
            ranked_ids = [
                str(row["option_id"])
                for row in sorted(payload["candidate_assessments"], key=lambda row: int(row["rank"]))
            ]
            base_row.update(
                {
                    "prefer_spy": bool(payload["prefer_spy"]),
                    "top3_option_ids": top3,
                    "allocation": allocation,
                    "treatment_return_pct": treatment_return * 100.0,
                    "treatment_alpha_pct": (treatment_return - returns["SP500"]) * 100.0,
                    "control_return_pct": control_return * 100.0,
                    "control_alpha_pct": (control_return - returns["SP500"]) * 100.0,
                    "paired_improvement_pct": (treatment_return - control_return) * 100.0,
                    "treatment_winner_capture": realized_order[0] in top3,
                    "treatment_top3_capture": bool(realized_top3 & set(top3)),
                    "control_winner_capture": realized_order[0] in control_ids,
                    "control_top3_capture": bool(realized_top3 & set(control_ids)),
                    "candidate_rank_spearman": _spearman_rank(ranked_ids, returns),
                }
            )
            rows.append(base_row)
    return rows


def _mean(rows: Iterable[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return statistics.mean(values) if values else None


def aggregate(config: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [row for row in rows if row["valid"]]
    by_model: dict[str, dict[str, Any]] = {}
    for model_id in config["models"]:
        subset = [row for row in valid if row["model_id"] == model_id]
        by_model[model_id] = {
            "valid_pairs": len(subset),
            "mean_treatment_alpha_pct": _mean(subset, "treatment_alpha_pct"),
            "mean_paired_improvement_pct": _mean(subset, "paired_improvement_pct"),
        }
    by_period: dict[str, dict[str, Any]] = {}
    for episode in config["episodes"]:
        replay_id = str(episode["replay_id"])
        subset = [row for row in valid if row["replay_id"] == replay_id]
        by_period[replay_id] = {
            "valid_pairs": len(subset),
            "mean_treatment_alpha_pct": _mean(subset, "treatment_alpha_pct"),
            "mean_paired_improvement_pct": _mean(subset, "paired_improvement_pct"),
            "slate_winner_capture": subset[0]["slate_winner_capture"] if subset else None,
            "slate_top3_capture_count": subset[0]["slate_top3_capture_count"] if subset else None,
        }
    overall = {
        "valid_pairs": len(valid),
        "mean_treatment_return_pct": _mean(valid, "treatment_return_pct"),
        "mean_treatment_alpha_pct": _mean(valid, "treatment_alpha_pct"),
        "mean_control_alpha_pct": _mean(valid, "control_alpha_pct"),
        "mean_paired_improvement_pct": _mean(valid, "paired_improvement_pct"),
        "positive_pairs": sum(float(row["paired_improvement_pct"]) > 0 for row in valid),
        "treatment_spy_beats": sum(float(row["treatment_alpha_pct"]) > 0 for row in valid),
        "control_spy_beats": sum(float(row["control_alpha_pct"]) > 0 for row in valid),
        "treatment_winner_captures": sum(bool(row["treatment_winner_capture"]) for row in valid),
        "control_winner_captures": sum(bool(row["control_winner_capture"]) for row in valid),
        "treatment_top3_captures": sum(bool(row["treatment_top3_capture"]) for row in valid),
        "control_top3_captures": sum(bool(row["control_top3_capture"]) for row in valid),
        "mean_candidate_rank_spearman": _mean(valid, "candidate_rank_spearman"),
    }
    gate = config["gate"]
    positive_models = sum(
        row["mean_treatment_alpha_pct"] is not None and row["mean_treatment_alpha_pct"] > 0
        for row in by_model.values()
    )
    positive_periods = sum(
        row["mean_treatment_alpha_pct"] is not None and row["mean_treatment_alpha_pct"] > 0
        for row in by_period.values()
    )
    worst_period_improvement = min(
        (float(row["mean_paired_improvement_pct"]) for row in by_period.values() if row["mean_paired_improvement_pct"] is not None),
        default=-999.0,
    )
    checks = {
        "valid_pairs": overall["valid_pairs"] >= int(gate["minimum_valid_pairs"]),
        "positive_treatment_alpha": (
            overall["mean_treatment_alpha_pct"] is not None
            and overall["mean_treatment_alpha_pct"] > float(gate["minimum_mean_treatment_alpha_pct"])
        ),
        "paired_improvement": (
            overall["mean_paired_improvement_pct"] is not None
            and overall["mean_paired_improvement_pct"] >= float(gate["minimum_mean_paired_improvement_pct"])
        ),
        "positive_pairs": overall["positive_pairs"] >= int(gate["minimum_positive_pairs"]),
        "positive_models": positive_models >= int(gate["minimum_positive_models"]),
        "positive_periods": positive_periods >= int(gate["minimum_positive_periods"]),
        "worst_period": worst_period_improvement >= -float(gate["maximum_worst_period_deterioration_pct"]),
        "top3_capture_not_worse": (
            overall["treatment_top3_captures"] - overall["control_top3_captures"]
            >= int(gate["minimum_selected_top3_capture_change"])
        ),
    }
    return {
        "overall": overall,
        "by_model": by_model,
        "by_period": by_period,
        "positive_models": positive_models,
        "positive_periods": positive_periods,
        "worst_period_improvement_pct": worst_period_improvement,
        "gate_checks": checks,
        "passes_gate": all(checks.values()),
    }


def _fmt(value: Any) -> str:
    return "n/a" if value is None else f"{float(value):.2f}%"


def render_report(config: dict[str, Any], summary: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    aggregate_row = summary["aggregate"]
    overall = aggregate_row["overall"]
    lines = [
        "# Portfolio V3 Anti-Extrapolation Replay Results",
        "",
        f"Decision: **{summary['decision']}**",
        "",
        "## Primary Result",
        "",
        f"- Valid paired cells: {overall['valid_pairs']}/12",
        f"- V3A mean alpha versus SPY: {_fmt(overall['mean_treatment_alpha_pct'])}",
        f"- Saved V2.2 control mean alpha: {_fmt(overall['mean_control_alpha_pct'])}",
        f"- Mean paired V3A improvement: {_fmt(overall['mean_paired_improvement_pct'])}",
        f"- V3A SPY beats: {overall['treatment_spy_beats']}/{overall['valid_pairs']}",
        f"- Improved pairs: {overall['positive_pairs']}/{overall['valid_pairs']}",
        f"- V3A selected top-three captures: {overall['treatment_top3_captures']} (control {overall['control_top3_captures']})",
        f"- Mean candidate rank correlation: {overall['mean_candidate_rank_spearman']:.3f}" if overall["mean_candidate_rank_spearman"] is not None else "- Mean candidate rank correlation: n/a",
        "",
        "## By Test Set",
        "",
        "| Set | V3A alpha | Paired improvement | Slate winner present | Slate top-three count |",
        "| --- | ---: | ---: | --- | ---: |",
    ]
    for replay_id, row in aggregate_row["by_period"].items():
        lines.append(
            f"| {replay_id} | {_fmt(row['mean_treatment_alpha_pct'])} | {_fmt(row['mean_paired_improvement_pct'])} | "
            f"{'yes' if row['slate_winner_capture'] else 'no'} | {row['slate_top3_capture_count']} |"
        )
    lines.extend(
        [
            "",
            "## By Model",
            "",
            "| Model | Valid sets | V3A alpha | Paired improvement |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for model_id, row in aggregate_row["by_model"].items():
        lines.append(
            f"| {model_id} | {row['valid_pairs']} | {_fmt(row['mean_treatment_alpha_pct'])} | {_fmt(row['mean_paired_improvement_pct'])} |"
        )
    lines.extend(["", "## Frozen Gate", ""])
    for key, passed in aggregate_row["gate_checks"].items():
        lines.append(f"- {key.replace('_', ' ')}: {'PASS' if passed else 'FAIL'}")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            (
                "V3A cleared the frozen historical gate and may advance unchanged to a private prospective shadow. "
                "This replay is not production confirmation and must not alter official methodology by itself."
                if aggregate_row["passes_gate"]
                else "V3A failed at least one frozen gate and is rejected. Do not tune it on these three test sets or adopt it in production."
            ),
            "",
            "The three source windows occur after the first eligible dates of the tested models and do not overlap. "
            "Packets were frozen before the scorer loaded outcomes. Historical replay can still reject more strongly than it can prove future alpha, so any passing result requires a fresh prospective shadow.",
            "",
            "## Cell Results",
            "",
            "| Set | Model | V3A alpha | V2.2 alpha | Improvement | V3A top three | Valid |",
            "| --- | --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['replay_id']} | {row['model_id']} | {_fmt(row.get('treatment_alpha_pct'))} | "
            f"{_fmt(row.get('control_alpha_pct'))} | {_fmt(row.get('paired_improvement_pct'))} | "
            f"{', '.join(row.get('top3_option_ids') or []) or 'n/a'} | {'yes' if row['valid'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## Reproducibility",
            "",
            f"- Experiment: `{config['experiment_id']}`",
            f"- Calls used: {summary['calls_used']} (maximum {config['max_calls']})",
            f"- Test sets: {len(config['episodes'])} (maximum {config['max_test_sets']})",
            "- Participant tools, browsing, retrieval, and follow-up: disabled",
            "- Official score eligibility: no",
            "",
        ]
    )
    return "\n".join(lines)


def score(config_path: Path) -> None:
    config_path = config_path.resolve()
    config = load_config(config_path)
    verify_freeze(config_path, config)
    rows = score_rows(config)
    aggregate_row = aggregate(config, rows)
    records_dir = output_dir(config) / "records"
    records = [json.loads(path.read_text(encoding="utf-8")) for path in records_dir.glob("*.json")]
    calls_used = sum(int(row.get("attempts") or 0) for row in records)
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": "advance_to_prospective_shadow" if aggregate_row["passes_gate"] else "rejected",
        "aggregate": aggregate_row,
        "calls_used": calls_used,
        "max_calls": int(config["max_calls"]),
        "test_sets": len(config["episodes"]),
        "official_score_eligible": False,
        "production_impact": "none",
        "config_sha256": base.sha256_file(config_path),
        "freeze_manifest_sha256": base.sha256_file(output_dir(config) / "freeze_manifest.json"),
    }
    base.write_json(output_dir(config) / "score_summary.json", summary)
    base.write_csv(output_dir(config) / "scored_cells.csv", rows)
    base.write_json(canonical_summary(config), summary)
    report = render_report(config, summary, rows)
    canonical_report(config).parent.mkdir(parents=True, exist_ok=True)
    canonical_report(config).write_text(report, encoding="utf-8", newline="\n")
    print(f"decision={summary['decision']}")
    print(f"valid_pairs={aggregate_row['overall']['valid_pairs']}/12")
    print(f"mean_treatment_alpha_pct={aggregate_row['overall']['mean_treatment_alpha_pct']}")
    print(f"mean_paired_improvement_pct={aggregate_row['overall']['mean_paired_improvement_pct']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("prepare")
    subparsers.add_parser("run")
    subparsers.add_parser("score")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "prepare":
        prepare(args.config)
    elif args.command == "run":
        run(args.config)
    elif args.command == "score":
        score(args.config)


if __name__ == "__main__":
    main()

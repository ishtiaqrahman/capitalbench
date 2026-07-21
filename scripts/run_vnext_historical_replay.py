#!/usr/bin/env python3
"""Prepare, run, and score the private VNext historical replay experiment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from statistics import mean, pstdev
from typing import Any, Iterable, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from capitalbench.config import load_model_configs  # noqa: E402
from capitalbench.providers import GoogleProvider, OpenAIProvider, XAIProvider  # noqa: E402
from capitalbench.providers.base import ProviderResult  # noqa: E402
from capitalbench.schemas import ModelConfig, RuntimeSettings  # noqa: E402


DEFAULT_EXPERIMENT = ROOT / "experiments" / "vnext-historical-replay-2026-07-20.yaml"
DEFAULT_REPORT_COPY = ROOT / "docs" / "vnext_historical_replay_report.md"
MODEL_CONFIG_PATH = ROOT / "configs" / "models.v2.yaml"

PROVIDERS = {
    "google": GoogleProvider,
    "openai": OpenAIProvider,
    "xai": XAIProvider,
}

SIGNAL_TYPES = {"continuation", "reversal", "catalyst", "defensive", "mixed"}
RAW_RETURN_FIELDS = ("return_7d", "return_30d", "return_6m", "return_1y")
SETUP_ROW_MARKERS = (
    "research cutoff",
    "decision deadline",
    "weekly round",
    "monthly round",
    "weekly entry and exit dates",
    "monthly entry and exit dates",
    "entry snapshot",
)
ROUND_ID_RE = re.compile(r"CB-\d{4}-\d{2}-\d{2}(?:-V2)?-1[WM]")


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8", newline="\n")
        return
    columns: list[str] = []
    for row in rows:
        for key in row:
            if key not in columns:
                columns.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            clean: dict[str, Any] = {}
            for key in columns:
                value = row.get(key)
                if isinstance(value, float):
                    clean[key] = f"{value:.10f}" if math.isfinite(value) else ""
                elif isinstance(value, (list, dict, tuple)):
                    clean[key] = json.dumps(value, sort_keys=True)
                elif value is None:
                    clean[key] = ""
                else:
                    clean[key] = value
            writer.writerow(clean)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8", newline="\n")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def as_float(value: Any) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def load_local_env() -> None:
    for path in (ROOT / ".env", ROOT / ".env.local"):
        if not path.exists():
            continue
        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            if key and key not in os.environ:
                os.environ[key] = value.strip().strip("\"'")


def percentile_ranks(values: Sequence[float | None]) -> list[float | None]:
    indexed = [(index, value) for index, value in enumerate(values) if value is not None]
    if not indexed:
        return [None] * len(values)
    ordered = sorted(indexed, key=lambda item: float(item[1]))
    output: list[float | None] = [None] * len(values)
    denominator = max(len(ordered) - 1, 1)
    cursor = 0
    while cursor < len(ordered):
        end = cursor + 1
        while end < len(ordered) and ordered[end][1] == ordered[cursor][1]:
            end += 1
        rank = ((cursor + end - 1) / 2.0) / denominator if len(ordered) > 1 else 0.5
        for original_index, _value in ordered[cursor:end]:
            output[original_index] = rank
        cursor = end
    return output


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def experiment_output(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def episode_index(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["replay_id"]): item for item in config["episodes"]}


def source_round(episode: dict[str, Any]) -> Path:
    return ROOT / "rounds" / str(episode["round_id"])


def load_options(round_path: Path) -> list[dict[str, Any]]:
    payload = load_yaml(round_path / "options.yaml")
    return [row for row in payload.get("options", []) if isinstance(row, dict) and row.get("id")]


def model_index(config: dict[str, Any]) -> dict[str, ModelConfig]:
    selected = set(str(value) for value in config["models"])
    api_model_overrides = {
        str(key): str(value)
        for key, value in (config.get("api_model_overrides") or {}).items()
    }
    loaded = {item.model_id: item for item in load_model_configs(MODEL_CONFIG_PATH)}
    missing = sorted(selected - set(loaded))
    if missing:
        raise ValueError(f"missing model configs: {missing}")
    output: dict[str, ModelConfig] = {}
    for model_id in selected:
        original = loaded[model_id]
        if original.provider == "anthropic":
            raise ValueError("Anthropic models are prohibited in this experiment")
        updates: dict[str, Any] = {
            "max_completion_tokens": int(config["max_output_tokens"]),
        }
        if model_id in api_model_overrides:
            updates["api_model_name"] = api_model_overrides[model_id]
        output[model_id] = original.model_copy(update=updates)
    return output


def _section_map(markdown: str) -> dict[int, list[str]]:
    sections: dict[int, list[str]] = defaultdict(list)
    current = 0
    for line in markdown.splitlines():
        match = re.match(r"^##\s+(\d+)\.", line)
        if match:
            current = int(match.group(1))
        if current:
            sections[current].append(line)
    return dict(sections)


def sanitize_full_briefing(markdown: str) -> str:
    sections = _section_map(markdown)
    kept: list[str] = []
    for number in sorted(sections):
        if number in {1, 2, 7, 9}:
            continue
        for line in sections[number]:
            lowered = line.lower()
            if any(marker in lowered for marker in SETUP_ROW_MARKERS):
                continue
            if "round exit close" in lowered:
                continue
            kept.append(ROUND_ID_RE.sub("REPLAY-ROUND", line))
    return "\n".join(kept).strip()


def _event_inside_window(line: str, entry: date, exit_date: date) -> bool:
    if "round exit close" in line.lower() or "capitalbench" in line.lower():
        return False
    match = re.search(r"\d{4}-\d{2}-\d{2}", line)
    if not match:
        return False
    event_date = date.fromisoformat(match.group(0))
    return entry <= event_date <= exit_date


def focused_briefing(markdown: str, entry: date, exit_date: date) -> str:
    sections = _section_map(markdown)
    kept: list[str] = []
    for number in (3, 4, 6):
        kept.extend(sections.get(number, []))
    event_lines = sections.get(8, [])
    event_heading = event_lines[:3]
    events = [line for line in event_lines[3:] if line.startswith("|") and _event_inside_window(line, entry, exit_date)]
    if events:
        kept.extend(event_heading)
        kept.extend(events)
    return "\n".join(ROUND_ID_RE.sub("REPLAY-ROUND", line) for line in kept).strip()


def common_market_rows(round_path: Path) -> list[dict[str, Any]]:
    source = read_csv(round_path / "market_data" / "universe_trailing_returns.csv")
    options = {str(row["id"]): row for row in load_options(round_path)}
    rows: list[dict[str, Any]] = []
    for source_row in source:
        option_id = str(source_row.get("option_id") or "")
        option = options.get(option_id)
        if not option or bool(option.get("is_cash")) or str(source_row.get("status")) != "pass":
            continue
        row: dict[str, Any] = {
            "option_id": option_id,
            "symbol": source_row.get("symbol") or option.get("symbol") or "",
            "name": source_row.get("name") or option.get("name") or option_id,
            "option_group": option.get("option_group") or source_row.get("option_group") or "",
            "risk_bucket": option.get("risk_bucket") or source_row.get("risk_bucket") or "",
            "is_benchmark": bool(option.get("is_benchmark")) or option_id == "SP500",
        }
        for field in RAW_RETURN_FIELDS:
            row[field] = as_float(source_row.get(field))
        rows.append(row)
    if not rows:
        raise ValueError(f"no common market rows for {round_path.name}")
    if sum(bool(row["is_benchmark"]) for row in rows) != 1:
        raise ValueError(f"{round_path.name} must contain exactly one SP500 row")
    return rows


def derived_market_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output = [dict(row) for row in rows]
    spy = next(row for row in rows if row["is_benchmark"])
    for field in RAW_RETURN_FIELDS:
        ranks = percentile_ranks([as_float(row.get(field)) for row in rows])
        for row, rank in zip(output, ranks):
            row[f"rank_{field}"] = rank
            value = as_float(row.get(field))
            spy_value = as_float(spy.get(field))
            row[f"active_{field}"] = value - spy_value if value is not None and spy_value is not None else None
    for row in output:
        rank_7d = as_float(row.get("rank_return_7d"))
        rank_30d = as_float(row.get("rank_return_30d"))
        rank_6m = as_float(row.get("rank_return_6m"))
        rank_1y = as_float(row.get("rank_return_1y"))
        row["recent_vs_medium_rank_shift"] = (
            rank_7d - rank_30d if rank_7d is not None and rank_30d is not None else None
        )
        ranks = [value for value in (rank_7d, rank_30d, rank_6m, rank_1y) if value is not None]
        row["trend_rank_dispersion"] = pstdev(ranks) if len(ranks) >= 2 else None
    return output


def _pct(value: Any) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.2f}%"


def _rank(value: Any) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.1f}"


def raw_market_table(rows: list[dict[str, Any]]) -> str:
    data = [
        [
            row["option_id"],
            row["symbol"],
            row["option_group"],
            row["risk_bucket"],
            _pct(row.get("return_7d")),
            _pct(row.get("return_30d")),
            _pct(row.get("return_6m")),
            _pct(row.get("return_1y")),
        ]
        for row in rows
    ]
    return markdown_table(
        ["option_id", "symbol", "group", "risk", "7d", "30d", "6m", "1y"],
        data,
    )


def derived_market_table(rows: list[dict[str, Any]]) -> str:
    data = [
        [
            row["option_id"],
            row["symbol"],
            row["option_group"],
            _pct(row.get("active_return_7d")),
            _pct(row.get("active_return_30d")),
            _rank(row.get("rank_return_7d")),
            _rank(row.get("rank_return_30d")),
            _rank(row.get("rank_return_6m")),
            _rank(row.get("rank_return_1y")),
            _rank(row.get("recent_vs_medium_rank_shift")),
            _rank(row.get("trend_rank_dispersion")),
        ]
        for row in rows
    ]
    return markdown_table(
        [
            "option_id",
            "symbol",
            "group",
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


def response_schema() -> dict[str, Any]:
    top5_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "rank": {"type": "integer", "minimum": 1, "maximum": 5},
            "option_id": {"type": "string"},
            "forecast_return_pct": {"type": "number"},
            "expected_alpha_vs_spy_pct": {"type": "number"},
            "signal_type": {"type": "string", "enum": sorted(SIGNAL_TYPES)},
            "evidence": {"type": "string"},
            "invalidation": {"type": "string"},
        },
        "required": [
            "rank",
            "option_id",
            "forecast_return_pct",
            "expected_alpha_vs_spy_pct",
            "signal_type",
            "evidence",
            "invalidation",
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
            "shortlist_option_ids": {
                "type": "array",
                "minItems": 10,
                "maxItems": 10,
                "items": {"type": "string"},
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
            "shortlist_option_ids",
            "top5",
        ],
    }


COMMON_TASK = """
You are participating in a private, retrospective CapitalBench input experiment.
Treat the packet as an unknown decision point. Use only the supplied packet and
do not use remembered historical outcomes, tools, browsing, search, or external
facts. The investment horizon is one week.

Forecast SPY separately. Then identify ten non-cash, non-SPY active candidates
from the complete option table and reduce them to a ranked final five. The final
five must be a subset of the ten. Use exact option_id values. Rank 1 is your
highest expected one-week return. expected_alpha_vs_spy_pct must equal the
candidate forecast minus your SPY forecast. prefer_spy should be true when none
of the five candidates is expected to beat SPY.

Return only JSON matching the required schema. Keep evidence and invalidation
fields factual and concise.
""".strip()

RANK_FIRST = """
Apply this fixed process before returning JSON:
1. Screen the complete universe rather than only briefing-mentioned assets.
2. Build a ten-option shortlist using expected one-week alpha versus SPY.
3. For each finalist, explicitly distinguish continuation evidence from reversal risk.
4. Check whether any identified catalyst can matter inside one week.
5. Challenge crowded or extreme recent moves before finalizing the rank.
6. Forecast SPY independently, then select and rank the final five.
""".strip()


def build_prompt(config: dict[str, Any], episode: dict[str, Any], treatment: str) -> str:
    round_path = source_round(episode)
    manifest = load_yaml(round_path / "manifest.yaml")
    entry = date.fromisoformat(str(manifest["entry_date"])[:10])
    exit_date = date.fromisoformat(str(manifest["exit_date"])[:10])
    briefing_path = round_path / "research" / "final_briefing.md"
    if not briefing_path.exists():
        briefing_path = round_path / "briefing.md"
    briefing = briefing_path.read_text(encoding="utf-8")
    raw_rows = common_market_rows(round_path)

    if treatment == "H3":
        briefing_text = focused_briefing(briefing, entry, exit_date)
    else:
        briefing_text = sanitize_full_briefing(briefing)
    if treatment == "H2":
        table = derived_market_table(derived_market_rows(raw_rows))
    else:
        table = raw_market_table(raw_rows)

    treatment_text = {
        "H0": "Evaluate the supplied facts directly. No additional decision scaffold is prescribed.",
        "H1": RANK_FIRST,
        "H2": RANK_FIRST
        + "\nThe comparison table supplies within-universe percentiles. Percentiles describe relative position, not certainty or a recommendation.",
        "H3": RANK_FIRST
        + "\nThe briefing is mechanically limited to current market facts and events inside the scoring horizon. Do not assume omitted facts are negative.",
    }[treatment]
    return (
        f"{COMMON_TASK}\n\n"
        f"Replay identifier: {episode['replay_id']}\n"
        f"Treatment identifier: {treatment}\n\n"
        f"Treatment instructions:\n{treatment_text}\n\n"
        f"Frozen factual briefing:\n{briefing_text}\n\n"
        f"Complete option comparison table:\n{table}\n"
    )


def allowed_active_ids(episode: dict[str, Any]) -> set[str]:
    return {
        str(row["id"])
        for row in load_options(source_round(episode))
        if not bool(row.get("is_cash")) and not bool(row.get("is_benchmark")) and str(row["id"]) != "SP500"
    }


def canonicalize_option_ids(payload: Any, episode: dict[str, Any]) -> Any:
    """Map unambiguous ticker aliases back to frozen CapitalBench option IDs."""
    if not isinstance(payload, dict):
        return payload
    aliases: dict[str, str] = {}
    ambiguous: set[str] = set()
    for row in load_options(source_round(episode)):
        option_id = str(row["id"])
        if bool(row.get("is_cash")) or bool(row.get("is_benchmark")) or option_id == "SP500":
            continue
        for candidate in (option_id, row.get("symbol")):
            alias = str(candidate or "").strip().upper()
            if not alias:
                continue
            if alias in aliases and aliases[alias] != option_id:
                ambiguous.add(alias)
            else:
                aliases[alias] = option_id
    for alias in ambiguous:
        aliases.pop(alias, None)

    def canonical(value: Any) -> str:
        text = str(value or "").strip()
        return aliases.get(text.upper(), text)

    normalized = json.loads(json.dumps(payload))
    shortlist = normalized.get("shortlist_option_ids")
    if isinstance(shortlist, list):
        normalized["shortlist_option_ids"] = [canonical(value) for value in shortlist]
    top5 = normalized.get("top5")
    if isinstance(top5, list):
        for item in top5:
            if isinstance(item, dict):
                item["option_id"] = canonical(item.get("option_id"))
    return normalized


def validate_payload(payload: Any, episode: dict[str, Any], treatment: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["response is not a JSON object"]
    if payload.get("replay_id") != episode["replay_id"]:
        errors.append("replay_id mismatch")
    if payload.get("treatment_id") != treatment:
        errors.append("treatment_id mismatch")
    spy_forecast = as_float(payload.get("spy_forecast_return_pct"))
    if spy_forecast is None:
        errors.append("invalid SPY forecast")
    if not isinstance(payload.get("prefer_spy"), bool):
        errors.append("prefer_spy must be boolean")

    active_ids = allowed_active_ids(episode)
    shortlist = payload.get("shortlist_option_ids")
    if not isinstance(shortlist, list) or len(shortlist) != 10:
        errors.append("shortlist must contain exactly 10 IDs")
        shortlist = []
    shortlist_ids = [str(value) for value in shortlist]
    if len(set(shortlist_ids)) != len(shortlist_ids):
        errors.append("shortlist IDs must be unique")
    unknown_shortlist = sorted(set(shortlist_ids) - active_ids)
    if unknown_shortlist:
        errors.append(f"invalid shortlist IDs: {unknown_shortlist}")

    top5 = payload.get("top5")
    if not isinstance(top5, list) or len(top5) != 5:
        errors.append("top5 must contain exactly 5 rows")
        top5 = []
    top_ids: list[str] = []
    ranks: list[int] = []
    for item in top5:
        if not isinstance(item, dict):
            errors.append("top5 row is not an object")
            continue
        option_id = str(item.get("option_id") or "")
        top_ids.append(option_id)
        try:
            ranks.append(int(item.get("rank")))
        except (TypeError, ValueError):
            errors.append(f"invalid rank for {option_id}")
        forecast = as_float(item.get("forecast_return_pct"))
        alpha = as_float(item.get("expected_alpha_vs_spy_pct"))
        if forecast is None or alpha is None:
            errors.append(f"invalid forecasts for {option_id}")
        elif spy_forecast is not None and abs((forecast - spy_forecast) - alpha) > 0.26:
            errors.append(f"alpha arithmetic mismatch for {option_id}")
        if item.get("signal_type") not in SIGNAL_TYPES:
            errors.append(f"invalid signal type for {option_id}")
        if not str(item.get("evidence") or "").strip():
            errors.append(f"missing evidence for {option_id}")
        if not str(item.get("invalidation") or "").strip():
            errors.append(f"missing invalidation for {option_id}")
    if len(set(top_ids)) != len(top_ids):
        errors.append("top5 IDs must be unique")
    if set(top_ids) - active_ids:
        errors.append(f"invalid top5 IDs: {sorted(set(top_ids) - active_ids)}")
    if set(top_ids) - set(shortlist_ids):
        errors.append("top5 must be a subset of shortlist")
    if sorted(ranks) != [1, 2, 3, 4, 5]:
        errors.append("top5 ranks must be 1 through 5")
    return sorted(set(errors))


def discovery_calls(config: dict[str, Any]) -> list[dict[str, str]]:
    episodes = [item for item in config["episodes"] if item["phase"] == "discovery"]
    assignments = config["discovery_assignment"]
    calls: list[dict[str, str]] = []
    for model_id in config["models"]:
        treatments = assignments[model_id]
        if len(treatments) != len(episodes):
            raise ValueError(f"discovery assignment length mismatch for {model_id}")
        for episode, challenger in zip(episodes, treatments):
            calls.append({"replay_id": episode["replay_id"], "model_id": model_id, "treatment": "H0"})
            calls.append({"replay_id": episode["replay_id"], "model_id": model_id, "treatment": challenger})
    return calls


def confirmation_calls(config: dict[str, Any], selected: str) -> list[dict[str, str]]:
    calls: list[dict[str, str]] = []
    for episode in config["episodes"]:
        if episode["phase"] != "confirmation":
            continue
        for model_id in config["models"]:
            for treatment in ("H0", selected):
                calls.append({"replay_id": episode["replay_id"], "model_id": model_id, "treatment": treatment})
    return calls


def response_stem(call: dict[str, str]) -> str:
    safe_model = call["model_id"].replace("/", "_")
    return f"{call['replay_id']}__{safe_model}__{call['treatment']}"


def prepare(config_path: Path) -> None:
    config = load_yaml(config_path)
    output = experiment_output(config)
    packets = output / "packets"
    packets.mkdir(parents=True, exist_ok=True)
    manifest_rows: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        for treatment in config["treatments"]:
            prompt = build_prompt(config, episode, treatment)
            path = packets / f"{episode['replay_id']}__{treatment}.txt"
            path.write_text(prompt, encoding="utf-8", newline="\n")
            manifest_rows.append(
                {
                    "replay_id": episode["replay_id"],
                    "phase": episode["phase"],
                    "treatment": treatment,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": sha256_text(prompt),
                    "characters": len(prompt),
                    "estimated_tokens": round(len(prompt) / 4),
                }
            )
    freeze = {
        "experiment_id": config["experiment_id"],
        "frozen_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "experiment_config_path": config_path.relative_to(ROOT).as_posix(),
        "experiment_config_sha256": sha256_file(config_path),
        "protocol_path": str(config["protocol"]),
        "protocol_sha256": sha256_file(ROOT / str(config["protocol"])),
        "script_sha256": sha256_file(Path(__file__)),
        "response_schema_sha256": sha256_text(json.dumps(response_schema(), sort_keys=True)),
        "packets": manifest_rows,
        "discovery_calls": discovery_calls(config),
        "outcomes_loaded": False,
    }
    write_json(output / "freeze_manifest.json", freeze)
    write_csv(output / "packet_manifest.csv", manifest_rows)
    print(f"prepared_packets={len(manifest_rows)}")
    print(f"discovery_calls={len(freeze['discovery_calls'])}")
    print(f"wrote={output / 'freeze_manifest.json'}")


def verify_freeze(config: dict[str, Any]) -> dict[str, Any]:
    output = experiment_output(config)
    freeze_path = output / "freeze_manifest.json"
    if not freeze_path.exists():
        raise RuntimeError("freeze manifest is missing; run prepare first")
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    if freeze.get("outcomes_loaded") is not False:
        raise RuntimeError("freeze manifest does not certify outcomes_loaded=false")
    for packet in freeze["packets"]:
        path = ROOT / packet["path"]
        if sha256_file(path) != packet["sha256"]:
            raise RuntimeError(f"packet hash mismatch: {path}")
    return freeze


def _transport_error(message: str) -> bool:
    lowered = message.lower()
    return any(
        marker in lowered
        for marker in ("http 429", "http 500", "http 502", "http 503", "timed out", "timeout", "temporarily")
    )


def call_provider(model: ModelConfig, prompt: str, retries: int) -> tuple[ProviderResult, int]:
    provider_class = PROVIDERS.get(model.provider)
    if provider_class is None:
        raise ValueError(f"provider not allowed: {model.provider}")
    runtime = RuntimeSettings(
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
            return result, attempts
        except Exception as exc:
            if attempts > retries or not _transport_error(str(exc)):
                raise
            time.sleep(2.0 * attempts)


def run_calls(config_path: Path, phase: str) -> None:
    config = load_yaml(config_path)
    freeze = verify_freeze(config)
    output = experiment_output(config)
    episodes = episode_index(config)
    models = model_index(config)
    load_local_env()
    required_env = {PROVIDERS[model.provider].api_key_env_var for model in models.values()}
    missing = sorted(name for name in required_env if not os.environ.get(name, "").strip())
    if missing:
        raise RuntimeError(f"missing provider credentials: {missing}")

    if phase == "discovery":
        calls = discovery_calls(config)
    else:
        decision_path = output / "discovery_decision.json"
        if not decision_path.exists():
            raise RuntimeError("discovery decision is missing")
        decision = json.loads(decision_path.read_text(encoding="utf-8"))
        selected = decision.get("selected_challenger")
        if not selected:
            print("confirmation_skipped=no discovery challenger passed")
            return
        calls = confirmation_calls(config, str(selected))

    response_dir = output / "responses" / phase
    record_dir = output / "records" / phase
    response_dir.mkdir(parents=True, exist_ok=True)
    record_dir.mkdir(parents=True, exist_ok=True)
    completed = 0
    for position, call in enumerate(calls, start=1):
        stem = response_stem(call)
        record_path = record_dir / f"{stem}.json"
        if record_path.exists():
            existing = json.loads(record_path.read_text(encoding="utf-8"))
            if not existing.get("provider_error"):
                normalized = canonicalize_option_ids(existing.get("parsed_json"), episodes[call["replay_id"]])
                errors = validate_payload(normalized, episodes[call["replay_id"]], call["treatment"])
                existing["parsed_json"] = normalized
                existing["validation_errors"] = sorted(set(errors))
                existing["valid"] = not errors
                write_json(record_path, existing)
                if existing["valid"] or errors != ["response is not a JSON object"]:
                    completed += 1
                    print(
                        f"[{position}/{len(calls)}] skip_existing valid={existing['valid']} {stem}",
                        flush=True,
                    )
                    continue
                print(f"[{position}/{len(calls)}] retry_truncated_json {stem}", flush=True)
            print(f"[{position}/{len(calls)}] retry_provider_error {stem}", flush=True)
        packet_path = output / "packets" / f"{call['replay_id']}__{call['treatment']}.txt"
        prompt = packet_path.read_text(encoding="utf-8")
        packet_hash = sha256_text(prompt)
        frozen_packet = next(
            row for row in freeze["packets"]
            if row["replay_id"] == call["replay_id"] and row["treatment"] == call["treatment"]
        )
        if packet_hash != frozen_packet["sha256"]:
            raise RuntimeError(f"packet changed after freeze: {packet_path}")
        print(f"[{position}/{len(calls)}] call {stem}", flush=True)
        started = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        try:
            result, attempts = call_provider(models[call["model_id"]], prompt, int(config["transport_retries"]))
            error = result.error
        except Exception as exc:
            result = ProviderResult(raw_text="", parsed_json=None, usage={}, error=str(exc))
            attempts = 1
            error = str(exc)
        completed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        raw_path = response_dir / f"{stem}.txt"
        raw_path.write_text(result.raw_text, encoding="utf-8", newline="\n")
        provider_payload = result.parsed_json
        parsed_payload = canonicalize_option_ids(provider_payload, episodes[call["replay_id"]])
        errors = validate_payload(parsed_payload, episodes[call["replay_id"]], call["treatment"])
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
            "raw_response_sha256": sha256_text(result.raw_text),
            "raw_response_path": raw_path.relative_to(ROOT).as_posix(),
            "provider_parsed_json": provider_payload,
            "parsed_json": parsed_payload,
            "usage": result.usage.model_dump(mode="json", exclude_none=True),
            "provider_error": error,
            "validation_errors": sorted(set(errors)),
            "valid": not errors,
        }
        write_json(record_path, record)
        completed += 1
        print(f"[{position}/{len(calls)}] saved valid={record['valid']} {stem}", flush=True)
        if error and not _transport_error(error):
            raise RuntimeError(f"provider call failed for {stem}: {error}")
    print(f"{phase}_records={completed}")


def _selected_official_run(round_path: Path) -> Path:
    matches: list[Path] = []
    for manifest_path in round_path.glob("runs/*/run_manifest.yaml"):
        manifest = load_yaml(manifest_path)
        if (
            manifest.get("run_type") == "official"
            and manifest.get("mock") is False
            and manifest.get("operator_selected_official") is True
            and manifest.get("resolved_at_utc")
            and manifest.get("official_score_eligible") is not False
        ):
            matches.append(manifest_path.parent)
    if len(matches) != 1:
        raise ValueError(f"{round_path.name} has {len(matches)} selected resolved official runs")
    return matches[0]


def load_outcomes(episode: dict[str, Any]) -> dict[str, Any]:
    round_path = source_round(episode)
    run = _selected_official_run(round_path)
    rows = read_csv(run / "results" / "returns.csv")
    returns = {
        str(row["option_id"]): float(row["return"])
        for row in rows
        if row.get("option_id") and as_float(row.get("return")) is not None
    }
    active = allowed_active_ids(episode)
    active_returns = {option_id: returns[option_id] for option_id in active if option_id in returns}
    if len(active_returns) != len(active):
        raise ValueError(f"missing active outcomes for {episode['replay_id']}")
    spy_return = returns["SP500"]
    best_return = max(active_returns.values())
    winners = sorted(option_id for option_id, value in active_returns.items() if value == best_return)
    ordered = sorted(active_returns.items(), key=lambda item: (-item[1], item[0]))
    percentile = {
        option_id: 1.0 - index / max(len(ordered) - 1, 1)
        for index, (option_id, _value) in enumerate(ordered)
    }
    return {
        "returns": returns,
        "active_returns": active_returns,
        "spy_return": spy_return,
        "best_return": best_return,
        "winner_ids": winners,
        "percentile": percentile,
    }


def load_records(config: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    record_dir = experiment_output(config) / "records" / phase
    if not record_dir.exists():
        return []
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(record_dir.glob("*.json"))]


def score_record(record: dict[str, Any], episode: dict[str, Any], outcome: dict[str, Any]) -> dict[str, Any]:
    payload = record.get("parsed_json") if record.get("valid") else None
    base = {
        "phase": episode["phase"],
        "replay_id": episode["replay_id"],
        "model_id": record["model_id"],
        "treatment": record["treatment"],
        "valid": bool(record.get("valid")),
        "validation_errors": record.get("validation_errors", []),
        "spy_return": outcome["spy_return"],
        "best_active_return": outcome["best_return"],
        "winner_ids": outcome["winner_ids"],
        "input_tokens": (record.get("usage") or {}).get("input_tokens"),
        "output_tokens": (record.get("usage") or {}).get("output_tokens"),
        "reasoning_tokens": (record.get("usage") or {}).get("reasoning_tokens"),
        "latency_seconds": (record.get("usage") or {}).get("latency_seconds"),
    }
    if not isinstance(payload, dict):
        return base
    shortlist = [str(value) for value in payload["shortlist_option_ids"]]
    top5_rows = sorted(payload["top5"], key=lambda item: int(item["rank"]))
    top5 = [str(item["option_id"]) for item in top5_rows]
    top5_return = mean(outcome["returns"][option_id] for option_id in top5)
    top1 = top5[0]
    shortlist_best = max(outcome["returns"][option_id] for option_id in shortlist)
    base.update(
        {
            "prefer_spy": payload["prefer_spy"],
            "shortlist_ids": shortlist,
            "top5_ids": top5,
            "top1_id": top1,
            "top10_capture": bool(set(shortlist) & set(outcome["winner_ids"])),
            "top5_capture": bool(set(top5) & set(outcome["winner_ids"])),
            "top5_return": top5_return,
            "top5_alpha": top5_return - outcome["spy_return"],
            "top1_return": outcome["returns"][top1],
            "top1_alpha": outcome["returns"][top1] - outcome["spy_return"],
            "top1_realized_percentile": outcome["percentile"][top1],
            "shortlist_best_return": shortlist_best,
            "shortlist_oracle_regret": outcome["best_return"] - shortlist_best,
        }
    )
    return base


def score_phase(config: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    episodes = episode_index(config)
    outcomes = {
        replay_id: load_outcomes(episode)
        for replay_id, episode in episodes.items()
        if episode["phase"] == phase
    }
    return [score_record(record, episodes[record["replay_id"]], outcomes[record["replay_id"]]) for record in load_records(config, phase)]


def paired_rows(scored: Sequence[dict[str, Any]], challenger_only: str | None = None) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in scored:
        grouped[(str(row["replay_id"]), str(row["model_id"]))][str(row["treatment"])] = row
    output: list[dict[str, Any]] = []
    for (replay_id, model_id), treatments in sorted(grouped.items()):
        control = treatments.get("H0")
        for treatment, challenger in treatments.items():
            if treatment == "H0" or (challenger_only and treatment != challenger_only):
                continue
            if control is None:
                continue
            pair_valid = bool(control.get("valid")) and bool(challenger.get("valid"))
            output.append(
                {
                    "phase": challenger["phase"],
                    "replay_id": replay_id,
                    "model_id": model_id,
                    "challenger": treatment,
                    "pair_valid": pair_valid,
                    "control_top5_capture": control.get("top5_capture"),
                    "challenger_top5_capture": challenger.get("top5_capture"),
                    "capture_change": (
                        int(bool(challenger.get("top5_capture"))) - int(bool(control.get("top5_capture")))
                        if pair_valid else None
                    ),
                    "control_top5_alpha": control.get("top5_alpha"),
                    "challenger_top5_alpha": challenger.get("top5_alpha"),
                    "paired_top5_alpha_improvement": (
                        float(challenger["top5_alpha"]) - float(control["top5_alpha"])
                        if pair_valid else None
                    ),
                    "control_top1_alpha": control.get("top1_alpha"),
                    "challenger_top1_alpha": challenger.get("top1_alpha"),
                    "paired_top1_alpha_improvement": (
                        float(challenger["top1_alpha"]) - float(control["top1_alpha"])
                        if pair_valid else None
                    ),
                }
            )
    return output


def aggregate_pairs(rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["challenger"])].append(row)
    output: list[dict[str, Any]] = []
    for treatment, subset in sorted(grouped.items()):
        valid = [row for row in subset if row["pair_valid"]]
        alpha_diffs = [float(row["paired_top5_alpha_improvement"]) for row in valid]
        control_capture = sum(int(bool(row["control_top5_capture"])) for row in valid)
        challenger_capture = sum(int(bool(row["challenger_top5_capture"])) for row in valid)
        output.append(
            {
                "challenger": treatment,
                "pairs": len(subset),
                "valid_pairs": len(valid),
                "control_capture_count": control_capture,
                "challenger_capture_count": challenger_capture,
                "capture_change": challenger_capture - control_capture,
                "mean_paired_top5_alpha_improvement": mean(alpha_diffs) if alpha_diffs else None,
                "positive_pair_count": sum(value > 0 for value in alpha_diffs),
                "passes_discovery_gate": bool(
                    len(valid) >= 3
                    and alpha_diffs
                    and mean(alpha_diffs) > 0
                    and challenger_capture > control_capture
                ),
            }
        )
    return output


def score_discovery(config_path: Path) -> dict[str, Any]:
    config = load_yaml(config_path)
    verify_freeze(config)
    scored = score_phase(config, "discovery")
    pairs = paired_rows(scored)
    aggregates = aggregate_pairs(pairs)
    passing = [row for row in aggregates if row["passes_discovery_gate"]]
    passing.sort(
        key=lambda row: (
            -float(row["mean_paired_top5_alpha_improvement"]),
            {"H1": 0, "H2": 1, "H3": 2}.get(str(row["challenger"]), 9),
        )
    )
    selected = passing[0]["challenger"] if passing else None
    decision = {
        "scored_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "selected_challenger": selected,
        "confirmation_allowed": selected is not None,
        "gate": "positive paired top5 alpha, greater winner capture, at least 3 valid pairs",
        "aggregates": aggregates,
    }
    output = experiment_output(config)
    write_csv(output / "discovery_call_metrics.csv", scored)
    write_csv(output / "discovery_pairs.csv", pairs)
    write_csv(output / "discovery_aggregate.csv", aggregates)
    write_json(output / "discovery_decision.json", decision)
    print(json.dumps(decision, indent=2))
    return decision


def _pct_report(value: Any, digits: int = 2) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.{digits}f}%"


def usage_summary(records: Sequence[dict[str, Any]]) -> dict[str, Any]:
    usage_rows = [row.get("usage") or {} for row in records]
    return {
        "calls": len(records),
        "valid_calls": sum(bool(row.get("valid")) for row in records),
        "input_tokens": sum(int(row.get("input_tokens") or 0) for row in usage_rows),
        "output_tokens": sum(int(row.get("output_tokens") or 0) for row in usage_rows),
        "reasoning_tokens": sum(int(row.get("reasoning_tokens") or 0) for row in usage_rows),
        "latency_seconds": sum(float(row.get("latency_seconds") or 0.0) for row in usage_rows),
    }


def confirmation_gate(pairs: Sequence[dict[str, Any]], selected: str) -> dict[str, Any]:
    valid = [row for row in pairs if row["pair_valid"] and row["challenger"] == selected]
    diffs = [float(row["paired_top5_alpha_improvement"]) for row in valid]
    control_capture = sum(int(bool(row["control_top5_capture"])) for row in valid)
    challenger_capture = sum(int(bool(row["challenger_top5_capture"])) for row in valid)
    by_model: dict[str, list[float]] = defaultdict(list)
    by_episode: dict[str, list[float]] = defaultdict(list)
    for row in valid:
        value = float(row["paired_top5_alpha_improvement"])
        by_model[str(row["model_id"])].append(value)
        by_episode[str(row["replay_id"])].append(value)
    positive_models = sum(mean(values) > 0 for values in by_model.values())
    positive_episodes = sum(mean(values) > 0 for values in by_episode.values())
    passed = bool(
        len(valid) >= 10
        and diffs
        and mean(diffs) > 0
        and challenger_capture > control_capture
        and positive_models >= 3
        and positive_episodes >= 2
    )
    return {
        "selected_challenger": selected,
        "valid_pairs": len(valid),
        "control_capture_count": control_capture,
        "challenger_capture_count": challenger_capture,
        "mean_paired_top5_alpha_improvement": mean(diffs) if diffs else None,
        "positive_models": positive_models,
        "positive_episodes": positive_episodes,
        "passes_confirmation_gate": passed,
    }


def mechanical_baselines(config: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        raw = common_market_rows(source_round(episode))
        outcome = load_outcomes(episode)
        active = [row for row in raw if not row["is_benchmark"]]
        rules = {
            "7d_continuation": sorted(active, key=lambda row: as_float(row["return_7d"]) or -999, reverse=True)[:5],
            "1y_reversal": sorted(active, key=lambda row: as_float(row["return_1y"]) or 999)[:5],
        }
        universe_mean = mean(outcome["active_returns"].values())
        rows.append(
            {
                "replay_id": episode["replay_id"],
                "baseline": "random_expectation",
                "top5_capture_probability": 5 / len(active),
                "top5_return": universe_mean,
                "top5_alpha": universe_mean - outcome["spy_return"],
            }
        )
        for name, selected in rules.items():
            ids = [str(row["option_id"]) for row in selected]
            selected_return = mean(outcome["returns"][option_id] for option_id in ids)
            rows.append(
                {
                    "replay_id": episode["replay_id"],
                    "baseline": name,
                    "top5_ids": ids,
                    "top5_capture": bool(set(ids) & set(outcome["winner_ids"])),
                    "top5_return": selected_return,
                    "top5_alpha": selected_return - outcome["spy_return"],
                }
            )
    return rows


def render_report(
    config: dict[str, Any],
    discovery_scored: Sequence[dict[str, Any]],
    discovery_aggregates: Sequence[dict[str, Any]],
    discovery_decision: dict[str, Any],
    confirmation_scored: Sequence[dict[str, Any]],
    confirmation_result: dict[str, Any] | None,
    usage: dict[str, Any],
) -> str:
    selected = discovery_decision.get("selected_challenger")
    if selected is None:
        bottom_line = (
            "No challenger passed the frozen discovery gate. The experiment stopped after discovery, so the historical replay does not support changing the V2.1 input or prompt."
        )
    elif confirmation_result and confirmation_result["passes_confirmation_gate"]:
        bottom_line = (
            f"{selected} passed both the discovery and confirmation gates. It is eligible for a future live weekly shadow test, but this retrospective result is not production evidence."
        )
    elif confirmation_result:
        bottom_line = (
            f"{selected} won discovery but failed the frozen confirmation gate. The replay does not support a live shadow test."
        )
    else:
        bottom_line = f"{selected} passed discovery; confirmation has not been scored."

    discovery_rows = [
        [
            row["challenger"],
            row["valid_pairs"],
            f"{row['challenger_capture_count']}/{row['control_capture_count']}",
            _pct_report(row["mean_paired_top5_alpha_improvement"]),
            row["positive_pair_count"],
            "Pass" if row["passes_discovery_gate"] else "Fail",
        ]
        for row in discovery_aggregates
    ]
    lines = [
        "# VNext Historical Replay Results",
        "",
        f"Generated at: `{datetime.now(timezone.utc).replace(microsecond=0).isoformat()}`",
        "",
        "Protocol: `docs/experiments/vnext-historical-replay-2026-07-20.md`",
        "",
        "## Bottom Line",
        "",
        bottom_line,
        "",
        "## Discovery",
        "",
        markdown_table(
            ["Treatment", "Valid pairs", "Winner captures challenger/control", "Top-5 alpha improvement", "Positive pairs", "Gate"],
            discovery_rows,
        ),
        "",
    ]
    if confirmation_result:
        lines.extend(
            [
                "## Confirmation",
                "",
                markdown_table(
                    ["Treatment", "Valid pairs", "Winner captures challenger/control", "Top-5 alpha improvement", "Positive models", "Positive episodes", "Gate"],
                    [[
                        confirmation_result["selected_challenger"],
                        confirmation_result["valid_pairs"],
                        f"{confirmation_result['challenger_capture_count']}/{confirmation_result['control_capture_count']}",
                        _pct_report(confirmation_result["mean_paired_top5_alpha_improvement"]),
                        confirmation_result["positive_models"],
                        confirmation_result["positive_episodes"],
                        "Pass" if confirmation_result["passes_confirmation_gate"] else "Fail",
                    ]],
                ),
                "",
            ]
        )
    lines.extend(
        [
            "## Execution",
            "",
            f"- Provider calls: {usage['calls']}",
            f"- Valid responses: {usage['valid_calls']}",
            f"- Input tokens: {usage['input_tokens']:,}",
            f"- Output tokens: {usage['output_tokens']:,}",
            f"- Reported reasoning tokens: {usage['reasoning_tokens']:,}",
            f"- Total provider latency: {usage['latency_seconds']:.1f} seconds",
            "",
            "## Interpretation",
            "",
            "This is a retrospective screening test. Dates and setup identifiers were reduced, tools and search were disabled, and packets were frozen before outcomes were loaded. Current models may still possess historical knowledge, so even a passing treatment requires a genuinely prospective live shadow test.",
            "",
            "The experiment measures candidate discovery, not final portfolio construction. Top-five returns are equal-weight diagnostics and are not official CapitalBench portfolio results.",
            "",
        ]
    )
    return "\n".join(lines)


def score_final(config_path: Path, report_copy: Path) -> None:
    config = load_yaml(config_path)
    output = experiment_output(config)
    if not (output / "discovery_decision.json").exists():
        discovery_decision = score_discovery(config_path)
    else:
        discovery_decision = json.loads((output / "discovery_decision.json").read_text(encoding="utf-8"))
    discovery_scored = score_phase(config, "discovery")
    discovery_pairs = paired_rows(discovery_scored)
    discovery_aggregates = aggregate_pairs(discovery_pairs)
    selected = discovery_decision.get("selected_challenger")

    confirmation_scored: list[dict[str, Any]] = []
    confirmation_result: dict[str, Any] | None = None
    if selected and load_records(config, "confirmation"):
        confirmation_scored = score_phase(config, "confirmation")
        confirmation_pairs = paired_rows(confirmation_scored, str(selected))
        confirmation_result = confirmation_gate(confirmation_pairs, str(selected))
        write_csv(output / "confirmation_call_metrics.csv", confirmation_scored)
        write_csv(output / "confirmation_pairs.csv", confirmation_pairs)
        write_json(output / "confirmation_decision.json", confirmation_result)

    all_records = load_records(config, "discovery") + load_records(config, "confirmation")
    usage = usage_summary(all_records)
    baselines = mechanical_baselines(config)
    write_csv(output / "mechanical_baselines.csv", baselines)
    report = render_report(
        config,
        discovery_scored,
        discovery_aggregates,
        discovery_decision,
        confirmation_scored,
        confirmation_result,
        usage,
    )
    (output / "report.md").write_text(report, encoding="utf-8", newline="\n")
    report_copy.parent.mkdir(parents=True, exist_ok=True)
    report_copy.write_text(report, encoding="utf-8", newline="\n")
    print(report)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=("prepare", "run-discovery", "score-discovery", "run-confirmation", "score-final"),
    )
    parser.add_argument("--experiment", type=Path, default=DEFAULT_EXPERIMENT)
    parser.add_argument("--report-copy", type=Path, default=DEFAULT_REPORT_COPY)
    args = parser.parse_args()
    config_path = args.experiment.resolve()
    if args.command == "prepare":
        prepare(config_path)
    elif args.command == "run-discovery":
        run_calls(config_path, "discovery")
    elif args.command == "score-discovery":
        score_discovery(config_path)
    elif args.command == "run-confirmation":
        run_calls(config_path, "confirmation")
    elif args.command == "score-final":
        score_final(config_path, args.report_copy.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

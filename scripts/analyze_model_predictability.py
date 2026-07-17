#!/usr/bin/env python3
"""Audit whether frozen CapitalBench V1 inputs predict subsequent winners.

The analysis is deliberately retrospective but cutoff-safe: features come only
from frozen model-facing artifacts, while realized prices are outcomes. It does
not edit round artifacts, publish results, or alter the active V2 experiment.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from statistics import mean, median
from typing import Any, Callable, Sequence

import numpy as np
import yaml


ROUND_ID_RE = re.compile(r"^CB-\d{4}-\d{2}-\d{2}-1(?P<track>[WM])$")
RESEARCH_CUTOFF_RE = re.compile(
    r"Research cutoff:\s*`?(?P<cutoff>\d{4}-\d{2}-\d{2}T[^\s`]+)",
    re.IGNORECASE,
)

TRAILING_RETURN_FIELDS = (
    "return_7d",
    "return_30d",
    "return_6m",
    "return_1y",
)
BENCHMARK_RELATIVE_FIELDS = (
    "return_vs_sp500_7d",
    "return_vs_sp500_30d",
    "return_vs_sp500_6m",
    "return_vs_sp500_1y",
)
PATH_RISK_FIELDS = (
    "volatility_30d",
    "max_drawdown_30d",
    "up_day_share_30d",
    "distance_from_52w_high",
    "distance_from_52w_low",
    "corr_to_sp500_1y",
    "beta_to_sp500_1y",
)
MECHANICAL_FIELDS = TRAILING_RETURN_FIELDS + BENCHMARK_RELATIVE_FIELDS + PATH_RISK_FIELDS

RISK_SCORE = {
    "cash": 0.0,
    "low": 20.0,
    "medium": 50.0,
    "high": 75.0,
    "very_high": 90.0,
}

RIDGE_FEATURES = (
    "return_7d",
    "return_30d",
    "return_6m",
    "return_1y",
    "volatility_30d",
    "max_drawdown_30d",
    "up_day_share_30d",
    "distance_from_52w_high",
    "distance_from_52w_low",
    "corr_to_sp500_1y",
    "beta_to_sp500_1y",
    "position_in_52w_range",
    "risk_score",
    "briefing_mentions",
    "mean_allocation_pct",
    "model_breadth",
    "rationale_mention_rate",
)

RIDGE_ALPHA = 10.0
MIN_WALK_FORWARD_ROUNDS = 8
BOOTSTRAP_REPLICATES = 2000
BOOTSTRAP_SEED = 20260717


@dataclass(frozen=True)
class OfficialRun:
    run_id: str
    path: Path
    manifest: dict[str, Any]


@dataclass
class ModelRecord:
    model_id: str
    allocation: dict[str, float]
    text: str
    portfolio_return: float | None
    alpha_vs_sp500: float | None


@dataclass
class RoundRecord:
    round_id: str
    track: str
    decision_date: date
    entry_date: date
    exit_date: date
    decision_deadline: datetime | None
    run_id: str
    assets: list[dict[str, Any]]
    models: list[ModelRecord]
    sp500_return: float
    oracle_return: float
    winner_ids: tuple[str, ...]
    split: str = ""
    prior_purged_rounds: int = 0


@dataclass(frozen=True)
class SignalSpec:
    name: str
    scorer: Callable[[dict[str, Any]], float | None]
    family: str


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Sequence[dict[str, Any]], fieldnames: Sequence[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8", newline="\n")
        return
    columns = list(fieldnames or rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            clean: dict[str, Any] = {}
            for key in columns:
                value = row.get(key)
                if isinstance(value, float):
                    clean[key] = "" if not math.isfinite(value) else f"{value:.10f}"
                elif isinstance(value, (date, datetime)):
                    clean[key] = value.isoformat()
                elif isinstance(value, (dict, list, tuple)):
                    clean[key] = json.dumps(value, sort_keys=True)
                elif value is None:
                    clean[key] = ""
                else:
                    clean[key] = value
            writer.writerow(clean)


def as_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def first_float(*values: Any) -> float | None:
    for value in values:
        parsed = as_float(value)
        if parsed is not None:
            return parsed
    return None


def parse_date(value: Any) -> date:
    return date.fromisoformat(str(value)[:10])


def parse_datetime(value: Any) -> datetime | None:
    if not value:
        return None
    text = str(value).strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def choose_official_run(round_dir: Path) -> tuple[OfficialRun | None, str]:
    matches: list[OfficialRun] = []
    for path in sorted(round_dir.glob("runs/*/run_manifest.yaml")):
        manifest = load_yaml(path)
        if (
            manifest.get("run_type") == "official"
            and manifest.get("mock") is False
            and manifest.get("operator_selected_official") is True
        ):
            matches.append(OfficialRun(path.parent.name, path.parent, manifest))
    if not matches:
        return None, "no_selected_official_run"
    if len(matches) > 1:
        return None, "multiple_selected_official_runs"
    return matches[0], ""


def eligibility(round_dir: Path) -> tuple[OfficialRun | None, dict[str, Any]]:
    row: dict[str, Any] = {
        "round_id": round_dir.name,
        "eligible": False,
        "reason": "",
        "track": "",
        "run_id": "",
    }
    match = ROUND_ID_RE.fullmatch(round_dir.name)
    if not match:
        row["reason"] = "non_v1_round_id"
        return None, row
    row["track"] = "weekly" if match.group("track") == "W" else "monthly"

    manifest_path = round_dir / "manifest.yaml"
    required_round_files = (
        manifest_path,
        round_dir / "prompt.md",
        round_dir / "briefing.md",
        round_dir / "options.yaml",
        round_dir / "market_data" / "universe_trailing_returns.csv",
    )
    missing = [path.name for path in required_round_files if not path.exists()]
    if missing:
        row["reason"] = "missing_frozen_input:" + ",".join(missing)
        return None, row

    manifest = load_yaml(manifest_path)
    methodology = str(manifest.get("methodology_version") or "").strip()
    if methodology and methodology != "portfolio-v1.0":
        row["reason"] = f"non_v1_methodology:{methodology}"
        return None, row

    run, reason = choose_official_run(round_dir)
    if run is None:
        row["reason"] = reason
        return None, row
    row["run_id"] = run.run_id
    if not run.manifest.get("resolved_at_utc"):
        row["reason"] = "unresolved"
        return None, row
    if run.manifest.get("official_score_eligible") is False:
        row["reason"] = "not_official_score_eligible"
        return None, row

    required_results = tuple(run.path / "results" / name for name in ("returns.csv", "leaderboard.csv", "allocations.csv"))
    missing_results = [path.name for path in required_results if not path.exists()]
    if missing_results:
        row["reason"] = "missing_final_result:" + ",".join(missing_results)
        return None, row
    parsed_dir = run.path / "submissions" / "parsed"
    if not parsed_dir.exists() or not any(parsed_dir.glob("*.json")):
        row["reason"] = "missing_parsed_submissions"
        return None, row

    row["eligible"] = True
    row["reason"] = "eligible"
    return run, row


def option_aliases(option: dict[str, Any]) -> tuple[list[str], list[str]]:
    insensitive: set[str] = set()
    sensitive: set[str] = set()
    option_id = str(option.get("id") or "").strip()
    name = str(option.get("name") or "").strip()
    symbol = str(option.get("symbol") or "").strip()

    if option_id:
        spaced = option_id.replace("_", " ").lower()
        if len(spaced) >= 4:
            insensitive.add(spaced)
    if name and len(name) >= 4:
        insensitive.add(name.lower())
        simplified = re.sub(r"\b(sector|equities|equity|etf|index|fund)\b", "", name.lower())
        simplified = re.sub(r"\s+", " ", simplified).strip()
        if len(simplified) >= 5:
            insensitive.add(simplified)
    if len(symbol) >= 3:
        sensitive.add(symbol.upper())
    return sorted(insensitive, key=len, reverse=True), sorted(sensitive, key=len, reverse=True)


def mention_count(text: str, option: dict[str, Any]) -> int:
    insensitive, sensitive = option_aliases(option)
    lower = text.lower()
    counts = [len(re.findall(rf"(?<!\w){re.escape(alias)}(?!\w)", lower)) for alias in insensitive]
    counts.extend(len(re.findall(rf"(?<![A-Z0-9]){re.escape(alias)}(?![A-Z0-9])", text)) for alias in sensitive)
    return max(counts, default=0)


def submission_text(payload: dict[str, Any]) -> str:
    pieces: list[str] = []
    for key in ("rationale_summary", "portfolio_rationale"):
        if payload.get(key):
            pieces.append(str(payload[key]))
    for value in payload.get("key_risks", []) or []:
        if value:
            pieces.append(str(value))
    for holding in payload.get("portfolio", []) or []:
        if isinstance(holding, dict) and holding.get("rationale"):
            pieces.append(str(holding["rationale"]))
    return " ".join(pieces)


def parse_submission(path: Path, leaderboard: dict[str, dict[str, str]]) -> ModelRecord:
    payload = json.loads(path.read_text(encoding="utf-8"))
    model_id = str(payload.get("model_id") or path.stem)
    if isinstance(payload.get("portfolio"), list):
        allocation = {
            str(item.get("option_id")): float(item.get("allocation_pct") or 0.0)
            for item in payload["portfolio"]
            if isinstance(item, dict) and item.get("option_id")
        }
    elif payload.get("selected_option_id"):
        allocation = {str(payload["selected_option_id"]): 100.0}
    else:
        allocation = {}
    score = leaderboard.get(model_id, {})
    portfolio_return = first_float(score.get("portfolio_return"), score.get("selected_asset_return"))
    return ModelRecord(
        model_id=model_id,
        allocation=allocation,
        text=submission_text(payload),
        portfolio_return=portfolio_return,
        alpha_vs_sp500=as_float(score.get("alpha_vs_sp500")),
    )


def percentile_ranks(values: Sequence[float | None]) -> list[float | None]:
    indexed = [(index, value) for index, value in enumerate(values) if value is not None and math.isfinite(value)]
    if not indexed:
        return [None] * len(values)
    ordered = sorted(indexed, key=lambda item: item[1])
    output: list[float | None] = [None] * len(values)
    denominator = max(len(ordered) - 1, 1)
    cursor = 0
    while cursor < len(ordered):
        end = cursor + 1
        while end < len(ordered) and ordered[end][1] == ordered[cursor][1]:
            end += 1
        average_position = (cursor + end - 1) / 2.0
        percentile = average_position / denominator if len(ordered) > 1 else 0.5
        for original_index, _value in ordered[cursor:end]:
            output[original_index] = percentile
        cursor = end
    return output


def pearson(left: Sequence[float], right: Sequence[float]) -> float | None:
    if len(left) < 3 or len(left) != len(right):
        return None
    left_mean = mean(left)
    right_mean = mean(right)
    numerator = sum((a - left_mean) * (b - right_mean) for a, b in zip(left, right))
    left_ss = sum((a - left_mean) ** 2 for a in left)
    right_ss = sum((b - right_mean) ** 2 for b in right)
    if left_ss <= 0.0 or right_ss <= 0.0:
        return None
    return numerator / math.sqrt(left_ss * right_ss)


def spearman(left: Sequence[float], right: Sequence[float]) -> float | None:
    left_ranks = percentile_ranks(left)
    right_ranks = percentile_ranks(right)
    pairs = [(a, b) for a, b in zip(left_ranks, right_ranks) if a is not None and b is not None]
    return pearson([item[0] for item in pairs], [item[1] for item in pairs]) if pairs else None


def position_in_52w_range(distance_high: float | None, distance_low: float | None) -> float | None:
    if distance_high is None or distance_low is None:
        return None
    high_multiple = 1.0 / (1.0 + distance_high) if 1.0 + distance_high > 0.0 else None
    low_multiple = 1.0 / (1.0 + distance_low) if 1.0 + distance_low > 0.0 else None
    if high_multiple is None or low_multiple is None or high_multiple <= low_multiple:
        return None
    return (1.0 - low_multiple) / (high_multiple - low_multiple)


def load_options(round_dir: Path) -> list[dict[str, Any]]:
    payload = load_yaml(round_dir / "options.yaml")
    return [item for item in payload.get("options", []) if isinstance(item, dict) and item.get("id")]


def boolean(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes"}


def build_round(
    round_dir: Path,
    run: OfficialRun,
) -> tuple[RoundRecord, list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    manifest = load_yaml(round_dir / "manifest.yaml")
    decision_date = parse_date(manifest.get("decision_date"))
    entry_date = parse_date(manifest.get("entry_date") or decision_date)
    exit_date = parse_date(manifest.get("exit_date"))
    decision_deadline = parse_datetime(manifest.get("decision_deadline"))
    track = "weekly" if round_dir.name.endswith("1W") else "monthly"

    options = load_options(round_dir)
    options_by_id = {str(item["id"]): item for item in options}
    market_rows = read_csv(round_dir / "market_data" / "universe_trailing_returns.csv")
    market_by_id = {str(row.get("option_id")): row for row in market_rows if row.get("option_id")}
    return_rows = read_csv(run.path / "results" / "returns.csv")
    returns_by_id = {str(row.get("option_id")): row for row in return_rows if row.get("option_id")}
    leaderboard_rows = read_csv(run.path / "results" / "leaderboard.csv")
    leaderboard = {str(row.get("model_id")): row for row in leaderboard_rows if row.get("model_id")}
    parsed_paths = sorted((run.path / "submissions" / "parsed").glob("*.json"))
    models = [parse_submission(path, leaderboard) for path in parsed_paths]
    briefing_text = (round_dir / "briefing.md").read_text(encoding="utf-8")

    option_return_errors: list[float] = []
    for row in return_rows:
        entry_price = as_float(row.get("entry_price"))
        exit_price = as_float(row.get("exit_price"))
        reported_return = as_float(row.get("return"))
        if entry_price is None or exit_price is None or reported_return is None or entry_price == 0.0:
            continue
        option_return_errors.append(abs((exit_price / entry_price - 1.0) - reported_return))

    assets: list[dict[str, Any]] = []
    for option in options:
        option_id = str(option["id"])
        outcome = returns_by_id.get(option_id)
        if outcome is None:
            continue
        context = market_by_id.get(option_id, {})
        allocations = [model.allocation.get(option_id, 0.0) for model in models]
        rationale_mentions = [mention_count(model.text, option) for model in models]
        distance_high = as_float(context.get("distance_from_52w_high"))
        distance_low = as_float(context.get("distance_from_52w_low"))
        row: dict[str, Any] = {
            "round_id": round_dir.name,
            "track": track,
            "decision_date": decision_date,
            "entry_date": entry_date,
            "exit_date": exit_date,
            "run_id": run.run_id,
            "option_id": option_id,
            "symbol": option.get("symbol") or outcome.get("asset_symbol") or "",
            "name": option.get("name") or outcome.get("label") or option_id,
            "asset_class": option.get("asset_class") or "",
            "category": option.get("category") or "",
            "option_group": option.get("option_group") or "",
            "risk_bucket": option.get("risk_bucket") or context.get("risk_bucket") or "",
            "risk_score": RISK_SCORE.get(str(option.get("risk_bucket") or context.get("risk_bucket") or ""), 50.0),
            "is_cash": bool(option.get("is_cash")) or boolean(outcome.get("is_cash")),
            "is_benchmark": bool(option.get("is_benchmark")) or boolean(outcome.get("is_benchmark")),
            "future_return": as_float(outcome.get("return")),
            "future_rank": as_float(outcome.get("rank")),
            "briefing_mentions": float(mention_count(briefing_text, option)),
            "models_holding": sum(1 for value in allocations if value > 0.0),
            "model_breadth": sum(1 for value in allocations if value > 0.0) / len(models) if models else 0.0,
            "mean_allocation_pct": mean(allocations) if allocations else 0.0,
            "median_allocation_pct": median(allocations) if allocations else 0.0,
            "max_allocation_pct": max(allocations, default=0.0),
            "rationale_mentions": sum(1 for value in rationale_mentions if value > 0),
            "rationale_mention_rate": sum(1 for value in rationale_mentions if value > 0) / len(models) if models else 0.0,
            "position_in_52w_range": position_in_52w_range(distance_high, distance_low),
        }
        for field in MECHANICAL_FIELDS:
            row[field] = as_float(context.get(field))
        assets.append(row)

    if not assets:
        raise ValueError(f"{round_dir.name} has no scored options")
    if any(row["future_return"] is None for row in assets):
        missing = [row["option_id"] for row in assets if row["future_return"] is None]
        raise ValueError(f"{round_dir.name} has missing realized returns: {missing}")

    ranked_fields = tuple(
        dict.fromkeys(
            MECHANICAL_FIELDS
            + (
                "position_in_52w_range",
                "risk_score",
                "briefing_mentions",
                "mean_allocation_pct",
                "model_breadth",
                "rationale_mention_rate",
                "future_return",
            )
        )
    )
    risky_assets = [row for row in assets if not row["is_cash"]]
    for field in ranked_fields:
        ranks = percentile_ranks([as_float(row.get(field)) for row in risky_assets])
        for row, rank in zip(risky_assets, ranks):
            row[f"rank_{field}"] = rank
        for row in assets:
            if row["is_cash"]:
                row[f"rank_{field}"] = None

    benchmark_rows = [row for row in assets if row["is_benchmark"] or row["option_id"] == "SP500"]
    if len(benchmark_rows) != 1:
        raise ValueError(f"{round_dir.name} must have exactly one S&P 500 benchmark row")
    sp500_return = float(benchmark_rows[0]["future_return"])
    oracle_return = max(float(row["future_return"]) for row in risky_assets)
    winner_ids = tuple(
        sorted(row["option_id"] for row in risky_assets if math.isclose(float(row["future_return"]), oracle_return))
    )
    top3_ids = {
        row["option_id"]
        for row in sorted(risky_assets, key=lambda item: float(item["future_return"]), reverse=True)[:3]
    }

    model_rows: list[dict[str, Any]] = []
    portfolio_return_errors: list[float] = []
    allocation_total_errors: list[float] = []
    for model in models:
        allocation_total_errors.append(abs(sum(model.allocation.values()) - 100.0))
        recomputed_return = sum(
            weight / 100.0 * float(returns_by_id[option_id]["return"])
            for option_id, weight in model.allocation.items()
            if option_id in returns_by_id and as_float(returns_by_id[option_id].get("return")) is not None
        )
        if model.portfolio_return is not None:
            portfolio_return_errors.append(abs(recomputed_return - model.portfolio_return))
        winner_allocation = sum(model.allocation.get(option_id, 0.0) for option_id in winner_ids)
        top3_allocation = sum(model.allocation.get(option_id, 0.0) for option_id in top3_ids)
        model_rows.append(
            {
                "round_id": round_dir.name,
                "track": track,
                "decision_date": decision_date,
                "model_id": model.model_id,
                "portfolio_return": model.portfolio_return,
                "sp500_return": sp500_return,
                "alpha_vs_sp500": model.alpha_vs_sp500,
                "beats_sp500": (
                    model.portfolio_return > sp500_return if model.portfolio_return is not None else None
                ),
                "oracle_regret": (
                    oracle_return - model.portfolio_return if model.portfolio_return is not None else None
                ),
                "winner_allocation_pct": winner_allocation,
                "top3_allocation_pct": top3_allocation,
                "holding_count": len(model.allocation),
            }
        )

    winner = next(row for row in risky_assets if row["option_id"] == winner_ids[0])
    strong_mechanical = any(
        (winner.get(f"rank_{field}") or 0.0) >= 0.8 for field in TRAILING_RETURN_FIELDS
    )
    if winner["models_holding"] == 0:
        trace_label = "signal_ignored" if strong_mechanical or winner["briefing_mentions"] > 0 else "signal_absent"
    elif winner["mean_allocation_pct"] < 15.0:
        trace_label = "recognized_underweighted"
    else:
        trace_label = "recognized"

    best_model = max(
        (row for row in model_rows if row["portfolio_return"] is not None),
        key=lambda item: float(item["portfolio_return"]),
        default=None,
    )
    winner_trace: dict[str, Any] = {
        "round_id": round_dir.name,
        "track": track,
        "decision_date": decision_date,
        "winner_option_id": winner["option_id"],
        "winner_symbol": winner["symbol"],
        "winner_name": winner["name"],
        "winner_return": winner["future_return"],
        "sp500_return": sp500_return,
        "oracle_alpha_vs_sp500": oracle_return - sp500_return,
        "briefing_mentions": winner["briefing_mentions"],
        "models_holding_winner": winner["models_holding"],
        "model_count": len(models),
        "mean_winner_allocation_pct": winner["mean_allocation_pct"],
        "max_winner_allocation_pct": winner["max_allocation_pct"],
        "best_model_id": best_model["model_id"] if best_model else "",
        "best_model_return": best_model["portfolio_return"] if best_model else None,
        "best_model_winner_allocation_pct": (
            next(
                (
                    row["winner_allocation_pct"]
                    for row in model_rows
                    if best_model and row["model_id"] == best_model["model_id"]
                ),
                None,
            )
        ),
        "trace_label": trace_label,
    }
    for field in TRAILING_RETURN_FIELDS:
        winner_trace[f"winner_{field}"] = winner.get(field)
        winner_trace[f"winner_rank_{field}"] = winner.get(f"rank_{field}")

    market_dates = [
        parse_date(row["as_of_price_date"])
        for row in market_rows
        if row.get("as_of_price_date")
        and not bool(options_by_id.get(str(row.get("option_id")), {}).get("is_cash"))
    ]
    future_market_dates = [item for item in market_dates if item > entry_date]
    briefing_match = RESEARCH_CUTOFF_RE.search(briefing_text)
    briefing_cutoff = parse_datetime(briefing_match.group("cutoff")) if briefing_match else None
    accepted_at = parse_datetime(run.manifest.get("accepted_at_utc"))
    completed_at = parse_datetime(run.manifest.get("completed_at_utc"))
    leakage_findings: list[str] = []
    timing_warnings: list[str] = []
    max_option_return_error = max(option_return_errors, default=0.0)
    max_portfolio_return_error = max(portfolio_return_errors, default=0.0)
    max_allocation_total_error = max(allocation_total_errors, default=0.0)
    if max_option_return_error > 1e-9:
        leakage_findings.append("option_return_reconciliation_failed")
    if max_portfolio_return_error > 1e-9:
        leakage_findings.append("portfolio_return_reconciliation_failed")
    if max_allocation_total_error > 1e-6:
        leakage_findings.append("allocation_total_reconciliation_failed")
    expected_models = run.manifest.get("valid_submissions")
    if expected_models is not None and int(expected_models) != len(models):
        leakage_findings.append("parsed_submission_count_mismatch")
    if future_market_dates:
        leakage_findings.append("market_context_after_entry")
    if briefing_cutoff and decision_deadline and briefing_cutoff > decision_deadline:
        leakage_findings.append("briefing_cutoff_after_deadline")
    if completed_at and completed_at.date() > exit_date:
        leakage_findings.append("official_run_completed_after_exit_date")
    elif completed_at and decision_deadline and completed_at > decision_deadline:
        timing_warnings.append("official_run_completed_after_deadline")
    forbidden_headers = {
        key
        for key in (market_rows[0].keys() if market_rows else [])
        if re.search(r"(^|_)(future|exit|realized|forward)(_|$)", key, re.IGNORECASE)
    }
    if forbidden_headers:
        leakage_findings.append("future_field_in_market_context:" + ",".join(sorted(forbidden_headers)))
    leakage_row = {
        "round_id": round_dir.name,
        "track": track,
        "decision_deadline": decision_deadline.isoformat() if decision_deadline else "",
        "briefing_cutoff": briefing_cutoff.isoformat() if briefing_cutoff else "",
        "entry_date": entry_date,
        "latest_market_price_date": max(market_dates) if market_dates else None,
        "completed_at": completed_at.isoformat() if completed_at else "",
        "accepted_at": accepted_at.isoformat() if accepted_at else "",
        "status": "fail" if leakage_findings else ("warn" if timing_warnings else "pass"),
        "findings": ";".join(leakage_findings),
        "warnings": ";".join(timing_warnings),
        "max_option_return_error": max_option_return_error,
        "max_portfolio_return_error": max_portfolio_return_error,
        "max_allocation_total_error": max_allocation_total_error,
    }
    round_summary = {
        "round_id": round_dir.name,
        "track": track,
        "decision_date": decision_date,
        "entry_date": entry_date,
        "exit_date": exit_date,
        "run_id": run.run_id,
        "option_count": len(assets),
        "risky_option_count": len(risky_assets),
        "model_count": len(models),
        "sp500_return": sp500_return,
        "oracle_return": oracle_return,
        "oracle_alpha_vs_sp500": oracle_return - sp500_return,
        "winner_ids": ";".join(winner_ids),
        "market_context_sha256": file_sha256(round_dir / "market_data" / "universe_trailing_returns.csv"),
        "briefing_sha256": file_sha256(round_dir / "briefing.md"),
        "available_mechanical_fields": ";".join(
            field for field in MECHANICAL_FIELDS if any(row.get(field) is not None for row in assets)
        ),
    }
    record = RoundRecord(
        round_id=round_dir.name,
        track=track,
        decision_date=decision_date,
        entry_date=entry_date,
        exit_date=exit_date,
        decision_deadline=decision_deadline,
        run_id=run.run_id,
        assets=assets,
        models=models,
        sp500_return=sp500_return,
        oracle_return=oracle_return,
        winner_ids=winner_ids,
    )
    return record, assets, model_rows, winner_trace, {**round_summary, **{f"audit_{k}": v for k, v in leakage_row.items()}}


def build_dataset(
    rounds_dir: Path,
) -> tuple[
    list[RoundRecord],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    rounds: list[RoundRecord] = []
    asset_rows: list[dict[str, Any]] = []
    model_rows: list[dict[str, Any]] = []
    winner_traces: list[dict[str, Any]] = []
    eligibility_rows: list[dict[str, Any]] = []
    round_summaries: list[dict[str, Any]] = []

    for round_dir in sorted(path for path in rounds_dir.glob("CB-*") if path.is_dir()):
        run, eligibility_row = eligibility(round_dir)
        eligibility_rows.append(eligibility_row)
        if run is None:
            continue
        record, assets, models, trace, summary = build_round(round_dir, run)
        if summary.get("audit_status") == "fail":
            eligibility_row["eligible"] = False
            eligibility_row["reason"] = "leakage_audit_failed:" + str(summary.get("audit_findings") or "")
            continue
        rounds.append(record)
        asset_rows.extend(assets)
        model_rows.extend(models)
        winner_traces.append(trace)
        round_summaries.append(summary)

    rounds.sort(key=lambda item: (item.track, item.decision_date, item.round_id))
    for track in ("weekly", "monthly"):
        track_rounds = sorted((item for item in rounds if item.track == track), key=lambda item: (item.decision_date, item.round_id))
        discovery_count = max(1, min(len(track_rounds) - 1, int(len(track_rounds) * 0.7))) if len(track_rounds) > 1 else len(track_rounds)
        for index, record in enumerate(track_rounds):
            record.split = "discovery" if index < discovery_count else "holdout"
            record.prior_purged_rounds = sum(1 for prior in track_rounds[:index] if prior.exit_date < record.entry_date)
            for row in record.assets:
                row["split"] = record.split
                row["prior_purged_rounds"] = record.prior_purged_rounds
    split_by_round = {item.round_id: (item.split, item.prior_purged_rounds) for item in rounds}
    for rows in (model_rows, winner_traces, round_summaries):
        for row in rows:
            split, prior = split_by_round[row["round_id"]]
            row["split"] = split
            row["prior_purged_rounds"] = prior

    return rounds, asset_rows, model_rows, winner_traces, eligibility_rows, round_summaries


def average_available(row: dict[str, Any], fields: Sequence[str]) -> float | None:
    values = [as_float(row.get(field)) for field in fields]
    present = [value for value in values if value is not None]
    return mean(present) if present else None


def signal_specs() -> list[SignalSpec]:
    specs = [SignalSpec("random_expectation", lambda _row: 0.0, "baseline")]
    for field in TRAILING_RETURN_FIELDS:
        specs.append(SignalSpec(f"{field}_continuation", lambda row, key=field: as_float(row.get(f"rank_{key}")), "mechanical"))
        specs.append(
            SignalSpec(
                f"{field}_reversal",
                lambda row, key=field: (
                    1.0 - float(row[f"rank_{key}"]) if row.get(f"rank_{key}") is not None else None
                ),
                "mechanical",
            )
        )
    specs.extend(
        [
            SignalSpec(
                "short_horizon_momentum",
                lambda row: average_available(row, ("rank_return_7d", "rank_return_30d")),
                "composite",
            ),
            SignalSpec(
                "medium_horizon_momentum",
                lambda row: average_available(row, ("rank_return_6m", "rank_return_1y")),
                "composite",
            ),
            SignalSpec(
                "model_consensus_allocation",
                lambda row: as_float(row.get("rank_mean_allocation_pct")),
                "model_evidence",
            ),
            SignalSpec(
                "model_consensus_breadth",
                lambda row: as_float(row.get("rank_model_breadth")),
                "model_evidence",
            ),
            SignalSpec(
                "briefing_salience",
                lambda row: as_float(row.get("rank_briefing_mentions")),
                "text_evidence",
            ),
            SignalSpec(
                "rationale_salience",
                lambda row: as_float(row.get("rank_rationale_mention_rate")),
                "model_evidence",
            ),
            SignalSpec(
                "sp500_only",
                lambda row: 1.0 if row.get("option_id") == "SP500" else 0.0,
                "baseline",
            ),
        ]
    )
    return specs


def selection_probabilities(scores: Sequence[float], count: int) -> list[float]:
    if count <= 0:
        return [0.0] * len(scores)
    count = min(count, len(scores))
    grouped: dict[float, list[int]] = defaultdict(list)
    for index, score in enumerate(scores):
        grouped[score].append(index)
    probabilities = [0.0] * len(scores)
    remaining = float(count)
    for score in sorted(grouped, reverse=True):
        members = grouped[score]
        if remaining <= 0.0:
            break
        probability = min(1.0, remaining / len(members))
        for index in members:
            probabilities[index] = probability
        remaining -= probability * len(members)
    return probabilities


def evaluate_scores(
    round_record: RoundRecord,
    signal_name: str,
    signal_family: str,
    score_by_option: dict[str, float | None],
) -> dict[str, Any] | None:
    assets = [row for row in round_record.assets if not row["is_cash"]]
    pairs = [(row, score_by_option.get(row["option_id"])) for row in assets]
    present = [(row, float(score)) for row, score in pairs if score is not None and math.isfinite(float(score))]
    if len(present) < max(3, math.ceil(len(assets) * 0.9)):
        return None
    if not all(any(row["option_id"] == winner for row, _score in present) for winner in round_record.winner_ids):
        return None

    rows = [row for row, _score in present]
    scores = [score for _row, score in present]
    returns = [float(row["future_return"]) for row in rows]
    top1_probability = selection_probabilities(scores, 1)
    top3_probability = selection_probabilities(scores, 3)
    top5_probability = selection_probabilities(scores, 5)
    winner_indexes = [index for index, row in enumerate(rows) if row["option_id"] in round_record.winner_ids]
    signal_ranks = percentile_ranks(scores)
    top1_return = sum(probability * value for probability, value in zip(top1_probability, returns))
    top3_return = sum(probability * value for probability, value in zip(top3_probability, returns)) / 3.0

    return {
        "round_id": round_record.round_id,
        "track": round_record.track,
        "decision_date": round_record.decision_date,
        "split": round_record.split,
        "prior_purged_rounds": round_record.prior_purged_rounds,
        "walk_forward_window": round_record.prior_purged_rounds >= MIN_WALK_FORWARD_ROUNDS,
        "signal": signal_name,
        "signal_family": signal_family,
        "option_count": len(rows),
        "rank_ic": spearman(scores, returns),
        "exact_winner_hit": max(top1_probability[index] for index in winner_indexes),
        "top3_capture": max(top3_probability[index] for index in winner_indexes),
        "top5_capture": max(top5_probability[index] for index in winner_indexes),
        "winner_signal_percentile": max(float(signal_ranks[index]) for index in winner_indexes if signal_ranks[index] is not None),
        "top1_return": top1_return,
        "top3_return": top3_return,
        "sp500_return": round_record.sp500_return,
        "oracle_return": round_record.oracle_return,
        "top1_alpha_vs_sp500": top1_return - round_record.sp500_return,
        "top3_alpha_vs_sp500": top3_return - round_record.sp500_return,
        "top1_oracle_regret": round_record.oracle_return - top1_return,
        "top3_oracle_regret": round_record.oracle_return - top3_return,
        "top3_beats_sp500": top3_return > round_record.sp500_return,
    }


def evaluate_predefined_signals(rounds: Sequence[RoundRecord]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for round_record in rounds:
        for spec in signal_specs():
            scores = {row["option_id"]: spec.scorer(row) for row in round_record.assets if not row["is_cash"]}
            metric = evaluate_scores(round_record, spec.name, spec.family, scores)
            if metric is not None:
                output.append(metric)
    return output


def ridge_feature_names() -> list[str]:
    names: list[str] = []
    for feature in RIDGE_FEATURES:
        names.extend((feature, f"{feature}_available"))
    return names


def ridge_vector(asset: dict[str, Any]) -> list[float]:
    values: list[float] = []
    for feature in RIDGE_FEATURES:
        rank = as_float(asset.get(f"rank_{feature}"))
        values.append(rank if rank is not None else 0.5)
        values.append(1.0 if rank is not None else 0.0)
    return values


def fit_ridge(rounds: Sequence[RoundRecord]) -> dict[str, Any]:
    x_rows: list[list[float]] = []
    y_values: list[float] = []
    weights: list[float] = []
    for round_record in rounds:
        assets = [row for row in round_record.assets if not row["is_cash"]]
        if not assets:
            continue
        round_weight = 1.0 / len(assets)
        for asset in assets:
            target = as_float(asset.get("rank_future_return"))
            if target is None:
                continue
            x_rows.append(ridge_vector(asset))
            y_values.append(target)
            weights.append(round_weight)
    if not x_rows:
        raise ValueError("ridge training set is empty")

    x = np.asarray(x_rows, dtype=float)
    y = np.asarray(y_values, dtype=float)
    sample_weights = np.asarray(weights, dtype=float)
    weight_sum = float(sample_weights.sum())
    feature_means = np.sum(x * sample_weights[:, None], axis=0) / weight_sum
    centered = x - feature_means
    feature_variances = np.sum((centered**2) * sample_weights[:, None], axis=0) / weight_sum
    feature_scales = np.sqrt(feature_variances)
    feature_scales[feature_scales < 1e-9] = 1.0
    standardized = centered / feature_scales
    design = np.column_stack([np.ones(len(standardized)), standardized])
    root_weights = np.sqrt(sample_weights)
    weighted_design = design * root_weights[:, None]
    weighted_target = y * root_weights
    penalty = np.eye(design.shape[1]) * RIDGE_ALPHA
    penalty[0, 0] = 0.0
    coefficients = np.linalg.solve(weighted_design.T @ weighted_design + penalty, weighted_design.T @ weighted_target)
    return {
        "feature_names": ridge_feature_names(),
        "feature_means": feature_means,
        "feature_scales": feature_scales,
        "coefficients": coefficients,
        "training_rows": len(x_rows),
        "training_rounds": len(rounds),
    }


def predict_ridge(model: dict[str, Any], asset: dict[str, Any]) -> float:
    vector = np.asarray(ridge_vector(asset), dtype=float)
    standardized = (vector - model["feature_means"]) / model["feature_scales"]
    return float(model["coefficients"][0] + standardized @ model["coefficients"][1:])


def ridge_coefficient_rows(
    model: dict[str, Any],
    track: str,
    test_round_id: str,
    mode: str,
) -> list[dict[str, Any]]:
    rows = [
        {
            "track": track,
            "test_round_id": test_round_id,
            "mode": mode,
            "training_rounds": model["training_rounds"],
            "training_rows": model["training_rows"],
            "feature": "intercept",
            "coefficient": float(model["coefficients"][0]),
        }
    ]
    for name, coefficient in zip(model["feature_names"], model["coefficients"][1:]):
        rows.append(
            {
                "track": track,
                "test_round_id": test_round_id,
                "mode": mode,
                "training_rounds": model["training_rounds"],
                "training_rows": model["training_rows"],
                "feature": name,
                "coefficient": float(coefficient),
            }
        )
    return rows


def purged_training_rounds(
    candidates: Sequence[RoundRecord],
    test_round: RoundRecord,
) -> list[RoundRecord]:
    return [
        item
        for item in candidates
        if item.decision_date < test_round.decision_date and item.exit_date < test_round.entry_date
    ]


def evaluate_ridge(
    rounds: Sequence[RoundRecord],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    metrics: list[dict[str, Any]] = []
    predictions: list[dict[str, Any]] = []
    coefficients: list[dict[str, Any]] = []

    for track in ("weekly", "monthly"):
        ordered = sorted((item for item in rounds if item.track == track), key=lambda item: (item.decision_date, item.round_id))
        discovery = [item for item in ordered if item.split == "discovery"]
        holdout = [item for item in ordered if item.split == "holdout"]

        for test_round in ordered:
            training = purged_training_rounds(ordered, test_round)
            if len(training) < MIN_WALK_FORWARD_ROUNDS:
                continue
            model = fit_ridge(training)
            score_map: dict[str, float] = {}
            for asset in test_round.assets:
                if asset["is_cash"]:
                    continue
                score = predict_ridge(model, asset)
                score_map[asset["option_id"]] = score
                predictions.append(
                    {
                        "mode": "purged_walk_forward",
                        "track": track,
                        "test_round_id": test_round.round_id,
                        "training_rounds": len(training),
                        "latest_training_exit": max(item.exit_date for item in training),
                        "test_entry_date": test_round.entry_date,
                        "option_id": asset["option_id"],
                        "predicted_rank_score": score,
                        "future_return": asset["future_return"],
                    }
                )
            metric = evaluate_scores(
                test_round,
                "ridge_purged_walk_forward",
                "learned_ranker",
                score_map,
            )
            if metric is not None:
                metrics.append(metric)
            coefficients.extend(ridge_coefficient_rows(model, track, test_round.round_id, "purged_walk_forward"))

        for test_round in holdout:
            training = purged_training_rounds(discovery, test_round)
            if len(training) < MIN_WALK_FORWARD_ROUNDS:
                continue
            model = fit_ridge(training)
            score_map = {
                asset["option_id"]: predict_ridge(model, asset)
                for asset in test_round.assets
                if not asset["is_cash"]
            }
            for asset in test_round.assets:
                if asset["is_cash"]:
                    continue
                predictions.append(
                    {
                        "mode": "locked_holdout",
                        "track": track,
                        "test_round_id": test_round.round_id,
                        "training_rounds": len(training),
                        "latest_training_exit": max(item.exit_date for item in training),
                        "test_entry_date": test_round.entry_date,
                        "option_id": asset["option_id"],
                        "predicted_rank_score": score_map[asset["option_id"]],
                        "future_return": asset["future_return"],
                    }
                )
            metric = evaluate_scores(
                test_round,
                "ridge_locked_holdout",
                "learned_ranker",
                score_map,
            )
            if metric is not None:
                metrics.append(metric)
            coefficients.extend(ridge_coefficient_rows(model, track, test_round.round_id, "locked_holdout"))
    return metrics, predictions, coefficients


def nonnull_mean(rows: Sequence[dict[str, Any]], key: str) -> float | None:
    values = [as_float(row.get(key)) for row in rows]
    present = [value for value in values if value is not None]
    return mean(present) if present else None


def nonnull_median(rows: Sequence[dict[str, Any]], key: str) -> float | None:
    values = [as_float(row.get(key)) for row in rows]
    present = [value for value in values if value is not None]
    return median(present) if present else None


def quantile(values: Sequence[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def moving_block_ci(
    rows: Sequence[dict[str, Any]],
    key: str,
    block_length: int,
    seed_key: str,
) -> tuple[float | None, float | None]:
    ordered_rows = sorted(rows, key=lambda item: (str(item.get("decision_date")), str(item.get("round_id"))))
    values = [as_float(row.get(key)) for row in ordered_rows]
    series = [value for value in values if value is not None]
    if len(series) < 4:
        return None, None
    block = max(1, min(block_length, len(series)))
    seed = BOOTSTRAP_SEED + int(hashlib.sha256(seed_key.encode("utf-8")).hexdigest()[:8], 16)
    rng = random.Random(seed)
    estimates: list[float] = []
    for _replicate in range(BOOTSTRAP_REPLICATES):
        sample: list[float] = []
        while len(sample) < len(series):
            start = rng.randrange(len(series))
            sample.extend(series[(start + offset) % len(series)] for offset in range(block))
        estimates.append(mean(sample[: len(series)]))
    return quantile(estimates, 0.025), quantile(estimates, 0.975)


def aggregate_signal_metrics(round_metrics: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in round_metrics:
        grouped[(str(row["track"]), str(row["signal"]), str(row["signal_family"]))].append(row)
    output: list[dict[str, Any]] = []
    for (track, signal, family), rows in sorted(grouped.items()):
        subsets = {
            "all": list(rows),
            "discovery": [row for row in rows if row.get("split") == "discovery"],
            "holdout": [row for row in rows if row.get("split") == "holdout"],
            "walk_forward_window": [row for row in rows if row.get("walk_forward_window")],
        }
        for split, subset in subsets.items():
            if not subset:
                continue
            block_length = 5 if track == "weekly" else 10
            ic_low, ic_high = moving_block_ci(subset, "rank_ic", block_length, f"{track}:{signal}:{split}:ic")
            alpha_low, alpha_high = moving_block_ci(
                subset,
                "top3_alpha_vs_sp500",
                block_length,
                f"{track}:{signal}:{split}:alpha",
            )
            alpha_rows = [row for row in subset if as_float(row.get("top3_alpha_vs_sp500")) is not None]
            leave_best_out = None
            if len(alpha_rows) >= 2:
                best = max(alpha_rows, key=lambda item: float(item["top3_alpha_vs_sp500"]))
                leave_best_out = mean(
                    float(item["top3_alpha_vs_sp500"])
                    for item in alpha_rows
                    if item is not best
                )
            output.append(
                {
                    "track": track,
                    "signal": signal,
                    "signal_family": family,
                    "split": split,
                    "rounds": len(subset),
                    "mean_rank_ic": nonnull_mean(subset, "rank_ic"),
                    "median_rank_ic": nonnull_median(subset, "rank_ic"),
                    "rank_ic_ci_low": ic_low,
                    "rank_ic_ci_high": ic_high,
                    "exact_winner_hit_rate": nonnull_mean(subset, "exact_winner_hit"),
                    "top3_capture_rate": nonnull_mean(subset, "top3_capture"),
                    "top5_capture_rate": nonnull_mean(subset, "top5_capture"),
                    "mean_winner_signal_percentile": nonnull_mean(subset, "winner_signal_percentile"),
                    "mean_top1_return": nonnull_mean(subset, "top1_return"),
                    "mean_top3_return": nonnull_mean(subset, "top3_return"),
                    "mean_sp500_return": nonnull_mean(subset, "sp500_return"),
                    "mean_top1_alpha_vs_sp500": nonnull_mean(subset, "top1_alpha_vs_sp500"),
                    "mean_top3_alpha_vs_sp500": nonnull_mean(subset, "top3_alpha_vs_sp500"),
                    "top3_alpha_ci_low": alpha_low,
                    "top3_alpha_ci_high": alpha_high,
                    "top3_beat_sp500_rate": nonnull_mean(subset, "top3_beats_sp500"),
                    "mean_top1_oracle_regret": nonnull_mean(subset, "top1_oracle_regret"),
                    "mean_top3_oracle_regret": nonnull_mean(subset, "top3_oracle_regret"),
                    "leave_best_round_out_top3_alpha": leave_best_out,
                }
            )
    return output


def aggregate_model_metrics(model_rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in model_rows:
        grouped[(str(row["track"]), str(row["model_id"]))].append(row)
    output: list[dict[str, Any]] = []
    for (track, model_id), rows in sorted(grouped.items()):
        for split, subset in (
            ("all", rows),
            ("discovery", [row for row in rows if row.get("split") == "discovery"]),
            ("holdout", [row for row in rows if row.get("split") == "holdout"]),
        ):
            if not subset:
                continue
            output.append(
                {
                    "track": track,
                    "model_id": model_id,
                    "split": split,
                    "rounds": len(subset),
                    "mean_portfolio_return": nonnull_mean(subset, "portfolio_return"),
                    "mean_sp500_return": nonnull_mean(subset, "sp500_return"),
                    "mean_alpha_vs_sp500": nonnull_mean(subset, "alpha_vs_sp500"),
                    "beat_sp500_rate": nonnull_mean(subset, "beats_sp500"),
                    "mean_oracle_regret": nonnull_mean(subset, "oracle_regret"),
                    "mean_winner_allocation_pct": nonnull_mean(subset, "winner_allocation_pct"),
                    "mean_top3_allocation_pct": nonnull_mean(subset, "top3_allocation_pct"),
                }
            )
    return output


def actionability_decisions(signal_metrics: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    index = {
        (str(row["track"]), str(row["signal"]), str(row["split"])): row
        for row in signal_metrics
    }
    candidates = sorted(
        {
            (str(row["track"]), str(row["signal"]), str(row["signal_family"]))
            for row in signal_metrics
            if row.get("signal_family") not in {"baseline"}
            and row.get("signal") not in {"ridge_locked_holdout"}
        }
    )
    output: list[dict[str, Any]] = []
    for track, signal, family in candidates:
        discovery = index.get((track, signal, "discovery"))
        holdout = index.get((track, signal, "holdout"))
        walk_forward = index.get((track, signal, "walk_forward_window"))
        conditions = {
            "positive_discovery_ic": bool(discovery and (discovery.get("mean_rank_ic") or 0.0) > 0.0),
            "positive_holdout_ic": bool(holdout and (holdout.get("mean_rank_ic") or 0.0) > 0.0),
            "positive_walk_forward_alpha": bool(
                walk_forward and (walk_forward.get("mean_top3_alpha_vs_sp500") or 0.0) > 0.0
            ),
            "walk_forward_beat_rate_above_half": bool(
                walk_forward and (walk_forward.get("top3_beat_sp500_rate") or 0.0) > 0.5
            ),
            "positive_leave_best_out_alpha": bool(
                walk_forward and (walk_forward.get("leave_best_round_out_top3_alpha") or 0.0) > 0.0
            ),
            "minimum_holdout_rounds": bool(holdout and int(holdout.get("rounds") or 0) >= 3),
            "minimum_walk_forward_rounds": bool(walk_forward and int(walk_forward.get("rounds") or 0) >= 3),
        }
        output.append(
            {
                "track": track,
                "signal": signal,
                "signal_family": family,
                **conditions,
                "passes_all": all(conditions.values()),
                "holdout_rounds": holdout.get("rounds") if holdout else 0,
                "holdout_mean_rank_ic": holdout.get("mean_rank_ic") if holdout else None,
                "walk_forward_rounds": walk_forward.get("rounds") if walk_forward else 0,
                "walk_forward_mean_top3_alpha": (
                    walk_forward.get("mean_top3_alpha_vs_sp500") if walk_forward else None
                ),
                "walk_forward_beat_rate": walk_forward.get("top3_beat_sp500_rate") if walk_forward else None,
                "leave_best_round_out_alpha": (
                    walk_forward.get("leave_best_round_out_top3_alpha") if walk_forward else None
                ),
            }
        )
    return output


def format_pct(value: Any, digits: int = 2) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.{digits}f}%"


def format_number(value: Any, digits: int = 3) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed:.{digits}f}"


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _header in headers) + " |",
    ]
    for row in rows:
        values = [str(value).replace("|", "\\|").replace("\n", " ") for value in row]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def signal_metric_index(signal_metrics: Sequence[dict[str, Any]]) -> dict[tuple[str, str, str], dict[str, Any]]:
    return {
        (str(row["track"]), str(row["signal"]), str(row["split"])): row
        for row in signal_metrics
    }


def feature_coverage(rounds: Sequence[RoundRecord]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for track in ("weekly", "monthly"):
        track_rounds = [item for item in rounds if item.track == track]
        for field in MECHANICAL_FIELDS + ("position_in_52w_range",):
            covered = sum(
                1
                for item in track_rounds
                if any(row.get(field) is not None for row in item.assets if not row["is_cash"])
            )
            output.append(
                {
                    "track": track,
                    "feature": field,
                    "rounds_available": covered,
                    "rounds_total": len(track_rounds),
                    "coverage_rate": covered / len(track_rounds) if track_rounds else None,
                }
            )
    return output


def relative_rank_redundancy(rounds: Sequence[RoundRecord]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    pairs = zip(TRAILING_RETURN_FIELDS, BENCHMARK_RELATIVE_FIELDS)
    for raw_field, relative_field in pairs:
        comparable = 0
        identical = 0
        for round_record in rounds:
            pairs_in_round = [
                (row.get(f"rank_{raw_field}"), row.get(f"rank_{relative_field}"))
                for row in round_record.assets
                if not row["is_cash"]
                and row.get(f"rank_{raw_field}") is not None
                and row.get(f"rank_{relative_field}") is not None
            ]
            if not pairs_in_round:
                continue
            comparable += 1
            if all(math.isclose(float(left), float(right), abs_tol=1e-12) for left, right in pairs_in_round):
                identical += 1
        output.append(
            {
                "raw_feature": raw_field,
                "relative_feature": relative_field,
                "comparable_rounds": comparable,
                "identical_rank_rounds": identical,
                "identical_rate": identical / comparable if comparable else None,
            }
        )
    return output


def report_signal_rows(
    signal_metrics: Sequence[dict[str, Any]],
    track: str,
    split: str,
    limit: int = 6,
) -> list[dict[str, Any]]:
    rows = [
        row
        for row in signal_metrics
        if row["track"] == track
        and row["split"] == split
        and row["signal_family"] not in {"baseline", "learned_ranker"}
    ]
    def sort_value(value: Any) -> float:
        parsed = as_float(value)
        return parsed if parsed is not None else -999.0

    rows.sort(
        key=lambda item: (
            -sort_value(item.get("mean_top3_alpha_vs_sp500")),
            -sort_value(item.get("mean_rank_ic")),
        )
    )
    return rows[:limit]


def write_report(
    path: Path,
    rounds: Sequence[RoundRecord],
    round_summaries: Sequence[dict[str, Any]],
    asset_rows: Sequence[dict[str, Any]],
    model_rows: Sequence[dict[str, Any]],
    winner_traces: Sequence[dict[str, Any]],
    eligibility_rows: Sequence[dict[str, Any]],
    signal_metrics: Sequence[dict[str, Any]],
    model_metrics: Sequence[dict[str, Any]],
    decisions: Sequence[dict[str, Any]],
    coverage_rows: Sequence[dict[str, Any]],
    redundancy_rows: Sequence[dict[str, Any]],
) -> None:
    generated_at = datetime.now().astimezone().replace(microsecond=0).isoformat()
    metric_index = signal_metric_index(signal_metrics)
    eligible_count = sum(1 for row in eligibility_rows if row.get("eligible"))
    excluded_reasons = Counter(str(row.get("reason")) for row in eligibility_rows if not row.get("eligible"))
    failed_audits = [row for row in eligibility_rows if str(row.get("reason", "")).startswith("leakage_audit_failed")]
    timing_warning_count = sum(1 for row in round_summaries if row.get("audit_status") == "warn")

    track_rows: list[list[Any]] = []
    for track in ("weekly", "monthly"):
        items = sorted((item for item in rounds if item.track == track), key=lambda item: item.decision_date)
        discovery = sum(1 for item in items if item.split == "discovery")
        holdout = sum(1 for item in items if item.split == "holdout")
        wf = sum(1 for item in items if item.prior_purged_rounds >= MIN_WALK_FORWARD_ROUNDS)
        track_rows.append(
            [
                track.title(),
                len(items),
                items[0].decision_date if items else "n/a",
                items[-1].decision_date if items else "n/a",
                discovery,
                holdout,
                wf,
            ]
        )

    model_summary_rows: list[list[Any]] = []
    for track in ("weekly", "monthly"):
        rows = [row for row in model_rows if row["track"] == track]
        traces = [row for row in winner_traces if row["track"] == track]
        model_summary_rows.append(
            [
                track.title(),
                len(rows),
                format_pct(nonnull_mean(rows, "portfolio_return")),
                format_pct(nonnull_mean(rows, "sp500_return")),
                format_pct(nonnull_mean(rows, "alpha_vs_sp500")),
                format_pct(nonnull_mean(rows, "beats_sp500"), 1),
                f"{nonnull_mean(rows, 'winner_allocation_pct') or 0.0:.1f}%",
                format_pct(nonnull_mean(traces, "oracle_alpha_vs_sp500")),
            ]
        )

    trace_counts: dict[str, Counter[str]] = {}
    for track in ("weekly", "monthly"):
        trace_counts[track] = Counter(
            str(row["trace_label"]) for row in winner_traces if row["track"] == track
        )
    trace_table = [
        [
            label.replace("_", " ").title(),
            trace_counts["weekly"].get(label, 0),
            trace_counts["monthly"].get(label, 0),
        ]
        for label in ("signal_absent", "signal_ignored", "recognized_underweighted", "recognized")
    ]

    signal_sections: list[str] = []
    for track in ("weekly", "monthly"):
        holdout_rows = report_signal_rows(signal_metrics, track, "holdout")
        wf_rows = report_signal_rows(signal_metrics, track, "walk_forward_window")
        signal_sections.extend(
            [
                f"### {track.title()}",
                "",
                "Best predefined candidates in the locked holdout:",
                "",
                markdown_table(
                    ["Signal", "Rounds", "Rank IC", "Top-3 alpha", "Beat S&P", "Winner pctile"],
                    [
                        [
                            row["signal"],
                            row["rounds"],
                            format_number(row["mean_rank_ic"]),
                            format_pct(row["mean_top3_alpha_vs_sp500"]),
                            format_pct(row["top3_beat_sp500_rate"], 1),
                            format_pct(row["mean_winner_signal_percentile"], 1),
                        ]
                        for row in holdout_rows
                    ],
                ),
                "",
                "The same candidate set on dates with at least eight fully resolved, non-overlapping prior rounds:",
                "",
                markdown_table(
                    ["Signal", "Rounds", "Rank IC", "Top-3 alpha", "95% interval", "Beat S&P", "Leave-best-out"],
                    [
                        [
                            row["signal"],
                            row["rounds"],
                            format_number(row["mean_rank_ic"]),
                            format_pct(row["mean_top3_alpha_vs_sp500"]),
                            f"{format_pct(row['top3_alpha_ci_low'])} to {format_pct(row['top3_alpha_ci_high'])}",
                            format_pct(row["top3_beat_sp500_rate"], 1),
                            format_pct(row["leave_best_round_out_top3_alpha"]),
                        ]
                        for row in wf_rows
                    ],
                ),
                "",
            ]
        )

    ridge_rows: list[list[Any]] = []
    for track in ("weekly", "monthly"):
        for signal, split in (
            ("ridge_locked_holdout", "holdout"),
            ("ridge_purged_walk_forward", "walk_forward_window"),
        ):
            row = metric_index.get((track, signal, split))
            ridge_rows.append(
                [
                    track.title(),
                    signal.replace("ridge_", "").replace("_", " "),
                    row["rounds"] if row else 0,
                    format_number(row.get("mean_rank_ic") if row else None),
                    format_pct(row.get("mean_top3_alpha_vs_sp500") if row else None),
                    format_pct(row.get("top3_beat_sp500_rate") if row else None, 1),
                ]
            )

    passing = [row for row in decisions if row.get("passes_all")]
    passing.sort(
        key=lambda item: -(
            as_float(item.get("walk_forward_mean_top3_alpha"))
            if as_float(item.get("walk_forward_mean_top3_alpha")) is not None
            else -999.0
        )
    )
    if passing:
        leader = passing[0]
        leader_walk_forward = metric_index.get((leader["track"], leader["signal"], "walk_forward_window"), {})
        leader_discovery = metric_index.get((leader["track"], leader["signal"], "discovery"), {})
        leader_all = metric_index.get((leader["track"], leader["signal"], "all"), {})
        recommendation = (
            f"The frozen rule identifies `{leader['signal']}` on the {leader['track']} track as eligible only for a "
            f"future shadow test. Its purged-window top-3 alpha was {format_pct(leader_walk_forward.get('mean_top3_alpha_vs_sp500'))}, "
            f"but the moving-block 95% interval was {format_pct(leader_walk_forward.get('top3_alpha_ci_low'))} to "
            f"{format_pct(leader_walk_forward.get('top3_alpha_ci_high'))}; discovery alpha was "
            f"{format_pct(leader_discovery.get('mean_top3_alpha_vs_sp500'))}, and full-history alpha was "
            f"{format_pct(leader_all.get('mean_top3_alpha_vs_sp500'))}. It captured the realized winner in its top "
            f"three {format_pct(leader_walk_forward.get('top3_capture_rate'), 1)} of the time and hit the exact winner "
            f"as its top choice {format_pct(leader_walk_forward.get('exact_winner_hit_rate'), 1)} of the time. That "
            "regime instability and limited winner precision are not enough to replace V1. The next evidence must "
            "be a frozen prospective shadow run with no additional paid model calls."
        )
    else:
        recommendation = (
            "No predefined signal passed every frozen actionability condition. The historical evidence therefore "
            "does not justify changing V1 or adding a paid challenger. Keep the analysis as a diagnostic and wait "
            "for genuinely prospective evidence."
        )

    dominant_trace = Counter(str(row["trace_label"]) for row in winner_traces).most_common(1)
    dominant_label = dominant_trace[0][0] if dominant_trace else "none"
    intervention = {
        "signal_absent": "The dominant failure is an input-information gap; richer cutoff-safe data is the first intervention to test.",
        "signal_ignored": "Most winners were mechanically salient under the broad trace rule but unallocated. Because most individual mechanical signals still failed out of sample, this is not proof that models ignored a reliable rule; it shows that the current inputs create many plausible candidates without separating the eventual winner.",
        "recognized_underweighted": "The dominant failure is allocation dilution; a precommitted concentration or confidence rule is the first intervention to test.",
        "recognized": "Models often recognized the winner, so the remaining gap is portfolio construction and competing-position error rather than simple omission.",
    }.get(dominant_label, "The winner traces do not support a single intervention.")

    coverage_table = []
    for field in TRAILING_RETURN_FIELDS + PATH_RISK_FIELDS:
        weekly = next((row for row in coverage_rows if row["track"] == "weekly" and row["feature"] == field), None)
        monthly = next((row for row in coverage_rows if row["track"] == "monthly" and row["feature"] == field), None)
        coverage_table.append(
            [
                field,
                f"{weekly['rounds_available']}/{weekly['rounds_total']}" if weekly else "n/a",
                f"{monthly['rounds_available']}/{monthly['rounds_total']}" if monthly else "n/a",
            ]
        )

    def model_alpha_sort(item: dict[str, Any]) -> tuple[str, float]:
        alpha = as_float(item.get("mean_alpha_vs_sp500"))
        return str(item["track"]), -(alpha if alpha is not None else -999.0)

    model_table_rows: list[list[Any]] = []
    for row in sorted((item for item in model_metrics if item["split"] == "all"), key=model_alpha_sort):
        model_table_rows.append(
            [
                str(row["track"]).title(),
                row["model_id"],
                row["rounds"],
                format_pct(row["mean_portfolio_return"]),
                format_pct(row["mean_alpha_vs_sp500"]),
                format_pct(row["beat_sp500_rate"], 1),
                f"{as_float(row.get('mean_winner_allocation_pct')) or 0.0:.1f}%",
                f"{as_float(row.get('mean_top3_allocation_pct')) or 0.0:.1f}%",
            ]
        )

    winner_counts = Counter((str(row["track"]), str(row["winner_option_id"])) for row in winner_traces)
    recurring_winner_rows = [
        [track.title(), option_id, count]
        for (track, option_id), count in sorted(
            winner_counts.items(),
            key=lambda item: (item[0][0], -item[1], item[0][1]),
        )
        if count > 1
    ]
    positive_full_models = sorted(
        f"{row['track']}:{row['model_id']}"
        for row in model_metrics
        if row["split"] == "all" and (as_float(row.get("mean_alpha_vs_sp500")) or 0.0) > 0.0
    )
    positive_holdout_models = sorted(
        f"{row['track']}:{row['model_id']}"
        for row in model_metrics
        if row["split"] == "holdout" and (as_float(row.get("mean_alpha_vs_sp500")) or 0.0) > 0.0
    )
    model_result_note = (
        "Full-history positive-alpha model/track pairs: "
        + (", ".join(f"`{item}`" for item in positive_full_models) if positive_full_models else "none")
        + ". Locked-holdout positive-alpha model/track pairs: "
        + (", ".join(f"`{item}`" for item in positive_holdout_models) if positive_holdout_models else "none")
        + "."
    )
    monthly_winner_counts = Counter(
        str(row["winner_option_id"]) for row in winner_traces if row["track"] == "monthly"
    )
    weekly_winner_counts = Counter(
        str(row["winner_option_id"]) for row in winner_traces if row["track"] == "weekly"
    )
    monthly_leader = monthly_winner_counts.most_common(1)
    weekly_clusters = ", ".join(
        f"{option_id} ({count})" for option_id, count in weekly_winner_counts.most_common(4)
    )
    episode_note = (
        f"These are overlapping observations, not independent victories. {monthly_leader[0][0]} accounts for "
        f"{monthly_leader[0][1]} of {sum(monthly_winner_counts.values())} monthly winners; the largest weekly "
        f"clusters are {weekly_clusters}. The effective number of market episodes is therefore much smaller than "
        f"{len(winner_traces)}."
        if monthly_leader
        else "These are overlapping observations, not independent victories."
    )

    report = [
        "# Can CapitalBench Inputs Predict The Winning Asset?",
        "",
        f"Generated at: `{generated_at}`",
        "",
        "Protocol: `docs/model_performance_predictability_protocol.md`",
        "",
        "## Bottom Line",
        "",
        recommendation,
        "",
        intervention,
        "",
        "The strongest target is not exact winner prediction by itself. With roughly seventy choices and a short, noisy horizon, top-3 capture, return versus S&P 500, and oracle regret are more stable diagnostics. Exact winner hits are still reported, but they are not allowed to drive the recommendation.",
        "",
        "## Data Used",
        "",
        f"The repository contained {len(eligibility_rows)} candidate round folders. {eligible_count} resolved V1 rounds passed the frozen eligibility and leakage rules, producing {len(asset_rows):,} round-asset observations and {len(model_rows):,} saved model decisions.",
        "",
        markdown_table(
            ["Track", "Rounds", "First", "Last", "Discovery", "Holdout", "Purged WF"],
            track_rows,
        ),
        "",
        "Excluded folders by reason:",
        "",
        markdown_table(
            ["Reason", "Count"],
            [[reason, count] for reason, count in sorted(excluded_reasons.items())],
        ),
        "",
        f"Leakage audit failures: {len(failed_audits)}. Timing warnings: {timing_warning_count}. Failed rounds, if any, were excluded; after-deadline operational completions that remained before the scoring exit were retained as warnings because their frozen closed-capability inputs did not contain future data.",
        "",
        "## Current Performance Gap",
        "",
        markdown_table(
            ["Track", "Model decisions", "Model return", "S&P 500", "Model alpha", "Beat rate", "Winner alloc", "Oracle alpha"],
            model_summary_rows,
        ),
        "",
        "`Oracle alpha` is the return of the best allowed risky option minus S&P 500. It shows that a winning answer existed; it does not show that the answer was knowable before the deadline.",
        "",
        "### Model-Level Results",
        "",
        markdown_table(
            ["Track", "Model", "Rounds", "Return", "Alpha", "Beat S&P", "Winner alloc", "Top-3 alloc"],
            model_table_rows,
        ),
        "",
        model_result_note,
        "",
        "## What Happened To The Winner?",
        "",
        markdown_table(["Trace", "Weekly rounds", "Monthly rounds"], trace_table),
        "",
        "A strong mechanical rank means the realized winner was already in the top 20% on at least one of four frozen trailing-return horizons. With four chances to qualify, `signal ignored` is a broad salience label, not evidence that a profitable signal was ignored. A briefing mention is exact ticker, option ID, or distinctive asset-name matching. These labels do not infer post-deadline news.",
        "",
        "### Repeated Winner Episodes",
        "",
        markdown_table(["Track", "Winning option", "Rounds"], recurring_winner_rows),
        "",
        episode_note,
        "",
        "## Frozen Signal Tests",
        "",
        "All signals are within-round percentile ranks. Tied scores use fractional selection probabilities, so a sparse mention signal cannot receive an artificial win from option ordering.",
        "",
        *signal_sections,
        "## Fixed Ridge Diagnostic",
        "",
        "The ridge ranker uses only preregistered mechanical, briefing-salience, and model-consensus fields. Its penalty is fixed at 10 and is never tuned on the holdout.",
        "",
        markdown_table(
            ["Track", "Evaluation", "Rounds", "Rank IC", "Top-3 alpha", "Beat S&P"],
            ridge_rows,
        ),
        "",
        "## Feature Coverage",
        "",
        markdown_table(["Feature", "Weekly", "Monthly"], coverage_table),
        "",
        "The benchmark-relative return columns are retained in the audit dataset but not duplicated in the ridge model. Subtracting the same S&P 500 return from every option in a round cannot change within-round ranks.",
        "",
        markdown_table(
            ["Raw", "Relative", "Comparable rounds", "Identical rank rounds"],
            [
                [row["raw_feature"], row["relative_feature"], row["comparable_rounds"], row["identical_rank_rounds"]]
                for row in redundancy_rows
            ],
        ),
        "",
        "## Interpretation",
        "",
        "1. In-sample winner stories are not sufficient. The decision table requires the same direction in discovery and holdout, positive top-3 alpha in a purged window, a majority beat rate, and a positive result after removing the best round.",
        "2. Overlapping rounds are not independent. The purged walk-forward fit uses only rounds whose exit precedes the next test entry, and moving-block bootstrap intervals are included in `signal_metrics.csv`.",
        "3. Model consensus is analyzed separately from individual portfolios. If consensus ranks well while portfolios do not, allocation construction is the likely bottleneck. If both fail, adding more portfolio rules will not manufacture information.",
        "4. The active July 13 V2 pilot remains untouched and excluded. Its July 20 frozen acceptance rule is the only rule that can accept or reject V2.",
        "",
        "## Recommended Next Step",
        "",
        recommendation,
        "",
        "Do not optimize the prompt around the historical best asset. If a shadow rule is tested, freeze its formula before the next decision, score it without another model API call, and require several non-overlapping observations before spending money on another paired model run.",
        "",
        "## Reproducibility",
        "",
        "Run:",
        "",
        "```bash",
        "python scripts/analyze_model_predictability.py --rounds-dir rounds --output output/model_performance_predictability --report-copy docs/model_performance_predictability_report.md",
        "```",
        "",
        "Machine-readable outputs include eligibility, leakage, asset-level data, winner traces, per-round signal metrics, aggregate signal metrics, model diagnostics, ridge predictions, coefficients, actionability decisions, and `summary.json`.",
        "",
        "## Method Notes",
        "",
        "The design follows the core warning from White's Reality Check that searching many strategies can produce a best-looking rule by chance, uses chronological prediction rather than random splits, and treats forecast combination as a diagnostic rather than proof. Primary references: [White (2000)](https://onlinelibrary.wiley.com/doi/10.1111/1468-0262.00152), [Harvey, Liu, and Zhu (2016)](https://www.nber.org/papers/w20592), [Gu, Kelly, and Xiu (2020)](https://www.nber.org/papers/w25398), and [Bates and Granger (1969)](https://www.tandfonline.com/doi/abs/10.1057/jors.1969.103).",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(report), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds-dir", type=Path, default=Path("rounds"))
    parser.add_argument("--output", type=Path, default=Path("output/model_performance_predictability"))
    parser.add_argument("--report-copy", type=Path)
    parser.add_argument(
        "--protocol",
        type=Path,
        default=Path("docs/model_performance_predictability_protocol.md"),
    )
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    rounds, asset_rows, model_rows, winner_traces, eligibility_rows, round_summaries = build_dataset(args.rounds_dir)
    if not rounds:
        raise SystemExit("no eligible resolved V1 rounds")

    predefined_round_metrics = evaluate_predefined_signals(rounds)
    ridge_round_metrics, ridge_predictions, ridge_coefficients = evaluate_ridge(rounds)
    signal_round_metrics = predefined_round_metrics + ridge_round_metrics
    signal_metrics = aggregate_signal_metrics(signal_round_metrics)
    model_metrics = aggregate_model_metrics(model_rows)
    decisions = actionability_decisions(signal_metrics)
    coverage_rows = feature_coverage(rounds)
    redundancy_rows = relative_rank_redundancy(rounds)

    leakage_rows = [
        {
            key.removeprefix("audit_"): value
            for key, value in row.items()
            if key.startswith("audit_")
        }
        for row in round_summaries
    ]
    write_csv(args.output / "eligibility.csv", eligibility_rows)
    write_csv(args.output / "leakage_audit.csv", leakage_rows)
    write_csv(args.output / "round_summary.csv", round_summaries)
    write_csv(args.output / "asset_dataset.csv", asset_rows)
    write_csv(args.output / "winner_traces.csv", winner_traces)
    write_csv(args.output / "model_round_metrics.csv", model_rows)
    write_csv(args.output / "model_metrics.csv", model_metrics)
    write_csv(args.output / "signal_round_metrics.csv", signal_round_metrics)
    write_csv(args.output / "signal_metrics.csv", signal_metrics)
    write_csv(args.output / "ridge_predictions.csv", ridge_predictions)
    write_csv(args.output / "ridge_coefficients.csv", ridge_coefficients)
    write_csv(args.output / "actionability_decisions.csv", decisions)
    write_csv(args.output / "feature_coverage.csv", coverage_rows)
    write_csv(args.output / "relative_rank_redundancy.csv", redundancy_rows)

    summary = {
        "generated_at": datetime.now().astimezone().replace(microsecond=0).isoformat(),
        "protocol_path": str(args.protocol),
        "protocol_sha256": file_sha256(args.protocol) if args.protocol.exists() else None,
        "script_sha256": file_sha256(Path(__file__)),
        "eligible_rounds": len(rounds),
        "weekly_rounds": sum(1 for item in rounds if item.track == "weekly"),
        "monthly_rounds": sum(1 for item in rounds if item.track == "monthly"),
        "asset_rows": len(asset_rows),
        "model_decisions": len(model_rows),
        "eligibility_exclusions": dict(
            Counter(str(row["reason"]) for row in eligibility_rows if not row.get("eligible"))
        ),
        "leakage_failures": [
            row for row in eligibility_rows if str(row.get("reason", "")).startswith("leakage_audit_failed")
        ],
        "timing_warnings": [row for row in leakage_rows if row.get("status") == "warn"],
        "passing_shadow_candidates": [row for row in decisions if row.get("passes_all")],
        "trace_labels": dict(Counter(str(row["trace_label"]) for row in winner_traces)),
        "ridge_alpha": RIDGE_ALPHA,
        "minimum_walk_forward_rounds": MIN_WALK_FORWARD_ROUNDS,
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
    }
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2, default=str),
        encoding="utf-8",
        newline="\n",
    )

    report_path = args.output / "report.md"
    write_report(
        report_path,
        rounds,
        round_summaries,
        asset_rows,
        model_rows,
        winner_traces,
        eligibility_rows,
        signal_metrics,
        model_metrics,
        decisions,
        coverage_rows,
        redundancy_rows,
    )
    if args.report_copy:
        args.report_copy.parent.mkdir(parents=True, exist_ok=True)
        args.report_copy.write_text(report_path.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")

    print(f"eligible_rounds={len(rounds)} weekly={summary['weekly_rounds']} monthly={summary['monthly_rounds']}")
    print(f"asset_rows={len(asset_rows)} model_decisions={len(model_rows)}")
    print(f"passing_shadow_candidates={len(summary['passing_shadow_candidates'])}")
    print(f"wrote analysis to {args.output}")
    if args.report_copy:
        print(f"wrote report copy to {args.report_copy}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

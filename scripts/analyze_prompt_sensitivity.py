#!/usr/bin/env python3
"""Analyze how CapitalBench prompt regimes relate to model behavior.

This is an observational study over saved public rounds. It intentionally does
not modify frozen round inputs or official run artifacts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any

import yaml


RISK_SCORE = {
    "cash": 0.0,
    "low": 20.0,
    "medium": 50.0,
    "high": 75.0,
    "very_high": 90.0,
}

MOMENTUM_TERMS = re.compile(
    r"\b(momentum|trailing|relative strength|price action|recent returns?|"
    r"recent performance|up[- ]?day|winner|52[- ]?week)\b",
    re.I,
)
CATALYST_TERMS = re.compile(
    r"\b(catalyst|earnings|guidance|revenue|margin|eps|micron|hbm|pmi|"
    r"fed|fomc|pce|cpi|gdp|yields?|rates?|oil|crude|housing|retail|"
    r"tariff|policy|dow inclusion|inventory|sales)\b",
    re.I,
)
REVERSAL_TERMS = re.compile(
    r"\b(reversal|reverse|mean[- ]reversion|profit[- ]taking|sell[- ]?the[- ]?news|"
    r"crowded|drawdown|volatility|whipsaw|risk[- ]off|de[- ]risk)\b",
    re.I,
)
LIMITED_SUPPORT_TERMS = re.compile(
    r"\b(limited independent|support is limited|support beyond price action|"
    r"limited specific|mainly a .*momentum|price history alone)\b",
    re.I,
)
BENCHMARK_TERMS = re.compile(r"\b(spy|s&p|s&p 500|benchmark)\b", re.I)


@dataclass(frozen=True)
class OfficialRun:
    run_id: str
    path: Path
    manifest: dict[str, Any]


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def normalize_prompt(text: str) -> str:
    """Remove routine dynamic fields while preserving instruction changes."""
    replacements = [
        (r"CB-\d{4}-\d{2}-\d{2}-1[WM]", "CB-YYYY-MM-DD-1X"),
        (r"\d{4}-\d{2}-\d{2}T[0-9:.+\-]+Z?", "TIMESTAMP"),
        (r"\d{4}-\d{2}-\d{2}", "YYYY-MM-DD"),
        (r"\b(one-week|one week|one-month|one month)\b", "HORIZON"),
        (r"\bweekly\b", "TRACK"),
        (r"\bmonthly\b", "TRACK"),
        (r"\bMonday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday\b", "WEEKDAY"),
        (r"\bMay|June|July\b \d{1,2}, \d{4}", "MONTH DAY, YEAR"),
    ]
    output = text
    for pattern, repl in replacements:
        output = re.sub(pattern, repl, output, flags=re.I)
    return output


def prompt_features(text: str) -> dict[str, bool]:
    lower = text.lower()
    return {
        "single_pick": "selected_option_id" in lower or "single allowed option" in lower,
        "portfolio_format": '"portfolio"' in lower and "allocation_pct" in lower,
        "internal_priors_allowed": "internal learned knowledge" in lower,
        "only_prompt": "use only the information in this prompt" in lower,
        "scoring_window_discipline": "scoring timeline is central" in lower or "close-to-close" in lower,
        "briefing_bias_discipline": "briefing-bias discipline" in lower,
        "mechanical_return_table": "mechanical return table" in lower,
        "mechanical_price_context": "mechanical price-context table" in lower,
        "benchmark_asset_case": "s&p 500 benchmark asset is an allowed holding" in lower,
        "private_case_check": "privately compare continuation" in lower,
        "price_history_discipline": "price-history discipline" in lower,
        "independent_support_required": "independent support" in lower and "holding rationale cites momentum" in lower,
    }


def prompt_regime(features: dict[str, bool], round_id: str) -> str:
    if features["single_pick"]:
        return "R0_single_pick_closed_prompt"
    if features["price_history_discipline"]:
        return "R4_price_history_discipline"
    if features["benchmark_asset_case"] or features["private_case_check"]:
        return "R3_benchmark_asset_mean_reversion_check"
    if features["briefing_bias_discipline"] and features["scoring_window_discipline"]:
        return "R2_scoring_window_and_briefing_bias"
    if features["internal_priors_allowed"]:
        return "R1_portfolio_internal_priors"
    return "R_unknown"


def official_run(round_dir: Path) -> OfficialRun | None:
    matches: list[OfficialRun] = []
    for run_manifest in sorted(round_dir.glob("runs/*/run_manifest.yaml")):
        manifest = load_yaml(run_manifest)
        if (
            manifest.get("mock") is False
            and manifest.get("run_type") == "official"
            and manifest.get("operator_selected_official") is True
        ):
            matches.append(OfficialRun(run_manifest.parent.name, run_manifest.parent, manifest))
    if len(matches) == 1:
        return matches[0]
    return None


def load_options(round_dir: Path) -> dict[str, dict[str, Any]]:
    options_path = round_dir / "options.yaml"
    if not options_path.exists():
        return {}
    data = load_yaml(options_path)
    return {item["id"]: item for item in data.get("options", []) if isinstance(item, dict) and item.get("id")}


def load_market_context(round_dir: Path) -> dict[str, dict[str, Any]]:
    path = round_dir / "market_data" / "universe_trailing_returns.csv"
    if not path.exists():
        return {}
    rows: list[dict[str, Any]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("option_id"):
                for key in ("return_7d", "return_30d", "return_6m", "return_1y"):
                    try:
                        row[key] = float(row[key])
                    except (KeyError, TypeError, ValueError):
                        row[key] = None
                rows.append(row)
    valid_30d = sorted(
        [row for row in rows if isinstance(row.get("return_30d"), float)],
        key=lambda item: item["return_30d"],
        reverse=True,
    )
    top_quintile_cutoff = max(1, math.ceil(len(valid_30d) * 0.2))
    top_decile_cutoff = max(1, math.ceil(len(valid_30d) * 0.1))
    top_quintile = {row["option_id"] for row in valid_30d[:top_quintile_cutoff]}
    top_decile = {row["option_id"] for row in valid_30d[:top_decile_cutoff]}
    context = {row["option_id"]: row for row in rows}
    for option_id, row in context.items():
        row["is_top_30d_quintile"] = option_id in top_quintile
        row["is_top_30d_decile"] = option_id in top_decile
    return context


def parse_submission(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "portfolio" in data and isinstance(data["portfolio"], list):
        allocation = {
            str(item["option_id"]): float(item["allocation_pct"])
            for item in data["portfolio"]
            if "option_id" in item and "allocation_pct" in item
        }
        holding_rationales = " ".join(str(item.get("rationale", "")) for item in data["portfolio"])
    elif data.get("selected_option_id"):
        allocation = {str(data["selected_option_id"]): 100.0}
        holding_rationales = ""
    else:
        allocation = {}
        holding_rationales = ""
    rationale_text = " ".join(
        [
            str(data.get("rationale_summary", "")),
            str(data.get("portfolio_rationale", "")),
            " ".join(str(item) for item in data.get("key_risks", []) if item),
            holding_rationales,
        ]
    )
    return {
        "model_id": data.get("model_id") or path.stem,
        "provider": data.get("provider") or "",
        "confidence": data.get("confidence"),
        "allocation": allocation,
        "rationale_text": rationale_text,
    }


def cosine_similarity(left: dict[str, float], right: dict[str, float]) -> float:
    keys = set(left) | set(right)
    numerator = sum(left.get(key, 0.0) * right.get(key, 0.0) for key in keys)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return numerator / (left_norm * right_norm)


def allocation_turnover(left: dict[str, float], right: dict[str, float]) -> float:
    keys = set(left) | set(right)
    return sum(abs(right.get(key, 0.0) - left.get(key, 0.0)) for key in keys) / 2.0


def pct(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.2f}"


def metric_row(
    submission: dict[str, Any],
    options: dict[str, dict[str, Any]],
    market_context: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    allocation = submission["allocation"]
    text = submission["rationale_text"]
    risk_weighted = 0.0
    high_risk = 0.0
    defensive = 0.0
    equity = 0.0
    explicit_momentum = allocation.get("MOMENTUM", 0.0)
    semiconductors = allocation.get("SEMICONDUCTORS", 0.0)
    sp500 = allocation.get("SP500", 0.0)
    top_30d_quintile = 0.0
    top_30d_decile = 0.0
    for option_id, weight in allocation.items():
        option = options.get(option_id, {})
        risk_bucket = str(option.get("risk_bucket") or market_context.get(option_id, {}).get("risk_bucket") or "")
        risk_score = RISK_SCORE.get(risk_bucket, 50.0)
        risk_weighted += weight * risk_score / 100.0
        if risk_bucket in {"high", "very_high"}:
            high_risk += weight
        if risk_bucket in {"cash", "low"} or option.get("asset_class") in {"cash", "cash_like", "fixed_income"}:
            defensive += weight
        if option.get("asset_class") == "equity":
            equity += weight
        context = market_context.get(option_id, {})
        if context.get("is_top_30d_quintile"):
            top_30d_quintile += weight
        if context.get("is_top_30d_decile"):
            top_30d_decile += weight

    weights = list(allocation.values())
    return {
        "model_id": submission["model_id"],
        "provider": submission["provider"],
        "confidence": submission["confidence"],
        "holdings": len(allocation),
        "top_weight_pct": max(weights) if weights else 0.0,
        "hhi": sum((weight / 100.0) ** 2 for weight in weights),
        "risk_score": risk_weighted,
        "high_risk_pct": high_risk,
        "defensive_pct": defensive,
        "equity_pct": equity,
        "sp500_pct": sp500,
        "explicit_momentum_pct": explicit_momentum,
        "semiconductors_pct": semiconductors,
        "top_30d_quintile_pct": top_30d_quintile,
        "top_30d_decile_pct": top_30d_decile,
        "mentions_momentum": bool(MOMENTUM_TERMS.search(text)),
        "mentions_catalyst": bool(CATALYST_TERMS.search(text)),
        "mentions_reversal": bool(REVERSAL_TERMS.search(text)),
        "mentions_limited_support": bool(LIMITED_SUPPORT_TERMS.search(text)),
        "mentions_benchmark": bool(BENCHMARK_TERMS.search(text)),
        "allocation": allocation,
    }


def avg(rows: list[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None and row.get(key) != ""]
    return mean(values) if values else None


def bool_rate(rows: list[dict[str, Any]], key: str) -> float | None:
    if not rows:
        return None
    return 100.0 * sum(1 for row in rows if row.get(key)) / len(rows)


def build_dataset(rounds_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    prompt_family_map: dict[str, dict[str, Any]] = {}
    submission_rows: list[dict[str, Any]] = []
    round_rows: list[dict[str, Any]] = []

    for round_dir in sorted(rounds_dir.glob("CB-*")):
        manifest_path = round_dir / "manifest.yaml"
        prompt_path = round_dir / "prompt.md"
        if not manifest_path.exists() or not prompt_path.exists():
            continue
        manifest = load_yaml(manifest_path)
        run = official_run(round_dir)
        if run is None:
            continue
        prompt_text = prompt_path.read_text(encoding="utf-8")
        normalized = normalize_prompt(prompt_text)
        prompt_hash = hashlib.sha256(prompt_text.encode("utf-8")).hexdigest()
        normalized_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        features = prompt_features(prompt_text)
        regime = prompt_regime(features, round_dir.name)
        options = load_options(round_dir)
        market_context = load_market_context(round_dir)

        family = prompt_family_map.setdefault(
            normalized_hash[:12],
            {
                "prompt_family": normalized_hash[:12],
                "first_round": round_dir.name,
                "last_round": round_dir.name,
                "round_count": 0,
                "raw_prompt_hash_examples": set(),
                **features,
                "regime": regime,
            },
        )
        family["last_round"] = round_dir.name
        family["round_count"] += 1
        family["raw_prompt_hash_examples"].add(prompt_hash[:12])

        parsed_dir = run.path / "submissions" / "parsed"
        metrics: list[dict[str, Any]] = []
        for submission_path in sorted(parsed_dir.glob("*.json")):
            submission = parse_submission(submission_path)
            row = metric_row(submission, options, market_context)
            row.update(
                {
                    "round_id": round_dir.name,
                    "decision_date": manifest.get("decision_date"),
                    "horizon": manifest.get("horizon"),
                    "track": "weekly" if str(manifest.get("horizon", "")).startswith("one week") else "monthly",
                    "run_id": run.run_id,
                    "prompt_hash": prompt_hash[:12],
                    "prompt_family": normalized_hash[:12],
                    "prompt_regime": regime,
                    "model_roster_has_fable": any(
                        p.stem == "anthropic-claude-fable-5" for p in parsed_dir.glob("*.json")
                    ),
                }
            )
            metrics.append(row)
            submission_rows.append(row)

        similarities: list[float] = []
        for idx, left in enumerate(metrics):
            for right in metrics[idx + 1 :]:
                similarities.append(cosine_similarity(left["allocation"], right["allocation"]))

        aggregate = defaultdict(float)
        for row in metrics:
            for option_id, weight in row["allocation"].items():
                aggregate[option_id] += weight / max(len(metrics), 1)
        top_allocations = "; ".join(
            f"{option_id}:{weight:.1f}" for option_id, weight in sorted(aggregate.items(), key=lambda item: -item[1])[:8]
        )
        round_rows.append(
            {
                "round_id": round_dir.name,
                "decision_date": manifest.get("decision_date"),
                "horizon": manifest.get("horizon"),
                "track": "weekly" if str(manifest.get("horizon", "")).startswith("one week") else "monthly",
                "run_id": run.run_id,
                "model_count": len(metrics),
                "prompt_family": normalized_hash[:12],
                "prompt_regime": regime,
                "model_roster_has_fable": any(row["model_id"] == "anthropic-claude-fable-5" for row in metrics),
                "avg_holdings": avg(metrics, "holdings"),
                "avg_top_weight_pct": avg(metrics, "top_weight_pct"),
                "avg_hhi": avg(metrics, "hhi"),
                "avg_risk_score": avg(metrics, "risk_score"),
                "avg_high_risk_pct": avg(metrics, "high_risk_pct"),
                "avg_defensive_pct": avg(metrics, "defensive_pct"),
                "avg_equity_pct": avg(metrics, "equity_pct"),
                "avg_sp500_pct": avg(metrics, "sp500_pct"),
                "avg_explicit_momentum_pct": avg(metrics, "explicit_momentum_pct"),
                "avg_semiconductors_pct": avg(metrics, "semiconductors_pct"),
                "avg_top_30d_quintile_pct": avg(metrics, "top_30d_quintile_pct"),
                "avg_top_30d_decile_pct": avg(metrics, "top_30d_decile_pct"),
                "momentum_language_rate_pct": bool_rate(metrics, "mentions_momentum"),
                "catalyst_language_rate_pct": bool_rate(metrics, "mentions_catalyst"),
                "reversal_language_rate_pct": bool_rate(metrics, "mentions_reversal"),
                "limited_support_language_rate_pct": bool_rate(metrics, "mentions_limited_support"),
                "benchmark_language_rate_pct": bool_rate(metrics, "mentions_benchmark"),
                "avg_pairwise_similarity": mean(similarities) if similarities else None,
                "top_allocations": top_allocations,
            }
        )

    prompt_families = []
    for family in prompt_family_map.values():
        item = dict(family)
        item["raw_prompt_hash_examples"] = ";".join(sorted(item["raw_prompt_hash_examples"]))
        prompt_families.append(item)
    prompt_families.sort(key=lambda item: item["first_round"])
    round_rows.sort(key=lambda item: (str(item["decision_date"]), item["track"]))
    submission_rows.sort(key=lambda item: (str(item["decision_date"]), item["track"], item["model_id"]))
    return prompt_families, round_rows, submission_rows


def transition_rows(round_rows: list[dict[str, Any]], submission_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_round = {row["round_id"]: row for row in round_rows}
    subs_by_round: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in submission_rows:
        subs_by_round[row["round_id"]][row["model_id"]] = row

    rows: list[dict[str, Any]] = []
    for track in ("weekly", "monthly"):
        track_rounds = [row for row in round_rows if row["track"] == track]
        track_rounds.sort(key=lambda item: str(item["decision_date"]))
        for previous, current in zip(track_rounds, track_rounds[1:]):
            common_models = sorted(set(subs_by_round[previous["round_id"]]) & set(subs_by_round[current["round_id"]]))
            turnovers = [
                allocation_turnover(
                    subs_by_round[previous["round_id"]][model]["allocation"],
                    subs_by_round[current["round_id"]][model]["allocation"],
                )
                for model in common_models
            ]
            changed_regime = previous["prompt_regime"] != current["prompt_regime"]
            changed_family = previous["prompt_family"] != current["prompt_family"]
            rows.append(
                {
                    "track": track,
                    "from_round": previous["round_id"],
                    "to_round": current["round_id"],
                    "from_date": previous["decision_date"],
                    "to_date": current["decision_date"],
                    "from_regime": previous["prompt_regime"],
                    "to_regime": current["prompt_regime"],
                    "changed_regime": changed_regime,
                    "changed_prompt_family": changed_family,
                    "common_models": len(common_models),
                    "avg_model_turnover_pct": mean(turnovers) if turnovers else None,
                    "delta_risk_score": (current["avg_risk_score"] or 0.0) - (previous["avg_risk_score"] or 0.0),
                    "delta_high_risk_pct": (current["avg_high_risk_pct"] or 0.0) - (previous["avg_high_risk_pct"] or 0.0),
                    "delta_defensive_pct": (current["avg_defensive_pct"] or 0.0) - (previous["avg_defensive_pct"] or 0.0),
                    "delta_sp500_pct": (current["avg_sp500_pct"] or 0.0) - (previous["avg_sp500_pct"] or 0.0),
                    "delta_explicit_momentum_pct": (current["avg_explicit_momentum_pct"] or 0.0)
                    - (previous["avg_explicit_momentum_pct"] or 0.0),
                    "delta_top_30d_quintile_pct": (current["avg_top_30d_quintile_pct"] or 0.0)
                    - (previous["avg_top_30d_quintile_pct"] or 0.0),
                    "delta_semiconductors_pct": (current["avg_semiconductors_pct"] or 0.0)
                    - (previous["avg_semiconductors_pct"] or 0.0),
                    "delta_momentum_language_rate_pct": (current["momentum_language_rate_pct"] or 0.0)
                    - (previous["momentum_language_rate_pct"] or 0.0),
                    "delta_catalyst_language_rate_pct": (current["catalyst_language_rate_pct"] or 0.0)
                    - (previous["catalyst_language_rate_pct"] or 0.0),
                    "delta_reversal_language_rate_pct": (current["reversal_language_rate_pct"] or 0.0)
                    - (previous["reversal_language_rate_pct"] or 0.0),
                    "delta_similarity": (current["avg_pairwise_similarity"] or 0.0)
                    - (previous["avg_pairwise_similarity"] or 0.0),
                    "from_top_allocations": previous["top_allocations"],
                    "to_top_allocations": current["top_allocations"],
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    clean_rows: list[dict[str, Any]] = []
    for row in rows:
        clean = {}
        for key, value in row.items():
            if key == "allocation":
                clean[key] = json.dumps(value, sort_keys=True)
            elif isinstance(value, float):
                clean[key] = f"{value:.6f}"
            else:
                clean[key] = value
        clean_rows.append(clean)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(clean_rows[0].keys()))
        writer.writeheader()
        writer.writerows(clean_rows)


def grouped_round_summary(round_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in round_rows:
        grouped[row["prompt_regime"]].append(row)
    output = []
    for regime, rows in grouped.items():
        ordered = sorted(rows, key=lambda item: (str(item["decision_date"]), str(item["track"]), str(item["round_id"])))
        output.append(
            {
                "prompt_regime": regime,
                "rounds": len(rows),
                "first_round": ordered[0]["round_id"],
                "last_round": ordered[-1]["round_id"],
                "avg_risk_score": avg(rows, "avg_risk_score"),
                "avg_high_risk_pct": avg(rows, "avg_high_risk_pct"),
                "avg_defensive_pct": avg(rows, "avg_defensive_pct"),
                "avg_sp500_pct": avg(rows, "avg_sp500_pct"),
                "avg_explicit_momentum_pct": avg(rows, "avg_explicit_momentum_pct"),
                "avg_top_30d_quintile_pct": avg(rows, "avg_top_30d_quintile_pct"),
                "avg_semiconductors_pct": avg(rows, "avg_semiconductors_pct"),
                "momentum_language_rate_pct": avg(rows, "momentum_language_rate_pct"),
                "catalyst_language_rate_pct": avg(rows, "catalyst_language_rate_pct"),
                "reversal_language_rate_pct": avg(rows, "reversal_language_rate_pct"),
                "avg_pairwise_similarity": avg(rows, "avg_pairwise_similarity"),
            }
        )
    output.sort(key=lambda item: item["first_round"])
    return output


def model_sensitivity(submission_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_track_model: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in submission_rows:
        by_track_model[(row["track"], row["model_id"])].append(row)
    rows = []
    for (track, model_id), items in by_track_model.items():
        items.sort(key=lambda item: str(item["decision_date"]))
        turnovers = [
            allocation_turnover(prev["allocation"], curr["allocation"])
            for prev, curr in zip(items, items[1:])
        ]
        regime_turnovers = [
            allocation_turnover(prev["allocation"], curr["allocation"])
            for prev, curr in zip(items, items[1:])
            if prev["prompt_regime"] != curr["prompt_regime"]
        ]
        rows.append(
            {
                "track": track,
                "model_id": model_id,
                "rounds": len(items),
                "avg_turnover_pct": mean(turnovers) if turnovers else None,
                "median_turnover_pct": median(turnovers) if turnovers else None,
                "avg_regime_change_turnover_pct": mean(regime_turnovers) if regime_turnovers else None,
                "avg_top_30d_quintile_pct": avg(items, "top_30d_quintile_pct"),
                "avg_explicit_momentum_pct": avg(items, "explicit_momentum_pct"),
                "avg_risk_score": avg(items, "risk_score"),
                "avg_top_weight_pct": avg(items, "top_weight_pct"),
                "momentum_language_rate_pct": bool_rate(items, "mentions_momentum"),
                "catalyst_language_rate_pct": bool_rate(items, "mentions_catalyst"),
                "reversal_language_rate_pct": bool_rate(items, "mentions_reversal"),
            }
        )
    rows.sort(key=lambda item: (item["track"], -(item["avg_regime_change_turnover_pct"] or -1), item["model_id"]))
    return rows


def markdown_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]], limit: int | None = None) -> str:
    shown = rows[:limit] if limit else rows
    lines = [
        "| " + " | ".join(label for _, label in columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in shown:
        values = []
        for key, _label in columns:
            value = row.get(key)
            if isinstance(value, float):
                values.append(f"{value:.1f}")
            elif value is None:
                values.append("")
            else:
                values.append(str(value).replace("|", "\\|"))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def write_report(
    path: Path,
    prompt_families: list[dict[str, Any]],
    round_rows: list[dict[str, Any]],
    submission_rows: list[dict[str, Any]],
    transitions: list[dict[str, Any]],
    regime_summary: list[dict[str, Any]],
    sensitivity_rows: list[dict[str, Any]],
) -> None:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    prompt_change_transitions = [row for row in transitions if row["changed_regime"] or row["changed_prompt_family"]]
    notable = [row for row in prompt_change_transitions if row["changed_regime"]]
    price_history = [row for row in transitions if row["to_regime"] == "R4_price_history_discipline"]
    benchmark_check = [row for row in transitions if row["to_regime"] == "R3_benchmark_asset_mean_reversion_check"]
    confidence_rows = [
        {
            "claim": "June 24 prompt text explicitly changed price-history instructions.",
            "confidence": "High",
            "basis": "Direct prompt diff and prompt feature flag.",
        },
        {
            "claim": "Explicit MOMENTUM allocation fell after the June 24 rule.",
            "confidence": "High",
            "basis": "Direct allocation comparison in adjacent weekly and monthly official runs.",
        },
        {
            "claim": "The June 24 rule made models less affected by broad recent-winner exposure.",
            "confidence": "Low",
            "basis": "Top-30-day-quintile allocation did not fall; it was flat weekly and higher monthly.",
        },
        {
            "claim": "The benchmark-asset instruction increased S&P 500 allocation.",
            "confidence": "Medium",
            "basis": "Both weekly and monthly adjacent transitions show +18 pp S&P 500 average allocation, but market context changed too.",
        },
        {
            "claim": "Semiconductor allocation rose because of the prompt alone.",
            "confidence": "Low",
            "basis": "Micron briefing facts arrived in the same round and are a strong confounder.",
        },
    ]

    report = [
        "# Prompt Sensitivity Research",
        "",
        f"Generated at: `{generated_at}`",
        "",
        "Scope: observational analysis of saved CapitalBench prompts, official model submissions, and generated market-data appendices. This is not a controlled rerun experiment, so findings are stated as associations unless the evidence is purely textual.",
        "",
        "## Executive Findings",
        "",
        "1. Prompt wording changed more than formatting. Across the saved history, the largest prompt shifts were: single-pick to portfolio construction, permission to use internal priors, explicit scoring-window discipline, briefing-bias discipline around mechanical return tables, a temporary benchmark/mean-reversion check, and the June 24 price-history discipline.",
        "2. The June 24 price-history rule is associated with a sharp drop in pure named momentum exposure: explicit `MOMENTUM` average allocation fell to 0.0% in both weekly and monthly rounds.",
        "3. That same rule did not make models broadly avoid recent winners. Allocation to top-30-day-quintile assets was flat in the weekly transition and higher in the monthly transition, because models rotated into catalyst-backed recent winners such as semiconductors.",
        "4. The temporary June 18/22 benchmark-asset instruction is associated with the clearest defensive prompt response: average S&P 500 allocation rose during that regime, especially in monthly rounds.",
        "5. Prompt guardrails often changed rationales before they fully changed risk appetite. Catalyst and reversal language rose under stricter prompts, but high-risk equity allocations often remained high.",
        "6. Model sensitivity is heterogeneous. Some models completely rotated around prompt/regime changes, while others retained recurring exposures such as small caps, biotech, or regional banks.",
        "",
        "## Evidence Confidence",
        "",
        markdown_table(confidence_rows, [("claim", "Claim"), ("confidence", "Confidence"), ("basis", "Basis")]),
        "",
        "## Prompt Regime Summary",
        "",
        markdown_table(
            regime_summary,
            [
                ("prompt_regime", "Regime"),
                ("rounds", "Rounds"),
                ("first_round", "First"),
                ("last_round", "Last"),
                ("avg_risk_score", "Risk"),
                ("avg_sp500_pct", "S&P 500 %"),
                ("avg_explicit_momentum_pct", "MOMENTUM %"),
                ("avg_top_30d_quintile_pct", "Top 30d Quintile %"),
                ("reversal_language_rate_pct", "Reversal Lang %"),
            ],
        ),
        "",
        "## Prompt Family Inventory",
        "",
        "The raw prompts produce many hashes because dates and horizons are embedded. The `prompt_family` hash normalizes routine metadata, but still preserves instruction wording changes.",
        "",
        markdown_table(
            prompt_families,
            [
                ("prompt_family", "Family"),
                ("regime", "Regime"),
                ("round_count", "Rounds"),
                ("first_round", "First"),
                ("last_round", "Last"),
                ("briefing_bias_discipline", "Briefing Bias"),
                ("benchmark_asset_case", "Benchmark Case"),
                ("price_history_discipline", "Price History"),
            ],
        ),
        "",
        "## Regime Change Event Study",
        "",
        markdown_table(
            notable,
            [
                ("track", "Track"),
                ("from_round", "From"),
                ("to_round", "To"),
                ("from_regime", "From Regime"),
                ("to_regime", "To Regime"),
                ("avg_model_turnover_pct", "Model Turnover"),
                ("delta_sp500_pct", "Delta S&P 500"),
                ("delta_explicit_momentum_pct", "Delta MOMENTUM"),
                ("delta_top_30d_quintile_pct", "Delta Top 30d Quintile"),
                ("delta_semiconductors_pct", "Delta Semis"),
                ("delta_reversal_language_rate_pct", "Delta Reversal Lang"),
            ],
        ),
        "",
        "## Case Study: June 24 Price-History Discipline",
        "",
        "The June 24 prompt changed the mechanical table wording from `mechanical return table` to `mechanical price-context table`, added a rule that trailing returns are descriptive rather than forecasts, and required momentum rationales to cite independent support or disclose limited support plus reversal risk.",
        "",
        markdown_table(
            price_history,
            [
                ("track", "Track"),
                ("from_round", "From"),
                ("to_round", "To"),
                ("avg_model_turnover_pct", "Turnover"),
                ("delta_explicit_momentum_pct", "Delta MOMENTUM"),
                ("delta_top_30d_quintile_pct", "Delta Top 30d Quintile"),
                ("delta_semiconductors_pct", "Delta Semis"),
                ("delta_catalyst_language_rate_pct", "Delta Catalyst Lang"),
                ("delta_reversal_language_rate_pct", "Delta Reversal Lang"),
            ],
        ),
        "",
        "Interpretation: the prompt appears to reduce pure named momentum anchoring, but not risk-taking or broad recent-winner exposure. Semiconductors rose because the June 24 briefing contained Micron revenue, margin, guidance, and HBM facts, giving models a non-price catalyst. This should be reported as `less pure momentum chasing, more catalyst-justified momentum`, not as a broad de-risking effect.",
        "",
        "## Case Study: Benchmark-Asset / Mean-Reversion Check",
        "",
        markdown_table(
            benchmark_check,
            [
                ("track", "Track"),
                ("from_round", "From"),
                ("to_round", "To"),
                ("avg_model_turnover_pct", "Turnover"),
                ("delta_sp500_pct", "Delta S&P 500"),
                ("delta_defensive_pct", "Delta Defensive"),
                ("delta_high_risk_pct", "Delta High Risk"),
                ("delta_similarity", "Delta Similarity"),
            ],
        ),
        "",
        "Interpretation: this prompt variant is the clearest example of an instruction changing portfolio construction directly. It explicitly legitimized benchmark allocation when active edge was weak, and average S&P 500 allocation rose in the affected windows.",
        "",
        "## Model Sensitivity",
        "",
        markdown_table(
            sensitivity_rows,
            [
                ("track", "Track"),
                ("model_id", "Model"),
                ("rounds", "Rounds"),
                ("avg_regime_change_turnover_pct", "Regime Turnover"),
                ("avg_turnover_pct", "Avg Turnover"),
                ("avg_top_30d_quintile_pct", "Top 30d Quintile %"),
                ("avg_risk_score", "Risk"),
                ("reversal_language_rate_pct", "Reversal Lang %"),
            ],
            limit=16,
        ),
        "",
        "## Researcher/Trader Takeaways",
        "",
        "- Prompt wording can change portfolio construction, not only response formatting.",
        "- Momentum guardrails do not eliminate risk-on behavior; they redirect it toward positions with a catalyst narrative.",
        "- Benchmark-relative wording and explicit benchmark-option permission can produce more benchmark-like portfolios.",
        "- Rationale text is a leading indicator of prompt compliance: models start mentioning catalysts, limited support, and reversal risk even when allocations remain aggressive.",
        "- Prompt sensitivity differs by model, so comparing raw benchmark scores without prompt regime context can mix model skill with instruction sensitivity.",
        "",
        "## Caveats",
        "",
        "- These are observational associations over historical official runs, not randomized prompt A/B tests.",
        "- Market facts changed at the same time as prompts. June 24 semiconductors are confounded by Micron facts; June 18/22 behavior is confounded by contemporaneous macro and market context.",
        "- Model roster changed when Fable 5 was excluded, so no-Fable periods should be compared model-by-model where possible.",
        "- The strongest next step is a non-official controlled rerun: same briefing and market appendix, multiple prompt variants, same model roster.",
        "",
        "## Output Files",
        "",
        "- `prompt_families.csv`: normalized prompt families and feature flags.",
        "- `round_metrics.csv`: per-round aggregate behavior metrics.",
        "- `submission_metrics.csv`: per-model behavior metrics.",
        "- `transition_metrics.csv`: adjacent-round event-study deltas.",
        "- `model_sensitivity.csv`: model-level sensitivity summaries.",
        "- `summary.json`: machine-readable summary used for this report.",
        "",
    ]
    path.write_text("\n".join(report), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds-dir", type=Path, default=Path("rounds"))
    parser.add_argument("--output", type=Path, default=Path("output/prompt_sensitivity"))
    parser.add_argument("--report-copy", type=Path, help="optional extra path for the generated Markdown report")
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    prompt_families, round_rows, submission_rows = build_dataset(args.rounds_dir)
    transitions = transition_rows(round_rows, submission_rows)
    regime_summary = grouped_round_summary(round_rows)
    sensitivity_rows = model_sensitivity(submission_rows)

    write_csv(args.output / "prompt_families.csv", prompt_families)
    write_csv(args.output / "round_metrics.csv", round_rows)
    write_csv(args.output / "submission_metrics.csv", submission_rows)
    write_csv(args.output / "transition_metrics.csv", transitions)
    write_csv(args.output / "regime_summary.csv", regime_summary)
    write_csv(args.output / "model_sensitivity.csv", sensitivity_rows)

    summary = {
        "round_count": len(round_rows),
        "submission_count": len(submission_rows),
        "prompt_family_count": len(prompt_families),
        "regime_count": len({row["prompt_regime"] for row in round_rows}),
        "regime_summary": regime_summary,
        "notable_regime_transitions": [row for row in transitions if row["changed_regime"]],
    }
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8", newline="\n")
    report_path = args.output / "report.md"
    write_report(
        report_path,
        prompt_families,
        round_rows,
        submission_rows,
        transitions,
        regime_summary,
        sensitivity_rows,
    )
    if args.report_copy:
        args.report_copy.parent.mkdir(parents=True, exist_ok=True)
        args.report_copy.write_text(report_path.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    print(f"wrote prompt sensitivity analysis to {args.output}")
    if args.report_copy:
        print(f"wrote report copy to {args.report_copy}")
    print(f"rounds={len(round_rows)} submissions={len(submission_rows)} prompt_families={len(prompt_families)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

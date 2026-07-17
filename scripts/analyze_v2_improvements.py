#!/usr/bin/env python3
"""Diagnose Portfolio V2 and rank evidence-backed V2.1 interventions.

The active July 13 V2 pilot is structural evidence only. This script never
reads interim or final V2 prices, never edits a round, and never publishes a
result. Historical return diagnostics use only resolved V1 rounds admitted by
the frozen model-predictability protocol.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any, Iterable, Sequence

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import analyze_model_predictability as base  # noqa: E402


V1_ROUND_ID = "CB-2026-07-13-1W"
V1_RUN_ID = "official-20260713"
V2_ROUND_ID = "CB-2026-07-13-V2-1W"
V2_RUN_ID = "official-v2-20260713"
PAIRED_MODELS = (
    "openai-gpt-5-5",
    "openai-gpt-5-6-sol",
    "xai-grok-4-3",
    "xai-grok-4-5",
)

V2_CONTEXT_FIELDS = (
    "return_3s",
    "return_5s",
    "active_return_5s",
    "prior_16s_active_return",
    "volatility_21s",
    "max_drawdown_21s",
    "volume_zscore_5v60",
    "corr_spy_63s",
    "beta_spy_63s",
    "distance_52w_high",
)

COMPACT_CONTEXT_FIELDS = (
    "option_id",
    "symbol",
    "option_group",
    "return_3s",
    "active_return_5s",
    "prior_16s_active_return",
    "volatility_21s",
    "max_drawdown_21s",
    "volume_zscore_5v60",
    "corr_spy_63s",
    "beta_spy_63s",
    "distance_52w_high",
)

FIELD_USAGE_PATTERNS = {
    "recent_window": (r"five[- ]session", r"5[- ]session", r"latest five", r"recent"),
    "prior_window": (r"prior 16", r"preceding sixteen", r"prior[- ]window"),
    "spy_relative": (r"\bspy\b", r"s&p", r"alpha", r"relative"),
    "volatility": (r"volatil",),
    "drawdown": (r"drawdown",),
    "volume": (r"volume",),
    "correlation_or_beta": (r"correlat", r"\bbeta\b"),
    "52_week_position": (r"52[- ]week", r"52w", r"year[- ]high"),
    "catalyst": (r"catalyst", r"scheduled", r"earnings", r"blockade", r"cpi"),
    "counter_case": (r"invalidation", r"if .* disappoint", r"if .* fall", r"if .* reverse"),
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def allocation_from_payload(payload: dict[str, Any]) -> dict[str, float]:
    return {
        str(item["option_id"]): float(item.get("allocation_pct") or 0.0)
        for item in payload.get("portfolio", [])
        if isinstance(item, dict) and item.get("option_id") and float(item.get("allocation_pct") or 0.0) > 0.0
    }


def submission_text(payload: dict[str, Any]) -> str:
    pieces = [
        str(payload.get("portfolio_rationale") or ""),
        str(payload.get("rationale_summary") or ""),
        " ".join(str(value) for value in payload.get("key_risks", []) if value),
    ]
    for item in payload.get("portfolio", []) or []:
        if not isinstance(item, dict):
            continue
        pieces.extend(
            str(item.get(key) or "")
            for key in ("time_window_catalyst", "invalidation_condition", "rationale")
        )
    return " ".join(piece for piece in pieces if piece).lower()


def portfolio_return(allocation: dict[str, float], returns: dict[str, float]) -> float:
    return sum(weight / 100.0 * returns[option_id] for option_id, weight in allocation.items())


def equal_weight(allocation: dict[str, float]) -> dict[str, float]:
    selected = sorted(option_id for option_id, weight in allocation.items() if weight > 0.0)
    if not selected:
        return {}
    weight = 100.0 / len(selected)
    return {option_id: weight for option_id in selected}


def cap_active_holding(allocation: dict[str, float], cap_pct: float) -> dict[str, float]:
    transformed: dict[str, float] = {}
    redirected = 0.0
    for option_id, weight in allocation.items():
        if option_id == "SP500":
            transformed[option_id] = transformed.get(option_id, 0.0) + weight
            continue
        kept = min(weight, cap_pct)
        transformed[option_id] = kept
        redirected += weight - kept
    transformed["SP500"] = transformed.get("SP500", 0.0) + redirected
    return {option_id: weight for option_id, weight in transformed.items() if weight > 0.0}


def blend_with_spy(allocation: dict[str, float], spy_reserve_pct: float) -> dict[str, float]:
    active_scale = (100.0 - spy_reserve_pct) / 100.0
    transformed = {option_id: weight * active_scale for option_id, weight in allocation.items()}
    transformed["SP500"] = transformed.get("SP500", 0.0) + spy_reserve_pct
    return {option_id: weight for option_id, weight in transformed.items() if weight > 0.0}


def allocation_turnover(left: dict[str, float], right: dict[str, float]) -> float:
    ids = set(left) | set(right)
    return 0.5 * sum(abs(left.get(option_id, 0.0) - right.get(option_id, 0.0)) for option_id in ids)


def allocation_overlap(left: dict[str, float], right: dict[str, float]) -> float:
    return sum(min(left.get(option_id, 0.0), right.get(option_id, 0.0)) for option_id in set(left) | set(right))


def concentration(allocation: dict[str, float]) -> tuple[float, float]:
    weights = [value / 100.0 for value in allocation.values() if value > 0.0]
    hhi = sum(value * value for value in weights)
    return hhi, (1.0 / hhi if hhi > 0.0 else 0.0)


def average(rows: Sequence[dict[str, Any]], key: str) -> float | None:
    values = [base.as_float(row.get(key)) for row in rows]
    present = [value for value in values if value is not None]
    return mean(present) if present else None


def aggregate_failure_rows(rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["track"]), "all")].append(row)
        grouped[(str(row["track"]), str(row["model_id"]))].append(row)

    output: list[dict[str, Any]] = []
    for (track, model_id), subset in sorted(grouped.items()):
        total_regret = average(subset, "total_oracle_regret") or 0.0
        search_regret = average(subset, "search_regret") or 0.0
        sizing_regret = average(subset, "sizing_regret") or 0.0
        output.append(
            {
                "track": track,
                "model_id": model_id,
                "decisions": len(subset),
                "mean_portfolio_return": average(subset, "portfolio_return"),
                "mean_sp500_return": average(subset, "sp500_return"),
                "mean_alpha": average(subset, "alpha_vs_sp500"),
                "beat_rate": mean(float(bool(row["beats_sp500"])) for row in subset),
                "mean_total_oracle_regret": total_regret,
                "mean_search_regret": search_regret,
                "mean_sizing_regret": sizing_regret,
                "search_share_of_regret": search_regret / total_regret if total_regret > 0.0 else None,
                "sizing_share_of_regret": sizing_regret / total_regret if total_regret > 0.0 else None,
                "mean_equal_selected_alpha": average(subset, "equal_selected_alpha"),
                "mean_equal_selected_edge_vs_universe": average(subset, "equal_selected_edge_vs_universe"),
                "mean_weight_beating_sp500": average(subset, "weight_beating_sp500_pct"),
                "mean_holding_beat_share": average(subset, "holding_beat_share"),
                "top1_capture_rate": mean(float(bool(row["top1_captured"])) for row in subset),
                "top3_capture_rate": mean(float(bool(row["top3_captured"])) for row in subset),
                "top5_capture_rate": mean(float(bool(row["top5_captured"])) for row in subset),
            }
        )
    return output


def analyze_historical_failures(rounds: Sequence[base.RoundRecord]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    for record in rounds:
        returns = {
            str(asset["option_id"]): float(asset["future_return"])
            for asset in record.assets
            if asset.get("future_return") is not None
        }
        risky = [asset for asset in record.assets if not asset.get("is_cash")]
        ranked = sorted(risky, key=lambda item: float(item["future_return"]), reverse=True)
        top_ids = {
            size: {str(asset["option_id"]) for asset in ranked[:size]}
            for size in (1, 3, 5)
        }
        universe_equal = mean(float(asset["future_return"]) for asset in risky)
        for model in record.models:
            allocation = {
                option_id: weight
                for option_id, weight in model.allocation.items()
                if weight > 0.0 and option_id in returns
            }
            if not allocation:
                continue
            selected = set(allocation)
            actual = portfolio_return(allocation, returns)
            selected_best = max(returns[option_id] for option_id in selected)
            equal_selected = portfolio_return(equal_weight(allocation), returns)
            total_regret = record.oracle_return - actual
            search_regret = record.oracle_return - selected_best
            sizing_regret = selected_best - actual
            rows.append(
                {
                    "round_id": record.round_id,
                    "track": record.track,
                    "decision_date": record.decision_date,
                    "model_id": model.model_id,
                    "holding_count": len(selected),
                    "portfolio_return": actual,
                    "sp500_return": record.sp500_return,
                    "alpha_vs_sp500": actual - record.sp500_return,
                    "beats_sp500": actual > record.sp500_return,
                    "oracle_return": record.oracle_return,
                    "best_selected_return": selected_best,
                    "total_oracle_regret": total_regret,
                    "search_regret": search_regret,
                    "sizing_regret": sizing_regret,
                    "regret_identity_error": abs(total_regret - search_regret - sizing_regret),
                    "equal_selected_return": equal_selected,
                    "equal_selected_alpha": equal_selected - record.sp500_return,
                    "equal_selected_edge_vs_universe": equal_selected - universe_equal,
                    "weight_beating_sp500_pct": sum(
                        weight for option_id, weight in allocation.items() if returns[option_id] > record.sp500_return
                    ),
                    "holding_beat_share": mean(
                        float(returns[option_id] > record.sp500_return) for option_id in selected
                    ),
                    "top1_captured": bool(selected & top_ids[1]),
                    "top3_captured": bool(selected & top_ids[3]),
                    "top5_captured": bool(selected & top_ids[5]),
                }
            )
    return rows, aggregate_failure_rows(rows)


def portfolio_rule_allocations(allocation: dict[str, float]) -> dict[str, dict[str, float]]:
    return {
        "submitted": dict(allocation),
        "equal_selected": equal_weight(allocation),
        "cap_active_50_to_spy": cap_active_holding(allocation, 50.0),
        "cap_active_35_to_spy": cap_active_holding(allocation, 35.0),
        "spy_reserve_25": blend_with_spy(allocation, 25.0),
        "spy_reserve_50": blend_with_spy(allocation, 50.0),
    }


def analyze_portfolio_rules(rounds: Sequence[base.RoundRecord]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    for record in rounds:
        returns = {
            str(asset["option_id"]): float(asset["future_return"])
            for asset in record.assets
            if asset.get("future_return") is not None
        }
        for model in record.models:
            allocation = {
                option_id: weight
                for option_id, weight in model.allocation.items()
                if weight > 0.0 and option_id in returns
            }
            if not allocation:
                continue
            submitted = portfolio_return(allocation, returns)
            for rule, transformed in portfolio_rule_allocations(allocation).items():
                result = portfolio_return(transformed, returns)
                rows.append(
                    {
                        "round_id": record.round_id,
                        "track": record.track,
                        "decision_date": record.decision_date,
                        "model_id": model.model_id,
                        "rule": rule,
                        "portfolio_return": result,
                        "sp500_return": record.sp500_return,
                        "alpha_vs_sp500": result - record.sp500_return,
                        "beats_sp500": result > record.sp500_return,
                        "improvement_vs_submitted": result - submitted,
                        "submitted_return": submitted,
                        "max_weight_pct": max(transformed.values(), default=0.0),
                        "spy_weight_pct": transformed.get("SP500", 0.0),
                    }
                )

    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["track"]), str(row["rule"]), "all")].append(row)
        grouped[(str(row["track"]), str(row["rule"]), str(row["model_id"]))].append(row)

    summaries: list[dict[str, Any]] = []
    for (track, rule, model_id), subset in sorted(grouped.items()):
        by_round: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in subset:
            by_round[str(row["round_id"])].append(row)
        round_rows = [
            {
                "round_id": round_id,
                "decision_date": values[0]["decision_date"],
                "improvement": mean(float(item["improvement_vs_submitted"]) for item in values),
            }
            for round_id, values in by_round.items()
        ]
        block_length = 5 if track == "weekly" else 10
        ci_low, ci_high = base.moving_block_ci(
            round_rows,
            "improvement",
            block_length,
            f"v2-improvement:{track}:{rule}:{model_id}",
        )
        improvements = [float(row["improvement_vs_submitted"]) for row in subset]
        summaries.append(
            {
                "track": track,
                "rule": rule,
                "model_id": model_id,
                "decisions": len(subset),
                "rounds": len(by_round),
                "mean_return": average(subset, "portfolio_return"),
                "mean_alpha": average(subset, "alpha_vs_sp500"),
                "beat_rate": mean(float(bool(row["beats_sp500"])) for row in subset),
                "mean_improvement_vs_submitted": mean(improvements),
                "median_improvement_vs_submitted": median(improvements),
                "improvement_rate": mean(float(value > 0.0) for value in improvements),
                "improvement_ci_low": ci_low,
                "improvement_ci_high": ci_high,
                "mean_spy_weight_pct": average(subset, "spy_weight_pct"),
            }
        )
    return rows, summaries


def grouped_concentration(
    allocation: dict[str, float],
    options: dict[str, dict[str, Any]],
    field: str,
) -> float:
    groups: dict[str, float] = defaultdict(float)
    for option_id, weight in allocation.items():
        group = str(options.get(option_id, {}).get(field) or "unknown")
        groups[group] += weight
    return max(groups.values(), default=0.0)


def selected_feature_rows(
    payloads: dict[str, dict[str, Any]],
    context_rows: Sequence[dict[str, str]],
    options_order: Sequence[str],
    briefing_text: str,
    options: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    context = {str(row["option_id"]): row for row in context_rows}
    noncash_ids = [option_id for option_id in options_order if option_id != "CASH" and option_id in context]
    ranks: dict[str, dict[str, float | None]] = defaultdict(dict)
    for field in V2_CONTEXT_FIELDS:
        values = [base.as_float(context[option_id].get(field)) for option_id in noncash_ids]
        for option_id, rank in zip(noncash_ids, base.percentile_ranks(values)):
            ranks[option_id][field] = rank
    positions = {option_id: index + 1 for index, option_id in enumerate(options_order)}

    rows: list[dict[str, Any]] = []
    for model_id, payload in payloads.items():
        for holding in payload.get("portfolio", []) or []:
            if not isinstance(holding, dict) or not holding.get("option_id"):
                continue
            option_id = str(holding["option_id"])
            context_row = context.get(option_id, {})
            option = options.get(option_id, {})
            row: dict[str, Any] = {
                "model_id": model_id,
                "option_id": option_id,
                "allocation_pct": base.as_float(holding.get("allocation_pct")),
                "expected_return_pct": base.as_float(holding.get("expected_return_pct")),
                "option_position": positions.get(option_id),
                "option_position_pct": (
                    (positions[option_id] - 1) / max(len(options_order) - 1, 1)
                    if option_id in positions
                    else None
                ),
                "asset_class": option.get("asset_class") or "",
                "option_group": option.get("option_group") or "",
                "briefing_mentions": base.mention_count(briefing_text, option) if option else 0,
            }
            for field in V2_CONTEXT_FIELDS:
                row[field] = base.as_float(context_row.get(field))
                row[f"rank_{field}"] = ranks.get(option_id, {}).get(field)
            rows.append(row)
    return rows


def load_structural_payloads(rounds_dir: Path, round_id: str, run_id: str) -> dict[str, dict[str, Any]]:
    parsed = rounds_dir / round_id / "runs" / run_id / "submissions" / "parsed"
    return {
        model_id: load_json(parsed / f"{model_id}.json")
        for model_id in PAIRED_MODELS
    }


def analyze_v2_structure(rounds_dir: Path) -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    dict[str, Any],
]:
    v1_payloads = load_structural_payloads(rounds_dir, V1_ROUND_ID, V1_RUN_ID)
    v2_payloads = load_structural_payloads(rounds_dir, V2_ROUND_ID, V2_RUN_ID)
    v2_round = rounds_dir / V2_ROUND_ID
    option_list = base.load_options(v2_round)
    options = {str(item["id"]): item for item in option_list}
    options_order = [str(item["id"]) for item in option_list]
    context_rows = read_csv(v2_round / "market_data" / "universe_decision_context.csv")
    briefing_text = (v2_round / "briefing.md").read_text(encoding="utf-8")
    selected_rows = selected_feature_rows(
        v2_payloads,
        context_rows,
        options_order,
        briefing_text,
        options,
    )

    comparison_rows: list[dict[str, Any]] = []
    usage_rows: list[dict[str, Any]] = []
    for model_id in PAIRED_MODELS:
        v1 = v1_payloads[model_id]
        v2 = v2_payloads[model_id]
        v1_alloc = allocation_from_payload(v1)
        v2_alloc = allocation_from_payload(v2)
        common = set(v1_alloc) & set(v2_alloc)
        union = set(v1_alloc) | set(v2_alloc)
        hhi, effective = concentration(v2_alloc)
        holdings = [item for item in v2.get("portfolio", []) if isinstance(item, dict)]
        weighted_forecast = sum(
            float(item.get("allocation_pct") or 0.0) / 100.0
            * float(item.get("expected_return_pct") or 0.0)
            for item in holdings
        )
        alpha_arithmetic = (
            float(v2.get("portfolio_expected_return_pct") or 0.0)
            - float(v2.get("benchmark_expected_return_pct") or 0.0)
        )
        selected_for_model = [row for row in selected_rows if row["model_id"] == model_id]
        comparison_rows.append(
            {
                "model_id": model_id,
                "v1_holdings": ";".join(sorted(v1_alloc)),
                "v2_holdings": ";".join(sorted(v2_alloc)),
                "common_holding_count": len(common),
                "holding_jaccard": len(common) / len(union) if union else 1.0,
                "allocation_turnover_pct": allocation_turnover(v1_alloc, v2_alloc),
                "v1_max_weight_pct": max(v1_alloc.values(), default=0.0),
                "v2_max_weight_pct": max(v2_alloc.values(), default=0.0),
                "v2_hhi": hhi,
                "v2_effective_holdings": effective,
                "v2_max_option_group_weight_pct": grouped_concentration(v2_alloc, options, "option_group"),
                "v2_max_asset_class_weight_pct": grouped_concentration(v2_alloc, options, "asset_class"),
                "v2_spy_weight_pct": v2_alloc.get("SP500", 0.0),
                "benchmark_expected_return_pct": base.as_float(v2.get("benchmark_expected_return_pct")),
                "portfolio_expected_return_pct": base.as_float(v2.get("portfolio_expected_return_pct")),
                "expected_alpha_pct": base.as_float(v2.get("expected_alpha_vs_sp500_pct")),
                "confidence": base.as_float(v2.get("confidence")),
                "weighted_forecast_error_pct": abs(
                    weighted_forecast - float(v2.get("portfolio_expected_return_pct") or 0.0)
                ),
                "alpha_arithmetic_error_pct": abs(
                    alpha_arithmetic - float(v2.get("expected_alpha_vs_sp500_pct") or 0.0)
                ),
                "allocation_to_briefing_mentioned_pct": sum(
                    float(row.get("allocation_pct") or 0.0)
                    for row in selected_for_model
                    if float(row.get("briefing_mentions") or 0.0) > 0.0
                ),
                "allocation_to_top_recent_quintile_pct": sum(
                    float(row.get("allocation_pct") or 0.0)
                    for row in selected_for_model
                    if float(row.get("rank_active_return_5s") or 0.0) >= 0.8
                ),
                "allocation_to_top_prior_quintile_pct": sum(
                    float(row.get("allocation_pct") or 0.0)
                    for row in selected_for_model
                    if float(row.get("rank_prior_16s_active_return") or 0.0) >= 0.8
                ),
                "v1_input_tokens": base.as_float((v1.get("usage") or {}).get("input_tokens")),
                "v2_input_tokens": base.as_float((v2.get("usage") or {}).get("input_tokens")),
                "v2_output_tokens": base.as_float((v2.get("usage") or {}).get("output_tokens")),
                "v2_reasoning_tokens": base.as_float((v2.get("usage") or {}).get("reasoning_tokens")),
            }
        )
        text = submission_text(v2)
        usage_rows.append(
            {
                "model_id": model_id,
                **{
                    field: any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)
                    for field, patterns in FIELD_USAGE_PATTERNS.items()
                },
            }
        )

    pair_rows: list[dict[str, Any]] = []
    for version, payloads in (("v1", v1_payloads), ("v2", v2_payloads)):
        allocations = {model_id: allocation_from_payload(payload) for model_id, payload in payloads.items()}
        for left, right in combinations(PAIRED_MODELS, 2):
            pair_rows.append(
                {
                    "version": version,
                    "model_a": left,
                    "model_b": right,
                    "allocation_overlap_pct": allocation_overlap(allocations[left], allocations[right]),
                    "holding_jaccard": (
                        len(set(allocations[left]) & set(allocations[right]))
                        / len(set(allocations[left]) | set(allocations[right]))
                    ),
                }
            )

    v2_overlaps = [row["allocation_overlap_pct"] for row in pair_rows if row["version"] == "v2"]
    v1_overlaps = [row["allocation_overlap_pct"] for row in pair_rows if row["version"] == "v1"]
    forecasts = [float(row["portfolio_expected_return_pct"]) for row in comparison_rows]
    benchmark_forecasts = [float(row["benchmark_expected_return_pct"]) for row in comparison_rows]
    confidences = [float(row["confidence"]) for row in comparison_rows]
    structural_summary = {
        "paired_models": len(PAIRED_MODELS),
        "mean_holding_jaccard_v1_to_v2": mean(float(row["holding_jaccard"]) for row in comparison_rows),
        "mean_allocation_turnover_pct": mean(float(row["allocation_turnover_pct"]) for row in comparison_rows),
        "mean_pairwise_overlap_v1_pct": mean(v1_overlaps),
        "mean_pairwise_overlap_v2_pct": mean(v2_overlaps),
        "mean_v2_max_weight_pct": mean(float(row["v2_max_weight_pct"]) for row in comparison_rows),
        "mean_v2_spy_weight_pct": mean(float(row["v2_spy_weight_pct"]) for row in comparison_rows),
        "mean_v2_effective_holdings": mean(float(row["v2_effective_holdings"]) for row in comparison_rows),
        "mean_v2_allocation_top_recent_quintile_pct": mean(
            float(row["allocation_to_top_recent_quintile_pct"]) for row in comparison_rows
        ),
        "mean_v2_allocation_top_prior_quintile_pct": mean(
            float(row["allocation_to_top_prior_quintile_pct"]) for row in comparison_rows
        ),
        "mean_v2_input_token_increase_pct": mean(
            100.0
            * (float(row["v2_input_tokens"]) - float(row["v1_input_tokens"]))
            / float(row["v1_input_tokens"])
            for row in comparison_rows
        ),
        "portfolio_forecast_mean_pct": mean(forecasts),
        "portfolio_forecast_sd_pct": pstdev(forecasts),
        "benchmark_forecast_mean_pct": mean(benchmark_forecasts),
        "benchmark_forecast_sd_pct": pstdev(benchmark_forecasts),
        "confidence_mean": mean(confidences),
        "confidence_sd": pstdev(confidences),
        "reasoning_tokens_min": min(float(row["v2_reasoning_tokens"]) for row in comparison_rows),
        "reasoning_tokens_max": max(float(row["v2_reasoning_tokens"]) for row in comparison_rows),
        "explicit_usage_model_counts": {
            field: sum(bool(row[field]) for row in usage_rows)
            for field in FIELD_USAGE_PATTERNS
        },
    }
    return comparison_rows, selected_rows, pair_rows, {"usage_rows": usage_rows, **structural_summary}


def build_compact_context(rounds_dir: Path, output_dir: Path) -> dict[str, Any]:
    source = rounds_dir / V2_ROUND_ID / "market_data" / "universe_decision_context.csv"
    rows = read_csv(source)
    compact_path = output_dir / "proposed_compact_context.csv"
    base.write_csv(compact_path, rows, COMPACT_CONTEXT_FIELDS)
    source_text = source.read_text(encoding="utf-8")
    compact_text = compact_path.read_text(encoding="utf-8")
    noncash = [row for row in rows if row.get("option_id") != "CASH"]
    return_5s = [base.as_float(row.get("return_5s")) for row in noncash]
    active_5s = [base.as_float(row.get("active_return_5s")) for row in noncash]
    pairs = [(left, right) for left, right in zip(return_5s, active_5s) if left is not None and right is not None]
    rank_correlation = base.spearman([left for left, _right in pairs], [right for _left, right in pairs])
    return {
        "rows": len(rows),
        "current_columns": len(rows[0]) if rows else 0,
        "compact_columns": len(COMPACT_CONTEXT_FIELDS),
        "current_characters": len(source_text),
        "compact_characters": len(compact_text),
        "character_reduction_pct": 100.0 * (1.0 - len(compact_text) / len(source_text)),
        "return_5s_active_5s_rank_correlation": rank_correlation,
        "distinct_as_of_dates": len({row.get("as_of_price_date") for row in rows}),
        "pass_status_rows": sum(row.get("status") == "pass" for row in rows),
        "fields_removed": [field for field in rows[0] if field not in COMPACT_CONTEXT_FIELDS] if rows else [],
        "compact_path": str(compact_path),
    }


def prompt_contract_audit(rounds_dir: Path) -> list[dict[str, Any]]:
    prompt = (rounds_dir / V2_ROUND_ID / "prompt.md").read_text(encoding="utf-8").lower()
    checks = [
        ("full_universe_shortlist", False, "No auditable shortlist; the prompt explicitly prohibits a ranked list."),
        ("forecasts_for_rejected_finalists", False, "Only selected holdings receive expected-return forecasts."),
        ("explicit_spy_forecast", "estimate spy" in prompt, "SPY forecast is required."),
        ("selected_holding_must_beat_spy", False, "The portfolio is compared with SPY, but no holding-level hurdle is enforced."),
        ("hard_economic_exposure_cap", False, "Correlation is a soft consideration, not a validated constraint."),
        ("forecast_interval", False, "Only point forecasts are recorded."),
        ("beat_spy_probability", '"confidence"' in prompt, "A probability is recorded but has no prior calibration."),
        ("holding_invalidation", "invalidation_condition" in prompt, "Every selected holding requires an invalidation condition."),
        ("allows_spy", "spy is an allowed option" in prompt, "SPY is available but no fallback rule is specified."),
        ("single_turn_non_agentic", "single-turn, non-agentic" in prompt, "The benchmark contract is preserved."),
    ]
    return [
        {"check": name, "present": present, "interpretation": interpretation}
        for name, present, interpretation in checks
    ]


def data_family_matrix() -> list[dict[str, Any]]:
    rows = [
        ("compact_price_path", 4, 5, 5, 5, 5, "prospective_test", "Keep existing path data but remove redundant columns and test a more readable table."),
        ("structured_event_calendar", 5, 5, 5, 4, 5, "prospective_test", "Convert scheduled events already researched into date, uncertainty, and affected-exposure fields without a directional recommendation."),
        ("economic_exposure_map", 5, 5, 5, 5, 5, "implement", "Required to detect ENERGY plus OIL and other cross-asset expressions of the same economic bet."),
        ("market_breadth_and_regime", 3, 5, 5, 5, 5, "keep_compact", "Already present in V2; test whether a short regime label is used more reliably than a dense metric header."),
        ("analyst_revision_breadth", 4, 3, 4, 3, 3, "instrument_first", "Potentially useful around earnings, but ETF/index coverage and reproducible licensing must be solved first."),
        ("valuation", 2, 4, 5, 4, 4, "monthly_only_test", "More plausible for the monthly track than a seven-day winner; avoid spending weekly context on it."),
        ("options_implied_information", 4, 2, 3, 2, 2, "reject_for_now", "Coverage, normalization, and cost are poor across a heterogeneous 70-option universe."),
        ("fund_flows_and_crowding", 3, 3, 3, 3, 3, "instrument_first", "Evidence is horizon- and market-dependent; define a complete mechanical source before model use."),
        ("more_unstructured_news", 3, 4, 3, 2, 1, "reject", "The existing briefing already anchors decisions; more narrative increases context and selection bias without complete option comparison."),
    ]
    return [
        {
            "data_family": family,
            "horizon_relevance_1_5": horizon,
            "coverage_1_5": coverage,
            "cutoff_auditability_1_5": auditability,
            "reproducibility_1_5": reproducibility,
            "context_efficiency_1_5": efficiency,
            "total_25": horizon + coverage + auditability + reproducibility + efficiency,
            "rating": rating,
            "reason": reason,
        }
        for family, horizon, coverage, auditability, reproducibility, efficiency, rating, reason in rows
    ]


def literature_evidence() -> list[dict[str, Any]]:
    return [
        {
            "topic": "long_context_retrieval",
            "source": "Liu et al. (2024), Lost in the Middle",
            "url": "https://aclanthology.org/2024.tacl-1.9/",
            "primary_finding": "Relevant-information position materially changes long-context retrieval accuracy.",
            "capitalbench_implication": "Test option-order sensitivity and reduce avoidable table density; do not assume a 70-row table is used uniformly.",
            "limitation": "The paper studies retrieval and QA, not portfolio returns.",
        },
        {
            "topic": "table_reference_accuracy",
            "source": "Yang et al. (2026), When LLMs Read Tables Carelessly",
            "url": "https://aclanthology.org/2026.acl-long.762/",
            "primary_finding": "Models can omit or cite incorrect table values even when they understand table structure.",
            "capitalbench_implication": "Record source values in a candidate ledger and test deterministic value-reference accuracy before a paid run.",
            "limitation": "Tested models and tasks do not exactly match CapitalBench participants.",
        },
        {
            "topic": "language_model_forecasting",
            "source": "Halawi et al. (2024), Approaching Human-Level Forecasting with Language Models",
            "url": "https://arxiv.org/abs/2402.18563",
            "primary_finding": "Retrieval, structured forecasting, and aggregation can approach competitive human forecasting on some questions.",
            "capitalbench_implication": "Structured probabilistic forecasts are useful instrumentation, but CapitalBench should preserve its single-call non-agentic treatment.",
            "limitation": "The studied system is retrieval-augmented and aggregated, unlike CapitalBench.",
        },
        {
            "topic": "confidence_calibration",
            "source": "Zhang et al. (2024), Calibrating Confidence by Eliciting Fidelity",
            "url": "https://arxiv.org/abs/2404.02655",
            "primary_finding": "Post-aligned language models can be overconfident and require explicit calibration methods.",
            "capitalbench_implication": "Do not size portfolios from one verbalized confidence number before prospective calibration.",
            "limitation": "The experiments focus on question answering rather than return forecasting.",
        },
        {
            "topic": "forecast_scoring",
            "source": "Karger et al. (2025), ForecastBench",
            "url": "https://www.forecastbench.org/docs/",
            "primary_finding": "Probabilistic forecast rankings require proper scoring, many resolved questions, and difficulty controls.",
            "capitalbench_implication": "Use Brier scores and calibration curves across many finalist-vs-SPY forecasts, not one aggregate confidence per round.",
            "limitation": "Binary event questions differ from continuous asset returns.",
        },
        {
            "topic": "llm_news_signal",
            "source": "Lopez-Lira and Tang (2023), Can ChatGPT Forecast Stock Price Movements?",
            "url": "https://arxiv.org/abs/2304.07619",
            "primary_finding": "LLM interpretation of news headlines contains out-of-sample daily return information in the studied sample.",
            "capitalbench_implication": "Option-specific factual event mapping is more promising than indiscriminately adding price-history columns.",
            "limitation": "Individual-stock headline classification is not a 70-ETF portfolio task and effects may decay with adoption.",
        },
        {
            "topic": "llm_return_bias",
            "source": "Chen et al. (2024), Extrapolation and Miscalibration in LLM Stock Return Forecasts",
            "url": "https://arxiv.org/abs/2409.11540",
            "primary_finding": "LLMs over-extrapolate recent returns, are optimistic, and understate parts of the return distribution.",
            "capitalbench_implication": "Require explicit continuation and reversal cases plus forecast ranges and base-rate comparison.",
            "limitation": "Prompt and asset setup differ from CapitalBench.",
        },
        {
            "topic": "weekly_reversal",
            "source": "Lehmann (1990), Fads, Martingales, and Market Efficiency",
            "url": "https://www.nber.org/papers/w2533",
            "primary_finding": "One-week winners and losers showed sizeable subsequent reversals in the historical equity sample.",
            "capitalbench_implication": "A recent winner should trigger a reversal check, not automatic continuation or automatic rejection.",
            "limitation": "The evidence is old, security-level, and not a universal ETF rule.",
        },
        {
            "topic": "medium_horizon_momentum",
            "source": "Jegadeesh and Titman (1993), Returns to Buying Winners and Selling Losers",
            "url": "https://doi.org/10.1111/j.1540-6261.1993.tb04702.x",
            "primary_finding": "Intermediate-horizon past winners outperformed past losers in the studied sample.",
            "capitalbench_implication": "Recent and prior windows must be treated as horizon-specific evidence rather than collapsed into one trend story.",
            "limitation": "Three-to-twelve-month momentum does not establish one-week or one-month predictability in this universe.",
        },
        {
            "topic": "analyst_revisions",
            "source": "Asquith, Mikhail, and Au (2005), Information Content of Equity Analyst Reports",
            "url": "https://www.nber.org/papers/w9246",
            "primary_finding": "Recommendation, earnings-forecast, price-target, and report-text changes contain market information.",
            "capitalbench_implication": "Revision breadth may help around earnings if complete ETF/index coverage and licensing are available.",
            "limitation": "ETF-level aggregation and current data access are unresolved.",
        },
        {
            "topic": "options_information",
            "source": "Muravyev, Pearson, and Pollet (2018), Why Does Options Market Information Predict Stock Returns?",
            "url": "https://doi.org/10.2139/ssrn.2851560",
            "primary_finding": "Some options-derived signals predict stock returns, with substantial links to borrowing fees and trading frictions.",
            "capitalbench_implication": "Options data is not a simple universal signal and should wait for complete, normalized coverage.",
            "limitation": "Many CapitalBench options lack comparable liquid option surfaces.",
        },
        {
            "topic": "portfolio_weight_estimation",
            "source": "DeMiguel, Garlappi, and Uppal (2009), Optimal Versus Naive Diversification",
            "url": "https://doi.org/10.1093/rfs/hhm075",
            "primary_finding": "Estimated optimized portfolios did not consistently beat 1/N out of sample across the studied datasets.",
            "capitalbench_implication": "Avoid elaborate post-model optimizers on a tiny sample; test transparent caps and equal weighting prospectively.",
            "limitation": "The paper studies conventional estimated portfolios, not LLM-selected ETF portfolios.",
        },
    ]


def intervention_matrix(failure_summary: Sequence[dict[str, Any]], structural: dict[str, Any]) -> list[dict[str, Any]]:
    weekly = next(row for row in failure_summary if row["track"] == "weekly" and row["model_id"] == "all")
    monthly = next(row for row in failure_summary if row["track"] == "monthly" and row["model_id"] == "all")
    return [
        {
            "priority": 1,
            "intervention": "auditable_full_universe_candidate_ledger",
            "rating": "implement",
            "mechanism": "Force the single call to expose 6-8 finalists before final allocation, including rejected finalists and SPY.",
            "evidence": f"Search regret is {weekly['search_share_of_regret']:.1%} of weekly and {monthly['search_share_of_regret']:.1%} of monthly total oracle regret; current V2 records only selected holdings.",
            "success_metric": "Top-3/top-5 candidate capture, candidate forecast rank correlation, and eventual paired alpha.",
        },
        {
            "priority": 2,
            "intervention": "compact_nonredundant_decision_table",
            "rating": "prospective_test",
            "mechanism": "Remove repeated date/status fields and rank-equivalent raw/active-return duplication while preserving every option in frozen order.",
            "evidence": "The current table is dense and contains fields that do not add within-round ordering information; long-context and table-reference errors are established LLM failure modes.",
            "success_metric": "Synthetic value-reference accuracy, order sensitivity, candidate coverage, then paired realized alpha.",
        },
        {
            "priority": 3,
            "intervention": "holding_level_spy_hurdle",
            "rating": "prospective_test",
            "mechanism": "Forbid an active holding whose base expected return does not exceed the model's SPY base forecast; permit 100% SPY when none qualify.",
            "evidence": "V2 asks for portfolio-level comparison but does not enforce a holding-level relative-return condition.",
            "success_metric": "Forecasted and realized alpha of selected holdings versus SPY, plus fallback frequency.",
        },
        {
            "priority": 4,
            "intervention": "economic_exposure_clusters_and_cap",
            "rating": "prospective_test",
            "mechanism": "Add static exposure clusters and cap a single economic thesis at 50%, even when expressed through different asset classes.",
            "evidence": f"V2 pairwise allocation overlap averages {structural['mean_pairwise_overlap_v2_pct']:.1f}%; one valid portfolio used only ENERGY and OIL despite the soft correlation instruction.",
            "success_metric": "Cluster concentration, downside from failed shared catalysts, and paired realized alpha.",
        },
        {
            "priority": 5,
            "intervention": "forecast_ranges_and_calibration_ledger",
            "rating": "instrument_first",
            "mechanism": "Record low/base/high return forecasts for SPY and every finalist and score point error, interval coverage, and beat-SPY Brier score.",
            "evidence": f"The first V2 confidences occupy only a narrow {structural['confidence_sd']:.3f} standard-deviation band and have no resolved calibration history.",
            "success_metric": "MAE, rank IC, interval coverage, Brier score, and calibration slope after sufficient prospective observations.",
        },
        {
            "priority": 6,
            "intervention": "structured_event_exposure_matrix",
            "rating": "prospective_test",
            "mechanism": "Represent scheduled events as compact factual rows and require the model to connect each finalist to an event or explicitly state no event edge.",
            "evidence": "All four V2 models concentrated on briefing catalysts, but the briefing is narrative and does not provide complete option-by-event comparison.",
            "success_metric": "Candidate breadth, unsupported-catalyst rate, and realized event-window alpha.",
        },
        {
            "priority": 7,
            "intervention": "fixed_spy_sleeve_as_alpha_solution",
            "rating": "reject",
            "mechanism": "Reserve a fixed share in SPY regardless of the model forecast.",
            "evidence": "It mechanically shrinks both positive and negative alpha; it can control risk but cannot create selection skill.",
            "success_metric": "Not applicable as a claimed return improvement.",
        },
        {
            "priority": 8,
            "intervention": "add_all_available_data",
            "rating": "reject",
            "mechanism": "Append more unstructured facts and market fields without an ablation or complete coverage rule.",
            "evidence": "V2 already increased input size while producing high cross-model thesis overlap; more context does not guarantee better retrieval.",
            "success_metric": "Not applicable until each data family passes its own coverage and prospective test.",
        },
        {
            "priority": 9,
            "intervention": "increase_reasoning_effort_only",
            "rating": "instrument_first",
            "mechanism": "Increase provider reasoning settings without changing the decision architecture.",
            "evidence": f"Observed V2 reasoning usage ranges from {structural['reasoning_tokens_min']:.0f} to {structural['reasoning_tokens_max']:.0f} tokens, but one unresolved round cannot link more tokens to better returns.",
            "success_metric": "Candidate coverage and paired return under a separately frozen configuration test.",
        },
    ]


def hypothesis_results(
    failure_summary: Sequence[dict[str, Any]],
    structural: dict[str, Any],
) -> list[dict[str, Any]]:
    weekly = find_summary(failure_summary, "weekly")
    monthly = find_summary(failure_summary, "monthly")
    return [
        {
            "hypothesis": "candidate_search_is_primary_bottleneck",
            "verdict": "supported_as_diagnosis",
            "evidence": f"Search accounts for {weekly['search_share_of_regret']:.1%} of weekly and {monthly['search_share_of_regret']:.1%} of monthly oracle regret; equal-selected alpha remains negative.",
            "limit": "Oracle regret uses hindsight and does not prove the winner was predictable.",
        },
        {
            "hypothesis": "flat_context_encourages_selective_use",
            "verdict": "partially_supported",
            "evidence": f"V2 added {structural['mean_v2_input_token_increase_pct']:.1f}% input tokens, allocated {structural['mean_v2_allocation_top_recent_quintile_pct']:.1f}% to latest-window top-quintile assets, and explicitly referenced several supplied fields rarely or never.",
            "limit": "No paid order-permutation experiment was run, so positional causality is unproven.",
        },
        {
            "hypothesis": "relative_spy_hurdle_is_too_weak",
            "verdict": "contract_gap_confirmed",
            "evidence": "V2 requires a portfolio-level SPY comparison but no finalist or holding is required to clear SPY.",
            "limit": "The return effect of a hard holding-level hurdle requires prospective forecasts and outcomes.",
        },
        {
            "hypothesis": "forecast_confidence_is_not_ready_for_sizing",
            "verdict": "instrument_first",
            "evidence": f"Only four unresolved probabilities exist and their cross-model standard deviation is {structural['confidence_sd']:.3f}.",
            "limit": "No resolved V2 confidence history exists yet.",
        },
        {
            "hypothesis": "soft_correlation_wording_allows_shared_bets",
            "verdict": "supported_structurally",
            "evidence": f"Average V2 pairwise allocation overlap is {structural['mean_pairwise_overlap_v2_pct']:.1f}%, and a valid portfolio allocated 100% to ENERGY plus OIL.",
            "limit": "Diversification can lower or raise realized return; a hard cluster cap must be prospectively tested.",
        },
        {
            "hypothesis": "more_unstructured_context_will_not_fix_v2",
            "verdict": "supported_as_rejection_of_default",
            "evidence": "The first V2 input expansion did not broaden the dominant thesis, while a 15% table reduction can remove only repeated or reconstructable fields.",
            "limit": "Specific complete data families may still add value and require separate ablations.",
        },
    ]


def pct(value: Any, digits: int = 2) -> str:
    parsed = base.as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.{digits}f}%"


def pp(value: Any, digits: int = 2) -> str:
    parsed = base.as_float(value)
    return "n/a" if parsed is None else f"{parsed:.{digits}f}%"


def markdown_table(headers: Sequence[str], rows: Iterable[Sequence[Any]]) -> list[str]:
    output = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    output.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return output


def find_summary(rows: Sequence[dict[str, Any]], track: str, model_id: str = "all") -> dict[str, Any]:
    return next(row for row in rows if row["track"] == track and row["model_id"] == model_id)


def find_rule(rows: Sequence[dict[str, Any]], track: str, rule: str) -> dict[str, Any]:
    return next(
        row
        for row in rows
        if row["track"] == track and row["rule"] == rule and row["model_id"] == "all"
    )


def render_report(
    failure_summary: Sequence[dict[str, Any]],
    rule_summary: Sequence[dict[str, Any]],
    structural_rows: Sequence[dict[str, Any]],
    structural: dict[str, Any],
    compaction: dict[str, Any],
    contract: Sequence[dict[str, Any]],
    hypotheses: Sequence[dict[str, Any]],
    data_families: Sequence[dict[str, Any]],
    interventions: Sequence[dict[str, Any]],
) -> str:
    weekly = find_summary(failure_summary, "weekly")
    monthly = find_summary(failure_summary, "monthly")
    lines = [
        "# How CapitalBench Should Improve Portfolio V2",
        "",
        "Generated on: `2026-07-17`",
        "",
        "Protocol: `docs/v2_improvement_research_protocol.md`",
        "",
        "Status: pre-resolution research. The active July 13 V2 pilot is frozen and its interim or final returns were not used.",
        "",
        "## Bottom Line",
        "",
        "The most important V2.1 change is not simply more market data. CapitalBench must make the model's candidate search auditable and systematic before asking it to allocate. Historical V1 decisions lose most of their available return before weighting: the best submitted holding is already far below the best allowed option. V2 still exposes only the final selected holdings, so it cannot distinguish a considered rejection from an option the model never evaluated.",
        "",
        f"The first V2 treatment also produced an average {structural['mean_pairwise_overlap_v2_pct']:.1f}% pairwise allocation overlap across models, versus {structural['mean_pairwise_overlap_v1_pct']:.1f}% in paired V1. Every model chose OIL and/or ENERGY, no model allocated to SPY, and the prompt's soft correlation instruction allowed a 100% ENERGY/OIL portfolio. V2 improved instrumentation, but it did not solve candidate breadth, calibration, or correlated-thesis control.",
        "",
        "The recommended V2.1 treatment is one single-turn call with a compact nonredundant table, a required 6-8 candidate ledger spanning economic-exposure groups, forecasts for SPY and all finalists, a holding-level SPY hurdle, and a hard 50% cap on one economic exposure. Confidence-based sizing should wait until enough prospective forecasts exist to calibrate it.",
        "",
        "## Where Historical Return Was Lost",
        "",
        "`Search regret` is the best allowed return minus the best return among a model's submitted holdings. `Sizing regret` is the best submitted holding minus the submitted weighted portfolio. Both are hindsight diagnostics, not tradable strategies.",
        "",
    ]
    lines.extend(
        markdown_table(
            ["Track", "Decisions", "Model alpha", "Total regret", "Search regret", "Sizing regret", "Search share", "Top-5 capture"],
            [
                [
                    "Weekly",
                    weekly["decisions"],
                    pct(weekly["mean_alpha"]),
                    pct(weekly["mean_total_oracle_regret"]),
                    pct(weekly["mean_search_regret"]),
                    pct(weekly["mean_sizing_regret"]),
                    pct(weekly["search_share_of_regret"]),
                    pct(weekly["top5_capture_rate"]),
                ],
                [
                    "Monthly",
                    monthly["decisions"],
                    pct(monthly["mean_alpha"]),
                    pct(monthly["mean_total_oracle_regret"]),
                    pct(monthly["mean_search_regret"]),
                    pct(monthly["mean_sizing_regret"]),
                    pct(monthly["search_share_of_regret"]),
                    pct(monthly["top5_capture_rate"]),
                ],
            ],
        )
    )
    lines.extend(
        [
            "",
            f"The selected holdings themselves do not show positive discrimination: equal-weighting each submitted selected set produced {pct(weekly['mean_equal_selected_alpha'])} weekly alpha and {pct(monthly['mean_equal_selected_alpha'])} monthly alpha. Relative to equal weight across the whole risky universe, the selected sets added {pct(weekly['mean_equal_selected_edge_vs_universe'])} weekly and {pct(monthly['mean_equal_selected_edge_vs_universe'])} monthly. This is why weight optimization alone cannot repair V2.",
            "",
            "The 29 weekly and 15 monthly rounds overlap, and several model decisions share each market episode. These averages are stage diagnostics rather than independent observations or evidence that the hindsight-best option was knowable.",
            "",
            "## Portfolio-Rule Counterfactuals",
            "",
            "These rules reuse the exact submitted candidate set. They diagnose weighting and concentration; they do not establish a new predictive strategy.",
            "",
        ]
    )
    rule_names = (
        ("submitted", "Submitted"),
        ("equal_selected", "Equal selected"),
        ("cap_active_50_to_spy", "50% holding cap"),
        ("cap_active_35_to_spy", "35% holding cap"),
        ("spy_reserve_25", "25% SPY reserve"),
        ("spy_reserve_50", "50% SPY reserve"),
    )
    lines.extend(
        markdown_table(
            ["Rule", "Weekly alpha", "Weekly change", "Monthly alpha", "Monthly change"],
            [
                [
                    label,
                    pct(find_rule(rule_summary, "weekly", rule)["mean_alpha"]),
                    pct(find_rule(rule_summary, "weekly", rule)["mean_improvement_vs_submitted"]),
                    pct(find_rule(rule_summary, "monthly", rule)["mean_alpha"]),
                    pct(find_rule(rule_summary, "monthly", rule)["mean_improvement_vs_submitted"]),
                ]
                for rule, label in rule_names
            ],
        )
    )
    lines.extend(
        [
            "",
            "A fixed SPY sleeve predictably moves a negative-alpha portfolio closer to zero, but it cannot create selection skill: its alpha is exactly a scaled version of submitted alpha. Holding caps and equal weighting are useful controls only if their paired improvements are stable; the moving-block intervals in `portfolio_rule_summary.csv` show the uncertainty.",
            "",
            "## What V2 Actually Changed",
            "",
        ]
    )
    lines.extend(
        markdown_table(
            ["Model", "V1 to V2 overlap", "Turnover", "V2 max weight", "Effective holdings", "SPY", "Forecast alpha", "Confidence"],
            [
                [
                    row["model_id"],
                    pct(row["holding_jaccard"]),
                    pp(row["allocation_turnover_pct"]),
                    pp(row["v2_max_weight_pct"]),
                    f"{row['v2_effective_holdings']:.2f}",
                    pp(row["v2_spy_weight_pct"]),
                    pp(row["expected_alpha_pct"]),
                    f"{row['confidence']:.2f}",
                ]
                for row in structural_rows
            ],
        )
    )
    lines.extend(
        [
            "",
            f"The V2 portfolio forecasts average {structural['portfolio_forecast_mean_pct']:.2f}% while SPY forecasts average {structural['benchmark_forecast_mean_pct']:.2f}%. The four confidence values cluster tightly around {structural['confidence_mean']:.2f}. Until outcomes accumulate, those numbers are declarations, not calibrated probabilities.",
            "",
            f"V2 input tokens increased {structural['mean_v2_input_token_increase_pct']:.1f}% over paired V1. Despite the instruction to separate the latest five sessions from the prior sixteen, models placed an average {structural['mean_v2_allocation_top_recent_quintile_pct']:.1f}% in the latest-window top quintile and only {structural['mean_v2_allocation_top_prior_quintile_pct']:.1f}% in the prior-window top quintile. This does not prove the recent choices were wrong before resolution, but it shows that the new table did not prevent convergence on the most recent oil/energy move.",
            "",
            "Explicit response text used the requested evidence unevenly:",
            "",
        ]
    )
    lines.extend(
        markdown_table(
            ["Evidence field", "Models explicitly referencing it"],
            [
                [field.replace("_", " "), f"{count}/4"]
                for field, count in structural["explicit_usage_model_counts"].items()
            ],
        )
    )
    lines.extend(
        [
            "",
            "Keyword traces are conservative, but they show why adding fields is not the same as using them. The model-facing contract should make comparison fields auditable rather than relying on narrative rationales.",
            "",
            "## Decision-Table Audit",
            "",
            f"The V2 context has {compaction['rows']} rows and {compaction['current_columns']} columns. A nonredundant research variant retains every unique numeric signal in {compaction['compact_columns']} columns and is {compaction['character_reduction_pct']:.1f}% smaller. Five-session raw return and five-session SPY-relative return have within-round rank correlation {compaction['return_5s_active_5s_rank_correlation']:.3f}; with the SPY return already in the header, one is mechanically reconstructable from the other. The date is repeated on every row and pass status is repeated on {compaction['pass_status_rows']} rows.",
            "",
            "The compact variant is not yet a benchmark input. It demonstrates that V2 can reduce retrieval burden without deleting an option or adding a recommendation score.",
            "",
            "## Contract Gaps",
            "",
        ]
    )
    lines.extend(
        markdown_table(
            ["Check", "Present", "Interpretation"],
            [[row["check"].replace("_", " "), "Yes" if row["present"] else "No", row["interpretation"]] for row in contract],
        )
    )
    lines.extend(["", "## Hypothesis Results", ""])
    lines.extend(
        markdown_table(
            ["Hypothesis", "Verdict", "Evidence", "Limit"],
            [
                [
                    row["hypothesis"].replace("_", " "),
                    row["verdict"].replace("_", " "),
                    row["evidence"],
                    row["limit"],
                ]
                for row in hypotheses
            ],
        )
    )
    lines.extend(["", "## Evidence-Ranked Interventions", ""])
    lines.extend(
        markdown_table(
            ["Priority", "Intervention", "Rating", "Why"],
            [[row["priority"], row["intervention"].replace("_", " "), row["rating"], row["evidence"]] for row in interventions],
        )
    )
    lines.extend(["", "## Additional Data", ""])
    lines.extend(
        markdown_table(
            ["Data family", "Score / 25", "Rating", "Decision"],
            [
                [row["data_family"].replace("_", " "), row["total_25"], row["rating"], row["reason"]]
                for row in sorted(data_families, key=lambda item: (-int(item["total_25"]), str(item["data_family"])))
            ],
        )
    )
    lines.extend(
        [
            "",
            "Research supports disciplined use of text and event information, not indiscriminate context expansion. News-derived language-model signals have shown out-of-sample return information, while separate work finds that LLMs over-extrapolate historical stock returns and produce optimistic, narrow forecasts. See [Lopez-Lira and Tang](https://arxiv.org/abs/2304.07619) and [Chen et al.](https://arxiv.org/abs/2409.11540). Short-horizon reversal and medium-horizon momentum also operate at different horizons, so V2 should force a continuation-versus-reversal comparison rather than treating one trailing return as universally directional: [Lehmann](https://www.nber.org/papers/w2533) and [Jegadeesh and Titman](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x).",
            "",
            "The V2 confidence field should be treated as an uncalibrated forecast. Research documents overconfidence in post-aligned models, while live forecasting benchmarks rely on proper scores and many resolved questions rather than trusting verbal confidence directly: [Zhang et al.](https://arxiv.org/abs/2404.02655) and [ForecastBench methodology](https://www.forecastbench.org/docs/).",
            "",
            "Analyst revisions and option-implied information can contain return information, but CapitalBench uses heterogeneous ETFs and macro assets. Coverage and licensing must be solved before those fields can be fair model inputs. Primary examples include [Asquith, Mikhail, and Au](https://www.nber.org/papers/w9246) and [Muravyev, Pearson, and Pollet](https://doi.org/10.2139/ssrn.2851560).",
            "",
            "## Proposed V2.1 Contract",
            "",
            "1. Keep one single-turn, non-agentic call and the complete 70-option universe.",
            "2. Replace redundant table fields with the compact decision table; keep frozen option order.",
            "3. Add a static economic-exposure cluster to every option and a compact scheduled-event table.",
            "4. Require a 6-8 row candidate ledger before the final portfolio. It must include SPY, span at least four economic-exposure clusters, and retain rejected finalists.",
            "5. Record low/base/high return forecasts for SPY and every finalist, the evidence used, continuation case, reversal case, and forecast invalidation.",
            "6. Permit an active holding only when its base forecast exceeds the SPY base forecast. If none qualify, 100% SPY is valid.",
            "7. Cap one economic exposure at 50%, including equivalent bets expressed through different asset classes. Do not use confidence to loosen the cap yet.",
            "8. Save the candidate ledger and forecasts for calibration; continue scoring only the final frozen portfolio.",
            "",
            "This staged format is an auditable decision scaffold, not hidden chain-of-thought. Long-context research shows that information position can materially affect retrieval, and table research documents incorrect or omitted values even when structure is understood: [Liu et al.](https://aclanthology.org/2024.tacl-1.9/) and [Yang et al.](https://aclanthology.org/2026.acl-long.762/).",
            "",
            "## What Not To Claim Yet",
            "",
            "- The unresolved V2 forecasts cannot be called accurate or inaccurate.",
            "- A candidate ledger, compact table, or exposure cap has not yet demonstrated positive alpha.",
            "- More reasoning tokens are not proven to improve these portfolios.",
            "- A fixed SPY reserve reduces underperformance mechanically but does not make the model a better selector.",
            "- Historical exact winners are not a valid prompt-tuning target.",
            "",
            "## Prospective Test",
            "",
            "After the July 20 V2 decision is recorded, freeze one combined V2.1 treatment and compare it with unchanged V2 on the same future weekly date, models, universe, and prices. The primary endpoint is paired realized alpha. Candidate capture, forecast rank correlation, point error, interval coverage, Brier score, and exposure concentration explain the result. One round is a screen; adoption requires multiple non-overlapping weekly windows and later monthly confirmation.",
            "",
            "No second model call, provider search, retrospective rerun, or monthly V2.1 call is required for the first screen.",
            "",
            "## Reproducibility",
            "",
            "```bash",
            "python scripts/analyze_model_predictability.py --rounds-dir rounds --output output/model_performance_predictability --report-copy docs/model_performance_predictability_report.md",
            "python scripts/analyze_v2_improvements.py --rounds-dir rounds --output output/v2_improvement_research --report-copy docs/v2_improvement_research_report.md",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds-dir", type=Path, default=Path("rounds"))
    parser.add_argument("--output", type=Path, default=Path("output/v2_improvement_research"))
    parser.add_argument("--report-copy", type=Path, default=Path("docs/v2_improvement_research_report.md"))
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    rounds, _assets, _models, _traces, eligibility, _summaries = base.build_dataset(args.rounds_dir)
    failure_rows, failure_summary = analyze_historical_failures(rounds)
    rule_rows, rule_summary = analyze_portfolio_rules(rounds)
    structural_rows, selected_rows, overlap_rows, structural = analyze_v2_structure(args.rounds_dir)
    compaction = build_compact_context(args.rounds_dir, args.output)
    contract = prompt_contract_audit(args.rounds_dir)
    data_families = data_family_matrix()
    literature = literature_evidence()
    interventions = intervention_matrix(failure_summary, structural)
    hypotheses = hypothesis_results(failure_summary, structural)

    base.write_csv(args.output / "failure_decomposition.csv", failure_rows)
    base.write_csv(args.output / "failure_summary.csv", failure_summary)
    base.write_csv(args.output / "portfolio_counterfactuals.csv", rule_rows)
    base.write_csv(args.output / "portfolio_rule_summary.csv", rule_summary)
    base.write_csv(args.output / "v1_v2_structural_comparison.csv", structural_rows)
    base.write_csv(args.output / "v2_selected_holding_features.csv", selected_rows)
    base.write_csv(args.output / "cross_model_overlap.csv", overlap_rows)
    base.write_csv(args.output / "v2_explicit_field_usage.csv", structural.pop("usage_rows"))
    base.write_csv(args.output / "prompt_contract_audit.csv", contract)
    base.write_csv(args.output / "data_family_matrix.csv", data_families)
    base.write_csv(args.output / "literature_evidence.csv", literature)
    base.write_csv(args.output / "intervention_matrix.csv", interventions)
    base.write_csv(args.output / "hypothesis_results.csv", hypotheses)
    (args.output / "context_compaction.json").write_text(
        json.dumps(compaction, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    summary = {
        "eligible_v1_rounds": len(rounds),
        "eligible_weekly_rounds": sum(record.track == "weekly" for record in rounds),
        "eligible_monthly_rounds": sum(record.track == "monthly" for record in rounds),
        "historical_model_decisions": len(failure_rows),
        "active_v2_outcomes_used": False,
        "v2_round_status": "frozen_unresolved_structural_evidence_only",
        "failure_summary": failure_summary,
        "v2_structural_summary": structural,
        "context_compaction": compaction,
        "eligible_round_audit_rows": len(eligibility),
    }
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    report = render_report(
        failure_summary,
        rule_summary,
        structural_rows,
        structural,
        compaction,
        contract,
        hypotheses,
        data_families,
        interventions,
    )
    (args.output / "report.md").write_text(report, encoding="utf-8", newline="\n")
    args.report_copy.parent.mkdir(parents=True, exist_ok=True)
    args.report_copy.write_text(report, encoding="utf-8", newline="\n")

    print(f"eligible_v1_rounds={len(rounds)} model_decisions={len(failure_rows)}")
    print(f"active_v2_outcomes_used=false paired_models={structural['paired_models']}")
    print(f"wrote analysis to {args.output}")
    print(f"wrote report copy to {args.report_copy}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

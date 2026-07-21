#!/usr/bin/env python3
"""Evaluate frozen quality-pullback overlays on historical model portfolios."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.analyze_model_predictability import RoundRecord, build_dataset  # noqa: E402
from scripts.analyze_historical_decision_context import (  # noqa: E402
    as_float,
    percentile_ranks,
    selection_probabilities,
)


DEFAULT_CONFIG = ROOT / "experiments" / "model-quality-hybrid-screen-2026-07-21.yaml"
CANONICAL_REPORT = ROOT / "docs" / "model_quality_hybrid_screen_report.md"
CANONICAL_SUMMARY = ROOT / "research" / "results" / "model-quality-hybrid-screen-2026-07-21.json"


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"invalid config: {path}")
    return payload


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    columns = list(rows[0])
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: f"{value:.10f}" if isinstance(value, float) and math.isfinite(value) else value
                    for key, value in row.items()
                }
            )


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def quality_scores(config: dict[str, Any]) -> dict[tuple[str, str], float]:
    rows = read_csv(ROOT / str(config["feature_panel"]))
    weights = config["quality_signal"]
    fields = {
        "recent_active_reversal_rank": "rank_recent_active_reversal",
        "prior_active_rank": "rank_prior_active_return",
        "low_volatility_rank": "rank_low_volatility",
        "shallow_drawdown_rank": "rank_shallow_drawdown",
    }
    result: dict[tuple[str, str], float] = {}
    for row in rows:
        result[(row["round_id"], row["option_id"])] = sum(
            float(row[fields[name]]) * float(weight) for name, weight in weights.items()
        )
    return result


def normalize(allocation: dict[str, float]) -> dict[str, float]:
    total = sum(max(0.0, float(value)) for value in allocation.values())
    if total <= 0:
        return {}
    return {key: max(0.0, float(value)) * 100.0 / total for key, value in allocation.items() if value > 0.0}


def portfolio_return(allocation: dict[str, float], returns: dict[str, float]) -> float:
    return sum(float(weight) / 100.0 * float(returns[option_id]) for option_id, weight in allocation.items())


def quality_allocation(
    option_ids: Sequence[str],
    scores: dict[str, float],
    count: int,
) -> dict[str, float]:
    ordered = [option_id for option_id in option_ids if option_id in scores]
    probabilities = selection_probabilities([scores[item] for item in ordered], count)
    return {item: probability * 100.0 / count for item, probability in zip(ordered, probabilities) if probability > 0}


def quality_sleeve(
    original: dict[str, float],
    mechanical: dict[str, float],
    original_weight: float,
    quality_weight: float,
) -> dict[str, float]:
    option_ids = set(original) | set(mechanical)
    return normalize(
        {
            option_id: original_weight * original.get(option_id, 0.0)
            + quality_weight * mechanical.get(option_id, 0.0)
            for option_id in option_ids
        }
    )


def union_rerank(
    original: dict[str, float],
    mechanical: dict[str, float],
    scores: dict[str, float],
    model_weight: float,
    quality_weight: float,
    count: int,
) -> dict[str, float]:
    candidates = sorted(set(original) | set(mechanical))
    conviction_ranks = percentile_ranks([original.get(item, 0.0) for item in candidates])
    combined = [
        model_weight * float(conviction_rank) + quality_weight * float(scores.get(option_id, 0.5))
        for option_id, conviction_rank in zip(candidates, conviction_ranks)
    ]
    probabilities = selection_probabilities(combined, count)
    return {item: probability * 100.0 / count for item, probability in zip(candidates, probabilities) if probability > 0}


def within_holdings_tilt(
    original: dict[str, float],
    scores: dict[str, float],
    minimum_multiplier: float,
    quality_multiplier: float,
    cash_multiplier: float,
) -> dict[str, float]:
    tilted: dict[str, float] = {}
    for option_id, weight in original.items():
        multiplier = cash_multiplier if option_id == "CASH" else minimum_multiplier + quality_multiplier * scores.get(option_id, 0.5)
        tilted[option_id] = float(weight) * multiplier
    return normalize(tilted)


def overlap_count(original: dict[str, float], mechanical: dict[str, float]) -> int:
    held = {key for key, value in original.items() if value > 0.0 and key != "CASH"}
    selected = {key for key, value in mechanical.items() if value > 0.0}
    return len(held & selected)


def reconstruct(config: dict[str, Any]) -> tuple[list[dict[str, Any]], list[RoundRecord]]:
    rounds, _assets, _models, _traces, _eligibility, _summaries = build_dataset(ROOT / str(config["rounds_dir"]))
    scores_by_key = quality_scores(config)
    count = int(config["selection"]["assets"])
    transformations = config["transformations"]
    rows: list[dict[str, Any]] = []
    for round_record in rounds:
        returns = {str(row["option_id"]): float(row["future_return"]) for row in round_record.assets}
        risky_ids = [str(row["option_id"]) for row in round_record.assets if not row["is_cash"]]
        scores = {
            option_id: scores_by_key[(round_record.round_id, option_id)]
            for option_id in risky_ids
            if (round_record.round_id, option_id) in scores_by_key
        }
        if len(scores) < math.ceil(len(risky_ids) * 0.9):
            continue
        mechanical = quality_allocation(risky_ids, scores, count)
        mechanical_return = portfolio_return(mechanical, returns)
        for model in round_record.models:
            original = normalize(model.allocation)
            if not original or any(option_id not in returns for option_id in original):
                continue
            original_return = portfolio_return(original, returns)
            allocations = {
                "quality_sleeve_25": quality_sleeve(
                    original,
                    mechanical,
                    float(transformations["quality_sleeve_25"]["original_weight"]),
                    float(transformations["quality_sleeve_25"]["quality_weight"]),
                ),
                "conviction_quality_union": union_rerank(
                    original,
                    mechanical,
                    scores,
                    float(transformations["conviction_quality_union"]["model_conviction_rank"]),
                    float(transformations["conviction_quality_union"]["quality_rank"]),
                    int(transformations["conviction_quality_union"]["assets"]),
                ),
                "within_holdings_quality_tilt": within_holdings_tilt(
                    original,
                    scores,
                    float(transformations["within_holdings_quality_tilt"]["minimum_multiplier"]),
                    float(transformations["within_holdings_quality_tilt"]["quality_multiplier"]),
                    float(transformations["within_holdings_quality_tilt"]["cash_multiplier"]),
                ),
            }
            weighted_quality = sum(
                weight / 100.0 * scores.get(option_id, 0.5) for option_id, weight in original.items()
            )
            base = {
                "round_id": round_record.round_id,
                "track": round_record.track,
                "split": round_record.split,
                "entry_date": round_record.entry_date.isoformat(),
                "exit_date": round_record.exit_date.isoformat(),
                "model_id": model.model_id,
                "sp500_return": round_record.sp500_return,
                "original_return": original_return,
                "original_alpha": original_return - round_record.sp500_return,
                "quality_return": mechanical_return,
                "quality_alpha": mechanical_return - round_record.sp500_return,
                "model_quality_overlap": overlap_count(original, mechanical),
                "model_weighted_quality_score": weighted_quality,
                "spy_regime": "up" if round_record.sp500_return >= 0.0 else "down",
                "original_holdings": ",".join(sorted(original)),
                "quality_holdings": ",".join(sorted(mechanical)),
            }
            for name, allocation in allocations.items():
                transformed_return = portfolio_return(allocation, returns)
                rows.append(
                    {
                        **base,
                        "transformation": name,
                        "transformed_return": transformed_return,
                        "transformed_alpha": transformed_return - round_record.sp500_return,
                        "improvement": transformed_return - original_return,
                        "improved": transformed_return > original_return,
                        "transformed_holdings": ",".join(sorted(allocation)),
                    }
                )
    return rows, rounds


def mean_or_none(values: Iterable[float]) -> float | None:
    present = list(values)
    return statistics.mean(present) if present else None


def nonoverlap_round_ids(rows: Sequence[dict[str, Any]]) -> list[str]:
    dates: dict[str, tuple[date, date]] = {}
    for row in rows:
        dates[row["round_id"]] = (date.fromisoformat(row["entry_date"]), date.fromisoformat(row["exit_date"]))
    selected: list[str] = []
    last_exit: date | None = None
    for round_id, (entry, exit_date) in sorted(dates.items(), key=lambda item: (item[1][0], item[0])):
        if last_exit is None or entry >= last_exit:
            selected.append(round_id)
            last_exit = exit_date
    return selected


def round_means(rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row["round_id"]].append(row)
    return [
        {
            "round_id": round_id,
            "entry_date": items[0]["entry_date"],
            "exit_date": items[0]["exit_date"],
            "mean_improvement": statistics.mean(float(row["improvement"]) for row in items),
        }
        for round_id, items in grouped.items()
    ]


def aggregate(rows: Sequence[dict[str, Any]], gate: dict[str, Any]) -> dict[str, Any]:
    if not rows:
        return {}
    per_model: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        per_model[row["model_id"]].append(float(row["improvement"]))
    positive_models = {model_id: statistics.mean(values) for model_id, values in per_model.items() if statistics.mean(values) > 0.0}
    by_round = round_means(rows)
    nonoverlap_ids = set(nonoverlap_round_ids(rows))
    independent = [row for row in by_round if row["round_id"] in nonoverlap_ids]
    leave_best = list(by_round)
    if leave_best:
        leave_best.remove(max(leave_best, key=lambda row: float(row["mean_improvement"])))
    result = {
        "pairs": len(rows),
        "rounds": len(by_round),
        "models": len(per_model),
        "mean_original_return": statistics.mean(float(row["original_return"]) for row in rows),
        "mean_transformed_return": statistics.mean(float(row["transformed_return"]) for row in rows),
        "mean_original_alpha": statistics.mean(float(row["original_alpha"]) for row in rows),
        "mean_transformed_alpha": statistics.mean(float(row["transformed_alpha"]) for row in rows),
        "mean_improvement": statistics.mean(float(row["improvement"]) for row in rows),
        "pair_improvement_rate": sum(bool(row["improved"]) for row in rows) / len(rows),
        "positive_models": positive_models,
        "positive_model_share": len(positive_models) / len(per_model),
        "nonoverlap_rounds": len(independent),
        "nonoverlap_round_ids": sorted(nonoverlap_ids),
        "nonoverlap_mean_improvement": mean_or_none(float(row["mean_improvement"]) for row in independent),
        "leave_best_round_out_improvement": mean_or_none(float(row["mean_improvement"]) for row in leave_best),
    }
    result["passes_gate"] = (
        result["mean_improvement"] >= float(gate["minimum_mean_return_improvement"])
        and result["mean_transformed_alpha"] > float(gate["minimum_resulting_alpha"])
        and result["pair_improvement_rate"] > float(gate["minimum_pair_improvement_rate"])
        and result["positive_model_share"] > float(gate["minimum_positive_model_share"])
        and result["nonoverlap_rounds"] >= int(gate["minimum_nonoverlap_rounds"])
        and float(result["nonoverlap_mean_improvement"] or -1.0) > float(gate["minimum_nonoverlap_improvement"])
        and float(result["leave_best_round_out_improvement"] or -1.0) > float(gate["minimum_leave_best_round_out_improvement"])
    )
    return result


def grouped_diagnostics(rows: Sequence[dict[str, Any]], field: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row[field])].append(row)
    return [
        {
            field: key,
            "pairs": len(items),
            "mean_improvement": statistics.mean(float(row["improvement"]) for row in items),
            "mean_transformed_alpha": statistics.mean(float(row["transformed_alpha"]) for row in items),
            "improvement_rate": sum(bool(row["improved"]) for row in items) / len(items),
        }
        for key, items in sorted(grouped.items())
    ]


def analyze(config: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows, rounds = reconstruct(config)
    gate = config["gate"]
    summaries: list[dict[str, Any]] = []
    diagnostics: dict[str, Any] = {}
    for track in ("weekly", "monthly"):
        for transformation in config["transformations"]:
            subset = [row for row in rows if row["track"] == track and row["transformation"] == transformation]
            overall = aggregate(subset, gate)
            discovery = aggregate([row for row in subset if row["split"] == "discovery"], gate)
            holdout = aggregate([row for row in subset if row["split"] == "holdout"], gate)
            passes = (
                track == gate["eligible_track"]
                and bool(overall.get("passes_gate"))
                and float(holdout.get("mean_improvement") or -1.0) > float(gate["minimum_holdout_improvement"])
            )
            summaries.append(
                {
                    "track": track,
                    "transformation": transformation,
                    "passes_gate": passes,
                    "overall": overall,
                    "discovery": discovery,
                    "holdout": holdout,
                }
            )
            key = f"{track}:{transformation}"
            diagnostics[key] = {
                "by_model": grouped_diagnostics(subset, "model_id"),
                "by_spy_regime": grouped_diagnostics(subset, "spy_regime"),
                "by_overlap": grouped_diagnostics(subset, "model_quality_overlap"),
            }
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "decision": "advance_to_prompt_replay" if any(row["passes_gate"] for row in summaries) else "rejected",
        "passing_transformations": [
            f"{row['track']}:{row['transformation']}" for row in summaries if row["passes_gate"]
        ],
        "eligible_rounds": len({row["round_id"] for row in rows}),
        "model_decisions": len({(row["round_id"], row["model_id"]) for row in rows}),
        "summaries": summaries,
        "diagnostics": diagnostics,
        "official_score_eligible": False,
        "production_impact": "none",
    }
    directory = output_dir(config)
    write_csv(directory / "pair_results.csv", rows)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return rows, summary


def pct(value: Any) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.2f}%"


def render_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Model-Quality Hybrid Screen Results",
        "",
        f"Decision: **{summary['decision']}**",
        "",
        f"- Eligible rounds: {summary['eligible_rounds']}",
        f"- Reconstructed model decisions: {summary['model_decisions']}",
        "- New model calls: 0",
        "",
        "## Frozen Transformations",
        "",
        "| Track | Transformation | Return change | Resulting alpha | Pair wins | Positive models | Holdout change | Non-overlap change | Leave-best-out | Gate |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in summary["summaries"]:
        overall = row["overall"]
        holdout = row["holdout"]
        lines.append(
            "| {track} | {name} | {change} | {alpha} | {wins} | {models} | {holdout} | {nonoverlap} ({rounds}) | {leave_best} | {gate} |".format(
                track=row["track"],
                name=row["transformation"].replace("_", " "),
                change=pct(overall.get("mean_improvement")),
                alpha=pct(overall.get("mean_transformed_alpha")),
                wins=pct(overall.get("pair_improvement_rate")),
                models=pct(overall.get("positive_model_share")),
                holdout=pct(holdout.get("mean_improvement")),
                nonoverlap=pct(overall.get("nonoverlap_mean_improvement")),
                rounds=overall.get("nonoverlap_rounds", 0),
                leave_best=pct(overall.get("leave_best_round_out_improvement")),
                gate="pass" if row["passes_gate"] else "fail",
            )
        )
    lines.extend(["", "## Weekly Model Attribution", ""])
    for row in (item for item in summary["summaries"] if item["track"] == "weekly"):
        key = f"weekly:{row['transformation']}"
        lines.extend(
            [
                f"### {row['transformation'].replace('_', ' ').title()}",
                "",
                "| Model | Pairs | Return change | Resulting alpha | Pair wins |",
                "| --- | ---: | ---: | ---: | ---: |",
            ]
        )
        for item in summary["diagnostics"][key]["by_model"]:
            lines.append(
                f"| {item['model_id']} | {item['pairs']} | {pct(item['mean_improvement'])} | {pct(item['mean_transformed_alpha'])} | {pct(item['improvement_rate'])} |"
            )
        lines.extend(["", "SPY regime attribution:", "", "| Regime | Pairs | Return change | Resulting alpha |", "| --- | ---: | ---: | ---: |"])
        for item in summary["diagnostics"][key]["by_spy_regime"]:
            lines.append(
                f"| {item['spy_regime']} | {item['pairs']} | {pct(item['mean_improvement'])} | {pct(item['mean_transformed_alpha'])} |"
            )
        lines.append("")
    lines.extend(
        [
            "## Interpretation",
            "",
            "Historical reuse makes this a reject-only screen. A passing transformation authorizes only the separately frozen bounded private prompt replay; it does not alter production V2 or official scores.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()
    config = load_yaml(args.config)
    _rows, summary = analyze(config)
    report = render_report(summary)
    (output_dir(config) / "report.md").write_text(report, encoding="utf-8")
    CANONICAL_REPORT.write_text(report, encoding="utf-8")
    CANONICAL_SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    CANONICAL_SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": summary["decision"], "passing_transformations": summary["passing_transformations"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

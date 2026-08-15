#!/usr/bin/env python3
"""Run the zero-call, post-hoc V3A anti-extrapolation compliance diagnostic."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import run_portfolio_v3_replay as v3


DEFAULT_CONFIG = v3.DEFAULT_CONFIG
DEFAULT_REPORT = v3.ROOT / "docs" / "portfolio_v3_anti_extrapolation_compliance_diagnostic.md"
DEFAULT_SUMMARY = (
    v3.ROOT
    / "research"
    / "results"
    / "portfolio-v3-anti-extrapolation-compliance-diagnostic-2026-08-13.json"
)

MINIMUM_BEAT_SPY_PROBABILITY_PCT = 55.0


def eligible_assessments(assessments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep only confident overreaction calls, preserving the model's ranking."""

    return [
        row
        for row in sorted(assessments, key=lambda value: int(value["rank"]))
        if str(row["recent_return_interpretation"]) == "overreaction"
        and float(row["p_beat_spy_pct"]) >= MINIMUM_BEAT_SPY_PROBABILITY_PCT
    ]


def _mean(rows: Iterable[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return statistics.mean(values) if values else None


def _records(config: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    records_dir = v3.output_dir(config) / "records"
    return {
        (str(record["replay_id"]), str(record["model_id"])): record
        for record in (
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(records_dir.glob("*.json"))
        )
    }


def candidate_calibration(config: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    episodes = v3.episode_index(config)
    for record in _records(config).values():
        if not record.get("valid"):
            continue
        episode = episodes[str(record["replay_id"])]
        _, returns_path, _ = v3.control_paths(episode)
        returns = {
            str(row["option_id"]): float(row["return"]) * 100.0
            for row in v3.read_csv(returns_path)
        }
        spy_return = returns["SP500"]
        for assessment in record["parsed_json"]["candidate_assessments"]:
            option_id = str(assessment["option_id"])
            if option_id not in returns:
                continue
            rows.append(
                {
                    "interpretation": str(assessment["recent_return_interpretation"]),
                    "probability": float(assessment["p_beat_spy_pct"]),
                    "alpha": returns[option_id] - spy_return,
                }
            )

    def describe(predicate: Any) -> dict[str, Any]:
        subset = [row for row in rows if predicate(row)]
        return {
            "candidate_count": len(subset),
            "spy_beat_count": sum(float(row["alpha"]) > 0 for row in subset),
            "spy_beat_rate": (
                sum(float(row["alpha"]) > 0 for row in subset) / len(subset)
                if subset
                else None
            ),
            "mean_alpha_pct": statistics.mean(float(row["alpha"]) for row in subset)
            if subset
            else None,
            "mean_model_probability_pct": statistics.mean(
                float(row["probability"]) for row in subset
            )
            if subset
            else None,
        }

    return {
        "all_candidates": describe(lambda row: True),
        "probability_at_least_55": describe(
            lambda row: float(row["probability"]) >= MINIMUM_BEAT_SPY_PROBABILITY_PCT
        ),
        "overreaction_probability_at_least_55": describe(
            lambda row: row["interpretation"] == "overreaction"
            and float(row["probability"]) >= MINIMUM_BEAT_SPY_PROBABILITY_PCT
        ),
        "continuation_probability_at_least_55": describe(
            lambda row: row["interpretation"] == "supported_continuation"
            and float(row["probability"]) >= MINIMUM_BEAT_SPY_PROBABILITY_PCT
        ),
        "warning": (
            "Candidate rows repeat models and assets within only three periods and are not "
            "independent observations. These descriptive rates cannot support inference."
        ),
    }


def diagnostic_rows(config: dict[str, Any]) -> list[dict[str, Any]]:
    records = _records(config)
    original_rows = {
        (str(row["replay_id"]), str(row["model_id"])): row
        for row in v3.score_rows(config)
    }
    allocations = [float(value) for value in config["portfolio"]["rank_allocations_pct"]]
    rows: list[dict[str, Any]] = []

    for episode in config["episodes"]:
        _, returns_path, _ = v3.control_paths(episode)
        return_rows = v3.read_csv(returns_path)
        returns = {str(row["option_id"]): float(row["return"]) for row in return_rows}
        realized_order = [
            str(row["option_id"])
            for row in sorted(return_rows, key=lambda row: float(row["return"]), reverse=True)
        ]
        realized_top3 = set(realized_order[:3])

        for model_id in config["models"]:
            key = (str(episode["replay_id"]), str(model_id))
            record = records.get(key)
            original = original_rows[key]
            if not record or not record.get("valid") or not original.get("valid"):
                rows.append(
                    {
                        "replay_id": key[0],
                        "model_id": key[1],
                        "valid": False,
                        "provider_error": record.get("provider_error") if record else "missing record",
                    }
                )
                continue

            eligible = eligible_assessments(
                list(record["parsed_json"]["candidate_assessments"])
            )[:3]
            top3 = [str(row["option_id"]) for row in eligible]
            allocation: dict[str, float] = {}
            for index, weight in enumerate(allocations):
                option_id = top3[index] if index < len(top3) else "SP500"
                allocation[option_id] = allocation.get(option_id, 0.0) + weight
            treatment_return = v3._portfolio_return(allocation, returns) * 100.0
            spy_return = returns["SP500"] * 100.0
            control_return = float(original["control_return_pct"])
            original_return = float(original["treatment_return_pct"])
            rows.append(
                {
                    "replay_id": key[0],
                    "model_id": key[1],
                    "valid": True,
                    "top3_option_ids": top3,
                    "allocation": allocation,
                    "spy_return_pct": spy_return,
                    "control_return_pct": control_return,
                    "original_v3a_return_pct": original_return,
                    "reranked_return_pct": treatment_return,
                    "reranked_alpha_pct": treatment_return - spy_return,
                    "change_vs_original_v3a_pct": treatment_return - original_return,
                    "paired_improvement_pct": treatment_return - control_return,
                    "winner_capture": realized_order[0] in top3,
                    "top3_capture": bool(realized_top3 & set(top3)),
                }
            )
    return rows


def summarize(config: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [row for row in rows if row["valid"]]
    by_model: dict[str, Any] = {}
    for model_id in config["models"]:
        subset = [row for row in valid if row["model_id"] == model_id]
        by_model[str(model_id)] = {
            "valid_pairs": len(subset),
            "mean_gated_alpha_pct": _mean(subset, "reranked_alpha_pct"),
            "mean_change_vs_original_v3a_pct": _mean(subset, "change_vs_original_v3a_pct"),
            "mean_paired_improvement_pct": _mean(subset, "paired_improvement_pct"),
        }

    by_period: dict[str, Any] = {}
    for episode in config["episodes"]:
        replay_id = str(episode["replay_id"])
        subset = [row for row in valid if row["replay_id"] == replay_id]
        by_period[replay_id] = {
            "valid_pairs": len(subset),
            "mean_gated_alpha_pct": _mean(subset, "reranked_alpha_pct"),
            "mean_change_vs_original_v3a_pct": _mean(subset, "change_vs_original_v3a_pct"),
            "mean_paired_improvement_pct": _mean(subset, "paired_improvement_pct"),
        }

    invalid = [row for row in rows if not row["valid"]]
    return {
        "diagnostic_id": "portfolio-v3-anti-extrapolation-compliance-diagnostic-2026-08-13",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": "diagnostic_only",
        "calls": 0,
        "post_hoc": True,
        "production_eligible": False,
        "rule": (
            "An active candidate is eligible only when the model labels the setup as "
            "an overreaction and assigns at least a 55% probability of beating SPY. "
            "Preserve model rank among eligible candidates and allocate unused "
            "35/35/30 slots to SPY. A prospective version may also admit continuation "
            "only when it cites machine-verifiable, candidate-specific non-price evidence."
        ),
        "overall": {
            "valid_pairs": len(valid),
            "invalid_pairs": len(invalid),
            "mean_gated_alpha_pct": _mean(valid, "reranked_alpha_pct"),
            "mean_original_v3a_alpha_pct": (
                _mean(valid, "original_v3a_return_pct") - _mean(valid, "spy_return_pct")
                if valid
                else None
            ),
            "mean_change_vs_original_v3a_pct": _mean(valid, "change_vs_original_v3a_pct"),
            "mean_paired_improvement_pct": _mean(valid, "paired_improvement_pct"),
            "spy_beats": sum(float(row["reranked_alpha_pct"]) > 0 for row in valid),
            "nonnegative_alpha_cells": sum(
                float(row["reranked_alpha_pct"]) >= -1e-12 for row in valid
            ),
            "control_improvements": sum(
                float(row["paired_improvement_pct"]) > 0 for row in valid
            ),
            "winner_captures": sum(bool(row["winner_capture"]) for row in valid),
            "top3_captures": sum(bool(row["top3_capture"]) for row in valid),
        },
        "by_model": by_model,
        "by_period": by_period,
        "candidate_calibration": candidate_calibration(config),
        "invalid_operations": [
            {
                "replay_id": row["replay_id"],
                "model_id": row["model_id"],
                "provider_error": row.get("provider_error"),
            }
            for row in invalid
        ],
        "rows": rows,
        "interpretation": (
            "This diagnostic was defined after V3A outcomes were inspected. It identifies "
            "a plausible confidence-and-evidence gate but cannot validate it, "
            "change the frozen V3A decision, or support production adoption."
        ),
    }


def _fmt(value: Any) -> str:
    return "n/a" if value is None else f"{float(value):.2f}%"


def render(summary: dict[str, Any]) -> str:
    overall = summary["overall"]
    lines = [
        "# Portfolio V3 Anti-Extrapolation Compliance Diagnostic",
        "",
        "Decision: **diagnostic only**",
        "",
        "## Question",
        "",
        "What would have happened if V3A had required a meaningful confidence margin, "
        "rejected unaudited continuation, and used SPY whenever too few candidates qualified?",
        "",
        "## Counterfactual Rule",
        "",
        summary["rule"],
        "",
        "The rule makes no additional model calls. It uses only each saved response, but "
        "it was specified after outcomes were inspected and is therefore not a valid "
        "confirmation test.",
        "",
        "## Result",
        "",
        f"- Valid cells: {overall['valid_pairs']}/12",
        f"- Counterfactual mean alpha versus SPY: {_fmt(overall['mean_gated_alpha_pct'])}",
        f"- Original V3A mean alpha on the same cells: {_fmt(overall['mean_original_v3a_alpha_pct'])}",
        f"- Change versus original V3A: {_fmt(overall['mean_change_vs_original_v3a_pct'])}",
        f"- Mean improvement versus saved V2.2 controls: {_fmt(overall['mean_paired_improvement_pct'])}",
        f"- SPY beats: {overall['spy_beats']}/{overall['valid_pairs']}",
        f"- Nonnegative alpha cells: {overall['nonnegative_alpha_cells']}/{overall['valid_pairs']}",
        f"- V2.2 control improvements: {overall['control_improvements']}/{overall['valid_pairs']}",
        f"- Eventual winner captures: {overall['winner_captures']}",
        f"- Eventual top-three captures: {overall['top3_captures']}",
        "",
        "## By Period",
        "",
        "| Set | Valid cells | Alpha vs SPY | Change vs V3A | Improvement vs V2.2 |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for replay_id, row in summary["by_period"].items():
        lines.append(
            f"| {replay_id} | {row['valid_pairs']} | {_fmt(row['mean_gated_alpha_pct'])} | "
            f"{_fmt(row['mean_change_vs_original_v3a_pct'])} | "
            f"{_fmt(row['mean_paired_improvement_pct'])} |"
        )

    lines.extend(
        [
            "",
            "## By Model",
            "",
            "| Model | Valid sets | Alpha vs SPY | Change vs V3A | Improvement vs V2.2 |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for model_id, row in summary["by_model"].items():
        lines.append(
            f"| {model_id} | {row['valid_pairs']} | {_fmt(row['mean_gated_alpha_pct'])} | "
            f"{_fmt(row['mean_change_vs_original_v3a_pct'])} | "
            f"{_fmt(row['mean_paired_improvement_pct'])} |"
        )

    overreaction = summary["candidate_calibration"][
        "overreaction_probability_at_least_55"
    ]
    continuation = summary["candidate_calibration"][
        "continuation_probability_at_least_55"
    ]
    lines.extend(
        [
            "",
            "## Candidate-Level Diagnostic",
            "",
            f"- Confident overreaction calls beat SPY in {overreaction['spy_beat_count']}/"
            f"{overreaction['candidate_count']} rows and averaged "
            f"{_fmt(overreaction['mean_alpha_pct'])} alpha.",
            f"- Confident continuation calls beat SPY in {continuation['spy_beat_count']}/"
            f"{continuation['candidate_count']} rows and averaged "
            f"{_fmt(continuation['mean_alpha_pct'])} alpha.",
            "- These rows repeat assets and models inside only three periods. They are "
            "descriptive and clustered, not independent evidence or a significance test.",
        ]
    )

    lines.extend(
        [
            "",
            "## What This Means",
            "",
            "The candidate slate was not the main failure: it contained the eventual winner "
            "in all three weeks. The strongest remaining lead is to make unsupported "
            "continuation claims auditable, require a confidence margin over SPY, and "
            "allocate every unfilled active slot to SPY.",
            "",
            "This is a design lead, not evidence of a validated strategy. The frozen V3A "
            "decision remains rejected, these three periods must not be tuned again, and any "
            "successor needs a fresh prospective shadow before production consideration.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    args = parser.parse_args()

    config_path = args.config.resolve()
    config = v3.load_config(config_path)
    v3.verify_freeze(config_path, config)
    rows = diagnostic_rows(config)
    summary = summarize(config, rows)
    report_path = args.report.resolve()
    summary_path = args.summary.resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render(summary), encoding="utf-8", newline="\n")
    v3.base.write_json(summary_path, summary)
    print(f"valid_pairs={summary['overall']['valid_pairs']}/12")
    print(f"mean_gated_alpha_pct={summary['overall']['mean_gated_alpha_pct']}")
    print(f"change_vs_original_v3a_pct={summary['overall']['mean_change_vs_original_v3a_pct']}")


if __name__ == "__main__":
    main()

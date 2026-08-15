#!/usr/bin/env python3
"""Audit the post-hoc Portfolio V3 candidate without making model calls."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections.abc import Callable, Iterable, Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from capitalbench.portfolio_v3 import (  # noqa: E402
    DEFAULT_MINIMUM_BEAT_SPY_PROBABILITY_PCT,
    build_portfolio_v3_allocation,
)
from scripts import run_portfolio_v3_replay as replay  # noqa: E402


DEFAULT_CONFIG = replay.DEFAULT_CONFIG
DEFAULT_REPORT = ROOT / "docs" / "portfolio_v3_robustness_report.md"
DEFAULT_SUMMARY = (
    ROOT
    / "research"
    / "results"
    / "portfolio-v3-robustness-diagnostic-2026-08-14.json"
)
SENSITIVITY_THRESHOLDS = (45.0, 50.0, 52.5, 55.0, 57.5, 60.0, 62.5, 65.0, 67.5)


def _mean(rows: Iterable[Mapping[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return statistics.mean(values) if values else None


def load_cells(config: dict[str, Any]) -> list[dict[str, Any]]:
    records_dir = replay.output_dir(config) / "records"
    records = {
        (str(record["replay_id"]), str(record["model_id"])): record
        for record in (
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(records_dir.glob("*.json"))
        )
    }
    original_rows = {
        (str(row["replay_id"]), str(row["model_id"])): row
        for row in replay.score_rows(config)
    }
    cells: list[dict[str, Any]] = []
    for episode in config["episodes"]:
        return_rows = replay.read_csv(replay.control_paths(episode)[1])
        returns = {str(row["option_id"]): float(row["return"]) for row in return_rows}
        realized_order = [
            str(row["option_id"])
            for row in sorted(return_rows, key=lambda row: float(row["return"]), reverse=True)
        ]
        for model_id in config["models"]:
            key = (str(episode["replay_id"]), str(model_id))
            record = records.get(key)
            original = original_rows[key]
            if not record or not record.get("valid") or not original.get("valid"):
                continue
            cells.append(
                {
                    "replay_id": key[0],
                    "model_id": key[1],
                    "assessments": list(record["parsed_json"]["candidate_assessments"]),
                    "returns": returns,
                    "spy_return_pct": returns["SP500"] * 100.0,
                    "control_return_pct": float(original["control_return_pct"]),
                    "original_v3a_return_pct": float(original["treatment_return_pct"]),
                    "realized_top3": realized_order[:3],
                }
            )
    return cells


def evaluate_v3_rule(cells: Sequence[Mapping[str, Any]], threshold: float) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for cell in cells:
        construction = build_portfolio_v3_allocation(
            cell["assessments"],
            minimum_beat_spy_probability_pct=threshold,
        )
        allocation = construction["allocation_pct"]
        treatment_return = sum(
            float(weight) / 100.0 * float(cell["returns"][option_id])
            for option_id, weight in allocation.items()
        ) * 100.0
        selected = list(construction["selected_active_option_ids"])
        rows.append(
            {
                "replay_id": cell["replay_id"],
                "model_id": cell["model_id"],
                "alpha_pct": treatment_return - float(cell["spy_return_pct"]),
                "paired_improvement_pct": treatment_return
                - float(cell["control_return_pct"]),
                "active_positions": len(selected),
                "top3_capture": bool(set(selected) & set(cell["realized_top3"])),
            }
        )
    return rows


def evaluate_predicate_rule(
    cells: Sequence[Mapping[str, Any]], predicate: Callable[[Mapping[str, Any]], bool]
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    slot_weights = (35.0, 35.0, 30.0)
    for cell in cells:
        selected = [
            str(row["option_id"])
            for row in sorted(cell["assessments"], key=lambda row: int(row["rank"]))
            if str(row["option_id"]) != "SP500" and predicate(row)
        ][:3]
        allocation: dict[str, float] = {}
        for index, weight in enumerate(slot_weights):
            option_id = selected[index] if index < len(selected) else "SP500"
            allocation[option_id] = allocation.get(option_id, 0.0) + weight
        treatment_return = sum(
            weight / 100.0 * float(cell["returns"][option_id])
            for option_id, weight in allocation.items()
        ) * 100.0
        rows.append(
            {
                "alpha_pct": treatment_return - float(cell["spy_return_pct"]),
                "active_positions": len(selected),
            }
        )
    return {
        "mean_alpha_pct": _mean(rows, "alpha_pct"),
        "spy_beats": sum(float(row["alpha_pct"]) > 1e-12 for row in rows),
        "nonnegative_alpha_cells": sum(float(row["alpha_pct"]) >= -1e-12 for row in rows),
        "active_cells": sum(int(row["active_positions"]) > 0 for row in rows),
        "active_slots": sum(int(row["active_positions"]) for row in rows),
    }


def summarize_rows(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    models = sorted({str(row["model_id"]) for row in rows})
    periods = sorted({str(row["replay_id"]) for row in rows})
    by_model = {
        model_id: _mean((row for row in rows if row["model_id"] == model_id), "alpha_pct")
        for model_id in models
    }
    by_period = {
        replay_id: _mean((row for row in rows if row["replay_id"] == replay_id), "alpha_pct")
        for replay_id in periods
    }
    leave_one_model_out = {
        model_id: _mean((row for row in rows if row["model_id"] != model_id), "alpha_pct")
        for model_id in models
    }
    leave_one_period_out = {
        replay_id: _mean((row for row in rows if row["replay_id"] != replay_id), "alpha_pct")
        for replay_id in periods
    }
    leave_one_cell_out = []
    for index, omitted in enumerate(rows):
        remaining = [row for position, row in enumerate(rows) if position != index]
        leave_one_cell_out.append(
            {
                "omitted_replay_id": omitted["replay_id"],
                "omitted_model_id": omitted["model_id"],
                "mean_alpha_pct": _mean(remaining, "alpha_pct"),
            }
        )
    return {
        "valid_cells": len(rows),
        "mean_alpha_pct": _mean(rows, "alpha_pct"),
        "mean_paired_improvement_pct": _mean(rows, "paired_improvement_pct"),
        "spy_beats": sum(float(row["alpha_pct"]) > 1e-12 for row in rows),
        "nonnegative_alpha_cells": sum(float(row["alpha_pct"]) >= -1e-12 for row in rows),
        "active_cells": sum(int(row["active_positions"]) > 0 for row in rows),
        "active_slots": sum(int(row["active_positions"]) for row in rows),
        "top3_captures": sum(bool(row["top3_capture"]) for row in rows),
        "positive_models": sum(value is not None and value > 0 for value in by_model.values()),
        "positive_periods": sum(value is not None and value > 0 for value in by_period.values()),
        "worst_period_alpha_pct": min(value for value in by_period.values() if value is not None),
        "by_model_alpha_pct": by_model,
        "by_period_alpha_pct": by_period,
        "leave_one_model_out_alpha_pct": leave_one_model_out,
        "leave_one_period_out_alpha_pct": leave_one_period_out,
        "minimum_leave_one_cell_out_alpha_pct": min(
            float(row["mean_alpha_pct"]) for row in leave_one_cell_out
        ),
        "leave_one_cell_out": leave_one_cell_out,
    }


def analyze(config: dict[str, Any]) -> dict[str, Any]:
    cells = load_cells(config)
    primary_rows = evaluate_v3_rule(cells, DEFAULT_MINIMUM_BEAT_SPY_PROBABILITY_PCT)
    threshold_sensitivity = []
    for threshold in SENSITIVITY_THRESHOLDS:
        metrics = summarize_rows(evaluate_v3_rule(cells, threshold))
        threshold_sensitivity.append(
            {
                "threshold_pct": threshold,
                **{
                    key: metrics[key]
                    for key in (
                        "mean_alpha_pct",
                        "mean_paired_improvement_pct",
                        "spy_beats",
                        "nonnegative_alpha_cells",
                        "positive_models",
                        "positive_periods",
                        "worst_period_alpha_pct",
                        "active_cells",
                        "active_slots",
                        "top3_captures",
                        "minimum_leave_one_cell_out_alpha_pct",
                    )
                },
            }
        )

    probability_55 = lambda row: float(row["p_beat_spy_pct"]) >= 55.0
    overreaction = lambda row: str(row["recent_return_interpretation"]) == "overreaction"
    continuation = (
        lambda row: str(row["recent_return_interpretation"]) == "supported_continuation"
    )
    mechanism_controls = {
        "probability_at_least_55_only": evaluate_predicate_rule(cells, probability_55),
        "overreaction_any_probability": evaluate_predicate_rule(cells, overreaction),
        "overreaction_probability_at_least_55": evaluate_predicate_rule(
            cells, lambda row: overreaction(row) and probability_55(row)
        ),
        "continuation_probability_at_least_55": evaluate_predicate_rule(
            cells, lambda row: continuation(row) and probability_55(row)
        ),
        "overreaction_or_continuation_probability_at_least_55": evaluate_predicate_rule(
            cells, lambda row: (overreaction(row) or continuation(row)) and probability_55(row)
        ),
    }
    return {
        "diagnostic_id": "portfolio-v3-robustness-diagnostic-2026-08-14",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": "development_candidate_only",
        "calls": 0,
        "post_hoc": True,
        "production_eligible": False,
        "primary_rule": (
            "Select at most three model-ranked candidates classified as overreaction "
            "with at least a 55% estimated probability of beating SPY; fill unused "
            "35/35/30 slots with SPY."
        ),
        "primary": summarize_rows(primary_rows),
        "threshold_sensitivity": threshold_sensitivity,
        "mechanism_controls": mechanism_controls,
        "interpretation": (
            "The positive result is stable to broad probability cutoffs and removal of "
            "any one model, period, or cell, but the rule was developed after these "
            "historical outcomes were available. It is a V3 development candidate, "
            "not prospective validation or a production adoption decision."
        ),
    }


def _pct(value: Any) -> str:
    return "n/a" if value is None else f"{float(value):.2f}%"


def render(summary: Mapping[str, Any]) -> str:
    primary = summary["primary"]
    lines = [
        "# Portfolio V3 Robustness Diagnostic",
        "",
        "Decision: **development candidate only**",
        "",
        "## Candidate Rule",
        "",
        str(summary["primary_rule"]),
        "",
        "This analysis made no model calls. It uses the eleven valid responses from the "
        "three frozen V3A development weeks. The rule is post-hoc and cannot establish "
        "prospective performance.",
        "",
        "## Main Result",
        "",
        f"- Mean alpha versus SPY: {_pct(primary['mean_alpha_pct'])}",
        f"- Mean improvement versus paired V2.2: {_pct(primary['mean_paired_improvement_pct'])}",
        f"- Strict SPY beats: {primary['spy_beats']}/{primary['valid_cells']}",
        f"- Nonnegative cells: {primary['nonnegative_alpha_cells']}/{primary['valid_cells']}",
        f"- Active decisions: {primary['active_cells']}/{primary['valid_cells']} cells and "
        f"{primary['active_slots']}/33 available slots",
        f"- Positive model families: {primary['positive_models']}/4",
        f"- Positive periods: {primary['positive_periods']}/3",
        f"- Weakest period: {_pct(primary['worst_period_alpha_pct'])}",
        "",
        "## Removal Tests",
        "",
        f"- Lowest mean alpha after removing any one model: "
        f"{_pct(min(primary['leave_one_model_out_alpha_pct'].values()))}",
        f"- Lowest mean alpha after removing any one period: "
        f"{_pct(min(primary['leave_one_period_out_alpha_pct'].values()))}",
        f"- Lowest mean alpha after removing any one cell: "
        f"{_pct(primary['minimum_leave_one_cell_out_alpha_pct'])}",
        "",
        "## Threshold Sensitivity",
        "",
        "| Probability hurdle | Alpha vs SPY | SPY beats | Nonnegative | Positive models | "
        "Positive periods | Active cells |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary["threshold_sensitivity"]:
        lines.append(
            f"| {row['threshold_pct']:.1f}% | {_pct(row['mean_alpha_pct'])} | "
            f"{row['spy_beats']}/11 | {row['nonnegative_alpha_cells']}/11 | "
            f"{row['positive_models']}/4 | {row['positive_periods']}/3 | "
            f"{row['active_cells']}/11 |"
        )

    lines.extend(
        [
            "",
            "Every tested nontrivial hurdle from 45% through 67.5% remained above SPY. "
            "The 55% hurdle is retained because it was frozen before the Gemini responses; "
            "choosing the best-looking cutoff now would be outcome tuning.",
            "",
            "## Mechanism Check",
            "",
            "| Rule | Alpha vs SPY | SPY beats | Active cells |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for name, row in summary["mechanism_controls"].items():
        lines.append(
            f"| {name.replace('_', ' ')} | {_pct(row['mean_alpha_pct'])} | "
            f"{row['spy_beats']}/11 | {row['active_cells']}/11 |"
        )
    lines.extend(
        [
            "",
            "Confidence alone did not work. Confident continuation lost to SPY, while the "
            "overreaction classification produced the positive result. This supports a "
            "simple V3 candidate that excludes continuation rather than adding more prompt "
            "complexity.",
            "",
            "## Interpretation",
            "",
            str(summary["interpretation"]),
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
    config = replay.load_config(config_path)
    replay.verify_freeze(config_path, config)
    summary = analyze(config)
    report_path = args.report.resolve()
    summary_path = args.summary.resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render(summary), encoding="utf-8", newline="\n")
    replay.base.write_json(summary_path, summary)
    print(f"valid_cells={summary['primary']['valid_cells']}/12")
    print(f"mean_alpha_pct={summary['primary']['mean_alpha_pct']}")
    print(
        "minimum_leave_one_model_out_alpha_pct="
        f"{min(summary['primary']['leave_one_model_out_alpha_pct'].values())}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run and score the frozen low-cost Portfolio V3.0 holdout comparison."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
for path in (ROOT, SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from capitalbench.portfolio_v3 import build_portfolio_v3_allocation  # noqa: E402
from scripts import analyze_model_predictability as v1_analysis  # noqa: E402
from scripts import run_portfolio_v3_replay as replay  # noqa: E402


DEFAULT_CONFIG = ROOT / "experiments" / "portfolio-v3-holdout-comparison-2026-08-14.yaml"
CONSTRUCTOR_PATH = ROOT / "src" / "capitalbench" / "portfolio_v3.py"


def _mean(rows: Iterable[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return statistics.mean(values) if values else None


def _verify_holdout_freeze(config_path: Path, config: dict[str, Any]) -> dict[str, Any]:
    manifest = replay.verify_freeze(config_path, config)
    expected = {
        "holdout_runner_sha256": replay.base.sha256_file(Path(__file__)),
        "portfolio_v3_constructor_sha256": replay.base.sha256_file(CONSTRUCTOR_PATH),
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise RuntimeError(f"frozen artifact changed: {key}")
    return manifest


def prepare(config_path: Path) -> None:
    replay.prepare(config_path)
    config = replay.load_config(config_path)
    manifest_path = replay.output_dir(config) / "freeze_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "holdout_runner_sha256": replay.base.sha256_file(Path(__file__)),
            "portfolio_v3_constructor_sha256": replay.base.sha256_file(CONSTRUCTOR_PATH),
            "portfolio_rule": "ranked overreaction at p>=55; unused 35/35/30 slots to SP500",
            "baseline_calls": 0,
        }
    )
    replay.base.write_json(manifest_path, manifest)
    _verify_holdout_freeze(config_path, config)
    print("holdout_freeze=verified")


def run(config_path: Path) -> None:
    config = replay.load_config(config_path)
    _verify_holdout_freeze(config_path, config)
    replay.run(config_path)


def _v1_reference(model_ids: set[str]) -> dict[str, Any]:
    rounds, *_rest = v1_analysis.build_dataset(ROOT / "rounds")
    cells: list[dict[str, Any]] = []
    by_model: dict[str, list[float]] = {model_id: [] for model_id in sorted(model_ids)}
    for round_record in rounds:
        if round_record.track != "weekly":
            continue
        for model in round_record.models:
            if model.model_id not in model_ids or model.alpha_vs_sp500 is None:
                continue
            alpha_pct = float(model.alpha_vs_sp500) * 100.0
            by_model[model.model_id].append(alpha_pct)
            cells.append({"round_id": round_record.round_id, "model_id": model.model_id, "alpha_pct": alpha_pct})
    values = [row["alpha_pct"] for row in cells]
    return {
        "paired": False,
        "valid_cells": len(values),
        "mean_alpha_pct": statistics.mean(values) if values else None,
        "by_model": {
            model_id: {
                "valid_cells": len(model_values),
                "mean_alpha_pct": statistics.mean(model_values) if model_values else None,
            }
            for model_id, model_values in by_model.items()
        },
        "note": "Historical weekly V1 reference only; dates and model coverage differ from the V3 holdout.",
    }


def score_rows(config: dict[str, Any]) -> list[dict[str, Any]]:
    records_dir = replay.output_dir(config) / "records"
    records = {
        (str(row["replay_id"]), str(row["model_id"])): row
        for row in (
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(records_dir.glob("*.json"))
        )
    }
    rows: list[dict[str, Any]] = []
    threshold = float(config["portfolio"]["minimum_beat_spy_probability_pct"])
    slots = [float(value) for value in config["portfolio"]["rank_allocations_pct"]]
    for episode in config["episodes"]:
        leaderboard_path, returns_path, control_run = replay.control_paths(episode)
        leaderboard = {row["model_id"]: row for row in replay.read_csv(leaderboard_path)}
        return_rows = replay.read_csv(returns_path)
        returns = {row["option_id"]: float(row["return"]) for row in return_rows}
        realized_order = [
            row["option_id"]
            for row in sorted(return_rows, key=lambda row: float(row["return"]), reverse=True)
        ]
        realized_top3 = set(realized_order[:3])
        slate_ids = {str(row["option_id"]) for row in replay.candidate_slate(config, episode)}
        for model_id in config["models"]:
            record = records.get((str(episode["replay_id"]), str(model_id)))
            control = leaderboard.get(str(model_id))
            row: dict[str, Any] = {
                "replay_id": episode["replay_id"],
                "round_id": episode["round_id"],
                "model_id": model_id,
                "valid": bool(record and record.get("valid") and control),
                "provider_error": record.get("provider_error") if record else "missing record",
                "validation_errors": record.get("validation_errors") if record else ["missing record"],
                "spy_return_pct": returns["SP500"] * 100.0,
                "winner_option_id": realized_order[0],
                "realized_top3": realized_order[:3],
                "slate_winner_capture": realized_order[0] in slate_ids,
            }
            if not row["valid"]:
                rows.append(row)
                continue
            payload = record["parsed_json"]
            built = build_portfolio_v3_allocation(
                payload["candidate_assessments"],
                minimum_beat_spy_probability_pct=threshold,
                slot_weights_pct=slots,
            )
            allocation = built["allocation_pct"]
            treatment_return = replay._portfolio_return(allocation, returns)
            control_return = float(control["portfolio_return"])
            selected = list(built["selected_active_option_ids"])
            control_ids = replay._control_portfolio(control_run, str(model_id))
            row.update(
                {
                    "selected_active_option_ids": selected,
                    "allocation": allocation,
                    "active_slots": len(selected),
                    "treatment_return_pct": treatment_return * 100.0,
                    "treatment_alpha_pct": (treatment_return - returns["SP500"]) * 100.0,
                    "control_return_pct": control_return * 100.0,
                    "control_alpha_pct": (control_return - returns["SP500"]) * 100.0,
                    "paired_improvement_pct": (treatment_return - control_return) * 100.0,
                    "treatment_winner_capture": realized_order[0] in selected,
                    "treatment_top3_capture": bool(realized_top3 & set(selected)),
                    "control_winner_capture": realized_order[0] in control_ids,
                    "control_top3_capture": bool(realized_top3 & set(control_ids)),
                }
            )
            rows.append(row)
    return rows


def aggregate(config: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [row for row in rows if row["valid"]]
    by_model: dict[str, dict[str, Any]] = {}
    for model_id in config["models"]:
        subset = [row for row in valid if row["model_id"] == model_id]
        by_model[model_id] = {
            "valid_pairs": len(subset),
            "mean_treatment_alpha_pct": _mean(subset, "treatment_alpha_pct"),
            "mean_control_alpha_pct": _mean(subset, "control_alpha_pct"),
            "mean_paired_improvement_pct": _mean(subset, "paired_improvement_pct"),
        }
    by_period: dict[str, dict[str, Any]] = {}
    for episode in config["episodes"]:
        replay_id = str(episode["replay_id"])
        subset = [row for row in valid if row["replay_id"] == replay_id]
        by_period[replay_id] = {
            "valid_pairs": len(subset),
            "mean_treatment_alpha_pct": _mean(subset, "treatment_alpha_pct"),
            "mean_control_alpha_pct": _mean(subset, "control_alpha_pct"),
            "mean_paired_improvement_pct": _mean(subset, "paired_improvement_pct"),
        }
    overall = {
        "valid_pairs": len(valid),
        "mean_treatment_return_pct": _mean(valid, "treatment_return_pct"),
        "mean_treatment_alpha_pct": _mean(valid, "treatment_alpha_pct"),
        "mean_control_return_pct": _mean(valid, "control_return_pct"),
        "mean_control_alpha_pct": _mean(valid, "control_alpha_pct"),
        "mean_paired_improvement_pct": _mean(valid, "paired_improvement_pct"),
        "nonnegative_alpha_cells": sum(float(row["treatment_alpha_pct"]) >= -1e-9 for row in valid),
        "positive_pairs": sum(float(row["paired_improvement_pct"]) > 0 for row in valid),
        "treatment_spy_beats": sum(float(row["treatment_alpha_pct"]) > 0 for row in valid),
        "control_spy_beats": sum(float(row["control_alpha_pct"]) > 0 for row in valid),
        "treatment_top3_captures": sum(bool(row["treatment_top3_capture"]) for row in valid),
        "control_top3_captures": sum(bool(row["control_top3_capture"]) for row in valid),
        "full_spy_fallback_cells": sum(int(row.get("active_slots") or 0) == 0 for row in valid),
    }
    positive_models = sum(
        row["mean_treatment_alpha_pct"] is not None and row["mean_treatment_alpha_pct"] > 0
        for row in by_model.values()
    )
    positive_periods = sum(
        row["mean_treatment_alpha_pct"] is not None and row["mean_treatment_alpha_pct"] > 0
        for row in by_period.values()
    )
    worst_period_alpha = min(
        (float(row["mean_treatment_alpha_pct"]) for row in by_period.values() if row["mean_treatment_alpha_pct"] is not None),
        default=-999.0,
    )
    gate = config["gate"]
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
        "nonnegative_alpha_cells": overall["nonnegative_alpha_cells"] >= int(gate["minimum_nonnegative_alpha_cells"]),
        "positive_models": positive_models >= int(gate["minimum_positive_models"]),
        "positive_periods": positive_periods >= int(gate["minimum_positive_periods"]),
        "worst_period_alpha": worst_period_alpha >= float(gate["minimum_worst_period_alpha_pct"]),
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
        "worst_period_alpha_pct": worst_period_alpha,
        "gate_checks": checks,
        "passes_gate": all(checks.values()),
    }


def _fmt(value: Any) -> str:
    return "n/a" if value is None else f"{float(value):.2f}%"


def render_report(config: dict[str, Any], summary: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    aggregate_row = summary["aggregate"]
    overall = aggregate_row["overall"]
    legacy = summary["v1_historical_reference"]
    decision = "ACCEPT V3.0" if aggregate_row["passes_gate"] else "REJECT V3.0"
    lines = [
        "# Portfolio V3.0 Holdout Comparison",
        "",
        f"Decision: **{decision}**",
        "",
        "## Bottom Line",
        "",
        f"- Valid exact V3/V2.2 pairs: {overall['valid_pairs']}/12",
        f"- V3 mean alpha versus SPY: {_fmt(overall['mean_treatment_alpha_pct'])}",
        f"- Exact V2.2 control mean alpha: {_fmt(overall['mean_control_alpha_pct'])}",
        f"- V3 improvement over V2.2: {_fmt(overall['mean_paired_improvement_pct'])}",
        f"- V3 cells at or above SPY: {overall['nonnegative_alpha_cells']}/{overall['valid_pairs']}",
        f"- Historical V1 same-ID reference alpha: {_fmt(legacy['mean_alpha_pct'])} across {legacy['valid_cells']} unevenly covered cells (not paired)",
        "",
        "## Frozen Gate",
        "",
    ]
    for key, passed in aggregate_row["gate_checks"].items():
        lines.append(f"- {key.replace('_', ' ')}: {'PASS' if passed else 'FAIL'}")
    lines.extend(
        [
            "",
            "## By Period",
            "",
            "| Set | V3 alpha | V2.2 alpha | Improvement |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for replay_id, row in aggregate_row["by_period"].items():
        lines.append(
            f"| {replay_id} | {_fmt(row['mean_treatment_alpha_pct'])} | {_fmt(row['mean_control_alpha_pct'])} | {_fmt(row['mean_paired_improvement_pct'])} |"
        )
    lines.extend(
        [
            "",
            "## By Model",
            "",
            "| Model | Pairs | V3 alpha | V2.2 alpha | Improvement |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for model_id, row in aggregate_row["by_model"].items():
        lines.append(
            f"| {model_id} | {row['valid_pairs']} | {_fmt(row['mean_treatment_alpha_pct'])} | {_fmt(row['mean_control_alpha_pct'])} | {_fmt(row['mean_paired_improvement_pct'])} |"
        )
    lines.extend(
        [
            "",
            "## Cell Results",
            "",
            "| Set | Model | V3 alpha | V2.2 alpha | Improvement | V3 active choices | Valid |",
            "| --- | --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['replay_id']} | {row['model_id']} | {_fmt(row.get('treatment_alpha_pct'))} | "
            f"{_fmt(row.get('control_alpha_pct'))} | {_fmt(row.get('paired_improvement_pct'))} | "
            f"{', '.join(row.get('selected_active_option_ids') or []) or 'SPY only'} | {'yes' if row['valid'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "V2.2 is an exact same-model, same-date control. V1 is not: it ended before these rounds and the newer models have sparse V1 coverage. The V1 number is context only.",
            "",
            "The three holdout windows are one-day-shifted from the V3 development windows and share market history. This is a frozen operational decision test, not independent proof of persistent future alpha.",
            "",
            "## Execution",
            "",
            f"- New provider attempts: {summary['calls_used']} (maximum {config['max_calls']})",
            "- New V1/V2.2 calls: 0",
            "- Participant tools, browsing, retrieval, follow-up, and best-of-many selection: disabled",
            "- Official score eligibility: no",
            "",
        ]
    )
    return "\n".join(lines)


def score(config_path: Path) -> None:
    config = replay.load_config(config_path)
    _verify_holdout_freeze(config_path, config)
    rows = score_rows(config)
    aggregate_row = aggregate(config, rows)
    records = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in (replay.output_dir(config) / "records").glob("*.json")
    ]
    calls_used = sum(int(row.get("attempts") or 0) for row in records)
    legacy = _v1_reference(set(config["models"]))
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "decision": "accept_v3_for_next_production_round" if aggregate_row["passes_gate"] else "reject_v3",
        "aggregate": aggregate_row,
        "v1_historical_reference": legacy,
        "calls_used": calls_used,
        "max_calls": int(config["max_calls"]),
        "official_score_eligible": False,
        "production_impact": "none_until_operator_adoption",
        "config_sha256": replay.base.sha256_file(config_path),
        "freeze_manifest_sha256": replay.base.sha256_file(replay.output_dir(config) / "freeze_manifest.json"),
    }
    replay.base.write_json(replay.output_dir(config) / "score_summary.json", summary)
    replay.base.write_csv(replay.output_dir(config) / "scored_cells.csv", rows)
    replay.base.write_json(replay.canonical_summary(config), summary)
    report = render_report(config, summary, rows)
    report_path = replay.canonical_report(config)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8", newline="\n")
    print(f"decision={summary['decision']}")
    print(f"valid_pairs={aggregate_row['overall']['valid_pairs']}/12")
    print(f"mean_v3_alpha_pct={aggregate_row['overall']['mean_treatment_alpha_pct']}")
    print(f"mean_v2_2_improvement_pct={aggregate_row['overall']['mean_paired_improvement_pct']}")
    print(f"v1_historical_reference_alpha_pct={legacy['mean_alpha_pct']}")


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
    config_path = args.config.resolve()
    if args.command == "prepare":
        prepare(config_path)
    elif args.command == "run":
        run(config_path)
    elif args.command == "score":
        score(config_path)


if __name__ == "__main__":
    main()

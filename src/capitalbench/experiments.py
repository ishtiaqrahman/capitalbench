from __future__ import annotations

import csv
import itertools
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .hashing import round_hashes_match, sha256_file
from .io import load_manifest, load_options, read_json, read_yaml, write_json
from .run_store import get_run_paths, read_run_manifest


@dataclass(frozen=True)
class ExperimentEvaluationOutput:
    decision: str
    json_path: Path
    markdown_path: Path


def evaluate_experiment(*, config_path: Path, rounds_dir: Path) -> ExperimentEvaluationOutput:
    config = read_yaml(config_path)
    model_ids = [str(item) for item in config.get("models") or []]
    if not model_ids:
        raise ValueError("experiment config requires models")
    v1_round = rounds_dir / str(config["paired_v1_round_id"])
    v2_round = rounds_dir / str(config["v2_round_id"])
    v1_run_id = str(config["paired_v1_run_id"])
    v2_run_id = str(config["v2_run_id"])
    v1_rows = _leaderboard_by_model(v1_round, v1_run_id, model_ids)
    v2_rows = _leaderboard_by_model(v2_round, v2_run_id, model_ids)
    v2_manifest = read_run_manifest(get_run_paths(v2_round, v2_run_id))

    paired_rows = []
    for model_id in model_ids:
        v1 = v1_rows[model_id]
        v2 = v2_rows[model_id]
        v1_return = _float(v1, "portfolio_return")
        v2_return = _float(v2, "portfolio_return")
        v1_alpha = _float(v1, "alpha_vs_sp500")
        v2_alpha = _float(v2, "alpha_vs_sp500")
        paired_rows.append(
            {
                "model_id": model_id,
                "v1_return": v1_return,
                "v2_return": v2_return,
                "v1_alpha_vs_sp500": v1_alpha,
                "v2_alpha_vs_sp500": v2_alpha,
                "paired_improvement": v2_return - v1_return,
                "v1_beats_sp500": _bool(v1.get("beats_sp500")),
                "v2_beats_sp500": _bool(v2.get("beats_sp500")),
            }
        )

    mean_v1_alpha = _mean(row["v1_alpha_vs_sp500"] for row in paired_rows)
    mean_v2_alpha = _mean(row["v2_alpha_vs_sp500"] for row in paired_rows)
    improved_count = sum(1 for row in paired_rows if row["paired_improvement"] > 0)
    v1_beat_count = sum(1 for row in paired_rows if row["v1_beats_sp500"])
    v2_beat_count = sum(1 for row in paired_rows if row["v2_beats_sp500"])
    controlled_inputs = _controlled_inputs_match(v1_round, v2_round, str(config["research_cutoff_utc"]))
    all_v2_valid = (
        int(v2_manifest.get("valid_submissions") or 0) == len(model_ids)
        and int(v2_manifest.get("invalid_submissions") or 0) == 0
        and bool(v2_manifest.get("operator_selected_official"))
        and round_hashes_match(v2_round)
    )
    gates = {
        "all_v2_submissions_valid_and_frozen": all_v2_valid,
        "average_v2_alpha_above_zero": mean_v2_alpha > 0,
        "average_v2_alpha_above_v1": mean_v2_alpha > mean_v1_alpha,
        "at_least_three_models_improved": improved_count >= int(
            (config.get("acceptance_rule") or {}).get("minimum_models_improved") or 3
        ),
        "v2_beat_count_not_lower": v2_beat_count >= v1_beat_count,
        "controlled_inputs_match": controlled_inputs,
    }
    decision = "accepted" if all(gates.values()) else "rejected"
    diagnostics = _diagnostics(v1_round, v2_round, v1_run_id, v2_run_id, model_ids, paired_rows)
    report = {
        "version": "capitalbench_portfolio_v2_experiment_evaluation_v1",
        "experiment_id": str(config["experiment_id"]),
        "decision": decision,
        "paired_v1_round_id": v1_round.name,
        "v2_round_id": v2_round.name,
        "models": model_ids,
        "summary": {
            "average_v1_alpha_vs_sp500": mean_v1_alpha,
            "average_v2_alpha_vs_sp500": mean_v2_alpha,
            "average_paired_improvement": _mean(row["paired_improvement"] for row in paired_rows),
            "models_improved": improved_count,
            "v1_beat_sp500_count": v1_beat_count,
            "v2_beat_sp500_count": v2_beat_count,
        },
        "gates": gates,
        "paired_results": paired_rows,
        "diagnostics": diagnostics,
    }
    output_dir = v2_round / "experiment"
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "paired_v1_v2_evaluation.json"
    markdown_path = output_dir / "paired_v1_v2_evaluation.md"
    write_json(json_path, report)
    markdown_path.write_text(_render_report(report), encoding="utf-8")
    return ExperimentEvaluationOutput(decision=decision, json_path=json_path, markdown_path=markdown_path)


def _leaderboard_by_model(round_path: Path, run_id: str, model_ids: list[str]) -> dict[str, dict[str, str]]:
    path = get_run_paths(round_path, run_id).results_dir / "leaderboard.csv"
    if not path.exists():
        raise FileNotFoundError(f"experiment requires resolved leaderboard: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = {row["model_id"]: row for row in csv.DictReader(handle) if row.get("model_id") in model_ids}
    missing = [model_id for model_id in model_ids if model_id not in rows]
    if missing:
        raise ValueError(f"leaderboard missing experiment models: {', '.join(missing)}")
    return rows


def _controlled_inputs_match(v1_round: Path, v2_round: Path, cutoff: str) -> bool:
    v1_manifest = load_manifest(v1_round)
    v2_manifest = load_manifest(v2_round)
    if any(
        [
            v1_manifest.entry_date != v2_manifest.entry_date,
            v1_manifest.exit_date != v2_manifest.exit_date,
            v1_manifest.horizon != v2_manifest.horizon,
            sha256_file(v1_round / "options.yaml") != sha256_file(v2_round / "options.yaml"),
            sha256_file(v1_round / "prices" / "entry_prices.csv")
            != sha256_file(v2_round / "prices" / "entry_prices.csv"),
        ]
    ):
        return False
    for round_path in [v1_round, v2_round]:
        research = read_yaml(round_path / "research" / "research_manifest.yaml")
        if str(research.get("research_cutoff_utc") or "") != cutoff:
            return False
    history = read_json(v2_round / "market_data" / "decision_context_source_history.json")
    dates = [
        str(row.get("date") or "")
        for option in history.get("options") or []
        for row in option.get("rows") or []
    ]
    return not dates or max(dates) <= str(v2_manifest.entry_date)


def _diagnostics(
    v1_round: Path,
    v2_round: Path,
    v1_run_id: str,
    v2_run_id: str,
    model_ids: list[str],
    paired_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    v1_weights = _portfolio_weights(v1_round, v1_run_id, model_ids)
    v2_weights = _portfolio_weights(v2_round, v2_run_id, model_ids)
    context = read_json(v2_round / "market_data" / "universe_decision_context.json")
    ranked = sorted(
        [
            row
            for row in context.get("rows") or []
            if row.get("status") == "pass" and row.get("return_5s") not in {None, ""}
        ],
        key=lambda row: float(row["return_5s"]),
        reverse=True,
    )
    top_count = max(1, math.ceil(len(ranked) * 0.20))
    recent_winners = {str(row["option_id"]) for row in ranked[:top_count]}
    groups = {option.option_id: option.option_group for option in load_options(v2_round)}
    v2_submissions = _parsed_submissions(v2_round, v2_run_id, model_ids)
    realized_by_model = {row["model_id"]: row["v2_return"] for row in paired_rows}
    sp500_return = next(iter(_leaderboard_by_model(v2_round, v2_run_id, model_ids).values()))["sp500_return"]
    forecast_errors = []
    for model_id, submission in v2_submissions.items():
        if submission.get("portfolio_expected_return_pct") is None:
            continue
        forecast_errors.append(
            {
                "model_id": model_id,
                "portfolio_forecast_error_pct": float(submission["portfolio_expected_return_pct"])
                - realized_by_model[model_id] * 100.0,
                "spy_forecast_error_pct": float(submission["benchmark_expected_return_pct"])
                - float(sp500_return) * 100.0,
            }
        )
    return {
        "v1_average_recent_winner_allocation": _average_set_weight(v1_weights, recent_winners),
        "v2_average_recent_winner_allocation": _average_set_weight(v2_weights, recent_winners),
        "v1_cross_model_overlap": _average_overlap(v1_weights),
        "v2_cross_model_overlap": _average_overlap(v2_weights),
        "v1_average_largest_theme_weight": _average_largest_group_weight(v1_weights, groups),
        "v2_average_largest_theme_weight": _average_largest_group_weight(v2_weights, groups),
        "forecast_errors": forecast_errors,
    }


def _portfolio_weights(round_path: Path, run_id: str, model_ids: list[str]) -> dict[str, dict[str, float]]:
    submissions = _parsed_submissions(round_path, run_id, model_ids)
    return {
        model_id: {
            str(item["option_id"]): float(item["allocation_pct"]) / 100.0
            for item in submission.get("portfolio") or []
        }
        for model_id, submission in submissions.items()
    }


def _parsed_submissions(round_path: Path, run_id: str, model_ids: list[str]) -> dict[str, dict[str, Any]]:
    parsed_dir = get_run_paths(round_path, run_id).parsed_dir
    submissions: dict[str, dict[str, Any]] = {}
    for path in parsed_dir.glob("*.json"):
        payload = read_json(path)
        model_id = str(payload.get("model_id") or "")
        if model_id in model_ids:
            submissions[model_id] = payload
    missing = [model_id for model_id in model_ids if model_id not in submissions]
    if missing:
        raise ValueError(f"parsed submissions missing experiment models: {', '.join(missing)}")
    return submissions


def _average_set_weight(portfolios: dict[str, dict[str, float]], option_ids: set[str]) -> float:
    return _mean(sum(weight for option_id, weight in portfolio.items() if option_id in option_ids) for portfolio in portfolios.values())


def _average_overlap(portfolios: dict[str, dict[str, float]]) -> float:
    pairs = list(itertools.combinations(portfolios.values(), 2))
    return _mean(
        sum(min(left.get(option_id, 0.0), right.get(option_id, 0.0)) for option_id in set(left) | set(right))
        for left, right in pairs
    ) if pairs else 0.0


def _average_largest_group_weight(portfolios: dict[str, dict[str, float]], groups: dict[str, str]) -> float:
    largest = []
    for portfolio in portfolios.values():
        grouped: dict[str, float] = {}
        for option_id, weight in portfolio.items():
            group = groups.get(option_id, "unknown")
            grouped[group] = grouped.get(group, 0.0) + weight
        largest.append(max(grouped.values()) if grouped else 0.0)
    return _mean(largest)


def _render_report(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# Portfolio V2 Paired Evaluation",
        "",
        f"Decision: **{str(report['decision']).upper()}**",
        "",
        f"- Average V1 alpha vs SPY: {summary['average_v1_alpha_vs_sp500'] * 100:.2f}%",
        f"- Average V2 alpha vs SPY: {summary['average_v2_alpha_vs_sp500'] * 100:.2f}%",
        f"- Average paired improvement: {summary['average_paired_improvement'] * 100:.2f}%",
        f"- Models improved: {summary['models_improved']}/{len(report['models'])}",
        f"- V1 portfolios beating SPY: {summary['v1_beat_sp500_count']}/{len(report['models'])}",
        f"- V2 portfolios beating SPY: {summary['v2_beat_sp500_count']}/{len(report['models'])}",
        "",
        "## Acceptance Gates",
        "",
    ]
    lines.extend(f"- {'PASS' if passed else 'FAIL'}: {name}" for name, passed in report["gates"].items())
    lines.extend(["", "## Paired Results", "", "| model | V1 return | V2 return | improvement |", "| --- | ---: | ---: | ---: |"])
    for row in report["paired_results"]:
        lines.append(
            f"| {row['model_id']} | {row['v1_return'] * 100:.2f}% | {row['v2_return'] * 100:.2f}% | {row['paired_improvement'] * 100:.2f}% |"
        )
    return "\n".join(lines) + "\n"


def _float(row: dict[str, str], key: str) -> float:
    value = row.get(key)
    if value in {None, ""}:
        raise ValueError(f"leaderboard field is missing: {key}")
    return float(value)


def _bool(value: Any) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _mean(values: Any) -> float:
    items = [float(value) for value in values]
    if not items:
        raise ValueError("cannot calculate experiment mean from no values")
    return sum(items) / len(items)

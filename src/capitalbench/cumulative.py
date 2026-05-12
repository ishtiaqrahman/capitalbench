from __future__ import annotations

import csv
import math
import statistics
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from .io import load_manifest, read_yaml
from .run_store import get_run_paths, list_run_ids, read_run_manifest


OFFICIAL_COLUMNS = [
    "model_id",
    "provider",
    "resolved_rounds",
    "average_official_return",
    "average_sp500_return",
    "average_alpha_vs_sp500",
    "median_alpha_vs_sp500",
    "cumulative_model_return",
    "cumulative_sp500_return",
    "cumulative_log_alpha",
    "hit_rate_vs_sp500",
    "hit_rate_vs_cash",
    "average_regret_vs_best_option",
    "best_round_alpha",
    "worst_round_alpha",
    "total_cost_usd",
    "average_cost_usd",
    "rounds_included",
]

STABILITY_COLUMNS = [
    "model_id",
    "provider",
    "resolved_rounds",
    "total_replicates",
    "average_repeated_return",
    "average_repeated_alpha_vs_sp500",
    "median_repeated_alpha_vs_sp500",
    "average_consistency_rate",
    "average_modal_pick_alpha_vs_sp500",
    "average_modal_pick_return",
    "average_best_replicate_return",
    "average_worst_replicate_return",
    "best_round_repeated_alpha",
    "worst_round_repeated_alpha",
    "total_cost_usd",
    "average_cost_per_round",
    "rounds_included",
]

ROUND_INDEX_COLUMNS = [
    "round_id",
    "decision_deadline_utc",
    "horizon_days",
    "official_run_id",
    "stability_run_id",
    "official_models_count",
    "stability_models_count",
    "included_in_latest",
    "included_in_official_cumulative",
    "included_in_stability_cumulative",
    "warnings",
]


@dataclass(frozen=True)
class CumulativeRoundSelection:
    round_id: str
    round_path: Path
    decision_deadline_utc: str
    horizon_days: int | None
    official_run_id: str | None
    stability_run_id: str | None
    official_rows: list[dict[str, str]]
    stability_rows: list[dict[str, str]]
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class CumulativeStatus:
    selections: list[CumulativeRoundSelection]
    skipped_rounds: dict[str, list[str]]
    warnings: list[str]


@dataclass(frozen=True)
class CumulativeOutput:
    official_leaderboard_path: Path
    stability_leaderboard_path: Path
    cumulative_report_path: Path
    round_index_path: Path
    status: CumulativeStatus


@dataclass(frozen=True)
class LatestOutput:
    latest_leaderboard_path: Path
    latest_report_path: Path
    selected_round: CumulativeRoundSelection
    status: CumulativeStatus


def discover_rounds(rounds_dir: Path) -> list[Path]:
    if not rounds_dir.exists():
        return []
    return sorted(
        item
        for item in rounds_dir.iterdir()
        if item.is_dir() and (item / "manifest.yaml").exists()
    )


def load_selection(selection_path: Path | None) -> dict[str, dict[str, str]]:
    if selection_path is None:
        return {}
    data = read_yaml(selection_path)
    raw_rounds = data.get("rounds") if isinstance(data, dict) else None
    if not isinstance(raw_rounds, dict):
        raise ValueError("selection file must contain a 'rounds' mapping")
    selection: dict[str, dict[str, str]] = {}
    for round_id, raw_entry in raw_rounds.items():
        if not isinstance(raw_entry, dict):
            raise ValueError(f"selection for {round_id} must be a mapping")
        official_run_id = str(raw_entry.get("official_run_id") or "").strip()
        stability_run_id = str(raw_entry.get("stability_run_id") or "").strip()
        if not official_run_id or not stability_run_id:
            raise ValueError(f"selection for {round_id} must define official_run_id and stability_run_id")
        selection[str(round_id)] = {
            "official_run_id": official_run_id,
            "stability_run_id": stability_run_id,
        }
    return selection


def select_runs_for_round(
    round_path: Path,
    selection: dict[str, dict[str, str]] | None = None,
) -> CumulativeRoundSelection | None:
    manifest = load_manifest(round_path)
    round_id = manifest.round_id
    horizon_days = _horizon_days(manifest.entry_date, manifest.exit_date)
    explicit = selection.get(round_id) if selection else None
    warnings: list[str] = []

    if explicit is not None:
        official_run_id = explicit["official_run_id"]
        stability_run_id = explicit["stability_run_id"]
        _require_selected_run(round_path, official_run_id, expected_run_type="official", official=True)
        _require_selected_run(round_path, stability_run_id, expected_run_type="stability", official=False)
    else:
        run_ids = list_run_ids(round_path)
        official_candidates: list[str] = []
        stability_candidates: list[str] = []
        for run_id in run_ids:
            run_paths = get_run_paths(round_path, run_id)
            manifest_data = read_run_manifest(run_paths)
            run_type = str(manifest_data.get("run_type") or "")
            if (
                run_type == "official"
                and manifest_data.get("mock") is not True
                and bool(manifest_data.get("official_score_eligible"))
                and (run_paths.results_dir / "leaderboard.csv").exists()
            ):
                official_candidates.append(run_id)
            if (
                run_type == "stability"
                and manifest_data.get("mock") is not True
                and (run_paths.results_dir / "stability.csv").exists()
            ):
                stability_candidates.append(run_id)

        if len(official_candidates) > 1:
            warnings.append(
                f"Round {round_id} has multiple official eligible runs. "
                "Add cumulative_selection.yaml or pass explicit selections."
            )
            return CumulativeRoundSelection(
                round_id=round_id,
                round_path=round_path,
                decision_deadline_utc=manifest.decision_deadline or "",
                horizon_days=horizon_days,
                official_run_id=None,
                stability_run_id=None,
                official_rows=[],
                stability_rows=[],
                warnings=warnings,
            )
        if len(stability_candidates) > 1:
            warnings.append(
                f"Round {round_id} has multiple scored stability runs. "
                "Add cumulative_selection.yaml or pass explicit selections."
            )

        official_run_id = official_candidates[0] if len(official_candidates) == 1 else None
        stability_run_id = stability_candidates[0] if len(stability_candidates) == 1 else None
        if official_run_id is None and stability_run_id is None and not warnings:
            warnings.append(f"Round {round_id} has no scored official or stability runs.")

    official_rows = load_official_results(round_path, official_run_id) if official_run_id else []
    stability_rows = load_stability_results(round_path, stability_run_id) if stability_run_id else []
    return CumulativeRoundSelection(
        round_id=round_id,
        round_path=round_path,
        decision_deadline_utc=manifest.decision_deadline or "",
        horizon_days=horizon_days,
        official_run_id=official_run_id,
        stability_run_id=stability_run_id,
        official_rows=official_rows,
        stability_rows=stability_rows,
        warnings=warnings,
    )


def cumulative_status(rounds_dir: Path, selection_path: Path | None = None) -> CumulativeStatus:
    selection = load_selection(selection_path)
    round_paths = discover_rounds(rounds_dir)
    round_paths_by_id = {load_manifest(path).round_id: path for path in round_paths}
    selections: list[CumulativeRoundSelection] = []
    skipped_rounds: dict[str, list[str]] = {}
    warnings: list[str] = []

    if selection:
        for round_id in selection:
            if round_id not in round_paths_by_id:
                raise ValueError(f"selected round_id not found under {rounds_dir}: {round_id}")
            selected = select_runs_for_round(round_paths_by_id[round_id], selection)
            if selected is not None:
                selections.append(selected)
                warnings.extend(selected.warnings)
        return CumulativeStatus(selections=selections, skipped_rounds=skipped_rounds, warnings=warnings)

    for round_path in round_paths:
        selected = select_runs_for_round(round_path, selection)
        if selected is None:
            continue
        if selected.official_rows or selected.stability_rows:
            selections.append(selected)
        else:
            skipped_rounds[selected.round_id] = selected.warnings
        warnings.extend(selected.warnings)
    return CumulativeStatus(selections=selections, skipped_rounds=skipped_rounds, warnings=warnings)


def load_official_results(round_path: Path, run_id: str) -> list[dict[str, str]]:
    return _read_csv(get_run_paths(round_path, run_id).results_dir / "leaderboard.csv")


def load_stability_results(round_path: Path, run_id: str) -> list[dict[str, str]]:
    return _read_csv(get_run_paths(round_path, run_id).results_dir / "stability.csv")


def build_cumulative_official(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["model_id"], []).append(row)

    cumulative_rows: list[dict[str, object]] = []
    for model_id, model_rows in grouped.items():
        selected_returns = [_float(row["selected_asset_return"]) for row in model_rows]
        sp500_returns = [_float(row["sp500_return"]) for row in model_rows]
        alphas = [_float(row["alpha_vs_sp500"]) for row in model_rows]
        regret_values = [_optional_float(row.get("regret_vs_best_option")) for row in model_rows]
        regrets = [value for value in regret_values if value is not None]
        cost_values = [_optional_float(row.get("cost_usd")) for row in model_rows]
        available_costs = [cost for cost in cost_values if cost is not None]
        resolved_rounds = len(model_rows)
        cumulative_rows.append(
            {
                "model_id": model_id,
                "provider": model_rows[0].get("provider", ""),
                "resolved_rounds": resolved_rounds,
                "average_official_return": _average(selected_returns),
                "average_sp500_return": _average(sp500_returns),
                "average_alpha_vs_sp500": _average(alphas),
                "median_alpha_vs_sp500": statistics.median(alphas),
                "cumulative_model_return": _compound(selected_returns),
                "cumulative_sp500_return": _compound(sp500_returns),
                "cumulative_log_alpha": _cumulative_log_alpha(selected_returns, sp500_returns),
                "hit_rate_vs_sp500": sum(1 for row in model_rows if _bool(row.get("beats_sp500"))) / resolved_rounds,
                "hit_rate_vs_cash": sum(1 for row in model_rows if _bool(row.get("beats_cash"))) / resolved_rounds,
                "average_regret_vs_best_option": _average(regrets) if regrets else None,
                "best_round_alpha": max(alphas),
                "worst_round_alpha": min(alphas),
                "total_cost_usd": sum(available_costs) if available_costs else None,
                "average_cost_usd": _average(available_costs) if available_costs else None,
                "rounds_included": ",".join(row["round_id"] for row in model_rows),
            }
        )

    return sorted(
        cumulative_rows,
        key=lambda row: (
            -float(row["average_alpha_vs_sp500"]),
            -float(row["cumulative_log_alpha"]),
            -float(row["hit_rate_vs_sp500"]),
            str(row["model_id"]),
        ),
    )


def build_cumulative_stability(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["model_id"], []).append(row)

    cumulative_rows: list[dict[str, object]] = []
    for model_id, model_rows in grouped.items():
        repeated_returns = [_float(row["average_repeated_return"]) for row in model_rows]
        repeated_alphas = [_float(row["average_repeated_alpha_vs_sp500"]) for row in model_rows]
        consistency = [_float(row["consistency_rate"]) for row in model_rows]
        modal_alphas = [_float(row["modal_pick_alpha_vs_sp500"]) for row in model_rows]
        modal_returns = [_float(row["modal_pick_return"]) for row in model_rows]
        best_returns = [_float(row["best_replicate_return"]) for row in model_rows]
        worst_returns = [_float(row["worst_replicate_return"]) for row in model_rows]
        cost_values = [_optional_float(row.get("total_cost_usd")) for row in model_rows]
        available_costs = [cost for cost in cost_values if cost is not None]
        cumulative_rows.append(
            {
                "model_id": model_id,
                "provider": model_rows[0].get("provider", ""),
                "resolved_rounds": len(model_rows),
                "total_replicates": sum(int(_float(row["valid_replicates"])) for row in model_rows),
                "average_repeated_return": _average(repeated_returns),
                "average_repeated_alpha_vs_sp500": _average(repeated_alphas),
                "median_repeated_alpha_vs_sp500": statistics.median(repeated_alphas),
                "average_consistency_rate": _average(consistency),
                "average_modal_pick_alpha_vs_sp500": _average(modal_alphas),
                "average_modal_pick_return": _average(modal_returns),
                "average_best_replicate_return": _average(best_returns),
                "average_worst_replicate_return": _average(worst_returns),
                "best_round_repeated_alpha": max(repeated_alphas),
                "worst_round_repeated_alpha": min(repeated_alphas),
                "total_cost_usd": sum(available_costs) if available_costs else None,
                "average_cost_per_round": _average(available_costs) if available_costs else None,
                "rounds_included": ",".join(row["round_id"] for row in model_rows),
            }
        )

    return sorted(
        cumulative_rows,
        key=lambda row: (
            -float(row["average_repeated_alpha_vs_sp500"]),
            -float(row["average_consistency_rate"]),
            -float(row["average_modal_pick_alpha_vs_sp500"]),
            str(row["model_id"]),
        ),
    )


def publish_cumulative(
    rounds_dir: Path,
    output: Path,
    selection_path: Path | None = None,
) -> CumulativeOutput:
    status = cumulative_status(rounds_dir, selection_path)
    official_input_rows: list[dict[str, str]] = []
    stability_input_rows: list[dict[str, str]] = []
    for selected in status.selections:
        for row in selected.official_rows:
            official_input_rows.append({**row, "round_id": selected.round_id})
        for row in selected.stability_rows:
            stability_input_rows.append({**row, "round_id": selected.round_id})

    official_rows = build_cumulative_official(official_input_rows) if official_input_rows else []
    stability_rows = build_cumulative_stability(stability_input_rows) if stability_input_rows else []
    latest_round_id = _latest_round_id(status.selections)
    round_index_rows = _build_round_index(status.selections, latest_round_id=latest_round_id)

    output.mkdir(parents=True, exist_ok=True)
    official_path = output / "official_leaderboard.csv"
    stability_path = output / "stability_leaderboard.csv"
    round_index_path = output / "round_index.csv"
    report_path = output / "cumulative_report.md"
    _write_csv(official_path, OFFICIAL_COLUMNS, official_rows)
    _write_csv(stability_path, STABILITY_COLUMNS, stability_rows)
    _write_csv(round_index_path, ROUND_INDEX_COLUMNS, round_index_rows)
    publish_cumulative_report(report_path, official_rows, stability_rows, round_index_rows, status)
    return CumulativeOutput(
        official_leaderboard_path=official_path,
        stability_leaderboard_path=stability_path,
        cumulative_report_path=report_path,
        round_index_path=round_index_path,
        status=status,
    )


def publish_latest(
    rounds_dir: Path,
    output: Path,
    selection_path: Path | None = None,
) -> LatestOutput:
    status = latest_status(rounds_dir, selection_path)
    if not status.selections:
        raise ValueError("no resolved official rounds found for latest leaderboard")
    selected = max(
        status.selections,
        key=lambda item: (item.decision_deadline_utc, item.round_id),
    )
    if not selected.official_rows or selected.official_run_id is None:
        raise ValueError("newest resolved round does not have a selected official run")

    output.mkdir(parents=True, exist_ok=True)
    leaderboard_path = output / "latest_round_leaderboard.csv"
    report_path = output / "latest_round_report.md"
    _write_csv(leaderboard_path, list(selected.official_rows[0].keys()), selected.official_rows)
    _write_latest_report(report_path, selected, status)
    return LatestOutput(
        latest_leaderboard_path=leaderboard_path,
        latest_report_path=report_path,
        selected_round=selected,
        status=status,
    )


def latest_status(rounds_dir: Path, selection_path: Path | None = None) -> CumulativeStatus:
    selection = load_selection(selection_path)
    round_paths = discover_rounds(rounds_dir)
    round_paths_by_id = {load_manifest(path).round_id: path for path in round_paths}
    selections: list[CumulativeRoundSelection] = []
    skipped_rounds: dict[str, list[str]] = {}
    warnings: list[str] = []

    paths_to_scan: list[Path]
    if selection:
        missing = [round_id for round_id in selection if round_id not in round_paths_by_id]
        if missing:
            raise ValueError(f"selected round_id not found under {rounds_dir}: {missing[0]}")
        paths_to_scan = [round_paths_by_id[round_id] for round_id in selection]
    else:
        paths_to_scan = round_paths

    for round_path in paths_to_scan:
        selected = _select_latest_run_for_round(round_path, selection)
        if selected.official_rows:
            selections.append(selected)
        else:
            skipped_rounds[selected.round_id] = selected.warnings
        warnings.extend(selected.warnings)
    return CumulativeStatus(selections=selections, skipped_rounds=skipped_rounds, warnings=warnings)


def publish_cumulative_report(
    report_path: Path,
    official_rows: list[dict[str, object]],
    stability_rows: list[dict[str, object]],
    round_index_rows: list[dict[str, object]],
    status: CumulativeStatus,
) -> Path:
    report = "\n\n".join(
        [
            "# CapitalBench Cumulative Results",
            "## What This Is\n\n"
            "Each round is a separate one-month market decision. "
            "Official results use one call per model. Stability results use repeated calls per model. "
            "Models may have different numbers of resolved rounds because new models enter CapitalBench only in future rounds. "
            "We do not backfill models into past official rounds. "
            "The official and stability leaderboards are separate, and there is no combined weighted score.",
            "## Cumulative Official Leaderboard\n\n"
            + _markdown_table(
                _ranked_report_rows(official_rows, _official_report_row),
                [
                    "Rank",
                    "Model",
                    "Provider",
                    "Resolved Rounds",
                    "Avg Return",
                    "Avg S&P Return",
                    "Avg Alpha",
                    "Hit Rate vs S&P",
                    "Avg Regret",
                    "Cumulative Return",
                    "Cumulative S&P Return",
                ],
            ),
            "## Cumulative Stability Leaderboard\n\n"
            + _markdown_table(
                _ranked_report_rows(stability_rows, _stability_report_row),
                [
                    "Rank",
                    "Model",
                    "Provider",
                    "Resolved Rounds",
                    "Total Replicates",
                    "Avg Repeated Alpha",
                    "Avg Consistency",
                    "Avg Modal Pick Alpha",
                    "Best Round",
                    "Worst Round",
                ],
            ),
            "## Round Index\n\n"
            + _markdown_table(
                [
                    {
                        "Round": row["round_id"],
                        "Official Run": row["official_run_id"],
                        "Stability Run": row["stability_run_id"],
                        "Official Included": row["included_in_official_cumulative"],
                        "Stability Included": row["included_in_stability_cumulative"],
                        "Warnings": row["warnings"],
                    }
                    for row in round_index_rows
                ],
                ["Round", "Official Run", "Stability Run", "Official Included", "Stability Included", "Warnings"],
            ),
            "## Methodology\n\n"
            "Official cumulative score: For each model, we average its official one-shot alpha versus the S&P 500 across the rounds where each model participated.\n\n"
            "Stability cumulative score: For each model, we average its repeated-run alpha and consistency across the rounds where each model participated.\n\n"
            "The cumulative official leaderboard is sorted by average alpha versus the S&P 500 across the rounds where each model participated.\n\n"
            "The cumulative stability leaderboard is sorted by average repeated-run alpha versus the S&P 500 across the rounds where each model participated.\n\n"
            "The official leaderboard measures one-shot decision quality. The stability leaderboard measures consistency under repeated calls. They are not combined.",
            "## Limitations\n\n"
            "- A small number of rounds may be noisy.\n"
            "- One-month market returns are noisy.\n"
            "- Models can win by luck.\n"
            "- This is not financial advice.\n"
            "- Provider costs and hidden reasoning tokens may not be directly comparable.\n"
            "- Only resolved rounds are included.",
        ]
    )
    if status.warnings:
        report += "\n\n## Warnings\n\n" + "\n".join(f"- {warning}" for warning in status.warnings)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report + "\n", encoding="utf-8")
    return report_path


def _select_latest_run_for_round(
    round_path: Path,
    selection: dict[str, dict[str, str]] | None,
) -> CumulativeRoundSelection:
    manifest = load_manifest(round_path)
    round_id = manifest.round_id
    horizon_days = _horizon_days(manifest.entry_date, manifest.exit_date)
    explicit = selection.get(round_id) if selection else None
    warnings: list[str] = []
    if explicit:
        official_run_id = explicit["official_run_id"]
        _require_selected_run(
            round_path,
            official_run_id,
            expected_run_type="official",
            official=True,
        )
    else:
        eligible_official_run_ids: list[str] = []
        for run_id in list_run_ids(round_path):
            paths = get_run_paths(round_path, run_id)
            manifest_data = read_run_manifest(paths)
            if (
                str(manifest_data.get("run_type") or "") == "official"
                and manifest_data.get("mock") is not True
                and bool(manifest_data.get("official_score_eligible"))
                and (paths.results_dir / "leaderboard.csv").exists()
            ):
                eligible_official_run_ids.append(run_id)
        if len(eligible_official_run_ids) > 1:
            raise ValueError(
                f"Round {round_id} has multiple official-score-eligible runs. "
                "Add cumulative_selection.yaml or pass explicit selections."
            )
        official_run_id = eligible_official_run_ids[0] if len(eligible_official_run_ids) == 1 else None

    official_rows = load_official_results(round_path, official_run_id) if official_run_id else []
    if not official_rows:
        warnings.append(f"Round {round_id} has no scored official run.")
    return CumulativeRoundSelection(
        round_id=round_id,
        round_path=round_path,
        decision_deadline_utc=manifest.decision_deadline or "",
        horizon_days=horizon_days,
        official_run_id=official_run_id,
        stability_run_id=None,
        official_rows=official_rows,
        stability_rows=[],
        warnings=warnings,
    )


def _require_selected_run(
    round_path: Path,
    run_id: str,
    *,
    expected_run_type: str,
    official: bool,
    allow_mock: bool = False,
) -> None:
    run_paths = get_run_paths(round_path, run_id)
    if not run_paths.run_path.exists():
        raise FileNotFoundError(f"selected run does not exist: {round_path.name}/{run_id}")
    manifest = read_run_manifest(run_paths)
    run_type = str(manifest.get("run_type") or "")
    if run_type != expected_run_type:
        raise ValueError(f"selected run {run_id} is not run_type {expected_run_type}: {run_type}")
    if not allow_mock and manifest.get("mock") is True:
        raise ValueError(f"selected run {run_id} is mock and cannot be used in public cumulative leaderboards")
    if official and not bool(manifest.get("official_score_eligible")):
        raise ValueError(f"selected official run is not official_score_eligible: {run_id}")
    expected_file = "leaderboard.csv" if expected_run_type == "official" else "stability.csv"
    if not (run_paths.results_dir / expected_file).exists():
        raise FileNotFoundError(f"selected run is not scored; missing results/{expected_file}: {run_id}")


def _latest_round_id(selections: list[CumulativeRoundSelection]) -> str | None:
    if not selections:
        return None
    selected = max(selections, key=lambda item: (item.decision_deadline_utc, item.round_id))
    return selected.round_id


def _build_round_index(
    selections: list[CumulativeRoundSelection],
    latest_round_id: str | None = None,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for selected in selections:
        rows.append(
            {
                "round_id": selected.round_id,
                "decision_deadline_utc": selected.decision_deadline_utc,
                "horizon_days": selected.horizon_days if selected.horizon_days is not None else "",
                "official_run_id": selected.official_run_id or "",
                "stability_run_id": selected.stability_run_id or "",
                "official_models_count": len(selected.official_rows),
                "stability_models_count": len(selected.stability_rows),
                "included_in_latest": "yes" if selected.round_id == latest_round_id else "no",
                "included_in_official_cumulative": "yes" if selected.official_rows else "no",
                "included_in_stability_cumulative": "yes" if selected.stability_rows else "no",
                "warnings": " | ".join(selected.warnings),
            }
        )
    return rows


def _write_latest_report(
    report_path: Path,
    selected: CumulativeRoundSelection,
    status: CumulativeStatus,
) -> None:
    manifest = load_manifest(selected.round_path)
    run_paths = get_run_paths(selected.round_path, selected.official_run_id or "")
    run_manifest = read_run_manifest(run_paths)
    returns = _read_csv(run_paths.results_dir / "returns.csv")
    leaderboard_columns = [
        "model_id",
        "selected_option_id",
        "confidence",
        "selected_asset_return",
        "alpha_vs_sp500",
        "regret_vs_best_option",
        "rank_among_options",
        "beats_sp500",
        "beats_cash",
    ]
    decision_columns = ["model_id", "provider", "selected_option_id", "confidence", "rationale_summary", "key_risks"]
    return_columns = ["option_id", "label", "entry_price", "exit_price", "return", "rank"]
    report = "\n\n".join(
        [
            "# CapitalBench Latest Round Leaderboard",
            "## Round\n\n"
            f"- Round ID: {selected.round_id}\n"
            f"- Decision deadline: {selected.decision_deadline_utc}\n"
            f"- Horizon: {manifest.horizon}\n"
            f"- Official run ID: {selected.official_run_id}\n"
            f"- Mock: {'yes' if run_manifest.get('mock') else 'no'}",
            "## Model Decisions\n\n" + _markdown_table(selected.official_rows, decision_columns),
            "## Realized Returns\n\n" + _markdown_table(returns, return_columns),
            "## Official Leaderboard\n\n" + _markdown_table(selected.official_rows, leaderboard_columns),
            "## Notes\n\n"
            "- This is one standalone round.\n"
            "- Cumulative results are separate.\n"
            "- Stability results are separate and do not affect this leaderboard.",
        ]
    )
    if status.warnings:
        report += "\n\n## Warnings\n\n" + "\n".join(f"- {warning}" for warning in status.warnings)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report + "\n", encoding="utf-8")


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, columns: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: _csv_value(row.get(column)) for column in columns})


def _markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    if not rows:
        return "_No rows._"
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _column in columns) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    return "\n".join(lines)


def _ranked_report_rows(rows: list[dict[str, object]], transform) -> list[dict[str, object]]:
    transformed: list[dict[str, object]] = []
    for rank, row in enumerate(rows, start=1):
        transformed.append({"Rank": rank, **transform(row)})
    return transformed


def _official_report_row(row: dict[str, object]) -> dict[str, object]:
    return {
        "Model": row["model_id"],
        "Provider": row["provider"],
        "Resolved Rounds": row["resolved_rounds"],
        "Avg Return": _pct(row["average_official_return"]),
        "Avg S&P Return": _pct(row["average_sp500_return"]),
        "Avg Alpha": _pct(row["average_alpha_vs_sp500"]),
        "Hit Rate vs S&P": _pct(row["hit_rate_vs_sp500"]),
        "Avg Regret": _pct(row["average_regret_vs_best_option"]),
        "Cumulative Return": _pct(row["cumulative_model_return"]),
        "Cumulative S&P Return": _pct(row["cumulative_sp500_return"]),
    }


def _stability_report_row(row: dict[str, object]) -> dict[str, object]:
    return {
        "Model": row["model_id"],
        "Provider": row["provider"],
        "Resolved Rounds": row["resolved_rounds"],
        "Total Replicates": row["total_replicates"],
        "Avg Repeated Alpha": _pct(row["average_repeated_alpha_vs_sp500"]),
        "Avg Consistency": _pct(row["average_consistency_rate"]),
        "Avg Modal Pick Alpha": _pct(row["average_modal_pick_alpha_vs_sp500"]),
        "Best Round": _pct(row["best_round_repeated_alpha"]),
        "Worst Round": _pct(row["worst_round_repeated_alpha"]),
    }


def _horizon_days(entry_date: str | None, exit_date: str | None) -> int | None:
    if not entry_date or not exit_date:
        return None
    try:
        return (date.fromisoformat(exit_date) - date.fromisoformat(entry_date)).days
    except ValueError:
        return None


def _float(value: str | object) -> float:
    return float(value)


def _optional_float(value: str | object | None) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


def _bool(value: str | object | None) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes"}


def _average(values: list[float]) -> float:
    return sum(values) / len(values)


def _compound(returns: list[float]) -> float:
    value = 1.0
    for item in returns:
        value *= 1 + item
    return value - 1


def _cumulative_log_alpha(model_returns: list[float], sp500_returns: list[float]) -> float:
    total = 0.0
    for model_return, sp500_return in zip(model_returns, sp500_returns):
        if model_return <= -1 or sp500_return <= -1:
            raise ValueError("cannot calculate cumulative_log_alpha for returns <= -100%")
        total += math.log(1 + model_return) - math.log(1 + sp500_return)
    return total


def _csv_value(value: object) -> object:
    return "" if value is None else value


def _pct(value: object) -> str:
    if value is None or value == "":
        return ""
    return f"{float(value) * 100:.2f}%"

from __future__ import annotations

import csv
from pathlib import Path

from .hashing import compute_round_hashes
from .io import load_manifest, load_options
from .portfolio import constraints_from_manifest, submission_format_from_manifest
from .research import final_briefing_matches_round_briefing, research_artifact_rows
from .run_store import RunPaths, get_run_paths, get_selected_run_paths, read_run_manifest
from .validation import _load_submission, iter_submission_files, validate_submission_payload


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"missing results file: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _markdown_table(rows: list[dict[str, str]], columns: list[str]) -> str:
    if not rows:
        return "_No rows._"
    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, divider]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    return "\n".join(lines)


def _sort_cost_adjusted(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    with_cost = [row for row in rows if row.get("alpha_per_dollar")]
    return sorted(with_cost, key=lambda row: float(row["alpha_per_dollar"]), reverse=True)


def _invalid_submission_summary(round_path: Path, run_paths: RunPaths) -> tuple[int, list[str]]:
    manifest = load_manifest(round_path)
    options = load_options(round_path)
    submission_format = submission_format_from_manifest(manifest)
    portfolio_constraints = constraints_from_manifest(manifest)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)
    invalid_files: list[str] = []
    for raw_file in iter_submission_files(run_paths.raw_dir):
        try:
            validate_submission_payload(
                _load_submission(raw_file),
                options,
                manifest.round_id,
                run_type=run_type,
                replicate_count=replicate_count,
                require_run_metadata=run_type in {"official", "stability", "retrospective"},
                submission_format=submission_format,
                portfolio_constraints=portfolio_constraints,
            )
        except Exception:
            invalid_files.append(raw_file.name)
    return len(invalid_files), sorted(invalid_files)


def _reproducibility_section(round_path: Path) -> str:
    current_hashes = compute_round_hashes(round_path)
    rows = [
        {"file": filename, "sha256": current_hashes["files"][filename]}
        for filename in current_hashes["files"]
    ]
    hashes_match = False
    hashes_path = round_path / "hashes.json"
    if hashes_path.exists():
        import json

        try:
            hashes_match = json.loads(hashes_path.read_text(encoding="utf-8")) == current_hashes
        except Exception:
            hashes_match = False
    return (
        f"- hashes.json matches current files: {'yes' if hashes_match else 'no'}\n\n"
        + _markdown_table(rows, ["file", "sha256"])
    )


def _research_artifacts_section(round_path: Path) -> str:
    rows = research_artifact_rows(round_path)
    if not any(row["exists"] == "yes" for row in rows):
        return "_No research artifacts found._"
    briefing_match = final_briefing_matches_round_briefing(round_path)
    match_text = "unavailable" if briefing_match is None else ("yes" if briefing_match else "no")
    return (
        "- Market fact report: stored in research/market_fact_report.md, audit-only\n"
        "- Briefing audit report: stored in research/briefing_audit_report.md, audit-only\n"
        "- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing\n"
        f"- final_briefing.md hash matches briefing.md: {match_text}\n\n"
        + _markdown_table(rows, ["artifact", "path", "visibility", "sha256", "exists"])
    )


def publish_report(round_path: Path, run_id: str | None = None) -> Path:
    manifest = load_manifest(round_path)
    options = load_options(round_path)
    run_paths = get_selected_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    if run_type == "stability":
        return _publish_stability_report(round_path, run_paths, manifest, options, run_manifest)
    return _publish_official_report(round_path, run_paths, manifest, options, run_manifest)


def _publish_official_report(
    round_path: Path,
    run_paths: RunPaths,
    manifest,
    options,
    run_manifest: dict[str, object],
) -> Path:
    results_dir = run_paths.results_dir
    returns = _read_csv(results_dir / "returns.csv")
    leaderboard = _read_csv(results_dir / "leaderboard.csv")
    allocations = _read_csv(results_dir / "allocations.csv") if (results_dir / "allocations.csv").exists() else []
    cost_adjusted = _sort_cost_adjusted(leaderboard)
    invalid_count, invalid_files = _invalid_submission_summary(round_path, run_paths)

    selected_columns = [
        "model_id",
        "provider",
        "submission_format",
        "selected_option_id",
        "holding_count",
        "confidence",
        "rationale_summary",
        "key_risks",
    ]
    leaderboard_columns = [
        "model_id",
        "selected_option_id",
        "holding_count",
        "confidence",
        "selected_asset_return",
        "portfolio_return",
        "alpha_vs_sp500",
        "regret_vs_best_option",
        "rank_among_options",
        "beats_sp500",
        "beats_cash",
    ]
    cost_columns = ["model_id", "selected_option_id", "alpha_vs_sp500", "cost_usd", "alpha_per_dollar"]
    return_columns = ["option_id", "label", "entry_price", "exit_price", "return", "rank"]
    allocation_columns = ["model_id", "option_id", "allocation_pct", "option_return", "return_contribution", "rationale"]

    report = "\n\n".join(
        [
            f"# CapitalBench Report: {manifest.round_id} / {run_paths.run_id}",
            _official_heading(run_manifest),
            "## Round Summary\n\n"
            f"- Run ID: {run_paths.run_id}\n"
            f"- Run type: {run_manifest.get('run_type')}\n"
            f"- Replicates: {run_manifest.get('replicates')}\n"
            f"- Mock: {'yes' if run_manifest.get('mock') else 'no'}\n"
            f"- Title: {manifest.title}\n"
            f"- Description: {manifest.description}\n"
            f"- Decision date: {manifest.decision_date or ''}\n"
            f"- Decision deadline: {manifest.decision_deadline or ''}\n"
            f"- Horizon: {manifest.horizon}\n"
            f"- Entry date: {manifest.entry_date or ''}\n"
            f"- Exit date: {manifest.exit_date or ''}\n"
            f"- Entry rule: {manifest.entry_rule}\n"
            f"- Exit rule: {manifest.exit_rule}\n"
            f"- Options: {len(options)}",
            "## Model Decisions\n\n" + _markdown_table(leaderboard, selected_columns),
            "## Realized Returns\n\n" + _markdown_table(returns, return_columns),
            "## Portfolio Allocations\n\n"
            + (_markdown_table(allocations, allocation_columns) if allocations else "_No allocation rows found._"),
            "## Leaderboard\n\nOfficial One-Shot Leaderboard\n\n"
            + _markdown_table(leaderboard, leaderboard_columns),
            "## Cost-Adjusted Leaderboard\n\n"
            + (_markdown_table(cost_adjusted, cost_columns) if cost_adjusted else "_No cost data available._"),
            "## Invalid Submissions\n\n"
            + f"- Invalid raw submissions: {invalid_count}\n"
            + (f"- Files: {', '.join(invalid_files)}" if invalid_files else "- Files: none"),
            "## Reproducibility\n\n" + _reproducibility_section(round_path),
            "## Research Artifacts\n\n" + _research_artifacts_section(round_path),
            "## Limitations\n\n"
            "- Prices are loaded from local CSV files and are not fetched live.\n"
            "- Official scoring uses the round's declared submission format.\n"
            "- Stability analysis, when present, is separate and does not change this leaderboard.\n"
            "- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.\n"
            "- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.",
        ]
    )

    report_path = results_dir / "report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report + "\n", encoding="utf-8")
    return report_path


def _official_heading(run_manifest: dict[str, object]) -> str:
    if run_manifest.get("run_type") == "retrospective":
        return (
            "## Retrospective / Not Official\n\n"
            "Retrospective / not official. This run is excluded from official and cumulative leaderboards."
        )
    return (
        "## Official One-Shot Leaderboard\n\n"
        "This is the official CapitalBench score for this run.\n\n"
        + ("_This run used mock execution and is not a public benchmark result._" if run_manifest.get("mock") else "")
    )


def _publish_stability_report(
    round_path: Path,
    run_paths: RunPaths,
    manifest,
    options,
    run_manifest: dict[str, object],
) -> Path:
    results_dir = run_paths.results_dir
    repeated_picks = _read_csv(results_dir / "returns.csv")
    stability = _read_csv(results_dir / "stability.csv")
    invalid_count, invalid_files = _invalid_submission_summary(round_path, run_paths)

    repeated_columns = [
        "model_id",
        "replicate_index",
        "selected_option_id",
        "selected_asset_return",
        "alpha_vs_sp500",
        "cost_usd",
    ]
    stability_columns = [
        "model_id",
        "provider",
        "valid_replicates",
        "invalid_replicates",
        "pick_distribution",
        "modal_pick",
        "consistency_rate",
        "average_repeated_return",
        "average_repeated_alpha_vs_sp500",
        "best_replicate_option_id",
        "best_replicate_return",
        "worst_replicate_option_id",
        "worst_replicate_return",
        "total_cost_usd",
        "average_cost_usd",
        "notes",
    ]

    report = "\n\n".join(
        [
            f"# CapitalBench Report: {manifest.round_id} / {run_paths.run_id}",
            "## Multi-Run Stability Analysis\n\n"
            "This is not the official leaderboard. It measures decision stability under repeated calls.\n\n"
            f"- Replicate count: {run_manifest.get('replicates')}\n"
            f"- Mock: {'yes' if run_manifest.get('mock') else 'no'}",
            "## Round Summary\n\n"
            f"- Run ID: {run_paths.run_id}\n"
            f"- Run type: {run_manifest.get('run_type')}\n"
            f"- Title: {manifest.title}\n"
            f"- Decision deadline: {manifest.decision_deadline or ''}\n"
            f"- Horizon: {manifest.horizon}\n"
            f"- Entry rule: {manifest.entry_rule}\n"
            f"- Exit rule: {manifest.exit_rule}\n"
            f"- Options: {len(options)}",
            "## All Repeated Picks\n\n" + _markdown_table(repeated_picks, repeated_columns),
            "## Stability Table\n\n" + _markdown_table(stability, stability_columns),
            "## Invalid Submissions\n\n"
            + f"- Invalid raw submissions: {invalid_count}\n"
            + (f"- Files: {', '.join(invalid_files)}" if invalid_files else "- Files: none"),
            "## Reproducibility\n\n" + _reproducibility_section(round_path),
            "## Research Artifacts\n\n" + _research_artifacts_section(round_path),
            "## Limitations\n\n"
            "- Stability analysis is secondary and does not replace the official one-shot leaderboard.\n"
            "- Repeated calls use the same prompt, briefing, and options, but provider systems may still vary internally.\n"
            "- Prices are loaded from local CSV files and are not fetched live.\n"
            "- Scores follow the round's declared submission format; portfolio rounds use weighted allocations.",
        ]
    )

    report_path = results_dir / "report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report + "\n", encoding="utf-8")
    return report_path


def publish_round_summary(
    round_path: Path,
    official_run_id: str,
    stability_run_id: str,
) -> Path:
    manifest = load_manifest(round_path)
    official_paths = get_run_paths(round_path, official_run_id)
    stability_paths = get_run_paths(round_path, stability_run_id)
    official_leaderboard = _read_csv(official_paths.results_dir / "leaderboard.csv")
    stability = _read_csv(stability_paths.results_dir / "stability.csv")

    leaderboard_columns = [
        "model_id",
        "submission_format",
        "selected_option_id",
        "holding_count",
        "selected_asset_return",
        "alpha_vs_sp500",
        "regret_vs_best_option",
        "rank_among_options",
    ]
    stability_columns = [
        "model_id",
        "pick_distribution",
        "modal_pick",
        "consistency_rate",
        "average_repeated_return",
        "average_repeated_alpha_vs_sp500",
        "best_replicate_option_id",
        "worst_replicate_option_id",
    ]

    summary = "\n\n".join(
        [
            f"# CapitalBench Round Summary: {manifest.round_id}",
            "## Round Overview\n\n"
            f"- Title: {manifest.title}\n"
            f"- Description: {manifest.description}\n"
            f"- Decision deadline: {manifest.decision_deadline or ''}\n"
            f"- Horizon: {manifest.horizon}\n"
            f"- Entry rule: {manifest.entry_rule}\n"
            f"- Exit rule: {manifest.exit_rule}\n"
            f"- Submission format: {getattr(manifest, 'submission_format', 'single_pick')}\n"
            f"- Official run ID: {official_run_id}\n"
            f"- Stability run ID: {stability_run_id}",
            "## Result Types\n\n"
            "The official leaderboard and stability analysis are separate. "
            "The official leaderboard is the one-shot score. Stability measures repeated-call consistency. "
            "CapitalBench does not create a combined weighted score.",
            "## Official One-Shot Leaderboard\n\n"
            + _markdown_table(official_leaderboard, leaderboard_columns),
            "## Multi-Run Stability Analysis\n\n"
            + _markdown_table(stability, stability_columns),
            "## Reproducibility\n\n" + _reproducibility_section(round_path),
            "## Research Artifacts\n\n" + _research_artifacts_section(round_path),
            "## Limitations\n\n"
            "- The official score uses exactly one scored decision per model.\n"
            "- Stability analysis is secondary and does not change the official leaderboard.\n"
            "- Prices are loaded from local CSV files and are not fetched live.\n"
            "- Scores follow the round's declared submission format; portfolio rounds use weighted allocations.",
        ]
    )
    summary_path = round_path / "round_summary.md"
    summary_path.write_text(summary + "\n", encoding="utf-8")
    return summary_path

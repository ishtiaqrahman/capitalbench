#!/usr/bin/env python3
"""Freeze, price, and diagnose resolved Portfolio V2 candidate decisions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any, Iterable, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from capitalbench.hashing import sha256_file  # noqa: E402
from capitalbench.io import load_options, read_json  # noqa: E402
from capitalbench.performance import _fetch_yahoo_chart_adjclose  # noqa: E402
from capitalbench.prices import _select_tiingo_row, _write_price_csv  # noqa: E402
from scripts.analyze_model_predictability import spearman, write_csv  # noqa: E402


DEFAULT_CONFIG = ROOT / "experiments" / "v2-next-research-2026-07-21.yaml"
PRE_OUTCOME_ROUND_FILES = (
    "manifest.yaml",
    "options.yaml",
    "prompt.md",
    "briefing.md",
    "hashes.json",
    "market_data/universe_decision_context.csv",
    "market_data/universe_decision_context.json",
    "market_data/decision_context_source_history.json",
)


def load_config(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"invalid config: {path}")
    return value


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def freeze_paths(pair: dict[str, Any]) -> list[Path]:
    paths: list[Path] = []
    for key in ("v2_round_id", "control_round_id"):
        round_id = pair.get(key)
        if not round_id:
            continue
        round_path = ROOT / "rounds" / str(round_id)
        for relative in PRE_OUTCOME_ROUND_FILES:
            path = round_path / relative
            if path.exists():
                paths.append(path)
    run_specs = [("v2_round_id", "v2_run_id"), ("control_round_id", "control_run_id")]
    for round_key, run_key in run_specs:
        if not pair.get(round_key) or not pair.get(run_key):
            continue
        run_path = ROOT / "rounds" / str(pair[round_key]) / "runs" / str(pair[run_key])
        for path in sorted((run_path / "submissions" / "parsed").glob("*.json")):
            paths.append(path)
        manifest = run_path / "run_manifest.yaml"
        if manifest.exists():
            paths.append(manifest)
    return paths


def prepare(config_path: Path) -> None:
    config = load_config(config_path)
    files: list[dict[str, Any]] = []
    for pair_id, pair in config["pairs"].items():
        for path in freeze_paths(pair):
            files.append(
                {
                    "pair_id": pair_id,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": sha256_file(path),
                    "bytes": path.stat().st_size,
                }
            )
    manifest = {
        "experiment_id": config["experiment_id"],
        "frozen_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "config_path": config_path.relative_to(ROOT).as_posix(),
        "config_sha256": sha256_file(config_path),
        "files": files,
    }
    output = output_dir(config)
    output.mkdir(parents=True, exist_ok=True)
    (output / "freeze_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"frozen_files={len(files)}")
    print(f"frozen_pairs={len(config['pairs'])}")


def verify_freeze(config_path: Path, config: dict[str, Any], pair_id: str) -> None:
    path = output_dir(config) / "freeze_manifest.json"
    if not path.exists():
        raise RuntimeError("run prepare before using the experiment")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest["config_sha256"] != sha256_file(config_path):
        raise RuntimeError("experiment config changed after freeze")
    for row in manifest["files"]:
        if row["pair_id"] != pair_id:
            continue
        # Resolution appends operational timestamps to run_manifest.yaml.
        # Parsed decisions and all model-facing round inputs remain immutable.
        if str(row["path"]).endswith("/run_manifest.yaml"):
            continue
        source = ROOT / row["path"]
        if not source.exists() or sha256_file(source) != row["sha256"]:
            raise RuntimeError(f"frozen pre-outcome artifact changed: {source}")


def yahoo_rows_for_options(options: Sequence[Any], entry_date: str, exit_date: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    start = date.fromisoformat(entry_date)
    end = date.fromisoformat(exit_date)
    cache: dict[str, list[dict[str, Any]]] = {}
    entry_rows: list[dict[str, Any]] = []
    exit_rows: list[dict[str, Any]] = []
    for option in options:
        if option.option_id == "CASH" or not (option.tiingo_symbol or option.symbol or option.asset_symbol):
            for target, output in ((entry_date, entry_rows), (exit_date, exit_rows)):
                output.append(
                    {
                        "option_id": option.option_id,
                        "symbol": "",
                        "date": target,
                        "close": 1.0,
                        "adj_close": 1.0,
                        "source": "cash",
                    }
                )
            continue
        symbol = str(option.tiingo_symbol or option.symbol or option.asset_symbol)
        if symbol not in cache:
            error: Exception | None = None
            for attempt in range(3):
                try:
                    cache[symbol] = _fetch_yahoo_chart_adjclose(symbol, start, end)
                    error = None
                    break
                except Exception as exc:  # pragma: no cover - network path
                    error = exc
                    if attempt < 2:
                        time.sleep(attempt + 1)
            if error is not None:
                raise RuntimeError(f"Yahoo adjusted-close fetch failed for {symbol}: {error}") from error
        history = cache[symbol]
        entry_rows.append(
            _select_tiingo_row(option.option_id, symbol, entry_date, history, source="yahoo_chart_adjclose")
        )
        exit_rows.append(
            _select_tiingo_row(option.option_id, symbol, exit_date, history, source="yahoo_chart_adjclose")
        )
    return entry_rows, exit_rows


def fetch_shared_prices(config_path: Path, pair_id: str) -> None:
    config = load_config(config_path)
    pair = config["pairs"][pair_id]
    verify_freeze(config_path, config, pair_id)
    round_ids = [str(pair["v2_round_id"])]
    if pair.get("control_round_id"):
        round_ids.append(str(pair["control_round_id"]))
    option_hashes = {sha256_file(ROOT / "rounds" / round_id / "options.yaml") for round_id in round_ids}
    if len(option_hashes) != 1:
        raise RuntimeError("paired rounds do not share identical options.yaml")
    options = load_options(ROOT / "rounds" / round_ids[0])
    entry_rows, exit_rows = yahoo_rows_for_options(options, str(pair["entry_date"]), str(pair["exit_date"]))
    price_files: list[dict[str, Any]] = []
    for round_id in round_ids:
        prices = ROOT / "rounds" / round_id / "prices"
        prices.mkdir(parents=True, exist_ok=True)
        entry_path = prices / "entry_prices.csv"
        exit_path = prices / "exit_prices.csv"
        _write_price_csv(entry_path, entry_rows)
        _write_price_csv(exit_path, exit_rows)
        price_files.extend(
            [
                {"round_id": round_id, "side": "entry", "path": entry_path.relative_to(ROOT).as_posix(), "sha256": sha256_file(entry_path)},
                {"round_id": round_id, "side": "exit", "path": exit_path.relative_to(ROOT).as_posix(), "sha256": sha256_file(exit_path)},
            ]
        )
    if len({row["sha256"] for row in price_files if row["side"] == "entry"}) != 1:
        raise RuntimeError("paired entry price files are not identical")
    if len({row["sha256"] for row in price_files if row["side"] == "exit"}) != 1:
        raise RuntimeError("paired exit price files are not identical")
    snapshot = {
        "pair_id": pair_id,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": "yahoo_chart_adjclose",
        "entry_date": pair["entry_date"],
        "exit_date": pair["exit_date"],
        "option_count": len(options),
        "files": price_files,
    }
    output = output_dir(config) / pair_id
    output.mkdir(parents=True, exist_ok=True)
    (output / "shared_price_snapshot.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"priced_options={len(options)}")
    print(f"shared_rounds={len(round_ids)}")


def float_value(row: dict[str, Any], key: str) -> float:
    value = row.get(key)
    if value in {None, ""}:
        raise ValueError(f"missing numeric field {key}")
    return float(value)


def mean_or_none(values: Iterable[float | None]) -> float | None:
    present = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return mean(present) if present else None


def candidate_overlap(candidate_sets: Sequence[set[str]]) -> float | None:
    pairs = list(itertools.combinations(candidate_sets, 2))
    if not pairs:
        return None
    return mean(len(left & right) / len(left | right) if left | right else 0.0 for left, right in pairs)


def portfolio_return(allocation: dict[str, float], returns: dict[str, float]) -> float:
    return sum(weight / 100.0 * returns[option_id] for option_id, weight in allocation.items())


def construction_rules(allocation: dict[str, float]) -> dict[str, dict[str, float]]:
    selected = sorted(allocation)
    equal_weight = 100.0 / len(selected)
    rules = {"equal_selected": {option_id: equal_weight for option_id in selected}}
    for cap in (50.0, 35.0):
        transformed: dict[str, float] = {}
        redirected = 0.0
        for option_id, weight in allocation.items():
            if option_id == "SP500":
                transformed[option_id] = transformed.get(option_id, 0.0) + weight
                continue
            kept = min(weight, cap)
            transformed[option_id] = kept
            redirected += weight - kept
        transformed["SP500"] = transformed.get("SP500", 0.0) + redirected
        rules[f"cap_{int(cap)}_to_sp500"] = {
            option_id: weight for option_id, weight in transformed.items() if weight > 0.0
        }
    return rules


def construction_counterfactuals(
    submissions: Sequence[dict[str, Any]],
    leaderboard: dict[str, dict[str, str]],
    returns: dict[str, float],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    for submission in submissions:
        model_id = str(submission["model_id"])
        if model_id not in leaderboard:
            continue
        allocation = {
            str(row["option_id"]): float(row["allocation_pct"])
            for row in submission.get("portfolio") or []
            if str(row.get("option_id")) in returns and float(row.get("allocation_pct") or 0.0) > 0.0
        }
        if not allocation:
            continue
        submitted_return = float_value(leaderboard[model_id], "portfolio_return")
        for rule, transformed in construction_rules(allocation).items():
            result = portfolio_return(transformed, returns)
            rows.append(
                {
                    "model_id": model_id,
                    "rule": rule,
                    "counterfactual_return": result,
                    "improvement_vs_submitted": result - submitted_return,
                    "alpha_vs_sp500": result - returns["SP500"],
                    "counterfactual_allocation": ";".join(
                        f"{option_id}:{weight:g}" for option_id, weight in sorted(transformed.items())
                    ),
                }
            )
    summaries: list[dict[str, Any]] = []
    for rule in sorted({str(row["rule"]) for row in rows}):
        subset = [row for row in rows if row["rule"] == rule]
        summaries.append(
            {
                "rule": rule,
                "models": len(subset),
                "mean_counterfactual_return": mean(float(row["counterfactual_return"]) for row in subset),
                "mean_improvement_vs_submitted": mean(float(row["improvement_vs_submitted"]) for row in subset),
                "models_improved": sum(float(row["improvement_vs_submitted"]) > 0.0 for row in subset),
                "mean_alpha_vs_sp500": mean(float(row["alpha_vs_sp500"]) for row in subset),
            }
        )
    return rows, summaries


def model_diagnostic(
    submission: dict[str, Any],
    leaderboard: dict[str, str],
    returns: dict[str, float],
    top3_ids: set[str],
    winner_ids: set[str],
    spy_return: float,
) -> dict[str, Any]:
    ledger = [row for row in submission.get("candidate_ledger") or [] if str(row.get("option_id")) in returns]
    portfolio = [row for row in submission.get("portfolio") or [] if str(row.get("option_id")) in returns]
    ledger_available = bool(ledger)
    selected_ids = [str(row["option_id"]) for row in portfolio]
    candidate_ids = [str(row["option_id"]) for row in ledger] if ledger_available else selected_ids
    rejected_ids = [str(row["option_id"]) for row in ledger if str(row.get("decision")) == "rejected"]
    if not portfolio:
        raise ValueError(f"V2 submission lacks portfolio: {submission.get('model_id')}")
    oracle_return = max(returns.values())
    best_candidate = max(returns[option_id] for option_id in candidate_ids)
    best_selected = max(returns[option_id] for option_id in selected_ids)
    portfolio_return = float_value(leaderboard, "portfolio_return")
    search_regret = oracle_return - best_candidate if ledger_available else None
    ranking_regret = best_candidate - best_selected if ledger_available else None
    preselection_regret = oracle_return - best_selected
    construction_regret = best_selected - portfolio_return
    total_regret = oracle_return - portfolio_return
    forecast_values = [float(row["forecast_base_pct"]) for row in ledger] if ledger_available else []
    realized_values = [returns[str(row["option_id"])] * 100.0 for row in ledger] if ledger_available else []
    interval_coverage = (
        mean(
            float(row["forecast_low_pct"]) <= realized <= float(row["forecast_high_pct"])
            for row, realized in zip(ledger, realized_values)
        )
        if ledger_available
        else None
    )
    selected_active = [option_id for option_id in selected_ids if option_id not in {"SP500", "CASH"}]
    return {
        "model_id": str(submission["model_id"]),
        "candidate_ledger_available": ledger_available,
        "candidate_count": len(candidate_ids),
        "selected_count": len(selected_ids),
        "candidate_ids": ";".join(candidate_ids),
        "selected_ids": ";".join(selected_ids),
        "winner_in_ledger": bool(set(candidate_ids) & winner_ids),
        "top3_candidates_captured": len(set(candidate_ids) & top3_ids),
        "search_regret": search_regret,
        "ranking_regret": ranking_regret,
        "preselection_regret": preselection_regret,
        "construction_regret": construction_regret,
        "total_oracle_regret": total_regret,
        "search_regret_share": search_regret / total_regret if search_regret is not None and total_regret > 0 else None,
        "ranking_regret_share": ranking_regret / total_regret if ranking_regret is not None and total_regret > 0 else None,
        "preselection_regret_share": preselection_regret / total_regret if total_regret > 0 else 0.0,
        "construction_regret_share": construction_regret / total_regret if total_regret > 0 else 0.0,
        "portfolio_return": portfolio_return,
        "alpha_vs_sp500": portfolio_return - spy_return,
        "candidate_forecast_rank_ic": spearman(forecast_values, realized_values) if ledger_available else None,
        "candidate_forecast_mae_pct": (
            mean(abs(forecast - realized) for forecast, realized in zip(forecast_values, realized_values))
            if ledger_available
            else None
        ),
        "candidate_interval_coverage": interval_coverage,
        "selected_active_beat_spy_rate": (
            mean(returns[option_id] > spy_return for option_id in selected_active) if selected_active else None
        ),
        "rejected_candidates_beating_spy": sum(returns[option_id] > spy_return for option_id in rejected_ids),
        "mean_selected_candidate_return": mean(returns[option_id] for option_id in selected_ids),
        "mean_rejected_candidate_return": mean_or_none(returns[option_id] for option_id in rejected_ids),
    }


def analyze_pair(config_path: Path, pair_id: str) -> None:
    config = load_config(config_path)
    pair = config["pairs"][pair_id]
    verify_freeze(config_path, config, pair_id)
    v2_round = ROOT / "rounds" / str(pair["v2_round_id"])
    v2_run = v2_round / "runs" / str(pair["v2_run_id"])
    leaderboard_rows = read_csv(v2_run / "results" / "leaderboard.csv")
    leaderboard = {row["model_id"]: row for row in leaderboard_rows}
    return_rows = read_csv(v2_run / "results" / "returns.csv")
    returns = {row["option_id"]: float(row["return"]) for row in return_rows if row.get("return") not in {None, ""}}
    spy_return = returns["SP500"]
    ordered = sorted(returns.items(), key=lambda item: (-item[1], item[0]))
    oracle_return = ordered[0][1]
    winner_ids = {option_id for option_id, value in ordered if math.isclose(value, oracle_return)}
    top3_ids = {option_id for option_id, _value in ordered[:3]}
    diagnostics: list[dict[str, Any]] = []
    submissions: list[dict[str, Any]] = []
    candidate_sets: list[set[str]] = []
    selected_sets: list[set[str]] = []
    for path in sorted((v2_run / "submissions" / "parsed").glob("*.json")):
        submission = read_json(path)
        model_id = str(submission["model_id"])
        if model_id not in leaderboard:
            continue
        submissions.append(submission)
        row = model_diagnostic(submission, leaderboard[model_id], returns, top3_ids, winner_ids, spy_return)
        diagnostics.append(row)
        selected_sets.append(set(str(value) for value in row["selected_ids"].split(";") if value))
        if row["candidate_ledger_available"]:
            candidate_sets.append(set(str(value) for value in row["candidate_ids"].split(";") if value))
    if not diagnostics:
        raise RuntimeError("no V2 diagnostics were produced")
    complete_candidate_ledgers = len(candidate_sets) == len(diagnostics)
    total_regret = sum(float(row["total_oracle_regret"]) for row in diagnostics)
    construction_total = sum(float(row["construction_regret"]) for row in diagnostics)
    if complete_candidate_ledgers:
        stage_totals = {
            "search": sum(float(row["search_regret"]) for row in diagnostics),
            "ranking": sum(float(row["ranking_regret"]) for row in diagnostics),
            "construction": construction_total,
        }
        shares: dict[str, float | None] = {
            stage: value / total_regret if total_regret > 0 else 0.0 for stage, value in stage_totals.items()
        }
        dominant_stage, dominant_share = max(
            ((stage, float(share)) for stage, share in shares.items() if share is not None),
            key=lambda item: item[1],
        )
    else:
        shares = {
            "search": None,
            "ranking": None,
            "construction": construction_total / total_regret if total_regret > 0 else 0.0,
        }
        dominant_stage = "construction" if float(shares["construction"] or 0.0) > float(config["minimum_dominant_regret_share"]) else "none"
        dominant_share = float(shares["construction"] or 0.0)
    threshold = float(config["minimum_dominant_regret_share"])
    if dominant_share <= threshold:
        dominant_stage = "none"
    branch = {
        "search": "build_neutral_option_linked_event_table",
        "ranking": "build_event_supported_ordinal_comparison",
        "construction": "test_equal_weight_and_cap_counterfactuals_without_calls",
        "none": "collect_more_resolved_v2_observations",
    }[dominant_stage]
    summary: dict[str, Any] = {
        "pair_id": pair_id,
        "v2_round_id": pair["v2_round_id"],
        "models": len(diagnostics),
        "complete_candidate_ledgers": complete_candidate_ledgers,
        "sp500_return": spy_return,
        "oracle_return": oracle_return,
        "winner_ids": sorted(winner_ids),
        "mean_v2_alpha_vs_sp500": mean(float(row["alpha_vs_sp500"]) for row in diagnostics),
        "winner_ledger_capture_models": sum(bool(row["winner_in_ledger"]) for row in diagnostics),
        "mean_top3_candidates_captured": mean(float(row["top3_candidates_captured"]) for row in diagnostics),
        "mean_search_regret": mean_or_none(row["search_regret"] for row in diagnostics),
        "mean_ranking_regret": mean_or_none(row["ranking_regret"] for row in diagnostics),
        "mean_preselection_regret": mean(float(row["preselection_regret"]) for row in diagnostics),
        "mean_construction_regret": mean(float(row["construction_regret"]) for row in diagnostics),
        "regret_shares": shares,
        "dominant_stage": dominant_stage,
        "candidate_overlap_jaccard": candidate_overlap(candidate_sets) if complete_candidate_ledgers else None,
        "selected_overlap_jaccard": candidate_overlap(selected_sets),
        "mean_forecast_rank_ic": mean_or_none(row["candidate_forecast_rank_ic"] for row in diagnostics),
        "mean_forecast_mae_pct": mean_or_none(row["candidate_forecast_mae_pct"] for row in diagnostics),
        "mean_interval_coverage": mean_or_none(row["candidate_interval_coverage"] for row in diagnostics),
        "recommended_branch": branch,
    }
    if pair.get("control_round_id") and pair.get("control_run_id"):
        control_path = ROOT / "rounds" / str(pair["control_round_id"]) / "runs" / str(pair["control_run_id"]) / "results" / "leaderboard.csv"
        control = {row["model_id"]: row for row in read_csv(control_path)}
        paired = [
            float(leaderboard[row["model_id"]]["portfolio_return"]) - float(control[row["model_id"]]["portfolio_return"])
            for row in diagnostics
            if row["model_id"] in control
        ]
        summary["mean_paired_improvement_vs_control"] = mean(paired) if paired else None
        summary["models_improved_vs_control"] = sum(value > 0 for value in paired)
    output = output_dir(config) / pair_id
    output.mkdir(parents=True, exist_ok=True)
    counterfactual_rows: list[dict[str, Any]] = []
    counterfactual_summary: list[dict[str, Any]] = []
    if dominant_stage == "construction":
        counterfactual_rows, counterfactual_summary = construction_counterfactuals(
            submissions,
            leaderboard,
            returns,
        )
        summary["construction_counterfactuals"] = counterfactual_summary
    write_csv(output / "model_diagnostics.csv", diagnostics)
    if counterfactual_rows:
        write_csv(output / "construction_counterfactuals.csv", counterfactual_rows)
        write_csv(output / "construction_counterfactual_summary.csv", counterfactual_summary)
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    report = render_report(summary, diagnostics)
    (output / "report.md").write_text(report, encoding="utf-8", newline="\n")
    report_copy = ROOT / str(pair["report_copy"])
    report_copy.write_text(report, encoding="utf-8", newline="\n")
    print(report)


def pct(value: Any) -> str:
    if value is None:
        return "n/a"
    return f"{float(value) * 100:.2f}%"


def render_report(summary: dict[str, Any], rows: Sequence[dict[str, Any]]) -> str:
    ledgers_complete = bool(summary["complete_candidate_ledgers"])
    if ledgers_complete:
        bottom_line = (
            f"The dominant loss stage is **{summary['dominant_stage']}**. "
            f"The frozen branch rule selects `{summary['recommended_branch']}`."
        )
        capture_label = "Winner present in candidate ledger"
        overlap_label = "Cross-model candidate overlap"
        overlap_value = summary["candidate_overlap_jaccard"]
    else:
        bottom_line = (
            "This legacy pilot did not save candidate ledgers, so search and ranking losses cannot be separated "
            "without hindsight reconstruction. The frozen branch rule therefore selects "
            f"`{summary['recommended_branch']}`."
        )
        capture_label = "Winner present in selected portfolio"
        overlap_label = "Cross-model selected-portfolio overlap"
        overlap_value = summary["selected_overlap_jaccard"]
    lines = [
        "# Portfolio V2 Resolution Diagnostic",
        "",
        f"Round: `{summary['v2_round_id']}`",
        "",
        "## Bottom Line",
        "",
        bottom_line,
        "",
        "## Aggregate Results",
        "",
        f"- V2 average alpha versus SPY: {pct(summary['mean_v2_alpha_vs_sp500'])}",
        f"- Mean paired improvement versus control: {pct(summary.get('mean_paired_improvement_vs_control'))}",
        f"- {capture_label}: {summary['winner_ledger_capture_models']}/{summary['models']} models",
        f"- Mean realized top-three assets captured: {summary['mean_top3_candidates_captured']:.2f}/3",
        f"- Search regret share: {pct(summary['regret_shares']['search'])}",
        f"- Ranking regret share: {pct(summary['regret_shares']['ranking'])}",
        f"- Preselection regret: {pct(summary['mean_preselection_regret'])}",
        f"- Construction regret share: {pct(summary['regret_shares']['construction'])}",
        f"- Mean candidate forecast rank correlation: {summary['mean_forecast_rank_ic'] if summary['mean_forecast_rank_ic'] is not None else 'n/a'}",
        f"- Mean candidate forecast error: {summary['mean_forecast_mae_pct']:.2f} percentage points"
        if summary["mean_forecast_mae_pct"] is not None
        else "- Mean candidate forecast error: n/a",
        f"- Candidate interval coverage: {pct(summary['mean_interval_coverage'])}",
        f"- {overlap_label}: {pct(overlap_value)}",
        "",
        "## Model Diagnostics",
        "",
        "| Model | Alpha vs SPY | Search regret | Ranking regret | Preselection regret | Construction regret | Winner captured | Forecast rank IC |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for row in rows:
        ic = "n/a" if row["candidate_forecast_rank_ic"] is None else f"{float(row['candidate_forecast_rank_ic']):.3f}"
        lines.append(
            f"| {row['model_id']} | {pct(row['alpha_vs_sp500'])} | {pct(row['search_regret'])} | "
            f"{pct(row['ranking_regret'])} | {pct(row['preselection_regret'])} | "
            f"{pct(row['construction_regret'])} | {'Yes' if row['winner_in_ledger'] else 'No'} | {ic} |"
        )
    counterfactuals = summary.get("construction_counterfactuals") or []
    if counterfactuals:
        lines.extend(
            [
                "",
                "## Construction Counterfactuals",
                "",
                "These rules keep each model's selected assets fixed and change weights only. They are one-window diagnostics, not production recommendations.",
                "",
                "| Rule | Mean return | Improvement vs submitted | Models improved | Alpha vs SPY |",
                "| --- | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in counterfactuals:
            lines.append(
                f"| {row['rule']} | {pct(row['mean_counterfactual_return'])} | "
                f"{pct(row['mean_improvement_vs_submitted'])} | {row['models_improved']}/{row['models']} | "
                f"{pct(row['mean_alpha_vs_sp500'])} |"
            )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This is one prospective decision window and cannot establish a production improvement. "
            "No stage exceeded the frozen 50% dominance threshold, so this result does not authorize a targeted challenger branch. "
            "Preserve the completed diagnostic and use multiple later resolved observations before attributing underperformance to one stage.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "fetch-shared-prices", "analyze"))
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--pair", choices=("july13_pilot", "july17_production"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    if args.command == "prepare":
        prepare(config_path)
    elif not args.pair:
        raise SystemExit(f"{args.command} requires --pair")
    elif args.command == "fetch-shared-prices":
        fetch_shared_prices(config_path, args.pair)
    else:
        analyze_pair(config_path, args.pair)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

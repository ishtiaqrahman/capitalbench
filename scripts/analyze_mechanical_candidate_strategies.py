#!/usr/bin/env python3
"""Screen fixed, zero-API candidate strategies on resolved CapitalBench rounds."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any, Iterable, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.analyze_model_predictability import (  # noqa: E402
    RoundRecord,
    as_float,
    build_dataset,
    eligibility,
    percentile_ranks,
    selection_probabilities,
    spearman,
    write_csv,
)


DEFAULT_CONFIG = ROOT / "experiments" / "mechanical-candidate-screen-2026-07-21.yaml"
RETURN_FIELDS = ("return_7d", "return_30d", "return_6m", "return_1y")
QUALITY_FIELDS = (
    "volatility_30d",
    "max_drawdown_30d",
    "up_day_share_30d",
    "distance_from_52w_high",
    "distance_from_52w_low",
)


def load_config(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"invalid experiment config: {path}")
    return payload


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def active_assets(round_record: RoundRecord) -> list[dict[str, Any]]:
    return [row for row in round_record.assets if not row["is_cash"]]


def weighted_rank(
    asset: dict[str, Any],
    weights: dict[str, float],
    *,
    reverse: bool = False,
) -> float | None:
    values: list[tuple[float, float]] = []
    for field, weight in weights.items():
        value = as_float(asset.get(f"rank_{field}"))
        if value is None:
            return None
        values.append(((1.0 - value) if reverse else value, float(weight)))
    weight_sum = sum(weight for _value, weight in values)
    return sum(value * weight for value, weight in values) / weight_sum if weight_sum > 0.0 else None


def path_quality(asset: dict[str, Any]) -> float | None:
    ranks = {field: as_float(asset.get(f"rank_{field}")) for field in QUALITY_FIELDS}
    if any(value is None for value in ranks.values()):
        return None
    # Lower volatility is better; the remaining fields are ordered so higher
    # means a steadier or less damaged path.
    return mean(
        (
            1.0 - float(ranks["volatility_30d"]),
            float(ranks["max_drawdown_30d"]),
            float(ranks["up_day_share_30d"]),
            float(ranks["distance_from_52w_high"]),
            float(ranks["distance_from_52w_low"]),
        )
    )


def score_components(
    asset: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, float | None]:
    strategies = config["strategies"]
    continuation = weighted_rank(asset, strategies["continuation"]["weights"])
    reversal = weighted_rank(asset, strategies["reversal"]["weights"], reverse=True)
    quality = strategies["quality_pullback"]
    trend = weighted_rank(asset, quality["trend_weights"])
    pullback = weighted_rank(asset, quality["pullback_weights"], reverse=True)
    path = path_quality(asset)
    quality_pullback = None
    if trend is not None and pullback is not None and path is not None:
        component_weights = quality["component_weights"]
        quality_pullback = (
            trend * float(component_weights["established_trend"])
            + pullback * float(component_weights["recent_pullback"])
            + path * float(component_weights["path_quality"])
        )
    trend_pullback = None if trend is None or pullback is None else (trend + pullback) / 2.0
    return {
        "continuation": continuation,
        "reversal": reversal,
        "quality_pullback": quality_pullback,
        "trend_pullback": trend_pullback,
    }


def classify_regime(round_record: RoundRecord, config: dict[str, Any]) -> str:
    assets = active_assets(round_record)
    spy = next((row for row in assets if row.get("option_id") == "SP500"), None)
    if spy is None:
        return "unavailable"
    spy_return = as_float(spy.get("return_30d"))
    breadth_values = [
        as_float(row.get("return_30d"))
        for row in assets
        if row.get("option_id") != "SP500" and not row.get("is_benchmark")
    ]
    present = [value for value in breadth_values if value is not None]
    if spy_return is None or len(present) < max(3, math.ceil(len(breadth_values) * 0.9)):
        return "unavailable"
    breadth = sum(value > 0.0 for value in present) / len(present)
    threshold = float(config["strategies"]["regime_router"]["positive_breadth_threshold"])
    if spy_return >= 0.0 and breadth >= threshold:
        return "bullish"
    if spy_return < 0.0 and breadth < threshold:
        return "bearish"
    return "mixed"


def strategy_scores(
    round_record: RoundRecord,
    strategy: str,
    config: dict[str, Any],
) -> tuple[dict[str, float | None], str]:
    regime = classify_regime(round_record, config)
    scores: dict[str, float | None] = {}
    for asset in active_assets(round_record):
        components = score_components(asset, config)
        if strategy == "regime_router":
            route = {"bullish": "continuation", "bearish": "reversal", "mixed": "trend_pullback"}.get(regime)
            score = components.get(route) if route else None
        else:
            score = components[strategy]
        scores[str(asset["option_id"])] = score
    return scores, regime


def evaluate_strategy(
    round_record: RoundRecord,
    strategy: str,
    config: dict[str, Any],
) -> dict[str, Any] | None:
    assets = active_assets(round_record)
    scores, regime = strategy_scores(round_record, strategy, config)
    present = [
        (row, float(scores[str(row["option_id"])]))
        for row in assets
        if scores.get(str(row["option_id"])) is not None
    ]
    if len(present) < max(3, math.ceil(len(assets) * 0.9)):
        return None
    rows = [row for row, _score in present]
    score_values = [score for _row, score in present]
    returns = [float(row["future_return"]) for row in rows]
    top3_probabilities = selection_probabilities(score_values, 3)
    top5_probabilities = selection_probabilities(score_values, 5)
    top3_return = sum(probability * value for probability, value in zip(top3_probabilities, returns)) / 3.0
    top5_return = sum(probability * value for probability, value in zip(top5_probabilities, returns)) / 5.0
    ordered_outcomes = sorted(rows, key=lambda row: (-float(row["future_return"]), str(row["option_id"])))
    top2_ids = {str(row["option_id"]) for row in ordered_outcomes[:2]}
    winner_ids = set(round_record.winner_ids)
    deterministic_top5 = [
        str(row["option_id"])
        for row, _score in sorted(present, key=lambda item: (-item[1], str(item[0]["option_id"])))[:5]
    ]
    selected_returns = [
        float(row["future_return"])
        for row in rows
        if str(row["option_id"]) in set(deterministic_top5)
    ]
    winner_capture = max(
        (top5_probabilities[index] for index, row in enumerate(rows) if str(row["option_id"]) in winner_ids),
        default=0.0,
    )
    top2_capture = sum(
        top5_probabilities[index]
        for index, row in enumerate(rows)
        if str(row["option_id"]) in top2_ids
    )
    return {
        "round_id": round_record.round_id,
        "track": round_record.track,
        "decision_date": round_record.decision_date,
        "entry_date": round_record.entry_date,
        "exit_date": round_record.exit_date,
        "split": round_record.split,
        "prior_purged_rounds": round_record.prior_purged_rounds,
        "strategy": strategy,
        "regime": regime,
        "option_count": len(rows),
        "selected_option_ids": ";".join(deterministic_top5),
        "rank_ic": spearman(score_values, returns),
        "top3_return": top3_return,
        "top5_return": top5_return,
        "sp500_return": round_record.sp500_return,
        "top3_alpha_vs_sp500": top3_return - round_record.sp500_return,
        "top5_alpha_vs_sp500": top5_return - round_record.sp500_return,
        "top5_beats_sp500": top5_return > round_record.sp500_return,
        "winner_capture": winner_capture,
        "top2_capture_count": top2_capture,
        "oracle_regret": round_record.oracle_return - max(selected_returns),
    }


def maximal_non_overlapping(rounds: Sequence[RoundRecord]) -> set[str]:
    selected: set[str] = set()
    last_exit: date | None = None
    for item in sorted(rounds, key=lambda row: (row.entry_date, row.exit_date, row.round_id)):
        if last_exit is None or item.entry_date > last_exit:
            selected.add(item.round_id)
            last_exit = item.exit_date
    return selected


def mean_or_none(values: Iterable[float | None]) -> float | None:
    present = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return mean(present) if present else None


def percentile(values: Sequence[float], quantile: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * quantile
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] * (upper - position) + ordered[upper] * (position - lower)


def bootstrap_mean_ci(values: Sequence[float], seed: int) -> tuple[float | None, float | None]:
    if len(values) < 3:
        return None, None
    # A tiny local generator avoids a dependency and keeps reports reproducible.
    state = seed & 0x7FFFFFFF

    def draw_index(size: int) -> int:
        nonlocal state
        state = (1103515245 * state + 12345) & 0x7FFFFFFF
        return state % size

    samples = [mean(values[draw_index(len(values))] for _ in values) for _ in range(2000)]
    return percentile(samples, 0.025), percentile(samples, 0.975)


def aggregate_rows(
    metrics: Sequence[dict[str, Any]],
    rounds: Sequence[RoundRecord],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    round_index = {row.round_id: row for row in rounds}
    non_overlap = {
        track: maximal_non_overlapping([row for row in rounds if row.track == track])
        for track in ("weekly", "monthly")
    }
    scopes = {
        "all": lambda row: True,
        "discovery": lambda row: row["split"] == "discovery",
        "holdout": lambda row: row["split"] == "holdout",
        "purged_walk_forward": lambda row: int(row["prior_purged_rounds"]) >= int(config["minimum_prior_purged_rounds"]),
        "non_overlapping": lambda row: row["round_id"] in non_overlap[row["track"]],
        "non_overlapping_discovery": lambda row: (
            row["round_id"] in non_overlap[row["track"]] and row["split"] == "discovery"
        ),
        "non_overlapping_holdout": lambda row: (
            row["round_id"] in non_overlap[row["track"]] and row["split"] == "holdout"
        ),
    }
    output: list[dict[str, Any]] = []
    for track in ("weekly", "monthly"):
        for strategy in config["strategies"]:
            strategy_rows = [row for row in metrics if row["track"] == track and row["strategy"] == strategy]
            for scope, include in scopes.items():
                subset = [row for row in strategy_rows if include(row)]
                alpha = [float(row["top5_alpha_vs_sp500"]) for row in subset]
                losses = [-value for value in alpha if value < 0.0]
                low, high = bootstrap_mean_ci(alpha, seed=sum(ord(char) for char in f"{track}:{strategy}:{scope}"))
                output.append(
                    {
                        "track": track,
                        "strategy": strategy,
                        "scope": scope,
                        "rounds": len(subset),
                        "mean_top5_return": mean_or_none(row["top5_return"] for row in subset),
                        "mean_sp500_return": mean_or_none(row["sp500_return"] for row in subset),
                        "mean_top5_alpha": mean_or_none(alpha),
                        "median_top5_alpha": median(alpha) if alpha else None,
                        "alpha_ci_low": low,
                        "alpha_ci_high": high,
                        "sp500_beat_rate": mean_or_none(float(row["top5_beats_sp500"]) for row in subset),
                        "mean_top3_alpha": mean_or_none(row["top3_alpha_vs_sp500"] for row in subset),
                        "mean_rank_ic": mean_or_none(row["rank_ic"] for row in subset),
                        "winner_capture_rate": mean_or_none(row["winner_capture"] for row in subset),
                        "mean_top2_capture_count": mean_or_none(row["top2_capture_count"] for row in subset),
                        "mean_oracle_regret": mean_or_none(row["oracle_regret"] for row in subset),
                        "mean_underperformance_when_losing": mean(losses) if losses else 0.0 if subset else None,
                        "first_entry": min((round_index[row["round_id"]].entry_date for row in subset), default=None),
                        "last_exit": max((round_index[row["round_id"]].exit_date for row in subset), default=None),
                    }
                )
    return output


def advancement_rows(aggregates: Sequence[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    index = {(row["track"], row["strategy"], row["scope"]): row for row in aggregates}
    output: list[dict[str, Any]] = []
    for track in ("weekly", "monthly"):
        for strategy in config["strategies"]:
            primary = index[(track, strategy, "non_overlapping")]
            discovery = index[(track, strategy, "non_overlapping_discovery")]
            holdout = index[(track, strategy, "non_overlapping_holdout")]
            reasons: list[str] = []
            if int(primary["rounds"]) < int(config["minimum_non_overlapping_rounds"]):
                reasons.append("insufficient_non_overlapping_rounds")
            if primary["mean_top5_alpha"] is None or float(primary["mean_top5_alpha"]) < float(config["minimum_mean_top5_alpha"]):
                reasons.append("alpha_below_threshold")
            if primary["sp500_beat_rate"] is None or float(primary["sp500_beat_rate"]) < float(config["minimum_sp500_beat_rate"]):
                reasons.append("beat_rate_below_threshold")
            if discovery["mean_top5_alpha"] is None or float(discovery["mean_top5_alpha"]) <= 0.0:
                reasons.append("discovery_alpha_not_positive")
            if holdout["mean_top5_alpha"] is None or float(holdout["mean_top5_alpha"]) <= 0.0:
                reasons.append("holdout_alpha_not_positive")
            output.append(
                {
                    "track": track,
                    "strategy": strategy,
                    "eligible_for_model_shadow": not reasons,
                    "non_overlapping_rounds": primary["rounds"],
                    "non_overlapping_mean_alpha": primary["mean_top5_alpha"],
                    "non_overlapping_beat_rate": primary["sp500_beat_rate"],
                    "discovery_mean_alpha": discovery["mean_top5_alpha"],
                    "holdout_mean_alpha": holdout["mean_top5_alpha"],
                    "reasons": ";".join(reasons) if reasons else "passed",
                }
            )
    return output


def source_paths(round_dir: Path, run_path: Path) -> list[Path]:
    return [
        round_dir / "manifest.yaml",
        round_dir / "options.yaml",
        round_dir / "market_data" / "universe_trailing_returns.csv",
        run_path / "run_manifest.yaml",
        run_path / "results" / "returns.csv",
    ]


def prepare(config_path: Path) -> None:
    config = load_config(config_path)
    rounds_dir = ROOT / str(config["rounds_dir"])
    frozen_sources: list[dict[str, Any]] = []
    for round_dir in sorted(path for path in rounds_dir.glob("CB-*") if path.is_dir()):
        run, _row = eligibility(round_dir)
        if run is None:
            continue
        for path in source_paths(round_dir, run.path):
            frozen_sources.append(
                {
                    "round_id": round_dir.name,
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
        "eligible_rounds": len({row["round_id"] for row in frozen_sources}),
        "sources": frozen_sources,
    }
    output = output_dir(config)
    output.mkdir(parents=True, exist_ok=True)
    (output / "freeze_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"frozen_rounds={manifest['eligible_rounds']}")
    print(f"frozen_sources={len(frozen_sources)}")


def verify_freeze(config_path: Path, config: dict[str, Any]) -> dict[str, Any]:
    manifest_path = output_dir(config) / "freeze_manifest.json"
    if not manifest_path.exists():
        raise RuntimeError("run prepare before analyze")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["config_sha256"] != sha256_file(config_path):
        raise RuntimeError("experiment config changed after freeze")
    for row in manifest["sources"]:
        path = ROOT / row["path"]
        if not path.exists() or sha256_file(path) != row["sha256"]:
            raise RuntimeError(f"frozen source changed: {path}")
    return manifest


def pct(value: Any) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.2f}%"


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return "\n".join(lines)


def build_report(
    rounds: Sequence[RoundRecord],
    metrics: Sequence[dict[str, Any]],
    aggregates: Sequence[dict[str, Any]],
    decisions: Sequence[dict[str, Any]],
    config: dict[str, Any],
) -> str:
    passed = [row for row in decisions if row["eligible_for_model_shadow"]]
    if passed:
        names = ", ".join(f"{row['track']} {row['strategy']}" for row in passed)
        bottom_line = f"{names} passed the development gate and may proceed only to a prospective paid model shadow."
    else:
        bottom_line = "No mechanical candidate strategy passed the frozen development gate. No paid model-shadow experiment is justified by this screen."
    decision_table = []
    for row in decisions:
        decision_table.append(
            [
                row["track"],
                row["strategy"],
                row["non_overlapping_rounds"],
                pct(row["non_overlapping_mean_alpha"]),
                pct(row["non_overlapping_beat_rate"]),
                pct(row["discovery_mean_alpha"]),
                pct(row["holdout_mean_alpha"]),
                "Pass" if row["eligible_for_model_shadow"] else "Fail",
            ]
        )
    aggregate_index = {(row["track"], row["strategy"], row["scope"]): row for row in aggregates}
    diagnostic_tables: list[str] = []
    for track in ("weekly", "monthly"):
        rows = []
        for strategy in config["strategies"]:
            all_row = aggregate_index[(track, strategy, "all")]
            purged = aggregate_index[(track, strategy, "purged_walk_forward")]
            rows.append(
                [
                    strategy,
                    all_row["rounds"],
                    pct(all_row["mean_top5_alpha"]),
                    pct(all_row["sp500_beat_rate"]),
                    pct(all_row["mean_top3_alpha"]),
                    pct(all_row["winner_capture_rate"]),
                    purged["rounds"],
                    pct(purged["mean_top5_alpha"]),
                ]
            )
        diagnostic_tables.extend(
            [
                f"## {track.title()} Diagnostics",
                "",
                markdown_table(
                    ["Strategy", "Rounds", "Top-5 alpha", "Beat S&P", "Top-3 alpha", "Winner in top 5", "Mature purged", "Purged alpha"],
                    rows,
                ),
                "",
            ]
        )
    quality_weekly = aggregate_index[("weekly", "quality_pullback", "all")]
    quality_monthly = aggregate_index[("monthly", "quality_pullback", "all")]
    return "\n".join(
        [
            "# Mechanical Candidate Strategy Screen",
            "",
            f"Generated at: `{datetime.now(timezone.utc).replace(microsecond=0).isoformat()}`",
            "",
            "## Bottom Line",
            "",
            bottom_line,
            "",
            "## Advancement Decision",
            "",
            markdown_table(
                ["Track", "Strategy", "Non-overlap N", "Non-overlap alpha", "Beat S&P", "Discovery alpha", "Holdout alpha", "Gate"],
                decision_table,
            ),
            "",
            *diagnostic_tables,
            "## Coverage And Interpretation",
            "",
            f"- Eligible resolved V1 rounds: {len(rounds)} ({sum(row.track == 'weekly' for row in rounds)} weekly, {sum(row.track == 'monthly' for row in rounds)} monthly).",
            f"- Quality-pullback coverage: {quality_weekly['rounds']} weekly rounds and {quality_monthly['rounds']} monthly rounds.",
            "- Daily-start rounds overlap. The advancement gate uses the deterministic non-overlapping sequence; all-round figures are correlated diagnostics.",
            "- These hypotheses were selected after earlier CapitalBench analysis and therefore remain development evidence even if a gate passes.",
            "- Exact winner capture is not the adoption target. The decision target is broad, repeatable top-five alpha versus S&P 500.",
            "",
            "## Next Action",
            "",
            (
                "Freeze the passing strategy as a candidate-evidence layer and run one additional single-turn weekly challenger call per model alongside unchanged V2.0."
                if passed
                else "Do not buy another prompt replay or V2 challenger call from these four hypotheses. Continue unchanged official V2.0 rounds and wait for additional non-overlapping data before defining a materially different feature hypothesis."
            ),
            "",
            "## Reproducibility",
            "",
            "```bash",
            "python scripts/analyze_mechanical_candidate_strategies.py prepare",
            "python scripts/analyze_mechanical_candidate_strategies.py analyze",
            "```",
            "",
        ]
    )


def analyze(config_path: Path) -> None:
    config = load_config(config_path)
    verify_freeze(config_path, config)
    rounds, asset_rows, _model_rows, _winner_traces, eligibility_rows, round_summaries = build_dataset(
        ROOT / str(config["rounds_dir"])
    )
    metrics: list[dict[str, Any]] = []
    for round_record in rounds:
        for strategy in config["strategies"]:
            row = evaluate_strategy(round_record, strategy, config)
            if row is not None:
                metrics.append(row)
    aggregates = aggregate_rows(metrics, rounds, config)
    decisions = advancement_rows(aggregates, config)
    output = output_dir(config)
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "eligibility.csv", eligibility_rows)
    write_csv(output / "round_summary.csv", round_summaries)
    write_csv(output / "strategy_round_metrics.csv", metrics)
    write_csv(output / "strategy_metrics.csv", aggregates)
    write_csv(output / "advancement_decisions.csv", decisions)
    report = build_report(rounds, metrics, aggregates, decisions, config)
    (output / "report.md").write_text(report, encoding="utf-8", newline="\n")
    report_copy = ROOT / str(config["report_copy"])
    report_copy.write_text(report, encoding="utf-8", newline="\n")
    summary = {
        "experiment_id": config["experiment_id"],
        "eligible_rounds": len(rounds),
        "strategy_round_cells": len(metrics),
        "passing_strategies": [
            {"track": row["track"], "strategy": row["strategy"]}
            for row in decisions
            if row["eligible_for_model_shadow"]
        ],
        "official_artifacts_changed": False,
        "model_api_calls": 0,
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(report)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "analyze"))
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    if args.command == "prepare":
        prepare(config_path)
    else:
        analyze(config_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

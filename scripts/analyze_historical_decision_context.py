#!/usr/bin/env python3
"""Backfill V2-style price features and screen frozen mechanical rules."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import statistics
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

import yaml


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from capitalbench.decision_context import (  # noqa: E402
    _aligned_return_pairs,
    _annualized_volatility,
    _beta,
    _default_history_fetcher,
    _max_drawdown,
    _parse_history,
    _prior_session_return,
    _returns_by_date,
    _session_return,
    _volume_zscore,
)


DEFAULT_CONFIG = ROOT / "experiments" / "historical-decision-context-backfill-2026-07-21.yaml"
CANONICAL_REPORT = ROOT / "docs" / "historical_decision_context_backfill_report.md"
CANONICAL_SUMMARY = ROOT / "research" / "results" / "historical-decision-context-backfill-2026-07-21.json"


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
            clean = {
                key: (f"{value:.10f}" if isinstance(value, float) and math.isfinite(value) else value)
                for key, value in row.items()
            }
            writer.writerow(clean)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def as_float(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def percentile_ranks(values: Sequence[float | None]) -> list[float | None]:
    indexed = [(index, value) for index, value in enumerate(values) if value is not None]
    output: list[float | None] = [None] * len(values)
    if not indexed:
        return output
    ordered = sorted(indexed, key=lambda item: float(item[1]))
    denominator = max(len(ordered) - 1, 1)
    cursor = 0
    while cursor < len(ordered):
        end = cursor + 1
        while end < len(ordered) and ordered[end][1] == ordered[cursor][1]:
            end += 1
        rank = ((cursor + end - 1) / 2.0) / denominator if len(ordered) > 1 else 0.5
        for original_index, _value in ordered[cursor:end]:
            output[original_index] = rank
        cursor = end
    return output


def selection_probabilities(scores: Sequence[float], count: int) -> list[float]:
    """Return fractional membership probabilities when a tie crosses the cutoff."""
    if count <= 0 or not scores:
        return [0.0] * len(scores)
    count = min(count, len(scores))
    threshold = sorted(scores, reverse=True)[count - 1]
    above = sum(score > threshold for score in scores)
    tied = sum(score == threshold for score in scores)
    tie_probability = (count - above) / tied
    return [1.0 if score > threshold else tie_probability if score == threshold else 0.0 for score in scores]


def output_dir(config: dict[str, Any]) -> Path:
    return ROOT / str(config["output_dir"])


def history_path(config: dict[str, Any], symbol: str) -> Path:
    return output_dir(config) / "price_history" / f"{symbol}.json"


def fetch_histories(config: dict[str, Any]) -> dict[str, Any]:
    assets = read_csv(ROOT / str(config["input_dataset"]))
    symbols = sorted({row["symbol"] for row in assets if row.get("symbol") and row["symbol"] != "CASH"})
    start = date.fromisoformat(str(config["price_source"]["history_start"]))
    end = date.fromisoformat(str(config["price_source"]["history_end"]))
    manifest: dict[str, Any] = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "requested_symbols": len(symbols),
        "history_start": start.isoformat(),
        "history_end": end.isoformat(),
        "symbols": {},
    }
    for index, symbol in enumerate(symbols, start=1):
        path = history_path(config, symbol)
        if path.exists():
            cached = json.loads(path.read_text(encoding="utf-8"))
            manifest["symbols"][symbol] = {
                "status": "cached",
                "source": cached.get("source", "unknown"),
                "rows": len(cached.get("history") or []),
            }
            continue
        error = ""
        for attempt in range(3):
            try:
                raw, source = _default_history_fetcher(symbol, start, end)
                history = _parse_history(raw, end)
                if not history:
                    raise ValueError("empty history")
                payload = {
                    "symbol": symbol,
                    "source": source,
                    "requested_start": start.isoformat(),
                    "requested_end": end.isoformat(),
                    "history": history,
                }
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                manifest["symbols"][symbol] = {"status": "fetched", "source": source, "rows": len(history)}
                error = ""
                break
            except Exception as exc:  # pragma: no cover - network failures vary
                error = f"{type(exc).__name__}: {exc}"
                time.sleep(1.5 * (attempt + 1))
        if error:
            manifest["symbols"][symbol] = {"status": "failed", "error": error, "rows": 0}
        print(f"[{index}/{len(symbols)}] {symbol}: {manifest['symbols'][symbol]['status']}", flush=True)
        time.sleep(0.05)
    path = output_dir(config) / "price_fetch_manifest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def load_histories(config: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    histories: dict[str, list[dict[str, Any]]] = {}
    directory = output_dir(config) / "price_history"
    for path in sorted(directory.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        histories[str(payload["symbol"])] = list(payload.get("history") or [])
    return histories


def feature_row(
    asset: dict[str, str],
    history: list[dict[str, Any]],
    spy_history: list[dict[str, Any]],
    config: dict[str, Any],
) -> dict[str, Any] | None:
    entry = date.fromisoformat(asset["entry_date"])
    track = asset["track"]
    settings = config["weekly_metrics" if track == "weekly" else "monthly_metrics"]
    sliced = [row for row in history if str(row["date"]) <= entry.isoformat()]
    spy_sliced = [row for row in spy_history if str(row["date"]) <= entry.isoformat()]
    prices = [float(row["adj_close"]) for row in sliced]
    recent = int(settings["recent_sessions"])
    prior = int(settings["prior_sessions"])
    vol_sessions = int(settings["volatility_sessions"])
    corr_sessions = int(settings["correlation_sessions"])
    recent_return = as_float(_session_return(prices, recent))
    prior_return = as_float(_prior_session_return(prices, recent=recent, prior=prior))
    spy_prices = [float(row["adj_close"]) for row in spy_sliced]
    spy_recent = as_float(_session_return(spy_prices, recent))
    spy_prior = as_float(_prior_session_return(spy_prices, recent=recent, prior=prior))
    volatility = as_float(_annualized_volatility(prices[-(vol_sessions + 1) :]))
    drawdown = as_float(_max_drawdown(prices[-(vol_sessions + 1) :]))
    volume = as_float(
        _volume_zscore(
            sliced,
            recent=int(settings["volume_recent_sessions"]),
            baseline=int(settings["volume_baseline_sessions"]),
        )
    )
    pairs = _aligned_return_pairs(_returns_by_date(sliced), _returns_by_date(spy_sliced), corr_sessions)
    beta = as_float(_beta(pairs))
    values = (recent_return, prior_return, spy_recent, spy_prior, volatility, drawdown, volume, beta)
    if any(value is None for value in values):
        return None
    return {
        "round_id": asset["round_id"],
        "track": track,
        "split": asset["split"],
        "entry_date": asset["entry_date"],
        "exit_date": asset["exit_date"],
        "option_id": asset["option_id"],
        "symbol": asset["symbol"],
        "future_return": float(asset["future_return"]),
        "recent_active_return": float(recent_return) - float(spy_recent),
        "prior_active_return": float(prior_return) - float(spy_prior),
        "volatility": float(volatility),
        "max_drawdown": float(drawdown),
        "volume_zscore": float(volume),
        "beta_spy": float(beta),
    }


def add_ranks(rows: list[dict[str, Any]]) -> None:
    fields = ("recent_active_return", "prior_active_return", "volatility", "max_drawdown", "volume_zscore", "beta_spy")
    for field in fields:
        ranks = percentile_ranks([as_float(row[field]) for row in rows])
        for row, rank in zip(rows, ranks):
            row[f"rank_{field}"] = rank
    for row in rows:
        row["rank_low_volatility"] = 1.0 - float(row["rank_volatility"])
        row["rank_shallow_drawdown"] = float(row["rank_max_drawdown"])
        row["rank_recent_active_reversal"] = 1.0 - float(row["rank_recent_active_return"])
        row["rank_low_beta"] = 1.0 - float(row["rank_beta_spy"])


COMPONENT_FIELD = {
    "recent_active_rank": "rank_recent_active_return",
    "prior_active_rank": "rank_prior_active_return",
    "low_volatility_rank": "rank_low_volatility",
    "shallow_drawdown_rank": "rank_shallow_drawdown",
    "recent_active_reversal_rank": "rank_recent_active_reversal",
    "volume_rank": "rank_volume_zscore",
    "low_beta_rank": "rank_low_beta",
}


def signal_score(row: dict[str, Any], weights: dict[str, float]) -> float:
    return sum(float(row[COMPONENT_FIELD[name]]) * float(weight) for name, weight in weights.items())


def build_feature_panel(config: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    assets = read_csv(ROOT / str(config["input_dataset"]))
    rounds = {row["round_id"]: row for row in read_csv(ROOT / str(config["round_dataset"]))}
    histories = load_histories(config)
    by_round: dict[str, list[dict[str, str]]] = defaultdict(list)
    for asset in assets:
        if asset.get("is_cash") == "True" or asset.get("symbol") == "CASH":
            continue
        metadata = rounds[asset["round_id"]]
        merged = dict(asset)
        merged.update({key: metadata[key] for key in ("entry_date", "exit_date", "split")})
        by_round[asset["round_id"]].append(merged)

    feature_rows: list[dict[str, Any]] = []
    coverage_rows: list[dict[str, Any]] = []
    minimum_share = float(config["coverage"]["minimum_asset_share_per_round"])
    for round_id, round_assets in sorted(by_round.items()):
        spy_asset = next((row for row in round_assets if row["option_id"] == "SP500"), None)
        spy_history = histories.get(spy_asset["symbol"], []) if spy_asset else []
        computed: list[dict[str, Any]] = []
        for asset in round_assets:
            history = histories.get(asset["symbol"], [])
            row = feature_row(asset, history, spy_history, config) if history and spy_history else None
            if row is not None:
                computed.append(row)
        share = len(computed) / len(round_assets) if round_assets else 0.0
        eligible = share >= minimum_share and any(row["option_id"] == "SP500" for row in computed)
        coverage_rows.append(
            {
                "round_id": round_id,
                "track": round_assets[0]["track"],
                "assets_available": len(computed),
                "assets_total": len(round_assets),
                "coverage": share,
                "eligible": eligible,
            }
        )
        if eligible:
            add_ranks(computed)
            feature_rows.extend(computed)
    return feature_rows, coverage_rows


def evaluate_round(rows: list[dict[str, Any]], signal: str, weights: dict[str, float], count: int) -> dict[str, Any]:
    scores = [signal_score(row, weights) for row in rows]
    probabilities = selection_probabilities(scores, count)
    portfolio_return = sum(probability * float(row["future_return"]) for probability, row in zip(probabilities, rows)) / count
    spy = next(row for row in rows if row["option_id"] == "SP500")
    spy_return = float(spy["future_return"])
    ordered = sorted(rows, key=lambda row: float(row["future_return"]), reverse=True)
    top3_ids = {row["option_id"] for row in ordered[:3]}
    top3_capture = sum(probability for probability, row in zip(probabilities, rows) if row["option_id"] in top3_ids)
    return {
        "round_id": rows[0]["round_id"],
        "track": rows[0]["track"],
        "split": rows[0]["split"],
        "entry_date": rows[0]["entry_date"],
        "exit_date": rows[0]["exit_date"],
        "signal": signal,
        "portfolio_return": portfolio_return,
        "spy_return": spy_return,
        "alpha": portfolio_return - spy_return,
        "beat_spy": portfolio_return > spy_return,
        "oracle_return": float(ordered[0]["future_return"]),
        "shortlist_regret": float(ordered[0]["future_return"]) - portfolio_return,
        "top3_capture": top3_capture,
        "selected": ",".join(
            row["option_id"] for probability, row in sorted(zip(probabilities, rows), key=lambda item: (-item[0], item[1]["option_id"])) if probability > 0
        ),
    }


def nonoverlap(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    last_exit: date | None = None
    for row in sorted(rows, key=lambda item: (item["entry_date"], item["round_id"])):
        entry = date.fromisoformat(row["entry_date"])
        if last_exit is None or entry >= last_exit:
            selected.append(row)
            last_exit = date.fromisoformat(row["exit_date"])
    return selected


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {"rounds": 0, "mean_alpha": None, "beat_rate": None, "mean_regret": None, "top3_capture": None}
    alphas = [float(row["alpha"]) for row in rows]
    without_best = alphas.copy()
    without_best.remove(max(without_best))
    return {
        "rounds": len(rows),
        "mean_alpha": statistics.mean(alphas),
        "beat_rate": sum(bool(row["beat_spy"]) for row in rows) / len(rows),
        "mean_regret": statistics.mean(float(row["shortlist_regret"]) for row in rows),
        "top3_capture": statistics.mean(float(row["top3_capture"]) for row in rows),
        "leave_best_out_alpha": statistics.mean(without_best) if without_best else alphas[0],
    }


def evaluate(config: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    features, coverage = build_feature_panel(config)
    by_round: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in features:
        by_round[row["round_id"]].append(row)
    metrics: list[dict[str, Any]] = []
    count = int(config["selection"]["assets"])
    for round_rows in by_round.values():
        for signal, weights in config["signals"].items():
            metrics.append(evaluate_round(round_rows, signal, weights, count))

    coverage_by_track: dict[str, dict[str, Any]] = {}
    for track in ("weekly", "monthly"):
        rows = [row for row in coverage if row["track"] == track]
        coverage_by_track[track] = {
            "eligible_rounds": sum(bool(row["eligible"]) for row in rows),
            "total_rounds": len(rows),
            "round_coverage": sum(bool(row["eligible"]) for row in rows) / len(rows) if rows else 0.0,
        }

    results: list[dict[str, Any]] = []
    gate = config["gate"]
    for track in ("weekly", "monthly"):
        for signal in config["signals"]:
            subset = [row for row in metrics if row["track"] == track and row["signal"] == signal]
            discovery = [row for row in subset if row["split"] == "discovery"]
            holdout = [row for row in subset if row["split"] == "holdout"]
            independent = nonoverlap(subset)
            overall_stats = aggregate(subset)
            discovery_stats = aggregate(discovery)
            holdout_stats = aggregate(holdout)
            nonoverlap_stats = aggregate(independent)
            passes = (
                track == gate["eligible_track"]
                and coverage_by_track[track]["round_coverage"] >= float(gate["minimum_feature_coverage"])
                and nonoverlap_stats["rounds"] >= int(gate["minimum_nonoverlap_rounds"])
                and float(nonoverlap_stats["mean_alpha"] or -1) > float(gate["minimum_nonoverlap_alpha"])
                and float(nonoverlap_stats["beat_rate"] or 0) > float(gate["minimum_nonoverlap_beat_rate"])
                and float(discovery_stats["mean_alpha"] or -1) > float(gate["minimum_discovery_alpha"])
                and float(holdout_stats["mean_alpha"] or -1) > float(gate["minimum_holdout_alpha"])
                and float(overall_stats["leave_best_out_alpha"] or -1) > float(gate["minimum_leave_best_out_alpha"])
            )
            results.append(
                {
                    "track": track,
                    "signal": signal,
                    "passes_gate": passes,
                    "coverage": coverage_by_track[track],
                    "overall": overall_stats,
                    "discovery": discovery_stats,
                    "holdout": holdout_stats,
                    "nonoverlap": nonoverlap_stats,
                    "nonoverlap_round_ids": [row["round_id"] for row in independent],
                }
            )
    summary = {
        "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "decision": "accepted_for_shadow" if any(row["passes_gate"] for row in results) else "rejected",
        "passing_signals": [f"{row['track']}:{row['signal']}" for row in results if row["passes_gate"]],
        "coverage": coverage_by_track,
        "results": results,
        "official_score_eligible": False,
        "production_impact": "none",
        "config_sha256": sha256_file(DEFAULT_CONFIG),
    }
    write_csv(output_dir(config) / "feature_panel.csv", features)
    write_csv(output_dir(config) / "coverage.csv", coverage)
    write_csv(output_dir(config) / "round_metrics.csv", metrics)
    output_dir(config).mkdir(parents=True, exist_ok=True)
    (output_dir(config) / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return metrics, summary


def pct(value: Any) -> str:
    parsed = as_float(value)
    return "n/a" if parsed is None else f"{parsed * 100:.2f}%"


def render_report(summary: dict[str, Any], fetch_manifest: dict[str, Any]) -> str:
    source_counts: dict[str, int] = defaultdict(int)
    failures: list[str] = []
    for symbol, row in fetch_manifest.get("symbols", {}).items():
        if row.get("status") == "failed":
            failures.append(symbol)
        else:
            source_counts[str(row.get("source") or "unknown")] += 1
    lines = [
        "# Historical Decision-Context Backfill Results",
        "",
        f"Decision: **{summary['decision']}**",
        "",
        "## Data Coverage",
        "",
        f"- Price sources: {', '.join(f'{name} ({count})' for name, count in sorted(source_counts.items())) or 'none'}",
        f"- Failed symbols: {', '.join(failures) if failures else 'none'}",
        f"- Weekly eligible rounds: {summary['coverage']['weekly']['eligible_rounds']}/{summary['coverage']['weekly']['total_rounds']}",
        f"- Monthly eligible rounds: {summary['coverage']['monthly']['eligible_rounds']}/{summary['coverage']['monthly']['total_rounds']}",
        "",
        "## Frozen Signal Results",
        "",
        "| Track | Signal | All alpha | Discovery | Holdout | Non-overlap alpha | Non-overlap beat | All leave-best-out | Non-overlap leave-best-out | Gate |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in summary["results"]:
        lines.append(
            "| {track} | {signal} | {all_alpha} | {discovery} | {holdout} | {independent} ({rounds}) | {beat} | {leave_best} | {independent_leave_best} | {gate} |".format(
                track=row["track"],
                signal=row["signal"].replace("_", " "),
                all_alpha=pct(row["overall"]["mean_alpha"]),
                discovery=pct(row["discovery"]["mean_alpha"]),
                holdout=pct(row["holdout"]["mean_alpha"]),
                independent=pct(row["nonoverlap"]["mean_alpha"]),
                rounds=row["nonoverlap"]["rounds"],
                beat=pct(row["nonoverlap"]["beat_rate"]),
                leave_best=pct(row["overall"]["leave_best_out_alpha"]),
                independent_leave_best=pct(row["nonoverlap"]["leave_best_out_alpha"]),
                gate="pass" if row["passes_gate"] else "fail",
            )
        )
    best_weekly = max(
        (row for row in summary["results"] if row["track"] == "weekly"),
        key=lambda row: float(row["nonoverlap"]["mean_alpha"] or -999),
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            f"The strongest weekly non-overlapping result was `{best_weekly['signal']}` at {pct(best_weekly['nonoverlap']['mean_alpha'])} alpha across {best_weekly['nonoverlap']['rounds']} rounds. "
            + ("It cleared every frozen gate." if best_weekly["passes_gate"] else "It did not clear every frozen gate."),
            f"Its non-overlapping alpha falls to {pct(best_weekly['nonoverlap']['leave_best_out_alpha'])} when the best week is removed, so the result should be treated as fragile even though it passed the predeclared gate.",
            "",
            "This is reused historical data. A pass can authorize only a prospective private shadow; it cannot change Portfolio V2.0 or official scores.",
            "",
        ]
    )
    return "\n".join(lines)


def score(config: dict[str, Any]) -> dict[str, Any]:
    _metrics, summary = evaluate(config)
    fetch_manifest_path = output_dir(config) / "price_fetch_manifest.json"
    fetch_manifest = json.loads(fetch_manifest_path.read_text(encoding="utf-8"))
    report = render_report(summary, fetch_manifest)
    (output_dir(config) / "report.md").write_text(report, encoding="utf-8")
    CANONICAL_REPORT.write_text(report, encoding="utf-8")
    CANONICAL_SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    CANONICAL_SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("fetch", "score", "all"))
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()
    config = load_yaml(args.config)
    if args.command in {"fetch", "all"}:
        fetch_histories(config)
    if args.command in {"score", "all"}:
        summary = score(config)
        print(json.dumps({"decision": summary["decision"], "passing_signals": summary["passing_signals"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

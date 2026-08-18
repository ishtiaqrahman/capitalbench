from __future__ import annotations

import csv
import math
import os
import statistics
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

from .exposures import economic_exposure_cluster
from .io import load_manifest, load_options, write_json
from .methodology import is_production_portfolio, uses_quality_evidence
from .performance import _fetch_yahoo_chart_adjclose
from .scoring import _is_cash_option
from .universe import TIINGO_API_KEY_ENV, fetch_tiingo_eod_prices

DECISION_CONTEXT_CSV = "universe_decision_context.csv"
DECISION_CONTEXT_JSON = "universe_decision_context.json"
DECISION_CONTEXT_MD = "universe_decision_context.md"
DECISION_CONTEXT_HISTORY_JSON = "decision_context_source_history.json"
DECISION_CONTEXT_TITLE = "Full-Universe Horizon-Specific Decision Context"
QUALITY_EVIDENCE_JSON = "universe_quality_evidence.json"
QUALITY_EVIDENCE_MD = "universe_quality_evidence.md"
QUALITY_EVIDENCE_TITLE = "Complete Option-Level Quality Evidence"
QUALITY_EVIDENCE_MINIMUM_COVERAGE = 0.90
QUALITY_EVIDENCE_WEIGHTS = {
    "prior_active_rank": 0.45,
    "recent_active_reversal_rank": 0.30,
    "low_volatility_rank": 0.15,
    "shallow_drawdown_rank": 0.10,
}

HistoryFetcher = Callable[[str, date, date], tuple[list[dict[str, Any]], str]]


@dataclass(frozen=True)
class DecisionContextOutput:
    csv_path: Path
    json_path: Path
    markdown_path: Path
    history_path: Path
    profile: str
    total_options: int
    failed_options: list[str]
    quality_json_path: Path | None = None
    quality_markdown_path: Path | None = None


def fetch_universe_decision_context(
    *,
    round_path: Path,
    as_of_date: str,
    overwrite: bool = False,
    fetcher: HistoryFetcher | None = None,
) -> DecisionContextOutput:
    manifest = load_manifest(round_path)
    profile = _profile_for_manifest(manifest)
    compact = is_production_portfolio(manifest.methodology_version)
    market_data_dir = round_path / "market_data"
    market_data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = market_data_dir / DECISION_CONTEXT_CSV
    json_path = market_data_dir / DECISION_CONTEXT_JSON
    markdown_path = market_data_dir / DECISION_CONTEXT_MD
    history_path = market_data_dir / DECISION_CONTEXT_HISTORY_JSON
    quality_json_path = market_data_dir / QUALITY_EVIDENCE_JSON
    quality_markdown_path = market_data_dir / QUALITY_EVIDENCE_MD
    include_quality_evidence = uses_quality_evidence(manifest.methodology_version)
    output_paths = [csv_path, json_path, markdown_path, history_path]
    if include_quality_evidence:
        output_paths.extend([quality_json_path, quality_markdown_path])
    if not overwrite:
        existing = [str(path) for path in output_paths if path.exists()]
        if existing:
            raise FileExistsError(
                "decision-context files already exist; pass --overwrite-decision-context: "
                + ", ".join(existing)
            )

    as_of = datetime.strptime(as_of_date, "%Y-%m-%d").date()
    fetch_start = as_of - timedelta(days=430)
    selected_fetcher = fetcher or _default_history_fetcher
    options = [option for option in load_options(round_path) if option.include_in_universe]
    internal_rows: list[dict[str, Any]] = []
    source_rows: list[dict[str, Any]] = []
    sources: set[str] = set()
    failed_options: list[str] = []

    for option in options:
        if _is_cash_option(option):
            internal_rows.append(_cash_row(option, as_of, profile, compact=compact))
            source_rows.append({"option_id": option.option_id, "symbol": "", "source": "cash", "rows": []})
            continue
        symbol = option.tiingo_symbol or option.symbol or ""
        try:
            raw_rows, source = selected_fetcher(symbol, fetch_start, as_of)
            history = _parse_history(raw_rows, as_of)
            if not history or history[-1]["date"] != as_of.isoformat():
                raise ValueError(f"no adjusted close for {as_of.isoformat()}")
            internal_rows.append(_decision_row(option, symbol, as_of, history, profile, source))
            source_rows.append(
                {
                    "option_id": option.option_id,
                    "symbol": symbol,
                    "source": source,
                    "rows": history,
                }
            )
            sources.add(source)
        except Exception as exc:
            failed_options.append(option.option_id)
            internal_rows.append(_failed_row(option, symbol, as_of, profile, str(exc), compact=compact))
            source_rows.append(
                {"option_id": option.option_id, "symbol": symbol, "source": "unavailable", "rows": [], "error": str(exc)}
            )

    _add_benchmark_metrics(internal_rows, profile)
    quality_evidence = (
        _quality_evidence_report(internal_rows, profile, as_of, manifest.methodology_version)
        if include_quality_evidence
        else None
    )
    rows = [_public_row(row, profile, compact=compact) for row in internal_rows]
    market_state = _market_state(internal_rows)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    report = {
        "version": "capitalbench_decision_context_v2" if compact else "capitalbench_decision_context_v1",
        "generated_at_utc": generated_at,
        "methodology_version": manifest.methodology_version,
        "profile": profile,
        "source": "; ".join(sorted(sources)) or "cash only",
        "as_of_date_requested": as_of.isoformat(),
        "total_options": len(rows),
        "failed_options": failed_options,
        "market_state": market_state,
        "columns": _metric_columns(profile, compact=compact),
        "rows": rows,
    }
    history_report = {
        "version": "capitalbench_decision_context_source_history_v1",
        "generated_at_utc": generated_at,
        "as_of_date_requested": as_of.isoformat(),
        "fetch_start_date": fetch_start.isoformat(),
        "sources": sorted(sources),
        "options": source_rows,
    }
    _write_csv(csv_path, rows, profile, compact=compact)
    write_json(json_path, report)
    write_json(history_path, history_report)
    markdown_path.write_text(_render_markdown(report), encoding="utf-8")
    if quality_evidence is not None:
        write_json(quality_json_path, quality_evidence)
        quality_markdown_path.write_text(
            _render_quality_evidence_markdown(quality_evidence),
            encoding="utf-8",
        )
    return DecisionContextOutput(
        csv_path=csv_path,
        json_path=json_path,
        markdown_path=markdown_path,
        history_path=history_path,
        profile=profile,
        total_options=len(rows),
        failed_options=failed_options,
        quality_json_path=quality_json_path if include_quality_evidence else None,
        quality_markdown_path=quality_markdown_path if include_quality_evidence else None,
    )


def _profile_for_manifest(manifest: Any) -> str:
    horizon = str(manifest.horizon or "").lower()
    if "month" in horizon:
        return "monthly"
    if manifest.entry_date and manifest.exit_date:
        start = datetime.fromisoformat(manifest.entry_date).date()
        end = datetime.fromisoformat(manifest.exit_date).date()
        if (end - start).days >= 21:
            return "monthly"
    return "weekly"


def _default_history_fetcher(symbol: str, start: date, end: date) -> tuple[list[dict[str, Any]], str]:
    api_key = os.environ.get(TIINGO_API_KEY_ENV, "").strip()
    if api_key:
        try:
            rows = fetch_tiingo_eod_prices(symbol, start.isoformat(), end.isoformat(), api_key)
            if rows:
                return rows, "tiingo_eod_adjusted_price_and_volume"
        except Exception:
            pass
    return _fetch_yahoo_history(symbol, start, end), "yahoo_chart_adjusted_close_and_reported_volume"


def _fetch_yahoo_history(symbol: str, start: date, end: date) -> list[dict[str, Any]]:
    return [
        {
            "date": row["date"],
            "adjClose": row["adjClose"],
            "volume": row.get("volume"),
        }
        for row in _fetch_yahoo_chart_adjclose(symbol, start, end)
    ]


def _parse_history(rows: list[dict[str, Any]], as_of: date) -> list[dict[str, Any]]:
    parsed: dict[str, dict[str, Any]] = {}
    for row in rows:
        raw_date = str(row.get("date") or "")[:10]
        raw_price = row.get("adjClose", row.get("adj_close"))
        if not raw_date or raw_price is None or raw_date > as_of.isoformat():
            continue
        volume = row.get("adjVolume", row.get("adj_volume", row.get("volume")))
        parsed[raw_date] = {
            "date": raw_date,
            "adj_close": float(raw_price),
            "volume": None if volume in {None, ""} else float(volume),
        }
    return [parsed[key] for key in sorted(parsed)]


def _decision_row(option: Any, symbol: str, as_of: date, history: list[dict[str, Any]], profile: str, source: str) -> dict[str, Any]:
    prices = [float(item["adj_close"]) for item in history]
    row = _base_row(option, symbol, as_of, "pass")
    row.update({"as_of_price_date": history[-1]["date"], "source": source, "_history": history})
    if profile == "weekly":
        row.update(
            {
                "return_3s": _session_return(prices, 3),
                "return_5s": _session_return(prices, 5),
                "return_21s": _session_return(prices, 21),
                "prior_16s_return": _prior_session_return(prices, recent=5, prior=16),
                "volatility_21s": _annualized_volatility(prices[-22:]),
                "max_drawdown_21s": _max_drawdown(prices[-22:]),
                "volume_zscore_5v60": _volume_zscore(history, recent=5, baseline=60),
                "distance_52w_high": _distance_from_high(prices[-252:]),
            }
        )
    else:
        row.update(
            {
                "return_5s": _session_return(prices, 5),
                "return_21s": _session_return(prices, 21),
                "prior_105s_return": _prior_session_return(prices, recent=21, prior=105),
                "volatility_63s": _annualized_volatility(prices[-64:]),
                "max_drawdown_63s": _max_drawdown(prices[-64:]),
                "volume_zscore_20v120": _volume_zscore(history, recent=20, baseline=120),
                "distance_52w_high": _distance_from_high(prices[-252:]),
            }
        )
    return row


def _cash_row(option: Any, as_of: date, profile: str, *, compact: bool = False) -> dict[str, Any]:
    row = _base_row(option, "", as_of, "cash")
    row.update({"as_of_price_date": as_of.isoformat(), "source": "cash", "_history": []})
    metric_names = _metric_columns(profile, compact=compact)
    for name in metric_names:
        if name not in {
            "option_id",
            "symbol",
            "option_group",
            "economic_exposure_cluster",
            "as_of_price_date",
            "status",
        }:
            row[name] = 0.0 if "corr" not in name and "distance" not in name else ""
    if profile == "weekly":
        row.update({"return_5s": 0.0, "return_21s": 0.0, "prior_16s_return": 0.0})
    else:
        row.update({"return_21s": 0.0, "prior_105s_return": 0.0})
    return row


def _failed_row(
    option: Any,
    symbol: str,
    as_of: date,
    profile: str,
    message: str,
    *,
    compact: bool = False,
) -> dict[str, Any]:
    row = _base_row(option, symbol, as_of, "fail")
    row.update({"as_of_price_date": "", "source": "unavailable", "message": message, "_history": []})
    for name in _metric_columns(profile, compact=compact):
        row.setdefault(name, "")
    return row


def _base_row(option: Any, symbol: str, as_of: date, status: str) -> dict[str, Any]:
    return {
        "option_id": option.option_id,
        "symbol": symbol,
        "option_group": option.option_group,
        "economic_exposure_cluster": economic_exposure_cluster(option),
        "as_of_date_requested": as_of.isoformat(),
        "status": status,
        "_is_benchmark": bool(getattr(option, "is_benchmark", False))
        or str(option.option_id).upper() == "SP500"
        or str(symbol).upper() == "SPY",
        "_is_cash": bool(getattr(option, "is_cash", False)),
    }


def _add_benchmark_metrics(rows: list[dict[str, Any]], profile: str) -> None:
    benchmark = next(
        (row for row in rows if str(row.get("option_id") or "").upper() == "SP500"),
        next((row for row in rows if str(row.get("symbol") or "").upper() == "SPY"), None),
    )
    if benchmark is None:
        return
    benchmark_history = benchmark.get("_history") or []
    benchmark_returns = _returns_by_date(benchmark_history)
    for row in rows:
        if row.get("status") == "fail":
            continue
        if profile == "weekly":
            row["active_return_5s"] = _subtract(row.get("return_5s"), benchmark.get("return_5s"))
            row["prior_16s_active_return"] = _subtract(
                row.get("prior_16s_return"), benchmark.get("prior_16s_return")
            )
            observations = 63
        else:
            row["active_return_21s"] = _subtract(row.get("return_21s"), benchmark.get("return_21s"))
            row["prior_105s_active_return"] = _subtract(
                row.get("prior_105s_return"), benchmark.get("prior_105s_return")
            )
            observations = 252
        if row.get("status") == "cash":
            row[f"corr_spy_{observations}s"] = ""
            row[f"beta_spy_{observations}s"] = 0.0
            continue
        pairs = _aligned_return_pairs(_returns_by_date(row.get("_history") or []), benchmark_returns, observations)
        row[f"corr_spy_{observations}s"] = _correlation(pairs)
        row[f"beta_spy_{observations}s"] = _beta(pairs)


def _quality_evidence_report(
    rows: list[dict[str, Any]],
    profile: str,
    as_of: date,
    methodology_version: str | None,
) -> dict[str, Any]:
    if profile == "weekly":
        component_fields = {
            "prior_active_rank": "prior_16s_active_return",
            "recent_active_reversal_rank": "active_return_5s",
            "low_volatility_rank": "volatility_21s",
            "shallow_drawdown_rank": "max_drawdown_21s",
        }
    else:
        component_fields = {
            "prior_active_rank": "prior_105s_active_return",
            "recent_active_reversal_rank": "active_return_21s",
            "low_volatility_rank": "volatility_63s",
            "shallow_drawdown_rank": "max_drawdown_63s",
        }

    active_rows = [
        row
        for row in rows
        if not bool(row.get("_is_benchmark")) and not bool(row.get("_is_cash"))
    ]
    complete_rows = [
        row
        for row in active_rows
        if row.get("status") == "pass"
        and all(_number(row.get(field)) is not None for field in component_fields.values())
    ]
    ranks = {
        component: _percentile_ranks(complete_rows, field)
        for component, field in component_fields.items()
    }
    evidence_rows: list[dict[str, Any]] = []
    for index, row in enumerate(complete_rows):
        components = {
            "prior_active_rank": ranks["prior_active_rank"][index],
            "recent_active_reversal_rank": 1.0 - ranks["recent_active_reversal_rank"][index],
            "low_volatility_rank": 1.0 - ranks["low_volatility_rank"][index],
            "shallow_drawdown_rank": ranks["shallow_drawdown_rank"][index],
        }
        quality_score = sum(
            QUALITY_EVIDENCE_WEIGHTS[name] * value
            for name, value in components.items()
        )
        evidence_rows.append(
            {
                "option_id": row["option_id"],
                **components,
                "quality_evidence_score": quality_score,
            }
        )
    total_active = len(active_rows)
    coverage = len(evidence_rows) / total_active if total_active else 0.0
    return {
        "version": "capitalbench_quality_evidence_v1",
        "methodology_version": methodology_version,
        "profile": profile,
        "as_of_date_requested": as_of.isoformat(),
        "total_active_options": total_active,
        "complete_options": len(evidence_rows),
        "coverage": coverage,
        "minimum_required_coverage": QUALITY_EVIDENCE_MINIMUM_COVERAGE,
        "weights": QUALITY_EVIDENCE_WEIGHTS,
        "rows": evidence_rows,
    }


def _percentile_ranks(rows: list[dict[str, Any]], field: str) -> list[float]:
    if not rows:
        return []
    ordered = sorted(
        ((index, float(row[field])) for index, row in enumerate(rows)),
        key=lambda item: item[1],
    )
    output = [0.0] * len(rows)
    denominator = max(len(rows) - 1, 1)
    cursor = 0
    while cursor < len(ordered):
        end = cursor + 1
        while end < len(ordered) and ordered[end][1] == ordered[cursor][1]:
            end += 1
        rank = ((cursor + end - 1) / 2.0) / denominator if len(rows) > 1 else 0.5
        for original_index, _value in ordered[cursor:end]:
            output[original_index] = rank
        cursor = end
    return output


def _public_row(row: dict[str, Any], profile: str, *, compact: bool = False) -> dict[str, Any]:
    return {column: row.get(column, "") for column in _metric_columns(profile, compact=compact)}


def _metric_columns(profile: str, *, compact: bool = False) -> list[str]:
    identity = (
        ["option_id", "symbol", "economic_exposure_cluster"]
        if compact
        else ["option_id", "symbol", "option_group", "as_of_price_date"]
    )
    if profile == "weekly":
        metrics = ["return_3s", "active_return_5s", "prior_16s_active_return"] if compact else [
            "return_3s", "return_5s", "active_return_5s", "prior_16s_active_return"
        ]
        metrics.extend(
            [
                "volatility_21s",
                "max_drawdown_21s",
                "volume_zscore_5v60",
                "corr_spy_63s",
                "beta_spy_63s",
                "distance_52w_high",
            ]
        )
    else:
        metrics = ["return_5s", "active_return_21s", "prior_105s_active_return"] if compact else [
            "return_5s", "return_21s", "active_return_21s", "prior_105s_active_return"
        ]
        metrics.extend(
            [
                "volatility_63s",
                "max_drawdown_63s",
                "volume_zscore_20v120",
                "corr_spy_252s",
                "beta_spy_252s",
                "distance_52w_high",
            ]
        )
    return identity + metrics + ([] if compact else ["status"])


def _market_state(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_symbol = {str(row.get("symbol") or "").upper(): row for row in rows}
    state: dict[str, Any] = {}
    for symbol in ["SPY", "RSP", "HYG", "TLT", "UUP", "USO", "IAU"]:
        row = by_symbol.get(symbol)
        state[f"{symbol.lower()}_return_5s"] = row.get("return_5s", "") if row else ""
        state[f"{symbol.lower()}_return_21s"] = row.get("return_21s", "") if row else ""
    spy = by_symbol.get("SPY")
    rsp = by_symbol.get("RSP")
    state["rsp_minus_spy_5s"] = _subtract(
        rsp.get("return_5s") if rsp else None,
        spy.get("return_5s") if spy else None,
    )
    state["rsp_minus_spy_21s"] = _subtract(
        rsp.get("return_21s") if rsp else None,
        spy.get("return_21s") if spy else None,
    )
    noncash = [row for row in rows if row.get("status") == "pass"]
    for window in ["5s", "21s"]:
        values = [_number(row.get(f"return_{window}")) for row in noncash]
        available = [value for value in values if value is not None]
        state[f"positive_asset_share_{window}"] = (
            sum(1 for value in available if value > 0) / len(available) if available else ""
        )
    active = [_number(row.get("active_return_5s")) for row in noncash]
    active_values = [value for value in active if value is not None]
    state["active_return_dispersion_5s"] = statistics.stdev(active_values) if len(active_values) >= 2 else ""
    return state


def _session_return(prices: list[float], sessions: int) -> float | str:
    if len(prices) <= sessions or prices[-sessions - 1] <= 0:
        return ""
    return prices[-1] / prices[-sessions - 1] - 1.0


def _prior_session_return(prices: list[float], *, recent: int, prior: int) -> float | str:
    if len(prices) <= recent + prior or prices[-recent - prior - 1] <= 0:
        return ""
    return prices[-recent - 1] / prices[-recent - prior - 1] - 1.0


def _annualized_volatility(prices: list[float]) -> float | str:
    returns = [prices[index] / prices[index - 1] - 1.0 for index in range(1, len(prices)) if prices[index - 1] > 0]
    return statistics.stdev(returns) * math.sqrt(252) if len(returns) >= 2 else ""


def _max_drawdown(prices: list[float]) -> float | str:
    if not prices:
        return ""
    peak = prices[0]
    drawdown = 0.0
    for price in prices:
        peak = max(peak, price)
        if peak > 0:
            drawdown = min(drawdown, price / peak - 1.0)
    return drawdown


def _distance_from_high(prices: list[float]) -> float | str:
    if not prices:
        return ""
    high = max(prices)
    return prices[-1] / high - 1.0 if high > 0 else ""


def _volume_zscore(history: list[dict[str, Any]], *, recent: int, baseline: int) -> float | str:
    volumes = [item.get("volume") for item in history]
    if len(volumes) < recent + baseline or any(value is None for value in volumes[-recent - baseline :]):
        return ""
    recent_values = [float(value) for value in volumes[-recent:]]
    baseline_values = [float(value) for value in volumes[-recent - baseline : -recent]]
    baseline_stdev = statistics.stdev(baseline_values)
    if baseline_stdev <= 0:
        return ""
    return (statistics.mean(recent_values) - statistics.mean(baseline_values)) / baseline_stdev


def _returns_by_date(history: list[dict[str, Any]]) -> dict[str, float]:
    returns: dict[str, float] = {}
    for index in range(1, len(history)):
        previous = float(history[index - 1]["adj_close"])
        if previous > 0:
            returns[str(history[index]["date"])] = float(history[index]["adj_close"]) / previous - 1.0
    return returns


def _aligned_return_pairs(left: dict[str, float], right: dict[str, float], observations: int) -> list[tuple[float, float]]:
    dates = sorted(set(left) & set(right))[-observations:]
    return [(left[item], right[item]) for item in dates]


def _correlation(pairs: list[tuple[float, float]]) -> float | str:
    if len(pairs) < 2:
        return ""
    left = [item[0] for item in pairs]
    right = [item[1] for item in pairs]
    left_stdev = statistics.stdev(left)
    right_stdev = statistics.stdev(right)
    if left_stdev <= 0 or right_stdev <= 0:
        return ""
    return statistics.correlation(left, right)


def _beta(pairs: list[tuple[float, float]]) -> float | str:
    if len(pairs) < 2:
        return ""
    left = [item[0] for item in pairs]
    right = [item[1] for item in pairs]
    variance = statistics.variance(right)
    return statistics.covariance(left, right) / variance if variance > 0 else ""


def _subtract(left: Any, right: Any) -> float | str:
    left_value = _number(left)
    right_value = _number(right)
    return left_value - right_value if left_value is not None and right_value is not None else ""


def _number(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _write_csv(path: Path, rows: list[dict[str, Any]], profile: str, *, compact: bool = False) -> None:
    columns = _metric_columns(profile, compact=compact)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _render_markdown(report: dict[str, Any]) -> str:
    profile = str(report["profile"])
    lines = [
        f"# {DECISION_CONTEXT_TITLE}",
        "",
        f"Profile: {profile}. All values stop at the requested close and are sorted by frozen option order, not performance.",
        "",
        "Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.",
        "",
        "No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.",
        "",
        f"- Source: {report['source']}",
        f"- As-of date requested: {report['as_of_date_requested']}",
        f"- Failed options: {len(report['failed_options'])}",
        "",
        "## Mechanical Market State",
        "",
        "| metric | value |",
        "| --- | --- |",
    ]
    for key, value in report["market_state"].items():
        lines.append(f"| {key} | {_format_cell(value, key)} |")
    columns = list(report.get("columns") or _metric_columns(profile))
    lines.extend(
        [
            "",
            "## Option Decision Context",
            "",
            "| " + " | ".join(columns) + " |",
            "| " + " | ".join("---" for _ in columns) + " |",
        ]
    )
    for row in report["rows"]:
        lines.append("| " + " | ".join(_format_cell(row.get(column), column) for column in columns) + " |")
    return "\n".join(lines) + "\n"


def _render_quality_evidence_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# {QUALITY_EVIDENCE_TITLE}",
        "",
        (
            "Additional entry-time information follows. This is a complete cross-sectional "
            "evidence table, not a recommendation or reduced universe."
        ),
        "",
        (
            "A higher quality evidence score combines a stronger prior relative trend, a deeper "
            "recent relative pullback, lower volatility, and shallower drawdown. Use or reject "
            "this evidence as you judge appropriate."
        ),
        "",
        (
            "All values are entry-date percentile ranks from 0 to 1. The score is frozen at "
            "45% prior active rank, 30% recent active pullback rank, 15% low-volatility rank, "
            "and 10% shallow-drawdown rank. No outcome data is included."
        ),
        "",
        f"- Profile: {report['profile']}",
        f"- As-of date requested: {report['as_of_date_requested']}",
        f"- Coverage: {int(report['complete_options'])}/{int(report['total_active_options'])}",
        "",
        "| option_id | prior active rank | recent pullback rank | low volatility rank | shallow drawdown rank | quality evidence score |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in report["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["option_id"]),
                    f"{float(row['prior_active_rank']):.3f}",
                    f"{float(row['recent_active_reversal_rank']):.3f}",
                    f"{float(row['low_volatility_rank']):.3f}",
                    f"{float(row['shallow_drawdown_rank']):.3f}",
                    f"{float(row['quality_evidence_score']):.3f}",
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _format_cell(value: Any, column: str) -> str:
    number = _number(value)
    if number is None:
        return "" if value in {None, ""} else str(value).replace("|", "\\|")
    if "return" in column or "volatility" in column or "drawdown" in column or "distance" in column or "share" in column or column.startswith(("spy_", "rsp_", "hyg_", "tlt_", "uup_", "uso_", "iau_")):
        return f"{number * 100:.2f}%"
    return f"{number:.3f}"

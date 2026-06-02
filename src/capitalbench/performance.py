from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any
import urllib.parse
import urllib.request

from .io import load_options, write_json
from .scoring import _is_cash_option
from .universe import TIINGO_API_KEY_ENV, TiingoFetcher, fetch_tiingo_eod_prices

MARKET_DATA_DIRNAME = "market_data"
UNIVERSE_TRAILING_RETURNS_CSV = "universe_trailing_returns.csv"
UNIVERSE_TRAILING_RETURNS_MD = "universe_trailing_returns.md"
UNIVERSE_TRAILING_RETURNS_JSON = "universe_trailing_returns.json"


@dataclass(frozen=True)
class UniversePerformanceOutput:
    csv_path: Path
    markdown_path: Path
    json_path: Path
    total_options: int
    fetched_symbols: list[str]
    failed_options: list[str]


def fetch_universe_performance(
    *,
    round_path: Path,
    as_of_date: str,
    overwrite_performance: bool = False,
    fetcher: TiingoFetcher | None = None,
) -> UniversePerformanceOutput:
    api_key = os.environ.get(TIINGO_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError("TIINGO_API_KEY is required for full-universe performance fetching")

    market_data_dir = round_path / MARKET_DATA_DIRNAME
    market_data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = market_data_dir / UNIVERSE_TRAILING_RETURNS_CSV
    markdown_path = market_data_dir / UNIVERSE_TRAILING_RETURNS_MD
    json_path = market_data_dir / UNIVERSE_TRAILING_RETURNS_JSON
    if not overwrite_performance:
        existing = [str(path) for path in [csv_path, markdown_path, json_path] if path.exists()]
        if existing:
            raise FileExistsError(
                "universe performance files already exist; pass --overwrite-performance to replace them: "
                + ", ".join(existing)
            )

    as_of = _parse_date(as_of_date)
    lookbacks = _lookback_dates(as_of)
    fetch_start = min(lookbacks.values()) - timedelta(days=10)
    fetch = fetcher or fetch_tiingo_eod_prices

    rows: list[dict[str, Any]] = []
    fetched_symbols: list[str] = []
    failed_options: list[str] = []
    for option in load_options(round_path):
        if not option.include_in_universe:
            continue
        if _is_cash_option(option):
            rows.append(_cash_performance_row(option, as_of))
            continue
        symbol = option.tiingo_symbol or option.symbol
        if not symbol:
            row = _failed_performance_row(option, as_of, "missing Tiingo symbol")
            rows.append(row)
            failed_options.append(option.option_id)
            continue
        fetched_symbols.append(symbol)
        try:
            tiingo_rows = fetch(symbol, fetch_start.isoformat(), as_of.isoformat(), api_key)
            row = _performance_row_from_tiingo(option, symbol, as_of, lookbacks, tiingo_rows)
            if row["status"] == "pass" and row.get("as_of_price_date") != as_of.isoformat():
                yahoo_row = _fallback_performance_row_from_yahoo(option, symbol, as_of, lookbacks, fetch_start)
                if yahoo_row is not None and yahoo_row.get("as_of_price_date") == as_of.isoformat():
                    row = yahoo_row
        except Exception as exc:
            row = _fallback_performance_row_from_yahoo(option, symbol, as_of, lookbacks, fetch_start)
            if row is None:
                row = _failed_performance_row(option, as_of, str(exc), symbol=symbol)
        rows.append(row)
        if row["status"] != "pass":
            failed_options.append(option.option_id)

    report = {
        "generated_at_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "source": _performance_source(rows),
        "as_of_date_requested": as_of.isoformat(),
        "return_windows": ["7d", "30d", "6m", "1y"],
        "total_options": len(rows),
        "fetched_symbols": sorted(set(fetched_symbols)),
        "failed_options": failed_options,
        "rows": rows,
    }
    _write_performance_csv(csv_path, rows)
    markdown_path.write_text(_render_performance_markdown(report), encoding="utf-8")
    write_json(json_path, report)
    return UniversePerformanceOutput(
        csv_path=csv_path,
        markdown_path=markdown_path,
        json_path=json_path,
        total_options=len(rows),
        fetched_symbols=sorted(set(fetched_symbols)),
        failed_options=failed_options,
    )


def _parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _lookback_dates(as_of: date) -> dict[str, date]:
    return {
        "7d": as_of - timedelta(days=7),
        "30d": as_of - timedelta(days=30),
        "6m": _subtract_months(as_of, 6),
        "1y": _subtract_months(as_of, 12),
    }


def _subtract_months(value: date, months: int) -> date:
    month_index = value.month - 1 - months
    year = value.year + month_index // 12
    month = month_index % 12 + 1
    day = min(value.day, _days_in_month(year, month))
    return date(year, month, day)


def _days_in_month(year: int, month: int) -> int:
    if month == 12:
        return 31
    return (date(year, month + 1, 1) - timedelta(days=1)).day


def _cash_performance_row(option: Any, as_of: date) -> dict[str, Any]:
    row = _base_row(option, symbol="", as_of=as_of, status="cash")
    row.update(
        {
            "as_of_price_date": as_of.isoformat(),
            "as_of_adj_close": 1.0,
            "price_date_7d": as_of.isoformat(),
            "return_7d": 0.0,
            "price_date_30d": as_of.isoformat(),
            "return_30d": 0.0,
            "price_date_6m": as_of.isoformat(),
            "return_6m": 0.0,
            "price_date_1y": as_of.isoformat(),
            "return_1y": 0.0,
            "message": "Cash return is treated as 0.0 for trailing performance.",
        }
    )
    return row


def _performance_row_from_tiingo(
    option: Any,
    symbol: str,
    as_of: date,
    lookbacks: dict[str, date],
    rows: list[dict[str, Any]],
) -> dict[str, Any]:
    prices = _parse_tiingo_prices(rows)
    if not prices:
        return _failed_performance_row(option, as_of, "Tiingo returned no usable adjClose rows.", symbol=symbol)
    as_of_point = _nearest_on_or_before(prices, as_of)
    if as_of_point is None:
        return _failed_performance_row(option, as_of, "No Tiingo adjClose row on or before as-of date.", symbol=symbol)

    output = _base_row(option, symbol=symbol, as_of=as_of, status="pass")
    output["as_of_price_date"] = as_of_point[0].isoformat()
    output["as_of_adj_close"] = as_of_point[1]
    messages: list[str] = []
    for label, target_date in lookbacks.items():
        point = _nearest_on_or_before(prices, target_date)
        output[f"price_date_{label}"] = point[0].isoformat() if point else ""
        output[f"return_{label}"] = (as_of_point[1] / point[1] - 1.0) if point else ""
        if point is None:
            messages.append(f"missing baseline for {label}")
    if messages:
        output["status"] = "fail"
        output["message"] = "; ".join(messages)
    else:
        output["message"] = "OK"
    return output


def _failed_performance_row(option: Any, as_of: date, message: str, symbol: str | None = None) -> dict[str, Any]:
    row = _base_row(option, symbol=symbol or option.symbol or "", as_of=as_of, status="fail")
    row.update(
        {
            "as_of_price_date": "",
            "as_of_adj_close": "",
            "price_date_7d": "",
            "return_7d": "",
            "price_date_30d": "",
            "return_30d": "",
            "price_date_6m": "",
            "return_6m": "",
            "price_date_1y": "",
            "return_1y": "",
            "message": message,
        }
    )
    return row


def _fallback_performance_row_from_yahoo(
    option: Any,
    symbol: str,
    as_of: date,
    lookbacks: dict[str, date],
    fetch_start: date,
) -> dict[str, Any] | None:
    try:
        yahoo_rows = _fetch_yahoo_chart_adjclose(symbol, fetch_start, as_of)
    except Exception:
        return None
    row = _performance_row_from_tiingo(option, symbol, as_of, lookbacks, yahoo_rows)
    if row["status"] != "pass":
        return None
    row["message"] = "OK; yahoo_chart_adjclose fallback after Tiingo hourly rate limit or delayed EOD row"
    return row


def _fetch_yahoo_chart_adjclose(symbol: str, start_date: date, end_date: date) -> list[dict[str, Any]]:
    period1 = int(datetime.combine(start_date, time.min, tzinfo=timezone.utc).timestamp())
    period2 = int(datetime.combine(end_date + timedelta(days=2), time.min, tzinfo=timezone.utc).timestamp())
    encoded_symbol = urllib.parse.quote(symbol, safe="")
    query = urllib.parse.urlencode({"period1": period1, "period2": period2, "interval": "1d", "events": "history"})
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{encoded_symbol}?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": "CapitalBench/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read().decode("utf-8")
    data = json.loads(payload)
    result = ((data.get("chart") or {}).get("result") or [None])[0]
    if not result:
        raise ValueError(f"Yahoo chart returned no result for {symbol}")
    timestamps = result.get("timestamp") or []
    indicators = result.get("indicators") or {}
    quote = (indicators.get("quote") or [{}])[0]
    adjclose = (indicators.get("adjclose") or [{}])[0].get("adjclose") or []
    closes = quote.get("close") or []
    rows: list[dict[str, Any]] = []
    for index, timestamp in enumerate(timestamps):
        close = closes[index] if index < len(closes) else None
        adj_close = adjclose[index] if index < len(adjclose) else close
        if close is None or adj_close is None:
            continue
        rows.append(
            {
                "date": datetime.fromtimestamp(int(timestamp), tz=timezone.utc).date().isoformat(),
                "close": close,
                "adjClose": adj_close,
            }
        )
    if not rows:
        raise ValueError(f"Yahoo chart returned no usable adjusted close rows for {symbol}")
    return rows


def _performance_source(rows: list[dict[str, Any]]) -> str:
    has_yahoo = any("yahoo_chart_adjclose fallback" in str(row.get("message") or "") for row in rows)
    if has_yahoo:
        return "tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message"
    return "tiingo_eod_adj_close"


def _base_row(option: Any, symbol: str, as_of: date, status: str) -> dict[str, Any]:
    return {
        "option_id": option.option_id,
        "symbol": symbol,
        "name": option.name,
        "asset_class": option.asset_class,
        "category": option.category,
        "option_group": option.option_group,
        "risk_bucket": option.risk_bucket,
        "as_of_date_requested": as_of.isoformat(),
        "status": status,
    }


def _parse_tiingo_prices(rows: list[dict[str, Any]]) -> list[tuple[date, float]]:
    parsed: list[tuple[date, float]] = []
    for row in rows:
        raw_date = row.get("date")
        adj_close = row.get("adjClose", row.get("adj_close"))
        if raw_date is None or adj_close is None:
            continue
        parsed.append((_parse_date(str(raw_date)[:10]), float(adj_close)))
    return sorted(parsed, key=lambda item: item[0])


def _nearest_on_or_before(prices: list[tuple[date, float]], target: date) -> tuple[date, float] | None:
    candidates = [point for point in prices if point[0] <= target]
    return candidates[-1] if candidates else None


def _write_performance_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "option_id",
        "symbol",
        "name",
        "asset_class",
        "category",
        "option_group",
        "risk_bucket",
        "as_of_date_requested",
        "as_of_price_date",
        "as_of_adj_close",
        "price_date_7d",
        "return_7d",
        "price_date_30d",
        "return_30d",
        "price_date_6m",
        "return_6m",
        "price_date_1y",
        "return_1y",
        "status",
        "message",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _render_performance_markdown(report: dict[str, Any]) -> str:
    rows = report["rows"]
    header = [
        "# Full-Universe Trailing Returns",
        "",
        "This table is mechanically calculated from Tiingo EOD adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.",
        "",
        f"- Source: {report['source']}",
        f"- As-of date requested: {report['as_of_date_requested']}",
        f"- Failed options: {len(report['failed_options'])}",
        "",
    ]
    columns = [
        "option_id",
        "symbol",
        "option_group",
        "as_of_price_date",
        "return_7d",
        "return_30d",
        "return_6m",
        "return_1y",
        "status",
    ]
    table = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _column in columns) + " |",
    ]
    for row in rows:
        table.append("| " + " | ".join(_format_markdown_cell(row.get(column), column) for column in columns) + " |")
    return "\n".join(header + table) + "\n"


def _format_markdown_cell(value: Any, column: str) -> str:
    if value is None or value == "":
        return ""
    if column.startswith("return_"):
        return f"{float(value) * 100:.2f}%"
    return str(value)

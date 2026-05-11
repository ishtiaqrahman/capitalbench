from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Any

from .io import load_options, load_options_file, write_json
from .schemas import MarketOption

TIINGO_API_KEY_ENV = "TIINGO_API_KEY"

TiingoFetcher = Callable[[str, str, str, str], list[dict[str, Any]]]


@dataclass(frozen=True)
class UniverseValidationOutput:
    json_path: Path
    markdown_path: Path
    report: dict[str, Any]


def fetch_tiingo_eod_prices(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, Any]]:
    encoded_symbol = urllib.parse.quote(symbol, safe="")
    query = urllib.parse.urlencode({"startDate": start_date, "endDate": end_date})
    url = f"https://api.tiingo.com/tiingo/daily/{encoded_symbol}/prices?{query}"
    request = urllib.request.Request(url, headers={"Authorization": f"Token {api_key}"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read().decode("utf-8")
    data = json.loads(payload)
    if not isinstance(data, list):
        raise ValueError(f"Tiingo response for {symbol} was not a price row list")
    return data


def validate_universe(
    *,
    options_path: Path | None = None,
    round_path: Path | None = None,
    start_date: str,
    end_date: str,
    fetcher: TiingoFetcher | None = None,
) -> UniverseValidationOutput:
    if (options_path is None) == (round_path is None):
        raise ValueError("pass exactly one of options_path or round_path")

    api_key = os.environ.get(TIINGO_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError("TIINGO_API_KEY is required for universe validation")

    options = load_options(round_path) if round_path is not None else load_options_file(options_path or Path())
    output_dir = round_path if round_path is not None else (options_path or Path()).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    fetch = fetcher or fetch_tiingo_eod_prices

    results: list[dict[str, Any]] = []
    warnings: list[str] = []
    for option in options:
        if option.is_cash:
            results.append(_cash_result(option))
            continue
        try:
            rows = fetch(option.tiingo_symbol or option.symbol or "", start_date, end_date, api_key)
            results.append(_validate_tiingo_rows(option, rows))
        except Exception as exc:
            results.append(_failed_result(option, str(exc)))

    failed = [result["tiingo_symbol"] for result in results if result["status"] == "fail"]
    passed = [result["tiingo_symbol"] for result in results if result["status"] == "pass"]
    cash_count = sum(1 for result in results if result["status"] == "skipped_cash")
    if failed:
        warnings.append("No failed ticker should be used in a public round.")

    report = {
        "validated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "tiingo",
        "start_date": start_date,
        "end_date": end_date,
        "total_options": len(options),
        "cash_options": cash_count,
        "validated_tickers": passed,
        "failed_tickers": failed,
        "warnings": warnings,
        "results": results,
    }
    json_path = output_dir / "universe_validation_report.json"
    markdown_path = output_dir / "universe_validation_report.md"
    write_json(json_path, report)
    markdown_path.write_text(_render_markdown_report(report), encoding="utf-8")
    return UniverseValidationOutput(json_path=json_path, markdown_path=markdown_path, report=report)


def _cash_result(option: MarketOption) -> dict[str, Any]:
    return {
        "id": option.id,
        "symbol": option.symbol,
        "tiingo_symbol": option.tiingo_symbol,
        "status": "skipped_cash",
        "rows_returned": 0,
        "first_date": None,
        "last_date": None,
        "has_close": False,
        "has_adj_close": False,
        "null_adj_close_count": 0,
        "message": "Cash option skipped; Tiingo validation is not required.",
    }


def _failed_result(option: MarketOption, message: str, rows_returned: int = 0) -> dict[str, Any]:
    return {
        "id": option.id,
        "symbol": option.symbol,
        "tiingo_symbol": option.tiingo_symbol,
        "status": "fail",
        "rows_returned": rows_returned,
        "first_date": None,
        "last_date": None,
        "has_close": False,
        "has_adj_close": False,
        "null_adj_close_count": 0,
        "message": message,
    }


def _validate_tiingo_rows(option: MarketOption, rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return _failed_result(option, "Tiingo returned no price rows.", rows_returned=0)
    dates = [str(row.get("date") or "") for row in rows if row.get("date")]
    close_values = [row.get("close") for row in rows]
    adj_values = [_adj_close_value(row) for row in rows]
    has_close = any(value is not None for value in close_values)
    has_adj_close = any(value is not None for value in adj_values)
    null_adj_close_count = sum(1 for value in adj_values if value is None)
    messages: list[str] = []
    if not has_close:
        messages.append("Tiingo rows are missing close.")
    if not has_adj_close:
        messages.append("Tiingo rows are missing adjClose.")
    if null_adj_close_count:
        messages.append("Tiingo rows include null adjClose values.")
    status = "fail" if messages else "pass"
    return {
        "id": option.id,
        "symbol": option.symbol,
        "tiingo_symbol": option.tiingo_symbol,
        "status": status,
        "rows_returned": len(rows),
        "first_date": min(dates) if dates else None,
        "last_date": max(dates) if dates else None,
        "has_close": has_close,
        "has_adj_close": has_adj_close,
        "null_adj_close_count": null_adj_close_count,
        "message": "OK" if not messages else " ".join(messages),
    }


def _adj_close_value(row: dict[str, Any]) -> Any:
    if "adjClose" in row:
        return row.get("adjClose")
    return row.get("adj_close")


def _render_markdown_report(report: dict[str, Any]) -> str:
    passed = [result for result in report["results"] if result["status"] == "pass"]
    failed = [result for result in report["results"] if result["status"] == "fail"]
    cash = [result for result in report["results"] if result["status"] == "skipped_cash"]
    sections = [
        "# CapitalBench Universe Validation Report",
        "## Summary\n\n"
        f"- Source: {report['source']}\n"
        f"- Start date: {report['start_date']}\n"
        f"- End date: {report['end_date']}\n"
        f"- Total options: {report['total_options']}\n"
        f"- Cash options: {report['cash_options']}\n"
        f"- Passed tickers: {len(passed)}\n"
        f"- Failed tickers: {len(failed)}",
        "## Passed Tickers\n\n" + _result_table(passed),
        "## Failed Tickers\n\n" + _result_table(failed),
        "## Cash Options\n\n" + _result_table(cash),
        "## Warnings\n\n" + ("\n".join(f"- {warning}" for warning in report["warnings"]) if report["warnings"] else "_None._"),
        "## Rule\n\nNo failed ticker should be used in a public round.",
    ]
    return "\n\n".join(sections) + "\n"


def _result_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_None._"
    columns = ["id", "symbol", "tiingo_symbol", "status", "rows_returned", "first_date", "last_date", "message"]
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _column in columns) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column) or "") for column in columns) + " |")
    return "\n".join(lines)

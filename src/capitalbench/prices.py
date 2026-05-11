from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .io import load_manifest, load_options, read_json
from .run_store import get_selected_run_paths, read_run_manifest
from .scoring import _find_sp500_option, _is_cash_option
from .universe import TIINGO_API_KEY_ENV, TiingoFetcher, fetch_tiingo_eod_prices
from .validation import iter_submission_files, validate_submission_payload


@dataclass(frozen=True)
class SelectedPriceFetchOutput:
    entry_prices_path: Path
    exit_prices_path: Path
    option_ids: list[str]
    fetched_symbols: list[str]
    cash_option_ids: list[str]


def selected_price_options(round_path: Path, run_id: str | None = None) -> list:
    manifest = load_manifest(round_path)
    options = load_options(round_path)
    options_by_id = {option.option_id: option for option in options}
    run_paths = get_selected_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)

    selected_option_ids: set[str] = set()
    for parsed_file in iter_submission_files(run_paths.parsed_dir):
        submission = validate_submission_payload(
            read_json(parsed_file),
            options,
            manifest.round_id,
            run_type=run_type,
            replicate_count=replicate_count,
            require_run_metadata=run_type in {"official", "stability", "retrospective"},
        )
        selected_option_ids.add(submission.selected_option_id)

    if not selected_option_ids:
        raise ValueError("no valid parsed submissions found for selected price fetching")

    required_ids = set(selected_option_ids)
    required_ids.add(_find_sp500_option(options).option_id)
    required_ids.update(option.option_id for option in options if _is_cash_option(option))
    return [option for option in options if option.option_id in required_ids]


def fetch_selected_prices(
    *,
    round_path: Path,
    run_id: str | None,
    entry_date: str,
    exit_date: str,
    overwrite_prices: bool = False,
    fetcher: TiingoFetcher | None = None,
) -> SelectedPriceFetchOutput:
    api_key = os.environ.get(TIINGO_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError("TIINGO_API_KEY is required for selected price fetching")

    prices_dir = round_path / "prices"
    prices_dir.mkdir(parents=True, exist_ok=True)
    entry_path = prices_dir / "entry_prices.csv"
    exit_path = prices_dir / "exit_prices.csv"
    if not overwrite_prices:
        existing = [str(path) for path in [entry_path, exit_path] if path.exists()]
        if existing:
            raise FileExistsError(
                "price files already exist; pass --overwrite-prices to replace selected price files: "
                + ", ".join(existing)
            )

    options = selected_price_options(round_path, run_id)
    fetch = fetcher or fetch_tiingo_eod_prices
    entry_rows = _price_rows_for_date(options, entry_date, api_key, fetch)
    exit_rows = _price_rows_for_date(options, exit_date, api_key, fetch)
    _write_price_csv(entry_path, entry_rows)
    _write_price_csv(exit_path, exit_rows)
    fetched_symbols = sorted(
        {
            str(row["symbol"])
            for row in entry_rows + exit_rows
            if row.get("symbol")
        }
    )
    cash_ids = [option.option_id for option in options if _is_cash_option(option)]
    return SelectedPriceFetchOutput(
        entry_prices_path=entry_path,
        exit_prices_path=exit_path,
        option_ids=[option.option_id for option in options],
        fetched_symbols=fetched_symbols,
        cash_option_ids=cash_ids,
    )


def _price_rows_for_date(options: list, price_date: str, api_key: str, fetch: TiingoFetcher) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for option in options:
        if _is_cash_option(option):
            rows.append(
                {
                    "option_id": option.option_id,
                    "symbol": "",
                    "date": price_date,
                    "close": 1.0,
                    "adj_close": 1.0,
                    "source": "cash",
                }
            )
            continue
        symbol = option.tiingo_symbol or option.symbol or option.asset_symbol
        if not symbol:
            raise ValueError(f"non-cash option has no Tiingo symbol: {option.option_id}")
        tiingo_rows = fetch(symbol, price_date, price_date, api_key)
        price_row = _select_tiingo_row(option.option_id, symbol, price_date, tiingo_rows)
        rows.append(price_row)
    return rows


def _select_tiingo_row(option_id: str, symbol: str, price_date: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        raise ValueError(f"Tiingo returned no price rows for {option_id} ({symbol}) on {price_date}")
    row = rows[0]
    close = row.get("close")
    adj_close = row.get("adjClose", row.get("adj_close"))
    if close is None:
        raise ValueError(f"Tiingo row missing close for {option_id} ({symbol}) on {price_date}")
    if adj_close is None:
        raise ValueError(f"Tiingo row missing adjClose for {option_id} ({symbol}) on {price_date}")
    return {
        "option_id": option_id,
        "symbol": symbol,
        "date": str(row.get("date") or price_date)[:10],
        "close": close,
        "adj_close": adj_close,
        "source": "tiingo_eod",
    }


def _write_price_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = ["option_id", "symbol", "date", "close", "adj_close", "source"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

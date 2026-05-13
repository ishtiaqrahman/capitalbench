from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .io import load_manifest, load_options, read_json
from .portfolio import (
    constraints_from_manifest,
    selected_option_ids as submission_selected_option_ids,
    submission_format_from_manifest,
)
from .run_store import get_selected_run_paths, read_run_manifest
from .scoring import _find_sp500_option, _is_cash_option
from .universe import TIINGO_API_KEY_ENV, TiingoFetcher, fetch_tiingo_eod_prices
from .validation import iter_submission_files, validate_submission_payload


@dataclass(frozen=True)
class SelectedPriceFetchOutput:
    entry_prices_path: Path | None
    exit_prices_path: Path | None
    price_scope: str
    price_side: str
    option_ids: list[str]
    fetched_symbols: list[str]
    cash_option_ids: list[str]


def selected_price_options(round_path: Path, run_id: str | None = None) -> list:
    manifest = load_manifest(round_path)
    options = load_options(round_path)
    submission_format = submission_format_from_manifest(manifest)
    portfolio_constraints = constraints_from_manifest(manifest)
    run_paths = get_selected_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)

    selected_ids: set[str] = set()
    for parsed_file in iter_submission_files(run_paths.parsed_dir):
        submission = validate_submission_payload(
            read_json(parsed_file),
            options,
            manifest.round_id,
            run_type=run_type,
            replicate_count=replicate_count,
            require_run_metadata=run_type in {"official", "stability", "retrospective"},
            submission_format=submission_format,
            portfolio_constraints=portfolio_constraints,
        )
        selected_ids.update(submission_selected_option_ids(submission))

    if not selected_ids:
        raise ValueError("no valid parsed submissions found for selected price fetching")

    required_ids = set(selected_ids)
    required_ids.add(_find_sp500_option(options).option_id)
    required_ids.update(option.option_id for option in options if _is_cash_option(option))
    return [option for option in options if option.option_id in required_ids]


def fetch_selected_prices(
    *,
    round_path: Path,
    run_id: str | None,
    entry_date: str | None,
    exit_date: str | None,
    overwrite_prices: bool = False,
    full_universe: bool = False,
    price_side: str = "both",
    fetcher: TiingoFetcher | None = None,
) -> SelectedPriceFetchOutput:
    if price_side not in {"entry", "exit", "both"}:
        raise ValueError("price_side must be one of: entry, exit, both")
    if price_side in {"entry", "both"} and not entry_date:
        raise ValueError("entry_date is required when fetching entry prices")
    if price_side in {"exit", "both"} and not exit_date:
        raise ValueError("exit_date is required when fetching exit prices")

    api_key = os.environ.get(TIINGO_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError("TIINGO_API_KEY is required for price fetching")

    prices_dir = round_path / "prices"
    prices_dir.mkdir(parents=True, exist_ok=True)
    entry_path = prices_dir / "entry_prices.csv"
    exit_path = prices_dir / "exit_prices.csv"
    requested_paths = []
    if price_side in {"entry", "both"}:
        requested_paths.append(entry_path)
    if price_side in {"exit", "both"}:
        requested_paths.append(exit_path)
    if not overwrite_prices:
        existing = [str(path) for path in requested_paths if path.exists()]
        if existing:
            raise FileExistsError(
                "price files already exist; pass --overwrite-prices to replace selected price files: "
                + ", ".join(existing)
            )

    options = load_options(round_path) if full_universe else selected_price_options(round_path, run_id)
    fetch = fetcher or fetch_tiingo_eod_prices
    entry_rows: list[dict[str, Any]] = []
    exit_rows: list[dict[str, Any]] = []
    if price_side in {"entry", "both"}:
        assert entry_date is not None
        entry_rows = _price_rows_for_date(options, entry_date, api_key, fetch)
        _write_price_csv(entry_path, entry_rows)
    if price_side in {"exit", "both"}:
        assert exit_date is not None
        exit_rows = _price_rows_for_date(options, exit_date, api_key, fetch)
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
        entry_prices_path=entry_path if price_side in {"entry", "both"} else None,
        exit_prices_path=exit_path if price_side in {"exit", "both"} else None,
        price_scope="full_universe" if full_universe else "selected",
        price_side=price_side,
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
    matching_rows = [
        row
        for row in rows
        if _normalize_tiingo_date(row.get("date")) == price_date
    ]
    if not matching_rows:
        available_dates = sorted(
            {
                normalized
                for row in rows
                if (normalized := _normalize_tiingo_date(row.get("date"))) is not None
            }
        )
        available = ", ".join(available_dates) if available_dates else "none"
        raise ValueError(
            f"Tiingo returned no row exactly matching requested date {price_date} "
            f"for {option_id} ({symbol}); available dates: {available}"
        )
    row = matching_rows[0]
    close = row.get("close")
    adj_close = row.get("adjClose", row.get("adj_close"))
    if close is None:
        raise ValueError(f"Tiingo row missing close for {option_id} ({symbol}) on {price_date}")
    if adj_close is None:
        raise ValueError(f"Tiingo row missing adjClose for {option_id} ({symbol}) on {price_date}")
    return {
        "option_id": option_id,
        "symbol": symbol,
        "date": price_date,
        "close": close,
        "adj_close": adj_close,
        "source": "tiingo_eod",
    }


def _normalize_tiingo_date(raw_date: Any) -> str | None:
    if raw_date is None:
        return None
    text = str(raw_date)
    if len(text) < 10:
        return None
    return text[:10]


def _write_price_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = ["option_id", "symbol", "date", "close", "adj_close", "source"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

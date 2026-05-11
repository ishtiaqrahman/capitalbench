import csv
import json
from pathlib import Path

import pytest
import yaml

from capitalbench.performance import fetch_universe_performance
from capitalbench.prices import fetch_selected_prices
from capitalbench.scoring import score_round


def _create_round_with_submission(tmp_path: Path) -> Path:
    round_path = tmp_path / "round"
    parsed_dir = round_path / "submissions" / "parsed"
    parsed_dir.mkdir(parents=True)
    (round_path / "prices").mkdir(parents=True)
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "test",
                "title": "Test Round",
                "decision_date": "2026-01-01",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_rule": "Use entry CSV.",
                "exit_rule": "Use exit CSV.",
                "entry_date": "2026-01-02",
                "exit_date": "2026-02-02",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "options.yaml").write_text(
        yaml.safe_dump(
            {
                "options": [
                    {"option_id": "opt_a", "label": "Option A", "asset_symbol": "AAA"},
                    {"option_id": "opt_b", "label": "Option B", "asset_symbol": "BBB"},
                    {
                        "option_id": "sp500",
                        "label": "S&P 500",
                        "asset_symbol": "SPY",
                        "is_benchmark": True,
                    },
                    {"option_id": "cash", "label": "Cash", "asset_symbol": "USD", "is_cash": True},
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (parsed_dir / "model-a.json").write_text(
        json.dumps(
            {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        ),
        encoding="utf-8",
    )
    return round_path


def test_fetch_selected_prices_only_fetches_selected_plus_sp500(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")
    calls: list[str] = []

    def fake_fetch(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, object]]:
        calls.append(symbol)
        assert api_key == "test-key"
        return [{"date": f"{start_date}T00:00:00Z", "close": 100.0, "adjClose": 100.0}]

    output = fetch_selected_prices(
        round_path=round_path,
        run_id=None,
        entry_date="2026-01-02",
        exit_date="2026-02-02",
        fetcher=fake_fetch,
    )

    assert calls == ["AAA", "SPY", "AAA", "SPY"]
    assert output.option_ids == ["opt_a", "sp500", "cash"]
    assert output.fetched_symbols == ["AAA", "SPY"]

    with output.entry_prices_path.open("r", encoding="utf-8", newline="") as handle:
        entry_rows = list(csv.DictReader(handle))
    assert {row["option_id"] for row in entry_rows} == {"opt_a", "sp500", "cash"}
    assert "opt_b" not in {row["option_id"] for row in entry_rows}


def test_fetch_prices_full_universe_fetches_every_non_cash_option(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")
    calls: list[tuple[str, str, str]] = []

    def fake_fetch(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, object]]:
        calls.append((symbol, start_date, end_date))
        assert api_key == "test-key"
        return [{"date": f"{start_date}T00:00:00Z", "close": 100.0, "adjClose": 100.0}]

    output = fetch_selected_prices(
        round_path=round_path,
        run_id=None,
        entry_date="2026-01-02",
        exit_date="2026-02-02",
        full_universe=True,
        fetcher=fake_fetch,
    )

    assert calls == [
        ("AAA", "2026-01-02", "2026-01-02"),
        ("BBB", "2026-01-02", "2026-01-02"),
        ("SPY", "2026-01-02", "2026-01-02"),
        ("AAA", "2026-02-02", "2026-02-02"),
        ("BBB", "2026-02-02", "2026-02-02"),
        ("SPY", "2026-02-02", "2026-02-02"),
    ]
    assert output.price_scope == "full_universe"
    assert output.option_ids == ["opt_a", "opt_b", "sp500", "cash"]
    assert output.fetched_symbols == ["AAA", "BBB", "SPY"]

    with output.entry_prices_path.open("r", encoding="utf-8", newline="") as handle:
        entry_rows = list(csv.DictReader(handle))
    assert {row["option_id"] for row in entry_rows} == {"opt_a", "opt_b", "sp500", "cash"}


def test_full_universe_fetch_populates_regret_and_rank_when_scored(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")

    prices = {
        ("AAA", "2026-01-02"): 100.0,
        ("AAA", "2026-02-02"): 110.0,
        ("BBB", "2026-01-02"): 100.0,
        ("BBB", "2026-02-02"): 130.0,
        ("SPY", "2026-01-02"): 100.0,
        ("SPY", "2026-02-02"): 105.0,
    }

    def fake_fetch(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, object]]:
        price = prices[(symbol, start_date)]
        return [{"date": f"{start_date}T00:00:00.000Z", "close": price, "adjClose": price}]

    fetch_selected_prices(
        round_path=round_path,
        run_id=None,
        entry_date="2026-01-02",
        exit_date="2026-02-02",
        full_universe=True,
        fetcher=fake_fetch,
    )
    scores = score_round(round_path, run_id="legacy-run")

    assert len(scores) == 1
    assert scores[0].selected_option_id == "opt_a"
    assert scores[0].selected_asset_return == pytest.approx(0.10)
    assert scores[0].regret_vs_best_option == pytest.approx(0.20)
    assert scores[0].rank_among_options == 2


def test_fetch_prices_uses_exact_requested_tiingo_date(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")

    def fake_fetch(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, object]]:
        return [
            {"date": "2026-01-01T00:00:00.000Z", "close": 90.0, "adjClose": 90.0},
            {"date": f"{start_date}T00:00:00.000Z", "close": 100.0, "adjClose": 100.0},
        ]

    output = fetch_selected_prices(
        round_path=round_path,
        run_id=None,
        entry_date="2026-01-02",
        exit_date="2026-02-02",
        fetcher=fake_fetch,
    )

    with output.entry_prices_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    non_cash_rows = [row for row in rows if row["source"] == "tiingo_eod"]
    assert non_cash_rows
    assert all(row["date"] == "2026-01-02" for row in non_cash_rows)
    assert all(row["close"] == "100.0" for row in non_cash_rows)


def test_fetch_prices_fails_when_tiingo_date_does_not_match_request(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")

    def fake_fetch(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, object]]:
        return [{"date": "2026-01-03T00:00:00.000Z", "close": 100.0, "adjClose": 100.0}]

    with pytest.raises(ValueError, match="exactly matching requested date 2026-01-02"):
        fetch_selected_prices(
            round_path=round_path,
            run_id=None,
            entry_date="2026-01-02",
            exit_date="2026-02-02",
            fetcher=fake_fetch,
        )


def test_fetch_selected_prices_requires_tiingo_key(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.delenv("TIINGO_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="TIINGO_API_KEY"):
        fetch_selected_prices(
            round_path=round_path,
            run_id=None,
            entry_date="2026-01-02",
            exit_date="2026-02-02",
            fetcher=lambda *_args: [],
        )


def test_fetch_universe_performance_fetches_all_non_cash_options(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")
    calls: list[str] = []

    def fake_fetch(symbol: str, start_date: str, end_date: str, api_key: str) -> list[dict[str, object]]:
        calls.append(symbol)
        assert api_key == "test-key"
        return [
            {"date": "2025-01-10T00:00:00Z", "close": 80.0, "adjClose": 80.0},
            {"date": "2025-07-10T00:00:00Z", "close": 90.0, "adjClose": 90.0},
            {"date": "2025-12-11T00:00:00Z", "close": 95.0, "adjClose": 95.0},
            {"date": "2026-01-03T00:00:00Z", "close": 100.0, "adjClose": 100.0},
            {"date": "2026-01-10T00:00:00Z", "close": 110.0, "adjClose": 110.0},
        ]

    output = fetch_universe_performance(
        round_path=round_path,
        as_of_date="2026-01-10",
        fetcher=fake_fetch,
    )

    assert calls == ["AAA", "BBB", "SPY"]
    assert output.fetched_symbols == ["AAA", "BBB", "SPY"]
    assert output.failed_options == []
    assert output.csv_path.exists()
    assert output.markdown_path.exists()
    assert output.json_path.exists()

    with output.csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {row["option_id"]: row for row in rows}
    assert set(by_id) == {"opt_a", "opt_b", "sp500", "cash"}
    assert by_id["cash"]["return_7d"] == "0.0"
    assert float(by_id["opt_b"]["return_7d"]) == pytest.approx(0.10)
    assert float(by_id["opt_b"]["return_30d"]) == pytest.approx(110.0 / 95.0 - 1.0)
    assert "# Full-Universe Trailing Returns" in output.markdown_path.read_text(encoding="utf-8")


def test_fetch_universe_performance_requires_tiingo_key(tmp_path: Path, monkeypatch) -> None:
    round_path = _create_round_with_submission(tmp_path)
    monkeypatch.delenv("TIINGO_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="TIINGO_API_KEY"):
        fetch_universe_performance(
            round_path=round_path,
            as_of_date="2026-01-10",
            fetcher=lambda *_args: [],
        )

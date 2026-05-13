import csv
import json
import math
from pathlib import Path

import pytest
import yaml

from capitalbench.report import publish_report
from capitalbench.run_store import get_selected_run_paths
from capitalbench.scoring import score_round


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["option_id", "price"])
        writer.writeheader()
        writer.writerows(rows)


def _write_custom_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _create_round(tmp_path: Path, submissions: dict[str, dict[str, object]]) -> Path:
    round_path = tmp_path / "round"
    (round_path / "submissions" / "parsed").mkdir(parents=True)
    (round_path / "prices").mkdir(parents=True)
    (round_path / "results").mkdir(parents=True)

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
                    {
                        "option_id": "opt_a",
                        "label": "Option A",
                        "asset_symbol": "AAA",
                    },
                    {
                        "option_id": "opt_b",
                        "label": "Option B",
                        "asset_symbol": "BBB",
                    },
                    {
                        "option_id": "sp500",
                        "label": "S&P 500",
                        "asset_symbol": "SPY",
                        "is_benchmark": True,
                    },
                    {
                        "option_id": "cash",
                        "label": "Cash",
                        "asset_symbol": "USD",
                        "is_cash": True,
                    },
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_a", "price": 100},
            {"option_id": "opt_b", "price": 50},
            {"option_id": "sp500", "price": 100},
            {"option_id": "cash", "price": 1},
        ],
    )
    _write_csv(
        round_path / "prices" / "exit_prices.csv",
        [
            {"option_id": "opt_a", "price": 110},
            {"option_id": "opt_b", "price": 60},
            {"option_id": "sp500", "price": 105},
            {"option_id": "cash", "price": 1},
        ],
    )
    for filename, submission in submissions.items():
        (round_path / "submissions" / "parsed" / filename).write_text(
            json.dumps(submission),
            encoding="utf-8",
        )
    return round_path


def test_scoring_math_and_regret_calculation(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
                "cost_usd": 0.05,
            }
        },
    )

    scores = score_round(round_path)

    assert len(scores) == 1
    score = scores[0]
    assert math.isclose(score.selected_asset_return, 0.10)
    assert math.isclose(score.sp500_return, 0.05)
    assert math.isclose(score.alpha_vs_sp500, 0.05)
    assert math.isclose(score.regret_vs_best_option, 0.10)
    assert score.rank_among_options == 2
    assert score.beats_sp500 is True
    assert score.beats_cash is True
    assert math.isclose(score.alpha_per_dollar or 0, 1.0)
    run_paths = get_selected_run_paths(round_path)
    assert (run_paths.results_dir / "returns.csv").exists()
    assert (run_paths.results_dir / "leaderboard.csv").exists()


def test_portfolio_scoring_uses_weighted_returns_and_writes_allocations(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-p.json": {
                "round_id": "test",
                "model_id": "model-p",
                "provider": "openai",
                "mode": "closed_capability",
                "portfolio": [
                    {"option_id": "opt_a", "allocation_pct": 60, "rationale": "Upside exposure."},
                    {"option_id": "sp500", "allocation_pct": 25, "rationale": "Benchmark ballast."},
                    {"option_id": "cash", "allocation_pct": 15, "rationale": "Defensive ballast."},
                ],
                "confidence": 0.55,
                "portfolio_rationale": "A concentrated but partially defensive portfolio.",
                "rationale_summary": "Weighted portfolio submission.",
                "key_risks": ["Risk one"],
            }
        },
    )
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["submission_format"] = "portfolio"
    manifest["portfolio_constraints"] = {
        "min_holdings": 1,
        "max_holdings": 5,
        "allocation_increment_pct": 5,
        "min_allocation_pct": 5,
        "max_total_allocation_pct": 100,
        "allow_cash": True,
        "allow_benchmark_asset": True,
    }
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    [score] = score_round(round_path)

    expected_return = (0.60 * 0.10) + (0.25 * 0.05) + (0.15 * 0.0)
    assert score.submission_format == "portfolio"
    assert score.selected_option_id == "opt_a"
    assert score.holding_count == 3
    assert score.max_allocation_bps == 6000
    assert score.cash_allocation_bps == 1500
    assert score.benchmark_allocation_bps == 2500
    assert math.isclose(score.selected_asset_return, expected_return)
    assert math.isclose(score.portfolio_return or 0, expected_return)
    assert math.isclose(score.alpha_vs_sp500, expected_return - 0.05)

    allocations_path = get_selected_run_paths(round_path).results_dir / "allocations.csv"
    with allocations_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert [row["option_id"] for row in rows] == ["opt_a", "sp500", "cash"]
    assert [row["allocation_bps"] for row in rows] == ["6000", "2500", "1500"]


def test_scoring_allows_selected_only_price_files(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        },
    )
    _write_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_a", "price": 100},
            {"option_id": "sp500", "price": 100},
        ],
    )
    _write_csv(
        round_path / "prices" / "exit_prices.csv",
        [
            {"option_id": "opt_a", "price": 110},
            {"option_id": "sp500", "price": 105},
        ],
    )

    [score] = score_round(round_path)

    assert math.isclose(score.selected_asset_return, 0.10)
    assert math.isclose(score.alpha_vs_sp500, 0.05)
    assert score.regret_vs_best_option is None
    assert score.rank_among_options is None
    returns_path = get_selected_run_paths(round_path).results_dir / "returns.csv"
    with returns_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert {row["option_id"] for row in rows} == {"opt_a", "sp500", "cash"}
    assert all(row["rank"] == "" for row in rows)
    assert score.beats_sp500 is True
    assert score.beats_cash is True


def test_leaderboard_sorting(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-low.json": {
                "round_id": "test",
                "model_id": "model-low",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "sp500",
                "confidence": 0.9,
                "rationale_summary": "Benchmark.",
                "key_risks": ["Tracking risk"],
            },
            "model-high.json": {
                "round_id": "test",
                "model_id": "model-high",
                "provider": "anthropic",
                "mode": "closed_capability",
                "selected_option_id": "opt_b",
                "confidence": 0.4,
                "rationale_summary": "Highest return.",
                "key_risks": ["Reversal risk"],
            },
            "model-mid.json": {
                "round_id": "test",
                "model_id": "model-mid",
                "provider": "google",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.8,
                "rationale_summary": "Middle return.",
                "key_risks": ["Valuation risk"],
            },
        },
    )

    scores = score_round(round_path)

    assert [score.model_id for score in scores] == ["model-high", "model-mid", "model-low"]

    run_paths = get_selected_run_paths(round_path)
    with (run_paths.results_dir / "leaderboard.csv").open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert [row["model_id"] for row in rows] == ["model-high", "model-mid", "model-low"]


def test_cash_return_handling_without_prices(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-cash.json": {
                "round_id": "test",
                "model_id": "model-cash",
                "provider": "xai",
                "mode": "closed_capability",
                "selected_option_id": "cash",
                "confidence": 0.3,
                "rationale_summary": "Defensive choice.",
                "key_risks": ["Opportunity cost"],
            }
        },
    )
    _write_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_a", "price": 100},
            {"option_id": "opt_b", "price": 50},
            {"option_id": "sp500", "price": 100},
        ],
    )
    _write_csv(
        round_path / "prices" / "exit_prices.csv",
        [
            {"option_id": "opt_a", "price": 110},
            {"option_id": "opt_b", "price": 60},
            {"option_id": "sp500", "price": 105},
        ],
    )

    scores = score_round(round_path)

    assert scores[0].selected_option_id == "cash"
    assert scores[0].selected_asset_return == 0.0
    assert scores[0].beats_cash is False


def test_missing_sp500_price_failure(tmp_path: Path) -> None:
    round_path = _create_round(tmp_path, {})
    _write_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_a", "price": 100},
            {"option_id": "opt_b", "price": 50},
            {"option_id": "cash", "price": 1},
        ],
    )

    with pytest.raises(ValueError, match="SP500 benchmark"):
        score_round(round_path)


def test_missing_selected_option_price_failure(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        },
    )
    _write_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_b", "price": 50},
            {"option_id": "sp500", "price": 100},
            {"option_id": "cash", "price": 1},
        ],
    )

    with pytest.raises(ValueError, match="selected option_id: opt_a"):
        score_round(round_path)


def test_alpha_per_dollar_only_when_cost_is_positive(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-with-cost.json": {
                "round_id": "test",
                "model_id": "model-with-cost",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "Costed call.",
                "key_risks": ["Risk one"],
                "cost_usd": 0.05,
            },
            "model-zero-cost.json": {
                "round_id": "test",
                "model_id": "model-zero-cost",
                "provider": "google",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.6,
                "rationale_summary": "Zero cost call.",
                "key_risks": ["Risk one"],
                "cost_usd": 0,
            },
        },
    )

    scores = {score.model_id: score for score in score_round(round_path)}

    assert math.isclose(scores["model-with-cost"].alpha_per_dollar or 0, 1.0)
    assert scores["model-zero-cost"].alpha_per_dollar is None


def test_report_generation_includes_leaderboard_and_limitations(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        },
    )
    (round_path / "briefing.md").write_text("briefing", encoding="utf-8")
    (round_path / "prompt.md").write_text("prompt", encoding="utf-8")
    (round_path / "hashes.json").write_text("{}", encoding="utf-8")
    score_round(round_path)

    report_path = publish_report(round_path)
    report = report_path.read_text(encoding="utf-8")

    assert "## Leaderboard" in report
    assert "## Limitations" in report
    assert "## Reproducibility" in report


def test_scoring_uses_adj_close_when_available(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        },
    )
    fieldnames = ["option_id", "symbol", "date", "close", "adj_close"]
    _write_custom_csv(
        round_path / "prices" / "entry_prices.csv",
        fieldnames,
        [
            {"option_id": "opt_a", "symbol": "AAA", "date": "2026-01-02", "close": 100, "adj_close": 50},
            {"option_id": "opt_b", "symbol": "BBB", "date": "2026-01-02", "close": 50, "adj_close": 50},
            {"option_id": "sp500", "symbol": "SPY", "date": "2026-01-02", "close": 100, "adj_close": 100},
            {"option_id": "cash", "symbol": "", "date": "2026-01-02", "close": 1, "adj_close": 1},
        ],
    )
    _write_custom_csv(
        round_path / "prices" / "exit_prices.csv",
        fieldnames,
        [
            {"option_id": "opt_a", "symbol": "AAA", "date": "2026-02-02", "close": 200, "adj_close": 55},
            {"option_id": "opt_b", "symbol": "BBB", "date": "2026-02-02", "close": 60, "adj_close": 60},
            {"option_id": "sp500", "symbol": "SPY", "date": "2026-02-02", "close": 105, "adj_close": 105},
            {"option_id": "cash", "symbol": "", "date": "2026-02-02", "close": 1, "adj_close": 1},
        ],
    )

    score = score_round(round_path)[0]

    assert math.isclose(score.selected_asset_return, 0.10)


def test_scoring_can_map_price_rows_by_symbol(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        },
    )
    fieldnames = ["symbol", "date", "close", "adj_close"]
    _write_custom_csv(
        round_path / "prices" / "entry_prices.csv",
        fieldnames,
        [
            {"symbol": "AAA", "date": "2026-01-02", "close": 100, "adj_close": 100},
            {"symbol": "BBB", "date": "2026-01-02", "close": 50, "adj_close": 50},
            {"symbol": "SPY", "date": "2026-01-02", "close": 100, "adj_close": 100},
            {"symbol": "CASH", "date": "2026-01-02", "close": 1, "adj_close": 1},
        ],
    )
    _write_custom_csv(
        round_path / "prices" / "exit_prices.csv",
        fieldnames,
        [
            {"symbol": "AAA", "date": "2026-02-02", "close": 110, "adj_close": 110},
            {"symbol": "BBB", "date": "2026-02-02", "close": 60, "adj_close": 60},
            {"symbol": "SPY", "date": "2026-02-02", "close": 105, "adj_close": 105},
            {"symbol": "CASH", "date": "2026-02-02", "close": 1, "adj_close": 1},
        ],
    )

    score = score_round(round_path)[0]

    assert math.isclose(score.selected_asset_return, 0.10)


def test_scoring_warns_when_only_close_is_available(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "model-a.json": {
                "round_id": "test",
                "model_id": "model-a",
                "provider": "openai",
                "mode": "closed_capability",
                "selected_option_id": "opt_a",
                "confidence": 0.7,
                "rationale_summary": "A balanced choice.",
                "key_risks": ["Risk one"],
            }
        },
    )
    fieldnames = ["option_id", "symbol", "date", "close"]
    _write_custom_csv(
        round_path / "prices" / "entry_prices.csv",
        fieldnames,
        [
            {"option_id": "opt_a", "symbol": "AAA", "date": "2026-01-02", "close": 100},
            {"option_id": "opt_b", "symbol": "BBB", "date": "2026-01-02", "close": 50},
            {"option_id": "sp500", "symbol": "SPY", "date": "2026-01-02", "close": 100},
            {"option_id": "cash", "symbol": "", "date": "2026-01-02", "close": 1},
        ],
    )
    _write_custom_csv(
        round_path / "prices" / "exit_prices.csv",
        fieldnames,
        [
            {"option_id": "opt_a", "symbol": "AAA", "date": "2026-02-02", "close": 110},
            {"option_id": "opt_b", "symbol": "BBB", "date": "2026-02-02", "close": 60},
            {"option_id": "sp500", "symbol": "SPY", "date": "2026-02-02", "close": 105},
            {"option_id": "cash", "symbol": "", "date": "2026-02-02", "close": 1},
        ],
    )

    with pytest.warns(UserWarning, match="uses close"):
        score_round(round_path)

    assert (get_selected_run_paths(round_path).results_dir / "price_warnings.json").exists()

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import yaml

from capitalbench.weekly import update_weekly_performance


def _write_prices(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["option_id", "price", "date", "source"])
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _create_round(tmp_path: Path, submission: dict[str, object], *, submission_format: str = "single_pick") -> Path:
    round_path = tmp_path / "round"
    parsed_dir = round_path / "runs" / "official" / "submissions" / "parsed"
    parsed_dir.mkdir(parents=True)
    (round_path / "runs" / "official" / "results").mkdir(parents=True)
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "test-round",
                "title": "Test Round",
                "decision_date": "2026-01-01",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_rule": "Entry adjusted close.",
                "exit_rule": "Exit adjusted close.",
                "entry_date": "2026-01-02",
                "exit_date": "2026-02-02",
                "submission_format": submission_format,
                "portfolio_constraints": {
                    "min_holdings": 1,
                    "max_holdings": 5,
                    "allocation_increment_pct": 5,
                    "min_allocation_pct": 5,
                    "max_total_allocation_pct": 100,
                    "allow_cash": True,
                    "allow_benchmark_asset": True,
                },
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
                    {"option_id": "sp500", "label": "S&P 500", "asset_symbol": "SPY", "is_benchmark": True},
                    {"option_id": "cash", "label": "Cash", "asset_symbol": "USD", "is_cash": True},
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_prices(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_a", "price": 100, "date": "2026-01-02", "source": "fixture"},
            {"option_id": "opt_b", "price": 100, "date": "2026-01-02", "source": "fixture"},
            {"option_id": "sp500", "price": 100, "date": "2026-01-02", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-02", "source": "cash"},
        ],
    )
    (round_path / "runs" / "official" / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "official",
                "round_id": "test-round",
                "run_type": "official",
                "mode": "closed_capability",
                "mock": False,
                "official_score_eligible": True,
                "replicates": 1,
                "model_count": 1,
                "valid_submissions": 1,
                "invalid_submissions": 0,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    parsed_dir.joinpath("model-a.json").write_text(json.dumps(submission), encoding="utf-8")
    return round_path


def test_update_weekly_performance_scores_single_pick_snapshot(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "round_id": "test-round",
            "model_id": "model-a",
            "provider": "openai",
            "mode": "closed_capability",
            "run_type": "official",
            "replicate_index": 1,
            "replicate_count": 1,
            "is_official_score": True,
            "selected_option_id": "opt_a",
            "confidence": 0.7,
            "rationale_summary": "A balanced choice.",
            "key_risks": ["Risk one"],
        },
    )
    snapshot_path = tmp_path / "week-1.csv"
    _write_prices(
        snapshot_path,
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-09", "source": "cash"},
        ],
    )

    output = update_weekly_performance(
        round_path,
        "official",
        snapshot_price_files=[snapshot_path],
        snapshot_dates=["2026-01-09"],
    )

    assert output.snapshot_count == 2
    rows = _read_csv(output.weekly_performance_path)
    assert [row["target_date"] for row in rows] == ["2026-01-02", "2026-01-09"]
    assert math.isclose(float(rows[0]["model_return"]), 0.0)
    assert math.isclose(float(rows[1]["model_return"]), 0.10)
    assert math.isclose(float(rows[1]["sp500_return"]), 0.05)
    assert math.isclose(float(rows[1]["alpha_vs_sp500"]), 0.05)
    price_rows = _read_csv(output.weekly_prices_path)
    assert {row["option_id"] for row in price_rows} == {"opt_a", "sp500", "cash"}


def test_update_weekly_performance_scores_portfolio_snapshot(tmp_path: Path) -> None:
    round_path = _create_round(
        tmp_path,
        {
            "round_id": "test-round",
            "model_id": "model-a",
            "provider": "openai",
            "mode": "closed_capability",
            "run_type": "official",
            "replicate_index": 1,
            "replicate_count": 1,
            "is_official_score": True,
            "portfolio": [
                {"option_id": "opt_a", "allocation_pct": 60, "rationale": "Upside."},
                {"option_id": "cash", "allocation_pct": 40, "rationale": "Reserve."},
            ],
            "portfolio_rationale": "Weighted allocation.",
            "confidence": 0.7,
            "rationale_summary": "A balanced choice.",
            "key_risks": ["Risk one"],
        },
        submission_format="portfolio",
    )
    snapshot_path = tmp_path / "week-1.csv"
    _write_prices(
        snapshot_path,
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-09", "source": "cash"},
        ],
    )

    output = update_weekly_performance(
        round_path,
        "official",
        snapshot_price_files=[snapshot_path],
        snapshot_dates=["2026-01-09"],
    )

    rows = _read_csv(output.weekly_performance_path)
    week_one = rows[1]
    assert week_one["submission_format"] == "portfolio"
    assert week_one["selected_option_id"] == "opt_a"
    assert week_one["holding_count"] == "2"
    assert math.isclose(float(week_one["model_return"]), 0.06)
    assert math.isclose(float(week_one["alpha_vs_sp500"]), 0.01)

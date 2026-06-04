from __future__ import annotations

import csv
import json
from pathlib import Path

import yaml

from capitalbench.interim import update_interim_performance


def _write_prices(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["option_id", "price", "date", "source"])
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _create_round(
    rounds_dir: Path,
    round_id: str,
    *,
    entry_date: str,
    exit_date: str,
    horizon: str = "one month",
) -> Path:
    round_path = rounds_dir / round_id
    run_id = "official"
    parsed_dir = round_path / "runs" / run_id / "submissions" / "parsed"
    parsed_dir.mkdir(parents=True)
    (round_path / "runs" / run_id / "results").mkdir(parents=True)
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": round_id,
                "title": round_id,
                "decision_date": entry_date,
                "decision_deadline": f"{entry_date}T20:00:00Z",
                "horizon": horizon,
                "entry_rule": "Entry adjusted close.",
                "exit_rule": "Exit adjusted close.",
                "entry_date": entry_date,
                "exit_date": exit_date,
                "submission_format": "single_pick",
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
            {"option_id": "opt_a", "price": 100, "date": entry_date, "source": "fixture"},
            {"option_id": "opt_b", "price": 100, "date": entry_date, "source": "fixture"},
            {"option_id": "sp500", "price": 100, "date": entry_date, "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": entry_date, "source": "cash"},
        ],
    )
    (round_path / "runs" / run_id / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": run_id,
                "round_id": round_id,
                "run_type": "official",
                "mode": "closed_capability",
                "mock": False,
                "official_score_eligible": True,
                "operator_selected_official": True,
                "replicates": 1,
                "model_count": 1,
                "valid_submissions": 1,
                "invalid_submissions": 0,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    parsed_dir.joinpath("model-a.json").write_text(
        json.dumps(
            {
                "round_id": round_id,
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
            }
        ),
        encoding="utf-8",
    )
    return round_path


def test_update_interim_performance_reuses_one_snapshot_for_multiple_monthly_rounds(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    first = _create_round(rounds_dir, "round-one", entry_date="2026-01-02", exit_date="2026-02-02")
    second = _create_round(rounds_dir, "round-two", entry_date="2026-01-05", exit_date="2026-02-05")
    snapshots_dir = tmp_path / "snapshots"
    _write_prices(
        snapshots_dir / "2026-01-09.csv",
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "opt_b", "price": 95, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-09", "source": "cash"},
        ],
    )
    _write_prices(
        snapshots_dir / "2026-01-12.csv",
        [
            {"option_id": "opt_a", "price": 112, "date": "2026-01-12", "source": "fixture"},
            {"option_id": "opt_b", "price": 97, "date": "2026-01-12", "source": "fixture"},
            {"option_id": "sp500", "price": 106, "date": "2026-01-12", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-12", "source": "cash"},
        ],
    )

    output = update_interim_performance(
        rounds_dir=rounds_dir,
        snapshot_date="2026-01-12",
        snapshots_dir=snapshots_dir,
        skip_fetch=True,
        sync=False,
        min_snapshot_rows=1,
    )

    assert output.snapshot_status == "reused"
    assert {item.round_id for item in output.updated_rounds} == {"round-one", "round-two"}
    expected_dates = {
        first: ["2026-01-02", "2026-01-05", "2026-01-09", "2026-01-12"],
        second: ["2026-01-05", "2026-01-09", "2026-01-12"],
    }
    for round_path, dates in expected_dates.items():
        rows = _read_csv(round_path / "runs" / "official" / "results" / "weekly_performance.csv")
        assert [row["target_date"] for row in rows] == dates


def test_update_interim_performance_skips_weekly_track_by_default(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    weekly = _create_round(
        rounds_dir,
        "weekly-round",
        entry_date="2026-01-02",
        exit_date="2026-01-09",
        horizon="one week",
    )
    snapshots_dir = tmp_path / "snapshots"
    _write_prices(
        snapshots_dir / "2026-01-06.csv",
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-06", "source": "cash"},
        ],
    )

    output = update_interim_performance(
        rounds_dir=rounds_dir,
        snapshot_date="2026-01-06",
        snapshots_dir=snapshots_dir,
        skip_fetch=True,
        sync=False,
        min_snapshot_rows=1,
    )

    assert output.updated_rounds == []
    assert not (weekly / "runs" / "official" / "results" / "weekly_performance.csv").exists()
    assert any(item.round_id == "weekly-round" and item.message == "not a monthly round" for item in output.skipped_rounds)


def test_update_interim_performance_track_all_includes_weekly_rounds(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    weekly = _create_round(
        rounds_dir,
        "weekly-round",
        entry_date="2026-01-02",
        exit_date="2026-01-09",
        horizon="one week",
    )
    monthly = _create_round(rounds_dir, "monthly-round", entry_date="2026-01-02", exit_date="2026-02-02")
    snapshots_dir = tmp_path / "snapshots"
    _write_prices(
        snapshots_dir / "2026-01-06.csv",
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "opt_b", "price": 97, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-06", "source": "cash"},
        ],
    )

    output = update_interim_performance(
        rounds_dir=rounds_dir,
        snapshot_date="2026-01-06",
        snapshots_dir=snapshots_dir,
        track="all",
        skip_fetch=True,
        sync=False,
        min_snapshot_rows=1,
    )

    assert {item.round_id for item in output.updated_rounds} == {"weekly-round", "monthly-round"}
    assert (weekly / "runs" / "official" / "results" / "weekly_performance.csv").exists()
    assert (monthly / "runs" / "official" / "results" / "weekly_performance.csv").exists()


def test_update_interim_performance_weekly_track_skips_monthly_rounds(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    weekly = _create_round(
        rounds_dir,
        "weekly-round",
        entry_date="2026-01-02",
        exit_date="2026-01-09",
        horizon="one week",
    )
    monthly = _create_round(rounds_dir, "monthly-round", entry_date="2026-01-02", exit_date="2026-02-02")
    snapshots_dir = tmp_path / "snapshots"
    _write_prices(
        snapshots_dir / "2026-01-06.csv",
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "opt_b", "price": 97, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-06", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-06", "source": "cash"},
        ],
    )

    output = update_interim_performance(
        rounds_dir=rounds_dir,
        snapshot_date="2026-01-06",
        snapshots_dir=snapshots_dir,
        track="weekly",
        skip_fetch=True,
        sync=False,
        min_snapshot_rows=1,
    )

    assert {item.round_id for item in output.updated_rounds} == {"weekly-round"}
    assert (weekly / "runs" / "official" / "results" / "weekly_performance.csv").exists()
    assert not (monthly / "runs" / "official" / "results" / "weekly_performance.csv").exists()
    assert any(item.round_id == "monthly-round" and item.message == "not a weekly round" for item in output.skipped_rounds)


def test_update_interim_performance_keeps_sync_failure_as_round_warning(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(rounds_dir, "round-one", entry_date="2026-01-02", exit_date="2026-02-02")
    snapshots_dir = tmp_path / "snapshots"
    _write_prices(
        snapshots_dir / "2026-01-09.csv",
        [
            {"option_id": "opt_a", "price": 110, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "sp500", "price": 105, "date": "2026-01-09", "source": "fixture"},
            {"option_id": "cash", "price": 1, "date": "2026-01-09", "source": "cash"},
        ],
    )

    def fail_sync(_round_path: Path, _run_id: str) -> None:
        raise RuntimeError("hash mismatch")

    output = update_interim_performance(
        rounds_dir=rounds_dir,
        snapshot_date="2026-01-09",
        snapshots_dir=snapshots_dir,
        skip_fetch=True,
        sync=True,
        sync_func=fail_sync,
        min_snapshot_rows=1,
    )

    assert len(output.updated_rounds) == 1
    updated = output.updated_rounds[0]
    assert updated.sync_status == "failed"
    assert updated.sync_message == "hash mismatch"
    assert "Supabase sync failed" in updated.message

import csv
import json
from pathlib import Path

import yaml

from capitalbench.experiments import evaluate_experiment
from capitalbench.hashing import write_round_hashes


MODELS = ["model-a", "model-b"]
CUTOFF = "2026-07-13T20:55:45Z"


def _write_yaml(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _create_round(rounds_dir: Path, round_id: str, *, methodology: str, stream: str) -> Path:
    round_path = rounds_dir / round_id
    _write_yaml(
        round_path / "manifest.yaml",
        {
            "round_id": round_id,
            "title": round_id,
            "decision_date": "2026-07-13",
            "decision_deadline": "2026-07-14T07:30:00Z",
            "horizon": "one week",
            "methodology_version": methodology,
            "publication_stream": stream,
            "submission_format": "portfolio",
            "entry_date": "2026-07-13",
            "exit_date": "2026-07-20",
        },
    )
    _write_yaml(
        round_path / "options.yaml",
        {
            "options": [
                {
                    "id": "ASSET_A",
                    "name": "Asset A",
                    "symbol": "AAA",
                    "tiingo_symbol": "AAA",
                    "asset_class": "equity",
                    "category": "test",
                    "option_group": "group-a",
                    "risk_bucket": "high",
                    "exposure_description": "Asset A exposure.",
                },
                {
                    "id": "ASSET_B",
                    "name": "Asset B",
                    "symbol": "BBB",
                    "tiingo_symbol": "BBB",
                    "asset_class": "equity",
                    "category": "test",
                    "option_group": "group-b",
                    "risk_bucket": "medium",
                    "exposure_description": "Asset B exposure.",
                },
            ]
        },
    )
    _write_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "ASSET_A", "price": 100},
            {"option_id": "ASSET_B", "price": 100},
        ],
    )
    (round_path / "briefing.md").write_text("Frozen briefing.\n", encoding="utf-8")
    (round_path / "prompt.md").write_text("Frozen prompt.\n", encoding="utf-8")
    _write_yaml(round_path / "research" / "research_manifest.yaml", {"research_cutoff_utc": CUTOFF})
    return round_path


def _create_run(
    round_path: Path,
    run_id: str,
    *,
    returns: dict[str, float],
    sp500_return: float,
    v2: bool,
) -> None:
    run_path = round_path / "runs" / run_id
    _write_yaml(
        run_path / "run_manifest.yaml",
        {
            "run_id": run_id,
            "round_id": round_path.name,
            "run_type": "official",
            "mock": False,
            "valid_submissions": len(MODELS),
            "invalid_submissions": 0,
            "operator_selected_official": True,
        },
    )
    leaderboard = []
    for model_id, portfolio_return in returns.items():
        leaderboard.append(
            {
                "model_id": model_id,
                "portfolio_return": portfolio_return,
                "sp500_return": sp500_return,
                "alpha_vs_sp500": portfolio_return - sp500_return,
                "beats_sp500": portfolio_return > sp500_return,
            }
        )
        submission: dict[str, object] = {
            "model_id": model_id,
            "portfolio": [{"option_id": "ASSET_A", "allocation_pct": 100}],
        }
        if v2:
            submission.update(
                {
                    "benchmark_expected_return_pct": 1.0,
                    "portfolio_expected_return_pct": 2.5,
                    "expected_alpha_vs_sp500_pct": 1.5,
                }
            )
        _write_json(run_path / "submissions" / "parsed" / f"{model_id}.json", submission)
    _write_csv(run_path / "results" / "leaderboard.csv", leaderboard)


def test_evaluate_experiment_applies_frozen_paired_gates(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    v1_round = _create_round(rounds_dir, "V1", methodology="portfolio-v1.0", stream="primary")
    v2_round = _create_round(rounds_dir, "V2", methodology="portfolio-v2.0-pilot", stream="pilot")
    _create_run(v1_round, "official-v1", returns={"model-a": 0.0, "model-b": 0.005}, sp500_return=0.01, v2=False)
    _create_run(v2_round, "official-v2", returns={"model-a": 0.02, "model-b": 0.03}, sp500_return=0.01, v2=True)
    _write_json(
        v2_round / "market_data" / "universe_decision_context.json",
        {
            "rows": [
                {"option_id": "ASSET_A", "status": "pass", "return_5s": 0.05},
                {"option_id": "ASSET_B", "status": "pass", "return_5s": -0.02},
            ]
        },
    )
    _write_json(
        v2_round / "market_data" / "decision_context_source_history.json",
        {"options": [{"option_id": "ASSET_A", "rows": [{"date": "2026-07-13"}]}]},
    )
    write_round_hashes(v2_round)
    config_path = tmp_path / "experiment.yaml"
    _write_yaml(
        config_path,
        {
            "experiment_id": "portfolio-v2-test",
            "paired_v1_round_id": "V1",
            "paired_v1_run_id": "official-v1",
            "v2_round_id": "V2",
            "v2_run_id": "official-v2",
            "research_cutoff_utc": CUTOFF,
            "models": MODELS,
            "acceptance_rule": {"minimum_models_improved": 2},
        },
    )

    output = evaluate_experiment(config_path=config_path, rounds_dir=rounds_dir)

    assert output.decision == "accepted"
    report = json.loads(output.json_path.read_text(encoding="utf-8"))
    assert all(report["gates"].values())
    assert report["summary"]["models_improved"] == 2
    assert report["summary"]["v2_beat_sp500_count"] == 2
    assert report["diagnostics"]["v2_average_recent_winner_allocation"] == 1.0
    assert output.markdown_path.exists()

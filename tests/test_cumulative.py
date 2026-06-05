import csv
import math
from pathlib import Path

import pytest
import yaml

from capitalbench.cli import main
from capitalbench.cumulative import publish_cumulative, publish_latest


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _create_round(
    rounds_dir: Path,
    round_id: str,
    *,
    official_run_id: str = "official",
    stability_run_id: str = "stability",
    model_alpha: float,
    model_return: float,
    sp500_return: float,
    beats_sp500: bool,
    beats_cash: bool,
    stability_alpha: float,
    stability_return: float,
    consistency: float,
    modal_alpha: float,
    modal_return: float,
    best_replicate: float,
    worst_replicate: float,
    valid_replicates: int = 5,
    include_results: bool = True,
    mock: bool = False,
    official_run_type: str = "official",
    stability_run_type: str = "stability",
    official_score_eligible: bool = True,
    decision_deadline: str = "2026-01-01T20:00:00Z",
    entry_date: str = "2026-01-02",
    exit_date: str = "2026-02-02",
    horizon: str = "one month",
) -> Path:
    round_path = rounds_dir / round_id
    round_path.mkdir(parents=True)
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": round_id,
                "title": round_id,
                "decision_deadline": decision_deadline,
                "entry_date": entry_date,
                "exit_date": exit_date,
                "horizon": horizon,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    official_path = round_path / "runs" / official_run_id
    stability_path = round_path / "runs" / stability_run_id
    official_path.mkdir(parents=True)
    stability_path.mkdir(parents=True)
    (official_path / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": official_run_id,
                "round_id": round_id,
                "run_type": official_run_type,
                "mode": "closed_capability",
                "replicates": 1,
                "mock": mock,
                "official_score_eligible": official_score_eligible,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (stability_path / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": stability_run_id,
                "round_id": round_id,
                "run_type": stability_run_type,
                "mode": "closed_capability",
                "replicates": valid_replicates,
                "mock": mock,
                "official_score_eligible": False,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    if include_results:
        _write_csv(
            official_path / "results" / "leaderboard.csv",
            [
                "round_id",
                "model_id",
                "provider",
                "mode",
                "selected_option_id",
                "confidence",
                "rationale_summary",
                "key_risks",
                "selected_asset_return",
                "sp500_return",
                "alpha_vs_sp500",
                "regret_vs_best_option",
                "rank_among_options",
                "beats_sp500",
                "beats_cash",
                "cost_usd",
                "alpha_per_dollar",
            ],
            [
                {
                    "round_id": round_id,
                    "model_id": "model-a",
                    "provider": "openai",
                    "mode": "closed_capability",
                    "selected_option_id": "SP500",
                    "confidence": 0.5,
                    "rationale_summary": "test",
                    "key_risks": "risk",
                    "selected_asset_return": model_return,
                    "sp500_return": sp500_return,
                    "alpha_vs_sp500": model_alpha,
                    "regret_vs_best_option": 0.03,
                    "rank_among_options": 1,
                    "beats_sp500": beats_sp500,
                    "beats_cash": beats_cash,
                    "cost_usd": 0.10,
                    "alpha_per_dollar": "",
                }
            ],
        )
        _write_csv(
            stability_path / "results" / "stability.csv",
            [
                "model_id",
                "provider",
                "replicate_count",
                "valid_replicates",
                "invalid_replicates",
                "selected_option_ids",
                "pick_distribution",
                "modal_pick",
                "modal_pick_count",
                "consistency_rate",
                "average_repeated_return",
                "average_repeated_alpha_vs_sp500",
                "best_replicate_return",
                "worst_replicate_return",
                "best_replicate_option_id",
                "worst_replicate_option_id",
                "modal_pick_return",
                "modal_pick_alpha_vs_sp500",
                "total_cost_usd",
                "average_cost_usd",
                "notes",
            ],
            [
                {
                    "model_id": "model-a",
                    "provider": "openai",
                    "replicate_count": valid_replicates,
                    "valid_replicates": valid_replicates,
                    "invalid_replicates": 0,
                    "selected_option_ids": "[]",
                    "pick_distribution": "{}",
                    "modal_pick": "SP500",
                    "modal_pick_count": int(consistency * valid_replicates),
                    "consistency_rate": consistency,
                    "average_repeated_return": stability_return,
                    "average_repeated_alpha_vs_sp500": stability_alpha,
                    "best_replicate_return": best_replicate,
                    "worst_replicate_return": worst_replicate,
                    "best_replicate_option_id": "BEST",
                    "worst_replicate_option_id": "WORST",
                    "modal_pick_return": modal_return,
                    "modal_pick_alpha_vs_sp500": modal_alpha,
                    "total_cost_usd": 0.50,
                    "average_cost_usd": 0.10,
                    "notes": "",
                }
            ],
        )
    return round_path


def test_publish_cumulative_creates_outputs_and_calculates_official_metrics(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    _create_round(
        rounds_dir,
        "round-2",
        model_alpha=-0.01,
        model_return=0.01,
        sp500_return=0.02,
        beats_sp500=False,
        beats_cash=True,
        stability_alpha=0.008,
        stability_return=0.028,
        consistency=0.8,
        modal_alpha=0.012,
        modal_return=0.032,
        best_replicate=0.05,
        worst_replicate=0.0,
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")

    official_rows = _read_csv(output.official_leaderboard_path)
    stability_rows = _read_csv(output.stability_leaderboard_path)
    round_index_rows = _read_csv(output.round_index_path)
    assert output.cumulative_report_path.exists()
    assert output.round_index_path.exists()
    assert len(official_rows) == 1
    official = official_rows[0]
    assert math.isclose(float(official["average_alpha_vs_sp500"]), 0.005)
    assert math.isclose(float(official["hit_rate_vs_sp500"]), 0.5)
    assert math.isclose(float(official["cumulative_model_return"]), (1.05 * 1.01) - 1)
    expected_log_alpha = math.log(1.05) - math.log(1.03) + math.log(1.01) - math.log(1.02)
    assert math.isclose(float(official["cumulative_log_alpha"]), expected_log_alpha)
    assert len(stability_rows) == 1
    assert {row["round_id"]: row["included_in_latest"] for row in round_index_rows} == {
        "round-1": "no",
        "round-2": "yes",
    }


def test_publish_cumulative_calculates_stability_metrics(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    _create_round(
        rounds_dir,
        "round-2",
        model_alpha=-0.01,
        model_return=0.01,
        sp500_return=0.02,
        beats_sp500=False,
        beats_cash=True,
        stability_alpha=0.008,
        stability_return=0.028,
        consistency=0.8,
        modal_alpha=0.012,
        modal_return=0.032,
        best_replicate=0.05,
        worst_replicate=0.0,
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")
    stability = _read_csv(output.stability_leaderboard_path)[0]

    assert stability["total_replicates"] == "10"
    assert math.isclose(float(stability["average_repeated_alpha_vs_sp500"]), 0.011)
    assert math.isclose(float(stability["average_consistency_rate"]), 0.7)
    assert math.isclose(float(stability["average_modal_pick_alpha_vs_sp500"]), 0.011)


def test_round_with_multiple_official_runs_is_skipped_without_selection(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    round_path = _create_round(
        rounds_dir,
        "round-1",
        official_run_id="official-a",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    second = round_path / "runs" / "official-b"
    second.mkdir(parents=True)
    (second / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "official-b",
                "round_id": "round-1",
                "run_type": "official",
                "official_score_eligible": True,
                "replicates": 1,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_csv(second / "results" / "leaderboard.csv", list(_read_csv(round_path / "runs" / "official-a" / "results" / "leaderboard.csv")[0].keys()), _read_csv(round_path / "runs" / "official-a" / "results" / "leaderboard.csv"))

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")

    assert _read_csv(output.official_leaderboard_path) == []
    assert "multiple official eligible runs" in output.status.warnings[0]


def test_selection_file_chooses_exact_runs(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    round_path = _create_round(
        rounds_dir,
        "round-1",
        official_run_id="official-a",
        stability_run_id="stability-a",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    duplicate = round_path / "runs" / "official-b"
    duplicate.mkdir(parents=True)
    (duplicate / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "official-b",
                "round_id": "round-1",
                "run_type": "official",
                "official_score_eligible": True,
                "replicates": 1,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_csv(duplicate / "results" / "leaderboard.csv", list(_read_csv(round_path / "runs" / "official-a" / "results" / "leaderboard.csv")[0].keys()), _read_csv(round_path / "runs" / "official-a" / "results" / "leaderboard.csv"))
    selection_path = tmp_path / "selection.yaml"
    selection_path.write_text(
        yaml.safe_dump(
            {
                "rounds": {
                    "round-1": {
                        "official_run_id": "official-a",
                        "stability_run_id": "stability-a",
                    }
                }
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative", selection_path=selection_path)

    assert len(_read_csv(output.official_leaderboard_path)) == 1
    assert len(_read_csv(output.stability_leaderboard_path)) == 1


def test_invalid_selection_fails_clearly(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    selection_path = tmp_path / "selection.yaml"
    selection_path.write_text(
        yaml.safe_dump(
            {"rounds": {"round-1": {"official_run_id": "missing", "stability_run_id": "stability"}}},
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    with pytest.raises(FileNotFoundError, match="selected run does not exist"):
        publish_cumulative(rounds_dir, tmp_path / "cumulative", selection_path=selection_path)


def test_unresolved_round_is_skipped_and_round_index_is_created(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
        include_results=False,
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")

    assert output.round_index_path.exists()
    assert _read_csv(output.round_index_path) == []
    assert "no scored official or stability runs" in output.status.skipped_rounds["round-1"][0]


def test_cumulative_report_says_no_combined_weighted_score(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")
    report = output.cumulative_report_path.read_text(encoding="utf-8")

    assert "there is no combined weighted score" in report
    assert "qualified leaderboard" not in report.lower()
    assert "maturity" not in report.lower()


def test_retrospective_run_is_excluded_from_cumulative_leaderboards(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        official_run_type="retrospective",
        official_score_eligible=False,
        stability_run_type="retrospective",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")

    assert _read_csv(output.official_leaderboard_path) == []
    assert _read_csv(output.stability_leaderboard_path) == []


def test_mock_runs_are_excluded_from_public_cumulative_leaderboards(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        mock=True,
        official_score_eligible=True,
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")

    assert _read_csv(output.official_leaderboard_path) == []
    assert _read_csv(output.stability_leaderboard_path) == []


def test_publish_latest_excludes_mock_official_runs(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        mock=True,
        official_score_eligible=True,
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )

    with pytest.raises(ValueError, match="no resolved official rounds found"):
        publish_latest(rounds_dir, tmp_path / "latest")


def test_publish_latest_selects_newest_resolved_round(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    round_2 = _create_round(
        rounds_dir,
        "round-2",
        model_alpha=-0.01,
        model_return=0.01,
        sp500_return=0.02,
        beats_sp500=False,
        beats_cash=True,
        stability_alpha=0.008,
        stability_return=0.028,
        consistency=0.8,
        modal_alpha=0.012,
        modal_return=0.032,
        best_replicate=0.05,
        worst_replicate=0.0,
    )
    manifest = yaml.safe_load((round_2 / "manifest.yaml").read_text(encoding="utf-8"))
    manifest["decision_deadline"] = "2026-03-01T20:00:00Z"
    (round_2 / "manifest.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    output = publish_latest(rounds_dir, tmp_path / "latest")

    assert output.selected_round.round_id == "round-2"
    assert output.latest_leaderboard_path.exists()
    assert output.latest_report_path.exists()


def test_publish_latest_uses_scoring_end_date_before_decision_deadline(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-later-decision-earlier-end",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
        decision_deadline="2026-03-01T20:00:00Z",
        entry_date="2026-03-02",
        exit_date="2026-03-09",
        horizon="one week",
    )
    _create_round(
        rounds_dir,
        "round-earlier-decision-later-end",
        model_alpha=-0.01,
        model_return=0.01,
        sp500_return=0.02,
        beats_sp500=False,
        beats_cash=True,
        stability_alpha=0.008,
        stability_return=0.028,
        consistency=0.8,
        modal_alpha=0.012,
        modal_return=0.032,
        best_replicate=0.05,
        worst_replicate=0.0,
        decision_deadline="2026-02-01T20:00:00Z",
        entry_date="2026-03-10",
        exit_date="2026-03-17",
        horizon="one week",
    )

    output = publish_latest(rounds_dir, tmp_path / "latest")

    assert output.selected_round.round_id == "round-earlier-decision-later-end"


def test_publish_latest_and_cumulative_can_filter_by_track(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "CB-2026-01-01-1W",
        model_alpha=0.07,
        model_return=0.08,
        sp500_return=0.01,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.02,
        stability_return=0.03,
        consistency=0.6,
        modal_alpha=0.02,
        modal_return=0.03,
        best_replicate=0.08,
        worst_replicate=-0.01,
        entry_date="2026-01-02",
        exit_date="2026-01-09",
        horizon="one week",
    )
    _create_round(
        rounds_dir,
        "CB-2026-01-01-1M",
        model_alpha=-0.02,
        model_return=0.00,
        sp500_return=0.02,
        beats_sp500=False,
        beats_cash=False,
        stability_alpha=-0.01,
        stability_return=0.01,
        consistency=0.8,
        modal_alpha=-0.01,
        modal_return=0.01,
        best_replicate=0.04,
        worst_replicate=-0.03,
    )

    weekly_latest = publish_latest(rounds_dir, tmp_path / "latest-weekly", track="weekly")
    monthly_latest = publish_latest(rounds_dir, tmp_path / "latest-monthly", track="monthly")
    weekly_cumulative = publish_cumulative(rounds_dir, tmp_path / "cumulative-weekly", track="weekly")
    monthly_cumulative = publish_cumulative(rounds_dir, tmp_path / "cumulative-monthly", track="monthly")

    assert weekly_latest.selected_round.round_id == "CB-2026-01-01-1W"
    assert monthly_latest.selected_round.round_id == "CB-2026-01-01-1M"
    assert _read_csv(weekly_cumulative.official_leaderboard_path)[0]["rounds_included"] == "CB-2026-01-01-1W"
    assert _read_csv(monthly_cumulative.official_leaderboard_path)[0]["rounds_included"] == "CB-2026-01-01-1M"


def test_publish_latest_fails_with_multiple_official_runs_without_selection(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    round_path = _create_round(
        rounds_dir,
        "round-1",
        official_run_id="official-a",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    second = round_path / "runs" / "official-b"
    second.mkdir(parents=True)
    (second / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "official-b",
                "round_id": "round-1",
                "run_type": "official",
                "replicates": 1,
                "official_score_eligible": True,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    source_rows = _read_csv(round_path / "runs" / "official-a" / "results" / "leaderboard.csv")
    _write_csv(second / "results" / "leaderboard.csv", list(source_rows[0].keys()), source_rows)

    with pytest.raises(ValueError, match="multiple official-score-eligible runs"):
        publish_latest(rounds_dir, tmp_path / "latest")


def test_cumulative_does_not_penalize_models_missing_older_rounds(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )
    round_2 = _create_round(
        rounds_dir,
        "round-2",
        model_alpha=0.01,
        model_return=0.04,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.009,
        stability_return=0.039,
        consistency=0.8,
        modal_alpha=0.009,
        modal_return=0.039,
        best_replicate=0.06,
        worst_replicate=0.01,
    )
    leaderboard_path = round_2 / "runs" / "official" / "results" / "leaderboard.csv"
    rows = _read_csv(leaderboard_path)
    new_model = {**rows[0], "model_id": "model-b", "alpha_vs_sp500": "0.03", "selected_asset_return": "0.06"}
    _write_csv(leaderboard_path, list(rows[0].keys()), rows + [new_model])
    stability_path = round_2 / "runs" / "stability" / "results" / "stability.csv"
    stability_rows = _read_csv(stability_path)
    new_stability = {
        **stability_rows[0],
        "model_id": "model-b",
        "average_repeated_alpha_vs_sp500": "0.025",
        "average_repeated_return": "0.055",
        "valid_replicates": "5",
    }
    _write_csv(stability_path, list(stability_rows[0].keys()), stability_rows + [new_stability])

    output = publish_cumulative(rounds_dir, tmp_path / "cumulative")
    official = {row["model_id"]: row for row in _read_csv(output.official_leaderboard_path)}
    stability = {row["model_id"]: row for row in _read_csv(output.stability_leaderboard_path)}

    assert official["model-a"]["resolved_rounds"] == "2"
    assert official["model-b"]["resolved_rounds"] == "1"
    assert stability["model-a"]["resolved_rounds"] == "2"
    assert stability["model-b"]["resolved_rounds"] == "1"


def test_publish_cumulative_cli_creates_outputs(tmp_path: Path) -> None:
    rounds_dir = tmp_path / "rounds"
    output_dir = tmp_path / "cumulative"
    _create_round(
        rounds_dir,
        "round-1",
        model_alpha=0.02,
        model_return=0.05,
        sp500_return=0.03,
        beats_sp500=True,
        beats_cash=True,
        stability_alpha=0.014,
        stability_return=0.044,
        consistency=0.6,
        modal_alpha=0.01,
        modal_return=0.04,
        best_replicate=0.08,
        worst_replicate=-0.01,
    )

    exit_code = main(["publish-cumulative", "--rounds-dir", str(rounds_dir), "--output", str(output_dir)])

    assert exit_code == 0
    assert (output_dir / "official_leaderboard.csv").exists()
    assert (output_dir / "stability_leaderboard.csv").exists()
    assert (output_dir / "cumulative_report.md").exists()
    assert (output_dir / "round_index.csv").exists()

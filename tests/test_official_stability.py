import csv
import json
import math
from pathlib import Path
from shutil import copytree

import pytest
import yaml

from capitalbench.audit import audit_round
from capitalbench.cli import main
from capitalbench.report import publish_report, publish_round_summary
from capitalbench.runner import run_round
from capitalbench.scoring import score_round
from capitalbench.validation import validate_submissions


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROUND = PROJECT_ROOT / "rounds" / "example-round"
MODELS_EXAMPLE = PROJECT_ROOT / "configs" / "models.example.yaml"


def _copy_example_round(tmp_path: Path) -> Path:
    target = tmp_path / "example-round"
    copytree(EXAMPLE_ROUND, target)
    return target


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_official_run_creates_one_submission_per_model(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)

    summary = run_round(
        round_path,
        MODELS_EXAMPLE,
        mock=True,
        run_id="official-test",
        run_type="official",
    )

    run_path = round_path / "runs" / "official-test"
    raw_files = sorted((run_path / "submissions" / "raw").glob("*.json"))
    parsed_files = sorted((run_path / "submissions" / "parsed").glob("*.json"))
    manifest = yaml.safe_load((run_path / "run_manifest.yaml").read_text(encoding="utf-8"))

    assert summary.attempted_models == 4
    assert len(raw_files) == 4
    assert len(parsed_files) == 4
    assert all("__replicate_" not in path.name for path in raw_files)
    assert manifest["run_type"] == "official"
    assert manifest["replicates"] == 1
    assert manifest["official_score_eligible"] is False


def test_official_run_rejects_replicates_greater_than_one(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)

    with pytest.raises(ValueError, match="official runs require exactly one replicate"):
        run_round(
            round_path,
            MODELS_EXAMPLE,
            mock=True,
            run_id="bad-official",
            run_type="official",
            replicates=2,
        )


def test_stability_run_creates_replicate_submissions_without_overwrite(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)

    summary = run_round(
        round_path,
        MODELS_EXAMPLE,
        mock=True,
        run_id="stability-test",
        run_type="stability",
        replicates=5,
    )

    run_path = round_path / "runs" / "stability-test"
    raw_files = sorted((run_path / "submissions" / "raw").glob("*.json"))
    parsed_files = sorted((run_path / "submissions" / "parsed").glob("*.json"))

    assert summary.attempted_models == 20
    assert len(raw_files) == 20
    assert len(parsed_files) == 20
    assert (run_path / "submissions" / "raw" / "openai-example__replicate_001.json").exists()
    assert (run_path / "submissions" / "raw" / "openai-example__replicate_005.json").exists()


def test_duplicate_model_id_rejected_for_official_runs(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="official-dupe", run_type="official")
    raw_dir = round_path / "runs" / "official-dupe" / "submissions" / "raw"
    duplicate = json.loads((raw_dir / "openai-example.json").read_text(encoding="utf-8"))
    (raw_dir / "openai-example-copy.json").write_text(json.dumps(duplicate), encoding="utf-8")

    summary = validate_submissions(round_path, run_id="official-dupe")

    assert summary.invalid_count == 1
    assert any("duplicate model_id" in errors[0] for errors in summary.errors.values())


def test_duplicate_model_id_allowed_for_stability_when_replicate_index_is_unique(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="stability-valid", run_type="stability", replicates=2)

    summary = validate_submissions(round_path, run_id="stability-valid")

    assert summary.valid_count == 8
    assert summary.invalid_count == 0


def test_duplicate_replicate_index_rejected_for_stability_runs(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="stability-dupe", run_type="stability", replicates=2)
    raw_dir = round_path / "runs" / "stability-dupe" / "submissions" / "raw"
    duplicate = json.loads((raw_dir / "openai-example__replicate_001.json").read_text(encoding="utf-8"))
    (raw_dir / "openai-example__replicate_001_copy.json").write_text(json.dumps(duplicate), encoding="utf-8")

    summary = validate_submissions(round_path, run_id="stability-dupe")

    assert summary.invalid_count == 1
    assert "duplicate replicate_index" in summary.errors["openai-example__replicate_001_copy.json"][0]


def _write_price_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["option_id", "price"])
        writer.writeheader()
        writer.writerows(rows)


def _create_stability_round(
    tmp_path: Path,
    *,
    replicate_count: int,
    picks_by_model: dict[str, list[str]],
) -> Path:
    round_path = tmp_path / "round"
    (round_path / "runs" / "stability" / "submissions" / "raw").mkdir(parents=True)
    parsed_dir = round_path / "runs" / "stability" / "submissions" / "parsed"
    parsed_dir.mkdir(parents=True)
    (round_path / "runs" / "stability" / "results").mkdir(parents=True)
    (round_path / "runs" / "stability" / "run_manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "run_id": "stability",
                "round_id": "test",
                "run_type": "stability",
                "mode": "closed_capability",
                "created_at_utc": "2026-01-01T00:00:00Z",
                "replicates": replicate_count,
                "mock": True,
                "official_score_eligible": False,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "test",
                "title": "Test Round",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_rule": "Use entry.",
                "exit_rule": "Use exit.",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (round_path / "briefing.md").write_text("briefing", encoding="utf-8")
    (round_path / "prompt.md").write_text("prompt", encoding="utf-8")
    (round_path / "hashes.json").write_text("{}", encoding="utf-8")
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
    _write_price_csv(
        round_path / "prices" / "entry_prices.csv",
        [
            {"option_id": "opt_a", "price": 100},
            {"option_id": "opt_b", "price": 100},
            {"option_id": "sp500", "price": 100},
            {"option_id": "cash", "price": 1},
        ],
    )
    _write_price_csv(
        round_path / "prices" / "exit_prices.csv",
        [
            {"option_id": "opt_a", "price": 110},
            {"option_id": "opt_b", "price": 120},
            {"option_id": "sp500", "price": 105},
            {"option_id": "cash", "price": 1},
        ],
    )
    for model_id, picks in picks_by_model.items():
        for index, pick in enumerate(picks, start=1):
            payload = {
                "round_id": "test",
                "model_id": model_id,
                "provider": "openai",
                "mode": "closed_capability",
                "run_type": "stability",
                "replicate_index": index,
                "replicate_count": replicate_count,
                "is_official_score": False,
                "selected_option_id": pick,
                "confidence": 0.5,
                "rationale_summary": "Repeated choice.",
                "key_risks": ["Risk"],
            }
            filename = f"{model_id}__replicate_{index:03d}.json"
            (parsed_dir / filename).write_text(json.dumps(payload), encoding="utf-8")
    return round_path


def test_stability_csv_calculations(tmp_path: Path) -> None:
    round_path = _create_stability_round(
        tmp_path,
        replicate_count=5,
        picks_by_model={"model-a": ["opt_a", "opt_a", "sp500", "opt_a", "opt_b"]},
    )

    score_round(round_path, run_id="stability")
    rows = _read_csv(round_path / "runs" / "stability" / "results" / "stability.csv")
    row = rows[0]

    assert row["modal_pick"] == "opt_a"
    assert row["modal_pick_count"] == "3"
    assert math.isclose(float(row["consistency_rate"]), 0.6)
    assert math.isclose(float(row["average_repeated_return"]), 0.11)
    assert math.isclose(float(row["average_repeated_alpha_vs_sp500"]), 0.06)
    assert row["best_replicate_option_id"] == "opt_b"
    assert math.isclose(float(row["best_replicate_return"]), 0.2)
    assert row["worst_replicate_option_id"] == "sp500"
    assert math.isclose(float(row["worst_replicate_return"]), 0.05)
    assert math.isclose(float(row["modal_pick_return"]), 0.1)
    assert math.isclose(float(row["modal_pick_alpha_vs_sp500"]), 0.05)
    assert (round_path / "runs" / "stability" / "results" / "returns.csv").exists()


def test_modal_pick_tie_resolved_by_highest_realized_return(tmp_path: Path) -> None:
    round_path = _create_stability_round(
        tmp_path,
        replicate_count=4,
        picks_by_model={"model-tie": ["opt_a", "opt_b", "opt_a", "opt_b"]},
    )

    score_round(round_path, run_id="stability")
    row = _read_csv(round_path / "runs" / "stability" / "results" / "stability.csv")[0]

    assert row["modal_pick"] == "opt_b"
    assert "tie resolved" in row["notes"]


def test_publish_report_labels_official_and_stability_modes(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="official-report", run_type="official")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="stability-report", run_type="stability", replicates=2)
    score_round(round_path, run_id="official-report")
    score_round(round_path, run_id="stability-report")

    official_report = publish_report(round_path, run_id="official-report").read_text(encoding="utf-8")
    stability_report = publish_report(round_path, run_id="stability-report").read_text(encoding="utf-8")

    assert "Official Public Leaderboard" in official_report
    assert "This is the official CapitalBench score for this run." in official_report
    assert "Multi-Run Stability Analysis" in stability_report
    assert "This is not the official leaderboard" in stability_report


def test_publish_round_summary_includes_official_and_stability_sections(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="official-summary", run_type="official")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="stability-summary", run_type="stability", replicates=2)
    score_round(round_path, run_id="official-summary")
    score_round(round_path, run_id="stability-summary")

    summary_path = publish_round_summary(round_path, "official-summary", "stability-summary")
    summary = summary_path.read_text(encoding="utf-8")

    assert "Official Public Leaderboard" in summary
    assert "Multi-Run Stability Analysis" in summary
    assert "does not create a combined weighted score" in summary


def test_audit_warns_when_multiple_official_eligible_runs_exist(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="official-one", run_type="official")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="official-two", run_type="official")
    for run_id in ["official-one", "official-two"]:
        manifest_path = round_path / "runs" / run_id / "run_manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        manifest["mock"] = False
        manifest["official_score_eligible"] = True
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    audit = audit_round(round_path)

    assert any("multiple official-score-eligible runs" in line for line in audit.lines)


def test_list_runs_includes_run_type_and_official_score_eligible(tmp_path: Path, capsys) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="official-list", run_type="official")

    exit_code = main(["list-runs", "--round", str(round_path)])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "run_type" in output
    assert "official_score_eligible" in output
    assert "official-list\tofficial\t1" in output

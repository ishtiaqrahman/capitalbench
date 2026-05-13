import json
from pathlib import Path

import yaml

from capitalbench.schemas import MarketOption
from capitalbench.validation import validate_submissions


def _write_round_base(round_path: Path) -> None:
    (round_path / "submissions" / "raw").mkdir(parents=True)
    (round_path / "submissions" / "parsed").mkdir(parents=True)
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump({"round_id": "round-a", "title": "Round A"}),
        encoding="utf-8",
    )


def _valid_payload() -> dict[str, object]:
    return {
        "round_id": "round-a",
        "model_id": "model-a",
        "provider": "openai",
        "mode": "closed_capability",
        "selected_option_id": "sp500",
        "confidence": 0.6,
        "rationale_summary": "Valid rationale.",
        "key_risks": ["Risk one"],
    }


def _valid_portfolio_payload() -> dict[str, object]:
    return {
        "round_id": "round-a",
        "model_id": "model-a",
        "provider": "openai",
        "mode": "closed_capability",
        "portfolio": [
            {"option_id": "sp500", "allocation_pct": 60, "rationale": "Benchmark exposure."},
            {"option_id": "cash", "allocation_pct": 40, "rationale": "Defensive exposure."},
        ],
        "confidence": 0.6,
        "portfolio_rationale": "A balanced benchmark and cash portfolio.",
        "rationale_summary": "Valid portfolio rationale.",
        "key_risks": ["Risk one"],
    }


def _options() -> list[MarketOption]:
    return [
        MarketOption(option_id="sp500", label="S&P 500", asset_symbol="SPY", is_benchmark=True),
        MarketOption(option_id="cash", label="Cash", asset_symbol="USD", is_cash=True),
    ]


def test_invalid_selected_option_rejection(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    raw_dir = round_path / "submissions" / "raw"

    payload = _valid_payload()
    payload["selected_option_id"] = "not-an-option"
    (raw_dir / "bad.json").write_text(
        json.dumps(payload),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.valid_count == 0
    assert summary.invalid_count == 1
    assert "bad.json" in summary.errors
    assert not (round_path / "submissions" / "parsed" / "bad.json").exists()
    assert (raw_dir / "bad.json").exists()


def test_invalid_round_id_rejection(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    payload = _valid_payload()
    payload["round_id"] = "wrong-round"
    (round_path / "submissions" / "raw" / "bad-round.json").write_text(
        json.dumps(payload),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "round_id does not match" in summary.errors["bad-round.json"][0]


def test_invalid_provider_rejection(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    payload = _valid_payload()
    payload["provider"] = "manual"
    (round_path / "submissions" / "raw" / "bad-provider.json").write_text(
        json.dumps(payload),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "provider" in summary.errors["bad-provider.json"][0]


def test_malformed_json_rejection(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    raw_file = round_path / "submissions" / "raw" / "malformed.json"
    raw_file.write_text('{"round_id": "round-a",', encoding="utf-8")

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "malformed JSON" in summary.errors["malformed.json"][0]
    assert raw_file.exists()


def test_portfolio_submission_validates_against_round_constraints(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
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
    (round_path / "submissions" / "raw" / "portfolio.json").write_text(
        json.dumps(_valid_portfolio_payload()),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.valid_count == 1
    parsed = json.loads((round_path / "runs" / "legacy-run" / "submissions" / "parsed" / "portfolio.json").read_text(encoding="utf-8"))
    assert parsed["portfolio"][0]["allocation_pct"] == 60


def test_portfolio_submission_rejects_invalid_allocation_sum(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["submission_format"] = "portfolio"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    payload = _valid_portfolio_payload()
    payload["portfolio"] = [
        {"option_id": "sp500", "allocation_pct": 60, "rationale": "Benchmark exposure."},
        {"option_id": "cash", "allocation_pct": 35, "rationale": "Defensive exposure."},
    ]
    (round_path / "submissions" / "raw" / "bad-sum.json").write_text(json.dumps(payload), encoding="utf-8")

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "sum to 100%" in summary.errors["bad-sum.json"][0]


def test_portfolio_submission_rejects_too_many_holdings(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["submission_format"] = "portfolio"
    manifest["portfolio_constraints"] = {"max_holdings": 1}
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    (round_path / "submissions" / "raw" / "too-many.json").write_text(
        json.dumps(_valid_portfolio_payload()),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "between 1 and 1 holdings" in summary.errors["too-many.json"][0]


def test_portfolio_submission_rejects_disallowed_cash_allocation(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["submission_format"] = "portfolio"
    manifest["portfolio_constraints"] = {"allow_cash": False}
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    (round_path / "submissions" / "raw" / "cash.json").write_text(
        json.dumps(_valid_portfolio_payload()),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "cash allocation is not allowed" in summary.errors["cash.json"][0]


def test_portfolio_submission_rejects_disallowed_benchmark_allocation(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    manifest_path = round_path / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["submission_format"] = "portfolio"
    manifest["portfolio_constraints"] = {"allow_benchmark_asset": False}
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    (round_path / "submissions" / "raw" / "benchmark.json").write_text(
        json.dumps(_valid_portfolio_payload()),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "benchmark asset allocation is not allowed" in summary.errors["benchmark.json"][0]


def test_single_pick_round_rejects_portfolio_payload(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    _write_round_base(round_path)
    (round_path / "submissions" / "raw" / "portfolio.json").write_text(
        json.dumps(_valid_portfolio_payload()),
        encoding="utf-8",
    )

    summary = validate_submissions(round_path, _options())

    assert summary.invalid_count == 1
    assert "single_pick rounds require selected_option_id" in summary.errors["portfolio.json"][0]

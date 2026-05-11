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

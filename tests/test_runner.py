import hashlib
import json
from pathlib import Path
from shutil import copytree

import pytest
import yaml

import capitalbench.runner as runner_module
from capitalbench.config import calculate_cost_usd, load_model_configs, load_pricing_config
from capitalbench.providers.base import ProviderResult
from capitalbench.runner import run_round
from capitalbench.schemas import RuntimeSettings, Usage


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROUND = PROJECT_ROOT / "rounds" / "example-round"


def _copy_example_round(tmp_path: Path) -> Path:
    target = tmp_path / "example-round"
    copytree(EXAMPLE_ROUND, target)
    return target


def _write_models(path: Path, models: list[dict[str, object]]) -> Path:
    path.write_text(yaml.safe_dump({"models": models}, sort_keys=False), encoding="utf-8")
    return path


def _model(
    *,
    model_id: str = "openai-example",
    provider: str = "openai",
    enabled: bool = True,
    api_model_name: str = "mock-model",
) -> dict[str, object]:
    return {
        "model_id": model_id,
        "provider": provider,
        "api_model_name": api_model_name,
        "enabled": enabled,
        "mode": "closed_capability",
        "temperature": 0,
        "max_completion_tokens": 3000,
        "max_wall_clock_seconds": 120,
        "reasoning_effort": None,
    }


def test_mock_run_creates_raw_and_parsed_submissions(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])

    summary = run_round(round_path, models_path, mock=True)

    assert summary.attempted_models == 1
    assert summary.valid_submissions == 1
    run_path = round_path / "runs" / summary.run_id
    assert (run_path / "submissions" / "raw" / "openai-example.json").exists()
    assert (run_path / "submissions" / "parsed" / "openai-example.json").exists()


def test_run_round_preserves_exact_raw_response_text_and_hash(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])

    summary = run_round(round_path, models_path, mock=True, run_id="raw-preserved")

    run_path = round_path / "runs" / summary.run_id
    raw_response_path = run_path / "raw_responses" / "openai-example.txt"
    assert raw_response_path.exists()
    raw_text = raw_response_path.read_text(encoding="utf-8")
    log_record = json.loads((run_path / "run_log.jsonl").read_text(encoding="utf-8").splitlines()[0])

    assert log_record["raw_response_path"] == "raw_responses/openai-example.txt"
    assert hashlib.sha256(raw_text.encode("utf-8")).hexdigest() == log_record["raw_response_sha256"]


def test_run_round_without_allow_real_api_calls_does_not_call_real_providers(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])
    existing_run = round_path / "runs" / "forbidden"
    existing_run.mkdir(parents=True)

    with pytest.raises(RuntimeError, match="without --allow-real-api-calls"):
        run_round(round_path, models_path, run_id="forbidden")

    assert not (existing_run / "submissions").exists()


def test_missing_api_key_fails_clearly_when_real_calls_are_allowed(tmp_path: Path, monkeypatch) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        run_round(round_path, models_path, allow_real_api_calls=True)


def test_invalid_provider_fails_clearly(tmp_path: Path) -> None:
    models_path = _write_models(
        tmp_path / "models.yaml",
        [_model(provider="not-a-provider")],
    )

    with pytest.raises(ValueError, match="invalid model config"):
        load_model_configs(models_path)


def test_pricing_calculation_works_when_pricing_is_provided(tmp_path: Path) -> None:
    pricing_path = tmp_path / "pricing.yaml"
    pricing_path.write_text(
        yaml.safe_dump(
            {
                "pricing": {
                    "openai": {
                        "mock-model": {
                            "input_per_1m_tokens_usd": 2.0,
                            "output_per_1m_tokens_usd": 8.0,
                        }
                    }
                }
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    pricing = load_pricing_config(pricing_path)

    cost = calculate_cost_usd(
        "openai",
        "mock-model",
        Usage(input_tokens=1_000_000, output_tokens=500_000),
        pricing,
    )

    assert cost == 6.0


def test_pricing_remains_null_when_pricing_is_missing(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])

    summary = run_round(round_path, models_path, mock=True)
    payload = json.loads(
        (round_path / "runs" / summary.run_id / "submissions" / "parsed" / "openai-example.json").read_text()
    )

    assert "cost_usd" not in payload
    assert "cost_usd" not in payload["usage"]


def test_raw_responses_are_preserved_when_validation_fails(tmp_path: Path, monkeypatch) -> None:
    class InvalidMockProvider:
        def run_model(self, model_config, prompt, json_schema, runtime_limits: RuntimeSettings) -> ProviderResult:
            payload = {
                "round_id": model_config.metadata["round_id"],
                "model_id": model_config.model_id,
                "provider": model_config.provider,
                "mode": model_config.mode,
                "confidence": 0.5,
                "rationale_summary": "Missing selected option.",
                "key_risks": ["Invalid on purpose"],
            }
            return ProviderResult(
                raw_text=json.dumps(payload),
                parsed_json=payload,
                usage=Usage(input_tokens=1, output_tokens=1, latency_seconds=0),
                error=None,
            )

    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])
    monkeypatch.setattr("capitalbench.runner.MockProvider", InvalidMockProvider)

    summary = run_round(round_path, models_path, mock=True)

    assert summary.invalid_submissions == 1
    run_path = round_path / "runs" / summary.run_id
    assert (run_path / "submissions" / "raw" / "openai-example.json").exists()
    assert not (run_path / "submissions" / "parsed" / "openai-example.json").exists()


def test_clean_real_official_run_becomes_official_score_eligible(tmp_path: Path, monkeypatch) -> None:
    class ValidProvider:
        api_key_env_var = "OPENAI_API_KEY"

        def run_model(self, model_config, prompt, json_schema, runtime_limits: RuntimeSettings) -> ProviderResult:
            payload = {
                "round_id": model_config.metadata["round_id"],
                "model_id": model_config.model_id,
                "provider": model_config.provider,
                "mode": model_config.mode,
                "run_type": "official",
                "replicate_index": 1,
                "replicate_count": 1,
                "is_official_score": True,
                "selected_option_id": "SP500",
                "confidence": 0.5,
                "rationale_summary": "Valid official response.",
                "key_risks": ["Risk one"],
            }
            return ProviderResult(
                raw_text=json.dumps(payload),
                parsed_json=payload,
                usage=Usage(input_tokens=1, output_tokens=1, latency_seconds=0),
                error=None,
            )

    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setitem(runner_module.PROVIDER_CLASSES, "openai", ValidProvider)

    summary = run_round(
        round_path,
        models_path,
        run_id="official-clean",
        run_type="official",
        allow_real_api_calls=True,
    )
    manifest = yaml.safe_load(
        (round_path / "runs" / summary.run_id / "run_manifest.yaml").read_text(encoding="utf-8")
    )

    assert summary.valid_submissions == 1
    assert manifest["official_score_eligible"] is True


def test_invalid_real_official_run_is_not_official_score_eligible(tmp_path: Path, monkeypatch) -> None:
    class InvalidProvider:
        api_key_env_var = "OPENAI_API_KEY"

        def run_model(self, model_config, prompt, json_schema, runtime_limits: RuntimeSettings) -> ProviderResult:
            payload = {
                "round_id": model_config.metadata["round_id"],
                "model_id": model_config.model_id,
                "provider": model_config.provider,
                "mode": model_config.mode,
                "run_type": "official",
                "replicate_index": 1,
                "replicate_count": 1,
                "is_official_score": True,
                "confidence": 0.5,
                "rationale_summary": "Missing selected option.",
                "key_risks": ["Invalid on purpose"],
            }
            return ProviderResult(
                raw_text=json.dumps(payload),
                parsed_json=payload,
                usage=Usage(input_tokens=1, output_tokens=1, latency_seconds=0),
                error=None,
            )

    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setitem(runner_module.PROVIDER_CLASSES, "openai", InvalidProvider)

    summary = run_round(
        round_path,
        models_path,
        run_id="official-invalid",
        run_type="official",
        allow_real_api_calls=True,
    )
    manifest = yaml.safe_load(
        (round_path / "runs" / summary.run_id / "run_manifest.yaml").read_text(encoding="utf-8")
    )

    assert summary.invalid_submissions == 1
    assert manifest["official_score_eligible"] is False
    assert "invalid submissions" in manifest["notes"]


def test_model_config_loading_works(tmp_path: Path) -> None:
    models_path = _write_models(tmp_path / "models.yaml", [_model(), _model(model_id="google-example", provider="google")])

    configs = load_model_configs(models_path)

    assert [config.model_id for config in configs] == ["openai-example", "google-example"]
    assert configs[0].api_model_name == "mock-model"


def test_disabled_models_are_skipped(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(
        tmp_path / "models.yaml",
        [
            _model(model_id="enabled"),
            _model(model_id="disabled", enabled=False),
        ],
    )

    summary = run_round(round_path, models_path, mock=True)

    assert summary.loaded_models == 2
    assert summary.skipped_models == 1
    assert summary.attempted_models == 1
    run_path = round_path / "runs" / summary.run_id
    assert (run_path / "submissions" / "parsed" / "enabled.json").exists()
    assert not (run_path / "submissions" / "parsed" / "disabled.json").exists()


def test_future_first_eligible_round_is_skipped_from_older_round(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    manifest = yaml.safe_load((round_path / "manifest.yaml").read_text(encoding="utf-8"))
    manifest["round_id"] = "CB-2026-05-01-1M"
    (round_path / "manifest.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    future_model = _model(model_id="future-model")
    future_model["first_eligible_round"] = "CB-2026-06-01-1M"
    models_path = _write_models(tmp_path / "models.yaml", [future_model])

    summary = run_round(round_path, models_path, mock=True, run_type="official")

    assert summary.attempted_models == 0
    assert any("not eligible until CB-2026-06-01-1M" in reason for reason in summary.skipped_reasons)


def test_first_eligible_round_includes_model_on_future_round(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    manifest = yaml.safe_load((round_path / "manifest.yaml").read_text(encoding="utf-8"))
    manifest["round_id"] = "CB-2026-06-01-1M"
    (round_path / "manifest.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    future_model = _model(model_id="future-model")
    future_model["first_eligible_round"] = "CB-2026-06-01-1M"
    models_path = _write_models(tmp_path / "models.yaml", [future_model])

    summary = run_round(round_path, models_path, mock=True, run_type="official")

    assert summary.attempted_models == 1
    assert summary.skipped_reasons == []


def test_first_eligible_date_utc_is_respected(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    date_model = _model(model_id="date-model")
    date_model["first_eligible_date_utc"] = "2026-05-01T00:00:00Z"
    models_path = _write_models(tmp_path / "models.yaml", [date_model])

    summary = run_round(round_path, models_path, mock=True, run_type="official")

    assert summary.attempted_models == 0
    assert any("not eligible until 2026-05-01T00:00:00Z" in reason for reason in summary.skipped_reasons)


def test_retrospective_run_is_never_official_score_eligible(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    models_path = _write_models(tmp_path / "models.yaml", [_model()])

    summary = run_round(round_path, models_path, mock=True, run_type="retrospective")
    run_manifest = yaml.safe_load(
        (round_path / "runs" / summary.run_id / "run_manifest.yaml").read_text(encoding="utf-8")
    )

    assert run_manifest["run_type"] == "retrospective"
    assert run_manifest["official_score_eligible"] is False

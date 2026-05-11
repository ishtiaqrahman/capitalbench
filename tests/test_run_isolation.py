import json
from pathlib import Path
from shutil import copytree, rmtree

import pytest

import capitalbench.provider_smoke as provider_smoke_module
from capitalbench.cli import main
from capitalbench.provider_smoke import smoke_provider
from capitalbench.run_store import LEGACY_RUN_ID, get_run_paths, list_run_ids, read_run_manifest
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


def test_run_round_creates_named_run_directory(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)

    summary = run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="mock-a")

    run_path = round_path / "runs" / "mock-a"
    assert summary.run_id == "mock-a"
    assert (run_path / "submissions" / "raw").is_dir()
    assert (run_path / "submissions" / "parsed").is_dir()
    assert (run_path / "run_log.jsonl").exists()
    assert (run_path / "run_manifest.yaml").exists()
    assert (run_path / "validation_summary.json").exists()


def test_repeated_run_id_fails_without_overwrite(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="same-run")

    with pytest.raises(FileExistsError, match="already exists"):
        run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="same-run")


def test_overwrite_run_replaces_only_selected_run(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="target")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="other")
    sentinel = round_path / "runs" / "target" / "sentinel.txt"
    sentinel.write_text("remove me", encoding="utf-8")
    other_log = round_path / "runs" / "other" / "run_log.jsonl"
    manifest = round_path / "manifest.yaml"

    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="target", overwrite_run=True)

    assert not sentinel.exists()
    assert other_log.exists()
    assert manifest.exists()


def test_validate_submissions_requires_run_id_when_multiple_runs_exist(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="run-one")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="run-two")

    with pytest.raises(ValueError, match="multiple runs found"):
        validate_submissions(round_path)


def test_score_round_uses_selected_run_id(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="run-one")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="run-two")

    scores = score_round(round_path, run_id="run-one")

    assert len(scores) == 4
    assert (round_path / "runs" / "run-one" / "results" / "leaderboard.csv").exists()
    assert not (round_path / "runs" / "run-two" / "results" / "leaderboard.csv").exists()


def test_publish_report_writes_into_selected_run_results(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="report-run")
    score_round(round_path, run_id="report-run")

    exit_code = main(["publish-report", "--round", str(round_path), "--run-id", "report-run"])

    assert exit_code == 0
    assert (round_path / "runs" / "report-run" / "results" / "report.md").exists()


def test_list_runs_shows_available_runs(tmp_path: Path, capsys) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="list-one")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="list-two")

    exit_code = main(["list-runs", "--round", str(round_path)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "list-one" in captured.out
    assert "list-two" in captured.out


def test_mock_run_manifest_cannot_be_official_score_eligible(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    run_path = round_path / "runs" / "stale-mock-official"
    run_path.mkdir(parents=True)
    (run_path / "run_manifest.yaml").write_text(
        "\n".join(
            [
                "run_id: stale-mock-official",
                "round_id: example-round",
                "run_type: official",
                "mock: true",
                "replicates: 1",
                "official_score_eligible: true",
                "",
            ]
        ),
        encoding="utf-8",
    )

    manifest = read_run_manifest(get_run_paths(round_path, "stale-mock-official"))

    assert manifest["official_score_eligible"] is False


def test_audit_round_works_with_and_without_run_id(tmp_path: Path, capsys) -> None:
    round_path = _copy_example_round(tmp_path)
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="audit-one")
    run_round(round_path, MODELS_EXAMPLE, mock=True, run_id="audit-two")

    assert main(["audit-round", "--round", str(round_path)]) == 0
    without_run = capsys.readouterr().out
    assert "Available runs:" in without_run
    assert "Warning: multiple runs exist" in without_run

    assert main(["audit-round", "--round", str(round_path), "--run-id", "audit-one"]) == 0
    with_run = capsys.readouterr().out
    assert "Selected run: audit-one" in with_run
    assert "Run run_log.jsonl: yes" in with_run


def test_old_submissions_are_migrated_safely(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)
    source_payload = round_path / "runs" / LEGACY_RUN_ID / "submissions" / "raw" / "openai-gpt-example.json"
    payload = source_payload.read_text(encoding="utf-8")
    rmtree(round_path / "runs" / LEGACY_RUN_ID)
    legacy_raw = round_path / "submissions" / "raw"
    legacy_raw.mkdir(parents=True)
    (legacy_raw / "legacy.json").write_text(
        payload,
        encoding="utf-8",
    )
    assert legacy_raw.exists()

    run_ids = list_run_ids(round_path)
    if LEGACY_RUN_ID not in run_ids:
        main(["list-runs", "--round", str(round_path)])

    assert (round_path / "runs" / LEGACY_RUN_ID / "submissions" / "raw").exists()
    assert (round_path / "runs" / LEGACY_RUN_ID / "submissions" / "raw" / "legacy.json").exists()
    assert legacy_raw.exists()


def test_smoke_provider_refuses_without_allow_real_api_calls(tmp_path: Path) -> None:
    round_path = _copy_example_round(tmp_path)

    with pytest.raises(RuntimeError, match="without --allow-real-api-calls"):
        smoke_provider(
            provider="openai",
            api_model_name="model",
            round_path=round_path,
            allow_real_api_calls=False,
        )


def test_smoke_provider_fails_clearly_when_api_key_missing(tmp_path: Path, monkeypatch) -> None:
    round_path = _copy_example_round(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        smoke_provider(
            provider="openai",
            api_model_name="model",
            round_path=round_path,
            allow_real_api_calls=True,
        )


def test_smoke_provider_preserves_provider_error_artifacts(tmp_path: Path, monkeypatch) -> None:
    round_path = _copy_example_round(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    class FailingProvider:
        def run_model(self, model_config, prompt, json_schema, runtime_limits):
            raise RuntimeError("openai API request failed with HTTP 429")

    monkeypatch.setitem(provider_smoke_module.PROVIDER_CLASSES, "openai", FailingProvider)

    summary = smoke_provider(
        provider="openai",
        api_model_name="model",
        round_path=round_path,
        allow_real_api_calls=True,
    )

    smoke_log = json.loads((summary.smoke_dir / "smoke_log.json").read_text(encoding="utf-8"))
    validation_result = json.loads((summary.smoke_dir / "validation_result.json").read_text(encoding="utf-8"))

    assert summary.validation_status == "invalid"
    assert "HTTP 429" in (summary.error or "")
    assert (summary.smoke_dir / "raw_response.txt").exists()
    assert smoke_log["validation_status"] == "invalid"
    assert "HTTP 429" in smoke_log["error"]
    assert validation_result["validation_status"] == "invalid"


def test_smoke_provider_uses_minimal_openai_reasoning_effort(tmp_path: Path, monkeypatch) -> None:
    round_path = _copy_example_round(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    captured = {}

    class CapturingProvider:
        def run_model(self, model_config, prompt, json_schema, runtime_limits):
            captured["model_reasoning_effort"] = model_config.reasoning_effort
            captured["runtime_reasoning_effort"] = runtime_limits.reasoning_effort
            from capitalbench.schemas import Usage
            from capitalbench.providers.base import ProviderResult

            return ProviderResult(
                raw_text=(
                    '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
                    '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
                    '"rationale_summary":"Test","key_risks":["Risk one","Risk two"]}'
                ),
                parsed_json={
                    "round_id": "example-round",
                    "model_id": "openai-smoke",
                    "provider": "openai",
                    "mode": "closed_capability",
                    "selected_option_id": "SP500",
                    "confidence": 0.5,
                    "rationale_summary": "Test",
                    "key_risks": ["Risk one", "Risk two"],
                },
                usage=Usage(latency_seconds=0.01),
                error=None,
            )

    monkeypatch.setitem(provider_smoke_module.PROVIDER_CLASSES, "openai", CapturingProvider)

    summary = smoke_provider(
        provider="openai",
        api_model_name="model",
        round_path=round_path,
        allow_real_api_calls=True,
    )

    assert summary.validation_status == "valid"
    assert captured["model_reasoning_effort"] == "minimal"
    assert captured["runtime_reasoning_effort"] == "minimal"


def test_smoke_provider_uses_low_google_reasoning_effort(tmp_path: Path, monkeypatch) -> None:
    round_path = _copy_example_round(tmp_path)
    monkeypatch.setenv("GOOGLE_API_KEY", "test-key")
    captured = {}

    class CapturingProvider:
        def run_model(self, model_config, prompt, json_schema, runtime_limits):
            captured["model_reasoning_effort"] = model_config.reasoning_effort
            captured["runtime_reasoning_effort"] = runtime_limits.reasoning_effort
            from capitalbench.schemas import Usage
            from capitalbench.providers.base import ProviderResult

            return ProviderResult(
                raw_text=(
                    '{"round_id":"example-round","model_id":"google-smoke","provider":"google",'
                    '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
                    '"rationale_summary":"Test","key_risks":["Risk one","Risk two"]}'
                ),
                parsed_json={
                    "round_id": "example-round",
                    "model_id": "google-smoke",
                    "provider": "google",
                    "mode": "closed_capability",
                    "selected_option_id": "SP500",
                    "confidence": 0.5,
                    "rationale_summary": "Test",
                    "key_risks": ["Risk one", "Risk two"],
                },
                usage=Usage(latency_seconds=0.01),
                error=None,
            )

    monkeypatch.setitem(provider_smoke_module.PROVIDER_CLASSES, "google", CapturingProvider)

    summary = smoke_provider(
        provider="google",
        api_model_name="model",
        round_path=round_path,
        allow_real_api_calls=True,
    )

    assert summary.validation_status == "valid"
    assert captured["model_reasoning_effort"] == "low"
    assert captured["runtime_reasoning_effort"] == "low"


def test_check_providers_does_not_print_secrets(monkeypatch, capsys) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-secret-value")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.delenv("XAI_API_KEY", raising=False)

    exit_code = main(["check-providers"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "OPENAI_API_KEY: present" in output
    assert "ANTHROPIC_API_KEY: missing" in output
    assert "sk-secret-value" not in output

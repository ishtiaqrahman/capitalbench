from capitalbench.providers.base import parse_json_object
from capitalbench.providers.anthropic_provider import AnthropicProvider
from capitalbench.providers.google_provider import GoogleProvider, _to_google_response_schema
from capitalbench.providers.mock_provider import MockProvider
from capitalbench.providers.openai_provider import OpenAIProvider
from capitalbench.providers.xai_provider import XAIProvider
from capitalbench.schemas import ModelConfig, RuntimeSettings
from capitalbench.submission_schema import provider_submission_schema


def test_parse_clean_json_object() -> None:
    assert parse_json_object('{"selected_option_id": "SP500"}') == {"selected_option_id": "SP500"}


def test_parse_json_wrapped_in_markdown() -> None:
    raw = '```json\n{"selected_option_id": "SP500"}\n```'
    assert parse_json_object(raw) == {"selected_option_id": "SP500"}


def test_parse_json_with_extra_prose() -> None:
    raw = 'Here is the answer:\n{"selected_option_id": "SP500"}\nDone.'
    assert parse_json_object(raw) == {"selected_option_id": "SP500"}


def test_parse_malformed_json_returns_none() -> None:
    assert parse_json_object('{"selected_option_id": ') is None


def test_parse_non_object_json_returns_none() -> None:
    assert parse_json_object('["SP500"]') is None


def _model_config() -> ModelConfig:
    return ModelConfig(
        model_id="openai-smoke",
        provider="openai",
        api_model_name="gpt-test",
        enabled=True,
        mode="closed_capability",
        temperature=0,
        max_completion_tokens=500,
        max_wall_clock_seconds=60,
        reasoning_effort=None,
        metadata={
            "round_id": "example-round",
            "option_ids": ["SP500", "CASH"],
        },
    )


def _portfolio_model_config() -> ModelConfig:
    config = _model_config()
    return config.model_copy(
        update={
            "metadata": {
                **config.metadata,
                "submission_format": "portfolio",
                "portfolio_constraints": {
                    "min_holdings": 1,
                    "max_holdings": 5,
                    "allocation_increment_pct": 5,
                    "min_allocation_pct": 5,
                    "max_total_allocation_pct": 100,
                },
            }
        }
    )


def test_provider_submission_schema_supports_portfolio_format() -> None:
    schema = provider_submission_schema(_portfolio_model_config())

    assert "portfolio" in schema["required"]
    portfolio_schema = schema["properties"]["portfolio"]
    assert portfolio_schema["minItems"] == 1
    assert portfolio_schema["maxItems"] == 5
    assert portfolio_schema["items"]["properties"]["allocation_pct"]["multipleOf"] == 5


def test_mock_provider_respects_portfolio_allocation_constraints() -> None:
    config = _portfolio_model_config().model_copy(
        update={
            "metadata": {
                "round_id": "example-round",
                "option_ids": ["SP500", "CASH", "TECHNOLOGY", "HEALTHCARE"],
                "submission_format": "portfolio",
                "portfolio_constraints": {
                    "min_holdings": 2,
                    "max_holdings": 3,
                    "allocation_increment_pct": 10,
                    "min_allocation_pct": 10,
                    "max_total_allocation_pct": 100,
                },
            }
        }
    )

    result = MockProvider().run_model(config, "prompt", provider_submission_schema(config), RuntimeSettings())
    portfolio = result.parsed_json["portfolio"]
    allocations = [item["allocation_pct"] for item in portfolio]
    assert 2 <= len(portfolio) <= 3
    assert sum(allocations) == 100
    assert all(allocation >= 10 and allocation % 10 == 0 for allocation in allocations)


def _xai_model_config() -> ModelConfig:
    return ModelConfig(
        model_id="xai-smoke",
        provider="xai",
        api_model_name="grok-test",
        enabled=True,
        mode="closed_capability",
        temperature=0,
        max_completion_tokens=500,
        max_wall_clock_seconds=60,
        reasoning_effort=None,
        metadata={
            "round_id": "example-round",
            "option_ids": ["SP500", "CASH"],
        },
    )


def _anthropic_model_config() -> ModelConfig:
    return ModelConfig(
        model_id="anthropic-smoke",
        provider="anthropic",
        api_model_name="claude-test",
        enabled=True,
        mode="closed_capability",
        temperature=0,
        max_completion_tokens=500,
        max_wall_clock_seconds=60,
        reasoning_effort=None,
        metadata={
            "round_id": "example-round",
            "option_ids": ["SP500", "CASH"],
        },
    )


def test_openai_provider_disables_tools_in_payload(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    provider = OpenAIProvider()
    captured_payload = {}
    raw_json = (
        '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        captured_payload.update(payload)
        return {"output_text": raw_json}

    monkeypatch.setattr(provider, "_post_json", fake_post)
    model_config = _model_config()

    provider.run_model(
        model_config,
        "prompt",
        provider_submission_schema(model_config),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
    )

    assert captured_payload["tools"] == []
    assert captured_payload["tool_choice"] == "none"


def test_openai_provider_handles_missing_usage_fields(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    provider = OpenAIProvider()
    raw_json = (
        '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )
    monkeypatch.setattr(provider, "_post_json", lambda *args, **kwargs: {"output_text": raw_json})

    result = provider.run_model(
        _model_config(),
        "prompt",
        provider_submission_schema(_model_config()),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
    )

    assert result.parsed_json is not None
    assert result.parsed_json["selected_option_id"] == "SP500"
    assert result.usage.input_tokens is None
    assert result.usage.output_tokens is None
    assert result.usage.latency_seconds is not None


def test_openai_provider_retries_without_temperature_when_unsupported(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    provider = OpenAIProvider()
    payloads = []
    raw_json = (
        '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        payloads.append(dict(payload))
        if len(payloads) == 1:
            raise RuntimeError("openai API request failed with HTTP 400: Unsupported parameter: 'temperature'")
        return {"output_text": raw_json}

    monkeypatch.setattr(provider, "_post_json", fake_post)

    result = provider.run_model(
        _model_config(),
        "prompt",
        provider_submission_schema(_model_config()),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
    )

    assert result.parsed_json is not None
    assert "temperature" in payloads[0]
    assert "temperature" not in payloads[1]


def test_openai_provider_error_response_is_raised(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    provider = OpenAIProvider()

    def fail(*args, **kwargs):
        raise RuntimeError("openai API request failed with HTTP 400")

    monkeypatch.setattr(provider, "_post_json", fail)

    try:
        provider.run_model(
            _model_config(),
            "prompt",
            provider_submission_schema(_model_config()),
            RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
        )
    except RuntimeError as exc:
        assert "HTTP 400" in str(exc)
    else:
        raise AssertionError("provider error was not raised")


def test_openai_provider_missing_api_key_fails(monkeypatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    provider = OpenAIProvider()

    try:
        provider.run_model(
            _model_config(),
            "prompt",
            provider_submission_schema(_model_config()),
            RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
        )
    except RuntimeError as exc:
        assert "OPENAI_API_KEY" in str(exc)
    else:
        raise AssertionError("missing API key did not fail")


def test_anthropic_provider_disables_tools_in_payload(monkeypatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    provider = AnthropicProvider()
    captured_payload = {}
    raw_json = (
        '{"round_id":"example-round","model_id":"anthropic-smoke","provider":"anthropic",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        captured_payload.update(payload)
        return {
            "content": [{"type": "text", "text": raw_json}],
            "usage": {"input_tokens": 1, "output_tokens": 1},
        }

    monkeypatch.setattr(provider, "_post_json", fake_post)
    model_config = _anthropic_model_config()

    provider.run_model(
        model_config,
        "prompt",
        provider_submission_schema(model_config),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
    )

    assert captured_payload["tool_choice"] == {"type": "none"}
    assert "tools" not in captured_payload


def test_anthropic_provider_retries_without_deprecated_temperature(monkeypatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    provider = AnthropicProvider()
    payloads = []
    raw_json = (
        '{"round_id":"example-round","model_id":"anthropic-smoke","provider":"anthropic",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        payloads.append(dict(payload))
        if len(payloads) == 1:
            raise RuntimeError("anthropic API request failed with HTTP 400: temperature is deprecated")
        return {
            "content": [{"type": "text", "text": raw_json}],
            "usage": {"input_tokens": 1, "output_tokens": 1},
        }

    monkeypatch.setattr(provider, "_post_json", fake_post)

    result = provider.run_model(
        _anthropic_model_config(),
        "prompt",
        provider_submission_schema(_anthropic_model_config()),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
    )

    assert result.parsed_json is not None
    assert "temperature" in payloads[0]
    assert "temperature" not in payloads[1]


def test_google_schema_conversion_strips_unsupported_keywords() -> None:
    schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "allocation_pct": {"type": "integer", "minimum": 5, "maximum": 100, "multipleOf": 5},
            "key_risks": {
                "type": "array",
                "items": {"type": "string", "additionalProperties": False},
            },
        },
    }

    converted = _to_google_response_schema(schema)

    assert "additionalProperties" not in converted
    assert "minimum" not in converted["properties"]["confidence"]
    assert "maximum" not in converted["properties"]["confidence"]
    assert "multipleOf" not in converted["properties"]["allocation_pct"]
    assert "additionalProperties" not in converted["properties"]["key_risks"]["items"]


def test_google_provider_disables_thinking_when_requested(monkeypatch) -> None:
    monkeypatch.setenv("GOOGLE_API_KEY", "test-key")
    provider = GoogleProvider()
    captured_payload = {}
    captured_request = {}
    raw_json = (
        '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        captured_request["url"] = url
        captured_request["headers"] = headers
        captured_payload.update(payload)
        return {
            "candidates": [{"content": {"parts": [{"text": raw_json}]}}],
            "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "totalTokenCount": 2},
        }

    monkeypatch.setattr(provider, "_post_json", fake_post)

    provider.run_model(
        _model_config(),
        "prompt",
        provider_submission_schema(_model_config()),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0, reasoning_effort="none"),
    )

    generation_config = captured_payload["generationConfig"]
    assert generation_config["thinkingConfig"] == {"thinkingBudget": 0}
    assert "key=" not in captured_request["url"]
    assert captured_request["headers"] == {"x-goog-api-key": "test-key"}
    assert captured_payload["tools"] == []
    assert captured_payload["toolConfig"] == {"functionCallingConfig": {"mode": "NONE"}}


def test_google_provider_supports_low_thinking_budget(monkeypatch) -> None:
    monkeypatch.setenv("GOOGLE_API_KEY", "test-key")
    provider = GoogleProvider()
    captured_payload = {}
    raw_json = (
        '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        captured_payload.update(payload)
        return {
            "candidates": [{"content": {"parts": [{"text": raw_json}]}}],
            "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "totalTokenCount": 2},
        }

    monkeypatch.setattr(provider, "_post_json", fake_post)

    provider.run_model(
        _model_config(),
        "prompt",
        provider_submission_schema(_model_config()),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0, reasoning_effort="low"),
    )

    generation_config = captured_payload["generationConfig"]
    assert generation_config["thinkingConfig"] == {"thinkingBudget": 512}
    assert captured_payload["tools"] == []
    assert captured_payload["toolConfig"] == {"functionCallingConfig": {"mode": "NONE"}}


def test_google_provider_leaves_thinking_default_for_real_runs(monkeypatch) -> None:
    monkeypatch.setenv("GOOGLE_API_KEY", "test-key")
    provider = GoogleProvider()
    captured_payload = {}
    raw_json = (
        '{"round_id":"example-round","model_id":"openai-smoke","provider":"openai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        captured_payload.update(payload)
        return {
            "candidates": [{"content": {"parts": [{"text": raw_json}]}}],
            "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "totalTokenCount": 2},
        }

    monkeypatch.setattr(provider, "_post_json", fake_post)

    provider.run_model(
        _model_config(),
        "prompt",
        provider_submission_schema(_model_config()),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=3000, temperature=0),
    )

    generation_config = captured_payload["generationConfig"]
    assert "thinkingConfig" not in generation_config
    assert captured_payload["tools"] == []
    assert captured_payload["toolConfig"] == {"functionCallingConfig": {"mode": "NONE"}}


def test_xai_provider_disables_tools_without_deprecated_live_search_parameters(monkeypatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "test-key")
    provider = XAIProvider()
    captured_payload = {}
    raw_json = (
        '{"round_id":"example-round","model_id":"xai-smoke","provider":"xai",'
        '"mode":"closed_capability","selected_option_id":"SP500","confidence":0.5,'
        '"rationale_summary":"Test","key_risks":["Risk"]}'
    )

    def fake_post(url, headers, payload, timeout):
        captured_payload.update(payload)
        return {
            "choices": [{"message": {"content": raw_json}}],
            "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
        }

    monkeypatch.setattr(provider, "_post_json", fake_post)

    model_config = _xai_model_config()
    provider.run_model(
        model_config,
        "prompt",
        provider_submission_schema(model_config),
        RuntimeSettings(timeout_seconds=1, max_output_tokens=500, temperature=0),
    )

    assert captured_payload["tools"] == []
    assert "tool_choice" not in captured_payload
    assert "search_parameters" not in captured_payload

import json
from pathlib import Path

import yaml

from capitalbench.insights import DEFAULT_NVIDIA_MODEL_ID, LLM_OUTPUT_VERSION, build_insights_input, generate_insights, validate_insights


def _write_yaml(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0])
    lines = [",".join(fieldnames)]
    for row in rows:
        values = []
        for field in fieldnames:
            value = str(row.get(field, ""))
            if "," in value:
                value = '"' + value.replace('"', '""') + '"'
            values.append(value)
        lines.append(",".join(values))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _options() -> dict:
    base = {
        "asset_class": "equity",
        "category": "test",
        "option_group": "test",
        "risk_bucket": "medium",
        "exposure_description": "Test exposure.",
        "currency": "USD",
        "include_in_universe": True,
    }
    return {
        "options": [
            {
                **base,
                "id": "CASH",
                "name": "Cash",
                "symbol": None,
                "asset_class": "cash",
                "category": "cash",
                "option_group": "cash",
                "risk_bucket": "cash",
                "tiingo_symbol": None,
                "is_cash": True,
            },
            {
                **base,
                "id": "SP500",
                "name": "S&P 500",
                "symbol": "SPY",
                "tiingo_symbol": "SPY",
                "is_benchmark": True,
            },
            {
                **base,
                "id": "TECHNOLOGY",
                "name": "Technology Sector",
                "symbol": "XLK",
                "tiingo_symbol": "XLK",
                "category": "us_sector",
                "risk_bucket": "high",
            },
            {
                **base,
                "id": "BONDS",
                "name": "Aggregate Bonds",
                "symbol": "AGG",
                "tiingo_symbol": "AGG",
                "asset_class": "bond",
                "category": "bonds",
            },
        ]
    }


def _write_run(round_path: Path, *, resolved: bool) -> None:
    run_path = round_path / "runs" / "official"
    parsed = run_path / "submissions" / "parsed"
    parsed.mkdir(parents=True, exist_ok=True)
    _write_yaml(
        run_path / "run_manifest.yaml",
        {
            "run_id": "official",
            "round_id": round_path.name,
            "run_type": "official",
            "mode": "closed_capability",
            "mock": False,
            "official_score_eligible": True,
            "operator_selected_official": True,
            "model_count": 2,
            "valid_submissions": 2,
            "invalid_submissions": 0,
        },
    )
    submissions = {
        "model-a": [
            {"option_id": "TECHNOLOGY", "allocation_pct": 50, "rationale": "Growth."},
            {"option_id": "SP500", "allocation_pct": 50, "rationale": "Benchmark."},
        ],
        "model-b": [{"option_id": "BONDS", "allocation_pct": 100, "rationale": "Defense."}],
    }
    for model_id, portfolio in submissions.items():
        (parsed / f"{model_id}.json").write_text(
            json.dumps(
                {
                    "round_id": round_path.name,
                    "run_type": "official",
                    "replicate_index": 1,
                    "replicate_count": 1,
                    "is_official_score": True,
                    "model_id": model_id,
                    "provider": "openai",
                    "mode": "closed_capability",
                    "portfolio": portfolio,
                    "confidence": 0.7 if model_id == "model-a" else 0.4,
                    "portfolio_rationale": "Test rationale.",
                    "rationale_summary": "Test summary.",
                    "key_risks": ["Risk one", "Risk two"],
                }
            ),
            encoding="utf-8",
        )
    if not resolved:
        return
    _write_csv(
        run_path / "results" / "returns.csv",
        [
            {"option_id": "TECHNOLOGY", "label": "Technology Sector", "asset_symbol": "XLK", "return": 0.1, "rank": 1, "is_benchmark": False, "is_cash": False},
            {"option_id": "SP500", "label": "S&P 500", "asset_symbol": "SPY", "return": 0.02, "rank": 2, "is_benchmark": True, "is_cash": False},
            {"option_id": "CASH", "label": "Cash", "asset_symbol": "CASH", "return": 0, "rank": 3, "is_benchmark": False, "is_cash": True},
            {"option_id": "BONDS", "label": "Aggregate Bonds", "asset_symbol": "AGG", "return": -0.01, "rank": 4, "is_benchmark": False, "is_cash": False},
        ],
    )
    _write_csv(
        run_path / "results" / "leaderboard.csv",
        [
            {"round_id": round_path.name, "model_id": "model-a", "provider": "openai", "selected_option_id": "TECHNOLOGY", "confidence": 0.7, "portfolio_return": 0.06, "selected_asset_return": 0.1, "sp500_return": 0.02, "alpha_vs_sp500": 0.04, "regret_vs_best_option": 0.04, "rank_among_options": 1, "holding_count": 2, "beats_sp500": True, "beats_cash": True},
            {"round_id": round_path.name, "model_id": "model-b", "provider": "openai", "selected_option_id": "BONDS", "confidence": 0.4, "portfolio_return": -0.01, "selected_asset_return": -0.01, "sp500_return": 0.02, "alpha_vs_sp500": -0.03, "regret_vs_best_option": 0.11, "rank_among_options": 4, "holding_count": 1, "beats_sp500": False, "beats_cash": False},
        ],
    )
    _write_csv(
        run_path / "results" / "allocations.csv",
        [
            {"round_id": round_path.name, "model_id": "model-a", "provider": "openai", "option_id": "TECHNOLOGY", "allocation_pct": 50, "allocation_rank": 1, "option_return": 0.1, "return_contribution": 0.05, "rationale": "Growth."},
            {"round_id": round_path.name, "model_id": "model-a", "provider": "openai", "option_id": "SP500", "allocation_pct": 50, "allocation_rank": 2, "option_return": 0.02, "return_contribution": 0.01, "rationale": "Benchmark."},
            {"round_id": round_path.name, "model_id": "model-b", "provider": "openai", "option_id": "BONDS", "allocation_pct": 100, "allocation_rank": 1, "option_return": -0.01, "return_contribution": -0.01, "rationale": "Defense."},
        ],
    )


def _write_round(rounds_dir: Path, round_id: str, *, resolved: bool) -> None:
    round_path = rounds_dir / round_id
    round_path.mkdir(parents=True)
    _write_yaml(
        round_path / "manifest.yaml",
        {
            "round_id": round_id,
            "title": round_id,
            "decision_date": "2026-01-01" if resolved else "2026-01-08",
            "decision_deadline": "2026-01-01T20:00:00Z" if resolved else "2026-01-08T20:00:00Z",
            "entry_date": "2026-01-01" if resolved else "2026-01-08",
            "exit_date": "2026-01-08" if resolved else "2026-01-15",
            "horizon": "one week",
            "submission_format": "portfolio",
        },
    )
    _write_yaml(round_path / "options.yaml", _options())
    _write_run(round_path, resolved=resolved)


def test_generate_and_validate_deterministic_insights(tmp_path: Path) -> None:
    repo_root = tmp_path
    rounds_dir = tmp_path / "rounds"
    _write_yaml(
        repo_root / "configs" / "asset_risk_model.yaml",
        {
            "version": "test",
            "assets": {
                "CASH": {"risk_on_loading": -1, "risk_score_1_5": 1, "regime_group": "liquidity_defensive"},
                "SP500": {"risk_on_loading": 0.35, "risk_score_1_5": 3, "regime_group": "broad_cyclical_equity"},
                "TECHNOLOGY": {"risk_on_loading": 0.75, "risk_score_1_5": 4, "regime_group": "growth_technology"},
                "BONDS": {"risk_on_loading": -0.55, "risk_score_1_5": 3, "regime_group": "duration_credit"},
            },
        },
    )
    _write_round(rounds_dir, "CB-2026-01-01-1W", resolved=True)
    _write_round(rounds_dir, "CB-2026-01-08-1W", resolved=False)

    input_output = build_insights_input(
        rounds_dir=rounds_dir,
        output_path=tmp_path / "input.json",
        run_date="2026-01-09",
        generated_at="2026-01-09T04:35:00Z",
        repo_root=repo_root,
    )
    assert input_output.round_count == 2
    assert input_output.portfolio_count == 4
    assert input_output.result_count == 2

    generated = generate_insights(input_path=input_output.output_path, output_dir=tmp_path / "insights")
    validated = validate_insights(insights_dir=tmp_path / "insights")

    assert generated.insight_count >= 4
    assert validated.insight_count == generated.insight_count
    latest = json.loads(generated.latest_path.read_text(encoding="utf-8"))
    categories = {row["category"] for row in latest["insights"]}
    assert "consensus_performance" in categories
    assert "benchmark_difficulty" in categories
    assert "current_positioning" in categories
    consensus = next(row for row in latest["insights"] if row["category"] == "consensus_performance")
    consensus_return = next(row for row in consensus["calculations"] if row["name"] == "consensus_portfolio_return")
    assert consensus_return["value"] == 2.5
    manifest = json.loads((generated.run_dir / "run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["llm_status"] == "not_configured"
    assert manifest["data_fingerprint"] == latest["source"]["data_fingerprint"]
    assert generated.published is True
    assert not (generated.run_dir / "llm_request.redacted.json").exists()


def test_generate_insights_skips_unchanged_benchmark_data_before_llm(tmp_path: Path) -> None:
    repo_root = tmp_path
    rounds_dir = tmp_path / "rounds"
    output_dir = tmp_path / "insights"
    _write_yaml(
        repo_root / "configs" / "asset_risk_model.yaml",
        {
            "version": "test",
            "assets": {
                "CASH": {"risk_on_loading": -1, "risk_score_1_5": 1, "regime_group": "liquidity_defensive"},
                "SP500": {"risk_on_loading": 0.35, "risk_score_1_5": 3, "regime_group": "broad_cyclical_equity"},
                "TECHNOLOGY": {"risk_on_loading": 0.75, "risk_score_1_5": 4, "regime_group": "growth_technology"},
                "BONDS": {"risk_on_loading": -0.55, "risk_score_1_5": 3, "regime_group": "duration_credit"},
            },
        },
    )
    _write_round(rounds_dir, "CB-2026-01-01-1W", resolved=True)
    _write_round(rounds_dir, "CB-2026-01-08-1W", resolved=False)

    first_input = build_insights_input(
        rounds_dir=rounds_dir,
        output_path=tmp_path / "first-input.json",
        run_date="2026-01-09",
        generated_at="2026-01-09T04:35:00Z",
        repo_root=repo_root,
    )
    first = generate_insights(input_path=first_input.output_path, output_dir=output_dir)
    first_latest = json.loads(first.latest_path.read_text(encoding="utf-8"))

    second_input = build_insights_input(
        rounds_dir=rounds_dir,
        output_path=tmp_path / "second-input.json",
        run_date="2026-01-10",
        generated_at="2026-01-10T06:12:00Z",
        repo_root=repo_root,
    )

    def unexpected_client(request_payload: dict) -> dict:
        raise AssertionError("LLM should not be called when benchmark data is unchanged")

    second = generate_insights(
        input_path=second_input.output_path,
        output_dir=output_dir,
        llm_mode="required",
        nvidia_api_key="test-key-not-written",
        llm_client=unexpected_client,
    )
    latest_after_skip = json.loads(first.latest_path.read_text(encoding="utf-8"))

    assert second.published is False
    assert second.skipped_reason == "data_unchanged"
    assert second.llm_status == "skipped_unchanged"
    assert second.data_fingerprint == first.data_fingerprint
    assert not second.run_dir.exists()
    assert latest_after_skip["generated_at"] == first_latest["generated_at"]
    assert latest_after_skip["source"]["data_fingerprint"] == first_latest["source"]["data_fingerprint"]


def test_generate_insights_applies_valid_nvidia_llm_rewrite(tmp_path: Path) -> None:
    repo_root = tmp_path
    rounds_dir = tmp_path / "rounds"
    _write_yaml(
        repo_root / "configs" / "asset_risk_model.yaml",
        {
            "version": "test",
            "assets": {
                "CASH": {"risk_on_loading": -1, "risk_score_1_5": 1, "regime_group": "liquidity_defensive"},
                "SP500": {"risk_on_loading": 0.35, "risk_score_1_5": 3, "regime_group": "broad_cyclical_equity"},
                "TECHNOLOGY": {"risk_on_loading": 0.75, "risk_score_1_5": 4, "regime_group": "growth_technology"},
                "BONDS": {"risk_on_loading": -0.55, "risk_score_1_5": 3, "regime_group": "duration_credit"},
            },
        },
    )
    _write_round(rounds_dir, "CB-2026-01-01-1W", resolved=True)
    _write_round(rounds_dir, "CB-2026-01-08-1W", resolved=False)
    input_output = build_insights_input(
        rounds_dir=rounds_dir,
        output_path=tmp_path / "input.json",
        run_date="2026-01-09",
        generated_at="2026-01-09T04:35:00Z",
        repo_root=repo_root,
    )
    captured: dict[str, object] = {}

    def fake_client(request_payload: dict) -> dict:
        captured["request"] = request_payload
        packet = json.loads(request_payload["messages"][1]["content"])
        candidate = packet["candidate_insights"][0]
        return {
            "id": "mock-nvidia-response",
            "model": request_payload["model"],
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {
                        "content": json.dumps(
                            {
                                "version": LLM_OUTPUT_VERSION,
                                "selected_candidate_ids": [candidate["id"]],
                                "rewrites": [
                                    {
                                        "candidate_id": candidate["id"],
                                        "title": "AI consensus portfolio result is clearer",
                                        "summary": candidate["summary"],
                                        "why_it_matters": candidate["why_it_matters"],
                                    }
                                ],
                                "rejected_candidate_ids": [],
                            }
                        )
                    },
                }
            ],
            "usage": {"prompt_tokens": 100, "completion_tokens": 40},
        }

    generated = generate_insights(
        input_path=input_output.output_path,
        output_dir=tmp_path / "insights",
        llm_mode="required",
        nvidia_api_key="test-key-not-written",
        llm_client=fake_client,
    )
    latest = json.loads(generated.latest_path.read_text(encoding="utf-8"))
    first = latest["insights"][0]
    manifest = json.loads((generated.run_dir / "run_manifest.json").read_text(encoding="utf-8"))
    redacted_request = json.loads((generated.run_dir / "llm_request.redacted.json").read_text(encoding="utf-8"))
    llm_response = json.loads((generated.run_dir / "llm_response.json").read_text(encoding="utf-8"))

    assert generated.llm_status == "succeeded"
    assert manifest["llm_status"] == "succeeded"
    assert manifest["llm_model"] == DEFAULT_NVIDIA_MODEL_ID
    assert first["source_type"] == "llm_assisted"
    assert first["title"] == "AI consensus portfolio result is clearer"
    assert first["llm_assisted_by"]["model"] == DEFAULT_NVIDIA_MODEL_ID
    assert redacted_request["authorization"] == "redacted"
    assert "test-key-not-written" not in json.dumps(redacted_request)
    assert llm_response["status"] == "succeeded"
    assert captured["request"]["model"] == DEFAULT_NVIDIA_MODEL_ID


def test_generate_insights_accepts_compact_nvidia_rewrite_output(tmp_path: Path) -> None:
    repo_root = tmp_path
    rounds_dir = tmp_path / "rounds"
    _write_yaml(
        repo_root / "configs" / "asset_risk_model.yaml",
        {
            "version": "test",
            "assets": {
                "CASH": {"risk_on_loading": -1, "risk_score_1_5": 1, "regime_group": "liquidity_defensive"},
                "SP500": {"risk_on_loading": 0.35, "risk_score_1_5": 3, "regime_group": "broad_cyclical_equity"},
                "TECHNOLOGY": {"risk_on_loading": 0.75, "risk_score_1_5": 4, "regime_group": "growth_technology"},
                "BONDS": {"risk_on_loading": -0.55, "risk_score_1_5": 3, "regime_group": "duration_credit"},
            },
        },
    )
    _write_round(rounds_dir, "CB-2026-01-01-1W", resolved=True)
    input_output = build_insights_input(
        rounds_dir=rounds_dir,
        output_path=tmp_path / "input.json",
        run_date="2026-01-09",
        generated_at="2026-01-09T04:35:00Z",
        repo_root=repo_root,
    )

    def fake_client(request_payload: dict) -> dict:
        packet = json.loads(request_payload["messages"][1]["content"])
        candidate = packet["candidate_insights"][0]
        return {
            "choices": [
                {
                    "message": {
                        "content": json.dumps(
                            {
                                "rewrites": [
                                    {
                                        "candidate_id": candidate["id"],
                                        "title": "Compact NVIDIA rewrite accepted",
                                    }
                                ]
                            }
                        )
                    }
                }
            ]
        }

    generated = generate_insights(
        input_path=input_output.output_path,
        output_dir=tmp_path / "insights",
        llm_mode="required",
        nvidia_api_key="test-key-not-written",
        llm_client=fake_client,
    )
    latest = json.loads(generated.latest_path.read_text(encoding="utf-8"))
    llm_response = json.loads((generated.run_dir / "llm_response.json").read_text(encoding="utf-8"))

    assert generated.llm_status == "succeeded"
    assert latest["insights"][0]["title"] == "Compact NVIDIA rewrite accepted"
    assert llm_response["output"]["version"] == LLM_OUTPUT_VERSION
    assert llm_response["output"]["selected_candidate_ids"] == [latest["insights"][0]["id"]]


def test_generate_insights_falls_back_when_llm_introduces_unsupported_number(tmp_path: Path) -> None:
    repo_root = tmp_path
    rounds_dir = tmp_path / "rounds"
    _write_yaml(
        repo_root / "configs" / "asset_risk_model.yaml",
        {
            "version": "test",
            "assets": {
                "CASH": {"risk_on_loading": -1, "risk_score_1_5": 1, "regime_group": "liquidity_defensive"},
                "SP500": {"risk_on_loading": 0.35, "risk_score_1_5": 3, "regime_group": "broad_cyclical_equity"},
                "TECHNOLOGY": {"risk_on_loading": 0.75, "risk_score_1_5": 4, "regime_group": "growth_technology"},
                "BONDS": {"risk_on_loading": -0.55, "risk_score_1_5": 3, "regime_group": "duration_credit"},
            },
        },
    )
    _write_round(rounds_dir, "CB-2026-01-01-1W", resolved=True)
    _write_round(rounds_dir, "CB-2026-01-08-1W", resolved=False)
    input_output = build_insights_input(
        rounds_dir=rounds_dir,
        output_path=tmp_path / "input.json",
        run_date="2026-01-09",
        generated_at="2026-01-09T04:35:00Z",
        repo_root=repo_root,
    )

    def fake_client(request_payload: dict) -> dict:
        packet = json.loads(request_payload["messages"][1]["content"])
        candidate = packet["candidate_insights"][0]
        return {
            "choices": [
                {
                    "message": {
                        "content": json.dumps(
                            {
                                "version": LLM_OUTPUT_VERSION,
                                "selected_candidate_ids": [candidate["id"]],
                                "rewrites": [
                                    {
                                        "candidate_id": candidate["id"],
                                        "title": "AI consensus portfolio jumped 999%",
                                    }
                                ],
                                "rejected_candidate_ids": [],
                            }
                        )
                    }
                }
            ]
        }

    generated = generate_insights(
        input_path=input_output.output_path,
        output_dir=tmp_path / "insights",
        llm_mode="auto",
        nvidia_api_key="test-key-not-written",
        llm_client=fake_client,
    )
    latest = json.loads(generated.latest_path.read_text(encoding="utf-8"))
    manifest = json.loads((generated.run_dir / "run_manifest.json").read_text(encoding="utf-8"))

    assert generated.llm_status == "failed"
    assert manifest["llm_status"] == "failed"
    assert "unsupported number" in manifest["llm_error"]
    assert latest["source"]["type"] == "deterministic"
    assert latest["insights"][0]["source_type"] == "deterministic"

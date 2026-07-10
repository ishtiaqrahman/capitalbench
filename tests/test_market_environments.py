from __future__ import annotations

from capitalbench import insights as insights_module
from capitalbench.insights import build_deterministic_candidates
from capitalbench.market_environments import (
    build_market_environment,
    classify_market_direction,
    classify_market_environment,
)


def _round(
    *,
    track: str,
    index: int,
    sp500_return: float,
    model_returns: dict[str, float],
) -> dict:
    suffix = "1W" if track == "weekly" else "1M"
    day = index + 1
    round_id = f"CB-2026-01-{day:02d}-{suffix}"
    results = [
        {
            "round_id": round_id,
            "model_id": model_id,
            "provider": model_id.split("-", 1)[0],
            "portfolio_return": portfolio_return,
            "sp500_return": sp500_return,
            "alpha_vs_sp500": portfolio_return - sp500_return,
        }
        for model_id, portfolio_return in model_returns.items()
    ]
    return {
        "round_id": round_id,
        "run_id": "official",
        "track": track,
        "status": "resolved",
        "decision_date": f"2026-01-{day:02d}",
        "entry_date": f"2026-01-{day:02d}",
        "exit_date": f"2026-02-{day:02d}",
        "allocations": [],
        "interim_performance": [],
        "options": [],
        "portfolios": [],
        "results": results,
        "returns": [
            {"option_id": "SP500", "is_benchmark": True, "return": sp500_return},
            {"option_id": "ORACLE", "is_benchmark": False, "return": 0.10},
        ],
        "trailing_returns": [],
    }


def _snapshot(rounds: list[dict]) -> dict:
    return {
        "version": "test_input_v1",
        "generated_at": "2026-03-01T00:00:00Z",
        "run_date": "2026-03-01",
        "asset_risk_model": {},
        "rounds": rounds,
    }


def test_market_environment_threshold_boundaries() -> None:
    assert classify_market_environment("weekly", -0.02) == "sharp_down"
    assert classify_market_environment("weekly", -0.005) == "flat"
    assert classify_market_environment("weekly", 0.005) == "flat"
    assert classify_market_environment("weekly", 0.02) == "sharp_up"
    assert classify_market_environment("monthly", -0.03) == "sharp_down"
    assert classify_market_environment("monthly", -0.01) == "flat"
    assert classify_market_environment("monthly", 0.01) == "flat"
    assert classify_market_environment("monthly", 0.03) == "sharp_up"
    assert classify_market_direction("weekly", -0.0051) == "down"
    assert classify_market_direction("weekly", 0.005) == "flat"
    assert classify_market_direction("monthly", 0.0101) == "up"


def test_late_participant_cannot_inherit_ready_bucket_status() -> None:
    rounds = [
        _round(
            track="weekly",
            index=index,
            sp500_return=0.0,
            model_returns={"model-steady": 0.01, "model-peer": 0.005},
        )
        for index in range(4)
    ]
    rounds[-1]["results"].append(
        {
            "round_id": rounds[-1]["round_id"],
            "model_id": "model-late",
            "provider": "test",
            "portfolio_return": 0.08,
            "sp500_return": 0.0,
            "alpha_vs_sp500": 0.08,
        }
    )

    market = build_market_environment(_snapshot(rounds))
    flat_bucket = next(row for row in market["tracks"]["weekly"]["directions"] if row["key"] == "flat")
    flat_signal = next(row for row in market["tracks"]["weekly"]["signals"] if row["key"] == "weekly-flat-leader")

    assert flat_bucket["status"] == "ready"
    assert flat_signal["model"]["model_id"] == "model-steady"
    assert flat_signal["model"]["tests"] == 4
    assert "model-late" not in flat_bucket["comparison"]["eligible_model_ids"]
    assert flat_signal["maturity"] == "ready"
    assert flat_signal["confidence"] == "medium"


def test_ready_direction_and_split_require_model_observations() -> None:
    rounds = []
    for index in range(3):
        rounds.append(
            _round(
                track="weekly",
                index=index,
                sp500_return=-0.01,
                model_returns={"model-a": 0.02, "model-b": -0.01},
            )
        )
    for index in range(3, 6):
        rounds.append(
            _round(
                track="weekly",
                index=index,
                sp500_return=0.01,
                model_returns={"model-a": -0.01, "model-b": 0.03},
            )
        )
    rounds.append(
        _round(track="weekly", index=6, sp500_return=0.0, model_returns={"model-a": -0.08})
    )

    market = build_market_environment(_snapshot(rounds))
    signals = {row["key"]: row for row in market["tracks"]["weekly"]["signals"]}

    assert signals["weekly-down-leader"]["maturity"] == "ready"
    assert signals["weekly-up-leader"]["maturity"] == "ready"
    assert signals["weekly-down-leader"]["confidence"] == "medium"
    assert signals["weekly-up-leader"]["confidence"] == "medium"
    assert signals["weekly-split"]["maturity"] == "ready"
    assert signals["weekly-synthesis"]["model_ids"] == ["model-a", "model-b"]
    assert signals["weekly-steady"]["candidate"]["directions_covered"] == 2
    assert "flat" not in signals["weekly-steady"]["candidate"]["direction_tests"]


def test_market_environment_candidates_have_structured_context() -> None:
    rounds = []
    for index in range(3):
        rounds.append(
            _round(
                track="weekly",
                index=index,
                sp500_return=-0.01,
                model_returns={"model-a": 0.02, "model-b": 0.0},
            )
        )
    for index in range(3, 6):
        rounds.append(
            _round(
                track="weekly",
                index=index,
                sp500_return=0.01,
                model_returns={"model-a": 0.0, "model-b": 0.03},
            )
        )
    snapshot = _snapshot(rounds)
    candidates = build_deterministic_candidates(snapshot)
    market_rows = [row for row in candidates if row["category"] == "market_environment"]
    synthesis = next(row for row in market_rows if row["context"].get("insight_kind") == "synthesis")

    assert synthesis["id"] == "market-environment-weekly-synthesis"
    assert synthesis["confidence"] == "medium"
    assert synthesis["context"]["scope"] == "resolved_history"
    assert synthesis["context"]["model_ids"] == ["model-a", "model-b"]
    assert synthesis["evidence"][0]["href"].endswith("#market-environment-insight-weekly-synthesis")


def test_build_fingerprint_changes_with_engine_version_but_data_fingerprint_does_not(monkeypatch) -> None:
    snapshot = _snapshot([])
    data_fingerprint = insights_module._snapshot_data_fingerprint(snapshot)
    llm_config = {"mode": "off", "enabled": False}
    before = insights_module._snapshot_build_fingerprint(
        data_fingerprint=data_fingerprint, llm_config=llm_config
    )
    monkeypatch.setattr(insights_module, "DETERMINISTIC_ENGINE_VERSION", "deterministic_insights_test")
    after_data = insights_module._snapshot_data_fingerprint(snapshot)
    after = insights_module._snapshot_build_fingerprint(
        data_fingerprint=after_data, llm_config=llm_config
    )

    assert data_fingerprint == after_data
    assert before != after


def test_shared_comparison_uses_identical_rounds_for_every_model() -> None:
    rounds = []
    for index in range(6):
        model_returns = {"model-a": 0.01, "model-b": 0.005}
        if index >= 3:
            model_returns["model-late"] = 0.02
        rounds.append(_round(track="weekly", index=index, sp500_return=0.0, model_returns=model_returns))

    market = build_market_environment(_snapshot(rounds))
    flat = next(row for row in market["tracks"]["weekly"]["directions"] if row["key"] == "flat")
    comparison = flat["comparison"]

    assert comparison["status"] == "ready"
    assert comparison["round_count"] == 3
    assert comparison["confidence"] == "medium"
    assert {tuple(row["round_ids"]) for row in comparison["model_rows"]} == {
        tuple(comparison["round_ids"])
    }
    assert {row["tests"] for row in comparison["model_rows"]} == {3}


def test_high_confidence_requires_established_stable_leadership() -> None:
    rounds = [
        _round(
            track="weekly",
            index=index,
            sp500_return=0.0,
            model_returns={"model-a": 0.03, "model-b": 0.0},
        )
        for index in range(6)
    ]

    market = build_market_environment(_snapshot(rounds))
    flat = next(row for row in market["tracks"]["weekly"]["directions"] if row["key"] == "flat")

    assert flat["comparison"]["confidence"] == "high"
    assert flat["comparison"]["leave_one_out_stability"] == 1.0
    assert flat["comparison"]["leader_margin_ci_95_low"] > 0

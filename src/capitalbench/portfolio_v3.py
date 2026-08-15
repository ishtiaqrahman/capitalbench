from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from .io import load_options
from .methodology import PORTFOLIO_V3_VERSION

DEFAULT_BENCHMARK_OPTION_ID = "SP500"
DEFAULT_MINIMUM_BEAT_SPY_PROBABILITY_PCT = 55.0
DEFAULT_SLOT_WEIGHTS_PCT = (35.0, 35.0, 30.0)
OVERREACTION = "overreaction"
MAXIMUM_WILDCARDS = 2
V3_LANES = (
    "shock_reversal",
    "medium_strength",
    "short_continuation",
    "quality_pullback",
    "volume_dislocation",
    "benchmark",
    "wildcard",
)
V3_MECHANISMS = ("continuation", "reversal", "catalyst", "defensive", "no_edge")
V3_RECENT_INTERPRETATIONS = (
    OVERREACTION,
    "fundamental_deterioration",
    "supported_continuation",
    "no_edge",
)
V3_SLATE_COUNTS = {
    "shock_reversal": 5,
    "medium_strength": 3,
    "short_continuation": 2,
    "quality_pullback": 3,
    "volume_dislocation": 2,
}


def build_portfolio_v3_candidate_slate(round_path: Path) -> list[dict[str, Any]]:
    """Build the frozen V3 search slate from entry-time round data."""

    context_path = round_path / "market_data" / "universe_decision_context.csv"
    quality_path = round_path / "market_data" / "universe_quality_evidence.json"
    with context_path.open(encoding="utf-8-sig", newline="") as handle:
        context_rows = list(csv.DictReader(handle))
    if not context_rows:
        raise ValueError(f"empty V3 decision context: {context_path}")
    quality_payload = json.loads(quality_path.read_text(encoding="utf-8"))
    coverage = float(quality_payload.get("coverage") or 0.0)
    if coverage < 0.90:
        raise ValueError(f"V3 quality-evidence coverage must be at least 90%: {coverage:.1%}")
    quality = {
        str(row["option_id"]): float(row["quality_evidence_score"])
        for row in quality_payload.get("rows", [])
    }
    options = {option.option_id: option for option in load_options(round_path)}
    active_rows = [
        row for row in context_rows if str(row.get("option_id")) not in {"CASH", "SP500"}
    ]
    metrics = _metric_profile(context_rows)
    lanes = {
        "shock_reversal": _ranked_option_ids(
            active_rows,
            metrics["active_return"],
            V3_SLATE_COUNTS["shock_reversal"],
            reverse=False,
        ),
        "medium_strength": _ranked_option_ids(
            active_rows,
            metrics["prior_active_return"],
            V3_SLATE_COUNTS["medium_strength"],
            reverse=True,
        ),
        "short_continuation": _ranked_option_ids(
            active_rows,
            metrics["active_return"],
            V3_SLATE_COUNTS["short_continuation"],
            reverse=True,
        ),
        "quality_pullback": [
            option_id
            for option_id in sorted(quality, key=lambda value: (-quality[value], value))
            if option_id not in {"CASH", "SP500"}
        ][: V3_SLATE_COUNTS["quality_pullback"]],
        "volume_dislocation": _ranked_option_ids(
            active_rows,
            metrics["volume_zscore"],
            V3_SLATE_COUNTS["volume_dislocation"],
            reverse=True,
            absolute=True,
        ),
    }
    memberships: dict[str, list[str]] = defaultdict(list)
    ordered_ids: list[str] = []
    for lane in V3_SLATE_COUNTS:
        for option_id in lanes[lane]:
            memberships[option_id].append(lane)
            if option_id not in ordered_ids:
                ordered_ids.append(option_id)
    ordered_ids.append(DEFAULT_BENCHMARK_OPTION_ID)
    memberships[DEFAULT_BENCHMARK_OPTION_ID] = ["benchmark"]

    context = {str(row["option_id"]): row for row in context_rows}
    missing = sorted(set(ordered_ids) - set(context))
    if missing:
        raise ValueError(f"V3 candidate data is missing: {', '.join(missing)}")
    slate: list[dict[str, Any]] = []
    for option_id in ordered_ids:
        row = context[option_id]
        option = options[option_id]
        slate.append(
            {
                "option_id": option_id,
                "symbol": option.symbol or "",
                "name": option.name,
                "economic_exposure_cluster": row.get("economic_exposure_cluster") or "",
                "risk_bucket": option.risk_bucket,
                "origin_lanes": memberships[option_id],
                "metric_profile": metrics["profile"],
                "recent_return_pct": _percentage(row, metrics["recent_return"]),
                "recent_active_return_pct": _percentage(row, metrics["active_return"]),
                "prior_active_return_pct": _percentage(row, metrics["prior_active_return"]),
                "volatility_pct": _percentage(row, metrics["volatility"]),
                "max_drawdown_pct": _percentage(row, metrics["max_drawdown"]),
                "volume_zscore": _number(row, metrics["volume_zscore"]),
                "corr_spy": _number(row, metrics["corr_spy"]),
                "beta_spy": _number(row, metrics["beta_spy"]),
                "distance_52w_high_pct": _percentage(row, "distance_52w_high"),
                "quality_evidence_score": quality.get(option_id),
            }
        )
    if not 10 <= len(slate) <= 16:
        raise ValueError(f"unexpected V3 candidate slate size: {len(slate)}")
    return slate


def render_portfolio_v3_candidate_slate(slate: Sequence[Mapping[str, Any]]) -> str:
    headers = (
        "option_id",
        "symbol",
        "name",
        "origin_lanes",
        "profile",
        "recent return %",
        "recent active %",
        "prior active %",
        "horizon vol %",
        "horizon max drawdown %",
        "volume z",
        "SPY corr",
        "SPY beta",
        "52w-high distance %",
        "quality score",
    )
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in slate:
        values = (
            row["option_id"],
            row["symbol"],
            row["name"],
            ",".join(str(value) for value in row["origin_lanes"]),
            row.get("metric_profile"),
            _display(row.get("recent_return_pct")),
            _display(row.get("recent_active_return_pct")),
            _display(row.get("prior_active_return_pct")),
            _display(row.get("volatility_pct")),
            _display(row.get("max_drawdown_pct")),
            _display(row.get("volume_zscore")),
            _display(row.get("corr_spy")),
            _display(row.get("beta_spy")),
            _display(row.get("distance_52w_high_pct")),
            _display(row.get("quality_evidence_score"), digits=3),
        )
        lines.append("| " + " | ".join(str(value).replace("|", "\\|") for value in values) + " |")
    return "\n".join(lines)


def materialize_portfolio_v3_submission(
    payload: Mapping[str, Any],
    *,
    round_id: str,
    model_id: str,
    provider: str,
    mode: str,
    candidate_slate: Sequence[Mapping[str, Any]],
    allowed_option_ids: Sequence[str],
) -> dict[str, Any]:
    """Validate one V3 judgment and materialize its deterministic scored portfolio."""

    normalized = json.loads(json.dumps(payload))
    _validate_v3_response(
        normalized,
        round_id=round_id,
        model_id=model_id,
        provider=provider,
        mode=mode,
        candidate_slate=candidate_slate,
        allowed_option_ids=allowed_option_ids,
    )
    assessments = list(normalized["candidate_assessments"])
    built = build_portfolio_v3_allocation(assessments)
    by_id = {str(row["option_id"]): row for row in assessments}
    portfolio: list[dict[str, Any]] = []
    for option_id, allocation_pct in built["allocation_pct"].items():
        if option_id == DEFAULT_BENCHMARK_OPTION_ID:
            rationale = "Deterministic SPY fallback for V3 slots without an eligible active candidate."
        else:
            assessment = by_id[option_id]
            rationale = (
                f"V3 selected model rank {assessment['rank']}: overreaction with "
                f"{float(assessment['p_beat_spy_pct']):g}% estimated probability of beating SPY."
            )
        portfolio.append(
            {
                "option_id": option_id,
                "allocation_pct": int(round(float(allocation_pct))),
                "rationale": rationale,
            }
        )
    selected = [by_id[option_id] for option_id in built["selected_active_option_ids"]]
    confidence = (
        sum(float(row["p_beat_spy_pct"]) for row in selected) / len(selected) / 100.0
        if selected
        else 0.5
    )
    return {
        "round_id": round_id,
        "model_id": model_id,
        "provider": provider,
        "mode": mode,
        "portfolio": portfolio,
        "confidence": round(confidence, 4),
        "portfolio_rationale": str(normalized["portfolio_rationale"]).strip(),
        "rationale_summary": str(normalized["market_rationale"]).strip(),
        "key_risks": [str(value).strip() for value in normalized["key_risks"]],
        "metadata": {
            "portfolio_v3": {
                "methodology_version": PORTFOLIO_V3_VERSION,
                "candidate_slate_option_ids": [str(row["option_id"]) for row in candidate_slate],
                "candidate_assessments": assessments,
                "top3_option_ids": list(normalized["top3_option_ids"]),
                "prefer_spy": bool(normalized["prefer_spy"]),
                "dispersion_state": normalized["dispersion_state"],
                "dominant_pattern": normalized["dominant_pattern"],
                "market_rationale": normalized["market_rationale"],
                "deterministic_allocation": built,
                "confidence_derivation": (
                    "mean selected-active p_beat_spy_pct; 0.5 when all slots fall back to SPY"
                ),
            }
        },
    }


def build_portfolio_v3_allocation(
    assessments: Sequence[Mapping[str, Any]],
    *,
    benchmark_option_id: str = DEFAULT_BENCHMARK_OPTION_ID,
    minimum_beat_spy_probability_pct: float = DEFAULT_MINIMUM_BEAT_SPY_PROBABILITY_PCT,
    slot_weights_pct: Sequence[float] = DEFAULT_SLOT_WEIGHTS_PCT,
) -> dict[str, Any]:
    """Build the fixed V3 candidate portfolio from one model response.

    A non-benchmark option is eligible only when the model classifies its recent
    move as an overreaction and assigns at least the fixed probability hurdle of
    beating SPY. Eligible options keep the model's rank. SPY fills every unused
    slot, so abstention cannot create avoidable benchmark underperformance.
    """

    weights = _validated_weights(slot_weights_pct)
    threshold = float(minimum_beat_spy_probability_pct)
    if not math.isfinite(threshold) or not 0.0 <= threshold <= 100.0:
        raise ValueError("minimum_beat_spy_probability_pct must be between 0 and 100")
    if not benchmark_option_id.strip():
        raise ValueError("benchmark_option_id must not be empty")

    normalized = [_normalize_assessment(row) for row in assessments]
    _validate_unique_fields(normalized)
    ordered = sorted(normalized, key=lambda row: row["rank"])

    decisions: list[dict[str, Any]] = []
    eligible: list[dict[str, Any]] = []
    for row in ordered:
        reason = _eligibility_reason(row, benchmark_option_id, threshold)
        decision = {
            **row,
            "eligible": reason == "eligible",
            "selected": False,
            "reason": reason,
        }
        decisions.append(decision)
        if decision["eligible"]:
            eligible.append(decision)

    selected = eligible[: len(weights)]
    selected_ids = [str(row["option_id"]) for row in selected]
    selected_set = set(selected_ids)
    for decision in decisions:
        if decision["option_id"] in selected_set:
            decision["selected"] = True
        elif decision["eligible"]:
            decision["reason"] = "outside_available_slots"

    allocation: dict[str, float] = {}
    for index, weight in enumerate(weights):
        option_id = selected_ids[index] if index < len(selected_ids) else benchmark_option_id
        allocation[option_id] = allocation.get(option_id, 0.0) + weight

    if not math.isclose(sum(allocation.values()), 100.0, abs_tol=1e-9):
        raise ValueError("slot_weights_pct must sum to 100")

    return {
        "methodology_version": PORTFOLIO_V3_VERSION,
        "benchmark_option_id": benchmark_option_id,
        "minimum_beat_spy_probability_pct": threshold,
        "slot_weights_pct": list(weights),
        "selected_active_option_ids": selected_ids,
        "allocation_pct": allocation,
        "decisions": decisions,
    }


def _validate_v3_response(
    payload: Mapping[str, Any],
    *,
    round_id: str,
    model_id: str,
    provider: str,
    mode: str,
    candidate_slate: Sequence[Mapping[str, Any]],
    allowed_option_ids: Sequence[str],
) -> None:
    expected_identifiers = {
        "round_id": round_id,
        "model_id": model_id,
        "provider": provider,
        "mode": mode,
    }
    for field, expected in expected_identifiers.items():
        if payload.get(field) != expected:
            raise ValueError(f"V3 {field} mismatch: {payload.get(field)!r} != {expected!r}")
    for field in (
        "dispersion_state",
        "dominant_pattern",
        "market_rationale",
        "candidate_assessments",
        "top3_option_ids",
        "prefer_spy",
        "portfolio_rationale",
        "key_risks",
    ):
        if field not in payload:
            raise ValueError(f"V3 response requires {field}")
    if payload["dispersion_state"] not in {"low", "normal", "high"}:
        raise ValueError("invalid V3 dispersion_state")
    if payload["dominant_pattern"] not in {"continuation", "reversal", "mixed"}:
        raise ValueError("invalid V3 dominant_pattern")
    if not isinstance(payload["prefer_spy"], bool):
        raise ValueError("V3 prefer_spy must be a boolean")
    if not str(payload["market_rationale"]).strip() or not str(payload["portfolio_rationale"]).strip():
        raise ValueError("V3 rationales must not be blank")
    risks = payload["key_risks"]
    if not isinstance(risks, list) or not 2 <= len(risks) <= 5 or any(
        not str(value).strip() for value in risks
    ):
        raise ValueError("V3 key_risks must contain 2-5 non-empty items")

    assessments = payload["candidate_assessments"]
    if not isinstance(assessments, list):
        raise ValueError("V3 candidate_assessments must be an array")
    expected_lanes = {
        str(row["option_id"]): [str(value) for value in row["origin_lanes"]]
        for row in candidate_slate
    }
    if not len(expected_lanes) <= len(assessments) <= len(expected_lanes) + MAXIMUM_WILDCARDS:
        raise ValueError(
            "V3 candidate_assessments must contain the complete deterministic slate "
            f"and at most {MAXIMUM_WILDCARDS} wildcards"
        )
    allowed = set(str(value) for value in allowed_option_ids) - {"CASH"}
    ids: list[str] = []
    ranks: list[int] = []
    for assessment in assessments:
        if not isinstance(assessment, dict):
            raise ValueError("every V3 candidate assessment must be an object")
        option_id = str(assessment.get("option_id") or "").strip()
        ids.append(option_id)
        if option_id not in allowed:
            raise ValueError(f"V3 assessment contains invalid option_id: {option_id}")
        origins = assessment.get("origin_lanes")
        required_origins = expected_lanes.get(option_id, ["wildcard"])
        if not isinstance(origins, list) or sorted(str(value) for value in origins) != sorted(required_origins):
            raise ValueError(f"V3 origin_lanes mismatch for {option_id}")
        mechanism = assessment.get("mechanism")
        interpretation = assessment.get("recent_return_interpretation")
        if mechanism not in V3_MECHANISMS:
            raise ValueError(f"invalid V3 mechanism for {option_id}")
        if interpretation not in V3_RECENT_INTERPRETATIONS:
            raise ValueError(f"invalid V3 recent-return interpretation for {option_id}")
        rank = int(assessment.get("rank"))
        ranks.append(rank)
        probability = float(assessment.get("p_beat_spy_pct"))
        top3_probability = float(assessment.get("p_top3_pct"))
        if not 0 <= probability <= 100 or not 0 <= top3_probability <= 100:
            raise ValueError(f"V3 probabilities must be between 0 and 100 for {option_id}")
        low = float(assessment.get("excess_return_p10_pct"))
        median = float(assessment.get("excess_return_p50_pct"))
        high = float(assessment.get("excess_return_p90_pct"))
        if not low <= median <= high:
            raise ValueError(f"V3 excess-return quantiles are out of order for {option_id}")
        evidence = assessment.get("evidence")
        if not isinstance(evidence, list) or not 1 <= len(evidence) <= 3 or any(
            not str(value).strip() for value in evidence
        ):
            raise ValueError(f"V3 evidence must contain 1-3 non-empty items for {option_id}")
        if any(
            marker in str(value).lower()
            for value in evidence
            for marker in ("http://", "https://", "www.")
        ):
            raise ValueError(f"V3 evidence must not contain URLs for {option_id}")
    if len(ids) != len(set(ids)):
        raise ValueError("V3 candidate option IDs must be unique")
    missing = sorted(set(expected_lanes) - set(ids))
    if missing:
        raise ValueError(f"V3 response is missing slate candidates: {', '.join(missing)}")
    if sorted(ranks) != list(range(1, len(assessments) + 1)):
        raise ValueError("V3 candidate ranks must be contiguous and unique")
    ranked_top3 = [
        str(row["option_id"])
        for row in sorted(assessments, key=lambda row: int(row["rank"]))[:3]
    ]
    if payload["top3_option_ids"] != ranked_top3:
        raise ValueError("V3 top3_option_ids must equal candidate ranks 1-3")


def _number(row: Mapping[str, Any], key: str) -> float | None:
    value = row.get(key)
    if value in {None, ""}:
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _metric_profile(rows: Sequence[Mapping[str, Any]]) -> dict[str, str]:
    columns = set(rows[0]) if rows else set()
    if "active_return_5s" in columns:
        return {
            "profile": "weekly",
            "recent_return": "return_3s",
            "active_return": "active_return_5s",
            "prior_active_return": "prior_16s_active_return",
            "volatility": "volatility_21s",
            "max_drawdown": "max_drawdown_21s",
            "volume_zscore": "volume_zscore_5v60",
            "corr_spy": "corr_spy_63s",
            "beta_spy": "beta_spy_63s",
        }
    if "active_return_21s" in columns:
        return {
            "profile": "monthly",
            "recent_return": "return_5s",
            "active_return": "active_return_21s",
            "prior_active_return": "prior_105s_active_return",
            "volatility": "volatility_63s",
            "max_drawdown": "max_drawdown_63s",
            "volume_zscore": "volume_zscore_20v120",
            "corr_spy": "corr_spy_252s",
            "beta_spy": "beta_spy_252s",
        }
    raise ValueError("V3 decision context does not match a weekly or monthly metric profile")


def _percentage(row: Mapping[str, Any], key: str) -> float | None:
    value = _number(row, key)
    return None if value is None else value * 100.0


def _ranked_option_ids(
    rows: Sequence[Mapping[str, Any]],
    key: str,
    count: int,
    *,
    reverse: bool,
    absolute: bool = False,
) -> list[str]:
    present = [row for row in rows if _number(row, key) is not None]
    ordered = sorted(
        present,
        key=lambda row: (
            abs(float(row[key])) if absolute else float(row[key]),
            str(row["option_id"]),
        ),
        reverse=reverse,
    )
    return [str(row["option_id"]) for row in ordered[:count]]


def _display(value: Any, *, digits: int = 2) -> str:
    if value is None or value == "":
        return "n/a"
    return f"{float(value):.{digits}f}"


def _validated_weights(values: Sequence[float]) -> tuple[float, ...]:
    weights = tuple(float(value) for value in values)
    if not weights:
        raise ValueError("slot_weights_pct must contain at least one slot")
    if any(not math.isfinite(value) or value <= 0 for value in weights):
        raise ValueError("slot_weights_pct values must be finite and positive")
    if not math.isclose(sum(weights), 100.0, abs_tol=1e-9):
        raise ValueError("slot_weights_pct must sum to 100")
    return weights


def _normalize_assessment(row: Mapping[str, Any]) -> dict[str, Any]:
    option_id = str(row.get("option_id") or "").strip()
    if not option_id:
        raise ValueError("every assessment requires option_id")
    try:
        rank = int(row["rank"])
        probability = float(row["p_beat_spy_pct"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid rank or p_beat_spy_pct for {option_id}") from exc
    if rank < 1:
        raise ValueError(f"rank must be positive for {option_id}")
    if not math.isfinite(probability) or not 0.0 <= probability <= 100.0:
        raise ValueError(f"p_beat_spy_pct must be between 0 and 100 for {option_id}")
    interpretation = str(
        row.get("recent_return_interpretation") or row.get("thesis_type") or ""
    ).strip()
    if not interpretation:
        raise ValueError(f"recent_return_interpretation is required for {option_id}")
    return {
        "option_id": option_id,
        "rank": rank,
        "recent_return_interpretation": interpretation,
        "p_beat_spy_pct": probability,
    }


def _validate_unique_fields(rows: Sequence[Mapping[str, Any]]) -> None:
    option_ids = [str(row["option_id"]) for row in rows]
    ranks = [int(row["rank"]) for row in rows]
    if len(option_ids) != len(set(option_ids)):
        raise ValueError("assessment option_id values must be unique")
    if len(ranks) != len(set(ranks)):
        raise ValueError("assessment rank values must be unique")


def _eligibility_reason(
    row: Mapping[str, Any], benchmark_option_id: str, threshold: float
) -> str:
    if row["option_id"] == benchmark_option_id:
        return "benchmark_fallback"
    if row["recent_return_interpretation"] != OVERREACTION:
        return "not_overreaction"
    if float(row["p_beat_spy_pct"]) < threshold:
        return "below_probability_hurdle"
    return "eligible"

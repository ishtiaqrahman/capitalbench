from __future__ import annotations

import math
import statistics
from typing import Any


MARKET_ENVIRONMENT_VERSION = "capitalbench_market_environment_v1"
MARKET_ENVIRONMENT_ENGINE_VERSION = "market_environment_engine_v4"
READY_ROUND_THRESHOLD = 3
MODEL_READY_OBSERVATION_THRESHOLD = 3
BALANCED_SAMPLE_THRESHOLD = 3
ESTABLISHED_OBSERVATION_THRESHOLD = 6
STABILITY_THRESHOLD = 0.8
SCORE_EPSILON = 1e-7

TRACK_DEFINITIONS: dict[str, dict[str, list[dict[str, str]]]] = {
    "weekly": {
        "environments": [
            {"key": "sharp_down", "label": "Sharp Down", "range_label": "S&P <= -2.0%", "direction": "down"},
            {"key": "down", "label": "Down", "range_label": "-2.0% to -0.5%", "direction": "down"},
            {"key": "flat", "label": "Flat", "range_label": "-0.5% to +0.5%", "direction": "flat"},
            {"key": "up", "label": "Up", "range_label": "+0.5% to +2.0%", "direction": "up"},
            {"key": "sharp_up", "label": "Sharp Up", "range_label": "S&P >= +2.0%", "direction": "up"},
        ],
        "directions": [
            {"key": "down", "label": "Down", "range_label": "S&P < -0.5%"},
            {"key": "flat", "label": "Flat", "range_label": "-0.5% to +0.5%"},
            {"key": "up", "label": "Up", "range_label": "S&P > +0.5%"},
        ],
    },
    "monthly": {
        "environments": [
            {"key": "sharp_down", "label": "Sharp Down", "range_label": "S&P <= -3.0%", "direction": "down"},
            {"key": "down", "label": "Down", "range_label": "-3.0% to -1.0%", "direction": "down"},
            {"key": "flat", "label": "Flat", "range_label": "-1.0% to +1.0%", "direction": "flat"},
            {"key": "up", "label": "Up", "range_label": "+1.0% to +3.0%", "direction": "up"},
            {"key": "sharp_up", "label": "Sharp Up", "range_label": "S&P >= +3.0%", "direction": "up"},
        ],
        "directions": [
            {"key": "down", "label": "Down", "range_label": "S&P < -1.0%"},
            {"key": "flat", "label": "Flat", "range_label": "-1.0% to +1.0%"},
            {"key": "up", "label": "Up", "range_label": "S&P > +1.0%"},
        ],
    },
}


MODEL_LABELS = {
    "anthropic-claude-fable-5": "Claude Fable 5",
    "anthropic-claude-fable-5-1": "Claude Fable 5.1",
    "anthropic-claude-opus-4-7": "Claude Opus 4.7",
    "anthropic-claude-opus-4-8": "Claude Opus 4.8",
    "anthropic-claude-opus-5": "Claude Opus 5",
    "google-gemini-3-1-pro": "Gemini 3.1 Pro",
    "openai-gpt-5-5": "GPT-5.5",
    "openai-gpt-5-6-sol": "GPT-5.6 Sol",
    "xai-grok-4-3": "Grok 4.3",
    "xai-grok-4-5": "Grok 4.5",
    "xai-grok-4-6": "Grok 4.6",
}


def model_label(model_id: str) -> str:
    return MODEL_LABELS.get(model_id, model_id)


def classify_market_environment(track: str, sp500_return: float) -> str:
    if track == "weekly":
        if sp500_return <= -0.02:
            return "sharp_down"
        if sp500_return < -0.005:
            return "down"
        if sp500_return <= 0.005:
            return "flat"
        if sp500_return < 0.02:
            return "up"
        return "sharp_up"
    if track == "monthly":
        if sp500_return <= -0.03:
            return "sharp_down"
        if sp500_return < -0.01:
            return "down"
        if sp500_return <= 0.01:
            return "flat"
        if sp500_return < 0.03:
            return "up"
        return "sharp_up"
    raise ValueError(f"unsupported market-environment track: {track}")


def classify_market_direction(track: str, sp500_return: float) -> str:
    flat_limit = 0.005 if track == "weekly" else 0.01 if track == "monthly" else None
    if flat_limit is None:
        raise ValueError(f"unsupported market-environment track: {track}")
    if sp500_return < -flat_limit:
        return "down"
    if sp500_return <= flat_limit:
        return "flat"
    return "up"


def build_market_environment(snapshot: dict[str, Any], *, generated_at: str | None = None) -> dict[str, Any]:
    generated_at = generated_at or str(snapshot.get("generated_at") or "")
    resolved_rounds = [_normalize_round(row) for row in snapshot.get("rounds") or []]
    resolved_rounds = [row for row in resolved_rounds if row is not None]
    tracks = {track: _build_track(track, resolved_rounds) for track in ("weekly", "monthly")}
    data_as_of = max(
        (str(row.get("exit_date") or row.get("entry_date") or "") for row in resolved_rounds),
        default=generated_at[:10],
    )
    return {
        "version": MARKET_ENVIRONMENT_VERSION,
        "engine_version": MARKET_ENVIRONMENT_ENGINE_VERSION,
        "generated_at": generated_at,
        "data_as_of": data_as_of,
        "status": "ready" if resolved_rounds else "unavailable",
        "thresholds": {
            "environment_rounds": READY_ROUND_THRESHOLD,
            "model_observations": MODEL_READY_OBSERVATION_THRESHOLD,
            "balanced_sample_per_direction": BALANCED_SAMPLE_THRESHOLD,
            "established_observations": ESTABLISHED_OBSERVATION_THRESHOLD,
        },
        "definitions": TRACK_DEFINITIONS,
        "tracks": tracks,
        "source": {
            "type": "deterministic",
            "input_version": snapshot.get("version"),
            "capitalbench_generated_at": snapshot.get("generated_at"),
        },
    }


def _build_track(track: str, rounds: list[dict[str, Any]]) -> dict[str, Any]:
    track_rounds = sorted(
        (row for row in rounds if row["track"] == track),
        key=lambda row: (row.get("exit_date") or "", row["round_id"]),
    )
    environments = []
    for definition in TRACK_DEFINITIONS[track]["environments"]:
        selected = [row for row in track_rounds if row["environment_key"] == definition["key"]]
        environments.append(_bucket(definition, selected))

    directions = []
    for definition in TRACK_DEFINITIONS[track]["directions"]:
        selected = [row for row in track_rounds if row["direction_key"] == definition["key"]]
        directions.append(_bucket(definition, selected))

    raw_ready_environments = [row for row in environments if row["status"] == "ready"]
    ready_environments = [
        row for row in raw_ready_environments if row["comparison"]["status"] == "ready"
    ]
    has_ready_down = any(row["direction"] == "down" for row in ready_environments)
    has_ready_up = any(row["direction"] == "up" for row in ready_environments)
    if not ready_environments:
        confidence = {
            "status": "empty",
            "label": "No counting environments",
            "detail": "The benchmark will update after more resolved rounds exist.",
        }
    elif has_ready_down and has_ready_up:
        confidence = {
            "status": "ready",
            "label": "More balanced",
            "detail": f"{len(ready_environments)} environments count now, including up and down environments.",
        }
    else:
        suffix = "" if len(ready_environments) == 1 else "s"
        confidence = {
            "status": "forming",
            "label": "Still one-sided",
            "detail": f"{len(ready_environments)} environment{suffix} count now; more S&P 500 variety is needed.",
        }

    return {
        "track": track,
        "label": "Weekly" if track == "weekly" else "Monthly",
        "data_as_of": max((row.get("exit_date") or "" for row in track_rounds), default=""),
        "round_count": len(track_rounds),
        "raw_ready_environment_count": len(raw_ready_environments),
        "ready_environment_count": len(ready_environments),
        "confidence": confidence,
        "rounds": track_rounds,
        "environments": environments,
        "directions": directions,
        "regime_leaderboard": _regime_leaderboard(track_rounds, ready_environments),
        "balanced_sample": _balanced_sample(track, track_rounds),
        "signals": _signals(track, directions),
    }


def _normalize_round(raw: dict[str, Any]) -> dict[str, Any] | None:
    track = str(raw.get("track") or "")
    if raw.get("status") != "resolved" or track not in TRACK_DEFINITIONS:
        return None
    sp500_return = _sp500_return(raw)
    oracle_return = _oracle_return(raw.get("returns") or [])
    if sp500_return is None or oracle_return is None:
        return None
    environment_key = classify_market_environment(track, sp500_return)
    direction_key = classify_market_direction(track, sp500_return)
    results = []
    for result in raw.get("results") or []:
        portfolio_return = _number(result.get("portfolio_return"))
        if portfolio_return is None:
            portfolio_return = _number(result.get("selected_asset_return"))
        model_id = str(result.get("model_id") or "")
        if portfolio_return is None or not model_id:
            continue
        alpha = _number(result.get("alpha_vs_sp500"))
        if alpha is None:
            alpha = portfolio_return - sp500_return
        results.append(
            {
                "model_id": model_id,
                "model_label": model_label(model_id),
                "provider": str(result.get("provider") or ""),
                "portfolio_return": portfolio_return,
                "sp500_return": sp500_return,
                "alpha_vs_sp500": alpha,
                "beats_sp500": alpha > 0,
                "capitalbench_score": _capitalbench_score(portfolio_return, oracle_return),
            }
        )
    if not results:
        return None
    results.sort(key=lambda row: (-row["portfolio_return"], row["model_label"]))
    result_model_ids = sorted({row["model_id"] for row in results})
    expected_model_ids = sorted(
        {
            str(model_id)
            for model_id in raw.get("expected_model_ids") or []
            if str(model_id).strip()
        }
    )
    comparison_model_ids = expected_model_ids if len(expected_model_ids) >= 2 else result_model_ids
    model_roster_version = str(raw.get("model_roster_version") or "").strip()
    alphas = [row["alpha_vs_sp500"] for row in results]
    return {
        "round_id": str(raw.get("round_id") or ""),
        "track": track,
        "decision_date": str(raw.get("decision_date") or ""),
        "decision_deadline_utc": str(raw.get("decision_deadline_utc") or ""),
        "entry_date": str(raw.get("entry_date") or ""),
        "exit_date": str(raw.get("exit_date") or ""),
        "model_roster_version": model_roster_version or None,
        "expected_model_ids": expected_model_ids,
        "comparison_cohort_id": model_roster_version or f"observed:{'|'.join(comparison_model_ids)}",
        "comparison_cohort_source": "frozen_roster" if expected_model_ids else "observed_roster",
        "comparison_model_ids": comparison_model_ids,
        "environment_key": environment_key,
        "direction_key": direction_key,
        "sp500_return": sp500_return,
        "max_possible_return": oracle_return,
        "average_alpha": _average(alphas),
        "hit_rate": sum(1 for value in alphas if value > 0) / len(alphas),
        "model_count": len(results),
        "results": results,
    }


def _bucket(definition: dict[str, str], rounds: list[dict[str, Any]]) -> dict[str, Any]:
    status = "ready" if len(rounds) >= READY_ROUND_THRESHOLD else "forming" if rounds else "no_data"
    return {
        **definition,
        "count": len(rounds),
        "status": status,
        "average_sp500_return": _average([row["sp500_return"] for row in rounds]),
        "round_ids": [row["round_id"] for row in rounds],
        "model_rows": _model_rows(rounds),
        "comparison": _fair_comparison(rounds),
    }


def _fair_comparison(rounds: list[dict[str, Any]]) -> dict[str, Any]:
    candidates = [_comparison_candidate(rounds, cohort) for cohort in _comparison_cohorts(rounds)]
    ready_candidates = [row for row in candidates if row["round_count"] >= READY_ROUND_THRESHOLD]
    if ready_candidates:
        selected_candidate = max(
            ready_candidates,
            key=lambda row: (row["started_index"], len(row["model_ids"]), row["round_count"]),
        )
    elif candidates:
        selected_candidate = max(
            candidates,
            key=lambda row: (row["round_count"], row["started_index"], len(row["model_ids"])),
        )
    else:
        selected_candidate = None

    eligible_model_ids = list(selected_candidate["model_ids"]) if selected_candidate else []
    ordered_round_ids = list(selected_candidate["round_ids"]) if selected_candidate else []
    comparable = len(eligible_model_ids) >= 2 and bool(ordered_round_ids)
    ready = comparable and len(ordered_round_ids) >= READY_ROUND_THRESHOLD
    selected_round_ids = set(ordered_round_ids)
    selected_rounds = [row for row in rounds if row["round_id"] in selected_round_ids] if comparable else []
    model_rows = [
        row
        for row in _model_rows(selected_rounds)
        if row["model_id"] in set(eligible_model_ids) and row["tests"] == len(ordered_round_ids)
    ]
    leader = model_rows[0] if model_rows else None
    runner_up = model_rows[1] if len(model_rows) > 1 else None
    leader_returns = _model_returns(selected_rounds, leader["model_id"]) if leader else []
    runner_returns = _model_returns(selected_rounds, runner_up["model_id"]) if runner_up else []
    leader_standard_error = _standard_error(leader_returns)
    leader_margin = (
        float(leader["average_return"]) - float(runner_up["average_return"])
        if leader and runner_up and leader.get("average_return") is not None and runner_up.get("average_return") is not None
        else None
    )
    paired_margins = [left - right for left, right in zip(leader_returns, runner_returns)]
    margin_standard_error = _standard_error(paired_margins)
    leave_one_out_stability = _leave_one_out_stability(selected_rounds, leader["model_id"], eligible_model_ids) if leader else None
    margin_ci_low = (
        leader_margin - 1.96 * margin_standard_error
        if leader_margin is not None and margin_standard_error is not None
        else None
    )
    margin_ci_high = (
        leader_margin + 1.96 * margin_standard_error
        if leader_margin is not None and margin_standard_error is not None
        else None
    )
    established = bool(
        ready
        and len(ordered_round_ids) >= ESTABLISHED_OBSERVATION_THRESHOLD
        and leave_one_out_stability is not None
        and leave_one_out_stability >= STABILITY_THRESHOLD
        and margin_ci_low is not None
        and margin_ci_low > 0
    )
    return {
        "status": "ready" if ready else "forming",
        "confidence": "high" if established else "medium" if ready else "low",
        "round_ids": ordered_round_ids if comparable else [],
        "round_count": len(ordered_round_ids) if comparable else 0,
        "eligible_model_ids": eligible_model_ids,
        "eligible_model_count": len(eligible_model_ids),
        "cohort_id": selected_candidate.get("cohort_id") if selected_candidate else None,
        "cohort_source": selected_candidate.get("source") if selected_candidate else None,
        "cohort_started_round_id": (
            selected_candidate.get("started_round_id") if selected_candidate else None
        ),
        "model_rows": model_rows,
        "leader_model_id": leader.get("model_id") if leader else None,
        "runner_up_model_id": runner_up.get("model_id") if runner_up else None,
        "leader_margin": leader_margin,
        "leader_standard_error": leader_standard_error,
        "leader_ci_95_low": (
            float(leader["average_return"]) - 1.96 * leader_standard_error
            if leader and leader.get("average_return") is not None and leader_standard_error is not None
            else None
        ),
        "leader_ci_95_high": (
            float(leader["average_return"]) + 1.96 * leader_standard_error
            if leader and leader.get("average_return") is not None and leader_standard_error is not None
            else None
        ),
        "leader_margin_standard_error": margin_standard_error,
        "leader_margin_ci_95_low": margin_ci_low,
        "leader_margin_ci_95_high": margin_ci_high,
        "leave_one_out_stability": leave_one_out_stability,
        "established_observation_threshold": ESTABLISHED_OBSERVATION_THRESHOLD,
        "stability_threshold": STABILITY_THRESHOLD,
    }


def _comparison_cohorts(rounds: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cohorts: list[dict[str, Any]] = []
    for index, round_item in enumerate(rounds):
        model_ids = tuple(sorted(set(round_item.get("comparison_model_ids") or [])))
        if len(model_ids) < 2:
            continue
        cohort_id = str(
            round_item.get("comparison_cohort_id") or f"observed:{'|'.join(model_ids)}"
        )
        source = str(round_item.get("comparison_cohort_source") or "observed_roster")
        if source == "frozen_roster":
            if any(row["cohort_id"] == cohort_id for row in cohorts):
                continue
        elif any(set(row["model_ids"]).issuperset(model_ids) for row in cohorts):
            continue
        cohorts.append(
            {
                "cohort_id": cohort_id,
                "source": source,
                "model_ids": model_ids,
                "started_index": index,
                "started_round_id": round_item["round_id"],
            }
        )
    return cohorts


def _comparison_candidate(rounds: list[dict[str, Any]], cohort: dict[str, Any]) -> dict[str, Any]:
    required_model_ids = set(cohort["model_ids"])
    selected_rounds = []
    for index, round_item in enumerate(rounds):
        if index < cohort["started_index"]:
            continue
        result_model_ids = {row["model_id"] for row in round_item["results"]}
        if required_model_ids.issubset(result_model_ids):
            selected_rounds.append(round_item)
    return {
        **cohort,
        "round_ids": [row["round_id"] for row in selected_rounds],
        "round_count": len(selected_rounds),
    }


def _model_returns(rounds: list[dict[str, Any]], model_id: str) -> list[float]:
    values = []
    for round_item in rounds:
        result = next((row for row in round_item["results"] if row["model_id"] == model_id), None)
        if result is not None:
            values.append(float(result["portfolio_return"]))
    return values


def _standard_error(values: list[float]) -> float | None:
    if not values:
        return None
    if len(values) == 1:
        return 0.0
    return statistics.stdev(values) / math.sqrt(len(values))


def _leave_one_out_stability(
    rounds: list[dict[str, Any]], leader_model_id: str, eligible_model_ids: list[str]
) -> float | None:
    if len(rounds) < 2:
        return None
    stable = 0
    for omitted_index in range(len(rounds)):
        sample = [row for index, row in enumerate(rounds) if index != omitted_index]
        rows = [row for row in _model_rows(sample) if row["model_id"] in set(eligible_model_ids)]
        if rows and rows[0]["model_id"] == leader_model_id:
            stable += 1
    return stable / len(rounds)


def _model_rows(rounds: list[dict[str, Any]]) -> list[dict[str, Any]]:
    accumulators: dict[str, dict[str, Any]] = {}
    for round_item in rounds:
        for result in round_item["results"]:
            model_id = result["model_id"]
            row = accumulators.setdefault(
                model_id,
                {
                    "model_id": model_id,
                    "model_label": result["model_label"],
                    "provider": result["provider"],
                    "returns": [],
                    "max_returns": [],
                    "sp500_returns": [],
                    "alphas": [],
                    "hits": [],
                    "round_ids": [],
                },
            )
            row["returns"].append(result["portfolio_return"])
            row["max_returns"].append(round_item["max_possible_return"])
            row["sp500_returns"].append(round_item["sp500_return"])
            row["alphas"].append(result["alpha_vs_sp500"])
            row["hits"].append(result["beats_sp500"])
            row["round_ids"].append(round_item["round_id"])

    rows = []
    for row in accumulators.values():
        tests = len(row["returns"])
        rows.append(
            {
                "model_id": row["model_id"],
                "model_label": row["model_label"],
                "provider": row["provider"],
                "score": _cumulative_score(row["returns"], row["max_returns"]),
                "average_return": _average(row["returns"]),
                "average_sp500_return": _average(row["sp500_returns"]),
                "average_alpha": _average(row["alphas"]),
                "hit_rate": sum(1 for value in row["hits"] if value) / tests,
                "tests": tests,
                "round_ids": row["round_ids"],
                "maturity": "ready" if tests >= MODEL_READY_OBSERVATION_THRESHOLD else "forming",
            }
        )
    return sorted(
        rows,
        key=lambda row: (
            -float(row["average_return"] if row["average_return"] is not None else -999),
            -float(row["score"] if row["score"] is not None else -999),
            row["model_label"],
        ),
    )


def _regime_leaderboard(
    track_rounds: list[dict[str, Any]], ready_environments: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    model_ids = sorted(
        {
            row["model_id"]
            for environment in ready_environments
            for row in environment["comparison"]["model_rows"]
        }
    )
    all_round_rows = {row["model_id"]: row for row in _model_rows(track_rounds)}
    output = []
    for model_id in model_ids:
        environment_scores = []
        for environment in ready_environments:
            comparison = environment["comparison"]
            model_row = next((row for row in comparison["model_rows"] if row["model_id"] == model_id), None)
            environment_scores.append(
                {
                    "key": environment["key"],
                    "label": environment["label"],
                    "score": model_row.get("score") if model_row else None,
                    "average_return": model_row.get("average_return") if model_row else None,
                    "average_sp500_return": model_row.get("average_sp500_return") if model_row else None,
                    "tests": model_row.get("tests", 0) if model_row else 0,
                    "maturity": model_row.get("maturity", "forming") if model_row else "forming",
                    "comparison_confidence": comparison["confidence"],
                }
            )
        included = [row for row in environment_scores if row["score"] is not None]
        source_row = all_round_rows.get(model_id) or next(
            row
            for environment in ready_environments
            for row in environment["comparison"]["model_rows"]
            if row["model_id"] == model_id
        )
        ready = bool(ready_environments) and all(row["tests"] >= MODEL_READY_OBSERVATION_THRESHOLD for row in environment_scores)
        ready_round_ids = {
            round_id for environment in ready_environments for round_id in environment["comparison"]["round_ids"]
        }
        included_results = [
            result
            for round_item in track_rounds
            if round_item["round_id"] in ready_round_ids
            for result in round_item["results"]
            if result["model_id"] == model_id
        ]
        sp500_scores = []
        for environment in ready_environments:
            rounds = [
                row
                for row in track_rounds
                if row["round_id"] in set(environment["comparison"]["round_ids"])
            ]
            score = _cumulative_score(
                [row["sp500_return"] for row in rounds],
                [row["max_possible_return"] for row in rounds],
            )
            if score is not None:
                sp500_scores.append(score)
        output.append(
            {
                "model_id": model_id,
                "model_label": source_row["model_label"],
                "provider": source_row["provider"],
                "average_return": _average([row["average_return"] for row in included]),
                "average_sp500_return": _average([row["average_sp500_return"] for row in included]),
                "regime_balanced_score": _average([row["score"] for row in included]),
                "sp500_regime_score": _average(sp500_scores),
                "all_round_score": source_row.get("score"),
                "average_alpha": _average([row["alpha_vs_sp500"] for row in included_results]),
                "hit_rate": (
                    sum(1 for row in included_results if row["beats_sp500"]) / len(included_results)
                    if included_results
                    else None
                ),
                "tests_included": sum(row["tests"] for row in environment_scores),
                "ready_environments_covered": sum(
                    1 for row in environment_scores if row["tests"] >= MODEL_READY_OBSERVATION_THRESHOLD
                ),
                "ready_environments_required": len(ready_environments),
                "status": "ready" if ready else "forming",
                "environment_scores": environment_scores,
            }
        )
    return sorted(
        output,
        key=lambda row: (
            0 if row["status"] == "ready" else 1,
            -float(row["average_return"] if row["average_return"] is not None else -999),
            -float(row["regime_balanced_score"] if row["regime_balanced_score"] is not None else -999),
            row["model_label"],
        ),
    )


def _balanced_sample(track: str, rounds: list[dict[str, Any]]) -> dict[str, Any]:
    categories = []
    rounds_by_direction = {}
    for definition in TRACK_DEFINITIONS[track]["directions"]:
        selected = [row for row in rounds if row["direction_key"] == definition["key"]]
        rounds_by_direction[definition["key"]] = selected
        categories.append(
            {
                **definition,
                "count": len(selected),
                "missing": max(0, BALANCED_SAMPLE_THRESHOLD - len(selected)),
                "selected_count": 0,
            }
        )
    ready = all(row["count"] >= BALANCED_SAMPLE_THRESHOLD for row in categories)
    sample_size = min((row["count"] for row in categories), default=0) if ready else 0
    selected_rounds = []
    if ready:
        for category in categories:
            rows = sorted(
                rounds_by_direction[category["key"]],
                key=lambda row: (row.get("exit_date") or "", row["round_id"]),
                reverse=True,
            )[:sample_size]
            category["selected_count"] = len(rows)
            selected_rounds.extend(rows)
    leaderboard = []
    for row in _model_rows(selected_rounds):
        leaderboard.append(
            {
                **row,
                "tests_included": row["tests"],
                "tests_required": len(selected_rounds),
                "status": "ready" if row["tests"] == len(selected_rounds) and selected_rounds else "forming",
            }
        )
    leaderboard.sort(
        key=lambda row: (
            0 if row["status"] == "ready" else 1,
            -float(row["score"] if row["score"] is not None else -999),
            row["model_label"],
        )
    )
    return {
        "status": "ready" if ready else "forming",
        "sample_size": sample_size,
        "categories": categories,
        "selected_round_ids": [row["round_id"] for row in selected_rounds],
        "leaderboard": leaderboard,
    }


def _signals(track: str, directions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key = {row["key"]: row for row in directions}
    signals = []
    direction_signals = []
    for direction in ("down", "flat", "up"):
        bucket = by_key[direction]
        comparison = bucket["comparison"]
        leader = comparison["model_rows"][0] if comparison["model_rows"] else None
        ready = bool(leader and comparison["status"] == "ready")
        signal = {
            "key": f"{track}-{direction}-leader",
            "kind": "direction_leader",
            "track": track,
            "direction": direction,
            "maturity": "ready" if ready else "forming",
            "confidence": comparison["confidence"],
            "environment_round_count": bucket["count"],
            "comparison_round_count": comparison["round_count"],
            "eligible_model_count": comparison["eligible_model_count"],
            "average_sp500_return": leader.get("average_sp500_return") if leader else None,
            "range_label": bucket["range_label"],
            "round_ids": comparison["round_ids"],
            "model": leader,
            "comparison": {
                key: comparison[key]
                for key in (
                    "leader_margin",
                    "leader_standard_error",
                    "leader_ci_95_low",
                    "leader_ci_95_high",
                    "leader_margin_standard_error",
                    "leader_margin_ci_95_low",
                    "leader_margin_ci_95_high",
                    "leave_one_out_stability",
                )
            },
        }
        signals.append(signal)
        direction_signals.append(signal)

    consistency = _consistency_signal(track, directions)
    split = _split_signal(track, by_key["down"], by_key["up"])
    signals.extend([consistency, split])
    ready_directions = [row for row in direction_signals if row["maturity"] == "ready" and row["model"]]
    preferred = [row for row in ready_directions if row["direction"] in {"down", "up"}]
    selected = preferred if len(preferred) >= 2 else ready_directions
    if len(selected) >= 2:
        selected = selected[:3]
        signals.append(
            {
                "key": f"{track}-synthesis",
                "kind": "synthesis",
                "track": track,
                "maturity": "ready",
                "confidence": "high" if all(row["confidence"] == "high" for row in selected) else "medium",
                "directions": selected,
                "model_ids": list(dict.fromkeys(row["model"]["model_id"] for row in selected)),
                "round_ids": sorted({round_id for row in selected for round_id in row["round_ids"]}),
            }
        )
    return signals


def _consistency_signal(track: str, directions: list[dict[str, Any]]) -> dict[str, Any]:
    model_ids = sorted(
        {row["model_id"] for bucket in directions for row in bucket["comparison"]["model_rows"]}
    )
    candidates = []
    for model_id in model_ids:
        rows = []
        for bucket in directions:
            comparison = bucket["comparison"]
            model_row = next((row for row in comparison["model_rows"] if row["model_id"] == model_id), None)
            if model_row and model_row["score"] is not None:
                rows.append({"bucket": bucket, "model": model_row, "comparison": comparison})
        if len(rows) < 2:
            continue
        ready_rows = [
            row
            for row in rows
            if row["comparison"]["status"] == "ready"
        ]
        maturity = "ready" if len(ready_rows) >= 2 else "forming"
        compared_rows = ready_rows if maturity == "ready" else rows
        model = compared_rows[0]["model"]
        candidates.append(
            {
                "model": model,
                "floor_score": min(row["model"]["score"] for row in compared_rows),
                "average_score": _average([row["model"]["score"] for row in compared_rows]),
                "average_return": _average([row["model"]["average_return"] for row in compared_rows]),
                "average_sp500_return": _average(
                    [row["model"]["average_sp500_return"] for row in compared_rows]
                ),
                "directions_covered": len(compared_rows),
                "ready_directions": len(ready_rows),
                "direction_tests": {
                    row["bucket"]["key"]: row["model"]["tests"] for row in compared_rows
                },
                "round_ids": sorted(
                    {round_id for row in compared_rows for round_id in row["model"]["round_ids"]}
                ),
                "maturity": maturity,
                "confidence": (
                    "high"
                    if maturity == "ready" and all(row["comparison"]["confidence"] == "high" for row in compared_rows)
                    else "medium" if maturity == "ready" else "low"
                ),
            }
        )
    candidates.sort(
        key=lambda row: (
            0 if row["maturity"] == "ready" else 1,
            -row["floor_score"],
            -row["directions_covered"],
            row["model"]["model_label"],
        )
    )
    leader = candidates[0] if candidates else None
    return {
        "key": f"{track}-steady",
        "kind": "consistency",
        "track": track,
        "maturity": leader["maturity"] if leader else "forming",
        "confidence": leader["confidence"] if leader else "low",
        "candidate": leader,
    }


def _split_signal(track: str, down: dict[str, Any], up: dict[str, Any]) -> dict[str, Any]:
    down_comparison = down["comparison"]
    up_comparison = up["comparison"]
    down_rows = {row["model_id"]: row for row in down_comparison["model_rows"]}
    up_rows = {row["model_id"]: row for row in up_comparison["model_rows"]}
    candidates = []
    for model_id in sorted(set(down_rows) & set(up_rows)):
        down_row = down_rows[model_id]
        up_row = up_rows[model_id]
        if down_row["score"] is None or up_row["score"] is None:
            continue
        ready = down_comparison["status"] == "ready" and up_comparison["status"] == "ready"
        candidates.append(
            {
                "model": up_row,
                "down_score": down_row["score"],
                "up_score": up_row["score"],
                "score_gap": up_row["score"] - down_row["score"],
                "absolute_score_gap": abs(up_row["score"] - down_row["score"]),
                "down_return": down_row["average_return"],
                "up_return": up_row["average_return"],
                "return_gap": up_row["average_return"] - down_row["average_return"],
                "down_tests": down_row["tests"],
                "up_tests": up_row["tests"],
                "round_ids": sorted(set(down_row["round_ids"] + up_row["round_ids"])),
                "maturity": "ready" if ready else "forming",
                "confidence": (
                    "high"
                    if ready and down_comparison["confidence"] == "high" and up_comparison["confidence"] == "high"
                    else "medium" if ready else "low"
                ),
            }
        )
    candidates.sort(
        key=lambda row: (
            0 if row["maturity"] == "ready" else 1,
            -row["absolute_score_gap"],
            row["model"]["model_label"],
        )
    )
    leader = candidates[0] if candidates else None
    return {
        "key": f"{track}-split",
        "kind": "split",
        "track": track,
        "maturity": leader["maturity"] if leader else "forming",
        "confidence": leader["confidence"] if leader else "low",
        "candidate": leader,
        "down_environment_round_count": down["count"],
        "up_environment_round_count": up["count"],
    }


def _sp500_return(round_item: dict[str, Any]) -> float | None:
    for row in round_item.get("returns") or []:
        if (row.get("option_id") == "SP500" or row.get("is_benchmark")) and _number(row.get("return")) is not None:
            return _number(row.get("return"))
    for row in round_item.get("results") or []:
        value = _number(row.get("sp500_return"))
        if value is not None:
            return value
    return None


def _oracle_return(rows: list[dict[str, Any]]) -> float | None:
    values = [_number(row.get("return")) for row in rows]
    finite = [value for value in values if value is not None]
    return max(finite) if finite else None


def _capitalbench_score(portfolio_return: float, oracle_return: float) -> float | None:
    if abs(oracle_return) <= SCORE_EPSILON:
        return 100.0 if abs(portfolio_return - oracle_return) <= SCORE_EPSILON else None
    return min(100.0, portfolio_return / oracle_return * 100)


def _cumulative_score(returns: list[float], oracle_returns: list[float]) -> float | None:
    if not returns or len(returns) != len(oracle_returns):
        return None
    return _capitalbench_score(sum(returns), sum(oracle_returns))


def _average(values: list[Any]) -> float | None:
    finite = [value for value in (_number(item) for item in values) if value is not None]
    return sum(finite) / len(finite) if finite else None


def _number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if number == number and number not in {float("inf"), float("-inf")} else None

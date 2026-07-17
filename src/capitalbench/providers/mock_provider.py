from __future__ import annotations

import hashlib
import json
import time
from typing import Any

from ..methodology import is_portfolio_v2, is_production_portfolio_v2
from ..schemas import ModelConfig, RuntimeSettings
from .base import ProviderResult, elapsed_usage


class MockProvider:
    provider_name = "mock"
    api_key_env_var = ""

    def run_model(
        self,
        model_config: ModelConfig,
        prompt: str,
        json_schema: dict[str, Any],
        runtime_limits: RuntimeSettings,
    ) -> ProviderResult:
        started_at = time.monotonic()
        options = model_config.metadata.get("option_ids") or ["CASH"]
        option_ids = [str(option_id) for option_id in options]
        if not option_ids:
            option_ids = ["CASH"]
        index = int(hashlib.sha256(model_config.model_id.encode("utf-8")).hexdigest(), 16) % len(option_ids)
        selected_option_id = option_ids[index]
        confidence = 0.5 + ((index % 4) * 0.08)
        base_payload = {
            "round_id": model_config.metadata["round_id"],
            "model_id": model_config.model_id,
            "provider": model_config.provider,
            "mode": model_config.mode,
            "confidence": round(confidence, 2),
            "rationale_summary": (
                f"Mock dry-run selected {selected_option_id} deterministically for "
                f"{model_config.model_id}."
            ),
            "key_risks": [
                "Mock output is not a real model decision",
                "Dry-run data must not be interpreted as benchmark evidence",
            ],
        }
        if model_config.metadata.get("submission_format") == "portfolio":
            constraints = dict(model_config.metadata.get("portfolio_constraints") or {})
            min_holdings = max(1, int(constraints.get("min_holdings") or 1))
            max_holdings = max(1, int(constraints.get("max_holdings") or 5))
            increment = max(1, int(constraints.get("allocation_increment_pct") or 5))
            minimum = max(1, int(constraints.get("min_allocation_pct") or 5))
            total = max(1, int(constraints.get("max_total_allocation_pct") or 100))
            feasible_by_minimum = max(1, total // minimum)
            methodology_version = str(model_config.metadata.get("methodology_version") or "")
            v2 = is_portfolio_v2(methodology_version)
            production_v2 = is_production_portfolio_v2(methodology_version)
            if production_v2:
                benchmark_option_id = str(model_config.metadata.get("benchmark_option_id") or "SP500")
                selected = [benchmark_option_id]
                allocations = [total]
            else:
                holding_count = min(max_holdings, len(option_ids), feasible_by_minimum)
                holding_count = min(len(option_ids), max(min_holdings, holding_count))
                selected = [option_ids[(index + offset) % len(option_ids)] for offset in range(holding_count)]
                allocations = [minimum for _ in selected]
                remainder = total - sum(allocations)
                cursor = 0
                while remainder > 0 and selected:
                    step = min(increment, remainder)
                    allocations[cursor % len(allocations)] += step
                    remainder -= step
                    cursor += 1
            holding_expected_returns = (
                [0.25]
                if production_v2
                else [round(0.4 + position * 0.1, 2) for position in range(len(selected))]
            )
            portfolio = []
            for position, option_id in enumerate(selected):
                holding = {
                    "option_id": option_id,
                    "allocation_pct": allocations[position],
                    "rationale": f"Mock portfolio allocation to {option_id}.",
                }
                if v2:
                    holding.update(
                        {
                            "expected_return_pct": holding_expected_returns[position],
                            "time_window_catalyst": "none identified",
                            "invalidation_condition": "Mock validation condition.",
                        }
                    )
                portfolio.append(holding)
            payload = {
                **base_payload,
                "portfolio": portfolio,
                "portfolio_rationale": "Mock dry-run portfolio built deterministically.",
            }
            if v2:
                portfolio_expected_return = sum(
                    holding_expected_returns[position] * allocations[position] / 100.0
                    for position in range(len(selected))
                )
                benchmark_expected_return = 0.25
                payload.update(
                    {
                        "benchmark_expected_return_pct": benchmark_expected_return,
                        "portfolio_expected_return_pct": round(portfolio_expected_return, 4),
                        "expected_alpha_vs_sp500_pct": round(
                            portfolio_expected_return - benchmark_expected_return,
                            4,
                        ),
                    }
                )
            if production_v2:
                cluster_by_id = dict(model_config.metadata.get("economic_exposure_clusters") or {})
                benchmark_option_id = selected[0]
                candidate_ids = [benchmark_option_id]
                represented = {cluster_by_id.get(benchmark_option_id, benchmark_option_id)}
                for option_id in option_ids:
                    cluster = cluster_by_id.get(option_id, option_id)
                    if option_id not in candidate_ids and cluster not in represented:
                        candidate_ids.append(option_id)
                        represented.add(cluster)
                    if len(represented) >= 4 and len(candidate_ids) >= 6:
                        break
                for option_id in option_ids:
                    if len(candidate_ids) >= 6:
                        break
                    if option_id not in candidate_ids:
                        candidate_ids.append(option_id)
                payload["candidate_ledger"] = [
                    {
                        "option_id": option_id,
                        "decision": "selected" if option_id == benchmark_option_id else "rejected",
                        "forecast_low_pct": round((-0.75 if position == 0 else -0.5) + position * 0.05, 2),
                        "forecast_base_pct": round(0.25 + position * 0.1, 2),
                        "forecast_high_pct": round(1.25 + position * 0.15, 2),
                        "evidence": ["Mock evidence for structural validation."],
                        "continuation_case": "Mock continuation case.",
                        "reversal_case": "Mock reversal case.",
                        "time_window_catalyst": "none identified",
                        "invalidation_condition": "Mock validation condition.",
                    }
                    for position, option_id in enumerate(candidate_ids[:8])
                ]
        else:
            payload = {
                **base_payload,
                "selected_option_id": selected_option_id,
            }
        raw_text = json.dumps(payload, sort_keys=True)
        usage = elapsed_usage(
            started_at,
            input_tokens=len(prompt.split()),
            output_tokens=len(raw_text.split()),
        )
        return ProviderResult(
            raw_text=raw_text,
            parsed_json=payload,
            usage=usage,
            error=None,
        )

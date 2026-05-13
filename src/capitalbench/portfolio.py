from __future__ import annotations

import json
from dataclasses import dataclass

from .schemas import MarketOption, ModelSubmission, PortfolioConstraints, SubmissionFormat


@dataclass(frozen=True)
class AllocationView:
    option_id: str
    allocation_bps: int
    allocation_rank: int
    rationale: str


@dataclass(frozen=True)
class PortfolioMetrics:
    holding_count: int
    max_allocation_bps: int
    cash_allocation_bps: int
    benchmark_allocation_bps: int
    concentration_hhi: float


def submission_format_from_manifest(manifest: object) -> SubmissionFormat:
    value = str(getattr(manifest, "submission_format", "single_pick") or "single_pick")
    if value not in {"single_pick", "portfolio"}:
        raise ValueError("submission_format must be one of: single_pick, portfolio")
    return value  # type: ignore[return-value]


def constraints_from_manifest(manifest: object) -> PortfolioConstraints:
    constraints = getattr(manifest, "portfolio_constraints", None)
    if isinstance(constraints, PortfolioConstraints):
        return constraints
    if isinstance(constraints, dict):
        return PortfolioConstraints.model_validate(constraints)
    return PortfolioConstraints()


def allocation_increment_bps(constraints: PortfolioConstraints) -> int:
    return constraints.allocation_increment_pct * 100


def min_allocation_bps(constraints: PortfolioConstraints) -> int:
    return constraints.min_allocation_pct * 100


def total_allocation_bps(constraints: PortfolioConstraints) -> int:
    return constraints.max_total_allocation_pct * 100


def allocation_views(submission: ModelSubmission) -> list[AllocationView]:
    if submission.portfolio is None:
        if submission.selected_option_id is None:
            return []
        return [
            AllocationView(
                option_id=submission.selected_option_id,
                allocation_bps=10000,
                allocation_rank=1,
                rationale=submission.rationale_summary,
            )
        ]
    return [
        AllocationView(
            option_id=item.option_id,
            allocation_bps=item.allocation_pct * 100,
            allocation_rank=index,
            rationale=item.rationale,
        )
        for index, item in enumerate(submission.portfolio, start=1)
    ]


def selected_option_ids(submission: ModelSubmission) -> set[str]:
    return {allocation.option_id for allocation in allocation_views(submission)}


def primary_option_id(submission: ModelSubmission) -> str:
    allocations = allocation_views(submission)
    if not allocations:
        raise ValueError(f"submission has no selected options: {submission.model_id}")
    return sorted(allocations, key=lambda item: (-item.allocation_bps, item.allocation_rank, item.option_id))[0].option_id


def portfolio_summary_json(submission: ModelSubmission) -> str:
    return json.dumps(
        [
            {
                "option_id": allocation.option_id,
                "allocation_bps": allocation.allocation_bps,
                "allocation_pct": allocation.allocation_bps / 100,
                "rationale": allocation.rationale,
            }
            for allocation in allocation_views(submission)
        ],
        sort_keys=True,
    )


def score_portfolio_return(submission: ModelSubmission, option_returns: dict[str, float]) -> float:
    total = 0.0
    for allocation in allocation_views(submission):
        if allocation.option_id not in option_returns:
            raise ValueError(f"missing price data for selected option_id: {allocation.option_id}")
        total += (allocation.allocation_bps / 10000) * option_returns[allocation.option_id]
    return total


def portfolio_metrics(submission: ModelSubmission, options_by_id: dict[str, MarketOption]) -> PortfolioMetrics:
    allocations = allocation_views(submission)
    holding_count = len(allocations)
    max_allocation = max((allocation.allocation_bps for allocation in allocations), default=0)
    cash_allocation = 0
    benchmark_allocation = 0
    concentration = 0.0
    for allocation in allocations:
        option = options_by_id.get(allocation.option_id)
        if option is not None:
            if option.is_cash:
                cash_allocation += allocation.allocation_bps
            if option.is_benchmark or option.option_id.upper() == "SP500":
                benchmark_allocation += allocation.allocation_bps
        weight = allocation.allocation_bps / 10000
        concentration += weight * weight
    return PortfolioMetrics(
        holding_count=holding_count,
        max_allocation_bps=max_allocation,
        cash_allocation_bps=cash_allocation,
        benchmark_allocation_bps=benchmark_allocation,
        concentration_hhi=concentration,
    )

from __future__ import annotations

from pathlib import Path

from .decision_context import (
    DECISION_CONTEXT_MD,
    DECISION_CONTEXT_TITLE,
    QUALITY_EVIDENCE_JSON,
    QUALITY_EVIDENCE_MD,
    QUALITY_EVIDENCE_MINIMUM_COVERAGE,
    QUALITY_EVIDENCE_TITLE,
)
from .exposures import economic_exposure_cluster
from .io import load_manifest, load_options, read_json, read_yaml
from .methodology import (
    is_portfolio_v2,
    is_portfolio_v3,
    is_production_portfolio,
    is_production_portfolio_v2,
    uses_portfolio_decision_context,
    uses_quality_evidence,
)
from .performance import MARKET_DATA_DIRNAME, UNIVERSE_PRICE_CONTEXT_TITLE, UNIVERSE_TRAILING_RETURNS_MD
from .portfolio import constraints_from_manifest, submission_format_from_manifest
from .portfolio_v3 import build_portfolio_v3_candidate_slate, render_portfolio_v3_candidate_slate
from .schemas import MarketOption

DISALLOWED_MODEL_INPUT_SNIPPETS = (
    " ".join(
        [
            "The S&P 500 benchmark asset is an allowed holding.",
            "Allocate to it when expected active edge is weak",
            "or when the benchmark case is more robust than available active alternatives.",
            "Do not add active risk only because this is a benchmark contest.",
        ]
    ),
)

UNIVERSE_CONTEXT_TITLE_ALIASES = (
    UNIVERSE_PRICE_CONTEXT_TITLE,
    "Full-Universe Trailing Returns",
    DECISION_CONTEXT_TITLE,
)


def validate_model_input_guardrails(text: str) -> None:
    normalized = " ".join(text.split()).lower()
    for snippet in DISALLOWED_MODEL_INPUT_SNIPPETS:
        if " ".join(snippet.split()).lower() in normalized:
            raise ValueError(
                "model input contains prohibited benchmark-allocation instruction: "
                f"{snippet}"
            )


def build_prompt(round_path: Path) -> str:
    prompt = (round_path / "prompt.md").read_text(encoding="utf-8").strip()
    manifest = load_manifest(round_path)
    briefing = (round_path / "briefing.md").read_text(encoding="utf-8").strip()
    metadata = render_round_metadata(round_path, manifest)
    context_title, universe_performance = _market_context_section(round_path, manifest)
    if uses_portfolio_decision_context(manifest.methodology_version) and not universe_performance:
        raise FileNotFoundError(
            f"portfolio round requires market_data/{DECISION_CONTEXT_MD}"
        )
    if _briefing_contains_universe_performance(briefing):
        universe_performance = None
    options = render_options_for_prompt(
        load_options(round_path),
        compact=is_production_portfolio(manifest.methodology_version),
    )
    quality_evidence = _quality_evidence_section(round_path, manifest)
    parts = [f"{prompt}\n\n## Round Metadata\n\n{metadata}"]
    if is_portfolio_v3(manifest.methodology_version):
        slate = build_portfolio_v3_candidate_slate(round_path)
        parts.append(
            "## Deterministic V3 Candidate Slate\n\n"
            "This slate prevents omission and is not a recommendation. Assess every row. "
            "The origin_lanes in your response must exactly match this table.\n\n"
            f"{render_portfolio_v3_candidate_slate(slate)}"
        )
    if quality_evidence:
        parts.append(f"## {QUALITY_EVIDENCE_TITLE}\n\n{quality_evidence}")
    parts.append(f"## Briefing\n\n{briefing}")
    if universe_performance:
        parts.append(f"## {context_title}\n\n{universe_performance}")
    parts.append(f"## Options\n\n{options}\n")
    model_input = "\n\n".join(parts)
    validate_model_input_guardrails(model_input)
    return model_input


def render_round_metadata(round_path: Path, manifest) -> str:
    research_cutoff = _research_cutoff_utc(round_path)
    submission_format = submission_format_from_manifest(manifest)
    lines = [
        f"Round ID: {manifest.round_id}",
        f"Decision date: {manifest.decision_date or 'TBD'}",
        f"Research cutoff UTC: {research_cutoff or 'TBD'}",
        f"Decision deadline UTC: {manifest.decision_deadline or 'TBD'}",
        f"Horizon: {manifest.horizon}",
        f"Entry date: {manifest.entry_date or 'TBD'}",
        f"Exit date: {manifest.exit_date or 'TBD'}",
        f"Methodology version: {manifest.methodology_version or 'TBD'}",
        (
            f"Scoring window: {manifest.entry_date or 'entry date'} to {manifest.exit_date or 'exit date'}; "
            f"optimize for this {manifest.horizon} window only."
        ),
        (
            "Close-to-close scoring: the entry price is the adjusted close on the entry date, "
            "and the exit price is the adjusted close on the exit date after regular trading ends."
        ),
        "Timeline focus: prioritize facts, catalysts, and risks that can plausibly affect prices before the exit close.",
        (
            "Input-bias control: treat fact inclusion, section order, grouping, and price-context table order "
            "as context, not recommendations; do not infer expected return from mention count or placement."
        ),
        (
            "Price-history discipline: trailing returns are descriptive data, not forecasts. Use price history "
            "as one input, not as a standalone reason to select or allocate to an option."
        ),
        (
            "Continuation evidence: when a holding or selection relies on recent price strength, compare it with "
            "the briefing's catalysts, macro context, valuation or fundamental facts if supplied, volatility, "
            "drawdown, and reversal risk before the exit close. Do not invent support that is not in the input."
        ),
        f"Entry rule: {manifest.entry_rule or 'TBD'}",
        f"Exit rule: {manifest.exit_rule or 'TBD'}",
        f"Submission format: {submission_format}",
        "Scoring benchmark: S&P 500 / SPY",
        "Return calculation: adjusted close prices are used when available.",
    ]
    if submission_format == "portfolio":
        constraints = constraints_from_manifest(manifest)
        lines.extend(
            [
                f"Portfolio holdings allowed: {constraints.min_holdings}-{constraints.max_holdings}",
                f"Portfolio allocation increment: {constraints.allocation_increment_pct}%",
                f"Portfolio minimum allocation: {constraints.min_allocation_pct}%",
                f"Portfolio total allocation: {constraints.max_total_allocation_pct}%",
            ]
        )
    if is_portfolio_v2(manifest.methodology_version):
        lines.extend(
            [
                "Decision protocol: single-turn, non-agentic, with no tools or follow-up calls.",
                "Forecast sequence: estimate SPY, estimate the selected holdings, then construct the portfolio.",
                "Confidence meaning: probability from 0 to 1 that the submitted portfolio beats SPY over this scoring window.",
                "Expected-return units: percentage points; 1.25 means an expected return of +1.25%.",
            ]
        )
    if is_portfolio_v3(manifest.methodology_version):
        lines.extend(
            [
                "Decision protocol: single-turn, non-agentic, with no tools or follow-up calls.",
                "Search protocol: assess the complete deterministic V3 slate and add no more than two evidence-backed wildcards.",
                "Model role: rank and classify candidates; CapitalBench constructs the final portfolio deterministically.",
                "Portfolio rule: select at most three ranked non-SPY candidates labeled overreaction with at least 55% probability of beating SPY.",
                "Allocation rule: fill 35%, 35%, and 30% slots in rank order; every unused slot goes to SPY.",
                "Probability units: report p_beat_spy_pct and p_top3_pct as whole percentages from 0 to 100.",
            ]
        )
    if is_production_portfolio_v2(manifest.methodology_version):
        constraints = constraints_from_manifest(manifest)
        lines.extend(
            [
                "Candidate protocol: assess 6-8 unique options, include SP500, and span at least four economic-exposure clusters.",
                "Forecast protocol: record low/base/high returns plus continuation, reversal, catalyst, and invalidation for every candidate.",
                "Active-holding hurdle: every selected non-SP500, non-CASH holding must have a base forecast greater than SP500's base forecast.",
                (
                    "Economic-exposure cap: no non-SP500, non-CASH cluster may exceed "
                    f"{constraints.max_economic_exposure_pct or 50}% of the portfolio."
                ),
            ]
        )
    return "\n".join(f"- {line}" for line in lines)


def _research_cutoff_utc(round_path: Path) -> str | None:
    research_manifest_path = round_path / "research" / "research_manifest.yaml"
    if not research_manifest_path.exists():
        return None
    try:
        data = read_yaml(research_manifest_path)
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    value = data.get("research_cutoff_utc")
    return str(value) if value else None


def _universe_performance_section(round_path: Path) -> str | None:
    path = round_path / MARKET_DATA_DIRNAME / UNIVERSE_TRAILING_RETURNS_MD
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8").strip()
    for title in UNIVERSE_CONTEXT_TITLE_ALIASES:
        heading = f"# {title}"
        if text.startswith(heading):
            text = text.removeprefix(heading).strip()
            break
    return text or None


def _market_context_section(round_path: Path, manifest) -> tuple[str, str | None]:
    if uses_portfolio_decision_context(manifest.methodology_version):
        path = round_path / MARKET_DATA_DIRNAME / DECISION_CONTEXT_MD
        return DECISION_CONTEXT_TITLE, _strip_context_heading(path, DECISION_CONTEXT_TITLE)
    return UNIVERSE_PRICE_CONTEXT_TITLE, _universe_performance_section(round_path)


def _quality_evidence_section(round_path: Path, manifest) -> str | None:
    if not uses_quality_evidence(manifest.methodology_version):
        return None
    market_data = round_path / MARKET_DATA_DIRNAME
    markdown_path = market_data / QUALITY_EVIDENCE_MD
    json_path = market_data / QUALITY_EVIDENCE_JSON
    if not markdown_path.exists() or not json_path.exists():
        raise FileNotFoundError(
            "this portfolio methodology requires "
            f"market_data/{QUALITY_EVIDENCE_MD} and market_data/{QUALITY_EVIDENCE_JSON}"
        )
    report = read_json(json_path)
    coverage = float(report.get("coverage") or 0.0)
    if coverage < QUALITY_EVIDENCE_MINIMUM_COVERAGE:
        raise ValueError(
            "portfolio quality-evidence coverage is below the required "
            f"{QUALITY_EVIDENCE_MINIMUM_COVERAGE:.0%}: {coverage:.1%}"
        )
    return _strip_context_heading(markdown_path, QUALITY_EVIDENCE_TITLE)


def _strip_context_heading(path: Path, title: str) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8").strip()
    heading = f"# {title}"
    if text.startswith(heading):
        text = text.removeprefix(heading).strip()
    return text or None


def _briefing_contains_universe_performance(briefing: str) -> bool:
    return any(title in briefing for title in UNIVERSE_CONTEXT_TITLE_ALIASES)


def render_options_for_prompt(options: list[MarketOption], *, compact: bool = False) -> str:
    if compact:
        lines = [
            "| option_id | symbol | name | economic_exposure_cluster | risk | neutral_exposure |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for option in options:
            if not option.include_in_universe:
                continue
            cells = [
                option.id,
                option.symbol or "N/A",
                option.name,
                economic_exposure_cluster(option),
                option.risk_bucket,
                option.exposure_description,
            ]
            lines.append("| " + " | ".join(str(cell).replace("|", "\\|") for cell in cells) + " |")
        return "\n".join(lines)
    rendered: list[str] = []
    for option in options:
        if not option.include_in_universe:
            continue
        rendered.append(
            "\n".join(
                [
                    "Allowed option:",
                    f"ID: {option.id}",
                    f"Name: {option.name}",
                    f"Symbol: {option.symbol or 'N/A'}",
                    f"Asset class: {option.asset_class}",
                    f"Category: {option.category}",
                    f"Group: {option.option_group}",
                    f"Risk bucket: {option.risk_bucket}",
                    f"Description: {option.exposure_description}",
                ]
            )
        )
    return "\n\n".join(rendered)

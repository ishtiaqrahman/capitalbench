from __future__ import annotations

from pathlib import Path

from .io import load_manifest, load_options, read_yaml
from .performance import MARKET_DATA_DIRNAME, UNIVERSE_TRAILING_RETURNS_MD
from .portfolio import constraints_from_manifest, submission_format_from_manifest
from .schemas import MarketOption

DISALLOWED_MODEL_INPUT_SNIPPETS = (
    (
        "The S&P 500 benchmark asset is an allowed holding. Allocate to it when expected active edge is weak "
        "or when the benchmark case is more robust than available active alternatives. Do not add active risk "
        "only because this is a benchmark contest."
    ),
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
    universe_performance = None if _briefing_contains_universe_performance(briefing) else _universe_performance_section(round_path)
    options = render_options_for_prompt(load_options(round_path))
    parts = [
        f"{prompt}\n\n"
        f"## Round Metadata\n\n{metadata}\n\n"
        f"## Briefing\n\n{briefing}"
    ]
    if universe_performance:
        parts.append(f"## Full-Universe Trailing Returns\n\n{universe_performance}")
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
            "Input-bias control: treat fact inclusion, section order, grouping, and trailing-return table order "
            "as context, not recommendations; do not infer expected return from mention count or placement."
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
    if text.startswith("# Full-Universe Trailing Returns"):
        text = text.removeprefix("# Full-Universe Trailing Returns").strip()
    return text or None


def _briefing_contains_universe_performance(briefing: str) -> bool:
    return "Full-Universe Trailing Returns" in briefing


def render_options_for_prompt(options: list[MarketOption]) -> str:
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

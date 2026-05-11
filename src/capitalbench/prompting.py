from __future__ import annotations

from pathlib import Path

from .io import load_manifest, load_options, read_yaml
from .performance import MARKET_DATA_DIRNAME, UNIVERSE_TRAILING_RETURNS_MD
from .schemas import MarketOption


def build_prompt(round_path: Path) -> str:
    prompt = (round_path / "prompt.md").read_text(encoding="utf-8").strip()
    manifest = load_manifest(round_path)
    briefing = (round_path / "briefing.md").read_text(encoding="utf-8").strip()
    metadata = render_round_metadata(round_path, manifest)
    universe_performance = _universe_performance_section(round_path)
    options = render_options_for_prompt(load_options(round_path))
    parts = [
        f"{prompt}\n\n"
        f"## Round Metadata\n\n{metadata}\n\n"
        f"## Briefing\n\n{briefing}"
    ]
    if universe_performance:
        parts.append(f"## Full-Universe Trailing Returns\n\n{universe_performance}")
    parts.append(f"## Options\n\n{options}\n")
    return "\n\n".join(parts)


def render_round_metadata(round_path: Path, manifest) -> str:
    research_cutoff = _research_cutoff_utc(round_path)
    lines = [
        f"Round ID: {manifest.round_id}",
        f"Decision date: {manifest.decision_date or 'TBD'}",
        f"Research cutoff UTC: {research_cutoff or 'TBD'}",
        f"Decision deadline UTC: {manifest.decision_deadline or 'TBD'}",
        f"Horizon: {manifest.horizon}",
        f"Entry date: {manifest.entry_date or 'TBD'}",
        f"Exit date: {manifest.exit_date or 'TBD'}",
        f"Entry rule: {manifest.entry_rule or 'TBD'}",
        f"Exit rule: {manifest.exit_rule or 'TBD'}",
        "Scoring benchmark: S&P 500 / SPY",
        "Return calculation: adjusted close prices are used when available.",
    ]
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

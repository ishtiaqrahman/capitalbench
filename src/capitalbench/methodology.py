from __future__ import annotations


PORTFOLIO_V2_2_VERSION = "portfolio-v2.2"
PORTFOLIO_V2_VERSION = PORTFOLIO_V2_2_VERSION
PORTFOLIO_V3_VERSION = "portfolio-v3.0"
DEFAULT_PORTFOLIO_VERSION = PORTFOLIO_V3_VERSION


def is_portfolio_v2(methodology_version: str | None) -> bool:
    return str(methodology_version or "").startswith("portfolio-v2")


def is_production_portfolio_v2(methodology_version: str | None) -> bool:
    version = str(methodology_version or "")
    return version.startswith("portfolio-v2") and not version.endswith("-pilot")


def is_portfolio_v2_2(methodology_version: str | None) -> bool:
    return str(methodology_version or "").startswith(PORTFOLIO_V2_2_VERSION)


def is_portfolio_v3(methodology_version: str | None) -> bool:
    return str(methodology_version or "") == PORTFOLIO_V3_VERSION


def is_portfolio_methodology(methodology_version: str | None) -> bool:
    return is_portfolio_v2(methodology_version) or is_portfolio_v3(methodology_version)


def is_production_portfolio(methodology_version: str | None) -> bool:
    return is_production_portfolio_v2(methodology_version) or is_portfolio_v3(methodology_version)


def uses_portfolio_decision_context(methodology_version: str | None) -> bool:
    return is_portfolio_methodology(methodology_version)


def uses_quality_evidence(methodology_version: str | None) -> bool:
    return is_portfolio_v2_2(methodology_version) or is_portfolio_v3(methodology_version)

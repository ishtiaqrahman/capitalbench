from __future__ import annotations


PORTFOLIO_V2_2_VERSION = "portfolio-v2.2"
PORTFOLIO_V2_VERSION = PORTFOLIO_V2_2_VERSION


def is_portfolio_v2(methodology_version: str | None) -> bool:
    return str(methodology_version or "").startswith("portfolio-v2")


def is_production_portfolio_v2(methodology_version: str | None) -> bool:
    version = str(methodology_version or "")
    return version.startswith("portfolio-v2") and not version.endswith("-pilot")


def is_portfolio_v2_2(methodology_version: str | None) -> bool:
    return str(methodology_version or "").startswith(PORTFOLIO_V2_2_VERSION)

from __future__ import annotations

from .schemas import MarketOption


_OPTION_CLUSTERS: dict[str, str] = {
    "CASH": "capital_preservation",
    "SHORT_TREASURY": "capital_preservation",
    "SP500": "diversified_us_equity",
    "TOTAL_US_MARKET": "diversified_us_equity",
    "EQUAL_WEIGHT_SP500": "diversified_us_equity",
    "LARGE_VALUE": "diversified_us_equity",
    "MID_CAP": "diversified_us_equity",
    "SMALL_CAP": "diversified_us_equity",
    "SMALL_VALUE": "diversified_us_equity",
    "DIVIDEND": "diversified_us_equity",
    "LOW_VOL": "diversified_us_equity",
    "MOMENTUM": "diversified_us_equity",
    "NASDAQ100": "technology_and_growth",
    "LARGE_GROWTH": "technology_and_growth",
    "TECHNOLOGY": "technology_and_growth",
    "COMMUNICATIONS": "technology_and_growth",
    "SEMICONDUCTORS": "technology_and_growth",
    "SOFTWARE": "technology_and_growth",
    "BROAD_AI_TECH": "technology_and_growth",
    "AUTONOMOUS_ROBOTICS": "technology_and_growth",
    "CYBERSECURITY": "technology_and_growth",
    "CONSUMER_DISCRETIONARY": "consumer_cyclical",
    "CONSUMER_STAPLES": "consumer_defensive",
    "HEALTHCARE": "healthcare_and_biotech",
    "BIOTECH": "healthcare_and_biotech",
    "FINANCIALS": "financials",
    "REGIONAL_BANKS": "financials",
    "INDUSTRIALS": "industrials_and_defense",
    "AEROSPACE_DEFENSE": "industrials_and_defense",
    "ENERGY": "energy",
    "OIL": "energy",
    "MATERIALS": "materials_and_mining",
    "METALS_MINING": "materials_and_mining",
    "UTILITIES": "rate_sensitive_defensive",
    "REAL_ESTATE": "rate_sensitive_defensive",
    "SOLAR": "clean_energy",
    "INTERMEDIATE_TREASURY": "rates_and_duration",
    "LONG_TREASURY": "rates_and_duration",
    "TIPS": "rates_and_duration",
    "AGGREGATE_BONDS": "rates_and_duration",
    "MORTGAGE_BACKED_BONDS": "rates_and_duration",
    "MUNICIPAL_BONDS": "rates_and_duration",
    "INTERNATIONAL_BONDS": "rates_and_duration",
    "INVESTMENT_GRADE_CREDIT": "credit",
    "HIGH_YIELD_CREDIT": "credit",
    "EMERGING_MARKET_BONDS": "credit",
    "GOLD": "precious_metals",
    "SILVER": "precious_metals",
    "BROAD_COMMODITIES": "non_energy_commodities",
    "COPPER": "non_energy_commodities",
    "AGRICULTURE": "non_energy_commodities",
    "US_DOLLAR": "currencies",
    "EURO": "currencies",
    "YEN": "currencies",
    "BITCOIN_ETF": "crypto_assets",
    "ETHEREUM_ETF": "crypto_assets",
}


def economic_exposure_cluster(option: MarketOption) -> str:
    explicit = _OPTION_CLUSTERS.get(option.option_id)
    if explicit:
        return explicit
    if option.option_group in {"international_equity", "country_equity"}:
        return "international_equity"
    return option.option_group


def exposure_clusters_by_option(options: list[MarketOption]) -> dict[str, str]:
    return {option.option_id: economic_exposure_cluster(option) for option in options}

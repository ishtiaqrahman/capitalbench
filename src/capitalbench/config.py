from __future__ import annotations

from pathlib import Path

from pydantic import Field, ValidationError

from .io import read_yaml
from .schemas import ModelConfig, ProviderName, StrictModel, Usage


class PricingEntry(StrictModel):
    input_per_1m_tokens_usd: float | None = Field(default=None, ge=0)
    output_per_1m_tokens_usd: float | None = Field(default=None, ge=0)
    reasoning_per_1m_tokens_usd: float | None = Field(default=None, ge=0)


PricingTable = dict[str, dict[str, PricingEntry]]


def load_model_configs(path: Path) -> list[ModelConfig]:
    data = read_yaml(path)
    raw_models = data.get("models") if isinstance(data, dict) else None
    if not isinstance(raw_models, list):
        raise ValueError(f"{path} must contain a 'models' list")

    configs: list[ModelConfig] = []
    for index, raw_model in enumerate(raw_models):
        try:
            configs.append(ModelConfig.model_validate(raw_model))
        except ValidationError as exc:
            raise ValueError(f"invalid model config at models[{index}]: {exc}") from exc
    return configs


def load_pricing_config(path: Path | None) -> PricingTable:
    if path is None:
        return {}
    data = read_yaml(path)
    raw_pricing = data.get("pricing") if isinstance(data, dict) else None
    if raw_pricing is None:
        raise ValueError(f"{path} must contain a 'pricing' mapping")
    if not isinstance(raw_pricing, dict):
        raise ValueError(f"{path} pricing must be a mapping")

    pricing: PricingTable = {}
    for provider, provider_prices in raw_pricing.items():
        if provider not in {"openai", "anthropic", "google", "xai"}:
            raise ValueError(f"invalid pricing provider: {provider}")
        if not isinstance(provider_prices, dict):
            raise ValueError(f"pricing for {provider} must be a mapping")
        pricing[provider] = {}
        for api_model_name, raw_entry in provider_prices.items():
            pricing[provider][api_model_name] = PricingEntry.model_validate(raw_entry or {})
    return pricing


def calculate_cost_usd(
    provider: ProviderName,
    api_model_name: str,
    usage: Usage,
    pricing: PricingTable,
) -> float | None:
    entry = pricing.get(provider, {}).get(api_model_name)
    if entry is None:
        return None

    cost = 0.0
    used_any_price = False
    if usage.input_tokens is not None:
        if entry.input_per_1m_tokens_usd is None:
            return None
        cost += (usage.input_tokens / 1_000_000) * entry.input_per_1m_tokens_usd
        used_any_price = True
    if usage.output_tokens is not None:
        if entry.output_per_1m_tokens_usd is None:
            return None
        cost += (usage.output_tokens / 1_000_000) * entry.output_per_1m_tokens_usd
        used_any_price = True
    if usage.reasoning_tokens is not None:
        if entry.reasoning_per_1m_tokens_usd is None:
            return None
        cost += (usage.reasoning_tokens / 1_000_000) * entry.reasoning_per_1m_tokens_usd
        used_any_price = True
    return cost if used_any_price else None

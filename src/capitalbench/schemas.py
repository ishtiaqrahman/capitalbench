from __future__ import annotations

import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        protected_namespaces=(),
        validate_assignment=True,
    )


class RoundManifest(StrictModel):
    round_id: str
    title: str = ""
    description: str = ""
    decision_date: str | None = None
    decision_deadline: str | None = None
    horizon: str = "one month"
    entry_rule: str = ""
    exit_rule: str = ""
    entry_date: str | None = None
    exit_date: str | None = None
    created_at: str | None = None
    notes: str = ""

    @field_validator("round_id")
    @classmethod
    def require_round_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("round_id is required")
        return value


def _none_if_blank(value: object) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip()
    return normalized or None


RiskBucket = Literal["cash", "low", "medium", "high", "very_high"]


class MarketOption(StrictModel):
    id: str
    name: str
    symbol: str | None
    asset_class: str
    category: str
    option_group: str
    risk_bucket: RiskBucket
    exposure_description: str
    tiingo_symbol: str | None
    currency: str = "USD"
    is_cash: bool = False
    include_in_universe: bool = True
    is_benchmark: bool = False

    @model_validator(mode="before")
    @classmethod
    def normalize_legacy_fields(cls, data: object) -> object:
        if not isinstance(data, dict):
            return data
        normalized = dict(data)
        if "id" not in normalized and "option_id" in normalized:
            normalized["id"] = normalized["option_id"]
        if "name" not in normalized and "label" in normalized:
            normalized["name"] = normalized["label"]
        legacy_symbol = "symbol" not in normalized and "asset_symbol" in normalized
        if "symbol" not in normalized and "asset_symbol" in normalized:
            normalized["symbol"] = normalized["asset_symbol"]
        if "exposure_description" not in normalized and "description" in normalized:
            normalized["exposure_description"] = normalized["description"]

        is_cash = bool(normalized.get("is_cash")) or str(normalized.get("id", "")).upper() == "CASH"
        symbol = _none_if_blank(normalized.get("symbol"))
        if is_cash and symbol in {"USD", "CASH"}:
            symbol = None
        normalized["symbol"] = symbol
        normalized["tiingo_symbol"] = _none_if_blank(normalized.get("tiingo_symbol"))
        if legacy_symbol and not is_cash and normalized.get("tiingo_symbol") is None and symbol is not None:
            normalized["tiingo_symbol"] = symbol

        normalized.setdefault("asset_class", "cash" if is_cash else "unknown")
        normalized.setdefault("category", str(normalized.get("kind") or normalized.get("asset_class") or "unknown"))
        normalized.setdefault("option_group", str(normalized.get("category") or "unknown"))
        normalized.setdefault("risk_bucket", "cash" if is_cash else "medium")
        normalized.setdefault("currency", "USD")
        normalized.setdefault("include_in_universe", True)
        normalized["is_cash"] = is_cash
        if "exposure_description" not in normalized or _none_if_blank(normalized.get("exposure_description")) is None:
            normalized["exposure_description"] = f"{normalized.get('name', normalized.get('id', 'Option'))} exposure."
        for legacy_key in ["option_id", "label", "asset_symbol", "asset_name", "description", "kind"]:
            normalized.pop(legacy_key, None)
        return normalized

    @field_validator("id", "name", "asset_class", "category", "option_group", "currency")
    @classmethod
    def require_non_empty_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("field cannot be blank")
        return value

    @field_validator("symbol", "tiingo_symbol")
    @classmethod
    def normalize_optional_symbol(cls, value: str | None) -> str | None:
        if value is None:
            return value
        normalized = value.strip().upper()
        return normalized or None

    @field_validator("exposure_description")
    @classmethod
    def validate_exposure_description(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("exposure_description cannot be blank")
        sentence_count = len([part for part in re.split(r"[.!?]+", value) if part.strip()])
        if sentence_count > 2:
            raise ValueError("exposure_description must be 1 to 2 neutral sentences")
        banned_phrases = [
            "will outperform",
            "likely to outperform",
            "expected to outperform",
            "should outperform",
            "will beat",
            "likely to beat",
            "best pick",
            "recommended",
        ]
        lowered = value.lower()
        for phrase in banned_phrases:
            if phrase in lowered:
                raise ValueError("exposure_description must avoid predictive language")
        return value

    @model_validator(mode="after")
    def validate_symbols(self) -> "MarketOption":
        if self.is_cash:
            if self.symbol is not None or self.tiingo_symbol is not None:
                raise ValueError("cash options must have null symbol and null tiingo_symbol")
            return self
        if not self.symbol:
            raise ValueError("non-CASH options require symbol")
        if not self.tiingo_symbol:
            raise ValueError("non-CASH options require tiingo_symbol")
        return self

    @property
    def option_id(self) -> str:
        return self.id

    @property
    def label(self) -> str:
        return self.name

    @property
    def asset_symbol(self) -> str:
        return self.symbol or "CASH"

    @property
    def asset_name(self) -> str:
        return self.name

    @property
    def description(self) -> str:
        return self.exposure_description

    @property
    def kind(self) -> str:
        return self.category


ProviderName = Literal["openai", "anthropic", "google", "xai"]
RunMode = Literal["closed_capability"]
RunType = Literal["official", "stability", "mock", "provider_smoke", "retrospective"]


class ModelConfig(StrictModel):
    model_id: str
    provider: ProviderName
    api_model_name: str
    enabled: bool = True
    mode: RunMode = "closed_capability"
    temperature: float | None = Field(default=None, ge=0, le=2)
    max_completion_tokens: int = Field(default=3000, ge=1)
    max_wall_clock_seconds: int = Field(default=120, ge=1)
    reasoning_effort: str | None = None
    first_eligible_round: str | None = None
    first_eligible_date_utc: str | None = None
    model_release_date: str | None = None
    notes: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("model_id", "api_model_name")
    @classmethod
    def require_model_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("field cannot be blank")
        return value

    @field_validator("first_eligible_round", "first_eligible_date_utc", "model_release_date", "notes")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return value
        return value.strip()


class Usage(StrictModel):
    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)
    reasoning_tokens: int | None = Field(default=None, ge=0)
    total_tokens: int | None = Field(default=None, ge=0)
    cost_usd: float | None = Field(default=None, ge=0)
    latency_seconds: float | None = Field(default=None, ge=0)

    @model_validator(mode="before")
    @classmethod
    def set_total_tokens(cls, data: object) -> object:
        if not isinstance(data, dict) or data.get("total_tokens") is not None:
            return data
        output_tokens = int(data.get("output_tokens") or 0)
        reasoning_tokens = int(data.get("reasoning_tokens") or 0)
        computed_total = int(data.get("input_tokens") or 0) + max(output_tokens, reasoning_tokens)
        if computed_total:
            return {**data, "total_tokens": computed_total}
        return data

    @model_validator(mode="after")
    def validate_total_tokens(self) -> "Usage":
        # Some providers report reasoning tokens as a subset of output tokens,
        # not an additional bucket. Validate against the largest known output
        # count instead of double-counting hidden reasoning.
        computed_total = (self.input_tokens or 0) + max(self.output_tokens or 0, self.reasoning_tokens or 0)
        if self.total_tokens is not None and self.total_tokens < computed_total:
            raise ValueError("total_tokens cannot be less than available token counts")
        return self


class RuntimeSettings(StrictModel):
    timeout_seconds: int = Field(default=120, ge=1)
    max_retries: int = Field(default=0, ge=0)
    max_output_tokens: int = Field(default=3000, ge=1)
    temperature: float | None = Field(default=None, ge=0, le=2)
    reasoning_effort: str | None = None
    seed: int | None = None


class ModelSubmission(StrictModel):
    round_id: str
    model_id: str
    provider: ProviderName
    mode: RunMode
    run_type: RunType | None = None
    replicate_index: int | None = Field(default=None, ge=1)
    replicate_count: int | None = Field(default=None, ge=1)
    is_official_score: bool = False
    selected_option_id: str
    confidence: float = Field(ge=0, le=1)
    rationale_summary: str
    key_risks: list[str]
    usage: Usage | None = None
    cost_usd: float | None = Field(default=None, ge=0)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("round_id", "model_id", "selected_option_id", "rationale_summary")
    @classmethod
    def require_non_empty_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("field cannot be blank")
        return value

    @field_validator("key_risks")
    @classmethod
    def normalize_key_risks(cls, value: list[str]) -> list[str]:
        normalized = [item.strip() for item in value]
        if any(not item for item in normalized):
            raise ValueError("key_risks cannot contain blank items")
        return normalized


class PriceRecord(StrictModel):
    option_id: str | None = None
    symbol: str | None = None
    price: float | None = Field(default=None, gt=0)
    close: float | None = Field(default=None, gt=0)
    adj_close: float | None = Field(default=None, gt=0)
    date: str | None = None
    currency: str = "USD"
    source: str = ""
    price_source: Literal["price", "adj_close", "close"] = "price"

    @model_validator(mode="before")
    @classmethod
    def normalize_price_fields(cls, data: object) -> object:
        if not isinstance(data, dict):
            return data
        normalized = {
            key: (None if value == "" else value)
            for key, value in data.items()
        }
        if "adj_close" not in normalized and "adjClose" in normalized:
            normalized["adj_close"] = normalized.pop("adjClose")
        if "symbol" in normalized and normalized["symbol"] is not None:
            normalized["symbol"] = str(normalized["symbol"]).strip().upper() or None
        if "option_id" in normalized and normalized["option_id"] is not None:
            normalized["option_id"] = str(normalized["option_id"]).strip() or None
        adj_close = normalized.get("adj_close")
        price = normalized.get("price")
        close = normalized.get("close")
        if adj_close is not None:
            normalized["price"] = adj_close
            normalized["price_source"] = "adj_close"
        elif price is not None:
            normalized["price_source"] = "price"
        elif close is not None:
            normalized["price"] = close
            normalized["price_source"] = "close"
        return normalized

    @field_validator("option_id", "symbol")
    @classmethod
    def normalize_price_identifier(cls, value: str | None) -> str | None:
        if value is None:
            return value
        value = value.strip()
        return value or None

    @model_validator(mode="after")
    def validate_price_record(self) -> "PriceRecord":
        if not self.option_id and not self.symbol:
            raise ValueError("price row requires option_id or symbol")
        if self.price is None:
            raise ValueError("price row requires price, adj_close, or close")
        return self


class ScoreRecord(StrictModel):
    round_id: str
    model_id: str
    provider: ProviderName
    mode: RunMode
    selected_option_id: str
    confidence: float
    rationale_summary: str
    key_risks: list[str]
    selected_asset_return: float
    sp500_return: float
    alpha_vs_sp500: float
    regret_vs_best_option: float | None = None
    rank_among_options: int | None = None
    beats_sp500: bool
    beats_cash: bool
    cost_usd: float | None = None
    alpha_per_dollar: float | None = None

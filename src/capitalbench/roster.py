from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Mapping

from .config import load_model_configs
from .methodology import is_production_portfolio_v2
from .schemas import ModelConfig


LEGACY_PORTFOLIO_V2_METHODOLOGY = "portfolio-v2.0"
CANONICAL_PORTFOLIO_V2_MODELS_PATH = Path(__file__).resolve().parents[2] / "configs" / "models.v2.yaml"


def canonical_portfolio_v2_model_ids() -> tuple[str, ...]:
    configs = load_model_configs(CANONICAL_PORTFOLIO_V2_MODELS_PATH)
    model_ids = tuple(config.model_id for config in configs if config.enabled)
    duplicates = sorted(model_id for model_id, count in Counter(model_ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"canonical Portfolio V2 roster contains duplicate model IDs: {', '.join(duplicates)}")
    if not model_ids:
        raise ValueError("canonical Portfolio V2 roster is empty")
    return model_ids


def active_portfolio_v2_model_ids(
    as_of_utc: datetime | str | None = None,
    round_id: str | None = None,
) -> tuple[str, ...]:
    as_of = _as_utc_datetime(as_of_utc) if as_of_utc is not None else datetime.now(timezone.utc)
    configs = load_model_configs(CANONICAL_PORTFOLIO_V2_MODELS_PATH)
    model_ids = tuple(
        config.model_id
        for config in configs
        if config.enabled
        and not model_is_retired(config, as_of)
        and not _model_is_before_first_eligibility(config, as_of, round_id)
    )
    _validate_model_ids(model_ids, "active Portfolio V2 roster")
    return model_ids


def portfolio_v2_roster_version(model_ids: Iterable[str]) -> str:
    normalized = tuple(sorted(str(model_id).strip() for model_id in model_ids))
    _validate_model_ids(normalized, "Portfolio V2 roster")
    digest = sha256("\n".join(normalized).encode("utf-8")).hexdigest()[:12]
    return f"portfolio-v2-roster-{digest}"


def model_is_retired(model_config: ModelConfig, as_of_utc: datetime | str) -> bool:
    if not model_config.retired_at_utc:
        return False
    retired_at = _as_utc_datetime(model_config.retired_at_utc)
    as_of = _as_utc_datetime(as_of_utc)
    return as_of >= retired_at


def _model_is_before_first_eligibility(
    model_config: ModelConfig,
    as_of_utc: datetime,
    round_id: str | None,
) -> bool:
    if model_config.first_eligible_round and round_id and round_id < model_config.first_eligible_round:
        return True
    if model_config.first_eligible_date_utc:
        return as_of_utc < _as_utc_datetime(model_config.first_eligible_date_utc)
    return False


def validate_official_portfolio_v2_roster(
    methodology_version: str | None,
    model_configs: Iterable[ModelConfig],
    expected_model_ids: Iterable[str] | None = None,
) -> tuple[str, ...]:
    actual_ids = tuple(config.model_id for config in model_configs)
    if not is_production_portfolio_v2(methodology_version):
        return actual_ids

    expected_ids = _expected_model_ids(methodology_version, expected_model_ids)
    if Counter(actual_ids) != Counter(expected_ids):
        missing = sorted(Counter(expected_ids) - Counter(actual_ids))
        unexpected = sorted(Counter(actual_ids) - Counter(expected_ids))
        details: list[str] = []
        if missing:
            details.append(f"missing: {', '.join(missing)}")
        if unexpected:
            details.append(f"unexpected: {', '.join(unexpected)}")
        raise ValueError(
            "official Portfolio V2 runs require the complete frozen model roster"
            + (f" ({'; '.join(details)})" if details else "")
        )
    return actual_ids


def validate_official_portfolio_v2_run_manifest(
    methodology_version: str | None,
    run_manifest: Mapping[str, Any],
    expected_model_ids: Iterable[str] | None = None,
) -> None:
    if not is_production_portfolio_v2(methodology_version):
        return

    expected_ids = _expected_model_ids(methodology_version, expected_model_ids)
    model_count = int(run_manifest.get("model_count") or 0)
    if model_count != len(expected_ids):
        raise ValueError(
            "official Portfolio V2 run model_count does not match the complete canonical roster: "
            f"{model_count} != {len(expected_ids)}"
        )

    raw_model_ids = run_manifest.get("model_ids")
    if raw_model_ids is None:
        return
    if not isinstance(raw_model_ids, list) or Counter(str(model_id) for model_id in raw_model_ids) != Counter(expected_ids):
        raise ValueError("official Portfolio V2 run model_ids do not match the complete frozen roster")


def _expected_model_ids(
    methodology_version: str | None,
    expected_model_ids: Iterable[str] | None,
) -> tuple[str, ...]:
    frozen_ids = tuple(str(model_id).strip() for model_id in (expected_model_ids or ()))
    if frozen_ids:
        _validate_model_ids(frozen_ids, "frozen Portfolio V2 roster")
        return frozen_ids
    if methodology_version == LEGACY_PORTFOLIO_V2_METHODOLOGY:
        return canonical_portfolio_v2_model_ids()
    raise ValueError(
        "official Portfolio V2 rounds must freeze expected_model_ids in the round manifest"
    )


def _validate_model_ids(model_ids: tuple[str, ...], label: str) -> None:
    duplicates = sorted(model_id for model_id, count in Counter(model_ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"{label} contains duplicate model IDs: {', '.join(duplicates)}")
    if not model_ids:
        raise ValueError(f"{label} is empty")
    if any(not model_id for model_id in model_ids):
        raise ValueError(f"{label} contains a blank model ID")


def _as_utc_datetime(value: datetime | str) -> datetime:
    parsed = value if isinstance(value, datetime) else datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("roster lifecycle timestamps must include a timezone")
    return parsed.astimezone(timezone.utc)

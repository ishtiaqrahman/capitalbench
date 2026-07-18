from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping

from .config import load_model_configs
from .schemas import ModelConfig


PORTFOLIO_V2_METHODOLOGY = "portfolio-v2.0"
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


def validate_official_portfolio_v2_roster(
    methodology_version: str | None,
    model_configs: Iterable[ModelConfig],
) -> tuple[str, ...]:
    actual_ids = tuple(config.model_id for config in model_configs)
    if methodology_version != PORTFOLIO_V2_METHODOLOGY:
        return actual_ids

    expected_ids = canonical_portfolio_v2_model_ids()
    if Counter(actual_ids) != Counter(expected_ids):
        missing = sorted(Counter(expected_ids) - Counter(actual_ids))
        unexpected = sorted(Counter(actual_ids) - Counter(expected_ids))
        details: list[str] = []
        if missing:
            details.append(f"missing: {', '.join(missing)}")
        if unexpected:
            details.append(f"unexpected: {', '.join(unexpected)}")
        raise ValueError(
            "official Portfolio V2 runs require the complete canonical model roster"
            + (f" ({'; '.join(details)})" if details else "")
        )
    return actual_ids


def validate_official_portfolio_v2_run_manifest(
    methodology_version: str | None,
    run_manifest: Mapping[str, Any],
) -> None:
    if methodology_version != PORTFOLIO_V2_METHODOLOGY:
        return

    expected_ids = canonical_portfolio_v2_model_ids()
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
        raise ValueError("official Portfolio V2 run model_ids do not match the complete canonical roster")

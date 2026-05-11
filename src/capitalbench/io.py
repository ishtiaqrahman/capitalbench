from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .schemas import MarketOption, RoundManifest


def read_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def write_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False)


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")


def load_manifest(round_path: Path) -> RoundManifest:
    return RoundManifest.model_validate(read_yaml(round_path / "manifest.yaml"))


def load_options(round_path: Path) -> list[MarketOption]:
    return load_options_file(round_path / "options.yaml")


def load_options_file(path: Path) -> list[MarketOption]:
    data = read_yaml(path)
    raw_options = data.get("options", data) if isinstance(data, dict) else data
    if not isinstance(raw_options, list):
        raise ValueError(f"{path} must contain a list or an 'options' list")
    options = [MarketOption.model_validate(item) for item in raw_options]
    option_ids = [option.option_id for option in options]
    duplicates = sorted({option_id for option_id in option_ids if option_ids.count(option_id) > 1})
    if duplicates:
        raise ValueError(f"duplicate option_id values: {', '.join(duplicates)}")
    return options

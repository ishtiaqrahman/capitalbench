from __future__ import annotations

import hashlib
from pathlib import Path

from .io import read_json, write_json

HASHED_ROUND_FILES = ["briefing.md", "options.yaml", "prompt.md", "manifest.yaml"]
OPTIONAL_HASHED_ROUND_FILES = [
    "market_data/universe_trailing_returns.csv",
    "market_data/universe_trailing_returns.md",
    "market_data/universe_trailing_returns.json",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compute_round_hashes(round_path: Path) -> dict[str, object]:
    hashes: dict[str, str] = {}
    for filename in HASHED_ROUND_FILES:
        path = round_path / filename
        if not path.exists():
            raise FileNotFoundError(f"missing required round file: {path}")
        hashes[filename] = sha256_file(path)
    for filename in OPTIONAL_HASHED_ROUND_FILES:
        path = round_path / filename
        if path.exists():
            hashes[filename] = sha256_file(path)
    return {"algorithm": "sha256", "files": hashes}


def write_round_hashes(round_path: Path) -> dict[str, object]:
    hashes = compute_round_hashes(round_path)
    write_json(round_path / "hashes.json", hashes)
    return hashes


def read_round_hashes(round_path: Path) -> dict[str, object]:
    return read_json(round_path / "hashes.json")


def round_hashes_match(round_path: Path) -> bool:
    return read_round_hashes(round_path) == compute_round_hashes(round_path)

from copy import deepcopy
from pathlib import Path

from capitalbench.research_registry import (
    load_research_registry,
    validate_research_registry,
    validate_research_registry_file,
)


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research" / "registry.yaml"


def test_repository_research_registry_is_valid() -> None:
    assert validate_research_registry_file(REGISTRY, ROOT) == []


def test_registry_rejects_duplicate_ids() -> None:
    payload = load_research_registry(REGISTRY)
    payload["experiments"].append(deepcopy(payload["experiments"][0]))
    errors = validate_research_registry(payload, ROOT)
    assert any("duplicate experiment id" in error for error in errors)


def test_registry_rejects_disposable_output_as_canonical() -> None:
    payload = load_research_registry(REGISTRY)
    payload["experiments"][0]["canonical_artifacts"] = ["output/result.json"]
    errors = validate_research_registry(payload, ROOT)
    assert any("cannot be under output/" in error for error in errors)


def test_registry_rejects_missing_canonical_artifact() -> None:
    payload = load_research_registry(REGISTRY)
    payload["experiments"][0]["canonical_artifacts"] = ["docs/not-real.md"]
    errors = validate_research_registry(payload, ROOT)
    assert any("does not exist" in error for error in errors)

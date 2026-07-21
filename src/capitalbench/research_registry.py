from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


REQUIRED_FIELDS = {
    "id", "date", "status", "decision", "question", "method", "sample",
    "models", "calls", "gates", "findings", "lessons", "limitations",
    "canonical_artifacts", "related", "next_action",
}
ALLOWED_STATUSES = {"active", "complete"}
ALLOWED_DECISIONS = {"active", "accepted", "rejected", "inconclusive", "diagnostic_only"}


def load_research_registry(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("research registry must be a mapping")
    return payload


def validate_research_registry(payload: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    if payload.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if not isinstance(payload.get("current_program"), dict):
        errors.append("current_program must be a mapping")
    experiments = payload.get("experiments")
    if not isinstance(experiments, list) or not experiments:
        return errors + ["experiments must be a non-empty list"]

    known_ids = {
        str(item.get("id")) for item in experiments
        if isinstance(item, dict) and item.get("id")
    }
    seen: set[str] = set()
    for index, item in enumerate(experiments):
        prefix = f"experiments[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        experiment_id = str(item.get("id") or "")
        if not experiment_id:
            errors.append(f"{prefix}.id is required")
        elif experiment_id in seen:
            errors.append(f"duplicate experiment id: {experiment_id}")
        seen.add(experiment_id)
        missing = sorted(REQUIRED_FIELDS - set(item))
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(missing)}")
        if item.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{prefix}.status is invalid")
        if item.get("decision") not in ALLOWED_DECISIONS:
            errors.append(f"{prefix}.decision is invalid")
        if item.get("status") == "active" and item.get("decision") != "active":
            errors.append(f"{prefix} active status requires active decision")
        if item.get("status") == "complete" and item.get("decision") == "active":
            errors.append(f"{prefix} complete status cannot have active decision")
        for field in ("findings", "lessons", "limitations", "canonical_artifacts"):
            value = item.get(field)
            if not isinstance(value, list) or not value:
                errors.append(f"{prefix}.{field} must be a non-empty list")
        for artifact in item.get("canonical_artifacts") or []:
            artifact_text = str(artifact).replace("\\", "/")
            artifact_path = Path(artifact_text)
            if artifact_path.is_absolute() or ".." in artifact_path.parts:
                errors.append(f"{prefix} has unsafe artifact path: {artifact_text}")
            elif artifact_text == "output" or artifact_text.startswith("output/"):
                errors.append(f"{prefix} canonical artifact cannot be under output/: {artifact_text}")
            elif not (root / artifact_path).exists():
                errors.append(f"{prefix} canonical artifact does not exist: {artifact_text}")
        related = item.get("related")
        if not isinstance(related, list):
            errors.append(f"{prefix}.related must be a list")
        else:
            for related_id in related:
                if str(related_id) not in known_ids:
                    errors.append(f"{prefix} references unknown experiment: {related_id}")

    current_id = str((payload.get("current_program") or {}).get("experiment_id") or "")
    if current_id not in known_ids:
        errors.append("current_program.experiment_id must reference a registered experiment")
    return errors


def validate_research_registry_file(path: Path, root: Path) -> list[str]:
    return validate_research_registry(load_research_registry(path), root)

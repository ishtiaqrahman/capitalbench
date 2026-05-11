from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .io import read_json, read_yaml, write_yaml

LEGACY_RUN_ID = "legacy-run"


@dataclass(frozen=True)
class RunPaths:
    round_path: Path
    run_id: str
    run_path: Path
    raw_dir: Path
    parsed_dir: Path
    raw_responses_dir: Path
    results_dir: Path
    run_log_path: Path
    run_manifest_path: Path
    validation_summary_path: Path


@dataclass(frozen=True)
class RunListItem:
    run_id: str
    run_type: str
    mode: str
    replicates: int | None
    created_at_utc: str
    model_count: int | None
    valid_submissions: int | None
    invalid_submissions: int | None
    scored: bool
    report_exists: bool
    official_score_eligible: bool


def validate_run_id(run_id: str) -> str:
    run_id = run_id.strip()
    if not run_id:
        raise ValueError("run_id is required")
    if "/" in run_id or "\\" in run_id or run_id in {".", ".."}:
        raise ValueError(f"invalid run_id: {run_id}")
    return run_id


def generate_run_id(mode: str, mock: bool, run_type: str | None = None) -> str:
    suffix = (run_type or ("mock" if mock else mode)).replace("_", "-")
    return f"{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{suffix}"


def get_run_paths(round_path: Path, run_id: str) -> RunPaths:
    run_id = validate_run_id(run_id)
    run_path = round_path / "runs" / run_id
    return RunPaths(
        round_path=round_path,
        run_id=run_id,
        run_path=run_path,
        raw_dir=run_path / "submissions" / "raw",
        parsed_dir=run_path / "submissions" / "parsed",
        raw_responses_dir=run_path / "raw_responses",
        results_dir=run_path / "results",
        run_log_path=run_path / "run_log.jsonl",
        run_manifest_path=run_path / "run_manifest.yaml",
        validation_summary_path=run_path / "validation_summary.json",
    )


def create_run_paths(round_path: Path, run_id: str, overwrite: bool = False) -> RunPaths:
    paths = get_run_paths(round_path, run_id)
    if paths.run_path.exists():
        if not overwrite:
            raise FileExistsError(
                f"run_id already exists: {run_id}; pass --overwrite-run to replace only this run"
            )
        shutil.rmtree(paths.run_path)
    paths.raw_dir.mkdir(parents=True, exist_ok=True)
    paths.parsed_dir.mkdir(parents=True, exist_ok=True)
    paths.raw_responses_dir.mkdir(parents=True, exist_ok=True)
    paths.results_dir.mkdir(parents=True, exist_ok=True)
    return paths


def list_run_ids(round_path: Path) -> list[str]:
    runs_dir = round_path / "runs"
    if not runs_dir.exists():
        return []
    return sorted(item.name for item in runs_dir.iterdir() if item.is_dir())


def resolve_run_id(round_path: Path, run_id: str | None = None) -> str:
    migrate_legacy_run_if_needed(round_path)
    if run_id is not None:
        run_id = validate_run_id(run_id)
        if not (round_path / "runs" / run_id).is_dir():
            raise FileNotFoundError(f"run_id not found: {run_id}")
        return run_id

    run_ids = list_run_ids(round_path)
    if len(run_ids) == 1:
        return run_ids[0]
    if not run_ids:
        raise FileNotFoundError("no runs found; run capitalbench run-round first or pass --run-id")
    raise ValueError(
        "multiple runs found; pass --run-id. Available run_ids: "
        + ", ".join(run_ids)
    )


def get_selected_run_paths(round_path: Path, run_id: str | None = None) -> RunPaths:
    return get_run_paths(round_path, resolve_run_id(round_path, run_id))


def write_initial_run_manifest(
    paths: RunPaths,
    *,
    round_id: str,
    mode: str,
    run_type: str,
    mock: bool,
    models_path: Path,
    pricing_path: Path | None,
    replicates: int,
    allow_real_api_calls: bool,
    official_score_eligible: bool,
) -> None:
    write_yaml(
        paths.run_manifest_path,
        {
            "run_id": paths.run_id,
            "round_id": round_id,
            "run_type": run_type,
            "mode": mode,
            "mock": mock,
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "models_config_file": str(models_path),
            "models_path": str(models_path),
            "pricing_path": str(pricing_path) if pricing_path else None,
            "replicates": replicates,
            "allow_real_api_calls": allow_real_api_calls,
            "official_score_eligible": official_score_eligible,
            "model_count": None,
            "valid_submissions": None,
            "invalid_submissions": None,
        },
    )


def update_run_manifest(paths: RunPaths, updates: dict[str, object]) -> None:
    data = read_yaml(paths.run_manifest_path) if paths.run_manifest_path.exists() else {}
    data.update(updates)
    write_yaml(paths.run_manifest_path, data)


def read_run_manifest(paths: RunPaths) -> dict[str, object]:
    manifest = read_yaml(paths.run_manifest_path) if paths.run_manifest_path.exists() else {}
    return normalize_run_manifest(manifest)


def normalize_run_manifest(manifest: dict[str, object]) -> dict[str, object]:
    run_type = str(manifest.get("run_type") or "")
    mode = str(manifest.get("mode") or "")
    mock = manifest.get("mock")
    if run_type not in {"official", "stability", "mock", "provider_smoke", "retrospective"}:
        if mode == "stability":
            run_type = "stability"
        elif mode in {"legacy", "mock"} or mock is True:
            run_type = "mock"
        else:
            run_type = "official"
    replicates = _maybe_int(manifest.get("replicates")) or 1
    mock = manifest.get("mock")
    if run_type != "official" or mock is True:
        official_score_eligible = False
    elif "official_score_eligible" not in manifest:
        official_score_eligible = True
    else:
        official_score_eligible = bool(manifest.get("official_score_eligible"))
    return {
        **manifest,
        "run_type": run_type,
        "replicates": replicates,
        "official_score_eligible": official_score_eligible,
    }


def list_runs(round_path: Path) -> list[RunListItem]:
    migrate_legacy_run_if_needed(round_path)
    items: list[RunListItem] = []
    for run_id in list_run_ids(round_path):
        paths = get_run_paths(round_path, run_id)
        manifest = read_run_manifest(paths)
        validation = read_json(paths.validation_summary_path) if paths.validation_summary_path.exists() else {}
        items.append(
            RunListItem(
                run_id=run_id,
                run_type=str(manifest.get("run_type") or ""),
                mode=str(manifest.get("mode") or ""),
                replicates=_maybe_int(manifest.get("replicates")),
                created_at_utc=str(manifest.get("created_at_utc") or ""),
                model_count=_maybe_int(manifest.get("model_count")),
                valid_submissions=_maybe_int(validation.get("valid_count", manifest.get("valid_submissions"))),
                invalid_submissions=_maybe_int(validation.get("invalid_count", manifest.get("invalid_submissions"))),
                scored=(paths.results_dir / "leaderboard.csv").exists() or (paths.results_dir / "stability.csv").exists(),
                report_exists=(paths.results_dir / "report.md").exists(),
                official_score_eligible=bool(manifest.get("official_score_eligible")),
            )
        )
    return items


def migrate_legacy_run_if_needed(round_path: Path) -> bool:
    legacy_submissions = round_path / "submissions"
    legacy_results = round_path / "results"
    if not legacy_submissions.exists():
        return False
    legacy_paths = get_run_paths(round_path, LEGACY_RUN_ID)
    if legacy_paths.run_path.exists():
        return False

    legacy_paths.raw_dir.mkdir(parents=True, exist_ok=True)
    legacy_paths.parsed_dir.mkdir(parents=True, exist_ok=True)
    legacy_paths.results_dir.mkdir(parents=True, exist_ok=True)

    if (legacy_submissions / "raw").exists():
        _copy_contents(legacy_submissions / "raw", legacy_paths.raw_dir)
    if (legacy_submissions / "parsed").exists():
        _copy_contents(legacy_submissions / "parsed", legacy_paths.parsed_dir)
    if legacy_results.exists():
        _copy_contents(legacy_results, legacy_paths.results_dir)
        legacy_log = legacy_results / "run_log.jsonl"
        if legacy_log.exists():
            shutil.copy2(legacy_log, legacy_paths.run_log_path)

    round_id = read_yaml(round_path / "manifest.yaml").get("round_id", "") if (round_path / "manifest.yaml").exists() else ""
    write_yaml(
        legacy_paths.run_manifest_path,
        {
            "run_id": LEGACY_RUN_ID,
            "round_id": round_id,
            "run_type": "mock",
            "mode": "legacy",
            "mock": None,
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "models_config_file": None,
            "models_path": None,
            "pricing_path": None,
            "replicates": 1,
            "allow_real_api_calls": False,
            "official_score_eligible": False,
            "model_count": None,
            "valid_submissions": None,
            "invalid_submissions": None,
            "legacy_source": "round-level submissions/results migrated by CapitalBench v1.1",
        },
    )
    return True


def _copy_contents(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        destination = target / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(item, destination)


def _maybe_int(value: object) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

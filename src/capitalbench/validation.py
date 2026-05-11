from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from .io import load_manifest, load_options, read_json, read_yaml, write_json
from .run_store import get_selected_run_paths, read_run_manifest
from .schemas import MarketOption, ModelSubmission

SUBMISSION_EXTENSIONS = {".json", ".yaml", ".yml"}


@dataclass(frozen=True)
class SubmissionValidationSummary:
    raw_count: int
    valid_count: int
    invalid_count: int
    errors: dict[str, list[str]]


def _load_submission(path: Path) -> Any:
    if path.suffix == ".json":
        try:
            return read_json(path)
        except json.JSONDecodeError as exc:
            raise ValueError(f"malformed JSON: {exc}") from exc
    if path.suffix in {".yaml", ".yml"}:
        return read_yaml(path)
    raise ValueError(f"unsupported submission file type: {path}")


def _format_validation_error(error: ValidationError) -> list[str]:
    messages = []
    for item in error.errors():
        location = ".".join(str(part) for part in item["loc"])
        messages.append(f"{location}: {item['msg']}" if location else item["msg"])
    return messages


def validate_submission_payload(
    payload: Any,
    options: list[MarketOption],
    round_id: str | None = None,
    run_type: str | None = None,
    replicate_count: int | None = None,
    require_run_metadata: bool = False,
) -> ModelSubmission:
    if not isinstance(payload, dict):
        raise ValueError("submission must be a JSON/YAML object")

    multi_select_fields = {"selected_option_ids", "selected_options", "selections"}
    present_multi_select_fields = sorted(multi_select_fields.intersection(payload))
    if present_multi_select_fields:
        fields = ", ".join(present_multi_select_fields)
        raise ValueError(f"exactly one selected_option_id is required; remove {fields}")
    if isinstance(payload.get("selected_option_id"), list):
        raise ValueError("exactly one selected_option_id is required")

    try:
        submission = ModelSubmission.model_validate(payload)
    except ValidationError as error:
        raise ValueError("; ".join(_format_validation_error(error))) from error

    valid_option_ids = {option.option_id for option in options}
    if submission.selected_option_id not in valid_option_ids:
        raise ValueError(
            "selected_option_id must exist in options.yaml: "
            f"{submission.selected_option_id}"
        )
    if round_id is not None and submission.round_id != round_id:
        raise ValueError(
            "submission round_id does not match manifest.yaml: "
            f"{submission.round_id} != {round_id}"
        )
    _validate_run_metadata(
        submission,
        run_type=run_type,
        replicate_count=replicate_count,
        require_run_metadata=require_run_metadata,
    )
    return submission


def _validate_run_metadata(
    submission: ModelSubmission,
    *,
    run_type: str | None,
    replicate_count: int | None,
    require_run_metadata: bool,
) -> None:
    if run_type is None:
        return
    if run_type not in {"official", "stability", "mock", "provider_smoke", "retrospective"}:
        raise ValueError(f"unrecognized run_type in run manifest: {run_type}")

    has_run_metadata = any(
        value is not None
        for value in [submission.run_type, submission.replicate_index, submission.replicate_count]
    )
    if require_run_metadata or has_run_metadata:
        if submission.run_type != run_type:
            raise ValueError(f"submission run_type does not match run_manifest.yaml: {submission.run_type} != {run_type}")

    if run_type == "official":
        expected_count = replicate_count or 1
        if expected_count != 1:
            raise ValueError("official run has replicates > 1")
        if require_run_metadata or has_run_metadata:
            if submission.replicate_index != 1:
                raise ValueError("official submissions require replicate_index = 1")
            if submission.replicate_count != 1:
                raise ValueError("official submissions require replicate_count = 1")
            if submission.is_official_score is not True:
                raise ValueError("official submissions require is_official_score = true")

    if run_type == "stability":
        if replicate_count is None:
            raise ValueError("stability run_manifest.yaml must define replicates")
        if submission.replicate_index is None:
            raise ValueError("stability submissions require replicate_index")
        if submission.replicate_count is None:
            raise ValueError("stability submissions require replicate_count")
        if submission.replicate_count != replicate_count:
            raise ValueError(
                f"submission replicate_count does not match run_manifest.yaml: "
                f"{submission.replicate_count} != {replicate_count}"
            )
        if submission.replicate_index < 1 or submission.replicate_index > replicate_count:
            raise ValueError("replicate_index must be between 1 and replicate_count")
        if submission.is_official_score is not False:
            raise ValueError("stability submissions require is_official_score = false")

    if run_type == "retrospective":
        if require_run_metadata or has_run_metadata:
            if submission.is_official_score is not False:
                raise ValueError("retrospective submissions require is_official_score = false")


def iter_submission_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted(
        item
        for item in path.iterdir()
        if item.is_file()
        and item.suffix in SUBMISSION_EXTENSIONS
        and not item.name.startswith("_")
    )


def validate_submissions(
    round_path: Path,
    options: list[MarketOption] | None = None,
    run_id: str | None = None,
) -> SubmissionValidationSummary:
    manifest = load_manifest(round_path)
    if options is None:
        options = load_options(round_path)
    run_paths = get_selected_run_paths(round_path, run_id)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)
    require_run_metadata = run_type in {"official", "stability", "retrospective"}
    if run_type == "official" and replicate_count != 1:
        raise ValueError("official run has replicates > 1")
    raw_dir = run_paths.raw_dir
    parsed_dir = run_paths.parsed_dir
    raw_dir.mkdir(parents=True, exist_ok=True)
    parsed_dir.mkdir(parents=True, exist_ok=True)

    errors: dict[str, list[str]] = {}
    valid_count = 0
    raw_files = iter_submission_files(raw_dir)
    parsed_candidates: list[tuple[Path, Path, ModelSubmission]] = []

    for raw_file in raw_files:
        parsed_file = parsed_dir / f"{raw_file.stem}.json"
        try:
            payload = _load_submission(raw_file)
            submission = validate_submission_payload(
                payload,
                options,
                manifest.round_id,
                run_type=run_type,
                replicate_count=replicate_count,
                require_run_metadata=require_run_metadata,
            )
        except Exception as exc:
            errors[raw_file.name] = [str(exc)]
            if parsed_file.exists():
                parsed_file.unlink()
            continue

        parsed_candidates.append((raw_file, parsed_file, submission))

    sequence_errors = _validate_submission_sequence(parsed_candidates, run_type)
    for raw_file_name, message in sequence_errors.items():
        errors[raw_file_name] = [message]

    for raw_file, parsed_file, submission in parsed_candidates:
        if raw_file.name in errors:
            if parsed_file.exists():
                parsed_file.unlink()
            continue
        write_json(parsed_file, submission.model_dump(mode="json", exclude_none=True))
        valid_count += 1

    summary = SubmissionValidationSummary(
        raw_count=len(raw_files),
        valid_count=valid_count,
        invalid_count=len(errors),
        errors=errors,
    )
    summary_payload = {
        "run_id": run_paths.run_id,
        "run_type": run_type,
        "replicates": replicate_count,
        "raw_count": summary.raw_count,
        "valid_count": summary.valid_count,
        "invalid_count": summary.invalid_count,
        "errors": summary.errors,
    }
    write_json(raw_dir / "_validation_errors.json", errors)
    write_json(run_paths.validation_summary_path, summary_payload)
    return summary


def _validate_submission_sequence(
    candidates: list[tuple[Path, Path, ModelSubmission]],
    run_type: str,
) -> dict[str, str]:
    errors: dict[str, str] = {}
    if run_type == "official":
        seen_model_ids: set[str] = set()
        for raw_file, _parsed_file, submission in candidates:
            if submission.model_id in seen_model_ids:
                errors[raw_file.name] = f"duplicate model_id in official parsed submissions: {submission.model_id}"
                continue
            seen_model_ids.add(submission.model_id)
    elif run_type == "stability":
        seen_replicates: set[tuple[str, int | None]] = set()
        for raw_file, _parsed_file, submission in candidates:
            key = (submission.model_id, submission.replicate_index)
            if key in seen_replicates:
                errors[raw_file.name] = (
                    "duplicate replicate_index for model_id in stability parsed submissions: "
                    f"{submission.model_id} replicate {submission.replicate_index}"
                )
                continue
            seen_replicates.add(key)
    return errors

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .hashing import HASHED_ROUND_FILES, compute_round_hashes
from .io import load_manifest, load_options, read_json
from .prices import selected_price_options
from .portfolio import constraints_from_manifest, submission_format_from_manifest
from .research import (
    BRIEFING_AUDIT_REPORT,
    FINAL_BRIEFING,
    MARKET_FACT_REPORT,
    RESEARCH_HASHES,
    RESEARCH_MANIFEST,
    final_briefing_matches_round_briefing,
    only_final_briefing_model_facing,
)
from .run_store import RunPaths, get_run_paths, list_runs, read_run_manifest, resolve_run_id
from .scoring import read_price_records
from .validation import _load_submission, iter_submission_files, validate_submission_payload

REQUIRED_FILES = ["manifest.yaml", "briefing.md", "options.yaml", "prompt.md", "hashes.json"]
REQUIRED_DIRS = ["prices"]


@dataclass(frozen=True)
class AuditCheck:
    label: str
    ok: bool
    detail: str = ""


@dataclass(frozen=True)
class RoundAudit:
    round_path: Path
    checks: list[AuditCheck]
    lines: list[str]

    @property
    def ok(self) -> bool:
        return all(check.ok for check in self.checks)


def _yes_no(value: bool) -> str:
    return "yes" if value else "no"


def _count_invalid_raw_submissions(round_path: Path, run_paths: RunPaths) -> tuple[int, int, dict[str, list[str]]]:
    try:
        manifest = load_manifest(round_path)
        options = load_options(round_path)
        submission_format = submission_format_from_manifest(manifest)
        portfolio_constraints = constraints_from_manifest(manifest)
    except Exception as exc:
        return 0, 0, {"round": [str(exc)]}

    raw_files = iter_submission_files(run_paths.raw_dir)
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)
    errors: dict[str, list[str]] = {}
    valid_count = 0
    for raw_file in raw_files:
        try:
            payload = _load_submission(raw_file)
            validate_submission_payload(
                payload,
                options,
                manifest.round_id,
                run_type=run_type,
                replicate_count=replicate_count,
                require_run_metadata=run_type in {"official", "stability", "retrospective"},
                submission_format=submission_format,
                portfolio_constraints=portfolio_constraints,
            )
        except Exception as exc:
            errors[raw_file.name] = [str(exc)]
            continue
        valid_count += 1
    return len(raw_files), valid_count, errors


def _count_valid_parsed_submissions(round_path: Path, run_paths: RunPaths) -> int:
    try:
        manifest = load_manifest(round_path)
        options = load_options(round_path)
        submission_format = submission_format_from_manifest(manifest)
        portfolio_constraints = constraints_from_manifest(manifest)
    except Exception:
        return 0

    valid_count = 0
    run_manifest = read_run_manifest(run_paths)
    run_type = str(run_manifest.get("run_type") or "mock")
    replicate_count = int(run_manifest.get("replicates") or 1)
    for parsed_file in iter_submission_files(run_paths.parsed_dir):
        try:
            validate_submission_payload(
                read_json(parsed_file),
                options,
                manifest.round_id,
                run_type=run_type,
                replicate_count=replicate_count,
                require_run_metadata=run_type in {"official", "stability", "retrospective"},
                submission_format=submission_format,
                portfolio_constraints=portfolio_constraints,
            )
        except Exception:
            continue
        valid_count += 1
    return valid_count


def _price_keys_for_option(option) -> set[str]:
    return {key for key in [option.option_id, option.symbol, option.tiingo_symbol, option.asset_symbol] if key}


def _audit_prices(round_path: Path, run_paths: RunPaths | None = None) -> tuple[list[AuditCheck], list[str]]:
    checks: list[AuditCheck] = []
    lines: list[str] = []
    entry_path = round_path / "prices" / "entry_prices.csv"
    exit_path = round_path / "prices" / "exit_prices.csv"
    entry_exists = entry_path.exists()
    exit_exists = exit_path.exists()
    checks.append(AuditCheck("entry prices exist", entry_exists, str(entry_path)))
    checks.append(AuditCheck("exit prices exist", exit_exists, str(exit_path)))
    lines.append(f"Entry prices exist: {_yes_no(entry_exists)}")
    lines.append(f"Exit prices exist: {_yes_no(exit_exists)}")

    if not entry_exists or not exit_exists:
        return checks, lines

    try:
        options = load_options(round_path)
        entry_prices = read_price_records(entry_path)
        exit_prices = read_price_records(exit_path)
    except Exception as exc:
        checks.append(AuditCheck("prices readable", False, str(exc)))
        lines.append(f"Prices readable: no ({exc})")
        return checks, lines

    full_universe_missing: list[str] = []
    for option in options:
        is_cash = option.is_cash or option.option_id.upper() == "CASH" or option.asset_symbol.upper() in {"USD", "CASH"}
        if is_cash:
            continue
        price_keys = _price_keys_for_option(option)
        if not price_keys.intersection(entry_prices):
            full_universe_missing.append(f"{option.option_id} entry")
        if not price_keys.intersection(exit_prices):
            full_universe_missing.append(f"{option.option_id} exit")

    full_universe_complete = not full_universe_missing
    lines.append(f"Full-universe prices available: {_yes_no(full_universe_complete)}")
    if full_universe_missing:
        lines.append("Missing full-universe prices: " + ", ".join(full_universe_missing))

    if run_paths is not None:
        try:
            required_options = selected_price_options(round_path, run_paths.run_id)
        except Exception as exc:
            checks.append(AuditCheck("selected price requirements computable", False, str(exc)))
            lines.append(f"Selected price requirements computable: no ({exc})")
            return checks, lines
        selected_missing: list[str] = []
        for option in required_options:
            if option.is_cash or option.option_id.upper() == "CASH" or option.asset_symbol.upper() in {"USD", "CASH"}:
                continue
            price_keys = _price_keys_for_option(option)
            if not price_keys.intersection(entry_prices):
                selected_missing.append(f"{option.option_id} entry")
            if not price_keys.intersection(exit_prices):
                selected_missing.append(f"{option.option_id} exit")
        selected_prices_complete = not selected_missing
        checks.append(AuditCheck("selected options and SP500 have prices", selected_prices_complete, ", ".join(selected_missing)))
        lines.append(f"Selected options and SP500 have prices: {_yes_no(selected_prices_complete)}")
        if selected_missing:
            lines.append("Missing selected-run prices: " + ", ".join(selected_missing))
    return checks, lines


def _audit_research(round_path: Path) -> tuple[list[AuditCheck], list[str]]:
    checks: list[AuditCheck] = []
    lines: list[str] = ["Research artifacts:"]
    research_dir = round_path / "research"
    filenames = [
        MARKET_FACT_REPORT,
        BRIEFING_AUDIT_REPORT,
        FINAL_BRIEFING,
        RESEARCH_MANIFEST,
        RESEARCH_HASHES,
    ]
    has_any_research = research_dir.exists() or any((research_dir / filename).exists() for filename in filenames)
    for filename in filenames:
        exists = (research_dir / filename).exists()
        if has_any_research:
            checks.append(AuditCheck(f"research/{filename} exists", exists))
        lines.append(f"  research/{filename} exists: {_yes_no(exists)}")

    briefing_match = final_briefing_matches_round_briefing(round_path)
    if briefing_match is None:
        lines.append("  final_briefing.md hash matches briefing.md: unavailable")
    else:
        if has_any_research:
            checks.append(AuditCheck("final briefing matches briefing.md", briefing_match))
        lines.append(f"  final_briefing.md hash matches briefing.md: {_yes_no(briefing_match)}")
        if not briefing_match:
            lines.append("  Warning: research/final_briefing.md and briefing.md do not match")

    model_facing_ok = only_final_briefing_model_facing(round_path)
    if model_facing_ok is None:
        lines.append("  only final_briefing is model-facing: unavailable")
    else:
        if has_any_research:
            checks.append(AuditCheck("only final briefing is model-facing", model_facing_ok))
        lines.append(f"  only final_briefing is model-facing: {_yes_no(model_facing_ok)}")
    return checks, lines


def audit_round(round_path: Path, run_id: str | None = None) -> RoundAudit:
    checks: list[AuditCheck] = []
    lines: list[str] = [f"CapitalBench audit: {round_path}"]

    for filename in REQUIRED_FILES:
        exists = (round_path / filename).exists()
        checks.append(AuditCheck(f"required file {filename}", exists))
        lines.append(f"Required file {filename}: {_yes_no(exists)}")

    for dirname in REQUIRED_DIRS:
        exists = (round_path / dirname).is_dir()
        checks.append(AuditCheck(f"required directory {dirname}", exists))
        lines.append(f"Required directory {dirname}: {_yes_no(exists)}")

    try:
        current_hashes = compute_round_hashes(round_path)
        lines.append("Current SHA256 hashes:")
        for filename, digest in current_hashes["files"].items():
            lines.append(f"  {filename}: {digest}")
    except Exception as exc:
        checks.append(AuditCheck("current hashes computable", False, str(exc)))
        lines.append(f"Current SHA256 hashes: unavailable ({exc})")
        current_hashes = None

    hashes_path = round_path / "hashes.json"
    if hashes_path.exists() and current_hashes is not None:
        try:
            stored_hashes = read_json(hashes_path)
            hashes_match = stored_hashes == current_hashes
            checks.append(AuditCheck("hashes.json matches current files", hashes_match))
            lines.append(f"hashes.json matches current files: {_yes_no(hashes_match)}")
        except Exception as exc:
            checks.append(AuditCheck("hashes.json readable", False, str(exc)))
            lines.append(f"hashes.json readable: no ({exc})")

    research_checks, research_lines = _audit_research(round_path)
    checks.extend(research_checks)
    lines.extend(research_lines)

    available_runs = list_runs(round_path)
    if available_runs:
        lines.append("Available runs:")
        for item in available_runs:
            lines.append(
                "  "
                + f"{item.run_id} "
                + f"(run_type={item.run_type}, replicates={item.replicates}, "
                + f"valid={item.valid_submissions}, invalid={item.invalid_submissions}, "
                + f"official_score_eligible={_yes_no(item.official_score_eligible)}, "
                + f"leaderboard={_yes_no((round_path / 'runs' / item.run_id / 'results' / 'leaderboard.csv').exists())}, "
                + f"stability={_yes_no((round_path / 'runs' / item.run_id / 'results' / 'stability.csv').exists())}, "
                + f"report={_yes_no(item.report_exists)})"
            )
    else:
        lines.append("Available runs: none")
    official_runs = [item.run_id for item in available_runs if item.official_score_eligible]
    if len(official_runs) > 1:
        lines.append(
            "Warning: multiple official-score-eligible runs found. "
            "Public reporting should identify exactly one official run."
        )

    selected_run_id: str | None = None
    if run_id is not None:
        selected_run_id = resolve_run_id(round_path, run_id)
    elif len(available_runs) > 1:
        lines.append("Warning: multiple runs exist; pass --run-id to audit one run")

    if selected_run_id is not None:
        run_paths = get_run_paths(round_path, selected_run_id)
        run_manifest = read_run_manifest(run_paths)
        price_checks, price_lines = _audit_prices(round_path, run_paths)
        checks.extend(price_checks)
        lines.extend(price_lines)
        run_type = str(run_manifest.get("run_type") or "mock")
        lines.append(f"Selected run: {selected_run_id}")
        lines.append(f"Run type: {run_type}")
        lines.append(f"Replicates: {run_manifest.get('replicates')}")
        lines.append(f"Official score eligible: {_yes_no(bool(run_manifest.get('official_score_eligible')))}")

        run_required = [
            ("submissions/raw", run_paths.raw_dir.is_dir()),
            ("submissions/parsed", run_paths.parsed_dir.is_dir()),
            ("raw_responses", run_paths.raw_responses_dir.is_dir()),
            ("run_log.jsonl", run_paths.run_log_path.exists()),
            ("run_manifest.yaml", run_paths.run_manifest_path.exists()),
            ("validation_summary.json", run_paths.validation_summary_path.exists()),
        ]
        for label, exists in run_required:
            checks.append(AuditCheck(f"run {label} exists", exists))
            lines.append(f"Run {label}: {_yes_no(exists)}")

        raw_count, raw_valid_count, raw_errors = _count_invalid_raw_submissions(round_path, run_paths)
        parsed_valid_count = _count_valid_parsed_submissions(round_path, run_paths)
        lines.append(f"Raw submissions: {raw_count}")
        lines.append(f"Raw valid submissions: {raw_valid_count}")
        lines.append(f"Parsed valid submissions: {parsed_valid_count}")
        lines.append(f"Invalid submissions: {len(raw_errors)}")
        raw_response_count = len(list(run_paths.raw_responses_dir.glob("*.txt"))) if run_paths.raw_responses_dir.is_dir() else 0
        raw_response_ok = raw_response_count == raw_count
        raw_response_preservation = str(run_manifest.get("raw_response_text_preservation") or "")
        raw_response_legacy_sha_only = (
            raw_response_preservation == "sha_only_for_this_run"
            and raw_response_count == 0
            and raw_count > 0
            and run_paths.raw_responses_dir.is_dir()
        )
        checks.append(
            AuditCheck(
                "raw response text files exist for every raw submission",
                raw_response_ok or raw_response_legacy_sha_only,
            )
        )
        lines.append(f"Raw response text files: {raw_response_count}/{raw_count}")
        if raw_response_legacy_sha_only:
            lines.append("Raw response text files note: legacy SHA-only run disclosed in run_manifest.yaml")
        if raw_errors:
            lines.append("Invalid submission files: " + ", ".join(sorted(raw_errors)))

        returns_exists = (run_paths.results_dir / "returns.csv").exists()
        leaderboard_exists = (run_paths.results_dir / "leaderboard.csv").exists()
        stability_exists = (run_paths.results_dir / "stability.csv").exists()
        report_exists = (run_paths.results_dir / "report.md").exists()
        results_exist = returns_exists and (stability_exists if run_type == "stability" else leaderboard_exists)
        lines.append(f"Results exist: {_yes_no(results_exist)}")
        lines.append(f"Leaderboard exists: {_yes_no(leaderboard_exists)}")
        lines.append(f"Stability results exist: {_yes_no(stability_exists)}")
        lines.append(f"Report exists: {_yes_no(report_exists)}")
    else:
        price_checks, price_lines = _audit_prices(round_path)
        checks.extend(price_checks)
        lines.extend(price_lines)

    lines.append(f"Audit status: {'PASS' if all(check.ok for check in checks) else 'FAIL'}")
    return RoundAudit(round_path=round_path, checks=checks, lines=lines)

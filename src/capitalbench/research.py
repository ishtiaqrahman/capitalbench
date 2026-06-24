from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .hashing import sha256_file, write_round_hashes
from .io import load_manifest, read_json, write_json, write_yaml

RESEARCH_DIRNAME = "research"
MARKET_FACT_REPORT = "market_fact_report.md"
BRIEFING_AUDIT_REPORT = "briefing_audit_report.md"
FINAL_BRIEFING = "final_briefing.md"
RESEARCH_MANIFEST = "research_manifest.yaml"
RESEARCH_HASHES = "research_hashes.json"
RESEARCH_FILES = [MARKET_FACT_REPORT, BRIEFING_AUDIT_REPORT, FINAL_BRIEFING, RESEARCH_MANIFEST]

RECOMMENDATION_PATTERNS = [
    "best pick",
    "should buy",
    "top choice",
    "will outperform",
    "recommended option",
    "final recommendation",
    "ranked #1",
    "best option",
    "worst option",
]

SUBJECTIVE_MODEL_FACING_PATTERNS = [
    "scenario analysis",
    "why it matters",
    "affected market areas",
    "affected-market mapping",
    "market impact",
    "investment thesis",
    "market thesis",
    "interpretation",
    "this favors",
    "this hurts",
    "will benefit",
    "should benefit",
    "likely benefit",
    "benefits from",
    "will suffer",
    "should suffer",
    "likely suffer",
    "suffers from",
    "should outperform",
    "likely to outperform",
    "expected to outperform",
    "underperform",
    "best positioned",
    "dominant narrative",
    "attractive",
    "unattractive",
    "favorable",
    "unfavorable",
    "constructive",
]


@dataclass(frozen=True)
class ResearchImportSummary:
    research_dir: Path
    copied_files: list[Path]
    research_manifest_path: Path
    research_hashes_path: Path
    round_hashes_path: Path
    warnings: list[str]


def import_research_artifacts(
    *,
    round_path: Path,
    market_fact_report: Path,
    audit_report: Path,
    final_briefing: Path,
    research_cutoff_utc: str,
) -> ResearchImportSummary:
    manifest = load_manifest(round_path)
    warnings = validate_final_briefing(final_briefing)
    research_dir = round_path / RESEARCH_DIRNAME
    research_dir.mkdir(parents=True, exist_ok=True)

    targets = [
        (market_fact_report, research_dir / MARKET_FACT_REPORT),
        (audit_report, research_dir / BRIEFING_AUDIT_REPORT),
        (final_briefing, research_dir / FINAL_BRIEFING),
    ]
    copied_files: list[Path] = []
    for source, target in targets:
        if not source.exists():
            raise FileNotFoundError(f"research artifact not found: {source}")
        if not source.is_file():
            raise ValueError(f"research artifact is not a file: {source}")
        shutil.copy2(source, target)
        copied_files.append(target)

    briefing_path = round_path / "briefing.md"
    shutil.copy2(research_dir / FINAL_BRIEFING, briefing_path)

    research_manifest_path = research_dir / RESEARCH_MANIFEST
    write_yaml(
        research_manifest_path,
        {
            "round_id": manifest.round_id,
            "research_cutoff_utc": research_cutoff_utc,
            "decision_deadline_utc": manifest.decision_deadline,
            "research_files": [
                {
                    "filename": MARKET_FACT_REPORT,
                    "artifact_type": "market_fact_report",
                    "model_facing": False,
                    "description": "Deep Research market facts report; audit-only source material.",
                },
                {
                    "filename": BRIEFING_AUDIT_REPORT,
                    "artifact_type": "audit_report",
                    "model_facing": False,
                    "description": "Independent audit and gap-check report; audit-only source material.",
                },
                {
                    "filename": FINAL_BRIEFING,
                    "artifact_type": "final_briefing",
                    "model_facing": True,
                    "description": "Final model-facing CapitalBench briefing copied to briefing.md.",
                },
            ],
        },
    )

    research_hashes_path = write_research_hashes(round_path)
    round_hashes = write_round_hashes(round_path)
    return ResearchImportSummary(
        research_dir=research_dir,
        copied_files=copied_files,
        research_manifest_path=research_manifest_path,
        research_hashes_path=research_hashes_path,
        round_hashes_path=round_path / "hashes.json",
        warnings=warnings,
    )


def validate_final_briefing(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"final briefing not found: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("final_briefing.md cannot be empty")
    lowered = text.lower()
    for phrase in RECOMMENDATION_PATTERNS:
        if phrase in lowered:
            raise ValueError(f"final_briefing.md contains prohibited recommendation/ranking language: {phrase}")
    for phrase in SUBJECTIVE_MODEL_FACING_PATTERNS:
        if phrase in lowered:
            raise ValueError(f"final_briefing.md contains prohibited subjective/analysis language: {phrase}")

    warnings: list[str] = []
    if re.search(r"https?://|www\.", text, flags=re.IGNORECASE):
        warnings.append("URLs found in final_briefing.md; source links should usually stay in audit artifacts.")
    if re.search(r"\[[^\]]+\]\([^)]+\)", text) or re.search(r"^\s*\[[^\]]+\]:", text, flags=re.MULTILINE):
        warnings.append("Markdown citations found in final_briefing.md; source citations should usually stay in audit artifacts.")
    if re.search(r"\b(source ledger|sources?:|references?:|bibliography|citations?)\b", text, flags=re.IGNORECASE):
        warnings.append("Source ledger language found in final_briefing.md; source ledgers should stay in audit artifacts.")
    if re.search(r"\bselected mechanical return context\b", text, flags=re.IGNORECASE):
        raise ValueError(
            "final_briefing.md contains selected mechanical return context; keep mechanical price context "
            "in market_data/universe_trailing_returns.md so every option gets the same price-history interpretation."
        )
    if len(text.split()) > 8000:
        warnings.append("final_briefing.md is very long; confirm the model-facing briefing is concise enough for the target models.")
    return warnings


def compute_research_hashes(round_path: Path) -> dict[str, object]:
    research_dir = round_path / RESEARCH_DIRNAME
    hashes: dict[str, str] = {}
    for filename in RESEARCH_FILES:
        path = research_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"missing research file: {path}")
        hashes[f"{RESEARCH_DIRNAME}/{filename}"] = sha256_file(path)
    return {"algorithm": "sha256", "files": hashes}


def write_research_hashes(round_path: Path) -> Path:
    research_dir = round_path / RESEARCH_DIRNAME
    hashes = compute_research_hashes(round_path)
    path = research_dir / RESEARCH_HASHES
    write_json(path, hashes)
    return path


def read_research_hashes(round_path: Path) -> dict[str, object] | None:
    path = round_path / RESEARCH_DIRNAME / RESEARCH_HASHES
    if not path.exists():
        return None
    return read_json(path)


def research_artifact_rows(round_path: Path) -> list[dict[str, Any]]:
    research_dir = round_path / RESEARCH_DIRNAME
    stored_hashes = read_research_hashes(round_path) or {"files": {}}
    files = stored_hashes.get("files") if isinstance(stored_hashes, dict) else {}
    if not isinstance(files, dict):
        files = {}
    metadata = [
        (MARKET_FACT_REPORT, "Market fact report", "audit-only"),
        (BRIEFING_AUDIT_REPORT, "Briefing audit report", "audit-only"),
        (FINAL_BRIEFING, "Final briefing", "model-facing"),
    ]
    rows: list[dict[str, Any]] = []
    for filename, label, visibility in metadata:
        key = f"{RESEARCH_DIRNAME}/{filename}"
        rows.append(
            {
                "artifact": label,
                "path": key,
                "visibility": visibility,
                "sha256": files.get(key, ""),
                "exists": "yes" if (research_dir / filename).exists() else "no",
            }
        )
    return rows


def final_briefing_matches_round_briefing(round_path: Path) -> bool | None:
    final_path = round_path / RESEARCH_DIRNAME / FINAL_BRIEFING
    briefing_path = round_path / "briefing.md"
    if not final_path.exists() or not briefing_path.exists():
        return None
    return sha256_file(final_path) == sha256_file(briefing_path)


def only_final_briefing_model_facing(round_path: Path) -> bool | None:
    manifest_path = round_path / RESEARCH_DIRNAME / RESEARCH_MANIFEST
    if not manifest_path.exists():
        return None
    import yaml

    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    files = data.get("research_files")
    if not isinstance(files, list):
        return False
    model_facing = [item for item in files if isinstance(item, dict) and item.get("model_facing") is True]
    return len(model_facing) == 1 and model_facing[0].get("filename") == FINAL_BRIEFING

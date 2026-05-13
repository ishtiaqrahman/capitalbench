#!/usr/bin/env python3
"""Audit files that are eligible to enter the public repository.

The repository intentionally publishes benchmark methodology, normalized
submissions, sanitized run metadata, reports, and hashes. It must not publish
operator secrets, local credentials, provider smoke-test output, raw provider
responses, generated screenshots, or deployment-only identifiers.
"""

from __future__ import annotations

import fnmatch
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

SENSITIVE_ENV_NAMES = {
    "ANTHROPIC_API_KEY",
    "CLOUDFLARE_API_TOKEN",
    "CLOUDFLARE_PAGES_DEPLOY_HOOK",
    "GOOGLE_API_KEY",
    "GITHUB_TOKEN",
    "OPENAI_API_KEY",
    "PUBLIC_SUPABASE_ANON_KEY",
    "STRIPE_API_KEY",
    "STRIPE_PUBLISHABLE_KEY",
    "STRIPE_RESTRICTED_KEY",
    "STRIPE_SECRET_KEY",
    "STRIPE_WEBHOOK_SECRET",
    "SUPABASE_ANON_KEY",
    "SUPABASE_SERVICE_ROLE_KEY",
    "TIINGO_API_KEY",
    "XAI_API_KEY",
}

TOKEN_PATTERNS = [
    ("OpenAI API key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("Anthropic API key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b")),
    ("Stripe secret or restricted key", re.compile(r"\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{16,}\b")),
    ("Stripe publishable key", re.compile(r"\bpk_(?:live|test)_[A-Za-z0-9]{16,}\b")),
    ("Stripe webhook secret", re.compile(r"\bwhsec_[A-Za-z0-9]{16,}\b")),
    ("Cloudflare API token", re.compile(r"\bcf[a-z0-9]{2}_[A-Za-z0-9_-]{20,}\b")),
    ("xAI API key", re.compile(r"\bxai-[A-Za-z0-9_-]{20,}\b")),
    ("JWT-like token", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("Bearer token", re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}")),
    ("Supabase project URL", re.compile(r"https://[a-z0-9]{20}\.supabase\.co")),
]

ENV_ASSIGNMENT_RE = re.compile(
    r"^\s*(?:export\s+)?(?P<key>[A-Z][A-Z0-9_]{2,})\s*(?::|=)\s*(?P<value>.+?)\s*(?:#.*)?$"
)
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PROJECT_REF_LINE_RE = re.compile(r"\b[a-z0-9]{20}\b")

FORBIDDEN_GLOBS = {
    "build output": ["build/**", "dist/**", "apps/web/dist/**"],
    "generated local output": ["output/**"],
    "Node dependencies": ["node_modules/**", "apps/web/node_modules/**"],
    "Playwright cache": [".playwright-cli/**"],
    "Supabase local temp data": ["supabase/.temp/**"],
    "local model config": ["configs/*.local.yaml"],
    "private provider smoke output": ["rounds/*/provider-smoke-tests/**", "rounds/*/runs/*/provider-smoke-tests/**"],
    "private raw provider response": [
        "rounds/*/runs/*/raw_response.txt",
        "rounds/*/runs/*/smoke_log.json",
        "rounds/*/runs/*/raw_responses/**",
    ],
    "private key material": ["*.pem", "*.key", "*.p8", "*.p12", "*.mobileprovision"],
    "local database": ["*.db", "*.sqlite", "*.sqlite3"],
}

RAW_RESPONSE_README_GLOB = "rounds/*/runs/*/raw_responses/README.md"
RUN_LOG_DENIED_KEYS = {
    "api_key",
    "authorization",
    "content",
    "headers",
    "prompt",
    "provider_payload",
    "provider_response",
    "raw_response",
    "raw_response_text",
    "response_text",
}


@dataclass(frozen=True)
class Finding:
    path: str
    message: str
    line: int | None = None

    def format(self) -> str:
        location = self.path if self.line is None else f"{self.path}:{self.line}"
        return f"{location}: {self.message}"


def git_candidate_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def is_allowed_placeholder(value: str) -> bool:
    stripped = value.strip().strip('"').strip("'")
    lower = stripped.lower()
    return (
        not stripped
        or stripped.startswith("${{")
        or stripped.startswith("$")
        or stripped.startswith("<")
        or stripped.startswith("replace_with")
        or stripped.startswith("REPLACE_")
        or "replace-with" in lower
        or "replace_with" in lower
        or "placeholder" in lower
        or "example" in lower
        or lower in {"dummy", "test", "test-key", "test_key", "none", "null"}
    )


def file_text(path: Path) -> str | None:
    data = path.read_bytes()
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="ignore")


def audit_path(path: Path) -> list[Finding]:
    path_str = rel(path)
    findings: list[Finding] = []

    if path_str == ".env" or (path_str.startswith(".env.") and path_str != ".env.example"):
        findings.append(Finding(path_str, "environment files must stay local; only .env.example is public"))

    for label, patterns in FORBIDDEN_GLOBS.items():
        if path_str.endswith("/raw_responses/README.md") and matches_any(path_str, [RAW_RESPONSE_README_GLOB]):
            continue
        if matches_any(path_str, patterns):
            findings.append(Finding(path_str, f"{label} should not be committed to the public repo"))
            break

    return findings


def nested_keys(value: object) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from nested_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from nested_keys(child)


def audit_run_log(path: Path, text: str) -> list[Finding]:
    path_str = rel(path)
    findings: list[Finding] = []
    if path.name != "run_log.jsonl":
        return findings

    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            record = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        denied = sorted(set(nested_keys(record)).intersection(RUN_LOG_DENIED_KEYS))
        if denied:
            findings.append(
                Finding(
                    path_str,
                    "run logs may contain sanitized audit metadata only; remove fields "
                    + ", ".join(f"`{key}`" for key in denied),
                    line_number,
                )
            )
    return findings


def audit_text(path: Path, text: str) -> list[Finding]:
    path_str = rel(path)
    findings: list[Finding] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        for label, pattern in TOKEN_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(path_str, f"possible {label} found", line_number))

        env_match = ENV_ASSIGNMENT_RE.match(line)
        if env_match:
            key = env_match.group("key")
            value = env_match.group("value")
            if key in SENSITIVE_ENV_NAMES and not is_allowed_placeholder(value):
                findings.append(Finding(path_str, f"`{key}` appears to be assigned a real value", line_number))

        lower = line.lower()
        if "supabase account" in lower and EMAIL_RE.search(line):
            findings.append(Finding(path_str, "do not publish the operational Supabase account email", line_number))
        if "project ref" in lower and PROJECT_REF_LINE_RE.search(line) and "replace" not in lower:
            findings.append(Finding(path_str, "do not publish the Supabase project ref", line_number))

    findings.extend(audit_run_log(path, text))
    return findings


def main() -> int:
    try:
        files = git_candidate_files()
    except subprocess.CalledProcessError as exc:
        print(f"public repo audit failed to list git files: {exc}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    scanned_text_files = 0
    for path in files:
        if not path.exists() or path.is_dir():
            continue
        findings.extend(audit_path(path))
        text = file_text(path)
        if text is None:
            continue
        scanned_text_files += 1
        findings.extend(audit_text(path, text))

    if findings:
        print("Public repo audit failed:\n")
        for finding in findings:
            print(f"- {finding.format()}")
        print("\nRemove the file, replace the value with a placeholder, or add a narrow allowlist in the audit script.")
        return 1

    print(f"Public repo audit passed: scanned {len(files)} candidate files and {scanned_text_files} text files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

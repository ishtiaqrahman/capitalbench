from __future__ import annotations

from pathlib import Path

from capitalbench.research_registry import validate_research_registry_file


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research" / "registry.yaml"


def main() -> int:
    errors = validate_research_registry_file(REGISTRY, ROOT)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"research_registry_valid={REGISTRY.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

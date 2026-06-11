#!/usr/bin/env python3
"""Verify behavior-changing proof is wired into source-to-system extraction."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "behavior contract": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "behavior-changing-extraction-contract.md",
    "source extraction primitive": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "source-to-skill-extraction.md",
    "skill system contract": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "skill-system-contract.md",
    "source-to-skill workflow": ROOT / ".agent" / "workflows" / "source-to-skill-system.md",
    "sam proof lab": ROOT / "_active" / "sam-parr-copywriting-os" / "06-before-after-proof-lab.md",
    "sam command": ROOT / ".agent" / "workflows" / "sam-parr-copywriting-mechanics.md",
}

REQUIRED_PHRASES = {
    "behavior contract": [
        "Behavior Proof",
        "Behavior delta",
        "before/after",
        "cold-start run",
    ],
    "source extraction primitive": [
        "Behavior-changing proof",
        "Structural pass, usefulness fail",
    ],
    "skill system contract": [
        "Behavior-changing proof",
        "transformed artifact",
    ],
    "source-to-skill workflow": [
        "Require behavior-changing proof",
        "verify_behavior_changing_extraction_contract.py",
    ],
    "sam proof lab": [
        "Weak-Copy Fixture",
        "Behavior Delta",
        "Remaining Risk",
    ],
    "sam command": [
        "Original weak section",
        "Before/after delta",
        "Reader-behavior explanation",
    ],
}


def main() -> int:
    failures: list[str] = []
    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        searchable = content.lower()
        for phrase in REQUIRED_PHRASES[label]:
            if phrase.lower() not in searchable:
                failures.append(f"{label} missing phrase: {phrase}")

    if failures:
        print("Behavior-changing extraction contract: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Behavior-changing extraction contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

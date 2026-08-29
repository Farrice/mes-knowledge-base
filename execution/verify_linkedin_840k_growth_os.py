#!/usr/bin/env python3
"""Verify source, wiring, runtime, and safety for the LinkedIn 840K growth OS."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "source contract": ROOT / "extractions/video-context/GKbNTGLfd34/source-to-skill-contract.md",
    "deep extraction": ROOT / "extractions/video-context/GKbNTGLfd34/deep-extraction.md",
    "behavior proof": ROOT / "extractions/video-context/GKbNTGLfd34/behavior-proof.md",
    "mastery report": ROOT / "extractions/video-context/GKbNTGLfd34/virtuoso-mastery-extraction-report.md",
    "crown jewel map": ROOT / "extractions/video-context/GKbNTGLfd34/crown-jewel-prompt-suite.md",
    "transcendence dossier": ROOT / "extractions/video-context/GKbNTGLfd34/transcendence-opportunity-dossier.md",
    "hook deck transcript": ROOT / "extractions/video-context/GKbNTGLfd34/hook-deck-transcript.md",
    "source uncertainty": ROOT / "extractions/video-context/GKbNTGLfd34/uncertainty-report.md",
    "source guide": ROOT / "extractions/video-context/GKbNTGLfd34/hubspot-full-content.md",
    "source deck": ROOT / "extractions/video-context/GKbNTGLfd34/ben-meer-10-hook-frameworks.pptx",
    "workflow": ROOT / "skills/diandra-escobar-linkedin-growth/workflows/23-zero-to-840k-operating-system.md",
    "prompt": ROOT / "skills/diandra-escobar-linkedin-growth/references/prompts-v2/zero-to-840k-operating-system.md",
    "reference": ROOT / "skills/diandra-escobar-linkedin-growth/references/ben-meer-hubspot-growth-layer.md",
    "runtime": ROOT / "execution/linkedin_growth_os.py",
    "runtime tests": ROOT / "execution/test_linkedin_growth_os.py",
}


def require_terms(label: str, path: Path, terms: tuple[str, ...], failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    for term in terms:
        if term.lower() not in text:
            failures.append(f"{label} missing required term: {term}")


def main() -> int:
    failures = [f"missing {label}: {path.relative_to(ROOT)}" for label, path in REQUIRED.items() if not path.is_file() or path.stat().st_size == 0]
    if not failures:
        require_terms(
            "contract",
            REQUIRED["source contract"],
            ("Composition rule", "Behavior-changing proof", "Result surface", "Context policy", "Reuse hook", "NO EVENT"),
            failures,
        )
        require_terms(
            "mastery report",
            REQUIRED["mastery report"],
            ("Genius patterns decoded", "Hidden knowledge revealed", "Four-week mastery path", "First 24 hours", "First 30 days"),
            failures,
        )
        require_terms(
            "transcendence dossier",
            REQUIRED["transcendence dossier"],
            ("Hidden patterns", "Cross-domain applications", "Technology amplification", "Constraint removal", "Five pillars"),
            failures,
        )
        require_terms(
            "workflow",
            REQUIRED["workflow"],
            ("rank-ideas", "body first", "3-5 peers", "Never coordinate", "review", "840K target is never presented as guaranteed"),
            failures,
        )
        require_terms(
            "prompt",
            REQUIRED["prompt"],
            ("Input Required", "Execution Protocol", "Output Contract", "Output Skeleton", "Quality Gate", "Deploy When"),
            failures,
        )
        require_terms(
            "orchestrator",
            ROOT / ".agent/workflows/diandra-linkedin-system.md",
            ("GKbNTGLfd34", "Rule-of-100 Operating Loop", "execution/linkedin_growth_os.py"),
            failures,
        )
        require_terms(
            "skill menu",
            ROOT / "skills/diandra-escobar-linkedin-growth/SKILL.md",
            ("23-zero-to-840k-operating-system.md", "ben-meer-hubspot-growth-layer.md"),
            failures,
        )
        test = subprocess.run(
            [sys.executable, str(REQUIRED["runtime tests"])],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if test.returncode:
            failures.append(f"runtime tests failed: {test.stdout} {test.stderr}".strip())
    if failures:
        print("LinkedIn 840K growth OS: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("LinkedIn 840K growth OS: PASS")
    print("- source package, full guide, and hook deck present")
    print("- workflow, born-v2 prompt, source layer, and Diandra owner wired")
    print("- runtime and false-green controls passed")
    print("- guaranteed-outcome and coordinated-engagement safeguards present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

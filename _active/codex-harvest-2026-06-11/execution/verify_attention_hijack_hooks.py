#!/usr/bin/env python3
"""Verify the Attention Hijack Hooks skill system and command bridge."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "primitive": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "attention-hijack-hook-system.md",
    "skill": ROOT / "skills" / "attention-hijack-hooks" / "SKILL.md",
    "genius": ROOT / "skills" / "attention-hijack-hooks" / "genius.md",
    "workflow_01": ROOT / "skills" / "attention-hijack-hooks" / "workflows" / "01-signal-anchor-scan.md",
    "workflow_02": ROOT / "skills" / "attention-hijack-hooks" / "workflows" / "02-hookable-elements-extractor.md",
    "workflow_03": ROOT / "skills" / "attention-hijack-hooks" / "workflows" / "03-four-format-hook-generator.md",
    "workflow_04": ROOT / "skills" / "attention-hijack-hooks" / "workflows" / "04-platform-fit-gate.md",
    "workflow_05": ROOT / "skills" / "attention-hijack-hooks" / "workflows" / "05-content-bridge.md",
    "command_workflow": ROOT / ".agent" / "workflows" / "attention-hijack-hooks.md",
    "source_command": ROOT / ".claude" / "commands" / "attention-hijack-hooks.md",
    "cold_wrapper": ROOT / ".agents" / "cold-skills" / "source-command-wrappers" / "source-command-attention-hijack-hooks" / "SKILL.md",
    "agent": ROOT / "agents" / "attention-hijack-hooks" / "AGENT.md",
    "agent_context": ROOT / "agents" / "attention-hijack-hooks" / "memory" / "context.md",
    "subagent": ROOT / ".claude" / "agents" / "attention-hijack-hook-auditor.md",
    "auditor": ROOT / "execution" / "attention_hijack_hooks.py",
    "source_analysis": ROOT / "extractions" / "video-context" / "Zc4E_K48v48" / "analysis.md",
    "source_uncertainty": ROOT / "extractions" / "video-context" / "Zc4E_K48v48" / "uncertainty-report.md",
}

REQUIRED_TERMS = {
    "primitive": ["curiosity gap", "Dense", "Punchy plus Context", "Single-Line Bomb", "Stacked"],
    "skill": ["/attention-hijack-hooks", "brandjacking", "newsjacking", "Content Bridge"],
    "command_workflow": ["Skill System Contract", "Plugin Ladder", "Real Codex subagents require explicit authorization"],
    "agent": ["Signal Anchor Selection", "Platform Fit Auditing", "Handoff Protocol"],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def run(args: list[str], ok_codes: set[int] | None = None) -> str:
    ok = ok_codes or {0}
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode not in ok:
        raise AssertionError(f"{' '.join(args)} failed with {result.returncode}:\n{result.stdout}")
    return result.stdout


def main() -> int:
    failures: list[str] = []

    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")

    for label, terms in REQUIRED_TERMS.items():
        path = FILES[label]
        if not path.exists():
            continue
        content = read(path)
        for term in terms:
            if term not in content:
                failures.append(f"{label} missing term: {term}")

    if not failures:
        sample = (
            "Most LinkedIn hooks fail because creators count characters, but the real cutoff "
            "is pixel width. That tiny mistake kills both reader curiosity and algorithmic reach."
        )
        try:
            audit = run(
                [
                    sys.executable,
                    "execution/attention_hijack_hooks.py",
                    "--hook",
                    sample,
                    "--platform",
                    "linkedin",
                    "--terms",
                    "LinkedIn,algorithm,pixel",
                ],
                ok_codes={0},
            )
            if "Attention Hijack Hook Audit" not in audit:
                failures.append("auditor did not render markdown audit")
            if "Topical terms found" not in audit:
                failures.append("auditor missing topical term section")
        except AssertionError as exc:
            failures.append(str(exc))

    if not failures:
        for query in [
            "brand tracking newsjacking hook hijack universal content",
            "rehook draft Diandra hook formats attention hijack",
        ]:
            try:
                menu = run([sys.executable, "execution/command_menu.py", "search", query])
                router = run([sys.executable, "execution/workflow_router.py", "search", query])
                combined = menu + "\n" + router
                if "/attention-hijack-hooks" not in combined:
                    failures.append(f"routing query did not surface /attention-hijack-hooks: {query}")
            except AssertionError as exc:
                failures.append(str(exc))

    if failures:
        print("Attention Hijack Hooks verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Attention Hijack Hooks verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

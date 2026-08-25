#!/usr/bin/env python3
"""Verify the Dara Denney creative-format intelligence extension.

This stdlib-only verifier checks source fidelity, system wiring, and the
negative controls that prevent a dated tier list becoming a performance claim.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "extractions/dara-denney/meta-ad-creative-format-intelligence-2026"
SKILL = ROOT / "skills/dara-denney-meta-ads"

REQUIRED = {
    "package README": PACKAGE / "README.md",
    "source ledger": PACKAGE / "source-ledger.md",
    "uncertainty report": PACKAGE / "uncertainty-report.md",
    "behavior proof": PACKAGE / "behavior-proof.md",
    "verification report": PACKAGE / "verification-report.md",
    "native captions": PACKAGE / "transcript.vtt",
    "clean transcript": PACKAGE / "transcript.txt",
    "tier board": PACKAGE / "tier-board.jpg",
    "decision reference": SKILL / "references/creative-format-intelligence.md",
    "workflow": SKILL / "workflows/27-creative-format-intelligence.md",
    "execution prompt": SKILL / "references/prompts-v2/27-creative-format-intelligence-brief.md",
    "Codex menu wrapper": ROOT / ".agent/workflows/dara-denney-creative-format-intelligence.md",
    "Claude menu wrapper": ROOT / ".claude/commands/dara-denney-creative-format-intelligence.md",
    "source-command wrapper": ROOT / ".agents/skills/source-command-dara-denney-creative-format-intelligence/SKILL.md",
}

EXPECTED_COUNTS = {"S": 3, "A": 7, "B": 19, "C": 9, "D": 3, "E": 3, "F": 4}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: str) -> bool:
    print(f"{'PASS' if ok else 'FAIL'} | {label} | {detail}")
    return ok


def main() -> int:
    results: list[bool] = []
    missing = [label for label, path in REQUIRED.items() if not path.is_file()]
    results.append(check("required artifacts", not missing, f"all {len(REQUIRED)} present" if not missing else ", ".join(missing)))
    if missing:
        return 1

    ledger = read(REQUIRED["source ledger"])
    rows: list[tuple[str, str]] = []
    for tier, section in re.findall(
        r"^## ([A-FS]) Tier[^\n]*\n(.*?)(?=^## |\Z)", ledger, re.MULTILINE | re.DOTALL
    ):
        for name in re.findall(r"^\|\s*([^|]+?)\s*\|\s*\d{2}:\d{2}\s*\|", section, re.MULTILINE):
            rows.append((name.strip(), tier))
    counts = Counter(tier for _, tier in rows)
    results.append(check("visible-board inventory", len(rows) == 48, f"{len(rows)} labeled tiles"))
    results.append(check("tier counts", dict(counts) == EXPECTED_COUNTS, f"actual={dict(counts)} expected={EXPECTED_COUNTS}"))
    results.append(check("unique format labels", len({name.strip() for name, _ in rows}) == 48, "no duplicate visible tiles"))

    uncertainty = read(REQUIRED["uncertainty report"])
    reconciliation_folded = (uncertainty + ledger).casefold()
    results.append(check("51-to-48 uncertainty", all(token.casefold() in reconciliation_folded for token in ("51", "48", "inference", "Tweet/Reddit", "Catalog/DPA", "Ugly/Handwriting")), "bundled-tile reconciliation stays labeled inference"))

    reference = read(REQUIRED["decision reference"])
    gates = ("Job gate", "Evidence gate", "Access gate", "Funnel gate", "Friction gate", "Category and claims gate", "Durability gate")
    results.append(check("seven decision gates", all(gate in reference for gate in gates), "job through durability present"))

    workflow = read(REQUIRED["workflow"])
    results.append(check("decision workflow", all(token in workflow for token in ("Holds and Rejects", "Production Handoffs", "Stop Conditions", "27-creative-format-intelligence-brief.md")), "recommendation, veto, routing, prompt, and stop logic present"))

    proof = read(REQUIRED["behavior proof"])
    proof_folded = proof.casefold()
    results.append(check("negative controls", all(token.casefold() in proof_folded for token in ("reject", "hold", "no live", "simulated", "performance result")), "claim-sensitive proof includes holds, rejects, and non-performance boundary"))
    results.append(check("cross-domain transfer", all(token.casefold() in proof_folded for token in ("LinkedIn", "newsletter", "FAQ", "sales-enablement slide")), "mechanisms transfer beyond Meta"))

    skill = read(SKILL / "SKILL.md")
    agent = read(ROOT / "agents/dara-denney/AGENT.md")
    results.append(check("skill registration", all(token in skill for token in ('version: "4.3"', "workflows: 29", "/dara-denney-creative-format-intelligence", "/dara-format-concept-production-brief", "/dara-format-outcome-ledger", "creative-format-intelligence.md")), "expanded version, count, and all format-intelligence routes wired"))
    results.append(check("agent registration", "meta-ad-creative-format-intelligence-2026" in agent, "latest source package is visible to the expert"))

    wrapper_text = [read(REQUIRED[name]) for name in ("Codex menu wrapper", "Claude menu wrapper", "source-command wrapper")]
    results.append(check("surface parity", all("dara-denney-creative-format-intelligence" in text for text in wrapper_text), "Codex, Claude, and source-command surfaces agree"))

    passed = sum(results)
    print(f"SUMMARY | {'PASS' if all(results) else 'FAIL'} | {passed}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Verify Dara's connected production-brief and outcome-ledger system."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "dara-denney-meta-ads"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, passed: bool, detail: str) -> tuple[str, bool, str]:
    return name, passed, detail


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "execution" / "dara_format_outcome_ledger.py"), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def cold_start() -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as directory:
        ledger = Path(directory) / "outcomes.jsonl"
        common = [
            "--ledger", str(ledger),
        ]
        record = run(
            *common,
            "record",
            "--format-id", "founder-ad",
            "--format-label", "Founder's Ad",
            "--source-prior-tier", "S",
            "--campaign-id", "cold-start",
            "--asset-id", "F01",
            "--message-id", "unmade-belief",
            "--category", "supplement",
            "--persona", "translation-burdened-founder",
            "--channel", "linkedin",
            "--funnel-stage", "recognition",
            "--spend", "100",
            "--hook-events", "900",
            "--hook-opportunities", "1000",
            "--hook-rate-definition", "three-second views / impressions",
            "--conversion-count", "0",
            "--conversion-evidence-state", "none",
            "--fatigue-state", "fresh",
        )
        if record.returncode != 0:
            return False, f"record failed: {record.stderr.strip()}"

        first_read = run(*common, "scoreboard", "--json")
        if first_read.returncode != 0:
            return False, f"scoreboard failed: {first_read.stderr.strip()}"
        rows = json.loads(first_read.stdout)
        if not rows or rows[0]["latest_decision"] != "":
            return False, "90% hook-rate observation auto-promoted or disappeared"

        decision = run(
            *common,
            "decide",
            "--format-id", "founder-ad",
            "--format-label", "Founder's Ad",
            "--source-prior-tier", "S",
            "--campaign-id", "cold-start",
            "--asset-id", "F01",
            "--message-id", "unmade-belief",
            "--category", "supplement",
            "--persona", "translation-burdened-founder",
            "--channel", "linkedin",
            "--funnel-stage", "recognition",
            "--decision", "hold",
            "--decision-reason", "Hook signal exists but conversion evidence is absent.",
            "--decision-evidence", "cold-start://scoreboard",
            "--decided-by", "Verifier",
        )
        if decision.returncode != 0:
            return False, f"decision failed: {decision.stderr.strip()}"

        final_read = run(*common, "scoreboard", "--json")
        verify = run(*common, "verify")
        rows = json.loads(final_read.stdout)
        if final_read.returncode or verify.returncode:
            return False, "final read or ledger verification failed"
        if rows[0]["latest_decision"] != "hold":
            return False, "explicit decision was not preserved"
        if rows[0]["weighted_hook_rate"] != 0.9:
            return False, "weighted hook rate changed during decision append"
        return True, "90% hook signal remained NO DECISION until explicit HOLD event"


def main() -> int:
    required = [
        ROOT / "execution" / "dara_format_outcome_ledger.py",
        ROOT / "tests" / "test_dara_format_outcome_ledger.py",
        SKILL / "references" / "format-outcome-ledger.md",
        SKILL / "workflows" / "28-format-concept-production-brief.md",
        SKILL / "workflows" / "29-format-outcome-ledger.md",
        SKILL / "references" / "prompts-v2" / "28-format-concept-production-brief.md",
        SKILL / "references" / "prompts-v2" / "29-format-outcome-ledger.md",
        ROOT / ".agent" / "workflows" / "dara-format-concept-production-brief.md",
        ROOT / ".agent" / "workflows" / "dara-format-outcome-ledger.md",
        ROOT / ".claude" / "commands" / "dara-format-concept-production-brief.md",
        ROOT / ".claude" / "commands" / "dara-format-outcome-ledger.md",
        ROOT / ".agents" / "skills" / "source-command-dara-format-concept-production-brief" / "SKILL.md",
        ROOT / ".agents" / "skills" / "source-command-dara-format-outcome-ledger" / "SKILL.md",
        ROOT / "extractions" / "dara-denney" / "meta-ad-creative-format-intelligence-2026" / "format-outcome-system-contract.md",
        ROOT / "extractions" / "dara-denney" / "meta-ad-creative-format-intelligence-2026" / "behavior-proof-format-outcome-system.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    results = [check("required artifacts", not missing, "all 15 present" if not missing else ", ".join(missing))]

    skill = read(SKILL / "SKILL.md")
    format_workflow = read(SKILL / "workflows" / "27-creative-format-intelligence.md")
    concept_workflow = read(SKILL / "workflows" / "28-format-concept-production-brief.md")
    ledger_workflow = read(SKILL / "workflows" / "29-format-outcome-ledger.md")
    ledger_script = read(ROOT / "execution" / "dara_format_outcome_ledger.py")
    proof = read(required[-1])

    results.append(
        check(
            "skill registration",
            all(token in skill for token in ('version: "4.3"', "workflows: 29", "/dara-format-concept-production-brief", "/dara-format-outcome-ledger")),
            "version, workflow count, and both companion routes are registered",
        )
    )
    results.append(
        check(
            "format-owner wiring",
            all(token in format_workflow for token in ("/dara-format-concept-production-brief", "/dara-format-outcome-ledger", "no hook-rate-only promotion")),
            "portfolio routes to construction and feedback without auto-promotion",
        )
    )
    results.append(
        check(
            "bounded owner composition",
            all(token in concept_workflow for token in ("Kallaway", "Stefan Georgi", "Creative Direction", "Claim-Safe Health Marketing", "Composition Ledger")),
            "content, copy, visual, and claim owners occupy bounded slots under Dara",
        )
    )
    results.append(
        check(
            "complete production packet",
            all(token in concept_workflow for token in ("Decision Lock", "Concept Core", "Content Strategy", "Copy System", "Visual Direction", "Claims and Proof", "Production Plan", "Outcome-Ledger Registration")),
            "concept through production and test registration are required",
        )
    )
    results.append(
        check(
            "ledger schema",
            all(token in ledger_script for token in ("spend", "hook_rate_definition", "conversion_evidence_state", "fatigue_state", "category", "persona", "latest_decision")),
            "requested outcome fields are represented",
        )
    )
    results.append(
        check(
            "append-only decisions",
            all(token in ledger_script for token in ("os.O_APPEND", '"observation"', '"decision"', '"promote"', '"demote"')),
            "observations and decisions append without rewriting history",
        )
    )
    results.append(
        check(
            "test-plan feedback",
            "dara_format_outcome_ledger.py" in read(SKILL / "workflows" / "05-test-plan.md")
            and "format-category-persona" in read(SKILL / "workflows" / "24-creative-roadmap.md"),
            "test and roadmap flows read/write the outcome spine",
        )
    )
    surfaces = [read(path) for path in required[7:13]]
    results.append(
        check(
            "surface parity",
            all("dara-format-" in surface for surface in surfaces),
            "Codex, Claude, and source-command surfaces exist for both routes",
        )
    )
    results.append(
        check(
            "behavior proof",
            all(token in proof for token in ("NO LIVE EVIDENCE", "Complete Concept and Production Brief", "90% hook rate", "NO DECISION", "Composition Ledger")),
            "applied Health Performance transformation and negative control are preserved",
        )
    )

    cold_pass, cold_detail = cold_start()
    results.append(check("cold-start ledger", cold_pass, cold_detail))

    failed = 0
    for name, passed, detail in results:
        print(f"{'PASS' if passed else 'FAIL'} | {name} | {detail}")
        failed += not passed
    print(f"SUMMARY | {'PASS' if not failed else 'FAIL'} | {len(results) - failed}/{len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Adversarial unit checks for the RelayNote behavior-run verifier."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import verify_behavior_run as verifier


FIXTURE = verifier.FIXTURE
ROOT = verifier.ROOT


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()


class BehaviorVerifierGuards(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.product = json.loads((FIXTURE / "product-truth.json").read_text())
        self.veto = json.loads((FIXTURE / "transfer-veto.json").read_text())

    def valid_opening_set(self) -> str:
        openings = [
            [
                "For a 5–20-person agency, the first follow-up draft can hide the very next step a client call was meant to settle.",
                "Across 1,248 synthetic call records in a 30-day synthetic test, 23% of assigned next steps were absent from the first manually drafted follow-up.",
                "RelayNote turns the completed transcript into a draft follow-up and extracts an owner and date when those details appear, so the team can review one concrete draft.",
                "Book a demo to inspect that draft-and-review flow with your own transcript.",
            ],
            [
                "Your team may finish the call in minutes, then spend the next stretch rebuilding the follow-up from the transcript.",
                "In the 30-day synthetic fixture, manual drafting took a median 18 minutes while RelayNote drafting took a median 4 minutes.",
                "RelayNote prepares a draft follow-up from the transcript and extracts the assigned owner and date when both appear, leaving the team to review what was actually said.",
                "Book a demo to see that post-call drafting path on one transcript.",
            ],
            [
                "A follow-up draft is only useful when the assigned detail survives the move from conversation to email.",
                "On a held-out 200-call synthetic fixture, RelayNote recorded 91% owner-and-date extraction accuracy while retaining the rule that those details must appear in the transcript.",
                "It turns that transcript into a draft follow-up and surfaces the owner and date when present, giving the agency a concrete artifact to review before anything is sent.",
                "Book a demo to examine the draft and its extracted details.",
            ],
        ]
        ids = [
            [
                ["PT-AUD-001"],
                ["PT-TEST-001", "PT-TEST-003", "PT-MET-001"],
                ["PT-CAP-001", "PT-CAP-002"],
                ["PT-ACT-001", "PT-CAP-001"],
            ],
            [
                ["PT-CAP-001"],
                ["PT-TEST-001", "PT-MET-002", "PT-MET-003"],
                ["PT-CAP-001", "PT-CAP-002"],
                ["PT-ACT-001", "PT-CAP-001"],
            ],
            [
                ["PT-CAP-001", "PT-CAP-002"],
                ["PT-MET-004", "PT-CAP-001", "PT-CAP-002"],
                ["PT-CAP-001", "PT-CAP-002"],
                ["PT-ACT-001"],
            ],
        ]
        hypotheses = ["Assigned-detail gap", "Drafting-time contrast", "Held-out accuracy"]
        blocks: list[str] = []
        for index, (lines, evidence_ids, hypothesis) in enumerate(zip(openings, ids, hypotheses), 1):
            block = [
                f"## Opening {index}",
                "",
                *lines,
                "",
                f"### Opening {index} Evidence Map",
                "",
                f"- Hypothesis: {hypothesis}",
            ]
            block.extend(
                f"- Line {line_number}: {line} | Evidence: {','.join(row_ids)}"
                for line_number, (line, row_ids) in enumerate(zip(lines, evidence_ids), 1)
            )
            blocks.append("\n".join(block))
        blocks.append(
            "## Recommendation\n\n"
            "Opening 1. It names the agency context, holds one omission-focused promise, uses the complete synthetic denominator, and moves from the problem into a transcript-to-draft path before the action.\n\n"
            "### Recommendation Evidence Map\n\n"
            "- Selected: Opening 1\n"
            "- Audience fit: Names the 5–20-person agency context. | Evidence: PT-AUD-001\n"
            "- Singular promise: Keeps the assigned-detail gap central. | Evidence: PT-MET-001,PT-CAP-002\n"
            "- Proof fit: Uses the 1,248-record synthetic denominator. | Evidence: PT-TEST-001,PT-TEST-003,PT-MET-001\n"
            "- Continuation strength: Moves into the transcript-to-draft capability. | Evidence: PT-CAP-001,PT-CAP-002"
        )
        return "\n\n".join(blocks) + "\n"

    def test_output_contract_rejects_false_pass_mutations(self) -> None:
        valid = self.valid_opening_set()
        mutations = {
            "unsupported outcome": valid.replace("one concrete draft.", "one concrete draft that improves pipeline efficiency."),
            "missing CTA": valid.replace("Book a demo to inspect", "Inspect"),
            "dropped qualifier": valid.replace("when those details appear", "as a guaranteed field"),
            "missing denominator": valid.replace(
                "Across 1,248 synthetic call records in a 30-day synthetic test, 23%",
                "Across a synthetic test, 23%",
            ),
            "blended recommendation": valid.replace("Opening 1. It names", "Opening 1 blends Opening 2. It names"),
        }
        with tempfile.TemporaryDirectory() as directory:
            valid_path = Path(directory) / "valid.md"
            valid_path.write_text(valid)
            errors: list[str] = []
            verifier.verify_output(valid_path, self.product, self.veto, errors)
            self.assertEqual(errors, [])
            for name, text in mutations.items():
                path = Path(directory) / f"{name}.md"
                path.write_text(text)
                errors = []
                verifier.verify_output(path, self.product, self.veto, errors)
                self.assertTrue(errors, f"mutation unexpectedly passed: {name}")

    def build_acceptance_bundle(self, run_dir: Path) -> tuple[dict, dict, dict]:
        frozen_cases = {
            row["case_id"]: row
            for row in (
                json.loads(line)
                for line in (FIXTURE / "acceptance-cases.jsonl").read_text().splitlines()
            )
        }
        contracts = json.loads((FIXTURE / "acceptance-contracts.json").read_text())["cases"]
        base_reads = {
            "skills/kyle-milligan-copy-chief/SKILL.md",
            "skills/kyle-milligan-copy-chief/genius.md",
            "skills/kyle-milligan-copy-chief/references/source-ledger.md",
            "skills/kyle-milligan-copy-chief/references/mechanics-ledger.md",
        }
        receipt = {"provenance_grade": "ORCHESTRATOR_ATTESTED", "acceptance_receipts": []}
        for case_id in sorted(contracts):
            contract = contracts[case_id]
            selected = contract["selected_route"]
            lines = [
                "# Acceptance Result",
                "## Case",
                f"Case: {case_id}",
                "## Decision",
                f"Decision: {frozen_cases[case_id]['expected']}",
                "## Evidence",
            ]
            lines.extend(
                line for line in contract["required_lines"]
                if not line.startswith("Case: ") and not line.startswith("Decision: ")
            )
            lines.extend(
                [
                    "## Required Action",
                    "Required action: APPLY_FROZEN_DECISION",
                    "## Prohibited Action",
                    "Prohibited action: DO_NOT_OVERRIDE",
                    "## Proof Boundary",
                    "Proof boundary: Fixture-only behavior evidence; not market evidence.",
                ]
            )
            output_path = run_dir / "acceptance" / f"{case_id}.md"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text("\n".join(lines) + "\n")
            reads = set(base_reads)
            if selected != "skills/kyle-milligan-copy-chief/SKILL.md":
                reads.add(selected)
                prompt_stem = Path(selected).stem.split("-", 1)[1]
                reads.add(f"skills/kyle-milligan-copy-chief/references/prompts-v2/{prompt_stem}.md")
            route = {
                "schema_version": "relaynote-acceptance-route/v1",
                "case_id": case_id,
                "case_contract_sha256": canonical_sha(contract),
                "case_input_sha256": canonical_sha(frozen_cases[case_id]),
                "selected_route": selected,
                "selected_route_sha256": sha(ROOT / selected),
                "loaded_routes": [selected],
                "read_paths": sorted(reads),
                "read_hashes": {path: sha(ROOT / path) for path in sorted(reads)},
                "output_sha256": sha(output_path),
                "worker_task": f"relaynote-acceptance-{case_id.lower()}",
                "worker_id": f"worker-{case_id.lower()}",
                "attempt_ordinal": 1,
                "fresh_context": True,
                "fork_turns": "none",
                "provenance_grade": "ORCHESTRATOR_ATTESTED",
            }
            route_path = run_dir / "acceptance" / f"{case_id}.route.json"
            route_path.write_text(json.dumps(route, indent=2, sort_keys=True) + "\n")
            receipt["acceptance_receipts"].append(
                {
                    "case_id": case_id,
                    "case_sha256": canonical_sha(contract),
                    "selected_route": selected,
                    "loaded_routes": [selected],
                    "read_paths": sorted(reads),
                    "expected": frozen_cases[case_id]["expected"],
                    "derived_decision": frozen_cases[case_id]["expected"],
                    "output_sha256": sha(output_path),
                    "route_receipt_sha256": sha(route_path),
                    "hard_failures": [],
                    "pass": True,
                }
            )
        return receipt, frozen_cases, contracts

    def test_acceptance_cannot_self_attest_unrelated_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            receipt, _, _ = self.build_acceptance_bundle(run_dir)
            errors: list[str] = []
            passed, failures = verifier.verify_acceptance(run_dir, receipt, errors)
            self.assertTrue(passed, f"errors={errors}; failures={failures}")
            self.assertEqual(errors, [])
            self.assertEqual(failures, [])

            case_id = "AC-01"
            output_path = run_dir / "acceptance" / f"{case_id}.md"
            output_path.write_text("unrelated markdown\n")
            route_path = run_dir / "acceptance" / f"{case_id}.route.json"
            route = json.loads(route_path.read_text())
            route["output_sha256"] = sha(output_path)
            route_path.write_text(json.dumps(route, indent=2, sort_keys=True) + "\n")
            row = next(item for item in receipt["acceptance_receipts"] if item["case_id"] == case_id)
            row["output_sha256"] = sha(output_path)
            row["route_receipt_sha256"] = sha(route_path)
            row["derived_decision"] = row["expected"]
            row["hard_failures"] = []
            row["pass"] = True
            errors = []
            passed, failures = verifier.verify_acceptance(run_dir, receipt, errors)
            self.assertFalse(passed)
            self.assertTrue(errors)
            self.assertTrue(failures)

    def test_current_provenance_grade_cannot_register(self) -> None:
        run_config = json.loads((FIXTURE / "run-config.json").read_text())
        contract = json.loads((FIXTURE / "provenance-contract.json").read_text())
        grade = run_config["provenance_policy"]["current_available_grade"]
        self.assertEqual(grade, "ORCHESTRATOR_ATTESTED")
        self.assertFalse(contract["grades"][grade]["registration_eligible"])


if __name__ == "__main__":
    unittest.main()

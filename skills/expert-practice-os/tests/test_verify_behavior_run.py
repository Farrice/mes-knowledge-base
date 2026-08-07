#!/usr/bin/env python3
"""Unit and adversarial tests for Expert Practice OS behavior verification."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from verify_behavior_run import load_json, verify


HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"


def fixture(name: str) -> tuple[dict, dict, dict]:
    base = FIXTURES / name
    return (
        load_json(base / "practitioner-protocol-packet.json"),
        load_json(base / "expected-route.json"),
        load_json(base / "acceptance-contract.json"),
    )


def parent_and_key(value: dict, dotted: str):
    parts = dotted.split(".")
    current = value
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    key = int(parts[-1]) if isinstance(current, list) else parts[-1]
    return current, key


def mutate(value: dict, case: dict) -> None:
    parent, key = parent_and_key(value, case["path"])
    op = case["op"]
    if op == "delete":
        del parent[key]
    elif op == "set":
        parent[key] = case["value"]
    elif op == "append":
        parent[key].append(case["value"])
    else:
        raise AssertionError(f"unsupported mutation op: {op}")


class BehaviorVerifierTests(unittest.TestCase):
    def test_final10_positive_hold(self):
        packet, actual, acceptance = fixture("final-10-ai-consulting")
        receipt = verify(packet, actual, acceptance)
        self.assertEqual("PASS", receipt["verifier_status"])
        self.assertEqual("STOP_OR_HOLD", receipt["terminal_decision_observed"])
        self.assertFalse(receipt["registration_eligible"])
        self.assertFalse(receipt["economics_eligible"])
        self.assertEqual([], receipt["errors"])

    def test_life_design_positive_advance_without_scale(self):
        packet, actual, acceptance = fixture("life-design-coach-pop")
        receipt = verify(packet, actual, acceptance)
        self.assertEqual("PASS", receipt["verifier_status"])
        self.assertEqual("ADVANCE_TO_REPEATABILITY", receipt["terminal_decision_observed"])
        self.assertEqual("STAGE_0_PAID_PROOF", actual["proof_stage"])
        self.assertEqual("STAGE_1_REPEATABLE_PRACTICE", actual["next_stage"])
        self.assertFalse(receipt["registration_eligible"])
        self.assertFalse(receipt["economics_eligible"])

    def test_all_adversarial_mutations_fail_for_named_reason(self):
        cases = [json.loads(line) for line in (FIXTURES / "acceptance-cases.jsonl").read_text().splitlines() if line.strip()]
        self.assertEqual(21, len(cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                packet, actual, acceptance = fixture(case["base_fixture"])
                packet = copy.deepcopy(packet)
                actual = copy.deepcopy(actual)
                mutate(packet if case["target"] == "packet" else actual, case)
                receipt = verify(packet, actual, acceptance)
                self.assertEqual("FAIL", receipt["verifier_status"])
                self.assertTrue(receipt["errors"])
                self.assertEqual(case["expected_error"], receipt["errors"][0], receipt["errors"])

    def test_receipts_are_hash_bound(self):
        packet, actual, acceptance = fixture("final-10-ai-consulting")
        receipt = verify(packet, actual, acceptance)
        for key in ("input_sha256", "actual_sha256", "acceptance_sha256"):
            self.assertRegex(receipt[key], r"^[0-9a-f]{64}$")


if __name__ == "__main__":
    unittest.main(verbosity=2)

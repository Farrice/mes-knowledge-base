import copy
import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "verify_mastery_transfer_proof_spine.py"
SPEC = importlib.util.spec_from_file_location("mastery_transfer_proof", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def base_manifest():
    states = {
        state: {"status": "UNTESTED", "evidence": []}
        for state in MODULE.PROOF_STATES
    }
    for state in ("CAPTURED", "GROUNDED", "RUNNABLE", "TRANSFERRED"):
        states[state] = {"status": "PASS", "evidence": ["proof.md"]}
    return {
        "schema_version": "mastery-transfer-proof/v1",
        "capability": "fixture-capability",
        "current_state": "TRANSFERRED",
        "claim_boundary": "Development behavior only; no field or superiority claim.",
        "next_gate": "Seal held-out near, far, and negative-control cases.",
        "governance": {
            "mode": "SHADOW",
            "promotion_eligible": False,
            "automatic_enforcement": False,
        },
        "proof_states": states,
        "field_events": {"state": "NO_EVENT", "real_uses": 0, "observed_outcomes": 0},
        "comparison": {},
    }


class MasteryTransferProofTests(unittest.TestCase):
    def validate(self, manifest):
        return MODULE.validate_manifest(manifest, check_paths=False)

    def test_valid_transferred_manifest_passes(self):
        self.assertEqual(self.validate(base_manifest()), [])

    def test_later_pass_cannot_skip_unearned_state(self):
        manifest = base_manifest()
        manifest["proof_states"]["BLIND_PREFERRED"] = {
            "status": "PASS",
            "evidence": ["blind.md"],
            "evaluation": {
                "independent": True,
                "blind": True,
                "precommitted_mapping": True,
                "preservation_pass": True,
                "verdict": "TREATMENT_WIN",
                "builder": "builder",
                "evaluator": "judge",
            },
        }
        manifest["current_state"] = "BLIND_PREFERRED"
        errors = self.validate(manifest)
        self.assertTrue(any("cannot PASS after an earlier unearned state" in e for e in errors))

    def test_generalized_requires_three_sealed_held_out_tests(self):
        manifest = base_manifest()
        manifest["proof_states"]["GENERALIZED"] = {
            "status": "PASS",
            "evidence": ["generalization.md"],
            "tests": {
                "near_transfer": {"status": "PASS", "held_out": True},
                "far_transfer": {"status": "PASS", "held_out": False},
                "negative_control": {"status": "PASS", "held_out": True},
            },
        }
        manifest["current_state"] = "GENERALIZED"
        errors = self.validate(manifest)
        self.assertTrue(any("far_transfer" in e for e in errors))

    def test_builder_cannot_self_grade_blind_preference(self):
        manifest = base_manifest()
        manifest["proof_states"]["GENERALIZED"] = {
            "status": "PASS",
            "evidence": ["generalization.md"],
            "tests": {
                name: {"status": "PASS", "held_out": True}
                for name in ("near_transfer", "far_transfer", "negative_control")
            },
        }
        manifest["proof_states"]["BLIND_PREFERRED"] = {
            "status": "PASS",
            "evidence": ["blind.md"],
            "evaluation": {
                "independent": True,
                "blind": True,
                "precommitted_mapping": True,
                "preservation_pass": True,
                "verdict": "MATERIAL_TREATMENT_WIN",
                "builder": "same-agent",
                "evaluator": "same-agent",
            },
        }
        manifest["current_state"] = "BLIND_PREFERRED"
        errors = self.validate(manifest)
        self.assertIn("builder cannot be the blind evaluator", errors)

    def test_no_event_cannot_be_field_validated(self):
        manifest = base_manifest()
        for state in ("GENERALIZED", "BLIND_PREFERRED"):
            manifest["proof_states"][state] = {"status": "PASS", "evidence": ["proof.md"]}
        manifest["proof_states"]["GENERALIZED"]["tests"] = {
            name: {"status": "PASS", "held_out": True}
            for name in ("near_transfer", "far_transfer", "negative_control")
        }
        manifest["proof_states"]["BLIND_PREFERRED"]["evaluation"] = {
            "independent": True,
            "blind": True,
            "precommitted_mapping": True,
            "preservation_pass": True,
            "verdict": "TREATMENT_WIN",
            "builder": "builder",
            "evaluator": "judge",
        }
        manifest["proof_states"]["FIELD_VALIDATED"] = {
            "status": "PASS",
            "evidence": ["field.md"],
        }
        manifest["current_state"] = "FIELD_VALIDATED"
        errors = self.validate(manifest)
        self.assertTrue(any("real use" in e for e in errors))
        self.assertTrue(any("NO_EVENT" in e for e in errors))


if __name__ == "__main__":
    unittest.main()

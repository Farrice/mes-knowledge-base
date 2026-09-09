"""Negative controls distinguish usable inputs from proof of better work."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))
from expert_production import (build_production_plan, revision_handoff,
                               check_integration, adoption_verdict, ROLES, CASES)


class ProductionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.packet = {"id": "test", "client": "jen", "objective": "New B-roll caption",
                       "output": "Complete overlay and caption", "preserve": "Approved register",
                       "constraints": ["No fictional client anecdotes"], "context": []}
        for kind in ("skill", "workflow", "execution_prompt", "source", "approved_example", "correction"):
            p = self.base / (kind + ".md")
            p.write_text("start\n" + "method details\n" * 600 + "CRUCIAL-END-DETAIL\n")
            self.packet["context"].append({"kind": kind, "path": p.name,
                "client": "shared" if kind in ("skill", "workflow", "execution_prompt") else "jen",
                "relevance": "Relevant selected method or Jen evidence"})

    def build(self):
        return build_production_plan(self.packet, self.base)

    def test_full_method_survives_prefix_limit(self):
        result = self.build()
        self.assertEqual(result["status"], "READY_FOR_DISPATCH")
        for member in result["members"]:
            self.assertIn("CRUCIAL-END-DETAIL", member["brief"])
            self.assertIn("collaboration.send_message", member["brief"])
        self.assertFalse(result["real_subagents_spawned"])

    def test_missing_execution_prompt_blocks_dispatch_not_fakes_fallback(self):
        (self.base / "execution_prompt.md").unlink()
        result = self.build()
        self.assertEqual(result["status"], "INPUT_GAP")
        self.assertEqual(result["members"], [])

    def test_irrelevant_client_scope_rejected(self):
        self.packet["context"][3]["client"] = "andrea"
        self.assertEqual(self.build()["status"], "INPUT_GAP")

    def test_undeclared_relevance_rejected(self):
        self.packet["context"][1]["relevance"] = ""
        self.assertEqual(self.build()["status"], "INPUT_GAP")

    def test_rejected_example_cannot_be_positive(self):
        self.packet["excluded_examples"] = ["approved_example.md"]
        self.assertEqual(self.build()["status"], "INPUT_GAP")

    def test_excluded_file_content_not_loaded(self):
        (self.base / "bad.md").write_text("REJECTED-PROSE-DO-NOT-IMITATE")
        self.packet["excluded_examples"] = ["bad.md"]
        self.assertNotIn("REJECTED-PROSE-DO-NOT-IMITATE", self.build()["common_brief"])

    def test_precise_selection_with_hash_receipt(self):
        self.packet["context"][0].update(start_line=602, end_line=602)
        result = self.build()
        receipt = result["context_receipts"][0]
        self.assertEqual(receipt["start_line"], 602)
        self.assertEqual(len(receipt["sha256"]), 64)

    def test_bad_line_range_rejected(self):
        self.packet["context"][0].update(start_line=90000)
        self.assertEqual(self.build()["status"], "INPUT_GAP")

    def test_claude_mapping_stays_separate(self):
        result = build_production_plan(self.packet, self.base, "claude")
        self.assertIn("native SendMessage", result["members"][0]["brief"])
        self.assertNotIn("collaboration.send_message", result["members"][0]["brief"])

    def test_real_cli_packet_and_missing_input_exit(self):
        path = self.base / "packet.json"
        path.write_text(json.dumps(self.packet))
        cmd = [sys.executable, str(ROOT / "execution/persona_team.py"), "production", "--packet", str(path)]
        out = subprocess.run(cmd, text=True, capture_output=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(json.loads(out.stdout)["status"], "READY_FOR_DISPATCH")
        (self.base / "source.md").unlink()
        out = subprocess.run(cmd, text=True, capture_output=True)
        self.assertEqual(out.returncode, 1)

    def test_legacy_cast_alias_unchanged(self):
        cmd = [sys.executable, str(ROOT / "execution/persona_team.py")]
        bare = subprocess.run(cmd + ["content decision"], capture_output=True, text=True)
        cast = subprocess.run(cmd + ["cast", "content decision"], capture_output=True, text=True)
        self.assertEqual(bare.returncode, 0, bare.stderr)
        self.assertEqual(bare.stdout, cast.stdout)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.contributions = [{"id": r+"-1", "role": r, "status": "complete",
            "body": "Complete original "+r, "revised_artifact": "VALUABLE-REVISION-"+r} for r in ROLES]
        self.final = {"final_artifact": "Actual final content", "decisions": {
            c["id"]: {"action": "accept", "reason": "Grounded specificity", "affected_passage": "line one"}
            for c in self.contributions}}

    def test_revised_work_preserved_without_lossy_summary(self):
        result = revision_handoff(self.contributions)
        self.assertEqual(result["contributions"], self.contributions)
        self.assertIn("VALUABLE-REVISION-craft_owner", json.dumps(result))

    def test_failed_specialist_is_incomplete(self):
        self.contributions[0]["status"] = "failed"
        self.assertEqual(revision_handoff(self.contributions)["status"], "INCOMPLETE")

    def test_summary_substituted_for_original_is_detected(self):
        originals = {c["id"]: c["body"] for c in self.contributions}
        self.contributions[0]["body"] = "Short plausible summary"
        result = revision_handoff(self.contributions, originals)
        self.assertEqual(result["status"], "INCOMPLETE")
        self.assertIn("original message mismatch", " ".join(result["errors"]))

    def test_no_original_receipt_does_not_claim_verbatim_fidelity(self):
        self.assertEqual(revision_handoff(self.contributions)["original_message_check"], "UNVERIFIED")

    def test_missing_specialist_is_incomplete(self):
        self.assertEqual(revision_handoff(self.contributions[:2])["status"], "INCOMPLETE")

    def test_unaddressed_contribution_rejected(self):
        self.final["decisions"].pop("source_strategist-1")
        self.assertEqual(check_integration(revision_handoff(self.contributions), self.final)["status"], "INCOMPLETE")

    def test_coverage_never_means_quality_pass(self):
        result = check_integration(revision_handoff(self.contributions), self.final)
        self.assertEqual(result["status"], "COVERAGE_VERIFIED")
        self.assertEqual(result["quality"], "HUMAN_REVIEW_REQUIRED")


class AdoptionTests(unittest.TestCase):
    def record(self):
        return {"repair_attempts": 0, "cases": [{"id": cid,
            "matched_inputs_verified": True, "no_regression": True, "approved_standard_met": True,
            "human_review": {"reviewer": "Farrice", "preferred": "swarm", "evidence": "fixture-human-verdict"},
            "effort": {"solo_minutes": 10, "swarm_minutes": 4,
                "basis": "observed_active_human_work", "evidence": "fixture-active-timer"},
            "feedback_application": {"verified": True, "evidence": "fixture-before-after"}}
            for cid in CASES]}

    def test_empty_record_cannot_pass(self):
        self.assertEqual(adoption_verdict({})["verdict"], "UNPROVEN")

    def test_all_three_human_outcomes_required(self):
        record = self.record(); record["cases"].pop()
        self.assertEqual(adoption_verdict(record)["verdict"], "UNPROVEN")

    def test_fixture_complete_record_can_adopt_only_for_jen(self):
        result = adoption_verdict(self.record())
        self.assertEqual(result["verdict"], "ADOPT_FOR_JEN_COMPARABLE_WORK")
        self.assertFalse(result["global_rollout"])

    def test_model_self_score_not_human_review(self):
        record = self.record(); record["cases"][0]["human_review"]["reviewer"] = "editor"
        self.assertEqual(adoption_verdict(record)["verdict"], "UNPROVEN")

    def test_tie_is_not_adoption(self):
        record = self.record(); record["cases"][0]["human_review"]["preferred"] = "tie"
        self.assertEqual(adoption_verdict(record)["verdict"], "REVISE")

    def test_chat_elapsed_time_is_not_effort(self):
        record = self.record(); record["cases"][0]["effort"]["basis"] = "chat_elapsed"
        self.assertEqual(adoption_verdict(record)["verdict"], "UNPROVEN")

    def test_equal_effort_fails_even_with_quality_win(self):
        record = self.record(); record["cases"][0]["effort"]["swarm_minutes"] = 10
        self.assertEqual(adoption_verdict(record)["verdict"], "REVISE")

    def test_nonfinite_or_boolean_time_is_not_measurement(self):
        for value in (float("nan"), float("inf"), True, -1, None):
            with self.subTest(value=value):
                record = self.record(); record["cases"][0]["effort"]["solo_minutes"] = value
                self.assertEqual(adoption_verdict(record)["verdict"], "UNPROVEN")

    def test_feedback_saved_without_application_is_not_learning(self):
        record = self.record(); record["cases"][1]["feedback_application"] = {"saved": True}
        self.assertEqual(adoption_verdict(record)["verdict"], "UNPROVEN")

    def test_second_failed_attempt_retains_current_method(self):
        record = self.record(); record["repair_attempts"] = 1
        record["cases"][0]["no_regression"] = False
        self.assertEqual(adoption_verdict(record)["verdict"], "RETAIN_CURRENT_METHOD")


if __name__ == "__main__":
    unittest.main()

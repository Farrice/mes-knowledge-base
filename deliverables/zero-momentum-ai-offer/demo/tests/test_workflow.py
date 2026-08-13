import json
import unittest
from pathlib import Path

from lead_to_proposal import LeadToProposalWorkflow, run_fixture


ROOT = Path(__file__).resolve().parent.parent


class WorkflowTests(unittest.TestCase):
    def test_full_fixture_and_negative_controls(self):
        out = ROOT / "test-receipt.tmp.json"
        try:
            receipt = run_fixture(ROOT / "fixtures" / "cases.json", out)
            self.assertEqual(receipt["failed"], 0)
            self.assertTrue(receipt["all_human_holds_worked"])
            self.assertEqual(receipt["cases"], 19)
        finally:
            out.unlink(missing_ok=True)

    def test_send_is_never_permitted(self):
        lead = {"lead_id":"T1","company":"Test","contact":"Human","email":"h@example.test","service":"Audit","budget":"$1,500","timeline":"Five days","send_requested":True}
        result = LeadToProposalWorkflow().run(lead)
        self.assertFalse(result.external_send_permitted)
        self.assertEqual(result.approval_status, "HOLD_FOR_HUMAN")

    def test_duplicate_is_held(self):
        workflow = LeadToProposalWorkflow()
        lead = {"lead_id":"T2","company":"Test","contact":"Human","email":"h@example.test","service":"Audit","budget":"$1,500","timeline":"Five days"}
        workflow.run(lead)
        result = workflow.run(lead)
        self.assertIn("DUPLICATE_INQUIRY", result.flags)
        self.assertEqual(result.status, "HELD")


if __name__ == "__main__":
    unittest.main()

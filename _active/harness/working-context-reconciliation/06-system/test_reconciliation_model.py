"""Protocol tests, not autonomous semantic or creative-quality proof."""
import copy
import unittest
from reconciliation_model import Conflict, initial, receive, reconcile, packet, validate_handoff, inspect_legacy

OWNER = "jen-fixture-only"
PURPOSE = "one-carousel"


def event(key, text):
    return {"id": key, "text": text, "source": "jen-replay:user-turn:" + key}


def decision(key, quote):
    return {"event": key, "quote": quote}


def item(key, slot, status, turn, quote, excerpt=None):
    out = {"id": key, "slot": slot, "status": status, "path": key + ".md", "sha256": key + "-hash",
           "decision": decision(turn, quote)}
    if excerpt:
        out["approved_excerpt"] = excerpt
    return out


def hashes(state):
    return {i["path"]: i["sha256"] for i in state["items"].values()}


def apply(state, items, resolutions, next_action=None, overrides=None, **kwargs):
    return reconcile(state, {"items": items, "resolutions": resolutions, "next_action": next_action,
                             "overrides": overrides or {}}, owner=kwargs.get("owner", OWNER),
                     purpose=kwargs.get("purpose", PURPOSE), expected_revision=kwargs.get("revision", state["revision"]))


def disposition(key, quote, effect="Keep partial approval distinct from full approval."):
    return {**decision(key, quote), "effect": effect}


def baseline():
    s = receive(initial(OWNER, PURPOSE, "One conversation about committing without knowing future listings."),
                event("opening", "The question and it might are good, so let's lock that in."))
    approved = item("opening", "opening", "approved", "opening", "let's lock that in",
                    "what if a better house comes along? / it might.")
    return apply(s, [approved], [disposition("opening", "let's lock that in")])


class ReconciliationTests(unittest.TestCase):
    def test_non_content_refinements_preserve_their_objectives(self):
        cases = [
            ("code", "Ship reliable account recovery", "Change the error message."),
            ("strategy", "Sell a paid diagnostic to one qualified buyer", "Make the explanation simpler."),
            ("research", "Determine why enrollment declined", "This source contradicts our earlier finding."),
            ("planning", "Complete the move before Friday", "Make the plan shorter."),
            ("thinking", "Work out what career choice fits my priorities", "That is not quite what I meant."),
        ]
        for purpose, goal, feedback in cases:
            with self.subTest(purpose=purpose):
                s = receive(initial(OWNER, purpose, goal), event("clarify", feedback))
                out = reconcile(s, {"items": [], "resolutions": [disposition("clarify", feedback, "Refine the working understanding within the original objective.")]},
                                owner=OWNER, purpose=purpose, expected_revision=s["revision"])
                self.assertEqual(out["goal"], goal)
                self.assertEqual(packet(out, {})["status"], "CURRENT")
                self.assertEqual(packet(out, {})["active"], [])

    def test_local_feedback_does_not_mutate_another_task(self):
        first = initial("task-a", "one-metaphor", "Explain the tradeoff")
        other = initial("task-b", "other-metaphor", "Explain a different tradeoff")
        before = copy.deepcopy(other)
        receive(first, event("reject", "That metaphor does not work here."))
        self.assertEqual(other, before)

    def test_latest_refinement_does_not_replace_whole_intent(self):
        s = receive(baseline(), event("shorten", "Make it shorter."))
        out = apply(s, list(s["items"].values()), [disposition("shorten", "Make it shorter", "Compress treatment; keep purpose, opening and payoff.")])
        self.assertEqual(out["goal"], s["goal"])
        self.assertEqual(out["items"]["opening"], s["items"]["opening"])
        with self.assertRaises(Conflict):
            reconcile(s, {"goal": "Minimize word count", "items": list(s["items"].values()),
                          "resolutions": [disposition("shorten", "Make it shorter")]},
                      owner=OWNER, purpose=PURPOSE, expected_revision=s["revision"])

    def test_explicit_objective_change_remains_possible(self):
        s = receive(baseline(), event("replace", "Stop the carousel. Make a buyer checklist instead."))
        out = reconcile(s, {"goal": "A buyer checklist", "items": list(s["items"].values()),
                             "resolutions": [disposition("replace", "Make a buyer checklist instead")],
                             "goal_change": {**decision("replace", "Stop the carousel"), "kind": "explicit-objective-change"}},
                        owner=OWNER, purpose=PURPOSE, expected_revision=s["revision"])
        self.assertEqual(out["goal"], "A buyer checklist")

    def test_receipt_does_not_infer_approval(self):
        s = receive(baseline(), event("v08", "This is better and more cohesive, but it is too much text."))
        self.assertEqual(len(s["items"]), 1)
        self.assertEqual(packet(s, hashes(s))["status"], "NEEDS_RECONCILIATION")

    def test_partial_approval_is_not_whole_draft_approval(self):
        s = receive(baseline(), event("v08", "This is better and more cohesive, but it is too much text."))
        v08 = item("v08", "middle", "candidate", "v08", "better and more cohesive")
        s = apply(s, [*s["items"].values(), v08], [disposition("v08", "too much text")])
        self.assertEqual(s["items"]["v08"]["status"], "candidate")

    def test_rejected_middle_never_enters_writer_packet(self):
        s = receive(baseline(), event("reject", "The middle changes the subject. Keep the opening."))
        bad = item("v07", "middle", "rejected", "reject", "middle changes the subject")
        bad["body"] = "What are you hoping the next house would change?"
        s = apply(s, [*s["items"].values(), bad], [disposition("reject", "Keep the opening")])
        p = packet(s, hashes(s))
        self.assertNotIn("What are you hoping", str(p))
        self.assertEqual([i["id"] for i in p["active"]], ["opening"])

    def test_rejection_invalidates_pending_next_action(self):
        s = receive(baseline(), event("candidate", "Try this candidate."))
        candidate = item("v09", "middle", "candidate", "candidate", "Try this candidate")
        s = apply(s, [*s["items"].values(), candidate], [disposition("candidate", "Try this candidate")],
                  {"text": "Review v09", "targets": ["v09"]})
        s = receive(s, event("reject", "The copy still doesn't work."))
        self.assertIsNone(packet(s, hashes(s))["next_action"])

    def test_old_next_action_cannot_survive_retirement(self):
        s = receive(baseline(), event("reject", "Reject v03."))
        bad = item("v03", "middle", "rejected", "reject", "Reject v03")
        with self.assertRaises(Conflict):
            apply(s, [*s["items"].values(), bad], [disposition("reject", "Reject v03")],
                  {"text": "Apply v03", "targets": ["v03"]})

    def test_two_current_candidates_in_same_slot_fail(self):
        s = receive(baseline(), event("try", "Try a revision."))
        items = [*s["items"].values(), item("v08", "middle", "candidate", "try", "Try a revision"),
                 item("v09", "middle", "candidate", "try", "Try a revision")]
        with self.assertRaises(Conflict):
            apply(s, items, [disposition("try", "Try a revision")])

    def test_protected_opening_cannot_be_silently_changed(self):
        s = receive(baseline(), event("middle", "Change the middle."))
        changed = copy.deepcopy(s["items"]["opening"])
        changed["approved_excerpt"] = "Replacement hook"
        with self.assertRaises(Conflict):
            apply(s, [changed], [disposition("middle", "Change the middle")])

    def test_user_can_change_previously_approved_component(self):
        s = receive(baseline(), event("change", "Replace the opening too."))
        changed = copy.deepcopy(s["items"]["opening"])
        changed.update(status="superseded", decision=decision("change", "Replace the opening too"))
        out = apply(s, [changed], [disposition("change", "Replace the opening too")],
                    overrides={"opening": decision("change", "Replace the opening too")})
        self.assertEqual(out["items"]["opening"]["status"], "superseded")

    def test_pending_turn_cannot_be_skipped(self):
        s = receive(baseline(), event("a", "Keep the metaphor."))
        s = receive(s, event("b", "Change the payoff."))
        with self.assertRaises(Conflict):
            apply(s, list(s["items"].values()), [disposition("b", "Change the payoff")])

    def test_no_change_disposition_supported(self):
        s = receive(baseline(), event("status", "What is the status?"))
        out = apply(s, list(s["items"].values()), [disposition("status", "What is the status", "Status question; no creative change.")])
        self.assertEqual(packet(out, hashes(out))["status"], "CURRENT")

    def test_stale_concurrent_revision_fails(self):
        s = baseline()
        revision = s["revision"]
        s = receive(s, event("new", "Keep the opening."))
        with self.assertRaises(Conflict):
            apply(s, list(s["items"].values()), [disposition("new", "Keep the opening")], revision=revision)

    def test_wrong_task_and_wrong_artifact_fail(self):
        s = baseline()
        for kwargs in ({"owner": "other-session"}, {"purpose": "other-carousel"}):
            with self.assertRaises(Conflict):
                apply(s, list(s["items"].values()), [], **kwargs)

    def test_receipts_are_idempotent_and_not_rewritable(self):
        s = receive(baseline(), event("same", "Keep the hook."))
        self.assertEqual(receive(s, event("same", "Keep the hook.")), s)
        with self.assertRaises(Conflict):
            receive(s, event("same", "Reject the hook."))

    def test_quote_provenance_cannot_be_fabricated(self):
        s = receive(baseline(), event("maybe", "Maybe, but change the ending."))
        with self.assertRaises(Conflict):
            apply(s, list(s["items"].values()), [disposition("maybe", "I approve everything")])

    def test_changed_source_hash_invalidates_packet(self):
        s = baseline()
        self.assertEqual(packet(s, {"opening.md": "different"})["status"], "SOURCE_CHANGED")

    def test_stale_or_edited_handoff_fails(self):
        s = baseline()
        p = packet(s, hashes(s))
        self.assertTrue(validate_handoff(p, s, hashes(s)))
        p["next_action"] = {"text": "Apply old copy", "targets": ["v03"]}
        with self.assertRaises(Conflict):
            validate_handoff(p, s, hashes(s))

    def test_rejected_history_requires_new_restoration_decision(self):
        s = receive(baseline(), event("reject", "Reject the middle."))
        old = item("v07", "middle", "rejected", "reject", "Reject the middle")
        s = apply(s, [*s["items"].values(), old], [disposition("reject", "Reject the middle")])
        restored = copy.deepcopy(s["items"]["v07"])
        restored["status"] = "candidate"
        with self.assertRaises(Conflict):
            apply(s, [s["items"]["opening"], restored], [])
        s = receive(s, event("restore", "Try the old middle again, as a candidate."))
        out = apply(s, [s["items"]["opening"], restored], [disposition("restore", "Try the old middle again")],
                    overrides={"v07": decision("restore", "Try the old middle again")})
        self.assertEqual(out["items"]["v07"]["status"], "candidate")

    def test_legacy_stack_detected_without_choosing_by_filename(self):
        self.assertEqual(inspect_legacy("> CURRENT v09\n> CURRENT v08\n# Current carousel — v05")["finding"], "COMPETING_CURRENT_LABELS")
        self.assertEqual(inspect_legacy("# Current carousel — v09")["finding"], "NO_STACK_DETECTED")


if __name__ == "__main__":
    unittest.main()

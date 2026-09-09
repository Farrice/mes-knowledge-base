#!/usr/bin/env python3
"""Stdlib-only regression and real-adapter subprocess proof; no model calls."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import outcome_next_proof as proof

ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / ".codex/tools/codex_hook_runner.py"


def message(role, text, phase=None):
    return {"type": "response_item", "payload": {"type": "message", "role": role, "phase": phase, "content": [{"type": "input_text" if role == "user" else "output_text", "text": text}]}}


def tool(output):
    return {"type": "response_item", "payload": {"type": "function_call_output", "call_id": "inspect", "output": json.dumps(output)}}


def call(name="exec_command", arguments=None):
    return {"type": "response_item", "payload": {"type": "function_call", "call_id": "inspect", "name": name, "arguments": json.dumps(arguments or {"cmd": "cat provider-access-check.txt"})}}


def assess(prompt, answer, outputs=()):
    return proof.assess(proof.current_turn([message("user", prompt), call(), *[tool(x) for x in outputs], message("assistant", answer, "final_answer")]))


class OutcomeProofTests(unittest.TestCase):
    def test_listing_failure(self):
        result = assess("Can you build a tool to make cinematic listing films and handle everything for me?", "Use Flow and subscribe to its paid plan.")
        self.assertEqual(result["flags"], ["provider_recommendation_without_observed_inspection", "requested_build_route_omitted"])

    def test_listing_comparison_with_inspection(self):
        result = assess("Can you build a tool to make cinematic listing films and handle everything for me?", "I compared a private tool, an assistant-operated workflow and the finished service. Use Flow provisionally; quality remains untested.", [{"exit_code": 0, "output": "Access checked; private build estimate and provider pricing inspected."}])
        self.assertEqual(result["status"], "NO_FLAG")
        self.assertFalse(result["quality_verified"])

    def test_invalid_test_rejection(self):
        result = assess("The wrong photo was attached and the upload failed. Can this app work?", "Therefore this is not feasible.")
        self.assertIn("invalid_test_used_for_broad_rejection", result["flags"])

    def test_invalid_test_qualified(self):
        result = assess("The wrong photo was attached and the upload failed. Can this app work?", "This does not prove the app cannot work. First correct the photo pairing; no new spending is authorized.")
        self.assertEqual(result["status"], "NO_FLAG")

    def test_authorized_action_handed_back(self):
        result = assess("Please install the approved local hook and verify the behavior now.", "Would you like me to install it?")
        self.assertIn("possible_premature_handoff", result["flags"])

    def test_read_only_negative_control(self):
        result = assess("Read-only MES diagnosis and ideation; do not build or run benchmarks.", "The comparison is incomplete. Here is the diagnosis and proposed proof; would you like me to implement it later?")
        self.assertEqual(result["status"], "NO_FLAG")

    def test_read_only_mutation_claim(self):
        result = assess("Read-only MES diagnosis and ideation; do not build or run benchmarks.", "I installed a new hook.")
        self.assertIn("claimed_mutation_in_read_only_turn", result["flags"])

    def test_real_blocker(self):
        result = assess("Please install the approved local hook and verify the behavior now.", "Integration is blocked by foreign changes. I need your approval for that separate reconciliation; you can run it later.")
        self.assertEqual(result["status"], "NO_FLAG")

    def test_tiny_and_system_turns_quiet(self):
        for prompt in ("Thanks!", "yes", "What time is it in Los Angeles?", "Translate this paragraph to Spanish please", "<task-notification>Build the app and install everything</task-notification>"):
            self.assertFalse(proof.meaningful(prompt), prompt)
        self.assertTrue(proof.meaningful("All right, let's install the approved hook and verify it please."))
        self.assertTrue(proof.meaningful("/system-audit"))

    def test_failed_running_unknown_tools_not_success(self):
        for output in ({"exit_code": 1}, {"session_id": 42}, {"isError": True}, {"output": "looks good"}, {"success": True, "isError": True}):
            turn = proof.current_turn([message("user", "Inspect the actual tools before recommending a subscription for the video."), call(), tool(output)])
            self.assertFalse(turn["observed_success"], output)

    def test_commentary_and_prior_turn_not_evidence(self):
        records = [message("user", "Old task"), call(), tool({"exit_code": 0}), message("assistant", "Old final"), message("user", "Install the approved hook and verify it now please."), message("assistant", "I verified everything", "commentary"), message("assistant", "Would you like me to install it?", "final_answer")]
        turn = proof.current_turn(records)
        self.assertFalse(turn["observed_success"])
        self.assertIn("possible_premature_handoff", proof.assess(turn)["flags"])

    def test_missing_transcript_or_final_is_unobserved(self):
        self.assertEqual(proof.assess(proof.current_turn([]))["status"], "UNOBSERVED")
        self.assertEqual(proof.assess(proof.current_turn([message("user", "Install the approved hook and verify it now please.")]))["status"], "UNOBSERVED")

    def test_wrong_session_rejected(self):
        records = [{"type": "session_meta", "payload": {"id": "other"}}, message("user", "Install the approved hook and verify it now please."), message("assistant", "Done.")]
        self.assertEqual(proof.assess(proof.current_turn(records, "this"))["status"], "UNOBSERVED")

    def test_claude_tool_envelope_keeps_user(self):
        records = [{"type": "user", "message": {"role": "user", "content": "Inspect tools and compare the listing video production routes please."}}, {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "tool_use", "id": "inspect", "name": "Read", "input": {"file_path": "access.txt"}}]}}, {"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "inspect", "is_error": False, "content": "Inspected provider"}]}}, {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "Use Flow provisionally; untested."}]}}]
        turn = proof.current_turn(records)
        self.assertTrue(turn["observed_success"])
        self.assertIn("Inspect tools", turn["prompt"])
        self.assertEqual(proof.assess(turn)["status"], "NO_FLAG")

    def test_activity_is_not_inspection(self):
        for name, args in (("exec_command", {"cmd": "mkdir output"}), ("clock__curr_time", {}), ("functions.exec", {"code": "text('finished')"})):
            turn = proof.current_turn([message("user", "Inspect provider access before recommending a paid video generation service please."), call(name, args), tool({"exit_code": 0}), message("assistant", "Use Flow and subscribe.", "final_answer")])
            self.assertFalse(turn["observed_success"])
            self.assertIn("provider_recommendation_without_observed_inspection", proof.assess(turn)["flags"])

    def test_unmatched_result_not_inspection(self):
        turn = proof.current_turn([message("user", "Inspect the video service and verify its execution access please."), tool({"exit_code": 0})])
        self.assertFalse(turn["observed_success"])

    def test_context_preserves_existing_fields(self):
        original = {"decision": "block", "reason": "existing gate", "hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "Existing routing"}}
        data = json.loads(proof.merge_context(json.dumps(original), "Outcome contract"))
        self.assertEqual(data["decision"], "block")
        self.assertEqual(data["reason"], "existing gate")
        self.assertEqual(data["hookSpecificOutput"]["additionalContext"], "Existing routing\n\nOutcome contract")

    def test_invalid_existing_json_fail_open(self):
        output, errors = proof.augment("skill-router", [], {"prompt": "Please install the approved local hook and verify it now."}, ROOT, "not json", "existing stderr\n")
        self.assertEqual(output, "not json")
        self.assertIn("UNOBSERVED", errors)
        self.assertTrue(errors.startswith("existing stderr"))

    def test_kill_switch_preserves_all(self):
        with patch.dict(os.environ, {"OUTCOME_NEXT_PROOF_OFF": "1"}):
            self.assertEqual(proof.augment("skill-router", [], {"prompt": "Please install the approved local hook and verify it now."}, ROOT, "original", "error"), ("original", "error"))

    def test_observer_dedup_and_stop_loop(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            transcript = root / "transcript.jsonl"
            transcript.write_text("\n".join(json.dumps(x) for x in [message("user", "Install the approved local hook and verify it now please."), message("assistant", "Would you like me to install it?", "final_answer")]))
            payload = {"session_id": "fixture", "transcript_path": str(transcript)}
            self.assertIn("possible_premature_handoff", proof.observe_stop(payload, root))
            self.assertEqual(proof.observe_stop(payload, root), "")
            self.assertEqual(proof.observe_stop({**payload, "stop_hook_active": True}, root), "")
            records = (root / ".agent/sessions/observe-log.jsonl").read_text().splitlines()
            self.assertEqual(len(records), 1)
            self.assertNotIn("Would you like", records[0])

    def test_actual_adapter_subprocess(self):
        # Actual adapter + actual companion; stub only unrelated legacy targets
        # to avoid mutating production ledgers or invoking unrelated workflows.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / ".agent/workflows").mkdir(parents=True)
            (root / "execution/hooks").mkdir(parents=True)
            (root / "CODEX.md").write_text("fixture")
            (root / Path(proof.CONTRACT).parent).mkdir(parents=True)
            shutil.copy(ROOT / proof.CONTRACT, root / proof.CONTRACT)
            for name in ("tool_event.py", "outcome_next_proof.py"):
                shutil.copy(ROOT / "execution" / name, root / "execution" / name)
            (root / "execution/skill_router_hook.py").write_text('import json\nprint(json.dumps({"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"EXISTING ROUTE"}}))\n')
            (root / "execution/hooks/session_ledger_hook.py").write_text('print("LEGACY STOP OUTPUT")\n')
            env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "OUTCOME_NEXT_PROOF_OFF": "0"}
            payload = {"cwd": str(root), "prompt": "Please compare the private tool and service for listing films and handle the execution."}
            proc = subprocess.run([sys.executable, str(RUNNER), "skill-router"], input=json.dumps(payload), capture_output=True, text=True, env=env)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            context = json.loads(proc.stdout)["hookSpecificOutput"]["additionalContext"]
            self.assertIn("EXISTING ROUTE", context)
            self.assertIn("Own the outcome through the next useful proof.", context)
            self.assertIn("read-only requests authorize investigation", context)
            transcript = root / "transcript.jsonl"
            transcript.write_text("\n".join(json.dumps(x) for x in [message("user", "Please build a tool for my listing videos and handle everything."), message("assistant", "Use Flow and subscribe.", "final_answer")]))
            proc = subprocess.run([sys.executable, str(RUNNER), "session-ledger", "stop"], input=json.dumps({"cwd": str(root), "transcript_path": str(transcript), "session_id": "fixture"}), capture_output=True, text=True, env=env)
            self.assertEqual(proc.returncode, 0)
            self.assertEqual(proc.stdout, "LEGACY STOP OUTPUT\n")
            self.assertIn("OUTCOME REVIEW", proc.stderr)
            self.assertTrue((root / ".agent/sessions/observe-log.jsonl").exists())

    def test_registrations_unchanged_and_adapted(self):
        hooks = json.loads((ROOT / ".codex/hooks.json").read_text())["hooks"]
        self.assertTrue(any("skill-router" in h["command"] for group in hooks["UserPromptSubmit"] for h in group["hooks"]))
        self.assertTrue(any("session-ledger stop" in h["command"] for group in hooks["Stop"] for h in group["hooks"]))
        self.assertIn("from outcome_next_proof import augment", RUNNER.read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)

import concurrent.futures
import copy
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import working_context as wc


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = self.root / 'state.sqlite3'
        self.sid = wc.key('codex', 'fixture-session')
        self.payload = {'session_id': 'fixture-session', 'cwd': str(self.root), 'prompt': 'Build a reliable recovery flow. Keep the API.', 'turn_id': 'turn-1'}
        wc.hook(self.payload, 'codex', 'UserPromptSubmit', self.store)

    def tearDown(self):
        self.temp.cleanup()

    def request(self, snapshot=True):
        state = wc.read(self.sid, self.store)
        out = {'expected_revision': state['revision'], 'resolutions': [
            {'turn': t['seq'], 'quote': t['text'], 'effect': 'Integrate refinement within the whole objective.'} for t in state['pending']]}
        if snapshot:
            out['snapshot'] = {'intent': 'Build a reliable recovery flow.', 'working_brief': 'Preserve the API while improving recovery.',
                               'preserved': [{'id': 'api', 'text': 'Keep the API.', 'scope': 'task', 'evidence': {'turn': 1, 'quote': 'Keep the API.'}}],
                               'artifacts': [], 'next_action': {'text': 'Implement and test recovery.', 'targets': []}}
        return out

    def commit(self, request=None):
        return wc.commit(self.sid, request or self.request(), self.store)

    def receive(self, text, turn='turn-2'):
        return wc.hook({**self.payload, 'prompt': text, 'turn_id': turn}, 'codex', 'UserPromptSubmit', self.store)

    def test_capture_and_reconcile(self):
        self.assertEqual(wc.read(self.sid, self.store)['status'], 'PENDING')
        self.commit()
        self.assertEqual(wc.read(self.sid, self.store)['status'], 'CURRENT')

    def test_duplicate_event_is_idempotent(self):
        before = wc.read(self.sid, self.store)
        wc.hook(self.payload, 'codex', 'UserPromptSubmit', self.store)
        self.assertEqual(wc.read(self.sid, self.store)['revision'], before['revision'])

    def test_identical_text_on_different_turns_is_captured(self):
        self.receive(self.payload['prompt'])
        self.assertEqual(len(wc.read(self.sid, self.store)['pending']), 2)

    def test_reused_identity_with_changed_text_fails(self):
        with self.assertRaises(wc.Conflict):
            self.receive('Different', 'turn-1')

    def test_every_turn_including_mid_turn_input(self):
        self.commit()
        self.receive('Make the wording shorter.')
        for tool in ['exec_command', 'Bash', 'apply_patch', 'Read', 'mcp__tool']:
            out = wc.hook({**self.payload, 'tool_name': tool}, 'codex', 'PreToolUse', self.store)
            self.assertIn('Pending turns: [2]', out['hookSpecificOutput']['additionalContext'])

    def test_status_question_explicit_no_change(self):
        self.commit()
        self.receive('What is the status?')
        self.commit(self.request(snapshot=False))
        self.assertEqual(wc.read(self.sid, self.store)['snapshot']['intent'], 'Build a reliable recovery flow.')

    def test_conversation_without_artifacts(self):
        request = self.request(snapshot=False)
        request['no_change_reason'] = 'Conversation-only turn.'
        self.commit(request)
        self.assertEqual(wc.handoff(self.sid, self.store)['snapshot'], None)

    def test_latest_correction_cannot_replace_objective(self):
        self.commit()
        self.receive('Make it shorter.')
        request = self.request()
        request['snapshot']['intent'] = 'Minimize word count.'
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_explicit_replacement_is_allowed(self):
        self.commit()
        self.receive('Stop recovery. Build export instead.')
        request = self.request()
        request['snapshot']['intent'] = 'Build export.'
        request['overrides'] = {'intent': {'turn': 2, 'quote': 'Build export instead.', 'kind': 'objective-change'}}
        self.commit(request)

    def test_preserved_part_cannot_disappear(self):
        self.commit()
        self.receive('Change the wording.')
        request = self.request()
        request['snapshot']['preserved'] = []
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_local_correction_not_promoted_globally(self):
        request = self.request()
        request['snapshot']['preserved'][0]['scope'] = 'global'
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_skip_pending_turn_fails(self):
        self.receive('Keep the goal.')
        request = self.request()
        request['resolutions'].pop()
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_wrong_quote_fails(self):
        request = self.request()
        request['resolutions'][0]['quote'] = 'I approve the entire artifact'
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_transaction_failure_preserves_state(self):
        before = wc.read(self.sid, self.store)
        request = self.request()
        request['snapshot']['intent'] = ''
        with self.assertRaises(wc.Conflict):
            self.commit(request)
        self.assertEqual(wc.read(self.sid, self.store)['revision'], before['revision'])
        self.assertEqual(wc.read(self.sid, self.store)['pending'], before['pending'])

    def test_stale_writer_fails(self):
        request = self.request()
        self.receive('New constraint.')
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_concurrent_receipts_are_lossless(self):
        def receive(n):
            wc.observe(self.sid, str(self.root), f'feedback {n}', f'parallel-{n}', path=self.store)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            list(executor.map(receive, range(12)))
        self.assertEqual(len(wc.read(self.sid, self.store)['pending']), 13)

    def test_stop_requests_one_recovery_and_does_not_loop(self):
        self.assertEqual(wc.hook(self.payload, 'codex', 'Stop', self.store)['decision'], 'block')
        self.assertEqual(wc.hook({**self.payload, 'stop_hook_active': True}, 'codex', 'Stop', self.store), {})
        self.commit()
        self.assertEqual(wc.hook(self.payload, 'codex', 'Stop', self.store), {})

    def test_resume_and_compaction_load_whole_intent(self):
        self.commit()
        for event in ['SessionStart', 'PreCompact', 'PostCompact']:
            out = wc.hook(self.payload, 'codex', event, self.store)
            self.assertEqual(out['hookSpecificOutput']['hookEventName'], event)
            self.assertIn('Build a reliable recovery flow.', out['hookSpecificOutput']['additionalContext'])

    def artifact(self, role='candidate', identity='draft', purpose='copy'):
        p = self.root / (identity + '.md')
        p.write_text('Original text')
        return {'id': identity, 'path': str(p), 'purpose': purpose, 'role': role,
                'evidence': {'turn': 1, 'quote': 'Build a reliable recovery flow.'}}

    def test_actual_source_change_detected_after_shell_write(self):
        request = self.request()
        artifact = self.artifact()
        request['snapshot']['artifacts'] = [artifact]
        self.commit(request)
        Path(artifact['path']).write_text('Changed by a shell or another tool')
        out = wc.hook({**self.payload, 'tool_name': 'exec_command'}, 'codex', 'PostToolUse', self.store)
        self.assertIn('SOURCE_CHANGED', out['hookSpecificOutput']['additionalContext'])

    def test_only_one_candidate_per_purpose(self):
        request = self.request()
        request['snapshot']['artifacts'] = [self.artifact(identity='v1'), self.artifact(identity='v2')]
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_rejected_target_cannot_be_next_action(self):
        request = self.request()
        artifact = self.artifact('rejected')
        artifact['reason'] = 'Failed the user brief.'
        request['snapshot']['artifacts'] = [artifact]
        request['snapshot']['next_action']['targets'] = ['draft']
        with self.assertRaises(wc.Conflict):
            self.commit(request)

    def test_history_excluded_from_handoff(self):
        request = self.request()
        artifact = self.artifact('rejected')
        artifact['reason'] = 'Wrong direction.'
        request['snapshot']['artifacts'] = [artifact]
        self.commit(request)
        self.assertEqual(wc.handoff(self.sid, self.store)['snapshot']['artifacts'], [])

    def test_handoff_stale_or_tampered_fails(self):
        self.commit()
        p = wc.handoff(self.sid, self.store)
        self.assertTrue(wc.verify_handoff(self.sid, p, self.store))
        p['revision'] += 1
        with self.assertRaises(wc.Conflict):
            wc.verify_handoff(self.sid, p, self.store)

    def test_current_view_is_replaced_not_stacked(self):
        request = self.request()
        request['write_root'] = str(self.root)
        self.commit(request)
        state = wc.read(self.sid, self.store)
        p = Path(state['current_view'])
        p.write_text(p.read_text() + '\nCURRENT v03 apply rejected copy\n')
        self.assertEqual(wc.read(self.sid, self.store)['status'], 'DRIFT')
        wc.render(wc.read(self.sid, self.store), self.store)
        self.assertNotIn('CURRENT v03', p.read_text())
        self.assertEqual(wc.read(self.sid, self.store)['status'], 'CURRENT')
        with wc.database(self.store) as db:
            self.assertIn('CURRENT v03', db.execute("SELECT data FROM events WHERE event='current-view-preserved'").fetchone()[0])

    def test_main_root_and_symlink_are_rejected(self):
        (self.root / '.git').mkdir()
        with self.assertRaises(wc.Conflict):
            wc.check_write_root(self.root)

    def test_ten_turns_cover_all_domains(self):
        self.commit()
        for n, text in enumerate(['Shorter plan', 'New research', 'Keep the audience', 'Change the interface', 'Status?', 'Revise the hook', 'Keep the budget', 'Return to the offer', 'Clarify the goal'], 2):
            self.receive(text, f'turn-{n}')
            self.commit(self.request(snapshot=False))
            self.assertEqual(wc.read(self.sid, self.store)['status'], 'CURRENT')
        with wc.database(self.store) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM turns WHERE resolved=1').fetchone()[0], 10)

    def test_session_isolation(self):
        other = wc.key('claude', 'fixture-session')
        wc.observe(other, str(self.root), 'Different purpose.', path=self.store)
        self.commit()
        self.assertEqual(wc.read(other, self.store)['status'], 'PENDING')


if __name__ == '__main__':
    unittest.main()

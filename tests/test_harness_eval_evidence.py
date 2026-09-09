"""Reject green scores based on missing, structural or changed evidence."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'execution'))
from verify_harness_eval_evidence import validate


class EvalEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.payload = {'results': [{'id': f'E{i}', 'status': 'NOT_RUN',
                                     'observation': 'No authorized fresh run available.'}
                                    for i in range(1, 7)]}

    def result(self, key, text, kind='model-run', filename='response.txt'):
        path = self.base / filename
        path.write_text(text)
        row = next(r for r in self.payload['results'] if r['id'] == key)
        row.update(status='PASS', kind=kind, input='what does execution/notify.py do? one paragraph.',
                   execution_ref='offline regression fixture; not a production model result',
                   evidence_file=filename, evidence_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                   observation='Fixture used to exercise the evidence checker.')
        return row

    def test_unrun_cases_are_valid_but_not_passes(self):
        self.assertEqual(validate(self.payload, self.base), [])
        self.assertFalse(any(r['status'] == 'PASS' for r in self.payload['results']))

    def test_old_instruction_presence_pass_is_rejected(self):
        row = self.payload['results'][4]
        row.update(status='PASS', observation='Model dialect specifies length constraints are honored.')
        self.assertTrue(validate(self.payload, self.base))

    def test_instruction_source_cannot_be_model_evidence(self):
        self.result('E5', 'Always answer in one paragraph.', filename='AGENTS.md')
        self.assertTrue(any('instruction file' in e for e in validate(self.payload, self.base)))

    def test_short_actual_response_is_accepted(self):
        self.result('E5', 'The script sends a macOS notification and optionally an ntfy push when a topic is configured.')
        self.assertEqual(validate(self.payload, self.base), [])

    def test_long_form_and_bullets_cannot_pass(self):
        for text in ('word ' * 121, 'First paragraph.\n\nSecond paragraph.', '# Heading\nContent', '- A list item'):
            with self.subTest(text=text[:25]):
                self.result('E5', text)
                self.assertTrue(validate(self.payload, self.base))

    def test_mutated_or_missing_output_is_rejected(self):
        self.result('E5', 'An original observed response.')
        (self.base / 'response.txt').write_text('A replacement, not the observed response.')
        self.assertTrue(validate(self.payload, self.base))
        (self.base / 'response.txt').unlink()
        self.assertTrue(validate(self.payload, self.base))

    def test_script_output_cannot_stand_in_for_model_behavior(self):
        self.result('E5', 'PASS: instructions exist.', kind='tool-run')
        self.assertTrue(validate(self.payload, self.base))

    def test_router_needs_execution_trace_as_well_as_answer(self):
        self.result('E1', 'Here is a LinkedIn draft.')
        self.assertTrue(any('trace_file' in e for e in validate(self.payload, self.base)))

    def test_all_six_cases_required_once(self):
        self.payload['results'].pop()
        self.assertTrue(validate(self.payload, self.base))


if __name__ == '__main__':
    unittest.main()

"""Offline controls: unavailable evidence must never become an empty log."""
import contextlib
import io
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'execution'))
import system_health as health


class HealthEvidenceTests(unittest.TestCase):
    def query(self, result=None, error=None):
        with patch.object(health, 'NotionAPI') as api:
            api.return_value.query_database.return_value = result
            api.return_value.query_database.side_effect = error
            return health.check_performance_log()

    def render(self, perf):
        ordinary = {'status': 'ACTIVE', 'health': 'Healthy', 'message': 'Today', 'count': 1}
        with tempfile.TemporaryDirectory() as temp, \
                patch.object(health, 'ROOT', Path(temp)), \
                patch.object(health, 'check_performance_log', return_value=perf), \
                patch.object(health, 'check_hookify_hooks', return_value=[]), \
                patch.object(health, 'check_session_state', return_value=ordinary), \
                patch.object(health, 'check_gap_log', return_value=ordinary), \
                patch.object(health, 'check_routing_intelligence', return_value=ordinary), \
                patch.object(health, 'check_memory', return_value={'status': 'MISSING', 'health': 'Unknown'}), \
                contextlib.redirect_stdout(io.StringIO()) as output:
            health.generate_health_report(quick=True)
            return output.getvalue()

    def test_network_error_is_unknown_in_data_and_report(self):
        perf = self.query(error=OSError('DNS unavailable'))
        self.assertEqual(perf['status'], 'UNKNOWN')
        self.assertIsNone(perf['count'])
        text = self.render(perf)
        self.assertIn('DNS unavailable', text)
        self.assertIn('| Skill Evolution (Phase 2) | UNKNOWN', text)
        self.assertIn('| Gap Detection (Phase 4) | UNKNOWN', text)
        self.assertIn('| Cross-Pollination (Phase 3) | UNMEASURED', text)
        self.assertNotIn('0/20', text)
        self.assertNotIn('Start logging performance entries', text)

    def test_malformed_response_is_not_zero(self):
        for response in (None, {}, {'results': None}, {'results': {}}, {'results': [None]}):
            with self.subTest(response=response):
                self.assertIsNone(self.query(response)['count'])

    def test_successful_empty_response_remains_zero(self):
        perf = self.query({'results': []})
        self.assertEqual((perf['status'], perf['count']), ('DORMANT', 0))
        self.assertNotIn('never fired', perf['message'])
        text = self.render(perf)
        self.assertIn('BLOCKED (0/20 entries)', text)
        self.assertIn('Start logging performance entries', text)

    def test_readiness_thresholds_remain_measured(self):
        page = {'properties': {'Date': {'type': 'date', 'date': {'start': date.today().isoformat()}}}}
        for count in (4, 5, 19, 20):
            with self.subTest(count=count):
                perf = self.query({'results': [page] * count})
                self.assertEqual(perf['count'], count)
                text = self.render(perf)
                phase2 = 'READY' if count >= 20 else f'BLOCKED ({count}/20 entries)'
                phase4 = 'READY' if count >= 5 else 'BLOCKED'
                self.assertIn(f'| Skill Evolution (Phase 2) | {phase2}', text)
                self.assertIn(f'| Gap Detection (Phase 4) | {phase4}', text)
                self.assertIn('| Cross-Pollination (Phase 3) | UNMEASURED', text)

    def test_legacy_error_zero_does_not_reintroduce_false_block(self):
        text = self.render({'status': 'ERROR', 'count': 0, 'health': 'Unknown',
                            'last_date': 'Error', 'message': 'Legacy upstream failure'})
        self.assertIn('| Skill Evolution (Phase 2) | UNKNOWN', text)
        self.assertNotIn('Start logging performance entries', text)


if __name__ == '__main__':
    unittest.main()

"""Offline safety/behavior proof. No Gemini key or network is used."""
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'execution'))
from content_analysis_pilot import Denied, Pilot, classify_source

NOW = 1789430400.0  # 2026-09-15 UTC; stable fixture clock, not provider time.
URL1 = 'https://www.youtube.com/watch?v=abcdefghijk'
URL2 = 'https://youtu.be/lmnopqrstuv'


def request(**kwargs):
    value = {'question': 'Identify visual evidence, with timestamps.',
             'items': [{'source': URL1, 'duration_seconds': 60}], 'timeout_seconds': 5}
    value.update(kwargs)
    return value


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.now = NOW
        self.pilot = Pilot(self.tmp.name, clock=lambda: self.now)

    def tearDown(self):
        self.tmp.cleanup()

    def batch(self, value=None, approve=True):
        result = self.pilot.preview(value or request())
        batch = result['batch']
        if approve:
            self.pilot.approve(batch, batch, '1.00', 'Authorized offline simulation; not a paid call')
        return batch

    def test_live_blocked_even_with_key_and_approval(self):
        batch = self.batch()
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'not-a-real-key', 'ENABLE_LIVE': '1'}):
            with self.assertRaisesRegex(Denied, 'LIVE EXECUTION DISABLED'):
                self.pilot.run(batch, live=True)
        self.assertEqual(self.pilot.status(batch)['calls'], [])

    def test_cli_run_blocked_without_creating_state(self):
        state = Path(self.tmp.name) / 'never-created'
        p = subprocess.run([sys.executable, str(ROOT/'execution/content_analysis_pilot.py'),
                            '--state-dir', str(state), 'run', 'anything'], capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)
        self.assertIn('LIVE EXECUTION DISABLED', p.stderr)
        self.assertFalse(state.exists())

    def test_no_approval_means_no_dispatch(self):
        batch = self.batch(approve=False)
        with self.assertRaises(Denied):
            self.pilot.run(batch)
        self.assertEqual(self.pilot.status(batch)['calls'], [])

    def test_hash_budget_and_expiry(self):
        batch = self.batch(approve=False)
        for expected, budget in [('wrong', '1'), (batch, '0'), (batch, 'NaN'), (batch, '-1')]:
            with self.assertRaises(Denied):
                self.pilot.approve(batch, expected, budget, 'simulation')
        self.pilot.approve(batch, batch, '1', 'simulation', ttl_seconds=1)
        self.now += 2
        with self.assertRaisesRegex(Denied, 'expired'):
            self.pilot.run(batch)
        self.assertEqual(self.pilot.status(batch)['calls'], [])

    def test_changed_question_gets_new_unapproved_batch(self):
        self.batch()
        changed = self.pilot.preview(request(question='Different analysis'))['batch']
        with self.assertRaises(Denied):
            self.pilot.run(changed)

    def test_plan_tampering_denied(self):
        batch = self.batch()
        with self.pilot.connect() as conn:
            conn.execute('UPDATE batches SET plan=? WHERE id=?', ('{}', batch))
        with self.assertRaisesRegex(Denied, 'integrity'):
            self.pilot.run(batch)

    def test_source_bytes_change_denied_before_reserving(self):
        source = Path(self.tmp.name)/'video.mp4'
        source.write_bytes(b'synthetic media bytes; no footage')
        batch = self.batch(request(items=[{'source': str(source), 'duration_seconds': 10}]))
        source.write_bytes(b'changed')
        with self.assertRaisesRegex(Denied, 'source changed'):
            self.pilot.run(batch)
        self.assertEqual(self.pilot.status(batch)['calls'], [])

    def test_youtube_alias_duplicates_denied(self):
        duplicate = request(items=[{'source': URL1+'&utm_source=x', 'duration_seconds': 10},
                                   {'source': 'https://youtu.be/abcdefghijk', 'duration_seconds': 10}])
        with self.assertRaisesRegex(Denied, 'duplicate'):
            self.pilot.preview(duplicate)

    def test_unsupported_links_are_not_claimed_accessible(self):
        for url in ['https://instagram.com/reel/example', 'https://tiktok.com/@x/video/1',
                    'https://example.com/article', 'https://www.youtube.com/@channel']:
            self.assertFalse(classify_source(url)['ready'])
            with self.assertRaisesRegex(Denied, 'retrieval or native reading'):
                self.pilot.preview(request(items=[{'source': url, 'duration_seconds': 10}]))

    def test_unknown_model_duration_and_expired_prices(self):
        for value in [request(model='unpriced'), request(max_output_tokens=True),
                      request(items=[{'source': URL1, 'duration_seconds': float('inf')}]),
                      request(items=[{'source': URL1, 'duration_seconds': -1}]),
                      request(items=[{'source': URL1, 'duration_seconds': 3600}], resolution='high')]:
            with self.assertRaises(Denied):
                self.pilot.preview(value)
        self.now = 1800000000
        with self.assertRaisesRegex(Denied, 'pricing snapshot expired'):
            self.pilot.preview(request())

    def test_agentic_preview_never_claims_a_bound(self):
        plan = self.pilot.preview(request(processing='agentic'))['preview']
        self.assertEqual(plan['agentic_cost_bound'], 'UNVERIFIED')
        self.assertEqual(plan['paid_execution'], 'DISABLED')

    def test_success_and_repeat_spend_nothing_more(self):
        batch = self.batch()
        first = self.pilot.run(batch)
        second = self.pilot.run(batch)
        self.assertEqual(first, second)
        self.assertEqual(len(second['calls']), 1)
        self.assertEqual(second['real_api_calls'], 0)
        self.assertEqual(second['quality_proof'], 'NOT_RUN')
        self.assertEqual(second['calls'][0]['result']['evidence_status'], 'SYNTHETIC_NOT_OBSERVED')

    def test_cache_reused_across_batches(self):
        first = self.batch()
        self.pilot.run(first)
        second = self.batch(request(items=[{'source': URL1, 'duration_seconds': 60},
                                           {'source': URL2, 'duration_seconds': 60}]))
        result = self.pilot.run(second)
        self.assertEqual(len(result['calls']), 1)
        self.assertEqual(result['planned_items'], 2)
        self.assertTrue(result['items'][0]['reused'])
        self.assertIsNotNone(result['items'][0]['result'])

    def test_concurrent_runners_cannot_double_dispatch(self):
        batch = self.batch()
        barrier = threading.Barrier(2)
        def run():
            barrier.wait()
            try:
                return self.pilot.run(batch)['status']
            except Denied:
                return 'denied'
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: run(), range(2)))
        self.assertIn('complete', results)
        self.assertEqual(len(self.pilot.status(batch)['calls']), 1)

    def test_crash_missing_usage_and_overrun_stop_batch(self):
        for fault in ['crash', 'missing-usage', 'overrun']:
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as directory:
                p = Pilot(directory, clock=lambda: NOW)
                batch = p.preview(request(items=[{'source': URL1, 'duration_seconds': 60},
                                                  {'source': URL2, 'duration_seconds': 60}]))['batch']
                p.approve(batch, batch, '1', 'simulation')
                with self.assertRaises(Denied):
                    p.run(batch, fault=fault)
                status = p.status(batch)
                self.assertEqual(status['status'], 'stopped')
                self.assertEqual(len(status['calls']), 1)
                call = status['calls'][0]
                self.assertEqual(call['status'], 'unknown')
                self.assertGreater(float(status['simulated_liability_usd']), 0)
                if fault == 'overrun':
                    self.assertGreater(call['actual'], call['reserved'])
                with self.assertRaises(Denied):
                    p.run(batch)

    def test_real_child_deadline_preserves_liability(self):
        batch = self.batch(request(timeout_seconds=1))
        start = time.monotonic()
        with self.assertRaisesRegex(Denied, 'deadline exceeded'):
            self.pilot.run(batch, fault='timeout')
        self.assertLess(time.monotonic() - start, 3)
        status = self.pilot.status(batch)
        self.assertEqual(status['calls'][0]['status'], 'unknown')
        self.assertIsNone(status['calls'][0]['actual'])
        self.assertGreater(float(status['simulated_liability_usd']), 0)

    def test_interruption_reservation_survives_restart_and_blocks_other_batch(self):
        batch = self.batch()
        with self.pilot.transaction() as conn:
            _, plan = self.pilot._load(conn, batch)
            conn.execute("UPDATE batches SET status='running' WHERE id=?", (batch,))
        self.pilot._reserve(batch, plan['items'][0])  # process died after durable reserve, before receipt
        fresh = Pilot(self.tmp.name, clock=lambda: NOW)
        other = fresh.preview(request(question='Another goal'))['batch']
        fresh.approve(other, other, '1', 'simulation')
        with self.assertRaisesRegex(Denied, 'unresolved reservation'):
            fresh.run(other)
        self.assertGreater(float(fresh.status(batch)['simulated_liability_usd']), 0)
        self.assertEqual(fresh.status(other)['calls'], [])

    def test_approval_expiring_mid_batch_stops_next_dispatch(self):
        batch = self.batch(request(items=[{'source': URL1, 'duration_seconds': 60},
                                           {'source': URL2, 'duration_seconds': 60}]))
        original = self.pilot._finish
        def finish(*args, **kwargs):
            original(*args, **kwargs)
            self.now += 1000
        with patch.object(self.pilot, '_finish', side_effect=finish):
            with self.assertRaisesRegex(Denied, 'expired'):
                self.pilot.run(batch)
        self.assertEqual(len(self.pilot.status(batch)['calls']), 1)

    def test_corrupt_database_never_resets_to_fresh_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, 'simulation.sqlite3').write_bytes(b'not a sqlite database')
            with self.assertRaises(sqlite3.DatabaseError):
                Pilot(directory)


if __name__ == '__main__':
    unittest.main(verbosity=2)

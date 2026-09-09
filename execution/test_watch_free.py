#!/usr/bin/env python3
"""Negative controls for the free watch adapter, stdlib only."""
import argparse
import ast
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import watch_free as w

class FreeWatchTests(unittest.TestCase):
    def test_caption_markup_and_rolling_overlap(self):
        text, parts = w.clean_vtt('WEBVTT\n\n00:00:00.000 --> 00:00:02.000\n<c>Hello &amp; welcome</c>\n\n00:00:02.000 --> 00:00:04.000\nHello &amp; welcome to this test\n')
        self.assertEqual([x['text'] for x in parts], ['Hello & welcome', 'to this test'])
        self.assertEqual(parts[-1]['end_seconds'], 4)
    def test_empty_is_not_success(self):
        self.assertEqual(w.coverage([], 60)['status'], 'missing')
    def test_gap_is_visible(self):
        c=w.coverage([{'start_seconds': 40, 'end_seconds': 45}], 100)
        self.assertEqual(c['gaps_over_30s'], [[0.,40], [45,100]])
        self.assertEqual(c['timeline_fraction'], .05)
    def test_cues_preserved(self):
        x=w.sample_times(100, 10, [3.14, 91.4])
        self.assertIn(3.14,x); self.assertIn(91.4,x)
        self.assertEqual(len(x),10)
        self.assertEqual(x[0],0); self.assertGreater(x[-1],99)
    def test_invalid_frame_request(self):
        for duration,n,cues in [(float('nan'),10,[]),(20,0,[]),(20,201,[]),(20,3,[21]),(20,2,[1,2,3])]:
            with self.assertRaises(ValueError): w.sample_times(duration,n,cues)
    def test_no_global_config_plugins_or_retries(self):
        cmd=w.ytdlp_args()
        for flag in ['--ignore-config','--no-plugin-dirs','--no-playlist']:
            self.assertIn(flag,cmd)
        self.assertEqual(cmd[cmd.index('--retries')+1], '0')
        source=Path(w.__file__).read_text()
        tree=ast.parse(source)
        imports={node.names[0].name for node in ast.walk(tree) if isinstance(node,ast.Import)}
        self.assertFalse(imports & {'requests','openai','groq','httpx'})
        self.assertNotIn('load_api_key',source)
    def test_timeout_is_failure(self):
        with tempfile.TemporaryDirectory() as d:
            rc=w.run([sys.executable,'-c','import time; time.sleep(10)'],Path(d)/'timeout.log',.05)
            self.assertEqual(rc,124)
            self.assertIn('TIMEOUT',(Path(d)/'timeout.log').read_text())
    def test_previous_capture_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'acquisition.json'; p.write_text('original')
            with self.assertRaises(ValueError):
                w.acquire(argparse.Namespace(out_dir=d))
            self.assertEqual(p.read_text(),'original')
    def test_dependency_failure_writes_honest_receipt(self):
        with tempfile.TemporaryDirectory() as d, patch.object(w.shutil,'which',return_value=None):
            with self.assertRaises(RuntimeError):
                w.acquire(argparse.Namespace(out_dir=d,source='missing.mp4',origin_url=None))
            r=json.loads((Path(d)/'acquisition.json').read_text())
            self.assertEqual(r['status'],'FAILED')
            self.assertEqual(r['review_status'],'NOT_REVIEWED')
            self.assertEqual(r['paid_api_calls'],0)

if __name__ == '__main__': unittest.main()

# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0"]
# ///
"""Unit tests for check_form_vs_ref.py — FORM-VS-REF SIGNATURE (woven ref → flat chips mis-route).

Tests the ref woven-signature pixel read, the output flat-isolated HTML read, and the evaluate
verdict — on synthetic inputs (no hardcoded slug). Run: uv run test_check_form_vs_ref.py
"""
import sys
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_form_vs_ref import (  # noqa: E402
    ref_woven_signature,
    output_flat_isolated,
    evaluate,
)

# Output HTML: 3 axis-aligned pills (NO rotate) — the flat-isolated shape (highlight-pills).
HTML_FLAT_PILLS = '''
<div class="zone headline" data-slot="HEADLINE"
     style="left:5%; top:12%; width:88%; height:72%;">We build agents</div>
<div class="callout-pill cream" data-slot="PILL_1" style="top:24%; right:3%;">Strategy first</div>
<div class="callout-pill dark"  data-slot="PILL_2" style="top:44%; right:3%;">Built for clarity</div>
<div class="callout-pill cream" data-slot="PILL_3" style="top:64%; left:5%;">Scales with you</div>
'''
# Output HTML: pills with transform: rotate — a genuine woven reproduction.
HTML_WOVEN_PILLS = '''
<div class="zone headline" data-slot="HEADLINE"
     style="left:5%; top:12%; width:88%; height:72%;">We build agents</div>
<div class="callout-pill" data-slot="PILL_1"
     style="top:24%; left:40%; transform: rotate(-8deg);">Strategy first</div>
<div class="callout-pill" data-slot="PILL_2"
     style="top:44%; left:45%; transform: rotate(6deg);">Built for clarity</div>
'''
HTML_NO_PILLS = '''
<div class="zone headline" data-slot="HEADLINE" style="left:5%; top:12%; width:88%; height:72%;">X</div>
'''


def _woven_ref(green_pills=4) -> Image.Image:
    """A cream canvas with N small vivid-green tilted pills in the headline band (the ref shape)."""
    arr = np.full((300, 240, 3), 240, np.uint8)  # cream field
    ys = [70, 120, 170, 210][:green_pills]
    for i, y in enumerate(ys):
        x = 60 + (i % 2) * 80
        # a tilted (diagonal) green blob — low bbox fill
        for dy in range(24):
            for dx in range(48):
                if abs(dx - dy * 2) < 14:  # a slanted band → low fill ratio
                    yy, xx = y + dy, x + dx
                    if yy < 300 and xx < 240:
                        arr[yy, xx] = (120, 210, 70)
    return Image.fromarray(arr)


def _plain_ref() -> Image.Image:
    """A cream canvas with NO vivid devices — not woven."""
    return Image.fromarray(np.full((300, 240, 3), 240, np.uint8))


class RefSignatureTests(unittest.TestCase):
    def test_woven_ref_reads_woven(self):
        sig = ref_woven_signature(_woven_ref(4))
        self.assertTrue(sig["is_woven"])
        self.assertGreaterEqual(sig["n_devices"], 2)
        self.assertGreaterEqual(sig["n_tilted"], 1)

    def test_plain_ref_not_woven(self):
        self.assertFalse(ref_woven_signature(_plain_ref())["is_woven"])


class OutputReadTests(unittest.TestCase):
    def test_flat_pills_read_flat_isolated(self):
        out = output_flat_isolated(HTML_FLAT_PILLS)
        self.assertTrue(out["flat_isolated"])
        self.assertEqual(out["n_pills"], 3)
        self.assertEqual(out["n_rotated"], 0)

    def test_rotated_pills_not_flat(self):
        out = output_flat_isolated(HTML_WOVEN_PILLS)
        self.assertFalse(out["flat_isolated"])
        self.assertEqual(out["n_rotated"], 2)

    def test_no_pills(self):
        self.assertEqual(output_flat_isolated(HTML_NO_PILLS)["n_pills"], 0)


class EvaluateTests(unittest.TestCase):
    def test_woven_ref_flat_output_is_mis_route(self):  # highlight-pills
        res = evaluate(HTML_FLAT_PILLS, _woven_ref(4), "#d05344")
        self.assertFalse(res["ok"])
        self.assertTrue(res["mis_route"])

    def test_woven_ref_woven_output_passes(self):
        res = evaluate(HTML_WOVEN_PILLS, _woven_ref(4), "#d05344")
        self.assertTrue(res["ok"])

    def test_plain_ref_no_mis_route(self):
        res = evaluate(HTML_FLAT_PILLS, _plain_ref(), "#d05344")
        self.assertTrue(res["ok"])
        self.assertFalse(res["mis_route"])

    def test_no_output_pills_is_not_applicable(self):
        res = evaluate(HTML_NO_PILLS, _woven_ref(4), "#d05344")
        self.assertTrue(res["ok"])

    def test_no_ref_is_indeterminate(self):
        res = evaluate(HTML_FLAT_PILLS, None, "#d05344")
        self.assertTrue(res["ok"])
        self.assertTrue(res["indeterminate"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

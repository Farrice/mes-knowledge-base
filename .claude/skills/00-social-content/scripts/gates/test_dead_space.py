# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0"]
# ///
"""Unit tests for dead_space.py — the dead-space / proportion gate measurement.

Tests the MEASUREMENT (deterministic geometry), not the aesthetic. Per AIOS-190 PRD:
"script-measured gate criteria need unit coverage ... test the measurement, not the aesthetic."

Run:
    uv run test_dead_space.py
    or: python test_dead_space.py
"""
import sys
import unittest
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from dead_space import (  # noqa: E402
    dominant_color,
    uniform_mask,
    largest_component_fraction,
    empty_fraction,
    text_height_fraction,
    evaluate,
)


class TestDominantColor(unittest.TestCase):
    def test_majority_color_wins(self):
        arr = np.zeros((100, 100, 3), dtype=np.uint8)
        arr[:] = (255, 255, 255)          # all white
        arr[:10, :10] = (10, 20, 30)      # small dark patch
        bg = dominant_color(arr)
        # white quantized to 240
        self.assertTrue((bg == np.array([240, 240, 240])).all())


class TestUniformMask(unittest.TestCase):
    def test_tolerance_boundary(self):
        arr = np.zeros((2, 3, 3), dtype=np.uint8)
        arr[0, 0] = (240, 240, 240)   # exact bg
        arr[0, 1] = (255, 255, 255)   # +15 → within tol 24
        arr[0, 2] = (200, 240, 240)   # -40 on one channel → outside tol
        mask = uniform_mask(arr, np.array([240, 240, 240]), tolerance=24)
        self.assertTrue(mask[0, 0])
        self.assertTrue(mask[0, 1])
        self.assertFalse(mask[0, 2])


class TestLargestComponent(unittest.TestCase):
    def test_full_true(self):
        mask = np.ones((10, 10), dtype=bool)
        self.assertAlmostEqual(largest_component_fraction(mask), 1.0)

    def test_two_blobs_takes_larger(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[0:6, :] = True     # 60 px connected band
        mask[8:10, 0:2] = True  # 4 px separate blob
        self.assertAlmostEqual(largest_component_fraction(mask), 0.60)

    def test_4_connectivity_not_diagonal(self):
        mask = np.zeros((3, 3), dtype=bool)
        mask[0, 0] = True
        mask[1, 1] = True   # diagonal — must NOT join
        self.assertAlmostEqual(largest_component_fraction(mask), 1 / 9)

    def test_empty_mask(self):
        self.assertAlmostEqual(largest_component_fraction(np.zeros((5, 5), dtype=bool)), 0.0)


class TestEmptyFraction(unittest.TestCase):
    def test_all_uniform_is_full(self):
        arr = np.full((100, 100, 3), 200, dtype=np.uint8)
        self.assertAlmostEqual(empty_fraction(arr), 1.0)

    def test_split_image(self):
        arr = np.zeros((100, 100, 3), dtype=np.uint8)
        arr[:60, :] = (255, 255, 255)   # 60% white (dominant)
        arr[60:, :] = (0, 0, 0)         # 40% black
        # largest near-white contiguous region ≈ 0.60
        self.assertAlmostEqual(empty_fraction(arr), 0.60, places=1)


class TestTextHeightFraction(unittest.TestCase):
    def test_union_of_intervals(self):
        els = [
            {"id": "headline", "bbox_pct": [5, 10, 90, 15]},  # 10..25
            {"id": "body", "bbox_pct": [5, 20, 90, 10]},      # 20..30  (overlaps)
        ]
        self.assertAlmostEqual(text_height_fraction(els), 0.20)  # union 10..30 = 20

    def test_excludes_own_fill(self):
        els = [
            {"id": "headline", "bbox_pct": [5, 10, 90, 15]},          # counts
            {"id": "body-pill", "type": "pill", "bbox_pct": [5, 40, 90, 30]},  # excluded
            {"id": "brand-logo", "bbox_pct": [80, 5, 15, 8]},        # excluded by 'logo' hint
        ]
        self.assertAlmostEqual(text_height_fraction(els), 0.15)

    def test_no_elements(self):
        self.assertAlmostEqual(text_height_fraction([]), 0.0)


class TestEvaluate(unittest.TestCase):
    def test_fail_when_both_conditions(self):
        res = evaluate(empty_frac=0.60, text_frac=0.20)
        self.assertEqual(res["verdict"], "FAIL")

    def test_ok_when_text_band_tall(self):
        res = evaluate(empty_frac=0.60, text_frac=0.30)
        self.assertEqual(res["verdict"], "OK")

    def test_ok_when_empty_small(self):
        res = evaluate(empty_frac=0.40, text_frac=0.20)
        self.assertEqual(res["verdict"], "OK")

    def test_warn_when_no_measurements_and_empty_large(self):
        res = evaluate(empty_frac=0.60, text_frac=None)
        self.assertEqual(res["verdict"], "WARN")

    def test_ok_when_no_measurements_and_empty_small(self):
        res = evaluate(empty_frac=0.40, text_frac=None)
        self.assertEqual(res["verdict"], "OK")


class TestAdvisoryForms(unittest.TestCase):
    """C / B1 forms: baked AI text is not measurable here → would-be FAIL/WARN downgraded."""

    def test_fail_downgraded_to_advisory_for_C(self):
        res = evaluate(empty_frac=0.60, text_frac=0.20, form="C")
        self.assertEqual(res["verdict"], "ADVISORY")
        self.assertIn("advisory", res["reason"].lower())

    def test_fail_downgraded_to_advisory_for_B1_case_insensitive(self):
        res = evaluate(empty_frac=0.60, text_frac=0.20, form="b1")
        self.assertEqual(res["verdict"], "ADVISORY")

    def test_warn_downgraded_to_advisory_for_C_no_measurements(self):
        res = evaluate(empty_frac=0.60, text_frac=None, form="C")
        self.assertEqual(res["verdict"], "ADVISORY")

    def test_advisory_form_still_ok_when_within_bounds(self):
        # C form but no dead space → still OK, not advisory noise
        res = evaluate(empty_frac=0.40, text_frac=0.30, form="C")
        self.assertEqual(res["verdict"], "OK")

    def test_non_advisory_form_still_hard_fails(self):
        res = evaluate(empty_frac=0.60, text_frac=0.20, form="B2")
        self.assertEqual(res["verdict"], "FAIL")

    def test_unknown_form_keeps_blocking_behaviour(self):
        # form=None → original behaviour preserved
        res = evaluate(empty_frac=0.60, text_frac=0.20, form=None)
        self.assertEqual(res["verdict"], "FAIL")
        res_warn = evaluate(empty_frac=0.60, text_frac=None, form=None)
        self.assertEqual(res_warn["verdict"], "WARN")


class TestReasonStringsAsciiSafe(unittest.TestCase):
    """The reason glyphs must be cp1252-encodable so a Windows console never crashes."""

    def test_fail_reason_encodes_to_cp1252(self):
        res = evaluate(empty_frac=0.60, text_frac=0.20)
        # would raise UnicodeEncodeError if a non-cp1252 glyph (e.g. arrow) were present
        res["reason"].encode("cp1252")

    def test_advisory_reason_encodes_to_cp1252(self):
        res = evaluate(empty_frac=0.60, text_frac=0.20, form="C")
        res["reason"].encode("cp1252")


if __name__ == "__main__":
    unittest.main()

# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for check_craft_lint.py — the type-craft lint above the overflow gate.

Tests the MEASUREMENT (deterministic CSS reads + the five craft-rule thresholds), not the
aesthetic — per the AIOS-190 posture "test the measurement, not the aesthetic". Each test
mirrors a confirmed RC-B defect CLASS (general, not slug-bound) and a clean counter-example.

Run:
    uv run test_check_craft_lint.py
    or: python test_check_craft_lint.py
"""
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_craft_lint import (  # noqa: E402
    evaluate,
    parse_cqw,
    parse_line_height,
    parse_letter_spacing_em,
    classify_role,
    count_lines,
    has_condensed_face,
)


def _doc(style="", body=""):
    return f"<html><head><style>{style}</style></head><body>{body}</body></html>"


class TestParsers(unittest.TestCase):
    def test_parse_cqw(self):
        self.assertEqual(parse_cqw("font-size:12cqw;", "font-size"), 12.0)
        self.assertEqual(parse_cqw("font-size: 3.2cqw", "font-size"), 3.2)
        self.assertIsNone(parse_cqw("font-size:16px", "font-size"))  # px is off-contract

    def test_parse_line_height(self):
        self.assertEqual(parse_line_height("line-height:0.95;"), 0.95)
        self.assertEqual(parse_line_height("line-height: 1.4"), 1.4)
        self.assertIsNone(parse_line_height("color:red"))

    def test_parse_letter_spacing(self):
        self.assertEqual(parse_letter_spacing_em("letter-spacing:-0.02em;"), -0.02)
        self.assertEqual(parse_letter_spacing_em("letter-spacing: 0.1em"), 0.1)
        self.assertIsNone(parse_letter_spacing_em("letter-spacing:2px"))

    def test_classify_role(self):
        self.assertEqual(classify_role("headline display"), "display")
        self.assertEqual(classify_role("body copy"), "body")
        self.assertIsNone(classify_role("footer pagination"))  # chrome → ignored
        # subtitle is body even though it could read as chrome-ish
        self.assertEqual(classify_role("subtitle"), "body")

    def test_count_lines(self):
        self.assertEqual(count_lines("one word"), 1)
        self.assertEqual(count_lines("line<br>two<br>three"), 3)

    def test_condensed_face(self):
        self.assertTrue(has_condensed_face("font-family:'Anton'", "<html></html>"))
        self.assertFalse(has_condensed_face("font-family:'Inter'", "<html></html>"))


class TestRatio(unittest.TestCase):
    def test_footnote_body_flagged(self):
        # statement-textural class: 19cqw display over 3.2cqw body = ~6:1 → footnote body.
        html = _doc(body=(
            '<div class="headline display" style="font-size:19cqw;line-height:0.95">H</div>'
            '<div class="body" style="font-size:3.2cqw;line-height:1.35">b</div>'))
        res = evaluate(html)
        self.assertFalse(res["ok"])
        self.assertTrue(any("ratio" in f and "footnote" in f for f in res["findings"]))

    def test_healthy_ratio_clean(self):
        html = _doc(body=(
            '<div class="headline display" style="font-size:14cqw;line-height:1.0">H</div>'
            '<div class="body" style="font-size:4.5cqw;line-height:1.35">b</div>'))
        res = evaluate(html)
        self.assertTrue(res["ok"], res["findings"])

    def test_flat_hierarchy_flagged(self):
        html = _doc(body=(
            '<div class="display" style="font-size:9cqw">H</div>'
            '<div class="body" style="font-size:6cqw;line-height:1.35">b</div>'))
        res = evaluate(html)
        self.assertFalse(res["ok"])
        self.assertTrue(any("flat hierarchy" in f for f in res["findings"]))


class TestFloors(unittest.TestCase):
    def test_body_below_floor(self):
        html = _doc(body=(
            '<div class="display" style="font-size:12cqw">H</div>'
            '<div class="body" style="font-size:3.0cqw;line-height:1.35">b</div>'))
        res = evaluate(html)
        self.assertTrue(any("floor" in f and "body" in f for f in res["findings"]))

    def test_display_below_floor(self):
        html = _doc(body='<div class="display" style="font-size:6cqw">H</div>')
        res = evaluate(html)
        self.assertTrue(any("display" in f and "floor" in f for f in res["findings"]))


class TestLineHeight(unittest.TestCase):
    def test_airy_body_flagged(self):
        # the "espaçamentos muito altos" case (numbered-photo loose spacing).
        html = _doc(body=(
            '<div class="display" style="font-size:12cqw;line-height:1.0">H</div>'
            '<div class="body" style="font-size:4.5cqw;line-height:1.9">b</div>'))
        res = evaluate(html)
        self.assertTrue(any("line-height" in f and "airy" in f for f in res["findings"]))

    def test_airy_display_flagged(self):
        html = _doc(body='<div class="display" style="font-size:12cqw;line-height:1.4">H</div>')
        res = evaluate(html)
        self.assertTrue(any("display line-height" in f for f in res["findings"]))


class TestCondensedTracking(unittest.TestCase):
    def test_negative_tracking_multiline_condensed_flagged(self):
        # numbered-fullbleed: Anton + letter-spacing:-0.02em + line-height:0.95, multi-line.
        html = _doc(
            style="@font-face{font-family:'Anton';src:url(x)}",
            body=('<div class="display" style="font-family:Anton;font-size:14cqw;'
                  'letter-spacing:-0.02em;line-height:0.95">A<br>B</div>'))
        res = evaluate(html)
        self.assertTrue(any("letter-spacing" in f and "condensed" in f for f in res["findings"]))
        self.assertTrue(any("line-height" in f and "condensed" in f for f in res["findings"]))

    def test_single_line_condensed_negative_tracking_ok(self):
        # one line condensed with negative tracking is the legit poster-tight move (§3) — clean.
        html = _doc(
            style="@font-face{font-family:'Anton';src:url(x)}",
            body=('<div class="display" style="font-family:Anton;font-size:14cqw;'
                  'letter-spacing:-0.02em;line-height:1.0">ONELINE</div>'))
        res = evaluate(html)
        self.assertFalse(any("condensed" in f for f in res["findings"]), res["findings"])


class TestTallStack(unittest.TestCase):
    def test_uncapped_tall_display_flagged(self):
        # hero-statement: 4-line display stack, no max-height → runs into the image subject.
        html = _doc(body=('<div class="display" style="font-size:11cqw;line-height:1.0">'
                          'one<br>two<br>three<br>four</div>'))
        res = evaluate(html)
        self.assertTrue(any("stack" in f and "max-height" in f for f in res["findings"]))

    def test_capped_tall_display_ok(self):
        html = _doc(body=('<div class="display" style="font-size:11cqw;line-height:1.0;'
                          'max-height:60cqw">one<br>two<br>three<br>four</div>'))
        res = evaluate(html)
        self.assertFalse(any("stack" in f for f in res["findings"]), res["findings"])


if __name__ == "__main__":
    unittest.main()

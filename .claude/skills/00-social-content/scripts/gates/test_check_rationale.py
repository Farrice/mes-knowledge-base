# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for check_rationale.py — Check A, the rationale gatekeeper (AIOS-190 W2).

Tests presence + completeness (deterministic parsing), NOT reasoning quality (out of scope
for the gate — that lives in the gabarito + by-eye golden set).

Run:
    uv run test_check_rationale.py
    or: python test_check_rationale.py
"""
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_rationale import (  # noqa: E402
    strip_marker,
    parse_sections,
    find_section,
    ambiguity_is_filler,
    evaluate,
)

COMPLETE = """
# rationale — ref-02

## ① Form + tree-path-with-why
form: B1 — surface in-scene.
Q1 solid color? no (photographic desk scene).
Q2 blank surface inside the scene? yes (the CRT screen holds the headline) -> B1.

## ② Per-block breakdown
- Headline (on screen) · AI-integrated · inside the monitor glass; HTML overlay misses the in-scene fit.
- Sticky notes · AI-integrated · handwritten marker on angled post-its; exotic font + perspective fail isolability.

## ③ Pipeline
edit_mode: total-recompose. when_ai_runs: every post. extraction: AI generates the desk/CRT scene with the headline on the screen.

## ④ Ambiguity (examined)
The sticky notes are SATELLITE in-scene surfaces beyond the primary CRT screen. Still B1 (all route to AI),
but considered routing the stickies to HTML — rejected because the marker font + perspective fail isolability.
"""


class TestStripMarker(unittest.TestCase):
    def test_circled_digit(self):
        self.assertEqual(strip_marker("① Form + tree-path-with-why"), "Form + tree-path-with-why")

    def test_numbered(self):
        self.assertEqual(strip_marker("1. Pipeline"), "Pipeline")
        self.assertEqual(strip_marker("4) Ambiguity (examined)"), "Ambiguity (examined)")

    def test_plain(self):
        self.assertEqual(strip_marker("Per-block breakdown"), "Per-block breakdown")


class TestParseSections(unittest.TestCase):
    def test_finds_four(self):
        secs = parse_sections(COMPLETE)
        headers = [h for h, _ in secs]
        self.assertTrue(any("form" in h for h in headers))
        self.assertTrue(any("per-block" in h for h in headers))
        self.assertTrue(any("pipeline" in h for h in headers))
        self.assertTrue(any("ambiguity" in h for h in headers))

    def test_body_captured(self):
        secs = parse_sections(COMPLETE)
        body = find_section(secs, ("pipeline",))
        self.assertIn("total-recompose", body)


class TestAmbiguityFiller(unittest.TestCase):
    def test_na_is_filler(self):
        self.assertTrue(ambiguity_is_filler("n/a"))
        self.assertTrue(ambiguity_is_filler("None"))
        self.assertTrue(ambiguity_is_filler("  -  "))
        self.assertTrue(ambiguity_is_filler(""))

    def test_no_ambiguity_bare_is_filler(self):
        self.assertTrue(ambiguity_is_filler("no ambiguity"))

    def test_ruled_out_with_reason_is_valid(self):
        # "no ambiguity BECAUSE ..." has real content -> NOT filler.
        self.assertFalse(ambiguity_is_filler(
            "No ambiguity — ruled out B1 because there's no blank in-scene surface."))

    def test_real_reasoning_is_valid(self):
        self.assertFalse(ambiguity_is_filler("Considered B1 but the screen is the hero, not a content surface."))


class TestEvaluate(unittest.TestCase):
    def test_complete_passes(self):
        res = evaluate(COMPLETE)
        self.assertTrue(res["ok"], res["reason"])

    def test_missing_ambiguity_blocks(self):
        text = COMPLETE.split("## ④")[0]
        res = evaluate(text)
        self.assertFalse(res["ok"])
        self.assertIn("ambiguity", res["reason"].lower())

    def test_empty_ambiguity_blocks(self):
        text = COMPLETE.split("## ④")[0] + "## ④ Ambiguity (examined)\n\n"
        res = evaluate(text)
        self.assertFalse(res["ok"])

    def test_filler_ambiguity_blocks(self):
        text = COMPLETE.split("## ④")[0] + "## ④ Ambiguity (examined)\nn/a\n"
        res = evaluate(text)
        self.assertFalse(res["ok"])
        self.assertTrue(res["ambiguity_filler"])

    def test_ruled_out_ambiguity_passes(self):
        text = (COMPLETE.split("## ④")[0]
                + "## ④ Ambiguity (examined)\nNo ambiguity — ruled out B1 because there is "
                  "no blank in-scene surface; the texture is the bg, not a content surface.\n")
        res = evaluate(text)
        self.assertTrue(res["ok"], res["reason"])

    def test_missing_pipeline_blocks(self):
        text = COMPLETE.replace("## ③ Pipeline", "## ③ Pipln-typo-not-matched")
        res = evaluate(text)
        self.assertFalse(res["ok"])
        self.assertIn("pipeline", res["reason"].lower())


if __name__ == "__main__":
    unittest.main()

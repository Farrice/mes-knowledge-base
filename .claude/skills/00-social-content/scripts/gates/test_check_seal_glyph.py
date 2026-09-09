# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0"]
# ///
"""Unit tests for check_seal_glyph.py — SEAL-GLYPH-PRESENT (a contracted seal glyph must render).

Tests the deterministic glyph-asset-resolves read + the region parse + the pixel read, on
synthetic inputs (no hardcoded slug). Run: uv run test_check_seal_glyph.py
"""
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_seal_glyph import (  # noqa: E402
    parse_seal_regions,
    glyph_asset_resolves,
    glyph_present,
    evaluate,
    _substitute_slots,
)

# A badge with a shell + a glyph img whose src is a {{SLOT}} placeholder.
HTML_BADGE = '''
<div class="badge-wrap" data-slot="BRAND_LOGO"
     style="left:68%; top:14%; width:14%; height:8%;">
  <img class="badge-starburst" src="assets/sunburst.svg" alt="">
  <img class="badge-logo" data-slot="BRAND_LOGO" src="{{BRAND_LOGO_PATH}}" alt="Claude">
</div>
'''
# A plain decorative shape with NO glyph contracted (and no rationale glyph) — not judged.
HTML_DECORATIVE = '''
<div class="accent-burst" style="left:80%; top:5%; width:8%; height:6%;"></div>
'''
RATIONALE_GLYPH = "## ② Per-block breakdown\n**Claude starburst badge** · the Claude mark inside the seal\n"
RATIONALE_NONE = "## ② Per-block breakdown\n**A plain accent shape** · ornamental only\n"


class SubstituteTests(unittest.TestCase):
    def test_substitutes_known_slot(self):
        self.assertEqual(_substitute_slots("{{BRAND_LOGO_PATH}}", {"BRAND_LOGO_PATH": "a/b.svg"}),
                         "a/b.svg")

    def test_leaves_unknown_slot(self):
        self.assertEqual(_substitute_slots("{{X}}", {}), "{{X}}")


class RegionParseTests(unittest.TestCase):
    def test_finds_badge_with_glyph_child_and_resolves_src_from_data(self):
        regs = parse_seal_regions(HTML_BADGE, "", {"BRAND_LOGO_PATH": "assets/claude.svg"})
        self.assertEqual(len(regs), 1)
        self.assertEqual(regs[0]["glyph_src"], "assets/claude.svg")  # shell skipped, glyph picked

    def test_shell_src_not_picked_as_glyph(self):
        regs = parse_seal_regions(HTML_BADGE, "", {"BRAND_LOGO_PATH": "assets/claude.svg"})
        self.assertNotIn("sunburst", regs[0]["glyph_src"])

    def test_decorative_shape_with_no_glyph_is_skipped(self):
        regs = parse_seal_regions(HTML_DECORATIVE, RATIONALE_NONE, {})
        self.assertEqual(regs, [])

    def test_rationale_glyph_declaration_contracts_even_without_child_img(self):
        # A seal selector + geometry, no nested img, but the rationale declares a glyph in it.
        html = '<div class="seal" style="left:5%; top:5%; width:10%; height:10%;"></div>'
        regs = parse_seal_regions(html, RATIONALE_GLYPH, {})
        self.assertEqual(len(regs), 1)


class GlyphResolveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        (self.dir / "assets").mkdir()
        (self.dir / "assets" / "claude.svg").write_text("<svg/>", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_existing_relative_path_resolves(self):
        ok, _ = glyph_asset_resolves("assets/claude.svg", self.dir)
        self.assertTrue(ok)

    def test_missing_path_does_not_resolve(self):  # the run-08 root cause
        ok, _ = glyph_asset_resolves(".claude/skills/x/claude.svg", self.dir)
        self.assertFalse(ok)

    def test_unresolved_placeholder_does_not_resolve(self):
        ok, _ = glyph_asset_resolves("{{BRAND_LOGO_PATH}}", self.dir)
        self.assertFalse(ok)

    def test_remote_url_is_treated_resolvable(self):
        ok, _ = glyph_asset_resolves("https://x/y.svg", self.dir)
        self.assertTrue(ok)

    def test_no_src_is_resolvable(self):
        ok, _ = glyph_asset_resolves(None, self.dir)
        self.assertTrue(ok)


class GlyphPixelTests(unittest.TestCase):
    def test_solid_fill_reads_absent(self):
        flat = Image.new("RGB", (64, 64), (200, 40, 40))
        self.assertFalse(glyph_present(flat)["present"])

    def test_glyph_with_edges_reads_present(self):
        arr = np.full((64, 64, 3), 200, np.uint8)
        arr[20:44, 28:36] = 10          # a dark vertical stroke (a glyph mark)
        arr[30:34, 18:46] = 10          # a crossbar
        self.assertTrue(glyph_present(Image.fromarray(arr))["present"])


class EvaluateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        (self.dir / "assets").mkdir()
        (self.dir / "assets" / "claude.svg").write_text("<svg/>", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_broken_glyph_path_fails(self):  # overlay-cover shape
        res = evaluate(HTML_BADGE, "", None, self.dir,
                       {"BRAND_LOGO_PATH": ".claude/skills/x/claude.svg"})
        self.assertFalse(res["ok"])
        self.assertTrue(any("broken glyph path" in f for f in res["flags"]))

    def test_resolving_glyph_path_passes(self):  # the fixed case
        res = evaluate(HTML_BADGE, "", None, self.dir,
                       {"BRAND_LOGO_PATH": "assets/claude.svg"})
        self.assertTrue(res["ok"])

    def test_no_seal_region_is_clean_pass(self):
        res = evaluate(HTML_DECORATIVE, RATIONALE_NONE, None, self.dir, {})
        self.assertTrue(res["ok"])
        self.assertEqual(res["regions_found"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

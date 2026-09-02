# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for check_palette_tokens.py — Check E, the palette-token (ref-palette leak) gate.

Tests the deterministic hex-vs-brand-token read (no hardcoded brand hue — the brand palette comes
from a tokens dict the test supplies), NOT colour taste.

Run:
    uv run test_check_palette_tokens.py
    or: python test_check_palette_tokens.py
"""
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_palette_tokens import (  # noqa: E402
    expand_hex,
    load_brand_hexes,
    is_brand_token,
    find_leaks,
    evaluate,
)

# A 3-color brand (ink + paper + coral) like the testbed Agentic Academy tokens.json.
BRAND_TOKENS = {
    "colors": {
        "primary": "#1f1816",   # ink
        "accent": "#d05344",    # coral
        "bg_light": "#efeeee",  # paper
        "bg_kraft": "#e8e2d6",
        "text_on_dark": "#f2f0eb",
    }
}


class TestExpandHex(unittest.TestCase):
    def test_long(self):
        self.assertEqual(expand_hex("#d05344"), (0xd0, 0x53, 0x44))

    def test_short(self):
        self.assertEqual(expand_hex("#fff"), (255, 255, 255))

    def test_alpha_dropped(self):
        self.assertEqual(expand_hex("#d05344ff"), (0xd0, 0x53, 0x44))

    def test_bad(self):
        self.assertIsNone(expand_hex("#xyz"))


class TestLoadBrandHexes(unittest.TestCase):
    def test_collects_all(self):
        brand = load_brand_hexes(BRAND_TOKENS)
        self.assertIn((0xd0, 0x53, 0x44), brand)   # coral
        self.assertIn((0x1f, 0x18, 0x16), brand)   # ink
        self.assertIn((0xef, 0xee, 0xee), brand)   # paper

    def test_suffix_form(self):
        # ai-image-style.md style: "#E2473D (accent)"
        brand = load_brand_hexes({"colors": ["#E2473D (accent)", "#FFFFFF (bg)"]})
        self.assertIn((0xe2, 0x47, 0x3d), brand)
        self.assertIn((255, 255, 255), brand)


class TestIsBrandToken(unittest.TestCase):
    def test_exact(self):
        brand = load_brand_hexes(BRAND_TOKENS)
        self.assertTrue(is_brand_token((0xd0, 0x53, 0x44), brand, 6))

    def test_within_tolerance(self):
        brand = load_brand_hexes(BRAND_TOKENS)
        self.assertTrue(is_brand_token((0xd2, 0x55, 0x46), brand, 6))  # coral +2/channel

    def test_off_token(self):
        brand = load_brand_hexes(BRAND_TOKENS)
        self.assertFalse(is_brand_token((0xb5, 0xe8, 0x53), brand, 6))  # the ref's lime green


class TestFindLeaks(unittest.TestCase):
    def setUp(self):
        self.brand = load_brand_hexes(BRAND_TOKENS)

    def test_ref_green_is_a_leak(self):
        # the run-08 list-on-object miss: ref lime-green kept as palette
        text = "palette: keep the ref's lime accent #b5e853 as the list bullet colour"
        self.assertEqual(find_leaks(text, self.brand, 6), ["#b5e853"])

    def test_brand_hex_is_clean(self):
        # a literal brand hex (still discouraged, but it IS a token — not a leak)
        text = "the accent maps to coral #d05344"
        self.assertEqual(find_leaks(text, self.brand, 6), [])

    def test_var_token_authoring_is_clean(self):
        # the RIGHT way — no literal hex at all
        text = "headline fill: var(--brand-ink); accent: var(--brand-accent)"
        self.assertEqual(find_leaks(text, self.brand, 6), [])

    def test_white_fill_leak(self):
        # fullbleed-photo-cover headline `fill: white` copied as a literal #ffffff,
        # not a brand token (brand has no pure white among ink/paper/coral)
        text = "the headline is set fill:#ffffff over the bright dojo floor"
        self.assertEqual(find_leaks(text, self.brand, 6), ["#ffffff"])


class TestEvaluate(unittest.TestCase):
    def setUp(self):
        self.brand = load_brand_hexes(BRAND_TOKENS)

    def test_clean_passes(self):
        sources = {
            "rationale.md": "accent maps to var(--brand-accent); headline var(--brand-ink)",
            "template.html": "color: var(--brand-text-on-light);",
        }
        res = evaluate(sources, self.brand, 6)
        self.assertTrue(res["ok"], res["reason"])
        self.assertEqual(res["leaks"], [])

    def test_leak_flagged_with_source(self):
        sources = {
            "rationale.md": "PALETTE: keep #b5e853 (the ref's lime) as the list colour",
            "template.html": "color: var(--brand-accent);",
        }
        res = evaluate(sources, self.brand, 6)
        self.assertFalse(res["ok"])
        self.assertIn("#b5e853", res["leaks"])
        self.assertIn("rationale.md", res["per_source"])
        self.assertNotIn("template.html", res["per_source"])

    def test_multiple_sources(self):
        sources = {
            "rationale.md": "ref accent #b5e853",
            "template.html": "fill:#ffffff",
        }
        res = evaluate(sources, self.brand, 6)
        self.assertFalse(res["ok"])
        self.assertEqual(set(res["leaks"]), {"#b5e853", "#ffffff"})


if __name__ == "__main__":
    unittest.main()

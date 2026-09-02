# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Tests for _inline_tinted_svgs() in render_template.py — the run-08 overlay-cover
SVG-tint fix (RC-C, cause side).

An SVG referenced via <img src="…svg"> using fill="currentColor" is an isolated
document, so the host `color: var(--brand-accent)` never cascades in and the glyph
paints black. The fix splices the SVG markup inline (carrying the <img>'s class/style/id)
so currentColor resolves against the cascaded color. Slug-agnostic: keys ONLY on the
SVG using `currentColor`; baked-colour SVGs stay <img>.

Runs via: uv run test_inline_tinted_svgs.py
          or: python test_inline_tinted_svgs.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from render_template import _inline_tinted_svgs  # noqa: E402


CURRENTCOLOR_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="currentColor">'
    '<circle cx="50" cy="50" r="40"/></svg>'
)
BAKED_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="#D97757">'
    '<circle cx="50" cy="50" r="40"/></svg>'
)


class InlineTintedSvgs(unittest.TestCase):
    def test_currentcolor_svg_is_inlined_with_tint_carried(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "assets").mkdir()
            (root / "assets" / "sunburst.svg").write_text(CURRENTCOLOR_SVG, encoding="utf-8")
            html = (
                '<img class="badge-starburst" '
                'style="color: var(--brand-accent);" src="assets/sunburst.svg" alt="">'
            )
            out = _inline_tinted_svgs(html, root)
            # The <img> is gone, replaced by inline <svg> carrying the tint hooks.
            self.assertNotIn("<img", out)
            self.assertIn("<svg", out)
            self.assertIn('fill="currentColor"', out)
            self.assertIn("badge-starburst", out)
            self.assertIn("color: var(--brand-accent)", out)

    def test_baked_colour_svg_left_as_img(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "assets").mkdir()
            (root / "assets" / "logo.svg").write_text(BAKED_SVG, encoding="utf-8")
            html = '<img class="badge-logo" src="assets/logo.svg" alt="Claude">'
            out = _inline_tinted_svgs(html, root)
            # Baked-colour mark must remain an <img> (no tint contract to satisfy).
            self.assertIn("<img", out)
            self.assertNotIn("<svg", out)

    def test_http_and_data_and_slot_srcs_untouched(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            html = (
                '<img src="https://x/y.svg">'
                '<img src="data:image/svg+xml;base64,AAA">'
                '<img src="{{BRAND_LOGO_PATH}}">'
            )
            out = _inline_tinted_svgs(html, root)
            self.assertEqual(out, html)

    def test_missing_file_untouched(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            html = '<img class="x" src="assets/nope.svg">'
            out = _inline_tinted_svgs(html, root)
            self.assertEqual(out, html)


if __name__ == "__main__":
    unittest.main()

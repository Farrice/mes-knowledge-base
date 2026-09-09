# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""test_roundtrip_parity.py -- automated additive-parity check for RNDR-05.

Validates at the HTML-string level (the deterministic precursor to pixel parity):
  (a) baseline render (tweaks=None) produces the same filled HTML as a render
      with an empty per-slide tweaks dict (tweaks={"slide-01": {}}) -- RNDR-05.
  (b) _build_tweaks_css({}) returns "" and no <style> block is injected when
      slide tweaks are empty.
  (c) a NON-empty tweak (e.g. HERO x=5) DOES change the HTML -- proves the
      override path is actually wired (guards against a trivially-passing test).

Stdlib only -- no Playwright, no external dependencies.
Run: uv run test_roundtrip_parity.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

# ── Cross-skill sys.path injection (REQUIRED) ──────────────────────────────
# This file lives in 00-social-content/scripts/content-studio/.
# Correct layout:
#   systems/00-social-content/skills/00-social-content/scripts/content-studio/  <- __file__
#   systems/00-social-content/skills/viz-image-gen/scripts/                     <- target
# So:
#   Path(__file__).parent          = content-studio
#   .parent                        = scripts
#   .parent                        = 00-social-content
#   .parent                        = skills
#   / 'viz-image-gen' / 'scripts'  = viz-image-gen/scripts
RENDER_SCRIPTS = Path(__file__).resolve().parent.parent.parent.parent / "viz-image-gen" / "scripts"
sys.path.insert(0, str(RENDER_SCRIPTS))

from render_template import (  # noqa: E402
    _build_tweaks_css,
    _materialize_texture,
    _tag_root_bg as _bake_tag_root_bg,
    apply_tweaks,
    fill,
)
from preview_editor import _tag_root_bg as _editor_tag_root_bg  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers -- build minimal in-memory HTML for testing
# ---------------------------------------------------------------------------

_TEMPLATE_HTML = """\
<!DOCTYPE html>
<html>
<head>
<title>Test slide</title>
</head>
<body>
<div class="slide" style="width:1080px;height:1350px;position:relative;">
  <div data-slot="HERO" style="position:absolute;left:10%;top:20%;width:80%;height:30%;">
    {{HERO}}
  </div>
  <div data-slot="BODY_TEXT" style="position:absolute;left:10%;top:55%;width:80%;height:20%;">
    {{BODY_TEXT}}
  </div>
</div>
</body>
</html>
"""

_SAMPLE_DATA = {
    "HERO": "Sample headline text",
    "BODY_TEXT": "Sample body copy here.",
    "BRAND_TOKENS_CSS": "",
}


def _render_filled(tweaks: dict | None, tweaks_slide: str | None) -> str:
    """Reproduce the tweaks injection + fill() pipeline from render_template.render().

    This mirrors lines 1101-1115 of render_template.py exactly:
      1. if tweaks and _slide_tweaks: apply text overrides + inject CSS.
      2. fill() with processed + BRAND_TOKENS_CSS.

    No Playwright -- returns the *filled HTML string* only.
    """
    raw_html = _TEMPLATE_HTML
    processed = dict(_SAMPLE_DATA)  # fresh copy each call

    # Derive _slide_tweaks the same way render() does (lines 970-971).
    slide_id = tweaks_slide or "slide-01"
    _slide_tweaks: dict = (tweaks or {}).get(slide_id, {}) if tweaks else {}

    # Mirror lines 1105-1113 of render_template.py.
    if tweaks and _slide_tweaks:
        apply_tweaks(processed, _slide_tweaks)
        _tweaks_css = _build_tweaks_css(_slide_tweaks)
        if _tweaks_css:
            _style_tag = f"<style>{_tweaks_css}</style>"
            if "</head>" in raw_html:
                raw_html = raw_html.replace("</head>", _style_tag + "</head>", 1)
            else:
                raw_html = _style_tag + raw_html

    return fill(raw_html, processed)


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

class TestAdditiveParity(unittest.TestCase):
    """RNDR-05: empty tweaks must produce output identical to no tweaks."""

    def test_baseline_equals_empty_slide_tweaks(self):
        """Baseline (tweaks=None) and empty per-slide tweaks produce identical HTML."""
        baseline = _render_filled(tweaks=None, tweaks_slide=None)
        empty_tweaks = _render_filled(
            tweaks={"slide-01": {}}, tweaks_slide="slide-01"
        )
        self.assertEqual(
            baseline,
            empty_tweaks,
            "RNDR-05 VIOLATED: empty tweaks produced different HTML than baseline.",
        )

    def test_empty_tweaks_css_is_empty_string(self):
        """_build_tweaks_css({}) returns '' -- no CSS emitted for empty tweaks."""
        css = _build_tweaks_css({})
        self.assertEqual(css, "", "_build_tweaks_css({}) must return empty string.")

    def test_no_style_tag_injected_for_empty_tweaks(self):
        """No <style> block is injected when slide tweaks are empty."""
        # Count <style> tags in baseline
        baseline = _render_filled(tweaks=None, tweaks_slide=None)
        empty_tweaks = _render_filled(
            tweaks={"slide-01": {}}, tweaks_slide="slide-01"
        )
        # Neither should have a tweaks-injected <style> block
        self.assertEqual(
            baseline.count("<style>"),
            empty_tweaks.count("<style>"),
            "Empty tweaks injected a <style> block that baseline does not have.",
        )


class TestOverridePathIsLive(unittest.TestCase):
    """Sanity guard: non-empty tweaks MUST actually change the output.

    If this test fails, the override path is not wired and the parity test
    above would pass trivially (doing nothing always looks identical).
    """

    def test_hero_x_tweak_changes_html(self):
        """A HERO x=5 tweak injects a CSS rule with left:5% -- output differs from baseline."""
        baseline = _render_filled(tweaks=None, tweaks_slide=None)
        tweaked = _render_filled(
            tweaks={"slide-01": {"HERO": {"x": 5}}},
            tweaks_slide="slide-01",
        )
        self.assertNotEqual(
            baseline,
            tweaked,
            "Override path NOT live: non-empty tweak produced identical HTML.",
        )
        self.assertIn(
            "translate: 54px",
            tweaked,
            "Expected 'translate: 54px' (x=5% of 1080) CSS rule in tweaked output.",
        )

    def test_hero_text_tweak_changes_filled_value(self):
        """A HERO text tweak replaces the slot value -- output differs from baseline."""
        baseline = _render_filled(tweaks=None, tweaks_slide=None)
        tweaked = _render_filled(
            tweaks={"slide-01": {"HERO": {"text": "OVERRIDDEN HEADLINE"}}},
            tweaks_slide="slide-01",
        )
        self.assertNotEqual(
            baseline,
            tweaked,
            "Text tweak did not change the filled HTML.",
        )
        self.assertIn(
            "OVERRIDDEN HEADLINE",
            tweaked,
            "Tweaked text value not found in output HTML.",
        )
        self.assertNotIn(
            "OVERRIDDEN HEADLINE",
            baseline,
            "Overridden text unexpectedly found in baseline output.",
        )


class TestBuildTweaksCssExtras(unittest.TestCase):
    """Additional _build_tweaks_css contracts relevant to parity."""

    def test_text_only_slot_produces_no_css_rule(self):
        """A slot with only 'text' has no CSS props -- empty string returned."""
        result = _build_tweaks_css({"HERO": {"text": "hello"}})
        self.assertEqual(result, "")

    def test_nonempty_css_props_produce_rule(self):
        """CSS props (x, y, fontSize, opacity, tilt) produce a [data-slot] rule."""
        result = _build_tweaks_css({"HERO": {"x": 10, "y": 20, "opacity": 0.8}})
        self.assertIn('[data-slot="HERO"]', result)
        self.assertIn("translate: 108px 270px", result)  # x=10,y=20 of 1080x1350
        self.assertIn("opacity: 0.8", result)

    def test_zorder_bakes_matching_live(self):
        """FASE 5 §1 (live WYSIWYG z-order): a layer's `z` tweak bakes to position:relative
        + z-index, exactly what the editor applies live via applyToSlide('z'), so a layer
        dragged above another overlaps the SAME way in preview and PNG (RNDR-04)."""
        result = _build_tweaks_css({"LAYER_00": {"z": 3}, "LAYER_01": {"z": 1}})
        self.assertIn('[data-slot="LAYER_00"]', result)
        self.assertIn("z-index: 3", result)
        self.assertIn("z-index: 1", result)
        self.assertIn("position: relative", result)


class TestTextureOverlay(unittest.TestCase):
    """Addendum 5 — per-slide post-production texture overlay (RNDR-04 parity).

    The bake injects the SAME overlay element the editor renders client-side from the
    same data URI / blend / intensity, so preview == baked PNG by construction."""

    _URI = "data:image/png;base64,QUJD"

    def test_reserved_texture_key_emits_no_css_rule(self):
        # __texture is non-slot metadata — must NOT become a [data-slot] CSS rule.
        css = _build_tweaks_css({"__texture": {"tex": self._URI, "blend": "multiply", "intensity": 0.5}})
        self.assertEqual(css, "")

    def test_reserved_texture_key_skipped_by_apply_tweaks(self):
        processed = {"HERO": "hi"}
        apply_tweaks(processed, {"__texture": {"tex": self._URI}})
        self.assertEqual(processed, {"HERO": "hi"})  # untouched

    def test_no_texture_is_a_noop(self):
        html = '<div class="slide"><p>x</p></div>'
        self.assertEqual(_materialize_texture(html, None), html)
        self.assertEqual(_materialize_texture(html, {}), html)
        self.assertEqual(_materialize_texture(html, {"blend": "screen"}), html)  # no 'tex'

    def test_overlay_injected_into_slide_with_blend_and_opacity(self):
        html = '<div class="slide"><p>content</p></div>'
        out = _materialize_texture(html, {"tex": self._URI, "blend": "overlay", "intensity": 0.4})
        self.assertIn('data-texture="1"', out)
        self.assertIn("mix-blend-mode:overlay", out)
        self.assertIn("opacity:0.4", out)
        self.assertIn(self._URI, out)
        # overlay sits inside .slide, AFTER the content (so it composites on top)
        self.assertLess(out.index("content"), out.index('data-texture="1"'))
        self.assertLess(out.index('data-texture="1"'), out.rindex("</div>"))

    def test_blend_allowlist_and_intensity_clamp(self):
        out = _materialize_texture('<div class="slide"></div>',
                                   {"tex": self._URI, "blend": "evil-blend", "intensity": 5})
        self.assertIn("mix-blend-mode:multiply", out)  # unknown blend → safe default
        self.assertIn("opacity:1", out)                # intensity clamped to <= 1


class TestBackgroundStackable(unittest.TestCase):
    """FASE 6 §1 — BACKGROUND is a real stackable layer (not the root container), so
    raising it overlaps the layers below, live AND on bake (RNDR-04)."""

    SLIDE = ('<div class="slide" style="position:relative">'
             '<h1 data-slot="HERO">x</h1></div>')

    def test_bg_injected_as_stackable_child(self):
        out = _bake_tag_root_bg(self.SLIDE)
        self.assertIn('data-slot="BACKGROUND"', out)
        self.assertIn("background:inherit", out)
        self.assertIn("inset:0", out)
        # injected as a CHILD (after the .slide open tag), NOT the .slide root tagged
        self.assertLess(out.index('class="slide"'), out.index('data-slot="BACKGROUND"'))
        self.assertNotRegex(out, r'class="slide"[^>]*data-slot="BACKGROUND"')

    def test_bg_zorder_bakes(self):
        # raising BACKGROUND writes a real z-index the bake honors (matches applyToSlide live)
        css = _build_tweaks_css({"BACKGROUND": {"z": 99}})
        self.assertIn('[data-slot="BACKGROUND"]', css)
        self.assertIn("z-index: 99", css)

    def test_editor_and_bake_tag_identically(self):
        # byte-identical tagging in both modules → preview == baked PNG (parity by construction)
        self.assertEqual(_editor_tag_root_bg(self.SLIDE), _bake_tag_root_bg(self.SLIDE))

    def test_noop_when_real_background_exists(self):
        # a real BACKGROUND element (e.g. div.bg / full-AI <img>) is left untouched
        html = '<div class="slide"><img data-slot="BACKGROUND" src="x"></div>'
        self.assertEqual(_bake_tag_root_bg(html), html)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""test_preview_editor.py — smoke tests for preview_editor.py.

Asserts (AND, not OR — all must pass simultaneously):
  (a) srcdoc contains data-slot="HERO"
  (b) panel has both a HERO text control AND a PHOTO_MAIN image control
      (generated from the two slots in instructions.md — EDIT-01)
  (c) _shared/styles.css content is inlined inside a <style> block
      (a unique marker string from styles.css appears inside a <style> tag)
  (d) at least one data:font or ;base64, font data-URI is present in the srcdoc
      (proving _inline_relative_urls ran over @font-face src and base64-encoded the .ttf)
      — both (c) AND (d) are required; neither alone passes the test
  (e) container-type: inline-size is present
  (f) the embedded tweaksState initial JSON has a "global" key

Run:
    uv run test_preview_editor.py
"""

import base64
import json
import os
import re
import struct
import sys
import tempfile
import unittest
from pathlib import Path

# ── Cross-skill import (same path as preview_editor uses) ──────────────────
_SCRIPT_DIR = Path(__file__).resolve().parent
RENDER_SCRIPTS = _SCRIPT_DIR.parent.parent.parent.parent / "viz-image-gen" / "scripts"
sys.path.insert(0, str(RENDER_SCRIPTS))

# Import the module under test
sys.path.insert(0, str(_SCRIPT_DIR))
from preview_editor import build_editor_html, CURATED_FONTS  # noqa: E402


def _make_minimal_ttf() -> bytes:
    """Return a syntactically valid (but functionally empty) TTF file.

    The font must satisfy _inline_relative_urls: the file must exist and have
    the .ttf extension so the mime-type lookup resolves to font/ttf. The TTF
    header below is the TrueType 'sfVersion' tag (0x00010000) + zero tables —
    small enough to base64-encode quickly, yet structurally valid enough that
    the media-type lookup works purely from the extension.
    """
    # TTF offset table: version=1.0 (0x00010000), numTables=0
    return struct.pack(">IHHHH", 0x00010000, 0, 0, 0, 0)


# ── JS-behaviour harness (r5f-followups Fix 2) ─────────────────────────────────
# The text-target walk is JS that ships inside the editor (and is mirrored in the
# bake parity). A string-presence test can't prove WHERE the style lands, so these
# helpers run the REAL emitted function under Node against a tiny DOM shim. Node is
# optional in CI, so callers guard with @skipUnless(_node_ready()).
import shutil as _shutil  # noqa: E402
import subprocess as _subprocess  # noqa: E402


def _node_ready() -> bool:
    return _shutil.which("node") is not None


def _extract_js_function(source: str, name: str) -> str:
    """Return the full `function <name>(...) { ... }` text from *source* by
    brace-counting (regex can't balance the nested braces the fix introduced)."""
    start = source.index("function " + name + "(")
    i = source.index("{", start)
    depth = 0
    for j in range(i, len(source)):
        c = source[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return source[start:j + 1]
    raise AssertionError(f"unbalanced braces extracting {name}")


# A minimal DOM shim + node spec builder shared by editor and bake-parity tests.
_DOM_SHIM = r"""
function El(tag, opts){ opts=opts||{}; this.tagName=tag; this.children=opts.children||[];
  this._text=opts.text||""; this.cls=opts.cls||""; this.style={}; this.src=opts.src; }
Object.defineProperty(El.prototype,'textContent',{get:function(){
  if(this.children.length===0) return this._text;
  return this.children.map(function(c){return c.textContent;}).join('');
}});
El.prototype.querySelector=function(sel){
  // only 'img' is needed by the parity script's imgSrc branch
  var stack=this.children.slice(), n;
  while(stack.length){ n=stack.shift(); if(n.tagName==='IMG') return n;
    stack=n.children.concat(stack); }
  return null;
};
"""


def _run_tt(func_src: str, func_name: str, dom_build_js: str, label_js: str) -> str:
    """Run *func_src* (a textTarget/tt fn) under Node; return the selected node's
    label. *dom_build_js* must define `var root = <El tree>`; *label_js* maps the
    result `r` to a string to print (e.g. 'r.cls')."""
    script = (
        _DOM_SHIM
        + "var INLINE_MARKUP={MARK:1,BR:1,B:1,I:1,EM:1,STRONG:1,SPAN:1,A:1,"
          "SMALL:1,SUP:1,SUB:1,U:1,S:1,WBR:1};\n"
        + "var INLINE=INLINE_MARKUP;\n"  # the parity fn calls its table INLINE
        + func_src + "\n"
        + dom_build_js + "\n"
        + "var r=" + func_name + "(root);\n"
        + "console.log(" + label_js + ");\n"
    )
    proc = _subprocess.run(
        ["node", "-e", script], capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        raise AssertionError(f"node failed: {proc.stderr or proc.stdout}")
    return proc.stdout.strip()


def _make_run_folder() -> tempfile.TemporaryDirectory:
    """Create a minimal run folder with all fixtures and return the TemporaryDirectory.

    Layout:
        <tmp>/
            _shared/
                styles.css              # contains a unique CSS marker
                stub.ttf                # minimal TTF so _inline_relative_urls encodes it
            slide-01/
                template.html           # has data-slot="HERO" and data-slot="PHOTO_MAIN"
                instructions.md         # HERO (text) + PHOTO_MAIN (image) slots
    """
    td = tempfile.TemporaryDirectory()
    root = Path(td.name)

    # ── _shared/styles.css ──────────────────────────────────────────────────
    shared_dir = root / "_shared"
    shared_dir.mkdir()

    # Unique marker string we will later assert is inlined inside <style>
    CSS_MARKER = "/* UNIQUE-CSS-MARKER-FOR-TEST */"
    css_content = (
        f"{CSS_MARKER}\n"
        f"@font-face {{\n"
        f"  font-family: 'TestFont';\n"
        f"  src: url('stub.ttf') format('truetype');\n"
        f"}}\n"
        f"body {{ margin: 0; }}\n"
    )
    (shared_dir / "styles.css").write_text(css_content, encoding="utf-8")

    # ── stub.ttf (real bytes — _inline_relative_urls needs a readable file) ─
    (shared_dir / "stub.ttf").write_bytes(_make_minimal_ttf())

    # ── slide-01/ ──────────────────────────────────────────────────────────
    slide_dir = root / "slide-01"
    slide_dir.mkdir()

    # template.html — uses data-slot on both zones
    template_html = (
        "<!doctype html><html><head><meta charset='utf-8'></head><body>"
        "<div class=\"zone\" data-slot=\"HERO\">{{{HERO}}}</div>"
        "<div class=\"zone\" data-slot=\"PHOTO_MAIN\">"
        "<img src=\"photo.png\" alt=\"photo\">"
        "</div>"
        "</body></html>"
    )
    (slide_dir / "template.html").write_text(template_html, encoding="utf-8")

    # instructions.md — HERO (text) + PHOTO_MAIN (image)
    instructions_md = """# Slide 01

## Slots

- **HERO** — main headline
  - bbox: 4% 22% 92% 7%
  - style: display-italic, 8cqw, white on coral, left-align
  - sample: "Test headline here"
  - max_chars: 60

- **PHOTO_MAIN** — main photo
  - bbox: 10% 40% 80% 50%
  - style: image, cover
  - sample: ""

## Notes

Nothing else here.
"""
    (slide_dir / "instructions.md").write_text(instructions_md, encoding="utf-8")

    return td


def _make_pool_run_folder() -> tempfile.TemporaryDirectory:
    """Create a run whose slide points at a template in a POOL whose shared CSS
    lives at <pool>/_shared/styles.css — the real layout render_template.py uses.

    Layout:
        <tmp>/
            pool/
                _shared/styles.css   # POOL-SHARED-CSS-MARKER + @font-face -> stub.ttf
                _shared/stub.ttf
                cover/
                    template.html    # data-slot="HERO"
                    instructions.md  # HERO slot
            run/
                _slides/slide-01/metadata.json -> {"template_dir": "<abs pool/cover>"}

    No shared_css_override is passed to build_editor_html, so it MUST discover the
    shared CSS from template_dir.parent/_shared (regression guard for the
    per-slide pool lookup — font parity, Pitfall 1).
    """
    td = tempfile.TemporaryDirectory()
    root = Path(td.name)

    shared = root / "pool" / "_shared"
    shared.mkdir(parents=True)
    (shared / "styles.css").write_text(
        "/* POOL-SHARED-CSS-MARKER */\n"
        "@font-face {\n  font-family: 'TestFont';\n"
        "  src: url('stub.ttf') format('truetype');\n}\n"
        "body { margin: 0; }\n",
        encoding="utf-8",
    )
    (shared / "stub.ttf").write_bytes(_make_minimal_ttf())

    tdir = root / "pool" / "cover"
    tdir.mkdir()
    (tdir / "template.html").write_text(
        "<!doctype html><html><head><meta charset='utf-8'></head><body>"
        "<div class=\"zone\" data-slot=\"HERO\">{{{HERO}}}</div>"
        "</body></html>",
        encoding="utf-8",
    )
    (tdir / "instructions.md").write_text(
        "# Slide\n\n## Slots\n\n- **HERO** — headline\n"
        "  - bbox: 4% 22% 92% 7%\n  - style: display, 8cqw\n  - sample: \"Hi\"\n",
        encoding="utf-8",
    )

    meta_dir = root / "run" / "_slides" / "slide-01"
    meta_dir.mkdir(parents=True)
    (meta_dir / "metadata.json").write_text(
        json.dumps({"template_dir": str(tdir), "slide_id": "slide-01"}),
        encoding="utf-8",
    )
    return td


class TestPoolSharedCssDiscovery(unittest.TestCase):
    """Regression guard: build_editor_html must discover <template_dir>.parent/
    _shared/styles.css (the real pool layout) and base64-inline its @font-face,
    WITHOUT any shared_css_override. Earlier this lookup missed the pool layout,
    so no brand fonts were inlined into the preview (the #1 font-parity risk)."""

    def setUp(self):
        self._td = _make_pool_run_folder()
        self._html = build_editor_html(Path(self._td.name) / "run")

    def tearDown(self):
        self._td.cleanup()

    def test_pool_shared_css_inlined(self):
        self.assertIn(
            "POOL-SHARED-CSS-MARKER", self._html,
            "pool _shared/styles.css was not discovered/inlined "
            "(template_dir.parent/_shared per-slide lookup regressed)",
        )

    def test_pool_font_base64_inlined(self):
        self.assertTrue(
            "data:font" in self._html or ";base64," in self._html,
            "pool @font-face was not base64-inlined — font parity broken "
            "for the real pool layout",
        )

    def test_cross_skill_import_ok(self):
        """The cross-skill render_template import MUST succeed. If RENDER_SCRIPTS
        overshoots the pack root (one .parent too many), the import silently falls
        back to stubs: no brand-tokens CSS and empty slide text. Locks that bug."""
        import preview_editor as _pe
        self.assertTrue(
            _pe._IMPORT_OK,
            "preview_editor failed to import render_template (RENDER_SCRIPTS path "
            "regression) — preview would render with stub fill/no brand tokens",
        )

    def test_slide_text_is_filled(self):
        """The HERO sample text must appear in the rendered slide srcdoc (not just
        the panel). When the cross-skill import falls back, the per-slide
        parse_sample_text import fails and slots render empty."""
        import html as _h
        import re as _r
        m = _r.search(r'srcdoc="([^"]*)"', self._html, _r.DOTALL)
        self.assertIsNotNone(m, "no iframe srcdoc found")
        src = _h.unescape(m.group(1))
        self.assertIn("Hi", src, "HERO sample text not filled into slide srcdoc")
        self.assertNotIn("{{HERO}}", src)
        self.assertNotIn(
            '<div class="zone" data-slot="HERO"></div>', src,
            "HERO zone rendered empty — sample text was not substituted",
        )


class TestBuildEditorHtml(unittest.TestCase):
    """Smoke tests for build_editor_html() — all assertions are AND, not OR."""

    def setUp(self):
        self._td = _make_run_folder()
        self._run = Path(self._td.name)
        shared_css = (self._run / "_shared" / "styles.css").read_text(encoding="utf-8")

        # Build the editor HTML, injecting the shared CSS from the temp dir.
        # shared_css_dir_override tells _build_srcdoc to resolve url() references
        # (i.e. the stub.ttf @font-face src) relative to _shared/, so the font
        # actually gets base64-encoded into the srcdoc (Pitfall 1 proof).
        self._html = build_editor_html(
            run=self._run,
            brand_context=None,
            shared_css_override=shared_css,
            shared_css_dir_override=self._run / "_shared",
        )

    def tearDown(self):
        self._td.cleanup()

    # ── (a) data-slot="HERO" in srcdoc ─────────────────────────────────────
    def test_a_data_slot_hero_present(self):
        """(a) The srcdoc must contain the data-slot='HERO' attribute."""
        self.assertIn('data-slot="HERO"', self._html,
                      "(a) FAILED: data-slot='HERO' not found in editor HTML")

    # ── (b) Panel has HERO text control AND PHOTO_MAIN image control ────────
    def test_b_hero_control_generated(self):
        """(b-i) Panel must contain a HERO control group (from parsed slots)."""
        self.assertIn('data-slot="HERO"', self._html,
                      "(b-i) FAILED: no HERO control in panel")
        # Assert it has data-control-type="text" (HERO is a text zone)
        self.assertIn('data-control-type="text"', self._html,
                      "(b-i) FAILED: no text control group for HERO")

    def test_b_photo_main_control_generated(self):
        """(b-ii) Panel must contain a PHOTO_MAIN control group (from parsed slots)."""
        self.assertIn('data-slot="PHOTO_MAIN"', self._html,
                      "(b-ii) FAILED: no PHOTO_MAIN control in panel")
        # PHOTO_MAIN style contains 'image' so it maps to image zone
        self.assertIn('data-control-type="image"', self._html,
                      "(b-ii) FAILED: no image control group for PHOTO_MAIN")

    def test_b_panel_not_hardcoded_slot_names(self):
        """(b) Controls are generated from parsed slots — verify the
        parse_slots_from_instructions call is feeding the panel (the
        slot names from instructions.md appear in both control and data-slot attrs)."""
        # Both must appear as data-slot attributes in the HTML
        hero_count = self._html.count('data-slot="HERO"')
        photo_count = self._html.count('data-slot="PHOTO_MAIN"')
        self.assertGreater(hero_count, 0,
                           "(b) FAILED: HERO data-slot not generated from slots")
        self.assertGreater(photo_count, 0,
                           "(b) FAILED: PHOTO_MAIN data-slot not generated from slots")

    # ── (c) _shared/styles.css inlined in a <style> block ──────────────────
    def test_c_shared_css_inlined_in_style_block(self):
        """(c) The unique CSS marker must appear inside a <style> block in the srcdoc.

        The srcdoc is HTML-attribute-escaped into srcdoc="..." in the outer HTML,
        so <style> appears as &lt;style&gt; in the raw outer HTML.  We unescape the
        srcdoc attribute value first, then search for the marker in <style> blocks
        within the decoded srcdoc.

        This is the CRITICAL font-parity assertion — if the shared CSS is NOT
        inlined, fonts will not load in the iframe.  Must pass even if (d) also
        passes; neither alone is sufficient.
        """
        import html as _html_mod
        MARKER = "UNIQUE-CSS-MARKER-FOR-TEST"
        self.assertIn(MARKER, self._html,
                      "(c) FAILED: CSS marker not found at all in editor HTML")

        # Extract srcdoc attribute values (they are HTML-escaped) and unescape them
        srcdoc_attrs = re.findall(r'srcdoc="([^"]*)"', self._html)
        unescaped_srcdocs = [_html_mod.unescape(s) for s in srcdoc_attrs]

        # The marker must appear inside a <style>...</style> in at least one srcdoc
        def _marker_in_style_block(unescaped: str) -> bool:
            blocks = re.findall(r"<style[^>]*>(.*?)</style>", unescaped, re.DOTALL | re.IGNORECASE)
            return any(MARKER in block for block in blocks)

        marker_in_srcdoc_style = any(_marker_in_style_block(s) for s in unescaped_srcdocs)
        self.assertTrue(marker_in_srcdoc_style,
                        f"(c) FAILED: CSS marker '{MARKER}' found in HTML but NOT inside a <style> block "
                        "within any srcdoc. The shared CSS is present but not inlined in a style element. "
                        f"Number of srcdoc attrs found: {len(srcdoc_attrs)}")

    # ── (d) data:font or ;base64, font URI in srcdoc ───────────────────────
    def test_d_font_base64_inlined(self):
        """(d) At least one data:font or ;base64, font data-URI must be present.

        This proves _inline_relative_urls ran over the @font-face src and
        base64-encoded the .ttf from _shared/styles.css.

        MUST pass independently of (c) — AND, not OR.
        """
        has_data_font = "data:font" in self._html
        has_base64_font = ";base64," in self._html
        self.assertTrue(has_data_font or has_base64_font,
                        "(d) FAILED: No data:font or ;base64, font data-URI found in editor HTML. "
                        "_inline_relative_urls did not base64-encode the @font-face .ttf. "
                        "Font parity with the baked PNG is BROKEN.")

    def test_c_and_d_both_required(self):
        """(c) AND (d) together — both CSS inline AND font base64 must pass.

        A separate combined assertion so the test name makes the AND requirement explicit.
        The srcdoc content is HTML-attribute-escaped, so we unescape to search inside it.
        """
        import html as _html_mod
        MARKER = "UNIQUE-CSS-MARKER-FOR-TEST"

        srcdoc_attrs = re.findall(r'srcdoc="([^"]*)"', self._html)
        unescaped_srcdocs = [_html_mod.unescape(s) for s in srcdoc_attrs]

        def _marker_in_style_block(unescaped: str) -> bool:
            blocks = re.findall(r"<style[^>]*>(.*?)</style>", unescaped, re.DOTALL | re.IGNORECASE)
            return any(MARKER in block for block in blocks)

        c_ok = any(_marker_in_style_block(s) for s in unescaped_srcdocs)
        d_ok = "data:font" in self._html or ";base64," in self._html

        self.assertTrue(c_ok and d_ok,
                        f"(c AND d) FAILED: c={c_ok}, d={d_ok}. "
                        "Both CSS inlining AND font base64 encoding are required for parity. "
                        "Weakening this to OR is NOT acceptable.")

    # ── (e) container-type: inline-size ────────────────────────────────────
    def test_e_container_type_present(self):
        """(e) The editor HTML must contain 'container-type: inline-size'
        so cqw units resolve against the slide container in a scaled iframe."""
        self.assertIn("container-type: inline-size", self._html,
                      "(e) FAILED: container-type: inline-size not found. "
                      "cqw units may not resolve correctly in a scaled iframe.")

    # ── (f) tweaksState has "global" key ───────────────────────────────────
    def test_f_tweaks_state_has_global_key(self):
        """(f) The embedded tweaksState JS initialization must include a 'global' key."""
        self.assertIn('"global"', self._html,
                      "(f) FAILED: 'global' key not found in editor HTML. "
                      "tweaksState.global is missing — global scope broken.")

    # ── Additional: pill zone distinct from text ────────────────────────────
    def test_pill_zone_no_font_size_slider(self):
        """Pill control groups must NOT include a font-size or opacity slider.
        (Plan spec: pill = text + position only.)
        """
        # Find all pill control groups
        pill_blocks = re.findall(
            r'data-control-type="pill".*?</div>\s*</div>',
            self._html, re.DOTALL
        )
        for block in pill_blocks:
            self.assertNotIn("Font size", block,
                             "Pill control group must NOT have a font-size slider")
            self.assertNotIn("Opacity", block,
                             "Pill control group must NOT have an opacity slider")

    # ── Additional: chrome zone distinct from text ──────────────────────────
    def test_chrome_zone_no_position_sliders(self):
        """Chrome control groups must NOT include position/text sliders.
        (Plan spec: chrome = global toggle only.)
        """
        chrome_blocks = re.findall(
            r'data-control-type="chrome".*?</div>\s*</div>',
            self._html, re.DOTALL
        )
        for block in chrome_blocks:
            self.assertNotIn("Font size", block,
                             "Chrome control group must NOT have a font-size slider")
            self.assertNotIn("Content", block,
                             "Chrome control group must NOT have a content/text input")
            self.assertNotIn("X (%)", block,
                             "Chrome control group must NOT have X position slider")

    # ── Additional: image zone has scale + opacity + rotate controls ─────────
    def test_image_zone_has_scale_opacity_rotate(self):
        """The PHOTO_MAIN image zone must let you scale, set opacity, and rotate it
        (the editing the user actually needs — no stale 'coming soon' note).

        Scale uses a custom dropdown (data-prop=scale) instead of a native <select>
        so it stays readable in the dark panel. Opacity and tilt still use direct
        applyToSlide inline handlers."""
        self.assertIn('data-control-type="image"', self._html,
                      "No image control group found — PHOTO_MAIN should be type=image")
        # Custom dropdown: the csel-trigger carries data-prop="scale" + the slide/handle.
        self.assertIn('data-prop="scale"', self._html,
                      "image zone must have a scale control (custom dropdown, data-prop=scale)")
        self.assertIn("data-handle=\"PHOTO_MAIN\"", self._html,
                      "image zone custom dropdown must carry data-handle=PHOTO_MAIN")
        self.assertIn("applyToSlide('slide-01','PHOTO_MAIN','opacity'", self._html,
                      "image zone must have an opacity control")
        self.assertIn("applyToSlide('slide-01','PHOTO_MAIN','tilt'", self._html,
                      "image zone must have a rotate (tilt) control")
        # No native <select> for scale: the custom dropdown prevents white-on-white.
        self.assertNotIn(
            'select onchange="applyToSlide(\'slide-01\',\'PHOTO_MAIN\',\'scale\'',
            self._html,
            "scale must use the custom dropdown, not a native <select>",
        )
        self.assertNotIn("coming soon", self._html.lower(),
                         "stale 'Layers (coming soon)' note should be gone")

    # ── Additional: export functions present ────────────────────────────────
    def test_export_tweaks_function_present(self):
        """exportTweaks() must be present in the embedded JS."""
        self.assertIn("exportTweaks", self._html,
                      "exportTweaks() not found in editor HTML")

    def test_download_blob_present(self):
        """exportTweaks must use Blob download (the UX upgrade from paste-back)."""
        self.assertIn("new Blob", self._html,
                      "exportTweaks must use Blob download; paste-back is the old approach")

    # ── Additional: no external CDN or JS framework ─────────────────────────
    def test_no_external_script_src(self):
        """No <script src='http...'>; all JS is self-contained (CONS-01)."""
        external = re.findall(r'<script\b[^>]+src\s*=\s*["\']https?://', self._html, re.IGNORECASE)
        self.assertEqual(external, [],
                         f"External CDN script tags found (CONS-01 violated): {external}")

    # ── Additional: build_editor_html returns a string ──────────────────────
    def test_returns_string(self):
        """build_editor_html must return a str (not write to disk directly in test)."""
        self.assertIsInstance(self._html, str,
                              "build_editor_html must return str")
        self.assertGreater(len(self._html), 500,
                           "build_editor_html returned suspiciously short string")


class TestFullbleedAiCollapse(unittest.TestCase):
    """A full-bleed AI composition (the whole slide IS one AI image) must surface as
    exactly ONE editable PHOTO_MAIN image layer — never a non-editable ``frame`` shape,
    never a duplicate/phantom empty PHOTO_MAIN slot. Some legacy templates were authored
    with the AI <img> inside a ``composition-frame`` wrapper PLUS a second, redundant
    invisible ``data-slot="PHOTO_MAIN"`` zone binding the same path. The editor repairs
    that (``_collapse_fullbleed_ai``, run inside ``_tag_decor``)."""

    # A frame-wrapped full-bleed AI image + a duplicate invisible PHOTO_MAIN marker.
    _LEGACY = (
        '<head></head><body><div class="slide">'
        '<div class="composition-frame">'
        '<img class="ai-render" src="{{PHOTO_MAIN_PATH}}" alt="">'
        '</div>'
        '<div class="card-zone-marker" data-zone="photo" data-slot="PHOTO_MAIN">'
        '<img class="card-render" src="{{PHOTO_MAIN_PATH}}" alt="{{PHOTO_SUBJECT}}">'
        '</div>'
        '</div></body>'
    )

    def test_exposes_exactly_one_editable_photo_main(self):
        import preview_editor as _pe
        out = _pe._tag_decor(self._LEGACY)
        self.assertEqual(out.count('data-slot="PHOTO_MAIN"'), 1,
                         "must collapse to a single PHOTO_MAIN (no phantom slot)")

    def test_frame_wrapper_becomes_the_editable_photo_main(self):
        import preview_editor as _pe
        out = _pe._tag_decor(self._LEGACY)
        m = re.search(r'<div[^>]*data-slot="PHOTO_MAIN"[^>]*>', out)
        self.assertIsNotNone(m)
        # The full-bleed AI wrapper (the one that renders the image) is the editable one.
        self.assertIn("composition-frame", m.group(0))

    def test_frame_not_classified_as_noneditable_shape(self):
        import preview_editor as _pe
        out = _pe._tag_decor(self._LEGACY)
        self.assertNotIn('data-slot="FRAME"', out,
                         "the AI composition must not be tagged as a non-editable FRAME")

    def test_redundant_marker_removed(self):
        import preview_editor as _pe
        out = _pe._tag_decor(self._LEGACY)
        self.assertNotIn("card-zone-marker", out)
        self.assertNotIn("card-render", out)

    def test_idempotent(self):
        import preview_editor as _pe
        once = _pe._tag_decor(self._LEGACY)
        twice = _pe._tag_decor(once)
        self.assertEqual(once.count('data-slot="PHOTO_MAIN"'),
                         twice.count('data-slot="PHOTO_MAIN"'))
        self.assertEqual(once, twice)

    def test_canonical_template_untouched(self):
        """A correctly authored single full-bleed PHOTO_MAIN (no frame wrapper) is a
        no-op for the collapse step."""
        import preview_editor as _pe
        canonical = (
            '<head></head><body><div class="slide">'
            '<img class="ai-render" data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}">'
            '</div></body>'
        )
        self.assertEqual(_pe._collapse_fullbleed_ai(canonical), canonical)


class TestImagePlaceholderAndShell(unittest.TestCase):
    """Empty image zone -> a VISIBLE labelled "missing image: <HANDLE>" placeholder
    (audit #3/#10, supersedes the 2026-06-03 transparent stub). A missing/unwired
    hero must read as obviously broken in the editor preview, not look identical to
    "by design". Editor-preview only — the real bake never calls this. Editor wraps
    the slide in the LinkedIn-post mock with the command-centre control panel."""

    def test_empty_img_gets_visible_missing_placeholder(self):
        import base64 as _b64
        import preview_editor as _pe
        html = '<head></head><body><img src="" data-slot="PHOTO_MAIN" alt="scaffold"></body>'
        out = _pe._placeholder_empty_images(html)
        self.assertIn("data:image/svg+xml;base64,", out)  # self-contained, no broken icon
        self.assertNotIn('src=""', out)
        self.assertIn('data-ph="1"', out)
        self.assertNotIn("blur(", out)  # not the old dimmed/blurred ghost
        # Decode the embedded SVG and prove it draws a VISIBLE hint: dashed box +
        # the slot handle in a "missing image" label.
        b64 = re.search(r'data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)', out).group(1)
        svg = _b64.b64decode(b64).decode("utf-8")
        self.assertIn("<rect", svg)              # the dashed box
        self.assertIn("stroke-dasharray", svg)   # dashed, not solid
        self.assertIn("<text", svg)              # the label
        self.assertIn("missing image: PHOTO_MAIN", svg)

    def test_empty_img_without_slot_falls_back_to_generic_label(self):
        import base64 as _b64
        import preview_editor as _pe
        html = '<head></head><body><img src=""></body>'
        out = _pe._placeholder_empty_images(html)
        b64 = re.search(r'data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)', out).group(1)
        svg = _b64.b64decode(b64).decode("utf-8")
        self.assertIn("missing image: image", svg)

    def test_placeholder_needs_no_ref_on_disk(self):
        """The placeholder is fully inline, so it works with no assets/ on disk."""
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            html = '<head></head><img src="">'
            out = _pe._placeholder_empty_images(html, Path(d))
            self.assertIn("data:image/svg+xml;base64,", out)
            self.assertIn('data-ph="1"', out)

    def test_no_empty_img_left_unchanged(self):
        import preview_editor as _pe
        html = '<body><img src="real.png"></body>'
        self.assertEqual(_pe._placeholder_empty_images(html), html)

    # ── D3 (studio-sweep): bg-image divs with an unfilled inline slot ──────────
    def test_unfilled_bg_div_gets_placeholder(self):
        """An unfilled {{PHOTO_MAIN_PATH}} in background-image:url('') (after Mustache
        fill) gets the same labelled placeholder an empty <img> gets (prop-scene-cover)."""
        import base64 as _b64
        import preview_editor as _pe
        html = (
            "<head></head><body>"
            "<div class='bg' data-slot='PHOTO_MAIN' "
            "style=\"background-image: url(''); background-size: cover;\"></div>"
            "</body>"
        )
        out = _pe._placeholder_empty_images(html)
        self.assertNotEqual(out, html, "unfilled bg div was not healed")
        self.assertIn('data-ph="1"', out)
        self.assertIn("background-image:url('data:image/svg+xml;base64,", out)
        b64 = re.search(r"data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)", out).group(1)
        svg = _b64.b64decode(b64).decode("utf-8")
        self.assertIn("missing image: PHOTO_MAIN", svg)

    def test_filled_bg_div_untouched(self):
        """A FILLED bg-image div (real data-URI) is a no-op."""
        import preview_editor as _pe
        html = (
            "<head></head><body>"
            "<div data-slot='PHOTO_MAIN' "
            "style=\"background-image: url('data:image/png;base64,AAAA');\"></div>"
            "</body>"
        )
        self.assertEqual(_pe._placeholder_empty_images(html), html)

    def test_real_path_bg_div_untouched(self):
        """A bg-image div pointing at a real (non-empty) path is a no-op."""
        import preview_editor as _pe
        html = (
            "<head></head><body>"
            "<div data-slot='PHOTO_MAIN' "
            "style=\"background-image: url('_ai_bg/photo_main.png');\"></div>"
            "</body>"
        )
        self.assertEqual(_pe._placeholder_empty_images(html), html)

    def test_bg_div_placeholder_idempotent(self):
        """Re-running on already-healed HTML is a no-op (the empty url() is gone)."""
        import preview_editor as _pe
        html = (
            "<head></head><body>"
            "<div data-slot='PHOTO_MAIN' style=\"background-image: url();\"></div>"
            "</body>"
        )
        once = _pe._placeholder_empty_images(html)
        twice = _pe._placeholder_empty_images(once)
        self.assertEqual(once, twice)

    # ── Template-mode hero resolution (fix-template-hero-resolve) ─────────────
    # In TEMPLATE mode the run's data never pins PHOTO_MAIN_PATH / BG_PATH, so
    # _build_srcdoc must resolve the unfilled hero slot to the template's real
    # _ai_bg asset BEFORE the empty-placeholder fires — else every template shows
    # "missing image" though its AI hero exists on disk.
    def _has_missing_placeholder(self, srcdoc):
        import base64 as _b64
        for tok in srcdoc.split("data:image/svg+xml;base64,")[1:]:
            b = tok.split('"')[0].split("'")[0]
            try:
                if b"missing image:" in _b64.b64decode(b):
                    return True
            except Exception:
                pass
        return False

    def test_hero_resolves_canonical_photo_main(self):
        """An unfilled {{PHOTO_MAIN_PATH}} with an existing _ai_bg/photo_main.png
        resolves to that asset in _build_srcdoc (real data-URI, no placeholder)."""
        import base64 as _b64
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "_ai_bg").mkdir()
            png = b"\x89PNG\r\n\x1a\n" + b"hero-canonical"
            (d / "_ai_bg" / "photo_main.png").write_bytes(png)
            th = d / "template.html"
            th.write_text(
                '<html><head></head><body>'
                '<img src="{{PHOTO_MAIN_PATH}}"></body></html>', encoding="utf-8")
            out = _pe._build_srcdoc(th, {}, "", "")
            uri = "data:image/png;base64," + _b64.b64encode(png).decode("ascii")
            self.assertIn(uri, out)                       # real asset shown
            self.assertFalse(self._has_missing_placeholder(out))

    def test_hero_resolves_single_ai_bg_bg_png(self):
        """A single _ai_bg/bg.png (numbered-body naming) resolves for an unfilled
        background-image:url('{{PHOTO_MAIN_PATH}}') — no placeholder."""
        import base64 as _b64
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "_ai_bg").mkdir()
            png = b"\x89PNG\r\n\x1a\n" + b"hero-bg"
            (d / "_ai_bg" / "bg.png").write_bytes(png)
            th = d / "template.html"
            th.write_text(
                '<html><head></head><body>'
                "<div style=\"background-image: url('{{PHOTO_MAIN_PATH}}');\"></div>"
                "</body></html>", encoding="utf-8")
            out = _pe._build_srcdoc(th, {}, "", "")
            uri = "data:image/png;base64," + _b64.b64encode(png).decode("ascii")
            self.assertIn(uri, out)
            self.assertFalse(self._has_missing_placeholder(out))

    def test_hero_genuinely_missing_still_gets_placeholder(self):
        """No _ai_bg asset → the hero slot stays empty and the "missing image"
        placeholder fires (the fix never masks a truly-unwired image)."""
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            th = d / "template.html"
            th.write_text(
                '<html><head></head><body>'
                '<img src="{{PHOTO_MAIN_PATH}}"></body></html>', encoding="utf-8")
            out = _pe._build_srcdoc(th, {}, "", "")
            self.assertTrue(self._has_missing_placeholder(out))

    def test_resolve_ai_bg_order(self):
        """_resolve_ai_bg_asset: canonical photo_main.png wins; else the single
        _ai_bg/*.png; else None when ambiguous/absent."""
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            ab = d / "_ai_bg"; ab.mkdir()
            self.assertIsNone(_pe._resolve_ai_bg_asset(d))         # empty → None
            (ab / "bg.png").write_bytes(b"x")
            self.assertEqual(_pe._resolve_ai_bg_asset(d).name, "bg.png")  # single
            (ab / "photo_main.png").write_bytes(b"y")
            self.assertEqual(_pe._resolve_ai_bg_asset(d).name, "photo_main.png")  # canonical wins
            (ab / "extra.png").write_bytes(b"z")
            # canonical still wins even with multiple
            self.assertEqual(_pe._resolve_ai_bg_asset(d).name, "photo_main.png")

    def test_no_slide_num_badge(self):
        """The slide-num corner badge was removed (user request)."""
        import preview_editor as _pe
        td = _make_pool_run_folder()
        try:
            html = _pe.build_editor_html(Path(td.name) / "run")
            self.assertNotIn("slide-num", html)
        finally:
            td.cleanup()

    def test_shell_has_linkedin_mock_and_panel(self):
        import preview_editor as _pe
        td = _make_pool_run_folder()
        try:
            html = _pe.build_editor_html(Path(td.name) / "run")
            for marker in ("li-post", "slide-frame-wrap", "li-react", "export-btn", "panel"):
                self.assertIn(marker, html, f"editor shell missing '{marker}'")
            # slide scaled to the post width (FASE 5 fit: 440/1080 so the whole slide shows)
            self.assertIn("scale(0.407407)", html)
        finally:
            td.cleanup()


def _make_asset_slot_run_folder() -> tempfile.TemporaryDirectory:
    """A run whose template has image/svg zones with STRIPPED data-slots while the
    instructions name them with the _PATH suffix — the real-world mismatch that made
    image edits no-ops. Also includes a prompt-only slot (no data-slot) to prove the
    phantom-control filter works."""
    td = tempfile.TemporaryDirectory()
    root = Path(td.name)
    sd = root / "slide-01"
    sd.mkdir(parents=True)
    (sd / "template.html").write_text(
        "<!doctype html><html><head><meta charset='utf-8'></head><body>"
        '<div data-slot="IMAGE" class="photo"><img src="{{IMAGE_PATH}}" alt=""></div>'
        '{{#ANNOTATION_SVG_PATH}}<div data-slot="ANNOTATION_SVG"><img src="{{ANNOTATION_SVG_PATH}}"></div>{{/ANNOTATION_SVG_PATH}}'
        '<div data-slot="TITLE">{{{TITLE}}}</div>'
        "</body></html>",
        encoding="utf-8",
    )
    (sd / "instructions.md").write_text(
        "# S\n\n## Slots\n\n"
        "- **TITLE** — headline\n  - bbox: 4% 10% 90% 8%\n  - style: display, 7cqw\n  - sample: \"Hi\"\n"
        "- **IMAGE_PATH** — the screenshot\n  - bbox: 6% 24% 88% 50%\n  - style: image, cover\n"
        "- **ANNOTATION_SVG_PATH** — optional red annotation overlay\n  - bbox: 6% 24% 88% 50%\n  - style: image, svg overlay\n"
        "- **PHOTO_SUBJECT** — prompt text describing the photo (not an on-slide zone)\n  - style: ai-image prompt\n",
        encoding="utf-8",
    )
    return td


class TestAssetSlotHandles(unittest.TestCase):
    """Fase A: image/SVG controls must target the STRIPPED data-slot handle, skip
    phantom (prompt-only / absent-optional) slots, and offer real editing."""

    @classmethod
    def setUpClass(cls):
        import preview_editor as _pe
        cls._td = _make_asset_slot_run_folder()
        cls._html = _pe.build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_slot_handle_strips_suffix(self):
        import preview_editor as _pe
        self.assertEqual(_pe._slot_handle("PHOTO_MAIN_PATH"), ("PHOTO_MAIN", True))
        self.assertEqual(_pe._slot_handle("ANNOTATION_SVG_PATH"), ("ANNOTATION_SVG", True))
        self.assertEqual(_pe._slot_handle("IMAGE_PATH"), ("IMAGE", True))
        self.assertEqual(_pe._slot_handle("TITLE"), ("TITLE", False))

    def test_image_control_targets_stripped_handle(self):
        # control + applyToSlide must use IMAGE, never IMAGE_PATH (the bug)
        self.assertIn('data-slot="IMAGE"', self._html)
        self.assertIn("applyToSlide('slide-01','IMAGE',", self._html)
        self.assertNotIn("IMAGE_PATH", self._html)

    def test_phantom_prompt_slot_skipped(self):
        # PHOTO_SUBJECT has no data-slot in the DOM -> no control for it
        self.assertNotIn("PHOTO_SUBJECT", self._html)

    def test_absent_optional_overlay_skipped(self):
        # ANNOTATION_SVG is wrapped in {{#ANNOTATION_SVG_PATH}}; with no path supplied
        # the element isn't in the rendered DOM, so no control should appear.
        self.assertNotIn('data-slot="ANNOTATION_SVG"', self._html)
        self.assertNotIn("ANNOTATION_SVG_PATH", self._html)

    def test_blank_unresolved_assets(self):
        """Descriptive/unresolved *_PATH/*_SRC values are blanked; real assets kept."""
        import preview_editor as _pe
        out = _pe._blank_unresolved_assets({
            "ANNOTATION_SVG_PATH": "optional per-post SVG of red annotations",
            "LOGO_PATH": "data:image/png;base64,AAAA",
            "BG_SRC": "https://x/y.png",
            "TITLE": "not a path slot",
        })
        self.assertEqual(out["ANNOTATION_SVG_PATH"], "")          # descriptive -> blanked
        self.assertEqual(out["LOGO_PATH"], "data:image/png;base64,AAAA")  # real -> kept
        self.assertEqual(out["BG_SRC"], "https://x/y.png")         # real -> kept
        self.assertEqual(out["TITLE"], "not a path slot")          # non-asset -> untouched

    def test_scale_applies_chosen_value(self):
        # the JS scale handler must use the selected value, not hardcode 'cover'
        self.assertIn("value === 'crop' ? 'none' : 'cover'", self._html)
        self.assertIn("value === 'square' ? '1 / 1'", self._html)


def _make_two_slide_pool_run_folder() -> tempfile.TemporaryDirectory:
    """Like _make_pool_run_folder but with TWO slides pointing at the same template,
    so the multi-slide carousel chrome (nav arrows + dots) is exercised."""
    td = _make_pool_run_folder()
    root = Path(td.name)
    tdir = root / "pool" / "cover"
    meta_dir = root / "run" / "_slides" / "slide-02"
    meta_dir.mkdir(parents=True)
    (meta_dir / "metadata.json").write_text(
        json.dumps({"template_dir": str(tdir), "slide_id": "slide-02"}),
        encoding="utf-8",
    )
    return td


class TestSwipeCarousel(unittest.TestCase):
    """REFINED 2026-06-03 preview-UX: horizontal swipe carousel (drag + arrows +
    dots), editing the active slide one at a time — NOT tabs, NOT a vertical stack."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_two_slide_pool_run_folder()
        cls._html = build_editor_html(Path(cls._td.name) / "run")

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_has_horizontal_track(self):
        self.assertIn('id="carousel-track"', self._html)
        self.assertIn("class=\"carousel-track\"", self._html)
        self.assertIn("translateX(", self._html)  # the track is moved horizontally

    def test_iframe_does_not_swallow_drag(self):
        """The slide iframe must be pointer-events:none so drags reach the track."""
        self.assertIn("pointer-events: none", self._html)

    def test_not_tabs_not_vertical_stack(self):
        # The two earlier wrong interpretations must be gone.
        self.assertNotIn("slide-tab", self._html)      # NOT tabs
        self.assertNotIn("showSlide", self._html)       # old tab switcher removed
        self.assertNotIn("border-top: 6px solid", self._html)  # NOT a vertical stack

    def test_swipe_api_present(self):
        self.assertIn("function goToSlide", self._html)
        self.assertIn("navSlide", self._html)
        self.assertIn("pointerdown", self._html)
        self.assertIn("pointermove", self._html)

    def test_nav_arrows_and_dots_for_multislide(self):
        self.assertIn('id="nav-prev"', self._html)
        self.assertIn('id="nav-next"', self._html)
        self.assertIn('class="li-dot', self._html)
        self.assertIn("goToSlide(1)", self._html)  # a dot wired to slide index 1

    def test_active_panel_one_at_a_time(self):
        # Per-slide panels still hide all-but-active (edit one slide at a time).
        self.assertIn("slide-panel", self._html)
        self.assertIn("slide-counter", self._html)


class TestSingleSlideCarousel(unittest.TestCase):
    """With one slide, the track still exists but no nav arrows render."""

    def setUp(self):
        self._td = _make_pool_run_folder()
        self._html = build_editor_html(Path(self._td.name) / "run")

    def tearDown(self):
        self._td.cleanup()

    def test_track_present_no_arrows(self):
        self.assertIn('id="carousel-track"', self._html)
        self.assertNotIn('id="nav-prev"', self._html)


# ─────────────────────────────────────────────────────────────────────────────
# Editor v2 (AIOS-139 addendum): panel redesign, per-layer lock, comment pins,
# pipeline wiring. New behaviour locked below so a future refactor can't silently
# drop a section, the lock, the comment-pin persistence, or the pipeline wiring.
# ─────────────────────────────────────────────────────────────────────────────

def _make_v2_run_folder() -> tempfile.TemporaryDirectory:
    """A slide with one of every conditional zone type — text, pill, image, chrome —
    so the per-type section rules (Typography for text only; corner radius for image;
    no font-size on pill; toggle-only chrome) are all exercised in one build."""
    td = tempfile.TemporaryDirectory()
    root = Path(td.name)
    sd = root / "slide-01"
    sd.mkdir(parents=True)
    (sd / "template.html").write_text(
        "<!doctype html><html><head><meta charset='utf-8'></head><body>"
        '<div data-slot="HEAD">{{{HEAD}}}</div>'
        '<div data-slot="TAGPILL">{{{TAGPILL}}}</div>'
        '<div data-slot="PHOTO"><img src="photo.png" alt=""></div>'
        '<div data-slot="MAST">{{{MAST}}}</div>'
        "</body></html>",
        encoding="utf-8",
    )
    (sd / "instructions.md").write_text(
        "# S\n\n## Slots\n\n"
        "- **HEAD** — headline\n  - bbox: 4% 10% 90% 8%\n  - style: display, 7cqw\n  - sample: \"Hi\"\n"
        "- **TAGPILL** — category pill\n  - bbox: 4% 4% 20% 5%\n  - style: pill\n  - sample: \"NEW\"\n"
        "- **PHOTO** — main photo\n  - bbox: 6% 24% 88% 50%\n  - style: image, cover\n"
        "- **MAST** — masthead bar\n  - bbox: 0% 0% 100% 6%\n  - style: masthead chrome\n  - sample: \"@brand\"\n",
        encoding="utf-8",
    )
    return td


class TestEditorV2Panel(unittest.TestCase):
    """The generated panel matches the v2 mockup: indigo accent, panel-only fonts
    (no network <link>), single-scroll inspector (no Layers|Edit tabs), selection
    chip, and conditional sections driven per slot type."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_indigo_accent(self):
        # FASE 4 redesign: accent is the command-centre indigo #6366F1 (was #5B57D6).
        self.assertIn("#6366F1", self._html, "command-centre indigo accent not applied")

    def test_panel_fonts_stay_system_fallback(self):
        """Stage A relaxed CONS-01 for *slide* fonts (curated set via CDN), but the
        PANEL chrome must still use system-fallback stacks — no panel @font-face / no
        forcing the panel onto a network font. (--ui/--mono are plain fallback stacks.)"""
        self.assertIn("--ui:", self._html)
        self.assertIn("--mono:", self._html)
        self.assertIn("Hanken Grotesk", self._html)

    def test_panel_only_fonts_declared(self):
        """Panel UI fonts are panel-only system-fallback stacks (Hanken Grotesk /
        DM Mono if installed, else system). The slide is iframed so they never bleed."""
        self.assertIn("--ui:", self._html)
        self.assertIn("--mono:", self._html)
        self.assertIn("Hanken Grotesk", self._html)

    def test_single_scroll_no_panel_tabs(self):
        """v2 is one scroll, not Layers|Edit tabs — the old tab system is gone."""
        self.assertNotIn("panel-tab", self._html)
        self.assertNotIn("showTab", self._html)

    def test_selection_chip_present(self):
        self.assertIn('class="selbar"', self._html)
        self.assertIn("updateSelChip", self._html)

    def test_sections_in_mockup_order(self):
        """selection chip -> Layers -> Position & Size -> Appearance -> Typography."""
        layers = self._html.index(">Layers<")
        pos = self._html.index("Position &amp; Size")
        appe = self._html.index(">Appearance<")
        typo = self._html.index(">Typography<")
        self.assertLess(layers, pos)
        self.assertLess(pos, appe)
        self.assertLess(appe, typo)

    def test_typography_text_and_pill(self):
        """Typography is generated for TEXT and PILL control groups (r5f F1c — a
        pill is text in a badge, so it needs font size/family too), with the
        pill's fontSize range wired to applyToSlide. It never leaks into image."""
        text_block = re.search(
            r'data-control-type="text".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertIn("Typography", text_block)
        pill_block = re.search(
            r'data-control-type="pill".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertIn("Typography", pill_block)
        self.assertIn("'fontSize'", pill_block)
        image_block = re.search(
            r'data-control-type="image".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertNotIn("Typography", image_block)

    def test_corner_radius_image_not_text(self):
        """Corner radius (corner-field) appears for image, not for the text zone."""
        image_block = re.search(
            r'data-control-type="image".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertIn("corner-field", image_block)
        text_block = re.search(
            r'data-control-type="text".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertNotIn("corner-field", text_block)

    def test_nudge_pad_step_toggle(self):
        """Position has a nudge pad with a 1 / 8 / 24 px step toggle."""
        self.assertIn("setStep(1)", self._html)
        self.assertIn("setStep(8)", self._html)
        self.assertIn("setStep(24)", self._html)
        self.assertIn("function setStep", self._html)
        # the pad buttons call nudge with a direction, not a fixed delta
        self.assertIn("nudge('slide-01','HEAD','x',1)", self._html)
        self.assertIn("nudge('slide-01','HEAD','x',-1)", self._html)

    def test_nudge_converts_px_to_percent(self):
        """Nudge keeps positions in % (parity) but steps by px over the 1080x1350
        slide — the conversion must be in the JS, not a raw 1% step."""
        self.assertIn("nudgeStep", self._html)
        self.assertIn("SLIDE_W", self._html)
        self.assertIn("SLIDE_H", self._html)

    def test_pill_is_editable(self):
        """A real CALLOUT_PILL is a coloured badge with text (template-conventions.md
        `style: pill, brand-accent fill, white text`) — so the pill control must edit
        fill + text colour, not just content + position (review feedback)."""
        self.assertIn("applyToSlide('slide-01','TAGPILL','bgColor'", self._html)
        self.assertIn("applyToSlide('slide-01','TAGPILL','color'", self._html)

    def test_palette_decoupled_from_layer_fill(self):
        """The global brand-palette swatch sets ONLY the brand accent — it must not
        rewrite the selected layer's fill (two scopes; review feedback)."""
        self.assertIn("function applySwatch(hex) { applyGlobal('--brand-accent', hex); }", self._html)
        self.assertNotIn("syncFillUI", self._html)   # the old palette->fill coupling is gone


class TestLayerLock(unittest.TestCase):
    """Per-layer lock (new in v2): a lock button per layer, JS that disables the
    layer's inspector + blocks selection, state persisted in tweaksState."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_lock_button_per_layer(self):
        self.assertIn("actbtn--lk", self._html)
        self.assertIn("toggleLock('slide-01','HEAD',this)", self._html)

    def test_visibility_eye_still_present(self):
        """The eye (visibility) is the lock's sibling and must keep working."""
        self.assertIn("toggleVisible('slide-01','HEAD',this)", self._html)

    def test_lock_disables_and_blocks_selection(self):
        self.assertIn("function toggleLock", self._html)
        self.assertIn("st.locked = locked", self._html)            # persisted in state
        self.assertIn("el.disabled = locked", self._html)          # inputs disabled
        self.assertIn("data-locked", self._html)
        # selectZone refuses a locked row
        self.assertIn("getAttribute('data-locked') === '1'", self._html)

    def test_lock_key_ignored_by_rebake(self):
        """A `locked` key in the exported tweaks must not break render_template's
        CSS builder (it only reads known props) — proves preview-only lock state is
        safe to persist alongside real tweaks."""
        import render_template as rt
        css = rt._build_tweaks_css({"HEAD": {"locked": True, "x": 5}})
        self.assertIn("translate: 54px 0px", css)  # x=5 of 1080
        self.assertNotIn("locked", css)


class TestRemoveLayer(unittest.TestCase):
    """§4 remove asset: a trash button per layer row + removeLayer JS + a
    `removed` branch in applyToSlide that round-trips to the bake."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_no_trash_button_per_layer(self):
        # FASE 6 §3: the per-layer trash/delete icon is removed; the eye (hide) stays.
        self.assertNotIn("layer-trash", self._html)
        self.assertIn("layer-eye", self._html)

    def test_removeLayer_function_present(self):
        self.assertIn("function removeLayer", self._html)
        # Case A: LAYER_NN asset → hard delete the tweak entry
        self.assertIn("delete tweaksState[slideId][handle]", self._html)
        # Case B: template zone → removed:true flag (round-trips to bake)
        self.assertIn("'removed', true", self._html)

    def test_applyToSlide_has_removed_branch(self):
        self.assertIn("prop === 'removed'", self._html)

    def test_removed_flag_round_trips_to_bake(self):
        """The bake must honor removed:true with display:none (the round-trip gap
        this feature closes — a removed zone used to reappear in the PNG)."""
        import render_template as rt
        css = rt._build_tweaks_css({"HEAD": {"removed": True}})
        self.assertIn("display: none", css)


class TestCommentPins(unittest.TestCase):
    """Comment pins: click the stage to drop/edit/delete a note; persist in
    localStorage (keyed per run); preview-only — never the bake or tweaks.json."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_comment_layer_and_stage(self):
        self.assertIn('id="commentLayer"', self._html)
        self.assertIn('id="comment-stage"', self._html)
        self.assertIn('id="comment-hint"', self._html)

    def test_localstorage_persistence_keyed_per_run(self):
        self.assertIn("localStorage.setItem", self._html)
        self.assertIn("localStorage.getItem", self._html)
        self.assertIn("editor.comments.", self._html)
        self.assertIn("__EDITOR_RUN_ID__", self._html)

    def test_drop_edit_delete_composer(self):
        self.assertIn("function openComposer", self._html)
        self.assertIn("data-act=\"ok\"", self._html)
        self.assertIn("data-act=\"delete\"", self._html)
        self.assertIn("function renderPins", self._html)

    def test_pins_never_touch_tweaks_state(self):
        """The comment module is self-contained — it must not write into tweaksState
        (so an export carries no pin data). The initial tweaksState JSON has no
        'comments' key and the comment IIFE persists to localStorage only."""
        m = re.search(r"var tweaksState = (\{.*?\});", self._html, re.DOTALL)
        self.assertIsNotNone(m)
        state = json.loads(m.group(1))
        for k, v in state.items():
            if isinstance(v, dict):
                self.assertNotIn("comments", v)
        self.assertNotIn("tweaksState.comments", self._html)


def _make_brand_run_folder() -> tempfile.TemporaryDirectory:
    """A v2 run plus a sibling brand_context with palette colors + brand fonts, so
    Stage A (palette swatches + per-layer font, brand fonts pinned) is exercised."""
    td = _make_v2_run_folder()
    run = Path(td.name)
    vi = run / "brand_context" / "visual-identity"   # isolated inside the tmp run
    vi.mkdir(parents=True)
    (vi / "tokens.json").write_text(json.dumps({
        "colors": {"accent": "#5B57D6", "primary": "#1F2440",
                   "background": "#F4F2EE", "text": "#1B1B1B",
                   "accents": ["#2F9E6E", "#C7493B"]},
        "fonts": {"display": {"family": "Fraunces"}, "body": {"family": "Inter"}},
    }), encoding="utf-8")
    return td, vi


class TestStageATypographyColors(unittest.TestCase):
    """AIOS-139 Stage A: Global section = brand palette swatches; per-layer
    font-family (brand fonts pinned + curated set) with a Google-Fonts <link> in the
    slide so the chosen font survives the rebake; the broken global display-font is gone."""

    @classmethod
    def setUpClass(cls):
        cls._td, vi = _make_brand_run_folder()
        cls._html = build_editor_html(Path(cls._td.name), brand_context=vi)
        import html as _h, re as _r
        m = _r.search(r'srcdoc="([^"]*)"', cls._html, _r.DOTALL)
        cls._srcdoc = _h.unescape(m.group(1)) if m else ""

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_palette_swatches_with_hex(self):
        self.assertIn("swatch-chip", self._html)
        self.assertIn("#5B57D6", self._html)                 # accent swatch
        self.assertIn("#2F9E6E".upper(), self._html.upper())  # an accents[] extra
        self.assertIn("applySwatch(", self._html)

    def test_custom_picker_present(self):
        self.assertIn("swatch-sq--picker", self._html)

    def test_hardcoded_accent_removed(self):
        self.assertNotIn("#e25a45", self._html)

    def test_global_display_font_removed(self):
        """The broken global Display-font control (a <select> that set a CSS var the
        font never honored) is gone. (The brand's own `--type-display-family` token
        may still legitimately appear in the slide CSS — that's the brand, not the
        control; so assert on the removed control's handler, not the var name.)"""
        self.assertNotIn("applyGlobal('--type-display-family'", self._html)
        self.assertNotIn(">Display font<", self._html)
        self.assertNotIn("Display font", self._html)

    def test_per_layer_font_select(self):
        # Custom dropdown: applyToSlide is called from openEditorDrop JS, not inline.
        # The trigger carries the sid/handle/prop as data attributes instead.
        self.assertIn('data-prop="fontFamily"', self._html)
        self.assertIn('data-handle="HEAD"', self._html)
        # applyToSlide's fontFamily branch still exists in the JS engine.
        self.assertIn("prop === 'fontFamily'", self._html)

    def test_brand_fonts_pinned_library_hidden(self):
        # Fix #9: when brand fonts exist, only the Brand group is shown — Library
        # (curated fonts) is suppressed so the picker stays clean.
        # Font selector is a custom dropdown: options are JSON-encoded (HTML-escaped)
        # in data-opts. Words without special chars appear literally in the attribute.
        self.assertIn("Brand", self._html)    # group header word present in the JSON
        self.assertIn("Fraunces", self._html) # brand font name
        self.assertNotIn('"g": "Library"', self._html)  # Library group absent when brand fonts exist
        # Confirm it's the custom trigger, not a native <select>
        self.assertIn('class="csel-trigger"', self._html)

    def test_font_select_only_for_text(self):
        """Font selector lives in the text Typography section, not on image/pill."""
        img_block = re.search(r'data-control-type="image".*?(?=data-control-type=|</aside>)',
                              self._html, re.DOTALL).group(0)
        self.assertNotIn("'fontFamily'", img_block)

    def test_google_fonts_link_in_slide(self):
        """The curated <link> is injected into the slide srcdoc (so the iframe loads
        the fonts) — the parity counterpart of the bake-side injection."""
        self.assertIn("fonts.googleapis.com", self._srcdoc)
        self.assertIn("css2?family=Inter", self._srcdoc)
        self.assertIn("Playfair+Display", self._srcdoc)

    def test_same_link_builder_as_bake(self):
        """Editor + bake must share ONE link builder so preview == rebaked PNG."""
        import render_template as rt
        link = rt.build_google_fonts_link()
        # the curated families requested by the bake builder appear in the slide too
        self.assertIn("family=Sora", link)
        self.assertIn("family=Sora", self._srcdoc)

    def test_google_fonts_link_in_shell_head(self):
        """The shell <head> (top document, not iframe) must include the Google Fonts
        link so the font-family dropdown options render in their own typeface."""
        # The link must appear BEFORE the first <style> tag (i.e. in the <head>)
        head_end = self._html.find("<style>")
        head_section = self._html[:head_end] if head_end != -1 else self._html
        self.assertIn("fonts.googleapis.com", head_section,
                      "Google Fonts link missing from shell <head>")
        self.assertIn("css2?family=Inter", head_section)
        self.assertIn("Space+Grotesk", head_section)
        self.assertIn("Sora", head_section)


def _make_import_run_folder() -> tempfile.TemporaryDirectory:
    """A v2 run with an existing tweaks.json + comments.json + a baked slide PNG on
    disk — exercises Stage B import/resume + the PNG-via-bake link."""
    td = _make_v2_run_folder()
    run = Path(td.name)
    (run / "tweaks.json").write_text(json.dumps({
        "slide-01": {"HEAD": {"fontSize": 9, "fontFamily": "Sora"}},
        "global": {"accent": "#5B57D6"},
    }), encoding="utf-8")
    (run / "comments.json").write_text(json.dumps({
        "slide-01": [{"id": "c1", "xPct": 40.0, "yPct": 15.0, "zone": "HEAD",
                      "text": "make this smaller"}],
    }), encoding="utf-8")
    # a 1x1 PNG so SLIDE_PNGS picks the slide up
    (run / "slide-01.png").write_bytes(bytes.fromhex(
        "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4"
        "890000000a49444154789c6360000002000154a24f8d0000000049454e44ae426082"
    ))
    return td


def _make_rootbg_run_folder() -> tempfile.TemporaryDirectory:
    """A slide whose background lives on the root `.slide` (a CSS/inline bg, no
    `div.bg`) — Stage B must surface it as an editable BACKGROUND layer."""
    td = tempfile.TemporaryDirectory()
    sd = Path(td.name) / "slide-01"
    sd.mkdir(parents=True)
    (sd / "template.html").write_text(
        "<!doctype html><html><head><meta charset='utf-8'></head><body>"
        '<div class="slide" style="background:#111">'
        '<div data-slot="HEAD">{{{HEAD}}}</div></div>'
        "</body></html>", encoding="utf-8")
    (sd / "instructions.md").write_text(
        "# S\n\n## Slots\n\n- **HEAD** — headline\n  - bbox: 6% 20% 88% 10%\n  - style: display, 7cqw\n  - sample: \"Hi\"\n",
        encoding="utf-8")
    return td


class TestBrandContextResolve(unittest.TestCase):
    """Regression: a brand_context sitting next to the run (depth 0/1) must be found
    by auto-resolve, so the editor renders the brand palette/fonts without an explicit
    --brand-context. The earlier range(3,7) skipped these shallow depths."""

    def test_resolves_adjacent_brand_context(self):
        import preview_editor as pe
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "brand_context" / "visual-identity").mkdir(parents=True)
            (root / "brand_context" / "visual-identity" / "tokens.json").write_text(
                json.dumps({"colors": {"accent": "#5B57D6"}}), encoding="utf-8")
            run = root / "run"
            run.mkdir()
            self.assertEqual(pe._resolve_brand_context(run, None),
                             root / "brand_context")   # depth 1, was missed before

    def test_resolves_brand_context_inside_run(self):
        import preview_editor as pe
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "brand_context").mkdir()
            self.assertEqual(pe._resolve_brand_context(run, None), run / "brand_context")  # depth 0

    def test_palette_renders_via_autoresolve(self):
        """End-to-end: with brand_context adjacent to the run (no explicit arg), the
        editor renders the brand palette — the demo regression."""
        td, vi = _make_brand_run_folder()   # brand_context at <run>/brand_context
        try:
            html = build_editor_html(Path(td.name))   # NO brand_context arg
            self.assertIn("swatch-chip", html)
            self.assertIn("#5B57D6", html)
            self.assertNotIn("No brand palette", html)
        finally:
            td.cleanup()


class TestStageBReview(unittest.TestCase):
    """AIOS-139 Stage B: slide-anchored comments (canvas %, nearest zone) +
    comments.json export, import/resume, PNG-via-bake links, background-as-layer."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    # ── nearest-zone resolver (Python; JS mirrors it) ──
    def test_nearest_zone_python(self):
        import preview_editor as pe
        bbs = [{"handle": "HEAD", "x": 6, "y": 20, "w": 88, "h": 22},
               {"handle": "PHOTO", "x": 6, "y": 46, "w": 88, "h": 46}]
        self.assertEqual(pe._nearest_zone(bbs, 40, 25), "HEAD")     # inside HEAD
        self.assertEqual(pe._nearest_zone(bbs, 50, 60), "PHOTO")    # inside PHOTO
        self.assertEqual(pe._nearest_zone(bbs, 50, 2), "HEAD")      # above all → nearest centre
        self.assertIsNone(pe._nearest_zone([], 5, 5))

    def test_nearest_zone_smallest_containing(self):
        import preview_editor as pe
        bbs = [{"handle": "BG", "x": 0, "y": 0, "w": 100, "h": 100},
               {"handle": "CARD", "x": 20, "y": 20, "w": 30, "h": 30}]
        self.assertEqual(pe._nearest_zone(bbs, 30, 30), "CARD")     # smallest containing wins

    def test_slot_bboxes_injected(self):
        self.assertIn("SLOT_BBOXES =", self._html)
        self.assertIn('"handle": "HEAD"', self._html.replace("'", '"') or self._html)

    # ── anchored comments ──
    def test_comments_anchored_per_slide(self):
        self.assertIn("xPct", self._html)
        self.assertIn("yPct", self._html)
        self.assertIn("function nearestZone", self._html)
        self.assertIn("window.__activeSlide", self._html)
        self.assertIn("__renderPins", self._html)   # pins ride the carousel

    def test_export_includes_comments_json(self):
        self.assertIn("downloadJSON(comments, 'comments.json')", self._html)
        self.assertIn("__getComments", self._html)

    def test_export_diffs_against_defaults(self):
        """The export must ship ONLY the user's real edits — diff tweaksState vs the
        template DEFAULTS — so an untouched default (e.g. fontSize) is never applied
        on rebake (which would shrink the headline / drift from the editor)."""
        self.assertIn("var DEFAULTS =", self._html)
        self.assertIn("function diffTweaks", self._html)
        # FASE 5: edits are live + saved server-side (no tweaks.json download); diffTweaks
        # still ships ONLY real edits (diffed vs DEFAULTS) via the live __getTweaks path.
        self.assertIn("window.__getTweaks = diffTweaks", self._html)

    def test_defaults_match_initial_state(self):
        """DEFAULTS is the template's natural state; with no saved tweaks it equals the
        initial tweaksState (so a no-edit export diffs to empty)."""
        defaults = json.loads(re.search(r"var DEFAULTS = (\{.*?\});", self._html, re.DOTALL).group(1))
        state = json.loads(re.search(r"var tweaksState = (\{.*?\});", self._html, re.DOTALL).group(1))
        self.assertEqual(defaults, state)   # no tweaks.json on disk → identical

    def test_pins_never_in_tweaks(self):
        m = re.search(r"var tweaksState = (\{.*?\});", self._html, re.DOTALL)
        state = json.loads(m.group(1))
        for v in state.values():
            if isinstance(v, dict):
                self.assertNotIn("comments", v)
        # comments live in their own module/var, not tweaksState
        self.assertNotIn("tweaksState.comments", self._html)

    def test_no_png_buttons(self):
        """PNG download removed — editor is 100% static HTML (can't bake/rasterize
        faithfully in-browser); edited PNGs come from the apply-back rebake."""
        self.assertNotIn("downloadSlidePNG", self._html)
        self.assertNotIn("downloadAllPNGs", self._html)
        self.assertNotIn("png-btn", self._html)
        self.assertNotIn("html2canvas", self._html)   # never a client rasterizer (CONS-01)

    def test_export_button_label_for_claude(self):
        """The export button reads as a 'paste into Claude' action so the user knows
        what to do with the output."""
        self.assertIn("paste into Claude", self._html)

    def test_no_leftover_sentinels(self):
        leftover = [s for s in re.findall(r"__[A-Z_]+__", self._html)
                    if s != "__EDITOR_RUN_ID__"]   # that one is a real JS global
        self.assertEqual(leftover, [], f"unreplaced sentinels: {leftover}")


class TestStageBImportResume(unittest.TestCase):
    """Re-opening with an existing tweaks.json + comments.json restores edits + pins;
    the baked PNG is offered for download."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_import_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_imported_tweaks_applied_on_load(self):
        m = re.search(r"var IMPORTED_TWEAKS = (\{.*?\});", self._html, re.DOTALL)
        self.assertIsNotNone(m)
        imp = json.loads(m.group(1))
        self.assertEqual(imp["slide-01"]["HEAD"]["fontSize"], 9)
        self.assertEqual(imp["slide-01"]["HEAD"]["fontFamily"], "Sora")
        self.assertIn("applySavedTweaks", self._html)

    def test_tweaks_merged_into_state(self):
        """The saved tweak is merged over the computed defaults so export round-trips it."""
        m = re.search(r"var tweaksState = (\{.*?\});", self._html, re.DOTALL)
        state = json.loads(m.group(1))
        self.assertEqual(state["slide-01"]["HEAD"]["fontSize"], 9)

    def test_imported_comments_restored(self):
        m = re.search(r"var INITIAL_COMMENTS = (\{.*?\});", self._html, re.DOTALL)
        ic = json.loads(m.group(1))
        self.assertEqual(ic["slide-01"][0]["text"], "make this smaller")
        self.assertEqual(ic["slide-01"][0]["zone"], "HEAD")

    def test_no_png_embedding(self):
        """PNG download was removed (100% static HTML) — the editor must NOT embed
        baked PNGs (keeps the file small; edited PNGs come from the rebake)."""
        self.assertNotIn("SLIDE_PNGS", self._html)

    def test_fresh_run_imports_nothing(self):
        """A run with no tweaks.json/comments.json imports empty — fresh defaults
        are NOT replayed (that would break parity)."""
        td2 = _make_v2_run_folder()
        try:
            html = build_editor_html(Path(td2.name))
            m = re.search(r"var IMPORTED_TWEAKS = (\{.*?\});", html, re.DOTALL)
            self.assertEqual(json.loads(m.group(1)), {})
            m2 = re.search(r"var INITIAL_COMMENTS = (\{.*?\});", html, re.DOTALL)
            self.assertEqual(json.loads(m2.group(1)), {})
        finally:
            td2.cleanup()


class TestStageBBackgroundLayer(unittest.TestCase):
    """Background-as-layer: a root `.slide` background becomes an editable BACKGROUND
    layer; `_tag_decor` is identical in editor + bake (parity)."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_rootbg_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_background_layer_present(self):
        self.assertIn('data-slot="BACKGROUND"', self._html)
        self.assertIn("applyToSlide('slide-01','BACKGROUND','bgColor'", self._html)

    def test_tag_decor_parity_with_bake(self):
        import preview_editor as pe
        import render_template as rt
        html = '<html><head></head><body><div class="slide" style="background:#111">x</div></body></html>'
        self.assertEqual(pe._tag_decor(html), rt._tag_decor(html))
        self.assertIn('data-slot="BACKGROUND"', pe._tag_decor(html))

    def test_div_bg_still_wins(self):
        import preview_editor as pe
        html = '<body><div class="bg"></div><div class="slide"></div></body>'
        out = pe._tag_decor(html)
        self.assertEqual(out.count('data-slot="BACKGROUND"'), 1)   # not double-tagged

    def test_background_tweak_rebakes(self):
        """A BACKGROUND bgColor tweak emits a CSS rule the bake honors (parity)."""
        import render_template as rt
        css = rt._build_tweaks_css({"BACKGROUND": {"bgColor": "#222222"}})
        self.assertIn('[data-slot="BACKGROUND"]', css)
        self.assertIn("background: #222222", css)
        # Must be !important: the synthetic root BACKGROUND layer carries an INLINE
        # `background:inherit`, and inline beats a plain stylesheet rule — so without
        # !important the recolor is silently ignored in the bake (the bug this guards).
        self.assertIn("background: #222222 !important", css)


class TestPipelineWiring(unittest.TestCase):
    """The editor is wired into the real pipeline: Phase 7.5 calls preview_editor.py
    and Phase 7.6 is the apply-back rebake. Smoke-checks the docs the orchestrator
    actually reads (SKILL.md + pipeline-phases.md)."""

    @classmethod
    def setUpClass(cls):
        skills = _SCRIPT_DIR.parents[2]   # .../skills (content-studio is one level deeper than old mkt-vi/scripts)
        cls._skill = (skills / "00-social-content" / "SKILL.md").read_text(encoding="utf-8")
        cls._phases = (skills / "00-social-content" / "references" / "pipeline-phases.md").read_text(encoding="utf-8")

    def test_skill_phase_75_calls_editor(self):
        self.assertIn("preview_editor.py", self._skill)
        self.assertIn("**7.5**", self._skill)

    def test_skill_has_phase_76_apply_back(self):
        self.assertIn("**7.6**", self._skill)
        self.assertIn("--tweaks", self._skill)
        # no-AI guarantee stated
        self.assertIn("NO AI", self._skill.upper())

    def test_phases_doc_editor_and_apply_back(self):
        self.assertIn("preview_editor.py", self._phases)
        self.assertIn("Phase 7.6", self._phases)
        self.assertIn("render_template.py", self._phases)
        self.assertIn("--tweaks", self._phases)

    def test_carousel_kept_as_fallback(self):
        """preview_carousel.py stays referenced as the read-only fallback (PRD)."""
        self.assertIn("preview_carousel.py", self._skill)


class TestFullAiLayer(unittest.TestCase):
    """Addendum 5 Fix #2: a full-AI (flat image) slide must appear as a selectable
    layer carrying the magic-pencil break-into-layers affordance + a decompose-only
    disclaimer — not 'no editable layers'."""

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        run = Path(self._td.name)
        # A bare slide-01.png (no _slides/, no slide-01/ dir) → full-AI slide
        # (template_dir=None) via _find_slides_info's final fallback.
        (run / "slide-01.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00fake")
        self._html = build_editor_html(run)

    def tearDown(self):
        self._td.cleanup()

    def test_fullai_appears_as_a_layer_row(self):
        # The layers panel must show a real row for the AI image (not the old
        # 'no editable layers' message), selectable via selectZone.
        self.assertIn('class="layer-row layer-fullai"', self._html)
        self.assertIn('data-fullai="1"', self._html)
        self.assertIn(">AI image<", self._html)
        self.assertIn("selectZone('slide-01','BACKGROUND')", self._html)
        self.assertNotIn("Full-AI slide — no editable layers.", self._html)

    def test_layer_row_has_magic_pencil(self):
        # The row carries the magic-pencil button wired to break-into-layers.
        self.assertIn('class="actbtn layer-magic"', self._html)
        self.assertIn("window.__studioBreakIntoLayers('slide-01')", self._html)

    def test_inspector_has_decompose_only_disclaimer(self):
        # Selecting the image shows a disclaimer that direct edits are gated behind
        # 'break into layers' + the same pencil action.
        self.assertIn('class="control-group control-fullai"', self._html)
        self.assertIn('data-slot="BACKGROUND"', self._html)
        self.assertIn("break it into layers", self._html)
        self.assertIn('class="magic-break-btn"', self._html)


class TestCommentMode(unittest.TestCase):
    """AIOS-139 Addendum 9 #4 — comment pin-drop is gated behind an explicit mode so
    it never conflicts with caption/canvas editing; the hint follows that mode."""

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        run = Path(self._td.name)
        (run / "slide-01.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00fake")
        self._html = build_editor_html(run)

    def tearDown(self):
        self._td.cleanup()

    def test_pin_drop_gated_on_comment_mode(self):
        self.assertIn("if (!window.__commentMode) return;", self._html)

    def test_hint_follows_comment_mode(self):
        # the hint is shown only while comment mode is armed (not by comment count)
        self.assertIn("hint.style.display = window.__commentMode ? '' : 'none'", self._html)

    def test_set_comment_mode_hook_exposed(self):
        self.assertIn("window.__setCommentMode", self._html)


class TestEmitEditSlideContract(unittest.TestCase):
    """AIOS-139 FASE 7 #1 (Addendum 8) — the run-folder editing contract.

    render_template --emit-edit-slide writes _slides/slide-N/ (template.html +
    metadata.json{data}) for templated slides + a shared _slides/_shared/. The
    editor must: treat _shared as NOT a slide, keep flat full-AI PNGs in the
    carousel alongside the templated _slides entries (in order), and use the
    persisted real `data` as the live baseline."""

    def setUp(self):
        import preview_editor as _pe
        self._pe = _pe
        self._td = tempfile.TemporaryDirectory()
        self.run = Path(self._td.name)
        # A realistic mixed run: slide-01/03 templated (have _slides dirs),
        # slide-02 full-AI (flat PNG only). Plus the _shared dir from the writer.
        for n in ("01", "02", "03"):
            (self.run / f"slide-{n}.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00fake")
        slides = self.run / "_slides"
        (slides / "_shared").mkdir(parents=True)
        (slides / "_shared" / "styles.css").write_text("body{}", encoding="utf-8")
        for n, head in (("01", "First headline"), ("03", "Third headline")):
            sd = slides / f"slide-{n}"
            sd.mkdir(parents=True)
            (sd / "template.html").write_text(
                '<div class="slide"><div data-slot="HEADLINE">{{HEADLINE}}</div></div>',
                encoding="utf-8")
            (sd / "instructions.md").write_text(
                "## Slots\n- name: HEADLINE\n  sample: sample text\n", encoding="utf-8")
            (sd / "metadata.json").write_text(
                json.dumps({"slide_id": f"slide-{n}", "data": {"HEADLINE": head}}),
                encoding="utf-8")

    def tearDown(self):
        self._td.cleanup()

    def test_shared_is_not_a_slide(self):
        info = self._pe._find_slides_info(self.run)
        ids = [d["slide_id"] for d in info]
        self.assertNotIn("_shared", ids)

    def test_flat_png_kept_in_order_with_templated(self):
        info = self._pe._find_slides_info(self.run)
        ids = [d["slide_id"] for d in info]
        # All three slides present, in slide-number order (no dropped full-AI).
        self.assertEqual(ids, ["slide-01", "slide-02", "slide-03"])
        by = {d["slide_id"]: d for d in info}
        self.assertIsNotNone(by["slide-01"]["template_dir"])  # templated
        self.assertIsNone(by["slide-02"]["template_dir"])     # full-AI flat
        self.assertIsNotNone(by["slide-03"]["template_dir"])

    def test_real_data_carried_from_metadata(self):
        info = self._pe._find_slides_info(self.run)
        by = {d["slide_id"]: d for d in info}
        self.assertEqual(by["slide-01"]["data"], {"HEADLINE": "First headline"})

    def test_real_data_renders_over_sample_text(self):
        html = build_editor_html(self.run)
        # The persisted real copy wins over the instructions.md sample text.
        self.assertIn("First headline", html)
        self.assertNotIn("sample text", html)


class TestRichNonSlideNNDir(unittest.TestCase):
    """Audit #11 — a RICH emitted slide dir named after the output stem (e.g.
    `preview`, not `slide-NN`) carrying metadata.json{data} + template.html must
    NOT be silently dropped by the slide-NN-only filter. It is grafted onto a
    stable slide id (existing slide-NN, else slide-01) and becomes editable."""

    def setUp(self):
        import preview_editor as _pe
        self._pe = _pe
        self._td = tempfile.TemporaryDirectory()
        self.run = Path(self._td.name)

    def tearDown(self):
        self._td.cleanup()

    def _make_rich_dir(self, name="preview"):
        slides = self.run / "_slides"
        sd = slides / name
        sd.mkdir(parents=True)
        (sd / "template.html").write_text(
            '<div class="slide"><div data-slot="HEADLINE">{{HEADLINE}}</div></div>',
            encoding="utf-8")
        (sd / "instructions.md").write_text(
            "## Slots\n- name: HEADLINE\n  sample: sample text\n", encoding="utf-8")
        (sd / "metadata.json").write_text(
            json.dumps({"slide_id": name,
                        "data": {"HEADLINE": "Hero copy", "PHOTO_MAIN_PATH": "hero.png"}}),
            encoding="utf-8")
        return sd

    def test_preview_named_rich_dir_is_editable(self):
        # No flat PNG, no slide-NN dir — only _slides/preview/ with rich data.
        self._make_rich_dir("preview")
        info = self._pe._find_slides_info(self.run)
        self.assertEqual(len(info), 1)
        d = info[0]
        # Grafted onto a stable slide id (slide-01 when none exists).
        self.assertEqual(d["slide_id"], "slide-01")
        self.assertIsNotNone(d["template_dir"])
        self.assertIsNotNone(d["template"])
        self.assertEqual(d["data"], {"HEADLINE": "Hero copy", "PHOTO_MAIN_PATH": "hero.png"})

    def test_grafts_onto_existing_slide_nn_without_double_count(self):
        # A flat slide-01.png exists (full-AI flat) + a rich `preview` dir → the
        # rich data enriches slide-01, not a second entry.
        (self.run / "slide-01.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00fake")
        self._make_rich_dir("preview")
        info = self._pe._find_slides_info(self.run)
        ids = [d["slide_id"] for d in info]
        self.assertEqual(ids, ["slide-01"])  # no double-count
        d = info[0]
        self.assertEqual(d["data"], {"HEADLINE": "Hero copy", "PHOTO_MAIN_PATH": "hero.png"})
        self.assertIsNotNone(d["template_dir"])

    def test_shared_is_never_treated_as_rich_slide(self):
        slides = self.run / "_slides"
        (slides / "_shared").mkdir(parents=True)
        (slides / "_shared" / "styles.css").write_text("body{}", encoding="utf-8")
        # _shared alone yields no slides.
        self.assertEqual(self._pe._find_slides_info(self.run), [])

    def test_malformed_metadata_does_not_throw(self):
        slides = self.run / "_slides"
        sd = slides / "preview"
        sd.mkdir(parents=True)
        (sd / "metadata.json").write_text("{ not json", encoding="utf-8")
        # No template.html, broken metadata → skipped, no exception, no slides.
        self.assertEqual(self._pe._find_slides_info(self.run), [])

    def test_existing_slide_nn_dirs_unaffected(self):
        # Regression: a normal slide-01/slide-02 run with NO rich alias dir is
        # returned exactly as before.
        slides = self.run / "_slides"
        for n in ("01", "02"):
            (self.run / f"slide-{n}.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00fake")
            sd = slides / f"slide-{n}"
            sd.mkdir(parents=True)
            (sd / "template.html").write_text(
                '<div class="slide"></div>', encoding="utf-8")
            (sd / "metadata.json").write_text(
                json.dumps({"slide_id": f"slide-{n}", "data": {"HEADLINE": f"H{n}"}}),
                encoding="utf-8")
        info = self._pe._find_slides_info(self.run)
        self.assertEqual([d["slide_id"] for d in info], ["slide-01", "slide-02"])
        self.assertEqual(info[0]["data"], {"HEADLINE": "H01"})

    def test_content_textarea_seeds_from_live_value(self):
        """Audit #1/#9: the Content textarea seeds from the LIVE rendered copy
        (metadata.json `data`) so the panel matches the canvas + rebake, not the
        instructions.md sample. Uses the bold-style instructions the parser supports."""
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            run = Path(d) / "run"
            sd = run / "_slides" / "slide-01"
            sd.mkdir(parents=True)
            (sd / "template.html").write_text(
                '<div class="slide"><div data-slot="HEAD">{{HEAD}}</div></div>',
                encoding="utf-8")
            (sd / "instructions.md").write_text(
                "## Slots\n- **HEAD** — headline\n  - bbox: 4% 10% 90% 8%\n"
                "  - style: display, 7cqw\n  - sample: \"sample copy\"\n",
                encoding="utf-8")
            (sd / "metadata.json").write_text(
                json.dumps({"slide_id": "slide-01", "data": {"HEAD": "Live copy"}}),
                encoding="utf-8")
            html = _pe.build_editor_html(run)
            m = re.search(
                r"applyToSlide\('slide-01','HEAD','text',this\.value\)\">([^<]*)</textarea>",
                html)
            self.assertIsNotNone(m, "HEAD content textarea not found")
            self.assertEqual(m.group(1), "Live copy")

    def test_content_textarea_preserves_inline_markup(self):
        """A live value with <mark> seeds the textarea as escaped source (so the
        user edits the real markup), while the iframe renders the highlight. The
        bake renders the same text tweak RAW → live == PNG (audit #2)."""
        import preview_editor as _pe
        with tempfile.TemporaryDirectory() as d:
            run = Path(d) / "run"
            sd = run / "_slides" / "slide-01"
            sd.mkdir(parents=True)
            (sd / "template.html").write_text(
                '<div class="slide"><div data-slot="HEAD">{{HEAD}}</div></div>',
                encoding="utf-8")
            (sd / "instructions.md").write_text(
                "## Slots\n- **HEAD** — headline\n  - bbox: 4% 10% 90% 8%\n"
                "  - style: display, 7cqw\n  - sample: \"x\"\n",
                encoding="utf-8")
            (sd / "metadata.json").write_text(
                json.dumps({"slide_id": "slide-01",
                            "data": {"HEAD": "Big <mark>idea</mark>"}}),
                encoding="utf-8")
            html = _pe.build_editor_html(run)
            # Textarea source is escaped so the markup is editable, not collapsed.
            self.assertIn("Big &lt;mark&gt;idea&lt;/mark&gt;", html)


class TestTexturePanel(unittest.TestCase):
    """Texture overlay plumbing. FASE 5: the CONTROL moved to the global topbar
    (studio.js); preview_editor keeps the data + the parameterized API it drives."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_texture_set_embedded(self):
        # the curated textures are embedded as a JS map of data URIs (parity-safe)
        self.assertIn("window.__TEXTURES", self._html)
        self.assertIn('"paper"', self._html)
        self.assertIn("data:image/png;base64,", self._html)

    def test_texture_moved_out_of_per_slide_panel(self):
        # FASE 5 §4: the texture control is no longer a per-slide panel section.
        self.assertNotIn('class="section texture-section"', self._html)
        self.assertNotIn('class="tex-name"', self._html)

    def test_texture_api_exposed_for_topbar(self):
        h = self._html
        self.assertIn("window.__setTexture", h)     # topbar dropdown writes the active slide's texture
        self.assertIn("window.__getTexture", h)     # reflects current value back to the topbar
        self.assertIn("window.__textureNames", h)


class TestCommandCentrePalette(unittest.TestCase):
    """FASE 4 redesign: command-centre visual language — cream stage + dark floating panel."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_command_centre_palette(self):
        h = self._html
        self.assertIn("#FCF9F7", h)                 # cream stage bg
        self.assertIn("#1B1C1B", h)                 # ink
        self.assertIn("#93452A", h)                 # terracotta primary
        self.assertIn("#B25D3F", h)                 # terracotta secondary
        self.assertIn("#6366F1", h)                 # indigo accent
        self.assertIn("rgba(147,69,42,.06)", h)     # soft command-centre shadow

    def test_panel_is_dark_and_floating(self):
        h = self._html
        # the panel re-maps the semantic vars to a dark scheme
        self.assertIn("--ink: #F3EFEA", h)
        # floating, vertically-centered, detached, rounded card (FASE 5: + depth/glow)
        self.assertIn("align-self: center", h)
        self.assertIn("border-radius: 18px", h)

    def test_topbar_logo_and_actions_host(self):
        # FASE 5: the topbar shows the Agentic OS LOGO (not "Content Studio" text) + a
        # host where studio.js injects the left-clustered action pills.
        h = self._html
        self.assertIn('class="brand-logo"', h)
        self.assertIn("/agentic-logo.png", h)
        self.assertIn('id="topbar-actions"', h)

    def test_export_button_is_comments_only(self):
        # FASE 5 §7: the stale "export changes (tweaks)" round-trip is gone; only the
        # comments→Claude round-trip remains.
        h = self._html
        self.assertIn("Send comments to Claude", h)
        self.assertIn("exportComments()", h)
        self.assertNotIn("Export changes", h)

    def test_caption_is_editable(self):
        # FASE 6 §5: the LinkedIn caption is contenteditable and exposed for persistence.
        h = self._html
        self.assertIn('id="li-caption"', h)
        self.assertIn('contenteditable="true"', h)
        self.assertIn("window.__getCaption", h)

    def test_caption_scrollable_into_view(self):
        # FASE 6 §4: `safe center` keeps the caption (top of the mock) scroll-reachable
        # when the mock is taller than the stage (instead of being clipped by centering).
        self.assertIn("align-items: safe center", self._html)


class TestCustomDropdown(unittest.TestCase):
    """Custom dropdown replaces native <select> in the dark panel (UX fix — contrast).

    Verifies that the font-family and scale selectors use the custom .csel-trigger
    pattern so they stay readable in the dark panel (native <option> elements inherit
    the white foreground and render invisible on bright browser popup backgrounds).
    """

    @classmethod
    def setUpClass(cls):
        cls._td, vi = _make_brand_run_folder()
        cls._html = build_editor_html(Path(cls._td.name), brand_context=vi)

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_font_select_is_custom_not_native(self):
        """Font selector must be a .csel-trigger, never a native <select>."""
        self.assertIn('class="csel-trigger"', self._html)
        self.assertIn('data-prop="fontFamily"', self._html)
        # No native <select> must carry fontFamily as an inline event handler.
        self.assertNotIn("select onchange=\"applyToSlide('slide-01','HEAD','fontFamily'", self._html)

    def test_font_options_brand_only_when_brand_fonts_exist(self):
        """Fix #9: when brand fonts exist the Library group is suppressed entirely.
        The brand context used here has Fraunces + Inter, so only the Brand group
        should appear in data-opts — curated fonts must be absent."""
        # Brand group header and brand font names must be present
        self.assertIn("Brand", self._html)
        self.assertIn("Fraunces", self._html)
        self.assertIn("Inter", self._html)
        # Library group and curated-only fonts must NOT appear
        # (DM Sans is curated-only; verify at least one is absent)
        from preview_editor import CURATED_FONTS as _CF
        # All curated fonts that are NOT also brand fonts should be absent from data-opts
        brand_fonts = {"Fraunces", "Inter"}
        for name, _ in _CF:
            if name not in brand_fonts:
                self.assertNotIn(
                    f'"v": "{name}"', self._html,
                    f"Curated font '{name}' unexpectedly present in data-opts when brand fonts exist",
                )

    def test_scale_is_custom_not_native(self):
        """Scale selector must be a .csel-trigger, not a native <select>."""
        self.assertIn('data-prop="scale"', self._html)
        self.assertNotIn(
            "select onchange=\"applyToSlide('slide-01','PHOTO_MAIN','scale'",
            self._html,
        )

    def test_openEditorDrop_js_present(self):
        """openEditorDrop must be defined in the embedded JS."""
        self.assertIn("function openEditorDrop", self._html)
        self.assertIn("window.openEditorDrop", self._html)

    def test_ed_pop_css_present(self):
        """The .ed-pop popup styles must be present (not depending on studio.js)."""
        self.assertIn(".ed-pop", self._html)
        self.assertIn(".ed-opt", self._html)
        self.assertIn(".csel-trigger", self._html)


# ---------------------------------------------------------------------------
# r5f F2b — srcdoc heals root-loose refs via metadata's source_template_dir
# ---------------------------------------------------------------------------

class TestSrcdocSourceTemplateDirFallback(unittest.TestCase):
    """An ALREADY-EMITTED slide dir may lack a template-root ref (older
    emit_edit_slide copied only assets/ + _ai_bg/ — statement-headline's bg.png
    404'd → white editor background). _build_srcdoc must run a SECOND
    _inline_relative_urls pass against metadata.json's source_template_dir so
    the leftover ref still resolves."""

    def setUp(self):
        from preview_editor import _build_srcdoc
        self._build_srcdoc = _build_srcdoc
        self._td = tempfile.TemporaryDirectory()
        root = Path(self._td.name)
        # Source template dir HAS bg.png; the emitted slide dir does NOT.
        self.source = root / "brand" / "templates" / "pool" / "statement"
        self.source.mkdir(parents=True)
        (self.source / "bg.png").write_bytes(
            base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAA"
                             "fFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="))
        self.slide = root / "run" / "_slides" / "slide-01"
        self.slide.mkdir(parents=True)
        (self.slide / "template.html").write_text(
            "<!doctype html><html><head><style>"
            ".slide{background:url('bg.png')}</style></head>"
            "<body><div class='slide'><img src=\"bg.png\" class=\"bg\">"
            "<h1 data-slot=\"HEADLINE\">{{{HEADLINE}}}</h1></div></body></html>",
            encoding="utf-8")

    def tearDown(self):
        self._td.cleanup()

    def test_unresolved_ref_heals_against_source_template_dir(self):
        srcdoc = self._build_srcdoc(
            template_path=self.slide / "template.html",
            data={"HEADLINE": "Hi"},
            tokens_css="",
            shared_css_content="",
            source_template_dir=self.source,
        )
        self.assertNotIn("url('bg.png')", srcdoc, "css ref must not stay relative")
        self.assertNotIn('src="bg.png"', srcdoc, "img ref must not stay relative")
        self.assertIn("data:image/png;base64,", srcdoc)

    def test_without_fallback_ref_stays_unresolved(self):
        # Control: the old behaviour (no source_template_dir) leaves the 404.
        srcdoc = self._build_srcdoc(
            template_path=self.slide / "template.html",
            data={"HEADLINE": "Hi"},
            tokens_css="",
            shared_css_content="",
        )
        self.assertIn("url('bg.png')", srcdoc)

    def test_local_file_wins_over_fallback(self):
        # A ref the slide dir DOES carry must resolve locally (authoritative copy),
        # not against the source dir.
        (self.slide / "bg.png").write_bytes(b"LOCAL-BYTES-WIN")
        srcdoc = self._build_srcdoc(
            template_path=self.slide / "template.html",
            data={"HEADLINE": "Hi"},
            tokens_css="",
            shared_css_content="",
            source_template_dir=self.source,
        )
        local_b64 = base64.b64encode(b"LOCAL-BYTES-WIN").decode("ascii")
        self.assertIn(local_b64, srcdoc)

    def test_find_slides_info_plumbs_source_template_dir(self):
        from preview_editor import _find_slides_info
        (self.slide / "metadata.json").write_text(
            json.dumps({
                "slide_id": "slide-01",
                "source_template_dir": str(self.source),
                "data": {"HEADLINE": "Hi"},
            }), encoding="utf-8")
        infos = _find_slides_info(self.slide.parent.parent)
        info = next(i for i in infos if i["slide_id"] == "slide-01")
        self.assertEqual(info["source_template_dir"], self.source)


# ---------------------------------------------------------------------------
# r5f F1b/F5 — fill seeding wiring + Replace-image control
# ---------------------------------------------------------------------------

class TestFillSeedAndReplaceImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_fill_inputs_carry_data_prop(self):
        """F1b: the colour inputs are addressable by prop so selectZone can seed
        them from the zone's computed colour."""
        self.assertIn('data-prop="bgColor"', self._html)
        self.assertIn('data-prop="color"', self._html)

    def test_seed_fill_controls_js_present(self):
        self.assertIn("function seedFillControls", self._html)
        self.assertIn("function rgbToHex", self._html)
        # selectZone calls the seeder for the active group
        self.assertIn("seedFillControls(slideId, handle, g)", self._html)

    def test_text_target_helpers_present(self):
        """F1a: innermost + deepest-text-bearing targeting is in the editor JS."""
        self.assertIn("function getInnermostEl", self._html)
        self.assertIn("function textTarget", self._html)
        self.assertIn("TEXTISH_PROPS", self._html)

    def test_replace_image_button_in_image_group_only(self):
        image_block = re.search(
            r'data-control-type="image".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertIn("pickReplaceImage", image_block)
        self.assertIn("Replace image", image_block)
        text_block = re.search(
            r'data-control-type="text".*?(?=data-control-type=|</aside>)',
            self._html, re.DOTALL).group(0)
        self.assertNotIn("pickReplaceImage", text_block)

    def test_imgsrc_prop_handled_in_apply(self):
        self.assertIn("prop === 'imgSrc'", self._html)
        self.assertIn("function pickReplaceImage", self._html)
        self.assertIn("window.pickReplaceImage", self._html)


class TestTextTargetPillDescent(unittest.TestCase):
    """r5f-followups Fix 2 — a font-size/colour edit on a CALLOUT_PILL must land on
    the inner text node (.callout-pill > span.pill-text declares its own font-size,
    so styling the container is a no-op). textTarget now descends into a LONE inline
    text-bearing child while leaving every other shape untouched. Runs the REAL
    emitted JS under Node so it asserts behaviour, not just markup presence."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_v2_run_folder()
        cls._html = build_editor_html(Path(cls._td.name))
        cls._tt = _extract_js_function(cls._html, "textTarget")

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_pill_descends_to_inner_text_span(self):
        # div.callout-pill > span.pill-text("New tab") — fontSize must target the span.
        dom = (
            "var span=new El('SPAN',{text:'New tab',cls:'pill-text'});"
            "var root=new El('DIV',{children:[span],cls:'callout-pill'});"
        )
        self.assertEqual(_run_tt(self._tt, "textTarget", dom, "r.cls"), "pill-text")

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_mixed_inline_markup_stays_on_container(self):
        # <mark>a</mark> b <b>c</b> — 3 inline children → innerHTML must stay at the
        # container so the editor's verbatim text edit keeps the markup (no regress).
        dom = (
            "var root=new El('DIV',{cls:'headline',children:["
            "new El('MARK',{text:'a'}),new El('SPAN',{text:' b '}),"
            "new El('B',{text:'c'})]});"
        )
        self.assertEqual(_run_tt(self._tt, "textTarget", dom, "r.cls"), "headline")

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_structural_nesting_still_descends(self):
        # div.outer > div.inner('deep') — structural descent is unchanged.
        dom = (
            "var root=new El('DIV',{cls:'outer',children:["
            "new El('DIV',{text:'deep',cls:'inner'})]});"
        )
        self.assertEqual(_run_tt(self._tt, "textTarget", dom, "r.cls"), "inner")

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_lone_empty_br_does_not_descend(self):
        # A lone <br> has no text → nothing to style → stay at the container.
        dom = (
            "var root=new El('DIV',{cls:'box',children:[new El('BR',{text:''})]});"
        )
        self.assertEqual(_run_tt(self._tt, "textTarget", dom, "r.cls"), "box")

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_leaf_returns_itself(self):
        dom = "var root=new El('DIV',{cls:'leaf',text:'hello'});"
        self.assertEqual(_run_tt(self._tt, "textTarget", dom, "r.cls"), "leaf")


# ---------------------------------------------------------------------------
# studio-ai-edit — "Edit with AI" provider buttons + modal
# ---------------------------------------------------------------------------

def _make_ai_edit_run_folder() -> tempfile.TemporaryDirectory:
    """The v2 zoo (text/pill/image/chrome) PLUS an SVG asset slot, so the
    every-type gating of the AI-edit buttons is exercised in one build."""
    td = tempfile.TemporaryDirectory()
    root = Path(td.name)
    sd = root / "slide-01"
    sd.mkdir(parents=True)
    (sd / "template.html").write_text(
        "<!doctype html><html><head><meta charset='utf-8'></head><body>"
        '<div data-slot="HEAD">{{{HEAD}}}</div>'
        '<div data-slot="TAGPILL">{{{TAGPILL}}}</div>'
        '<div data-slot="PHOTO"><img src="photo.png" alt=""></div>'
        '<div data-slot="ICON_SVG"><svg viewBox="0 0 10 10"><path d="M0 0h10"/></svg></div>'
        '<div data-slot="MAST">{{{MAST}}}</div>'
        "</body></html>",
        encoding="utf-8",
    )
    (sd / "instructions.md").write_text(
        "# S\n\n## Slots\n\n"
        "- **HEAD** — headline\n  - bbox: 4% 10% 90% 8%\n  - style: display, 7cqw\n  - sample: \"Hi\"\n"
        "- **TAGPILL** — category pill\n  - bbox: 4% 4% 20% 5%\n  - style: pill\n  - sample: \"NEW\"\n"
        "- **PHOTO** — main photo\n  - bbox: 6% 24% 88% 50%\n  - style: image, cover\n"
        "- **ICON_SVG_PATH** — icon asset\n  - bbox: 4% 90% 8% 6%\n  - style: svg\n"
        "- **MAST** — masthead bar\n  - bbox: 0% 0% 100% 6%\n  - style: masthead chrome\n  - sample: \"@brand\"\n",
        encoding="utf-8",
    )
    return td


class TestAiEditButtonsAndModal(unittest.TestCase):
    """studio-ai-edit: AI-edit affordances are server-gated. A provider button
    renders ONLY for a provider whose key the server resolved (presence boolean);
    absent key → no button at all (never disabled); no providers → no AI section
    and no modal. Buttons live in IMAGE control groups only — never in
    text/pill/svg/chrome groups."""

    @classmethod
    def setUpClass(cls):
        cls._td = _make_ai_edit_run_folder()
        cls._run = Path(cls._td.name)
        cls._html_both = build_editor_html(
            cls._run, ai_edit_providers={"gpt": True, "gemini": True})
        cls._html_gem = build_editor_html(
            cls._run, ai_edit_providers={"gpt": False, "gemini": True})
        cls._html_none = build_editor_html(
            cls._run, ai_edit_providers={"gpt": False, "gemini": False})
        cls._html_default = build_editor_html(cls._run)  # static build: no server

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def _block(self, html_text: str, ctype: str) -> str:
        m = re.search(
            r'data-control-type="%s".*?(?=data-control-type=|</aside>)' % ctype,
            html_text, re.DOTALL)
        self.assertIsNotNone(m, f"no {ctype} control group in fixture build")
        return m.group(0)

    def test_ai_buttons_in_image_group_only(self):
        image_block = self._block(self._html_both, "image")
        self.assertIn('class="ai-edit-btn"', image_block)
        self.assertIn("openAiEdit('slide-01','PHOTO','gpt')", image_block)
        self.assertIn("openAiEdit('slide-01','PHOTO','gemini')", image_block)
        self.assertIn("Edit with GPT", image_block)
        self.assertIn("Edit with Gemini", image_block)
        # next to the Replace-image control, in the same group
        self.assertIn("pickReplaceImage", image_block)

    def test_ai_buttons_never_in_text_pill_chrome_svg(self):
        for ctype in ("text", "pill", "chrome", "svg"):
            block = self._block(self._html_both, ctype)
            self.assertNotIn('class="ai-edit-btn"', block,
                             f"AI-edit button leaked into the {ctype} group")
            self.assertNotIn("openAiEdit(", block,
                             f"openAiEdit leaked into the {ctype} group")

    def test_only_available_provider_renders(self):
        # gemini-only: the gpt button must NOT exist (not even disabled).
        self.assertNotIn('data-provider="gpt"', self._html_gem)
        image_block = self._block(self._html_gem, "image")
        self.assertIn('data-provider="gemini"', image_block)
        self.assertIn("Edit with Gemini", image_block)

    def test_no_keys_no_ai_section_no_modal(self):
        self.assertNotIn('class="ai-edit-btn"', self._html_none)
        self.assertNotIn('class="sec-sub ai-edit-sub"', self._html_none)
        self.assertNotIn('id="ai-edit-modal"', self._html_none)

    def test_static_default_build_has_no_ai_markup(self):
        # The standalone (file://) build passes no providers — zero AI markup.
        self.assertNotIn('class="ai-edit-btn"', self._html_default)
        self.assertNotIn('id="ai-edit-modal"', self._html_default)

    def test_modal_markup_present_with_providers(self):
        for el_id in ("ai-edit-modal", "ai-edit-before", "ai-edit-after",
                      "ai-edit-prompt", "ai-edit-status", "ai-edit-generate",
                      "ai-edit-apply", "ai-edit-retry", "ai-edit-cancel"):
            self.assertIn(f'id="{el_id}"', self._html_both, f"modal misses #{el_id}")

    def test_modal_js_contract(self):
        # The modal flow ships in the editor JS: fetch /ai-edit, one-at-a-time
        # busy guard, Apply through the EXISTING applyToSlide imgSrc path.
        self.assertIn("function openAiEdit", self._html_both)
        self.assertIn("window.openAiEdit", self._html_both)
        self.assertIn("fetch('/ai-edit'", self._html_both)
        self.assertIn("applyToSlide(aiEdit.slide, aiEdit.handle, 'imgSrc', aiEdit.result)",
                      self._html_both)

    def test_provider_logos_inline(self):
        # Logos are inline SVG constants (no vendor files) inside the buttons.
        image_block = self._block(self._html_both, "image")
        gpt_btn = re.search(r'<button[^>]*data-provider="gpt".*?</button>',
                            image_block, re.DOTALL)
        self.assertIsNotNone(gpt_btn)
        self.assertIn("<svg", gpt_btn.group(0))

    # ── ai-edit-multi-input: reference-image upload in the modal ─────────────
    def test_modal_has_reference_image_controls(self):
        for el_id in ("ai-edit-addref", "ai-edit-refthumbs", "ai-edit-refcount"):
            self.assertIn(f'id="{el_id}"', self._html_both, f"modal misses #{el_id}")
        self.assertIn("addAiRef()", self._html_both)

    def test_modal_js_sends_images_array(self):
        # The submit packs [slot image, ...references] into `images`, not a
        # singular `image` field.
        self.assertIn("images: [aiEdit.source].concat(aiEdit.refs)", self._html_both)
        self.assertIn("function addAiRef", self._html_both)
        self.assertIn("window.addAiRef", self._html_both)
        self.assertIn("function removeAiRef", self._html_both)

    def test_modal_js_provider_caps(self):
        # Per-provider total-image caps mirror the server (GPT 16 / Gemini 14).
        self.assertIn("AI_PROVIDER_CAP", self._html_both)
        self.assertIn("gpt: 16", self._html_both)
        self.assertIn("gemini: 14", self._html_both)

    # ── layer-image-ai-edit: Gemini transparency tag ────────────────────────
    def test_modal_has_gemini_transparency_tag(self):
        self.assertIn('id="ai-edit-gemini-tag"', self._html_both)
        self.assertIn("Gemini não preserva transparência", self._html_both)
        # tag starts hidden — only shown by JS when transparent + gemini
        m = re.search(r'id="ai-edit-gemini-tag"[^>]*style="display:none"',
                      self._html_both)
        self.assertIsNotNone(m, "Gemini tag must start hidden")

    def test_modal_js_gemini_tag_conditional(self):
        # The tag toggles on (provider == gemini) AND (slot image transparent).
        self.assertIn("function aiDetectAlpha", self._html_both)
        self.assertIn("function aiUpdateGeminiTag", self._html_both)
        self.assertIn("aiEdit.provider === 'gemini'", self._html_both)
        self.assertIn("aiEdit.sourceTransparent", self._html_both)

    # ── ai-edit-live-fixes Fix 2: non-raster (SVG) input blocked client-side ──
    def test_non_raster_guard_wired(self):
        """A friendly message + the raster-check helper ship in the editor JS, and
        the guard is wired into the slot-image path AND the reference-upload path."""
        # The human message (Portuguese, names SVG/vector + PNG/JPG) is present.
        self.assertIn("aiIsRasterDataUri", self._html_both)
        self.assertIn("AI_NON_RASTER_MSG", self._html_both)
        self.assertIn("SVG/vetor", self._html_both)
        self.assertIn("use PNG ou JPG", self._html_both)
        # Slot image (aiCurrentImage): a non-raster source is blocked, not shipped.
        self.assertIn("errCb(AI_NON_RASTER_MSG)", self._html_both)
        # Reference uploads (addAiRef): a non-raster file shows the message and is
        # NOT pushed (guarded by the same helper).
        m = re.search(r"function addAiRef.*?\n  \}", self._html_both, re.DOTALL)
        self.assertIsNotNone(m, "addAiRef not found")
        self.assertIn("aiIsRasterDataUri", m.group(0))
        self.assertIn("AI_NON_RASTER_MSG", m.group(0))

    def _run_is_raster(self, uri: str) -> str:
        """Run the REAL aiIsRasterDataUri() under Node against *uri*; return
        'true'/'false'. Asserts behaviour, not just presence."""
        fn = _extract_js_function(self._html_both, "aiIsRasterDataUri")
        script = fn + "\nconsole.log(aiIsRasterDataUri(" + json.dumps(uri) + "));\n"
        proc = _subprocess.run(
            ["node", "-e", script], capture_output=True, text=True, timeout=30)
        if proc.returncode != 0:
            raise AssertionError(f"node failed: {proc.stderr or proc.stdout}")
        return proc.stdout.strip()

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_raster_check_accepts_png_jpeg_webp_gif(self):
        for uri in ("data:image/png;base64,AAAA",
                    "data:image/jpeg;base64,AAAA",
                    "data:image/jpg;base64,AAAA",
                    "data:image/webp;base64,AAAA",
                    "data:image/gif;base64,AAAA"):
            self.assertEqual(self._run_is_raster(uri), "true", f"raster {uri!r} rejected")

    @unittest.skipUnless(_node_ready(), "node not available for JS-behaviour test")
    def test_raster_check_rejects_svg_and_empty(self):
        for uri in ("data:image/svg+xml;base64,PHN2Zy8+",
                    "data:image/svg+xml,<svg/>",
                    "data:,",                      # 0x0 canvas toDataURL fallback
                    "data:image/png;base64,",      # empty payload
                    ""):
            self.assertEqual(self._run_is_raster(uri), "false", f"non-raster {uri!r} accepted")


if __name__ == "__main__":
    # Run tests with verbose output; exit 0 on all-pass, non-zero on any failure
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

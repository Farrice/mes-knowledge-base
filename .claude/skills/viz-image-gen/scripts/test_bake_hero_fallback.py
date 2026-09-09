# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
E2E gate for the BAKE HERO/LOGO FALLBACK (fix-bake-hero-fallback).

Root cause (D1 regression): render_template's image-path inliner only inlines a
`*_PATH` slot ALREADY present in `data`. For a TEMPLATE's own preview/bake the run
`data` is EMPTY (a template isn't a post), so `<img src="{{PHOTO_MAIN_PATH}}">` and
`<img src="{{BRAND_LOGO_PATH}}">` were left as literal placeholders → broken-image
glyphs, and for an AI-baked-headline template (fullbleed-cover: the headline is baked
INTO _ai_bg/photo_main.png) the unresolved hero meant the headline vanished too. The
Studio front already healed this (preview_editor._resolve_hero_slots /
_resolve_brand_asset_slots); the bake render did NOT.

This gate locks the CLASS: for representative template structures rendered with EMPTY
data (the template-preview case), the rendered HTML has NO literal `{{*_PATH}}` left,
NO empty/broken image src, and hero+logo resolve to the real on-disk assets.

THE GATE FAILS ON PRE-FIX CODE (revert-and-confirm): pre-fix, `resolve_template_asset_slots`
does not exist and fill() leaves `src=""`/`url('')`. PASSES after.

Run:
    uv run python -m pytest test_bake_hero_fallback.py
"""

import importlib.util
import re
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

_HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("render_template", _HERE / "render_template.py")
RT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RT)


def _write_png(path: Path, w: int = 8, h: int = 8, rgb=(180, 40, 30)) -> None:
    """Write a tiny valid PNG (solid color) so on-disk asset resolution + base64
    inlining have a real, decodable file to work with."""
    def chunk(typ: bytes, data: bytes) -> bytes:
        c = typ + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)
    raw = b""
    row = bytes(rgb) * w
    for _ in range(h):
        raw += b"\x00" + row
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(raw))
           + chunk(b"IEND", b""))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)


# Representative template structures (the class the bug spans):
#   FULLBLEED  — hero <img src="{{PHOTO_MAIN_PATH}}"> + canonical _ai_bg/photo_main.png,
#                plus a logo <img src="{{BRAND_LOGO_PATH}}"> resolving from assets/*logo*.
#   BGDIV      — hero is a background-image div bound to {{PHOTO_MAIN_PATH}} + single
#                _ai_bg/bg.png (the numbered-body shape; resolves via the single-png tier).
_FULLBLEED_HTML = (
    "<!DOCTYPE html><html><body>"
    '<div class="photo-zone" data-zone="photo" data-slot="PHOTO_MAIN">'
    '<img src="{{PHOTO_MAIN_PATH}}" alt="cover scene"></div>'
    '<div class="logo-badge" data-slot="BRAND_LOGO">'
    '<img src="{{BRAND_LOGO_PATH}}" alt="brand"></div>'
    "</body></html>"
)
_BGDIV_HTML = (
    "<!DOCTYPE html><html><body>"
    '<div class="photo-zone" data-slot="PHOTO_MAIN" data-zone="photo" '
    "style=\"background-image: url('{{PHOTO_MAIN_PATH}}'); background-size: cover;\"></div>"
    "</body></html>"
)

# MULTI-LINE <img> hero (boxed-headline-cover shape): attributes on SEPARATE
# lines, single-quoted, with the hero role declared ONLY via data-zone='photo' on a
# line OTHER than src. The slot name (COVER) is deliberately NON-hero so detection
# MUST read the photo-zone marker across the multi-line tag. Pre-fix exact-substring
# (`'data-zone="photo"' in tag`) misses the single-quoted, line-split marker → empty src.
_MULTILINE_HERO_HTML = (
    "<!DOCTYPE html><html><body>\n"
    '<div class="cover">\n'
    "  <img\n"
    "    data-slot='COVER'\n"
    "    data-zone = 'photo'\n"
    "    src='{{COVER_PATH}}'\n"
    "    alt='cover scene'>\n"
    "</div>\n"
    "</body></html>"
)

_PLACEHOLDER_RE = re.compile(r"\{\{\s*[A-Za-z_][A-Za-z0-9_]*_PATH\s*\}\}")
_EMPTY_SRC_RE = re.compile(r"""src\s*=\s*['"]\s*['"]""", re.IGNORECASE)
_EMPTY_BGURL_RE = re.compile(r"""background-image\s*:\s*url\(\s*['"]?\s*['"]?\s*\)""", re.IGNORECASE)


class BakeHeroFallbackGate(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        self.brand_context = self.root / "brand_context"
        # Brand-global logo fallback (used when a template ships no assets/*logo*).
        _write_png(self.brand_context / "visual-identity" / "logos" / "brand-transparent.png")

    def tearDown(self):
        self.td.cleanup()

    def _render_template_html(self, template_dir: Path, raw_html: str) -> str:
        """Mirror the bake's pre-fill resolution + fill() for the EMPTY-data case."""
        data: dict = {}
        data = RT.resolve_template_asset_slots(raw_html, data, template_dir, self.brand_context)
        return RT.fill(raw_html, data)

    def _assert_no_broken_images(self, rendered: str):
        self.assertIsNone(_PLACEHOLDER_RE.search(rendered),
                          f"literal {{{{*_PATH}}}} left in render: {rendered[:300]}")
        self.assertIsNone(_EMPTY_SRC_RE.search(rendered), "empty src=\"\" in render")
        self.assertIsNone(_EMPTY_BGURL_RE.search(rendered), "empty background-image url() in render")

    # ── FULLBLEED-COVER CLASS: hero <img> + logo <img> ────────────────────────
    def test_fullbleed_cover_hero_and_logo_resolve(self):
        tdir = self.root / "templates" / "fullbleed-cover"
        _write_png(tdir / "_ai_bg" / "photo_main.png", rgb=(10, 120, 200))   # the baked hero (headline lives here)
        _write_png(tdir / "assets" / "logo-brand.png", rgb=(240, 240, 240))  # template-local mark
        rendered = self._render_template_html(tdir, _FULLBLEED_HTML)
        self._assert_no_broken_images(rendered)
        # Both slots resolved to REAL on-disk assets (data-URIs), not empty.
        self.assertEqual(rendered.count("src=\"data:image/"), 2,
                         "hero + logo should both resolve to data-URI assets")

    def test_fullbleed_cover_hero_resolves_to_ai_bg_not_logo(self):
        """Role-scoping: the hero must get _ai_bg/photo_main.png and the logo must get
        assets/*logo* — never cross-contaminated (the front's documented bug)."""
        tdir = self.root / "templates" / "fullbleed-cover"
        _write_png(tdir / "_ai_bg" / "photo_main.png", rgb=(10, 120, 200))
        _write_png(tdir / "assets" / "logo-brand.png", rgb=(240, 240, 240))
        data: dict = RT.resolve_template_asset_slots(_FULLBLEED_HTML, {}, tdir, self.brand_context)
        hero_uri = RT._bake_asset_to_data_uri(tdir / "_ai_bg" / "photo_main.png")
        logo_uri = RT._bake_asset_to_data_uri(tdir / "assets" / "logo-brand.png")
        self.assertEqual(data["PHOTO_MAIN_PATH"], hero_uri)
        self.assertEqual(data["BRAND_LOGO_PATH"], logo_uri)
        self.assertNotEqual(data["PHOTO_MAIN_PATH"], data["BRAND_LOGO_PATH"])

    # ── MULTI-LINE <img> HERO (boxed-headline-cover shape) ────────────────────
    def test_multiline_img_hero_resolves(self):
        """A hero whose <img> spans multiple lines with the data-zone='photo' marker
        on a line OTHER than src — and a NON-hero slot name — must still resolve to
        _ai_bg. Locks in multi-line + single-quote + spaced-attr robustness."""
        tdir = self.root / "templates" / "boxed-headline-cover"
        _write_png(tdir / "_ai_bg" / "photo_main.png", rgb=(10, 120, 200))
        data = RT.resolve_template_asset_slots(_MULTILINE_HERO_HTML, {}, tdir, self.brand_context)
        self.assertIn("COVER_PATH", data, "multi-line hero must be detected and resolved")
        self.assertTrue(data["COVER_PATH"].startswith("data:image/"),
                        "multi-line hero should resolve to a data-URI asset")
        rendered = RT.fill(_MULTILINE_HERO_HTML, data)
        self._assert_no_broken_images(rendered)

    # ── BG-DIV HERO + single _ai_bg/*.png (numbered-body shape) ───────────────
    def test_bgdiv_hero_resolves_single_ai_bg(self):
        tdir = self.root / "templates" / "numbered-body"
        _write_png(tdir / "_ai_bg" / "bg.png", rgb=(30, 30, 30))  # single non-canonical png → tier 2
        rendered = self._render_template_html(tdir, _BGDIV_HTML)
        self._assert_no_broken_images(rendered)
        self.assertIn("url('data:image/", rendered, "bg-div hero should resolve to a data-URI")

    # ── LOGO falls back to BRAND when the template ships no assets/*logo* ──────
    def test_logo_falls_back_to_brand_when_no_template_asset(self):
        tdir = self.root / "templates" / "no-local-logo"
        _write_png(tdir / "_ai_bg" / "photo_main.png", rgb=(10, 120, 200))
        rendered = self._render_template_html(tdir, _FULLBLEED_HTML)
        self._assert_no_broken_images(rendered)  # logo resolved from brand_context

    # ── CALLER-PROVIDED VALUE WINS (a real post pins the hero) ────────────────
    def test_caller_provided_hero_is_not_overwritten(self):
        tdir = self.root / "templates" / "fullbleed-cover"
        _write_png(tdir / "_ai_bg" / "photo_main.png", rgb=(10, 120, 200))
        _write_png(tdir / "assets" / "logo-brand.png", rgb=(240, 240, 240))
        pinned = "https://cdn.example.com/post-hero.png"
        data = RT.resolve_template_asset_slots(
            _FULLBLEED_HTML, {"PHOTO_MAIN_PATH": pinned}, tdir, self.brand_context)
        self.assertEqual(data["PHOTO_MAIN_PATH"], pinned)

    # ── GENUINELY UNWIRED: no asset → slot stays empty (no crash, no fake fill) ─
    def test_unwired_hero_left_empty_no_crash(self):
        tdir = self.root / "templates" / "empty"
        tdir.mkdir(parents=True, exist_ok=True)
        data = RT.resolve_template_asset_slots(_BGDIV_HTML, {}, tdir, None)
        self.assertNotIn("PHOTO_MAIN_PATH", data)  # nothing to resolve to → untouched

    # ── REVERT-AND-CONFIRM SENTINEL: pre-fix code leaves the literal placeholder ─
    def test_prefix_behavior_would_leave_placeholder(self):
        """Documents the pre-fix failure mode: WITHOUT resolve_template_asset_slots,
        a plain fill() on EMPTY data leaves src="" (the broken-image bug). Proves the
        gate above is meaningful — it would fail on the pre-fix path."""
        rendered_prefix = RT.fill(_FULLBLEED_HTML, {})  # the old path: no resolution
        self.assertIsNotNone(_EMPTY_SRC_RE.search(rendered_prefix),
                             "pre-fix fill() must leave empty src — confirms the gate bites")


def _playwright_available() -> bool:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        with sync_playwright() as p:
            b = p.chromium.launch()
            b.close()
        return True
    except Exception:
        return False


@unittest.skipUnless(_playwright_available(), "Playwright/chromium not available")
class BakeHeroFallbackFullRenderGate(unittest.TestCase):
    """Strongest E2E: drive the real bake (render → PNG via Playwright) on a
    fullbleed-cover-shaped template_dir with EMPTY data, and assert the produced
    preview is NON-TRIVIAL — i.e. the hero photo actually painted, not the photoless
    tiny render. A photoless render is near-uniform; a real hero adds size/variance."""

    def test_fullbleed_preview_is_nontrivial(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        tdir = root / "templates" / "fullbleed-cover"
        tdir.mkdir(parents=True, exist_ok=True)
        # A vivid hero so the rendered slide is visibly non-uniform.
        _write_png(tdir / "_ai_bg" / "photo_main.png", w=64, h=64, rgb=(10, 120, 200))
        _write_png(tdir / "assets" / "logo-brand.png", w=16, h=16, rgb=(240, 240, 240))
        (tdir / "template.html").write_text(
            "<!DOCTYPE html><html><head><meta charset='utf-8'>"
            "<style>html,body{margin:0}.slide{width:1080px;height:1350px;position:relative}"
            ".photo-zone{position:absolute;inset:0}.photo-zone img{width:100%;height:100%;object-fit:cover}"
            "</style></head><body><div class='slide'>"
            "<div class='photo-zone' data-zone='photo' data-slot='PHOTO_MAIN'>"
            "<img src='{{PHOTO_MAIN_PATH}}' alt='cover'></div>"
            "<div class='logo-badge' data-slot='BRAND_LOGO'>"
            "<img src='{{BRAND_LOGO_PATH}}' alt='brand' style='width:80px'></div>"
            "</div></body></html>",
            encoding="utf-8",
        )
        out = root / "preview.png"
        RT.render(out, {}, template_dir=tdir, brand_context=root / "brand_context")
        self.assertTrue(out.is_file(), "render produced no PNG")
        # Non-trivial: a full 1080x1350 hero render is well over a tiny photoless blank.
        self.assertGreater(out.stat().st_size, 1500,
                           "preview looks photoless/trivial — hero did not paint")


if __name__ == "__main__":
    unittest.main()

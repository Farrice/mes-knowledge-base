#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""test_studio_regression_gate.py — the permanent Template/Content Studio gate.

WHY THIS FILE EXISTS
--------------------
The "missing image: PHOTO_MAIN" placeholder bug kept coming back because the
fixes were verified only against ``_build_srcdoc`` in *isolation*, never against
the function the running server actually serves: ``build_editor_html``
(the entry ``content_studio.StudioState.editor_html()`` calls). A unit test on
``_build_srcdoc`` can pass while the real served HTML still breaks, because the
two studios feed that function differently:

  * TEMPLATE mode — ``content_studio.py <pool> --mode template`` adapts each pool
    template dir into a single-slide ``_slides/<id>/`` structure (via
    ``_setup_template_run``) and serves ``build_editor_html(template_dir)``.
  * CONTENT/POST mode — ``content_studio.py <post>`` serves
    ``build_editor_html(<post run>)`` over the generated ``_slides/``.

This gate drives the SAME real entry the server uses, for BOTH modes, against
fixtures that mirror the real on-disk template structures (single ``_ai_bg``
hero, full-bleed composition-frame, ``background-image`` div). It ASSERTS the
invariants the bug violated, so a regression FAILS here instead of shipping:

  1. No "missing image" placeholder for any image slot whose asset exists on disk
     (the hero resolves to the real ``_ai_bg``/``bg.png`` asset).
  2. Exactly ONE editable image layer per image slot (no non-editable frame, no
     phantom empty PHOTO_MAIN) — the full-bleed-AI collapse holds.
  3. The autosize text-fit parity script is present in the srcdoc (text == bake).
  4. (template mode) Every pool template — including ``needs-user-decision`` —
     is walkable through the real adapter.

PROOF OF TEETH: ``test_gate_fails_on_prefix_behavior`` monkeypatches
``_resolve_hero_slots`` back to a no-op (the pre-fix behavior) and asserts the
gate's missing-image check FIRES — i.e. the gate would have caught the original
bug. The same assertion PASSES with the fix in place.

Run:
    uv run test_studio_regression_gate.py
"""

import base64
import hashlib
import html as _htmlmod
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# ── Cross-skill import (same path order content_studio / preview_editor use) ──
_SCRIPT_DIR = Path(__file__).resolve().parent
_RENDER_SCRIPTS = _SCRIPT_DIR.parent.parent.parent.parent / "viz-image-gen" / "scripts"
sys.path.insert(0, str(_RENDER_SCRIPTS))
sys.path.insert(0, str(_SCRIPT_DIR))

import preview_editor as pe          # noqa: E402
import content_studio as cs          # noqa: E402


# A 1x1-ish PNG header + tail so the bytes are a plausible raster asset.
_PNG_BYTES = b"\x89PNG\r\n\x1a\n" + b"gate-hero-asset"
# A DISTINCT byte payload for the brand logo — so a gate can prove the logo slot
# resolved to the BRAND mark and NOT the (different) _ai_bg hero.
_LOGO_BYTES = b"\x89PNG\r\n\x1a\n" + b"gate-brand-logo-asset"


def _md5(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()


def _img_payload_md5_by_alt(srcdoc: str) -> dict:
    """Map each rendered ``<img alt="…">`` to the md5 of its decoded data-URI payload
    (or ``None`` when the src is not a data-URI). Lets the gate assert which image
    CLASS each role's slot resolved to — hero photo vs brand logo."""
    out: dict = {}
    for m in re.finditer(r"<img\b[^>]*>", srcdoc):
        tag = m.group(0)
        am = re.search(r'alt="([^"]*)"', tag)
        sm = re.search(r'src="([^"]*)"', tag)
        if not am or not sm:
            continue
        src = sm.group(1)
        if src.startswith("data:") and "base64," in src:
            b64 = src.split("base64,", 1)[1]
            try:
                out[am.group(1)] = _md5(base64.b64decode(b64 + "=" * (-len(b64) % 4)))
            except Exception:
                out[am.group(1)] = None
        else:
            out[am.group(1)] = None
    return out


def _srcdoc_of(served_html: str) -> str:
    """First iframe ``srcdoc`` payload, HTML-unescaped, from a build_editor_html string."""
    blocks = re.findall(r'srcdoc="(.*?)"\s*></iframe>', served_html, re.DOTALL)
    if not blocks:
        blocks = re.findall(r'srcdoc="(.*?)"', served_html, re.DOTALL)
    return _htmlmod.unescape(blocks[0]) if blocks else served_html


# ── Missing-image detection (decode the placeholder SVG data-URI) ─────────────
def _has_missing_image_placeholder(srcdoc: str) -> bool:
    """True iff the srcdoc carries a rendered "missing image:" placeholder.

    ``_missing_img_placeholder_svg`` is embedded as a ``data:image/svg+xml;base64``
    URI whose decoded body contains the literal ``missing image:``. We decode each
    such URI rather than string-matching ``data-ph`` (which also tags legitimately
    empty *editable* zones) so the gate flags ONLY a genuine missing-asset render.
    """
    for tok in srcdoc.split("data:image/svg+xml;base64,")[1:]:
        b64 = tok.split('"')[0].split("'")[0].split(")")[0]
        try:
            if b"missing image:" in base64.b64decode(b64 + "=" * (-len(b64) % 4)):
                return True
        except Exception:
            pass
    return False


def _count_editable_photo_layers(srcdoc: str) -> int:
    """Number of editable PHOTO_MAIN image layers in the rendered slide DOM.

    The full-bleed-AI collapse must leave EXACTLY ONE (no non-editable frame,
    no phantom empty marker)."""
    return srcdoc.count('data-slot="PHOTO_MAIN"')


# ── Shared fixture pieces ─────────────────────────────────────────────────────
def _write_shared(pool: Path) -> None:
    sh = pool / "_shared"
    sh.mkdir(parents=True, exist_ok=True)
    (sh / "styles.css").write_text(
        "/* GATE-SHARED */\nbody{margin:0}\n", encoding="utf-8")


def _make_template_dir(parent: Path, tid: str, body_html: str,
                       hero_asset_name: str = "photo_main.png",
                       with_sample_path: bool = False) -> Path:
    """Create a real-shaped template dir under a pool.

    Mirrors the live pool layout: ``<pool>/<tid>/`` carries ``template.html``,
    a single ``_ai_bg/<asset>`` hero, ``instructions.md``, and a co-located
    ``_slides/slide-01/`` (template.html + _ai_bg) — exactly what onboarding's
    ssc-template-builder ships and what content_studio's adapter walks.
    """
    tdir = parent / tid
    tdir.mkdir(parents=True, exist_ok=True)
    (tdir / "_ai_bg").mkdir(exist_ok=True)
    (tdir / "_ai_bg" / hero_asset_name).write_bytes(_PNG_BYTES)
    (tdir / "template.html").write_text(body_html, encoding="utf-8")
    sample = "\n  - sample: \"_ai_bg/%s\"" % hero_asset_name if with_sample_path else "\n  - sample: \"\""
    (tdir / "instructions.md").write_text(
        "# %s\n\n## Slots\n\n- **HEADLINE** — main headline\n"
        "  - sample: \"Sample headline\"\n\n"
        "- **PHOTO_MAIN** — hero photo\n  - style: image, cover%s\n" % (tid, sample),
        encoding="utf-8")
    # Co-located rich slide (the live pool ships this), WITHOUT a sample path so the
    # hero arrives unfilled — the exact pre-fix breakage condition.
    sl = tdir / "_slides" / "slide-01"
    sl.mkdir(parents=True, exist_ok=True)
    (sl / "_ai_bg").mkdir(exist_ok=True)
    (sl / "_ai_bg" / hero_asset_name).write_bytes(_PNG_BYTES)
    (sl / "template.html").write_text(body_html, encoding="utf-8")
    (sl / "instructions.md").write_text(
        "# %s\n\n## Slots\n\n- **HEADLINE** — main headline\n"
        "  - sample: \"Sample headline\"\n\n"
        "- **PHOTO_MAIN** — hero photo\n  - style: image, cover\n  - sample: \"\"\n" % tid,
        encoding="utf-8")
    return tdir


# Three real composition shapes the templates use for the hero:
_BODY_BG_DIV = (
    "<!doctype html><html><head><meta charset='utf-8'></head><body>"
    "<div class='slide'>"
    "<div class='bg' style=\"background-image: url('{{PHOTO_MAIN_PATH}}');\"></div>"
    "<h1 data-slot='HEADLINE'>{{{HEADLINE}}}</h1>"
    "</div></body></html>"
)
_BODY_IMG_SRC = (
    "<!doctype html><html><head><meta charset='utf-8'></head><body>"
    "<div class='slide'>"
    "<img data-slot='PHOTO_MAIN' src=\"{{PHOTO_MAIN_PATH}}\" alt='hero'>"
    "<h1 data-slot='HEADLINE'>{{{HEADLINE}}}</h1>"
    "</div></body></html>"
)
# MULTI-LINE <img> hero (boxed-headline-cover shape): the <img> spans several lines
# with data-slot / data-zone / src on SEPARATE lines. The exact shape that showed NO
# hero in the live report. Hero role is carried by data-zone='photo' on a different
# line than src; pre-fix exact-substring marker matching missed it on multi-line tags.
_BODY_MULTILINE_IMG = (
    "<!doctype html><html><head><meta charset='utf-8'></head><body>"
    "<div class='slide'>\n"
    "  <img\n"
    "    data-slot='PHOTO_MAIN'\n"
    "    data-zone = 'photo'\n"
    "    src='{{PHOTO_MAIN_PATH}}'\n"
    "    alt='cover scene'>\n"
    "  <h1 data-slot='HEADLINE'>{{{HEADLINE}}}</h1>\n"
    "</div></body></html>"
)
_BODY_FULLBLEED_FRAME = (
    # The full-bleed-AI anti-pattern (real authoring shape — double-quoted class,
    # marker div that binds the SAME PHOTO_MAIN path): a non-editable frame wrapper
    # holding the AI image AND a redundant standalone PHOTO_MAIN marker.
    # _collapse_fullbleed_ai must promote the frame and drop the marker, leaving
    # exactly ONE editable PHOTO_MAIN.
    "<!doctype html><html><head><meta charset='utf-8'></head><body>"
    "<div class=\"slide\">"
    "<div class=\"frame\"><img src=\"{{PHOTO_MAIN_PATH}}\" alt=\"hero\"></div>"
    "<div data-slot=\"PHOTO_MAIN\"><img src=\"{{PHOTO_MAIN_PATH}}\" alt=\"hero\"></div>"
    "<h1 data-slot=\"HEADLINE\">{{{HEADLINE}}}</h1>"
    "</div></body></html>"
)


# fullbleed-cover shape: a hero <img> (PHOTO_MAIN, data-zone=photo) AND a logo badge
# <img> binding {{BRAND_LOGO_PATH}}. Pre-fix, the broad hero-resolve clobbered the
# logo with the _ai_bg hero ("the top logo got replaced by the preview image").
_BODY_HERO_PLUS_LOGO = (
    "<!doctype html><html><head><meta charset='utf-8'></head><body>"
    "<div class=\"slide\">"
    "<div class=\"photo-zone\" data-zone=\"photo\" data-slot=\"PHOTO_MAIN\">"
    "<img src=\"{{PHOTO_MAIN_PATH}}\" alt=\"cover scene\"></div>"
    "<div class=\"logo-badge\" data-slot=\"BRAND_LOGO\">"
    "<img src=\"{{BRAND_LOGO_PATH}}\" alt=\"brand logo\"></div>"
    "<h1 data-slot=\"HEADLINE\">{{{HEADLINE}}}</h1>"
    "</div></body></html>"
)


def _make_hero_plus_logo_dir(parent: Path, tid: str = "fullbleed-cover") -> Path:
    """fullbleed-cover-shaped template dir: single _ai_bg hero (distinct bytes) +
    an ``assets/<logo>`` brand mark (distinct bytes), both unfilled in data — the
    exact pre-fix cross-contamination condition."""
    tdir = parent / tid
    (tdir / "_ai_bg").mkdir(parents=True, exist_ok=True)
    (tdir / "_ai_bg" / "photo_main.png").write_bytes(_PNG_BYTES)
    (tdir / "assets").mkdir(exist_ok=True)
    (tdir / "assets" / "logo-brand.png").write_bytes(_LOGO_BYTES)
    (tdir / "template.html").write_text(_BODY_HERO_PLUS_LOGO, encoding="utf-8")
    (tdir / "instructions.md").write_text(
        "# %s\n\n## Slots\n\n- **HEADLINE** — headline\n  - sample: \"H\"\n\n"
        "- **PHOTO_MAIN_PATH** — hero photo\n  - style: image, cover\n" % tid,
        encoding="utf-8")
    sl = tdir / "_slides" / "slide-01"
    sl.mkdir(parents=True, exist_ok=True)
    (sl / "_ai_bg").mkdir(exist_ok=True)
    (sl / "_ai_bg" / "photo_main.png").write_bytes(_PNG_BYTES)
    (sl / "assets").mkdir(exist_ok=True)
    (sl / "assets" / "logo-brand.png").write_bytes(_LOGO_BYTES)
    (sl / "template.html").write_text(_BODY_HERO_PLUS_LOGO, encoding="utf-8")
    (sl / "instructions.md").write_text(
        "# %s\n\n## Slots\n\n- **HEADLINE** — headline\n  - sample: \"H\"\n\n"
        "- **PHOTO_MAIN_PATH** — hero\n  - style: image, cover\n" % tid,
        encoding="utf-8")
    return tdir


def _make_template_pool() -> Path:
    """A pool with a manifest spanning the real shapes + statuses (incl.
    needs-user-decision) and the canonical single-_ai_bg naming + a bg.png-named
    variant. Returns the pool dir (caller cleans up the parent)."""
    parent = Path(tempfile.mkdtemp(prefix="gate-pool-"))
    pool = parent / "linkedin-carousel"
    pool.mkdir()
    _write_shared(pool)
    _make_template_dir(pool, "bgdiv-cover", _BODY_BG_DIV)
    _make_template_dir(pool, "imgsrc-body", _BODY_IMG_SRC)
    _make_template_dir(pool, "fullbleed-cover", _BODY_FULLBLEED_FRAME)
    # bg.png naming (numbered-body ships _ai_bg/bg.png, no photo_main.png).
    _make_template_dir(pool, "bgpng-body", _BODY_BG_DIV, hero_asset_name="bg.png")
    # Multi-line <img> hero (boxed-headline-cover shape).
    _make_template_dir(pool, "multiline-cover", _BODY_MULTILINE_IMG)
    manifest = {
        "pool": "linkedin-carousel",
        "version": 1,
        "templates": [
            {"id": "bgdiv-cover", "file": "bgdiv-cover/template.html",
             "role": "cover", "status": "ready"},
            {"id": "imgsrc-body", "file": "imgsrc-body/template.html",
             "role": "body", "status": "ready"},
            {"id": "fullbleed-cover", "file": "fullbleed-cover/template.html",
             "role": "cover", "status": "ready"},
            {"id": "bgpng-body", "file": "bgpng-body/template.html",
             "role": "body", "status": "needs-user-decision"},
            {"id": "multiline-cover", "file": "multiline-cover/template.html",
             "role": "cover", "status": "ready"},
        ],
    }
    (pool / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return pool


def _make_post_run() -> Path:
    """A generated-post run: ``_slides/slide-01/`` carrying template.html + a real
    ``_ai_bg`` hero, with the hero slot UNFILLED in metadata (the post-mode case the
    bug also hit). Returns the run dir (caller cleans up the parent)."""
    parent = Path(tempfile.mkdtemp(prefix="gate-post-"))
    run = parent / "post"
    run.mkdir()
    _write_shared(run)
    sl = run / "_slides" / "slide-01"
    sl.mkdir(parents=True)
    (sl / "_ai_bg").mkdir()
    (sl / "_ai_bg" / "photo_main.png").write_bytes(_PNG_BYTES)
    (sl / "template.html").write_text(_BODY_BG_DIV, encoding="utf-8")
    (sl / "instructions.md").write_text(
        "# post\n\n## Slots\n\n- **HEADLINE** — headline\n  - sample: \"H\"\n\n"
        "- **PHOTO_MAIN** — hero\n  - style: image, cover\n  - sample: \"\"\n",
        encoding="utf-8")
    # metadata WITHOUT a PHOTO_MAIN_PATH → unfilled hero, resolves only via _ai_bg.
    (sl / "metadata.json").write_text(
        json.dumps({"data": {"HEADLINE": "Live headline"}}), encoding="utf-8")
    return run


class StudioRegressionGate(unittest.TestCase):
    """The permanent gate. Both studios, real entry, asset-backed assertions."""

    # ── TEMPLATE MODE ─────────────────────────────────────────────────────────
    def test_template_mode_no_missing_image_for_every_pool_template(self):
        """For each pool template (incl. needs-user-decision), the SERVED HTML
        (build_editor_html, driven exactly as content_studio does) shows the real
        _ai_bg hero — never the 'missing image' placeholder."""
        pool = _make_template_pool()
        try:
            entries = cs._resolve_pool_templates(pool)
            self.assertEqual(len(entries), 5, "all 5 manifest entries must be renderable")
            statuses = {e["status"] for e in entries}
            self.assertIn("needs-user-decision", statuses,
                          "needs-user-decision template must be walkable")
            for e in entries:
                tdir = Path(e["template_dir"])
                cs._setup_template_run(tdir)          # what the server does at launch
                html = pe.build_editor_html(tdir)     # the REAL served entry
                self.assertFalse(
                    _has_missing_image_placeholder(html),
                    f"[{e['id']}] missing-image placeholder despite _ai_bg on disk")
                self.assertTrue(
                    ("data:image/png;base64," in html or "data:image/jpeg;base64," in html),
                    f"[{e['id']}] no real raster hero data-URI in served HTML")
        finally:
            shutil.rmtree(pool.parent, ignore_errors=True)

    def test_template_mode_multiline_img_hero_resolves(self):
        """A hero whose <img> spans multiple lines (data-slot/data-zone/src on
        separate lines — the boxed-headline-cover shape) must resolve to the real
        _ai_bg hero at the served entry, not the missing-image placeholder."""
        pool = _make_template_pool()
        try:
            entries = {e["id"]: e for e in cs._resolve_pool_templates(pool)}
            tdir = Path(entries["multiline-cover"]["template_dir"])
            cs._setup_template_run(tdir)
            html = pe.build_editor_html(tdir)
            self.assertFalse(
                _has_missing_image_placeholder(html),
                "multi-line <img> hero showed missing-image despite _ai_bg on disk")
            self.assertTrue(
                ("data:image/png;base64," in html or "data:image/jpeg;base64," in html),
                "multi-line <img> hero produced no real raster data-URI")
        finally:
            shutil.rmtree(pool.parent, ignore_errors=True)

    def test_template_mode_exactly_one_editable_image_layer(self):
        """The full-bleed-AI frame template must collapse to exactly ONE editable
        PHOTO_MAIN layer (no non-editable frame, no phantom empty marker) at the
        real entry."""
        pool = _make_template_pool()
        try:
            entries = {e["id"]: e for e in cs._resolve_pool_templates(pool)}
            tdir = Path(entries["fullbleed-cover"]["template_dir"])
            cs._setup_template_run(tdir)
            html = pe.build_editor_html(tdir)
            self.assertEqual(
                _count_editable_photo_layers(html), 1,
                "full-bleed-AI must expose exactly ONE editable PHOTO_MAIN layer")
        finally:
            shutil.rmtree(pool.parent, ignore_errors=True)

    def test_template_mode_autosize_parity_script_present(self):
        """The autosize text-fit parity script (preview == bake) must ship in the
        served HTML for a template-mode slide."""
        pool = _make_template_pool()
        try:
            entries = {e["id"]: e for e in cs._resolve_pool_templates(pool)}
            tdir = Path(entries["bgdiv-cover"]["template_dir"])
            cs._setup_template_run(tdir)
            html = pe.build_editor_html(tdir)
            self.assertIn("function autosize(", html,
                          "autosize parity script missing from served template HTML")
            self.assertIn("window.__autosizeRun", html,
                          "autosize re-fit hook missing (live text edit parity)")
        finally:
            shutil.rmtree(pool.parent, ignore_errors=True)

    # ── PER-SLOT ASSET CLASS (hero ≠ logo cross-contamination) ───────────────
    def test_logo_resolves_to_brand_not_hero(self):
        """fullbleed-cover repro: the logo-badge img must resolve to the BRAND logo
        asset, NEVER the _ai_bg hero. The hero img must resolve to the hero. Asserted
        by COMPARING decoded payload bytes, so a cross-contamination (logo == hero)
        FAILS here — the exact bug ('the top logo got replaced by the preview image').
        This assertion FAILS on the pre-fix broad hero-resolve (see teeth test)."""
        parent = Path(tempfile.mkdtemp(prefix="gate-hl-"))
        try:
            pool = parent / "linkedin-carousel"
            pool.mkdir()
            _write_shared(pool)
            tdir = _make_hero_plus_logo_dir(pool)
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir))
            by_alt = _img_payload_md5_by_alt(srcdoc)
            hero_md5, logo_md5 = _md5(_PNG_BYTES), _md5(_LOGO_BYTES)
            self.assertEqual(by_alt.get("cover scene"), hero_md5,
                             "hero slot must resolve to the _ai_bg hero asset")
            self.assertEqual(by_alt.get("brand logo"), logo_md5,
                             "logo slot must resolve to the BRAND logo asset")
            self.assertNotEqual(by_alt.get("brand logo"), hero_md5,
                                "CROSS-CONTAMINATION: logo got the _ai_bg hero image")
            self.assertFalse(_has_missing_image_placeholder(srcdoc),
                             "no missing-image placeholder when both assets exist")
        finally:
            shutil.rmtree(parent, ignore_errors=True)

    def test_live_fullbleed_logo_distinct_from_hero(self):
        """LIVE repro on the real ssc-run11 fullbleed-cover: the logo img payload
        must DIFFER from the hero img payload (logo = brand mark, hero = _ai_bg).
        Skipped when the pool isn't on disk."""
        live = Path.home() / "Downloads" / "ssc-run11" / "brand_context" / \
            "templates" / "linkedin-carousel"
        if not (live / "fullbleed-cover" / "template.html").is_file():
            self.skipTest("live ssc-run11 pool not present")
        work = Path(tempfile.mkdtemp(prefix="gate-live-fb-"))
        try:
            dst = work / "linkedin-carousel"
            shutil.copytree(live, dst)
            entries = {e["id"]: e for e in cs._resolve_pool_templates(dst)}
            tdir = Path(entries["fullbleed-cover"]["template_dir"])
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir, brand_context=dst.parent))
            by_alt = _img_payload_md5_by_alt(srcdoc)
            hero = by_alt.get("cover scene")
            logo = by_alt.get("Agentic Academy")
            self.assertIsNotNone(hero, "live hero img did not resolve to a data-URI")
            self.assertIsNotNone(logo, "live logo img did not resolve to a data-URI")
            self.assertNotEqual(
                logo, hero,
                "live fullbleed-cover: logo payload == hero payload (contaminated)")
        finally:
            shutil.rmtree(work, ignore_errors=True)

    def test_live_numbered_bg_div_loads(self):
        """LIVE repro on the real numbered-body: the PHOTO_MAIN bg-image DIV must
        resolve to a real raster data-URI (the photo loads) — not empty, not the
        missing-image placeholder. Skipped when the pool isn't on disk."""
        live = Path.home() / "Downloads" / "ssc-run11" / "brand_context" / \
            "templates" / "linkedin-carousel"
        if not (live / "numbered-body" / "template.html").is_file():
            self.skipTest("live ssc-run11 pool not present")
        work = Path(tempfile.mkdtemp(prefix="gate-live-nb-"))
        try:
            dst = work / "linkedin-carousel"
            shutil.copytree(live, dst)
            entries = {e["id"]: e for e in cs._resolve_pool_templates(dst)}
            tdir = Path(entries["numbered-body"]["template_dir"])
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir, brand_context=dst.parent))
            bg = re.search(
                r'data-slot="PHOTO_MAIN"[^>]*background-image:\s*url\(\s*[\'"]?(data:image[^\'")]*)'
                r'|background-image:\s*url\(\s*[\'"]?(data:image[^\'")]*)[^>]*data-slot="PHOTO_MAIN"',
                srcdoc)
            self.assertTrue(
                bg is not None,
                "numbered-body PHOTO_MAIN bg-div did not resolve to a data-URI photo")
            self.assertFalse(_has_missing_image_placeholder(srcdoc),
                             "numbered-body bg-div shows missing-image despite _ai_bg")
        finally:
            shutil.rmtree(work, ignore_errors=True)

    # ── CONTENT / POST MODE ──────────────────────────────────────────────────
    def test_post_mode_no_missing_image_when_asset_on_disk(self):
        """A generated post whose hero slot is UNFILLED but whose _ai_bg asset
        exists must render the real photo, not the 'missing image' placeholder, at
        the real entry."""
        run = _make_post_run()
        try:
            html = pe.build_editor_html(run)
            self.assertFalse(
                _has_missing_image_placeholder(html),
                "post-mode: missing-image placeholder despite _ai_bg on disk")
            self.assertTrue(
                ("data:image/png;base64," in html or "data:image/jpeg;base64," in html),
                "post-mode: no real raster hero data-URI in served HTML")
        finally:
            shutil.rmtree(run.parent, ignore_errors=True)

    def test_post_mode_autosize_parity_script_present(self):
        run = _make_post_run()
        try:
            html = pe.build_editor_html(run)
            self.assertIn("function autosize(", html,
                          "autosize parity script missing from served post HTML")
        finally:
            shutil.rmtree(run.parent, ignore_errors=True)

    # ── LIVE 11-TEMPLATE POOL (skipped when not on this machine) ─────────────
    def test_live_pool_walkable_no_missing_image(self):
        """When the real ssc-run11 pool is present, walk ALL its templates through
        the real entry and assert every one resolves its hero (no missing-image),
        carries exactly one editable PHOTO_MAIN, and ships the autosize parity
        script. Portable: skipped where the pool isn't on disk."""
        live = Path.home() / "Downloads" / "ssc-run11" / "brand_context" / \
            "templates" / "linkedin-carousel"
        if not (live / "manifest.json").is_file():
            self.skipTest("live ssc-run11 pool not present")
        # Work on a copy — _setup_template_run writes (slide-01.png seeds etc.).
        work = Path(tempfile.mkdtemp(prefix="gate-live-"))
        try:
            dst = work / "linkedin-carousel"
            shutil.copytree(live, dst)
            entries = cs._resolve_pool_templates(dst)
            self.assertGreaterEqual(len(entries), 1, "live pool has no renderable templates")
            for e in entries:
                tdir = Path(e["template_dir"])
                cs._setup_template_run(tdir)
                html = pe.build_editor_html(tdir, brand_context=dst.parent)
                self.assertFalse(
                    _has_missing_image_placeholder(html),
                    f"[live:{e['id']}] missing-image placeholder despite _ai_bg on disk")
                # No duplicated/phantom PHOTO_MAIN; the hero is editable either as a
                # PHOTO_MAIN <img> (composition shape) or as the single BACKGROUND
                # layer (CSS-backdrop bg.png shape) — never zero, never two.
                pm = _count_editable_photo_layers(html)
                bg = html.count('data-slot="BACKGROUND"')
                self.assertLessEqual(
                    pm, 1, f"[live:{e['id']}] phantom/duplicate PHOTO_MAIN ({pm})")
                self.assertEqual(
                    bg, 1, f"[live:{e['id']}] expected exactly ONE BACKGROUND layer ({bg})")
                self.assertGreaterEqual(
                    pm + bg, 1, f"[live:{e['id']}] no editable image layer for the hero")
                self.assertIn("function autosize(", html,
                              f"[live:{e['id']}] autosize parity script missing")
        finally:
            shutil.rmtree(work, ignore_errors=True)

    # ── PROOF THE GATE HAS TEETH ─────────────────────────────────────────────
    def test_gate_fails_on_prefix_behavior(self):
        """Monkeypatch _resolve_hero_slots back to the PRE-FIX no-op and assert the
        gate's missing-image check FIRES (template + post). With the fix in place
        the same check passes — this proves the gate would have caught the bug."""
        pool = _make_template_pool()
        run = _make_post_run()
        orig = pe._resolve_hero_slots
        pe._resolve_hero_slots = lambda raw, data, td: data  # pre-fix behavior
        try:
            # Template mode: at least one template must now show the placeholder.
            tmpl_broke = False
            for e in cs._resolve_pool_templates(pool):
                tdir = Path(e["template_dir"])
                cs._setup_template_run(tdir)
                if _has_missing_image_placeholder(pe.build_editor_html(tdir)):
                    tmpl_broke = True
            self.assertTrue(
                tmpl_broke,
                "PRE-FIX template mode should regress to missing-image — gate toothless")
            # Post mode: the unfilled hero must regress to the placeholder.
            self.assertTrue(
                _has_missing_image_placeholder(pe.build_editor_html(run)),
                "PRE-FIX post mode should regress to missing-image — gate toothless")
        finally:
            pe._resolve_hero_slots = orig
            shutil.rmtree(pool.parent, ignore_errors=True)
            shutil.rmtree(run.parent, ignore_errors=True)

    def test_teeth_prefix_contaminates_logo(self):
        """Restore the PRE-FIX broad hero-resolve (matches ANY {{*_PATH}} src and
        resolves it to the single _ai_bg hero) and assert the logo gets the HERO
        payload — i.e. cross-contamination. This proves the per-slot asset-class
        gate (test_logo_resolves_to_brand_not_hero) has teeth: the bug it guards
        reproduces here, and the fix eliminates it."""
        parent = Path(tempfile.mkdtemp(prefix="gate-teeth-hl-"))

        def _broad_resolve(raw, data, td):
            # The exact pre-fix body: match every {{*_PATH}} src/bg and assign the
            # single _ai_bg asset, ignoring slot role.
            if td is None:
                return data
            out = dict(data)
            asset = pe._resolve_ai_bg_asset(Path(td))
            if asset is None:
                return out
            uri = "data:image/png;base64," + base64.b64encode(asset.read_bytes()).decode()
            for m in pe._HERO_SLOT_IN_HTML_RE.finditer(raw):
                slot = m.group("slot").upper()
                ex = out.get(slot)
                if isinstance(ex, str) and ex.startswith(("data:", "http")):
                    continue
                out[slot] = uri
            return out

        orig_h = pe._resolve_hero_slots
        orig_b = pe._resolve_brand_asset_slots
        pe._resolve_hero_slots = _broad_resolve
        pe._resolve_brand_asset_slots = lambda raw, data, td, bc: data  # disabled pre-fix
        try:
            pool = parent / "linkedin-carousel"
            pool.mkdir()
            _write_shared(pool)
            tdir = _make_hero_plus_logo_dir(pool)
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir))
            by_alt = _img_payload_md5_by_alt(srcdoc)
            self.assertEqual(
                by_alt.get("brand logo"), _md5(_PNG_BYTES),
                "PRE-FIX broad resolve should contaminate the logo with the hero "
                "image — gate toothless")
        finally:
            pe._resolve_hero_slots = orig_h
            pe._resolve_brand_asset_slots = orig_b
            shutil.rmtree(parent, ignore_errors=True)

    # ---- Hero-img fit (23-hero-img-fit): a hero <img> in a fixed box must COVER-fill
    #      its box (object-fit:cover), identically in the front (build_editor_html
    #      srcdoc) and the bake (render_template). multiline-cover is the
    #      boxed-headline-cover shape: an <img data-slot=PHOTO_MAIN data-zone=photo>
    #      that omits object-fit → pre-fix the subject renders at intrinsic aspect and
    #      lands low ("pushed to the bottom"). ---------------------------------------

    _HERO_FIT_RE = re.compile(
        r'img\[data-slot="PHOTO_MAIN"\]\s*,\s*img\[data-zone="photo"\]\s*\{[^}]*'
        r'object-fit\s*:\s*cover', re.IGNORECASE)

    def test_front_injects_hero_cover_fit(self):
        """FRONT: build_editor_html srcdoc carries the cover-fit floor for the hero."""
        parent = Path(tempfile.mkdtemp())
        try:
            pool = parent / "linkedin-carousel"
            pool.mkdir()
            _write_shared(pool)
            tdir = _make_template_dir(pool, "multiline-cover", _BODY_MULTILINE_IMG)
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir))
            self.assertTrue(
                self._HERO_FIT_RE.search(srcdoc),
                "FRONT must inject object-fit:cover for img[data-slot=PHOTO_MAIN]/"
                "[data-zone=photo] — without it the hero renders at intrinsic aspect "
                "and the subject is pushed to the bottom of its box.")
        finally:
            shutil.rmtree(parent, ignore_errors=True)

    def test_bake_injects_hero_cover_fit(self):
        """BAKE: render_template injects the SAME cover-fit floor as the front."""
        import render_template as rt  # noqa: WPS433
        self.assertTrue(
            self._HERO_FIT_RE.search(rt.HERO_FIT_CSS),
            "BAKE HERO_FIT_CSS must floor the hero <img> to object-fit:cover.")

    def test_hero_cover_fit_bake_front_parity(self):
        """PARITY: the front's injected rule == render_template.HERO_FIT_CSS body, so
        the editor canvas and the rebaked PNG size the hero <img> identically."""
        import render_template as rt  # noqa: WPS433
        parent = Path(tempfile.mkdtemp())
        try:
            pool = parent / "linkedin-carousel"
            pool.mkdir()
            _write_shared(pool)
            tdir = _make_template_dir(pool, "multiline-cover", _BODY_MULTILINE_IMG)
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir))
            # The bake's exact rule body (strip the <style> wrapper) appears verbatim
            # in the front srcdoc → byte-level parity of the cover floor.
            rule_body = rt.HERO_FIT_CSS.replace("<style>", "").replace("</style>", "")
            self.assertIn(
                rule_body, srcdoc,
                "front rule must be byte-identical to render_template.HERO_FIT_CSS "
                "(bake == front).")
        finally:
            shutil.rmtree(parent, ignore_errors=True)

    def test_hero_cover_fit_negative_control(self):
        """Pre-fix the floor was absent: a srcdoc with the hero-fit <style> stripped
        does NOT cover the hero — proves the assertion has teeth (would fail pre-fix)."""
        parent = Path(tempfile.mkdtemp())
        try:
            pool = parent / "linkedin-carousel"
            pool.mkdir()
            _write_shared(pool)
            tdir = _make_template_dir(pool, "multiline-cover", _BODY_MULTILINE_IMG)
            cs._setup_template_run(tdir)
            srcdoc = _srcdoc_of(pe.build_editor_html(tdir))
            pre_fix = re.sub(
                r'<style>img\[data-slot="PHOTO_MAIN"\][^<]*</style>', "", srcdoc)
            self.assertFalse(
                self._HERO_FIT_RE.search(pre_fix),
                "negative control: without the injected floor the hero is NOT covered.")
        finally:
            shutil.rmtree(parent, ignore_errors=True)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

"""
Tests for the Lane 1 AI-bg canonical-routing fix in render_template.emit_edit_slide
(fix-bg-canonical).

Root cause (run-10): the post-specific AI bg was misrouted/discarded, so
emit_edit_slide copytree'd the template's DEMO _ai_bg wholesale into the post slide
dir and PHOTO_MAIN_PATH pointed at a never-written `slide-XX-bg.png`. The slide then
shipped the template's enlatado demo art, byte-for-byte.

The fix has two halves proved here:
  1. The demo _ai_bg must NOT clobber a per-post bg already written to the slide dir.
  2. A hard-fail gate aborts when the slide's resolved bg is byte-identical to the
     template demo, or when a *_PATH slot does not resolve on disk.

Run:
    uv run python -m pytest test_ai_bg_canonical.py
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

_HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("render_template", _HERE / "render_template.py")
RT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RT)


_TMPL_HTML = (
    "<html><body>"
    "<img data-slot=\"PHOTO_MAIN\" src=\"_ai_bg/photo_main.png\"></body></html>"
)


class AiBgCanonicalTests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        # Template dir with a DEMO _ai_bg + stale build-time log.
        self.tdir = self.root / "brand_context" / "templates" / "lc" / "numbered"
        (self.tdir / "_ai_bg").mkdir(parents=True, exist_ok=True)
        self.template_html = self.tdir / "template.html"
        self.template_html.write_text(_TMPL_HTML, encoding="utf-8")
        self.demo_bg = self.tdir / "_ai_bg" / "photo_main.png"
        self.demo_bg.write_bytes(b"DEMO-template-art-man-on-a-chair-on-water")
        (self.tdir / "_ai_bg" / "photo_main.log.md").write_text(
            "Output: .../ssc-run09/.../templates/.../_ai_bg/photo_main.png",
            encoding="utf-8",
        )
        # Post run dir.
        self.run = self.root / "projects" / "2026-06-15" / "best-memory"
        self.run.mkdir(parents=True, exist_ok=True)
        self.out_png = self.run / "slide-4.png"
        self.out_png.write_bytes(b"baked")

    def tearDown(self):
        self.td.cleanup()

    def _emit(self, data):
        return RT.emit_edit_slide(
            self.out_png, "slide-4", self.template_html, None, None, data,
            template_id="numbered", template_pool="lc",
        )

    def _emit_runtime(self, data):
        """Studio runtime rebake path (--tweaks): build guards OFF."""
        return RT.emit_edit_slide(
            self.out_png, "slide-4", self.template_html, None, None, data,
            template_id="numbered", template_pool="lc",
            enforce_build_guards=False,
        )

    # --- RED scenario: the old behaviour the gate must catch ----------------

    def test_dead_path_slot_hard_fails(self):
        """PHOTO_MAIN_PATH pointing at a never-written file → SystemExit."""
        with self.assertRaises(SystemExit) as cm:
            self._emit({"PHOTO_MAIN_PATH": "projects/2026-06-15/best-memory/slide-4-bg.png"})
        self.assertIn("does not", str(cm.exception).lower() + str(cm.exception))

    def test_demo_inheritance_hard_fails(self):
        """No per-post bg present → demo copied in → slide bg == demo → SystemExit."""
        # Slot points (relatively) at the demo file that copytree brings in.
        with self.assertRaises(SystemExit) as cm:
            self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_main.png"})
        self.assertIn("demo", str(cm.exception).lower())

    # --- GREEN scenario: per-post bg correctly routed -----------------------

    def test_per_post_bg_survives_and_passes(self):
        """A per-post bg already in the slide dir is NOT clobbered by the demo and
        the gate passes (md5 != demo, path resolves)."""
        sdir = self.run / "_slides" / "slide-4" / "_ai_bg"
        sdir.mkdir(parents=True, exist_ok=True)
        (sdir / "photo_main.png").write_bytes(b"REAL-per-post-generation-for-this-post")
        out = self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_main.png"})
        # Per-post bg preserved, not the demo.
        final_bg = (out / "_ai_bg" / "photo_main.png").read_bytes()
        self.assertEqual(final_bg, b"REAL-per-post-generation-for-this-post")
        self.assertNotEqual(final_bg, self.demo_bg.read_bytes())
        # Stale template build-time log not carried over the real bg.
        self.assertFalse((out / "_ai_bg" / "photo_main.log.md").exists())

    def test_per_post_bg_metadata_path_resolves(self):
        """metadata.json PHOTO_MAIN_PATH points at an existing slide-relative file."""
        import json
        sdir = self.run / "_slides" / "slide-4" / "_ai_bg"
        sdir.mkdir(parents=True, exist_ok=True)
        (sdir / "photo_main.png").write_bytes(b"REAL-per-post-generation-for-this-post")
        out = self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_main.png"})
        meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
        p = meta["data"]["PHOTO_MAIN_PATH"]
        self.assertEqual(p, "_ai_bg/photo_main.png")
        self.assertTrue((out / p).is_file())

    # --- Studio runtime rebake (--tweaks): the build guard MUST NOT hard-fail ---

    def test_runtime_rebake_dead_path_does_not_hard_fail(self):
        """fix-handoff-consolidate — on the Studio rebake path (enforce_build_guards
        =False) a *_PATH that doesn't resolve degrades to a warn, never SystemExit."""
        out = self._emit_runtime(
            {"PHOTO_MAIN_PATH": "projects/2026-06-15/best-memory/slide-4-bg.png"})
        self.assertTrue((out / "metadata.json").is_file())

    def test_runtime_rebake_demo_bg_does_not_hard_fail(self):
        """A slide bg byte-identical to the template demo must NOT kill a runtime
        rebake (legitimate for a not-yet-regenerated slide)."""
        out = self._emit_runtime({"PHOTO_MAIN_PATH": "_ai_bg/photo_main.png"})
        self.assertTrue((out / "metadata.json").is_file())

    # --- Build/authoring path STILL hard-fails (the guards stay correct there) ---

    def test_build_path_demo_bg_still_hard_fails(self):
        """Regression floor: with build guards ON (no --tweaks) a demo-md5 bg still
        raises SystemExit — Lane 1 stays fully active on the authoring/build path."""
        with self.assertRaises(SystemExit):
            self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_main.png"})


class AiBgVariantDivergenceTests(unittest.TestCase):
    """fix-bg-variant-divergence: a template whose _ai_bg/ accumulated multiple
    iteration variants (photo_main + photo_preview + photo_slide01) must resolve to
    ONE canonical photo_main.png in BOTH the bake path (persisted PHOTO_MAIN_PATH)
    and the front path (slide HTML static src), with no divergence — and the
    non-canonical variants must NOT be carried into the self-contained slide dir."""

    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        self.tdir = self.root / "brand_context" / "templates" / "lc" / "numbered"
        (self.tdir / "_ai_bg").mkdir(parents=True, exist_ok=True)
        self.template_html = self.tdir / "template.html"
        self.template_html.write_text(_TMPL_HTML, encoding="utf-8")
        # Template _ai_bg has THREE variants — the accumulation defect.
        (self.tdir / "_ai_bg" / "photo_main.png").write_bytes(b"CANON-main")
        (self.tdir / "_ai_bg" / "photo_main.log.md").write_text("main", encoding="utf-8")
        (self.tdir / "_ai_bg" / "photo_preview.png").write_bytes(b"VARIANT-preview")
        (self.tdir / "_ai_bg" / "photo_preview.log.md").write_text("prev", encoding="utf-8")
        (self.tdir / "_ai_bg" / "photo_slide01.png").write_bytes(b"VARIANT-slide01")
        self.run = self.root / "projects" / "2026-06-15" / "post"
        self.run.mkdir(parents=True, exist_ok=True)
        self.out_png = self.run / "slide-1.png"
        self.out_png.write_bytes(b"baked")

    def tearDown(self):
        self.td.cleanup()

    def _emit(self, data):
        # Per-post bg already written into the slide dir (the authoritative gen),
        # so the demo-md5 gate is satisfied and the build path doesn't hard-fail.
        sdir = self.run / "_slides" / "slide-1" / "_ai_bg"
        sdir.mkdir(parents=True, exist_ok=True)
        (sdir / "photo_main.png").write_bytes(b"REAL-per-post")
        return RT.emit_edit_slide(
            self.out_png, "slide-1", self.template_html, None, None, data,
            template_id="numbered", template_pool="lc",
        )

    def test_variant_helpers(self):
        self.assertTrue(RT._is_noncanonical_ai_bg_variant("photo_preview.png"))
        self.assertTrue(RT._is_noncanonical_ai_bg_variant("photo_slide01.png"))
        self.assertTrue(RT._is_noncanonical_ai_bg_variant("photo_preview.log.md"))
        self.assertFalse(RT._is_noncanonical_ai_bg_variant("photo_main.png"))
        self.assertFalse(RT._is_noncanonical_ai_bg_variant("photo_main.log.md"))
        # HYBRID companion kept.
        self.assertFalse(RT._is_noncanonical_ai_bg_variant("photo_main_setup.png"))
        # Unrelated files untouched.
        self.assertFalse(RT._is_noncanonical_ai_bg_variant("logo.png"))

    def test_noncanonical_variants_not_copied_into_slide(self):
        out = self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_main.png"})
        ai_bg = out / "_ai_bg"
        self.assertTrue((ai_bg / "photo_main.png").is_file())
        # The accumulated variants must NOT have been copied in.
        self.assertFalse((ai_bg / "photo_preview.png").exists())
        self.assertFalse((ai_bg / "photo_preview.log.md").exists())
        self.assertFalse((ai_bg / "photo_slide01.png").exists())

    def test_mispinned_variant_canonicalized_in_metadata(self):
        """A PHOTO_MAIN_PATH the caller pinned to a non-canonical variant is
        rewritten to the canonical photo_main.png — so the persisted data agrees
        with the slide HTML's static src='_ai_bg/photo_main.png' (no divergence)."""
        import json
        out = self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_slide01.png"})
        meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["data"]["PHOTO_MAIN_PATH"], "_ai_bg/photo_main.png")
        self.assertTrue((out / meta["data"]["PHOTO_MAIN_PATH"]).is_file())

    def test_bake_and_front_resolve_same_file(self):
        """The slide HTML (front) statically references _ai_bg/photo_main.png and
        the persisted PHOTO_MAIN_PATH (bake) now points at the SAME canonical file."""
        import json
        out = self._emit({"PHOTO_MAIN_PATH": "_ai_bg/photo_slide01.png"})
        front_html = (out / "template.html").read_text(encoding="utf-8")
        self.assertIn('src="_ai_bg/photo_main.png"', front_html)
        meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["data"]["PHOTO_MAIN_PATH"], "_ai_bg/photo_main.png")

    def test_canonicalize_helper_idempotent_and_scoped(self):
        sdir = self.run / "_slides" / "slide-1"
        (sdir / "_ai_bg").mkdir(parents=True, exist_ok=True)
        (sdir / "_ai_bg" / "photo_main.png").write_bytes(b"x")
        # Already canonical → unchanged.
        self.assertEqual(
            RT._canonicalize_ai_bg_path("_ai_bg/photo_main.png", sdir),
            "_ai_bg/photo_main.png")
        # Non-canonical variant → canonicalized.
        self.assertEqual(
            RT._canonicalize_ai_bg_path("_ai_bg/photo_preview.png", sdir),
            "_ai_bg/photo_main.png")
        # data:/http: and non-_ai_bg values untouched.
        self.assertEqual(RT._canonicalize_ai_bg_path("data:image/png;base64,AAA", sdir),
                         "data:image/png;base64,AAA")
        self.assertEqual(RT._canonicalize_ai_bg_path("assets/logo.png", sdir),
                         "assets/logo.png")
        # HYBRID *_setup companion untouched.
        self.assertEqual(RT._canonicalize_ai_bg_path("_ai_bg/photo_main_setup.png", sdir),
                         "_ai_bg/photo_main_setup.png")


if __name__ == "__main__":
    unittest.main()

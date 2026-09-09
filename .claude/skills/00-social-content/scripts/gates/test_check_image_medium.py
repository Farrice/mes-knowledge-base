# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for check_image_medium.py — the image-medium conference (r6-1-estilo, case 1).

Tests the medium-comparison LOGIC (deterministic, text-first) + the advisory contract:
  - a cartoon-example ref prompted as a documentary photo -> WARN (the run-07 services-billboard).
  - a cartoon ref prompted as illustration -> clean (matching).
  - a photo ref prompted as a photo -> clean.
  - a `mixed` brand default with a silent §2 -> never warns.
  - the gate ALWAYS exits 0 (advisory — a warning never blocks the build).

Run:
    uv run test_check_image_medium.py
    or: python test_check_image_medium.py
"""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_image_medium import (  # noqa: E402
    canonical_medium,
    mediums_in_text,
    negated_mediums_in_text,
    rationale_medium,
    brand_default_medium,
    parse_prompt_delta,
    evaluate,
    main,
    MIXED,
    PHOTO,
    ILLUSTRATION,
    WATERCOLOR,
    RENDER_3D,
)


# ---------------------------------------------------------------------------------------
# Fixtures — minimal rationale + template.html pairs.
# ---------------------------------------------------------------------------------------

def _rationale(medium_line: str) -> str:
    """A 4-section rationale whose §2 image-block line carries the given `medium:` read (or, if
    medium_line is '', no medium line at all)."""
    block = "- Image / hero · AI-integrated · the scene fills the canvas.\n"
    if medium_line:
        block += f"  - {medium_line}\n"
    return f"""# rationale — fixture

## ① Form + tree-path-with-why
form: c-integrated-text. Q1 no, Q4 yes -> C.

## ② Per-block breakdown
{block}  - containment: full-bleed
  - legibility-method: natural-composition

## ③ Pipeline
edit_mode: total-recompose. when_ai_runs: every post.

## ④ Ambiguity (examined)
No ambiguity — ruled out B1 because there's no blank in-scene surface.
"""


def _html(prompt_delta: str) -> str:
    """A template.html with one [ai-image-zone] block carrying the given prompt_delta."""
    return f"""<!doctype html><html><body>
<div data-slot="headline">Sample</div>
<!-- [ai-image-zone id="hero"]
prompt_delta: |
  {prompt_delta}
output_aspect: "4:5"
[/ai-image-zone] -->
</body></html>"""


CARTOON_RATIONALE = _rationale("medium: flat-illustration — the brand default is mixed, this ref is a flat vector cartoon")
PHOTO_RATIONALE = _rationale("medium: photo — documentary photograph of the desk scene")
SILENT_RATIONALE = _rationale("")  # no §2 medium line

PHOTO_PROMPT_HTML = _html("documentary photograph, warm coral palette, fine paper-grain texture, soft natural light")
ILLUSTRATION_PROMPT_HTML = _html("flat vector illustration in the warm coral palette, clean line work, fine grain")
WATERCOLOR_PROMPT_HTML = _html("loose watercolour wash, warm coral palette, soft natural light")


class TestCanonicalMedium(unittest.TestCase):
    def test_known_mediums(self):
        self.assertEqual(canonical_medium("flat-illustration"), ILLUSTRATION)
        self.assertEqual(canonical_medium("flat vector illustration"), ILLUSTRATION)
        self.assertEqual(canonical_medium("cartoon"), ILLUSTRATION)
        self.assertEqual(canonical_medium("photo"), PHOTO)
        self.assertEqual(canonical_medium("documentary photograph"), PHOTO)
        self.assertEqual(canonical_medium("photorealistic-3d-render"), RENDER_3D)
        self.assertEqual(canonical_medium("watercolour"), WATERCOLOR)

    def test_mixed(self):
        self.assertEqual(canonical_medium("mixed"), MIXED)

    def test_unknown_and_empty(self):
        self.assertIsNone(canonical_medium(""))
        self.assertIsNone(canonical_medium("   "))
        self.assertIsNone(canonical_medium("greyscale"))  # not a medium token here
        self.assertIsNone(canonical_medium(None))

    def test_3d_beats_photo(self):
        # "photorealistic 3d" must classify 3d-render, not photo (ordering matters).
        self.assertEqual(canonical_medium("photorealistic 3d render"), RENDER_3D)


class TestMediumsInText(unittest.TestCase):
    def test_single(self):
        self.assertEqual(mediums_in_text("a documentary photograph, soft light"), [PHOTO])
        self.assertEqual(mediums_in_text("flat vector illustration, clean lines"), [ILLUSTRATION])

    def test_none(self):
        self.assertEqual(mediums_in_text("warm coral palette, fine grain, soft light"), [])
        self.assertEqual(mediums_in_text(""), [])

    def test_negatives(self):
        self.assertEqual(negated_mediums_in_text("no illustration, no cartoon"), [ILLUSTRATION])
        self.assertEqual(negated_mediums_in_text("no photographs here"), [PHOTO])


class TestRationaleMedium(unittest.TestCase):
    def test_reads_section2_medium(self):
        self.assertEqual(rationale_medium(CARTOON_RATIONALE), ILLUSTRATION)
        self.assertEqual(rationale_medium(PHOTO_RATIONALE), PHOTO)

    def test_silent_section2(self):
        self.assertIsNone(rationale_medium(SILENT_RATIONALE))

    def test_does_not_read_dash_why_as_medium(self):
        # The "why" after the em-dash must not leak into the medium value.
        r = _rationale("medium: flat-illustration — not a documentary photograph despite the realism")
        self.assertEqual(rationale_medium(r), ILLUSTRATION)


class TestPromptDelta(unittest.TestCase):
    def test_extracts_prompt(self):
        d = parse_prompt_delta(PHOTO_PROMPT_HTML)
        self.assertIn("documentary photograph", d)
        self.assertNotIn("output_aspect", d)


class TestBrandDefault(unittest.TestCase):
    def test_default_medium(self):
        style = "<!--meta\ndefault_medium: mixed\npalette:\n  - white\n-->"
        self.assertEqual(brand_default_medium(style), MIXED)

    def test_legacy_medium_key(self):
        # A pre-r6 brand file with the old `medium:` key still resolves (back-compat).
        style = "<!--meta\nmedium: photorealistic-3d-render\n-->"
        self.assertEqual(brand_default_medium(style), RENDER_3D)

    def test_none(self):
        self.assertIsNone(brand_default_medium("<!--meta\npalette:\n  - white\n-->"))
        self.assertIsNone(brand_default_medium(""))


class TestEvaluateWarnings(unittest.TestCase):
    # --- THE spec fixtures ---------------------------------------------------------------
    def test_cartoon_example_photo_prompt_warns(self):
        """Spec fixture 1: a cartoon-example ref, a photo prompt -> WARNING."""
        res = evaluate(CARTOON_RATIONALE, PHOTO_PROMPT_HTML)
        self.assertFalse(res["ok"])
        self.assertIsNotNone(res["warn"])
        self.assertEqual(res["ref_medium"], ILLUSTRATION)
        self.assertIn(PHOTO, res["prompt_mediums"])
        self.assertIn("inverts the example", res["warn"])

    def test_matching_cartoon_is_clean(self):
        """Spec fixture 2: a cartoon-example ref, an illustration prompt -> clean."""
        res = evaluate(CARTOON_RATIONALE, ILLUSTRATION_PROMPT_HTML)
        self.assertTrue(res["ok"])
        self.assertIsNone(res["warn"])

    def test_photo_example_photo_prompt_is_clean(self):
        """Spec fixture 3: a photo-example ref, a photo prompt -> clean."""
        res = evaluate(PHOTO_RATIONALE, PHOTO_PROMPT_HTML)
        self.assertTrue(res["ok"])
        self.assertIsNone(res["warn"])

    # --- the negative-driven inversion ---------------------------------------------------
    def test_negative_forbids_ref_medium_warns(self):
        """A cartoon ref whose prompt carries 'no illustration' (the grade's blanket negative)
        -> WARN even with no positive photo term."""
        html = _html("warm coral palette, fine grain, no illustration, no cartoon")
        res = evaluate(CARTOON_RATIONALE, html)
        self.assertFalse(res["ok"])
        self.assertIn("medium-negative", res["warn"])

    # --- the soft-default / mixed paths --------------------------------------------------
    def test_mixed_brand_default_never_warns(self):
        """§2 silent + brand default_medium: mixed -> a mixed brand may ship any medium; no warn."""
        style = "<!--meta\ndefault_medium: mixed\n-->"
        res = evaluate(SILENT_RATIONALE, PHOTO_PROMPT_HTML, style)
        self.assertTrue(res["ok"])
        self.assertEqual(res["ref_medium"], MIXED)

    def test_default_medium_fallback_can_warn(self):
        """§2 silent + a CONCRETE brand default that the prompt inverts -> WARN off the default
        (the ambiguous-ref path still confers)."""
        style = "<!--meta\ndefault_medium: flat-illustration\n-->"
        res = evaluate(SILENT_RATIONALE, PHOTO_PROMPT_HTML, style)
        self.assertFalse(res["ok"])
        self.assertEqual(res["ref_source"], "ai-image-style default_medium")

    def test_no_medium_anywhere_is_clean(self):
        """§2 silent, no brand style, prompt names a medium -> nothing to compare against; clean
        (the conference needs a ref medium to confer on — it never invents one)."""
        res = evaluate(SILENT_RATIONALE, PHOTO_PROMPT_HTML, None)
        self.assertTrue(res["ok"])
        self.assertIsNone(res["ref_medium"])

    def test_no_ai_zone_is_clean(self):
        """No [ai-image-zone] (pure HTML template) -> no prompt to confer on; clean."""
        html = "<!doctype html><html><body><div data-slot='headline'>x</div></body></html>"
        res = evaluate(CARTOON_RATIONALE, html)
        self.assertTrue(res["ok"])

    def test_prompt_naming_both_mediums_does_not_warn(self):
        """A prompt that names the ref's medium AND another (an explicit mixed scene) is not an
        inversion — the ref's medium is present, so no warn."""
        html = _html("flat vector illustration with an inset documentary photograph detail")
        res = evaluate(CARTOON_RATIONALE, html)
        self.assertTrue(res["ok"])


class TestAdvisoryContract(unittest.TestCase):
    """The whole point: this gate NEVER blocks. main() returns 0 even on a warning."""

    def _run_main(self, rationale_text: str, html: str) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as d:
            rp = Path(d) / "rationale.md"
            hp = Path(d) / "template.html"
            rp.write_text(rationale_text, encoding="utf-8")
            hp.write_text(html, encoding="utf-8")
            argv = sys.argv
            sys.argv = ["check_image_medium.py", "--rationale", str(rp),
                        "--template-html", str(hp)]
            err = io.StringIO()
            try:
                with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
                    code = main()
            finally:
                sys.argv = argv
            return code, err.getvalue()

    def test_warning_still_exits_zero(self):
        code, err = self._run_main(CARTOON_RATIONALE, PHOTO_PROMPT_HTML)
        self.assertEqual(code, 0)  # advisory — a warning is NOT a block
        self.assertIn("[warn]", err)

    def test_clean_exits_zero(self):
        code, err = self._run_main(PHOTO_RATIONALE, PHOTO_PROMPT_HTML)
        self.assertEqual(code, 0)
        self.assertNotIn("[warn]", err)


if __name__ == "__main__":
    unittest.main(verbosity=2)

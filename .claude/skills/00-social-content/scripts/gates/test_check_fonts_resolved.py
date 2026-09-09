# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for check_fonts_resolved.py — gate hook A (SPEC-C C3).

Asserts the sidecar-reading verdict logic: resolved → exit 0, fallback → exit 2,
missing sidecar → exit 1. Invoked via subprocess (the logic lives in main()).

Run:
    uv run test_check_fonts_resolved.py
    or: python test_check_fonts_resolved.py
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "check_fonts_resolved.py"


def _run(args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True, text=True,
    )


class CheckFontsResolved(unittest.TestCase):
    def test_resolved_exit_0(self):
        with tempfile.TemporaryDirectory() as td:
            png = Path(td) / "slide.png"
            sidecar = png.with_suffix(png.suffix + ".fontcheck.json")
            sidecar.write_text(json.dumps({"family": "Anton", "resolved": True}), encoding="utf-8")
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("resolved", r.stdout)

    def test_fallback_exit_2(self):
        with tempfile.TemporaryDirectory() as td:
            png = Path(td) / "slide.png"
            sidecar = png.with_suffix(png.suffix + ".fontcheck.json")
            sidecar.write_text(json.dumps({"family": "Anton", "resolved": False}), encoding="utf-8")
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 2)
            self.assertIn("did NOT load", r.stderr)

    def test_missing_sidecar_exit_1(self):
        with tempfile.TemporaryDirectory() as td:
            png = Path(td) / "slide.png"
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 1)

    def test_direct_fontcheck_path(self):
        with tempfile.TemporaryDirectory() as td:
            sidecar = Path(td) / "x.json"
            sidecar.write_text(json.dumps({"family": "Bebas", "resolved": True}), encoding="utf-8")
            r = _run(["--fontcheck", str(sidecar)])
            self.assertEqual(r.returncode, 0, r.stderr)


# Templates for the SPEC-r5g not-applicable detection: a gate must never be satisfiable by
# ADDING visible elements — no display-font HTML text -> SKIP, never demand a ghost word.
HTML_NO_DISPLAY_TEXT = """
<style>
@font-face { font-family: 'Anton'; src: url('fonts/anton.woff2'); }
.masthead { font-family: var(--brand-body, 'Inter', sans-serif); }
</style>
<div class="masthead" data-slot="MASTHEAD"></div>
"""

HTML_USES_DISPLAY_VAR = """
<style>
.headline { font-family: var(--brand-display, 'Anton', sans-serif); }
</style>
<div class="headline" data-slot="HEADLINE">{{{HEADLINE}}}</div>
"""

HTML_USES_DISPLAY_LITERAL = """
<style>
.headline { font-family: 'Anton', sans-serif; }
</style>
<div class="headline" data-slot="HEADLINE">{{{HEADLINE}}}</div>
"""


def _write_case(td, html=None, **sidecar_data):
    """Write slide.png sidecar (+ optional template.html) into td; return the png path."""
    png = Path(td) / "slide.png"
    png.with_suffix(png.suffix + ".fontcheck.json").write_text(
        json.dumps(sidecar_data), encoding="utf-8")
    if html is not None:
        (Path(td) / "template.html").write_text(html, encoding="utf-8")
    return png


class CheckFontsNotApplicable(unittest.TestCase):
    """SPEC-r5g: unresolved + NO display-font HTML text -> SKIP (exit 0), never exit 2."""

    def test_no_display_text_skips(self):
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, html=HTML_NO_DISPLAY_TEXT, family="Anton", resolved=False)
            r = _run(["--render-output", str(png)])  # template.html auto-discovered
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("[skip]", r.stdout)
            self.assertIn("Do NOT add visible text", r.stdout)

    def test_display_var_usage_still_fails(self):
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, html=HTML_USES_DISPLAY_VAR, family="Anton", resolved=False)
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 2)
            self.assertIn("did NOT load", r.stderr)

    def test_display_literal_usage_still_fails(self):
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, html=HTML_USES_DISPLAY_LITERAL, family="Anton", resolved=False)
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 2)

    def test_font_face_declaration_is_not_usage(self):
        # the @font-face block names the family but nothing USES it -> still a SKIP.
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, html=HTML_NO_DISPLAY_TEXT, family="Anton", resolved=False)
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 0, r.stderr)

    def test_explicit_template_html_flag(self):
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, family="Anton", resolved=False)
            tpl = Path(td) / "other-name.html"
            tpl.write_text(HTML_NO_DISPLAY_TEXT, encoding="utf-8")
            r = _run(["--render-output", str(png), "--template-html", str(tpl)])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("[skip]", r.stdout)


class CheckFontsInvisibleProbe(unittest.TestCase):
    """A renderer that probes via document.fonts.load() writes probe_resolved — that verdict
    wins (no visible text involved either way)."""

    def test_probe_resolved_passes(self):
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, family="Anton", resolved=False, probe_resolved=True)
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("invisible", r.stdout)

    def test_probe_unresolved_fails_even_without_display_text(self):
        # the probe says the @font-face itself is broken -> fail, and the message must point
        # at the @font-face, not at adding text.
        with tempfile.TemporaryDirectory() as td:
            png = _write_case(td, html=HTML_NO_DISPLAY_TEXT, family="Anton",
                              resolved=False, probe_resolved=False)
            r = _run(["--render-output", str(png)])
            self.assertEqual(r.returncode, 2)
            self.assertIn("do NOT add visible text", r.stderr)


if __name__ == "__main__":
    unittest.main()

"""
Tests for the canonical-template-origin hard guard
(render_template.guard_canonical_template_origin) — Lane 2, re-render escape-hatch.

Root cause (run-09): hitting a template defect mid-run, the orchestrator hand-authored
a patched `_patches/<x>/template.html` with NO `_shared/` sibling, repointed the
re-render origin there, and self-certified "verified by eye — PASS". The missing
`_shared/` silently dropped brand-font injection. This guard refuses a re-render whose
template origin is non-canonical:

  - origin under a `_patches/` (improvised) dir  → HARD-FAIL
  - origin with no resolvable `_shared/` sibling → HARD-FAIL
  - a real pool template (templates/<pool>/<slug> with ../_shared) → PASS
  - an emitted self-contained slide (_slides/<slide-N> with ../_shared) → PASS

Run:
    uv run python -m pytest test_canonical_origin_guard.py
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

_HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("render_template", _HERE / "render_template.py")
RT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RT)


class CanonicalOriginGuardTests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)

    def tearDown(self):
        self.td.cleanup()

    def _pool_template(self) -> Path:
        """A canonical pool template: templates/<pool>/<slug>/ with a ../_shared sibling."""
        pool = self.root / "brand_context" / "templates" / "linkedin-carousel"
        slug = pool / "fullbleed-overlay-cover"
        slug.mkdir(parents=True, exist_ok=True)
        (slug / "template.html").write_text("<html></html>", encoding="utf-8")
        shared = pool / "_shared"
        shared.mkdir(parents=True, exist_ok=True)
        (shared / "styles.css").write_text("/* brand */", encoding="utf-8")
        return slug

    def _patches_template(self) -> Path:
        """The run-09 escape-hatch: _patches/<x>/template.html, no _shared/ sibling."""
        d = self.root / "project" / "_patches" / "cover-patched"
        d.mkdir(parents=True, exist_ok=True)
        (d / "template.html").write_text("<html></html>", encoding="utf-8")
        return d

    def _emitted_slide(self) -> Path:
        """A canonical emitted slide: _slides/<slide-N>/ with a ../_shared sibling."""
        slides = self.root / "run" / "_slides"
        sdir = slides / "slide-01"
        sdir.mkdir(parents=True, exist_ok=True)
        shared = slides / "_shared"
        shared.mkdir(parents=True, exist_ok=True)
        (shared / "styles.css").write_text("/* brand */", encoding="utf-8")
        return sdir

    # --- RED: non-canonical origins must hard-fail ---

    def test_patches_origin_hard_fails(self):
        bad = self._patches_template()
        with self.assertRaises(SystemExit) as cm:
            RT.guard_canonical_template_origin(bad)
        self.assertIn("_patches", str(cm.exception))

    def test_missing_shared_sibling_hard_fails(self):
        """An ad-hoc dir (no _patches marker) but with no resolvable _shared/ → fail."""
        d = self.root / "scratch" / "hand-authored"
        d.mkdir(parents=True, exist_ok=True)
        (d / "template.html").write_text("<html></html>", encoding="utf-8")
        with self.assertRaises(SystemExit) as cm:
            RT.guard_canonical_template_origin(d)
        self.assertIn("_shared", str(cm.exception))

    # --- GREEN: canonical origins pass ---

    def test_pool_template_passes(self):
        RT.guard_canonical_template_origin(self._pool_template())  # must not raise

    def test_emitted_slide_passes(self):
        RT.guard_canonical_template_origin(self._emitted_slide())  # must not raise


if __name__ == "__main__":
    unittest.main()

"""
Tests for the output-pool hard guard in render_template.guard_output_pool
(r8 output-path-canonical).

Root cause (run-09): the builder hand-composed the render --output path and
mistyped the pool segment — `templates/linux-carousel/<slug>/preview.png` instead
of `templates/linkedin-carousel/...` — and the render silently created the stray
top-level pool dir. The guard refuses to materialize a brand-new top-level pool as
a render side-effect: a typo'd pool hard-fails (suggesting the real pool) while a
correct pool, and genuine first-time creation, both pass.

Run:
    uv run python -m pytest test_output_pool_guard.py
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

_HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("render_template", _HERE / "render_template.py")
RT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RT)


def _make_pool(templates_dir: Path, name: str) -> Path:
    pool = templates_dir / name
    (pool).mkdir(parents=True, exist_ok=True)
    (pool / "manifest.json").write_text("{}", encoding="utf-8")
    return pool


class OutputPoolGuardTests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        self.templates = self.root / "brand_context" / "templates"
        _make_pool(self.templates, "linkedin-carousel")

    def tearDown(self):
        self.td.cleanup()

    def test_typo_pool_errors_with_suggestion(self):
        """A mistyped pool whose dir doesn't exist, while a real pool exists, errors."""
        bad = self.templates / "linux-carousel" / "numbered-statement-body" / "preview.png"
        with self.assertRaises(SystemExit) as cm:
            RT.guard_output_pool(bad)
        msg = str(cm.exception)
        self.assertIn("linux-carousel", msg)
        self.assertIn("linkedin-carousel", msg)  # the suggestion / known-pools list
        # And it must NOT have created the stray dir.
        self.assertFalse((self.templates / "linux-carousel").exists())

    def test_correct_pool_passes(self):
        """Output into the existing pool is allowed (no raise)."""
        good = self.templates / "linkedin-carousel" / "hero-typographic" / "preview.png"
        RT.guard_output_pool(good)  # must not raise

    def test_first_time_pool_creation_allowed(self):
        """When templates/ holds NO pool yet, first-ever creation is not the render's
        concern — guard is permissive (the onboarding writer owns creation)."""
        empty = self.root / "fresh" / "templates"
        empty.mkdir(parents=True, exist_ok=True)
        out = empty / "brand-new-pool" / "slug" / "preview.png"
        RT.guard_output_pool(out)  # must not raise

    def test_output_outside_templates_tree_ignored(self):
        """An --output not under any templates/<pool>/ path is a no-op."""
        RT.guard_output_pool(self.root / "Downloads" / "scratch" / "x.png")  # no raise


if __name__ == "__main__":
    unittest.main()

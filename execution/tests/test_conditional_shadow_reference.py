"""Preserve approved conditional support without permitting new overlay surfaces."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "adaptive_floor", Path(__file__).resolve().parents[1] / "verify_global_adaptive_judgment_floor.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SENTENCE = next(iter(MODULE.CONDITIONAL_OVERLAY_REFERENCES.values()))


class ConditionalOverlayTests(unittest.TestCase):
    def check(self, content, *, other=None, routing=False, banned=False):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            owner = root / "godin-ai-creative-practice.md"
            owner.write_text(content)
            if other:
                (root / "unapproved-owner.md").write_text(other)
            forbidden = root / "systems-thinking-expertise-intelligence-overlay"
            if banned:
                forbidden.mkdir()
            route = root / "routing.txt"
            if routing:
                route.write_text(SENTENCE)
            with patch.multiple(
                MODULE,
                ACTIVE_SURFACE_ROOTS=((root, "*.md"),),
                ROUTING_SURFACES=(route,),
                BANNED_OVERLAY_SURFACES=(forbidden,),
                ALLOWED_OVERLAY_SURFACE_REFERENCES=set(),
                CONDITIONAL_OVERLAY_REFERENCES={owner: SENTENCE},
            ):
                MODULE.check_no_competing_overlay_surfaces()

    def test_approved_conditional_reference_passes(self):
        self.check("# Godin\n" + SENTENCE)

    def test_unconditional_activation_fails(self):
        with self.assertRaises(AssertionError):
            self.check(SENTENCE.replace("only during system-gap diagnosis when its activation test is met", "on every task"))

    def test_additional_reference_fails(self):
        with self.assertRaises(AssertionError):
            self.check(SENTENCE + "\n" + SENTENCE)

    def test_other_owner_not_allowlisted(self):
        with self.assertRaises(AssertionError):
            self.check(SENTENCE, other=SENTENCE)

    def test_router_reference_still_fails(self):
        with self.assertRaises(AssertionError):
            self.check(SENTENCE, routing=True)

    def test_new_overlay_surface_still_fails(self):
        with self.assertRaises(AssertionError):
            self.check(SENTENCE, banned=True)


if __name__ == "__main__":
    unittest.main()

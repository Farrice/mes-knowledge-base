#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""test_migrate_data_slots.py — migrate() stamping + handle dedupe (r5f F1a sibling a).

The defect (cover-photo-hook): a template authors the handle on the CONTAINER
(`<div class="bottom-pill" data-slot="CALLOUT_TEXT">`) while the placeholder lives
in a child whose entire content is that placeholder — migrate() used to stamp the
child too, duplicating the handle. One handle must map to ONE zone: the editor and
the bake otherwise target two elements (text edits wipe the container's styled
children; box tweaks apply twice).

Run: uv run test_migrate_data_slots.py
"""

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from migrate_data_slots import infer_handle, migrate  # noqa: E402


PILL_TEMPLATE = (
    '<div class="bottom-pill" data-slot="CALLOUT_TEXT">'
    '  <div class="bottom-pill-text body">{{{CALLOUT_TEXT}}}</div>'
    '  <div class="pill-arrow">&#8594;</div>'
    '</div>'
)


class TestMigrateStamping(unittest.TestCase):
    def test_text_zone_gets_handle(self):
        out, n = migrate('<div class="kicker">{{KICKER}}</div>')
        self.assertEqual(n, 1)
        self.assertIn('data-slot="KICKER"', out)

    def test_image_zone_gets_suffix_stripped_handle(self):
        out, n = migrate(
            '<div class="photo-zone"><img src="{{PHOTO_MAIN_PATH}}"></div>')
        self.assertEqual(n, 1)
        self.assertIn('<div data-slot="PHOTO_MAIN"', out)

    def test_idempotent(self):
        once, n1 = migrate('<div class="kicker">{{KICKER}}</div>')
        twice, n2 = migrate(once)
        self.assertEqual(n1, 1)
        self.assertEqual(n2, 0)
        self.assertEqual(once, twice)

    def test_infer_handle_strips_suffixes(self):
        self.assertEqual(infer_handle("{{PHOTO_MAIN_PATH}}"), "PHOTO_MAIN")
        self.assertEqual(infer_handle("{{{HERO}}}"), "HERO")
        self.assertIsNone(infer_handle("no placeholder"))


class TestMigrateDedupe(unittest.TestCase):
    """One handle = one zone — never stamp a handle an ancestor already claims."""

    def test_ancestor_claimed_handle_not_restamped(self):
        out, n = migrate(PILL_TEMPLATE)
        self.assertEqual(n, 0, "child of an already-claimed handle must be skipped")
        self.assertEqual(out.count('data-slot="CALLOUT_TEXT"'), 1)
        # The original container keeps the handle; the text child stays clean.
        self.assertIn('class="bottom-pill" data-slot="CALLOUT_TEXT"', out)
        self.assertNotIn('data-slot="CALLOUT_TEXT" class="bottom-pill-text', out)

    def test_handle_stamped_once_within_single_run(self):
        # Two un-stamped zones sharing one placeholder name: only the first
        # occurrence gets the handle (a second stamp would recreate the dup defect).
        html = (
            '<div class="a">{{TITLE}}</div>'
            '<div class="b">{{TITLE}}</div>'
        )
        out, n = migrate(html)
        self.assertEqual(n, 1)
        self.assertEqual(out.count('data-slot="TITLE"'), 1)

    def test_unrelated_handles_still_stamped(self):
        html = PILL_TEMPLATE + '<div class="kicker">{{KICKER}}</div>'
        out, n = migrate(html)
        self.assertEqual(n, 1)
        self.assertIn('data-slot="KICKER"', out)
        self.assertEqual(out.count('data-slot="CALLOUT_TEXT"'), 1)


if __name__ == "__main__":
    unittest.main()

# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for check_buried_headline.py — Check I (buried-headline gate, r8).

Synthetic HTML only (no hardcoded slug): the buried recipe (text z < opaque photo z, overlapping)
flags; the clean recipe (text z > photo z) passes; the transparency exception (declared cutout /
honored mix-blend-mode) suppresses; non-overlapping zones pass. Run: uv run test_check_buried_headline.py
"""
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_buried_headline import evaluate, parse_zones, bbox_overlap  # noqa: E402

# --- BURIED: HEADLINE text at z-index 1, OPAQUE photo at z-index 10 overlapping it (run-09). ---
BURIED = '''
<style>
  .headline-zone { position:absolute; top:8%; left:0%; width:90%; z-index:1; }
  .photo-zone { position:absolute; top:20%; left:8%; width:84%; height:50%; z-index:10; }
</style>
<div class="headline-zone" data-slot="HEADLINE">{{{HEADLINE}}}</div>
<div class="photo-zone" data-slot="PHOTO_MAIN" data-zone="photo"><img src="{{PHOTO_MAIN_PATH}}"></div>
'''

# --- CLEAN: full-bleed photo at z-index 0, text zones at z-index 10 ON TOP (the canonical pattern). ---
CLEAN = '''
<style>
  .bg { position:absolute; inset:0; z-index:0; }
  .headline { position:absolute; top:22%; left:7%; width:86%; height:32%; z-index:10; }
  .body-text { position:absolute; top:57%; left:7%; width:86%; z-index:10; }
</style>
<div class="bg" data-slot="PHOTO_MAIN" data-zone="photo"><img src="x.png"></div>
<div class="headline" data-slot="HEADLINE">{{{HEADLINE}}}</div>
<div class="body-text" data-slot="BODY">{{{BODY}}}</div>
'''

# --- EXCEPTION A: same buried geometry but the image declares a transparent cutout → exempt. ---
CUTOUT = '''
<style>
  .headline-zone { position:absolute; top:8%; left:0%; width:90%; z-index:1; }
  .photo-zone { position:absolute; top:20%; left:8%; width:84%; height:50%; z-index:10; }
</style>
<div class="headline-zone" data-slot="HEADLINE">{{{HEADLINE}}}</div>
<div class="photo-zone" data-slot="PHOTO_MAIN" data-zone="photo" data-cutout="true"><img src="x.png"></div>
'''

# --- EXCEPTION B: same geometry but a HONORED mix-blend-mode is authored on the image → exempt. ---
BLEND = '''
<style>
  .headline-zone { position:absolute; top:8%; left:0%; width:90%; z-index:1; }
  .photo-zone { position:absolute; top:20%; left:8%; width:84%; height:50%; z-index:10; mix-blend-mode:multiply; }
</style>
<div class="headline-zone" data-slot="HEADLINE">{{{HEADLINE}}}</div>
<div class="photo-zone" data-slot="PHOTO_MAIN" data-zone="photo"><img src="x.png"></div>
'''

# --- NON-OVERLAP: text below the photo bbox, photo higher z but no intersection → pass. ---
NO_OVERLAP = '''
<style>
  .photo-zone { position:absolute; top:8%; left:8%; width:84%; height:40%; z-index:10; }
  .caption { position:absolute; top:80%; left:7%; width:86%; height:6%; z-index:1; }
</style>
<div class="photo-zone" data-slot="PHOTO_MAIN" data-zone="photo"><img src="x.png"></div>
<div class="caption" data-slot="CAPTION">words</div>
'''

# --- IMAGE BELOW TEXT but image is a CSS background-image full-bleed (no <img>); text z>img z → pass. ---
BG_FULLBLEED = '''
<style>
  .bg { position:absolute; inset:0; z-index:0; }
  .headline { position:absolute; top:20%; left:7%; width:86%; z-index:5; }
</style>
<div class="bg" style="background-image:url('_ai_bg/bg.png');" data-slot="PHOTO_MAIN" data-zone="photo"></div>
<div class="headline" data-slot="HEADLINE">{{{HEADLINE}}}</div>
'''


class TestBuriedHeadline(unittest.TestCase):
    def test_buried_flags(self):
        passed, flags = evaluate(BURIED)
        self.assertFalse(passed)
        self.assertTrue(any(f["text_slot"] == "HEADLINE" for f in flags))
        self.assertTrue(any(f["is_display"] for f in flags))

    def test_clean_passes(self):
        passed, flags = evaluate(CLEAN)
        self.assertTrue(passed, f"clean template wrongly flagged: {flags}")

    def test_transparent_cutout_exempt(self):
        passed, _ = evaluate(CUTOUT)
        self.assertTrue(passed, "a declared transparent cutout earns the woven exception")

    def test_honored_blend_mode_exempt(self):
        passed, _ = evaluate(BLEND)
        self.assertTrue(passed, "a honored mix-blend-mode earns the woven exception")

    def test_no_overlap_passes(self):
        passed, _ = evaluate(NO_OVERLAP)
        self.assertTrue(passed, "non-overlapping zones are never buried")

    def test_css_bg_under_text_passes(self):
        passed, _ = evaluate(BG_FULLBLEED)
        self.assertTrue(passed, "text above a CSS-bg photo is the clean pattern")

    def test_geometry_parsing(self):
        zones = {z.slot: z for z in parse_zones(BURIED) if z.slot}
        self.assertEqual(zones["HEADLINE"].z, 1)
        self.assertEqual(zones["PHOTO_MAIN"].z, 10)
        self.assertTrue(zones["HEADLINE"].is_text_slot())
        self.assertTrue(zones["PHOTO_MAIN"].is_photo_zone())
        self.assertTrue(zones["PHOTO_MAIN"].is_opaque())

    def test_bbox_overlap_fraction(self):
        # identical boxes overlap fully; disjoint boxes overlap 0.
        self.assertAlmostEqual(bbox_overlap((0, 0, 10, 10), (0, 0, 10, 10)), 1.0)
        self.assertEqual(bbox_overlap((0, 0, 10, 10), (50, 50, 10, 10)), 0.0)


if __name__ == "__main__":
    unittest.main()

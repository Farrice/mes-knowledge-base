# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0", "pyyaml>=6.0"]
# ///
"""Unit tests for check_treatment_contract.py — Check B (AIOS-190 W2).

Tests the treatment-match LOGIC (deterministic structural read), per the AIOS-190 brief:
  - rationale declares "AI-integrated" but the output is an HTML box -> flagged.
  - a raster zone declared-filled but rendered near-uniform-empty -> flagged.
plus the B1 surface-reuse fold and the happy paths.

Run:
    uv run test_check_treatment_contract.py
    or: python test_check_treatment_contract.py
"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_treatment_contract import (  # noqa: E402
    classify_treatment,
    ref_border_stats,
    containment_misread,
    find_undeclared_slots,
    parse_form,
    parse_block_treatments,
    parse_html_text_slots,
    has_ai_image_zone,
    declares_filled_raster,
    declares_surface_reuse,
    _per_block_section,
    parse_prompt_delta,
    parse_pipeline_edit_mode,
    parse_reserved_band_pct,
    html_text_bottom_extent,
    html_has_opaque_fullwidth_band,
    html_image_zone_is_full_bleed,
    accent_mask,
    detect_accent_regions,
    resolve_accent,
    DEFAULT_ACCENT_HEX,
    quadrant,
    size_band,
    parse_distinctive_elements,
    compare_elements_to_ref,
    evaluate,
    AI_INTEGRATED,
    HTML_OVERLAY,
    ICON_CHROME,
    # --- SPEC-r6g (items 8, 9, 6) ---
    slug_object_noun,
    hero_is_regenerated_per_post,
    face_is_hero,
    headshot_declared,
    is_placeholder_path,
    metadata_slot_value,
    seal_provenance_flags,
    IDENTITY_SLOT_KEY_RE,
    # --- D1 (studio-sweep, Check 15) ---
    static_hero_src_flags,
)

import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402

# Brand coral (~rgb(208,83,68), the DEFAULT accent) and neutral fills for synthetic fixtures.
CORAL = (208, 83, 68)
DARK = (24, 22, 20)
GREY = (130, 130, 130)
# A synthetic GREEN-accent brand (#22aa44) — proves Check 10 is brand-agnostic.
GREEN = (34, 170, 68)
GREEN_ACCENT = "#22aa44"


def _synth(width=200, height=250, bg=DARK, boxes=()):
    """Tiny synthetic PNG: a solid bg with optional coral (or other) boxes.

    boxes: iterable of (x0, y0, x1, y1, color) in [0,1] canvas fractions. Returns a PIL.Image
    so the tests exercise the real detect_accent_regions() pipeline (resize + mask + label)."""
    img = Image.new("RGB", (width, height), bg)
    arr = np.array(img)
    for x0, y0, x1, y1, color in boxes:
        arr[int(y0 * height):int(y1 * height), int(x0 * width):int(x1 * width)] = color
    return Image.fromarray(arr)

# A C-form rationale: headline AI-integrated/occluded, caption HTML, logo chrome.
RATIONALE_C = """
## ① Form
form: C — integrated-text.

## ② Per-block breakdown
- Headline "COLOQUE SEU FILHO" · AI-integrated · occluded behind the standing instructor; HTML cannot occlude.
- Caption "JIU-JITSU PARA CRIANCAS" · HTML overlay · bottom strip, plain bold caps, isolable.
- Brand logo · embedded icon / chrome · small mark, follows tokens.json chrome.

## ③ Pipeline
edit_mode: total-recompose. when_ai_runs: every post. extraction: AI generates the scene with the headline occluded.

## ④ Ambiguity (examined)
Considered HTML for the headline but the occlusion behind the instructor forbids it.
"""

# A B2 rationale that declares a filled hero raster zone.
RATIONALE_B2_FILLED = """
## ① Form
form: B2 — filled texture/landscape.

## ② Per-block breakdown
- Headline · HTML overlay · clean top zone, isolable.
- Caption · HTML overlay · thin bottom caption line, isolable.
- Chrome chain hero · AI-generated (hero) · full-bleed photographic subject; varies per post, filled every post.

## ③ Pipeline
edit_mode: partial — subject only. when_ai_runs: every post. extraction: AI generates the hero keeping a clean top.

## ④ Ambiguity (examined)
Considered C but the headline sits on a reserved clean zone, isolable -> B2.
"""

RATIONALE_B1_REUSE = """
## ① Form
form: B1 — surface in-scene.

## ② Per-block breakdown
- Statement text · AI-integrated · reuse the existing blank in-scene surface; place the text on the surface.

## ③ Pipeline
edit_mode: clean+reserve (preserve surface). when_ai_runs: every post. extraction: clean the ref surface, reserve it, AI renders the text onto it.

## ④ Ambiguity (examined)
Considered regenerating the scene but the ref already has a blank surface -> reuse it.
"""

# Same B1 reuse intent, but the pipeline wrongly says total-recompose (the r02 miss).
RATIONALE_B1_TOTAL_RECOMPOSE = """
## ① Form
form: B1 — surface in-scene.

## ② Per-block breakdown
- Statement text · AI-integrated · reuse the existing blank in-scene surface; place the text on the surface.

## ③ Pipeline
edit_mode: total-recompose. when_ai_runs: every post. extraction: AI regenerates the wall and renders the text.

## ④ Ambiguity (examined)
Considered reusing vs regenerating the surface.
"""

# A C rationale whose isolable CTA/byline are WRONGLY declared AI-integrated (the r07 fold).
RATIONALE_R07_BAKED_ISOLABLE = """
## ① Form
form: C — integrated-text.

## ② Per-block breakdown
- Display word "BUILD" · AI-integrated · occluded behind the creator, HTML can't occlude.
- Name label "SIMON" · AI-integrated · baked into the scene under the face.
- CTA badge "FOLLOW" · AI-integrated · rendered into the image corner.

## ③ Pipeline
edit_mode: total-recompose. when_ai_runs: every post. extraction: AI generates face + all type.

## ④ Ambiguity (examined)
Considered HTML for the CTA but kept it in the image.
"""

# Headline declared AI-integrated, but the prompt_delta forbids ALL text (the r01 contradiction).
HTML_PROMPT_CONTRADICTS = """
<!--
[ai-image-zone:1]
generation_route: edit-from-ref
ref_input: assets/ref-canonical.png
prompt_delta: |
  Same style and mood as the reference. Compose a new scene with the subject.
  No text, no lettering, no captions. Portrait 4:5.
variables:
  - name: subject
[/ai-image-zone]
-->
<div data-slot="CAPTION" class="caption">{{{CAPTION}}}</div>
"""

# Headline AI-integrated, and the prompt_delta DESCRIBES the integrated text (correct).
HTML_PROMPT_DESCRIBES_AI_TEXT = """
<!--
[ai-image-zone:1]
generation_route: edit-from-ref
ref_input: assets/ref-canonical.png
prompt_delta: |
  Same style and mood as the reference. Render the headline integrated behind the subject,
  partially occluded. No logos. Portrait 4:5.
variables:
  - name: subject
[/ai-image-zone]
-->
<div data-slot="CAPTION" class="caption">{{{CAPTION}}}</div>
"""

# A B2 prompt reserving the upper 45% for text.
HTML_RESERVED_45 = """
<!--
[ai-image-zone:1]
generation_route: edit-from-ref
prompt_delta: |
  Keep the upper 45% a calm, low-detail bright band with room for a headline; keep the
  subject and busy detail out of that band. Portrait 4:5.
[/ai-image-zone]
-->
<div data-slot="HEADLINE" class="headline">{{{HEADLINE}}}</div>
"""

HTML_WITH_AI_ZONE = """
<!-- [ai-image-zone:1] route: edit-from-ref -->
<div data-slot="CAPTION" class="caption">{{{CAPTION}}}</div>
<img data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}">
<div data-slot="BRAND_LOGO" class="logo"></div>
"""

HTML_FLAT_NO_AI_ZONE = """
<div data-slot="HEADLINE" class="headline">{{{HEADLINE}}}</div>
<div data-slot="CAPTION" class="caption">{{{CAPTION}}}</div>
"""


class TestClassify(unittest.TestCase):
    def test_ai(self):
        self.assertEqual(classify_treatment("AI / integrated"), AI_INTEGRATED)
        self.assertEqual(classify_treatment("AI-integrated (occluded)"), AI_INTEGRATED)

    def test_html(self):
        self.assertEqual(classify_treatment("HTML overlay"), HTML_OVERLAY)
        self.assertEqual(classify_treatment("HTML overlay (pill)"), HTML_OVERLAY)

    def test_chrome_wins_over_ai(self):
        # "embedded icon / chrome" must not be read as AI
        self.assertEqual(classify_treatment("embedded icon / chrome"), ICON_CHROME)


class TestParseForm(unittest.TestCase):
    def test_c(self):
        self.assertEqual(parse_form(RATIONALE_C), "C")

    def test_b1(self):
        self.assertEqual(parse_form(RATIONALE_B1_REUSE), "B1")

    def test_b2(self):
        self.assertEqual(parse_form(RATIONALE_B2_FILLED), "B2")


class TestParseBlocks(unittest.TestCase):
    def test_c_categories(self):
        blocks = parse_block_treatments(RATIONALE_C)
        cats = [b["category"] for b in blocks]
        self.assertIn(AI_INTEGRATED, cats)
        self.assertIn(HTML_OVERLAY, cats)
        self.assertIn(ICON_CHROME, cats)


class TestHtmlParse(unittest.TestCase):
    def test_text_slots_exclude_image_and_logo(self):
        slots = parse_html_text_slots(HTML_WITH_AI_ZONE)
        self.assertIn("CAPTION", slots)
        self.assertNotIn("PHOTO_MAIN", slots)
        self.assertNotIn("BRAND_LOGO", slots)

    def test_ai_zone_detected(self):
        self.assertTrue(has_ai_image_zone(HTML_WITH_AI_ZONE))
        self.assertFalse(has_ai_image_zone(HTML_FLAT_NO_AI_ZONE))


class TestDeclares(unittest.TestCase):
    def test_filled_raster(self):
        self.assertTrue(declares_filled_raster(RATIONALE_B2_FILLED))
        self.assertFalse(declares_filled_raster(RATIONALE_B1_REUSE))

    def test_surface_reuse(self):
        self.assertTrue(declares_surface_reuse(RATIONALE_B1_REUSE))
        self.assertFalse(declares_surface_reuse(RATIONALE_C))


class TestEvaluate(unittest.TestCase):
    def test_ai_integrated_but_flat_html_box_flagged(self):
        # C rationale declares AI-integrated headline, but output is flat HTML, no AI zone.
        res = evaluate(RATIONALE_C, HTML_FLAT_NO_AI_ZONE, empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("no [ai-image-zone]" in f or "flat HTML box" in f for f in res["flags"]))

    def test_ai_integrated_with_ai_zone_passes(self):
        res = evaluate(RATIONALE_C, HTML_WITH_AI_ZONE, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])

    def test_raster_declared_filled_but_empty_flagged(self):
        # B2 hero declared filled-every-post, but preview is near-uniform empty (grey placeholder).
        res = evaluate(RATIONALE_B2_FILLED, HTML_WITH_AI_ZONE, empty_frac=0.80)
        self.assertFalse(res["ok"])
        self.assertTrue(any("empty grey placeholder" in f for f in res["flags"]))

    def test_raster_declared_filled_and_filled_passes(self):
        res = evaluate(RATIONALE_B2_FILLED, HTML_WITH_AI_ZONE, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])

    def test_b1_surface_reuse_but_pure_html_flagged(self):
        # B1 says reuse the surface, but output is pure HTML text, no AI zone -> not reused.
        html = '<div data-slot="STATEMENT" class="headline">{{{STATEMENT}}}</div>'
        res = evaluate(RATIONALE_B1_REUSE, html, empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("surface" in f.lower() for f in res["flags"]))

    def test_b1_surface_reuse_with_ai_zone_passes(self):
        html = '<!-- [ai-image-zone:1] --> '
        res = evaluate(RATIONALE_B1_REUSE, html, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])

    def test_no_preview_skips_raster_check(self):
        # empty_frac None -> raster check skipped; B2 still passes structurally.
        res = evaluate(RATIONALE_B2_FILLED, HTML_WITH_AI_ZONE, empty_frac=None)
        self.assertTrue(res["ok"], res["reason"])

    def test_b1_reuse_corrected_edit_mode_passes(self):
        # B1 reuse with clean+reserve (not total-recompose) + an AI zone -> passes.
        html = '<!-- [ai-image-zone:1] --> '
        res = evaluate(RATIONALE_B1_REUSE, html, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])


class TestNewParsers(unittest.TestCase):
    def test_parse_prompt_delta(self):
        pd = parse_prompt_delta(HTML_PROMPT_CONTRADICTS)
        self.assertIn("no text", pd.lower())
        self.assertNotIn("variables", pd.lower())  # stops before the variables: key

    def test_parse_edit_mode(self):
        self.assertIn("total-recompose", parse_pipeline_edit_mode(RATIONALE_B1_TOTAL_RECOMPOSE))
        self.assertIn("clean+reserve", parse_pipeline_edit_mode(RATIONALE_B1_REUSE))

    def test_parse_reserved_band(self):
        self.assertAlmostEqual(parse_reserved_band_pct("keep the upper 45% calm"), 0.45)
        self.assertAlmostEqual(parse_reserved_band_pct("reserve the top third"), 1 / 3)
        self.assertIsNone(parse_reserved_band_pct("no band mentioned"))

    def test_html_text_bottom_extent(self):
        meas = {"elements": [
            {"bbox_pct": [4, 10, 90, 20]},   # bottom 30%
            {"bbox_pct": [4, 50, 90, 25]},   # bottom 75%
        ]}
        self.assertAlmostEqual(html_text_bottom_extent(meas), 0.75)
        self.assertIsNone(html_text_bottom_extent({"elements": []}))


class TestDeepenedChecks(unittest.TestCase):
    def test_check4_prompt_contradicts_ai_text_flagged(self):
        # C declares AI-integrated headline; prompt_delta forbids ALL text (r01).
        res = evaluate(RATIONALE_C, HTML_PROMPT_CONTRADICTS, empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("contradiction" in f or "no-text" in f for f in res["flags"]))

    def test_check4_prompt_describes_ai_text_passes(self):
        # Same C rationale, but the prompt DESCRIBES the integrated text (no blanket no-text).
        res = evaluate(RATIONALE_C, HTML_PROMPT_DESCRIBES_AI_TEXT, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])

    def test_check5_b1_total_recompose_flagged(self):
        res = evaluate(RATIONALE_B1_TOTAL_RECOMPOSE, '<!-- [ai-image-zone:1] -->', empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("total-recompose" in f for f in res["flags"]))

    def test_check6_baked_isolable_text_flagged(self):
        # CTA badge + name label declared AI-integrated -> baked isolable text (r07).
        res = evaluate(RATIONALE_R07_BAKED_ISOLABLE, '<!-- [ai-image-zone:1] -->', empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("isolable text" in f for f in res["flags"]))

    def test_check7_reserved_zone_geometry_flagged(self):
        # Prompt reserves upper 45%, but HTML text occupies down to 80% -> collision (r03).
        meas = {"elements": [{"bbox_pct": [4, 8, 90, 6]}, {"bbox_pct": [4, 60, 90, 20]}]}
        res = evaluate(RATIONALE_B2_FILLED, HTML_RESERVED_45, empty_frac=0.30, measurements=meas)
        self.assertFalse(res["ok"])
        self.assertTrue(any("reserved-zone geometry" in f for f in res["flags"]))

    def test_check7_reserved_zone_geometry_ok_within_band(self):
        # HTML text stays within the reserved 45% (+tolerance) -> no geometry flag.
        meas = {"elements": [{"bbox_pct": [4, 8, 90, 6]}, {"bbox_pct": [4, 30, 90, 18]}]}
        res = evaluate(RATIONALE_B2_FILLED, HTML_RESERVED_45, empty_frac=0.30, measurements=meas)
        self.assertTrue(res["ok"], res["reason"])

    def test_check7_skipped_without_measurements(self):
        res = evaluate(RATIONALE_B2_FILLED, HTML_RESERVED_45, empty_frac=0.30, measurements=None)
        self.assertTrue(res["ok"], res["reason"])


# --- SPEC-L1 fixtures (run-02 photographic-path fidelity: INVENTA, REMONTA) ---------------

# A B2 rationale whose photo block declares legibility by NATURAL composition (no band) —
# the correct read for numbered-fullbleed (ref-05). A scrim div must NOT be authored.
RATIONALE_B2_NATURAL = """
## ① Form
form: B2 — filled texture/landscape.

## ② Per-block breakdown
- Headline · HTML-isolable-overlay · floats on the reserved top sky band, isolable.
- Landscape photo (hero) · HTML-isolable-overlay · containment: full-bleed ·
  legibility-method: natural-composition · the ref reserves the calm TOP sky for the text; no
  band exists, the calm zone is generated in the scene. Filled every post.

## ③ Pipeline
edit_mode: partial-subject. when_ai_runs: every post. extraction: AI keeps the top sky calm.

## ④ Ambiguity (examined)
Considered C but the headline sits on a reserved clean sky zone, isolable -> B2.
"""

# A C rationale whose image block is a CONTAINED rectangle (creator-cta should match ref-07's
# contained card) and resolves legibility naturally — no scrim.
RATIONALE_C_CONTAINED_NATURAL = """
## ① Form
form: C — integrated-text.

## ② Per-block breakdown
- Display word "CAROUSEL" · HTML-isolable-overlay · sits over the portrait, isolable.
- Portrait photo · HTML-isolable-overlay · containment: contained-rectangle ·
  legibility-method: natural-composition · the face sits in a bounded upper rectangle (ref-07
  card); no band; the lower scene is naturally calm where the body copy sits.

## ③ Pipeline
edit_mode: none. when_ai_runs: setup-only. extraction: real-photo slot, no scrim.

## ④ Ambiguity (examined)
Considered full-bleed but the ref is a contained card -> contained-rectangle.
"""

# HTML that stamps a full-width opaque bottom scrim band (the INVENTA miss).
HTML_WITH_SCRIM = """
<style>
.bottom-scrim {
  position: absolute; left: 0; right: 0; bottom: 0; height: 52%;
  background: rgba(0, 0, 0, 0.68);
}
.photo { position:absolute; inset:0; object-fit:cover; width:100%; height:100%; }
</style>
<img class="photo" data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}">
<div class="bottom-scrim"></div>
<div data-slot="HEADLINE" class="headline">{{{HEADLINE}}}</div>
"""

# HTML with the calm zone resolved naturally — NO scrim div, a contained photo card.
HTML_NATURAL_CONTAINED = """
<style>
.photo-card { position:absolute; left:8%; top:6%; width:84%; height:44%; object-fit:cover; }
</style>
<img class="photo-card" data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}">
<div data-slot="HEADLINE" class="headline">{{{HEADLINE}}}</div>
"""

# HTML with a full-bleed photo (the REMONTA miss when the ref is contained).
HTML_FULLBLEED_PHOTO = """
<style>
.photo { position:absolute; inset:0; object-fit:cover; width:100%; height:100%; }
</style>
<img class="photo" data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}">
<div data-slot="HEADLINE" class="headline">{{{HEADLINE}}}</div>
"""


class TestL1Parsers(unittest.TestCase):
    def test_detect_opaque_fullwidth_band(self):
        self.assertTrue(html_has_opaque_fullwidth_band(HTML_WITH_SCRIM))
        self.assertFalse(html_has_opaque_fullwidth_band(HTML_NATURAL_CONTAINED))

    def test_faint_tint_is_not_a_scrim(self):
        # a low-alpha full-width tint (e.g. a coral cast) is NOT an opaque legibility band
        html = '.tint { left:0; right:0; height:100%; background: rgba(208,83,68,0.18); }'
        self.assertFalse(html_has_opaque_fullwidth_band(html))

    def test_detect_full_bleed_image_zone(self):
        self.assertTrue(html_image_zone_is_full_bleed(HTML_FULLBLEED_PHOTO))
        self.assertFalse(html_image_zone_is_full_bleed(HTML_NATURAL_CONTAINED))


class TestL1Checks(unittest.TestCase):
    def test_check8_scrim_vs_ref_flagged(self):
        # natural-composition declared, but HTML authors a full-width opaque scrim (INVENTA).
        res = evaluate(RATIONALE_B2_NATURAL, HTML_WITH_SCRIM, empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("scrim-vs-ref" in f for f in res["flags"]), res["reason"])

    def test_check8_natural_composition_no_scrim_passes(self):
        # natural-composition + NO scrim div -> the corrected build passes Check 8.
        res = evaluate(RATIONALE_B2_NATURAL, HTML_NATURAL_CONTAINED, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])

    def test_check8_skipped_when_ref_band_declared(self):
        # If the rationale legitimately declared ref-band, a scrim is correct -> no Check-8 flag.
        ratio_band = RATIONALE_B2_NATURAL.replace("natural-composition", "ref-band")
        res = evaluate(ratio_band, HTML_WITH_SCRIM, empty_frac=0.30)
        self.assertTrue(all("scrim-vs-ref" not in f for f in res["flags"]), res["reason"])

    def test_check9_containment_vs_ref_flagged(self):
        # contained-rectangle declared, but the image zone is full-bleed (REMONTA, ref-07).
        res = evaluate(RATIONALE_C_CONTAINED_NATURAL, HTML_FULLBLEED_PHOTO, empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("containment-vs-ref" in f for f in res["flags"]), res["reason"])

    def test_check9_contained_build_passes(self):
        # contained-rectangle declared + a bounded (contained) image zone -> passes Check 9.
        res = evaluate(RATIONALE_C_CONTAINED_NATURAL, HTML_NATURAL_CONTAINED, empty_frac=0.30)
        self.assertTrue(res["ok"], res["reason"])

    def test_check9_skipped_when_full_bleed_declared(self):
        # A full-bleed ref built full-bleed is correct -> no containment flag.
        res = evaluate(RATIONALE_B2_NATURAL, HTML_FULLBLEED_PHOTO, empty_frac=0.30)
        self.assertTrue(all("containment-vs-ref" not in f for f in res["flags"]), res["reason"])


# --- SPEC-r3 fixtures (per-element ref-vs-output comparator, Check 10) --------------------

# A cover-hook-shaped rationale: a coral graphic device, a dominant display word woven into a
# coral scene, a coral starburst BADGE the ref shows, and a coral caption PILL.
RATIONALE_COVER_HOOK = """
## ① Form
form: c-integrated-text

## ② Per-block breakdown
**Full-scene image zone** · AI-integrated · the coral-orange field is the entire scene.
  - `distinctive_graphics: "radial line-burst sunburst on the warm coral field"`
**HEADLINE / display word** ("system") · AI-integrated · the large display word is woven into
  the coral scene, dominant, occluded by the figures.
**STARBURST badge** ("Claude") · AI-integrated · small coral starburst seal between the figures.
**CAPTION PILL** · HTML-isolable-overlay · bottom coral callout pill.

## ③ Pipeline
edit_mode: total-recompose
"""

# A body-numbered-shaped rationale whose CORAL CALLOUT PILL is declared SMALL + lower-left in
# the ref (the corrected, ref-anchored read of ref-04). Paired with a full-width pill build it
# must FIRE the inflated-device check.
RATIONALE_BODY_NUMBERED = """
## ① Form
form: b2

## ② Per-block breakdown
Numbered circle badge · HTML-isolable-overlay · small coral chip top-left.
Coral callout pill · HTML-isolable-overlay · a small rounded coral pill, lower-left box.
Caption · HTML-isolable-overlay · thin caption text at the bottom.

## ③ Pipeline
edit_mode: partial-subject
"""

# A GREEN-accent brand's body-numbered-shaped rationale: same declarations, but the brand's
# accent devices are green — the gate must fire identically when pointed at --accent #22aa44.
RATIONALE_GREEN_BRAND = """
## ① Form
form: b2

## ② Per-block breakdown
Numbered circle badge · HTML-isolable-overlay · small accent chip top-left.
Accent callout pill · HTML-isolable-overlay · a small rounded accent pill, lower-left box.
Caption · HTML-isolable-overlay · thin caption text at the bottom.

## ③ Pipeline
edit_mode: partial-subject
"""

# HTML stub — Check 10 is region-based, the HTML only needs to be structurally clean so the
# other checks stay quiet while we exercise the accent comparator.
HTML_CLEAN = '<!-- [ai-image-zone:1] --> <div data-slot="CAPTION">{{{CAPTION}}}</div>'


class TestAccentMask(unittest.TestCase):
    def test_coral_pixels_detected_with_default_accent(self):
        arr = np.array(_synth(boxes=[(0.4, 0.4, 0.6, 0.6, CORAL)]))
        self.assertTrue(accent_mask(arr).any())

    def test_grey_is_not_accent(self):
        arr = np.array(_synth(bg=GREY))
        self.assertFalse(accent_mask(arr).any())

    # --- brand-agnosticism: the classifier follows the RESOLVED accent, not a hardcoded hue ---
    def test_green_accent_detected(self):
        arr = np.array(_synth(boxes=[(0.4, 0.4, 0.6, 0.6, GREEN)]))
        self.assertTrue(accent_mask(arr, GREEN_ACCENT).any())

    def test_green_invisible_under_default_coral_accent(self):
        # the pre-fix blindness, now explicit + intentional: a green device is NOT the coral
        # brand's accent — it only reads as a device when the accent says green.
        arr = np.array(_synth(boxes=[(0.4, 0.4, 0.6, 0.6, GREEN)]))
        self.assertFalse(accent_mask(arr).any())

    def test_coral_invisible_under_green_accent(self):
        arr = np.array(_synth(boxes=[(0.4, 0.4, 0.6, 0.6, CORAL)]))
        self.assertFalse(accent_mask(arr, GREEN_ACCENT).any())


class TestAccentRegions(unittest.TestCase):
    def test_field_vs_device_split(self):
        # a big coral field (top 50%) + a small coral device lower-center.
        img = _synth(boxes=[(0.0, 0.0, 1.0, 0.5, CORAL), (0.45, 0.7, 0.55, 0.78, CORAL)])
        r = detect_accent_regions(img)
        self.assertIsNotNone(r["field"])              # the big field is recognised as field
        self.assertGreaterEqual(len(r["devices"]), 1)  # the small box is a device, not field

    def test_no_coral_degrades(self):
        r = detect_accent_regions(_synth(bg=GREY))
        self.assertIsNone(r["field"])
        self.assertEqual(r["devices"], [])
        self.assertFalse(r["any_accent"])

    def test_quadrant_and_band(self):
        self.assertEqual(quadrant(0.1, 0.1), "top-left")
        self.assertEqual(quadrant(0.5, 0.9), "bottom-center")
        self.assertEqual(size_band(0.005), "small")
        self.assertEqual(size_band(0.05), "mid")
        self.assertEqual(size_band(0.30), "dominant")


class TestParseDistinctiveElements(unittest.TestCase):
    def test_cover_hook_elements(self):
        els = parse_distinctive_elements(RATIONALE_COVER_HOOK)
        kinds = {e["kind"] for e in els}
        self.assertIn("badge", kinds)
        self.assertIn("display", kinds)
        self.assertIn("graphic", kinds)
        self.assertIn("pill", kinds)

    def test_image_zone_line_not_mistyped_as_pill(self):
        # the image-zone line mentions a sibling "pill" in its prose — must not be typed pill.
        els = parse_distinctive_elements(RATIONALE_COVER_HOOK)
        names = [e["name"] for e in els if e["kind"] == "pill"]
        self.assertTrue(all("image zone" not in n.lower() for n in names))

    def test_absent_in_ref_marked(self):
        rat = RATIONALE_BODY_NUMBERED.replace(
            "lower-left box.", "lower-left box (present in ref-05, absent in ref-04).")
        pills = [e for e in parse_distinctive_elements(rat) if e["kind"] == "pill"]
        self.assertTrue(pills and pills[0]["present_in_ref"] is False)


class TestCheck10DroppedBadge(unittest.TestCase):
    def _ref(self):
        # ref: coral field (top 45%) + a coral BADGE mid-center (the "Claude" seal), with a
        # clear DARK gap between them so the seal is its own connected component (a device).
        return detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.45, CORAL),
                                                  (0.44, 0.58, 0.56, 0.68, CORAL)]))

    def test_dropped_badge_flagged(self):
        # built output: the field stays but the badge device is GONE.
        out = detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.45, CORAL)]))
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref())
        self.assertFalse(res["ok"])
        self.assertTrue(any("dropped device" in f or "relocated device" in f
                            for f in res["flags"]), res["reason"])

    def test_dropped_seal_names_dropped_not_relocated(self):
        # Reviewer item 3: when the seal truly VANISHED (no comparable coral device anywhere
        # else in the output, only the background field remains), the gate must name a DROPPED
        # device — not conflate it with a RELOCATED one. The badge has no relocated twin, so the
        # similar-size-elsewhere probe finds nothing → dropped, specifically.
        out = detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.45, CORAL)]))
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref())
        self.assertTrue(any("dropped device" in f for f in res["flags"]), res["reason"])
        self.assertTrue(all("relocated device" not in f for f in res["flags"]), res["reason"])

    def test_relocated_seal_names_relocated_not_dropped(self):
        # Contrast: the seal still EXISTS (a comparable small coral device) but moved to a
        # different corner → relocated, NOT dropped. This is the distinction the geometry-only
        # ref[0]-vs-out[0] compare could not make.
        out = detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.45, CORAL),
                                                 (0.04, 0.86, 0.16, 0.96, CORAL)]))
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref())
        self.assertTrue(any("relocated device" in f for f in res["flags"]), res["reason"])
        self.assertTrue(all("dropped device" not in f for f in res["flags"]), res["reason"])

    def test_badge_present_passes(self):
        # built output reproduces the badge in the same region → no dropped/relocated flag.
        out = detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.45, CORAL),
                                                (0.44, 0.58, 0.56, 0.68, CORAL)]))
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref())
        self.assertTrue(all("dropped device" not in f and "relocated device" not in f
                            for f in res["flags"]), res["reason"])


class TestCheck10InflatedPill(unittest.TestCase):
    def _ref_small_pill(self):
        # ref: a SMALL coral pill lower-left, no background field (the body-numbered ref-04 box).
        return detect_accent_regions(_synth(boxes=[(0.08, 0.80, 0.30, 0.88, CORAL)]))

    def test_inflated_pill_flagged(self):
        # built output: the pill is INFLATED to a near-full-width dominant coral strip.
        out = detect_accent_regions(_synth(boxes=[(0.05, 0.72, 0.95, 0.86, CORAL)]))
        res = evaluate(RATIONALE_BODY_NUMBERED, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_small_pill())
        self.assertFalse(res["ok"])
        self.assertTrue(any("inflated device" in f for f in res["flags"]), res["reason"])

    def test_matching_small_pill_passes(self):
        # built output keeps the pill small + lower-left → no inflation flag.
        out = detect_accent_regions(_synth(boxes=[(0.08, 0.80, 0.30, 0.88, CORAL)]))
        res = evaluate(RATIONALE_BODY_NUMBERED, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_small_pill())
        self.assertTrue(all("inflated device" not in f for f in res["flags"]), res["reason"])

    def test_relocated_pill_flagged(self):
        # same size band but moved from lower-left to top-right → relocated.
        out = detect_accent_regions(_synth(boxes=[(0.70, 0.05, 0.92, 0.13, CORAL)]))
        res = evaluate(RATIONALE_BODY_NUMBERED, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_small_pill())
        self.assertFalse(res["ok"])
        self.assertTrue(any("relocated device" in f for f in res["flags"]), res["reason"])


class TestCheck10GhostDisplay(unittest.TestCase):
    def _ref_dominant(self):
        # ref: a dominant coral scene (field) the display word is woven into.
        return detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.6, CORAL)]))

    def test_ghost_display_flagged(self):
        # built output: NO dominant coral region (the display ghosted to a tiny sliver).
        out = detect_accent_regions(_synth(boxes=[(0.48, 0.96, 0.52, 0.99, CORAL)]))
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_dominant())
        self.assertFalse(res["ok"])
        self.assertTrue(any("ghost display" in f for f in res["flags"]), res["reason"])

    def test_dominant_display_passes(self):
        # built output keeps a dominant coral region → no ghost flag.
        out = detect_accent_regions(_synth(boxes=[(0.0, 0.0, 1.0, 0.6, CORAL)]))
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_dominant())
        self.assertTrue(all("ghost display" not in f for f in res["flags"]), res["reason"])


class TestCheck10Skip(unittest.TestCase):
    def test_no_regions_skips_check10(self):
        # No out/ref regions supplied (no preview) → Check 10 is skipped, build passes.
        res = evaluate(RATIONALE_COVER_HOOK, HTML_CLEAN, empty_frac=0.30)
        self.assertTrue(all("device" not in f and "ghost display" not in f
                            for f in res["flags"]), res["reason"])

    def test_ref_anchored_subchecks_degrade_when_ref_has_no_coral(self):
        # A washed-out ref with NO coral → the REF-ANCHORED sub-checks (dropped / relocated /
        # ref-vs-out inflated) cannot run (nothing to compare against). With an output whose
        # pill stays SMALL + contained (no inflation), nothing should fire — graceful degrade,
        # no false positive from the missing ref coral.
        out = detect_accent_regions(_synth(boxes=[(0.08, 0.80, 0.30, 0.88, CORAL)]))
        ref = detect_accent_regions(_synth(bg=GREY))  # no coral recoverable
        res = evaluate(RATIONALE_BODY_NUMBERED, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=ref)
        self.assertTrue(all("device" not in f and "ghost display" not in f
                            and "inflated pill" not in f for f in res["flags"]), res["reason"])

    def test_ref_without_coral_still_catches_inflated_pill_off_output(self):
        # The TARGETED reviewer case (items 1+2): the REAL body-numbered ref-canonical carries
        # zero coral (any_coral=False), so the ref-anchored inflated path can never reach the
        # full-width pill. The ref-INDEPENDENT path must still name it off the OUTPUT alone.
        out = detect_accent_regions(_synth(boxes=[(0.05, 0.72, 0.95, 0.86, CORAL)]))
        ref = detect_accent_regions(_synth(bg=GREY))  # no coral recoverable (washed-out re-encode)
        self.assertFalse(ref["any_accent"])           # precondition: the ref truly has no coral
        res = evaluate(RATIONALE_BODY_NUMBERED, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=ref)
        self.assertFalse(res["ok"])
        self.assertTrue(any("inflated pill" in f for f in res["flags"]), res["reason"])

    def test_inflated_pill_fires_even_when_pill_absent_in_canonical_ref(self):
        # Reviewer item 2: a pill marked 'absent in ref-04' (present_in_ref=False) is EXCLUDED
        # from the ref-anchored compare, but an over-authored full-width pill must STILL flag —
        # the inflated-pill path is independent of present_in_ref.
        rat = RATIONALE_BODY_NUMBERED.replace(
            "lower-left box.", "lower-left box (present in ref-05, absent in ref-04).")
        pills = [e for e in parse_distinctive_elements(rat) if e["kind"] == "pill"]
        self.assertTrue(pills and pills[0]["present_in_ref"] is False)  # precondition
        out = detect_accent_regions(_synth(boxes=[(0.05, 0.72, 0.95, 0.86, CORAL)]))
        ref = detect_accent_regions(_synth(bg=GREY))
        res = evaluate(rat, HTML_CLEAN, empty_frac=0.30, out_regions=out, ref_regions=ref)
        self.assertTrue(any("inflated pill" in f for f in res["flags"]), res["reason"])


class TestCheck10GreenBrand(unittest.TestCase):
    """Brand-agnosticism (the owner-flagged blindness): the SAME Check 10 comparator must fire
    for a GREEN-accent brand when the detector is pointed at the brand's accent (the CLI's
    --accent \"#22aa44\" / tokens.json colors.accent) — and is provably blind without it."""

    def _ref_small_green_pill(self):
        # ref: a SMALL green pill lower-left (the green brand's body-numbered box).
        return detect_accent_regions(_synth(boxes=[(0.08, 0.80, 0.30, 0.88, GREEN)]),
                                     accent_hex=GREEN_ACCENT)

    def test_dropped_green_pill_flagged(self):
        # built output: the green pill is GONE → dropped device, exactly like the coral brand.
        out = detect_accent_regions(_synth(bg=DARK), accent_hex=GREEN_ACCENT)
        res = evaluate(RATIONALE_GREEN_BRAND, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_small_green_pill())
        self.assertFalse(res["ok"])
        self.assertTrue(any("dropped device" in f for f in res["flags"]), res["reason"])

    def test_inflated_green_pill_flagged(self):
        # built output: the small green pill blown to a near-full-width dominant green strip.
        out = detect_accent_regions(_synth(boxes=[(0.05, 0.72, 0.95, 0.86, GREEN)]),
                                    accent_hex=GREEN_ACCENT)
        res = evaluate(RATIONALE_GREEN_BRAND, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_small_green_pill())
        self.assertFalse(res["ok"])
        self.assertTrue(any("inflated device" in f for f in res["flags"]), res["reason"])

    def test_matching_green_pill_passes(self):
        out = detect_accent_regions(_synth(boxes=[(0.08, 0.80, 0.30, 0.88, GREEN)]),
                                    accent_hex=GREEN_ACCENT)
        res = evaluate(RATIONALE_GREEN_BRAND, HTML_CLEAN, empty_frac=0.30,
                       out_regions=out, ref_regions=self._ref_small_green_pill())
        self.assertTrue(all("device" not in f and "inflated pill" not in f
                            for f in res["flags"]), res["reason"])

    def test_green_brand_is_blind_under_default_coral_accent(self):
        # The exact pre-fix failure mode, pinned: detecting with the DEFAULT (coral) accent on
        # a green-brand ref recovers NO accent regions — the dropped pill would sail through.
        # This is why the accent MUST be resolved per brand (tokens.json / --accent).
        ref = detect_accent_regions(_synth(boxes=[(0.08, 0.80, 0.30, 0.88, GREEN)]))
        self.assertFalse(ref["any_accent"])


class TestResolveAccent(unittest.TestCase):
    """The accent resolution chain: --accent > brand_context tokens.json (walked up from the
    template/rationale path) > coral default with a stderr WARN."""

    def _tokens_tree(self, root: Path, accent: str = "#0055ff") -> Path:
        vi = root / "brand_context" / "visual-identity"
        vi.mkdir(parents=True)
        (vi / "tokens.json").write_text(
            json.dumps({"colors": {"accent": accent, "primary": "#1f1816"}}),
            encoding="utf-8")
        tpl = root / "brand_context" / "templates" / "family" / "template.html"
        tpl.parent.mkdir(parents=True)
        tpl.write_text("<html></html>", encoding="utf-8")
        return tpl

    def test_cli_accent_wins_over_tokens(self):
        with tempfile.TemporaryDirectory() as td:
            tpl = self._tokens_tree(Path(td))
            self.assertEqual(resolve_accent(GREEN_ACCENT, tpl), (GREEN_ACCENT, "--accent"))

    def test_tokens_autodiscovered_walking_up(self):
        with tempfile.TemporaryDirectory() as td:
            tpl = self._tokens_tree(Path(td))
            accent, source = resolve_accent(None, tpl)
            self.assertEqual(accent, "#0055ff")
            self.assertTrue(source.endswith("tokens.json"), source)

    def test_fallback_is_coral_with_warn(self):
        with tempfile.TemporaryDirectory() as td:
            orphan = Path(td) / "nowhere" / "template.html"
            buf = io.StringIO()
            with contextlib.redirect_stderr(buf):
                accent, source = resolve_accent(None, orphan)
            self.assertEqual((accent, source), (DEFAULT_ACCENT_HEX, "default"))
            self.assertIn("WARN", buf.getvalue())
            self.assertIn("--accent", buf.getvalue())

    def test_invalid_cli_accent_raises(self):
        with self.assertRaises(ValueError):
            resolve_accent("not-a-color", Path("x/template.html"))


# --- SPEC-r5g fixtures (run-06: Check 9b containment-vs-ref-pixels, Check 11 undeclared) ---

CREAM = (238, 233, 222)


def _fullbleed_scene_img(width=400, height=500):
    """A full-bleed water-like scene: a strong vertical luminance gradient reaching every
    edge (the run-06 numbered-photo-callout ref shape — teal water, dark floor, light top)."""
    grad = np.linspace(40, 225, height).astype(np.uint8)
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    arr[:, :, 0] = grad[:, None] // 2          # teal-ish: low red
    arr[:, :, 1] = grad[:, None]
    arr[:, :, 2] = grad[:, None]
    return Image.fromarray(arr)


def _textured_edges_img(width=400, height=500, seed=7):
    """Scene texture continuing to the side edges (coarse busy texture everywhere,
    tone-matched top-vs-bottom): trips the side-strip MAD bound, not the top/bottom tone
    bound. The texture is COARSE (generated small, upscaled nearest) so it survives the
    detector's downscale the way real scene structure does — fine pixel noise averages out."""
    rng = np.random.default_rng(seed)
    coarse = rng.integers(20, 235, size=(height // 12, width // 12, 3), dtype=np.uint8)
    return Image.fromarray(coarse).resize((width, height), Image.NEAREST)


def _contained_on_mat_img(width=400, height=500):
    """A GENUINE contained ref: a dark photo rectangle centered on a near-uniform cream mat,
    with sparse masthead-like text marks near the top edge (chrome legitimately sits in the
    top strip on a real mat — the index-card-cover shape)."""
    img = Image.new("RGB", (width, height), CREAM)
    arr = np.array(img)
    # the contained photo (bounded, clear margins on all sides)
    arr[int(0.30 * height):int(0.75 * height), int(0.15 * width):int(0.85 * width)] = DARK
    # sparse masthead text marks inside the top strip
    arr[int(0.01 * height):int(0.03 * height), int(0.30 * width):int(0.45 * width)] = DARK
    # a thin footer wordmark inside the bottom strip
    arr[int(0.97 * height):int(0.985 * height), int(0.40 * width):int(0.60 * width)] = DARK
    return Image.fromarray(arr)


class TestRefBorderStats(unittest.TestCase):
    def test_fullbleed_gradient_is_misread(self):
        # The run-06 shape: scene gradient reaches every edge -> contained is a misread.
        stats = ref_border_stats(_fullbleed_scene_img())
        reason = containment_misread(stats)
        self.assertIsNotNone(reason)
        self.assertIn("top-vs-bottom", reason)

    def test_textured_side_strips_are_misread(self):
        # Tone-matched top/bottom but busy texture at the side edges -> still a misread.
        stats = ref_border_stats(_textured_edges_img())
        reason = containment_misread(stats)
        self.assertIsNotNone(reason)
        self.assertIn("scene texture", reason)

    def test_genuine_contained_mat_passes(self):
        # Near-uniform mat + sparse chrome text in the top/bottom strips -> NOT a misread.
        stats = ref_border_stats(_contained_on_mat_img())
        self.assertIsNone(containment_misread(stats), stats)


class TestCheck9bContainmentVsRefPixels(unittest.TestCase):
    def test_hallucinated_contained_read_flagged(self):
        # rationale declares contained-rectangle, the HTML is consistent with it (so Check 9
        # passes), but the REF PIXELS are full-bleed -> 9b must catch the misread.
        border = ref_border_stats(_fullbleed_scene_img())
        res = evaluate(RATIONALE_C_CONTAINED_NATURAL, HTML_NATURAL_CONTAINED,
                       empty_frac=0.30, ref_border=border)
        self.assertFalse(res["ok"])
        self.assertTrue(any("containment-misread" in f for f in res["flags"]), res["reason"])
        self.assertTrue(any("misread" in f and "full-bleed" in f.lower()
                            for f in res["flags"]), res["reason"])

    def test_genuine_contained_ref_passes(self):
        border = ref_border_stats(_contained_on_mat_img())
        res = evaluate(RATIONALE_C_CONTAINED_NATURAL, HTML_NATURAL_CONTAINED,
                       empty_frac=0.30, ref_border=border)
        self.assertTrue(all("containment-misread" not in f for f in res["flags"]),
                        res["reason"])

    def test_skipped_when_fullbleed_declared(self):
        # a full-bleed declaration makes 9b moot even on a full-bleed ref.
        border = ref_border_stats(_fullbleed_scene_img())
        res = evaluate(RATIONALE_B2_NATURAL, HTML_FULLBLEED_PHOTO,
                       empty_frac=0.30, ref_border=border)
        self.assertTrue(all("containment-misread" not in f for f in res["flags"]),
                        res["reason"])

    def test_skipped_without_ref(self):
        # no ref supplied (ref_border=None) -> 9b skips; Check 9 self-consistency remains.
        res = evaluate(RATIONALE_C_CONTAINED_NATURAL, HTML_NATURAL_CONTAINED,
                       empty_frac=0.30, ref_border=None)
        self.assertTrue(all("containment-misread" not in f for f in res["flags"]),
                        res["reason"])


# A monitor-surface-shaped rationale: §2 declares the screen surface blocks + masthead chrome,
# but NO decorative word. The prose even contains the bare word "word" ("ONE key word in the
# headline") — the generic-token trap that must NOT count as declaring DECORATIVE_WORD.
RATIONALE_MONITOR_SHAPED = """
## ① Form
form: B1 — surface in-scene.

## ② Per-block breakdown
- Screen headline · AI-integrated · on the CRT screen surface; serif-italic accent for ONE key word in the headline.
- Sticky note satellites · AI-integrated · satellite surfaces, AI-placed.
- Masthead · HTML chrome · top edge, tokens.json chrome.

## ③ Pipeline
edit_mode: edit-from-ref (surface-preserving).
"""

# The shipped HTML carries a visible DECORATIVE_WORD div the rationale never declared (the
# run-06 ghost "system", injected to appease the font gate) + declared/chrome slots.
HTML_WITH_GHOST_WORD = """
<!-- [ai-image-zone:1] route: edit-from-ref -->
<div data-slot="MASTHEAD" class="masthead"></div>
<div data-slot="MASTHEAD_LEFT">{{MASTHEAD_LEFT}}</div>
<div class="decorative-word zone" data-slot="DECORATIVE_WORD">{{DECORATIVE_WORD}}</div>
"""

HTML_ALL_DECLARED = """
<!-- [ai-image-zone:1] route: edit-from-ref -->
<div data-slot="MASTHEAD" class="masthead"></div>
<div data-slot="SCREEN_HEADLINE">{{{SCREEN_HEADLINE}}}</div>
"""


class TestFindUndeclaredSlots(unittest.TestCase):
    def test_ghost_word_is_undeclared(self):
        und = find_undeclared_slots(RATIONALE_MONITOR_SHAPED, HTML_WITH_GHOST_WORD)
        self.assertEqual(und, ["DECORATIVE_WORD"])

    def test_generic_token_does_not_declare(self):
        # §2 contains the bare word "word" ("ONE key word") — that must NOT declare
        # DECORATIVE_WORD (generic tokens only declare via the full phrase).
        self.assertIn("word", RATIONALE_MONITOR_SHAPED.lower())  # the trap is present
        und = find_undeclared_slots(RATIONALE_MONITOR_SHAPED, HTML_WITH_GHOST_WORD)
        self.assertIn("DECORATIVE_WORD", und)

    def test_full_phrase_declares(self):
        rat = RATIONALE_MONITOR_SHAPED.replace(
            "- Masthead", "- Decorative word · HTML overlay · oversized bottom-edge word.\n- Masthead")
        self.assertEqual(find_undeclared_slots(rat, HTML_WITH_GHOST_WORD), [])

    def test_chrome_slots_excluded(self):
        und = find_undeclared_slots(RATIONALE_MONITOR_SHAPED, HTML_ALL_DECLARED)
        self.assertEqual(und, [])  # masthead chrome skipped, screen headline declared

    def test_synonym_display_word_declares_headline_slot(self):
        # a HEADLINE slot is declared by a §2 "Display word" block (design language ≠ slot id).
        html = '<div data-slot="HEADLINE">{{{HEADLINE}}}</div>'
        self.assertEqual(find_undeclared_slots(RATIONALE_C_CONTAINED_NATURAL, html), [])


class TestCheck11UndeclaredElement(unittest.TestCase):
    def test_ghost_word_flagged(self):
        res = evaluate(RATIONALE_MONITOR_SHAPED, HTML_WITH_GHOST_WORD, empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("undeclared visible element" in f and "DECORATIVE_WORD" in f
                            for f in res["flags"]), res["reason"])

    def test_all_declared_passes(self):
        res = evaluate(RATIONALE_MONITOR_SHAPED, HTML_ALL_DECLARED, empty_frac=0.30)
        self.assertTrue(all("undeclared visible element" not in f for f in res["flags"]),
                        res["reason"])


# === SPEC-r6g fixtures (run-07 items 8, 9, 6) =============================================

# Item 8 — the real highlight-headline-render rationale shape (chain → gears). The slug names
# `chain`; the hero is routed as the per-post AI-regenerated variation axis (the violation).
RATIONALE_FIXED_HERO_VIOLATED = """
## ① Form
form: B2 — filled subject on a clean top.

## ② Per-block breakdown
- Headline · HTML overlay · clean top paper zone, isolable.
- Chain hero (PHOTO_MAIN_PATH) · AI-integrated · the metal chain, generated by the AI image
  pipeline, the per-post variation axis. edit_mode: partial-subject (the chain is the per-post
  subject; the upper paper/headline zone is fixed).

## ③ Pipeline
edit_mode: partial-subject. when_ai_runs: every post (the 3D-rendered subject changes per post).
extraction: AI generates the hero keeping a clean top.

## ④ Ambiguity (examined)
Considered C but the headline sits on a reserved clean zone -> B2.
"""

# Item 8 — the CORRECTED read: the chain is FIXED, recolored from the ref, vary only framing.
RATIONALE_FIXED_HERO_HONORED = """
## ① Form
form: B2 — filled subject on a clean top.

## ② Per-block breakdown
- Headline · HTML overlay · clean top paper zone, isolable.
- Chain hero (PHOTO_MAIN_PATH) · AI-integrated · KEEP the subject: the ref's metal chain with
  one coral link; recolor the ref (green→coral); vary only framing/angle/lighting. Fixed-hero:
  the chain is the identity, not a per-post object.

## ③ Pipeline
edit_mode: partial-subject (recolor the ref's chain). extraction: clean recolor, no regenerate.

## ④ Ambiguity (examined)
The slug names 'chain' so the object is the identity -> recolor, never swap.
"""

# Item 9 — the real creator-cover-cta metadata.json shape (the placeholder + generic subject).
METADATA_CREATOR_PLACEHOLDER = {
    "PHOTO_MAIN_PATH": "_ai_bg/photo_main.png",
    "PHOTO_SUBJECT": "a male creator, dark hair, confident expression, arms crossed, dark clothing",
    "PHOTO_CREATOR_PATH": "(filled from brand-headshot: assets/simon-pic.jpg)",
}
# Item 9 — the CORRECTED build: the identity slot resolved to the real headshot path; subject
# names the brand person.
METADATA_CREATOR_RESOLVED = {
    "PHOTO_MAIN_PATH": "_ai_bg/photo_main.png",
    "PHOTO_SUBJECT": "Simon, the brand person, restyled to the scene medium",
    "PHOTO_CREATOR_PATH": "assets/simon-pic.jpg",
}

# A creator-cover rationale: the face is the hero, a brand headshot is in play.
RATIONALE_CREATOR_FACE_HERO = """
## ① Form
form: C — person in a scene.

## ② Per-block breakdown
- Creator face (PHOTO_CREATOR_PATH) · real-photo slot · the dominant hero face; use the brand
  headshot (simon-pic.jpg) as --input-image; the face is NEVER a baked AI face. brand-headshot.
- Display word · HTML overlay · sits over the scene, isolable.

## ③ Pipeline
edit_mode: scene-restyle-with-real-face. extraction: img2img guided by ref=style + headshot=identity.

## ④ Ambiguity (examined)
Considered inventing the face but a headshot exists -> derive from it.
"""

HTML_LOGO_INVERTED = """
<style>
.brand-logo { position:absolute; top:4%; left:4%; width:12%; filter: invert(1) brightness(0.9); }
</style>
<img class="brand-logo" data-slot="BRAND_LOGO" src="{{BRAND_LOGO_PATH}}">
"""

HTML_SEAL_AS_DISC = """
<style>
.brand-seal { position:absolute; top:40%; left:44%; width:12%; height:9.6%; border-radius:50%; }
</style>
<div class="brand-seal" data-slot="SEAL"></div>
"""

RATIONALE_SERRATED_SEAL = """
## ① Form
form: C.

## ② Per-block breakdown
- Starburst seal ("Claude") · embedded icon / chrome · a serrated sunburst starburst badge.

## ③ Pipeline
edit_mode: none.

## ④ Ambiguity (examined)
The seal is a serrated starburst, not a disc.
"""

HTML_CLEAN_LOGO = """
<style>.brand-logo { position:absolute; top:4%; left:4%; width:12%; }</style>
<img class="brand-logo" data-slot="BRAND_LOGO" src="{{BRAND_LOGO_PATH}}">
"""


class TestSlugObjectNoun(unittest.TestCase):
    def test_chain_slug_names_object(self):
        self.assertEqual(slug_object_noun("chain-highlight-headline"), "chain")
        self.assertEqual(slug_object_noun("highlight-headline-render"), None)  # no object noun

    def test_pool_role_slugs_name_nothing(self):
        for s in ("one-page-system-cover", "numbered-photo-rule", "gallery-statement-quote",
                  "creator-cover-cta", "about-callout-pills"):
            self.assertIsNone(slug_object_noun(s), s)

    def test_known_object_noun_anywhere(self):
        self.assertEqual(slug_object_noun("the-rocket-cover"), "rocket")


class TestHeroRegeneratedPerPost(unittest.TestCase):
    def test_violated_read_detected(self):
        self.assertTrue(hero_is_regenerated_per_post(RATIONALE_FIXED_HERO_VIOLATED))

    def test_honored_read_suppresses(self):
        # the keep/recolor contract is present -> NOT a per-post regenerate.
        self.assertFalse(hero_is_regenerated_per_post(RATIONALE_FIXED_HERO_HONORED))


class TestCheck12FixedHero(unittest.TestCase):
    def test_fixed_hero_mismatch_flagged(self):
        # slug names 'chain' + hero routed per-post-regenerated -> HARD FAIL (chain → gears).
        res = evaluate(RATIONALE_FIXED_HERO_VIOLATED, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       slug="chain-highlight-headline")
        self.assertFalse(res["ok"])
        self.assertTrue(any("fixed-hero mismatch" in f for f in res["flags"]), res["reason"])

    def test_fixed_hero_honored_passes(self):
        # same slug, but the rationale recolors the ref / keeps the subject -> no flag.
        res = evaluate(RATIONALE_FIXED_HERO_HONORED, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       slug="chain-highlight-headline")
        self.assertTrue(all("fixed-hero mismatch" not in f for f in res["flags"]), res["reason"])

    def test_no_object_slug_never_fires(self):
        # a pool/role slug names no object → the check can't fire even on a per-post routing
        # (a generic photo slot legitimately varies per post when it is NOT the identity).
        res = evaluate(RATIONALE_FIXED_HERO_VIOLATED, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       slug="numbered-photo-rule")
        self.assertTrue(all("fixed-hero mismatch" not in f for f in res["flags"]), res["reason"])

    def test_no_slug_skips_check12(self):
        res = evaluate(RATIONALE_FIXED_HERO_VIOLATED, HTML_WITH_AI_ZONE, empty_frac=0.30)
        self.assertTrue(all("fixed-hero mismatch" not in f for f in res["flags"]), res["reason"])


class TestPlaceholderAndFaceParsers(unittest.TestCase):
    def test_placeholder_path_detected(self):
        self.assertTrue(is_placeholder_path("(filled from brand-headshot: assets/simon-pic.jpg)"))
        self.assertTrue(is_placeholder_path(""))
        self.assertTrue(is_placeholder_path("TBD"))

    def test_resolved_path_not_placeholder(self):
        self.assertFalse(is_placeholder_path("assets/simon-pic.jpg"))
        self.assertFalse(is_placeholder_path("_slides/slide-01/photo_creator.png"))

    def test_metadata_slot_lookup(self):
        slot = metadata_slot_value(METADATA_CREATOR_PLACEHOLDER, IDENTITY_SLOT_KEY_RE)
        self.assertEqual(slot[0], "PHOTO_CREATOR_PATH")

    def test_face_is_hero(self):
        self.assertTrue(face_is_hero(RATIONALE_CREATOR_FACE_HERO))
        self.assertFalse(face_is_hero(RATIONALE_FIXED_HERO_VIOLATED))  # chain, not a face

    def test_headshot_declared(self):
        self.assertTrue(headshot_declared(RATIONALE_CREATOR_FACE_HERO, "",
                                          METADATA_CREATOR_PLACEHOLDER))


class TestCheck13SceneRestyle(unittest.TestCase):
    def test_placeholder_slot_flagged(self):
        # hero face + headshot + the identity slot is a placeholder + generic subject -> FLAG.
        res = evaluate(RATIONALE_CREATOR_FACE_HERO, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       metadata=METADATA_CREATOR_PLACEHOLDER)
        self.assertFalse(res["ok"])
        self.assertTrue(any("scene-restyle mismatch" in f for f in res["flags"]), res["reason"])
        self.assertTrue(any("placeholder" in f for f in res["flags"]), res["reason"])

    def test_generic_subject_named_in_flag(self):
        res = evaluate(RATIONALE_CREATOR_FACE_HERO, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       metadata=METADATA_CREATOR_PLACEHOLDER)
        self.assertTrue(any("generic person description" in f for f in res["flags"]), res["reason"])

    def test_resolved_headshot_passes(self):
        # the identity slot resolved to the real path + the subject names the brand person -> ok.
        res = evaluate(RATIONALE_CREATOR_FACE_HERO, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       metadata=METADATA_CREATOR_RESOLVED)
        self.assertTrue(all("scene-restyle mismatch" not in f for f in res["flags"]), res["reason"])

    def test_no_metadata_skips_check13(self):
        res = evaluate(RATIONALE_CREATOR_FACE_HERO, HTML_WITH_AI_ZONE, empty_frac=0.30)
        self.assertTrue(all("scene-restyle mismatch" not in f for f in res["flags"]), res["reason"])

    def test_no_face_hero_never_fires(self):
        # a non-face template with a placeholder slot must NOT trip the face-identity check.
        res = evaluate(RATIONALE_FIXED_HERO_VIOLATED, HTML_WITH_AI_ZONE, empty_frac=0.30,
                       metadata=METADATA_CREATOR_PLACEHOLDER)
        self.assertTrue(all("scene-restyle mismatch" not in f for f in res["flags"]), res["reason"])


class TestCheck14SealProvenance(unittest.TestCase):
    def test_inverted_logo_flagged(self):
        flags = seal_provenance_flags(HTML_LOGO_INVERTED, "## ② Per-block breakdown\n- logo")
        self.assertTrue(any("logo provenance" in f for f in flags), flags)

    def test_inverted_logo_flagged_via_evaluate(self):
        res = evaluate("## ② Per-block breakdown\n- Brand logo · chrome.", HTML_LOGO_INVERTED,
                       empty_frac=0.30)
        self.assertFalse(res["ok"])
        self.assertTrue(any("logo provenance" in f for f in res["flags"]), res["reason"])

    def test_serrated_seal_as_disc_flagged(self):
        flags = seal_provenance_flags(HTML_SEAL_AS_DISC, RATIONALE_SERRATED_SEAL)
        self.assertTrue(any("seal shape" in f for f in flags), flags)

    def test_disc_without_serrated_declaration_passes(self):
        # a border-radius:50% on a seal the rationale does NOT call serrated is fine (a real disc).
        plain = "## ② Per-block breakdown\n- Round dot badge · chrome · a simple circular dot."
        flags = seal_provenance_flags(HTML_SEAL_AS_DISC, plain)
        self.assertTrue(all("seal shape" not in f for f in flags), flags)

    def test_clean_logo_passes(self):
        flags = seal_provenance_flags(HTML_CLEAN_LOGO, "## ② Per-block breakdown\n- logo")
        self.assertEqual(flags, [])


# =============================================================================================
# Text routing (fix-text-routing): object-bound text → AI bakes the SUPPLIED text.
# (a) signboard-list-body — a multi-item LIST on the surface is OBJECT-BOUND: it routes to
#     AI-on-surface (surface-reuse), the supplied items NAMED in the prompt_delta + a negative
#     against invented/extra text. NOT HTML slots (the lane-3 routing, now reversed). Check 3
#     (surface-reuse) applies: an AI image zone must exist.
# (b) fullbleed-overlay-cover — the cover carries a NATIVE data-slot="HEADLINE" slot so the hook
#     has somewhere to render (no hand-patched .headline-zone). [separate concern — unchanged]
# =============================================================================================

# (a) The CORRECT list authoring: CONTENT = AI-on-surface, supplied items named in the prompt_delta,
# negative against invented/extra text (NOT a blanket no-text clause). An AI image zone exists.
RATIONALE_B1_LIST_AI_ON_SURFACE = """
## ① Form
form: B1 — surface in-scene.

## ② Per-block breakdown
- List items CONTENT · AI-integrated · reuse the existing surface; the AI renders the supplied items ON the billboard slats, obeying the slats' perspective/lighting. The prompt names the items verbatim; a negative forbids invented/extra text; the letter-fidelity check confirms the rendered text matches.

## ③ Pipeline
edit_mode: clean+reserve (preserve the slats, render the supplied items onto them). when_ai_runs: every post. extraction: AI bakes the supplied list onto the slats.

## ④ Ambiguity (examined)
Considered HTML slots to dodge hallucination, but that loses the slats' perspective/occlusion -> the list is object-bound, so AI bakes the supplied text + a negative against invented items.
"""

# Correct list HTML: an AI image zone whose prompt_delta NAMES the supplied items + a negative
# against invented/extra text. No HTML CONTENT_n slots — the list rides the surface.
HTML_B1_LIST_AI_ON_SURFACE = """
<!--
[ai-image-zone:1]
generation_route: edit-from-ref
ref_input: assets/ref-canonical.png
prompt_delta: |
  KEEP the ref's signboard slats (perspective, lighting, bounds) — clean the baked text off them
  and render these lines onto the slats, top to bottom: "Workflow Automation" / "Agent Frameworks"
  / "Tool Use" / "Evaluation". Render ONLY these lines, NO other words, NO invented items, NO extra
  captions. Change nothing else. Portrait 4:5.
[/ai-image-zone]
-->
"""

# (a) The BUGGY contradiction: rationale declares the list AI-on-surface / reuse-the-surface,
# but the HTML ships {{CONTENT_n}} slots and no AI zone -> Check 3 fires (the list was floated
# to flat HTML instead of baked onto the surface).
HTML_B1_LIST_FLAT_SLOTS_NO_ZONE = """
<div class="list-block">
  <div class="list-item" data-slot="CONTENT_1">{{{CONTENT_1}}}</div>
  <div class="list-item" data-slot="CONTENT_2">{{{CONTENT_2}}}</div>
  <div class="list-item" data-slot="CONTENT_3">{{{CONTENT_3}}}</div>
  <div class="list-item" data-slot="CONTENT_4">{{{CONTENT_4}}}</div>
</div>
"""

# (a) A blanket no-text clause over a surface that must carry the supplied list -> Check 4 fires
# (the model is told NOT to render the very text the rationale routed to the AI).
HTML_B1_LIST_BLANKET_NOTEXT = """
<!--
[ai-image-zone:1]
generation_route: edit-from-ref
ref_input: assets/ref-canonical.png
prompt_delta: |
  KEEP the ref's signboard slats — render the panels EMPTY, NO text, NO lettering, NO words,
  NO captions ON the panels. Change nothing else. Portrait 4:5.
[/ai-image-zone]
-->
"""

# (b) A cover that DOES carry a native HEADLINE slot over an AI scene (the fix).
RATIONALE_COVER_WITH_HEADLINE = """
## ① Form
form: C — integrated-text (full-bleed overlay cover).

## ② Per-block breakdown
- Headline (hook) · HTML overlay · decision: HTML — prominent display, native headline zone over the full-bleed scene.
- Full-bleed scene · AI-generated (hero) · edit-from-ref, filled every post.

## ③ Pipeline
edit_mode: total-recompose. when_ai_runs: every post.

## ④ Ambiguity (examined)
Headline sits clear of / above the opaque scene (Check I) -> HTML, not baked.
"""

HTML_COVER_WITH_HEADLINE = """
<!-- [ai-image-zone:1] route: edit-from-ref -->
<img data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}" style="position:absolute; inset:0; z-index:0;">
<div class="headline-zone" data-slot="HEADLINE"
     style="position:absolute; top:18%; left:8%; width:84%; z-index:10;">{{{HEADLINE}}}</div>
"""

# (b) The DEFECT: a full-bleed cover with NO headline slot — the hook has nowhere to render.
HTML_COVER_NO_HEADLINE = """
<!-- [ai-image-zone:1] route: edit-from-ref -->
<img data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}" style="position:absolute; inset:0; z-index:0;">
"""


class TestListAiOnSurface(unittest.TestCase):
    """(a) signboard-list-body — an object-bound list is AI-baked on the surface (the supplied
    items named in the prompt), NOT floated to flat HTML slots (lane-3 routing, reversed)."""

    def test_list_baked_on_surface_passes(self):
        # AI-on-surface list: an AI zone exists, the prompt names the supplied items + a negative
        # against invented/extra text. Check 3 (surface-reuse) is satisfied; Check 4 does not fire.
        res = evaluate(RATIONALE_B1_LIST_AI_ON_SURFACE, HTML_B1_LIST_AI_ON_SURFACE, empty_frac=0.30,
                       slug="signboard-list-body")
        self.assertTrue(res["ok"], res["reason"])

    def test_list_declares_surface_reuse(self):
        # The reversed contract: the list IS surface-reuse (AI-on-surface), so Check 3 applies.
        self.assertTrue(declares_surface_reuse(_per_block_section(RATIONALE_B1_LIST_AI_ON_SURFACE)))

    def test_list_prompt_names_items_and_forbids_invented(self):
        # The bake prompt feeds the supplied items AND forbids invented/extra text (not blanket).
        pd = parse_prompt_delta(HTML_B1_LIST_AI_ON_SURFACE).lower()
        self.assertIn("workflow automation", pd)        # a supplied item is named
        self.assertRegex(pd, r"no\s+invented")          # negative against invented text

    def test_list_declared_ai_on_surface_but_flat_html_slots_flagged(self):
        # The contradiction: rationale says AI-on-surface/reuse, but HTML floated the list to flat
        # CONTENT_n slots with NO AI zone -> Check 3 fires (the surface was not reused).
        res = evaluate(RATIONALE_B1_LIST_AI_ON_SURFACE, HTML_B1_LIST_FLAT_SLOTS_NO_ZONE,
                       empty_frac=0.30, slug="signboard-list-body")
        self.assertFalse(res["ok"])
        self.assertTrue(any("surface" in f.lower() for f in res["flags"]), res["reason"])

    def test_list_blanket_no_text_clause_flagged(self):
        # A blanket no-text clause over a surface that must carry the supplied list -> Check 4 fires
        # (the model is told NOT to render the very text the rationale routed to the AI).
        res = evaluate(RATIONALE_B1_LIST_AI_ON_SURFACE, HTML_B1_LIST_BLANKET_NOTEXT,
                       empty_frac=0.30, slug="signboard-list-body")
        self.assertFalse(res["ok"])
        self.assertTrue(any("no-text" in f.lower() or "no text" in f.lower()
                            for f in res["flags"]), res["reason"])


class TestLane3CoverHeadlineSlot(unittest.TestCase):
    """(b) fullbleed-overlay-cover — a native HTML headline slot for the hook."""

    def test_cover_has_native_headline_slot(self):
        slots = parse_html_text_slots(HTML_COVER_WITH_HEADLINE)
        self.assertIn("HEADLINE", slots)

    def test_cover_with_headline_slot_passes(self):
        res = evaluate(RATIONALE_COVER_WITH_HEADLINE, HTML_COVER_WITH_HEADLINE, empty_frac=0.30,
                       slug="fullbleed-overlay-cover")
        self.assertTrue(res["ok"], res["reason"])

    def test_cover_without_headline_slot_has_no_headline(self):
        # The defect: a cover whose HTML carries NO headline slot — the hook is lost.
        slots = parse_html_text_slots(HTML_COVER_NO_HEADLINE)
        self.assertNotIn("HEADLINE", slots)
        self.assertEqual(slots, [])


class TestStaticHeroSrc(unittest.TestCase):
    """D1 (Check 15) — a post-subject image bound by a STATIC `_ai_bg/…` src instead of the
    `{{…_PATH}}` Mustache placeholder is flagged; the placeholder binding passes."""

    HTML_STATIC_IMG = (
        '<div class="photo-zone" data-zone="photo" data-slot="PHOTO_MAIN">'
        '<img src="_ai_bg/photo_main.png" alt="" /></div>'
    )
    HTML_PLACEHOLDER_IMG = (
        '<div class="photo-zone" data-zone="photo" data-slot="PHOTO_MAIN">'
        '<img src="{{PHOTO_MAIN_PATH}}" alt="" /></div>'
    )
    HTML_STATIC_BG = (
        '<div class="bg-photo" data-slot="PHOTO_MAIN" '
        'style="background-image: url(\'_ai_bg/photo_main.png\'); background-size: cover;"></div>'
    )
    HTML_PLACEHOLDER_BG = (
        '<div class="bg-photo" data-slot="PHOTO_MAIN" '
        'style="background-image: url(\'{{PHOTO_MAIN_PATH}}\'); background-size: cover;"></div>'
    )
    HTML_LOGO_STATIC = (  # a non-hero (logo) static src must NOT be flagged
        '<img src="_ai_bg/logo.png" data-slot="LOGO" alt="" />'
    )

    def test_static_img_src_flagged(self):
        flags = static_hero_src_flags(self.HTML_STATIC_IMG)
        self.assertEqual(len(flags), 1, flags)
        self.assertIn("PHOTO_MAIN", flags[0])
        self.assertIn("static hero src", flags[0])

    def test_placeholder_img_src_passes(self):
        self.assertEqual(static_hero_src_flags(self.HTML_PLACEHOLDER_IMG), [])

    def test_static_bg_div_flagged(self):
        flags = static_hero_src_flags(self.HTML_STATIC_BG)
        self.assertEqual(len(flags), 1, flags)
        self.assertIn("PHOTO_MAIN", flags[0])

    def test_placeholder_bg_div_passes(self):
        self.assertEqual(static_hero_src_flags(self.HTML_PLACEHOLDER_BG), [])

    def test_non_hero_static_src_not_flagged(self):
        self.assertEqual(static_hero_src_flags(self.HTML_LOGO_STATIC), [])

    def test_evaluate_wires_static_hero_check(self):
        # The defect surfaces through the full evaluate() verdict (MISMATCH).
        rationale = ("## Per-block breakdown\n"
                     "- **PHOTO_MAIN** · AI-integrated · the full-bleed hero scene\n")
        res = evaluate(rationale, self.HTML_STATIC_IMG, empty_frac=0.30, slug="editorial-cover")
        self.assertFalse(res["ok"])
        self.assertTrue(any("static hero src" in f for f in res["flags"]), res["flags"])


if __name__ == "__main__":
    unittest.main()

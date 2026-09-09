#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0", "pyyaml>=6.0"]
# ///
"""Check B — the treatment-contract gate (AIOS-190 W2, the reasoning spine).

Sibling of measure_text_contrast.py / dead_space.py / check_rationale.py. Runs at the
QUALITY GATE (Step 6), AFTER generation. Where Check A verifies the rationale EXISTS, Check
B verifies the OUTPUT actually matches the TREATMENT the rationale declared per block.

It binds the CATEGORY, not the pixels/position (structural fidelity — the decision already
made: rationale says "headline = AI-integrated/occluded" -> the gate verifies it came out
integrated-in-the-image vs a flat HTML box, NOT its exact coordinates).

ELEVEN deterministic checks (+ one ref-pixel sub-check). 1–3 are the v1 subset; 4–7 (SPEC-A)
deepen the contract so the per-block treatment is carried FAITHFULLY into BOTH the prompt_delta
and the HTML; 8–9 (SPEC-L1) promote the two worst run-02 photographic-path regressions
(INVENTA, REMONTA) to a hard gate; 9b (SPEC-r5g) validates the containment CLAIM against the
REF PIXELS themselves (a hallucinated read passes 9's self-consistency — run-06
numbered-photo-callout); 10 (SPEC-r3) is the per-element ref-vs-output comparator the Check B
docstring named as the follow-up — it compares each declared distinctive element (badge/seal,
callout pill, accent graphic, display word) to assets/ref-canonical.png by coarse
accent-region detection (the brand accent resolved from --accent / brand_context tokens.json,
NOT a hardcoded hue); 11 (SPEC-r5g) makes the declared-vs-shipped contract BIDIRECTIONAL (an element the
rationale never declared must not ship):

  1. treatment-category presence (structural read of template.html + rationale §2):
       - Every block declared HTML-overlay SHOULD have a text-bearing data-slot in the HTML
         (it was supposed to ship as a real HTML box). Count mismatch -> flag.
       - When the rationale declares AT LEAST ONE AI-integrated text block, the output must
         carry an AI image zone ([ai-image-zone) — the integrated text lives in the image,
         not in HTML. Missing image zone while AI-integrated text was declared -> flag.

  2. raster-zone-filled (test-09-06 fold 2a): a declared raster zone (photo-zone / cutout /
     hero / photo-main) that the rationale says is filled-every-post must actually RENDER
     FILLED. We approximate via near-uniformity: if the preview's largest near-uniform
     region covers >= --empty-threshold of the canvas, the raster zone shipped as an empty
     grey placeholder -> FLAG (the body-numbered failure). Filled photos are not near-uniform.

  3. surface-reuse (test-09-06 fold 2b): a B1 ref whose rationale says "reuse the in-scene
     surface" must place that text on the surface — i.e. AI-placed, NOT a flat HTML box.
     Deterministic proxy: form is B1 + rationale says reuse-the-surface + the output is
     pure-HTML-text with no AI image zone -> the surface was not reused.

  4. prompt-contradicts-AI-text (SPEC-A, r01): the rationale declared text AI-integrated /
     occluded, but the prompt_delta forbids text wholesale ("No text, no lettering, no
     captions") -> the model has nothing to occlude. The no-text clause must apply ONLY to
     HTML-assigned blocks. n_ai > 0 AND a blanket no-text clause in prompt_delta -> FLAG.

  5. B1-total-recompose (SPEC-A, r02): a B1 that declares "reuse the surface" but whose §3
     pipeline edit_mode is total-recompose regenerates a lookalike surface instead of reusing
     the ref's. B1 must clean+reserve+reuse, never total-recompose -> FLAG.

  6. baked-isolable-text (SPEC-A, r07): a block whose NAME is isolable chrome-text
     (caption / CTA / byline / badge / label / handle) declared AI-integrated bakes it into
     the image, violating the brand hard-rule (all isolable type is HTML/overlay) -> FLAG.
     ("headline"/"display" are excluded — a headline CAN be genuinely occluded/AI.)

  7. reserved-zone-geometry (SPEC-A, r03; needs --measurements): the prompt_delta reserves an
     upper band for HTML text, but the HTML text zones (from _measurements.yaml) occupy
     further down than that band (+tolerance) -> the text collides with the busy scene below
     it. A single reserved-zone % must be shared by prompt_delta + HTML -> FLAG.

  8. scrim-vs-ref (SPEC-L1, run-02 INVENTA): the rationale §2 declares
     legibility-method=natural-composition (the ref has NO band) but template.html authors a
     full-width opaque band (a `.bottom-scrim`-style div) -> the builder stamped a scrim the
     ref does not show. A band is authored ONLY for legibility-method=ref-band -> FLAG.

  9. containment-vs-ref (SPEC-L1, run-02 REMONTA): the rationale §2 declares
     containment=contained-rectangle but the authored image zone is full-bleed (full-canvas)
     -> the contained ref was blown up to a full-bleed scene (ref-07). Containment is binding
     -> FLAG.

 9b. containment-vs-REF-PIXELS (SPEC-r5g, run-06 numbered-photo-callout): Check 9 compares the
     rationale to the HTML — pure self-consistency, so a HALLUCINATED contained-rectangle read
     (the rationale invented a paper mat on a full-bleed teal-water ref; everything downstream
     was consistently wrong) sails through. 9b validates the CLAIM against assets/
     ref-canonical.png itself: a genuinely contained photo sits on a near-uniform mat, so the
     ref's four border strips must read mat-like — side strips low-variance (robust MAD) and
     the strips mutually tone-matched. Scene-texture continuation at the edges (textured side
     strips, or a strong top-vs-bottom luminance gradient) -> the ref is full-bleed and
     contained-rectangle is a misread -> FLAG forcing a re-read. Coarse + deterministic
     (downscaled luminance, median/MAD with tolerance bands). The top/bottom strips carry only
     the tone-match bound, NOT the variance bound — masthead chrome and a headline legitimately
     sit in them on a genuine mat (measured on the real index-card-cover ref).

 10. ref-vs-output element fidelity (SPEC-r3; needs --preview + a ref): detect the brand's
     ACCENT DEVICE regions (seal/badge, callout pill, accent graphic) by accent-hue-proximity
     detection in BOTH the built preview and assets/ref-canonical.png, then per declared
     distinctive element assert presence + gross geometry (quadrant + size band). Hard-fails
     on a DROPPED device (ref shows an accent device the output region lacks — the dropped
     Claude seal), an INFLATED/RELOCATED device (authored accent device grossly larger or
     moved vs the ref — the small pill blown to a full-width strip), or a GHOST display (a
     declared display word dominant in the ref, near-absent in the output) -> FLAG.
     The accent comes from --accent, else brand_context/visual-identity/tokens.json
     (colors.accent), else the legacy coral default with a stderr WARN.

 11. undeclared visible element (SPEC-r5g, run-06 monitor-surface-cover): Checks 1-10 verify
     DECLARED blocks shipped faithfully; none flags an element the rationale never declared.
     The failure: a visible DECORATIVE_WORD div (a ghost word injected to appease the font
     gate) shipped with no §2 block — and passed everything. Check 11 closes the loop: every
     content data-slot in template.html (pure chrome excluded — see CHROME_SLOT_EXCLUDE) must
     have a corresponding §2 block in rationale.md; an undeclared slot -> FLAG naming it. A
     visible element exists because the rationale reasoned it into existence, never to
     satisfy a gate.

A FLAG is a contract MISMATCH -> the builder re-rolls via the existing 3-try ladder. If the
ladder exhausts with the contract still unmet -> needs-user-decision (the right decision was
not executable = a human case).

LIMITATION: a FULL by-block pixel-region comparator (matching each rationale block to a pixel
region) remains a follow-up. These nine are deterministic structural/geometry reads, each
flagging a real, named test-09-06 / run-02 failure mode — not faked. (distinctive-graphics and
reserved-band POSITION stay soft — by-eye golden set — as harder-to-assert reads.)

Exit codes:
  0  -> all checks pass (output matches declared treatments).
  1  -> usage / file-not-found error.
  2  -> at least one contract mismatch -> re-roll.

Usage:
    uv run check_treatment_contract.py --rationale <dir>/rationale.md \
        --template-html <dir>/template.html --preview <dir>/preview.png
"""
import argparse
import colorsys
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# Reuse the near-uniformity primitive from the dead-space gate (same definition of "empty").
from dead_space import empty_fraction  # noqa: E402


def _force_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# ---------------------------------------------------------------------------------------
# Treatment categories — the rationale's per-block treatment maps to ONE of these.
# ---------------------------------------------------------------------------------------
AI_INTEGRATED = "ai-integrated"   # text in the image: integrated / overlaid / occluded / on-surface
HTML_OVERLAY = "html-overlay"     # isolable HTML box / pill
ICON_CHROME = "icon-chrome"       # embedded mark / brand chrome — not a content text block

# substrings (lowercased) that classify a declared treatment string
AI_HINTS = ("ai", "integrated", "occlud", "in-scene", "surface", "baked", "woven")
HTML_HINTS = ("html", "overlay", "pill", "box", "isolable")
CHROME_HINTS = ("icon", "chrome", "embedded", "brand mark", "badge", "logo")

# data-slots that are NOT content text (chrome/image) — excluded from the HTML-text count.
NON_TEXT_SLOT_HINTS = ("logo", "badge", "icon", "photo", "image", "bg", "background",
                       "mark", "wordmark", "brand", "_path", "src")

RASTER_HINTS = ("photo-zone", "photo zone", "cutout", "hero", "photo-main", "photo main",
                "raster", "image zone", "ai image", "ai-generated")
FILLED_HINTS = ("every post", "filled", "varies per post", "per post", "fills")

# Block-NAME hints for text the brand hard-rule says must be HTML overlay, NEVER baked into
# the image. The anchor is the brand grade's `text_policy: html-overlay` key (a named,
# brand-wide routing key in ai-image-style.md — promoted from the old loose prose "all type
# is HTML/overlay" by the r6 image-style redesign so this anchor is stable even though the
# grade's STYLE fields (medium/lighting/treatment) moved per-template). Used by Check 6 (the
# r07 fold): a block whose NAME is one of these but whose declared treatment is AI-integrated
# = a baked isolable text block. NOTE this check reads only rationale.md + template.html — it
# does NOT parse the grade, so the grade's shrink does not affect it; the `text_policy` key is
# the conceptual anchor, kept brand-wide precisely so this gate keeps a stable reference.
# "headline"/"display" are deliberately EXCLUDED — a headline can be genuinely AI-integrated
# (occluded behind a subject HTML can't do); only the small isolable chrome-text below qualifies.
ISOLABLE_TEXT_NAME_HINTS = ("caption", "cta", "call to action", "badge", "byline",
                            "label", "handle", "tagline", "kicker", "subtitle", "name label",
                            "name-label", "wordmark")

# A blanket "no text"-style clause that, inside a prompt_delta, NEGATES a declared
# AI-integrated text treatment (the r01 contradiction). "no logos" is intentionally NOT here
# — forbidding logos is fine; forbidding TEXT while AI-text was declared is the bug.
NO_TEXT_CLAUSE_RE = re.compile(
    r"no\s+(?:text|lettering|letters|captions?|words|type|typography|writing|titles?)\b",
    re.IGNORECASE)

TOTAL_RECOMPOSE_RE = re.compile(r"total[\s-]?recompose", re.IGNORECASE)

# --- SPEC-L1 (run-02 fidelity, photographic path) ----------------------------------------
# Check 8 (scrim-vs-ref) + Check 9 (containment-vs-ref). The rationale §2 records two
# ref-reads per the builder agent schema: `legibility-method: ref-band | natural-composition`
# and `containment: contained-rectangle | full-bleed`. These two checks promote the run-02
# soft rules (INVENTA, REMONTA) to a hard gate — the leitura-mãe: a rule that re-drives across
# runs gets a deterministic gate.

# A rationale legibility-method declaring the ref has NO band (legibility from the scene).
NATURAL_COMPOSITION_RE = re.compile(
    r"legibility[\s_-]?method\s*[:=]\s*\**\s*natural[\s-]?composition", re.IGNORECASE)
# A rationale containment declaring the ref's image zone is a CONTAINED rectangle (not full-bleed).
CONTAINED_RECT_RE = re.compile(
    r"containment\s*[:=]\s*\**\s*contained[\s-]?rectangle", re.IGNORECASE)

# Minimum band height (fraction of canvas) for a "full-width band" to count as an opaque scrim.
SCRIM_MIN_HEIGHT_FRAC = 0.20
# Minimum alpha for a band to count as "opaque" (a contrast assertion, not a faint tint).
SCRIM_MIN_ALPHA = 0.45


# === SPEC-r6g — the run-07 mismatch detectors (items 8, 9) + seal provenance (item 6) =====
#
# Check 12 (item 8, fixed-hero mismatch — HARD FAIL): when the hero object IS the brand
# identity (the template SLUG names a concrete object, e.g. `chain-*`, and the ref shows that
# one dominant subject), the AI slot must RECOLOR the ref's object, not regenerate a per-post
# subject — else the object drifts category (the run-07 chain → gears). The post-render
# confirmation of the pre-render PHOTO_SUBJECT==ref check (item 4). Anchored in the real build:
# highlight-headline-render/rationale.md:82 `edit_mode: partial-subject (the chain is the
# per-post subject)`, :71 the hero slot is "generated by the AI image pipeline, the per-post
# variation axis", :83 `when_ai_runs: every post (the 3D-rendered subject changes per post)`.
# Inegociável: the object-identity must not change category.

# Slug tokens that are generic pool/family/role words, NOT an object-identity noun. A slug
# names an object-identity when it carries a CONCRETE-OBJECT token outside this stop-list.
SLUG_STOPWORDS = {
    "cover", "headline", "render", "statement", "quote", "card", "cards", "photo", "text",
    "rule", "ruled", "numbered", "number", "billboard", "system", "page", "one", "grid",
    "scribble", "screen", "surface", "crt", "fullbleed", "full", "bleed", "gallery", "steal",
    "creator", "portrait", "cta", "callout", "pills", "pill", "about", "hook", "main", "left",
    "right", "top", "bottom", "dark", "light", "byline", "kicker", "the", "a", "of", "with",
    "and", "in", "on", "to", "v1", "v2", "v3", "split", "stack", "band", "strip", "mat",
    "monitor", "index", "group", "highlight", "highlighted", "outlined", "title", "subtitle",
    "signboard", "overlay", "fullbleed", "body", "list", "panel", "panels", "slat", "slats",
}
# Concrete-object nouns a SLUG may carry that name a fixed hero-object identity (the run-07
# `chain-*` case + the obvious siblings). The list is the recognizer's seed, not a closed set:
# any non-stopword slug token ALSO names a candidate object — these are just the ones we name
# explicitly in the flag. The point is structural: a slug noun + a per-post-regenerated hero
# routing = the fixed-hero violation, whatever the noun.
KNOWN_OBJECT_SLUG_NOUNS = {
    "chain", "gear", "gears", "key", "keys", "lock", "padlock", "bulb", "lightbulb", "rocket",
    "ladder", "bridge", "anchor", "compass", "puzzle", "brick", "bricks", "engine", "wrench",
    "hammer", "shield", "trophy", "flag", "crown", "diamond", "leaf", "tree", "mountain",
    "wave", "bolt", "flame", "torch", "coin", "clock", "target", "magnet", "telescope",
}

# The rationale routes the hero as the per-post VARIATION AXIS / regenerated subject (not a
# recolor-the-ref). These phrasings, in §2/§3, mark the hero as AI-regenerated every post.
PER_POST_SUBJECT_RE = re.compile(
    r"(per[\s-]?post\s+(?:variation|subject|axis)|the\s+per[\s-]?post\s+subject|"
    r"(?:subject|object|hero|3d[\s-]?rendered\s+subject)\s+changes?\s+per\s+post|"
    r"varies?\s+per\s+post|when_ai_runs\s*[:=]\s*\**\s*every\s+post|"
    r"generated\s+by\s+the\s+ai\s+image\s+pipeline)", re.IGNORECASE)
# An explicit "keep / recolor the ref's subject" contract — the CORRECT fixed-hero read. Its
# presence means the builder honored the identity (vary only framing/lighting), so no flag.
KEEP_SUBJECT_RE = re.compile(
    r"(keep\s+the\s+subject|recolou?r\s+the\s+(?:ref|reference|subject|object)|"
    r"same\s+(?:object|subject)\s+as\s+the\s+ref|vary\s+only\s+(?:framing|angle|lighting)|"
    r"fixed[\s-]?hero|recolou?r(?:ed)?\s+ref|preserve\s+the\s+(?:object|subject))",
    re.IGNORECASE)


def slug_object_noun(slug: str | None) -> str | None:
    """The concrete-object noun a template slug names (the fixed hero-object identity), or None.

    A slug like `chain-highlight-headline` names `chain`; `one-page-system-cover` names nothing
    (all tokens are pool/role words). Returns the FIRST non-stopword token, preferring a
    known-object noun. Coarse + deterministic — the same altitude as the other §2 name reads."""
    if not slug:
        return None
    tokens = [t for t in re.split(r"[\s_\-]+", slug.lower()) if t]
    # Prefer an explicitly-known object noun anywhere in the slug.
    for t in tokens:
        if t in KNOWN_OBJECT_SLUG_NOUNS:
            return t
    # Else the first token that is not a generic pool/role stopword and is alphabetic.
    for t in tokens:
        if t.isalpha() and t not in SLUG_STOPWORDS and len(t) >= 3:
            return t
    return None


def hero_is_regenerated_per_post(rationale_text: str) -> bool:
    """True when the rationale routes the hero subject as the per-post AI-regenerated variation
    axis (NOT a recolor-the-ref). Scoped to §2+§3 (the block/pipeline body) so a §4 'considered
    regenerating but rejected' doesn't trip it; an explicit keep/recolor contract suppresses."""
    body = _per_block_section(rationale_text)
    pipeline = _section_body(rationale_text, r"pipeline") or ""
    scope = body + "\n" + pipeline
    if KEEP_SUBJECT_RE.search(scope):
        return False
    return bool(PER_POST_SUBJECT_RE.search(scope))


# --- Check 13 (item 9, scene-restyle mismatch — FLAG) -------------------------------------
# When the face/head is the HERO and the brand has a headshot, the output must DERIVE from the
# headshot (restyled to the medium), not invent a face. The build failure: the identity slot
# stayed a PLACEHOLDER string (never resolved to a path) and/or PHOTO_SUBJECT is a GENERIC
# person description (what the generator actually consumes → random face). Anchored in:
# creator-cover-cta/_slides/slide-01/metadata.json:17 `PHOTO_CREATOR_PATH: "(filled from
# brand-headshot: …simon-pic.jpg)"` (literal placeholder, never resolved) + :14 `PHOTO_SUBJECT:
# "a male creator, dark hair, confident expression, arms crossed, dark clothing"` (generic).
# Determinant: placeholder-shaped identity slot / generic-person subject with a headshot
# declared. Limit: detects placeholder/generic (deterministic); does NOT judge whether identity
# survived heavy stylization (the owner's eye — see r6c).

# An identity slot key that carries the brand person's headshot path (resolved at build).
IDENTITY_SLOT_KEY_RE = re.compile(
    r"(creator|headshot|portrait|face|person|founder|host|presenter)_?path", re.IGNORECASE)
# A value that is a PLACEHOLDER, not a resolved file path: a parenthetical note, a "filled
# from"/"to be filled"/"TBD" marker, or an empty/none. A genuine path ends in an image
# extension or contains a real directory separator with a filename.
PLACEHOLDER_VALUE_RE = re.compile(
    r"^\s*$|^\s*\(.*\)\s*$|filled\s+from|to\s+be\s+filled|tbd|todo|placeholder|"
    r"^\s*(?:none|null|n/?a|-+)\s*$|brand[\s-]?headshot\s*:", re.IGNORECASE)
IMAGE_PATH_RE = re.compile(r"\.(?:png|jpe?g|webp|gif|bmp|tiff?)\s*$", re.IGNORECASE)
# A PHOTO_SUBJECT that is a GENERIC person description (not a named identity). Person nouns +
# free-text appearance traits = an invented person the generator will draw fresh.
GENERIC_PERSON_RE = re.compile(
    r"\b(a|an|the)\s+(?:young\s+|older\s+|middle[\s-]aged\s+)?"
    r"(man|woman|male|female|person|creator|guy|lady|individual|figure|model|professional|"
    r"entrepreneur|founder|host|presenter|character)\b", re.IGNORECASE)


def metadata_slot_value(metadata: dict, key_re: re.Pattern) -> tuple[str, str] | None:
    """First (key, value) in a metadata.json-style dict whose KEY matches key_re and whose value
    is a string. metadata.json carries the slot fills the generator consumes (PHOTO_*_PATH,
    PHOTO_SUBJECT). Returns None when no such key is present."""
    for k, v in (metadata or {}).items():
        if isinstance(v, str) and key_re.search(str(k)):
            return str(k), v
    return None


def is_placeholder_path(value: str) -> bool:
    """True when an identity-slot value is a PLACEHOLDER (a parenthetical/`filled from` note,
    empty, or a non-path marker) rather than a resolved image path."""
    v = (value or "").strip()
    if IMAGE_PATH_RE.search(v):
        return False
    return bool(PLACEHOLDER_VALUE_RE.search(v))


def face_is_hero(rationale_text: str) -> bool:
    """True when the rationale marks a human face/head as a HERO element (any medium/style) — the
    item-9 trigger. Keys on §2 naming a face/head/portrait/creator as the dominant subject, NOT
    on the template being a 'creator cover' (the generalization: any hero face, even surreal)."""
    body = _per_block_section(rationale_text).lower()
    has_face = bool(re.search(
        r"\b(face|head|portrait|creator|person|headshot|visage|countenance)\b", body))
    hero_signal = bool(re.search(
        r"\b(hero|dominant|main subject|primary subject|center(?:piece)?|focal|the subject)\b",
        body)) or "photo_creator" in body or "photo_main" in body
    return has_face and hero_signal


def headshot_declared(rationale_text: str, html: str, metadata: dict | None) -> bool:
    """True when a brand headshot is in play — the precondition for the item-9 flag. Signals: a
    `brand-headshot` substitution method, a `simon-pic`/headshot path mention, an identity
    `*_PATH` slot, or a `PHOTO_CREATOR_PATH`-style key in metadata. (No headshot → the soft
    default is the AI inventing a face, which is NOT flagged.)"""
    blob = (rationale_text + "\n" + html).lower()
    if "brand-headshot" in blob or "brand headshot" in blob or "headshot" in blob:
        return True
    if re.search(r"\bsimon[-_]?pic\b", blob):
        return True
    if metadata and metadata_slot_value(metadata, IDENTITY_SLOT_KEY_RE):
        return True
    return False


# --- Check 14 (item 6, seal/logo provenance — HARD FAIL on the destructive CSS) -----------
# A brand seal/logo must keep its provenance + color. Two deterministic CSS red-flags the
# run-07 one-page miss exposed: (a) a colored logo killed by `filter: invert(…)` /
# `brightness(0)` (the coral seal turned monochrome), (b) a serrated/starburst seal APPROXIMATED
# as a plain CSS disc (`border-radius:50%`) on a logo/badge element — a serrated shape is never a
# circle. Both are authored in template.html, both destroy the mark; both hard-fail.
LOGO_SELECTOR_RE = re.compile(r"(logo|badge|seal|brandmark|brand-mark|wordmark|starburst|emblem)",
                              re.IGNORECASE)
DESTRUCTIVE_FILTER_RE = re.compile(
    r"filter\s*:\s*[^;}]*?(invert\s*\(\s*(?:1|100%|[1-9]\d*%)|brightness\s*\(\s*0\b)",
    re.IGNORECASE)
CIRCLE_RADIUS_RE = re.compile(r"border-radius\s*:\s*50%", re.IGNORECASE)
SERRATED_HINT_RE = re.compile(r"(starburst|serrated|sunburst|cog|gear|scalloped|sawtooth|zigzag)",
                              re.IGNORECASE)


def seal_provenance_flags(html: str, rationale_text: str) -> list[str]:
    """Hard-fail flags for a seal/logo whose authored CSS destroys its provenance/shape.

    (a) a logo/badge/seal selector with a destructive `filter: invert(…)`/`brightness(0)` — kills
        a colored mark's color. (b) a logo/seal the rationale calls serrated/starburst/cog that
        the HTML approximates with `border-radius:50%` (a plain disc) — a serrated shape is never
        a circle. Conservative: scans `selector { body }` CSS rule blocks so the selector and the
        offending property are read together."""
    flags: list[str] = []
    serrated_seal = bool(SERRATED_HINT_RE.search(_per_block_section(rationale_text)))
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", html):
        selector = m.group(1)
        body = m.group(2)
        if not LOGO_SELECTOR_RE.search(selector):
            continue
        if DESTRUCTIVE_FILTER_RE.search(body):
            flags.append(
                f"logo provenance: a brand logo/seal selector ('{selector.strip()[:48]}') carries "
                f"a destructive `filter: invert()`/`brightness(0)` — it kills a colored mark's "
                f"color (the run-07 one-page miss: `filter:invert` turned the coral seal "
                f"monochrome). A colored logo is placed as-is (commons asset), never inverted.")
        if serrated_seal and CIRCLE_RADIUS_RE.search(body):
            flags.append(
                f"seal shape: the rationale calls the seal serrated/starburst but the HTML "
                f"selector ('{selector.strip()[:48]}') approximates it with `border-radius:50%` "
                f"(a plain disc) — a serrated/starburst shape is never a CSS circle. Use the real "
                f"glyph (commons SVG), not a CSS approximation.")
    return flags


# --- Check 15 (D1, studio-sweep): hero image bound by a STATIC src, not the {{…_PATH}} slot --
# A post-subject AI image element (an <img> or a background-image div carrying data-slot) MUST
# bind its source to the Mustache placeholder ({{PHOTO_MAIN_PATH}} / {{<SLOT>_PATH}}) — the
# render-time substitution that fills it with the POST's generated image. A hardcoded relative
# `_ai_bg/…` path is NOT substituted, so every post ships the TEMPLATE's demo background (the
# "post ships the template demo" defect). The literal `_ai_bg/…` file is the template's demo
# asset only, never the binding the shipped template carries.
#
# Deterministic + conservative: only flags a post-subject element (a data-slot whose name reads
# as the photo/hero/AI image — PHOTO_*, *_MAIN, hero, image) whose src/background-image points at
# a literal `_ai_bg/…` path with NO `{{…}}` Mustache placeholder. A masthead/logo/decor slot is
# never flagged.
STATIC_AI_BG_RE = re.compile(r"_ai_bg/[^\"')\s]+", re.IGNORECASE)
MUSTACHE_RE = re.compile(r"\{\{\{?[^}]+\}?\}\}")
# data-slot names that denote the post-subject / hero AI image (the binding D1 governs).
HERO_SLOT_HINTS = ("photo", "hero", "image", "_main", "main", "subject", "bg", "background")


def _is_hero_slot(slot: str) -> bool:
    s = slot.lower()
    return any(h in s for h in HERO_SLOT_HINTS)


def static_hero_src_flags(html: str) -> list[str]:
    """Flags for a post-subject image element bound by a STATIC `_ai_bg/…` path instead of the
    `{{…_PATH}}` Mustache placeholder (Check 15 / D1).

    Walks each `<img …>` tag and each element carrying an inline `background-image:url(...)`.
    When the element carries a hero/photo `data-slot` AND its src/url is a literal `_ai_bg/…`
    path with no `{{…}}` placeholder, it is the static-src defect. Conservative: an element with
    a `{{…}}` placeholder anywhere in its src/url passes; a non-hero slot (masthead/logo) is
    skipped."""
    flags: list[str] = []

    def _emit(slot: str, kind: str) -> None:
        flags.append(
            f"static hero src: the post-subject {kind} for data-slot '{slot}' binds a literal "
            f"`_ai_bg/…` path instead of the `{{{{{slot}_PATH}}}}` Mustache placeholder. The "
            f"placeholder is what render-time substitution fills with the POST's image; a static "
            f"`_ai_bg/…` src is NEVER substituted, so every post ships the TEMPLATE's demo "
            f"background (the 'post ships the template demo' defect). Bind the hero image to "
            f"`{{{{{slot}_PATH}}}}` — the `_ai_bg/…` file is the demo asset only.")

    # <img …> tags. The data-slot may sit on the <img> OR on a wrapping photo-zone div
    # (the editor targets the div handle). So the binding defect is keyed on the SRC: any
    # <img> whose src is a literal `_ai_bg/…` AI-asset path with no `{{…}}` placeholder is a
    # static hero binding (the `_ai_bg/` dir is exclusively the per-post AI image). The slot
    # NAME (for the message) is read from the img if present, else its nearest enclosing
    # data-slot div, else the generic PHOTO_MAIN.
    for m in re.finditer(r"<img\b[^>]*>", html, re.IGNORECASE):
        tag = m.group(0)
        src_m = re.search(r'src\s*=\s*["\']([^"\']*)["\']', tag, re.IGNORECASE)
        if not src_m:
            continue
        src = src_m.group(1)
        if MUSTACHE_RE.search(src) or not STATIC_AI_BG_RE.search(src):
            continue
        slot_m = re.search(r'data-slot\s*=\s*["\']([^"\']+)["\']', tag, re.IGNORECASE)
        if slot_m:
            # A non-hero own-slot (logo/icon/badge) is not the post-subject binding — skip.
            if not _is_hero_slot(slot_m.group(1)):
                continue
            slot = slot_m.group(1)
        else:
            # nearest preceding data-slot opening div (the photo-zone wrapper holds the handle)
            before = html[: m.start()]
            wrap = re.findall(r'data-slot\s*=\s*["\']([^"\']+)["\']', before, re.IGNORECASE)
            slot = wrap[-1] if wrap and _is_hero_slot(wrap[-1]) else "PHOTO_MAIN"
        _emit(slot, "<img>")

    # background-image:url(...) divs (inline style) carrying a hero data-slot
    for m in re.finditer(r"<(?:div|section|figure)\b[^>]*>", html, re.IGNORECASE):
        tag = m.group(0)
        slot_m = re.search(r'data-slot\s*=\s*["\']([^"\']+)["\']', tag, re.IGNORECASE)
        if not slot_m or not _is_hero_slot(slot_m.group(1)):
            continue
        url_m = re.search(r"background-image\s*:\s*url\(\s*['\"]?([^'\")]*)['\"]?\s*\)",
                          tag, re.IGNORECASE)
        if not url_m:
            continue
        url = url_m.group(1)
        if MUSTACHE_RE.search(url):
            continue
        if STATIC_AI_BG_RE.search(url):
            _emit(slot_m.group(1), "background-image div")
    return flags


def html_has_opaque_fullwidth_band(html: str) -> bool:
    """True when template.html authors a full-width, high-opacity horizontal band — the
    `.bottom-scrim`-style div the INVENTA miss stamps over a photo (Check 8).

    Deterministic signal: a CSS rule with (a) a `*scrim*`/`*band*`-named selector OR full-width
    geometry (width:100% or left+right ~0), AND (b) an `rgba(...)`/`hsla(...)` background whose
    alpha >= SCRIM_MIN_ALPHA, AND (c) a height >= SCRIM_MIN_HEIGHT_FRAC of canvas (height:NN% /
    NNcqh, or top/bottom anchoring that spans the floor). We scan CSS rule blocks so opacity and
    geometry are read together. Conservative: ambiguous rules do NOT trip the flag (soft golden
    set still catches those)."""
    # Pull `selector { ... }` blocks from the <style> region.
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", html):
        selector = m.group(1).lower()
        body = m.group(2).lower()
        # background alpha
        alpha = _max_bg_alpha(body)
        if alpha is None or alpha < SCRIM_MIN_ALPHA:
            continue
        # full-width? named scrim/band selector, or explicit full-width geometry
        named = ("scrim" in selector or "band" in selector)
        full_width = named or ("width:100%" in body.replace(" ", "")) or _spans_full_width(body)
        if not full_width:
            continue
        # tall enough to be a legibility band (not a thin rule/border)
        if _band_height_frac(body) >= SCRIM_MIN_HEIGHT_FRAC:
            return True
    return False


def _max_bg_alpha(css_body: str) -> float | None:
    """Highest rgba()/hsla() alpha among background declarations in a CSS rule body, or None."""
    alphas: list[float] = []
    for m in re.finditer(r"(?:rgba|hsla)\([^)]*?,\s*([01]?\.?\d+)\s*\)", css_body):
        try:
            alphas.append(float(m.group(1)))
        except ValueError:
            continue
    return max(alphas) if alphas else None


def _spans_full_width(css_body: str) -> bool:
    b = css_body.replace(" ", "")
    has_left = re.search(r"left:0(?:px|%)?;", b) or "left:0;" in b
    has_right = re.search(r"right:0(?:px|%)?;", b) or "right:0;" in b
    return bool(has_left and has_right) or "inset:0" in b


def _band_height_frac(css_body: str) -> float:
    """Approximate the band's height as a fraction of canvas (1080×1350 ~ 4:5).
    Reads height:NN% (of canvas height), height:NNcqh, or top/bottom anchoring."""
    b = css_body.replace(" ", "")
    m = re.search(r"height:(\d{1,3})%", b)
    if m:
        return min(100, int(m.group(1))) / 100.0
    m = re.search(r"height:(\d{1,3}(?:\.\d+)?)cqh", b)
    if m:
        return min(100.0, float(m.group(1))) / 100.0
    # bottom:0 + top:NN%  → spans (100-NN)%
    mt = re.search(r"top:(\d{1,3})%", b)
    if ("bottom:0" in b) and mt:
        return max(0.0, (100 - int(mt.group(1))) / 100.0)
    # bottom-anchored with explicit bottom band height in cqw on a 4:5 canvas is rarer; default
    # to a permissive estimate so a clearly-named scrim div with no parsable height still counts.
    if "bottom:0" in b or "top:0" in b:
        return SCRIM_MIN_HEIGHT_FRAC  # anchored band, height unparsed → assume it qualifies
    return 0.0


def html_image_zone_is_full_bleed(html: str) -> bool:
    """True when the authored image/photo zone covers the full canvas (full-bleed) — the signal
    that a CONTAINED-rectangle ref was built full-bleed (Check 9, the ref-07 REMONTA miss).

    Deterministic proxy: an `<img>`/photo container with full-canvas geometry —
    `object-fit:cover` + (width:100%/height:100% or inset:0/left:0+right:0+top:0+bottom:0), or a
    selector whose rule sets width:100% AND height:100% on the image layer. A contained rectangle
    instead has a bounded width/height (< 100%) or padding/inset margins."""
    # Look at rules attached to image-bearing selectors or the photo slot.
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", html):
        selector = m.group(1).lower()
        body = m.group(2).replace(" ", "").lower()
        is_image_rule = ("img" in selector or "photo" in selector or "hero" in selector
                         or "scene" in selector or "bg" in selector or "cover" in selector)
        if not is_image_rule:
            continue
        full = (("width:100%" in body and "height:100%" in body)
                or "inset:0" in body
                or ("object-fit:cover" in body and ("width:100%" in body or "inset:0" in body)))
        if full:
            return True
    return False


# --- SPEC-r5g Check 9b — containment claim vs REF PIXELS ---------------------------------
# Check 9 is self-consistency (rationale vs HTML): a HALLUCINATED contained-rectangle read
# stays internally consistent and passes (run-06 numbered-photo-callout: the rationale invented
# a paper mat + kraft on a full-bleed teal-water ref). 9b samples the four border strips of
# assets/ref-canonical.png: a genuinely contained photo sits on a near-uniform mat, so the
# SIDE strips must be low-variance (robust MAD — mats keep text-free margins at the extreme
# left/right edges) and the strips mutually tone-matched. The TOP/BOTTOM strips carry only the
# tone-match bound, not the variance bound: masthead chrome and a headline legitimately sit in
# them on a genuine mat (measured: real index-card-cover ref, top-strip MAD ≈ 43 from headline
# ink on cream while its SIDE strips read MAD 4–5; the full-bleed numbered-photo-callout ref
# reads side MAD 26–30 and a 138-step top-vs-bottom luminance gradient).
REF_STRIP_FRAC = 0.06        # border-strip thickness as a fraction of each dimension
REF_STRIP_GRID_W = 128       # downscale width — coarse, deterministic, jitter-free
MAT_SIDE_MAD_MAX = 14.0      # side-strip luminance MAD above this = scene texture, not mat
MAT_SIDE_TONE_TOL = 35.0     # left-vs-right median luminance gap above this = no shared mat
MAT_TB_TONE_TOL = 90.0       # top-vs-bottom median gap above this = vertical scene gradient


def ref_border_stats(img: "Image.Image") -> dict:
    """Robust luminance stats for the four border strips of a ref image (Check 9b).

    Returns {top|bottom|left|right: {median, mad}} computed on a downscaled greyscale grid.
    Median/MAD (not mean/std) so sparse chrome text on a mat does not masquerade as texture."""
    grid_w = REF_STRIP_GRID_W
    grid_h = max(16, round(grid_w * img.height / img.width))
    small = img.convert("RGB").resize((grid_w, grid_h))
    arr = np.asarray(small).astype(float)
    lum = 0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.0722 * arr[:, :, 2]
    t = max(2, round(REF_STRIP_FRAC * grid_h))
    s = max(2, round(REF_STRIP_FRAC * grid_w))
    strips = {"top": lum[:t, :], "bottom": lum[-t:, :],
              "left": lum[:, :s], "right": lum[:, -s:]}
    out: dict = {}
    for name, v in strips.items():
        med = float(np.median(v))
        out[name] = {"median": med, "mad": float(np.median(np.abs(v - med)))}
    return out


def containment_misread(stats: dict) -> str | None:
    """Judge Check 9b border stats. Returns a reason string when the ref's border strips read
    as SCENE-TEXTURE CONTINUATION (the containment claim is a misread), or None when they are
    consistent with a near-uniform mat (a genuinely contained photo)."""
    reasons: list[str] = []
    for name in ("left", "right"):
        st = stats[name]
        if st["mad"] > MAT_SIDE_MAD_MAX:
            reasons.append(
                f"the {name} border strip carries scene texture (luminance MAD "
                f"{st['mad']:.0f} > {MAT_SIDE_MAD_MAX:.0f} — a mat is near-uniform at the "
                f"side edges)")
    lr_gap = abs(stats["left"]["median"] - stats["right"]["median"])
    if lr_gap > MAT_SIDE_TONE_TOL:
        reasons.append(
            f"the left/right border strips are not tone-matched (median luminance gap "
            f"{lr_gap:.0f} > {MAT_SIDE_TONE_TOL:.0f} — no single mat tone spans both sides)")
    tb_gap = abs(stats["top"]["median"] - stats["bottom"]["median"])
    if tb_gap > MAT_TB_TONE_TOL:
        reasons.append(
            f"strong top-vs-bottom luminance mismatch (median gap {tb_gap:.0f} > "
            f"{MAT_TB_TONE_TOL:.0f} — a vertical scene gradient, not a uniform mat)")
    return "; ".join(reasons) if reasons else None


# --- SPEC-r5g Check 11 — undeclared visible elements (bidirectional Check B) --------------
# Checks 1-10 only verify DECLARED blocks; an element the rationale never declared sails
# through (run-06 monitor-surface-cover: a visible DECORATIVE_WORD ghost div, injected to
# appease the font gate, shipped with no §2 block). Check 11 walks template.html's CONTENT
# data-slots and requires each to have a corresponding §2 block.
#
# Pure-chrome slots are EXCLUDED (the explicit exclusion list): chrome is injected from
# tokens.json by convention, not reasoned per-template in §2.
CHROME_SLOT_EXCLUDE = ("masthead", "wordmark", "pagination")
# Slot-name tokens too generic to count as "declared" on their own (the monitor §2 says
# "ONE key word in the headline" — that must NOT declare a DECORATIVE_WORD slot). A generic
# token only declares via the slot's FULL normalized phrase (e.g. "decorative word").
GENERIC_SLOT_TOKENS = {"word", "text", "main", "line", "item", "zone", "block", "content",
                       "slot", "area", "copy", "value", "string", "row", "col", "left",
                       "right", "center", "top", "bottom"}
# Slot-name token -> §2 vocabulary that legitimately declares it (rationales speak in design
# language, not slot ids: a HEADLINE slot is declared by a "display word" block).
SLOT_TOKEN_SYNONYMS = {
    "headline": ("headline", "display word", "display", "title"),
    "numeral": ("numeral", "number", "numbered"),
    "kicker": ("kicker", "eyebrow"),
    "cta": ("cta", "call to action", "call-to-action"),
    "byline": ("byline", "handle", "creator"),
    "callout": ("callout", "call-out", "pill"),
}


def find_undeclared_slots(rationale_text: str, html: str) -> list[str]:
    """Content text data-slots in template.html with NO corresponding block in rationale §2.

    A slot counts as declared when (a) its full normalized phrase appears in §2 (underscores/
    digits stripped: DECORATIVE_WORD -> "decorative word"), or (b) any of its NON-GENERIC
    name tokens (or their SLOT_TOKEN_SYNONYMS) appears as a whole word in §2. Pure chrome
    (CHROME_SLOT_EXCLUDE) is skipped. Coarse by design — same altitude as Checks 6/8/9."""
    body = _per_block_section(rationale_text).lower()
    undeclared: list[str] = []
    for slot in parse_html_text_slots(html):
        norm = re.sub(r"[\d_\-]+", " ", slot.lower())
        norm = re.sub(r"\s+", " ", norm).strip()
        if not norm or any(c in norm for c in CHROME_SLOT_EXCLUDE):
            continue
        if norm in body:  # full phrase declared
            continue
        declared = False
        for tok in norm.split():
            cands: tuple[str, ...] = ()
            if len(tok) >= 3 and tok not in GENERIC_SLOT_TOKENS:
                cands = (tok,)
            cands = cands + SLOT_TOKEN_SYNONYMS.get(tok, ())
            for cand in cands:
                if re.search(r"(?<![a-z0-9])" + re.escape(cand) + r"(?![a-z0-9])", body):
                    declared = True
                    break
            if declared:
                break
        if not declared:
            undeclared.append(slot)
    return undeclared


def classify_treatment(treatment: str) -> str | None:
    """Map a declared treatment string to a category, or None if unrecognized."""
    t = treatment.lower()
    # chrome first (an "embedded icon / chrome" line shouldn't be read as AI)
    if any(h in t for h in CHROME_HINTS):
        return ICON_CHROME
    if any(h in t for h in HTML_HINTS):
        return HTML_OVERLAY
    if any(h in t for h in AI_HINTS):
        return AI_INTEGRATED
    return None


# ---------------------------------------------------------------------------------------
# Rationale parsing — pull the per-block declared treatments + the form + reuse flags.
# ---------------------------------------------------------------------------------------

def parse_form(text: str) -> str:
    """Extract the form letter/key from §1 (e.g. 'B1', 'C', 'B2', 'A', 'solid')."""
    m = re.search(r"form\s*[:=]?\s*\**\s*(solid|b1|b2|a|c)\b", text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    # fallback: a bare token like "B1 — surface in-scene"
    m = re.search(r"\b(B1|B2|C|A|solid)\b\s*[—-]", text)
    return m.group(1).upper() if m else ""


def _section_body(text: str, header_re: str) -> str | None:
    """Return the body of the first markdown section whose header matches header_re
    (header → next header), or None when no matching header is found."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*\S)\s*$", line)
        if m and re.search(header_re, m.group(1), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(r"^\s{0,3}#{1,6}\s+\S", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def _per_block_section(text: str) -> str:
    """Return ONLY the §2 per-block-breakdown body. Scoping to §2 keeps §1 tree-path bullets
    and §4 ambiguity prose out of the block parse. Falls back to the whole text when no
    per-block header is found (headerless / data.js-style input)."""
    body = _section_body(text, r"per[\s-]?block|block breakdown|block treatment")
    return body if body is not None else text


# Pipeline edit-mode keywords (scanned in §3 when there is no explicit `edit_mode:` line).
_PIPELINE_MODE_KEYWORDS = (
    "total-recompose", "total recompose", "partial-subject", "partial subject",
    "partial-bg", "partial bg", "texture-extract", "texture extract",
)


def parse_block_treatments(text: str) -> list[dict]:
    """Parse §2 (per-block) into [{block, treatment, category, why}].

    Tolerant of multiple authoring styles. Recognizes lines shaped like:
       - **Block name** · AI-integrated · because ...
       - Headline "X" | AI / integrated | <why>
       - "block": "...", "treatment": "...", "why": "..."   (the data.js shape, if pasted)
    Falls back to splitting a line on the dot/pipe/dash separators with the treatment as the
    middle field. Each parsed block is classified into a category.
    """
    blocks: list[dict] = []

    # Style A: JSON-ish "treatment": "..." (the data.js gabarito shape) — search whole text.
    for m in re.finditer(r'treatment["\']?\s*[:=]\s*["\']([^"\']+)["\']', text, re.IGNORECASE):
        treatment = m.group(1).strip()
        blocks.append({"block": "", "treatment": treatment,
                       "category": classify_treatment(treatment), "why": ""})
    if blocks:
        return blocks

    # Style B/C operate on the §2 section only (so §1/§4 bullets don't leak in).
    text = _per_block_section(text)

    for raw in text.splitlines():
        stripped = raw.strip()

        # Style C: markdown TABLE rows (the real rationale shape — | block | treatment | why |
        # or | block | role | decision | why |, with the treatment column NOT fixed at #2).
        if stripped.startswith("|") and stripped.count("|") >= 2:
            cells = [c.strip().strip("*` ") for c in stripped.strip("|").split("|")]
            cells = [c for c in cells]
            if len(cells) < 2:
                continue
            # separator row (|---|---|) — every cell is only dashes/colons/spaces.
            if all(set(c) <= set("-: ") for c in cells if c != "") and any(cells):
                continue
            block = cells[0]
            if block.lower() in ("block", "text block", "element", "blocks", ""):
                continue  # header row
            # The why/reason is the LAST cell (prose that may name a rejected alternative —
            # never classified). Among the MIDDLE cells (role, decision, treatment) take the
            # LAST that classifies — a "decision" column usually follows a "role" column.
            mids = cells[1:-1] if len(cells) >= 3 else cells[1:]
            cat, treatment = None, ""
            for c in mids:
                cc = classify_treatment(c)
                if cc is not None:
                    cat, treatment = cc, c
            if cat is None:  # fall back to the 2nd cell verbatim
                cat, treatment = classify_treatment(cells[1]), cells[1]
            if cat is None:
                continue
            why = cells[-1] if len(cells) >= 3 else ""
            blocks.append({"block": block, "treatment": treatment, "category": cat, "why": why})
            continue

        # Style B: bullet ROWS (must START with a bullet marker) with a field separator
        # (· | — between block · treatment · why). Only the explicit TREATMENT field (2nd) is
        # classified, never the why-prose, so a block's reasoning can name a rejected
        # alternative without being mis-counted as that treatment.
        if not re.match(r"^[-*•]\s+", stripped):
            continue  # not a block row — skip prose, headers, form lines
        line = re.sub(r"^[-*•]\s+", "", stripped).strip().strip("|").strip()
        parts = re.split(r"\s*[·|]\s*|\s+[—–]\s+", line)
        parts = [p.strip() for p in parts if p.strip()]
        if len(parts) < 2:
            continue
        block = parts[0].strip("*` ")
        treatment = parts[1].strip("*` ")  # classify ONLY this field, never the why-prose
        cat = classify_treatment(treatment)
        if cat is None:
            continue
        why = parts[2] if len(parts) > 2 else ""
        blocks.append({"block": block, "treatment": treatment, "category": cat, "why": why})
    return blocks


def declares_surface_reuse(text: str) -> bool:
    """True when §2/§1 says the text should reuse the existing in-scene surface."""
    t = text.lower()
    return ("reuse" in t and "surface" in t) or "in-scene surface" in t or "on the surface" in t


def declares_filled_raster(text: str) -> bool:
    """True when a raster/photo zone is declared filled-every-post (must render filled)."""
    t = text.lower()
    has_raster = any(h in t for h in RASTER_HINTS)
    has_filled = any(h in t for h in FILLED_HINTS)
    return has_raster and has_filled


# ---------------------------------------------------------------------------------------
# template.html parsing — count the real HTML TEXT data-slots + detect an AI image zone.
# ---------------------------------------------------------------------------------------

def parse_html_text_slots(html: str) -> list[str]:
    """data-slot values that carry CONTENT TEXT (chrome/image slots excluded)."""
    slots = re.findall(r'data-slot\s*=\s*["\']([^"\']+)["\']', html, re.IGNORECASE)
    out = []
    for s in slots:
        sl = s.lower()
        if any(h in sl for h in NON_TEXT_SLOT_HINTS):
            continue
        out.append(s)
    return out


def has_ai_image_zone(html: str) -> bool:
    """True when template.html declares an [ai-image-zone...] block (AI generation happens)."""
    return bool(re.search(r"\[ai-image-zone", html, re.IGNORECASE))


def parse_prompt_delta(html: str) -> str:
    """Concatenate every [ai-image-zone] block's `prompt_delta:` text from template.html.

    The prompt the model actually receives lives next to the layout, in the
    [ai-image-zone]…[/ai-image-zone] comment block (see template-conventions.md). Checks 4
    and 7 compare that text against the rationale's declared treatments. Capture from
    `prompt_delta:` up to the next top-level key or the block close."""
    out: list[str] = []
    blocks = re.findall(r"\[ai-image-zone.*?\[/ai-image-zone\]", html, re.IGNORECASE | re.DOTALL)
    targets = blocks or ([html] if "prompt_delta" in html.lower() else [])
    for block in targets:
        m = re.search(
            r"prompt_delta\s*:\s*\|?\s*(.*?)"
            r"(?=^\s*(?:variables|output_aspect|ref_input|brand_style_source|slot_path|"
            r"generation_route|output|generated)\s*:|\[/ai-image-zone\]|\Z)",
            block, re.IGNORECASE | re.DOTALL | re.MULTILINE)
        if m:
            out.append(m.group(1).strip())
    return "\n".join(out)


def parse_pipeline_edit_mode(text: str) -> str:
    """Extract the edit mode (lowercased). Prefers an explicit `edit_mode:` line; otherwise
    scans the §3 Pipeline section for a known mode keyword (the real rationale writes it as
    prose, e.g. 'edit-from-ref (total-recompose mode — …)'). '' if neither is found.

    Scoping the keyword scan to §3 keeps a §4 'considered total-recompose but rejected' out
    of the result (the keyword is the chosen mode, not a ruled-out alternative)."""
    m = re.search(r"edit_mode\s*[:=]\s*([^\n.]+)", text, re.IGNORECASE)
    if m:
        return m.group(1).strip().lower()
    section = _section_body(text, r"pipeline") or ""
    sl = section.lower()
    for kw in _PIPELINE_MODE_KEYWORDS:
        if kw in sl:
            return kw.replace(" ", "-")
    return ""


def parse_reserved_band_pct(prompt_delta: str) -> float | None:
    """Parse the reserved-zone fraction the prompt promises for HTML text (Check 7).

    Recognizes 'upper/top NN%', 'top third/half/quarter', and the named bands. Returns the
    fraction of canvas HEIGHT reserved from the top (e.g. 0.45 for 'upper 45%'), or None."""
    t = prompt_delta.lower()
    m = re.search(r"(?:upper|top)\s+(\d{1,3})\s*%", t)
    if m:
        return min(100, int(m.group(1))) / 100.0
    if "top third" in t or "upper third" in t:
        return 1 / 3
    if "top half" in t or "upper half" in t:
        return 0.5
    if "top quarter" in t or "upper quarter" in t:
        return 0.25
    return None


def html_text_bottom_extent(measurements: dict | None) -> float | None:
    """The lowest bottom edge (top+height) across the measured HTML text zones, as a fraction
    of canvas height — the geometry the HTML actually occupies (Check 7). None if no zones."""
    els = (measurements or {}).get("elements") or []
    bottoms = []
    for el in els:
        bb = el.get("bbox_pct") or []
        if isinstance(bb, (list, tuple)) and len(bb) == 4:
            try:
                bottoms.append((float(bb[1]) + float(bb[3])) / 100.0)
            except (TypeError, ValueError):
                continue
    return max(bottoms) if bottoms else None


# ---------------------------------------------------------------------------------------
# Check 10 — per-element ref-vs-output fidelity (SPEC-r3, the ref-output comparator).
#
# The Check B docstring (and the L1 follow-up note) name a "full per-block pixel-region
# comparator" as the next gate. This is that follow-up, kept COARSE + DETERMINISTIC: it
# detects the brand's CORAL DEVICE regions (the seal/badge, the callout pill, the number
# chip, the coral graphic) by colour-region detection, then compares each declared
# distinctive element's PRESENCE + gross geometry (quadrant + size band) between the BUILT
# OUTPUT and assets/ref-canonical.png.
#
# It hard-fails on the run-03 misses nothing else catches:
#   - DROPPED BADGE  — the ref shows a coral device with NO comparable device anywhere in the
#     output (cover-hook: the "Claude" starburst seal vanished). Distinguished from a merely
#     RELOCATED device by a comparable-size-elsewhere probe: a seal that still EXISTS but moved
#     names "relocated", a seal that truly vanished names "dropped" (they are not conflated).
#   - INFLATED PILL — an authored coral pill/callout grossly LARGER than the ref's. TWO paths:
#       (b)  REF-ANCHORED: the ref's coral device matched (by bbox overlap) to a much larger
#            output device — fires when the ref carries recoverable coral.
#       (a') REF-INDEPENDENT: the rationale declares a small/contained coral pill but the OUTPUT
#            authors a DOMINANT / full-width-strip coral device with no contained counterpart —
#            fires off the OUTPUT ALONE. This is the path the REAL body-numbered miss needs: its
#            ref-canonical re-encode is washed out (any_accent=False), so (b) can never reach it.
#            It is also independent of present_in_ref — an over-authored pill is flagged whether
#            or not the canonical ref happens to carry it.
#   - GHOST DISPLAY — a declared display word the ref shows DOMINANT that the output renders
#     near-absent / tiny in its region (cover-hook: "system" ghosted at the floor).
#
# It is COARSE on purpose: no pixel-exact match. Detection is by accent mask + a pure-numpy
# connected-component pass on a downscaled grid (no scipy). The dominant accent BACKGROUND
# FIELD (e.g. the cover-hook orange wall) is separated from accent DEVICES by a size band so
# an accent background never masquerades as a badge. When the ref carries no usable accent
# signal (a washed-out re-encode), the REF-ANCHORED sub-checks (dropped / relocated / (b)
# inflated) DEGRADE GRACEFULLY (skip — nothing to compare against), but the REF-INDEPENDENT
# inflated-pill path (a') still fires off the output, so a washed-out ref cannot hide an
# over-authored pill — per the spec's "ship the cheap ones, log the rest".
# ---------------------------------------------------------------------------------------

# Accent mask: BRAND-AGNOSTIC hue-proximity classifier. A pixel is "device-colored" when its
# hue sits within ACCENT_HUE_TOL_DEG of the brand accent's hue (circular distance) AND its
# saturation/value clear floors derived from the accent itself (relative, with absolute
# minimums) — so a muted/antialiased rendition of the accent still counts, but neutrals,
# washed tints and dark shadows do not. The accent is RESOLVED, never hardcoded: --accent,
# else brand_context/visual-identity/tokens.json (colors.accent), else the legacy brand-coral
# default below with a stderr WARN. Calibrated so the coral brand (#d05344) keeps the exact
# 2.2.x behavior on the real ssc-e2e artifacts (field/seal/pill isolation, muted callout).
DEFAULT_ACCENT_HEX = "#d05344"   # legacy brand coral — the FALLBACK, not the rule
ACCENT_HUE_TOL_DEG = 25.0        # max circular hue distance from the accent hue (degrees) —
                                 # wide enough for the warm drift of an AI-rendered accent scene
                                 # (real coral-brand refs land 20-28° off the token), tight
                                 # enough to exclude the opposite half of the wheel outright
ACCENT_SAT_FLOOR_REL = 0.50      # saturation floor = this × the accent's own saturation…
ACCENT_SAT_FLOOR_MIN = 0.20      # …but never below this absolute floor
ACCENT_VAL_FLOOR_REL = 0.72      # value floor = this × the accent's own value (for coral this
                                 # lands at ~0.59 — the old mask's R>=150 floor, kept on purpose)…
ACCENT_VAL_FLOOR_MIN = 0.30      # …but never below this absolute floor

# An accent region this large (fraction of canvas) is the BACKGROUND FIELD, not a device.
ACCENT_FIELD_MIN_FRAC = 0.18
# An accent device must cover at least this fraction to count (filters JPEG speckle / antialias).
ACCENT_DEVICE_MIN_FRAC = 0.0015
# Grid resolution for the connected-component pass (coarse — geometry only).
ACCENT_GRID_W = 96

# Size bands for an accent DEVICE (fraction of canvas). A device that jumps more than one band
# between ref and output is "grossly" resized → a flag.
DEVICE_SIZE_BANDS = (
    ("small", 0.0, 0.020),
    ("mid", 0.020, 0.080),
    ("dominant", 0.080, 1.01),
)
# How far two device centroids may differ (fraction of canvas, Chebyshev) before "relocated".
DEVICE_RELOCATE_TOL = 0.28
# A device whose output area is this many× the ref's (or vice-versa) is "grossly" resized,
# even if it crosses only one size band (the small lower-left box → full-width strip case,
# ~4× area, sits right on the small/mid boundary so a band-hop alone under-counts it).
DEVICE_INFLATE_RATIO = 3.0
# Ref-INDEPENDENT inflated-pill path: an accent pill/callout declared SMALL/contained in the
# rationale that the OUTPUT authors as a DOMINANT accent device (>= this fraction of canvas)
# is an inflated pill — flagged even when the canonical ref carries NO recoverable accent (the
# real body-numbered ref-canonical re-encode is washed out → any_accent=False). This is the
# accent-region-free path the ref-anchored sub-checks can't reach. A device spanning most of
# the canvas WIDTH (a full-width strip) is the signature of the body-numbered miss.
AUTHORED_PILL_DOMINANT_FRAC = 0.060   # output accent device this large = "dominant", inflated
AUTHORED_PILL_FULLWIDTH_FRAC = 0.55   # device bbox spans >= this fraction of canvas width


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """#rgb / #rrggbb (leading # optional) → (r, g, b) ints. Raises ValueError on junk."""
    s = hex_color.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6 or any(c not in "0123456789abcdefABCDEF" for c in s):
        raise ValueError(f"invalid accent hex color: {hex_color!r} (expected #rrggbb)")
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


def accent_hsv(hex_color: str) -> tuple[float, float, float]:
    """The mask target: (hue_degrees [0,360), saturation [0,1], value [0,1]) of an accent."""
    r, g, b = (c / 255.0 for c in _hex_to_rgb(hex_color))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return h * 360.0, s, v


def _rgb_to_hsv_arrays(arr: "np.ndarray") -> tuple["np.ndarray", "np.ndarray", "np.ndarray"]:
    """Vectorized RGB→HSV for an HxWx3 uint8 array: (hue_degrees, sat [0,1], val [0,1])."""
    rgb = arr[:, :, :3].astype(np.float32) / 255.0
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx = rgb.max(axis=-1)
    mn = rgb.min(axis=-1)
    delta = mx - mn
    nz = delta > 0
    ds = np.where(nz, delta, 1.0)
    h = np.where(mx == r, ((g - b) / ds) % 6.0,
                 np.where(mx == g, (b - r) / ds + 2.0, (r - g) / ds + 4.0)) * 60.0
    h = np.where(nz, h, 0.0)
    s = np.where(mx > 0, delta / np.where(mx > 0, mx, 1.0), 0.0)
    return h, s, mx


def accent_mask(arr: "np.ndarray", accent_hex: str = DEFAULT_ACCENT_HEX) -> "np.ndarray":
    """Boolean mask of accent-colored (brand device) pixels in an HxWx3 uint8 RGB array.

    Brand-agnostic by construction: classification is hue-proximity to the RESOLVED brand
    accent (circular distance <= ACCENT_HUE_TOL_DEG) plus saturation/value floors scaled
    from the accent itself — a green/blue/yellow accent works exactly like the coral one."""
    a_hue, a_sat, a_val = accent_hsv(accent_hex)
    h, s, v = _rgb_to_hsv_arrays(arr)
    dh = np.abs(h - a_hue)
    dh = np.minimum(dh, 360.0 - dh)
    sat_floor = max(ACCENT_SAT_FLOOR_MIN, ACCENT_SAT_FLOOR_REL * a_sat)
    val_floor = max(ACCENT_VAL_FLOOR_MIN, ACCENT_VAL_FLOOR_REL * a_val)
    return (dh <= ACCENT_HUE_TOL_DEG) & (s >= sat_floor) & (v >= val_floor)


def _label_grid(mask: "np.ndarray") -> list[dict]:
    """Pure-numpy/Python connected-component labelling (4-connectivity) of a small boolean
    grid. Returns one dict per component: {frac, x0, x1, y0, y1, cx, cy} in [0,1] coords.

    Kept dependency-free (no scipy) and cheap — runs on a ~96-wide downscaled grid."""
    h, w = mask.shape
    total = h * w
    seen = [[False] * w for _ in range(h)]
    m = mask.tolist()
    comps: list[dict] = []
    for sy in range(h):
        for sx in range(w):
            if not m[sy][sx] or seen[sy][sx]:
                continue
            # iterative flood fill
            stack = [(sy, sx)]
            seen[sy][sx] = True
            xs0 = xs1 = sx
            ys0 = ys1 = sy
            sumx = sumy = cnt = 0
            while stack:
                cy, cx = stack.pop()
                cnt += 1
                sumx += cx
                sumy += cy
                xs0 = min(xs0, cx); xs1 = max(xs1, cx)
                ys0 = min(ys0, cy); ys1 = max(ys1, cy)
                for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                    if 0 <= ny < h and 0 <= nx < w and m[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        stack.append((ny, nx))
            comps.append({
                "frac": cnt / total,
                "x0": xs0 / w, "x1": (xs1 + 1) / w,
                "y0": ys0 / h, "y1": (ys1 + 1) / h,
                "cx": (sumx / cnt) / w, "cy": (sumy / cnt) / h,
            })
    return comps


def detect_accent_regions(img: "Image.Image", accent_hex: str = DEFAULT_ACCENT_HEX) -> dict:
    """Detect brand-accent regions in an image, split into the background FIELD and DEVICES.

    Returns {field: comp|None, devices: [comp,...], any_accent: bool}, each comp a dict with
    frac + bbox + centroid in [0,1]. Devices are sorted largest-first. Detection runs on a
    downscaled grid (ACCENT_GRID_W wide) so it is coarse + fast and ignores pixel jitter."""
    grid_w = ACCENT_GRID_W
    grid_h = max(1, round(grid_w * img.height / img.width))
    small = img.convert("RGB").resize((grid_w, grid_h))
    arr = np.array(small)
    mask = accent_mask(arr, accent_hex)
    comps = _label_grid(mask)
    field = None
    devices: list[dict] = []
    for c in comps:
        if c["frac"] >= ACCENT_FIELD_MIN_FRAC:
            if field is None or c["frac"] > field["frac"]:
                if field is not None:
                    devices.append(field)
                field = c
            else:
                devices.append(c)
        elif c["frac"] >= ACCENT_DEVICE_MIN_FRAC:
            devices.append(c)
    devices.sort(key=lambda c: c["frac"], reverse=True)
    return {"field": field, "devices": devices, "any_accent": bool(comps)}


def quadrant(cx: float, cy: float) -> str:
    """Coarse 9-cell band label for a centroid: vertical (top/mid/bottom) + horizontal
    (left/center/right). Used as the gross-position bucket for a device."""
    vy = "top" if cy < 1 / 3 else ("bottom" if cy > 2 / 3 else "mid")
    hx = "left" if cx < 1 / 3 else ("right" if cx > 2 / 3 else "center")
    return f"{vy}-{hx}"


def size_band(frac: float) -> str:
    """Map a device's canvas-fraction to a coarse size band (small / mid / dominant)."""
    for name, lo, hi in DEVICE_SIZE_BANDS:
        if lo <= frac < hi:
            return name
    return "dominant"


def _band_index(band: str) -> int:
    for i, (name, _lo, _hi) in enumerate(DEVICE_SIZE_BANDS):
        if name == band:
            return i
    return len(DEVICE_SIZE_BANDS) - 1


# Element-kind hints parsed from the rationale §2 element name / line.
BADGE_NAME_HINTS = ("badge", "seal", "starburst", "stamp", "sticker", "chip", "number")
PILL_NAME_HINTS = ("pill", "callout", "tag", "label box", "box", "strip", "banner", "lozenge")
GRAPHIC_NAME_HINTS = ("graphic", "line-burst", "sunburst", "burst", "device", "rays",
                      "starburst", "ornament")
DISPLAY_NAME_HINTS = ("display", "headline", "display word", "hero word", "big word")

# A device-kind is "accent" (the comparator's scope) when the element line marks it accent/
# coral/brand-primary OR names a known accent device (badge/seal/pill/callout/graphic).
# Display words are tracked separately (the ghost-display sub-check is size-based, not
# accent-region based).
ACCENT_DEVICE_KINDS = ("badge", "pill", "graphic")


def parse_distinctive_elements(rationale_text: str) -> list[dict]:
    """Pull the distinctive elements declared in §2 that the ref-vs-output comparator can
    reason about. Returns [{name, kind, accent, present_in_ref}].

      kind  ∈ {badge, pill, graphic, display}
      accent — the element line says the device is accent-colored (accent / coral /
              brand-primary) or is a known accent device kind.
      present_in_ref — the rationale asserts the ref shows this element (the default for a
              declared distinctive element; the comparator only enforces presence for these).

    Coarse on purpose: it keys on element NAMES + the `distinctive_graphics` tag, mirroring
    how Checks 6/8/9 read §2 by name + declared property rather than full NLP."""
    body = _per_block_section(rationale_text)
    out: list[dict] = []
    seen_kinds: set[str] = set()
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        low = line.lower()
        # the explicit distinctive_graphics tag → an accent graphic device.
        if "distinctive_graphics" in low and "graphic" not in seen_kinds:
            out.append({"name": "distinctive-graphic", "kind": "graphic",
                        "accent": True, "present_in_ref": True})
            seen_kinds.add("graphic")
            continue
        # Treat as an element declaration: a bullet / bold-led row, OR a plain `Name · …`
        # row (the real headerless rationale shape uses `· `-separated element lines with no
        # bullet). The `·` form must carry a `·` separator so prose paragraphs don't qualify.
        is_elem = (bool(re.match(r"^[-*•]\s+", line)) or line.startswith("**")
                   or ("·" in line and not line.startswith(("`", ">", "|"))))
        if not is_elem:
            continue
        # Classify on the element NAME ONLY (the segment before the first `·`/`|` separator),
        # never the trailing description — a block's prose can name a SIBLING device (e.g. the
        # image-zone line mentions "the dark pill container") without being mis-typed as it.
        name_seg = re.split(r"[·|]", re.sub(r"^[-*•\s]+", "", line).strip("* "))[0]
        name_seg = name_seg.replace("*", "").strip()
        name_low = name_seg.lower()
        accent_line = ("accent" in low or "coral" in low or "brand-primary" in low
                       or "brand primary" in low or "var(--brand-primary)" in low
                       or "var(--brand-accent)" in low)
        kind = None
        if any(h in name_low for h in BADGE_NAME_HINTS):
            kind = "badge"
        elif any(h in name_low for h in PILL_NAME_HINTS):
            kind = "pill"
        elif any(h in name_low for h in GRAPHIC_NAME_HINTS):
            kind = "graphic"
        elif any(h in name_low for h in DISPLAY_NAME_HINTS):
            kind = "display"
        if kind is None:
            continue
        if kind in seen_kinds:
            continue
        accent = accent_line or kind in ACCENT_DEVICE_KINDS
        # The rationale may mark an element as NOT shown by the canonical ref (e.g. an OPTIONAL
        # pill "present in ref-05, absent in ref-04"). Don't enforce its presence against the
        # ref — only elements the ref genuinely shows drive the dropped-device sub-check.
        present_in_ref = not re.search(r"absent\s+in\s+(?:the\s+)?ref", low)
        # The element line's declared REF size: a callout pill the rationale describes as
        # "small" / a "box" / "contained" / "lower-left box" is a SMALL/contained device in the
        # ref. This is read from the WHOLE line (description carries the geometry word), and
        # drives the ref-INDEPENDENT inflated-pill path (an authored DOMINANT accent device with
        # a declared-small ref form is inflated even when the ref carries no recoverable accent).
        declared_small = bool(re.search(
            r"\b(?:small|tiny|compact|contained|lower[\s-]left|upper[\s-]left|"
            r"lower[\s-]right|upper[\s-]right|corner|chip|lozenge)\b", low))
        declared_dominant = bool(re.search(
            r"\b(?:full[\s-]width|dominant|large|big|strip|banner|spans?\s+the\s+width)\b", low))
        name = name_seg.strip()[:60] or kind
        out.append({"name": name, "kind": kind, "accent": accent,
                    "present_in_ref": present_in_ref,
                    "declared_small": declared_small,
                    "declared_dominant": declared_dominant})
        seen_kinds.add(kind)
    return out


def _device_spans_full_width(dev: dict) -> bool:
    """True when an accent device's bbox spans most of the canvas WIDTH (a full-width strip —
    the body-numbered inflated-pill signature)."""
    return (dev.get("x1", 0.0) - dev.get("x0", 0.0)) >= AUTHORED_PILL_FULLWIDTH_FRAC


def _bbox_overlap(a: dict, b: dict) -> float:
    """Intersection area (fraction of canvas) of two device bboxes in [0,1] coords. Used to
    match an output device to a ref device by REGION — a device that grew/shrank in place still
    overlaps the ref's bbox even when its centroid drifts."""
    ix0 = max(a.get("x0", 0.0), b.get("x0", 0.0))
    iy0 = max(a.get("y0", 0.0), b.get("y0", 0.0))
    ix1 = min(a.get("x1", 0.0), b.get("x1", 0.0))
    iy1 = min(a.get("y1", 0.0), b.get("y1", 0.0))
    if ix1 <= ix0 or iy1 <= iy0:
        return 0.0
    return (ix1 - ix0) * (iy1 - iy0)


def compare_elements_to_ref(elements: list[dict], out_regions: dict,
                            ref_regions: dict) -> list[str]:
    """Compare declared distinctive elements between the built output and ref-canonical.

    Returns a list of hard-fail flag strings (empty = pass). Sub-checks:
      (a) dropped device  — an accent device the ref shows, absent in the output (and NOT merely
          relocated: no output accent device sits near the ref device's region);
      (b) inflated/moved  — an authored accent device grossly larger (>1 size band / >ratio) OR
          relocated (centroid moved > tolerance) vs the ref's matching device;
      (a') ref-INDEPENDENT inflated pill — a declared accent pill/callout authored as a DOMINANT
          / full-width accent device in the OUTPUT with no small contained counterpart, flagged
          even when the canonical ref carries NO recoverable accent (the real body-numbered
          ref-canonical is a washed-out re-encode → any_accent=False, so the ref-anchored (b)
          path can never reach it). This is the ref-accent-free path the spec's inflated pill
          actually needs.
      (c) ghost display   — a declared display word DOMINANT in the ref but near-absent in
          the output (proxied by the dominant-accent-field presence in the ref vs none / a
          tiny region in the output, the cover-hook 'system' ghost).

    DEGRADES GRACEFULLY: if the ref carries no usable accent, the ref-ANCHORED sub-checks (a/b)
    are skipped (no false fire), but the ref-INDEPENDENT inflated-pill path (a') still fires off
    the OUTPUT alone."""
    flags: list[str] = []
    # The inflated-pill path must NOT depend on present_in_ref: an authored pill blown up in the
    # OUTPUT is a regression regardless of whether the canonical ref happens to carry it (the
    # reviewer's item 2 — a pill 'absent in ref-04' is still inflated when over-authored).
    declares_accent_pill = any(e["accent"] and e["kind"] in ("pill", "graphic") for e in elements)
    declares_ref_accent_device = any(
        e["accent"] and e["kind"] in ACCENT_DEVICE_KINDS and e.get("present_in_ref", True)
        for e in elements)
    declares_display = any(e["kind"] == "display" for e in elements)

    ref_devices = ref_regions.get("devices", [])
    out_devices = out_regions.get("devices", [])
    ref_has_accent = ref_regions.get("any_accent") and (ref_devices or ref_regions.get("field"))
    out_field = out_regions.get("field")
    ref_field = ref_regions.get("field")

    # --- (a) dropped device + (b) inflated/relocated (REF-ANCHORED) -----------------------
    # Only run when the rationale declares an accent device the ref shows AND the ref exposes a
    # usable accent device region (else we cannot compare — degrade gracefully).
    if declares_ref_accent_device and ref_has_accent and ref_devices:
        ref_dev = ref_devices[0]              # the most prominent ref accent device
        # Match the ref device to an output device by REGION (bbox overlap OR centroid within
        # the relocate tolerance — an inflated device that grew over the ref still OVERLAPS the
        # ref's region even when its centroid shifts). This is the "same device, possibly
        # resized" branch.
        region_match = next(
            (d for d in out_devices
             if _bbox_overlap(d, ref_dev) > 0.0
             or (abs(d["cx"] - ref_dev["cx"]) <= DEVICE_RELOCATE_TOL
                 and abs(d["cy"] - ref_dev["cy"]) <= DEVICE_RELOCATE_TOL)),
            None)
        if region_match is not None:
            out_dev = region_match
            rb, ob = size_band(ref_dev["frac"]), size_band(out_dev["frac"])
            ratio = (out_dev["frac"] / ref_dev["frac"]) if ref_dev["frac"] > 0 else float("inf")
            band_hop = abs(_band_index(ob) - _band_index(rb)) >= 2
            gross_ratio = ratio >= DEVICE_INFLATE_RATIO or ratio <= 1 / DEVICE_INFLATE_RATIO
            if band_hop or gross_ratio:
                flags.append(
                    f"inflated device: the authored accent device is {ob} "
                    f"({out_dev['frac']:.1%} of canvas) vs the ref's {rb} "
                    f"({ref_dev['frac']:.1%}, {ratio:.1f}x) — grossly resized "
                    f"(the run-03 body-numbered miss: a small callout blown to a full-width "
                    f"accent strip).")
        else:
            # No output device overlaps / sits near the ref device's region. Is there an output
            # device of COMPARABLE SIZE anywhere else? If so it RELOCATED; if not it DROPPED.
            # This is the distinction the geometry-only ref[0]-vs-out[0] compare could not make
            # (reviewer item 3): a dropped seal vs a moved one.
            #
            # COUNT-AWARE: a "relocated" device is a 1-to-1 reassignment — the same device, moved.
            # It only holds when the output retains AT LEAST AS MANY comparable-size accent devices
            # as the ref shows. When the output has STRICTLY FEWER (the real cover-hook: the ref
            # shows several small accent devices incl. the seal, the bake has just one stray
            # remnant), at least one ref device was LOST → name DROPPED, not relocated. Without
            # this, a single surviving remnant masquerades as "the seal, relocated" and the
            # dropped seal the spec names is never reported.
            def _comparable(d: dict) -> bool:
                return (abs(_band_index(size_band(d["frac"]))
                            - _band_index(size_band(ref_dev["frac"]))) <= 1
                        and max(ref_dev["frac"], d["frac"])
                            / max(min(ref_dev["frac"], d["frac"]), 1e-9) < DEVICE_INFLATE_RATIO)
            ref_comparable_n = sum(1 for d in ref_devices if _comparable(d))
            out_comparable = [d for d in out_devices if _comparable(d)]
            similar_elsewhere = (out_devices and out_comparable
                                 and len(out_comparable) >= ref_comparable_n)
            if similar_elsewhere:
                similar_elsewhere = out_comparable[0]
                flags.append(
                    f"relocated device: the authored accent device is "
                    f"{quadrant(similar_elsewhere['cx'], similar_elsewhere['cy'])} vs the ref's "
                    f"{quadrant(ref_dev['cx'], ref_dev['cy'])} — moved out of the ref's region "
                    f"(> {DEVICE_RELOCATE_TOL:.0%} of canvas).")
            else:
                flags.append(
                    f"dropped device: the rationale declares an accent device "
                    f"({_first_accent_device_name(elements, prefer='badge')}) and ref-canonical "
                    f"shows an accent device ({size_band(ref_dev['frac'])}, "
                    f"{quadrant(ref_dev['cx'], ref_dev['cy'])}) but the built output has no "
                    f"comparable accent device — the seal/badge dropped in the bake (the run-03 "
                    f"cover-hook miss).")

    # --- (a') inflated pill — REF-INDEPENDENT (off the OUTPUT alone) -----------------------
    # The targeted body-numbered miss: the real ref-canonical carries NO recoverable accent, so
    # the ref-anchored path above never runs. Catch it from the OUTPUT: a declared accent
    # pill/callout authored as a DOMINANT (or full-width-strip) accent device, with NO small
    # contained accent counterpart in the output, is an inflated pill regardless of the ref. Only
    # fire when the ref-anchored inflated/relocated branch did NOT already account for it (avoid
    # double-flagging the same device).
    already_flagged_geom = any(f.startswith(("inflated device", "relocated device"))
                               for f in flags)
    if declares_accent_pill and not already_flagged_geom:
        inflated = next(
            (d for d in out_devices
             if size_band(d["frac"]) == "dominant"
             or d["frac"] >= AUTHORED_PILL_DOMINANT_FRAC
             or _device_spans_full_width(d)),
            None)
        # A legitimate small/contained pill in the output (matches the declared small ref form)
        # is fine — only flag when the dominant device has NO small contained sibling that would
        # explain it as the real pill (i.e. the dominant device IS the over-authored pill).
        has_small_contained = any(
            size_band(d["frac"]) in ("small", "mid") and not _device_spans_full_width(d)
            for d in out_devices)
        pill_declared_small = any(
            e["accent"] and e["kind"] in ("pill", "graphic")
            and (e.get("declared_small") or not e.get("declared_dominant", False))
            for e in elements)
        if inflated is not None and pill_declared_small and not (
                has_small_contained and not _device_spans_full_width(inflated)):
            flags.append(
                f"inflated pill: the rationale declares a small/contained accent callout pill "
                f"({_first_accent_device_name(elements, prefer='pill')}) but the built output authors a "
                f"{size_band(inflated['frac'])} accent device ({inflated['frac']:.1%} of canvas, "
                f"{quadrant(inflated['cx'], inflated['cy'])}"
                f"{', full-width strip' if _device_spans_full_width(inflated) else ''}) with no "
                f"contained pill counterpart — the small callout box blown to a full-width accent "
                f"strip (the run-03 body-numbered miss). This fires off the OUTPUT alone, so a "
                f"washed-out ref with no recoverable accent cannot hide it.")

    # --- (c) ghost display ----------------------------------------------------------------
    # A declared display word DOMINANT in the ref (a large accent field / device the display
    # is woven into) but near-absent accent in the output region = the display ghosted.
    if declares_display and ref_field is not None:
        out_dominant = (out_field is not None) or any(
            size_band(d["frac"]) == "dominant" for d in out_devices)
        if not out_dominant:
            flags.append(
                "ghost display: the rationale declares a dominant display word the ref shows "
                "woven into a dominant accent scene, but the built output has no dominant accent "
                "region — the display rendered near-absent / tiny (the run-03 cover-hook "
                "'system' ghost).")

    return flags


def _first_accent_device_name(elements: list[dict], prefer: str | None = None) -> str:
    if prefer is not None:
        for e in elements:
            if e["accent"] and e["kind"] == prefer:
                return e["name"]
    for e in elements:
        if e["accent"] and e["kind"] in ACCENT_DEVICE_KINDS:
            return e["name"]
    return "accent device"


# ---------------------------------------------------------------------------------------
# The verdict (pure — unit-tested).
# ---------------------------------------------------------------------------------------

GEOMETRY_TOLERANCE = 0.10  # HTML text may dip this far past the reserved band before flagging.


def evaluate(rationale_text: str, html: str, empty_frac: float | None,
             empty_threshold: float = 0.55, measurements: dict | None = None,
             out_regions: dict | None = None, ref_regions: dict | None = None,
             ref_border: dict | None = None, slug: str | None = None,
             metadata: dict | None = None) -> dict:
    """Combine the deterministic checks into a verdict dict.

    empty_frac: largest near-uniform region of the preview (from empty_fraction); None to
    skip the raster-fill check (no preview supplied).
    measurements: parsed _measurements.yaml ({elements:[{bbox_pct,...}]}); None to skip the
    reserved-zone geometry check (Check 7).
    out_regions / ref_regions: accent-region dicts from detect_accent_regions() for the built
    output and assets/ref-canonical.png; both None to skip the per-element ref comparator
    (Check 10) — e.g. no preview/ref supplied.
    ref_border: border-strip stats from ref_border_stats(ref-canonical) — None to skip the
    containment-vs-ref-pixels sub-check (Check 9b), e.g. no ref supplied.
    slug: the template slug (folder name) — enables Check 12 (fixed-hero mismatch, item 8):
    a slug naming a concrete object + a hero routed as per-post-regenerated = a hard fail.
    metadata: parsed _slides/<slide>/metadata.json ({PHOTO_*_PATH, PHOTO_SUBJECT, …}) —
    enables Check 13 (scene-restyle mismatch, item 9): a placeholder identity slot / generic
    PHOTO_SUBJECT with a headshot declared = a flag.
    """
    form = parse_form(rationale_text)
    blocks = parse_block_treatments(rationale_text)
    html_text_slots = parse_html_text_slots(html)
    ai_zone = has_ai_image_zone(html)
    prompt_delta = parse_prompt_delta(html)
    edit_mode = parse_pipeline_edit_mode(rationale_text)

    # Checks 1a / 4 reason about AI-integrated TEXT blocks (the docstring's "AI-integrated text
    # block"). A RASTER/photo/hero SCENE block (a blank backdrop, a full-bleed scene with no
    # on-surface text) also classifies AI_INTEGRATED but is NOT text — and such a scene legitimately
    # carries a scoped no-text negative. So exclude raster/scene blocks from the AI-TEXT count; only
    # genuine AI-placed text counts. (NB: a list BAKED onto a surface IS AI-placed text — its block
    # is "AI-integrated", carries no raster/scene hint, and so is correctly counted: Check 4 then
    # forbids a blanket no-text clause over the very list the bake must render.)
    def _is_raster_block(b: dict) -> bool:
        blob = (b.get("block", "") + " " + b.get("treatment", "")).lower()
        return any(h in blob for h in RASTER_HINTS) or "scene" in blob or "panel" in blob
    n_ai = sum(1 for b in blocks if b["category"] == AI_INTEGRATED and not _is_raster_block(b))
    n_html = sum(1 for b in blocks if b["category"] == HTML_OVERLAY)

    flags: list[str] = []

    # --- Check 1: treatment-category presence ---
    # 1a: AI-integrated text declared but NO image zone in the output -> it came out flat HTML.
    if n_ai > 0 and not ai_zone:
        flags.append(
            f"rationale declares {n_ai} AI-integrated text block(s) but template.html has no "
            f"[ai-image-zone] — the integrated/occluded text came out as a flat HTML box "
            f"instead of in the image")
    # 1b: HTML-overlay declared but NO content text data-slot exists -> the box never shipped.
    if n_html > 0 and len(html_text_slots) == 0:
        flags.append(
            f"rationale declares {n_html} HTML-overlay text block(s) but template.html has no "
            f"content text data-slot — the isolable HTML box(es) did not ship")

    # --- Check 2: raster-zone-filled (fold 2a) ---
    if declares_filled_raster(rationale_text) and empty_frac is not None:
        if empty_frac >= empty_threshold:
            flags.append(
                f"rationale declares a filled raster zone (photo/cutout/hero, filled every "
                f"post) but the preview's largest near-uniform region is "
                f"{empty_frac:.0%} >= {empty_threshold:.0%} — it shipped as an empty grey "
                f"placeholder, not a filled image (the body-numbered failure)")

    # --- Check 3: B1 surface-reuse (fold 2b) ---
    if form == "B1" and declares_surface_reuse(rationale_text):
        # surface text must be AI-placed: an AI image zone must exist. Pure-HTML-text output
        # (text slots present, no AI zone) means the surface was not reused.
        if not ai_zone and len(html_text_slots) > 0:
            flags.append(
                "B1 rationale says reuse the in-scene surface, but the output is pure HTML "
                "text with no AI image zone — the text was floated/regenerated instead of "
                "placed on the existing surface (the body-statement miss)")

    # --- Check 4: prompt_delta contradicts a declared AI-integrated text treatment (r01) ---
    # The rationale declared text as AI-integrated/occluded, but the prompt_delta forbids
    # text wholesale ("No text, no lettering, no captions") → the model has nothing to
    # occlude and free-styles. The "no text" clause must apply ONLY to HTML-assigned blocks.
    if n_ai > 0 and prompt_delta and NO_TEXT_CLAUSE_RE.search(prompt_delta):
        flags.append(
            f"rationale declares {n_ai} AI-integrated text block(s) but the prompt_delta "
            f"contains a blanket no-text clause — the model is told NOT to render the very "
            f"text the rationale said to integrate/occlude (the r01 contradiction). The "
            f"prompt must DESCRIBE the AI-integrated text and forbid text only for the blocks "
            f"the rationale assigned to HTML.")

    # --- Check 5: B1 reuse-surface but total-recompose (r02) ---
    # total-recompose re-synthesizes the whole scene → it repaints a lookalike surface
    # instead of reusing the ref's. A B1 that declares "reuse the surface" must preserve it.
    if form == "B1" and declares_surface_reuse(rationale_text) and TOTAL_RECOMPOSE_RE.search(edit_mode):
        flags.append(
            "B1 rationale says reuse the in-scene surface, but the pipeline edit_mode is "
            "total-recompose — that regenerates a lookalike surface instead of reusing the "
            "ref's (the r02 miss). B1 must clean+reserve the existing surface and place the "
            "text onto it, never total-recompose.")

    # --- Check 6: isolable text block declared AI-integrated (r07) ---
    # caption/CTA/byline/badge/label are isolable → the brand hard-rule keeps them HTML;
    # declaring one AI-integrated bakes it into the image (the r07 violation).
    baked_isolable = [b for b in blocks if b["category"] == AI_INTEGRATED
                      and any(h in b["block"].lower() for h in ISOLABLE_TEXT_NAME_HINTS)]
    if baked_isolable:
        names = ", ".join(b["block"] or "?" for b in baked_isolable)
        flags.append(
            f"isolable text block(s) declared AI-integrated ({names}) — caption/CTA/byline/"
            f"badge/label/handle are isolable and MUST be HTML overlay, never baked into the "
            f"image (brand hard-rule; the r07 failure). Only genuinely-integrated text (e.g. "
            f"an occluded headline HTML can't occlude) may be AI.")

    # --- Check 7: reserved-zone geometry mismatch (r03) ---
    # The prompt reserves an upper band for HTML text, but the HTML zones occupy further down
    # → the text lands on the busy scene below the reserved band (a contrast gamble). A single
    # reserved-zone % must be shared by the prompt_delta and the HTML.
    if measurements is not None and prompt_delta:
        reserved = parse_reserved_band_pct(prompt_delta)
        occupied = html_text_bottom_extent(measurements)
        if reserved is not None and occupied is not None and occupied > reserved + GEOMETRY_TOLERANCE:
            flags.append(
                f"reserved-zone geometry mismatch: the prompt_delta reserves the upper "
                f"{reserved:.0%} for text but the HTML text zones occupy down to "
                f"{occupied:.0%} (> {GEOMETRY_TOLERANCE:.0%} past the band) — the text will "
                f"collide with the busy scene below the reserved zone (the r03 collision). "
                f"Use a SINGLE reserved-zone % shared by the prompt_delta and the HTML.")

    # --- Check 8: scrim-vs-ref (SPEC-L1, run-02 INVENTA) ---
    # The rationale declared the ref resolves legibility by NATURAL composition (no band), but
    # template.html authors a full-width opaque band (`.bottom-scrim`-style div) anyway → the
    # builder stamped a band the ref does not have. A band is authored ONLY for `ref-band`.
    if NATURAL_COMPOSITION_RE.search(rationale_text) and html_has_opaque_fullwidth_band(html):
        flags.append(
            "scrim-vs-ref mismatch: rationale declares legibility-method=natural-composition "
            "(the ref has NO band) but template.html authors a full-width opaque band "
            "(>=45% alpha, >=20% canvas height) — a scrim the ref does not show (the run-02 "
            "INVENTA miss). Either reproduce the ref's natural dark zone in the bg prompt_delta "
            "and drop the scrim div, or — if the ref genuinely shows a band — declare "
            "legibility-method=ref-band.")

    # --- Check 9: containment-vs-ref (SPEC-L1, run-02 REMONTA) ---
    # The rationale declared the ref's image zone is a CONTAINED rectangle, but the authored
    # image zone is full-bleed (covers the whole canvas) → the builder re-framed the ref
    # (the ref-07 full-bleed-face miss). Containment is binding.
    if CONTAINED_RECT_RE.search(rationale_text) and html_image_zone_is_full_bleed(html):
        flags.append(
            "containment-vs-ref mismatch: rationale declares containment=contained-rectangle "
            "but the authored image zone is full-bleed (covers the full canvas) — the contained "
            "ref was blown up to a full-bleed scene (the run-02 REMONTA miss, ref-07). "
            "Containment is binding: a contained-rectangle ref builds a bounded image zone.")

    # --- Check 9b: containment claim vs REF PIXELS (SPEC-r5g) -------------------------------
    # Check 9 is self-consistency — a hallucinated contained-rectangle read passes it. 9b
    # validates the claim against ref-canonical's own border strips: a genuinely contained
    # photo sits on a near-uniform mat; scene texture at the edges = the read is wrong.
    if ref_border is not None and CONTAINED_RECT_RE.search(rationale_text):
        misread = containment_misread(ref_border)
        if misread:
            flags.append(
                f"containment-misread (vs ref pixels): rationale declares "
                f"containment=contained-rectangle, but ref-canonical's border strips read as "
                f"scene-texture continuation — {misread}. A genuinely contained photo sits on "
                f"a near-uniform mat at all four edges. The ref is FULL-BLEED; "
                f"contained-rectangle is a misread (the run-06 numbered-photo-callout "
                f"hallucination: a paper mat invented on a full-bleed teal-water ref). "
                f"RE-READ the ref and redo the §1 tree walk (Q3) before re-building — do not "
                f"patch the HTML to match the wrong read.")

    # --- Check 11: undeclared visible elements (SPEC-r5g, bidirectional Check B) ------------
    # The reverse direction of Checks 1-10: an element the rationale never declared must not
    # ship (the run-06 monitor-surface DECORATIVE_WORD ghost, injected to appease the font
    # gate). Every content data-slot needs a §2 block; pure chrome is excluded.
    for slot in find_undeclared_slots(rationale_text, html):
        flags.append(
            f"undeclared visible element: template.html ships content data-slot '{slot}' with "
            f"no corresponding block in rationale §2 (the run-06 monitor-surface "
            f"DECORATIVE_WORD ghost — a visible element added to appease a gate). Every "
            f"visible content element must be DECLARED in §2 with a treatment before it "
            f"ships: either add the §2 block (with treatment + why) or remove the element. "
            f"Never add visible elements the rationale did not reason about.")

    # --- Check 10: per-element ref-vs-output fidelity (SPEC-r3) -----------------------------
    # Compare each declared distinctive element (badge/seal, callout pill, accent graphic,
    # display word) between the BUILT OUTPUT and assets/ref-canonical.png by coarse accent
    # region detection: a dropped seal, an inflated/relocated pill, or a ghosted display all
    # hard-fail. Runs only when both region sets were supplied (a preview + a ref).
    elements = parse_distinctive_elements(rationale_text)
    if out_regions is not None and ref_regions is not None:
        flags.extend(compare_elements_to_ref(elements, out_regions, ref_regions))

    # --- Check 12: fixed-hero mismatch (SPEC-r6g item 8, HARD FAIL) -------------------------
    # The hero object IS the identity (the slug names a concrete object), but the rationale
    # routed it as a per-post AI-regenerated subject instead of recoloring the ref → the object
    # drifts category (the run-07 chain → gears). Needs the slug to know the object-identity.
    obj_noun = slug_object_noun(slug)
    if obj_noun is not None and hero_is_regenerated_per_post(rationale_text):
        flags.append(
            f"fixed-hero mismatch: the template slug names a concrete object ('{obj_noun}') so "
            f"the hero IS the brand identity, but the rationale routes it as a per-post "
            f"AI-regenerated subject (the per-post variation axis) instead of RECOLORING the "
            f"ref's '{obj_noun}' — the object-identity drifts category (the run-07 "
            f"highlight-headline miss: the chain became gears). When the hero is the identity, "
            f"FIX the subject (keep the ref's '{obj_noun}', vary only framing/angle/lighting) — "
            f"do not regenerate it per post. Inegociável: the object-identity must not change "
            f"category.")

    # --- Check 13: scene-restyle mismatch (SPEC-r6g item 9, FLAG) ---------------------------
    # A hero face + a brand headshot, but the build left the identity slot a PLACEHOLDER string
    # and/or PHOTO_SUBJECT a generic person description → the generator drew a random face
    # instead of the brand person (the run-07 creator-cover-cta miss). Reads metadata.json.
    if metadata is not None and face_is_hero(rationale_text) and headshot_declared(
            rationale_text, html, metadata):
        slot = metadata_slot_value(metadata, IDENTITY_SLOT_KEY_RE)
        subj = metadata.get("PHOTO_SUBJECT") if isinstance(
            metadata.get("PHOTO_SUBJECT"), str) else None
        reasons: list[str] = []
        if slot is not None and is_placeholder_path(slot[1]):
            reasons.append(
                f"the identity slot '{slot[0]}' is a placeholder ('{slot[1].strip()[:60]}'), "
                f"never resolved to the headshot path")
        if subj is not None and GENERIC_PERSON_RE.search(subj) and not re.search(
                r"\b(simon|the brand person|brand headshot)\b", subj, re.IGNORECASE):
            reasons.append(
                f"PHOTO_SUBJECT is a generic person description ('{subj.strip()[:60]}') — what "
                f"the generator consumes, so it invents a face")
        if reasons:
            flags.append(
                "scene-restyle mismatch (hero face ≠ brand identity): " + "; ".join(reasons)
                + ". A brand headshot is declared, so the hero face must DERIVE from it "
                "(restyled to the medium), never be invented. Resolve the identity slot to the "
                "headshot path at build time and describe the brand person (not a generic "
                "person) in PHOTO_SUBJECT. Inegociável when a headshot is declared and the build "
                "did not honor it. (Limit: this catches placeholder/generic deterministically; "
                "whether the identity survives heavy stylization is the owner's eye.)")

    # --- Check 14: seal/logo provenance (SPEC-r6g item 6, HARD FAIL on destructive CSS) -----
    # A colored logo killed by `filter:invert`/`brightness(0)`, or a serrated/starburst seal
    # approximated as a CSS disc (`border-radius:50%`) — both destroy the mark (the run-07
    # one-page / numbered-photo badge misses).
    flags.extend(seal_provenance_flags(html, rationale_text))

    # --- Check 15: static hero src (D1, studio-sweep) --------------------------------------
    # A post-subject AI image element bound by a literal `_ai_bg/…` path instead of the
    # `{{…_PATH}}` Mustache placeholder — render-time substitution can't reach a static src,
    # so every post ships the template's demo background.
    flags.extend(static_hero_src_flags(html))

    ok = not flags
    return {
        "ok": ok,
        "form": form,
        "n_ai_blocks": n_ai,
        "n_html_blocks": n_html,
        "html_text_slots": html_text_slots,
        "ai_zone": ai_zone,
        "empty_fraction": empty_frac,
        "edit_mode": edit_mode,
        "prompt_delta_present": bool(prompt_delta),
        "distinctive_elements": elements,
        "slug_object_noun": obj_noun,
        "flags": flags,
        "reason": "output matches declared treatments" if ok else "; ".join(flags),
    }


# Accent resolution chain (Check 10's device-color source): (a) explicit --accent;
# (b) auto-discovered brand tokens — walk UP from the template/rationale path to an ancestor
# carrying brand_context/visual-identity/tokens.json and read colors.accent; (c) the legacy
# coral default, with a stderr WARN (a wrong accent silently blinds the comparator).
TOKENS_ACCENT_KEYS = ("accent", "primary_accent", "primary-accent")


def _accent_from_tokens(tokens_path: Path) -> str | None:
    """colors.accent (or a primary-accent variant) from a tokens.json, validated; None if absent."""
    try:
        data = json.loads(tokens_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    colors = data.get("colors") or {}
    for key in TOKENS_ACCENT_KEYS:
        val = colors.get(key)
        if isinstance(val, str):
            try:
                _hex_to_rgb(val)
            except ValueError:
                continue
            return val
    return None


def resolve_accent(cli_accent: str | None, *anchors: Path) -> tuple[str, str]:
    """Resolve the brand accent for the Check 10 device-pixel classifier.

    Returns (accent_hex, source) where source ∈ {"--accent", "<tokens.json path>", "default"}.
    Chain: explicit --accent > brand_context/visual-identity/tokens.json auto-discovered by
    walking up from each anchor path (template.html, rationale.md) > DEFAULT_ACCENT_HEX with
    a stderr WARN. Raises ValueError on a malformed --accent."""
    if cli_accent:
        _hex_to_rgb(cli_accent)  # validate — raises ValueError on junk
        return cli_accent, "--accent"
    for anchor in anchors:
        if anchor is None:
            continue
        for anc in anchor.resolve().parents:
            candidates = [anc / "brand_context" / "visual-identity" / "tokens.json"]
            if anc.name == "brand_context":
                candidates.insert(0, anc / "visual-identity" / "tokens.json")
            for tok in candidates:
                if tok.is_file():
                    accent = _accent_from_tokens(tok)
                    if accent is not None:
                        return accent, str(tok)
    print("  WARN: accent not resolved; using coral default "
          f"({DEFAULT_ACCENT_HEX}) — pass --accent or ensure "
          "brand_context/visual-identity/tokens.json (colors.accent) is reachable from the "
          "template/rationale path", file=sys.stderr)
    return DEFAULT_ACCENT_HEX, "default"


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(description="Check B — treatment-contract gate.")
    ap.add_argument("--rationale", required=True, type=Path)
    ap.add_argument("--template-html", required=True, type=Path)
    ap.add_argument("--preview", type=Path, default=None,
                    help="rendered preview.png (enables the raster-zone-filled check)")
    ap.add_argument("--measurements", type=Path, default=None,
                    help="_measurements.yaml (enables the reserved-zone geometry check, Check 7)")
    ap.add_argument("--ref", type=Path, default=None,
                    help="ref-canonical.png to compare the built output against (Check 10). "
                         "Defaults to <template-dir>/assets/ref-canonical.png next to template.html.")
    ap.add_argument("--accent", type=str, default=None,
                    help="brand accent color as #rrggbb for the Check 10 device detector. "
                         "Default: auto-discovered from brand_context/visual-identity/"
                         "tokens.json (colors.accent) walking up from --template-html/"
                         "--rationale; coral fallback with a WARN if unresolved.")
    ap.add_argument("--empty-threshold", type=float, default=0.55)
    ap.add_argument("--slug", type=str, default=None,
                    help="template slug (folder name) for Check 12 (fixed-hero mismatch, item "
                         "8). Default: the template dir name (parent of template.html).")
    ap.add_argument("--metadata", type=Path, default=None,
                    help="_slides/<slide>/metadata.json for Check 13 (scene-restyle mismatch, "
                         "item 9). Default: auto-discovered at <template-dir>/_slides/*/"
                         "metadata.json.")
    args = ap.parse_args()

    if not args.rationale.exists():
        print(f"Error: rationale not found: {args.rationale}", file=sys.stderr)
        return 1
    if not args.template_html.exists():
        print(f"Error: template.html not found: {args.template_html}", file=sys.stderr)
        return 1

    rationale_text = args.rationale.read_text(encoding="utf-8")
    html = args.template_html.read_text(encoding="utf-8")

    try:
        accent_hex, accent_source = resolve_accent(args.accent, args.template_html,
                                                   args.rationale)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if accent_source != "default":
        print(f"  note: accent {accent_hex} ({accent_source})", file=sys.stderr)

    empty_frac = None
    out_regions = None
    if args.preview and args.preview.exists():
        preview_img = Image.open(args.preview).convert("RGB")
        empty_frac = empty_fraction(np.array(preview_img))
        out_regions = detect_accent_regions(preview_img, accent_hex)

    measurements = None
    if args.measurements and args.measurements.exists():
        import yaml  # local import: only needed for the optional geometry check
        measurements = yaml.safe_load(args.measurements.read_text(encoding="utf-8")) or {}

    # Resolve the ref (explicit --ref, else <template-dir>/assets/ref-canonical.png).
    # Check 9b (containment vs ref pixels) needs only the ref; Check 10 (per-element
    # comparator) needs the ref AND a built preview to compare it against.
    ref_path = args.ref or (args.template_html.parent / "assets" / "ref-canonical.png")
    ref_img = Image.open(ref_path).convert("RGB") if ref_path.exists() else None
    ref_border = ref_border_stats(ref_img) if ref_img is not None else None
    ref_regions = None
    if out_regions is not None:
        if ref_img is not None:
            ref_regions = detect_accent_regions(ref_img, accent_hex)
        else:
            print(f"  note: ref-canonical not found ({ref_path}) — Check 10 skipped",
                  file=sys.stderr)
            out_regions = None  # nothing to compare against → skip Check 10 cleanly
    if ref_img is None:
        print(f"  note: ref-canonical not found ({ref_path}) — Check 9b skipped",
              file=sys.stderr)

    # Slug (Check 12): explicit --slug, else the template dir name (template.html's parent).
    slug = args.slug or args.template_html.resolve().parent.name

    # Metadata (Check 13): explicit --metadata, else auto-discover the first
    # <template-dir>/_slides/*/metadata.json (the slot fills the generator consumed).
    metadata = None
    meta_path = args.metadata
    if meta_path is None:
        slides_dir = args.template_html.parent / "_slides"
        if slides_dir.is_dir():
            cands = sorted(slides_dir.glob("*/metadata.json"))
            meta_path = cands[0] if cands else None
    if meta_path is not None and meta_path.exists():
        try:
            metadata = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            print(f"  note: metadata.json unreadable ({meta_path}) — Check 13 skipped",
                  file=sys.stderr)
    elif args.metadata is not None:
        print(f"  note: metadata not found ({args.metadata}) — Check 13 skipped",
              file=sys.stderr)

    res = evaluate(rationale_text, html, empty_frac, args.empty_threshold, measurements,
                   out_regions=out_regions, ref_regions=ref_regions, ref_border=ref_border,
                   slug=slug, metadata=metadata)

    print(f"Check B — treatment-contract on {args.rationale.name}:")
    print(f"  form={res['form'] or '?'}  ai_blocks={res['n_ai_blocks']}  "
          f"html_blocks={res['n_html_blocks']}  ai_zone={res['ai_zone']}  "
          f"html_text_slots={len(res['html_text_slots'])}  edit_mode={res['edit_mode'] or '?'}")
    if res["empty_fraction"] is not None:
        print(f"  empty_fraction={res['empty_fraction']:.3f}")
    print(f"  verdict = {'PASS' if res['ok'] else 'MISMATCH'} — {res['reason']}")

    if res["ok"]:
        return 0
    for f in res["flags"]:
        print(f"[mismatch] {f}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())

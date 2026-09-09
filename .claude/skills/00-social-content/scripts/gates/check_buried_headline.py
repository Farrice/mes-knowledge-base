#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check I — the BURIED-HEADLINE gate (r8-no-buried-headline).

Sibling of check_treatment_contract.py / check_form_vs_ref.py / dead_space.py. Runs at the
QUALITY GATE (Step 6), reads ONLY template.html (pure geometry/z-index — no pixels, no model).

THE ANTI-PATTERN IT BANS (run-09 preview-cards-cover). The builder authored an HTML display
HEADLINE (a real editable `data-slot="HEADLINE"` text node) at a LOW z-index and placed an
OPAQUE AI image zone (the card cluster, `data-slot="PHOTO_MAIN" data-zone="photo"`) at a HIGHER
z-index ON TOP of it, intending the image to "weave" over the letterforms. But an edit-from-ref
AI image is an OPAQUE rectangle (GPT edit mode strips transparency — see the `gpt-edit-transparent`
spec): so the headline is BURIED under the image in the bake (reads "came as an image", with image
seams) AND in the Studio editor the text is occluded at its click point → it is no longer a
selectable, editable text layer. The headline behaves like an image.

THE RULE (general craft, NO slug, NO per-template constant):
  An HTML TEXT data-slot must NEVER sit UNDERNEATH an OPAQUE AI/photo image zone whose bounding
  box intersects the text zone. A text slot stays visually on top / in a clear zone and remains an
  editable text layer.

THE GEOMETRY THIS FLAGS:
  a TEXT data-slot zone whose effective z-index is STRICTLY LOWER than an OVERLAPPING
  photo / AI-image zone, AND the image zone is OPAQUE (not a transparent-bg cutout, no
  honored `mix-blend-mode`). That is the buried-headline anti-pattern → FLAG (exit 2).

THE TRANSPARENCY EXCEPTION (the ONLY way an AI element may overlap HTML type — the "woven"
composition): the AI element is a TRANSPARENT-BACKGROUND CUTOUT occluding ONLY its own region.
Transparency is unreliable from GPT edit mode, so it must be DECLARED on the image zone for the
exception to apply (a `data-transparent`/`data-cutout` marker, or a HONORED non-`normal`
`mix-blend-mode` actually authored in the CSS — a blend mode merely promised in the rationale but
not authored is the declared-but-not-honored gap, and does NOT earn the exception). When the
exception does not apply the text MUST NOT be occluded by the image at all (place the headline
clear of the image's bounding box).

The clean reference pattern (numbered-statement-body / fullbleed-overlay-cover): a full-bleed
photo `.bg` at z-index 0 with the text zones at z-index 10/20 ON TOP — text z > photo z → PASS
(`template-conventions.md` #9: a depth-illusion text zone gets z-index 10 OVER the fg subject).

Exit codes:
  0  -> PASS (no buried text slot).
  2  -> FLAG: at least one editable text slot is buried under an opaque image zone.
  1  -> usage / file-not-found error.

Usage:
    uv run check_buried_headline.py --template-html <dir>/template.html
"""
import argparse
import re
import sys
from pathlib import Path


def _force_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# data-slot name tokens that are NOT editable content TEXT (image / chrome slots). A text slot
# is anything with a data-slot that is not one of these — display words, headlines, body, etc.
NON_TEXT_SLOT_HINTS = ("photo", "image", "img", "bg", "background", "logo", "badge", "icon",
                       "mark", "wordmark", "_path", "src", "seal", "starburst", "emblem",
                       "masthead", "pagination", "dots")
# A DISPLAY/HEADLINE text slot — the most damaging to bury (the run-09 case). Used only to
# sharpen the flag message; the rule applies to ANY text slot, headline or not.
DISPLAY_SLOT_HINTS = ("headline", "display", "hero", "title", "secondary", "kicker")
# Selector / class / id / data-zone signals that a zone is a photo / AI-image raster zone.
PHOTO_SELECTOR_HINTS = ("photo-zone", "photo_zone", "photozone", "photo-main", "photo-",
                        "ai-image", "ai-zone", "hero-photo", "scene")
# A transparent-background cutout marker authored on the image zone (earns the woven exception).
TRANSPARENT_ATTR_RE = re.compile(
    r'data-(?:transparent|cutout|alpha)\s*=\s*["\']?\s*(?:true|1|yes|cutout|transparent)',
    re.IGNORECASE)
# A non-`normal` mix-blend-mode actually authored (HONORED) — also earns the exception.
BLEND_MODE_RE = re.compile(
    r"mix-blend-mode\s*:\s*(multiply|screen|overlay|darken|lighten|color-burn|"
    r"color-dodge|hard-light|soft-light|difference|exclusion|hue|saturation|color|luminosity)",
    re.IGNORECASE)


def parse_style_blocks(html: str) -> dict[str, str]:
    """Map a CSS class name -> its concatenated rule-body text, from the <style> region.

    Coarse (no full CSS engine): for each `selector { body }` rule, attribute the body to every
    `.class` token in the selector. Later rules for the same class APPEND (cascade-ish). This is
    the same altitude as check_treatment_contract.py's CSS rule scan."""
    out: dict[str, str] = {}
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", html):
        selector, body = m.group(1), m.group(2)
        # A selector may be a comma list; for each, attribute the body ONLY to classes in its
        # RIGHTMOST (key) compound segment — so a descendant rule like `.photo-zone img {...}`
        # does NOT pollute `.photo-zone` itself (the img sub-rule must not become the zone bbox).
        for sub in selector.split(","):
            key_seg = re.split(r"\s+|>|\+|~", sub.strip())[-1]
            for cls in re.findall(r"\.([A-Za-z_][\w-]*)", key_seg):
                out[cls] = out.get(cls, "") + ";" + body
    return out


def _decl(style: str, prop: str) -> str | None:
    """Last value of CSS declaration `prop` in a style string (semicolon-separated), or None."""
    val = None
    for m in re.finditer(re.escape(prop) + r"\s*:\s*([^;{}]+)", style, re.IGNORECASE):
        val = m.group(1).strip()
    return val


def _pct(value: str | None) -> float | None:
    """Parse a percentage value (e.g. '8%', '28 %') to a float fraction-of-100, else None."""
    if not value:
        return None
    m = re.search(r"(-?\d+(?:\.\d+)?)\s*%", value)
    return float(m.group(1)) if m else None


class Zone:
    """One positioned element: its combined style, role, z-index and bbox (in % of canvas)."""

    def __init__(self, name: str, style: str, slot: str | None, data_zone: str | None,
                 has_img: bool, raw_tag: str):
        self.name = name
        self.style = style
        self.slot = slot
        self.data_zone = (data_zone or "").lower()
        self.has_img = has_img
        self.raw_tag = raw_tag
        self.z = self._z()
        self.bbox = self._bbox()  # (left, top, width, height) in %  OR None when not positioned

    def _z(self) -> int:
        z = _decl(self.style, "z-index")
        if z is None:
            return 0  # CSS default auto ~ 0 for positioned siblings (convention #9: default zones)
        m = re.search(r"-?\d+", z)
        return int(m.group(0)) if m else 0

    def _bbox(self) -> tuple[float, float, float, float] | None:
        s = self.style.replace(" ", "")
        if re.search(r"inset:0(?:px|%)?(?:;|$)", s) or "inset:0;" in s:
            return (0.0, 0.0, 100.0, 100.0)
        left, top = _pct(_decl(self.style, "left")), _pct(_decl(self.style, "top"))
        right, bottom = _pct(_decl(self.style, "right")), _pct(_decl(self.style, "bottom"))
        w, h = _pct(_decl(self.style, "width")), _pct(_decl(self.style, "height"))
        # Full-bleed via left:0;right:0;top:0;bottom:0
        if left == 0 and right == 0 and top == 0 and bottom == 0:
            return (0.0, 0.0, 100.0, 100.0)
        # Derive missing left/top from right/bottom + width/height when possible.
        if left is None and right is not None and w is not None:
            left = 100.0 - right - w
        if top is None and bottom is not None and h is not None:
            top = 100.0 - bottom - h
        if left is None or top is None:
            return None
        if w is None:
            w = (100.0 - right - left) if right is not None else 100.0
        if h is None:
            h = (100.0 - bottom - top) if bottom is not None else 100.0
        return (left, top, max(0.0, w), max(0.0, h))

    # ---- role classification --------------------------------------------------------------
    def is_text_slot(self) -> bool:
        if not self.slot:
            return False
        sl = self.slot.lower()
        if any(h in sl for h in NON_TEXT_SLOT_HINTS):
            return False
        if self.has_img:           # an <img>-bearing zone is not a text slot
            return False
        if self.data_zone == "photo":
            return False
        return True

    def is_display_text(self) -> bool:
        sl = (self.slot or "").lower()
        nm = (self.name or "").lower()
        return any(h in sl or h in nm for h in DISPLAY_SLOT_HINTS)

    def is_photo_zone(self) -> bool:
        if self.data_zone == "photo":
            return True
        blob = (self.name + " " + (self.slot or "") + " " + self.raw_tag).lower()
        if self.has_img and any(h in blob for h in PHOTO_SELECTOR_HINTS):
            return True
        if self.has_img and self.slot and any(h in self.slot.lower()
                                              for h in ("photo", "image", "hero")):
            return True
        return any(h in blob for h in PHOTO_SELECTOR_HINTS) and self.has_img

    def is_opaque(self) -> bool:
        """The image zone is OPAQUE (no transparency exception). It is NON-opaque (exempt) ONLY
        when a transparent-cutout marker is declared OR a non-normal mix-blend-mode is authored."""
        if TRANSPARENT_ATTR_RE.search(self.raw_tag):
            return False
        if BLEND_MODE_RE.search(self.style):
            return False
        return True


def bbox_overlap(a: tuple[float, float, float, float],
                 b: tuple[float, float, float, float]) -> float:
    """Intersection area of two (l,t,w,h) % boxes, as a fraction of the SMALLER box. 0 = none."""
    al, at, aw, ah = a
    bl, bt, bw, bh = b
    ix = max(0.0, min(al + aw, bl + bw) - max(al, bl))
    iy = max(0.0, min(at + ah, bt + bh) - max(at, bt))
    inter = ix * iy
    if inter <= 0:
        return 0.0
    smaller = min(aw * ah, bw * bh)
    return inter / smaller if smaller > 0 else 0.0


# Minimum bbox overlap (fraction of the smaller box) to count the image as covering the text.
MIN_OVERLAP = 0.10


def parse_zones(html: str) -> list[Zone]:
    """Parse every positioned element (with a class or data-slot or data-zone) into a Zone."""
    class_styles = parse_style_blocks(html)
    zones: list[Zone] = []
    # Match opening tags of div/section/span/img-bearing containers that carry class/data-*/style.
    for m in re.finditer(r"<(div|section|span|figure)\b([^>]*)>", html, re.IGNORECASE):
        attrs = m.group(2)
        classes = re.findall(r"class\s*=\s*[\"']([^\"']*)[\"']", attrs)
        class_list = classes[0].split() if classes else []
        slot_m = re.search(r"data-slot\s*=\s*[\"']([^\"']+)[\"']", attrs)
        zone_m = re.search(r"data-zone\s*=\s*[\"']([^\"']+)[\"']", attrs)
        inline_m = re.search(r"style\s*=\s*[\"']([^\"']*)[\"']", attrs)
        inline = inline_m.group(1) if inline_m else ""
        if not (class_list or slot_m or zone_m or inline):
            continue
        combined = ";".join(class_styles.get(c, "") for c in class_list) + ";" + inline
        # Detect an <img> that belongs to THIS element: scan the tail only up to the next
        # block boundary (a child/sibling <div|section|figure ...> open OR a </...> close) so a
        # later sibling's <img> does not bleed in (the headline-then-photo false positive).
        tail = html[m.end(): m.end() + 600]
        boundary = re.search(r"<(?:div|section|figure)\b|</(?:div|section|figure)>", tail,
                             re.IGNORECASE)
        scope = tail[: boundary.start()] if boundary else tail
        has_img = bool(re.search(r"<img\b", scope, re.IGNORECASE))
        name = " ".join(class_list) or (slot_m.group(1) if slot_m else "?")
        zones.append(Zone(
            name=name, style=combined,
            slot=slot_m.group(1) if slot_m else None,
            data_zone=zone_m.group(1) if zone_m else None,
            has_img=has_img,
            raw_tag="<" + m.group(1) + attrs + ">"))
    return zones


def find_buried(zones: list[Zone]) -> list[dict]:
    """Return one flag dict per (text_slot, opaque_photo_zone) buried pair."""
    texts = [z for z in zones if z.is_text_slot() and z.bbox is not None]
    photos = [z for z in zones if z.is_photo_zone() and z.bbox is not None]
    flags: list[dict] = []
    for t in texts:
        for p in photos:
            if p.z <= t.z:                       # text is at or above the image → safe
                continue
            ov = bbox_overlap(t.bbox, p.bbox)
            if ov < MIN_OVERLAP:                 # no meaningful intersection → safe
                continue
            if not p.is_opaque():                # declared transparent-cutout / honored blend → exempt
                continue
            flags.append({
                "text_slot": t.slot, "text_z": t.z, "is_display": t.is_display_text(),
                "photo": p.name, "photo_slot": p.slot, "photo_z": p.z,
                "overlap": ov})
    return flags


def evaluate(html: str) -> tuple[bool, list[dict]]:
    """(passed, flags). passed=True when no editable text slot is buried under an opaque image."""
    return (lambda f: (not f, f))(find_buried(parse_zones(html)))


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(description="Check I — buried-headline gate (r8).")
    ap.add_argument("--template-html", required=True, type=Path)
    args = ap.parse_args()
    if not args.template_html.is_file():
        print(f"[error] template.html not found: {args.template_html}", file=sys.stderr)
        return 1
    html = args.template_html.read_text(encoding="utf-8", errors="replace")
    passed, flags = evaluate(html)
    if passed:
        print("[pass] check_buried_headline: no editable text slot is buried under an "
              "opaque image zone.")
        return 0
    for f in flags:
        kind = "DISPLAY/headline" if f["is_display"] else "text"
        print(
            f"[FLAG] buried {kind} slot '{f['text_slot']}' (z-index {f['text_z']}) sits UNDER "
            f"the opaque image zone '{f['photo_slot'] or f['photo']}' (z-index {f['photo_z']}, "
            f"overlap {f['overlap']*100:.0f}% of the text box). An opaque AI/photo image baked "
            f"on top BURIES the headline (reads as an image, not editable). Place the text ON TOP "
            f"(higher z-index) or CLEAR of the image bbox; the woven overlap is allowed ONLY for a "
            f"declared transparent-cutout image (data-cutout) or a HONORED mix-blend-mode.",
            file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

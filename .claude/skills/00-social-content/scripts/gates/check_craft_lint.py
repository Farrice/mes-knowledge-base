#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Craft-LINT — the type-craft layer ABOVE the overflow gate (r7-html-craft, RC-B).

Sibling of measure_text_contrast.py / dead_space.py / check_treatment_contract.py /
compare_render_to_ref.py. Runs AT THE QUALITY GATE (Step 6), post-bake. ADVISORY by
default (warns + surfaces for the human — the project's "gate WARNS on judgment" posture,
same as the palette flag and the image-medium conference); pass --enforce to make it block
and feed the 3-try ladder.

WHY THIS LAYER EXISTS — the class the existing gates structurally cannot see
----------------------------------------------------------------------------
The overflow gate (compare_render_to_ref.py) only fires when text spills the CANVAS; the
autosize net (render_template.py) only shrinks text that overflows its OWN box. Every defect
in scope here is "ugly-but-fits" or "cross-zone collision" — neither is a pixel-overflow
event, so neither gate ever fires:

  - a 3.2cqw body under a 19cqw display (6:1 ratio) is a stranded footnote — but it FITS;
  - negative letter-spacing + line-height < 1.0 on a multi-line CONDENSED display crams the
    glyphs until they collide — but the box still HOLDS the text;
  - a display stack with no height cap runs down into the image subject below it — a
    CROSS-ZONE collision, not a self-box overflow;
  - line-height that is too loose leaves an airy footnote feel ("espaçamentos muito altos")
    — perfectly within the box.

These are TYPOGRAPHY CRAFT defects, measurable deterministically from the authored CSS, not
from the rendered canvas overflow. This lint reads the per-zone `font-size` / `line-height` /
`letter-spacing` declarations in template.html (all in `cqw`, the canvas-relative unit the
craft rules mandate) and measures the five generalizable craft rules from html-craft.md:

  1. DISPLAY:BODY RATIO out of range — the hierarchy is either flat (ratio too low) or the
     body is a footnote under a giant display (ratio too high). Rule §5: ratio <= ~4:1.
  2. BODY BELOW MIN cqw — an under-scaled body reads as a footnote on a 1080-wide canvas.
     Rule §5: body >= ~4cqw (a tighter floor than §3's legacy 3.2cqw — RC-B raised it).
  3. EXCESSIVE LINE-HEIGHT / whitespace — "diminuir entrelinha, aumentar fonte": display
     line-height should sit ~0.95-1.10, body ~1.2-1.5; above the band reads airy/dead.
  4. NEGATIVE TRACKING ON MULTI-LINE CONDENSED DISPLAY — a condensed face (Anton, etc.) with
     negative letter-spacing AND line-height < 1.0 crams glyphs until they collide
     (numbered-fullbleed). Rule §4: no negative tracking on multi-line condensed; lh >= 1.0.
  5. TOO-TALL DISPLAY STACK — a display zone with no max-height / line budget can run a tall
     headline into the reserved image zone below (hero-statement chain collision). Rule §3:
     cap the display block to its reserved clean zone.

NO slug names appear in any rule — every threshold is general craft. Defects are NAMED in the
docstring as the originating cases for traceability only; the measurement keys on CSS values.

Exit codes:
  0  -> clean (or advisory mode with findings — findings printed, exit still 0).
  1  -> usage / file-not-found error.
  2  -> at least one craft-lint finding AND --enforce was passed (-> 3-try ladder).

Usage:
    uv run check_craft_lint.py --template-html <dir>/template.html
    uv run check_craft_lint.py --template-html <dir>/template.html --enforce
"""
import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------------------
# Thresholds — general craft (html-craft.md §3-§5). Defaults match the rules' stated bands;
# every one is overridable from the CLI so the gate stays tunable without editing the script.
# ---------------------------------------------------------------------------------------
DISPLAY_BODY_RATIO_MAX = 4.0     # §5: display:body <= ~4:1 (above = body stranded as footnote)
DISPLAY_BODY_RATIO_MIN = 1.6     # below = flat hierarchy (display reads as body)
BODY_MIN_CQW = 4.0               # §5: body >= ~4-4.5cqw (RC-B raised from the legacy 3.2)
DISPLAY_MIN_CQW = 8.0            # §3: below ~8cqw a "display" headline reads as body
DISPLAY_LH_MAX = 1.10            # §5: display line-height ~0.95-1.10 (above = airy)
DISPLAY_LH_MIN_CONDENSED = 1.0   # §4: condensed display line-height >= 1.0 (below = collide)
BODY_LH_MIN = 1.2                # §5: body line-height ~1.2-1.5
BODY_LH_MAX = 1.5                # §5: above = "espaçamentos muito altos" (airy footnote)
DISPLAY_STACK_MAX_LINES = 3      # §3: a display stack past ~3 lines with no height cap risks
                                 #     running into the reserved image zone below it

# Condensed display face name hints — a condensed face is where negative tracking + tight
# line-height collides glyphs. General (font-family substrings), not a brand-locked list.
CONDENSED_FACE_HINTS = ("anton", "oswald", "bebas", "condensed", "narrow", "compressed",
                        "impact", "archivo narrow", "barlow condensed", "fjalla")

# Class / data-slot name hints that mark a zone's ROLE — used to bucket each CSS rule into
# display vs body when no explicit role marker is present. General typographic vocabulary.
DISPLAY_ROLE_HINTS = ("display", "headline", "hero", "title", "head", "huge", "mega", "lead")
BODY_ROLE_HINTS = ("body", "para", "paragraph", "copy", "text-body", "subhead", "subtitle",
                   "caption", "lede", "deck", "blurb")
# Roles to IGNORE for the ratio/floor reads (chrome, not display/body content type).
CHROME_ROLE_HINTS = ("kicker", "eyebrow", "footer", "pagination", "badge", "wordmark",
                     "masthead", "handle", "tag", "label", "cta", "pill", "numeral", "number")


def strip_comments(css: str) -> str:
    """Drop /* ... */ CSS comments (incl. the [ai-image-zone] HTML-comment blocks' bodies are
    in HTML comments, not CSS, so this only touches real CSS comments)."""
    return re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)


def iter_css_rules(html: str):
    """Yield (selector, body) for each `selector { body }` CSS rule block in the HTML's
    <style> region(s). Mirrors check_treatment_contract.py's rule-block scan so the selector
    and its properties are read together. Inline `style="..."` is handled separately."""
    # restrict to <style>...</style> so we don't match attribute braces / JS object literals
    styles = re.findall(r"<style[^>]*>(.*?)</style>", html, re.IGNORECASE | re.DOTALL)
    blob = strip_comments("\n".join(styles)) if styles else ""
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", blob):
        yield m.group(1).strip(), m.group(2)


def iter_inline_zones(html: str):
    """Yield (descriptor, style_body, inner_text) for each element carrying an inline
    style=. The descriptor concatenates class + data-slot so role bucketing can read it. Most
    craft templates author the zone geometry/type inline (html-craft.md §1 examples), so the
    inline path is the primary source; the <style> path catches shared rules."""
    for m in re.finditer(r"<(\w+)([^>]*\bstyle\s*=\s*\"([^\"]*)\"[^>]*)>(.*?)</\1>",
                         html, re.IGNORECASE | re.DOTALL):
        attrs = m.group(2)
        style_body = m.group(3)
        inner = m.group(4)
        cls = " ".join(re.findall(r'class\s*=\s*"([^"]*)"', attrs, re.IGNORECASE))
        slot = " ".join(re.findall(r'data-slot\s*=\s*"([^"]*)"', attrs, re.IGNORECASE))
        yield f"{cls} {slot}".strip(), style_body, inner


def parse_cqw(body: str, prop: str) -> float | None:
    """The numeric `cqw` value of a CSS property in a declaration body, or None.
    Only cqw is read — px/em are off-contract for type scale (html-craft.md §3: sizes in cqw)."""
    m = re.search(prop + r"\s*:\s*([\d.]+)\s*cqw", body, re.IGNORECASE)
    return float(m.group(1)) if m else None


def parse_line_height(body: str) -> float | None:
    """Unitless line-height (the craft default form). Returns None for px/% line-heights
    (rare in these templates; the unitless form is the contract)."""
    m = re.search(r"line-height\s*:\s*([\d.]+)\s*(?:;|$|\})", body, re.IGNORECASE)
    return float(m.group(1)) if m else None


def parse_letter_spacing_em(body: str) -> float | None:
    """letter-spacing in em (negative = tracking tightened). None when absent or non-em."""
    m = re.search(r"letter-spacing\s*:\s*(-?[\d.]+)\s*em", body, re.IGNORECASE)
    return float(m.group(1)) if m else None


def parse_max_height(body: str) -> bool:
    """True when the zone caps its height (max-height OR a line budget via -webkit-line-clamp).
    A capped display stack cannot run into the reserved image zone below it (§3)."""
    return bool(re.search(r"max-height\s*:", body, re.IGNORECASE)
                or re.search(r"-webkit-line-clamp\s*:", body, re.IGNORECASE)
                or re.search(r"line-clamp\s*:", body, re.IGNORECASE))


def classify_role(descriptor: str) -> str | None:
    """Bucket a zone descriptor (class + data-slot) into 'display' | 'body' | None.
    Chrome roles (kicker/footer/badge/...) return None — they are not display/body content
    and must not skew the ratio or trip the floors."""
    d = descriptor.lower()
    if any(h in d for h in CHROME_ROLE_HINTS):
        # chrome wins only if NOT also a display/body word (e.g. 'subtitle' is body, not chrome)
        if not any(h in d for h in BODY_ROLE_HINTS) and not any(h in d for h in DISPLAY_ROLE_HINTS):
            return None
    # Body hints are MORE SPECIFIC (e.g. 'subtitle'/'subhead' contain the display word
    # 'title'/'head' as a substring) — match body first so they aren't swallowed as display.
    if any(h in d for h in BODY_ROLE_HINTS):
        return "body"
    if any(h in d for h in DISPLAY_ROLE_HINTS):
        return "display"
    return None


def count_lines(inner_html: str) -> int:
    """Approximate the rendered line count of a zone's authored content: <br> + Mustache slots
    that the author hard-broke. A single-line word counts as 1. Coarse — same altitude as the
    other §2 name reads; the point is 'multi-line' (>= 2), not an exact count."""
    text = inner_html
    brs = len(re.findall(r"<br\s*/?>", text, re.IGNORECASE))
    # a triple/double-brace slot with no <br> is still potentially one line; count the breaks.
    return brs + 1


def has_condensed_face(style_body: str, html: str) -> bool:
    """True when the zone (or the document's display @font-face) uses a CONDENSED face.
    Reads the zone's own font-family first, else the brand display family declared in
    @font-face / :root. General face-name hints, never a brand-locked name."""
    scope = style_body
    fam = re.search(r"font-family\s*:\s*([^;}]+)", style_body, re.IGNORECASE)
    blob = (fam.group(1).lower() if fam else "") + " " + html.lower()
    return any(h in blob for h in CONDENSED_FACE_HINTS)


def collect_zones(html: str) -> list[dict]:
    """Every type-bearing zone with a resolvable cqw font-size, bucketed by role.
    Merges the inline-style zones (primary) and the <style> rules (shared) into one list of
    {role, size_cqw, line_height, letter_spacing_em, lines, capped, condensed, where}."""
    zones: list[dict] = []

    def add(descriptor, style_body, inner, where):
        size = parse_cqw(style_body, "font-size")
        if size is None:
            return
        role = classify_role(descriptor)
        if role is None:
            return
        zones.append({
            "role": role,
            "size_cqw": size,
            "line_height": parse_line_height(style_body),
            "letter_spacing_em": parse_letter_spacing_em(style_body),
            "lines": count_lines(inner) if inner is not None else 1,
            "capped": parse_max_height(style_body),
            "condensed": has_condensed_face(style_body, html),
            "where": where,
        })

    for descriptor, style_body, inner in iter_inline_zones(html):
        add(descriptor, style_body, inner, f"inline:{descriptor[:40]}")
    for selector, body in iter_css_rules(html):
        add(selector, body, None, f"css:{selector[:40]}")
    return zones


def evaluate(html: str, *, ratio_max=DISPLAY_BODY_RATIO_MAX, ratio_min=DISPLAY_BODY_RATIO_MIN,
             body_min=BODY_MIN_CQW, display_min=DISPLAY_MIN_CQW,
             display_lh_max=DISPLAY_LH_MAX, body_lh_min=BODY_LH_MIN, body_lh_max=BODY_LH_MAX,
             stack_max_lines=DISPLAY_STACK_MAX_LINES) -> dict:
    """Measure the five craft rules. Returns {ok, findings:[...], stats:{...}}. Pure on the
    HTML string so the unit tests drive it directly (no files)."""
    zones = collect_zones(html)
    displays = [z for z in zones if z["role"] == "display"]
    bodies = [z for z in zones if z["role"] == "body"]
    findings: list[str] = []

    # The representative display = the LARGEST display size; body = the SMALLEST body size
    # (the worst-case hierarchy gap — a stranded footnote body under the biggest headline).
    disp_size = max((z["size_cqw"] for z in displays), default=None)
    body_size = min((z["size_cqw"] for z in bodies), default=None)

    # Rule 1 — display:body ratio in range.
    if disp_size and body_size and body_size > 0:
        ratio = disp_size / body_size
        if ratio > ratio_max:
            findings.append(
                f"display:body ratio {ratio:.1f}:1 exceeds {ratio_max:.0f}:1 — the body "
                f"(largest display {disp_size:.1f}cqw vs smallest body {body_size:.1f}cqw) is "
                f"stranded as a footnote. Raise the body and/or lower the display (html-craft "
                f"§5: ratio <= ~4:1, hierarchy strong AND body legible).")
        elif ratio < ratio_min:
            findings.append(
                f"display:body ratio {ratio:.1f}:1 is below {ratio_min:.1f}:1 — flat hierarchy "
                f"(display {disp_size:.1f}cqw barely above body {body_size:.1f}cqw); the display "
                f"reads as body. Grow the display (html-craft §3).")

    # Rule 2 — body floor + a display floor sanity (the display floor mirrors Check D's intent
    # at AUTHOR time, before the render).
    for z in bodies:
        if z["size_cqw"] < body_min:
            findings.append(
                f"body {z['size_cqw']:.1f}cqw is below the {body_min:.1f}cqw floor ({z['where']}) "
                f"— an under-scaled body reads as a footnote on a 1080-wide canvas (html-craft §5: "
                f"body >= ~4-4.5cqw).")
    for z in displays:
        if z["size_cqw"] < display_min:
            findings.append(
                f"display {z['size_cqw']:.1f}cqw is below the {display_min:.1f}cqw floor "
                f"({z['where']}) — a 'display' headline that small reads as body (html-craft §3).")

    # Rule 3 — line-height / whitespace discipline ("diminuir entrelinha, aumentar fonte").
    for z in displays:
        lh = z["line_height"]
        if lh is not None and lh > display_lh_max:
            findings.append(
                f"display line-height {lh:.2f} exceeds {display_lh_max:.2f} ({z['where']}) — "
                f"airy display; tighten toward ~0.95-1.05 (html-craft §5).")
    for z in bodies:
        lh = z["line_height"]
        if lh is not None and lh > body_lh_max:
            findings.append(
                f"body line-height {lh:.2f} exceeds {body_lh_max:.2f} ({z['where']}) — "
                f"'espaçamentos muito altos', the body feels airy/dead; tighten toward "
                f"~1.25-1.4 (html-craft §5: diminuir entrelinha, aumentar fonte).")
        if lh is not None and lh < body_lh_min:
            findings.append(
                f"body line-height {lh:.2f} is below {body_lh_min:.2f} ({z['where']}) — "
                f"body lines crowd; ease toward ~1.25-1.4 (html-craft §5).")

    # Rule 4 — negative tracking on a multi-line CONDENSED display collides glyphs.
    for z in displays:
        if not z["condensed"]:
            continue
        ls = z["letter_spacing_em"]
        lh = z["line_height"]
        multiline = z["lines"] >= 2
        if multiline and ls is not None and ls < 0:
            findings.append(
                f"negative letter-spacing {ls:+.3f}em on a MULTI-LINE condensed display "
                f"({z['where']}) — a condensed face crams glyphs until they collide. Drop the "
                f"negative tracking on multi-line condensed type (html-craft §4).")
        if multiline and lh is not None and lh < DISPLAY_LH_MIN_CONDENSED:
            findings.append(
                f"condensed display line-height {lh:.2f} < {DISPLAY_LH_MIN_CONDENSED:.2f} on "
                f"multi-line type ({z['where']}) — condensed faces collide below 1.0; set "
                f"line-height >= 1.0 (html-craft §4).")

    # Rule 5 — a tall display stack with no height cap can run into the image zone below.
    for z in displays:
        if z["lines"] >= stack_max_lines and not z["capped"]:
            findings.append(
                f"display stack of {z['lines']} lines with NO max-height / line budget "
                f"({z['where']}) — a tall headline can run down into the reserved image zone "
                f"below it. Cap the display block to its clean zone (max-height or "
                f"-webkit-line-clamp; html-craft §3).")

    return {
        "ok": not findings,
        "findings": findings,
        "stats": {
            "n_display": len(displays), "n_body": len(bodies),
            "display_cqw": disp_size, "body_cqw": body_size,
            "ratio": (disp_size / body_size) if (disp_size and body_size) else None,
        },
    }


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        rc = getattr(stream, "reconfigure", None)
        if rc:
            try:
                rc(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    ap = argparse.ArgumentParser(description="Craft-LINT — type-craft layer above the overflow gate.")
    ap.add_argument("--template-html", required=True, type=Path)
    ap.add_argument("--enforce", action="store_true",
                    help="block (exit 2) on a finding and feed the 3-try ladder. Default: "
                         "ADVISORY (print findings, exit 0).")
    ap.add_argument("--ratio-max", type=float, default=DISPLAY_BODY_RATIO_MAX)
    ap.add_argument("--body-min", type=float, default=BODY_MIN_CQW)
    args = ap.parse_args()

    if not args.template_html.exists():
        print(f"Error: template.html not found: {args.template_html}", file=sys.stderr)
        return 1

    html = args.template_html.read_text(encoding="utf-8")
    res = evaluate(html, ratio_max=args.ratio_max, body_min=args.body_min)
    st = res["stats"]

    print(f"Craft-LINT on {args.template_html.name}:")
    ratio_s = f"{st['ratio']:.1f}:1" if st["ratio"] else "n/a"
    print(f"  display={st['display_cqw']}cqw  body={st['body_cqw']}cqw  ratio={ratio_s}  "
          f"(display zones={st['n_display']} body zones={st['n_body']})")
    mode = "ENFORCE" if args.enforce else "ADVISORY"
    if res["ok"]:
        print(f"  verdict = CLEAN [{mode}]")
        return 0
    for f in res["findings"]:
        tag = "craft-lint" if args.enforce else "advisory"
        print(f"[{tag}] {f}", file=sys.stderr)
    print(f"  verdict = {len(res['findings'])} finding(s) [{mode}]")
    return 2 if args.enforce else 0


if __name__ == "__main__":
    sys.exit(main())

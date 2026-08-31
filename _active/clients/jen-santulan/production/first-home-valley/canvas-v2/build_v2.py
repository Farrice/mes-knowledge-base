#!/usr/bin/env python3
"""First Home Valley v2 — the v1 artboards with a photography layer injected.

Copy is never retyped. Each v1 .dc.html is read, a <div class="photo"> layer is
inserted directly after the .frame div, and slides that go full-bleed get their
hardcoded light-mode inline colours remapped to the dark set. v1 is untouched.

Photography: curated CC0 / public-domain real photographs from ../imagery/prepared,
embedded as base64 so each artboard stays self-contained for the canvas.

Treatments
  bleed  full-bleed colour photo + navy scrim, frame forced dark
  duo    full-bleed photo pushed to a navy duotone, frame forced dark
  band   photo strip at one edge, frame keeps its light ground
  none   no photo (A5 stays pure white — the restraint anchor)

  build_v2.py
"""
import base64, pathlib, re, shutil, sys

HERE = pathlib.Path(__file__).parent
V1 = HERE.parent / "canvas"
IMG = HERE.parent / "imagery" / "prepared"

# artboard -> dict(t=treatment, img=stem, note=..., [scale=], [pos=])
#
# BAND TREATMENTS REMOVED. Every v1 layout pins its content to both edges with
# justify-content:space-between, so an edge band lands ON live type — it buried
# A3's source line and page number, and swallowed M1's headline. The system is:
#
#   STRUCTURE slides stay white  (A3 comparison, A5 questions, M1 magnet card)
#   STORY slides carry photography (A1, A2, A4, A6, R1-R5)
#
# Three photo-free slides out of twelve is the deck's breathing rhythm, and they
# are exactly the three densest layouts. That is the rule, not an exception.
#
# scale/pos are PER SLIDE. A global scale(1.10), added once to hide a scan border
# on A2, was silently cropping 10% off every other image — that is what reduced
# R2 and R4 to a wrist on empty grey.
PLAN = {
    "Main": dict(t="bleed", img="palm-tree-sunset-city-02", pos="50% 42%",
                 note="A1 hook - the basin at golden hour"),
    "A2":   dict(t="duo", img="valley-street-01", scale=1.14, pos="50% 46%",
                 note="A2 old map - archival palm street; scale crops the scan border"),
    "A3":   dict(t="none", img=None, note="A3 29->40 - comparison slide, stays white"),
    "A4":   dict(t="duo", img="apartment-building-dusk-03", pos="50% 50%",
                 note="A4 21% - curved balconies (v1 frame already dark)"),
    "A5":   dict(t="none", img=None, note="A5 three questions - stays white"),
    "A6":   dict(t="bleed", img="valley-street-00", pos="50% 58%",
                 note="A6 CTA - apartment block at dusk (v1 frame already dark)"),
    "R1":   dict(t="bleed", img="apartment-building-dusk-01", pos="50% 40%",
                 note="R1 - looking out at the apartments you rent"),
    # paper-sheet-01 cropped to an unreadable smear of wrist and grey. A dusk
    # apartment is the literal subject of "renting is cheaper right now".
    "R2":   dict(t="bleed", img="apartment-building-dusk-02", pos="50% 45%",
                 note="R2 - renting, at dusk"),
    # front-door-house-00 (yellow wall / red door) is the better photograph but
    # reads Mediterranean and fights the navy brand. The bungalow is the Valley.
    "R3":   dict(t="bleed", img="california-bungalow-00", pos="50% 55%",
                 note="R3 - the entry home, together"),
    # contract-signing-pen-02 cropped to a pen tip on empty grey. An aerial of
    # the market survives any crop and carries "the wrong number" better.
    "R4":   dict(t="bleed", img="suburban-neighborhood-aerial-02", pos="50% 50%",
                 note="R4 - the 20% myth, over the market itself"),
    "R5":   dict(t="bleed", img="house-key-lock-00", pos="46% 50%",
                 note="R5 - keys in the lock"),
    "M1":   dict(t="none", img=None, note="M1 magnet - card layout, stays white"),
}

# Artboards whose v1 frame is ALREADY dark. Their inline colours are authored for
# a dark ground, so the light->dark remap must not touch them: on A6 it turned a
# white CTA button's navy label white, erasing "DM me MATH" entirely.
ALREADY_DARK = {"A4", "A6"}

EXTRA_CSS = """
  /* --- v2 photography layer ------------------------------------------- */
  .photo { position:absolute; inset:0; z-index:0; overflow:hidden; }
  /* No global scale — framing is set per slide via inline style on the img. */
  .photo > img { width:100%; height:100%; object-fit:cover; display:block;
                 transform-origin:center; }
  .tint  { position:absolute; inset:0; background:#16304F; mix-blend-mode:multiply; }
  .lift  { position:absolute; inset:0; background:#C9D7E8; mix-blend-mode:screen; }
  .scrim { position:absolute; inset:0; }
  /* duotone: desaturate hard, then push through navy — rich, not pale */
  .duo > img { filter:grayscale(1) contrast(1.14) brightness(0.86); }
  .duo .tint { opacity:0.92; }
  .duo .lift { opacity:0.10; }
  /* colour bleed: hold the photo, darken enough for type to sit on it everywhere */
  .bleed > img { filter:saturate(0.72) contrast(1.06) brightness(0.94); }
  .bleed .scrim { background:linear-gradient(180deg,
        rgba(9,20,34,0.62) 0%, rgba(9,20,34,0.48) 26%,
        rgba(9,20,34,0.66) 60%, rgba(9,20,34,0.92) 100%); }
  .bleed .tint { background:#16304F; opacity:0.42; }
"""

# Client-ready typography and brand repairs. These run after the v1 source is
# loaded and before photography is injected, so the rendered PNGs and editable
# v2 artboards share the same safe-area rules.
GLOBAL_REPLACEMENTS = [
    ("font-family:'Figtree','Avenir Next',sans-serif",
     "font-family:'Avenir Next','Helvetica Neue',sans-serif"),
    ("font-family:'Playfair Display',Georgia,serif",
     "font-family:Georgia,'Times New Roman',serif"),
    ("padding:64px 72px", "padding:76px 84px"),
]

SLIDE_REPLACEMENTS = {
    "Main": [
        ("font-size:104px; line-height:1.08", "font-size:98px; line-height:1.06"),
    ],
    "A3": [
        ('font-size:18px; color:#5A6B80;">SOURCE:',
         'font-size:20px; color:#5A6B80;">SOURCE:'),
    ],
    "A4": [
        ("font-size:88px; line-height:1.12", "font-size:82px; line-height:1.1"),
        ("font-size:18px; color:rgba(247,245,242,0.6);",
         "font-size:20px; color:rgba(247,245,242,0.68);"),
    ],
    "A5": [
        ("font-size:72px; line-height:1.12", "font-size:68px; line-height:1.08"),
        ("gap:28px; padding:28px 0", "gap:22px; padding:22px 0"),
        ("font-size:44px; color:#5A6B80; min-width:80px",
         "font-size:42px; color:#5A6B80; min-width:72px"),
        ("font-size:38px; font-weight:600; line-height:1.2",
         "font-size:36px; font-weight:600; line-height:1.18"),
        ("font-size:25px; line-height:1.45", "font-size:29px; line-height:1.38"),
        ('font-size:18px; color:#5A6B80;">TWO OR THREE',
         'font-size:19px; color:#5A6B80;">TWO OR THREE'),
    ],
    "A6": [
        ("font-size:92px; line-height:1.1", "font-size:86px; line-height:1.08"),
    ],
    "M1": [
        ("font-size:84px; line-height:1.12", "font-size:78px; line-height:1.08"),
        ('font-size:17px; color:#5A6B80;">NUMBERS VERIFIED',
         'font-size:19px; color:#5A6B80;">NUMBERS VERIFIED'),
    ],
}


def apply_client_ready_repairs(name, html):
    """Stabilize font metrics, safe areas, dense copy, and provisional marks."""
    # The PNG handoff must not depend on a network font arriving before capture.
    html = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/[^>]+>',
                  "", html)
    for old, new in GLOBAL_REPLACEMENTS:
        html = html.replace(old, new)
    for old, new in SLIDE_REPLACEMENTS.get(name, []):
        html = html.replace(old, new)

    if name in {"R1", "R2", "R3", "R4", "R5"}:
        html = html.replace(
            "font-size:96px; line-height:1.14; font-weight:600; "
            "letter-spacing:-0.02em; max-width:920px",
            "font-size:90px; line-height:1.1; font-weight:600; "
            "letter-spacing:-0.025em; max-width:880px",
        )

    if name == "R5":
        html = html.replace(
            "she told me she’d rent<br><span class=\"si\">forever.</span> last week<br>i handed her keys.",
            "think you’ll rent<br><span class=\"si\">forever?</span> run the<br>numbers first.",
        )

    # The House Sellers SVG was a provisional recreation. A client-ready social
    # asset should not imply an unofficial mark is approved. Use Jen's verified
    # identity until her official logo file is supplied.
    if name in {"A6", "M1"}:
        identity = ('<div class="caps" style="font-size:19px; letter-spacing:0.16em; '
                    'white-space:nowrap;">@_JIING · JEN SANTULAN</div>')
        html = re.sub(r'<svg width="(?:190|210)".*?</svg>', identity, html,
                      count=1, flags=re.S)
        if name == "A6":
            duplicate = (identity + '<div class="caps" style="font-size:17px; '
                         'color:rgba(247,245,242,0.6);">JEN SANTULAN · SFV &amp; LA</div>')
            single = ('<div class="caps" style="font-size:19px; letter-spacing:0.16em; '
                      'white-space:nowrap;">@_JIING · JEN SANTULAN · SFV + LA</div>')
            html = html.replace(duplicate, single)
    return html

# light-mode inline colours -> their dark-frame equivalents
DARKEN = [
    (r"color:#1E3A5F",  "color:#FFFFFF"),
    (r"#E7EDF4",        "rgba(255,255,255,0.09)"),   # ghost numeral
    (r"#DCE2EA",        "rgba(255,255,255,0.34)"),   # hairlines / rules
    (r"#5A6B80",        "rgba(255,255,255,0.74)"),   # muted body
    (r'stroke="#1E3A5F"', 'stroke="#FFFFFF"'),
    (r"border-top:6px solid #1E3A5F", "border-top:6px solid #FFFFFF"),
]


def b64(stem):
    p = IMG / (stem + ".jpg")
    if not p.exists():
        sys.exit("missing prepared image: %s" % p)
    return base64.b64encode(p.read_bytes()).decode()


def photo_div(treatment, stem, scale, pos):
    cls = "photo bleed" if treatment == "bleed" else "photo duo"
    layers = ('<div class="tint"></div><div class="scrim"></div>'
              if treatment == "bleed"
              else '<div class="tint"></div><div class="lift"></div>')
    style = "object-position:%s;" % pos
    if scale and scale != 1.0:
        style += "transform:scale(%s);" % scale
    return ('<div class="%s"><img alt="" style="%s" src="data:image/jpeg;base64,%s">%s</div>'
            % (cls, style, b64(stem), layers))


def main():
    HERE.mkdir(parents=True, exist_ok=True)
    made = []
    for name, spec in PLAN.items():
        treatment, stem = spec["t"], spec.get("img")
        src = V1 / ("%s.dc.html" % name)
        html = src.read_text()

        html = apply_client_ready_repairs(name, html)

        # 1. extend the stylesheet
        html = html.replace("</style>", EXTRA_CSS + "</style>", 1)

        if treatment != "none":
            # 2. flip the frame to dark; remap inline colours ONLY on artboards
            #    whose v1 frame was light (see ALREADY_DARK).
            head, sep, body = html.partition('<div class="frame')
            close = body.index(">")
            frame_attr, rest = body[:close], body[close:]
            frame_attr = frame_attr.replace("light", "dark")
            if name not in ALREADY_DARK:
                for pat, rep in DARKEN:
                    rest = rest.replace(pat, rep)
            html = head + sep + frame_attr + rest

            # 3. inject the photo layer immediately inside the frame
            m = re.search(r'(<div class="frame[^"]*">)', html)
            html = (html[:m.end()] + "\n"
                    + photo_div(treatment, stem, spec.get("scale"),
                                spec.get("pos", "50% 50%"))
                    + html[m.end():])

        # Generated sources are reviewed and committed alongside their PNGs.
        # Normalize line endings here so a harmless blank in the v1 template
        # does not create trailing-whitespace failures on every artboard.
        html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
        out = HERE / ("%s.dc.html" % name)
        out.write_text(html)
        kb = out.stat().st_size // 1024
        made.append((name, treatment, stem or "-", kb, spec["note"]))
        print("  %-5s %-6s %-34s %5d KB" % (name, treatment, stem or "-", kb))

    shutil.copy2(V1 / "canvas.json", HERE / "canvas.json")
    total = sum(m[3] for m in made)
    print("\n%d artboards, %.1f MB -> %s" % (len(made), total / 1024, HERE))


if __name__ == "__main__":
    main()

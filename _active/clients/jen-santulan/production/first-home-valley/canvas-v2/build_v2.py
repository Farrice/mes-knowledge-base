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

# artboard -> (treatment, image stem, note)
PLAN = {
    "Main": ("bleed", "palm-tree-sunset-city-02", "A1 hook - the basin at golden hour"),
    "A2":   ("duo",   "valley-street-01",         "A2 old map - archival palm street, 1981 beat"),
    "A3":   ("band-bottom", "los-angeles-street-00", "A3 29->40 - street sign band, data stays white"),
    "A4":   ("duo",   "apartment-building-dusk-03", "A4 21% - curved balconies, already a dark frame"),
    "A5":   ("none",  None,                       "A5 three questions - pure white, no photo"),
    "A6":   ("bleed", "valley-street-00",         "A6 CTA - apartment block at dusk, palms"),
    "R1":   ("bleed", "apartment-building-dusk-01", "R1 - looking out at the apartments you rent"),
    "R2":   ("bleed", "paper-sheet-01",           "R2 - the honest math, by hand"),
    # front-door-house-00 (yellow wall / red door) was the first pick and is a
    # better photograph — but it reads Mediterranean and fights the navy brand.
    # The craftsman bungalow is the Valley, which is the point.
    "R3":   ("bleed", "california-bungalow-00",   "R3 - the entry home, together"),
    "R4":   ("bleed", "contract-signing-pen-02",  "R4 - the 20% myth, on paper"),
    "R5":   ("bleed", "house-key-lock-00",        "R5 - keys in the lock"),
    "M1":   ("band-top", "sunlight-through-window-floor-03", "M1 magnet - palm shadow on grass"),
}

EXTRA_CSS = """
  /* --- v2 photography layer ------------------------------------------- */
  .photo { position:absolute; inset:0; z-index:0; overflow:hidden; }
  /* scale(1.05) pushes scan borders and edge artefacts off-frame */
  .photo > img { width:100%; height:100%; object-fit:cover; display:block;
                 transform:scale(1.10); transform-origin:center; }
  .photo.band-bottom { top:auto; height:320px; }
  .photo.band-top { bottom:auto; height:430px; }
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

# light-mode inline colours -> their dark-frame equivalents
DARKEN = [
    (r"color:#1E3A5F",  "color:#FFFFFF"),
    (r"#E7EDF4",        "rgba(255,255,255,0.15)"),   # ghost numeral
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


def photo_div(treatment, stem):
    cls = {"bleed": "photo bleed", "duo": "photo duo",
           "band-bottom": "photo duo band-bottom",
           "band-top": "photo duo band-top"}[treatment]
    layers = '<div class="tint"></div><div class="lift"></div>'
    if treatment == "bleed":
        layers = '<div class="tint"></div><div class="scrim"></div>'
    return ('<div class="%s"><img alt="" src="data:image/jpeg;base64,%s">%s</div>'
            % (cls, b64(stem), layers))


def main():
    HERE.mkdir(parents=True, exist_ok=True)
    made = []
    for name, (treatment, stem, note) in PLAN.items():
        src = V1 / ("%s.dc.html" % name)
        html = src.read_text()

        # 1. extend the stylesheet
        html = html.replace("</style>", EXTRA_CSS + "</style>", 1)

        if treatment != "none":
            # 2. full-bleed treatments flip the frame to dark and remap inline colours
            if treatment in ("bleed", "duo"):
                head, sep, body = html.partition('<div class="frame')
                close = body.index(">")
                frame_attr, rest = body[:close], body[close:]
                frame_attr = frame_attr.replace("light", "dark")
                for pat, rep in DARKEN:
                    rest = rest.replace(pat, rep)
                html = head + sep + frame_attr + rest

            # 3. inject the photo layer immediately inside the frame
            m = re.search(r'(<div class="frame[^"]*">)', html)
            html = html[:m.end()] + "\n" + photo_div(treatment, stem) + html[m.end():]

        out = HERE / ("%s.dc.html" % name)
        out.write_text(html)
        kb = out.stat().st_size // 1024
        made.append((name, treatment, stem or "-", kb, note))
        print("  %-5s %-11s %-34s %5d KB" % (name, treatment, stem or "-", kb))

    shutil.copy2(V1 / "canvas.json", HERE / "canvas.json")
    total = sum(m[3] for m in made)
    print("\n%d artboards, %.1f MB -> %s" % (len(made), total / 1024, HERE))


if __name__ == "__main__":
    main()

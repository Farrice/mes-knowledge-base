#!/usr/bin/env python3
"""Direction D — "valley native": the full 7-slide condo set in @_jiing's navy line
system, led by drawn cartography and a drawn Valley building vocabulary instead of the
category-default serif-italic-over-a-full-bleed-photo cover that 16 of 18 competitors run.

Copy is final (identical to Main.dc.html / C1S2-C1S7.dc.html). This file only executes design.
Writes DD1.dc.html ... DD7.dc.html next to itself. Touches nothing else.
Rules it obeys: navy / steel / soft blue / cream only, nothing warm; every piece of line art is
inline stroke SVG at one weight (2px); no emoji, no gradients, no rounded cards, no type shadows.
"""
import pathlib
import shutil

OUT = pathlib.Path(__file__).parent
IMG = OUT / "img"

# render_png.py copies img/*.jpg into its temp folder but not img/jen/*.jpg,
# so jen's three prints have to live at img/ root to resolve as bare filenames.
for _name in ("jen-porch-vannuys.jpg", "jen-frontdoor.jpg", "jen-portrait.jpg"):
    _src = IMG / "jen" / _name
    _dst = IMG / _name
    if _src.exists() and not _dst.exists():
        shutil.copy(_src, _dst)

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Overpass:wght@400;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">
  <style>
    body {{ margin: 0; font-family: Figtree, "Avenir Next", "Century Gothic", sans-serif; }}
    a {{ color: #1E3A5F; }} a:hover {{ color: #4C7CA8; }}
  </style>
</helmet>
{body}
</x-dc>
</body>
</html>
'''

SERIF = "font-family: 'Playfair Display', Georgia, serif;"
SIGN = "font-family: Overpass, 'Helvetica Neue', Arial, sans-serif;"
FRAME = "width: 1080px; height: 1350px; box-sizing: border-box; position: relative; overflow: hidden;"

INK = "#1E3A5F"        # navy
STEEL = "#4C7CA8"      # steel blue
SOFT = "#C9D4E2"       # soft blue
CREAM = "#F7F5F2"      # cream ground
HAIR = "#E0DBD2"       # hairline
GREY = "#6B6C70"       # body + label grey
DIMC = "#A6A296"       # her existing masthead / footer caption grey
DIMD = "#9FB4CC"       # dark-ground caption blue
GHOSTD = "#24436B"     # dark-ground ghost
RULED = "#3A5578"      # dark-ground rule


# ---------------------------------------------------------------- line art ---
def svg(w, h, vb, paths, stroke=INK, sw=2, extra="", defs=""):
    """Stroke-only SVG. `paths` items are either 'd' or ('d', fill).
    vector-effect holds every stroke at exactly `sw` px no matter how the art is scaled."""
    body = ""
    for p in paths:
        d, f = p if isinstance(p, tuple) else (p, "none")
        body += f'<path d="{d}" fill="{f}" vector-effect="non-scaling-stroke"/>'
    return (f'<svg width="{w}" height="{h}" viewBox="{vb}" fill="none" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'style="display: block; {extra}">{defs}{body}</svg>')


# Four drawn Valley facades on one canonical 100x120 grid, so they tile at any size.
FACADES = {
    # flat-roof dingbat over a carport — the Valley's own apartment type
    "dingbat": [
        ("M6 118 V38 H94 V118 Z", CREAM),
        "M2 38 H98",
        "M6 90 H94",
        "M32 118 V90 M64 118 V90",
        "M18 50 H34 V66 H18 Z M42 50 H58 V66 H42 Z M66 50 H82 V66 H66 Z",
        "M18 74 H34 V84 H18 Z M42 74 H58 V84 H42 Z M66 74 H82 V84 H66 Z",
    ],
    # two-story courtyard walk-up with an outside stair
    "courtyard": [
        ("M8 118 V50 H92 V118 Z", CREAM),
        "M4 50 H96",
        "M8 84 H92",
        "M18 60 H32 V74 H18 Z M42 60 H56 V74 H42 Z M66 60 H80 V74 H66 Z",
        "M18 118 V98 H34 V118",
        "M62 118 V112 H68 V106 H74 V100 H80 V94 H86 V88 H92",
        "M62 106 L88 80",
        "M62 118 V106 M88 88 V80",
    ],
    # mid-rise slab with balcony bands
    "midrise": [
        ("M14 118 V20 H86 V118 Z", CREAM),
        "M14 42 H86 M14 62 H86 M14 82 H86 M14 100 H86",
        "M50 20 V100",
        "M42 118 V104 H58 V118",
        "M22 28 H38 M62 28 H78",
    ],
    # gabled bungalow with a front porch
    "bungalow": [
        ("M10 118 V72 L50 40 L90 72 V118 Z", CREAM),
        "M4 76 L50 36 L96 76",
        "M44 60 L50 53 L56 60",
        "M14 88 H86",
        "M24 118 V88 M76 118 V88",
        "M43 118 V96 H57 V118",
        "M20 98 H34 V112 H20 Z M66 98 H80 V112 H66 Z",
    ],
}


def facade(kind, w, h, marked=False, uid="f"):
    """One drawn building. `marked` cross-hatches it in navy — used for the 15% tile."""
    paths = list(FACADES[kind])
    defs = ""
    if marked:
        defs = (f'<defs><pattern id="hx{uid}" width="9" height="9" patternUnits="userSpaceOnUse" '
                f'patternTransform="rotate(45)"><path d="M0 0 V9" stroke="{INK}" stroke-width="2.6"/>'
                f'</pattern></defs>')
        paths[0] = (paths[0][0], f"url(#hx{uid})")
    return svg(w, h, "0 0 100 120", paths, defs=defs)


def valley_map(w, h, stroke=SOFT, sw=2, extra=""):
    """The Valley grid, single-ink: the ridge, three freeways doubled, the boulevards."""
    return svg(w, h, "0 0 400 400", [
        "M0 44 L58 14 L108 48 L168 10 L238 46 L298 18 L358 50 L400 32",
        "M104 0 V400 M118 0 V400",
        "M296 0 V336 M310 0 V336",
        "M0 336 H400 M0 350 H400",
        "M0 300 H400", "M0 236 H400", "M0 170 H400", "M0 104 H400",
        "M48 66 V300", "M206 66 V300", "M252 66 V300", "M352 66 V300",
    ], stroke=stroke, sw=sw, extra=extra)


def arrow(w, h, stroke=INK, extra=""):
    """One drawn leader arrow. Points right-and-up."""
    return svg(w, h, "0 0 200 90", [
        "M6 82 C 44 78 104 66 150 26",
        "M150 26 L124 32 M150 26 L146 52",
    ], stroke=stroke, extra=extra)


def ring(w, h, stroke=INK, extra=""):
    """One drawn annotation circle."""
    return svg(w, h, "0 0 200 140", [
        "M104 12 C 168 12 196 52 184 88 C 170 128 96 140 48 122 "
        "C 10 108 2 52 44 26 C 60 16 82 12 104 12",
    ], stroke=stroke, extra=extra)


def minutes_page(w, h, stroke=RULED):
    """One drawn page of meeting minutes."""
    return svg(w, h, "0 0 56 74", [
        "M2 2 H54 V72 H2 Z",
        "M11 20 H45 M11 32 H45 M11 44 H45 M11 56 H33",
    ], stroke=stroke)


def stamp_mark(w, stroke=INK):
    """The 'from the valley' mark: a ridge over a boulevard, in a roundel."""
    return svg(w, w, "0 0 46 46", [
        "M23 3 C 34 3 43 12 43 23 C 43 34 34 43 23 43 C 12 43 3 34 3 23 C 3 12 12 3 23 3 Z",
        "M9 25 L15 18 L20 23 L27 13 L37 25",
        "M8 31 H38",
        "M13 36 H18 M21 36 H26 M29 36 H34",
    ], stroke=stroke)


# --------------------------------------------------------------- furniture ---
def stamp(dark=False):
    """The recurring signature — same mark, same words, same place on all seven slides."""
    ink = CREAM if dark else INK
    dim = "#7E96B4" if dark else GREY
    return f'''    <div style="display: flex; align-items: center; gap: 18px; padding-top: 4px;">
      {stamp_mark(44, ink)}
      <div style="display: flex; flex-direction: column; gap: 3px;">
        <span style="{SIGN} font-size: 22px; font-weight: 600; letter-spacing: 0.2em; color: {ink};">VAN NUYS &#183; 91401</span>
        <span style="{SIGN} font-size: 15px; font-weight: 400; letter-spacing: 0.28em; color: {dim};">FROM THE VALLEY</span>
      </div>
    </div>'''


def mast(dark=False):
    ink = CREAM if dark else INK
    rule = RULED if dark else HAIR
    dim = DIMD if dark else DIMC
    return f'''  <div style="position: relative; display: flex; flex-direction: column; gap: 26px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 25px; letter-spacing: 0.24em; color: {dim};">FIRST-TIME BUYER FILE</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
{stamp(dark)}
  </div>'''


def foot(label, n, dark=False):
    c = DIMD if dark else DIMC
    return f'''  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 25px; letter-spacing: 0.22em; color: {c};">{label}</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;7</span>
  </div>'''


def it(text, dark=False):
    c = DIMD if dark else INK
    return f'<span style="{SERIF} font-style: italic; font-weight: 400; color: {c};">{text}</span>'


def eyebrow(text, dark=False):
    c = DIMD if dark else DIMC
    return f'<div style="font-size: 26px; letter-spacing: 0.24em; color: {c};">{text}</div>'


def body(html, dark=False, width=760, size=34):
    rule = RULED if dark else "#D9D3C8"
    c = SOFT if dark else GREY
    return f'''    <div style="display: flex; gap: 32px;">
      <div style="width: 1px; background: {rule}; flex: none;"></div>
      <div style="font-size: {size}px; line-height: 1.55; color: {c}; max-width: {width}px;">{html}</div>
    </div>'''


def print_(src, w, h, rot=0, dark=False, img_h=None, obj_pos="50% 50%", cap=None, overlay=""):
    """A photographic print: thin navy (cream on dark) border, small mat, barely tilted.
    `overlay` takes at most one drawn annotation, positioned inside the print."""
    border = CREAM if dark else INK
    mat = GHOSTD if dark else CREAM
    capc = DIMD if dark else GREY
    ih = img_h or h
    caption = ""
    if cap:
        caption = (f'<div style="{SIGN} font-size: 17px; font-weight: 600; letter-spacing: 0.2em; '
                   f'color: {capc}; padding-top: 14px; text-align: center;">{cap}</div>')
    return f'''<div style="position: relative; transform: rotate({rot}deg); background: {mat}; border: 3px solid {border}; padding: 14px; box-sizing: content-box;">
      <div style="position: relative; width: {w}px; height: {h}px; overflow: hidden;">
        <img src="{src}" style="width: {w}px; height: {ih}px; object-fit: cover; object-position: {obj_pos}; display: block;">
{overlay}
      </div>{caption}
    </div>'''


def marker(n, dark=False):
    ink = CREAM if dark else INK
    bg = "transparent" if dark else CREAM
    return (f'<div style="width: 44px; height: 44px; border: 2px solid {ink}; background: {bg}; '
            f'box-sizing: border-box; display: flex; align-items: center; justify-content: center; flex: none;">'
            f'<span style="{SIGN} font-size: 21px; font-weight: 700; color: {ink};">{n}</span></div>')


def shell(inner, label, n, dark=False, absolute=""):
    bg = INK if dark else CREAM
    return f'''<div style="{FRAME} background: {bg}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
{absolute}
{mast(dark)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 38px;">
{inner}
  </div>
{foot(label, n, dark)}
</div>'''


slides = {}

# =============================================================== DD1 · cover ==
slides["DD1"] = f'''<div style="{FRAME} background: {CREAM}; display: flex; flex-direction: column; padding: 100px;">
  <div style="position: absolute; right: -200px; top: 152px;">{valley_map(660, 660, SOFT, 2)}</div>
{mast()}
  <div style="position: absolute; right: 92px; top: 250px;">
{print_("jen-porch-vannuys.jpg", 370, 462, rot=-1.5, obj_pos="50% 30%", cap="VAN NUYS &#183; THE FRONT STEP")}
  </div>
  <div style="position: absolute; left: 372px; top: 506px;">{arrow(190, 86, INK, "transform: rotate(-8deg);")}</div>
  <div style="position: absolute; left: 100px; right: 100px; bottom: 100px; display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 70px; font-weight: 600; line-height: 1.14; color: {INK}; letter-spacing: -0.015em; max-width: 880px;">what if the building is the problem...<br>{it("not me?")}</div>
    <div style="display: flex; align-items: center; gap: 32px;">
      <div style="width: 76px; height: 1px; background: {INK}; flex: none;"></div>
      <div style="font-size: 36px; line-height: 1.5; color: {GREY}; max-width: 620px;">the question under the 1am scroll.</div>
    </div>
  </div>
</div>'''

# ====================================================== DD2 · the four checks ==
KEY = [
    ("01", "dingbat", "THE SAVINGS ACCOUNT"),
    ("02", "courtyard", "12 MONTHS OF MEETING NOTES"),
    ("03", "midrise", "THE BUILDING&#8217;S OWN INSURANCE"),
    ("04", "bungalow", "WHO&#8217;S BEHIND ON DUES"),
]
key_cols = "".join(f'''        <div style="width: 190px; display: flex; justify-content: center; align-items: flex-end; height: 176px;">{facade(kind, 146, 176)}</div>''' for _, kind, _ in KEY)
key_labels = "".join(f'''        <div style="width: 190px; display: flex; flex-direction: column; align-items: center; gap: 14px;">
          {marker(num)}
          <div style="{SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.16em; line-height: 1.5; color: {INK}; text-align: center;">{lab}</div>
        </div>''' for num, _, lab in KEY)

slides["DD2"] = shell(f'''{eyebrow("THE PART NOBODY EXPLAINS")}
    <div style="{SERIF} font-style: italic; font-size: 94px; font-weight: 400; line-height: 1.0; color: {INK};">you were pre-approved.</div>
    <div style="font-size: 46px; font-weight: 500; line-height: 1.32; color: {INK}; letter-spacing: -0.01em;">the building wasn&#8217;t.</div>
{body("since august 3, 2026, banks check the building&#8217;s books on almost every regular condo loan... <span style='color: " + INK + "; font-weight: 500;'>the ordinary kind, not FHA or VA.</span>", width=800, size=32)}
    <div style="display: flex; flex-direction: column; gap: 0; padding-top: 4px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-end;">
{key_cols}
      </div>
      <div style="height: 2px; background: {INK};"></div>
      <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-top: 22px;">
{key_labels}
      </div>
    </div>''', "WHAT CHANGED ON AUGUST 3", 2)

# ======================================================== DD3 · reserve fund ==
def bar(label, value, width, strong=False):
    numc = INK if strong else GREY
    barc = STEEL if strong else "#D9D3C8"
    return f'''        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <span style="font-size: 32px; font-weight: 500; color: {INK};">{label}</span>
            <span style="{SERIF} font-size: 58px; font-weight: 500; color: {numc};">{value}</span>
          </div>
          <div style="height: 10px; background: #EDE9E2;"><div style="height: 10px; width: {width}%; background: {barc};"></div></div>
        </div>'''

slides["DD3"] = shell(f'''{eyebrow("01 &#183; THE SAVINGS ACCOUNT")}
    <div style="display: flex; gap: 48px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 32px;">
        <div style="font-size: 60px; font-weight: 600; line-height: 1.16; color: {INK}; letter-spacing: -0.01em;">i open the budget before i look at the balcony.</div>
{body("i&#8217;m looking for one thing: the savings account. 10% of the building&#8217;s budget today, 15% for loans dated january 4, 2027 or later.", width=440, size=31)}
      </div>
      <div style="flex: none; padding-top: 4px;">{facade("courtyard", 248, 298)}</div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 38px; padding-top: 6px;">
{bar("floor today", "10%", 40)}
{bar("from jan 4, 2027", "15%", 60, strong=True)}
    </div>''', "SHARE OF THE BUDGET SET ASIDE", 3)

# ============================================================= DD4 · minutes ==
minutes_row = "".join(f'<div>{minutes_page(56, 74)}</div>' for _ in range(12))
aerial_print = print_(
    "sfv-aerial-nara.jpg", 270, 203, rot=1.5, dark=True, cap="SAN FERNANDO VALLEY &#183; 1933",
    overlay=f'<div style="position: absolute; left: 62px; top: 88px;">{ring(135, 95, CREAM)}</div>')

slides["DD4"] = shell(f'''{eyebrow("02 &#183; TWELVE MONTHS OF MEETING NOTES", dark=True)}
    <div style="display: flex; gap: 46px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 38px;">
        <div style="font-size: 66px; font-weight: 600; line-height: 1.16; color: {CREAM}; letter-spacing: -0.01em;">somewhere around page four:<br>{it("&#8220;roof discussed.&#8221;", dark=True)}</div>
{body("that&#8217;s a surprise bill, split between every owner. it was in the notes <span style='color: " + CREAM + "; font-weight: 500;'>months before it hits your mailbox.</span>", dark=True, width=460, size=33)}
      </div>
      <div style="flex: none; padding-top: 8px;">{aerial_print}</div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 16px; padding-top: 14px;">
      <div style="display: flex; justify-content: space-between;">{minutes_row}</div>
      <div style="height: 1px; background: {RULED};"></div>
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: #7E96B4;">TWELVE MEETINGS &#183; ONE PDF &#183; ASK FOR ALL OF THEM</div>
    </div>''', "READ THEM BEFORE YOU OFFER", 4, dark=True)

# =========================================================== DD5 · insurance ==
blvd_print = print_(
    "vannuys-blvd-2024.jpg", 300, 470, rot=-1.5, obj_pos="50% 20%", cap="VAN NUYS BLVD &#183; 91401",
    overlay=f'<div style="position: absolute; left: 152px; top: 158px;">{ring(140, 98, INK)}</div>')

slides["DD5"] = f'''<div style="{FRAME} background: {CREAM}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
  <div style="position: absolute; right: 96px; top: 388px;">{blvd_print}</div>
{mast()}
  <div style="position: relative; display: flex; flex-direction: column; gap: 34px; max-width: 520px;">
{eyebrow("03 &#183; THE BUILDING&#8217;S OWN INSURANCE")}
    <div style="{SERIF} font-size: 176px; font-weight: 500; line-height: 0.98; color: {INK}; letter-spacing: -0.03em;">$50K</div>
    <div style="font-size: 48px; font-weight: 600; line-height: 1.22; color: {INK}; letter-spacing: -0.01em;">if your share of one claim goes over $50,000... the loan stops.</div>
{body("and the policy has to cover a full rebuild.", width=468, size=32)}
  </div>
{foot("THE BUILDING&#8217;S POLICY, NOT YOURS", 5)}
</div>'''

# ========================================================= DD6 · delinquency ==
KINDS = ["dingbat", "courtyard", "midrise", "bungalow"]
MARKED = {2, 9, 15}


def tile_row(lo, hi):
    return "".join(
        f'<div>{facade(KINDS[i % 4], 76, 92, marked=(i in MARKED), uid=str(i))}</div>'
        for i in range(lo, hi))


slides["DD6"] = shell(f'''{eyebrow("04 &#183; WHO&#8217;S BEHIND ON DUES")}
    <div style="display: flex; align-items: baseline; gap: 6px;">
      <span style="{SERIF} font-size: 190px; font-weight: 500; line-height: 0.95; color: {INK}; letter-spacing: -0.03em;">15</span><span style="{SERIF} font-style: italic; font-size: 90px; color: {STEEL};">%</span>
    </div>
    <div style="font-size: 48px; font-weight: 600; line-height: 1.22; color: {INK}; letter-spacing: -0.01em; max-width: 860px;">or more of units 60+ days behind on dues... and no bank lends on the building. yours included.</div>
{body("you can pay yours perfectly, on time, every month. it doesn&#8217;t change the answer.", width=760, size=31)}
    <div style="display: flex; flex-direction: column; gap: 14px; padding-top: 2px;">
      <div style="display: flex; justify-content: space-between;">{tile_row(0, 10)}</div>
      <div style="display: flex; justify-content: space-between;">{tile_row(10, 20)}</div>
      <div style="height: 2px; background: {INK};"></div>
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {GREY}; padding-top: 4px;">3 IN 20 &#183; THE LINE THE WHOLE BUILDING SITS ON</div>
    </div>''', "WHO&#8217;S PAYING, WHO ISN&#8217;T", 6)

# ============================================================== DD7 · close ===
# cropped from the top: the source frame carries a burned-in caption across its lower third.
door_print = print_("jen-frontdoor.jpg", 300, 286, rot=1.5, dark=True,
                    img_h=460, obj_pos="50% 14%", cap="JEN &#183; SAN FERNANDO VALLEY")

slides["DD7"] = f'''<div style="{FRAME} background: {INK}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
  <div style="position: absolute; right: -180px; top: 170px;">{valley_map(640, 640, GHOSTD, 2)}</div>
{mast(dark=True)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 80px; font-weight: 600; line-height: 1.16; color: {CREAM}; letter-spacing: -0.01em;">send me the address<br>{it("before you write.", dark=True)}</div>
    <div style="display: flex; gap: 46px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 40px;">
{body("we&#8217;ll read the four documents together and go from there. i&#8217;m here for you... i do this to protect you and your best interest.", dark=True, width=440, size=31)}
        <div style="display: flex; align-items: center; background: {CREAM}; padding: 30px 42px; align-self: flex-start;">
          <span style="{SERIF} font-style: italic; font-size: 46px; font-weight: 500; color: {INK}; white-space: nowrap;">my DMs are open</span>
        </div>
      </div>
      <div style="flex: none;">{door_print}</div>
    </div>
  </div>
  <div style="position: relative; display: flex; flex-direction: column; gap: 30px;">
    <div style="font-size: 22px; letter-spacing: 0.1em; line-height: 1.7; color: #7E96B4;">SOURCE: FANNIE MAE LENDER LETTER LL-2026-03 &#183; FREDDIE MAC BULLETIN 2026-C &#183; AUGUST 2026</div>
{foot("JEN SANTULAN &#183; SFV &amp; LOS ANGELES", 7, dark=True)}
  </div>
</div>'''

# ===================================================================== write ==
for name, html in slides.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=html))
print("wrote", len(slides), "valley-native artboards:", ", ".join(sorted(slides)))

#!/usr/bin/env python3
"""Valley Editions generator — the place-magazine surface for @_jiing (DESIGN.md is the spec).
Archetypes: cover_gem, cover_stack, moment, spot, grid, statement, close. Each returns page HTML;
render() turns it into a 1080x1350 PNG with chrome-headless-shell. Photos are absolute paths.

  python3 editions.py takes      # the two Tarzana · Edition 01 cover takes (A: gem, B: stack)
"""
import glob, html as _html, os, pathlib, re, subprocess, sys, urllib.parse

HERE = pathlib.Path(__file__).parent
SEPT = HERE.parent.parent / "04-deliverables" / "2026-09-01-september-carousels"
IMG = SEPT / "img"
OUT = HERE / "out"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

W, H = 1080, 1350
GUTTER = 108
SERIF = "font-family: 'Instrument Serif', 'Playfair Display', Georgia, serif;"
ACCENT = "#C9D4E2"
SANS = "font-family: 'Jost', system-ui, sans-serif;"
HAND = "font-family: 'Caveat', cursive;"
CREAM, WHITE, WASH = "#F7F5F2", "#FFFFFF", "15,20,30"
IVORY_GRAD = "linear-gradient(135deg, #C9D4E2 0%, #EEF2F7 40%, #FFFFFF 100%)"

HEAD = f'''<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Jost:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Instrument+Serif:ital@0;1&display=swap">
<style>html,body{{margin:0;background:#111}} .page{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#1E2430}}
.abs{{position:absolute}} .caps{{{SANS}font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:{WHITE}}} .sc{{{SERIF}letter-spacing:-.01em;text-transform:uppercase;color:{WHITE}}}
.grad{{background:{IVORY_GRAD};-webkit-background-clip:text;background-clip:text;color:transparent}}</style>'''


def fit(text, size, usable=W - 2 * GUTTER, em=0.42):
    longest = max(len(_html.unescape(re.sub(r"<[^>]+>", "", seg))) for seg in text.split("<br>"))
    return min(size, int(usable / max(longest, 1) / em))


def photo(src, pos="50% 50%", scale=1.0):
    return f'<img src="{pathlib.Path(src).resolve().as_uri()}" class="abs" style="inset:0;width:{W}px;height:{H}px;object-fit:cover;object-position:{pos};transform:scale({scale});transform-origin:{pos}">'


def wash(corner="bottom", plateau=False, grain=False):
    stops = f"rgba({WASH},.60) 0%, rgba({WASH},.55) 33%, rgba({WASH},.55) 66%, rgba({WASH},.42) 100%" if plateau \
        else f"rgba({WASH},.62) 0%, rgba({WASH},.40) 50%, rgba({WASH},0) 100%"
    deg = {"bottom": 0, "top": 180, "left": 90, "right": 270}[corner]
    g = f'<div class="abs" style="inset:0;background:linear-gradient({deg}deg, {stops})"></div>'
    if grain:
        g += '<div class="abs" style="inset:0;opacity:.10;background-image:url(data:image/svg+xml;utf8,<svg xmlns=%27http://www.w3.org/2000/svg%27 width=%27120%27 height=%27120%27><filter id=%27n%27><feTurbulence baseFrequency=%270.9%27 numOctaves=%272%27/></filter><rect width=%27120%27 height=%27120%27 filter=%27url(%23n)%27/></svg>)"></div>'
    return g


def masthead(left, right=""):
    r = f'<div class="abs caps" style="right:{GUTTER}px;top:82px;font-size:24px;text-align:right">{right}</div>' if right else ""
    return f'<div class="abs caps" style="left:{GUTTER}px;top:82px;font-size:24px;line-height:1.4">{left}</div>{r}'


def footer(left="@_JIING", right=""):
    r = f'<div class="abs caps" style="right:{GUTTER}px;bottom:70px;font-size:24px">{right}</div>' if right else ""
    return f'<div class="abs caps" style="left:{GUTTER}px;bottom:70px;font-size:24px">{left}</div>{r}'


def pill(text, left, top, w=290, h=72):
    return (f'<div class="abs" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;transform:rotate(-2deg)">'
            f'<svg class="abs" style="inset:0" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none"><ellipse cx="{w/2}" cy="{h/2}" rx="{w/2-3}" ry="{h/2-3}" stroke="{ACCENT}" stroke-width="2.5"/></svg>'
            f'<div class="abs sc" style="inset:0;display:flex;align-items:center;justify-content:center;font-size:25px">{text}</div></div>')


def arrow(left, top, rot=0, size=200, tail=0):
    """Hand-drawn arrow; tail>0 adds the template's long thin line trailing off to the right (the 'frame bar')."""
    t = f'<path d="M168 40 C 300 30, 600 20, {168+tail} 6" stroke-width="2.5"/>' if tail else ""
    return (f'<svg class="abs" style="left:{left}px;top:{top}px;transform:rotate({rot}deg);overflow:visible" width="{size}" height="{size*0.4:.0f}" viewBox="0 0 180 72" fill="none" '
            f'stroke="{ACCENT}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 44 C 60 22, 110 28, 160 38"/><path d="M128 12 L 168 38 L 130 58"/>{t}</svg>')


def smiley(left, top, size=130):
    return (f'<svg class="abs" style="left:{left}px;top:{top}px" width="{size}" height="{size*0.6:.0f}" viewBox="0 0 110 66" fill="none" stroke="{ACCENT}" stroke-width="7" stroke-linecap="round">'
            f'<path d="M14 38 C 40 72, 80 72, 100 34"/><path d="M28 10 L30 20"/><path d="M76 6 L78 16"/></svg>')


def sparkle(left, top, size=44):
    return (f'<svg class="abs" style="left:{left}px;top:{top}px" width="{size}" height="{size}" viewBox="0 0 44 44" fill="{ACCENT}">'
            f'<path d="M22 0 C 24 14, 30 20, 44 22 C 30 24, 24 30, 22 44 C 20 30, 14 24, 0 22 C 14 20, 20 14, 22 0 Z"/></svg>')


# ------------------------------------------------------------------ archetypes

def cover_gem(src, eyebrow, connector, headline, subline, handle="@_jiing", pos="50% 30%", size=170):
    """Design 1: eyebrow top-left, italic connector + big serif (ivory gradient) at the lower-left third, subline, pill, arrow."""
    size = fit(headline, size)
    return f'''<div class="page">{photo(src, pos)}{wash("top", plateau=True, grain=True)}
{masthead(eyebrow)}
<div class="abs" style="left:{GUTTER}px;top:{int(H*0.41)}px;width:{W-2*GUTTER}px">
  <div style="{SERIF}font-style:italic;font-size:{int(size*0.46)}px;line-height:1;color:{CREAM};margin-left:6px">{connector}</div>
  <div class="grad" style="{SERIF}font-size:{size}px;line-height:.92;letter-spacing:-.02em;margin-top:-6px">{headline}</div>
  <div style="{SANS}font-weight:300;font-size:28px;line-height:1.4;color:{WHITE};max-width:640px;margin-top:34px">{subline}</div>
</div>
{pill(handle, W - GUTTER - 262, int(H*0.335))}
{arrow(GUTTER - 6, H - 215, rot=-8)}
{footer("the valley &#183; a series", "01 / 05")}
</div>'''


def cover_stack(src, brand, tagline, word1, word2, connector, quote, credit, pos="50% 30%", size=178, corner="left"):
    """Design 3: two-word stack (word 2 bold) lower third, italic connector at the break, bold-italic quote line, credit opposite corner."""
    size = fit(f"{word1}<br>{word2}", size)
    align = "left" if corner == "left" else "right"
    box = f"left:{GUTTER}px;text-align:left" if corner == "left" else f"right:{GUTTER}px;text-align:right"
    cred = f"right:{GUTTER}px;text-align:right" if corner == "left" else f"left:{GUTTER}px"
    return f'''<div class="page">{photo(src, pos)}{wash("bottom")}
<div class="abs" style="left:{GUTTER}px;top:82px;{SERIF}font-weight:700;font-size:28px;line-height:1.15;color:{WHITE}">{brand}</div>
<div class="abs" style="right:{GUTTER}px;top:82px;{SERIF}font-style:italic;font-size:26px;line-height:1.2;color:{WHITE};text-align:right">{tagline}</div>
<div class="abs" style="{box};top:{int(H*0.50)}px;width:{W-2*GUTTER}px">
  <div style="{SERIF}font-size:{size}px;line-height:.95;letter-spacing:-.02em;color:{WHITE}">{word1} <span style="font-style:italic;font-size:{int(size*0.44)}px;vertical-align:middle">{connector}</span></div>
  <div style="{SERIF}font-weight:700;font-size:{size}px;line-height:.95;letter-spacing:-.02em;color:{WHITE}">{word2}</div>
  <div style="{SERIF}font-weight:700;font-style:italic;font-size:32px;line-height:1.3;color:{WHITE};margin-top:26px">{quote}</div>
</div>
<div class="abs" style="{cred};bottom:70px;{SERIF}color:{WHITE};font-size:24px;line-height:1.4">post by:<br><b style="font-size:32px">{credit}</b></div>
</div>'''


def statement(src, brand, tagline, word1, word2, body, corner="left", pos="50% 40%"):
    """Design 3 interior: two-word stack in a corner, body opposite, wash points away from the headline."""
    size = fit(f"{word1}<br>{word2}", 106)
    top = int(H * 0.36)
    hb = f"left:{GUTTER}px" if corner == "left" else f"right:{GUTTER}px;text-align:right"
    bb = f"right:{GUTTER}px;text-align:right" if corner == "left" else f"left:{GUTTER}px"
    return f'''<div class="page">{photo(src, pos)}{wash("bottom" if corner == "left" else "top")}
<div class="abs" style="left:{GUTTER}px;top:82px;{SERIF}font-weight:700;font-size:28px;color:{WHITE}">{brand}</div>
<div class="abs" style="right:{GUTTER}px;top:82px;{SERIF}font-style:italic;font-size:26px;color:{WHITE};text-align:right">{tagline}</div>
<div class="abs" style="{hb};top:{top}px;{SERIF}font-size:{size}px;line-height:.98;color:{WHITE}">{word1}<br><b>{word2}</b></div>
<div class="abs" style="{bb};top:{top + int(size*2.2)}px;width:{int(W*0.44)}px;{SANS}font-weight:300;font-size:28px;line-height:1.45;color:{WHITE}">{body}</div>
</div>'''


def moment(src, brand, edition, word, lines, n, pos="50% 40%", mirror=False):
    """Design 2: short headline word top-left, three staggered body lines down the page, chrome rules top and bottom."""
    rule = f'<div class="abs" style="left:0;right:0;height:1.5px;background:{WHITE};opacity:.8"></div>'
    tops = [int(H * t) for t in (0.62, 0.72, 0.82)]
    body = "".join(f'<div class="abs" style="{"right" if (mirror and i == 1) else "left"}:{GUTTER}px;top:{tops[i]}px;max-width:720px;{SANS}font-weight:400;font-size:36px;line-height:1.2;color:{WHITE};{"text-align:right" if (mirror and i == 1) else ""}">{l}</div>' for i, l in enumerate(lines))
    return f'''<div class="page">{photo(src, pos)}{wash("bottom")}
<div class="abs" style="top:32px;left:0;right:0;height:1.5px;background:{WHITE};opacity:.8"></div><div class="abs" style="top:116px;left:0;right:0;height:1.5px;background:{WHITE};opacity:.8"></div>
<div class="abs" style="bottom:116px;left:0;right:0;height:1.5px;background:{WHITE};opacity:.8"></div><div class="abs" style="bottom:32px;left:0;right:0;height:1.5px;background:{WHITE};opacity:.8"></div>
<div class="abs caps" style="left:{GUTTER}px;top:58px;font-size:26px">{brand}</div><div class="abs caps" style="right:{GUTTER}px;top:58px;font-size:26px">{edition}</div>
<div class="abs" style="left:{GUTTER}px;top:{int(H*0.13)}px;{SERIF}font-size:{fit(word, 150)}px;line-height:.95;color:{WHITE}">{word}</div>
{sparkle(GUTTER + 20, int(H*0.55))}
{body}
<div class="abs caps" style="left:{GUTTER}px;bottom:58px;font-size:26px">@_jiing</div><div class="abs caps" style="right:{GUTTER}px;bottom:58px;font-size:26px">slide 0{n}</div>
</div>'''


def spot(src, eyebrow, headline, label, body, inset_l, inset_r, handle="@_jiing", pos="50% 40%"):
    """Design 1 interior: centered serif headline, handle pill, one sentence, rounded photo pair at 66% height."""
    size = fit(headline, 150, usable=W - 2 * GUTTER, em=0.5)
    ins = lambda s, left: f'<img src="{pathlib.Path(s).resolve().as_uri()}" class="abs" style="left:{left}px;top:{int(H*0.66)}px;width:{int(W*0.40)}px;height:{int(H*0.194)}px;object-fit:cover;border-radius:30px">'
    return f'''<div class="page">{photo(src, pos)}{wash("top", plateau=True, grain=True)}
<div class="abs caps" style="left:0;right:0;top:82px;text-align:center;font-size:24px;line-height:1.4">{eyebrow}</div>
{sparkle(int(W/2)-16, 150, 32)}
<div class="abs grad" style="left:{GUTTER}px;right:{GUTTER}px;top:{int(H*0.24)}px;text-align:center;{SERIF}font-size:{size}px;line-height:.95;letter-spacing:-.02em">{headline}</div>
{pill(handle, int(W/2)-124, int(H*0.43))}
<div class="abs" style="left:{int(W*0.2)}px;width:{int(W*0.6)}px;top:{int(H*0.50)}px;text-align:center;{SANS}font-weight:300;font-size:26px;line-height:1.45;color:{WHITE}">{body}</div>
{ins(inset_l, int(W*0.083))}{ins(inset_r, int(W*0.516))}
<div class="abs caps" style="left:0;right:0;bottom:56px;text-align:center;font-size:22px;opacity:.85">{label}</div>
</div>'''


def grid(top_src, bot_src, top, bot):
    """Design 5: two 50% halves, each a numbered entry. entry = dict(num, name, headline, line, price, align)."""
    def half(src, e, y):
        al = "left" if e.get("align", "left") == "left" else "right"
        box = f"left:{GUTTER}px;text-align:left" if al == "left" else f"right:{GUTTER}px;text-align:right"
        return f'''<div class="abs" style="left:0;top:{y}px;width:{W}px;height:{H//2}px;overflow:hidden">
  <img src="{pathlib.Path(src).resolve().as_uri()}" style="width:{W}px;height:{H//2}px;object-fit:cover">
  <div class="abs" style="inset:0;background:linear-gradient({0 if al=="left" else 180}deg, rgba({WASH},.62) 0%, rgba({WASH},.25) 60%, rgba({WASH},.05) 100%)"></div>
  <div class="abs caps" style="{box};top:{int(H*0.08)}px;font-size:26px">{e["num"]} &#8212; {e["name"]}</div>
  <div class="abs" style="{box};top:{int(H*0.115)}px;width:{int(W*0.52)}px;height:1.5px;background:{WHITE};opacity:.7;{"" if al=="left" else "left:auto"}"></div>
  <div class="abs" style="{box};top:{int(H*0.14)}px;{SERIF}font-size:{fit(e["headline"], 93)}px;line-height:1;color:{WHITE}">{e["headline"]}</div>
  <div class="abs" style="{box};top:{int(H*0.235)}px;width:{int(W*0.5)}px;{SANS}font-weight:300;font-size:26px;line-height:1.4;color:{WHITE}">{e["line"]}</div>
  <div class="abs" style="{box};top:{int(H*0.31)}px;{SANS}font-weight:500;font-size:40px;color:{WHITE}">{e["price"]}</div>
</div>'''
    return f'<div class="page">{half(top_src, top, 0)}{half(bot_src, bot, H//2)}<div class="abs" style="inset:0">{wash("bottom")}</div></div>'.replace(f'{wash("bottom")}', "")


def close(src, eyebrow, headline, body, hand_line, handle="@_jiing", pos="50% 20%"):
    """Design 1/5 close: centered, no panels. the door line + her verbatim close."""
    return f'''<div class="page">{photo(src, pos)}{wash("top", plateau=True, grain=True)}
<div class="abs caps" style="left:0;right:0;top:82px;text-align:center;font-size:24px;line-height:1.4">{eyebrow}</div>
<div class="abs grad" style="left:{GUTTER}px;right:{GUTTER}px;top:{int(H*0.33)}px;text-align:center;{SERIF}font-size:{fit(headline, 150)}px;line-height:.95;letter-spacing:-.02em">{headline}</div>
{pill(handle, int(W/2)-124, int(H*0.55))}
<div class="abs" style="left:{int(W*0.18)}px;width:{int(W*0.64)}px;top:{int(H*0.63)}px;text-align:center;{SANS}font-weight:300;font-size:27px;line-height:1.45;color:{WHITE}">{body}</div>
<div class="abs" style="left:0;right:0;top:{int(H*0.79)}px;text-align:center;{HAND}font-size:52px;color:{WHITE}">{hand_line}</div>
{smiley(int(W/2)-55, H-150)}
</div>'''


# ------------------------------------------------------------------ render

def render(html_body, png):
    OUT.mkdir(exist_ok=True)
    tmp = OUT / ".tmp"; tmp.mkdir(exist_ok=True)
    shim = tmp / (pathlib.Path(png).stem + ".html")
    shim.write_text(HEAD + html_body)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", "--virtual-time-budget=5000", f"--screenshot={png}", shim.as_uri()],
                   check=True, capture_output=True)
    print(f"  {pathlib.Path(png).name} ({pathlib.Path(png).stat().st_size // 1024} KB)")


def takes():
    her = IMG / "jen-porch-vannuys.jpg"
    render(cover_gem(her, "The Valley &#183; Edition 01<br>Tarzana, September",
                     "this is", "Tarzana.",
                     "what $869K buys here this month, the coffee line on ventura at 7am, and the one street i&#8217;d go see first. buying or selling.",
                     pos="50% 12%"),
           OUT / "take-A-cover-gem.png")
    render(cover_stack(her, "Jen Santulan<br>Realtor", "buying or selling.<br>the valley.",
                       "Tarzana", "September.", "this",
                       "what $869K buys here this month &#8594;", "Jen Santulan", pos="50% 12%", corner="left"),
           OUT / "take-B-cover-stack.png")


# ------------------------------------------------------------------ exact-geometry cover (Design 1, page 1, numbers from CANVA-GRAMMAR.md)
PH = HERE / "photos" / "jen"


def placed(src, left, top, size, fill="#8d8878"):
    """Studio portrait on an extended wall: a flat radial fill in the backdrop's own khaki (no blurred copy, no ghost), the sharp square photo at
    (left, top, size) with its top and left edges feathered into the wall. Lets the head land where the template puts its subject (lower right)."""
    uri = pathlib.Path(src).resolve().as_uri()
    mask = "linear-gradient(180deg, transparent 0%, #000 18%, #000 100%), linear-gradient(90deg, transparent 0%, #000 14%, #000 100%)"
    return (f'<div class="abs" style="inset:0;background:radial-gradient(120% 90% at 68% 22%, #a39d8a 0%, #8d8878 45%, #67635a 100%)"></div>'
            f'<img src="{uri}" class="abs" style="left:{left}px;top:{top}px;width:{size}px;height:{size}px;object-fit:cover;'
            f'-webkit-mask-image:{mask};-webkit-mask-composite:source-in;mask-image:{mask};mask-composite:intersect">')


def cover_exact(src, eyebrow, line_italic, line_upright, subline, handle="@_jiing", pos="50% 50%", scale=1.0, fill=None, size=166, stripe=True, place=None):
    """D1 cover, nothing moved: masthead L5.6% T7.2% · headline L5.3% T16.6% W73% (166px, lh .75, italic first clause)
    · subline L5.3% T38.4% W55% (26px) · badge L5.3% T48% · pill L53% T20.4% · stripe T92% rot 7° · wash 4-stop over top 71%."""
    size = fit(f"{line_italic}<br>{line_upright}", size, usable=int(W * 0.733), em=0.44)
    if place:
        img = placed(src, *place)
    elif fill:  # extend the studio backdrop: a blurred copy of the photo fills the frame, the sharp photo sits small on top, edges feathered
        uri = pathlib.Path(src).resolve().as_uri()
        img = (f'<div class="abs" style="inset:0;background:{fill}"></div>'
               f'<img src="{uri}" class="abs" style="left:-60px;top:-60px;width:{W+120}px;height:{H+120}px;object-fit:cover;object-position:{pos};filter:blur(48px) brightness(.92)">'
               f'<img src="{uri}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px;object-fit:contain;object-position:{pos};transform:scale({scale});transform-origin:{pos};'
               f'-webkit-mask-image:linear-gradient(90deg, transparent 0%, #000 18%, #000 100%), linear-gradient(180deg, transparent 0%, #000 22%, #000 100%);-webkit-mask-composite:source-in;mask-composite:intersect">')
    else:
        img = photo(src, pos, scale)
    return f'''<div class="page">{img}
<div class="abs" style="left:0;top:0;width:{W}px;height:{int(H*0.711)}px;background:linear-gradient(180deg, rgba({WASH},.60) 0%, rgba({WASH},.55) 33%, rgba({WASH},.55) 66%, rgba({WASH},0) 100%)"></div>
<div class="abs sc" style="left:{int(W*0.056)}px;top:{int(H*0.072)}px;font-size:24px;line-height:1.3">{eyebrow}</div>
<div class="abs grad" style="left:{int(W*0.053)}px;top:{int(H*0.166)}px;width:{int(W*0.733)}px;{SERIF}font-size:{size}px;line-height:.78;letter-spacing:-.025em"><span style="font-style:italic">{line_italic}</span><br>{line_upright}</div>
<div class="abs" style="left:{int(W*0.053)}px;top:{int(H*0.384)}px;width:{int(W*0.554)}px;{SERIF}font-size:28px;line-height:1.35;color:{WHITE}">{subline}</div>
{smiley(int(W*0.053), int(H*0.48), 120)}
{pill(handle, int(W*0.531), int(H*0.204))}
{arrow(int(W*0.053), int(H*0.905), rot=-6, size=200, tail=700 if stripe else 0)}
</div>'''


def variations():
    eyebrow = "The Valley &#183; Tarzana<br>Edition 01"
    sub = "three homes, one price, the coffee line on ventura at 7am, and the street i&#8217;d go see first. buying or selling."
    # V1 · the kitchen: people small in the lower half, headroom above for the type (closest to the template's own composition)
    render(cover_exact(PH / "jen-client-kitchen-sold.jpg", eyebrow, "$869K", "in Tarzana.", sub, pos="42% 100%"),
           OUT / "cover-v1-kitchen.png")
    # V2 · the studio headshot, background extended, Jen bottom-right and small, where the template puts its subject
    render(cover_exact(PH / "jen-headshot-studio.jpg", eyebrow, "$869K", "in Tarzana.", sub, pos="100% 100%", scale=0.78, fill="#8d8878"),
           OUT / "cover-v2-headshot.png")
    # V3 · the place, no person: the pool through the door, type over the wall
    render(cover_exact(PH / "listing-home-gym-pool.jpg", eyebrow, "$869K", "in Tarzana.", sub, pos="35% 50%"),
           OUT / "cover-v3-place.png")


# ------------------------------------------------------------------ Edition 01 · exact D1 interior + close geometry, plate slots, fact panel
# Numbers from CANVA-GRAMMAR.md, Design 1 pages 2-5. Nothing moved; where the template has a decorative stripe we set a text line in its slot.
# Playfair runs ~0.5em/char against the template face's ~0.31em, so two-line headlines are capped so they end above the pill (interior T41.6%, close T53.3%).
ED = HERE / "edition-01"


def headline_size(text, cap, box_px, usable, em=0.46, lh=0.82):
    lines = text.count("<br>") + 1
    return min(fit(text, cap, usable=usable, em=em), int(box_px / (lines * lh)))


def wash_d1():
    """D1 interior/close: 4-stop plateau over the whole page, dark end at the top."""
    return (f'<div class="abs" style="inset:0;background:linear-gradient(180deg, rgba({WASH},.55) 0%, rgba({WASH},.48) 33%, '
            f'rgba({WASH},.46) 66%, rgba({WASH},.34) 100%)"></div>')


def plate_bg(letter, note):
    """A labeled stand-in for an AI Valley plate that has not been generated yet. Never pretends to be a photo."""
    return (f'<div class="abs" style="inset:0;background:linear-gradient(160deg,#2A3442 0%,#1B2330 60%,#131923 100%)"></div>'
            f'<div class="abs caps" style="left:0;right:0;top:{int(H*0.60)}px;text-align:center;font-size:18px;opacity:.7">photo slot &#183; plate {letter}</div>'
            f'<div class="abs" style="left:{int(W*0.12)}px;width:{int(W*0.76)}px;top:{int(H*0.60)+28}px;text-align:center;{SANS}font-weight:300;font-size:17px;line-height:1.3;color:{WHITE};opacity:.65">{note}</div>')


def plate_inset(letter, note, left, top=None, w=None, h=None):
    top = int(H * 0.661) if top is None else top; w = int(W * 0.40) if w is None else w; h = int(H * 0.194) if h is None else h
    return (f'<div class="abs" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;border-radius:30px;overflow:hidden;'
            f'background:linear-gradient(160deg,#33404F 0%,#212B38 100%);border:1.5px solid rgba(247,245,242,.35)">'
            f'<div class="abs caps" style="left:0;right:0;top:{int(h*0.36)}px;text-align:center;font-size:15px;opacity:.75">plate {letter}</div>'
            f'<div class="abs" style="left:24px;right:24px;top:{int(h*0.36)+26}px;text-align:center;{SANS}font-weight:300;font-size:15px;line-height:1.3;color:{WHITE};opacity:.7">{note}</div></div>')


def fact_panel(left, eyebrow, big, small, top=None, w=None, h=None):
    """A fact in a photo panel's slot: same 30px radius, cream hairline, dark translucent fill. Used when a photo would mislead."""
    top = int(H * 0.661) if top is None else top; w = int(W * 0.40) if w is None else w; h = int(H * 0.194) if h is None else h
    return (f'<div class="abs" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;border-radius:30px;overflow:hidden;'
            f'background:rgba({WASH},.55);border:1.5px solid rgba(247,245,242,.6);text-align:center">'
            f'<div class="abs caps" style="left:0;right:0;top:34px;font-size:16px;opacity:.85">{eyebrow}</div>'
            f'<div class="abs grad" style="left:0;right:0;top:66px;{SERIF}font-size:{fit(big, 62, usable=w-40)}px;line-height:1">{big}</div>'
            f'<div class="abs" style="left:24px;right:24px;top:{h-64}px;{look()["panel_small"]};line-height:1.3;color:{WHITE}">{small}</div></div>')


def inset(src, left, pos="50% 50%"):
    return (f'<img src="{pathlib.Path(src).resolve().as_uri()}" class="abs" style="left:{left}px;top:{int(H*0.661)}px;width:{int(W*0.40)}px;'
            f'height:{int(H*0.194)}px;object-fit:cover;object-position:{pos};border-radius:30px">')


INSET_L, INSET_R = int(W * 0.083), int(W * 0.516)


def spot_exact(bg, masthead_text, headline, body, label, panel_l, panel_r, handle="@_jiing"):
    """D1 pages 2-4, nothing moved: masthead center T7.2% · sparkle T12.3% · headline L9.2% T23.8% W78.3% center (166px cap; two lines end above the pill)
    · pill L33.3% T41.6% · body L20.6% T50% W55.4% (26px) · two rounded panels L8.3%/51.6% T66.1% W40% H19.4% · label in the stripe slot T94.1%."""
    L = look()
    size = headline_size(headline, 176, int(H * (0.416 - 0.238)) - 4, int(W * 0.783), em=L["em"])
    g = f'background:{L["grad"]};-webkit-background-clip:text;background-clip:text;color:transparent'
    return (f'<div class="page">{bg}{wash_d1()}'
            f'<div {L["mast"]}>{masthead_text}</div>'
            f'{sparkle(int(W*0.467) + 2, int(H*0.123), 36)}'
            f'<div class="abs" style="left:{int(W*0.092)}px;width:{int(W*0.783)}px;top:{int(H*0.238)}px;text-align:center;{L["face"]}font-size:{size}px;line-height:.85;letter-spacing:-.02em;{g}">{headline}</div>'
            f'{pill(handle, int(W*0.333) + 40, int(H*0.416))}'
            f'<div class="abs" style="left:{int(W*0.206)}px;width:{int(W*0.554)}px;top:{int(H*0.50)}px;text-align:center;{L["body"]};color:{WHITE}">{body}</div>'
            f'{panel_l}{panel_r}'
            f'<div class="abs {L["label"]}" style="left:0;right:0;top:{int(H*0.941)}px;text-align:center;font-size:{L["label_size"]}px;opacity:.9">{label}</div>'
            f'</div>')


def close_exact(bg, masthead_text, headline, close_line, hand_line, handle="@_jiing"):
    """D1 page 5, nothing moved: masthead center T7.2% · headline L9.2% T34.6% W78.3% · pill L33.3% T53.3% · badge slot T86.4% = smiley.
    Two lines the template lacks, set in the empty band between pill and badge: her close (27px, T63%) and the hand line (T74%)."""
    L = look()
    size = headline_size(headline, 176, int(H * (0.533 - 0.346)) - 4, int(W * 0.783), em=L["em"])
    g = f'background:{L["grad"]};-webkit-background-clip:text;background-clip:text;color:transparent'
    return (f'<div class="page">{bg}{wash_d1()}'
            f'<div {L["mast"]}>{masthead_text}</div>'
            f'<div class="abs" style="left:{int(W*0.092)}px;width:{int(W*0.783)}px;top:{int(H*0.346)}px;text-align:center;{L["face"]}font-size:{size}px;line-height:.85;letter-spacing:-.02em;{g}">{headline}</div>'
            f'{pill(handle, int(W*0.333) + 40, int(H*0.533))}'
            f'<div class="abs" style="left:{int(W*0.18)}px;width:{int(W*0.64)}px;top:{int(H*0.63)}px;text-align:center;{L["body"]};font-size:29px;color:{WHITE}">{close_line}</div>'
            f'<div class="abs" style="left:0;right:0;top:{int(H*0.74)}px;text-align:center;{HAND}font-size:52px;color:{WHITE}">{hand_line}</div>'
            f'{arrow(int(W*0.42), int(H*0.90), rot=-8, size=190)}'
            f'</div>')


# ------------------------------------------------------------------ the other five grammars' covers, geometry exact (CANVA-GRAMMAR.md)

def cover_moment_exact(src, brand, headline, accent, handle="@_jiing", counter="slide 01", pos="50% 50%"):
    """D2 page 1 (percentages of the 1440 canvas applied to 1350): rules T2.4/8.6/91.3/97.5% · masthead L5.9% T4.4% 26.67px · mark top-right L87.8%
    · headline center L15.9% T25.2% W68% 147.73px · accent center L17.5% T51.8% 191.71px rotated -3.05° · handle L5.9% T93.4% · counter end-aligned T93.4%."""
    rule = lambda t: f'<div class="abs" style="top:{int(H*t)}px;left:0;right:0;height:1.5px;background:{WHITE};opacity:.85"></div>'
    hs = fit(headline, 148, usable=int(W * 0.68), em=0.55); as_ = fit(accent, 192, usable=int(W * 0.65), em=0.58)
    return (f'<div class="page">{photo(src, pos)}{wash("bottom")}'
            f'{rule(0.024)}{rule(0.086)}{rule(0.913)}{rule(0.975)}'
            f'<div class="abs" style="left:{int(W*0.059)}px;top:{int(H*0.044)}px;{SANS}font-weight:500;font-size:26.67px;color:{WHITE}">{brand}</div>'
            f'{sparkle(int(W*0.878), int(H*0.049), 40)}'
            f'<div class="abs" style="left:{int(W*0.159)}px;width:{int(W*0.68)}px;top:{int(H*0.252)}px;text-align:center;{SERIF}font-size:{hs}px;line-height:.95;color:{WHITE}">{headline}</div>'
            f'<div class="abs" style="left:{int(W*0.175)}px;width:{int(W*0.65)}px;top:{int(H*0.518)}px;text-align:center;{SANS}font-weight:500;font-size:{as_}px;line-height:1;letter-spacing:-.03em;color:{WHITE};transform:rotate(-3.05deg)">{accent}</div>'
            f'<div class="abs" style="left:{int(W*0.059)}px;top:{int(H*0.934)}px;{SANS}font-weight:500;font-size:26.67px;color:{WHITE}">{handle}</div>'
            f'<div class="abs" style="right:{int(W*0.059)}px;top:{int(H*0.934)}px;{SANS}font-weight:500;font-size:26.67px;color:{WHITE};text-align:right">{counter}</div>'
            f'</div>')


def cover_stack_exact(src, brand, tagline, word1, connector, word2, quote, credit, pos="50% 50%"):
    """D3 page 1: masthead L10.8% T8% 28px bold · tagline top-right 28px italic · word1 L10% T20.3% 178.96px · connector italic 78px end-aligned L59.2% T28.1%
    · word2 bold 198.34px under word1 · quote bold-italic 32px L11.7% T51.4% · credit bottom-right (post by: 26.67px / NAME 34.67px bold). Wash dark at the headline corner."""
    s1 = fit(word1, 179, usable=int(W * 0.80), em=0.55); s2 = fit(word2, 198, usable=int(W * 0.80), em=0.55)
    return (f'<div class="page">{photo(src, pos)}{wash("top")}'
            f'<div class="abs" style="left:{int(W*0.108)}px;top:{int(H*0.08)}px;{SERIF}font-weight:700;font-size:28px;color:{WHITE}">{brand}</div>'
            f'<div class="abs" style="right:{int(W*0.108)}px;top:{int(H*0.08)}px;{SERIF}font-style:italic;font-size:28px;line-height:1.2;color:{WHITE};text-align:right">{tagline}</div>'
            f'<div class="abs" style="left:{int(W*0.10)}px;top:{int(H*0.203)}px;{SERIF}font-size:{s1}px;line-height:.95;letter-spacing:-.02em;color:{WHITE}">{word1}</div>'
            f'<div class="abs" style="left:{int(W*0.592)}px;width:{int(W*0.30)}px;top:{int(H*0.281)}px;text-align:right;{SERIF}font-style:italic;font-size:78px;line-height:1;color:{WHITE}">{connector}</div>'
            f'<div class="abs" style="left:{int(W*0.10)}px;top:{int(H*0.203) + int(s1*0.95)}px;{SERIF}font-weight:700;font-size:{s2}px;line-height:.95;letter-spacing:-.02em;color:{WHITE}">{word2}</div>'
            f'<div class="abs" style="left:{int(W*0.117)}px;top:{int(H*0.514)}px;{SERIF}font-weight:700;font-style:italic;font-size:32px;line-height:1.3;color:{WHITE}">{quote}</div>'
            f'<div class="abs" style="right:{int(W*0.108)}px;bottom:{int(H*0.08)}px;text-align:right;{SERIF}color:{WHITE};font-size:26.67px;line-height:1.3">post by:<br><b style="font-size:34.67px">{credit}</b></div>'
            f'</div>')


def extended(src, pos, scale, fill):
    """Studio backdrop extended: a blurred copy fills the frame, the sharp photo sits small on top, edges feathered (same move as cover_exact)."""
    uri = pathlib.Path(src).resolve().as_uri()
    return (f'<div class="abs" style="inset:0;background:{fill}"></div>'
            f'<img src="{uri}" class="abs" style="left:-60px;top:-60px;width:{W+120}px;height:{H+120}px;object-fit:cover;object-position:{pos};filter:blur(48px) brightness(.92)">'
            f'<img src="{uri}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px;object-fit:contain;object-position:{pos};transform:scale({scale});transform-origin:{pos};'
            f'-webkit-mask-image:linear-gradient(90deg, transparent 0%, #000 18%, #000 100%), linear-gradient(180deg, transparent 0%, #000 22%, #000 100%);-webkit-mask-composite:source-in;mask-composite:intersect">')


def cover_guide_exact(src, eyebrow, headline, body, handle="@_jiing", pos="50% 50%", scale=1.0, fill=None):
    """D4 page 1: eyebrow L10% T5.8% 50.67px tracked · headline L10% T16.1% W60.9% 186.84px · body L10% T46.8% W42.6% 40px · divider L10% T53.9% W40%
    · handle L10% T87.6% 50.67px · the rotated doodle L75% T80.9% (76.5°) = the arrow, dropped when a person sits in that corner. All type cream."""
    hs = fit(headline, 187, usable=int(W * 0.609), em=0.55)
    img = placed(src, *fill) if isinstance(fill, tuple) else (extended(src, pos, scale, fill) if fill else photo(src, pos, scale))
    doodle = "" if fill else arrow(int(W*0.75), int(H*0.809), rot=76.5, size=150)
    return (f'<div class="page">{img}{wash("left")}'
            f'<div class="abs caps" style="left:{int(W*0.10)}px;top:{int(H*0.058)}px;font-size:34px;letter-spacing:.18em;color:{CREAM}">{eyebrow}</div>'
            f'<div class="abs grad" style="left:{int(W*0.10)}px;width:{int(W*0.609)}px;top:{int(H*0.161)}px;{SERIF}font-size:{hs}px;line-height:.9;letter-spacing:-.02em">{headline}</div>'
            f'<div class="abs" style="left:{int(W*0.10)}px;width:{int(W*0.426)}px;top:{int(H*0.468)}px;{SANS}font-weight:300;font-size:36px;line-height:1.15;color:{CREAM}">{body}</div>'
            f'<div class="abs" style="left:{int(W*0.10)}px;width:{int(W*0.40)}px;top:{int(H*0.539)}px;height:2px;background:{CREAM};opacity:.9"></div>'
            f'<div class="abs" style="left:{int(W*0.10)}px;top:{int(H*0.876)}px;{SANS}font-weight:500;font-size:44px;letter-spacing:.04em;color:{WHITE}">{handle}</div>'
            f'{doodle}'
            f'</div>')


def cover_urban_exact(src, eyebrow, subhead, headline, body, footer_tag, pos="50% 50%"):
    """D5 page 1, all centered: ring L36.1% T8% W27.8% H7.2% (2px stroke) with the eyebrow inside · subhead T31.3% 81.91px (box widened to the headline's 65.1%
    so one line survives in Playfair) · headline L17.4% T37.9% W65.1% 186.67px · body L27.4% T74.4% W45.3% 26.67px · footer tag T89.6% · grain 10%."""
    hs = fit(headline, 187, usable=int(W * 0.651), em=0.55); ss = fit(subhead, 82, usable=int(W * 0.651), em=0.56)
    return (f'<div class="page">{photo(src, pos)}{wash("top", plateau=True, grain=True)}'
            f'<div class="abs" style="left:{int(W*0.361)}px;top:{int(H*0.08)}px;width:{int(W*0.278)}px;height:{int(H*0.072)}px;border:2px solid {CREAM};border-radius:50%"></div>'
            f'<div class="abs caps" style="left:{int(W*0.361)}px;width:{int(W*0.278)}px;top:{int(H*0.08) + int(H*0.072/2) - 15}px;text-align:center;font-size:22px;letter-spacing:.16em">{eyebrow}</div>'
            f'<div class="abs" style="left:{int(W*0.174)}px;width:{int(W*0.651)}px;top:{int(H*0.313)}px;text-align:center;{SERIF}font-weight:400;font-size:{ss}px;line-height:1;color:{CREAM};white-space:nowrap">{subhead}</div>'
            f'<div class="abs grad" style="left:{int(W*0.174)}px;width:{int(W*0.651)}px;top:{int(H*0.379)}px;text-align:center;{SERIF}font-size:{hs}px;line-height:.9;letter-spacing:-.02em">{headline}</div>'
            f'<div class="abs" style="left:{int(W*0.274)}px;width:{int(W*0.453)}px;top:{int(H*0.744)}px;text-align:center;{SANS}font-weight:300;font-size:26.67px;line-height:1.4;color:{WHITE}">{body}</div>'
            f'<div class="abs caps" style="left:0;right:0;top:{int(H*0.896)}px;text-align:center;font-size:22px">{footer_tag}</div>'
            f'</div>')


def cover_initial_exact(src, rows, eyebrow, body, pos="50% 50%", k=0.76):
    """D6 page 1, the big-initial move: each word = a giant sans initial + the rest in serif, sharing one baseline (flex, align-items: baseline) at the template's
    slots (row 1 top 50px, row 2 top 235px; lefts as given). Sizes ×k because Playfair runs ~0.5em/char against the template face's ~0.31em.
    Eyebrow center T53.1% · body center T85.6% W75.8%."""
    tops = [50, 235]
    ii, rr = int(287.6 * k), int(211.9 * k)
    html = ""
    for r, row in enumerate(rows):
        for (init, rest, left) in row:
            html += (f'<div class="abs" style="left:{left}px;top:{tops[r]}px;display:flex;align-items:baseline;gap:6px;white-space:nowrap">'
                     f'<span style="{SANS}font-weight:500;font-size:{ii}px;line-height:.81;letter-spacing:-.04em;color:{WHITE}">{init}</span>'
                     f'<span style="{SERIF}font-size:{rr}px;line-height:.81;letter-spacing:-.03em;color:{WHITE}">{rest}</span></div>')
    return (f'<div class="page">{photo(src, pos)}{wash("top")}'
            f'{html}'
            f'<div class="abs" style="left:{int(W*0.271)}px;width:{int(W*0.457)}px;top:{int(H*0.531)}px;text-align:center;{SERIF}font-style:italic;font-size:44px;line-height:.9;letter-spacing:-.02em;color:{WHITE}">{eyebrow}</div>'
            f'<div class="abs" style="left:{int(W*0.121)}px;width:{int(W*0.758)}px;top:{int(H*0.856)}px;text-align:center;{SANS}font-weight:300;font-size:34px;line-height:1.15;color:{WHITE}">{body}</div>'
            f'</div>')


# ------------------------------------------------------------------ Edition 01 · the frames (copy: edition-01/CONTENT-PACK.md · photos: edition-01/PHOTO-PLAN.md)
MAST = "The Valley &#183; Tarzana<br>Edition 01"
LOOK = "take-a"   # Farrice 2026-09-02: "I like these two" (A1, A4) — Playfair + ivory gradient + Jost body; "template" = Instrument Serif everywhere


def look():
    if LOOK == "take-a":
        return dict(face="font-family: 'Playfair Display', Georgia, serif;", em=0.5, grad="linear-gradient(180deg, #FFF3D6 0%, #F7F5F2 55%, #FFFFFF 100%)",
                    mast=f'class="abs caps" style="left:0;right:0;top:{int(H*0.072)}px;text-align:center;font-size:22px;line-height:1.5"',
                    body=f"{SANS}font-weight:300;font-size:28px;line-height:1.4", label="caps", label_size=17, panel_small=f"{SANS}font-weight:300;font-size:18px")
    return dict(face=SERIF, em=0.46, grad=IVORY_GRAD,
                mast=f'class="abs sc" style="left:0;right:0;top:{int(H*0.072)}px;text-align:center;font-size:24px;line-height:1.3"',
                body=f"{SERIF}font-size:28px;line-height:1.35", label="sc", label_size=19, panel_small=f"{SERIF}font-size:21px")
POOL = IMG
COVER_PLACE = (200, 470, 1200)   # sharp portrait: left, top, size px — head lands lower right, wall carries the type


def frames():
    """(stem, title, html) for the five Edition 01 frames, then the five other-grammar covers (the system sheet)."""
    return [
        ("Main", "01 · cover", cover_gem_fixed(IMG / "jen-porch-vannuys.jpg", "The Valley &#183; Edition 01<br>Tarzana, September", "this is", "Tarzana.",
            "what $869K buys here this month, a 7am coffee on ventura, and the one house that&#8217;s mine. buying or selling.",
            pos="0% 0%", scale=1.45, face=PLAYFAIR, grad=IVORY, text_top=0.44, size=138, pill_at="under")),
        ("Frame02Laidrey", "02 · place", spot_exact(photo(PH / "listing-04-kitchen.jpg", "50% 100%"),  # PLACEHOLDER for plate A (her Bothwell kitchen)
            MAST, "Laidrey,<br>7am.",
            "18600 ventura blvd. doors open at 7 every day. this is where i&#8217;d meet you before we go look at houses.",
            "laidrey coffee roasters &#183; 18600 ventura blvd &#183; 7am&#8211;5pm daily",
            inset(POOL / "sunlight-through-window-floor-00.jpg", INSET_L, "50% 60%"), inset(PH / "listing-02-living.jpg", INSET_R, "30% 50%"))),  # PLACEHOLDERS for plates B, C
        ("Frame03Bothwell", "03 · her listing", spot_exact(photo(PH / "listing-01-exterior.jpg", "50% 100%"),
            MAST, "Three Buildings.<br>One Lot.",
            "new construction in tarzana: a 5,468 sq ft main house, an 882 sq ft guest house with its own kitchen, a pool. $5,695,000. mine. DM for a private showing.",
            "5421 bothwell rd &#183; tarzana &#183; equity union",
            inset(PH / "listing-02-living.jpg", INSET_L, "50% 60%"), inset(PH / "listing-03-pool.jpg", INSET_R, "50% 70%"))),
        ("Frame04Buys", "04 · what $869K buys", spot_exact(photo(PH / "listing-home-gym-pool.jpg", "50% 100%"),  # PLACEHOLDER for plate D (her older listing)
            MAST, "What $869K<br>Buys Here.",
            "3 bed, 1.5 bath, 1,136 sq ft, a 7,296 sq ft lot with room out back for a small second home. on the market now. not mine.",
            "send me your number, buying or selling &#183; i&#8217;ll send the three i&#8217;d go see",
            inset(POOL / "house-key-lock-00.jpg", INSET_L, "50% 50%"),  # PLACEHOLDER for plate E (CC0 pool)
            fact_panel(INSET_R, "sold in august", "$840K &#8211; $950K", "four tarzana homes, 36 to 119 days on the market"))),
        ("Frame05Close", "05 · close", close_exact(photo(PH / "listing-03-pool.jpg", "50% 0%"),
            MAST, "Send Me<br>the Street.",
            "i&#8217;m here for you. that&#8217;s my job. i do this to protect you and your best interest.",
            "my DMs are open &#8594;")),
        ("SheetMoment", "sheet · D2 moment", cover_moment_exact(PH / "listing-02-living.jpg", "Jen Santulan &#183; The Valley", "Small Valley<br>Moments", "Tarzana.", pos="50% 45%")),
        ("SheetStack", "sheet · D3 stack", cover_stack_exact(PH / "listing-01-exterior.jpg", "Jen Santulan", "buying or selling.<br>the valley.", "Tarzana", "in", "September.",
            "what $869K buys here this month &#8594;", "Jen Santulan", pos="50% 100%")),
        ("SheetGuide", "sheet · D4 city guide", cover_guide_exact(PH / "jen-headshot-studio.jpg", "the valley &#183; edition 01", "$869K in<br>Tarzana.",
            "three homes at one number. a 7am coffee on ventura.", fill=(300, 560, 1000))),
        ("SheetUrban", "sheet · D5 urban guide", cover_urban_exact(PH / "listing-03-pool.jpg", "The Valley &#183; Tarzana", "what $869K buys in", "Tarzana.",
            "three homes at one number, a 7am coffee on ventura, what sold in august, and the one house that&#8217;s mine.",
            "The Valley &#160;/&#160; Edition 01 &#160;/&#160; September", pos="50% 0%")),
        ("SheetInitial", "sheet · D6 big initial", cover_initial_exact(PH / "listing-01-exterior.jpg",
            [[("T", "arzana", 129)], [("t", "his", 40), ("m", "onth", 520)]],
            "the valley &#183; edition 01",
            "what $869K buys here, a 7am coffee on ventura, and the one house that&#8217;s mine.", pos="50% 100%")),
    ]


PNG_NAMES = {"Main": "01-cover", "Frame02Laidrey": "02-laidrey", "Frame03Bothwell": "03-bothwell", "Frame04Buys": "04-what-869k-buys", "Frame05Close": "05-close",
             "SheetMoment": "S2-moment-cover", "SheetStack": "S3-stack-cover", "SheetGuide": "S4-guide-cover", "SheetUrban": "S5-urban-cover", "SheetInitial": "S6-initial-cover"}


def edition01():
    out = OUT / "edition-01"; out.mkdir(exist_ok=True)
    for stem, _, html in frames():
        if not stem.startswith("Sheet"):
            render(html, out / f"{PNG_NAMES[stem]}.png")


def system_sheet():
    out = OUT / "edition-01"; out.mkdir(exist_ok=True)
    for stem, _, html in frames():
        if stem.startswith("Sheet"):
            render(html, out / f"{PNG_NAMES[stem]}.png")


# ------------------------------------------------------------------ Claude Design canvas: every frame becomes a .dc.html artboard, photos ride as small JPEGs
DESIGN_SKILL = pathlib.Path("/private/tmp/claude-501/bundled-skills/2.1.255/10316aa10eb7bae1198ccb2d2246294b/design")
CANVAS = OUT / "edition-01" / "canvas"
DC_STYLE = (f"body{{margin:0;background:#F7F5F2}} .page{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#1E2430}} "
            f".abs{{position:absolute}} .caps{{{SANS}font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:{WHITE}}} "
            f".grad{{background:{IVORY_GRAD};-webkit-background-clip:text;background-clip:text;color:transparent}} a{{color:#1E3A5F}} a:hover{{color:#4C7CA8}}")
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Jost:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap">'


def small_jpeg(src, dst, cap_kb=70):
    """Downsample with sips until the file sits under the canvas budget."""
    for z, q in ((1080, 58), (1080, 46), (960, 42), (860, 38), (760, 34)):
        subprocess.run(["sips", "-Z", str(z), "-s", "format", "jpeg", "-s", "formatOptions", str(q), str(src), "--out", str(dst)], check=True, capture_output=True)
        if dst.stat().st_size <= cap_kb * 1024:
            break
    return dst.stat().st_size // 1024


def take_a_boards():
    """The take-A page: his pick, with his four fixes, as live artboards, plus the original render as an image for reference."""
    her = IMG / "jen-porch-vannuys.jpg"
    sub = "what $869K buys here this month, a 7am coffee on ventura, and the one house that&#8217;s mine. buying or selling."
    mk = lambda **kw: cover_gem_fixed(her, "The Valley &#183; Edition 01<br>Tarzana, September", "this is", "Tarzana.", sub, **kw)
    orig = OUT / "take-A-cover-gem.png"
    img_board = (f'<div class="page"><img src="{orig.resolve().as_uri()}" class="abs" style="inset:0;width:{W}px;height:{H}px"></div>')
    return [
        ("TakeAOriginal", "take A · as you saw it", img_board),
        ("TakeA1", "A1 · four fixes (pill top-right, no arrow, text lower)", mk(pos="100% 0%", scale=1.12, face=PLAYFAIR, grad=IVORY, text_top=0.47)),
        ("TakeA2", "A2 · same, template serif", mk(pos="100% 0%", scale=1.12, face=SERIF, grad=IVORY, text_top=0.47, size=190)),
        ("TakeA4", "A4 · her in the right third", mk(pos="0% 0%", scale=1.45, face=PLAYFAIR, grad=IVORY, text_top=0.44, size=138, pill_at="under")),
    ]


def canvas(title="The Valley · Tarzana · Edition 01", filename="tarzana-edition-01.html"):
    import json
    CANVAS.mkdir(parents=True, exist_ok=True); (CANVAS / "img").mkdir(exist_ok=True)
    images = {}
    boards = []
    page_of = {}
    for stem, t, html in take_a_boards() + frames():
        page_of[stem] = "take-a" if stem.startswith("TakeA") else "edition"
        for uri in set(re.findall(r'src="(file://[^"]+)"', html)):
            src = pathlib.Path(urllib.parse.unquote(uri[len("file://"):]))
            name = src.stem + ".jpg"
            if name not in images:
                kb = small_jpeg(src, CANVAS / "img" / name); images[name] = kb
            html = html.replace(uri, name)
        doc = (f'<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  {FONTS}\n'
               f'  <style>{DC_STYLE}</style>\n</helmet>\n{html}\n</x-dc>\n</body>\n</html>\n')
        (CANVAS / f"{stem}.dc.html").write_text(doc)
        boards.append((stem, t))
    gap = 100
    layout = []
    ta = [b for b in boards if b[0].startswith("TakeA")]; ed = [b for b in boards if not b[0].startswith("TakeA")]
    for i, (stem, t) in enumerate(ta):
        layout.append({"file": f"{stem}.dc.html", "title": t, "x": i * (W + gap), "y": 0, "w": W, "h": H, "page": "take-a"})
    for i, (stem, t) in enumerate(ed):
        row = 0 if i < 5 else 1
        col = i if i < 5 else i - 5
        layout.append({"file": f"{stem}.dc.html", "title": t, "x": col * (W + gap), "y": row * (H + 260), "w": W, "h": H, "page": "edition"})
    manifest = {
        "pages": [{"id": "take-a", "name": "Take A · fixed"}, {"id": "edition", "name": "Edition 01 · take 2 + sheet"}],
        "artboards": layout,
        "annotations": [
            {"id": "take-a-note", "x": 0, "y": -170, "w": 640, "page": "take-a", "text": "Take A, the one you liked, with your four fixes. The source photo is a 360×430 grab from her grid, so she sits dead center and the headline lands on her legs in A1/A2; A4 pushes her right at the cost of sharpness. Her original file (or a one-time upscale) fixes both."},
            {"id": "row-edition", "x": 0, "y": -150, "w": 560, "page": "edition", "text": "Tarzana · Edition 01 · five frames on the Local Gem grammar (Design 1, geometry unmoved). Copy: edition-01/CONTENT-PACK.md. Every number labeled there."},
            {"id": "plates-pending", "x": W + gap, "y": H + 20, "w": 520, "page": "edition", "text": "Frames 2 and 4 carry demo placeholders (her Bothwell kitchen and living room, her older listing, two CC0 pool shots). The real plates A–E (Laidrey storefront, a Tarzana street, a porch step) generate after your go on the cost gate, ~$1–3 total. Her own photo of Laidrey beats a plate."},
            {"id": "row-sheet", "x": 0, "y": H + 260 - 150, "w": 560, "page": "edition", "text": "System sheet · the same cover in the five other grammars (D2 moment, D3 stack, D4 city guide, D5 urban guide, D6 big initial). Pick one per edition; none ships with Edition 01 unless you swap it in."},
        ],
        "launch": {"view": "canvas", "page": "take-a"},
    }
    (CANVAS / "canvas.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    out_html = CANVAS / filename
    cmd = ["node", str(DESIGN_SKILL / "seed-canvas.mjs"), "--template", str(DESIGN_SKILL / "payload.template.html"), "--out", str(out_html), "--title", title, "--canvas", str(CANVAS / "canvas.json")]
    for stem, _ in boards:
        cmd += ["--artboard", str(CANVAS / f"{stem}.dc.html")]
    for name in images:
        cmd += ["--image", str(CANVAS / "img" / name)]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=CANVAS)
    print(r.stdout.strip()); print(r.stderr.strip())
    r = subprocess.run(["node", str(DESIGN_SKILL / "seed-canvas.mjs"), "--check", str(out_html)], capture_output=True, text=True)
    print(r.stdout.strip()); print(r.stderr.strip())
    print("images (KB):", images)
    print("canvas:", out_html, out_html.stat().st_size // 1024, "KB")




# ------------------------------------------------------------------ Take A, fixed (Farrice's verdict, prior session): her framing off, pill badly placed, arrow goes, text a little lower
IVORY = "linear-gradient(180deg, #FFF3D6 0%, #F7F5F2 55%, #FFFFFF 100%)"
PLAYFAIR = "font-family: 'Playfair Display', Georgia, serif;"


def cover_gem_fixed(src, eyebrow, connector, headline, subline, handle="@_jiing", pos="50% 12%", scale=1.0, size=170,
                    face=PLAYFAIR, grad=IVORY, text_top=0.47, pill_at="top-right", arrow_on=False, footer_right="01 / 05"):
    """Take A (cover_gem) with the four fixes. face: PLAYFAIR (as he saw it) or SERIF (Instrument). grad: IVORY (as he saw it) or IVORY_GRAD (steel).
    text_top: the headline block's top as a share of height (was 0.41). pill_at: 'top-right' (beside the masthead) or 'under' (below the subline)."""
    size = fit(headline, size, em=0.5 if face == PLAYFAIR else 0.42)
    g = f'background:{grad};-webkit-background-clip:text;background-clip:text;color:transparent'
    pill_html = pill(handle, W - GUTTER - 290, 74) if pill_at == "top-right" else pill(handle, GUTTER, int(H * text_top) + int(size * 1.9) + 60)
    return f'''<div class="page">{photo(src, pos, scale)}{wash("top", plateau=True, grain=True)}
{masthead(eyebrow)}
<div class="abs" style="left:{GUTTER}px;top:{int(H*text_top)}px;width:{W-2*GUTTER}px">
  <div style="{face}font-style:italic;font-size:{int(size*0.46)}px;line-height:1;color:{CREAM};margin-left:6px">{connector}</div>
  <div style="{face}font-size:{size}px;line-height:.92;letter-spacing:-.02em;margin-top:-6px;{g}">{headline}</div>
  <div style="{SANS}font-weight:300;font-size:28px;line-height:1.4;color:{WHITE};max-width:640px;margin-top:30px">{subline}</div>
</div>
{pill_html}
{arrow(GUTTER - 6, H - 215, rot=-8) if arrow_on else ""}
{footer("the valley &#183; a series", footer_right)}
</div>'''


def take_a_fixed():
    out = OUT / "take-a-fixed"; out.mkdir(exist_ok=True)
    her = IMG / "jen-porch-vannuys.jpg"
    sub = "what $869K buys here this month, a 7am coffee on ventura, and the one house that&#8217;s mine. buying or selling."
    variants = {
        # A1 · as he saw it (Playfair, ivory), the four fixes: her shifted right and up, text lower, pill top-right, no arrow
        "A1-as-seen-fixed": dict(pos="100% 0%", scale=1.12, face=PLAYFAIR, grad=IVORY, text_top=0.47),
        # A2 · same, in the template's condensed serif
        "A2-template-serif": dict(pos="100% 0%", scale=1.12, face=SERIF, grad=IVORY, text_top=0.47, size=190),
        # A3 · her larger, text lowest, pill under the subline
        "A3-her-larger": dict(pos="100% 0%", scale=1.3, face=PLAYFAIR, grad=IVORY, text_top=0.52, pill_at="under"),
        # A4 · her in the right third (the only way this 360px frame gives the type a wall)
        "A4-her-right": dict(pos="0% 0%", scale=1.45, face=PLAYFAIR, grad=IVORY, text_top=0.44, size=138, pill_at="under"),
    }
    for name, kw in variants.items():
        render(cover_gem_fixed(her, "The Valley &#183; Edition 01<br>Tarzana, September", "this is", "Tarzana.", sub, **kw), out / f"{name}.png")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "takes"
    {"takes": takes, "variations": variations, "edition01": edition01, "sheet": system_sheet, "canvas": canvas, "take-a": take_a_fixed}[cmd]()

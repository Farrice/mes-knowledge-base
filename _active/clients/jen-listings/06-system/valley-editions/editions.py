#!/usr/bin/env python3
"""Valley Editions generator — the place-magazine surface for @_jiing (DESIGN.md is the spec).
Archetypes: cover_gem, cover_stack, moment, spot, grid, statement, close. Each returns page HTML;
render() turns it into a 1080x1350 PNG with chrome-headless-shell. Photos are absolute paths.

  python3 editions.py takes      # the two Tarzana · Edition 01 cover takes (A: gem, B: stack)
"""
import glob, html as _html, os, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).parent
SEPT = HERE.parent.parent / "04-deliverables" / "2026-09-01-september-carousels"
IMG = SEPT / "img"
OUT = HERE / "out"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

W, H = 1080, 1350
GUTTER = 108
SERIF = "font-family: 'Playfair Display', Georgia, serif;"
SANS = "font-family: 'Jost', system-ui, sans-serif;"
HAND = "font-family: 'Caveat', cursive;"
CREAM, WHITE, WASH = "#F7F5F2", "#FFFFFF", "15,20,30"
IVORY_GRAD = "linear-gradient(180deg, #FFF3D6 0%, #F7F5F2 55%, #FFFFFF 100%)"

HEAD = f'''<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Jost:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap">
<style>html,body{{margin:0;background:#111}} .page{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#1E2430}}
.abs{{position:absolute}} .caps{{{SANS}font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:{WHITE}}}
.grad{{background:{IVORY_GRAD};-webkit-background-clip:text;background-clip:text;color:transparent}}</style>'''


def fit(text, size, usable=W - 2 * GUTTER, em=0.50):
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


def pill(text, left, top):
    return (f'<div class="abs" style="left:{left}px;top:{top}px;padding:10px 30px;border:1.5px solid {CREAM};border-radius:60px;'
            f'{SANS}font-size:24px;letter-spacing:.06em;color:{WHITE}">{text}</div>')


def arrow(left, top, rot=0, size=180):
    return (f'<svg class="abs" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)" width="{size}" height="{size*0.4:.0f}" viewBox="0 0 180 72" fill="none" '
            f'stroke="{CREAM}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 40 C 60 22, 110 26, 168 36"/><path d="M140 14 L 170 36 L 138 52"/></svg>')


def smiley(left, top, size=110):
    return (f'<svg class="abs" style="left:{left}px;top:{top}px" width="{size}" height="{size*0.6:.0f}" viewBox="0 0 110 66" fill="none" stroke="{CREAM}" stroke-width="5" stroke-linecap="round">'
            f'<path d="M14 40 C 40 70, 80 70, 100 36"/><path d="M30 14 L31 20"/><path d="M76 10 L77 16"/></svg>')


def sparkle(left, top, size=44):
    return (f'<svg class="abs" style="left:{left}px;top:{top}px" width="{size}" height="{size}" viewBox="0 0 44 44" fill="{CREAM}">'
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


def cover_exact(src, eyebrow, line_italic, line_upright, subline, handle="@_jiing", pos="50% 50%", scale=1.0, fill=None, size=166):
    """D1 cover, nothing moved: masthead L5.6% T7.2% · headline L5.3% T16.6% W73% (166px, lh .75, italic first clause)
    · subline L5.3% T38.4% W55% (26px) · badge L5.3% T48% · pill L53% T20.4% · stripe T92% rot 7° · wash 4-stop over top 71%."""
    size = fit(f"{line_italic}<br>{line_upright}", size, usable=int(W * 0.733))
    if fill:  # extend the studio backdrop: a blurred copy of the photo fills the frame, the sharp photo sits small on top, edges feathered
        uri = pathlib.Path(src).resolve().as_uri()
        img = (f'<div class="abs" style="inset:0;background:{fill}"></div>'
               f'<img src="{uri}" class="abs" style="left:-60px;top:-60px;width:{W+120}px;height:{H+120}px;object-fit:cover;object-position:{pos};filter:blur(48px) brightness(.92)">'
               f'<img src="{uri}" class="abs" style="left:0;top:0;width:{W}px;height:{H}px;object-fit:contain;object-position:{pos};transform:scale({scale});transform-origin:{pos};'
               f'-webkit-mask-image:linear-gradient(90deg, transparent 0%, #000 18%, #000 100%), linear-gradient(180deg, transparent 0%, #000 22%, #000 100%);-webkit-mask-composite:source-in;mask-composite:intersect">')
    else:
        img = photo(src, pos, scale)
    return f'''<div class="page">{img}
<div class="abs" style="left:0;top:0;width:{W}px;height:{int(H*0.711)}px;background:linear-gradient(180deg, rgba({WASH},.60) 0%, rgba({WASH},.55) 33%, rgba({WASH},.55) 66%, rgba({WASH},0) 100%)"></div>
<div class="abs" style="left:{int(W*0.056)}px;top:{int(H*0.072)}px;{SANS}font-weight:400;font-size:24px;line-height:1.4;letter-spacing:-.02em;color:{WHITE}">{eyebrow}</div>
<div class="abs grad" style="left:{int(W*0.053)}px;top:{int(H*0.166)}px;width:{int(W*0.733)}px;{SERIF}font-size:{size}px;line-height:.8;letter-spacing:-.02em"><span style="font-style:italic">{line_italic}</span><br>{line_upright}</div>
<div class="abs" style="left:{int(W*0.053)}px;top:{int(H*0.384)}px;width:{int(W*0.554)}px;{SANS}font-weight:300;font-size:26px;line-height:1.4;color:{WHITE}">{subline}</div>
{sparkle(int(W*0.053), int(H*0.48), 40)}
{pill(handle, int(W*0.531), int(H*0.204))}
<div class="abs" style="left:{int(W*0.271)}px;top:{int(H*0.919)}px;width:{int(W*0.648)}px;height:3px;background:{CREAM};opacity:.9;transform:rotate(6.94deg)"></div>
<div class="abs caps" style="left:{int(W*0.053)}px;top:{int(H*0.888)}px;font-size:18px;opacity:.9">the valley &#183; a series</div>
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


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "takes"
    {"takes": takes, "variations": variations}[cmd]()

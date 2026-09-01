#!/usr/bin/env python3
"""Three visual DIRECTIONS for the September carousels, sketched on the condo set
(cover · slide 3 bars · slide 4 dark · slide 7 close). Same copy, three different skins,
each built to fight feed fatigue with real photography. Writes 12 artboards next to itself.

A  photo editorial   — full-bleed place photography + the existing type system
B  field notes       — paper ground, tilted photo prints, tape, handwritten annotations, red pencil
C  color block       — one bold series colour, duotone photography, oversized numerals
"""
import pathlib

OUT = pathlib.Path(__file__).parent

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Caveat:wght@500;600&display=swap">
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
HAND = "font-family: Caveat, 'Bradley Hand', 'Segoe Print', cursive;"
FRAME = "width: 1080px; height: 1350px; box-sizing: border-box; position: relative; overflow: hidden;"

def mast(ink, dim, rule):
    return f'''  <div style="display: flex; flex-direction: column; gap: 26px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 25px; letter-spacing: 0.24em; color: {dim};">FIRST-TIME BUYER FILE</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
  </div>'''

def foot(label, n, c):
    return f'''  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 25px; letter-spacing: 0.22em; color: {c};">{label}</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;7</span>
  </div>'''

def photo(src, style=""):
    return f'<img src="{src}" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; display: block; {style}">'

slides = {}

# =====================================================================
# DIRECTION A — photo editorial
# =====================================================================
slides["DA1"] = f'''<div style="{FRAME} background: #F7F5F2; display: flex; flex-direction: column;">
  <div style="position: relative; height: 820px; overflow: hidden; flex: none;">
    {photo("apartment-building-dusk-03.jpg")}
    <div style="position: absolute; left: 0; right: 0; top: 0; padding: 100px 100px 0;">{mast("#F7F5F2", "#F7F5F2", "rgba(247,245,242,0.55)")}</div>
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; justify-content: flex-end; gap: 34px; padding: 60px 100px 90px;">
    <div style="font-size: 84px; font-weight: 600; line-height: 1.1; color: #1E3A5F; letter-spacing: -0.015em;">the condo has to <span style="{SERIF} font-style: italic; font-weight: 400;">qualify</span> too.</div>
    <div style="display: flex; align-items: center; gap: 28px;">
      <div style="width: 60px; height: 1px; background: #1E3A5F;"></div>
      <div style="font-size: 32px; line-height: 1.45; color: #6B6C70;">what changed on august 3, and what i read before you get attached</div>
    </div>
  </div>
</div>'''

slides["DA2"] = f'''<div style="{FRAME} background: #F7F5F2; display: flex; flex-direction: column;">
  <div style="position: relative; height: 380px; overflow: hidden; flex: none;">
    {photo("sunlight-through-window-floor-00.jpg")}
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 64px 100px 100px;">
    <div style="display: flex; flex-direction: column; gap: 34px;">
      <div style="font-size: 26px; letter-spacing: 0.24em; color: #A6A296;">01 · THE RESERVE FUND</div>
      <div style="font-size: 66px; font-weight: 600; line-height: 1.16; color: #1E3A5F; letter-spacing: -0.01em;">the building's savings account</div>
      <div style="font-size: 34px; line-height: 1.5; color: #6B6C70; max-width: 760px;">roofs, plumbing, balconies. thin reserves are a special assessment waiting to happen.</div>
      <div style="display: flex; flex-direction: column; gap: 30px; padding-top: 6px;">
        <div style="display: flex; flex-direction: column; gap: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline;"><span style="font-size: 30px; font-weight: 500; color: #1E3A5F;">floor today</span><span style="{SERIF} font-size: 54px; font-weight: 500; color: #6B6C70;">10%</span></div>
          <div style="height: 10px; background: #EDE9E2;"><div style="height: 10px; width: 40%; background: #D9D3C8;"></div></div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline;"><span style="font-size: 30px; font-weight: 500; color: #1E3A5F;">from jan 4, 2027</span><span style="{SERIF} font-size: 54px; font-weight: 500; color: #1E3A5F;">15%</span></div>
          <div style="height: 10px; background: #EDE9E2;"><div style="height: 10px; width: 60%; background: #4C7CA8;"></div></div>
        </div>
      </div>
    </div>
{foot("SHARE OF THE BUDGET SET ASIDE", 3, "#A6A296")}
  </div>
</div>'''

slides["DA3"] = f'''<div style="{FRAME} background: #1E3A5F; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
  {photo("front-door-house-00.jpg", "opacity: 0.28; filter: grayscale(0.4);")}
  <div style="position: relative;">{mast("#F7F5F2", "#9FB4CC", "#3A5578")}</div>
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 26px; letter-spacing: 0.24em; color: #9FB4CC;">02 · THE LAST 12 MONTHS OF MINUTES</div>
    <div style="font-size: 92px; font-weight: 600; line-height: 1.14; color: #F7F5F2; letter-spacing: -0.01em;">not exciting.<br><span style="{SERIF} font-style: italic; font-weight: 400; color: #9FB4CC;">very useful.</span></div>
    <div style="display: flex; gap: 36px;"><div style="width: 1px; background: #6F8AAB;"></div><div style="font-size: 37px; line-height: 1.55; color: #E6ECF3; max-width: 700px;">leaks, insurance trouble, and an assessment being &#8220;discussed&#8221; all show up here... <span style="color: #FFFFFF; font-weight: 500;">before they're billed.</span></div></div>
  </div>
{foot("READ THEM BEFORE YOU OFFER", 4, "#9FB4CC")}
</div>'''

slides["DA4"] = f'''<div style="{FRAME} background: #1E3A5F; display: flex; flex-direction: column;">
  <div style="position: relative; height: 640px; overflow: hidden; flex: none;">
    {photo("house-key-lock-00.jpg")}
    <div style="position: absolute; left: 0; right: 0; top: 0; padding: 100px 100px 40px; background: rgba(30,58,95,0.55);">{mast("#F7F5F2", "#F7F5F2", "rgba(247,245,242,0.55)")}</div>
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 64px 100px 90px;">
    <div style="display: flex; flex-direction: column; gap: 34px;">
      <div style="font-size: 80px; font-weight: 600; line-height: 1.14; color: #F7F5F2; letter-spacing: -0.01em;">touring condos <span style="{SERIF} font-style: italic; font-weight: 400; color: #9FB4CC;">this fall?</span></div>
      <div style="font-size: 34px; line-height: 1.5; color: #C9D4E2; max-width: 760px;">send me the address before you write. i'll read the package with you.</div>
      <div style="display: flex; align-items: center; background: #F7F5F2; padding: 30px 44px; align-self: flex-start;"><span style="{SERIF} font-style: italic; font-size: 48px; font-weight: 500; color: #1E3A5F;">send me the address</span></div>
    </div>
{foot("JEN SANTULAN · SFV &amp; LOS ANGELES", 7, "#9FB4CC")}
  </div>
</div>'''

# =====================================================================
# DIRECTION B — field notes
# =====================================================================
PAPER = "#EFE7D8"
INK = "#1E3A5F"
PENCIL = "#C2452D"

def tape(x, y, rot):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 150px; height: 42px; background: rgba(255,250,235,0.78); border: 1px solid rgba(180,160,120,0.35); transform: rotate({rot}deg);"></div>'

def print_(src, x, y, w, h, rot, tapes=""):
    return f'''  <div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; background: #FFFDF8; padding: 18px 18px 54px; box-sizing: border-box; transform: rotate({rot}deg); box-shadow: 0 14px 30px rgba(60,40,20,0.18);">
    <img src="{src}" style="width: 100%; height: 100%; object-fit: cover; display: block;">
  </div>{tapes}'''

def hand(text, x, y, size=44, rot=-3, color=PENCIL):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; {HAND} font-size: {size}px; font-weight: 600; color: {color}; transform: rotate({rot}deg); line-height: 1.1; white-space: nowrap;">{text}</div>'

def circled(n, x, y):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 110px; height: 110px; border: 4px solid {PENCIL}; border-radius: 50%; display: flex; align-items: center; justify-content: center; transform: rotate(-6deg);"><span style="{HAND} font-size: 62px; font-weight: 600; color: {PENCIL};">{n}</span></div>'

slides["DB1"] = f'''<div style="{FRAME} background: {PAPER}; padding: 100px;">
{mast(INK, "#9A8E78", "#D6CBB6")}
{print_("vannuys-blvd-2024.jpg", 100, 260, 640, 520, -4, tape(120, 236, -18) + tape(600, 250, 12))}
{hand("read this before you fall for a unit &#8594;", 560, 700, 40, -8)}
  <div style="position: absolute; left: 100px; right: 100px; bottom: 100px; display: flex; flex-direction: column; gap: 30px;">
    <div style="font-size: 88px; font-weight: 600; line-height: 1.12; color: {INK}; letter-spacing: -0.015em;">the condo has to<br><span style="{SERIF} font-style: italic; font-weight: 400;">qualify</span> too.</div>
    <div style="font-size: 32px; line-height: 1.45; color: #6E6556; max-width: 700px;">what changed on august 3, and what i read before you get attached</div>
  </div>
</div>'''

slides["DB2"] = f'''<div style="{FRAME} background: {PAPER}; padding: 100px; display: flex; flex-direction: column; justify-content: space-between;">
{mast(INK, "#9A8E78", "#D6CBB6")}
  <div style="position: relative; display: flex; flex-direction: column; gap: 40px;">
{circled("01", 800, -30)}
    <div style="font-size: 26px; letter-spacing: 0.24em; color: #9A8E78;">THE RESERVE FUND</div>
    <div style="font-size: 76px; font-weight: 600; line-height: 1.16; color: {INK}; letter-spacing: -0.01em; max-width: 760px;">the building's savings account</div>
    <div style="font-size: 36px; line-height: 1.5; color: #6E6556; max-width: 740px;">roofs, plumbing, balconies. thin reserves are a special assessment waiting to happen.</div>
    <div style="display: flex; flex-direction: column; gap: 34px; padding-top: 10px;">
      <div style="display: flex; align-items: center; gap: 26px;"><div style="width: 320px; height: 48px; border: 3px solid {INK}; box-sizing: border-box;"></div><span style="{HAND} font-size: 52px; font-weight: 600; color: {INK};">10% today</span></div>
      <div style="display: flex; align-items: center; gap: 26px;"><div style="width: 400px; height: 48px; background: {PENCIL}; border: 3px solid {PENCIL}; box-sizing: border-box; transform: rotate(-0.6deg);"></div><span style="{HAND} font-size: 48px; font-weight: 600; color: {PENCIL};">15% from jan 4, 2027</span></div>
    </div>
  </div>
{foot("SHARE OF THE BUDGET SET ASIDE", 3, "#9A8E78")}
</div>'''

slides["DB3"] = f'''<div style="{FRAME} background: {PAPER}; padding: 100px; display: flex; flex-direction: column; justify-content: space-between;">
{mast(INK, "#9A8E78", "#D6CBB6")}
{print_("sunlight-through-window-floor-00.jpg", 620, 250, 380, 300, 5, tape(650, 232, -10))}
  <div style="position: relative; display: flex; flex-direction: column; gap: 40px;">
{circled("02", -14, -40)}
    <div style="font-size: 26px; letter-spacing: 0.24em; color: #9A8E78; padding-left: 130px; padding-top: 20px;">THE LAST 12 MONTHS OF MINUTES</div>
    <div style="font-size: 92px; font-weight: 600; line-height: 1.12; color: {INK}; letter-spacing: -0.01em;">not exciting.<br><span style="{SERIF} font-style: italic; font-weight: 400;">very useful.</span></div>
    <div style="font-size: 36px; line-height: 1.5; color: #6E6556; max-width: 700px;">leaks, insurance trouble, and an assessment being &#8220;discussed&#8221; all show up here... before they're billed.</div>
    <div style="{HAND} font-size: 46px; font-weight: 600; color: {PENCIL}; transform: rotate(-2deg); align-self: flex-start; border-bottom: 3px solid {PENCIL}; padding-bottom: 2px;">ask: anything discussed, not yet billed?</div>
  </div>
{foot("READ THEM BEFORE YOU OFFER", 4, "#9A8E78")}
</div>'''

slides["DB4"] = f'''<div style="{FRAME} background: {PAPER}; padding: 100px;">
{mast(INK, "#9A8E78", "#D6CBB6")}
{print_("house-key-lock-00.jpg", 420, 250, 560, 470, 3, tape(460, 228, -14) + tape(860, 240, 9))}
  <div style="position: absolute; left: 100px; right: 100px; bottom: 100px; display: flex; flex-direction: column; gap: 34px;">
    <div style="font-size: 84px; font-weight: 600; line-height: 1.12; color: {INK}; letter-spacing: -0.015em;">touring condos<br><span style="{SERIF} font-style: italic; font-weight: 400;">this fall?</span></div>
    <div style="font-size: 34px; line-height: 1.5; color: #6E6556; max-width: 640px;">send me the address before you write. i'll read the package with you.</div>
    <div style="{HAND} font-size: 66px; font-weight: 600; color: {PENCIL}; transform: rotate(-3deg); align-self: flex-start; border-bottom: 4px solid {PENCIL};">send me the address</div>
    <div style="display: flex; justify-content: space-between; align-items: baseline; padding-top: 8px;"><span style="font-size: 25px; letter-spacing: 0.22em; color: #9A8E78;">JEN SANTULAN · SFV &amp; LOS ANGELES</span><span style="{SERIF} font-style: italic; font-size: 30px; color: #9A8E78;">7&#8202;/&#8202;7</span></div>
  </div>
</div>'''

# =====================================================================
# DIRECTION C — color block + duotone  (series colour: terracotta)
# =====================================================================
ACC = "#C4663F"
CREAM = "#F7F5F2"

def duotone(src, tint=ACC, opacity=0.82):
    return f'''    <img src="{src}" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; display: block; filter: grayscale(1) contrast(1.15);">
    <div style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background: {tint}; mix-blend-mode: multiply; opacity: {opacity};"></div>'''

slides["DC1"] = f'''<div style="{FRAME} background: {ACC}; display: flex; flex-direction: column;">
  <div style="position: relative; height: 760px; overflow: hidden; flex: none;">
{duotone("apartment-building-dusk-03.jpg")}
    <div style="position: absolute; left: 0; right: 0; top: 0; padding: 100px 100px 0;">{mast(CREAM, CREAM, "rgba(247,245,242,0.5)")}</div>
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; justify-content: flex-end; gap: 30px; padding: 60px 100px 90px;">
    <div style="font-size: 96px; font-weight: 700; line-height: 1.04; color: {CREAM}; letter-spacing: -0.02em;">the condo has to <span style="{SERIF} font-style: italic; font-weight: 400;">qualify</span> too.</div>
    <div style="font-size: 32px; line-height: 1.45; color: #F9E4D8;">what changed on august 3, and what i read before you get attached</div>
  </div>
</div>'''

slides["DC2"] = f'''<div style="{FRAME} background: {CREAM}; padding: 100px; display: flex; flex-direction: column; justify-content: space-between;">
{mast(INK, "#A6A296", "#E0DBD2")}
  <div style="position: relative; display: flex; flex-direction: column; gap: 36px;">
    <div style="font-size: 26px; letter-spacing: 0.24em; color: {ACC};">01 · THE RESERVE FUND</div>
    <div style="display: flex; align-items: baseline; gap: 4px;"><span style="{SERIF} font-size: 300px; font-weight: 500; line-height: 0.9; color: {ACC}; letter-spacing: -0.04em;">15</span><span style="{SERIF} font-style: italic; font-size: 120px; color: {INK};">%</span></div>
    <div style="font-size: 54px; font-weight: 600; line-height: 1.2; color: {INK}; letter-spacing: -0.01em; max-width: 860px;">of the budget set aside for reserves from jan 4, 2027. today the floor is 10%.</div>
    <div style="display: flex; gap: 0; height: 48px;"><div style="width: 40%; background: {INK};"></div><div style="width: 20%; background: {ACC};"></div><div style="flex: 1; background: #EDE9E2;"></div></div>
    <div style="font-size: 32px; line-height: 1.5; color: #6B6C70; max-width: 760px;">roofs, plumbing, balconies. thin reserves are a special assessment waiting to happen.</div>
  </div>
{foot("THE BUILDING'S SAVINGS ACCOUNT", 3, "#A6A296")}
</div>'''

slides["DC3"] = f'''<div style="{FRAME} background: {ACC}; padding: 100px; display: flex; flex-direction: column; justify-content: space-between;">
{mast(CREAM, "#F3D2C2", "rgba(247,245,242,0.45)")}
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 26px; letter-spacing: 0.24em; color: #F3D2C2;">02 · THE LAST 12 MONTHS OF MINUTES</div>
    <div style="font-size: 104px; font-weight: 700; line-height: 1.04; color: {CREAM}; letter-spacing: -0.02em;">not exciting.<br><span style="{SERIF} font-style: italic; font-weight: 400; color: {INK};">very useful.</span></div>
    <div style="font-size: 37px; line-height: 1.55; color: #FBEDE4; max-width: 720px;">leaks, insurance trouble, and an assessment being &#8220;discussed&#8221; all show up here... <span style="color: {INK}; font-weight: 600;">before they're billed.</span></div>
  </div>
{foot("READ THEM BEFORE YOU OFFER", 4, "#F3D2C2")}
</div>'''

slides["DC4"] = f'''<div style="{FRAME} background: {INK}; padding: 100px; display: flex; flex-direction: column; justify-content: space-between;">
{duotone("house-key-lock-00.jpg", INK, 0.88)}
  <div style="position: relative;">{mast(CREAM, "#9FB4CC", "rgba(247,245,242,0.45)")}</div>
  <div style="position: relative; display: flex; flex-direction: column; gap: 40px;">
    <div style="font-size: 96px; font-weight: 700; line-height: 1.06; color: {CREAM}; letter-spacing: -0.02em;">touring condos<br><span style="{SERIF} font-style: italic; font-weight: 400; color: #F3D2C2;">this fall?</span></div>
    <div style="font-size: 36px; line-height: 1.5; color: #E6ECF3; max-width: 700px;">send me the address before you write. i'll read the package with you.</div>
    <div style="display: flex; align-items: center; background: {ACC}; padding: 34px 48px; align-self: flex-start;"><span style="{SERIF} font-style: italic; font-size: 52px; font-weight: 500; color: {CREAM};">send me the address</span></div>
  </div>
{foot("JEN SANTULAN · SFV &amp; LOS ANGELES", 7, "#9FB4CC")}
</div>'''

for name, html in slides.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=html))
print("wrote", len(slides), "direction artboards")

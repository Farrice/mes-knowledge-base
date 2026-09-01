#!/usr/bin/env python3
"""September 2026 carousels for @_jiing — three 7-slide sets in the Lane 1
"warm editorial minimal" system (brand card: _active/clients/jen-team-pilot/agents/jen-brand-card.md).
Copy is final from 2026-09-01-local-signal-slate-v1.md; this file only executes design.
Writes 21 artboards + canvas.json next to itself."""
import json
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">
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

# tokens — ground #F7F5F2 · ink #1E3A5F · ghost #E9E3D9 · hairline #E0DBD2 · grey #6B6C70 · steel #4C7CA8
# dark   — ground #1E3A5F · ghost #24436B · rule #3A5578 · soft #C9D4E2 · dim #9FB4CC

def mast(dark=False):
    ink = "#F7F5F2" if dark else "#1E3A5F"
    rule = "#3A5578" if dark else "#E0DBD2"
    dim = "#9FB4CC" if dark else "#A6A296"
    return f'''  <div style="display: flex; flex-direction: column; gap: 26px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 25px; letter-spacing: 0.24em; color: {dim};">FIRST-TIME BUYER FILE</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
  </div>'''

def foot(label, n, dark=False):
    c = "#9FB4CC" if dark else "#A6A296"
    return f'''  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 25px; letter-spacing: 0.22em; color: {c};">{label}</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;7</span>
  </div>'''

def page(inner, n, label, dark=False, ghost=None):
    bg = "#1E3A5F" if dark else "#F7F5F2"
    ghost_html = ""
    if ghost:
        gc = "#24436B" if dark else "#E9E3D9"
        ghost_html = f'''  <div style="{SERIF} font-size: 560px; font-weight: 500; line-height: 0.9; color: {gc}; position: absolute; top: 200px; right: -40px; letter-spacing: -0.04em;">{ghost}</div>'''
    return f'''<div style="width: 1080px; height: 1350px; background: {bg}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
{ghost_html}
{mast(dark)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
{inner}
  </div>
{foot(label, n, dark)}
</div>'''

def hook(headline_html, dek, ghost):
    """Slide 1: ghosted numeral, headline bottom-left, hairline + dek."""
    return f'''<div style="width: 1080px; height: 1350px; background: #F7F5F2; display: flex; flex-direction: column; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
{mast()}
  <div style="{SERIF} font-size: 560px; font-weight: 500; line-height: 0.9; color: #E9E3D9; position: absolute; top: 200px; right: -40px; letter-spacing: -0.04em;">{ghost}</div>
  <div style="position: absolute; left: 100px; right: 100px; bottom: 100px; display: flex; flex-direction: column; gap: 48px;">
    <div style="font-size: 92px; font-weight: 600; line-height: 1.14; color: #1E3A5F; letter-spacing: -0.015em;">{headline_html}</div>
    <div style="display: flex; align-items: center; gap: 32px;">
      <div style="width: 76px; height: 1px; background: #1E3A5F;"></div>
      <div style="font-size: 36px; line-height: 1.5; color: #6B6C70; max-width: 640px;">{dek}</div>
    </div>
  </div>
</div>'''

def it(text, dark=False):
    c = "#9FB4CC" if dark else "#1E3A5F"
    return f'<span style="{SERIF} font-style: italic; font-weight: 400; color: {c};">{text}</span>'

def eyebrow(text, dark=False):
    c = "#9FB4CC" if dark else "#A6A296"
    return f'<div style="font-size: 26px; letter-spacing: 0.24em; color: {c};">{text}</div>'

def headline(html, dark=False, size=76):
    c = "#F7F5F2" if dark else "#1E3A5F"
    return f'<div style="font-size: {size}px; font-weight: 600; line-height: 1.18; color: {c}; letter-spacing: -0.01em; max-width: 860px;">{html}</div>'

def body(html, dark=False):
    rule = "#3A5578" if dark else "#D9D3C8"
    c = "#C9D4E2" if dark else "#6B6C70"
    return f'''    <div style="display: flex; gap: 36px;">
      <div style="width: 1px; background: {rule};"></div>
      <div style="font-size: 37px; line-height: 1.55; color: {c}; max-width: 700px;">{html}</div>
    </div>'''

def bar(label, value, width, strong=False):
    numc = "#1E3A5F" if strong else "#6B6C70"
    barc = "#4C7CA8" if strong else "#D9D3C8"
    return f'''      <div style="display: flex; flex-direction: column; gap: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-size: 33px; font-weight: 500; color: #1E3A5F;">{label}</span>
          <span style="{SERIF} font-size: 60px; font-weight: 500; color: {numc};">{value}</span>
        </div>
        <div style="height: 10px; background: #EDE9E2;"><div style="height: 10px; width: {width}%; background: {barc};"></div></div>
      </div>'''

def bignum(num, unit=""):
    u = f'<span style="{SERIF} font-style: italic; font-size: 110px; color: #4C7CA8;">{unit}</span>' if unit else ""
    return f'''    <div style="display: flex; align-items: baseline; gap: 6px;">
      <span style="{SERIF} font-size: 280px; font-weight: 500; line-height: 0.95; color: #1E3A5F; letter-spacing: -0.03em;">{num}</span>{u}
    </div>'''

def panels(left_label, left_html, right_label, right_html, dark=False):
    return f'''    <div style="display: flex; gap: 0;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 22px; background: #F7F5F2; padding: 52px 44px;">
        <div style="font-size: 22px; letter-spacing: 0.14em; color: #A6A296;">{left_label}</div>
        <div style="{SERIF} font-size: 44px; font-weight: 500; line-height: 1.3; color: #1E3A5F;">{left_html}</div>
      </div>
      <div style="flex: 1; display: flex; flex-direction: column; gap: 22px; background: {'#24436B' if dark else '#FFFFFF'}; border: 1px solid {'#3A5578' if dark else '#E0DBD2'}; padding: 52px 44px;">
        <div style="font-size: 22px; letter-spacing: 0.14em; color: #9FB4CC;">{right_label}</div>
        <div style="{SERIF} font-size: 44px; font-weight: 500; line-height: 1.3; color: {'#F7F5F2' if dark else '#1E3A5F'};">{right_html}</div>
      </div>
    </div>'''

def cta(headline_html, body_text, ask_text, sources):
    return f'''<div style="width: 1080px; height: 1350px; background: #1E3A5F; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
  <svg style="position: absolute; right: -130px; top: 260px; opacity: 0.10;" width="700" height="700" viewBox="0 0 24 24" fill="none" stroke="#F7F5F2" stroke-width="0.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"></path><path d="M5 10v10h14V10"></path><path d="M10 20v-6h4v6"></path></svg>
{mast(dark=True)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 52px;">
    <div style="font-size: 92px; font-weight: 600; line-height: 1.16; color: #F7F5F2; letter-spacing: -0.01em;">{headline_html}</div>
{body(body_text, dark=True)}
    <div style="display: flex; align-items: center; gap: 30px; background: #F7F5F2; padding: 38px 52px; align-self: flex-start;">
      <span style="{SERIF} font-style: italic; font-size: 54px; font-weight: 500; color: #1E3A5F;">{ask_text}</span>
    </div>
    <div style="font-size: 22px; letter-spacing: 0.1em; line-height: 1.7; color: #7E96B4;">{sources}</div>
  </div>
{foot("JEN SANTULAN · SFV &amp; LOS ANGELES", 7, dark=True)}
</div>'''

slides = {}

# ============ CAROUSEL 1 — the condo has to qualify too ============
slides["Main"] = hook(
    f'the condo has to<br>{it("qualify")} too.',
    "what changed on august 3, and what i read before you get attached",
    "03")

slides["C1S2"] = page(f'''{eyebrow("THE PART NOBODY EXPLAINS")}
    <div style="{SERIF} font-style: italic; font-size: 120px; font-weight: 400; line-height: 1.0; color: #1E3A5F;">you're pre-approved.</div>
    <div style="font-size: 52px; font-weight: 500; line-height: 1.35; color: #1E3A5F; letter-spacing: -0.01em;">credit's clean.<br>the loan still dies.</div>
{body("since august 3, 2026, lenders run a full review of the building on almost every conventional condo loan. the unit passes. <span style='color: #1E3A5F; font-weight: 500;'>the building has to pass too.</span>")}''',
    2, "WHAT CHANGED ON AUGUST 3")

slides["C1S3"] = page(f'''{eyebrow("01 · THE RESERVE FUND")}
{headline("the building's savings account")}
{body("roofs, plumbing, balconies. thin reserves are a special assessment waiting to happen.")}
    <div style="display: flex; flex-direction: column; gap: 36px; padding-top: 10px;">
{bar("floor today", "10%", 40)}
{bar("from jan 4, 2027", "15%", 60, strong=True)}
    </div>''',
    3, "SHARE OF THE BUDGET SET ASIDE")

slides["C1S4"] = page(f'''{eyebrow("02 · THE LAST 12 MONTHS OF MINUTES", dark=True)}
{headline(f'not exciting.<br>{it("very useful.", dark=True)}', dark=True, size=88)}
{body("leaks, insurance trouble, and an assessment being &#8220;discussed&#8221; all show up here... <span style='color: #F7F5F2; font-weight: 500;'>before they're billed.</span>", dark=True)}''',
    4, "READ THEM BEFORE YOU OFFER", dark=True, ghost="12")

slides["C1S5"] = page(f'''{eyebrow("03 · THE MASTER INSURANCE")}
{bignum("$50K")}
{headline("the per-unit deductible ceiling", size=56)}
{body("the building's policy has to carry replacement cost with a per-unit deductible under $50,000. if it doesn't, conventional financing stops.")}''',
    5, "THE BUILDING'S POLICY, NOT YOURS")

slides["C1S6"] = page(f'''{eyebrow("04 · WHO'S BEHIND ON DUES")}
{bignum("15", "%")}
{headline("or more of units 60+ days late and the whole building is non-warrantable.", size=56)}
{body("every owner's loan. not just yours.")}''',
    6, "DELINQUENCY THRESHOLD")

slides["C1S7"] = cta(
    f'touring condos<br>{it("this fall?", dark=True)}',
    "send me the address before you write. i'll read the package with you.",
    "send me the address",
    "SOURCE: FANNIE MAE LENDER LETTER LL-2026-03 · FREDDIE MAC BULLETIN 2026-C · AUGUST 2026")

# ============ CAROUSEL 2 — van nuys is getting a train ============
slides["C2S1"] = hook(
    f'van nuys is getting<br>{it("a train.")}',
    "what it changes for a buyer... and what it doesn't",
    "31")

def fact(num, label):
    return f'''      <div style="display: flex; flex-direction: column; gap: 12px;">
        <span style="{SERIF} font-size: 150px; font-weight: 500; line-height: 0.95; color: #1E3A5F; letter-spacing: -0.03em;">{num}</span>
        <span style="font-size: 26px; letter-spacing: 0.22em; color: #A6A296;">{label}</span>
      </div>'''

slides["C2S2"] = page(f'''{eyebrow("EAST SAN FERNANDO VALLEY LIGHT RAIL")}
    <div style="display: flex; flex-direction: column; gap: 40px;">
{fact("6.7", "MILES")}
      <div style="height: 1px; background: #D9D3C8;"></div>
{fact("11", "STATIONS")}
      <div style="height: 1px; background: #D9D3C8;"></div>
{fact("2031", "OPENING · DECEMBER")}
    </div>
{body("van nuys blvd, from the G line to san fernando road. through van nuys, panorama city, arleta and pacoima.")}''',
    2, "LA METRO · CONTRACT AWARDED AUG 2026")

slides["C2S3"] = page(f'''{eyebrow("01 · WHAT IT DOESN'T DO")}
    <div style="{SERIF} font-style: italic; font-size: 140px; font-weight: 400; line-height: 1.0; color: #1E3A5F;">promise prices.</div>
{body("no one can underwrite 2031 today. anyone telling you the station adds value is guessing.")}''',
    3, "NOT A VALUE CLAIM")

slides["C2S4"] = page(f'''{eyebrow("02 · WHAT IT DOES", dark=True)}
{headline(f'change the {it("timeline", dark=True)} question.', dark=True, size=84)}
{body("how long you stay matters more than what you pay.", dark=True)}
{panels("7-YEAR BUYER", "worth a second look at the corridor.", "2-YEAR BUYER", "you're buying the construction, not the train.", dark=True)}''',
    4, "ASK HOW LONG, NOT HOW MUCH", dark=True)

slides["C2S5"] = page(f'''{eyebrow("03 · THE CONSTRUCTION YEARS ARE REAL")}
{headline("lane closures and detours on van nuys blvd through 2031.")}
{body("the van nuys G line station is closed for its own rebuild until around the end of 2027.")}''',
    5, "PLAN FOR THE DETOURS")

STATIONS = [("oxnard st", "G LINE · VAN NUYS"), ("victory", ""), ("vanowen", ""), ("sherman way", ""),
            ("van nuys / metrolink", "AMTRAK · METROLINK"), ("roscoe", ""), ("nordhoff", ""), ("woodman", ""),
            ("arleta", ""), ("laurel canyon", ""), ("van nuys / san fernando", "SAN FERNANDO RD")]
station_rows = "".join(f'''      <div style="display: flex; align-items: center; gap: 28px; height: 60px;">
        <div style="position: relative; width: 22px; height: 22px; border: 2px solid #1E3A5F; background: {'#1E3A5F' if i in (0, 10) else '#F7F5F2'}; box-sizing: border-box; flex: none;"></div>
        <span style="{SERIF} font-size: 40px; font-weight: 500; color: #1E3A5F; white-space: nowrap;">{name}</span>
        <span style="font-size: 20px; letter-spacing: 0.18em; color: #A6A296; padding-left: 8px;">{tag}</span>
      </div>''' for i, (name, tag) in enumerate(STATIONS))
slides["C2S6"] = page(f'''{eyebrow("04 · THE CORRIDOR TO ACTUALLY LOOK AT")}
{headline("van nuys blvd, oxnard to san fernando road.", size=54)}
    <div style="position: relative; display: flex; flex-direction: column; padding: 6px 0;">
      <div style="position: absolute; left: 10px; top: 30px; bottom: 30px; width: 2px; background: #1E3A5F;"></div>
{station_rows}
    </div>''',
    6, "SOURCE: LA METRO PROJECT STATUS REPORT")

slides["C2S7"] = cta(
    f'how long are you<br>{it("planning to stay?", dark=True)}',
    "tell me... i'll tell you if this changes your math.",
    "tell me your timeline",
    "SOURCES: LA METRO · LA DAILY NEWS AUG 24 2026 · COMMERCIAL OBSERVER AUG 14 2026")

# ============ CAROUSEL 3 — the insurance quote comes before the offer ============
slides["C3S1"] = hook(
    f'the insurance quote comes<br>{it("before the offer")} now.',
    "what october 15 changes",
    "15")

slides["C3S2"] = page(f'''{eyebrow("OCTOBER 15, 2026")}
{bignum("29.1", "%")}
{headline("the california FAIR plan rises, on average.", size=56)}
{body("weighted to wildfire exposure. some homes see far more than the average. some see less.")}''',
    2, "CALIFORNIA DEPARTMENT OF INSURANCE")

rows = "".join(f'''      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 30px 0; border-bottom: 1px solid #D9D3C8;">
        <span style="{SERIF} font-size: 54px; font-weight: 500; color: #1E3A5F;">{p}</span>
        <span style="font-size: 24px; letter-spacing: 0.18em; color: #A6A296;">{t}</span>
      </div>''' for p, t in [("sherman oaks hills", "HILLSIDE"), ("woodland hills", "HILLSIDE"), ("chatsworth", "FOOTHILL"), ("the sylmar fringe", "FOOTHILL")])
slides["C3S3"] = page(f'''{eyebrow("01 · WHO IT HITS")}
{headline("hillside. canyon. foothill.")}
    <div style="display: flex; flex-direction: column; border-top: 1px solid #D9D3C8;">
{rows}
    </div>''',
    3, "WHERE THE WILDFIRE WEIGHTING LANDS")

slides["C3S4"] = page(f'''{eyebrow("02 · WHO IT MOSTLY DOESN'T", dark=True)}
{headline(f'the {it("valley floor.", dark=True)}', dark=True, size=110)}
{body("most homes still get a regular carrier. get the real quote anyway... <span style='color: #F7F5F2; font-weight: 500;'>it's part of the payment.</span>", dark=True)}''',
    4, "BREATHE. THEN GET THE QUOTE.", dark=True)

slides["C3S5"] = page(f'''{eyebrow("03 · THE DATE DETAIL")}
{headline("the policy's start date decides the rate.")}
{panels("EFFECTIVE BEFORE OCT 15", "generally written at today's rate for its term.", "ON OR AFTER OCT 15", "the new rate, from day one.")}
{body("closing anywhere near mid-october? this is a conversation with your insurance broker, early.")}''',
    5, "CONFIRM WITH YOUR BROKER")

slides["C3S6"] = page(f'''{eyebrow("04 · WHAT A FAIR POLICY ACTUALLY IS")}
    <div style="{SERIF} font-style: italic; font-size: 140px; font-weight: 400; line-height: 1.0; color: #1E3A5F;">fire only.</div>
{body("you add a wrap (called DIC) for liability, theft and water. together it usually costs well above a standard policy.")}''',
    6, "FAIR PLAN + WRAP = THE REAL NUMBER")

slides["C3S7"] = cta(
    f'writing an offer<br>{it("this fall?", dark=True)}',
    "send me the address... i'll get the quote in hand before we write.",
    "send me the address",
    "SOURCE: CALIFORNIA DEPARTMENT OF INSURANCE · APPROVED RATE CHANGE EFFECTIVE OCT 15 2026")

# ============ write ============
for name, html in slides.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=html))

order = [
    ("the condo has to qualify too", ["Main", "C1S2", "C1S3", "C1S4", "C1S5", "C1S6", "C1S7"]),
    ("van nuys is getting a train", ["C2S1", "C2S2", "C2S3", "C2S4", "C2S5", "C2S6", "C2S7"]),
    ("the insurance quote comes before the offer", ["C3S1", "C3S2", "C3S3", "C3S4", "C3S5", "C3S6", "C3S7"]),
]
artboards = []
notes = []
X = 1180  # column pitch
ROW = 1560  # pitch between rows of 1350-tall slides

def note(nid, y, text, x=0, w=1100):
    notes.append({"id": nid, "x": x, "y": y, "w": w, "text": text})

# ---- row 1: cover + the look (valley native), the hero row ----
y = 0
note("row1", y - 260, "START HERE. left: the cover. then the seven slides of the new look, valley native: your colors, your line drawings, real valley places, you in the frame. the stamp under the masthead stays in the same spot on every slide, forever; the zip changes when the neighborhood does.")
artboards.append({"file": "P0.dc.html", "title": "start here", "x": 0, "y": y, "w": 1080, "h": 1350})
for col, name in enumerate(["DD1", "DD2", "DD3", "DD4", "DD5", "DD6", "DD7"]):
    artboards.append({"file": f"{name}.dc.html", "title": f"valley native · slide {col + 1}", "x": (col + 1) * X, "y": y, "w": 1080, "h": 1350})

# ---- row 2: the reading row (tall cards) ----
y = ROW
note("row2", y - 260, "THE WORDS. how to read this · the three reel scripts, word for word (hook, script, on-screen text, caption) · filming notes and the don't-say list · the rulebook for the look · the photo bank. click any card to read it big; they scroll.")
tall = [
    ("P1", "how to read this", 2200),
    ("R1", "reel 1 · the condo has to qualify too", 3200),
    ("R2", "reel 2 · van nuys is getting a train", 3200),
    ("R3", "reel 3 · the insurance quote", 3200),
    ("P2", "filming notes + don't say", 2200),
    ("P3", "the rulebook", 4400),
    ("P4", "the photo bank", 2600),
]
for col, (name, title, h) in enumerate(tall):
    artboards.append({"file": f"{name}.dc.html", "title": title, "x": col * X, "y": y, "w": 1080, "h": h, "print": "flow"})

# ---- rows 3-5: the three carousels in the current look ----
y = ROW + 4400 + 400
note("row3", y - 260, "THE THREE CAROUSELS in the current look, one per row. the words are final and every number is sourced on the last slide. once you pick the look, all three get rebuilt in it.\nrow a: the condo has to qualify too (post first). row b: van nuys is getting a train (the opinion is a draft of yours; change it to what you'd say). row c: the insurance quote comes before the offer.")
for row, (title, names) in enumerate(order):
    for col, name in enumerate(names):
        artboards.append({"file": f"{name}.dc.html", "title": f"{['a', 'b', 'c'][row]}.{col + 1} {title}", "x": col * X, "y": y + row * ROW, "w": 1080, "h": 1350})

# ---- row 6: earlier sketches ----
y = y + 3 * ROW + 300
note("row6", y - 260, "EARLIER SKETCHES on the condo set, kept so you can see what was left behind. left four: the current look with big photos. right four: a paper-and-handwriting idea that was the most fun but didn't feel like your grid. valley native keeps its layout ideas in your own look.")
for grp, (title, names) in enumerate([("A · photo editorial", ["DA1", "DA2", "DA3", "DA4"]), ("B · field notes", ["DB1", "DB2", "DB3", "DB4"])]):
    for col, name in enumerate(names):
        label = ["cover", "slide 3", "slide 4", "close"][col]
        artboards.append({"file": f"{name}.dc.html", "title": f"{title} · {label}", "x": (grp * 4 + col) * X + grp * 200, "y": y, "w": 1080, "h": 1350})

canvas = {
    "artboards": artboards,
    "annotations": notes,
    "launch": {"view": "canvas"},
}
(OUT / "canvas.json").write_text(json.dumps(canvas, indent=2))
print("wrote", len(slides), "artboards + canvas.json")

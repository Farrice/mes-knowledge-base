#!/usr/bin/env python3
"""Presentation artboards for the Jen walkthrough: cover, agenda, the three reel cards (copy pulled verbatim
from the slate), filming notes, the rulebook, and the photo bank. Jen-facing language only."""
import pathlib, re, html

HERE = pathlib.Path(__file__).parent
SLATE = HERE.parent / "2026-09-01-local-signal-slate-v1.md"
RULEBOOK = HERE / "VALLEY-NATIVE-RULEBOOK.md"

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Overpass:wght@600&display=swap">
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
SIGN = "font-family: Overpass, Figtree, sans-serif; font-weight: 600; letter-spacing: 0.22em;"
NAVY, STEEL, SOFT, CREAM, HAIR, GREY, DIM = "#1E3A5F", "#4C7CA8", "#C9D4E2", "#F7F5F2", "#E0DBD2", "#6B6C70", "#A6A296"

def mast(dark=False):
    ink = CREAM if dark else NAVY
    dim = "#9FB4CC" if dark else DIM
    rule = "#3A5578" if dark else HAIR
    return f'''  <div style="display: flex; flex-direction: column; gap: 22px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 26px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 22px; letter-spacing: 0.24em; color: {dim};">SEPTEMBER 2026</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
  </div>'''

def stamp(dark=False):
    ink = CREAM if dark else NAVY
    return f'''  <div style="display: flex; align-items: center; gap: 16px;">
    <svg width="44" height="44" viewBox="0 0 44 44" fill="none" stroke="{ink}" stroke-width="2"><circle cx="22" cy="22" r="20"></circle><path d="M8 26l7-8 5 5 6-9 10 12"></path><path d="M9 32h26"></path></svg>
    <div style="display: flex; flex-direction: column; gap: 2px;"><span style="{SIGN} font-size: 20px; color: {ink};">SAN FERNANDO VALLEY</span><span style="{SIGN} font-size: 14px; color: {'#9FB4CC' if dark else DIM};">FROM THE VALLEY</span></div>
  </div>'''

# ---------- tiny markdown -> html (enough for the slate + rulebook) ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r'<strong style="color: %s; font-weight: 600;">\1</strong>' % NAVY, s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*(?!\*)", r'<em style="%s font-style: italic;">\1</em>' % SERIF, s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s

def md_to_html(md, base=30):
    out, i, lines = [], 0, md.splitlines()
    para = []
    def flush():
        if para:
            out.append(f'<p style="margin: 0; font-size: {base}px; line-height: 1.55; color: {GREY};">{inline(" ".join(para))}</p>')
            para.clear()
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush(); i += 1; continue
        if ln.startswith("# "):
            flush(); out.append(f'<h1 style="margin: 0; font-size: {int(base*2.2)}px; font-weight: 600; line-height: 1.1; color: {NAVY}; letter-spacing: -0.015em;">{inline(ln[2:])}</h1>')
        elif ln.startswith("## "):
            flush(); out.append(f'<h2 style="margin: 18px 0 0; font-size: {int(base*1.45)}px; font-weight: 600; line-height: 1.2; color: {NAVY};">{inline(ln[3:])}</h2>')
        elif ln.startswith("### "):
            flush(); out.append(f'<h3 style="margin: 10px 0 0; {SIGN} font-size: {int(base*0.8)}px; color: {STEEL};">{html.escape(ln[4:].upper())}</h3>')
        elif ln.startswith("---"):
            flush(); out.append(f'<div style="height: 1px; background: {HAIR};"></div>')
        elif ln.startswith(">"):
            flush(); q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip()); i += 1
            body = "<br>".join(inline(x) for x in q)
            out.append(f'<div style="display: flex; gap: 26px;"><div style="width: 2px; background: {STEEL}; flex: none;"></div><div style="font-size: {base}px; line-height: 1.6; color: {NAVY};">{body}</div></div>')
            continue
        elif ln.lstrip().startswith(("- ", "* ")):
            flush(); items = []
            while i < len(lines) and lines[i].lstrip().startswith(("- ", "* ")):
                items.append(lines[i].lstrip()[2:]); i += 1
            lis = "".join(f'<li style="margin: 0 0 10px;">{inline(x)}</li>' for x in items)
            out.append(f'<ul style="margin: 0; padding-left: 34px; font-size: {base}px; line-height: 1.5; color: {GREY};">{lis}</ul>')
            continue
        elif re.match(r"^\d+\. ", ln):
            flush(); items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i])); i += 1
            lis = "".join(f'<li style="margin: 0 0 12px;">{inline(x)}</li>' for x in items)
            out.append(f'<ol style="margin: 0; padding-left: 40px; font-size: {base}px; line-height: 1.5; color: {GREY};">{lis}</ol>')
            continue
        elif ln.startswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            rows = [r for r in rows if not all(set(c) <= set("-: ") for c in r)]
            trs = ""
            for k, r in enumerate(rows):
                tds = "".join(f'<td style="padding: 12px 18px 12px 0; border-bottom: 1px solid {HAIR}; font-size: {int(base*0.85)}px; line-height: 1.4; color: {NAVY if k == 0 else GREY}; {"font-weight: 600;" if k == 0 else ""} vertical-align: top;">{inline(c)}</td>' for c in r)
                trs += f"<tr>{tds}</tr>"
            out.append(f'<table style="border-collapse: collapse; width: 100%;">{trs}</table>')
            continue
        else:
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)

def flow(body_html, dark=False, pad=100):
    bg = NAVY if dark else CREAM
    return f'''<div style="width: 1080px; background: {bg}; display: flex; flex-direction: column; gap: 40px; padding: {pad}px; box-sizing: border-box;">
{mast(dark)}
{stamp(dark)}
  <div style="display: flex; flex-direction: column; gap: 28px;">
{body_html}
  </div>
</div>'''

slides = {}

# ---------- P0 cover ----------
slides["P0"] = f'''<div style="width: 1080px; height: 1350px; background: {CREAM}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
  <svg style="position: absolute; right: -40px; top: 180px; opacity: 0.9;" width="620" height="420" viewBox="0 0 620 420" fill="none" stroke="{SOFT}" stroke-width="2"><path d="M0 300 L120 190 L200 250 L300 130 L420 260 L520 170 L620 280"></path><path d="M0 340 H620"></path><rect x="140" y="250" width="70" height="90"></rect><rect x="330" y="230" width="60" height="110"></rect><path d="M470 340 v-70 l35-30 l35 30 v70"></path></svg>
{mast()}
  <div style="position: relative; display: flex; flex-direction: column; gap: 40px;">
{stamp()}
    <div style="font-size: 104px; font-weight: 600; line-height: 1.06; color: {NAVY}; letter-spacing: -0.02em;">september,<br>for <span style="{SERIF} font-style: italic; font-weight: 400;">jen.</span></div>
    <div style="display: flex; align-items: center; gap: 28px;"><div style="width: 60px; height: 1px; background: {NAVY};"></div><div style="font-size: 34px; line-height: 1.45; color: {GREY}; max-width: 700px;">three reels, three carousels, and a look for your grid that says you're from here.</div></div>
  </div>
  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 24px; letter-spacing: 0.22em; color: {DIM};">A WALKTHROUGH · ABOUT 15 MINUTES</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {DIM};">start here</span>
  </div>
</div>'''

# ---------- P1 agenda / walkthrough ----------
agenda = f'''
<h1 style="margin: 0; font-size: 66px; font-weight: 600; line-height: 1.1; color: {NAVY}; letter-spacing: -0.015em;">how to read this</h1>
<p style="margin: 0; font-size: 30px; line-height: 1.55; color: {GREY};">everything for september is on this one canvas, in rows. here's the order.</p>
<div style="display: flex; flex-direction: column; gap: 26px;">
  <div style="display: flex; gap: 26px;"><span style="{SERIF} font-style: italic; font-size: 60px; color: {STEEL}; width: 70px; flex: none; line-height: 1;">1</span><div><div style="font-size: 34px; font-weight: 600; color: {NAVY};">the look: valley native (top row)</div><div style="font-size: 28px; line-height: 1.5; color: {GREY};">the condo carousel built in a new look for your grid. your colors, your line drawings, real valley places, you in the frame. the rulebook and the photo bank are in the row below it.</div></div></div>
  <div style="display: flex; gap: 26px;"><span style="{SERIF} font-style: italic; font-size: 60px; color: {STEEL}; width: 70px; flex: none; line-height: 1;">2</span><div><div style="font-size: 34px; font-weight: 600; color: {NAVY};">the three reels (this row)</div><div style="font-size: 28px; line-height: 1.5; color: {GREY};">each one is a tall card: the hook, the script, what goes on screen, and the caption. pick the one you'd actually say first. the condo one is my top pick.</div></div></div>
  <div style="display: flex; gap: 26px;"><span style="{SERIF} font-style: italic; font-size: 60px; color: {STEEL}; width: 70px; flex: none; line-height: 1;">3</span><div><div style="font-size: 34px; font-weight: 600; color: {NAVY};">all three carousels, copy approved (the three rows below)</div><div style="font-size: 28px; line-height: 1.5; color: {GREY};">the words are final and sourced. once you pick the look, all three get rebuilt in it.</div></div></div>
</div>
<div style="height: 1px; background: {HAIR};"></div>
<h2 style="margin: 0; font-size: 44px; font-weight: 600; color: {NAVY};">three things only you can answer</h2>
<ul style="margin: 0; padding-left: 34px; font-size: 30px; line-height: 1.55; color: {GREY};">
  <li style="margin-bottom: 12px;">which reel would you say first, in your words?</li>
  <li style="margin-bottom: 12px;">does the valley native look feel like you? what would you change?</li>
  <li style="margin-bottom: 12px;">how many could you actually film in one sitting? the plan assumes two reels and one carousel a week.</li>
</ul>
<div style="display: flex; gap: 26px;"><div style="width: 2px; background: {STEEL}; flex: none;"></div><div style="font-size: 30px; line-height: 1.6; color: {NAVY};">the photos of you on page 2 are pulled from your grid as placeholders. three quick phone shots replace them: you on a van nuys sidewalk, you at a condo building's front door, you holding an HOA packet.</div></div>
'''
slides["P1"] = flow(agenda)

# ---------- reel cards from the slate, verbatim ----------
slate = SLATE.read_text()
concepts = re.split(r"\n## (?=\d\. )", slate)[1:]
titles = []
for n, block in enumerate(concepts[:3], 1):
    title_line, _, rest = block.partition("\n")
    title = re.sub(r"^\d\. ", "", title_line).replace("(my top pick)", "").strip()
    titles.append(title)
    subject = re.search(r"\*the subject:\*(.+?)\n", rest)
    reel = rest.split("### reel")[1].split("### carousel")[0] if "### reel" in rest else rest
    reel_head, _, reel_body = reel.partition("\n")
    body = f'''
<div style="{SIGN} font-size: 22px; color: {STEEL};">REEL {n} OF 3{"  ·  MY TOP PICK" if n == 1 else ""}</div>
<h1 style="margin: 0; font-size: 72px; font-weight: 600; line-height: 1.08; color: {NAVY}; letter-spacing: -0.015em;">{inline(title)}</h1>
<div style="display: flex; gap: 26px;"><div style="width: 2px; background: {STEEL}; flex: none;"></div><div style="font-size: 30px; line-height: 1.6; color: {NAVY};">{inline((subject.group(1) if subject else "").strip())}</div></div>
<div style="{SIGN} font-size: 20px; color: {DIM};">{html.escape(reel_head.strip(" ·").upper())}</div>
{md_to_html(reel_body, base=29)}
'''
    slides[f"R{n}"] = flow(body)

# ---------- P2 filming notes + don't say ----------
notes = slate.split("## filming notes")[1] if "## filming notes" in slate else ""
slides["P2"] = flow(f'''
<h1 style="margin: 0; font-size: 66px; font-weight: 600; line-height: 1.1; color: {NAVY}; letter-spacing: -0.015em;">filming notes</h1>
{md_to_html(notes.replace("## don't say", "## don't say").replace("## ", "## ", 1), base=29)}
''')

# ---------- P3 rulebook ----------
rb = RULEBOOK.read_text()
slides["P3"] = flow(md_to_html(rb, base=28))

# ---------- P4 photo bank ----------
photos = [
    ("jen-porch-vannuys.jpg", "you · van nuys porch", "from your grid · swap for an original"),
    ("jen-frontdoor.jpg", "you · front door", "from your grid · swap for an original"),
    ("jen-portrait.jpg", "you · portrait", "from your grid · swap for an original"),
    ("vannuys-blvd-2024.jpg", "van nuys blvd · oct 2024", "real · cleared"),
    ("vannuys-valerio-2024.jpg", "van nuys blvd at valerio · oct 2024", "real · cleared"),
    ("vannuys-street-scene.jpg", "van nuys blvd · street scene", "real · cleared"),
    ("sfv-aerial-nara.jpg", "the valley from above · 1933", "archive · cleared"),
    ("apartment-building-dusk-03.jpg", "condo balconies · dusk", "real · cleared"),
    ("california-bungalow-00.jpg", "california bungalow", "real · cleared"),
    ("valley-street-01.jpg", "palm-lined street · archive", "archive · cleared"),
    ("house-key-lock-00.jpg", "keys in the door", "real · cleared"),
    ("sunlight-through-window-floor-00.jpg", "morning light", "real · cleared"),
]
cells = "".join(f'''
  <div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="border: 2px solid {NAVY}; padding: 10px; background: #FFFFFF;"><img src="{f}" style="width: 100%; height: 300px; object-fit: cover; display: block;"></div>
    <div style="{SIGN} font-size: 16px; color: {NAVY};">{html.escape(cap.upper())}</div>
    <div style="font-size: 20px; color: {GREY};">{html.escape(tag)}</div>
  </div>''' for f, cap, tag in photos)
slides["P4"] = flow(f'''
<h1 style="margin: 0; font-size: 66px; font-weight: 600; line-height: 1.1; color: {NAVY}; letter-spacing: -0.015em;">the photo bank</h1>
<p style="margin: 0; font-size: 30px; line-height: 1.55; color: {GREY};">every photo in the look is real. the valley shots are cleared for your feed with no credit needed. the three of you are placeholders from your own grid until you send originals.</p>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 40px 30px;">{cells}</div>
''')

for name, h in slides.items():
    (HERE / f"{name}.dc.html").write_text(HEAD.format(body=h))
print("wrote", len(slides), "presentation artboards:", ", ".join(slides))

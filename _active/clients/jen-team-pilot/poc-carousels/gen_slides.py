#!/usr/bin/env python3
"""POC carousels v2 — elevated editorial system. Writes all 12 artboards incl. Main."""
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

# ============ BUYER LANE — warm editorial minimal ============
# ground #F7F5F2 · ink #1E3A5F · ghost #E9E3D9 · hairline #E0DBD2 · grey #6B6C70

def b_mast(dark=False):
    ink = "#F7F5F2" if dark else "#1E3A5F"
    rule = "#3A5578" if dark else "#E0DBD2"
    return f'''  <div style="display: flex; flex-direction: column; gap: 26px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 25px; letter-spacing: 0.24em; color: {'#9FB4CC' if dark else '#A6A296'};">FIRST-TIME BUYER FILE</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
  </div>'''

def b_num(n, dark=False):
    c = "#9FB4CC" if dark else "#A6A296"
    return f'''<span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;6</span>'''

buyers = {}

buyers["Main"] = f'''<div style="width: 1080px; height: 1350px; background: #F7F5F2; display: flex; flex-direction: column; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
{b_mast()}
  <div style="{SERIF} font-size: 560px; font-weight: 500; line-height: 0.9; color: #E9E3D9; position: absolute; top: 200px; right: -40px; letter-spacing: -0.04em;">20</div>
  <div style="position: absolute; left: 100px; right: 100px; bottom: 100px; display: flex; flex-direction: column; gap: 48px;">
    <div style="font-size: 94px; font-weight: 600; line-height: 1.14; color: #1E3A5F; letter-spacing: -0.015em;">you don't need<br><span style="{SERIF} font-style: italic; font-weight: 500;">20 percent down</span><br>to buy a home in LA</div>
    <div style="display: flex; align-items: center; gap: 32px;">
      <div style="width: 76px; height: 1px; background: #1E3A5F;"></div>
      <div style="font-size: 36px; line-height: 1.5; color: #6B6C70; max-width: 640px;">what buyers here actually put down, and the programs that close the gap</div>
    </div>
  </div>
</div>'''

buyers["Buyer2"] = f'''<div style="width: 1080px; height: 1350px; background: #F7F5F2; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box;">
{b_mast()}
  <div style="display: flex; flex-direction: column; gap: 56px;">
    <div style="{SERIF} font-style: italic; font-size: 150px; font-weight: 400; line-height: 1.0; color: #1E3A5F;">the myth</div>
    <div style="font-size: 52px; font-weight: 500; line-height: 1.35; color: #1E3A5F; letter-spacing: -0.01em;">save $200K first,<br>then start looking.</div>
    <div style="display: flex; gap: 36px;">
      <div style="width: 1px; background: #D9D3C8;"></div>
      <div style="display: flex; flex-direction: column; gap: 26px; max-width: 700px;">
        <div style="font-size: 37px; line-height: 1.55; color: #6B6C70;">the LA median is around $1M, so the math feels impossible from the outside.</div>
        <div style="font-size: 37px; line-height: 1.55; color: #6B6C70;">but most first-time buyers here don't put 20% down. <span style="color: #1E3A5F; font-weight: 500;">down-payment programs exist for exactly this gap</span> — and they change through the year.</div>
      </div>
    </div>
  </div>
  <div style="display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 26px; letter-spacing: 0.24em; color: #A6A296;">THE PART NOBODY EXPLAINS</span>
    {b_num(2)}
  </div>
</div>'''

buyers["Buyer3"] = f'''<div style="width: 1080px; height: 1350px; background: #F7F5F2; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box;">
{b_mast()}
  <div style="display: flex; flex-direction: column; gap: 40px;">
    <div style="font-size: 26px; letter-spacing: 0.24em; color: #A6A296;">PROGRAM · CALHFA MYHOME</div>
    <div style="display: flex; align-items: baseline; gap: 6px;">
      <span style="{SERIF} font-size: 300px; font-weight: 500; line-height: 0.95; color: #1E3A5F; letter-spacing: -0.03em;">3.5</span>
      <span style="{SERIF} font-style: italic; font-size: 110px; color: #4C7CA8;">%</span>
    </div>
    <div style="font-size: 44px; font-weight: 500; line-height: 1.4; color: #1E3A5F; max-width: 780px;">of the purchase price, covered — for your down payment or closing costs.</div>
    <div style="display: flex; gap: 36px;">
      <div style="width: 1px; background: #D9D3C8;"></div>
      <div style="font-size: 34px; line-height: 1.55; color: #6B6C70; max-width: 680px;">a deferred-payment junior loan for california first-time buyers: no monthly payments on that piece while you live in the home.</div>
    </div>
  </div>
  <div style="display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 24px; letter-spacing: 0.12em; color: #A6A296;">SOURCE: CALHFA 2026 · CONFIRM AVAILABILITY</span>
    {b_num(3)}
  </div>
</div>'''

buyers["Buyer4"] = f'''<div style="width: 1080px; height: 1350px; background: #1E3A5F; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
  <div style="{SERIF} font-size: 640px; font-weight: 500; line-height: 0.85; color: #24436B; position: absolute; bottom: -110px; right: -60px; letter-spacing: -0.04em;">20</div>
{b_mast(dark=True)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 48px;">
    <div style="font-size: 88px; font-weight: 600; line-height: 1.18; color: #F7F5F2; letter-spacing: -0.01em; max-width: 860px;">some programs have covered up to <span style="{SERIF} font-style: italic; font-weight: 500; color: #9FB4CC;">20 percent</span> down</div>
    <div style="display: flex; gap: 36px;">
      <div style="width: 1px; background: #3A5578;"></div>
      <div style="display: flex; flex-direction: column; gap: 26px; max-width: 700px;">
        <div style="font-size: 37px; line-height: 1.55; color: #C9D4E2;">state assistance has covered as much as a fifth of the purchase price for eligible first-time buyers.</div>
        <div style="font-size: 37px; line-height: 1.55; color: #C9D4E2;">which ones are open and funded changes month to month. <span style="color: #F7F5F2; font-weight: 500;">tracking that is literally my job</span> — so you don't have to refresh a state website.</div>
      </div>
    </div>
  </div>
  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 26px; letter-spacing: 0.24em; color: #9FB4CC;">ASK WHAT IS OPEN RIGHT NOW</span>
    {b_num(4, dark=True)}
  </div>
</div>'''

buyers["Buyer5"] = f'''<div style="width: 1080px; height: 1350px; background: #F7F5F2; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box;">
{b_mast()}
  <div style="display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 74px; font-weight: 600; line-height: 1.2; color: #1E3A5F; letter-spacing: -0.01em;">the cost <span style="{SERIF} font-style: italic; font-weight: 400;">nobody warns you about</span></div>
    <div style="font-size: 38px; line-height: 1.55; color: #6B6C70; max-width: 760px;">closing costs run about 2-3% of the price — separate from your down payment.</div>
    <div style="display: flex; flex-direction: column; gap: 0px;">
      <div style="height: 1px; background: #D9D3C8;"></div>
      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 34px 0;">
        <span style="font-size: 34px; color: #6B6C70;">on a $750K home</span>
        <span style="{SERIF} font-size: 96px; font-weight: 500; color: #1E3A5F; letter-spacing: -0.02em;">$15-22.5K</span>
      </div>
      <div style="height: 1px; background: #D9D3C8;"></div>
      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 34px 0;">
        <span style="font-size: 34px; color: #6B6C70;">when to budget it</span>
        <span style="{SERIF} font-style: italic; font-size: 52px; color: #4C7CA8;">from day one</span>
      </div>
      <div style="height: 1px; background: #D9D3C8;"></div>
    </div>
  </div>
  <div style="display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 26px; letter-spacing: 0.24em; color: #A6A296;">NO SURPRISES AT THE FINISH LINE</span>
    {b_num(5)}
  </div>
</div>'''

buyers["Buyer6"] = f'''<div style="width: 1080px; height: 1350px; background: #1E3A5F; display: flex; flex-direction: column; justify-content: space-between; padding: 100px; box-sizing: border-box; position: relative; overflow: hidden;">
  <svg style="position: absolute; right: -130px; top: 260px; opacity: 0.10;" width="700" height="700" viewBox="0 0 24 24" fill="none" stroke="#F7F5F2" stroke-width="0.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="15" r="4"></circle><path d="M10.8 12.2 21 2"></path><path d="M17 6l3 3"></path><path d="M14 9l2 2"></path></svg>
{b_mast(dark=True)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 52px;">
    <div style="font-size: 92px; font-weight: 600; line-height: 1.16; color: #F7F5F2; letter-spacing: -0.01em;">want the <span style="{SERIF} font-style: italic; font-weight: 400; color: #9FB4CC;">real numbers</span> for your situation?</div>
    <div style="display: flex; gap: 36px;">
      <div style="width: 1px; background: #3A5578;"></div>
      <div style="font-size: 38px; line-height: 1.55; color: #C9D4E2; max-width: 680px;">rent vs. buy. what's open right now. what you'd actually need saved. no pressure — just the math.</div>
    </div>
    <div style="display: flex; align-items: center; gap: 30px; background: #F7F5F2; padding: 38px 52px; align-self: flex-start;">
      <span style="font-size: 30px; letter-spacing: 0.2em; color: #6B6C70;">DM ME</span>
      <span style="{SERIF} font-style: italic; font-size: 62px; font-weight: 500; color: #1E3A5F;">&#8220;keys&#8221;</span>
    </div>
  </div>
  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 26px; letter-spacing: 0.24em; color: #9FB4CC;">JEN SANTULAN · SFV &amp; LOS ANGELES</span>
    {b_num(6, dark=True)}
  </div>
</div>'''

# ============ SELLER LANE — quiet luxury print ============
# navy #16304F · panel #1E3A5F · white #FFFFFF · steel #4C7CA8 · soft #C9D4E2 · warm grey #8B93A5

def s_frame(inner, ground, border):
    return f'''<div style="width: 1080px; height: 1350px; background: {ground}; padding: 44px; box-sizing: border-box;">
  <div style="width: 100%; height: 100%; border: 1px solid {border}; padding: 64px 72px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;">
{inner}
  </div>
</div>'''

def s_lockup(ink, dim):
    return f'''    <div style="display: flex; justify-content: center; align-items: center; gap: 26px;">
      <span style="font-size: 30px; letter-spacing: 0.06em; color: {ink};"><span style="font-weight: 400;">HOUSE</span><span style="font-weight: 600;">SELLERS</span></span>
      <span style="width: 1px; height: 34px; background: {dim};"></span>
      <span style="font-size: 21px; letter-spacing: 0.26em; color: {dim};">EQUITY UNION REAL ESTATE</span>
    </div>'''

def s_foot(label, n, ink, dim):
    return f'''    <div style="display: flex; justify-content: space-between; align-items: baseline; border-top: 1px solid {dim}; padding-top: 30px;">
      <span style="font-size: 24px; letter-spacing: 0.3em; color: {ink};">{label}</span>
      <span style="{SERIF} font-style: italic; font-size: 30px; color: {ink};">{n}&#8202;/&#8202;6</span>
    </div>'''

sellers = {}

sellers["Seller1"] = s_frame(f'''{s_lockup("#FFFFFF", "#5A7292")}
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 52px;">
      <div style="width: 1px; height: 90px; background: #4C7CA8;"></div>
      <div style="{SERIF} font-size: 100px; font-weight: 500; line-height: 1.12; color: #FFFFFF; letter-spacing: 0.05em;">RENOVATING<br>BEFORE<br>YOU SELL?</div>
      <div style="{SERIF} font-style: italic; font-size: 50px; line-height: 1.4; color: #C9D4E2;">most Valley sellers fix<br>the wrong things.</div>
      <div style="font-size: 27px; letter-spacing: 0.22em; line-height: 1.9; color: #7E96B4;">WHAT THE COST-VS-VALUE DATA<br>ACTUALLY SAYS · SWIPE</div>
    </div>
{s_foot("THE VALLEY", 1, "#7E96B4", "#3A5578")}''', "#16304F", "#3A5578")

sellers["Seller2"] = s_frame(f'''{s_lockup("#1E3A5F", "#B9C2D0")}
    <div style="display: flex; flex-direction: column; gap: 0;">
      <div style="display: flex; flex-direction: column; gap: 20px; padding-bottom: 52px;">
        <div style="font-size: 25px; letter-spacing: 0.3em; color: #8B93A5;">THE INSTINCT</div>
        <div style="{SERIF} font-style: italic; font-size: 92px; font-weight: 400; line-height: 1.1; color: #1E3A5F;">remodel the kitchen.</div>
      </div>
      <div style="height: 1px; background: #D8DDE6;"></div>
      <div style="display: flex; flex-direction: column; gap: 20px; padding-top: 52px;">
        <div style="font-size: 25px; letter-spacing: 0.3em; color: #8B93A5;">THE DATA</div>
        <div style="{SERIF} font-size: 66px; font-weight: 500; line-height: 1.22; color: #1E3A5F;">Small, visible fixes beat big renovations — almost every time.</div>
        <div style="font-size: 35px; line-height: 1.6; color: #5C6579; max-width: 760px; padding-top: 14px;">A $90K kitchen rarely comes back at sale. Paint, landscaping, and the repairs that clear inspection objections usually do.</div>
      </div>
    </div>
{s_foot("THE VALLEY", 2, "#8B93A5", "#D8DDE6")}''', "#FFFFFF", "#D8DDE6")

def roi_row(label, pct, width, strong=False):
    numc = "#1E3A5F" if strong else "#5C6579"
    barc = "#4C7CA8" if strong else "#C7D2DF"
    return f'''      <div style="display: flex; flex-direction: column; gap: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <span style="font-size: 33px; font-weight: 500; color: #1E3A5F;">{label}</span>
          <span style="{SERIF} font-size: 54px; font-weight: 500; color: {numc};">{pct}</span>
        </div>
        <div style="height: 10px; background: #EEF1F5;"><div style="height: 10px; width: {width}%; background: {barc};"></div></div>
      </div>'''

sellers["Seller3"] = s_frame(f'''{s_lockup("#1E3A5F", "#B9C2D0")}
    <div style="display: flex; flex-direction: column; gap: 54px;">
      <div style="display: flex; flex-direction: column; gap: 18px;">
        <div style="font-size: 25px; letter-spacing: 0.3em; color: #8B93A5;">RETURN AT RESALE</div>
        <div style="{SERIF} font-size: 72px; font-weight: 500; line-height: 1.15; color: #1E3A5F;">What actually<br>comes back</div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 40px;">
{roi_row("Garage door replacement", "268%", 100, strong=True)}
{roi_row("Steel entry door", "216%", 81)}
{roi_row("Stone veneer · curb appeal", "208%", 78)}
{roi_row("Bathroom remodel", "50%", 19)}
      </div>
      <div style="font-size: 24px; letter-spacing: 0.06em; color: #8B93A5;">2025 COST VS. VALUE REPORT · NATIONAL SAMPLE FIGURES — YOUR HOUSE IS ITS OWN CASE</div>
    </div>
{s_foot("THE VALLEY", 3, "#8B93A5", "#D8DDE6")}''', "#FFFFFF", "#D8DDE6")

sellers["Seller4"] = s_frame(f'''{s_lockup("#FFFFFF", "#5A7292")}
    <div style="display: flex; flex-direction: column; gap: 56px;">
      <div style="{SERIF} font-size: 84px; font-weight: 500; line-height: 1.22; color: #FFFFFF;">Buyers don't fall in love with your finishes.</div>
      <div style="{SERIF} font-style: italic; font-size: 60px; line-height: 1.3; color: #9FB4CC;">They fall out of love with your deferred maintenance.</div>
      <div style="display: flex; gap: 34px;">
        <div style="width: 1px; background: #3A5578;"></div>
        <div style="font-size: 35px; line-height: 1.6; color: #C9D4E2; max-width: 720px;">Roof. HVAC. Water heater. The drip you stopped noticing. These surface in inspection, shake confidence, and complicate escrow more than any dated countertop ever will.</div>
      </div>
    </div>
{s_foot("THE VALLEY", 4, "#7E96B4", "#3A5578")}''', "#16304F", "#3A5578")

sellers["Seller5"] = s_frame(f'''{s_lockup("#1E3A5F", "#B9C2D0")}
    <div style="display: flex; flex-direction: column; gap: 50px;">
      <div style="{SERIF} font-size: 72px; font-weight: 500; line-height: 1.15; color: #1E3A5F;">Pricing beats<br>renovating</div>
      <div style="display: flex; gap: 0;">
        <div style="flex: 1; display: flex; flex-direction: column; gap: 22px; background: #16304F; padding: 52px 44px;">
          <div style="font-size: 21px; letter-spacing: 0.14em; color: #7E96B4;">PRICED RIGHT, DAY ONE</div>
          <div style="{SERIF} font-size: 84px; font-weight: 500; color: #FFFFFF; line-height: 1;">23-35</div>
          <div style="font-size: 30px; line-height: 1.5; color: #C9D4E2;">days on market —<br>often over asking</div>
        </div>
        <div style="flex: 1; display: flex; flex-direction: column; gap: 22px; background: #FFFFFF; border: 1px solid #D8DDE6; padding: 52px 44px;">
          <div style="font-size: 21px; letter-spacing: 0.14em; color: #8B93A5;">&#8220;TESTING THE MARKET&#8221;</div>
          <div style="{SERIF} font-size: 84px; font-weight: 500; color: #8B93A5; line-height: 1;">60+</div>
          <div style="font-size: 30px; line-height: 1.5; color: #8B93A5;">days — then selling<br>5-8% below</div>
        </div>
      </div>
      <div style="font-size: 24px; letter-spacing: 0.06em; color: #8B93A5;">SAMPLE MARKET FIGURES — WE RUN YOUR STREET'S ACTUAL COMPS BEFORE PICKING A NUMBER</div>
    </div>
{s_foot("THE VALLEY", 5, "#8B93A5", "#D8DDE6")}''', "#FFFFFF", "#D8DDE6")

sellers["Seller6"] = s_frame(f'''{s_lockup("#1E3A5F", "#B9C2D0")}
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 48px;">
      <div style="width: 1px; height: 70px; background: #4C7CA8;"></div>
      <div style="{SERIF} font-size: 88px; font-weight: 500; line-height: 1.18; color: #1E3A5F;">Thinking of selling<br>this year?</div>
      <div style="font-size: 36px; line-height: 1.6; color: #5C6579; max-width: 720px;">We'll walk your house room by room and tell you what's worth fixing — and what to leave exactly as it is.</div>
      <div style="display: flex; align-items: center; gap: 28px; background: #16304F; padding: 36px 56px;">
        <span style="font-size: 28px; letter-spacing: 0.22em; color: #7E96B4;">DM US</span>
        <span style="{SERIF} font-style: italic; font-size: 56px; font-weight: 500; color: #FFFFFF;">&#8220;sell&#8221;</span>
      </div>
    </div>
{s_foot("THE VALLEY · MYHOUSESELLERS.COM", 6, "#8B93A5", "#D8DDE6")}''', "#FFFFFF", "#D8DDE6")

for name, body in {**buyers, **sellers}.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=body))
    print("wrote", name)

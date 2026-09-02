#!/usr/bin/env python3
"""Valley Native · PHOTO — the same copy engine wearing Jen's own look (2026-09-02).
Full-bleed real photograph, soft dark wash for legibility, white serif headline, a handwritten accent line,
her signature lockup at the foot. No line drawings, no stamp block, no navy slides. Proof set: PH1 (cover), PH2 (a
middle slide), PH3 (the close) of the condo carousel. Photos are placeholders until her listing photography lands."""
import pathlib
from gen_valley import HEAD, FRAME

OUT = pathlib.Path(__file__).parent
SERIF = "font-family: 'Playfair Display', Georgia, serif;"
HAND = "font-family: 'Caveat', 'Bradley Hand', cursive;"
SANS = "font-family: 'Jost', 'Figtree', system-ui, sans-serif;"
WHITE = "#FFFFFF"

HEAD_PHOTO = HEAD.replace(
    "family=Figtree",
    "family=Caveat:wght@500;600&family=Jost:wght@300;400;500&family=Figtree")


def photo(src, pos="50% 50%", wash=0.42):
    return f'''  <img src="{src}" style="position: absolute; inset: 0; width: 1080px; height: 1350px; object-fit: cover; object-position: {pos};">
  <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(20,24,32,{wash - 0.12}) 0%, rgba(20,24,32,{wash}) 55%, rgba(20,24,32,{wash + 0.18}) 100%);"></div>'''


def lockup():
    return f'''  <div style="position: absolute; left: 0; right: 0; bottom: 64px; display: flex; flex-direction: column; align-items: center; gap: 2px;">
    <span style="{HAND} font-size: 44px; color: {WHITE}; line-height: 1;">Jen Santulan</span>
    <span style="{SANS} font-size: 15px; font-weight: 400; letter-spacing: 0.34em; color: rgba(255,255,255,0.85);">REALTOR&#174; &#183; SAN FERNANDO VALLEY</span>
  </div>'''


def serif(text, size=96, weight=400):
    return f'<div style="{SERIF} font-size: {size}px; font-weight: {weight}; line-height: 1.04; letter-spacing: -0.02em; color: {WHITE}; text-align: center; text-shadow: 0 2px 24px rgba(0,0,0,0.25);">{text}</div>'


def hand(text, size=52):
    return f'<div style="{HAND} font-size: {size}px; font-weight: 500; color: {WHITE}; text-align: center; line-height: 1.1;">{text}</div>'


def body(text, size=32, width=760):
    return f'<div style="{SANS} font-size: {size}px; font-weight: 300; line-height: 1.5; color: rgba(255,255,255,0.94); text-align: center; max-width: {width}px;">{text}</div>'


slides = {}

slides["PH1"] = f'''<div style="{FRAME} background: #1E2430;">
{photo("jen-frontdoor.jpg", pos="50% 20%", wash=0.40)}
  <div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; padding: 120px 90px 200px;">
    {serif("what if the building<br>is the problem...<br><em>not me?</em>", size=92)}
    {hand("the four things i read before you write &#8594;", size=46)}
  </div>
{lockup()}
</div>'''

slides["PH2"] = f'''<div style="{FRAME} background: #1E2430;">
{photo("sunlight-through-window-floor-00.jpg", pos="50% 50%", wash=0.50)}
  <div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px; padding: 120px 100px 200px;">
    {hand("no. 1", size=54)}
    {serif("The savings account.", size=88)}
    {body("i open the budget before i look at the balcony. i&#8217;m looking for one thing: how much the building sets aside every month for the roof, the pipes, the elevator.", size=31)}
    {body("<b style='font-weight: 500;'>10% of the budget today. 15% for loans dated january 4 or later.</b>", size=29, width=700)}
  </div>
{lockup()}
</div>'''

slides["PH3"] = f'''<div style="{FRAME} background: #1E2430;">
{photo("jen-porch-vannuys.jpg", pos="50% 0%", wash=0.44)}
  <div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 34px; padding: 120px 100px 200px;">
    {serif("Send me the address<br>before you write.", size=84)}
    {body("we&#8217;ll read the four documents together and go from there.", size=31, width=680)}
    {body("i&#8217;m here for you. that&#8217;s my job.<br>i do this to protect you and your best interest.", size=29, width=720)}
    {hand("my DMs are open &#8594;", size=50)}
  </div>
{lockup()}
</div>'''

if __name__ == "__main__":
    for name, html in slides.items():
        (OUT / f"{name}.dc.html").write_text(HEAD_PHOTO.format(body=html))
    print("wrote", ", ".join(slides))

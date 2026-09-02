#!/usr/bin/env python3
"""Valley Native, sets 2 and 3: the light-rail carousel (Van Nuys · 91401) and the insurance carousel
(Sherman Oaks · 91403). Same system as gen_valley.py (imported for its line art and furniture), copy written
plain-with-punch, every close on her own words. Writes DR1..DR7 and DI1..DI7 next to itself."""
import pathlib
from gen_valley import (HEAD, SERIF, SIGN, FRAME, INK, STEEL, SOFT, CREAM, HAIR, GREY, DIMC, DIMD, GHOSTD, RULED,
                        svg, valley_map, arrow, ring, stamp_mark, it, eyebrow, body, print_, marker)

OUT = pathlib.Path(__file__).parent


# ---- furniture with a rotating stamp -----------------------------------------------------------
def stamp(zipline, dark=False):
    ink = CREAM if dark else INK
    dim = "#7E96B4" if dark else GREY
    return f'''    <div style="display: flex; align-items: center; gap: 18px; padding-top: 4px;">
      {stamp_mark(44, ink)}
      <div style="display: flex; flex-direction: column; gap: 3px;">
        <span style="{SIGN} font-size: 22px; font-weight: 600; letter-spacing: 0.2em; color: {ink};">{zipline}</span>
        <span style="{SIGN} font-size: 15px; font-weight: 400; letter-spacing: 0.28em; color: {dim};">FROM THE VALLEY</span>
      </div>
    </div>'''


def mast(zipline, dark=False):
    ink = CREAM if dark else INK
    rule = RULED if dark else HAIR
    dim = DIMD if dark else DIMC
    return f'''  <div style="position: relative; display: flex; flex-direction: column; gap: 26px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 25px; letter-spacing: 0.24em; color: {dim};">THE VALLEY FILE</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
{stamp(zipline, dark)}
  </div>'''


def foot(label, n, dark=False):
    c = DIMD if dark else DIMC
    return f'''  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 25px; letter-spacing: 0.22em; color: {c};">{label}</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;7</span>
  </div>'''


def shell(zipline, inner, label, n, dark=False, absolute=""):
    bg = INK if dark else CREAM
    return f'''<div style="{FRAME} background: {bg}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
{absolute}
{mast(zipline, dark)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 38px;">
{inner}
  </div>
{foot(label, n, dark)}
</div>'''


def cover(zipline, photo, cap, headline_html, dek, obj_pos="50% 30%", pw=370, ph=462):
    return f'''<div style="{FRAME} background: {CREAM}; display: flex; flex-direction: column; padding: 100px;">
  <div style="position: absolute; right: -200px; top: 152px;">{valley_map(660, 660, SOFT, 2)}</div>
{mast(zipline)}
  <div style="position: absolute; right: 92px; top: 250px;">
{print_(photo, pw, ph, rot=-1.5, obj_pos=obj_pos, cap=cap)}
  </div>
  <div style="position: absolute; left: 372px; top: 506px;">{arrow(190, 86, INK, "transform: rotate(-8deg);")}</div>
  <div style="position: absolute; left: 100px; right: 100px; bottom: 100px; display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 70px; font-weight: 600; line-height: 1.14; color: {INK}; letter-spacing: -0.015em; max-width: 880px;">{headline_html}</div>
    <div style="display: flex; align-items: center; gap: 32px;">
      <div style="width: 76px; height: 1px; background: {INK}; flex: none;"></div>
      <div style="font-size: 36px; line-height: 1.5; color: {GREY}; max-width: 620px;">{dek}</div>
    </div>
  </div>
</div>'''


def keyed(zipline, eyebrow_txt, italic, sans, body_html, stops, label):
    """Slide 2: the keyed map. Four numbered stops on one drawn line, each with a drawn glyph."""
    cols = "".join(f'''        <div style="width: 190px; display: flex; justify-content: center; align-items: flex-end; height: 120px;">{g}</div>''' for g, _ in stops)
    labels = "".join(f'''        <div style="width: 190px; display: flex; flex-direction: column; align-items: center; gap: 14px;">
          {marker(f"0{i + 1}")}
          <div style="{SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.16em; line-height: 1.5; color: {INK}; text-align: center;">{lab}</div>
        </div>''' for i, (_, lab) in enumerate(stops))
    return shell(zipline, f'''{eyebrow(eyebrow_txt)}
    <div style="{SERIF} font-style: italic; font-size: 94px; font-weight: 400; line-height: 1.0; color: {INK};">{italic}</div>
    <div style="font-size: 46px; font-weight: 500; line-height: 1.32; color: {INK}; letter-spacing: -0.01em;">{sans}</div>
{body(body_html, width=800, size=31)}
    <div style="display: flex; flex-direction: column; gap: 0; padding-top: 4px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-end;">
{cols}
      </div>
      <div style="height: 2px; background: {INK};"></div>
      <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-top: 22px;">
{labels}
      </div>
    </div>''', label, 2)


def close(zipline, photo, cap, headline_html, body_html, source, obj_pos="50% 14%", img_h=None):
    pr = print_(photo, 300, 286, rot=1.5, dark=True, img_h=img_h, obj_pos=obj_pos, cap=cap)
    return f'''<div style="{FRAME} background: {INK}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
  <div style="position: absolute; right: -180px; top: 170px;">{valley_map(640, 640, GHOSTD, 2)}</div>
{mast(zipline, dark=True)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
    <div style="font-size: 80px; font-weight: 600; line-height: 1.16; color: {CREAM}; letter-spacing: -0.01em;">{headline_html}</div>
    <div style="display: flex; gap: 46px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 40px;">
{body(body_html, dark=True, width=440, size=31)}
        <div style="display: flex; align-items: center; background: {CREAM}; padding: 30px 42px; align-self: flex-start;">
          <span style="{SERIF} font-style: italic; font-size: 46px; font-weight: 500; color: {INK}; white-space: nowrap;">my DMs are open</span>
        </div>
      </div>
      <div style="flex: none;">{pr}</div>
    </div>
  </div>
  <div style="position: relative; display: flex; flex-direction: column; gap: 30px;">
    <div style="font-size: 22px; letter-spacing: 0.1em; line-height: 1.7; color: #7E96B4;">{source}</div>
{foot("JEN SANTULAN &#183; SFV &amp; LOS ANGELES", 7, dark=True)}
  </div>
</div>'''


def panels(l_label, l_html, r_label, r_html, dark=False):
    lbg, rbg = (CREAM, GHOSTD) if dark else (CREAM, "#FFFFFF")
    rborder = RULED if dark else HAIR
    rtext = CREAM if dark else INK
    return f'''    <div style="display: flex; gap: 0;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 22px; background: {lbg}; padding: 46px 40px;">
        <div style="{SIGN} font-size: 17px; font-weight: 600; letter-spacing: 0.16em; color: {GREY};">{l_label}</div>
        <div style="{SERIF} font-size: 40px; font-weight: 500; line-height: 1.3; color: {INK};">{l_html}</div>
      </div>
      <div style="flex: 1; display: flex; flex-direction: column; gap: 22px; background: {rbg}; border: 1px solid {rborder}; padding: 46px 40px;">
        <div style="{SIGN} font-size: 17px; font-weight: 600; letter-spacing: 0.16em; color: {DIMD if dark else GREY};">{r_label}</div>
        <div style="{SERIF} font-size: 40px; font-weight: 500; line-height: 1.3; color: {rtext};">{r_html}</div>
      </div>
    </div>'''


# ---- glyphs for the keyed maps ---------------------------------------------------------------
def station(w=110, h=100):
    """A drawn light-rail platform with a canopy and one car."""
    return svg(w, h, "0 0 110 100", [
        "M6 92 H104", "M14 92 V70 H96 V92", "M22 70 V40 M88 70 V40", "M10 40 H100",
        "M30 62 H80 V80 H30 Z", "M30 71 H80", "M40 62 V80 M60 62 V80",
    ])


def price_tag_x(w=110, h=100):
    """A crossed-out price tag: what the train doesn't do."""
    return svg(w, h, "0 0 110 100", [
        "M20 30 H70 L94 50 L70 70 H20 Z", "M32 50 H36", "M8 88 L102 12",
    ])


def calendar(w=110, h=100):
    return svg(w, h, "0 0 110 100", [
        "M16 22 H94 V90 H16 Z", "M16 40 H94", "M34 12 V30 M76 12 V30",
        "M30 54 H42 M50 54 H62 M70 54 H82 M30 70 H42 M50 70 H62",
    ])


def cone(w=110, h=100):
    return svg(w, h, "0 0 110 100", [
        "M42 88 L54 16 L66 88", "M26 88 H84", "M46 48 H62 M43 66 H65",
    ])


def house_hill(w=110, h=100):
    return svg(w, h, "0 0 110 100", [
        "M4 90 C 30 60 60 50 106 44", "M40 74 V54 L58 40 L76 54 V74 Z", "M52 74 V62 H64 V74",
        "M84 34 C 84 26 92 26 92 34 M88 26 V18",
    ])


def house_flat(w=110, h=100):
    return svg(w, h, "0 0 110 100", [
        "M6 88 H104", "M30 88 V56 L55 38 L80 56 V88 Z", "M48 88 V72 H62 V88", "M36 64 H44 V72 H36 Z M66 64 H74 V72 H66 Z",
    ])


def flame(w=110, h=100):
    return svg(w, h, "0 0 110 100", [
        "M55 14 C 40 40 30 46 30 64 C 30 80 42 90 55 90 C 68 90 80 80 80 64 C 80 52 72 44 66 38 C 66 50 60 54 56 52 C 58 42 58 30 55 14 Z",
    ])


slides = {}

# =====================================================================================
# SET 2 · the light rail · VAN NUYS · 91401
# =====================================================================================
VN = "VAN NUYS &#183; 91401"

slides["DR1"] = cover(VN, "vannuys-valerio-2024.jpg", "VAN NUYS BLVD &#183; 91401",
                      f'that torn-up median on van nuys blvd...<br>{it("is a train.")}',
                      "and it doesn&#8217;t open until december 2031.", obj_pos="50% 40%")

slides["DR2"] = keyed(VN, "WHAT&#8217;S ACTUALLY COMING", "eleven stations.", "van nuys to pacoima.",
                      "the east valley light rail runs down the middle of van nuys blvd, from the G line to san fernando road. metro signed the $2.43 billion contract in august... <span style='color: " + INK + "; font-weight: 500;'>so it&#8217;s real. it&#8217;s just five years out.</span>",
                      [(price_tag_x(), "WHAT IT DOESN&#8217;T DO"), (calendar(), "WHAT IT DOES"), (cone(), "THE CONSTRUCTION YEARS"), (station(), "THE STATIONS")],
                      "OPENING DECEMBER 2031")

def fact(num, label):
    return f'''      <div style="display: flex; flex-direction: column; gap: 8px;">
        <span style="{SERIF} font-size: 118px; font-weight: 500; line-height: 0.95; color: {INK}; letter-spacing: -0.03em;">{num}</span>
        <span style="{SIGN} font-size: 17px; font-weight: 600; letter-spacing: 0.22em; color: {GREY};">{label}</span>
      </div>'''

slides["DR3"] = shell(VN, f'''{eyebrow("01 &#183; WHAT IT DOESN&#8217;T DO")}
    <div style="font-size: 62px; font-weight: 600; line-height: 1.16; color: {INK}; letter-spacing: -0.01em;">it doesn&#8217;t promise prices.</div>
{body("nobody can put a number on 2031 today. anyone telling you the station adds value is guessing... <span style='color: " + INK + "; font-weight: 500;'>and you&#8217;d be paying for the guess.</span>", width=780, size=31)}
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding-top: 10px; border-bottom: 2px solid {INK}; padding-bottom: 26px;">
{fact("6.7", "MILES")}
{fact("11", "STATIONS")}
{fact("2031", "OPENING &#183; DECEMBER")}
    </div>''', "LA METRO &#183; CONTRACT AWARDED AUG 2026", 3)

slides["DR4"] = shell(VN, f'''{eyebrow("02 &#183; WHAT IT DOES", dark=True)}
    <div style="font-size: 78px; font-weight: 600; line-height: 1.14; color: {CREAM}; letter-spacing: -0.01em;">it changes the<br>{it("timeline", dark=True)} question.</div>
{body("how long you stay matters more than what you pay.", dark=True, width=700, size=34)}
{panels("7-YEAR BUYER", "the blocks people skip for the traffic deserve a second look.", "2-YEAR BUYER", "you&#8217;d be buying five years of construction, not a train.", dark=True)}''',
                      "ASK HOW LONG, NOT HOW MUCH", 4, dark=True)

blvd_print = print_("vannuys-street-scene.jpg", 330, 300, rot=-1.5, obj_pos="50% 70%", cap="VAN NUYS BLVD &#183; 91401")
slides["DR5"] = shell(VN, f'''{eyebrow("03 &#183; THE CONSTRUCTION YEARS")}
    <div style="display: flex; gap: 46px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 34px;">
        <div style="font-size: 58px; font-weight: 600; line-height: 1.16; color: {INK}; letter-spacing: -0.01em;">lane closures and detours through 2031.</div>
{body("and the van nuys G line station is closed for its own rebuild until around the end of 2027. <span style='color: " + INK + "; font-weight: 500;'>plan around the detours, not the ribbon-cutting.</span>", width=440, size=31)}
      </div>
      <div style="flex: none; padding-top: 6px;">{blvd_print}</div>
    </div>''', "PLAN FOR THE DETOURS", 5)

STATIONS = [("oxnard st", "G LINE"), ("victory", ""), ("vanowen", ""), ("sherman way", ""), ("van nuys / metrolink", "AMTRAK &#183; METROLINK"),
            ("roscoe", ""), ("nordhoff", ""), ("woodman", ""), ("arleta", ""), ("laurel canyon", ""), ("van nuys / san fernando", "SAN FERNANDO RD")]
rows = "".join(f'''      <div style="display: flex; align-items: center; gap: 26px; height: 58px;">
        <div style="position: relative; width: 20px; height: 20px; border: 2px solid {INK}; background: {INK if i in (0, 10) else CREAM}; box-sizing: border-box; flex: none;"></div>
        <span style="{SERIF} font-size: 38px; font-weight: 500; color: {INK}; white-space: nowrap;">{n}</span>
        <span style="{SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.18em; color: {GREY}; padding-left: 6px;">{t}</span>
      </div>''' for i, (n, t) in enumerate(STATIONS))
slides["DR6"] = shell(VN, f'''{eyebrow("04 &#183; THE STATIONS")}
    <div style="font-size: 52px; font-weight: 600; line-height: 1.18; color: {INK}; letter-spacing: -0.01em;">the corridor to actually look at.</div>
    <div style="position: relative; display: flex; flex-direction: column; padding: 4px 0;">
      <div style="position: absolute; left: 9px; top: 29px; bottom: 29px; width: 2px; background: {INK};"></div>
{rows}
    </div>''', "SOURCE: LA METRO PROJECT STATUS REPORT", 6)

slides["DR7"] = close(VN, "jen-porch-vannuys.jpg", "JEN &#183; VAN NUYS",
                      f'tell me how long<br>{it("you&#8217;re staying.", dark=True)}',
                      "i&#8217;ll tell you if the train changes your math... and that&#8217;s usually the whole conversation. i&#8217;m here for you... i do this to protect you and your best interest.",
                      "SOURCES: LA METRO &#183; LA DAILY NEWS AUG 24 2026 &#183; COMMERCIAL OBSERVER AUG 14 2026", obj_pos="50% 0%", img_h=380)

# =====================================================================================
# SET 3 · the insurance quote · SHERMAN OAKS · 91403
# =====================================================================================
SO = "SHERMAN OAKS &#183; 91403"

slides["DI1"] = cover(SO, "sfv-aerial-nara.jpg", "SAN FERNANDO VALLEY &#183; 1933",
                      f'fully approved... and the insurance quote<br>{it("still moves your payment.")}',
                      "what october 15 changes.", obj_pos="50% 50%")

slides["DI2"] = keyed(SO, "THE PART NOBODY EXPLAINS", "october 15.", "the state&#8217;s backup fire policy goes up.",
                      "the california FAIR plan is what you get when no regular company will cover the house. on october 15 it rises 29.1% on average... <span style='color: " + INK + "; font-weight: 500;'>weighted to wildfire, so hillsides move a lot more.</span>",
                      [(house_hill(), "WHO IT HITS"), (house_flat(), "WHO IT MOSTLY DOESN&#8217;T"), (calendar(), "THE DATE DETAIL"), (flame(), "WHAT IT ACTUALLY COVERS")],
                      "CALIFORNIA DEPARTMENT OF INSURANCE")

hill_rows = "".join(f'''      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 22px 0; border-bottom: 1px solid #D9D3C8;">
        <span style="{SERIF} font-size: 44px; font-weight: 500; color: {INK};">{p}</span>
        <span style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.18em; color: {GREY};">{t}</span>
      </div>''' for p, t in [("sherman oaks hills", "HILLSIDE"), ("woodland hills", "HILLSIDE"), ("chatsworth", "FOOTHILL"), ("the sylmar fringe", "FOOTHILL")])
slides["DI3"] = shell(SO, f'''{eyebrow("01 &#183; WHO IT HITS")}
    <div style="display: flex; align-items: baseline; gap: 6px;">
      <span style="{SERIF} font-size: 150px; font-weight: 500; line-height: 0.95; color: {INK}; letter-spacing: -0.03em;">29.1</span><span style="{SERIF} font-style: italic; font-size: 80px; color: {STEEL};">%</span>
    </div>
    <div style="font-size: 48px; font-weight: 600; line-height: 1.2; color: {INK}; letter-spacing: -0.01em;">is the average. hillsides, canyons and foothills can move far more.</div>
    <div style="display: flex; flex-direction: column; border-top: 1px solid #D9D3C8;">
{hill_rows}
    </div>''', "WHERE THE WILDFIRE WEIGHTING LANDS", 3)

floor_print = print_("valley-street-01.jpg", 300, 230, rot=1.5, dark=True, obj_pos="50% 60%", cap="THE VALLEY FLOOR")
slides["DI4"] = shell(SO, f'''{eyebrow("02 &#183; WHO IT MOSTLY DOESN&#8217;T", dark=True)}
    <div style="display: flex; gap: 46px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 36px;">
        <div style="font-size: 88px; font-weight: 600; line-height: 1.12; color: {CREAM}; letter-spacing: -0.01em;">the {it("valley floor.", dark=True)}</div>
{body("most homes down here still get a regular company. get the real quote anyway... it&#8217;s part of your payment, and <span style='color: " + CREAM + "; font-weight: 500;'>i&#8217;d rather you see it on a tuesday than once we&#8217;re in escrow with the clock running.</span>", dark=True, width=460, size=32)}
      </div>
      <div style="flex: none; padding-top: 8px;">{floor_print}</div>
    </div>''', "BREATHE. THEN GET THE QUOTE.", 4, dark=True)

slides["DI5"] = shell(SO, f'''{eyebrow("03 &#183; THE DATE DETAIL")}
    <div style="font-size: 62px; font-weight: 600; line-height: 1.16; color: {INK}; letter-spacing: -0.01em;">the day your policy starts decides your rate.</div>
{panels("STARTS BEFORE OCT 15", "generally today&#8217;s rate, for the whole term.", "STARTS ON OR AFTER", "the new rate, from day one.")}
{body("closing anywhere near mid-october? that&#8217;s a call to your insurance broker <span style='color: " + INK + "; font-weight: 500;'>this week, not next month.</span>", width=780, size=31)}''',
                      "CONFIRM WITH YOUR BROKER", 5)

slides["DI6"] = shell(SO, f'''{eyebrow("04 &#183; WHAT IT ACTUALLY COVERS")}
    <div style="{SERIF} font-style: italic; font-size: 140px; font-weight: 400; line-height: 1.0; color: {INK};">fire only.</div>
{body("the backup policy covers fire. you add a second policy for theft, water and liability. together they usually cost well above a regular one... <span style='color: " + INK + "; font-weight: 500;'>which is why the quote comes first now.</span>", width=780, size=32)}
    <div style="display: flex; align-items: center; gap: 36px; padding-top: 10px;">{flame(120, 110)}<div style="flex: 1 1 auto; min-width: 120px; height: 2px; background: {INK};"></div><div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {GREY}; flex: none;">BACKUP + SECOND POLICY = THE REAL NUMBER</div></div>''',
                      "THE QUOTE COMES FIRST NOW", 6)

slides["DI7"] = close(SO, "jen-frontdoor.jpg", "JEN &#183; SAN FERNANDO VALLEY",
                      f'send me the address<br>{it("before you write.", dark=True)}',
                      "i&#8217;ll get the quote in hand first... approved and insured are two different yeses. i&#8217;m here for you... i do this to protect you and your best interest.",
                      "SOURCE: CALIFORNIA DEPARTMENT OF INSURANCE &#183; RATE CHANGE EFFECTIVE OCT 15 2026", img_h=460)

for name, html in slides.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=html))
print("wrote", len(slides), "valley-native set artboards:", ", ".join(sorted(slides)))

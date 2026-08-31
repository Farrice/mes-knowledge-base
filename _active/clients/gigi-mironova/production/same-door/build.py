#!/usr/bin/env python3
"""
"Same Door" — the Gigi Mironova concept, v2.

Built on her real book, not on inference. Every number traces to ../../DEMAND-BRIEF.md.
Deliberately type-led and data-led: the story is two prices on one front door, and the
honest image for that is her own data at scale plus her own face — not stock houses.
Her listing photography drops into L1 when she sends it; she holds the rights as the
listing agent, and no CC0 substitute was worth the relevance it costs.

    python3 build.py
"""
import base64
import json
import pathlib

import tokens as T

HERE = pathlib.Path(__file__).parent
BRAND = HERE.parent.parent / "brand"

NAME = "GIGI MIRONOVA · DRE 02025393"
ADDR = "19350 SHERMAN WAY · RESEDA"
SERIES = "SAME DOOR"
SERIES_RU = "ОДНА И ТА ЖЕ ДВЕРЬ"


def embed(p):
    ext = p.suffix.lower()
    mime = "image/png" if ext == ".png" else "image/jpeg"
    return "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())


def ghost(n, right, top, dark):
    return ('<div class="ghost" style="right:%spx; top:%spx; color:%s;">%s</div>'
            % (right, top, T.D_GHOST if dark else T.GHOST, n))


def rule(left, right, dark):
    return ('<div class="rule" style="border-bottom:1px solid %s;">'
            '<div class="caps" style="font-size:20px;">%s</div>'
            '<div class="caps" style="font-size:20px; opacity:0.72;">%s</div></div>'
            % (T.D_HAIRLINE if dark else T.HAIRLINE, left, right))


def foot(left, right, dark, size=19):
    return ('<div class="foot">'
            '<div class="caps" style="font-size:%dpx; color:%s;">%s</div>'
            '<div class="si" style="font-size:29px; opacity:0.85;">%s</div></div>'
            % (size, T.D_MUTED if dark else T.MUTED, left, right))


def body(text, dark, width=690):
    return ('<div style="font-size:34px; line-height:1.5; color:%s; max-width:%dpx; '
            'border-left:2px solid %s; padding-left:28px;">%s</div>'
            % (T.D_MUTED if dark else T.MUTED, width,
               T.D_HAIRLINE if dark else T.HAIRLINE, text))


def frame(cls, inner, ru=False):
    return """<!doctype html>
<html>
<head><meta charset="utf-8"></head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="%s">
  <style>%s</style>
</helmet>
<div class="frame %s%s">
%s
</div>
</x-dc>
</body>
</html>
""" % (T.FONTS, T.CSS, cls, " ru" if ru else "", inner)


def slide(cls, top_l, top_r, mid, foot_l, foot_r, g=None, gx=-58, gy=210,
          ru=False, foot_size=19, justify="center"):
    dark = cls == "dark"
    inner = ghost(g, gx, gy, dark) if g else ""
    inner += ('<div class="pad">%s'
              '<div style="flex:1; display:flex; flex-direction:column; gap:46px; '
              'justify-content:%s; padding:20px 0 26px;">%s</div>%s</div>'
              % (rule(top_l, top_r, dark), justify, mid,
                 foot(foot_l, foot_r, dark, foot_size)))
    return frame(cls, inner, ru)


def head(text, size=92, dark=True):
    return '<div class="h" style="font-size:%dpx; line-height:1.13;">%s</div>' % (size, text)


# ---------------------------------------------------------------- components
def price_pair():
    """The whole argument in one object: one unit, two prices, both hers."""
    rows = [("$2,500", "A MONTH TO RENT IT", False),
            ("$319,999", "TO OWN IT", True)]
    out = []
    for amount, label, lead in rows:
        col = "#FFFFFF" if lead else T.D_MUTED
        border = T.ACCENT_LT if lead else T.D_HAIRLINE
        out.append(
            '<div style="border-top:3px solid %s; padding-top:20px;">'
            '<div class="num" style="font-size:150px; color:%s;">%s</div>'
            '<div class="caps" style="font-size:20px; color:%s; margin-top:14px;">%s</div>'
            '</div>' % (border, col, amount, T.D_MUTED, label))
    return ('<div style="display:flex; flex-direction:column; gap:34px;">%s</div>'
            % "".join(out))


def four_numbers():
    cells = [("THE RATE", "public"), ("THE TAXES", "public"),
             ("THE INSURANCE", "public"), ("THE HOA", "in the documents")]
    out = []
    for i, (label, where) in enumerate(cells):
        lead = i == 3
        out.append(
            '<div style="flex:1; border-top:5px solid %s; padding-top:20px;">'
            '<div class="num" style="font-size:86px; color:%s;">0%d</div>'
            '<div class="caps" style="font-size:19px; color:%s; margin-top:18px;">%s</div>'
            '<div style="font-size:24px; color:%s; margin-top:10px; font-style:italic;">%s</div>'
            '</div>' % (T.INK if lead else T.HAIRLINE,
                        T.INK if lead else T.MUTED, i + 1,
                        T.INK if lead else T.MUTED, label, T.MUTED, where))
    return '<div style="display:flex; gap:20px;">%s</div>' % "".join(out)


def stat_row():
    """Three unequal numbers, so they stack as a ladder — side-by-side columns collided
    and forced the labels to wrap to different depths, breaking the baselines."""
    stats = [("$393,000", "average sale in this building, last 12 months", True),
             ("82", "average days on market here", False),
             ("$1,034,250", "San Fernando Valley median, all property types", False)]
    out = []
    for n, label, lead in stats:
        out.append(
            '<div style="display:flex; align-items:baseline; gap:32px; '
            'border-top:%dpx solid %s; padding-top:20px;">'
            '<div class="num" style="font-size:%dpx; color:%s; min-width:560px;">%s</div>'
            '<div style="font-size:27px; line-height:1.4; color:%s;">%s</div></div>'
            % (5 if lead else 1, T.INK if lead else T.HAIRLINE,
               84 if len(n) > 9 else 96, T.INK if lead else T.MUTED, n, T.MUTED, label))
    return '<div style="display:flex; flex-direction:column; gap:26px;">%s</div>' % "".join(out)


def docs(items, note):
    rows = []
    for i, (title, sub) in enumerate(items, 1):
        rows.append(
            '<div style="display:flex; gap:26px; align-items:flex-start; '
            'border-top:1px solid %s; padding-top:20px;">'
            '<div class="si" style="font-size:52px; line-height:1; color:%s; '
            'min-width:68px;">0%d</div><div>'
            '<div style="font-size:35px; line-height:1.32; color:%s; font-weight:500;">%s</div>'
            '<div style="font-size:28px; line-height:1.42; color:%s; margin-top:10px;">%s</div>'
            '</div></div>' % (T.HAIRLINE, T.ACCENT, i, T.INK, title, T.MUTED, sub))
    tail = ('<div style="background:%s; padding:32px 36px; font-size:29px; '
            'line-height:1.45; color:%s;">%s</div>' % (T.BONE, T.INK, note))
    return ('<div style="display:flex; flex-direction:column; gap:22px;">%s%s</div>'
            % ("".join(rows), tail))


def portrait_board():
    """DESIGN.md rec 5. Her real headshot, published by her own brokerage — not stock."""
    img = embed(BRAND / "gigi-headshot.jpg")
    block = (
        '<div style="display:flex; gap:44px; align-items:flex-end;">'
        '<div style="position:relative; width:430px; height:430px; flex:none; '
        'overflow:hidden;">'
        '<img src="%s" alt="" style="width:100%%; height:100%%; object-fit:cover; '
        'display:block; filter:grayscale(1) contrast(1.06) brightness(0.98);">'
        '<div style="position:absolute; inset:0; background:%s; mix-blend-mode:multiply; '
        'opacity:0.55;"></div>'
        '<div style="position:absolute; inset:0; background:#C9D9EC; '
        'mix-blend-mode:screen; opacity:0.14;"></div></div>'
        '<div class="h" style="font-size:66px; line-height:1.16; padding-bottom:8px;">'
        'sixteen years<br>reading documents<br>before I ever<br>sold a '
        '<span class="si">house.</span></div></div>' % (img, T.BAND))
    return slide("dark", SERIES, "REEL · 04", block, NAME, "PORTRAIT",
                 justify="center")


def listing_slot():
    """The one place a photograph belongs — and it has to be hers."""
    box = ('<div style="border:2px dashed %s; padding:64px 48px; display:flex; '
           'flex-direction:column; gap:20px; align-items:flex-start;">'
           '<div class="caps" style="font-size:19px; color:%s;">YOUR LISTING PHOTOGRAPHY</div>'
           '<div class="h" style="font-size:54px; line-height:1.16; color:%s;">'
           'unit 124 goes <span class="si">here.</span></div>'
           '<div style="font-size:28px; line-height:1.48; color:%s; max-width:620px;">'
           'the only photograph this series needs is the one of the actual door. you already '
           'have the rights to it — send the set and it drops straight in.</div></div>'
           % (T.HAIRLINE, T.MUTED, T.INK, T.MUTED))
    return slide("light", NAME, ADDR, box, "PHOTOGRAPHY SLOT", "—", foot_size=17)


def profile_board():
    bio = ("I read contracts for 16 years before I ever sold a house. Now I read them "
           "for you — HOA docs, disclosures, offers.<br>Residential · Leasing · Investment"
           "<br>English &amp; Русский · DM PAPERS")
    card = ('<div style="border:1px solid %s; padding:40px 42px; display:flex; '
            'flex-direction:column; gap:18px;">'
            '<div class="caps" style="font-size:18px; color:%s;">GIGI MIRONOVA · REALTOR® · '
            'DRE 02025393</div>'
            '<div style="font-size:37px; line-height:1.52; color:%s;">%s</div></div>'
            '<div style="background:%s; padding:32px 36px; font-size:29px; line-height:1.45; '
            'color:%s;">the sixteen years are the whole differentiator, and they were sitting '
            'in the last paragraph of her brokerage bio where nobody <span class="si" '
            'style="font-size:31px;">reads.</span></div>'
            % (T.HAIRLINE, T.MUTED, T.INK, bio, T.BONE, T.INK))
    return slide("light", NAME, "PROFILE", card, "INSTAGRAM BIO", "01 / 02", foot_size=17, justify="flex-start")


def highlight_board():
    words = ["THE DOCS", "UNIT 124", "RESEDA", "LEASING", "BUYING",
             "РУССКИЙ", "REVIEWS", "TEAM", "GIGI"]
    cells = []
    for w in words:
        size = 24 if len(w) <= 8 else 20
        cells.append(
            '<div style="width:176px; height:176px; border-radius:50%%; background:%s; '
            'display:flex; align-items:center; justify-content:center;">'
            '<span class="caps" style="font-size:%dpx; color:#FFFFFF; '
            'letter-spacing:0.13em; text-align:center; line-height:1.25;">%s</span></div>'
            % (T.BAND, size, w))
    grid = ('<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:30px 22px; '
            'justify-items:center;">%s</div>' % "".join(cells))
    tail = ('<div style="background:%s; padding:26px 30px; font-size:26px; line-height:1.45; '
            'color:%s;">nine words, nine <span class="si" style="font-size:30px;">entrances</span>'
            ' — one for each thing someone arriving on the profile is actually after.</div>'
            % (T.BONE, T.INK))
    return slide("light", NAME, "PROFILE", grid + tail, "HIGHLIGHT COVER SET", "02 / 02",
                 foot_size=17, justify="flex-start")


# ---------------------------------------------------------------- the deck
BOARDS = [
    ("C1", "C1 · Same Door", lambda: slide(
        "dark", NAME, ADDR,
        head('one unit. listed<br>both ways, right now.', 74)
        + price_pair()
        + body("unit 124 — one bedroom, 619 square feet, two parking spaces. "
               "I am the agent on the lease and on the sale.", True),
        "SWIPE — THE NUMBER THAT DECIDES IT", "1 / 6", g="124", gx=-110, gy=96)),

    ("C2", "C2 · Four Numbers", lambda: slide(
        "light", NAME, SERIES,
        head('four numbers decide whether<br>owning it costs less than '
             '<span class="si">renting</span> it.', 66)
        + four_numbers()
        + body("three of them you can look up tonight. the fourth is not on the listing, "
               "and it is the one that moves the answer.", False, 760),
        "NOBODY QUOTES YOU THE FOURTH", "2 / 6", justify="flex-start")),

    ("C3", "C3 · The HOA", lambda: slide(
        "dark", NAME, SERIES,
        head('the number that decides it<br>is not the <span class="si">price.</span>', 74)
        + body("monthly dues move your payment more than half a point on the rate does — "
               "and they sit in the association's financials, next to the reserve balance "
               "and any assessment the board has already voted through.", True, 720),
        "ASK BEFORE YOU OFFER, NOT AFTER", "3 / 6", g="619", gy=250)),

    ("C4", "C4 · The Building", lambda: slide(
        "light", NAME, ADDR,
        head('what this building<br>actually <span class="si">does.</span>', 80)
        + stat_row()
        + body("a one-bedroom here lists at $319,999 in a valley whose median, across every "
               "property type, is over a million. that gap is the entire pitch — and it "
               "takes eighty-two days, so the buyer has time to read.", False, 780),
        "BUILDING 12-MONTH ACTIVITY · SFV APRIL 2026 CLOSED SALES", "4 / 6",
        foot_size=15, justify="flex-start")),

    ("C5", "C5 · Three Documents", lambda: slide(
        "light", NAME, SERIES,
        head('three documents to ask for<br>before you write an '
             '<span class="si">offer.</span>', 58)
        + docs([("the financials and the reserve study",
                 "is the building funded, or one repair away from an assessment?"),
                ("the CC&amp;Rs on renting",
                 "can you lease it later, or is the building already at its cap?"),
                ("the board minutes",
                 "has something been voted through that the dues do not show yet?")],
               "you are entitled to all three before you commit. almost nobody asks."),
        "SAVE THIS BEFORE YOUR NEXT OFFER", "5 / 6", justify="flex-start")),

    ("C5RU", "C5 · Three Documents · RU", lambda: slide(
        "light", NAME, SERIES_RU,
        head('три документа, которые нужно<br>запросить до '
             '<span class="si">оферты.</span>', 54)
        + docs([("финансы ассоциации и резервный фонд",
                 "дом обеспечен, или один ремонт отделяет вас от спецвзноса?"),
                ("правила CC&amp;R об аренде",
                 "сможете ли вы сдавать квартиру, или лимит уже исчерпан?"),
                ("протоколы собраний правления",
                 "что уже утвердили, но ещё не включили в ежемесячные взносы?")],
               "вы имеете право получить все три до подписания. почти никто не просит."),
        "ТОТ ЖЕ ВОПРОС, ДРУГОЙ ЯЗЫК", "5 / 6", ru=True, justify="flex-start")),

    ("C6", "C6 · CTA", lambda: slide(
        "dark", NAME, SERIES,
        head('I read documents for<br>sixteen years before I<br>ever sold a '
             '<span class="si">house.</span>', 76)
        + body("residential, leasing and investment at Equity Union. if you want the "
               "association's financials on unit 124 pulled and actually read before you "
               "decide anything — that is the job.", True, 700)
        + ('<div style="display:inline-flex; align-self:flex-start; background:#FFFFFF; '
           'padding:24px 40px; margin-top:4px;"><span class="caps" style="font-size:22px; '
           'color:%s;">DM «ДОКУМЕНТЫ» OR PAPERS</span></div>' % T.BAND),
        NAME, "6 / 6")),

    ("R1", "Reel 1 Cover", lambda: slide(
        "dark", SERIES, "REEL · 01",
        head('$2,500 to rent it.<br>$319,999 to own it.<br>same '
             '<span class="si">door.</span>', 84),
        NAME, "▶", g="124", gy=300)),

    ("R2", "Reel 2 Cover", lambda: slide(
        "dark", SERIES, "REEL · 02",
        head('the number that<br>decides it is not<br>the '
             '<span class="si">price.</span>', 88),
        NAME, "▶", g="04", gy=300)),

    ("R3", "Reel 3 Cover · RU", lambda: slide(
        "dark", SERIES_RU, "REEL · 03",
        head('$2,500 — снять.<br>$319,999 — купить.<br>одна и та же '
             '<span class="si">дверь.</span>', 72),
        NAME, "▶", g="124", gy=300, ru=True)),

    ("R4", "Reel 4 Cover · Portrait", portrait_board),
    ("L1", "Listing Photography Slot", listing_slot),
    ("P1", "Profile · Bio", profile_board),
    ("P2", "Profile · Highlights", highlight_board),
]


def main():
    boards = []
    for i, (key, title, fn) in enumerate(BOARDS):
        name = "%s.dc.html" % key
        (HERE / name).write_text(fn())
        boards.append({"file": name, "x": (i % 7) * 1200, "y": (i // 7) * 1520,
                       "w": 1080, "h": 1350, "title": title})
    (HERE / "canvas.json").write_text(
        json.dumps({"artboards": boards, "launch": {"view": "canvas"}}, indent=2))
    print("%d artboards -> %s" % (len(boards), HERE))


if __name__ == "__main__":
    main()

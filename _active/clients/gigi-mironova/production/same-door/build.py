#!/usr/bin/env python3
"""
"Same Door" v3 — the Gigi Mironova concept on the proven floor grammar.

Facts unchanged from v2 (all trace to ../../DEMAND-BRIEF.md and OPERATOR-NOTES.md § v2).
Rebuilt after Farrice's 2026-08-31 verdict: readable Figtree numerals instead of Bodoni
flare, soft navy instead of raw brand navy, and the First Home Valley composition —
photography-led story slides, dense white structure slides, ghost numerals — instead of
flat type boards.

Imagery: the CC0 bank prepared for this client in v1 (provenance carried in
../american-transaction/imagery/provenance.jsonl). Photo slides establish mood and place;
the one photograph that must be HER unit stays an explicit drop-in slot (L1).

    python3 build.py
"""
import base64
import json
import pathlib

import tokens as T

HERE = pathlib.Path(__file__).parent
IMG = HERE.parent / "american-transaction" / "imagery" / "prepared"
BRAND = HERE.parent.parent / "brand"

NAME = "GIGI MIRONOVA · DRE 02025393"
ADDR = "19350 SHERMAN WAY · RESEDA"
SERIES = "SAME DOOR"
SERIES_RU = "ОДНА И ТА ЖЕ ДВЕРЬ"


def embed(p):
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    return "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())


def photo(name, treatment, pos="50% 50%", scale=1.0):
    """Layer stack over one cover-fit image. Framing inline per slide — never global
    (the reference deck's one global scale silently cropped every other image)."""
    layers = ('<div class="tint"></div><div class="lift"></div><div class="panel"></div>'
              if treatment == "duo" else
              '<div class="tint" style="opacity:0.44"></div><div class="scrim"></div>'
              '<div class="panel"></div>')
    tf = "" if scale == 1.0 else " transform:scale(%s);" % scale
    return ('<div class="photo %s"><img alt="" style="object-position:%s;%s" src="%s.jpg">%s</div>'
            % (treatment, pos, tf, name, layers))


def ghost(n, right, top, dark):
    return ('<div class="ghost" style="right:%spx; top:%spx; color:%s;">%s</div>'
            % (right, top, T.D_GHOST if dark else T.GHOST, n))


def rule(left, right, dark):
    return ('<div class="rule" style="border-bottom:1px solid %s;">'
            '<div class="caps" style="font-size:21px;">%s</div>'
            '<div class="caps" style="font-size:21px; opacity:0.75;">%s</div></div>'
            % (T.D_HAIRLINE if dark else T.HAIRLINE, left, right))


def foot(left, right, dark, size=20):
    return ('<div class="foot">'
            '<div class="caps" style="font-size:%dpx; color:%s;">%s</div>'
            '<div class="si" style="font-size:30px; opacity:0.85;">%s</div></div>'
            % (size, T.D_MUTED if dark else T.MUTED, left, right))


def body(text, dark, width=680):
    return ('<div style="font-size:33px; line-height:1.47; color:%s; max-width:%dpx; '
            'border-left:2px solid %s; padding-left:28px;">%s</div>'
            % (T.D_MUTED if dark else T.MUTED, width,
               T.D_HAIRLINE if dark else T.HAIRLINE, text))


def frame(cls, inner, ru=False):
    return """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
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


def story(img_name, treatment, pos, g, mid, top_l, top_r, foot_l, foot_r,
          ru=False, gy=210, gx=-64, scale=1.0):
    """Full-bleed photograph; type carries the data, photo carries place and moment."""
    inner = photo(img_name, treatment, pos, scale)
    if g:
        inner += ghost(g, gx, gy, True)
    inner += ('<div class="pad">%s'
              '<div style="display:flex; flex-direction:column; gap:36px;">%s</div>'
              '%s</div>' % (rule(top_l, top_r, True), "".join(mid),
                            foot(foot_l, foot_r, True)))
    return frame("dark", inner, ru)


def structure(g, mid, top_l, top_r, foot_l, foot_r, ru=False, gy=170, foot_size=18):
    """White ground; the densest layouts in the deck — the white is the luxury."""
    inner = ghost(g, -64, gy, False) if g else ""
    inner += ('<div class="pad">%s'
              '<div style="display:flex; flex-direction:column; gap:42px;">%s</div>'
              '%s</div>' % (rule(top_l, top_r, False), "".join(mid),
                            foot(foot_l, foot_r, False, foot_size)))
    return frame("light", inner, ru)


def head(text, size=96, lh=1.12):
    return ('<div class="h" style="font-size:%dpx; line-height:%s;">%s</div>'
            % (size, lh, text))


# ---------------------------------------------------------------- components
def price_pair_dark():
    rows = [("$2,500", "A MONTH TO RENT IT", False),
            ("$319,999", "TO OWN IT", True)]
    out = []
    for amount, label, lead in rows:
        out.append(
            '<div style="border-top:3px solid %s; padding-top:18px;">'
            '<div class="num" style="font-size:124px; color:%s;">%s</div>'
            '<div class="caps" style="font-size:20px; color:%s; margin-top:14px;">%s</div>'
            '</div>' % (T.ACCENT_LT if lead else T.D_HAIRLINE,
                        "#FFFFFF" if lead else "rgba(255,255,255,0.85)",
                        amount, T.D_MUTED, label))
    return ('<div style="display:flex; flex-direction:column; gap:30px; '
            'max-width:720px;">%s</div>' % "".join(out))


def four_numbers():
    cells = [("01", "THE RATE", "public"), ("02", "THE TAXES", "public"),
             ("03", "THE INSURANCE", "public"), ("04", "THE HOA", "in the documents")]
    out = []
    for i, (n, label, where) in enumerate(cells):
        lead = i == 3
        out.append(
            '<div style="flex:1; border-top:6px solid %s; padding-top:24px;">'
            '<div class="num" style="font-size:84px; color:%s;">%s</div>'
            '<div class="caps" style="font-size:18px; color:%s; margin-top:18px;">%s</div>'
            '<div class="si" style="font-size:27px; color:%s; margin-top:10px;">%s</div>'
            '</div>' % (T.INK if lead else T.HAIRLINE,
                        T.INK if lead else T.MUTED, n,
                        T.INK if lead else T.MUTED, label, T.MUTED, where))
    return '<div style="display:flex; gap:22px;">%s</div>' % "".join(out)


def stat_ladder():
    stats = [("$393,000", "what homes in this building actually sell for", True),
             ("82", "days they usually take — no bidding-war panic", False),
             ("$1,034,250", "what the rest of the Valley costs right now", False)]
    out = []
    for n, label, lead in stats:
        out.append(
            '<div style="display:flex; align-items:baseline; gap:34px; '
            'border-top:%dpx solid %s; padding-top:22px;">'
            '<div class="num" style="font-size:88px; color:%s; min-width:500px;">%s</div>'
            '<div style="font-size:28px; line-height:1.42; color:%s;">%s</div></div>'
            % (6 if lead else 1, T.INK if lead else T.HAIRLINE,
               T.INK if lead else T.MUTED, n, T.MUTED, label))
    return '<div style="display:flex; flex-direction:column; gap:24px;">%s</div>' % "".join(out)


def payment_ladder():
    """The payoff, done for the reader. Every figure computed 2026-08-31 and labeled:
    rate 6.66% (Freddie Mac PMMS 8/27/26), tax est. 1.25% LA County, HOA $477 as
    recorded for a 2-bd in this building (MLS via Redfin), HO-6 insurance estimated."""
    rows = [("$1,645", "loan payment — 20% down, 6.66%"),
            ("$333", "property taxes, est. 1.25%"),
            ("$477", "association dues*"),
            ("$60", "insurance, est. HO-6")]
    out = []
    for n, label in rows:
        out.append(
            '<div style="display:flex; align-items:baseline; gap:30px; '
            'border-top:1px solid %s; padding-top:16px;">'
            '<div class="num" style="font-size:64px; color:%s; min-width:300px;">%s</div>'
            '<div style="font-size:27px; line-height:1.4; color:%s;">%s</div></div>'
            % (T.HAIRLINE, T.INK, n, T.MUTED, label))
    out.append(
        '<div style="display:flex; align-items:baseline; gap:30px; '
        'border-top:4px solid %s; padding-top:18px;">'
        '<div class="num" style="font-size:84px; color:%s; min-width:300px;">$2,515</div>'
        '<div style="font-size:28px; line-height:1.4; color:%s;">a month to own it — '
        'against $2,500 rent</div></div>' % (T.INK, T.INK, T.MUTED))
    return '<div style="display:flex; flex-direction:column; gap:18px; max-width:900px;">%s</div>' % "".join(out)


def hoa_covers():
    items = ["POOL + SPA", "GYM + SAUNA", "WATER", "TRASH",
             "BUILDING INSURANCE", "GROUNDS"]
    cells = []
    for w in items:
        cells.append('<div style="border:1px solid %s; padding:18px 26px;">'
                     '<span class="caps" style="font-size:19px; color:%s;">%s</span></div>'
                     % (T.HAIRLINE, T.INK, w))
    return ('<div style="display:flex; flex-wrap:wrap; gap:16px; max-width:880px;">%s</div>'
            % "".join(cells))


def docs(items, note):
    rows = []
    for i, (title, sub) in enumerate(items, 1):
        rows.append(
            '<div style="display:flex; gap:28px; align-items:flex-start; '
            'border-top:1px solid %s; padding-top:22px;">'
            '<div class="si" style="font-size:48px; line-height:1; color:%s; '
            'min-width:64px;">0%d</div><div>'
            '<div style="font-size:34px; line-height:1.32; color:%s; font-weight:600;">%s</div>'
            '<div style="font-size:28px; line-height:1.42; color:%s; margin-top:10px;">%s</div>'
            '</div></div>' % (T.HAIRLINE, T.ACCENT, i, T.INK, title, T.MUTED, sub))
    tail = ('<div style="background:%s; padding:30px 34px; font-size:28px; '
            'line-height:1.46; color:%s;">%s</div>' % (T.BONE, T.INK, note))
    return ('<div style="display:flex; flex-direction:column; gap:24px;">%s%s</div>'
            % ("".join(rows), tail))


def cta_button(label):
    return ('<div style="display:inline-flex; align-self:flex-start; background:#FFFFFF; '
            'padding:26px 44px; margin-top:6px;"><span class="caps" style="font-size:23px; '
            'color:%s;">%s</span></div>' % (T.BAND, label))


def play_icon():
    return ('<svg width="64" height="64" viewBox="0 0 64 64" fill="none">'
            '<circle cx="32" cy="32" r="30" stroke="#FFFFFF" stroke-width="2.5"/>'
            '<path d="M26 21 L45 32 L26 43 Z" stroke="#FFFFFF" stroke-width="2.5" '
            'stroke-linejoin="round" fill="none"/></svg>')


def reel(img_name, treatment, pos, g, headline, top_r, ru=False, series=None,
         gy=330, scale=1.0):
    inner = photo(img_name, treatment, pos, scale)
    if g:
        inner += ghost(g, -70, gy, True)
    inner += ('<div class="pad">%s'
              '<div class="h" style="font-size:94px; line-height:1.14; max-width:930px;">%s</div>'
              '<div style="display:flex; justify-content:space-between; align-items:center;">'
              '<div class="caps" style="font-size:21px; color:%s;">%s</div>%s</div></div>'
              % (rule(series or SERIES, top_r, True), headline, T.D_MUTED, NAME, play_icon()))
    return frame("dark", inner, ru)


def portrait_board():
    """Her real headshot (Equity Union profile) under the duo treatment, on the dark
    ground — the floor's photographic grammar applied to the portrait slot."""
    img = "gigi-headshot.jpg"
    block = (
        '<div style="display:flex; gap:48px; align-items:flex-end;">'
        '<div style="position:relative; width:440px; height:440px; flex:none; overflow:hidden;">'
        '<img src="%s" alt="" style="width:100%%; height:100%%; object-fit:cover; display:block; '
        'filter:grayscale(1) contrast(1.1) brightness(0.95);">'
        '<div style="position:absolute; inset:0; background:%s; mix-blend-mode:multiply; '
        'opacity:0.5;"></div>'
        '<div style="position:absolute; inset:0; background:#C9D7E8; mix-blend-mode:screen; '
        'opacity:0.14;"></div>'
        '<div style="position:absolute; inset:0; border:1px solid rgba(255,255,255,0.3);"></div>'
        '</div>'
        '<div class="h" style="font-size:64px; line-height:1.18; padding-bottom:6px;">'
        'sixteen years in<br>litigation support.<br>now the fine print<br>works for '
        '<span class="si">you.</span></div></div>' % (img, T.BAND))
    inner = ghost("16", -70, 640, True)
    inner += ('<div class="pad">%s%s%s</div>'
              % (rule(SERIES, "REEL · 04", True), block, foot(NAME, "PORTRAIT", True)))
    return frame("dark", inner)


def listing_slot():
    box = ('<div style="border:2px dashed %s; padding:70px 52px; display:flex; '
           'flex-direction:column; gap:22px; align-items:flex-start;">'
           '<div class="caps" style="font-size:20px; color:%s;">YOUR LISTING PHOTOGRAPHY</div>'
           '<div class="h" style="font-size:64px; line-height:1.14; color:%s;">'
           'unit 124 goes <span class="si">here.</span></div>'
           '<div style="font-size:30px; line-height:1.5; color:%s; max-width:680px;">'
           'the one photograph this series needs is the actual door. the rights are already '
           'yours — send the set and it drops straight in.</div></div>'
           % (T.HAIRLINE, T.MUTED, T.INK, T.MUTED))
    return structure("124", [box], NAME, ADDR, "PHOTOGRAPHY SLOT", "—", gy=520)


def profile_board():
    bio = ("I read contracts for 16 years before I ever sold a house. Now I read them "
           "for you — HOA docs, disclosures, offers.<br>Residential · Leasing · Investment"
           "<br>English &amp; Русский · DM PAPERS")
    card = ('<div style="border:1px solid %s; padding:42px 44px; display:flex; '
            'flex-direction:column; gap:20px;">'
            '<div class="caps" style="font-size:19px; color:%s;">GIGI MIRONOVA · REALTOR® · '
            'DRE 02025393</div>'
            '<div class="ru" style="font-size:36px; line-height:1.52; color:%s;">%s</div></div>'
            % (T.HAIRLINE, T.MUTED, T.INK, bio))
    tail = ('<div style="background:%s; padding:30px 34px; font-size:28px; line-height:1.46; '
            'color:%s;">the sixteen years are the whole differentiator — moved out of the '
            'last paragraph of the brokerage bio and into the first '
            '<span class="si" style="font-size:32px;">line.</span></div>' % (T.BONE, T.INK))
    return structure("16", [head('the bio, rebuilt around<br>the one credential nobody<br>'
                                 'can <span class="si">contest.</span>', 66), card, tail],
                     NAME, "PROFILE", "INSTAGRAM BIO", "01 / 02", gy=560)


def highlight_board():
    words = ["THE DOCS", "UNIT 124", "RESEDA", "LEASING", "BUYING",
             "РУССКИЙ", "REVIEWS", "TEAM", "GIGI"]
    cells = []
    for w in words:
        size = 25 if len(w) <= 8 else 21
        cells.append(
            '<div class="ru" style="width:182px; height:182px; border-radius:50%%; '
            'background:%s; display:flex; align-items:center; justify-content:center;">'
            '<span class="caps" style="font-size:%dpx; color:#FFFFFF; letter-spacing:0.13em; '
            'text-align:center; line-height:1.25;">%s</span></div>' % (T.BAND, size, w))
    grid = ('<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:32px 24px; '
            'justify-items:center;">%s</div>' % "".join(cells))
    tail = ('<div style="background:%s; padding:28px 32px; font-size:27px; line-height:1.46; '
            'color:%s;">nine words, nine <span class="si" style="font-size:31px;">entrances'
            '</span> — one for each thing someone arriving on the profile is actually '
            'after.</div>' % (T.BONE, T.INK))
    return structure("", [head('nine covers.<br>nine different <span class="si">doors.</span>',
                               66), grid, tail],
                     NAME, "PROFILE", "HIGHLIGHT COVER SET", "02 / 02")


BOARDS = [
    # 11 boards: 7-slide carousel (4 photo story / 3 white structure) + 4 reel covers.
    # The mockup boards (photo slot, profile meta) are gone — the kit page carries the
    # real bio text and the nine cover files instead.
    ("C1", "C1 · Same Door", lambda: story(
        "palm-tree-sunset-city-01", "bleed", "50% 58%", "124",
        [head('the renter and the owner<br>live behind the same <span class="si">door.</span>', 76),
         price_pair_dark(),
         body("same one-bedroom in Reseda. same parking spots, same pool. I'm the "
              "agent on both listings — so this isn't a what-if. swipe.", True, 640)],
        NAME, ADDR, "SWIPE — THE MATH NOBODY RUNS", "1 / 6", gy=120, gx=-100)),

    ("C2", "C2 · The Math", lambda: structure(
        "15",
        [head('fifteen dollars. that&#8217;s<br>the whole <span class="si">difference.</span>', 68),
         payment_ladder(),
         ('<div style="font-size:22px; line-height:1.5; color:%s; max-width:900px;">'
          'estimate, not a quote — 6.66%%: Freddie Mac avg 8/27/26 · tax est. 1.25%%'
          ' · *dues as recorded for a 2-bd in this building; unit 124&#8217;s exact figure is '
          'in its HOA documents · confirm with your lender</div>' % T.MUTED)],
        NAME, SERIES, "BEFORE A DOLLAR OF EQUITY — AND THE PRICE ISN'T WHY", "2 / 6",
        gy=430, foot_size=15)),

    ("C3", "C3 · The 477", lambda: structure(
        "477",
        [head('the fee that ambushes<br>first-time condo <span class="si">buyers.</span>', 70),
         hoa_covers(),
         body("you tour the place. you love it. you've done the math on the price — "
              "and then a fee you've never heard of shows up after you're already "
              "attached. dues: $477 a month here. this is what they buy. nobody puts "
              "it in the ad.", False, 800)],
        NAME, SERIES, "MOST BUYERS MEET THIS NUMBER AFTER THEY OFFER", "3 / 6",
        gy=430, foot_size=16)),

    ("C4", "C4 · Equity", lambda: structure(
        "224",
        [head('rent leaves. <span class="si">$224</span> of<br>this payment stays.', 72),
         stat_ladder(),
         body("every rent check is gone the day you send it. this payment keeps $224 "
              "the first month — your money, parked in your own walls — and the kept "
              "share grows every month after.", False, 800)],
        NAME, ADDR, "PRINCIPAL, MONTH ONE · BUILDING 12-MO · SFV APRIL 2026", "4 / 6",
        gy=430, foot_size=15)),

    ("C5", "C5 · Three Documents", lambda: structure(
        "",
        [head('three pieces of paper that<br>protect your life '
              '<span class="si">savings.</span>', 62),
         docs([("the building's bank account",
                "is money saved for the roof and pipes — or does everyone split a "
                "surprise bill?"),
               ("the rulebook",
                "can you rent it out someday? have a dog? the rules decide, not the "
                "seller."),
               ("the meeting notes",
                "boards vote on new fees months before they land on your statement.")],
              "you're allowed to read all three before you sign anything. most people "
              "never find that out.")],
        NAME, SERIES, "THREE PAGES THAT PROTECT YOUR SAVINGS", "5 / 6")),

    ("C5RU", "C5 · Three Documents · RU", lambda: structure(
        "",
        [head('три листа бумаги, которые<br>защищают ваши '
              '<span class="si">сбережения.</span>', 58),
         docs([("банковский счёт дома",
                "есть ли деньги на крышу и трубы — или всех ждёт внезапный счёт?"),
               ("правила дома",
                "сможете ли сдавать квартиру? завести собаку? решают правила, а не "
                "продавец."),
               ("протоколы собраний",
                "новые взносы утверждают за месяцы до того, как они придут вам в "
                "квитанции.")],
              "вы имеете право прочитать все три документа до подписи. большинство об "
              "этом просто не знает.")],
        NAME, SERIES_RU, "ТОТ ЖЕ ВОПРОС, ДРУГОЙ ЯЗЫК", "5 / 6", ru=True)),

    ("C6", "C6 · CTA", lambda: story(
        "front-door-house-02", "duo", "50% 56%", "",
        [head('sixteen years in litigation<br>support before I ever<br>sold a '
              '<span class="si">house.</span>', 76),
         body("before real estate, my job was reading legal documents. all day, for "
              "sixteen years. now I do it for people making the biggest purchase of "
              "their life. want the real numbers on this unit, in plain English or "
              "по-русски? one message.", True, 700),
         cta_button("DM ME “124”")],
        NAME, SERIES, NAME, "6 / 6", scale=1.16)),

    ("R1", "Reel 1 Cover", lambda: reel(
        "sunlight-through-window-floor-00", "bleed", "50% 62%", "124",
        '$2,500 to rent it.<br>$319,999 to own it.<br>same <span class="si">door.</span>',
        "REEL · 01")),

    ("R2", "Reel 2 Cover", lambda: reel(
        "balcony-plants-apartment-02", "duo", "50% 34%", "477",
        'the fee nobody<br>mentions until<br>it&#8217;s <span class="si">yours.</span>',
        "REEL · 02")),

    ("R3", "Reel 3 Cover · RU", lambda: reel(
        "palm-tree-sunset-city-00", "duo", "50% 46%", "124",
        '$2,500 — снять.<br>$319,999 — купить.<br>одна и та же <span class="si">дверь.</span>',
        "REEL · 03", ru=True, series=SERIES_RU, scale=1.18)),

    ("R4", "Reel 4 Cover · Portrait", portrait_board),
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

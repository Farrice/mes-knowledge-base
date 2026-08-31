#!/usr/bin/env python3
"""
Build the Gigi Mironova concept artboards.

Extends `_shared/realtor-editorial-system/DESIGN.md` — same grammar, oxblood register
(see tokens.py), and a Cyrillic type path the navy system never needed.

Copy lives in this file as data and is emitted, never retyped to restyle. Every image is
base64-embedded so each .dc.html is self-contained.

    python3 build.py       # writes *.dc.html + canvas.json
"""
import base64
import json
import mimetypes
import pathlib

import tokens as T

HERE = pathlib.Path(__file__).parent
IMG = HERE.parent / "imagery" / "prepared"

HANDLE = "@GIGIMIRONOVA_REALESTATE"
SERIES = "THE AMERICAN TRANSACTION"
SERIES_RU = "АМЕРИКАНСКАЯ СДЕЛКА"


# ---------------------------------------------------------------- primitives
def embed(name):
    p = IMG / (name if name.endswith(".jpg") else name + ".jpg")
    mime = mimetypes.guess_type(p.name)[0] or "image/jpeg"
    return "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())


def photo(name, treatment, pos="50% 50%", scale=1.0):
    """A layer stack over one cover-fit image.

    Framing is per slide and inline — never in the shared stylesheet. Several images in
    this bank are archival press negatives carrying a black scan border and a handwritten
    negative number; `scale` crops that off the individual frame that needs it. A global
    scale would silently crop every other photograph in the deck (DESIGN.md, first pass).
    """
    layers = '<div class="tint"></div><div class="lift"></div>' if treatment == "duo" \
        else '<div class="tint" style="opacity:0.50"></div><div class="scrim"></div>'
    tf = "" if scale == 1.0 else " transform:scale(%s);" % scale
    return ('<div class="photo %s"><img alt="" style="object-position:%s;%s" src="%s">%s</div>'
            % (treatment, pos, tf, embed(name), layers))


def ghost(n, right, top, dark):
    col = T.D_GHOST if dark else T.GHOST
    return ('<div class="ghost" style="right:%spx; top:%spx; color:%s;">%s</div>'
            % (right, top, col, n))


def rule(left, right, dark):
    line = T.D_HAIRLINE if dark else T.HAIRLINE
    op = "0.75"
    return ('<div class="rule" style="border-bottom:1px solid %s;">'
            '<div class="caps" style="font-size:21px;">%s</div>'
            '<div class="caps" style="font-size:21px; opacity:%s;">%s</div></div>'
            % (line, left, op, right))


def foot(left, right, dark, left_size=21):
    muted = T.D_MUTED if dark else T.MUTED
    return ('<div class="foot">'
            '<div class="caps" style="font-size:%dpx; color:%s;">%s</div>'
            '<div class="si" style="font-size:30px; opacity:0.8;">%s</div></div>'
            % (left_size, muted, left, right))


def body(text, dark, width=660):
    line = T.D_HAIRLINE if dark else T.HAIRLINE
    col = T.D_MUTED if dark else T.MUTED
    return ('<div style="font-size:33px; line-height:1.47; color:%s; max-width:%dpx; '
            'border-left:2px solid %s; padding-left:28px;">%s</div>'
            % (col, width, line, text))


def frame(cls, inner, ru=False):
    klass = "frame %s%s" % (cls, " ru" if ru else "")
    return """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="%s">
  <style>%s</style>
</helmet>
<div class="%s">
%s
</div>
</x-dc>
</body>
</html>
""" % (T.FONTS, T.CSS, klass, inner)


def story(img, treatment, pos, g, head, sub, top_l, top_r, foot_l, foot_r, ru=False,
          head_size=96, gx=-64, gy=200, extra="", scale=1.0):
    """Full-bleed photograph. Type carries the data; the photo carries place and moment."""
    inner = photo(img, treatment, pos, scale) if img else ""
    if g:
        inner += ghost(g, gx, gy, True)
    inner += ('<div class="pad">%s'
              '<div style="flex:1; display:flex; flex-direction:column; gap:36px; '
              'justify-content:flex-end; padding-bottom:34px;">'
              '<div class="h" style="font-size:%dpx; line-height:1.13;">%s</div>%s%s</div>'
              '%s</div>'
              % (rule(top_l, top_r, True), head_size, head,
                 body(sub, True) if sub else "", extra,
                 foot(foot_l, foot_r, True)))
    return frame("dark", inner, ru)


def structure(g, head, mid, top_l, top_r, foot_l, foot_r, ru=False, head_size=76,
              gx=-64, gy=170, foot_size=18):
    """White ground. The densest layouts in the deck — the white is the luxury."""
    inner = ghost(g, gx, gy, False) if g else ""
    inner += ('<div class="pad">%s'
              '<div style="flex:1; display:flex; flex-direction:column; gap:44px; '
              'justify-content:center; padding:18px 0 26px;">'
              '<div class="h" style="font-size:%dpx; line-height:1.14;">%s</div>%s</div>'
              '%s</div>'
              % (rule(top_l, top_r, False), head_size, head, mid,
                 foot(foot_l, foot_r, False, foot_size)))
    return frame("light", inner, ru)


# ---------------------------------------------------------------- the deck
def deadline_columns():
    cols = [("17", "INSPECTION", False), ("17", "APPRAISAL", False), ("21", "LOAN", True)]
    cells = []
    for num, label, lead in cols:
        border = T.INK if lead else T.HAIRLINE
        col = T.INK if lead else T.MUTED
        cells.append(
            '<div style="flex:1; border-top:6px solid %s; padding-top:24px;">'
            '<div class="si" style="font-size:132px; line-height:1; color:%s;">%s</div>'
            '<div class="caps" style="font-size:19px; color:%s; margin-top:14px;">%s</div>'
            '<div class="caps" style="font-size:19px; color:%s; margin-top:6px; '
            'opacity:0.6;">DAYS</div></div>' % (border, col, num, T.MUTED, label, T.MUTED))
    return ('<div style="display:flex; gap:24px; align-items:stretch;">%s</div>'
            '<div style="font-size:31px; line-height:1.5; color:%s; max-width:800px;">'
            'all three are defaults, and all three are negotiable. they count in '
            '<strong style="font-weight:600; color:%s;">calendar days</strong> — saturdays, '
            'sundays and holidays sit inside the number, not on top of it.</div>'
            % ("".join(cells), T.MUTED, T.INK))


def questions(items, note=None, ru=False):
    rows = []
    for i, q in enumerate(items, 1):
        rows.append(
            '<div style="display:flex; gap:28px; align-items:flex-start; '
            'border-top:1px solid %s; padding-top:22px;">'
            '<div class="si" style="font-size:46px; line-height:1; color:%s; '
            'min-width:64px;">0%d</div>'
            '<div style="font-size:31px; line-height:1.42; color:%s;">%s</div></div>'
            % (T.HAIRLINE, T.ACCENT, i, T.INK, q))
    tail = ""
    if note:
        tail = ('<div style="margin-top:8px; background:%s; padding:30px 34px; '
                'font-size:28px; line-height:1.46; color:%s;">%s</div>'
                % (T.HAIRLINE, T.INK, note))
    return ('<div style="display:flex; flex-direction:column; gap:24px;">%s%s</div>'
            % ("".join(rows), tail))


def cta_button(label):
    return ('<div style="display:inline-flex; align-self:flex-start; background:#FFFFFF; '
            'padding:26px 44px; margin-top:8px;">'
            '<span class="caps" style="font-size:24px; color:%s;">%s</span></div>'
            % (T.BAND, label))


def play_icon():
    return ('<svg width="64" height="64" viewBox="0 0 64 64" fill="none">'
            '<circle cx="32" cy="32" r="30" stroke="#FFFFFF" stroke-width="2.5"/>'
            '<path d="M26 21 L45 32 L26 43 Z" stroke="#FFFFFF" stroke-width="2.5" '
            'stroke-linejoin="round" fill="none"/></svg>')


def reel_foot():
    return ('<div style="display:flex; justify-content:space-between; align-items:center;">'
            '<div class="caps" style="font-size:21px; color:%s;">%s</div>%s</div>'
            % (T.D_MUTED, HANDLE, play_icon()))


def reel(img, treatment, pos, g, head, top_r, ru=False, series=None, gy=330, scale=1.0):
    inner = photo(img, treatment, pos, scale) if img else ""
    if g:
        inner += ghost(g, -70, gy, True)
    inner += ('<div class="pad">%s'
              '<div class="h" style="font-size:92px; line-height:1.14; max-width:930px;">%s</div>'
              '%s</div>' % (rule(series or SERIES, top_r, True), head, reel_foot()))
    return frame("dark", inner, ru)


def profile_board():
    bio = ("I explain the American transaction — escrow, contingencies, deposits — "
           "before you sign it.<br>English &amp; Русский · SFV + Conejo Valley<br>"
           "DM «СДЕЛКА» or ESCROW to start")
    card = ('<div style="border:1px solid %s; padding:44px 46px; display:flex; '
            'flex-direction:column; gap:20px;">'
            '<div class="caps" style="font-size:19px; color:%s;">GIGI MIRONOVA · REALTOR®</div>'
            '<div class="ru" style="font-size:37px; line-height:1.52; color:%s;">%s</div>'
            '</div>'
            '<div style="font-size:29px; line-height:1.5; color:%s; max-width:800px;">'
            'one promise, one service, one way in — and the second language moved out of the '
            'fine print and into the <span class="si" style="font-size:34px;">offer.</span></div>'
            '<div style="background:%s; padding:30px 34px; font-size:27px; line-height:1.45; '
            'color:%s;">'
            'her name leads every graphic. the brokerage sits in the profile name field.</div>'
            % (T.HAIRLINE, T.MUTED, T.INK, bio, T.MUTED, T.HAIRLINE, T.INK))
    return structure("", 'the bio, rebuilt around<br>the one thing a competitor<br>'
                         'cannot <span class="si">hire.</span>',
                     card, HANDLE, "PROFILE", "INSTAGRAM BIO — 149 CHARACTERS", "01 / 02",
                     head_size=64)


def highlight_board():
    words = ["ESCROW", "OFFERS", "CLOSED", "SFV", "CONEJO", "РУССКИЙ", "TIPS", "TEAM", "GIGI"]
    cells = []
    for w in words:
        size = 27 if len(w) <= 6 else 23
        cells.append(
            '<div style="display:flex; flex-direction:column; align-items:center; gap:16px;">'
            '<div class="ru" style="width:186px; height:186px; border-radius:50%%; '
            'background:%s; display:flex; align-items:center; justify-content:center;">'
            '<span class="caps" style="font-size:%dpx; color:#FFFFFF; letter-spacing:0.14em; '
            'text-align:center; line-height:1.2;">%s</span></div></div>' % (T.BAND, size, w))
    grid = ('<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:34px 24px; '
            'justify-items:center;">%s</div>' % "".join(cells))
    tail = ('<div style="background:%s; padding:30px 34px; font-size:27px; line-height:1.45; '
            'color:%s;">nine words, nine <span class="si" style="font-size:31px;">entrances</span> — one for each thing '
            'someone arriving on the profile is actually looking for.</div>' % (T.HAIRLINE, T.INK))
    return structure("", 'nine covers.<br>nine different <span class="si">doors.</span>',
                     grid + tail, HANDLE, "PROFILE", "HIGHLIGHT COVER SET", "02 / 02",
                     head_size=64)


BOARDS = [
    # STORY slides carry photography; STRUCTURE slides stay white and must be the
    # densest layouts in the deck. Ratio held at 2 structure / 4 story across the
    # carousel proper, matching the reference build.

    ("C1", "C1 · Hook", lambda: story(
        # golden-hour valley: the strongest frame in the bank, and warm enough that the
        # oxblood tint reads as the photograph's own light rather than a filter on it
        "palm-tree-sunset-city-01", "bleed", "50% 54%", "17",
        'your offer was accepted.<br>a clock started that<br>nobody '
        '<span class="si">explained.</span>',
        "three deadlines run from the day you sign. miss one and the protection you paid "
        "for quietly stops protecting you.",
        HANDLE, SERIES, "SWIPE — THE PART NOBODY EXPLAINS", "1 / 6", head_size=88)),

    ("C2", "C2 · Day Zero", lambda: story(
        # cropped hard onto the signature itself — the wide frame reads as stock, the
        # tight one reads as a moment
        "contract-signing-pen-01", "duo", "42% 64%", "0",
        'day <span class="si">zero</span> is the<br>day you both sign.',
        "every deadline in the contract counts from the next morning — not from the "
        "inspection, not from the day your lender finally calls. from acceptance.",
        HANDLE, SERIES, "THE AMERICAN TRANSACTION", "2 / 6", gy=240, scale=1.55)),

    ("C3", "C3 · Three Deadlines", lambda: structure(
        "21", 'three deadlines.<br>three <span class="si">separate</span> clocks.',
        deadline_columns(), HANDLE, SERIES,
        "SOURCE: C.A.R. RESIDENTIAL PURCHASE AGREEMENT — DEFAULT PERIODS", "3 / 6",
        gy=250)),

    ("C4", "C4 · The Deposit", lambda: story(
        # archival press negative — scale crops the black scan border off this frame only
        "table-math-01", "duo", "50% 46%", "3",
        'the deposit is due in<br>three business days.<br>it is not a '
        '<span class="si">fee.</span>',
        "1–3% of the price, wired to a neutral third party — not to the seller, not to "
        "your agent. while a contingency is still live, it comes back to you.",
        HANDLE, SERIES, "THE AMERICAN TRANSACTION", "4 / 6", gy=230, scale=1.16)),

    ("C5", "C5 · Three Questions", lambda: structure(
        "", 'three questions before<br>you remove <span class="si">anything.</span>',
        questions([
            "which contingency am I removing, and what does it stop protecting?",
            "what is the exact calendar date, counted from acceptance?",
            "what happens to my deposit if I walk away after this?",
        ], note="removing a contingency is a signature, not a formality. it is the moment "
                "your deposit stops being refundable."),
        HANDLE, SERIES, "SAVE THIS BEFORE YOUR NEXT OFFER", "5 / 6")),

    ("C5RU", "C5 · Three Questions · RU", lambda: structure(
        "", 'три вопроса, прежде<br>чем подписать отказ<br>от <span class="si">условий.</span>',
        questions([
            "От чего именно защищало меня это условие?",
            "Какая точная дата, если считать со дня подписания?",
            "Что будет с моим депозитом, если я выйду из сделки после этого?",
        ], note="снятие условия — это подпись, а не формальность. именно с этого момента "
                "депозит перестаёт быть возвратным."),
        HANDLE, SERIES_RU, "ТОТ ЖЕ ВОПРОС, ДРУГОЙ ЯЗЫК", "5 / 6",
        ru=True, head_size=62)),

    ("C6", "C6 · CTA", lambda: story(
        "sunlight-through-window-floor-00", "bleed", "50% 62%", "",
        'you can read<br>the contract. or you<br>can have it '
        '<span class="si">explained.</span>',
        "escrow, contingencies, deposits — the whole American transaction, walked through "
        "before you sign. in English or in Russian.",
        HANDLE, SERIES, "GIGI MIRONOVA · REALTOR®", "6 / 6",
        extra=cta_button("DM «СДЕЛКА» OR ESCROW"))),

    ("R1", "Reel 1 Cover", lambda: reel(
        "balcony-plants-apartment-02", "duo", "50% 40%", "17",
        'your offer got<br>accepted. a clock<br><span class="si">started.</span>',
        "REEL · 01")),

    ("R2", "Reel 2 Cover", lambda: reel(
        "front-door-house-02", "duo", "50% 50%", "3",
        'you wired three<br>percent. where<br>did it <span class="si">go?</span>',
        "REEL · 02", scale=1.14)),

    ("R3", "Reel 3 Cover · RU", lambda: reel(
        "palm-tree-sunset-city-00", "duo", "50% 46%", "21",
        'вам одобрили<br>предложение.<br>часы уже <span class="si">идут.</span>',
        "REEL · 03", ru=True, series=SERIES_RU, scale=1.18)),

    ("R4", "Reel 4 Cover · Portrait slot", lambda: reel(
        # no photograph on purpose. the bank has no usable portraiture (DESIGN.md § imagery
        # — every human frame under CC0 is posed stock), and this is the one line in the
        # set that is hers. an empty oxblood field is the strongest holder for it, and it
        # is exactly the shape her own portrait drops into when she sends one.
        None, None, None, "",
        'I don\'t have anyone<br>to fall back on.<br>so my clients '
        '<span class="si">do.</span>',
        "REEL · 04 — PORTRAIT SLOT")),

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

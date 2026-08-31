#!/usr/bin/env python3
"""
Authority drops — two post-today carousels beyond the unit-124 kit.

D-series (sellers): "The $25,000 Conversation" — the concession gap. Sources: SFV April
2026 closed-sales compilation (556 sales; labeled on-slide) + Redfin national record
(VERIFIED). K-series (buyers): "The Clock" — C.A.R. default contingency periods,
verified 2026-08-30 against multiple sources.

Runs AFTER build.py: reuses its helpers and appends to canvas.json.

    python3 build.py && python3 build_drops.py
"""
import json

import build as B
import tokens as T

HERE = B.HERE

S_NET = "THE $25,000 CONVERSATION"
S_CLOCK = "THE CLOCK"


def two_stat():
    rows = [("99.6%", "average sale-to-list price, SFV April closings", False),
            ("52.9%", "of those sales carried a seller concession", True)]
    out = []
    for n, label, lead in rows:
        out.append(
            '<div style="display:flex; align-items:baseline; gap:34px; '
            'border-top:%dpx solid %s; padding-top:22px;">'
            '<div class="num" style="font-size:96px; color:%s; min-width:340px;">%s</div>'
            '<div style="font-size:28px; line-height:1.42; color:%s;">%s</div></div>'
            % (6 if lead else 1, T.INK if lead else T.HAIRLINE,
               T.INK if lead else T.MUTED, n, T.MUTED, label))
    return '<div style="display:flex; flex-direction:column; gap:24px;">%s</div>' % "".join(out)


def days_pair():
    rows = [("22", "the median days on market you hear about", False),
            ("40.7", "the average nobody mentions", True),
            ("1 in 5", "homes took over sixty days", False)]
    out = []
    for n, label, lead in rows:
        out.append(
            '<div style="display:flex; align-items:baseline; gap:34px; '
            'border-top:%dpx solid %s; padding-top:20px;">'
            '<div class="num" style="font-size:84px; color:%s; min-width:340px;">%s</div>'
            '<div style="font-size:28px; line-height:1.42; color:%s;">%s</div></div>'
            % (6 if lead else 1, T.INK if lead else T.HAIRLINE,
               T.INK if lead else T.MUTED, n, T.MUTED, label))
    return '<div style="display:flex; flex-direction:column; gap:22px;">%s</div>' % "".join(out)


def clock_columns():
    cols = [("17", "INSPECTION", False), ("17", "APPRAISAL", False), ("21", "LOAN", True)]
    cells = []
    for num, label, lead in cols:
        cells.append(
            '<div style="flex:1; border-top:6px solid %s; padding-top:24px;">'
            '<div class="num" style="font-size:110px; color:%s;">%s</div>'
            '<div class="caps" style="font-size:18px; color:%s; margin-top:16px;">%s</div>'
            '<div class="caps" style="font-size:17px; color:%s; margin-top:8px; '
            'opacity:0.6;">DAYS</div></div>'
            % (T.INK if lead else T.HAIRLINE, T.INK if lead else T.MUTED, num,
               T.MUTED, label, T.MUTED))
    return ('<div style="display:flex; gap:24px;">%s</div>' % "".join(cells)) + B.body(
        "all three are C.A.R. defaults, and all three are negotiable. they count in "
        "calendar days — saturdays and sundays sit inside the number, not on top of it.",
        False, 800)


DROPS = [
    # ---- sellers: the $25,000 conversation --------------------------------
    ("D1", "D1 · Net Hook", lambda: B.story(
        "balcony-plants-apartment-02", "duo", "50% 60%", "25",
        [B.head('valley sellers got their<br>price. it cost them '
                '<span class="si">$25,000.</span>', 72),
         B.body("april's closed sales read 99.6% of list — and more than half of them "
                "quietly wrote a check on the way out. swipe.", True, 660)],
        B.NAME, S_NET, "SWIPE — WHERE THE NEGOTIATION WENT", "1 / 5")),

    ("D2", "D2 · Two Numbers", lambda: B.structure(
        "52",
        [B.head('the price held.<br>the <span class="si">net</span> moved.', 76),
         two_stat(),
         B.body("a concession is money back at closing — repairs, closing costs, a rate "
                "buydown. it never shows up in the sale price your neighbor quotes you. "
                "the median here: $25,000.", False, 800)],
        B.NAME, S_NET, "SFV APRIL 2026 · 556 CLOSED SALES, MLS COMPILATION", "2 / 5",
        gy=430, foot_size=15)),

    ("D3", "D3 · Two Markets", lambda: B.structure(
        "40",
        [B.head('"22 days on market"<br>is two markets wearing<br>one '
                '<span class="si">number.</span>', 64),
         days_pair(),
         B.body("a fifth of homes went in a week. another fifth sat past sixty days. "
                "which market your home lands in is decided before the sign goes up — "
                "by pricing, prep, and the story the listing tells.", False, 800)],
        B.NAME, S_NET, "SAME SOURCE — THE SPLIT INSIDE THE AVERAGE", "3 / 5",
        gy=430, foot_size=16)),

    ("D4", "D4 · The Question", lambda: B.structure(
        "",
        [B.head('stop asking what your<br>home will list for. ask<br>what you will '
                '<span class="si">net.</span>', 62),
         B.docs([("the concession plan",
                  "what does the data say buyers in this bracket are asking for?"),
                 ("the two-markets plan",
                  "what puts this home in the one-week market, not the sixty-day one?"),
                 ("the net sheet",
                  "after concessions, fees and payoff — what lands in your account?")],
                "any agent can quote a list price. the net sheet is where the truth "
                "lives, and I run it before you commit to anything.")],
        B.NAME, S_NET, "THREE QUESTIONS FOR ANY AGENT, ME INCLUDED", "4 / 5")),

    ("D5", "D5 · Net CTA", lambda: B.story(
        "sunlight-through-window-floor-00", "bleed", "50% 44%", "",
        [B.head('want the honest number,<br>not the flattering '
                '<span class="si">one?</span>', 72),
         B.body("send me your address and I'll run a net sheet — price, likely "
                "concessions, fees, what actually lands. no listing agreement, no "
                "pressure. sixteen years of reading fine print says I'd rather you "
                "know.", True, 700),
         B.cta_button("DM ME “NET”")],
        B.NAME, S_NET, B.NAME, "5 / 5")),

    # ---- buyers: the clock ------------------------------------------------
    ("K1", "K1 · Clock Hook", lambda: B.story(
        "roofline-sky-00", "bleed", "50% 78%", "17",
        [B.head('your offer was accepted.<br>three clocks just '
                '<span class="si">started.</span>', 72),
         B.body("and the protection you paid for expires on a schedule almost nobody "
                "explains. swipe — it takes ninety seconds.", True, 660)],
        B.NAME, S_CLOCK, "SWIPE — THE PART NOBODY EXPLAINS", "1 / 5")),

    ("K2", "K2 · Three Clocks", lambda: B.structure(
        "21",
        [B.head('three deadlines, three<br><span class="si">separate</span> clocks.', 72),
         clock_columns()],
        B.NAME, S_CLOCK, "SOURCE: C.A.R. RESIDENTIAL PURCHASE AGREEMENT DEFAULTS", "2 / 5",
        gy=430, foot_size=15)),

    ("K3", "K3 · Day Zero", lambda: B.structure(
        "0",
        [B.head('day zero is the day<br>you both <span class="si">sign.</span>', 76),
         B.docs([("the clocks start the next morning",
                  "not at inspection, not when your lender calls back. at acceptance."),
                 ("weekends count",
                  "17 calendar days with two weekends inside is 11 working days."),
                 ("the deposit moves first",
                  "typically 1–3% of the price, wired to neutral escrow within 3 "
                  "business days.")],
                "miss a removal date and the protection you negotiated stops "
                "protecting you. calendar first, feelings second.")],
        B.NAME, S_CLOCK, "HOW THE COUNTING ACTUALLY WORKS", "3 / 5")),

    ("K4", "K4 · The Move", lambda: B.structure(
        "3",
        [B.head('the move: date every<br>deadline before you '
                '<span class="si">offer.</span>', 66),
         B.docs([("write the actual dates",
                  "not “17 days” — the calendar date each protection expires."),
                 ("decide the walk-away math early",
                  "what has to be true by day 17 for you to remove inspection?"),
                 ("never remove by default",
                  "removal is a signature, not a deadline passing. nothing happens "
                  "automatically.")],
                "I build this calendar for my buyers the day an offer is drafted — "
                "before anyone is emotionally committed.")],
        B.NAME, S_CLOCK, "SAVE THIS FOR YOUR NEXT OFFER", "4 / 5")),

    ("K5", "K5 · Clock CTA", lambda: B.story(
        "palm-tree-sunset-city-00", "duo", "50% 46%", "",
        [B.head('want the deadline calendar<br>before you write an '
                '<span class="si">offer?</span>', 68),
         B.body("message me and I'll walk you through the clock on your exact "
                "timeline — in English or in Russian. reading the fine print is the "
                "sixteen-year habit I brought to this license.", True, 700),
         B.cta_button("DM ME “CLOCK”")],
        B.NAME, S_CLOCK, B.NAME, "5 / 5", scale=1.18)),
]


def main():
    cv = json.load(open(HERE / "canvas.json"))
    kept = [a for a in cv["artboards"] if not a["file"].split(".")[0] in
            {k for k, _, _ in DROPS}]
    y0 = 1520 * 2  # third row: drops sit under the kit boards
    for i, (key, title, fn) in enumerate(DROPS):
        name = "%s.dc.html" % key
        (HERE / name).write_text(fn())
        kept.append({"file": name, "x": (i % 5) * 1200, "y": y0 + (i // 5) * 1520,
                     "w": 1080, "h": 1350, "title": title})
    cv["artboards"] = kept
    json.dump(cv, open(HERE / "canvas.json", "w"), indent=2)
    print("%d drop artboards appended -> canvas.json (%d total)"
          % (len(DROPS), len(kept)))


if __name__ == "__main__":
    main()

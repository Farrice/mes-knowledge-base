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
    rows = [("99.6%", "of asking price — what the neighbors heard", False),
            ("52.9%", "of sellers quietly gave money back anyway", True)]
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
    rows = [("22", "the fast ones — priced right, gone in days", False),
            ("40.7", "the real average, once the slow ones count", True),
            ("1 in 5", "sat for two months or more", False)]
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
        "these are the standard defaults, and yes, they're negotiable. they also count "
        "in calendar days, weekends included. which matters more than it sounds, "
        "because of when they start.", False, 800)


DROPS = [
    # ---- sellers: the $25,000 conversation --------------------------------
    ("D1", "D1 · Net Hook", lambda: B.story(
        "balcony-plants-apartment-02", "duo", "50% 60%", "25",
        [B.head('your neighbor sold for<br>asking. they still wrote a<br>$25,000 <span class="si">check.</span>', 68),
         B.body("more than half the Valley homes that sold this spring handed money back "
                "at the closing table. so the number they told you and the number they "
                "kept aren't the same number.", True, 660)],
        B.NAME, S_NET, "SWIPE — WHERE THE NEGOTIATION WENT", "1 / 5")),

    ("D2", "D2 · Two Numbers", lambda: B.structure(
        "52",
        [B.head('the sale price is public.<br>the check is <span class="si">private.</span>', 70),
         two_stat(),
         B.body("repairs, the buyer's closing costs, a lower rate for them. all of it comes "
                "off your side, and none of it shows up on Zillow. that's why the street "
                "can look stronger than your own sale feels. and the price isn't the only "
                "number that hides.", False, 800)],
        B.NAME, S_NET, "SFV APRIL 2026 · 556 CLOSED SALES, MLS COMPILATION", "2 / 5",
        gy=430, foot_size=15)),

    ("D3", "D3 · Two Markets", lambda: B.structure(
        "40",
        [B.head('"her place sold in a week.<br>why is mine still '
                '<span class="si">sitting?"</span>', 62),
         days_pair(),
         B.body("same street, same month, completely different endings. that's rarely luck. "
                "it's pricing, prep, and how the listing is told — decided before the "
                "sign goes up. and all of it lands on one number nobody leads with.", False, 800)],
        B.NAME, S_NET, "SAME SOURCE — THE SPLIT INSIDE THE AVERAGE", "3 / 5",
        gy=430, foot_size=16)),

    ("D4", "D4 · The Question", lambda: B.structure(
        "",
        [B.head('the only number that<br>matters: what you '
                '<span class="si">keep.</span>', 68),
         B.docs([("what will buyers ask me to fix?",
                  "every bracket has its pattern. knowing it beats guessing at the "
                  "kitchen table."),
                 ("which market will my home land in?",
                  "the one-week market or the two-month one — decided before listing."),
                 ("after everything, what hits my account?",
                  "price minus give-backs, fees, and payoff. the number nobody leads "
                  "with.")],
                "I put all three on one page before you decide anything. it's called a net "
                "sheet, it's free, and it's the first thing I'd want if it were my house.")],
        B.NAME, S_NET, "THREE QUESTIONS FOR ANY AGENT, ME INCLUDED", "4 / 5")),

    ("D5", "D5 · Net CTA", lambda: B.story(
        "sunlight-through-window-floor-00", "bleed", "50% 44%", "",
        [B.head('want the honest number,<br>not the flattering '
                '<span class="si">one?</span>', 72),
         B.body("send me your address and I'll put the real number on one page. price, "
                "likely give-backs, fees, what actually lands. no listing agreement, no "
                "pressure. I'd rather you know early than find out at the table.", True, 700),
         B.cta_button("DM ME “NET”")],
        B.NAME, S_NET, B.NAME, "5 / 5")),

    # ---- buyers: the clock ------------------------------------------------
    ("K1", "K1 · Clock Hook", lambda: B.story(
        "roofline-sky-00", "bleed", "50% 78%", "17",
        [B.head('three deadlines started<br>the day you signed. nobody<br>hands you the <span class="si">dates.</span>', 64),
         B.body("they're already running. most first-time buyers find out when one has "
                "nearly run out. so here they are, all three, in about ninety seconds.", True, 660)],
        B.NAME, S_CLOCK, "SWIPE — THE PART NOBODY EXPLAINS", "1 / 5")),

    ("K2", "K2 · Three Clocks", lambda: B.structure(
        "21",
        [B.head('three deadlines, three<br><span class="si">separate</span> clocks.', 72),
         clock_columns()],
        B.NAME, S_CLOCK, "CALIFORNIA'S STANDARD CONTRACT — THE C.A.R. DEFAULTS", "2 / 5",
        gy=430, foot_size=15)),

    ("K3", "K3 · Day Zero", lambda: B.structure(
        "0",
        [B.head('the countdown starts<br>while you&#8217;re still '
                '<span class="si">celebrating.</span>', 66),
         B.docs([("the clocks start the morning after you sign",
                  "not at the inspection. not when the lender calls back. the morning "
                  "after."),
                 ("weekends count against you",
                  "17 days with two weekends inside is really 11 working days."),
                 ("your deposit moves in the first 3 days",
                  "1–3% of the price, wired to a neutral account while everything else "
                  "is still sinking in.")],
                "none of this is scary once somebody shows it to you. it's only dangerous "
                "in the dark. so here's what the buyers who stay calm actually do.")],
        B.NAME, S_CLOCK, "HOW THE COUNTING ACTUALLY WORKS", "3 / 5")),

    ("K4", "K4 · The Move", lambda: B.structure(
        "3",
        [B.head('buyers who keep their<br>deposits do <span class="si">this.</span>', 70),
         B.docs([("put the real dates in your phone",
                  "not “17 days” — the actual calendar date each protection ends."),
                 ("know your walk-away number early",
                  "decide what has to be true by day 17 — before you fall in love."),
                 ("never let a deadline pass quietly",
                  "giving up a protection is a signature you choose, not a date that "
                  "slips by.")],
                "I build this calendar for my buyers the day we draft the offer, while "
                "everyone's head is still clear. it takes about ten minutes.")],
        B.NAME, S_CLOCK, "SAVE THIS FOR YOUR NEXT OFFER", "4 / 5")),

    ("K5", "K5 · Clock CTA", lambda: B.story(
        "palm-tree-sunset-city-00", "duo", "50% 46%", "",
        [B.head('want your deadlines<br>mapped before you '
                '<span class="si">offer?</span>', 70),
         B.body("message me and I'll map your dates before you write anything, in plain "
                "English or по-русски. ten minutes now saves the conversation nobody "
                "wants to have later.", True, 700),
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

#!/usr/bin/env python3
"""Jen · 'still renting' v2 — craft-room pass on v1.
Pen: one integrator over three loaded sources — Alyssa Stalker hook-reframe (Topic + Who + Lens; her
account's outlier shape is the who-clause), Luke Iha vicious-hook principles (consequence first, open
loop, Germanic words, stakes, not-an-ad), Scrapes carousel-first-slide formulas (period in the middle,
broken numbers, expectation inversion). Check: Jen-as-herself (calm, no rent-shaming, no FOMO, fair-housing).
Take A = who-clause cover (her outlier pattern). Take B = expectation-inversion cover (cover_stack).
Interior frames are shared. Renders to v2/."""
import pathlib, sys

ROOT = pathlib.Path("/Users/farricecain/Google Antigravity")
VE = ROOT / "_active/clients/jen-listings/06-system/valley-editions"
IMG = ROOT / "_active/clients/jen-listings/04-deliverables/2026-09-01-september-carousels/img"
OUT = pathlib.Path(__file__).parent / "v2"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(VE))
import editions as E  # noqa: E402

cover_a = E.cover_gem(
    IMG / "vannuys-valerio-2024.jpg",
    "The Valley &#183; a market read<br>September 2026",
    "you saved the down payment.",
    "then stopped looking.",
    "four houses in tarzana just closed under the number you gave up on. here's the price nobody screenshots.",
    pos="50% 45%")

cover_b = E.cover_stack(
    IMG / "vannuys-valerio-2024.jpg", "Jen Santulan", "the valley, translated",
    "priced out", "the wrong number.", "of",
    "four tarzana houses closed between $840,000 and $950,000 last week. not one of them was on your screen.",
    "jen santulan", pos="50% 45%", corner="left")

interior = [
    ("02-asking.png", E.moment(
        IMG / "suburban-neighborhood-aerial-02.jpg", "THE VALLEY", "SEPTEMBER 2026", "Asking.",
        ["the price you screenshot at 11pm is the asking price. nobody pays it.",
         "the price that closes is a different number.",
         "tarzana, july: 98 cents on the dollar. after 58 days."], 2, pos="50% 50%")),
    ("03-closed.png", E.moment(
        IMG / "vannuys-street-scene.jpg", "THE VALLEY", "SEPTEMBER 2026", "Closed.",
        ["last week of august. four houses. tarzana.",
         "$840,000. $866,000. $917,500. $950,000.",
         "every one under the $1.2M you keep scrolling past."], 3, pos="50% 55%")),
    ("04-rent.png", E.moment(
        IMG / "apartment-building-dusk-03.jpg", "THE VALLEY", "SEPTEMBER 2026", "Rent.",
        ["$45,600. that's a year of la rent at $3,800 a month.",
         "you paid it. it kept a roof up. it's gone.",
         "the down payment you saved is the only money in this story that's still yours."], 4, pos="50% 40%")),
    ("05-wrong-number.png", E.statement(
        IMG / "jen-porch-vannuys.jpg", "Jen Santulan", "the valley, translated",
        "wrong", "number.",
        "you weren't priced out. you were reading the wrong number. send me yours, buying or selling, and i'll send you the three i'd actually go see.",
        corner="left", pos="50% 30%")),
    ("06-close.png", E.close(
        IMG / "sunlight-through-window-floor-00.jpg",
        "The Valley &#183; a series",
        "Send Me<br>Your Number.",
        "i'm here for you. that's my job. i do this to protect you and your best interest.",
        "my DMs are open &rarr;", pos="50% 50%")),
]

if __name__ == "__main__":
    E.render(cover_a, str(OUT / "01-cover-A.png"))
    E.render(cover_b, str(OUT / "01-cover-B.png"))
    for name, html in interior:
        E.render(html, str(OUT / name))
    print("rendered v2 →", OUT)

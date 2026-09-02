#!/usr/bin/env python3
"""Jen · 'still renting' carousel — renders six frames through Jen's approved surface
(valley-editions/editions.py archetypes: cover_gem, moment ×3, statement, close), which is
the on-brand translation of the 'Yellow and Black Modern Travel Moments' Canva grammar
(Design 2 → moment frames). Copy lives in post.yaml; this file is the plate list + calls."""
import pathlib, sys

ROOT = pathlib.Path("/Users/farricecain/Google Antigravity")
VE = ROOT / "_active/clients/jen-listings/06-system/valley-editions"
IMG = ROOT / "_active/clients/jen-listings/04-deliverables/2026-09-01-september-carousels/img"
OUT = pathlib.Path(__file__).parent
sys.path.insert(0, str(VE))
import editions as E  # noqa: E402

frames = [
    ("01-cover.png", E.cover_gem(
        IMG / "vannuys-valerio-2024.jpg",
        "The Valley &#183; a market read<br>September 2026",
        "you saved the down payment.",
        "still renting.",
        "everything you scroll reads $1.2M. four tarzana houses closed between $840K and $950K in the last week of august. here's the read.",
        pos="50% 45%")),
    ("02-asking.png", E.moment(
        IMG / "suburban-neighborhood-aerial-02.jpg", "THE VALLEY", "SEPTEMBER 2026", "Asking.",
        ["what you see on zillow is the asking price. not the sale price.",
         "in tarzana, homes closed at 98% of asking in july.",
         "after 58 days on the market. sellers are talking."], 2, pos="50% 50%")),
    ("03-closed.png", E.moment(
        IMG / "vannuys-street-scene.jpg", "THE VALLEY", "SEPTEMBER 2026", "Closed.",
        ["four tarzana houses sold in the last week of august.",
         "$840K. $866K. $917K. $950K. three to four bedrooms.",
         "the tarzana median is $949K. every one was at or under it."], 3, pos="50% 55%")),
    ("04-rent.png", E.moment(
        IMG / "apartment-building-dusk-03.jpg", "THE VALLEY", "SEPTEMBER 2026", "Rent.",
        ["the la median rent is $3,800 a month.",
         "that's $45,600 a year, and none of it comes back to you.",
         "you're not priced out. you're waiting for a number you'd feel good about."], 4, pos="50% 40%")),
    ("05-not-your-number.png", E.statement(
        IMG / "jen-porch-vannuys.jpg", "Jen Santulan", "the valley, translated",
        "not your", "number.",
        "the listing you screenshotted isn't the market. the closed ones are. send me your number, buying or selling, and i'll send you the three i'd actually go see.",
        corner="left", pos="50% 30%")),
    ("06-close.png", E.close(
        IMG / "sunlight-through-window-floor-00.jpg",
        "The Valley &#183; a series",
        "Send Me<br>Your Number.",
        "i'm here for you. that's my job. i do this to protect you and your best interest.",
        "my DMs are open &rarr;", pos="50% 50%")),
]

if __name__ == "__main__":
    for name, html in frames:
        E.render(html, str(OUT / name))
    print("rendered", len(frames), "frames →", OUT)

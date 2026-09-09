# First Home Valley — demo run of show

Everything below is built, smoke-tested, and live. This page is the operator sheet; nothing here is for Jen's eyes.

## Before you sit down

- Demo on **your own signed-in device**. All four artifacts are **private** — a link you text her opens as "Page not found" until you hit Share on each one.
- Laptop or iPad beats phone: the tap-through has a carousel lightbox and a teleprompter panel that both want room.
- Backup if the room has no wifi: `png/` — the same 12 assets as image files, swipeable from the camera roll.

## The three links, in order

| # | Open | What it does | Link |
|---|---|---|---|
| 1 | **The First Home Valley** | The demo itself. Four tap-through demos, a rebuttal round, the math to 2–3 closings, and three asks at the end. Self-running — you tap, she reacts. | https://claude.ai/code/artifact/14e85fc0-dcc2-40f5-9ab0-a112b1aacd23 |
| 2 | **The Willis Receipts** | "And here's what it did to your actual listing." 6853 Willis: three claims cut before filming, four gone stale in eight weeks including the price. | https://claude.ai/code/artifact/45a9af8d-e5e5-4468-967c-461dc2c28f1e |
| 3 | **The Content Audit** | Only if she asks how the numbers get checked. 41 claims across 13 assets, six corrections, one number still to pull. | https://claude.ai/code/artifact/b589df52-c342-498a-9862-e5176a2178ce |

Also live: **First Home Valley Assets** — the editable design canvas, linked from inside demo #1 ("Open the editable assets"). Don't open it cold; let the page take her there. https://claude.ai/code/artifact/d3ff25b2-dc0f-42f6-b088-8c6733919a47

## What she taps (verified working, 30 Aug)

- **Demo 01 · The feed** — 12 tiles. Tap one, a lightbox opens with Prev / Close / Next. Slide 1 is "is 40 too late to buy your first home?"
- **Demo 02 · The teleprompter** — "▸ Roll it" starts the Reel 02 script line by line, on-screen text and progress dots included. ~35 seconds of film time.
- **Demo 03 · The DM machine** — "▸ A viewer just commented" plays a 9-step keyword-to-booking sequence.
- **Demo 04 · The magnet** — the one-page math sheet, rent vs. 20% down vs. 3.5% + MyHome, with the 2026 program menu.
- **The rebuttal round** — six objections, each tap reveals the receipt. Start her on "Renting is cheaper right now."

## The close is already on the page

The last section asks her for three things. Don't improvise past it:

1. Pick the first post — carousel or any reel, goes up this week as-is.
2. Voice verdict — read the teleprompter script out loud; any line she wouldn't say to a friend gets rewritten.
3. Greenlight the channel — YouTube + math sheet live inside two weeks.

## Open item (not a demo blocker)

The flagship 12-minute script is cleared to shoot except one figure: **pull the SFV single-family median from SRAR the week you record**, or make the point without a number. The on-screen card already has the figure removed and a stop-line in the script.

## Where the source lives

- Artboards: `canvas/` (12 `.dc.html` + `canvas.json`) — recovered from the previous session's temp scratchpad, which would have been wiped.
- Rendered stills: `png/` — `python3 render_png.py` regenerates all 12 at 1080×1350 @2x.
- Edit the design in the canvas artifact, then re-export; edit copy in the `.dc.html` files and re-seed.

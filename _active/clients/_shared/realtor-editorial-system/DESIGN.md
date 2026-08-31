# The First Home File — realtor editorial system

**This is the floor, not a ceiling.** Verdict from Farrice, 2026-08-30, on the First Home
Valley v2 deck: *"premium, high taste, quality, done right… this should be the floor. If we
were to generate these for a different agent or person, this is a good starting point."*

Any agent deck built from here starts at this bar. Going below it is a regression, not a
style choice.

Reference build: `_active/clients/jen-santulan/production/first-home-valley/canvas-v2/`
Rendered proof: that folder's `png/` (regenerate with `render_v2.py`).

---

## The one rule everything else serves

**Photo carries place and moment. Type carries the data. They never fight.**

Every failure in the first pass came from breaking this — bands laid over live type, a
global crop applied to individual layouts, a colour remap run on a slide that didn't need
it. The rule is the system; the tokens below are just how it was executed once.

---

## Slide taxonomy

Two kinds of slide, and the kind decides the treatment. Do not mix.

| | STRUCTURE | STORY |
|---|---|---|
| Carries | comparisons, lists, dense data, card layouts | a hook, a moment, a place, a payoff |
| Ground | white, always | full-bleed photograph |
| Type | navy on white | white on scrim |
| Example | A3 (29→40), A5 (three questions), M1 (magnet card) | A1 hook, A6 CTA, R1–R5 reel covers |

**Ratio that worked: 3 structure / 9 story out of 12.** The structure slides must be the
densest layouts in the deck. Three white slides among nine photographic ones is what stops
it reading as a stock-photo deck — the white is the luxury, not the photography.

---

## Tokens

```
ink            #1E3A5F   navy — all body and heading type on white
band           #16304F   deeper navy — dark grounds, tint layer
muted          #5A6B80   secondary copy on white
hairline       #DCE2EA   rules, dividers, left-borders
ghost          #E7EDF4   the oversized background numeral
steel          #4C7CA8   the italic accent (.si) on light grounds
steel-light    #C9D4E2   the italic accent on dark grounds
paper          #FFFFFF
```

Dark-ground remap (only on slides converted from light):

```
color:#1E3A5F  ->  #FFFFFF
#E7EDF4        ->  rgba(255,255,255,0.15)    ghost numeral
#DCE2EA        ->  rgba(255,255,255,0.34)    hairlines
#5A6B80        ->  rgba(255,255,255,0.74)    muted body
```

**Never run the remap on a slide already authored dark.** It inverts type that was already
correct — on A6 it turned a white button's navy label white and erased the call to action
entirely. Keep an explicit exception list.

## Type

- **Figtree** 400/500/600/700 — everything structural. Lowercase headlines are the register.
- **Playfair Display** italic 400/500 — the accent word only. One or two per slide, never a
  whole line. This is the single move that makes the deck read editorial rather than
  corporate.
- Headline 88–104px at 1080×1350, line-height ~1.12, letter-spacing −0.02em.
- Body 32–36px, line-height 1.45–1.5, behind a 2px left border with 28px padding.
- Eyebrow / footer: 19–23px, weight 600, letter-spacing 0.24em, uppercase.

## The ghost numeral

One oversized Playfair numeral per slide, 760px, `line-height:0.8`, bled off the right edge,
sitting at z-index 0 behind everything. It is the deck's signature and it does real work:
it fills negative space without adding content. Pick the number the slide is actually
about (40, 29, 21, 37, 20, 3).

---

## Photographic treatments

Two, and only two. Both are layer stacks over an `object-fit:cover` image.

**`bleed`** — colour photograph held, darkened enough that type sits anywhere on it.

```css
img    { filter: saturate(0.72) contrast(1.06) brightness(0.94); }
.tint  { background:#16304F; mix-blend-mode:multiply; opacity:0.42; }
.scrim { background:linear-gradient(180deg,
           rgba(9,20,34,0.62) 0%,  rgba(9,20,34,0.48) 26%,
           rgba(9,20,34,0.66) 60%, rgba(9,20,34,0.92) 100%); }
```

**`duo`** — navy duotone. For archival photographs and pure architecture.

```css
img   { filter: grayscale(1) contrast(1.14) brightness(0.86); }
.tint { background:#16304F; mix-blend-mode:multiply; opacity:0.92; }
.lift { background:#C9D7E8; mix-blend-mode:screen;   opacity:0.10; }
```

**Framing is per slide.** `object-position` and `transform:scale()` go on the individual
`<img>`, never in the shared stylesheet. A single global `scale(1.10)` — added once to hide
a scan border on one slide — quietly cropped 10% off every other image in the deck and
reduced two reel covers to a wrist on empty grey.

**Banned: edge bands.** These layouts pin content to both edges with
`justify-content:space-between`, so a top or bottom band has no empty edge to occupy and
lands on live type. If a slide can't take a full bleed, it is a structure slide. White it.

---

## Imagery sourcing

Real photographs only. No generated images, no illustration, no CGI renders — Farrice,
2026-08-30: *"I don't want you to use generated images unless they are actually accurate and
real or close to photorealistic."*

**Licence floor: CC0 or Public Domain Mark only.** Client feeds must carry no attribution
obligation. Openverse needs no API key and delivers these from rawpixel and StockSnap at
3000–10000px. Record every file's id, provider, licence, landing page and query.

Pipeline: `_active/clients/jen-santulan/production/first-home-valley/imagery/`
— `fetch_bank.py` (role-based) → `sweep.py` (wide) → `contact_sheet.py` → `make_shortlist.py`
→ `prepare.py` (long edge 1600, q70).

**Curate by eye, never by filename.** The hit rate on that pool was 24%: 93 fetched, 22 kept.

What to cut on sight, learned the hard way:
- posed smiling stock families — the photographic equivalent of AI slop, worse than no image
- CGI renders sold as photography
- wrong geography (Pacific Northwest damp, European ivy) in a California deck
- anything whose colour fights the brand, **even when it is the better photograph** —
  a yellow-wall/red-door frame was the strongest image in the bank and was cut for this

The pool's strength is **place**. Its weakness is **people**: every human frame available
under CC0 is posed stock, an engraving, or disembodied hands. A free Pexels or Unsplash key
(the operator must create it — Claude cannot make accounts) opens real portraiture, and
`execution/broll_source.py` already has that path wired.

**The agent's own photography beats all of it.** Always ask for originals first.

---

## Build method

Never retype copy to restyle it. `build_v2.py` reads each v1 artboard, injects a photo
layer, remaps colours on the slides that need it, and writes v2 beside it. v1 stays live and
untouched; the two can never drift. Any restyle of an approved deck should work this way.

Verify by rendering all slides into **one contact sheet** and looking at the grid
(`review_sheet.py`). Three of the four defects in the first pass were invisible in source
and obvious in the grid.

---

## Registers built on this grammar

| Register | Hue family | Built for | Where |
|---|---|---|---|
| Navy (reference) | `#1E3A5F` / `#16304F` | Jen Santulan — First Home Valley | `jen-santulan/production/first-home-valley/canvas-v2/` |
| Oxblood | `#4A1420` / `#3B0F1A` | Gigi Mironova — The American Transaction | `gigi-mironova/production/american-transaction/canvas/` |

Recommendation 2 below is **built**. A register is a hue-family swap plus its own token
file (`tokens.py`) — the grammar, the slide taxonomy, the ghost numeral and the two photo
treatments are shared and must not be re-derived. Two rules learned building the second one:

**Warm the bleed when the register is warm.** `bleed` holds the photograph's own colour at
`saturate(0.72)`. In a navy register that is invisible, because the bank leans cool and the
tint agrees with it. Drop the same treatment into a warm register and every cool-cast
photograph fights the tint — a blue-hour street frame under an oxblood tint reads as though
it wandered in from the other agent's deck. The oxblood register prepends
`sepia(0.30) hue-rotate(-10deg)` and lifts the tint to `0.50`, which lands the whole bank
in one family. Any new register needs the equivalent pass, chosen by eye against its bank.

**Ease the bottom scrim.** The reference gradient ends at `0.92`, which crushes the lower
third of a darker photograph to featureless mud. `0.86` holds type just as well and keeps
the image alive. Applied in oxblood; worth backporting.

**Different agents get different photographs, not the same ones recoloured.** The oxblood
deck shares zero images with the navy one. Same system, same grammar, no visual overlap —
otherwise the second deck reads as the first one with a filter on it.

## Cyrillic, and any non-Latin lane

**Figtree ships `latin` and `latin-ext` only. It has no Cyrillic subset.** Russian set in it
falls back to a system sans without erroring, and the register quietly breaks on exactly the
slide meant to prove the second-language lane works.

**Manrope** carries `cyrillic` and `cyrillic-ext` and is the closest geometric-humanist match
to Figtree on Google Fonts. **Playfair Display's italic carries Cyrillic too**, so the
accent-word move — the single thing that makes this system read editorial — survives the
language switch intact. Verified against the Google Fonts CSS API, 2026-08-30.

Implementation: one `.ru` class swapping only the structural family, applied at the frame.
Everything else is unchanged. Check the same way before adding any other script.

## The archival-scan trap

A large share of the CC0 bank is archival press and FSA negatives, and many carry a black
scan border and a handwritten negative number inside the frame. They are often the best
photographs available and they want the `duo` treatment.

Crop the border with `transform:scale()` **inline on the individual `<img>`** — 1.14–1.18
is usually enough. Never in the shared stylesheet: the reference deck's one global
`scale(1.10)`, added to fix exactly this on one slide, silently cropped 10% off every other
image and reduced two reel covers to a wrist on empty grey.

## Open recommendations

Offered when Farrice asked what else could extend or vary this. Recommendation 2 is now
built (see *Registers* above); 5 is half-answered.

1. **A light register.** Everything here is navy- or oxblood-dominant. A warm-paper variant —
   bone ground, ink type, one warm accent — would suit a luxury or Conejo Valley listing lane
   without abandoning the grammar.
2. ~~**Duotone in a second hue.**~~ **BUILT** — oxblood, 2026-08-30. See *Registers* above.
3. **Motion.** Reel covers are static frames of a video. One slow push-in on the bleed photo
   with the type held still would make the covers work as the first frame of the reel.
4. **A data-slide vocabulary.** A3's 29-vs-40 comparison and the oxblood deck's three-deadline
   ladder are the only quantitative layouts in the system. Two or three more (a share-of-market
   bar, a payment stack) would let structure slides carry more of the argument.
5. **The agent's own face.** Every strong realtor account eventually rests on the person, and
   the CC0 pool has no usable portraiture — every human frame is posed stock, an engraving, or
   disembodied hands. The oxblood deck's answer is a **portrait slot**: a photograph-free
   board in the flat register hue carrying one line, which holds a personal statement better
   than bad stock does and is the exact shape a real portrait drops into. That is a holding
   pattern, not a portrait treatment. The treatment still needs building, and it needs a real
   photograph — always ask the agent for originals first.

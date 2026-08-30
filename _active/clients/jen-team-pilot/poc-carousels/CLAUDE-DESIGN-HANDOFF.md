# Claude Design Handoff — Jen Carousels

Everything needed to pick this work up in Claude Design (desktop app), independent of this session.

## Where the work lives right now

- **Live editable canvas** (Claude Design editor, published): https://claude.ai/code/artifact/fa99084f-4f8f-4c90-b723-345f3c042dfa — open it, click any slide to edit, Export gives per-slide PNG or one PDF. This is already the real product; the packet below is for rebuilding or extending in the Claude Design app.
- **Working files**: this folder (`Main.dc.html`, `Buyer2-6`, `Seller1-6`, `canvas.json`, `gen_slides.py` regenerates all 12).
- **Brand spec**: `../agents/jen-brand-card.md` — attach it to any Claude Design chat as the brand file ("the brain" in Sherrard's method).

## Setup in Claude Design (once)

1. Claude desktop app → a Project for Jen's content (e.g. "Jen · Carousels").
2. Add `jen-brand-card.md` to the Project files.
3. Open Claude Design, paste the master prompt below, attach the copy deck (section 3).

---

## 1. THE MASTER PROMPT (copy-paste verbatim)

> Attached are (1) a brand card for realtor Jen Santulan with two brand lanes and (2) a finished 12-slide copy deck for two Instagram carousels. Build all 12 slides as 1080×1350 graphics. The copy is final — do not rewrite, shorten, or "improve" any of it; your job is design execution only.
>
> TWO LANES, NEVER BLENDED:
>
> LANE 1 — @_jiing buyer carousel (slides B1–B6): "warm editorial minimal." Ground #F7F5F2, navy ink #1E3A5F, hairlines #E0DBD2, muted grey #6B6C70. Type: Figtree (sans) + Playfair Display (serif). Headlines lowercase sans with Playfair-italic accent words. Signature moves: oversized ghosted Playfair numerals in #E9E3D9 bleeding off the frame edge behind content; tracked-caps micro-labels (letter-spacing 0.24em); thin vertical hairline beside body text; slides B4 and B6 flip to navy ground for rhythm; masthead row "@_JIING · FIRST-TIME BUYER FILE" over a hairline on every slide; italic serif page number "n / 6."
>
> LANE 2 — House Sellers seller carousel (slides S1–S6): "quiet luxury print." Deep navy #16304F, white, steel #4C7CA8, soft blue #C9D4E2, hairlines #D8DDE6. Every slide framed by a 1px inner border inset ~44px from the edge (luxury print device). Centered text lockup on every slide: HOUSE (weight 400) SELLERS (weight 600) | thin divider | EQUITY UNION REAL ESTATE in tracked caps. Playfair Display serif display type, dramatic scale, Title/sentence case. Slides S1 and S4 are dark navy; the rest white. Footer: "THE VALLEY" tracked caps + italic serif "n / 6" over a hairline. Data as thin 10px bars with large serif numerals; accent color on the winning bar only.
>
> QUALITY CONTRACT (non-negotiable):
> - Studio-made, editorial grade: confident typography, real grid, generous whitespace, deliberate spacing. If it looks like default AI output, redo it.
> - ONE dominant element per slide, clear hierarchy, readable in 3 seconds on a phone.
> - Max 2 font families. Dramatic scale contrast between display and support text. Nothing centered by default (Lane 2's centered masthead/hook is the deliberate exception).
> - Stats become shapes (bars, side-by-side panels), never a number floating in space.
> - Square corners everywhere. One accent used sparingly.
> - BANNED: stock photos, emojis as design elements, gradients, drop shadows, clip art, text touching edges, rounded cards, more than one idea per slide.
>
> PROCESS: build slide B1 and slide S1 first and show me both before building the rest. Apply my feedback across the whole set so all 12 read as two coherent brands.

## 2. WHAT TO ATTACH

- `jen-brand-card.md` (brand lanes, tokens, voice rules, fair-housing floor)
- The copy deck below (save as `carousel-copy-deck.md` or paste after the prompt)

## 3. THE COPY DECK (final copy — design executes, never rewrites)

### Buyer carousel — @_jiing lane

**B1 (hook)** — masthead: @_JIING / FIRST-TIME BUYER FILE · ghost numeral "20"
Headline: "you don't need *20 percent down* to buy a home in LA" (italics = Playfair italic accent)
Dek: "what buyers here actually put down, and the programs that close the gap"

**B2 (myth)** — page 2/6 · footer label: THE PART NOBODY EXPLAINS
Display: "*the myth*" → "save $200K first, then start looking."
Body: "the LA median is around $1M, so the math feels impossible from the outside." / "but most first-time buyers here don't put 20% down. down-payment programs exist for exactly this gap — and they change through the year."

**B3 (CalHFA)** — page 3/6 · eyebrow: PROGRAM · CALHFA MYHOME · hero numeral "3.5%"
Body: "of the purchase price, covered — for your down payment or closing costs." / "a deferred-payment junior loan for california first-time buyers: no monthly payments on that piece while you live in the home."
Footer: SOURCE: CALHFA 2026 · CONFIRM AVAILABILITY

**B4 (20% programs — NAVY slide)** — page 4/6 · ghost numeral "20" · footer label: ASK WHAT IS OPEN RIGHT NOW
Headline: "some programs have covered up to *20 percent* down" (keep "have covered" — the program's funding pauses; never "cover")
Body: "state assistance has covered as much as a fifth of the purchase price for eligible first-time buyers." / "which ones are open and funded changes month to month. tracking that is literally my job — so you don't have to refresh a state website."

**B5 (closing costs)** — page 5/6 · footer label: NO SURPRISES AT THE FINISH LINE
Headline: "the cost *nobody warns you about*"
Body: "closing costs run about 2-3% of the price — separate from your down payment."
Ledger rows: "on a $750K home → $15-22.5K" / "when to budget it → *from day one*"

**B6 (CTA — NAVY slide)** — page 6/6 · ghost key icon · footer: JEN SANTULAN · SFV & LOS ANGELES
Headline: "want the *real numbers* for your situation?"
Body: "rent vs. buy. what's open right now. what you'd actually need saved. no pressure — just the math."
CTA plate: DM ME *"keys"*

### Seller carousel — House Sellers lane

**S1 (hook — NAVY slide)** — centered, vertical rule drop
Display: "RENOVATING / BEFORE / YOU SELL?" · Italic subline: "most Valley sellers fix the wrong things."
Caps line: "WHAT THE COST-VS-VALUE DATA ACTUALLY SAYS · SWIPE"

**S2 (instinct vs data)** — page 2/6, two-beat split with hairline
THE INSTINCT → "*remodel the kitchen.*" (large italic serif)
THE DATA → "Small, visible fixes beat big renovations — almost every time."
Body: "A $90K kitchen rarely comes back at sale. Paint, landscaping, and the repairs that clear inspection objections usually do."

**S3 (ROI bars)** — page 3/6 · eyebrow: RETURN AT RESALE · headline: "What actually comes back"
Bars (thin, serif numerals; accent on row 1 only): Garage door replacement 268% · Steel entry door 216% · Stone veneer / curb appeal 208% · Bathroom remodel 50%
Source line: 2025 COST VS. VALUE REPORT · NATIONAL SAMPLE FIGURES — YOUR HOUSE IS ITS OWN CASE

**S4 (maintenance — NAVY slide)** — page 4/6
Display: "Buyers don't fall in love with your finishes." · Italic: "They fall out of love with your deferred maintenance."
Body: "Roof. HVAC. Water heater. The drip you stopped noticing. These surface in inspection, shake confidence, and complicate escrow more than any dated countertop ever will."

**S5 (pricing panels)** — page 5/6 · headline: "Pricing beats renovating"
Panel 1 (navy): PRICED RIGHT, DAY ONE → "23-35" → "days on market — often over asking"
Panel 2 (white): "TESTING THE MARKET" → "60+" → "days — then selling 5-8% below"
Source line: SAMPLE MARKET FIGURES — WE RUN YOUR STREET'S ACTUAL COMPS BEFORE PICKING A NUMBER

**S6 (CTA)** — page 6/6, centered · footer: THE VALLEY · MYHOUSESELLERS.COM
Display: "Thinking of selling this year?"
Body: "We'll walk your house room by room and tell you what's worth fixing — and what to leave exactly as it is."
CTA plate (navy): DM US *"sell"*

## 4. Guardrails that travel with this work

- Fair-housing floor: never describe the people ("perfect for families/couples"), never "safe"/"low-crime"/"good neighborhood," no school talk, no religious/demographic landmarks, no invented urgency, no payment promises without a lender quote. Every new slide gets screened.
- Stat slides keep their source lines and "sample figures" hedges. Jen verifies numbers before anything posts.
- B4 stays "have covered" (past tense). Factual honesty is part of the product.
- New carousels for other agents: same prompt, swap the brand card — that's the repeatable system.

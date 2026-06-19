---
description: Mine 20+ distinct new angles on a saturated/boring topic, score each on freshness × outcome-pull, rank, and flag the top 5 for hooking.
---

# /novelty-angles — Divergent Angle-Mining Engine

Generates a ranked supply of fresh angles on a topic that is objectively old, stale, or saturated. Fire this when the brief is "I have nothing new to say about X" or "I'm out of ideas for this niche." The supply of genuinely-new *topics* is near zero; the supply of new *angles on old topics* is infinite (../genius.md, Genius Pattern 1). This is the breadth engine. Once an angle is chosen, hand off to `./novelty-reveal.md` to convert it into a hook.

## Pre-Flight Gate

Load `../genius.md` if it is not already hot. Then answer, from the Decision Framework:

1. **Old or genuinely new?** If a real new tool/study/method exists, Path A applies and you may not need 20 angles — note it, then mine anyway for stacking. Default and the reason you're here: Path B, old topic.
2. **What does the avatar already believe about this topic?** You need the held belief to mine the CONTRAST and ENEMY levers. If you can't name it, stop and define the avatar (`kallaway-audience-obsession`, `mcraney-deep-canvass`, or an ICP skill).
3. **What outcome does the avatar actually want?** This is the denominator of every angle's outcome-pull score. One primary wanted result; list 2-3 secondary ones — different wanted results are themselves a lever (new OUTCOME).
4. **Which assets is this feeding?** A short-form script wants different angles than a landing page. Note the target asset(s) now; it changes which levers you weight (see Content-Type Adaptations).

Do not start mining until 2 and 3 are answered. A vague avatar produces vague angles and zero bullseye potential downstream.

## Skill Acquisition

- **Always:** `../genius.md` (the IP anchor — five components, twelve patterns, decision framework, rubric).
- **For the held belief (Contrast/Enemy levers):** `kallaway-audience-obsession`, or `mcraney-deep-canvass`, or any loaded ICP/avatar payload.
- **Downstream handoff:** `./novelty-reveal.md` (angle → hook), then `./novelty-forge.md` (hook → full five-component assembly).
- **If the topic genuinely has a real recency window:** keep `./novelty-urgency.md` in mind — flag it on the TIMEFRAME/UPDATE angles, do not invent it here.

## Execution

The method is systematic, not inspirational. Walk every lever; force at least one angle per lever, then push for multiples on the high-yield ones (FRAME, NAME, MECHANISM, CONTRAST). Treat it as a sweep, not a wait for the muse — this is what makes it agent-runnable (Hidden Knowledge: angle-mining is a *process*, not creativity).

### Step 0 — Lock the spine

Write down, in one line each: **Topic**, **Avatar**, **Primary wanted outcome**, **Held belief** (the thing they already think is true about this topic). Everything below references these four.

### Step 1 — Sweep the eleven levers

For each lever, produce one or more angles. An angle is a *one-line statement of a true thing seen from a new door* — not yet a hook. Levers, with the diagnostic prompt that generates each:

| # | Lever | Generating question |
|---|---|---|
| 1 | **FRAME** (re-categorize) | What is this *really* a category of? File it under an unexpected category. |
| 2 | **NAME** (coin proprietary IP) | What memorable name could I give this thing/method/problem? (Cheapest novelty lever — naming alone manufactures novelty. ../genius.md Hidden Knowledge.) |
| 3 | **UPDATE** (what changed recently) | What about this is genuinely different now vs. a year ago? |
| 4 | **FINDING** (non-obvious fact/stat/result) | What true number or result would make them go "wait, really?" |
| 5 | **MECHANISM** (hidden how-it-works) | What is the under-the-hood reason this actually works that nobody explains? |
| 6 | **CONTRAST** (vs. a held belief) | What does the avatar believe that the truth directly opposes? |
| 7 | **OUTCOME** (different wanted result) | If I tie this to a *different* thing they want, what new angle appears? |
| 8 | **AUDIENCE** (sub-segment call-out) | Which narrow sub-group does this matter to *most* — and differently? |
| 9 | **COMPARISON** (analogy to a far domain) | What unrelated field does this secretly resemble? |
| 10 | **ENEMY** (what to position against) | What practice/product/belief is the villain here? |
| 11 | **TIMEFRAME** (historical vs. future) | What's the origin story, or the where-this-is-going story? |

**Yield rule:** 11 levers × ~2 each ≥ 22 angles. Force a second pass on FRAME/NAME/MECHANISM/CONTRAST before you accept fewer than 20. If you stall, combine two levers (e.g., NAME + MECHANISM = "the [coined-name] effect" explaining the hidden how).

### Step 2 — Score every angle

Two 1-5 scores per angle:

- **Freshness (1-5):** how much this breaks the avatar's prediction. 1 = they've heard it; 5 = it reframes something they thought was settled. (This is the brain-stops-on-prediction-breaks axis — ../genius.md Pattern 2.)
- **Outcome-pull (1-5):** how directly the angle connects to a result they *demonstrably* want. 1 = interesting but they don't act on it; 5 = it sits right on top of the primary wanted outcome.

**Composite = Freshness × Outcome-pull** (1-25). The multiply, not the add, is deliberate: a 5-freshness angle tied to nothing (5×1=5) loses to a 4×4=16. Novelty without a wanted outcome still gets scrolled (../genius.md, "the new reveal makes them look, the outcome mapping makes them stay").

### Step 3 — Rank and flag

Sort by composite descending. **Flag the top 5.** For each flagged angle, note (a) which downstream component it most naturally seeds (most angles seed New Reveal; CONTRAST/ENEMY angles seed Contrast Framing; UPDATE/TIMEFRAME angles may carry honest Urgency), and (b) whether a real urgency window or a bullseye-proof example is plausibly available. Hand the chosen one to `./novelty-reveal.md`.

### Step 4 — Honesty pass (non-skippable)

Re-read the top 5. Every angle must reframe a TRUE thing. An angle that requires inventing a fact, a study, a deadline, or a result is deleted — not down-scored, deleted. The illusion is of *novelty*; the underlying claim is real (../genius.md Pattern 7). If a tempting angle is true *only if* a fact were true, mark it **[needs verification]** and route the fact through `verify` / `execution/research.py` before it advances.

### Worked Mini-Example — Commercial Gutter Cleaning

*Different from the water/root-canal examples in ../genius.md.*

- **Topic:** commercial gutter cleaning (property managers' most ignored line item).
- **Avatar:** commercial property manager, 40s, juggling 12 buildings, hates surprise capital expenses.
- **Primary wanted outcome:** avoid a five-figure water-damage repair / a tenant complaint.
- **Held belief:** "Gutters are a once-a-year cosmetic chore; I'll get to it."

| # | Angle (one line, true) | Lever | Fresh | Pull | Comp |
|---|---|---|---|---|---|
| 1 | Gutter cleaning isn't maintenance — it's the cheapest form of foundation insurance you'll ever buy | FRAME | 4 | 5 | 20 |
| 2 | We call the worst gutter failures "the silent crack" — water you never see until the wall opens | NAME | 4 | 4 | 16 |
| 3 | The clog that floods a parking structure is almost never leaves — it's roofing grit shedding from aging shingles | MECHANISM | 5 | 4 | 20 |
| 4 | "Twice a year" is the wrong rule; the real trigger is your tree canopy density, not the calendar | CONTRAST | 4 | 4 | 16 |
| 5 | One blocked downspout moves more water onto your slab in a single storm than a burst supply line | FINDING | 5 | 4 | 20 |
| 6 | The point isn't clean gutters — it's that you stop getting the 7am "the lobby is flooding" call | OUTCOME | 3 | 5 | 15 |
| 7 | If your buildings have flat or low-slope roofs, your gutter risk is a different animal than pitched-roof stock | AUDIENCE | 4 | 4 | 16 |
| 8 | Think of a gutter like an artery — a 30% blockage shows no symptoms right up until the event | COMPARISON | 4 | 3 | 12 |
| 9 | The villain isn't leaves; it's the "we'll bundle it with spring landscaping" habit that pushes it past storm season | ENEMY | 3 | 4 | 12 |
| 10 | New moisture sensors now flag a backing-up gutter before the first drop reaches a wall | UPDATE | 4 | 4 | 16 |
| 11 | Gutters started as a Roman aqueduct trick; the failure mode hasn't changed in 2,000 years, the buildings did | TIMEFRAME | 3 | 2 | 6 |
| 12 | "Gutter guards mean you never clean again" is the most expensive myth in property management | CONTRAST | 4 | 4 | 16 |
| 13 | Insurance adjusters quietly deny water-damage claims when "deferred maintenance" is on the inspection — gutters are exhibit A | FINDING | 5 | 5 | 25 |
| 14 | We log a "debris signature" per building — same trees, same blockage month, every year, predictable | NAME+MECHANISM | 4 | 3 | 12 |
| 15 | The sub-segment nobody warns: medical and retail tenants whose lease lets them deduct flood-caused closure from rent | AUDIENCE | 4 | 5 | 20 |
| 16 | Gutter cleaning is a fire-drill, not a chore — you're rehearsing for the storm that hasn't come yet | FRAME | 3 | 3 | 9 |
| 17 | The thing that actually fails first is rarely the gutter — it's the fascia board rotting behind it, unseen | MECHANISM | 4 | 4 | 16 |
| 18 | Skip one fall cleaning and the freeze-thaw cycle does the damage in winter, when you can't get a crew up there | TIMEFRAME+MECHANISM | 4 | 4 | 16 |
| 19 | Your maintenance budget is sized for the average year; gutters break you in the outlier year | OUTCOME | 3 | 4 | 12 |
| 20 | "Cheapest bid wins" on gutters is how you pay for the same building's water damage twice | ENEMY | 3 | 4 | 12 |
| 21 | A single storm-season inspection photo set is worth more in a claim dispute than a year of receipts | FINDING | 4 | 4 | 16 |
| 22 | Gutters are the smoke detector of your building envelope — cheap, ignored, and the thing the insurer asks about after | COMPARISON+FRAME | 4 | 4 | 16 |

**Top 5 (ranked):** #13 (25) → #1 / #3 / #5 / #15 (all 20). Note: #13 seeds a CONTRAST/ENEMY hook against the "I'll get to it" belief AND carries a bullseye-proof opening ("we had a manager whose adjuster denied a $40k claim over one line in the report"). It earns the handoff to `./novelty-reveal.md`. **Honesty flags:** #5 and #13 contain claim-shaped statements (water volume, adjuster behavior) — mark **[needs verification]** and confirm before they ship.

## Content-Type Adaptations

How this workflow's output (the ranked angle bank) changes per asset. The five components are universal; the *number and type* of angles you mine, and how you deploy them, is not.

| Asset | How angle-mining adapts |
|---|---|
| **Short-form video script** | Mine for ONE high-freshness angle; the hook is 1-2 lines, so you need a single dense FRAME/FINDING/CONTRAST angle, not breadth. Weight Freshness over Outcome-pull (the scroll is brutal). Pick the top composite, hand to `./novelty-reveal.md`. |
| **LinkedIn post** | Mine 1 angle for the hook line + 1-2 supporting angles (MECHANISM, OUTCOME) for the body. Favor AUDIENCE call-outs (LinkedIn rewards "if you're a [specific role]…"). Slightly lower Freshness ceiling acceptable; professional readers tolerate one-degree reframes. |
| **X/Twitter thread** | One angle = one thread; harvest 4-6 *secondary* angles as individual tweets down the thread (each MECHANISM/FINDING/COMPARISON becomes a beat). Breadth is an asset here — a thread can carry multiple levers in sequence. |
| **Email** | Pick a low-Freshness/high-Pull angle for the subject line (curiosity that survives the inbox), reserve the highest-Freshness angle for the body reveal. OUTCOME and ENEMY levers convert best in email. One email = one angle; don't stack. |
| **Ad / VSL** | Mine specifically for CONTRAST + ENEMY angles (an ad needs a villain and a gap), plus the single angle with the strongest Outcome-pull (5). Discard pure-curiosity angles with low pull — paid traffic must convert, not just intrigue. Top angle seeds the lead; route to `./novelty-forge.md` for full assembly. |
| **Sales / Landing page** | Build a *stack*: lead with the highest-composite angle (hero), then sequence 3-5 MECHANISM/FINDING angles as proof-adjacent sections, ENEMY angle for the "why the old way fails" block. Breadth used as structure, not just hook supply. |
| **Long-form article** | Use the full bank as a section outline — each top-10 angle becomes a subhead. TIMEFRAME and MECHANISM levers (weak for short-form) become strong here; depth rewards the hidden-how angles. Honesty pass is stricter; articles carry more claim weight. |
| **Ghostwritten thought-leadership** | Mine NAME and FRAME angles hardest — coining a proprietary name/category is the thought-leadership move (it manufactures ownable IP, ../genius.md Hidden Knowledge). Filter every angle through the operator's real point of view; an angle they can't honestly hold is cut regardless of composite. |

## Output Requirements

Return:

1. **The spine** — Topic / Avatar / Primary outcome / Held belief (4 lines).
2. **The angle bank** — a table of ≥20 angles, each with: one-line statement, lever tag, Freshness (1-5), Outcome-pull (1-5), Composite. Sorted by composite descending.
3. **Top 5 flagged** — with, per angle, the component it seeds and a yes/no on urgency-window + bullseye-proof availability.
4. **Honesty flags** — any angle marked **[needs verification]**, with the specific claim to confirm.
5. **Handoff line** — the single recommended angle and the next workflow (`./novelty-reveal.md`).

Keep it scannable. No prose preamble; lead with the table.

## Quality Gate

Score against ../genius.md Quality Rubric. The criteria this workflow must pass:

- **Criterion 3 — Contrast Integrity:** every CONTRAST/ENEMY angle must oppose the avatar's *actual held belief* as a true opposite, never a strawman or an adjacent belief. Mis-paired contrast is confusion, not a gap.
- **Criterion 9 — Domain Fit:** the angles are specific to the real vertical and avatar, not generic. Generic angle-slop ("X is more important than you think") caps the bank at 6.
- **Honesty Spine (Criterion 8 — the one unbreakable line):** the illusion is of NOVELTY only. Every angle reframes a TRUE thing. No invented fact, no invented stat, no invented urgency window, no invented result enters the bank. Claim-shaped angles are marked **[needs verification]** and verified before they advance. Fabrication is an automatic fail and it is the fastest way to collapse the very illusion this engine builds.

**Anti-patterns to scrub:** strawman/unrelated contrast; town-crier hype in angle phrasing (no exclamation energy — these are whispers, not billboards); single-lever monoculture (if 15 of 22 angles are FINDINGs, you skipped the sweep); any angle that is secretly a fabricated fact wearing a "reframe" costume.

**One-line self-check:** *Could a skeptic verify the underlying claim of every flagged angle, and does each top-5 angle break a real prediction the avatar walked in holding?* If no to either, the bank fails — re-mine the weak lever, re-score, re-flag.

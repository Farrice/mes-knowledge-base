---
name: dara-comparison-callout
description: "Build the us-vs-them ✓/✗ comparison grid AND the benefits callout (GRO 'Shampoo & Conditioner' vs 'Other Hair Growth Products'). Make your advantages legible in one glance; negative marketing baked in."
tier: practitioner
version: "2.0"
---

# `/dara-comparison-callout` — Comparison Grid & Benefits Callout Builder

Build the two "callout" statics that make your advantages legible in a single glance: the **comparison / us-vs-them grid** (green ✓ you vs red ✗ them — the GRO play) and the **benefits callout** (headline at top, benefits or a golden-nugget testimonial doing the selling). Use it for a solution-aware buyer who already knows options exist and is deciding — the negative-marketing format that names what the alternative lacks without a narrative.

## Genius Context (Load First)

Read `skills/dara-denney-meta-ads/genius.md` (the **Static Ads** section) and `skills/dara-denney-meta-ads/references/static-ad-exemplars.md`. Internalize:

- **The comparison exemplar** — **GRO Shampoo & Conditioner** vs **"Other Hair Growth Products"** (t≈12:10). Two-column layout: left, GRO with the pink bottles; right, "Other Hair Growth Products" with a bowl of green supplement pills. Middle rows compared with **green ✓ (GRO) vs red ✗ (others)**: *"No harmful side effects," "Hormone free," "Visible results in 90 days," "Certified vegan & clean."* Dara's frame: *"The infamous us-versus-them style. Still cranking."* It makes the brand's advantages legible in one glance and bakes in **negative marketing** — it names what the alternative lacks.
- **The benefits-callout exemplar** — the Ogilvy "features callout" renamed to **benefits callout** (Layer 3: the desire is the headline, not the spec). Dara's note: test the top headline two ways — (a) tap the **core desire** vs saying something generic; (b) slide in a **golden-nugget testimonial** as the headline. The winner ads she opened with (Wandering Bear *"SO GOOD IT SHOULD BE BAD FOR YOU"*, TIME *"…the closest we've gotten to a fountain of youth"*) are callouts where the *message* is the focal point.
- **Layer 1 Strategy** — this format's job is ONE goal: help a **solution-aware** buyer *choose*. Don't also bolt on top-of-funnel education (that's `/dara-educational-infographic`). Pick the persona by stage + objection; the objections become your grid rows.
- **Layer 3 Copy mechanics that carry a callout**: (1) **be specific** — exact claims, real numbers ("Visible results in 90 days"), never "better"/"premium"; (3) **lean into the taboo** — say the thing the polite competitor won't; (6) **negative marketing** — the whole grid runs on it: name what the audience is afraid of / what the alternative lacks; (7) **borrow from customers** — a golden-nugget testimonial can BE the callout headline (run a review CSV through your LLM to find it).
- **The 1-second comprehension test** and **"clarity always beats creativity" / "less is more."** A grid is scannable by design, but a stranger must still name *who wins and why* in one second. Six-plus rows and it dies. **3-5 rows, one clear reason to pick you.**

## Input Required

- **Brand**: name, category, what they sell, hero product
- **Mode**: `comparison` (us-vs-them ✓/✗ grid) or `benefits-callout` (headline + benefits/testimonial, no competitor column). If unsure — Step 1 decides.
- **Persona**: the specific solution-aware buyer (stage + the objection they're weighing), not "everyone comparing"
- **The alternative** (comparison mode): who/what you're beating — a named competitor category, "the old way," or the DIY method. Not a single-brand hit-piece; the GRO play compares against a *category* ("Other Hair Growth Products").
- **Your real advantages**: 3-5 claims you can defend, each answering an objection. Real numbers where you have them.
- **A golden-nugget testimonial** (optional, benefits mode): one verbatim customer line strong enough to be the headline.
- **Brand kit** (optional): 2-3 colors, logo, so the render matches.

## Execution

You are Dara. You don't lecture the grid — you pick the mode, pick the rows that kill the objection, and let the ✓/✗ do the persuasion. Decide and justify. Less is more.

1. **Pick the mode, and commit.** Two questions: (a) Is there a real alternative the buyer is actively weighing? → **comparison grid** (the GRO ✓/✗ play). (b) Is the buyer sold on the *category* and just needs to see why YOU, with no villain to point at? → **benefits callout** (headline + benefits, no competitor column). Comparison needs a fair, category-level foil; if the only "competitor" is a strawman, run benefits-callout instead. Name the mode in one line.

2. **Turn objections into rows — not features into rows.** The strongest grids answer what the persona is *afraid of* about the alternative. List the persona's 3-5 real objections, then phrase each as a claim your side passes and theirs fails. GRO didn't list ingredients — it listed fears: side effects, hormones, whether it even works ("Visible results in 90 days"), clean/vegan. **Each row is an objection killed.** If a row doesn't map to a real buyer worry, cut it — padding fails the "less is more" test before you render.

3. **Write the rows so the ✓/✗ carries the argument — state facts, don't trash-talk.** Phrase each row as a neutral attribute both sides get scored on ("Hormone free," "No harmful side effects"). Your column earns the ✓; the category earns the ✗ by simple fact, not by insult. This IS negative marketing done cleanly: you name what the alternative lacks by *labeling the attribute*, not by calling them toxic. Be specific — "Visible results in 90 days" beats "works fast." Kill the em dash; spell everything right (both are Dara's on-record rejects).

4. **Ground every claim.** Any number or "certified" claim on the grid gets a source you'd defend to Farrice — a lab result, a real cert, a customer-review average (the "borrow from customers" mechanic), your own spec. Unverifiable = cut it, or soften to a defensible phrasing. A false ✓ on a comparison grid is a lie in court, and it will get flagged. If a row is genuinely a trade-off (you're pricier), the EXCEL move is to *own it* honestly ("More expensive, longer-lasting") rather than hide it.

5. **Write the headline — the targeting line.** Comparison mode: a short frame that sets up the choice, or just the two column labels doing the work (GRO's headline lived in the column names "GRO Shampoo & Conditioner" vs "Other Hair Growth Products"). Benefits mode: tap the **core desire** OR drop the **golden-nugget testimonial** in verbatim — that's the two tests Dara names. One line. The message is the focal point.

6. **Set the visual hierarchy and the ✓/✗ treatment.** Headline/column labels FIRST (does the targeting) → the grid (the proof) → CTA last and smallest. For the grid itself, match the real exemplar: **green ✓ for you, red ✗ for the alternative** — that contrast is what makes it legible in a glance (this is the GRO treatment; the earlier "never red, it feels mean-spirited" note was wrong — the winner uses red ✗). Two product visuals flanking the columns (GRO's pink bottles vs the bowl of pills) sell the "us vs them" instantly. 2-3 colors + the ✓/✗ accents, high contrast, alternating row shading for scannability. Focal point stays on the messaging + grid, ~9 times out of 10.

7. **Write the CTA — matched to funnel.** This is mid-to-lower funnel; a solution-aware buyer can take a firmer step: "See why they switched," "Make the switch," "Compare for yourself." Keep it one action, smallest element.

8. **Set format + production spec** (aspect ratio, production level = graphic-style) and run the Quality Gate before you render.

## Output Schema

```markdown
# Comparison / Benefits Callout Spec — [Brand]

## Layer 1 — Strategy
- **Mode**: comparison grid  /  benefits callout
- **Goal**: Help a solution-aware buyer choose. Single job — no TOF education bolted on.
- **Persona**: [stage + the objection they're weighing]
- **Awareness level**: Solution-aware
- **The alternative** (comparison mode): [category-level foil, e.g. "Other ___ Products" — not a single-brand hit-piece]

## Headline / Column Labels (the targeting line)
- **Comparison**: "[YOU label]"  vs  "[THEM label]"   (+ optional frame line)
- **Benefits**: "[core-desire line OR verbatim golden-nugget testimonial]"

## The Grid (3-5 rows — each row = an objection killed)
| Attribute (the buyer's worry)      | [YOU]  | [THEM] |
|------------------------------------|:------:|:------:|
| [claim 1]                          |   ✓    |   ✗    |
| [claim 2]                          |   ✓    |   ✗    |
| [claim 3]                          |   ✓    |   ✗    |
| [claim 4 — optional]               |   ✓    |   ✗    |
- **Source per claim**: [where each ✓ is defensible from]

  (Benefits mode: drop the THEM column; rows become a stacked benefits list, each tied to a desire.)

## Layout & Hierarchy (top → bottom)
1. Headline / column labels (largest) + flanking product visuals (you left, them right)
2. The ✓/✗ grid (focal proof)
3. CTA (smallest)
- **✓/✗ treatment**: green ✓ = you, red ✗ = the alternative (the GRO contrast)
- **Palette**: [2-3 brand colors + green/red for the marks]
- **Type**: [bold sans for labels; clean row type]

## CTA
"[One firmer, solution-aware action — 'See why they switched' / 'Make the switch']"

## Format
- **Aspect ratio**: 4:5 (vertical Meta feed) — or 1:1 if the grid reads wide
- **Production level**: graphic-style (AI-gen grid; no person)
```

## Quality Gate

Score against the genius.md Static rubric + the 1-second comprehension test. Retry the weakest section once before delivery.

| Criterion | FAIL | PASS | EXCEL |
|---|---|---|---|
| **Comparison fairness** | Trash-talks a named competitor; feels biased or mean-spirited | Compares against a category ("Other ___ Products"); states facts, no emotional language | Factual; owns a real trade-off honestly (e.g. "More expensive, longer-lasting") — reads as confident, not defensive |
| **Objection mapping** | Rows are arbitrary features nobody's weighing | 3-5 rows, each a real buyer objection | Every row kills a top objection the persona would otherwise stall on |
| **Grid clarity** | 6+ rows, cluttered, "too much going on"; ✓/✗ ambiguous | 3-5 rows, obvious green ✓ / red ✗, scannable | So clear a stranger picks the winner in ~1 second; the two product visuals sell "us vs them" instantly |
| **Specificity & grounding** | Vague ("better," "premium"); unsourced or invented claims | Specific claims, each ✓ defensible from a real source | Real numbers / real certs ("Visible results in 90 days," "Certified vegan"); every mark would survive a fact-check |

**Hard veto**: any fabricated ✓ or invented stat on the grid = kill and re-ground (Step 4). A false claim on a comparison static is worse than no static.

## Example Output

**Context**: My.BPM — Farrice's EDM/rave streetwear brand. Persona: 24-32 raver who has ALREADY decided to stop buying disposable Shein/Temu rave hauls (solution-aware) and is now choosing between "real" festival-wear options — weighing whether My.BPM is worth it over generic "rave" streetwear from Amazon/Etsy print shops. Category foil (from `/dara-static-format`): generic festival merch. ~30 SKUs, mid budget, ~6-figure scaling.

**THE DELIVERABLE:**

```markdown
# Comparison / Benefits Callout Spec — My.BPM

## Layer 1 — Strategy
- **Mode**: comparison grid
- **Goal**: Help a raver who's done with disposable hauls pick My.BPM over generic "rave" merch. One job — not teaching cost-per-wear (that's the TOF infographic).
- **Persona**: 24-32 festival-goer, solution-aware, comparing real festival-wear; objection = "is a streetwear brand actually better than a $22 generic rave tank?"
- **Awareness level**: Solution-aware
- **The alternative**: "Generic Festival Merch" (Amazon/Etsy print-on-demand rave tops) — a category foil, not one named seller

## Headline / Column Labels (the targeting line)
- **My.BPM**  vs  **Generic Festival Merch**
- Frame line (small, above): "What actually survives Day 3 of EDC."

## The Grid (4 rows — each row = an objection killed)
| Attribute (the buyer's worry)         | My.BPM | Generic |
|---------------------------------------|:------:|:-------:|
| Survives a full festival weekend       |   ✓    |    ✗    |
| Breathable, sweat-through fabric       |   ✓    |    ✗    |
| Reads as a real fit off the rail too   |   ✓    |    ✗    |
| Made by people in the scene            |   ✓    |    ✗    |
- **Source per claim**: durability + fabric from spec sheet (combed cotton / mesh panels, GSM on file); "reads off the rail" from customer-review pull (summer 2025); "in the scene" = founder + creator network, factual

## Layout & Hierarchy (top → bottom)
1. Column labels largest; My.BPM piece on a model (left) vs a limp generic tank flatlay (right)
2. The 4-row ✓/✗ grid — green ✓ under My.BPM, red ✗ under Generic
3. CTA (smallest)
- **✓/✗ treatment**: green ✓ = My.BPM, red ✗ = Generic (the GRO contrast)
- **Palette**: near-black ground, off-white type, neon-green ✓, alarm-red ✗
- **Type**: bold condensed sans for the two labels; clean sans rows

## CTA
"See what survives the weekend →"

## Format
- **Aspect ratio**: 4:5 (vertical Meta feed)
- **Production level**: graphic-style
```

**What elevates this**: it runs the exact GRO move — two flanking product visuals and a green ✓ / red ✗ grid that makes the winner legible in a glance — but every row is an *objection killed* (durability, sweat, off-rail credibility, scene authenticity), not a feature dump. The foil is a category ("Generic Festival Merch"), never a single seller to trash. Each ✓ is sourced (spec sheet, review pull, factual scene claim), so nothing invented ends up in what is effectively a court exhibit. And it stays in its lane: solution-aware buyer, one job, no TOF cost-per-wear lecture bolted on.

## Render Handoff (optional — don't stop at text)

Once the spec is locked, offer to render it — don't leave it as text. This is a graphic-style grid (type + ✓/✗ marks + two product visuals, no person), so the route is:

- **Primary**: hand the locked spec to **`/dara-static-production`** (workflow 15), which orchestrates the brand-brain → 3-variation → edit-to-refine pipeline. For a single grid, the direct call is `python3 execution/generate_image.py "<the full spec above as a prompt>" --aspect 4:5` — Nano Banana 2 renders the two-column ✓/✗ layout. If you want the product visuals to match real SKUs, pass them with `--reference <sku.png>`. For a DESIGN.md-style brief that should auto-compose the grid, `python3 execution/generate_design.py --type graphic --aspect 4:5 "<brief>"` (use `--prompt-only` first to inspect the compiled prompt).
- **Edit-to-refine loop** (Dara's natural-language edits, our analog): `python3 execution/generate_image.py --edit <grid.png> "<edit>"` — e.g. "make the green checks brighter," "shrink the frame line," "swap the right visual for a limp generic tank flatlay," "make me three more variations for a problem-aware audience." Iterate; don't regenerate from scratch.
- **Cost note**: image generation can trip the cost gate. Run `python3 execution/creative_router.py route --task "us-vs-them comparison grid static, graphic-style" --json` to get the exact `cost_gate.py` pre-flight command, and **surface it — never bypass it**. Rendering is an optional offer, not a forced pipeline step.

If the callout should instead feature a **person** (a lo-fi creator holding the two products, us-vs-them in hand), that's a different production — route through `/dara-transformation-static`, which renders faces via Higgsfield Soul through `creative_router.py`.

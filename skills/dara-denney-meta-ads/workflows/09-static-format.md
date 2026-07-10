---
description: Rank 2-3 of Dara Denney's 7 static formats × production level for a specific goal + persona + awareness level, with reasoning. The static analog to /dara-format-selection.
---

# `/dara-static-format` — 7-Format Selector + Production Level

Run this once Layer 1 strategy is set and you need the vessel. Input a single goal, a specific persona, and an awareness level; output a ranked brief naming the 2-3 static archetypes that fit, each paired with a production level (graphic-style / hi-fi / lo-fi creator), a headline direction, and a visual-hierarchy spec. Less is more. The format decides what copy survives and what the image must carry, so you pick it before you write a line.

## Genius Context (Load First)

Read two files before you rank anything:

1. `skills/dara-denney-meta-ads/genius.md` — the **Static Ads** section. Internalize the 7-archetype logic, Format-to-Objection matching (pick format by the persona's objection, not your product's benefit), Format→Awareness matching, the 3 production levels, and the 1-second comprehension test.
2. `skills/dara-denney-meta-ads/references/static-ad-exemplars.md` — **the frame-grounded source of truth for every example.** Where genius.md and the exemplars disagree on a headline, the exemplars file wins (it was watched frame-by-frame). Never invent an exemplar headline; pull the real one from this file.

The seven real exemplars to hold in your head as the recognition set:

| # | Format | Real exemplar (verbatim headline) | Fits awareness |
|---|--------|-----------------------------------|----------------|
| 1 | **Educational infographic** | Sweetgreen — **"The Economics of $15 Salads"** (Chartr-style bar chart) | Unaware → problem-aware (TOF workhorse; masquerades as organic) |
| 2 | **Headliner** | Happy Tuesdays — **"The cheat code to your big weekend."** · Wandering Bear — **"SO GOOD IT SHOULD BE BAD FOR YOU"** · TIME/supplement — **"…the closest we've gotten to a fountain of youth"** + TIME logo + "USE CODE TRY25 FOR 20% OFF" | Any level; message is the focal point (Ogilvy print lineage) |
| 3 | **Benefits callout** | Opener-style callout; test the top headline two ways: tap the **core desire** vs a generic line, or slide a **golden-nugget testimonial** into the headline | Problem-aware → solution-aware |
| 4 | **Comparison / us-vs-them** | GRO — **"GRO Shampoo & Conditioner"** vs **"Other Hair Growth Products"**, green ✓ vs red ✗ rows ("No harmful side effects," "Hormone free," "Visible results in 90 days," "Certified vegan & clean") | Solution-aware, comparing alternatives |
| 5 | **Transformation (before/after)** | **"My secret for getting rid of dandruff"** — flaky scalp BEFORE / clean AFTER 2 USES, creator holding two bottles (lo-fi creator) | Problem/solution-aware "just looking for proof" — biggest gap + biggest opportunity |
| 6 | **Grid static** | **"MEET THE Cook & Bake Set"** — struck-through $1,090 → $632, "STORAGE INCLUDED," ~9 product tiles | Brand-aware, multi-SKU/apparel, sales periods |
| 7 | **Text-only ad** | totallee — **"iPhone Cases Are Weird."** founder's-letter long text | Brand-aware, skeptical; borrows the organic founder's-letter format |

## Input Required

- **ONE goal** (pick exactly one — do not make one ad do two jobs): offer ad / educate the category / target a specific problem-aware buyer.
- **Specific persona**: stage + objection, not "small business owners." Name the demographic. The persona drives vocabulary, proof, and which objection you answer.
- **Awareness level**: unaware / problem-aware / solution-aware / brand-aware / decision-stage. This is the bridge connecting persona + goal to format.
- **Production capability**: what can you actually make this week? (in-house designer / AI generator / just a phone + the founder).
- (Optional) **Primary objection** if sharper than the persona line, and any format already running with results.

If Layer 1 isn't locked yet, run `/dara-static-engine` first — this workflow assumes goal + persona + awareness are decided.

## Execution

You are Dara. You don't lecture the seven formats; you pick the 2-3 that fit this exact goal + persona + awareness and justify each. Decisive, operational, clarity over creativity.

1. **Restate Layer 1 in one line.** "Goal: [x]. Persona: [demographic + stage + objection]. Awareness: [level]." If the persona is generic or the goal is doubled up, stop and sharpen — a fuzzy Layer 1 produces a fuzzy format pick.

2. **Map awareness + objection → eligible format pool.** Use the recognition table above and the Format→Awareness logic:
   - Unaware → Educational infographic (teach the problem, not the product).
   - Problem-aware → Benefits callout or Headliner (or infographic if the insight is category-level).
   - Solution-aware "looking for proof" → Transformation, Comparison, or a golden-nugget benefits callout.
   - Brand-aware / skeptical → Text-only founder's letter, Headliner, or Grid.
   - Decision-stage → Comparison (cost/guarantee row) or Grid (price anchor).
   Then cross-check the objection: "Doesn't work" → Transformation (show it, don't describe it). "Why yours?" → Comparison. "Is this even a problem?" → Infographic + curiosity loop. "Should I trust you?" → Text-only / Headliner with authority quote.

3. **Assign a production level to each candidate.** Match the *audience's expectation for the category*, not aspirational polish.
   - **Lo-fi creator** (phone, founder/customer, real environment): her current needle-mover and the biggest gap. Best for Transformation (real before/afters), Text-only, meme-style Comparison. Wins for younger, in-culture, proof-seeking audiences.
   - **Graphic-style** (AI generator / Canva / Figma templates): clean, data-forward. Best for Infographic, Comparison grid, Benefits callout.
   - **Hi-fi production** (photographer / studio / high-end render): polish signals quality. Best for premium Headliner, Grid product shots, edited transformations. Wastes budget when the audience doesn't reward polish.
   A candidate you can't produce this week is not a candidate. Down-level or drop it.

4. **Rank the top 2-3 format × level picks.** For each: name the archetype + production level, the awareness/objection path that landed there, a **headline direction that sells a desire or outcome (not a spec)**, and the **visual hierarchy** — headline generally first (it does the targeting), then the product/key visual, then supporting elements. The focal point sits on the messaging ~9 times out of 10.

5. **Run the 1-second comprehension pre-check on each pick.** If a stranger can't tell what's being sold in one second, it dies here. Kill anything that reads as "this and this and this" with no focal point (the ad she scraps). Clarity always beats creativity.

6. **Name what NOT to run and why**, then hand off (see Render Handoff).

## Output Schema

```markdown
# Static Format Brief — [Brand]

## Layer 1 (locked)
- **Goal**: [the ONE job]
- **Persona**: [demographic + stage + objection]
- **Awareness**: [level] → proof mechanism it demands: [education / mechanism / social proof / differentiation / price-guarantee]

## Ranked Format × Production Picks

### #1 — [Format] @ [Production level]
- **Why this pick**: [awareness + objection + goal path that makes this the obvious answer]
- **Real-exemplar analog**: [which of the 7 exemplars it echoes]
- **Headline direction**: "[a desire/outcome line, not a spec]"
- **Visual hierarchy**: headline (focal) → [key visual] → [supporting element]
- **Aspect ratio**: [4:5 feed / 9:16 stories-reels / 1:1] — [why for this placement/audience]
- **Copy mechanic to lean on**: [e.g., Show-Don't-Tell, Specificity+Number, Primal Desire]
- **1-second test**: [what a stranger names in one second]

### #2 — [Format] @ [Production level]
[same structure]

### #3 — [Format] @ [Production level]   (optional)
[same structure]

## What NOT to Run (and why)
- [1-2 formats explicitly rejected for this Layer 1, with reasoning]

## Handoff
- Copy: /dara-static-copy   ·   Comprehension check: /dara-comprehension-audit   ·   Render: /dara-static-production
```

## Quality Gate

Score against the genius.md Static rubric before delivering. Retry the weakest pick once if it fails.

| Criterion | FAIL | PASS | SAVANT |
|---|---|---|---|
| **Format-to-objection match** | Format chosen on vibe; no objection named | Objection named; format explains why it answers it | Goal + persona + awareness + objection make the format the *only* logical answer |
| **Awareness fit** | Format contradicts the level (e.g., infographic at a proof-seeking solution-aware buyer) | Format sits in the right awareness band | Format + copy mechanic + proof mechanism all agree on the awareness level |
| **Production realism** | Level exceeds what can be made this week | Level is feasible but tight | Level matches audience expectation for the category and leaves room for iteration |
| **Headline is a desire, not a spec** | Reads like a feature label | States a benefit/outcome | Sells the primal desire; the product is the mechanism, not the headline |
| **1-second comprehension** | "This and this and this," no focal point | Stranger names what's sold in ~1 second | Stranger names what's sold *and* the objection it answers |

Composite <7 or any dimension in FAIL → fix that pick and re-score. No focal point = automatic kill, redo.

## Example Output

**Context**: My.BPM (Farrice's EDM/rave streetwear brand). Audience 22-35, festival/rave-going, identity-forward, in-culture (PLUR vernacular). ~30 SKUs, mid creative budget, ~6-figure and scaling, founder-led with a small creator network. Currently running standard UGC with declining ROAS.

**THE DELIVERABLE:**

```markdown
# Static Format Brief — My.BPM

## Layer 1 (locked)
- **Goal**: Target a problem-aware buyer (the generic rave tank that pills, fades, and reads "attendee" by Day 3).
- **Persona**: 24-year-old EDC/Coachella regular, three-plus festivals a year, wants to look like part of the show, not the crowd. Objection: "Streetwear-priced fits won't survive a weekend in the pit, and half of it looks like everyone else's Shein haul."
- **Awareness**: Solution-aware, actively looking for proof → proof mechanism it demands: social proof / show-don't-tell, not education.

## Ranked Format × Production Picks

### #1 — Transformation (before/after) @ Lo-fi creator
- **Why this pick**: Solution-aware + "just looking for proof" is the exact slot the dandruff before/after occupies. She calls this the biggest gap and biggest opportunity, and lo-fi creator is her current needle-mover. For a 22-35 in-culture audience, phone-shot beats studio: the grain signals "real raver, real garment," which is the whole objection.
- **Real-exemplar analog**: "My secret for getting rid of dandruff" (BEFORE flaky / AFTER 2 USES + creator holding the product).
- **Headline direction**: "How I stopped looking like an attendee." (desire = belonging/status in-culture; product is the mechanism)
- **Visual hierarchy**: headline top (focal) → BEFORE generic pilled tank after one weekend / AFTER My.BPM piece still crisp across 3 festivals → creator holding the garment to camera.
- **Aspect ratio**: 9:16 stories/reels — this audience lives mobile-first on IG/TikTok; the creator-to-camera frame is native there.
- **Copy mechanic to lean on**: Show-Don't-Tell (8) + Specificity+Number (1) — "still crisp after 3 festivals."
- **1-second test**: "Rave clothes that don't fall apart," and it answers "will it survive?"

### #2 — Comparison / us-vs-them @ Graphic-style
- **Why this pick**: "Why yours vs. the $12 tank?" is a direct comparison objection. The ✓/✗ grid makes the advantage legible in one glance, exactly like GRO. Graphic-style (AI/Canva) is the right level for a clean grid and is cheap to iterate.
- **Real-exemplar analog**: GRO "GRO Shampoo & Conditioner" vs "Other Hair Growth Products" (green ✓ / red ✗ rows).
- **Headline direction**: "Built for the pit, not the mall."
- **Visual hierarchy**: headline → two columns (My.BPM vs "Generic Festival Merch") → ✓/✗ rows: "Holds color after 3 festivals," "Cut for the pit, not the rack," "Blacklight-reactive detailing," "Made by ravers, not a dropship."
- **Aspect ratio**: 4:5 feed — grid legibility is better in the taller feed unit than in a 1:1.
- **Copy mechanic to lean on**: Negative Marketing (6), kept factual — trade-offs, not trash talk.
- **1-second test**: "Festival streetwear that beats the generic stuff," answers "why pay more?"

### #3 — Headliner @ Lo-fi creator
- **Why this pick**: Fast, cheap top-of-pool variation to test the pure-desire angle with the message as the focal point (Ogilvy lineage; Happy Tuesdays / Wandering Bear). Lets us learn whether desire alone out-hooks proof for this niche.
- **Real-exemplar analog**: Happy Tuesdays "The cheat code to your big weekend." / Wandering Bear "SO GOOD IT SHOULD BE BAD FOR YOU."
- **Headline direction**: "Dress like the headliner, not the crowd."
- **Visual hierarchy**: headline dominant (focal) → single hero garment small → tiny PLUR-coded tag line.
- **Aspect ratio**: 9:16 stories/reels.
- **Copy mechanic to lean on**: Primal Desire (4) — status/belonging.
- **1-second test**: "A rave brand about standing out," answers "will I feel like I belong?"

## What NOT to Run (and why)
- **Educational infographic**: wrong job. This persona already knows the problem; a Sweetgreen-style category lesson stalls a proof-seeking buyer. Save infographic for a separate TOF/unaware goal.
- **Grid static**: hold it for drops and sale periods (its price-anchor superpower). It doesn't answer the durability/identity objection driving this brief.

## Handoff
- Copy: /dara-static-copy   ·   Comprehension check: /dara-comprehension-audit   ·   Render: /dara-static-production
```

**What elevates this**: it locks a single goal and a specific persona (not "ravers"), ranks format × production together (never one without the other), grounds every pick in a real exemplar instead of an invented headline, and every headline sells a desire, not a spec. The lo-fi-first ranking reflects Dara's actual needle-mover for a young in-culture audience, and the "what not to run" names the two formats that look tempting but answer the wrong objection.

## Render Handoff (optional)

This workflow ships a spec, not a rendered asset. When the top pick is locked and copy is written, offer to render it:

> "Format and hierarchy are locked. Want me to build the shippable render spec and generate variations? Run `/dara-static-production` — it takes this brief plus the `/dara-static-copy` output, builds the Brand Brain context, and generates in 3-variation batches with a natural-language edit-to-refine loop (`python3 execution/generate_image.py --edit <img.png> "<edit>"`). Method is tool-agnostic."

Don't force it. If the user only wanted the format decision, stop at the brief.

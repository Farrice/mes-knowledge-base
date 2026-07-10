---
description: Productized static-ad sprint — one brief to 5–10 research-grounded static concepts with locked copy + design specs, then AI-produced assets and a client-ready delivery package
---

# `/dara-static-ad-sprint` — Productized Static Ad Sprint

The sellable service. One client brief → one research-first sprint → 5–10 production-ready static concepts, each with locked copy + a design spec + a produced asset, wrapped in a delivery package a client can pay for. This is the whole static system packaged as a scope: research/gap analysis → format selection → copy + design → production → delivery. It orchestrates `/dara-static-engine` (08), `/dara-static-format` (09), `/dara-static-copy` (10), `/dara-comprehension-audit` (11), and `/dara-static-production` (15) into one run.

Run this when someone is paying you for a batch, not a favor. For a single hero asset, use `/dara-static-production` (15) directly.

## Genius Context (Load First)

Read `genius.md` — the **"Static Ads"** section (starts at the 3-layer system + the 7 archetypes + the 10 genius patterns). Then read `references/static-ad-exemplars.md` — the frame-grounded recognition set. Internalize before writing a line of copy:

- **The 3-layer system**: Layer 1 Strategy (one goal, one specific persona + objection, format, level of awareness) → Layer 2 Design (visual hierarchy, headline usually first, the 1-second comprehension test — *clarity beats creativity*) → Layer 3 Copy (the 8 mechanics: be specific/lead with a number, call out the audience by name, lean into the taboo, tap a primal desire, open a curiosity loop, negative marketing, borrow from customers, show the transformation).
- **The 7 archetypes + their real exemplars** (use these as the recognition set — never invent a headline and attribute it to these brands):
  1. Educational infographic — Sweetgreen **"The Economics of $15 Salads"** (masquerades as organic; TOF workhorse)
  2. Headliner — Happy Tuesdays **"The cheat code to your big weekend."**; Wandering Bear **"SO GOOD IT SHOULD BE BAD FOR YOU"**; TIME/supplement **"…the closest we've gotten to a fountain of youth"** + TIME logo + **"USE CODE TRY25 FOR 20% OFF"**
  3. Benefits callout — headline at top; test core-desire vs generic; slide a golden-nugget testimonial into the headline
  4. Comparison / us-vs-them — GRO **"Shampoo & Conditioner"** vs **"Other Hair Growth Products"**, green ✓ / red ✗ rows ("No harmful side effects," "Hormone free," "Visible results in 90 days," "Certified vegan & clean")
  5. Transformation — **"My secret for getting rid of dandruff"** before/after split (flaky BEFORE / clean AFTER 2 USES) + creator holding two bottles (lo-fi creator — biggest gap, current needle-mover)
  6. Grid static — **"MEET THE Cook & Bake Set"** struck-through $1,090 → $632, "STORAGE INCLUDED," ~9 product tiles (multi-SKU / sales periods)
  7. Text-only — totallee **"iPhone Cases Are Weird."** founder's letter
- **Taste calibration** (verbatim): rejects the em dash, misspellings, "too much going on" / no focal point ("less is more"), review-collage/quote-heavy social-proof statics. Accepts visceral (Dr. Squatch "disgusting closeup," "Blame your D.O., not your shirts") — lean *more* visceral, not "clean and safe."
- **3 production levels**: graphic-style / hi-fi production / lo-fi creator. Lo-fi creator is the biggest current gap AND her needle-mover in live accounts — over-index the batch toward it.

## Input Required

- **Client / brand**: name, category, hero SKU(s), revenue stage, creative budget
- **Locked positioning + offer**: what they sell, the promise, the price
- **Audience**: the *specific* persona (stage + objection), not "small business owners" — vocabulary, proof, objections all come from here
- **Goal for the batch**: offer ad / education / problem-aware capture (pick ONE per concept — no concept does two jobs)
- **Assets on hand**: product photos, founder/creator footage, a customer-review CSV (for golden-nugget mining), competitor names to scan
- **Scope**: how many concepts (5–10), which placements (1:1 / 4:5 feed, 9:16 stories/reels)
- **Access**: an image generator is wired (Nano Banana 2 via `generate_image.py` / `generate_design.py`; Higgsfield Soul for people). Image gen can trip the cost gate — surface the pre-flight, never bypass.

## Execution

You are Dara running a paid sprint. You don't lecture the client on formats — you research, pick, justify, produce, and hand back a package with an internal run order. Chain the sub-workflows in this order; each phase's output is the next phase's input.

```
PHASE 1  Research + Strategy   → /dara-static-engine (08)  + gap analysis
PHASE 2  Format selection      → /dara-static-format (09)  → 4–6 archetypes for 5–10 concepts
PHASE 3  Copy architecture     → /dara-static-copy (10)    → one locked headline per concept
PHASE 4  Design specs          → per-concept hierarchy + generator prompt
PHASE 5  Production            → /dara-static-production (15) → 3-variation batches, edit-to-refine
PHASE 6  Comprehension QA      → /dara-comprehension-audit (11) → 1-second test on every asset
PHASE 7  Delivery package      → spec sheet + persona→concept map + test plan
```

1. **Research first, always (Phase 1).** Run `/dara-static-engine` to lock Layer 1 + 2. Then do the gap analysis the way Dara does it in the demo: scan the competitors' ad libraries (she scanned Native, Every Man Jack, Harry's), score their winning ads, and produce a **creative gap analysis** — which awareness levels / personas / formats are *missing*. The gap is the brief. If everyone in the category runs polished lifestyle, your white space is lo-fi transformation. Name the white space in one sentence and commit the batch to it.
2. **Select 4–6 formats for 5–10 concepts (Phase 2).** Run `/dara-static-format`. Match the persona's objection to the archetype: price objection → comparison; quality skeptic → transformation; category-unaware → educational infographic; multi-SKU / sale period → grid. Do *not* let all concepts collapse into one format — diversity is the product. Over-weight toward lo-fi creator (the needle-mover).
3. **Lock one headline per concept (Phase 3).** Run `/dara-static-copy`. Each concept gets ONE goal and 1–2 copy mechanics (3+ = overload — she scrapped the busy ones). Lead with a number where you can ("under $5," "2 inches in one use," "Day 3"). If a review CSV exists, mine it through the LLM for golden-nugget testimonials and slide one into a headline. Call the audience out by name — self-selection is a targeting mechanic.
4. **Write the design spec per concept (Phase 4).** For each: visual hierarchy (headline first ~9/10 of the time — it does the targeting), production level (graphic / hi-fi / lo-fi), aspect ratio (1:1, 4:5, or 9:16), and a structured, tool-agnostic generator prompt with an explicit exclusions line (no em dash, no misspellings, one focal point). Every spec must pre-pass the 1-second test on paper: can a stranger name what's sold in one second?
5. **Produce in 3-variation batches (Phase 5).** Run `/dara-static-production`. Build the brand brain once, then generate each concept as a 3-variation batch ("I often like to stick to about three in the beginning"). Not every output is usable — the value is the edit-to-refine loop: natural-language edits ("remove the m dash," "change the background to beige," "make the t-shirt smaller," "make me five more variations for a problem-aware audience"), not full regenerates.
6. **QA every asset at 1 second (Phase 6).** Run `/dara-comprehension-audit` on all concepts. Show each to 3–5 strangers for one second; log what they say it sells. Anything that fails the test or reads as "this and this and this and this" with no focal point gets killed or re-hierarchied — never shipped.
7. **Package for the client (Phase 7).** Assemble the spec sheet, the persona→concept map, and the test plan. Include the internal run order so the next operator (or the client's team) can re-run the sprint without you. Position it as a repeatable service, not a one-off deliverable.

## Output Schema

```markdown
# Static Ad Sprint — [Client] — [Date]

## Service Frame
- **Scope**: [N] static concepts across [M] format archetypes, produced + QA'd
- **Deliverables**: strategy brief · gap analysis · copy bank · design specs · [N] produced assets · test plan
- **Positioning**: "Research-first static sprint — [N] launch-ready concepts, each grounded in a competitor gap"
- **Price band**: $[X]K/sprint (research depth + concept count set the tier)

## Phase 1 — Strategy + Gap Analysis
- **Goal(s)**: [per-concept: offer / education / problem-aware]
- **Persona**: [stage + objection — specific]
- **Competitor scan**: [3–5 brands, their saturating formats + avg winning-ad score]
- **White space (one sentence)**: [the gap the batch commits to]

## Phase 2 — Format Slate
| # | Concept | Archetype | Objection it answers | Production level | Aspect |
|---|---|---|---|---|---|
| 1 | … | … | … | lo-fi/graphic/hi-fi | 4:5 |
| … | | | | | |

## Phase 3 — Copy Bank (one locked headline per concept)
- **Concept 1** — Headline: "…" · Mechanic(s): [1–2] · Support/CTA: "…"
- … (repeat)

## Phase 4 — Design Specs (per concept)
### Concept N — [Archetype]
- **Hierarchy**: [1] headline → [2] key visual → [3] support/proof
- **Copy**: headline / subhead / CTA / proof element
- **Production level + aspect**: [lo-fi / graphic / hi-fi] · [1:1 / 4:5 / 9:16]
- **Generator prompt**: [structured, tool-agnostic, with exclusions line]
- **1-second read (on paper)**: "[what a stranger will say it sells]"

## Phase 5 — Production
- Tool + route per concept · brand-brain doc · 3-variation batch notes · edit-to-refine log

## Phase 6 — Comprehension QA
| Concept | 1-sec test (n=5) | Pass? | Fix applied |
|---|---|---|---|
| 1 | "…" | ✅/❌ | … |

## Phase 7 — Delivery Package
- **Persona → concept map**: which concept for which awareness stage / placement
- **Test plan**: launch order, budget split, primary metric, decision gate (day)
- **Internal run order**: the phase chain above, so the sprint is repeatable
```

## Quality Gate

Score against the genius.md Static rubric + the 1-second recognition test. Retry the weakest section once if any row fails.

| Criterion | FAIL | PASS | EXCEL |
|---|---|---|---|
| **Gap-grounded strategy** | No competitor scan; white space asserted, not found | Competitors scanned; one-sentence white space the batch commits to | Gap names a specific missing awareness-level/format the whole slate exploits |
| **Format diversity** | All concepts collapse into one archetype | 4–6 archetypes, each answering a different objection | Slate is a testing matrix — each format isolates one variable; lo-fi over-indexed |
| **Copy discipline** | Generic benefit; 3+ mechanics crammed; em dash / misspelling present | Each concept = one goal + 1–2 mechanics; leads with a number/name where possible | Golden-nugget testimonial mined into a headline; every word does work (nothing removable) |
| **1-second clarity** | Concepts read as "this and this and this," no focal point | Every spec pre-passes the 1-sec test on paper; QA n=5 run | 4/5 strangers name the offer in one second AND name the benefit unprompted |
| **Sellable package** | Loose assets, no run order | Spec sheet + persona map + test plan + internal run order | Client (or their team) can re-run the sprint without you — productized |

If a concept fails the 1-second test, it doesn't ship — re-hierarchy (headline bigger, one focal point) or kill it. Less is more.

## Example Output

**Context**: My.BPM (Farrice's EDM/rave streetwear brand). Audience 22–35, festival/rave-going, identity-forward, in-culture (PLUR vernacular). ~30 SKUs, mid creative budget, ~6-figure and scaling, founder-led with a small creator network. Currently runs standard UGC with declining ROAS. Ask: a paid sprint of 6 launch-ready statics off one gap.

```markdown
# Static Ad Sprint — My.BPM — 2026-07-07

## Service Frame
- Scope: 6 static concepts across 6 archetypes, produced + QA'd
- Deliverables: strategy brief · gap analysis · copy bank · 6 design specs · 6 assets · test plan
- Positioning: "Research-first static sprint — 6 launch-ready concepts, each grounded in a competitor gap"
- Price band: $2.5K sprint (mid research depth, 6 concepts)

## Phase 1 — Strategy + Gap Analysis
- Goal(s): C1 problem-aware capture · C2/C4 education-to-offer · C3 transformation proof · C5 sale-period offer · C6 organic-style trust
- Persona: 24–30 festival-goer who bought a $12 "rave" tank last season that pilled and faded by Day 3 of the set — objection: "why pay 4x for a tank?"
- Competitor scan: generic Shein/Amazon "rave" merch + two DTC festival brands — all running polished lifestyle carousels, avg winning-ad look ~60s. Nobody runs lo-fi transformation or a cost-of-cheap-merch infographic.
- White space (one sentence): the category sells the vibe in gloss; nobody shows what a $12 tank looks like on Day 3 vs a My.BPM fit — so we own proof and cost-per-wear.

## Phase 2 — Format Slate
| # | Concept | Archetype | Objection | Production | Aspect |
|---|---|---|---|---|---|
| 1 | Day-3 fit | Transformation (lo-fi creator) | "does it actually hold up?" | lo-fi | 9:16 |
| 2 | vs generic merch | Comparison / us-vs-them | "why 4x the price?" | graphic | 4:5 |
| 3 | Cost of a $12 tank | Educational infographic | category-unaware | graphic | 1:1 |
| 4 | Dress like the drop | Headliner (primal desire) | "will I stand out?" | hi-fi | 4:5 |
| 5 | Festival Season capsule | Grid static (sale period) | "is it worth a bundle?" | graphic | 1:1 |
| 6 | Rave merch is disposable | Text-only (founder letter) | trust / values | lo-fi | 4:5 |

## Phase 3 — Copy Bank (one locked headline per concept)
- C1 — "I wore this three days straight at EDC. Watch." · Show-the-transformation + call-out-by-name · Support: "Day 1 → Day 3, no pilling."
- C2 — "My.BPM vs the $12 rave tank" · Negative marketing + comparison · Rows below.
- C3 — "The real cost of a $12 rave tank" · Be-specific/number + taboo · Chartr-style cost bars.
- C4 — "Dress like the drop, not the crowd." · Primal desire (belonging/status) · CTA: "Shop the set."
- C5 — "The Festival Season Drop — everything you need for the weekend" · Grid + price anchor.
- C6 — "Rave merch is disposable. We think that's the problem." · Founder letter, borrows from customers.

## Phase 4 — Design Specs (per concept, C1–C3 shown)

### Concept 1 — Transformation (lo-fi creator)
- Hierarchy: [1] top quote headline → [2] before/after split (Day 1 crisp / Day 3 pilled generic vs My.BPM still crisp) → [3] creator holding the piece to camera
- Copy: Headline "I wore this three days straight at EDC. Watch." · Labels "DAY 1" / "DAY 3" · Proof: creator @handle
- Production + aspect: lo-fi creator · 9:16
- Generator prompt: `Vertical 9:16 UGC static. Top quote overlay "I wore this three days straight at EDC. Watch." Before/after split: left a generic black rave tank pilled and faded labeled DAY 3, right a My.BPM tank still crisp labeled DAY 3. Creator (24, festival styling) holding the tank to camera below. iPhone photo, natural festival lighting, authentic, unpolished. Exclusions: no em dash, no misspellings, one focal point (the split), no studio lighting, no AI-perfect faces.`
- 1-second read: "a rave shirt that survives the festival"

### Concept 2 — Comparison / us-vs-them
- Hierarchy: [1] two-column header → [2] ✓/✗ rows → [3] product shots per column
- Copy: Header "My.BPM" vs "The $12 rave tank" · Rows (green ✓ / red ✗): "Holds color 3+ days," "Cut for movement / doesn't ride up," "Breathable at 90°F," "No pilling by Day 3"
- Production + aspect: graphic-style · 4:5
- Generator prompt: `4:5 comparison static, two columns. Left "My.BPM" with a folded crisp tank; right "The $12 rave tank" with a pilled faded tank. Four center rows with green check (left) vs red X (right): "Holds color 3+ days", "Cut for movement", "Breathable at 90°F", "No pilling by Day 3". High-contrast type, dark bg, brand magenta accent. Exclusions: no em dash, no misspellings, one focal point.`
- 1-second read: "My.BPM beats cheap tanks on durability"

### Concept 3 — Educational infographic (Sweetgreen pattern)
- Hierarchy: [1] title → [2] cost bars → [3] one-line kicker
- Copy: Title "The real cost of a $12 rave tank" · Bars: "$12 sticker" vs "true cost ~$48" broken into replace-every-festival ($12 x4), embarrassment of a mid fit, resale $0 · Kicker: "One My.BPM tank outlasts four."
- Production + aspect: graphic-style (Chartr look) · 1:1
- Generator prompt: `1:1 Chartr-style bar-chart infographic titled "The real cost of a $12 rave tank". Green bar "$12 sticker price" vs taller red bar "~$48 true cost" split into segments (replaced x4 per season, zero resale). Clean editorial data-viz, muted background, one accent color, small footnote. Exclusions: no em dash, no misspellings, one focal point, not busy.`
- 1-second read: "cheap tanks actually cost more"

*(C4 headliner, C5 grid, C6 founder letter specs follow the same schema.)*

## Phase 5 — Production
- Brand brain: My.BPM voice (in-culture PLUR, never cringe-corporate), palette (black + festival magenta + UV-reactive accent), lo-fi over polish.
- Routes: C1 → Higgsfield Soul (creator/person). C3 → generate_design.py graphic-style. C5 → generate_image.py grid. Each as a 3-variation batch; keep the best, edit-to-refine the rest.
- Edit log (C1): "make the Day-3 generic tank look more pilled," "shrink the creator, make the split the focal point," "remove the m dash in the caption."

## Phase 6 — Comprehension QA
| Concept | 1-sec test (n=5) | Pass? | Fix applied |
|---|---|---|---|
| 1 | "a rave shirt that lasts" ×4 | ✅ | enlarged DAY labels |
| 2 | "cheaper tank comparison" ×5 | ✅ | — |
| 3 | "cost of cheap shirts" ×4 | ✅ | dropped one bar segment (too busy) |
| 4 | "festival streetwear" ×3, "a band?" ×2 | ❌→re-hierarchied | headline size +40%, product smaller |
| 5 | "a merch bundle" ×5 | ✅ | — |
| 6 | "a brand's opinion post" ×4 | ✅ | — |

## Phase 7 — Delivery Package
- Persona → concept map:
  - Problem-aware / burned by cheap merch → C1 (transformation), C2 (comparison) — MOF/retarget
  - Category-unaware / price-anchored → C3 (infographic), C4 (headliner) — TOF cold
  - Ready to buy / sale period → C5 (grid) — retarget + sale windows
  - Values/trust skeptic → C6 (founder letter) — TOF, organic-style
- Test plan: launch all 6 at $15/day for 7 days. Primary metric hook rate + CTR; decision gate Day 7 — top 3 by CTR/ROAS scale to lookalikes; kill the rest. Hypothesis: lo-fi transformation (C1) beats the category's polished lifestyle on hook rate.
- Internal run order: 08 → gap analysis → 09 → 10 → per-concept spec → 15 (3-var batches + edit-to-refine) → 11 → package. Repeatable as a $2.5K sprint.
```

**What elevates this**: the whole batch commits to ONE found gap (nobody shows Day-3 durability or cost-per-wear), so the six concepts are a testing matrix, not a grab bag. Every headline leads with a number or names the audience, each concept does exactly one job, C4 got caught by the 1-second test and re-hierarchied instead of shipped, and the package hands back an internal run order — the client's team could re-run it without Farrice. It's a service, not a favor.

## Render Handoff (optional — don't stop at text)

Once the design specs are locked (Phase 4), don't stop at prompts — offer to render. Production runs through `/dara-static-production` (15), which routes each concept to the right tool. Route by format:

- **Educational infographic / comparison grid** (C2, C3, C5) → `python3 execution/generate_design.py --type graphic --aspect <1:1|4:5> "<design brief>"` — art-direction → Nano Banana 2, best for a DESIGN.md-style brief that should auto-render (supports `--iterate`, `--prompt-only`).
- **Transformation / founder / anything with a real person** (C1, C6) → route people through Higgsfield Soul: `python3 execution/creative_router.py route --task "lo-fi festival creator holding tank, before/after" --json` — it picks the service and prints the exact `cost_gate.py` pre-flight. Surface that pre-flight; never bypass the cost gate.
- **Headliner / grid / product-forward statics** (C4, C5) → `python3 execution/generate_image.py "<prompt>" --aspect <1:1|4:5|9:16>` (Nano Banana 2).

**Edit-to-refine loop** (Dara's method, verbatim analog): after the first render, iterate with natural-language edits instead of regenerating — `python3 execution/generate_image.py --edit <concept.png> "remove the m dash / change the background to beige / make the tank smaller / make five more variations for a problem-aware audience"`. Keep the composition, fix only what's wrong. Image generation can trip the cost gate — run the `creative_router.py` pre-flight and surface the printed `cost_gate.py` command; do not work around it.

## Next Steps

- **Winners to video**: run `/dara-format-swap` (16) on the top 3 static winners to diversify into video.
- **New hypothesis**: re-run this sprint against a different gap to test against the current winners.
- **Productize**: package the run order above as a repeatable $2.5K–$5K sprint; research depth and concept count set the tier.

---
name: dara-educational-infographic
description: "Build the TOF educational infographic that masquerades as organic (Sweetgreen 'The Economics of $15 Salads'). Teach a category-level insight, visualize it as a chart, drive leads with a soft CTA."
tier: practitioner
version: "2.0"
---

# `/dara-educational-infographic` — TOF Educational Infographic Builder

Build the educational infographic — the top-of-funnel static that leads with *education*, not a pitch, and doesn't feel like an ad. It's the Sweetgreen "The Economics of $15 Salads" play: teach a category-level insight any persona benefits from, prove it with a chart, position yourself as the authority. Use it as the cold-prospecting workhorse when you want the "I'm learning" audience, not the "buy now" audience.

## Genius Context (Load First)

Read `skills/dara-denney-meta-ads/genius.md` (the **Static Ads** section) and `skills/dara-denney-meta-ads/references/static-ad-exemplars.md`. Internalize:

- **The exemplar** — Sweetgreen **"The Economics of $15 Salads"** (Chartr-style bar chart: green "Sweetgreen Sales $15" bar vs red "Total Opex $17.56" broken into cost components, footer noting the operating loss per $15 of revenue). Dara's frame: *"Masquerades as something that does well organically and really doesn't feel like an ad."* The build question is literally **"how can I create a piece of content any one of my personas actually benefits from"** (education / entertainment / narrowing choices).
- **Layer 1 Strategy** — this format's job is ONE goal: *education* for a problem-unaware / category-curious top-of-funnel persona. Don't make it also do offer-conversion. Pick the persona by stage + objection, not "everyone."
- **Layer 3 Copy mechanics that carry an infographic**: (1) **be specific — lead with a number** communicating time/effort/cost; (6) **negative marketing** — name the cost the audience doesn't see; (7) **borrow from customers** — a real number beats a made-up one.
- **The 1-second comprehension test** and **"clarity always beats creativity"** / **"less is more."** An infographic invites a longer read, but a stranger must still name *what category this teaches about* in one second — or it dies in the feed.

## Input Required

- **Brand**: name, category, what they sell, hero product
- **Persona**: the specific top-of-funnel viewer (stage + what they don't yet know), not "small business owners"
- **Category-level insight**: the one thing this persona doesn't know about how the *category* works (NOT a product feature). If you don't have one yet, Step 1 finds it.
- **Real numbers**: any data you can stand behind — price points, timelines, customer-review figures, published stats. The more you own, the stronger the chart. (Fabricated stats = a lie on a chart, and it will get flagged.)
- **Brand kit** (optional): 2-3 colors, logo, so the render matches.

## Execution

You are Dara. You don't lecture the format — you pick the insight, pick the chart that proves it, and write the one headline that does the targeting. Decide and justify.

1. **Lock the ONE insight.** Ask: what does this persona *need to know about the category* that they don't? Not "why we're better" — "how the category actually works, and what it's quietly costing them." Good insight shapes: a hidden cost, a debunked myth, a cost/time breakdown that surprises. Bad insight: any sentence with your product's spec in it. Write it as one sentence. If it doesn't make *you* go "huh, didn't clock that" — dig again. This is the "novel enough to earn a read" gate.

2. **Pick the chart that proves it — one chart, one point.** The insight is the headline; the visualization is the proof. Match the shape to the claim:
   - **Bar / stacked bar** — comparing quantities or exposing a cost breakdown (the Sweetgreen shape; the default, and usually the right call).
   - **Timeline / cumulative line** — a cost or effect compounding over time.
   - **Us-vs-them table** — only if the insight is genuinely comparative (otherwise that's the Comparison format — route to `/dara-comparison-callout`).
   Keep it to **3-5 data points**. More than 5 and you've failed the "less is more" test before you've rendered a pixel.

3. **Write the headline as the insight, framed like a research post — not a promo.** It should read like something a smart friend or an analyst wrote, e.g. "The Economics of $15 Salads." Lead with or feature the number. NO product name in the headline — the second a brand name appears, the "masquerades as organic" magic dies. One line. Kill the em dash.

4. **Ground the numbers.** Every figure on the chart gets a source you'd defend to Farrice: your own pricing, a customer-review average (run a review CSV through your LLM for the real number — that's the "borrow from customers" mechanic), or a citable published stat. Put a small footnote source line on the graphic. If a number is an estimate, label it an estimate. Unverifiable stat = cut it.

5. **Set the visual hierarchy.** Headline FIRST (does the targeting) → the chart (the proof) → footnote/source → soft CTA last and smallest. Focal point is the messaging + chart, ~9 times out of 10. 2-3 colors, high contrast, one accent for the "punchline" bar. No decoration that isn't carrying data.

6. **Write the soft CTA — matched to funnel position.** This is TOF; the CTA is a low-commitment next step, not a purchase. "See the full breakdown," "Get the guide," "Read the data." Never "Buy now" / "Sign up today" — wrong funnel, and it snaps the reader out of learning-mode.

7. **Set format + production spec** (aspect ratio, production level) and run the Quality Gate before you render.

## Output Schema

```markdown
# Educational Infographic Spec — [Brand]

## Layer 1 — Strategy
- **Goal**: Education (TOF). Single job — no offer-conversion bolted on.
- **Persona**: [stage + what they don't yet know]
- **Awareness level**: Problem-unaware / category-curious

## The Insight (one sentence)
[The category-level truth this teaches. No product spec.]

## Headline (the targeting line)
"[Research-framed insight, number-forward, no brand name]"

## Visualization
- **Chart type**: [Bar / stacked bar / timeline / cumulative line / table]
- **Data points (3-5)**:
  1. [label] — [value] — [source]
  2. [label] — [value] — [source]
  3. [label] — [value] — [source]  ← accent/punchline
- **Footnote / source line**: [where the numbers come from]

## Layout & Hierarchy (top → bottom)
1. Headline (largest)
2. Chart (focal proof)
3. Footnote / source (small)
4. Soft CTA (smallest)
- **Palette**: [2-3 colors + 1 accent for the punchline data point]
- **Type**: [sans-serif primary, accent secondary]

## Soft CTA
"[Low-commitment TOF next step — never 'Buy now']"

## Format
- **Aspect ratio**: 4:5 (vertical Meta feed, TOF default) — or 1:1 if the chart reads wide
- **Production level**: graphic-style (AI-gen infographic)
```

## Quality Gate

Score against the genius.md Static rubric + the 1-second comprehension test. Retry the weakest section once before delivery.

| Criterion | FAIL | PASS | EXCEL |
|---|---|---|---|
| **Category insight** | Teaches a product feature; brand name in the headline | Category-level principle, no product mention | Genuinely novel — the viewer learns something they didn't know |
| **Number grounding** | Invented / unsourced stats on the chart | Every figure has a defensible source; footnote present | Numbers pulled from real customer reviews or citable data; unassailable |
| **Chart clarity** | >5 data points, cluttered, hard to read | 3-5 points, one clear comparison, one accent | The chart alone lands the point without the headline |
| **1-second test** | Stranger can't tell it's about [category] in 1s; "too much going on" | Stranger names the category topic in ~1s | Reads instantly as an organic research post, not an ad |
| **Funnel fit** | Hard-sell CTA / product pitch | Soft TOF CTA, education-first | Feels like value the persona would save or share |

**Hard veto**: any fabricated statistic on the chart = kill and re-ground (Step 4). A wrong number on an "educational" ad is worse than no ad.

## Example Output

**Context**: My.BPM — Farrice's EDM/rave streetwear brand. Persona: 22-35 festival-goer who does a fast-fashion "haul" every summer (Shein/Temu rave fits), problem-unaware that it's a terrible cost-per-wear. Category villain (from `/dara-static-format`): disposable fast-fashion festival merch. ~30 SKUs, mid budget, ~6-figure scaling.

**THE DELIVERABLE:**

```markdown
# Educational Infographic Spec — My.BPM

## Layer 1 — Strategy
- **Goal**: Education (TOF). Not selling a piece — teaching the economics of festival fits.
- **Persona**: 22-35 raver who buys a fresh Shein/Temu haul before every festival and tosses it after
- **Awareness level**: Problem-unaware (doesn't compute cost-per-wear on rave fashion)

## The Insight (one sentence)
A cheap festival haul is the most expensive way to dress — it doesn't survive one summer, so the real cost-per-wear is brutal.

## Headline (the targeting line)
"The Economics of an $80 Festival Haul"

## Visualization
- **Chart type**: Horizontal bar — cost-per-wear (lower = better)
- **Data points (3)**:
  1. Shein/Temu weekend haul — **~$53 / wear** — $80 haul ÷ ~1.5 wears before it pills/tears (est.)
  2. Generic "rave" tank — **~$6 / wear** — $18 ÷ ~3 wears (est.)
  3. My.BPM piece — **~$1.45 / wear** — $58 ÷ 40+ wears, festival + street (est.)  ← accent bar
- **Footnote / source line**: "Cost-per-wear = price ÷ realistic wears. Haul durability estimated from customer reviews, summer 2025."

## Layout & Hierarchy (top → bottom)
1. "The Economics of an $80 Festival Haul" (largest)
2. Three-bar chart, the $53 bar in alarm-red, the $1.45 My.BPM bar in the brand's neon accent
3. Footnote / source (small)
4. Soft CTA (smallest)
- **Palette**: near-black background, off-white type, alarm-red for the expensive bar, neon-green accent for My.BPM
- **Type**: bold condensed sans headline; mono for the numbers (reads "data")

## Soft CTA
"See what actually survives a festival →"

## Format
- **Aspect ratio**: 4:5 (vertical Meta feed)
- **Production level**: graphic-style
```

**What elevates this**: it borrows the exact Sweetgreen move — a research-framed "The Economics of ___" headline over a bar chart that quietly indicts the category, with zero product name up top. The insight (cost-per-wear, not sticker price) is the reframe the persona has never run. The punchline bar carries the brand without pitching it. The CTA stays in learning-mode. And every number is an estimate *labeled as an estimate* with a stated method — no fake "5/5 testers" stat to get flagged.

## Render Handoff (optional — don't stop at text)

Once the spec is locked, offer to render it — don't leave it as text. This is a graphic-style infographic (chart + type, no person), so the route is:

- **Primary**: hand the locked spec to **`/dara-static-production`** (workflow 15), which orchestrates the brand-brain → 3-variation → edit-to-refine pipeline. For a single infographic, the direct call is `python3 execution/generate_design.py --type graphic --aspect 4:5 "<the full spec above as a brief>"` — its art-direction → Nano Banana 2 pipeline turns a DESIGN.md-style brief into a rendered chart. Use `--prompt-only` first if you want to inspect the compiled prompt.
- **Edit-to-refine loop** (Dara's natural-language edits, our analog): `python3 execution/generate_image.py --edit <infographic.png> "<edit>"` — e.g. "remove the em dash," "make the My.BPM bar the only colored bar," "make the headline bigger," "change the background to near-black." Iterate; don't regenerate from scratch.
- **Cost note**: image generation can trip the cost gate. Run `python3 execution/creative_router.py route --task "educational infographic bar chart, graphic-style" --json` to get the exact `cost_gate.py` pre-flight command, and **surface it — never bypass it**. Rendering is an optional offer, not a forced pipeline step.

For a version with a person (e.g. a lo-fi creator holding the "receipt"), that's a different format — route to `/dara-transformation-static`, which renders faces via Higgsfield Soul through `creative_router.py`.

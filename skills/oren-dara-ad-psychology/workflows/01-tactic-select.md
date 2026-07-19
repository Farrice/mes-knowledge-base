---
description: Front door — match a brand × persona × awareness state to 2-3 of the six psychological tactics, each with mechanism, concept seed, and failure-mode warning. Runs BEFORE format/vessel selection.
---

# `/adpsy-tactic-select` — Tactic Selection Brief

Decide the psychological mechanism before anyone talks formats. Output is a ranked brief of 2-3 tactics with concept seeds, ready to hand to the tactic builders (02–07) and then to `dara-denney-meta-ads` for the vessel.

## Pre-Flight Gate

- Is the goal a **cold-traffic ad concept**? If it's organic-only brand content → route `oren-content-flywheel`/`kallaway`. If it's pure static production with a locked concept → route `/dara-static-engine`.
- Do you have real customer-voice material (reviews, comments, organic saves)? If none exists, run the research step below honestly and flag confidence LOW — never substitute imagined customer voice.

## Skill Acquisition

Read `genius.md` (six-tactic table, patterns, vetoes) + `references/six-tactics-map.md` (selection heuristics). For live brands, mine actual inputs first: reviews CSV, comment sections, the audience's organic favorites (Pattern 6: organic beats competitor libraries).

## Input Required

- **[BRAND + PRODUCT]**: what's sold, price point / AOV, category
- **[PERSONA]**: who, in their own register — plus the #1 objection
- **[AWARENESS STATE]**: unaware / problem-aware / solution-aware / product-aware
- **[CUSTOMER-VOICE MATERIAL]**: reviews, comments, organic posts the audience loves (or state NONE)
- **[ACCOUNT CONTEXT]** (optional): what's already running; funnel drift

## Execution

1. **Mine the inner monologue.** From the customer-voice material, list 5-10 things this customer thinks/says privately but wouldn't post — group-chat register, not brand register. (Pattern 1: Inner-Monologue Sourcing.)
2. **Run the selection heuristics** from `six-tactics-map.md` against brand × persona × awareness. Score each of the six tactics: mechanism fit, evidence in the customer voice, category energy (taboo? rip-off? trust gap? demonstrable claim?).
3. **Rank the top 2-3.** For each, write: the named mechanism · one concept seed rooted in an actual customer line (quote it) · the **predicted comment section** (if you can't predict the comments vividly, the tactic-fit is weak) · the failure mode to avoid, named from genius.md.
4. **Run the vetoes** on every seed: shock-for-shock, golden-nugget review trap (lived-experience test), fake authority, claim-without-demonstration.
5. **Route.** Name the builder workflow for each pick (02–07) and the eventual vessel handoff (`six-tactics-map.md` right column).

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| High-AOV / luxury | Weight tactics 2 + 6; both-ends price play (justify AND filter) |
| Health / body / intimate | Tactic 1 candidate — but the lived-experience veto is mandatory and decisive |
| Commodity with rip-off energy | Weight tactic 3; study the demo's old TV for scenario formats |
| Multi-SKU / spatial value prop | Weight tactic 5; visual carries the prop |
| No client (spec work / pitch) | Same brief, one tactic, one written ad — the Spec-Ad Wedge |

## Output Requirements

The Tactic Selection Brief: persona inner-monologue list (quoted) → ranked 2-3 tactics, each with mechanism / concept seed with source quote / predicted comments / failure-mode warning / builder + vessel route. One page. Density over completeness.

Execution prompt: `references/prompts-v2/01-tactic-selection-brief.md`

## Quality Gate

Score against genius.md rubric: inner-thought rooting ≥7 (every seed traceable to a real customer line), mechanism named ≥7, comment design considered. Any veto hit = rework before delivery. If customer-voice material was NONE, the brief must carry a visible LOW-CONFIDENCE flag and a research-first recommendation.

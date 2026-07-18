# Awareness Distribution Map

> Run the RMBC 2.0 research stack before any copy decision: measure how the
> market actually distributes across the five awareness levels, then let that
> distribution set funnel length, mechanism complexity, and lead angle.
> Never assume awareness — Georgi's own brand misfired by assuming it.

## Expert
Stefan Georgi — Dopamine Copywriting Architecture (RMBC 2.0 layer)

## Inputs Required
1. **Product/Offer**: What's being sold + price point
2. **Category**: The solution category the market already knows (if any)
3. **Traffic Source(s)**: Meta / native / YouTube / TikTok / organic — each carries different buyer intent
4. **Main Competitors**: 3-5 names (or "unknown" — Phase 2 finds them)

## Phase 1: Awareness Distribution Research

Run deep research (Gemini deep research preferred; any strong research model works) with the Georgi query:

> "For [product] in [category], if you were going to put a percentage of the
> addressable market in each of these categories — unaware, problem aware,
> solution aware, product aware (Georgi rewrite: aware of the CATEGORY of
> solutions similar to this one), most aware — what would each percentage be,
> and why?"

Rules of interpretation:
- **Virality ≠ product awareness.** A viral TikTok moment can still mean only ~10% of the market is category aware (the whipped-tallow lesson).
- **Unaware is only sellable when the desire is universal** (money, status). "You're a video ad and you have a weight problem — surprise" does not work. Only established brands (the Grant Cardone effect) can message all the way up to unaware.
- The biggest scalers deliberately message one level BROADER than competitors fighting over the aware minority.

## Phase 2: Competitor Big-Idea Inventory

For the 5 main competitors, capture:
- Their **big idea** (the one they lead with — not their feature list)
- Value propositions, what buyers like/dislike (mine reviews)
- Which awareness segment their messaging assumes

> Georgi's critique rule: you cannot judge any headline until you can see
> "the five big ideas of the five main competitors." Build that table first.

## Phase 3: Psychographic Research (Classic RMBC Core)

Deep research pass on: deep-seated hopes, dreams, victories, failures, deepest desires — "the dark night of the soul when they're in bed staring at the ceiling at 2am."

## Phase 4: Unify

Feed all three outputs to the model: *"Here are three research documents. Create one unified research document that preserves every insight."* This document is the source of truth for every downstream decision.

## Phase 5: Calibration Decisions (Read Straight Off the Map)

| Distribution Reading | Funnel/Copy Decision |
|---|---|
| Concentrated at problem/solution aware | Educate-first: longer video ad, longer advertorial, longer product page. Introduce the category before differentiating within it |
| Concentrated at category aware + high buyer intent | Short condensed funnel — no long VSL, short video/static ads, minimal advertorial |
| High price point (any distribution) | Long copy returns — but it sells the URGENCY of the pain ("buy today, not in three months"), not the validity of the solution |
| Category aware | Mechanism = "why the other programs/products in this category failed you" |
| Broad/low awareness | Mechanism = simple paradigm-shift reframe of what they half-know ("income problem vs. asset problem") — do NOT overcomplicate |

## Phase 6: Gap-Finding Prompt

With the unified document loaded:
> "We're targeting the [X]-aware segment. Based on this awareness distribution,
> these competitor big ideas, and this psychographic research: what logical
> messaging for this segment is missing — what SHOULD be said that nobody is
> saying?"

Optionally rank candidate mechanisms: *"Here are the 5 I like most. Based on this research, rank them 1-5 by probability of success and explain why."*

## Quality Gate
Before shipping the unified research document and calibration verdict, verify:
- [ ] All 5 awareness levels have a % + rationale, not just a top-of-mind guess
- [ ] Competitor big-idea table names all 5 competitors' actual big idea (not their feature list)
- [ ] Psychographic pass reaches "2am staring at the ceiling" depth, not surface demographics
- [ ] Unified document exists as ONE artifact carrying every insight from all three passes — no orphaned research left in a separate file
- [ ] Calibration verdict names funnel length, mechanism complexity tier, AND target segment explicitly — not just a vague "educate more"
- [ ] At least 3 gap-derived angles surface messaging nobody in the category is currently using

If any box is unchecked, the research stack is incomplete — do not hand off to `copy-thinker-judgment-loop` or any drafting workflow.

## Output Contract
- Awareness distribution table (5 levels, % + rationale)
- Competitor big-idea inventory (5 × 5 table)
- Unified research document
- Calibration verdict: target segment, funnel length, asset lengths, mechanism complexity tier
- 3-5 gap-derived messaging angles nobody in the category is using

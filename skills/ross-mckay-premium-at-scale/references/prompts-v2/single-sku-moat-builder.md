---
name: "Single-SKU Moat Builder"
source_prompt: "skills/ross-mckay-premium-at-scale/references/prompts/single-sku-moat-builder.md"
skill: ross-mckay-premium-at-scale
standard: structure-pure-v2
refactored: 2026-07-11
---

# Single-SKU Moat Builder

## Purpose
Force radical focus to reach a $10M run rate before expanding the product line.

## Input Required
```
CURRENT_SKU_LINEUP: [List all current products]
HERO_SKU: [The one product with the highest traction/margin]
REVENUE_GOAL: [Target revenue to unlock the next phase, e.g., $10M]
```

## Instructions
Act as an elite CPG Operations Strategist. Design a 12-month operational roadmap that enforces radical single-SKU focus:
1. Kills or deprioritizes all products except the `[HERO_SKU]`. Provide harsh but logical rationales for cutting the fat.
2. Reallocates all supply chain and marketing capital exclusively behind the `[HERO_SKU]`.
3. Defines the milestone triggers required to hit `[REVENUE_GOAL]` before any new flavor or product can be introduced.
4. If tertiary products must exist, they must solely serve to cement the core ICP (e.g., DTC-only gels for hardcore athletes) without pulling retail focus.

Remember that manufacturing leverage comes from extreme volume on a single item. Complexity is the enemy of scale.

## Output Contract
Deliver a 12-month operational roadmap with four labeled sections:
- SKU Cut List: every item in `[CURRENT_SKU_LINEUP]` other than `[HERO_SKU]`, each with a one-line kill/deprioritize rationale
- Capital Reallocation: how supply chain and marketing spend shift to concentrate on `[HERO_SKU]`
- Milestone Gate: the specific revenue/velocity checkpoints that must be hit before `[REVENUE_GOAL]` unlocks any new product conversation
- Tertiary Product Rule (if applicable): the narrow condition under which any non-hero SKU is allowed to exist, and the guardrail preventing it from consuming retail focus
- Every SKU named in `[CURRENT_SKU_LINEUP]` must be accounted for exactly once — none dropped silently, none merged

## Output Skeleton
```
SINGLE-SKU ROADMAP: [HERO_SKU] → [REVENUE_GOAL]

1. SKU CUT LIST
- [SKU from lineup, not hero]: [kill or deprioritize] — [one-line rationale]
- [repeat for every non-hero SKU in CURRENT_SKU_LINEUP]

2. CAPITAL REALLOCATION
Supply chain: [how manufacturing/procurement capacity shifts to HERO_SKU]
Marketing: [how spend shifts to HERO_SKU]

3. MILESTONE GATE
Checkpoint 1: [revenue/velocity marker] → [what unlocks at this point, if anything]
Checkpoint 2: [next marker toward REVENUE_GOAL]
Full unlock: [REVENUE_GOAL reached] → [what product conversation reopens]

4. TERTIARY PRODUCT RULE
Condition for existing: [e.g., DTC-only, serves the core ICP directly]
Guardrail: [what keeps it from pulling retail focus or capital from HERO_SKU]
```

## Quality Gate
- Every SKU listed in `[CURRENT_SKU_LINEUP]` appears exactly once in the Cut List (except `[HERO_SKU]` itself)
- Each cut rationale is a stated tradeoff (what's lost) plus the reason it's worth losing — not a generic "focus is good" line
- The Milestone Gate ties directly to `[REVENUE_GOAL]` as supplied — no invented revenue figures
- The Tertiary Product Rule section is either populated with a real guardrail or explicitly states "no tertiary products permitted until goal is reached"
- No new SKUs, flavors, or line extensions are introduced anywhere in the roadmap ahead of `[REVENUE_GOAL]` being hit

## Deploy When
- Product roadmap planning and manufacturing capital allocation
- A founder or team is proposing to launch a second SKU before the first has proven retail traction
- Auditing an existing product line for where focus has drifted

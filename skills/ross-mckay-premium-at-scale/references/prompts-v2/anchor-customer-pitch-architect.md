---
name: "The Anchor Customer Pitch Architect"
source_prompt: "skills/ross-mckay-premium-at-scale/references/prompts/anchor-customer-pitch-architect.md"
skill: ross-mckay-premium-at-scale
standard: structure-pure-v2
refactored: 2026-07-11
---

# The Anchor Customer Pitch Architect

## Purpose
Build a pitch for a major mass retailer (Walmart, Target) that focuses on velocity over product features.

## Input Required
```
PRODUCT_NAME & BRAND: [Name and short descriptor]
TARGET_MASS_RETAILER: [e.g., Walmart, Target]
DTC_AUDIENCE_SIZE: [Active subscribers or email list size]
CATEGORY_VELOCITY_GOAL: [e.g., 20 units per store per week]
```

## Instructions
Act as a hyper-aggressive CPG Founder expanding from DTC to retail. Draft a pitch deck outline for retail buyers that explicitly ignores traditional specialty-market positioning (Whole Foods, farmers markets). The pitch must:
1. Lead with Incrementality: Show how the `[DTC_AUDIENCE_SIZE]` will be driven directly to the `[TARGET_MASS_RETAILER]`. Explain that these aren't just consumers; they are mobilized buyers.
2. Promise Velocity: Orient around hitting `[CATEGORY_VELOCITY_GOAL]` to prove you understand that shelf space is rented, not owned.
3. Detail the Trade Spend Strategy: Show exactly how you will fund promotions (e.g., 2-for-$4) to drive trial without the retailer taking the hit on margin.

Never pitch the distributor. You are pitching the anchor customer to secure the PO, which you will then use to dictate terms to the distributor.

## Output Contract
Deliver a retail buyer pitch deck outline with:
- One incrementality section that ties `[DTC_AUDIENCE_SIZE]` directly to projected traffic/sales lift at `[TARGET_MASS_RETAILER]`
- One velocity section stating the `[CATEGORY_VELOCITY_GOAL]` and the specific mechanisms that will drive it (not aspirational language)
- One trade spend section with a concrete promotional mechanic and who funds it
- Zero references to distributors, specialty grocers, or farmers markets as the entry channel — the retailer is the entry channel
- Slide-by-slide outline format (headline + 2-4 bullet points per slide), not prose paragraphs

## Output Skeleton
```
ANCHOR CUSTOMER PITCH: [PRODUCT_NAME] → [TARGET_MASS_RETAILER]

SLIDE 1 — THE ASK
[One-line statement of the PO/shelf commitment being requested]

SLIDE 2 — INCREMENTALITY
[How DTC_AUDIENCE_SIZE converts into retailer foot traffic / basket lift]
- [Mechanism 1 — e.g., geo-targeted email/SMS drive-to-store]
- [Mechanism 2 — e.g., audience overlap with retailer's existing shopper base]

SLIDE 3 — VELOCITY COMMITMENT
[Stated CATEGORY_VELOCITY_GOAL and the operational plan behind hitting it]
- [Supply readiness point]
- [Comparable category benchmark used to justify the number, if available]

SLIDE 4 — TRADE SPEND / TRIAL PLAN
[Specific promotional mechanic, e.g., "2-for-$4"]
- [Funding source — brand-funded, not retailer-margin-funded]
- [Duration / trigger for the promotion]

SLIDE 5 — THE CLOSE
[Direct ask for the PO — no distributor mention]
```

## Quality Gate
- Every bracketed input variable is used at least once in the output, with the retailer's actual name substituted (not left as a placeholder)
- The word "distributor" does not appear anywhere except explicitly excluded from the entry strategy
- The velocity claim is stated as a specific number tied to `[CATEGORY_VELOCITY_GOAL]`, not a vague "strong sell-through"
- The trade spend mechanic is concrete (a specific promo structure) rather than "we will run promotions"
- Output is structured as slide headlines + bullets, scannable in under 60 seconds

## Deploy When
- Expanding a physical product from DTC to retail distribution
- Preparing a buyer meeting with a major mass retailer before any distributor conversation
- Reworking a distributor-first go-to-market plan into a retailer-first one

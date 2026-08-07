---
description: Design a multi-bump checkout on the Vander Wielen model — break the one-bump rule, select bumps that serve the buyer the core product deliberately underserves, price against individual-purchase anchors
tier: 2
---

# /sv-order-bump-stack — The 60%-Attach Checkout

Produces a **complete order-bump stack**: which bumps, what they contain, how they're priced, and the checkout copy. Sam's stack attached at **60%** and produced **$103,000 — on top of the $500K**, a roughly 25% revenue lift.

The rule she broke: *"I always adopted the rule that you had to only have one order bump at checkout, or else. I started adding multiple and people buy them all."*

## Pre-Flight Gate

Load `genius.md`. The selection rule that makes this work:

> **A bump serves the buyer your core product deliberately underserves.**

Sam's core product targets the beginner entrepreneur. Her first bump is a pack of advanced templates that *"didn't necessarily make sense for the beginner… but somebody else."* The bump isn't a discount or an upsell — it's coverage for an adjacent buyer already in your checkout.

If a proposed bump is just "more of the same thing they're already buying," reject it.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md`
3. The core offer, its price, and who it deliberately excludes
4. Existing assets that could become bumps (this rarely requires new production)

## Execution

### Step 1 — Name who the core product underserves

Write it explicitly: *"[CORE OFFER] is built for [BUYER]. It deliberately does not serve [ADJACENT BUYER] because [REASON]."* Every bump answers that gap.

### Step 2 — Mine existing assets

Sam's three bumps were mostly assembly, not creation. Look for: advanced/edge-case material cut from the core, templates you use internally, a small training that removes an implementation blocker.

### Step 3 — Build the stack (2–4 bumps)

Model on Sam's structure:

| Bump | Shape | Her example |
|---|---|---|
| **1 — Depth** | Advanced/edge-case pack for the more sophisticated buyer | Additional contract templates, **$199, ~$1,000 if bought individually** |
| **2 — Adjacent job** | Solves a nearby problem the core doesn't touch | Email template pack: the late-paying-client email (written to stay inside debt-collection rules), the kind note to a copycat, the GDPR template |
| **3 — Implementation** | Removes the "now what do I do with this" blocker | *"A little training to teach them how to upload it to Kit — where to put it and how to use it"* |

Bump 3 is the most-skipped and cheapest to build: **a short training that gets the bump actually deployed.** Sam bundles it *with* bump 2 rather than selling it alone.

### Step 4 — Price against the individual-purchase anchor

Sam's anchor is explicit: **$199 for what would be almost $1,000 bought individually.** The anchor must be real — a genuine à-la-carte price you actually charge. Fabricated anchors are a slop tell.

Bumps should land well under the core price. Sam: $199 bumps against a $2,000–2,400 core.

### Step 5 — Write the checkout copy

Per bump: one line naming who it's for, one line on the concrete contents, the anchor, the price. No countdown, no "last chance."

### Step 6 — Model the lift separately

Report bump revenue **as its own line**, never folded into core revenue — Sam is emphatic that her $103K sat on top of the $500K, and Nathan had to ask twice to establish it.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Service business** | Bumps become scoped add-ons quoted at proposal, not checkout |
| **Sub-$500 core** | One bump maximum; the multi-bump play needs price headroom |
| **Subscription** | Bumps become one-time onboarding add-ons; never recurring |
| **Regulated content** | Any bump making a compliance promise (Sam's GDPR/debt-collection templates) needs review before sale |
| **Physical product** | Bump 3 (implementation) becomes a setup/care guide |

## Output Schema

```
ORDER BUMP STACK — [Core offer] @ [price]

## The Gap
Core serves: [ ]
Core deliberately does NOT serve: [ ] because [ ]

## The Stack
| # | Bump | Shape | Who it's for | Contents | Anchor (real à-la-carte) | Price |

## Checkout Copy (per bump, ready to paste)
### Bump 1
Who it's for: · What's in it: · Anchor: · Price:

## Assets Required
| Bump | Exists? | Build effort |

## Revenue Model (SEPARATE LINE — never folded into core)
Expected attach: [ ]% (Sam's benchmark: 60% — treat as her result, not your forecast)
Modeled bump revenue: [ ]
As % lift on core: [ ]%

## Compliance flags
```

## Quality Gate

Reject and rebuild if:
- Any bump is "more of the same" rather than coverage for an adjacent buyer
- The price anchor is fabricated rather than a real à-la-carte price
- Bump revenue is folded into core revenue in the model
- Sam's 60% attach is presented as the user's projection rather than her result
- There's no implementation bump and no stated reason for omitting it
- A compliance-adjacent template ships without a review flag

**Execution prompt**: `references/prompts-v2/order-bump-stack.md`

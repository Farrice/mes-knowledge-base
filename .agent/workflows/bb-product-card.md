---
description: BitBranding — Optimize a clothing-brand product card using the 5-component system (hover swap, quick-add, swatches, badges, variant siblings)
---

# /bb-product-card — Fashion Product Card Optimizer (BitBranding)

Read and execute `skills/bitbranding-fashion-shopify/workflows/03-fashion-product-card-optimizer.md`.

## Usage

```
/bb-product-card [current card URL or screenshot] vs [reference card]
```

## Pre-Flight

Load `skills/bitbranding-fashion-shopify/genius.md`, especially Pattern 6 (Product Card as 5-Component System) and the rubric.

## Inputs Required

1. Current product card (desktop + mobile screenshots OR live URL)
2. Reference card (premium brand benchmark)
3. Theme (Horizon / Dawn / Broadcast / paid)
4. App budget (free / one-app / multi-app)
5. Number of SKUs in catalog (affects variant siblings ROI)

## Output

5-component score (out of 10 each, composite /50). The ONE highest-leverage fix specified with exact lever path + time + expected score lift. Other 4 components ranked for later. Skip recommendations with explicit ROI reasoning. Mobile verification specific to the chosen fix.

## Key Heuristic

Don't optimize all 5 at once. Pick ONE component where current score is lowest AND fix is achievable AND it matches the brand profile. Frame everything else as "later."

## Pairs With

- `/bb-audit` — usually triggers this drill-in
- `Luke Iha` skill — write the product copy that goes IN the card
- `/bb-collection-content` — content layer wraps the card grid

**Execution prompts**: before producing the deliverable, check `skills/bitbranding-fashion-shopify/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).

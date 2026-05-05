---
description: Generate ad concepts as primary-emotion designs — the angle IS the emotion, not a feature pitch
---

# /vince-emotional-angle-engine

Read and execute the workflow at `skills/vince-nijhof-dtc-operator-system/workflows/05-emotional-angle-engine.md` — generates 10-20 ad concepts each engineered around ONE primary emotion, grounded in data bank quotes.

Load before execution:
- `skills/vince-nijhof-dtc-operator-system/genius.md`
- `skills/vince-nijhof-dtc-operator-system/references/emotional-angle-library.md`
- `skills/vince-nijhof-dtc-operator-system/references/data-bank-source-mining.md`

## Usage
```
/vince-emotional-angle-engine [brand + funnel stage + ICP + concept count target]
```

## When to use
- Need ad concepts for new campaign
- Existing ads feel feature-led — flat, generic
- Pivoting to new ICP segment
- Pre-launch concept generation for new SKU
- After data bank refresh

## Stacking
- Required upstream: `/vince-data-bank-build`
- Required downstream: `/vince-intent-first-launch` (kill committee)
- Pairs with: `/vince-vssl-ideation-pipeline` (high-volume VSSL pipeline)
- Pairs with: Luke Iha `vicious-hook-mastery` (hook craft layered on emotion)

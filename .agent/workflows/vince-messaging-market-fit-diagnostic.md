---
description: Diagnose brand-vs-customer language gap — the second-order scaling unlock after PMF
---

# /vince-messaging-market-fit-diagnostic

Read and execute the workflow at `skills/vince-nijhof-dtc-operator-system/workflows/02-messaging-market-fit-diagnostic.md` — find the gap between what your brand says and what your customers say, and close it.

Load before execution:
- `skills/vince-nijhof-dtc-operator-system/genius.md`
- `skills/vince-nijhof-dtc-operator-system/references/data-bank-source-mining.md`
- `skills/vince-nijhof-dtc-operator-system/references/emotional-angle-library.md`

## Usage
```
/vince-messaging-market-fit-diagnostic [brand + current ad copy + landing page]
```

## When to use
- PMF achieved but ad performance plateaued
- Brand expanding to new ICP segment
- Ads feel "from the brand" not "from the customer"
- Pre-launch when product is finalized but messaging untested

## Stacking
- Required upstream: `/vince-data-bank-build`
- Pairs with: `/vince-emotional-angle-engine` (downstream concept generation)
- Pairs with: Lara Acosta `8-word-rehook` (for short-form variations)
- Pairs with: Luke Iha `vicious-hooks` (for combative-tone variations)

**Execution prompts**: before producing the deliverable, check `skills/vince-nijhof-dtc-operator-system/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).

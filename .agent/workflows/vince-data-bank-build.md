---
description: Build customer voice data bank — systematic angle library mined from Trustpilot, Amazon, support tickets, competitor reviews
---

# /vince-data-bank-build

Read and execute the workflow at `skills/vince-nijhof-dtc-operator-system/workflows/01-data-bank-build.md` — the foundational customer voice extraction system underneath every other Vince Nijhof workflow.

Load before execution:
- `skills/vince-nijhof-dtc-operator-system/genius.md`
- `skills/vince-nijhof-dtc-operator-system/references/data-bank-source-mining.md`
- `skills/vince-nijhof-dtc-operator-system/references/emotional-angle-library.md`

## Usage
```
/vince-data-bank-build [brand name + review source URLs]
```

## When to use
- New brand onboarding
- Quarterly data bank refresh
- Brand has never systematically mined customer voice
- Pre-campaign angle generation
- Stale ad performance — angles feel invented

## Stacking
- Required upstream for: `/vince-messaging-market-fit-diagnostic`, `/vince-emotional-angle-engine`, `/vince-x-luke-data-driven-hooks`
- Refresh trigger: monthly cadence + pre-campaign + new product launch + post-data-event

**Execution prompts**: before producing the deliverable, check `skills/vince-nijhof-dtc-operator-system/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).

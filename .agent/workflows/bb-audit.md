---
description: BitBranding — Audit a clothing-brand collection page against a premium reference; produce 3-strategy breakdown with free-tier triage
---

# /bb-audit — Premium-Reference Collection Audit (BitBranding)

Read and execute `skills/bitbranding-fashion-shopify/workflows/01-premium-reference-collection-audit.md`.

## Usage

```
/bb-audit [brand collection URL] vs [premium reference URL]
```

## Pre-Flight

Load `skills/bitbranding-fashion-shopify/genius.md` for the 6 genius patterns, 5-component product card system, and quality rubric.

## Inputs Required

1. Brand's current collection page (URL or screenshots)
2. Premium reference (must be a real brand — Represent, Aimé Leon Dore, Stüssy, Fear of God, etc.)
3. Theme name (Horizon / Dawn / Broadcast / paid)
4. Budget tier (free-only / one-app-OK / paid-theme-OK)

## Output

3-strategy audit (visual hierarchy, product card system, collection content) with free-tier triage (🟢 / 🟡 / 🔴 per gap), top 3 fixes ranked by leverage, honest gaps with paid alternatives + free fallbacks, sequenced build order.

## Pairs With

- `/bb-rebuild` — execute the audit's recommendations
- `/bb-product-card` — drill deeper on Strategy 2 (card system)
- `/bb-collection-content` — drill deeper on Strategy 3 (content layer)

**Execution prompts**: before producing the deliverable, check `skills/bitbranding-fashion-shopify/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).

# Customer Truth Map — Agent Context

**Activated:** 2026-06-21

This agent owns the Customer Truth Map skill ([`skills/customer-truth-map/`](../../../skills/customer-truth-map/)) — the voice-of-customer / audience-truth layer.

## Composes (never reimplements)
- `/buyer-sourcer` — scaled, source-traced VoC mining (delegated by `/ctm-gather`)
- `/mcraney-deep-canvass` — surface map → belief/resistance depth (via `/ctm-deepen`)
- `consumer-posture` — identity / occupation / activity layer (via `/ctm-deepen`)

## Spine
Organize the customer's real words, never invent them. Verbatim Integrity is the veto — any fabricated or paraphrased quote is an automatic fail.

## Load order
1. `skills/customer-truth-map/genius.md` (IP anchor — patterns, hidden knowledge, moves, rubric)
2. The specific `/ctm-*` workflow in `skills/customer-truth-map/workflows/`

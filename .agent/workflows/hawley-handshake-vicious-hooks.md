---
description: "Stack: Noah Hawley's season architecture supplies the arc spine (theme stated first, ending locked before installment one, per-installment tonal position and escalation logic). Luke Iha's Vicious Hooks engine writes each installment's hook with knowledge of where it sits in that arc, so a content series opens every entry with a hook that can weaponize what earlier installments planted, and a finale that cashes the whole season's promise."
---

# /hawley-handshake-vicious-hooks

Read and execute the workflow at `skills/noah-hawley-storytelling-mastery/workflows/hawley-handshake-vicious-hooks.md` — Hawley supplies the season spine (theme, locked ending, per-installment tonal position, escalation logic) and the Plant Map of what each installment plants; Iha writes each installment's hook knowing its arc position, cashing earlier plants and setting up later ones.

Load before execution:
- `skills/noah-hawley-storytelling-mastery/genius.md` — theme-first breaking, ending-first architecture, tonal arc
- `skills/luke-iha-vicious-hooks/genius.md` — the 8 Vicious Hook Principles

## Usage
```
/hawley-handshake-vicious-hooks [series subject + audience + N installments/cadence + existing season bible if any]
```

## When to use
- A content series has real architecture (theme, locked ending, tonal positions) but every installment's open reads like a standalone post with no memory of the series
- Hooks were written installment-by-installment with no visibility into the rest of the arc, so stakes reset to zero every entry instead of compounding
- The finale needs to cash a promise the series has been building since the pilot, and the current draft opens it like every other entry

## Not This
Single-post hooks with no series context (no installment before or after to plant against) route to `/luke-iha-vicious-hooks` or `/vicious-hook` directly. Series architecture without hooks (opens aren't the bottleneck) routes to `/hawley-content-season` — build the season bible there, then bring it here.

## Stacking
- Upstream: `/hawley-content-season` (builds the season bible this workflow reads), `/hawley-tonal-arc` (deepens the tonal-arc compression in Step 1)
- Downstream: `/hook-viciousness-audit` (second-pass QA on the finished hook set, independent of arc position)
- Adjacent: `/luke-iha-vicious-hooks` / `/vicious-hook` — this crossing specializes it for series work with a Plant Map and No-Context Test neither alone provides

# Implementation Guide — Meg Heckman Buyer-Trigger OS

## Build Sequence (which workflow when)

```
NEW BRAND / NEW NICHE          EXISTING CATALOG               STORE LEAKING MONEY
/meg-sub-identity-map          /meg-trigger-audit             /meg-funnel-doctor
        ↓                              ↓                              ↓
/meg-concept-sprint            kills → /meg-concept-sprint    stage fix (or /meg-trigger-audit
        ↓                      leads → /meg-design-handoff     if all stages healthy)
/meg-trigger-audit                     ↓
        ↓                      /meg-listing-copy
/meg-listing-copy + /meg-design-handoff
        ↓
LAUNCH (smallest honest test) → /meg-factory-loop + metric instrumentation
```

**Or run the whole pipeline as one command: `/merch-os [brand]`** (phase-gated, resumable).

## Operating Rhythm (once live)

- Weekly: 6-metric review (`references/metric-thresholds.md`), kill/scale by pre-committed bands.
- Continuous: generate per `/meg-factory-loop` targets — the breakout might be design 312.
- 2-3×/week: email the list (pre-paid traffic).
- Per drop: `/meg-aov-architect` cohesion check before any upsell tooling.

## Stacking Order (non-negotiable)

**Meg first, execution second.** She decides WHAT will sell; downstream experts decide how it looks/ships/reads:
1. `/meg-*` verdict or concept →
2. Satori (composition) / Kittl (typography) / fantastic-posters (generation, cost-gated) →
3. BitBranding (Shopify build) →
4. writers-room (client-polish on copy) — optional.

Inverting this order produces beautiful decorations that sell nothing.

## Deployment Targets (live as of build)

| Target | Entry point | Context |
|---|---|---|
| Josh — swing-nerd shirts | `/meg-trigger-audit` on V1 re-score; `/merch-os` for V2 | `_active/josh-swing-nerd-shirts-v1/` (Bonfire, 3 candidates, trigger pass in production) |
| MyBPM — EDM streetwear | `/merch-os` full run | `_active/mybpm-merch-os-run-1/`, mybpm.store, PLUR culture, ~30 products |
| Client work | `/meg-trigger-audit` (productized audit) or `/merch-os` | 2-page deliverable cap per density rule |
| Non-merch surfaces | `/meg-trigger-transfer` | Offers, hooks, landing pages, positioning |

## Grounding Rules (always-on)

1. Her revenue figures: UNCONFIRMED, self-reported — never asserted as verified.
2. Her thresholds: calibration defaults (POD/Meta 2026) — recalibrate per category.
3. Vocabulary contract frozen: Identity Signal · Recognition Speed · Specificity · Social Currency · Familiar/Twist · Emotion First · Wearability · IP Safety (+ 50ms Clarity, Evergreen Index added at forge).
4. The joke is WITH the niche, never at the buyer.

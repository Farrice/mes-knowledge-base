---
description: "Phase 5 positioning + offers — turn an existing Customer Truth Map into 3–5 gap-aimed positioning angles and 3 offer extensions, each tied to the exact pain/wish it answers (simple vs major flagged), then hand off to BOS/positioning"
---

# /ctm-to-offer

Put the map to work: positioning & offers. Turn the underserved gaps into 3–5 sharp positioning angles — each with one sentence that makes a prospect feel understood — and 3 offer extensions, each tied to the exact pain/wish it answers and flagged simple vs major. Then hand off. Every angle aims at a specific gap.

## Trigger
`/ctm-to-offer`

## Workflow
`skills/customer-truth-map/workflows/ctm-to-offer.md`

## Quick Use
Provide a finished map + the ranked `/ctm-gaps` table + the `/ctm-jobs` list + the current offer. Runs prompt P9. The lead angle aims at one of the widest gaps.

## Pipeline
1 Draft 3–5 positioning angles, each aimed at a gap row, each with a "feel understood" sentence → 2 Suggest 3 offer extensions, each naming its pain/wish + Simple/Major effort flag → 3 Hand off (do not finish here)

## Output
The angle table (3–5 angles, each gap-anchored + traced "feel understood" line) + the offer-extension list (3, each pain/wish-anchored + honest effort flag) + the explicit handoff line. Does NOT build the finished Brand OS.

## Stacks With
→ finishing engines: `/build-bos` (full Brand OS), positioning skills (April Dunford-style, `oren-brand`, `daniel-priestley`), `offer-stack`, `design-digital-product-offer`
→ upstream `/ctm-gaps` (primary input) + `/ctm-jobs` · fact-verifier for market claims

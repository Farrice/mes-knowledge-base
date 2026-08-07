---
description: "/fladlien-terms — Diagnose why a viable or valuable offer asks too much buyer time, effort, routine change, money, or status and identity risk; run the 18-lever TERMS rebuild before package copy or acquisition when buyers do not adopt."
---

# /fladlien-terms

Public front door for Jason Fladlien’s TERMS offer diagnostic. The Revenue Offer Agent remains the function owner.

## Steps

1. Seat `.agent/workflows/revenue-offer-agent.md` as the controlling function owner. Do not recursively invoke this wrapper from inside its own run.
2. The Revenue Offer Agent establishes offer truth, preservation locks, market state, and the game verdict before delegation.
3. Read `skills/jason-fladlien-marketing/references/offer-terms.md`, then execute `skills/jason-fladlien-marketing/workflows/offer-terms-diagnostic-and-rebuild.md` as a bounded diagnostic component.
4. Invoke `skills/jason-fladlien-marketing/workflows/offer-adoption-and-proof-loop.md` only when the diagnostic names a valid trigger. Activate only supported submodules, and count every proposed module-level offer change inside the global three-change ceiling.
5. Treat diagnostic and internal-component decisions as recommendations. The Revenue Offer Agent separately accepts, offsets, rejects, or holds each recommendation, reassembles one coherent offer, and assigns the smallest honest `PRESERVE / PATCH / REBUILD / HOLD` label.
6. Return one Offer TERMS Rebuild Packet with the owner decision ledger, then run the public workflow’s Quality Gate.

## Boundaries

- Inspect all 18 levers; change no more than three offer decisions.
- Do not invent a nineteenth lever, buyer motive, proof, guarantee, scarcity, anchor, capacity, or demand.
- Do not hand off to copy or acquisition until `/revenue-offer-agent` accepts the rebuild.
- The diagnostic may recommend; only the Revenue Offer Agent may populate the final owner-decision fields.
- Framework coverage is not uplift by itself. If the owner and TERMS converge on the same accepted changes, prefer the narrower change class and report comparative value as unproven.
- Keep component validity, cold-start portability, and `sent / held / sold / collected` separate.

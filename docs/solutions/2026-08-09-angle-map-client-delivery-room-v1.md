# Solution Card — Dual-edition Angle Map client delivery room

**Date:** 2026-08-09 · **Domain:** client delivery / Briefing Room · **Status:** SOLVED V1

## Problem

A branded portable Briefing Room existed, but the process still began too late.
It could package an authored brief without controlling whether the intake was
complete, whether confidential handling was literal, whether private reasoning
had been transformed into client prose, or whether a human had approved the
release. That left future client work vulnerable to ad hoc folders, accidental
internal-language leakage, and polished outputs built on missing evidence.

## Solution

Build one owner-led delivery spine:

1. Initialize a guarded project with intake, source inventory, private brief,
   client brief, and release gate.
2. Use the current Angle Map offer boundary and evidence-first GTM workflows to
   author the private decision record.
3. Treat the client brief as a separate editorial transformation.
4. Allow a working-only build while release is held.
5. Block the client ZIP until five reviews, permission, reviewer identity,
   outward-language scan, path scan, brand scan, and portable verification pass.
6. Ship both folders, both ZIPs, and a hash-backed release receipt.

The executable owner is `execution/client_delivery_room.py`. The workflow is
`.agent/workflows/client-delivery-room.md`; the semantic contract is
`semantic_libraries/antigravity/primitives/client-delivery-room-contract.md`.

## Proof

- Fourteen unit and regression tests pass.
- Cold-start fixture builds both editions.
- Intentional client-facing implementation leakage is rejected.
- A release gate on `HOLD` still permits a private working build but blocks the
  client ZIP.
- Both folders and both ZIPs pass manifest, hash, local-link, and portable-path
  verification.
- Premium Minimal brand tokens and identity are present.
- Desktop visual review passed.
- At 390px, the final layout probe reported a 390px document width and every
  measured surface ending at 374px or earlier.

## Reuse

```bash
python3 execution/client_delivery_room.py init --project-dir <path> --client "<name>"
python3 execution/client_delivery_room.py check <project-dir>
python3 execution/client_delivery_room.py build <project-dir> --output <new-release-dir>
python3 execution/client_delivery_room.py verify <release-dir>
```

Run the V1 for three real Angle Map engagements before adding a hosted portal,
white-labeling, connectors, client accounts, other offers, or automatic source
ingestion.

## Boundary

The system proves fulfillment mechanics and release safety. It does not prove
the proposed segment, problem, message, buyer willingness to pay, campaign
performance, or market fit. Confidential client activation remains `HOLD`
until the current Angle Map handling procedure contains tested literal values.

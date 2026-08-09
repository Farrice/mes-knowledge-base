---
description: Turn an Angle Map intake and permissioned source pack into a private working room and a separate verified Premium Minimal client handoff
---

# /client-delivery-room — Angle Map Client Delivery V1

## Outcome

Build one private production record and one intentionally curated client room
for The Angle Map + Message-Market-Fit Intelligence. Never derive outward
permission from the existence of an internal brief.

Canonical contract:
`semantic_libraries/antigravity/primitives/client-delivery-room-contract.md`

## Commands

```bash
python3 execution/client_delivery_room.py init --project-dir <path> --client "<name>"
python3 execution/client_delivery_room.py check <project-dir>
python3 execution/client_delivery_room.py build <project-dir> --output <new-release-dir>
python3 execution/client_delivery_room.py verify <release-dir>
```

Use `build --working-only` before outward prose is approved. A normal build
requires every release gate and produces both ZIPs.

## Step 1 — Intake And Readiness

1. Use `templates/client-delivery-room/intake-form.md`.
2. Receive files only through the client-approved channel.
3. Record every source in `source-inventory.json` with evidence type,
   visibility, permission, date, and limitation.
4. Run `check`. Do not improvise around a `HOLD`.
5. Conduct one 45–60 minute kickoff. Use the form for facts; use the call to
   surface the unstated decision, contradictions, failed alternatives, claim
   boundaries, and what the final decision-maker must believe.

## Step 2 — Private Working Room

Load:

- `skills/jordan-crawford-gtm-intelligence/SKILL.md`
- `workflows/customer-truth-dossier.md`
- `workflows/problem-qualified-segment.md`
- `workflows/message-market-fit-test.md`
- the current Angle Map Activation Packet and Confidential Input Procedure

Produce, in order:

1. Source inventory and atomic evidence ledger.
2. Customer Truth Dossier with conflicts and unknowns.
3. `QUALIFIED`, `PROVISIONAL`, or `REJECTED` PQS.
4. Three campaign angles tied to the occasion, buyer belief, approved proof,
   and claim boundary.
5. One lead-angle recommendation.
6. One frozen message-market-fit test with commercial counters and no-send
   permission state.
7. Private brief JSON following the Briefing Room schema.

The private room may expose uncertainty, candid reasoning, local source paths,
and internal language. It is never the client handoff.

## Step 3 — Editorial And Privacy Firewall

Create the client brief as a transformation, not a copy:

- translate evidence into client-relevant decisions
- preserve proof-state labels and unknowns
- remove internal tools, experts, prompts, paths, costs, branch language, and
  system scaffolding
- omit raw private records and unrelated evidence
- include only client-approved or public sources
- keep one lead recommendation and one next decision
- write naturally in Farrice Cain Premium Minimal report language

Complete `release-gate.json`. The operator must sign every gate.

## Step 4 — Build And Verify

A successful normal build produces:

```text
<release-dir>/
  private-working-room/
  private-working-room.zip
  client-room/
  client-room.zip
  release-receipt.json
```

Run `verify` on the release directory. Then inspect the client room at desktop
and mobile widths before sending. Hash integrity proves the files were not
altered; it does not prove strategic truth.

## Quality Bar

- The client can understand the decision in under two minutes.
- Every recommendation is traceable to supplied or public evidence.
- A provisional customer pattern remains visibly provisional.
- The three angles differ in buyer belief, not adjectives.
- The lead recommendation names what to build first and what not to combine.
- The test measures qualification, value, language, and commercial outcomes
  separately.
- No client-facing file contains a local path or internal harness language.
- Both folders and both ZIPs pass the bundled verifier.

## Handoff And Learning Return

After delivery, record only real events: delivered, opened if observable,
clarification requested, revision requested, decision changed, asset built,
paid expansion, or reported outcome. Return those events to the private
dossier. Do not label client praise or room completion as market proof.

## Park Rule

Run this V1 three times before adding other offers, a hosted portal,
white-labeling, login accounts, automatic connector ingestion, or client-side
editing. Expansion without three delivery receipts is parked.

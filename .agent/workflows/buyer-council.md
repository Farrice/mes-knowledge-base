---
description: "Front door — convene a simulated buyer/customer panel against any artifact (idea, concept, offer, content, GTM plan) for predictive-marketing verdicts; two modes — TRIAGE (Mike Taylor, ~5 min, joint-anonymous synthesis) for fast directional calls, COUNCIL (Haynes×Woods handshake, dissent-preserved) for stakes"
---

# /buyer-council

Load first: `skills/geoff-woods-ai-thought-partner/SKILL.md` (Tier 3 entry) + `skills/geoff-woods-ai-thought-partner/genius.md` (Pattern 6 — Stakeholder Simulation with Reality Calibration).

Then read and execute `skills/geoff-woods-ai-thought-partner/workflows/17-buyer-council.md` — mode split first (TRIAGE: 10 cold personas, individual answers, joint-anonymous synthesis, ~5 min; COUNCIL: full pipeline below), then for COUNCIL: panel assembly (standing roster in `councils/buyers/` first, fresh-build only if no fit), simulation pass (first-15-seconds reaction, verbatim strongest objection, what flips them, per-element KILL/REVISE/SHIP), dissent preserved never averaged, mandatory NO-FIT seat + economic-gatekeeper seat, Buyer Council Verdict Sheet + Predicted Response Map + ranked revisions, and the `councils/buyers/calibration.jsonl` reality-calibration append.

## Usage
```
/buyer-council [artifact] --panel [roster file in councils/buyers/, or "build"] --question [the decision question]
```

## When to use
- Any idea, concept, offer, content piece, or GTM plan needs a predicted BUYER reaction before it ships — not an expert critique, a simulated customer's reaction
- A standing buyer panel already exists in `councils/buyers/` and this artifact should be run against it
- No panel exists yet for this audience and one needs to be built fresh

## Not This
- Expert-side councils (multi-expert strategy debate) → `/convene`
- Cold-offer-stack-specific stress test with objection-inventory intake → `/haynes-handshake-geoff-stakeholder` (the specialization; this is the general case)
- A known internal stakeholder/room pre-test (board, exec team) → `07-simulate-room.md` directly

## Stacking
- Sibling: `skills/jeremy-haynes-cold-offer/workflows/haynes-handshake-geoff-stakeholder.md`
- Deep-seat options: `mcclain-persona-forge`, `icp-deep-canvasser`
- Escalation: `/convene` if the buyer panel surfaces a strategy question rather than a buyer-reaction question

**Execution prompts**: before producing the deliverable, check `skills/geoff-woods-ai-thought-partner/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).

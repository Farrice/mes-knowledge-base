---
name: absence-claims-as-load-bearing-premises
problem_signature: "a strategy or mission brief inherits an ABSENCE claim ('no one does X', 'zero public proof exists') from an earlier research pass and builds its recommendation on it"
domain: strategy
tags: [research, verification, swarm, premise-risk, absence-claims]
date: 2026-07-07
status: active
session: swarm-apex-session-1
---

## Problem
The morning research swarm reported "no public evidence shows compliance-first agencies winning funded-brand deals" — an absence claim from one search sweep. Four hours later it was pasted into a heavy-swarm mission brief as a stated fact, and 8 expert takes plus the aggregate built the market-wedge strategy on it. Absence claims are the most fragile claim class: they encode "my sweep didn't find it," not "it doesn't exist."

## Root Cause
A single research pass can only prove presence, never absence. The original report even carried the honest hedge ("VERIFIED as an absence, per the worker's explicit check" + a solo-operators-may-be-SEO-invisible caveat), but the hedge evaporated when the finding was compressed into a downstream mission brief — compression strips epistemics first.

## Approach That Worked
1. Pipe every load-bearing premise into the mission's adversarial verify phase alongside the new claims — premises inherited from prior missions get NO trust carry-over.
2. When a premise is an absence claim, the verifier's job is one existence proof: search specifically for counterexamples (found: Hedy & Hopp, 1nessAgency public case studies with named results).
3. On refutation, correct the strategy IN the deliverable with a visible "Corrected framing (verification changed this)" block — narrow the claim to what survives (here: "generic case studies are retrospective; a redline of the prospect's OWN copy is proof-about-THEM") instead of deleting the thesis.
4. Log the refutation in the claim ledger with its effect on the answer, so the correction is auditable.

## Dead Ends
- Trusting "VERIFIED as an absence" labels across mission boundaries — the label was honest in context and wrong as a portable fact.
- Treating premise verification as optional because "we already researched this today."

## Verification
Heavy run wf_b82d1762-70f (receipt `2026-07-07T184806Z0000-swarm-heavy.md`): claim #1 REFUTED with source URLs, answer corrected in place, Day-1 competitor spot-check added to the build plan. Deliverable: `strategy_briefs/2026-07-07-path-a-proof-of-work-heavy.md` §Corrected framing + claim ledger row 1.

## Weaker-Model Trap
A mid-tier model treats an upstream report's labels as settled truth and optimizes the downstream deliverable's polish instead of re-testing its premises — it will confidently build on "zero proof exists" because questioning the brief feels out of scope. Tell it explicitly: premises are claims; absence claims are the first thing to re-verify.

## Pointers
- `strategy_briefs/2026-07-07-path-a-proof-of-work-heavy.md` (claim ledger row 1)
- `research_outputs/2026-07-07-claim-safe-content-landscape.md` (§2.4 — the original hedged absence finding)
- `.agent/workflows/swarm-heavy.workflow.js` (Verify phase)

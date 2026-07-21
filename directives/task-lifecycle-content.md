---
description: The Chain's produce→verify→finalize steps as a numbered, capped task lifecycle (Ray Amjad grammar, 2026-07-21)
---

# Task Lifecycle — Content Deliverables

> The Chain's Steps 4-6 as one numbered, capped lifecycle. Grammar from `skills/ray-amjad-agentic-ladder/` (subagent stages, capped loops, environment escape hatch, artifact receipts). This file is the shared spine that CLAUDE.md Step 5.5, `quality_gate.md` (Verdict Routing), and `verification-agent-protocol.md` point into: one lifecycle, not three overlapping rules. Ships in **observe register**: it documents what fires; enforcement stays with the existing observe-mode ledger (`LEDGER_ENFORCE` / `VERIFY_ENFORCE`) until Farrice flips it.

Input: Scored intent (Chain Steps 0-3 done: posture, score, route, load)

1. **Produce in the expert frame.** Expert context loaded at the Context Engine tier the task warrants. Never produce expert-domain output without the expert loaded.

2. **Slop check (deterministic).** `python3 execution/prose_classifier.py check <file>` on the draft. Fails → one rewrite of the flagged sections, re-check. Cap: 1.

3. **Verify in an ISOLATED subagent** (fact-bearing deliverables; the Step 5.5 activation table in `verification-agent-protocol.md` decides). Dispatch via the Agent tool with a fresh brief per `directives/sub_agent_protocol.md`. Never `.claude/agents/` files, never the producing context verifying itself (smarter models cheat better; isolation lets the verifier say "this claim doesn't hold" without inheriting the producer's optimism). Return contract: claim inventory with VERIFIED/LIKELY/UNCONFIRMED labels + verdict PASS/FAIL/PARTIAL.

4. **Route the findings** (house vocabulary, per `quality_gate.md` § Verdict Routing):
   - **VERIFIED-issue** (the verifier confirmed a defect) → one revision pass, then re-verify the touched claims. Cap: 1 (rides the existing "retry weakest section once" rule; no new loop).
   - **LIKELY / UNCONFIRMED-issue** → never auto-fixed. Delivery carries a one-line why-it-matters note per item so Farrice decides with context.

5. **Finalize with the receipt.** `chain_runner.py finalize … --receipt "<what was verified, on which surface, by what instrument, with counts>"`. The receipt satisfies Step 1.5's verification accountability; a fact-bearing finalize without one still logs a miss to `evolution_store/verification_misses.jsonl`.

6. **Environment escape hatch.** If verification is impossible (source unreachable, no access, no instrument), deliver with the gap NAMED in the delivery and `Verification: N/A (<gap>)` in notes. Never fake a receipt; never silently retry an environment failure.

Output: Deliverable + verification receipt + finalize entry

## Trust path (Ray's hidden knowledge: how this graduates)

Run the lifecycle consciously for 2-3 deliverables, refine steps that misfire, THEN consider flipping `VERIFY_ENFORCE=1`. Autonomy is earned per-loop, never granted by optimism. When a step gets skipped manually twice, that's a mechanism gap. Fix the lifecycle, not the session.

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-08-20 |

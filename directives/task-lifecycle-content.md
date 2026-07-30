---
description: The Chain's produce→verify→finalize steps as a numbered, capped task lifecycle (Ray Amjad grammar, 2026-07-21)
---

# Task Lifecycle — Content Deliverables

> The Chain's Steps 4-6 as one numbered, capped lifecycle. Grammar from `skills/ray-amjad-agentic-ladder/` (subagent stages, capped loops, environment escape hatch, artifact receipts). This file is the shared spine that CLAUDE.md Step 5.5, `quality_gate.md` (Verdict Routing), and `verification-agent-protocol.md` point into: one lifecycle, not three overlapping rules. Ships in **observe register**: it documents what fires; enforcement stays with the existing observe-mode ledger (`LEDGER_ENFORCE` / `VERIFY_ENFORCE`) until Farrice flips it.

Input: Scored intent (Chain Steps 0-3 done: posture, score, route, load)

1. **Produce in the expert frame.** Expert context loaded at the Context Engine tier the task warrants. Never produce expert-domain output without the expert loaded.

2. **Slop check (deterministic).** `python3 execution/prose_classifier.py check <file>` on the draft. Fails → one rewrite of the flagged sections, re-check. Cap: 1.

2.5. **Reader Contract (judgment, Farrice 2026-07-22 — three felt verdicts from the Week-1 launch posts, banked in the taste ledger).** Before verification, answer three yes/no questions about the draft; any "no" → one revision pass (rides the same cap discipline):
   - **Payoff**: does the reader leave with a usable move, or only with my story? Vulnerability without a reader payoff reads as a journal entry ("sorry for myself at the end" vs "the reader is better off for reading").
   - **Pull**: is there an open loop that closes late, and real beat variety? One emotional note held too long = the reader finishes out of politeness, not compulsion.
   - **Recognition**: does at least one line say the reader's private sentence better than they'd say it — a lived-in SPECIFIC detail carrying a UNIVERSAL feeling? Generic is dead; specific-but-unrelatable is equally dead. The mirror line is the unit of landing.

   **Bayer Mirror Mode (Farrice 2026-07-22, felt 10/10 on live A/B — the deep-topic body voice):** for spiritual / life-design / deep-insight content, the body author is `david-bayer-elite-communication` writing in **recognition-you** — the reader's inner world articulated back so they feel seen, never talked at ("universally relatable and agnostic, but spoken to by a friend"). Farrice's "I" gets ONE touch, never the spine: a single short credibility receipt right after the cold open ("I've done it four times myself") — and that is ALL (his final edit, same day: the ownership close and every additional touch "made the rest worse"; the expert's flow and close stay verbatim). Setup phrases ("watch what happens") are banned tells — the piece goes straight in. The controlled A/B (bayer-voice-test, 2026-07-22): identical architecture, the I-spine version read as "a journal entry" to Farrice himself; the mirror version felt 10/10. **Content-class taxonomy**: receipts/launch/story posts keep the I-narrative spine (Week-1 8.5s); deep-topic insight posts run Bayer Mirror. Charisma textures (Rock/Reynolds) are RETIRED for writing — in-person registers only.

   **Optional line-layer (Farrice 2026-07-22 — compose freely, never a forced step):** when delivery feels long-winded or abstract-Latinate ("outcome with no edges" mush), run the rhetoric pass on the flagged lines only: `/ward-saxon-punch` (Latinate setup → stony Saxon landing; decide the last word first) + `/ward-cadence-audit`; Forsyth (`mark-forsyth-rhetoric`) and the full `/how-i-write` composition (ONE body author from the ten How-I-Write experts, then `/voice-over` for Farrice's voice on top) are the deeper gears. Restraint law from the Farnsworth genius: one well-placed device beats five; if the reader notices the technique, it failed. Proof-of-concept: the Week-1 v4 pass, 7 surgical changes, gates clean.

3. **Ground factual claims in the producing context** (amnesty 2026-07-29 — contradiction C4 resolved in favor of the dialect law, Farrice-ratified: self-verification is native to the Claude 5 family; added verify-subagents are the over-verification failure mode). Label VERIFIED/LIKELY/UNCONFIRMED before delivery. Fresh-context reviewers fire in exactly two cases: Farrice asks, or the producing context is compromised (`CLAUDE.md` Step 5.5). When one does fire: Agent tool, fresh brief, never `.claude/agents/` files. Return contract: claim inventory with labels + verdict PASS/FAIL/PARTIAL.

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

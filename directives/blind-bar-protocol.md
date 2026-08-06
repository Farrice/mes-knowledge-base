---
description: "Blind Bar — falsifiable reference-anchored quality floor for deliverables (gauntlet-loop extraction, Farrice-approved 2026-08-05)"
---

# Blind Bar Protocol

**Goal**: Farrice's taste enters at a high baseline instead of QA-ing low-bar output. The producing loop proves a deliverable against a NAMED reference artifact before he sees it — so his verdicts spend on direction, not on floor defects.

**Scar (why this shape and no other)**: (1) 2026-05-02 — 12 paired critic-subagents killed for cause: critics judging *unanchored* quality produce generic critique, worse output, latency (`no-claude-code-subagents.md`). (2) C4 amnesty 2026-07-29 — verify-subagents are the over-verification failure mode; 333k tokens burned on one-line asks. (3) KetoneIQ edge (gauntlet-loop source video, 2026-08): a quality loop with no ground truth "optimizes toward the wrong thing" — polished and off-brief. (4) 2026-07-16 rubber-stamp — self-graded blind-pass looks identical to a real pass in every ledger. The Blind Bar exists because the *falsifiable-reference* mechanic survives all four scars; a critic fleet survives none.

**Source**: `knowledge/synthesis/gauntlet-loop-blind-bar-mechanism.md` (Shumer gauntlet-loop, decoded 2026-08-05). Approved by Farrice 2026-08-05: bar clause in briefs + blind bar on content/copy + Jen listing trial.

## The mechanic (in-context, never a subagent)

1. **Bar-as-artifact.** The brief names the reference the deliverable must survive: a golden ref, a rubric anchor's worked example, a register/voice exemplar, a real photo set. Adjectives orient; only the named artifact decides. *"Nothing else counts as done."* No named artifact available → the Blind Bar is N/A (say so); do NOT improvise a reference.
2. **Blind side-by-side.** In the producing context, set the deliverable next to the reference in reading order that hides which is which where format allows. Ask the falsifiable question: *which of these clears the bar / which is the exemplar?* If the deliverable is instantly distinguishable as the weaker piece, it FAILS the pass.
3. **Single-biggest-gap repair.** A FAIL names ONE gap — the biggest — and repairs exactly that. Never a critique essay, never a rewrite-from-scratch.
4. **Hard cap: 2 rounds.** Two fails on the same artifact = stop repairing and deliver WITH the gap named (mirror of the spiral brake: the input is wrong, not the polish). The bar is a floor-raiser, not a loop.
5. **Compass**: the Blind Bar nudges and repairs; it NEVER blocks delivery and never asks Farrice a mid-run question. Only the cost gate and factual veto block.

## Bar clause grammar (for every production/dispatch brief)

Every brief that produces a taste-bearing deliverable carries a one-line Bar clause:

> **Bar**: `<named reference artifact — path or exact exemplar>`. Nothing else counts as done.

Task / Build Method / **Bar** — the third line the gauntlet grammar got right. A brief whose Bar is adjectives ("high quality," "on-brand") has no bar; name the artifact or mark Bar: none (and skip the pass).

## Cost discipline (Farrice, 2026-08-05: "not burning through tokens recklessly")

- **Deterministic first, always**: `prose_classifier.py` / `voice_evaluator.py` / lints run before any model-judged pass — they are free and catch the cheap failures.
- **In-context only.** The pass is one structured reasoning step in the producing loop: ~5–15k tokens. Zero subagents, zero fresh contexts, zero fleets. Fresh-context reviewers remain governed by the existing law (Farrice asks / compromised context).
- **Fires only on**: taste-bearing deliverables headed to Farrice or a client (content, copy, client packages) that HAVE a named reference. Never on: answers, diagnostics, system work, corrections, drafts he asked to see raw, or anything without a real Bar artifact.
- **The full gauntlet** (worker+critic agent pairs, hours-long loops) is reserved for screenshot-verifiable builds on Farrice's explicit ask only — it is a spend decision, his to make, every time.
- **Receipt**: finalize notes carry `BlindBar: PASS|FAIL(gap: …)|N/A(no ref) — <n> rounds`. No silent passes; a skipped bar is written N/A, never implied.

## Where it's wired (2026-08-05)

- `directives/task-lifecycle-content.md` step 2.7 — content/copy deliverables.
- `skills/jen-santulan-listing-content/workflows/listing-package.md` Phase 6 — trial surface (golden refs: 6853 Willis + `knowledge/expert-benchmarks/jen-listing-content/`).
- Trust path: run consciously for 2–3 deliverables, refine, then judge whether it earns more surfaces. Extend by Farrice's decision, never by drift.

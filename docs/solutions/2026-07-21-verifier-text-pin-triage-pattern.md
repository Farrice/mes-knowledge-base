---
date: 2026-07-21
session: verifier-fleet triage
name: verifier-text-pin-triage-pattern
problem_class: harness / verifiers / stale text pins
domain: harness
status: proven
problem_signature: "a large batch of fleet verifiers goes red at once and most of them pinned exact prose sentences inside living docs that were deliberately rewritten — the behavior they guard still works but the pin died, and some assert schemes that were never committed at all"
tags: [verifiers, fleet, triage, pinning, health, archive]
---
# Verifier fleet triage — text-pin contracts rot against living docs; pin behaviors on stable anchors

**Date**: 2026-07-21 · **Session**: verifier-fleet triage (30 failing → 16 fixed, 14 proposed-archive) · **Domain**: system / verification

## Problem

30/86 fleet verifiers failing. Root-cause distribution after full triage:
- **~40% stale text-pins**: verifiers asserted exact prose sentences ("go with your verdict", "Composed Draft") in living docs (autopilot.md, primitives, GEMINI.md) that were deliberately rewritten (Apex waves, codex-coequal Phase 5, 765e9db12 install). The guarded *behavior* survived under new wording; the pin died.
- **~35% fork-residue contracts**: verifiers asserting Codex-fork schemes never committed to canon (`.agents/cold-skills/` had ZERO git history; farrice-content-os state home; 17-agent arsenal) — some asserting the exact inverse of the live scheme.
- **~15% half-install regressions**: the control-plane restore installed verifiers whose system half never landed (protocol_tracker lifecycle fields, vibe-tax router files) — the verifier was RIGHT; restore the system, don't touch the verifier.
- **~10% genuinely stale artifacts** with working generators (candidates snapshot) or real API drift (log_misroute signature change crashing closeout misroute capture).

## Solution (the triage grammar)

Per failing verifier, in order:
1. **git log the pinned target first** — deliberate rewrite vs accidental loss decides everything. Zero git history on the required path = fork residue → propose-archive.
2. **Behavior survives, wording changed** → repin to STABLE anchors: section headings (`## Steering Rule`), script paths, route names — never prose sentences (they line-wrap and get re-worded). Rank-1 routing pins → top-3 (a learning router with 2,300+ commands legitimately reorders).
3. **Verifier right, system regressed** → fix the SYSTEM (restore from harvest, align the API caller); never weaken the check.
4. **Dead scheme / completed one-off** → propose-archive via `.agent/health/pending-review.md` (propose-only; nothing executes without Farrice's yes). Check the existing ledger FIRST — 10 of our 30 already had proposals from 07-15.
5. Prove exit 0 after every fix; a fixed verifier that still delegates to a failing sibling stays red honestly.

## Re-solve guard

Before writing any new verifier: pin section headings/paths/route names, not sentences; use top-N not rank-1 for router checks; and record in the verifier a comment naming WHAT BEHAVIOR the pin guards, so the next rewrite can re-anchor instead of archiving. Before triaging fleet failures: read `.agent/health/pending-review.md` and `.agent/workflows/system-audit.md` "Deferred verifiers" — some red is expected-by-decision.

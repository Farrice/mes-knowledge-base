---
thread: harness-apex
status: ready
resume_hint: Wave 3 head-to-head: strike archetype on native Workflow engine vs prose-JCC, same brief, claim_audit-scored
unfinished: Waves 3-5 + 16 revenue check-ins + blind-pass corpus backfill + 3-morning World Pulse observation
branch: main
pin: true
---

# Harness Apex — Waves 0-2 Shipped (Verifier Layer + Routing Spine + World Pulse)

**Date:** 2026-07-09 · **Commit:** `e2fe22d4b` (pushed to origin/main, tree clean) · **Thread:** `harness-apex`

## Where things stand

The Harness Apex Plan (`_active/harness/harness-apex-2026-07-07/PLAN.md`) is approved and merged with Swarm Apex (`_active/harness/swarm-apex-2026-07-07/PLAN.md`). Core thesis: quality-defining mechanics lived in prose only frontier models execute reliably; move every load-bearing judgment into runnable verifiers, schema contracts, or mid-tier calibration blocks. **Waves 0, 1, 2 are SHIPPED and committed.** Waves 3-5 queued.

### Shipped this session (verify by running, not re-reading)
- **Wave 0:** `execution/world_brief.py` + `.agent/cos/interests.json` → World Pulse section in the COS morning brief (Tavily $0 floor; perplexity-research cost-gate approval still PENDING Farrice). Question engine v2 in `execution/cos_prep.py` (3 archetypes, specificity-anchored, no repeats).
- **Wave 1:** BINDINGS consulted upstream (`routing_enforcer.match_bindings` → `[BINDING]` pins in `workflow_router.py` + `skill_router_hook.py`), stopword fix, finalize-composite→routing-weight learning (±0.05, cursor `.agent/routing-quality-cursor.json`), abstention escalation. Binding pins yield to active control-plane governance by design.
- **Wave 2:** `execution/claim_audit.py` (untagged-claim net; exit 1 on fail), `execution/anchor_verify.py` (propagation score 1-10, explainable), `execution/gates.py` (autopilot G1-G3 one command; 12+fallback outcome classes), `execution/blind_pass.py` (corpus-gated ritual, eval_set auto-append), `skill_auditor.py` 6 heartbeat checks now tier-gating (8 skills capped A→B on first audit), `chain_runner.py` latches: any dim ≥8 requires `--anchor-named "<phrase>"`; `--type Extraction` requires a blind-pass verdict or logged `--skip-blind-pass`. Wired into jw-engine P4, supercomputer P3, autopilot, extract/extract-forge QC.
- **Solved:** the "7.25 flattening" = intended `taste_signature.py` Rule 2 (unanchored ≥8 → 7.25, below the 7.5 PASS floor). Card: `docs/solutions/2026-07-07-anchor-named-score-flattening.md`. Anchored finalizes preserve scores (verified 9/9/8 → 8.67).
- **Personal:** JJ Playbook at `.agent/cos/jj-playbook.md` (private, gitignored). COS daily done for 07-07; a NEW brief with 5 questions is waiting (`/cos`).

## Next session priorities (in order)

1. **Wave 3 head-to-head pilot** — author the `strike` mission archetype as a native Workflow-engine script (schema-validated stage contracts; model on `collective-genius-council.workflow.js`, the repo's only real parallel surface) and race it against prose-JCC (`~/.claude/plugins/installed/jarvis-command-center/`) on the SAME mission brief. Score: synthesis completeness, fabrication count (use `claim_audit.py`), wall-clock, operator burden. Evidence decides migration. Design constraints in Swarm Apex PLAN §Session 1 + "Binding Constraints" (12-worker cap, 4-field envelope, no new hubs, never pin Opus).
2. **16 revenue check-ins** — `python3 execution/revenue_tracker.py checkin`. Post-Wave-1 these train routing weights nightly; highest ROI-per-minute in the system.
3. **Blind-pass corpus backfill** — `python3 execution/blind_pass.py prepare --expert <slug>` against top A-tier extractions (start: ben-watkins-storytelling, corpus 0/2) and collect the reference pieces each names.
4. Observe 3 mornings of World Pulse briefs; if thin, Farrice may approve the perplexity-research gate.

## Known issues / watch-fors

- Post-finalize binding check false-fires when a bound surface's NAME appears in a finalize *description* (e.g. "supercomputer" in a system-audit finalize about supercomputer files). Advisory-only; Wave 1 refinement candidate.
- claim_audit "first"-superlative pattern is its noisiest carrier; anchor_verify counts structural headings as terms (use `--terms` to override).
- World Pulse "why it matters" lines are template-rotated (2 variants/interest) — upgrade path: model-rewrite against article content.
- Parallel builders: apply `docs/solutions/2026-07-07-parallel-builders-stale-contracts.md` (shared contracts up front + end-of-task counterpart probe).

## Suggested skills

- `/resume harness-apex` — surfaces this handoff and thread state first.
- `/cos` — 5-question daily brief is pending; run before deep work.
- `/go "<messy intent>"` — compiles intent → run packet → conductor; used successfully this session.
- `/system-audit` — owner lane for Wave 3 build work (control-plane hook will route here anyway).
- `/swarm` — heavy/research patterns live; use for the pilot's mission brief if it needs multi-expert input.
- Skill tool `code-review` after the Wave 3 workflow script is authored.

## Core context to load (only if needed beyond this doc)

- `_active/harness/harness-apex-2026-07-07/PLAN.md` (status header + Waves 3-5)
- `_active/harness/swarm-apex-2026-07-07/PLAN.md` (Session 1 spec + Binding Constraints)
- `.agent/run-receipts/2026-07-10T00*` (Wave 2 receipts with fixture evidence)

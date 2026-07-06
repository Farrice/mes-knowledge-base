---
thread: harness-frontier-loops
status: ready
resume_hint: Maiden runs: /go then /create, then revenue checkin + memory_review
unfinished: Validation only: /go + /create + linkedin-daily v2 + writers-room maiden runs; weekly-closeout Sunday; embed flag after report card; stash review
branch: main
pin: true
---

# Antigravity Harness — Frontier Session (7 Missions: Router Learns + /go + Doctrine)

**Date:** 2026-07-06 · **Branch:** all merged + pushed to `origin/main` (`d424b2066`) · **Driver:** Claude Fable 5 orchestrating ~20 Sonnet subagents (last full-capability Fable session)

## What the next session is for

**Validate in production, don't build.** Every mission shipped, verified by execution, committed, and pushed. The system's constraint is no longer capability — it's unproven-in-live-use paths. Next session = maiden runs + human-gate clearing.

## Immediate priorities (in order)

1. **Maiden run of `/go "<messy thought>"`** — the anti-bottleneck front door (`.agent/workflows/go.md`). First live run of the intent-compile → route → conduct → 3-Next-Prompts loop. Correct anything awkward; the design contract is: written assumptions, max ONE question round.
2. **Maiden run of `/create`** — universal content conductor (`.agent/workflows/create.md`). Verify Stage 2 (live zeitgeist: recall + perplexity + research.py) actually fires with receipts.
3. **`python3 execution/revenue_tracker.py checkin`** — interactive walk of 11 overdue + 19 never-logged outcomes. Then first-ever `/weekly-closeout` (Sunday).
4. **`python3 execution/memory_review.py`** — 9 distilled memories pending, oldest 36+ days (queue alarm now fires in daily harvest log past 14d).
5. **Validate the 07-01 rewrites** — `/linkedin-daily` v2 and `/writers-room` have zero runs since rewrite. One run each.
6. **After ~1 week:** read `.agent/router-report-card.md`; if loop alive + weights sane → `export SKILL_ROUTER_EMBED=1` (hybrid retrieval benchmarked +6pts top-3, p95 +600ms, built flag-off).
7. **Stash review:** `stash@{0}` (57 files: creative_router/workflow_router edits, satori WIP) + `stash@{1}` (6 files: jason-fladlien skill edits) — apply-or-drop deliberately.

## What shipped (reference, not re-read — it's all in these files)

- **Doctrine:** `directives/peak-operation.md` — LOAD THIS when orchestrating anything multi-step. Operating shape, outcome→engine routing table, drift signals, invariants.
- **Craft standard:** `directives/skill-craft-standard.md` — REQUIRED checklist at every extraction gate (wired into extract/extract-forge/MES-3.0). Pattern density > length; Heartbeat Test; earned scores.
- **Codex parity:** `docs/CODEX-PARITY-2026-07-06.md` — Codex ran it, 22 surgical commits, verified clean both sides.
- **Session memory:** auto-memory `project_harness-frontier-loops.md` holds the full 7-mission record with root causes.
- Key new machinery: router feedback loop (`routing-intelligence.json` + `.agent/skill-weights.json` nightly), `execution/thought_bank.py` (+ /dump delegation + nightly episodic backstop), `execution/claim_risk_scan.py` (auto-fires in finalize Step 2.6), `skills/claim-safe-health-marketing/` (B-tier; A-tier pends Farrice judging real Path-A client copy), COS brief now shows Outer Loop + 🧬 Evolution sections (6:45 daily), evolution Phase 3 LIFTED (supervise first 3 cross-pollination runs), `chain_runner.py finalize --auto`, Notion vault 250/250 rich bodies.

## Gotchas for the next agent

- **GOLDEN RULE was violated live this session** (concurrent Haiku session + Codex app-server); recovered via stash. `active_tool_lock` hook now warns — treat its warning as a stop sign.
- Quality gate caps self-reported 8+ at 7.25 (`_EARNED_8_CAP`) unless anchors convince it — by design (E1 lesson), not a bug. Name rubric anchors honestly.
- `.agent/skill-embeddings.json` (3.6MB) is untracked-by-design; regenerate via `find_skill.py --build-embeddings` (~$0.007).
- Never convert Notion property types (silently wipes values — experimentally confirmed). Additive only, via `execution/notion_api.py` (2022-06-28 pin).
- Fal budget guard state was blind 65 days; now records deterministically but balance estimate needs a wallet check at fal.ai before trusting.
- `com.antigravity.knowledge-compiler-weekly` fires first on Sunday 2026-07-12 05:00 — verify its log appears clean.

## Suggested skills

- `/go` and `/create` — the new front doors (this session's build; run them, don't rebuild them)
- `/resume harness-frontier-loops` — this thread
- `/system-audit` — if anything control-plane feels off
- `/claim-safe` — any health-brand copy (Path A)
- `superpowers:verification-before-completion` — hold the session's verify-by-execution bar

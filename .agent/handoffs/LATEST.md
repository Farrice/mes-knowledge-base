# Latest Handoff

**Thread:** wargame-os-forge  
**Full path:** .agent/handoffs/2026-07-07-wargame-os-forge.md  
**Date:** 2026-07-07 (today)  
**Status:** ready  
**Title:** Wargame OS — Kashef Forge Extraction + Command Menu Sync (10 /wargame-* workflows)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume wargame-os-forge` for this one.

---

---
thread: wargame-os-forge
status: ready
resume_hint: Judge blind-pass for A-tier (10 min), then /wargame-client on Jen listing engine
unfinished: A-tier judgment pending; first client deployment not yet run
branch: main
pin: true
---

# Wargame OS — Kashef Forge Extraction + Command Menu Sync (10 /wargame-* workflows)

**Date**: 2026-07-07 · **Thread**: `wargame-os-forge` · **Status**: ready (A-tier judgment pending)

## What this session shipped

1. **`skills/mark-kashef-wargame-os/` — LIVE, B-tier** (forge extraction, EVAL-033). Kashef's wargaming method: the frontier model fights a mission on paper (Move / Expected observation / Fail + cause / Counter-move / Trigger, RECON NEEDED with exact settling checks, aborts, verification runs) so a cheaper executor runs it blind. 10 workflows in 3 tiers, all registered as `/wargame-*` slash commands. Expansion of the existing `mark-kashef` agent (planning layer ABOVE `mark-kashef-agent-orchestration`).
2. **Command menu fully wired**: generated 769 missing command shims in `.claude/commands/` so all 1,542 `.agent/workflows/` files now appear in the typed `/` menu (was 1,130). Removed 1 dead orphan (`/references` — empty skill dir, no workflow). `SLASH_COMMANDS.md` regenerated (1,898 commands on disk). Zero gaps in either direction, verified by `comm` diff.
3. **Chain closeout done**: finalize logged (Intent 9 / Expert 8 / Adversarial 8 / Grounding 9, anchors named, composite 8.33, Notion logged), `forge_gate.py record` run, EVAL-033 appended to `evolution_store/ground_truth/eval_set_v1.jsonl`, project memory written (`project_wargame-os-shipped.md` + MEMORY.md pointer).

## Next session: two tasks, in order

### Task 1 — A-tier judgment (Farrice, ~10 min)
Read side by side:
- `extractions/wargame-source/blind-pass-output.md` (fresh Sonnet agent's wargame, produced from skill files only)
- `extractions/wargame-source/visual-context.md` § "The wargame output file itself" (Kashef's REAL 01-website.md artifact, transcribed from video frames 22–31)

PASS = indistinguishable or preferred. If PASS: update EVAL-033 (`calibrated_by_human: true`), note A-tier in `skills/mark-kashef-wargame-os/SKILL.md` frontmatter, log via finalize note. Known caveat to weigh: blind-pass Move 5's executor-mistake prediction reuses the exemplar's aria-hidden genre (apt transfer, not novel-class proof).

### Task 2 — First real deployment: `/wargame-client` on Jen listing engine
- Client context: `_active/jen-listings/CLAUDE.md` + `skills/jen-santulan-listing-content/` + golden ref: 6853 Willis production sheet (memory: `feedback-jen-reel-hook-style`, `feedback-client-content-production-format`).
- Goal: wargame the listing-content production route ONCE at frontier tier (frozen choices = Jen's hook style, production-sheet format, ADU-as-bonus rule), grade to DONE, store under the client project. Every future listing = `/wargame-execute` with instance inputs at Sonnet cost.

## Key artifacts (reference, don't rebuild)

- Skill: `skills/mark-kashef-wargame-os/` (SKILL.md, genius.md, 10 workflows, 4 references, folder template in assets/)
- Extraction trail: `extractions/wargame-source/` — vision.md, architecture.md, mes-extraction.md (12 patterns), transcript.txt, visual-context.md, laundry-list-notes.md (/goal + /loop verbatim), blind-pass-output.md
- Verbatim operating prompts: `skills/mark-kashef-wargame-os/references/goal-and-loop-contracts.md`
- 45 video frames kept at `extractions/wargame-source/watch/frames/` (37MB video download deleted)

## Operational lessons banked

- Forge on a thin transcript (2,946w) is valid when the companion kit carries methodology density — weigh artifacts, not word count.
- For demo-heavy creators, `/watch` visual context is PRIMARY, not additive — the frames held the richest artifact (complete worked wargame) that transcript + PDF lacked.
- Pinning reference contracts on disk before parallel builders (solution card 2026-07-07-parallel-builders-stale-contracts) produced zero integration gaps across 11 parallel-built files.
- Kashef landmine, now in genius.md: never ask a reasoning model to expose its thinking in output — request artifacts, findings, quotes, rewrites.

## Suggested skills for the next session

- `mark-kashef-wargame-os` (Skill tool) — loads genius.md + workflow set for both tasks
- `/wargame-client` — Task 2's front door (composes wargame-order → run → grade → execute)
- `/wargame-grade` — if the A-tier read surfaces fixable weaknesses, red-team + patch before promotion
- `jen-santulan` / `listing-content` — client context for Task 2
- `/resume wargame-os-forge` — reload this thread

## Hot experts this session

mark-kashef (deep — extraction target + existing orchestration context), embodiment/craft standards (`directives/skill-craft-standard.md`, `directives/embodiment-standard.md`).

No secrets, keys, or PII in this document.


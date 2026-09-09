---
thread: execution
status: active
resume_hint: Parity/menus green both harnesses (f8cf315ee); next: dedupe hook-count constant across the two verifiers
branch: main
pin: false
---

# Handoff — execution

## Purpose
Registration sweep: make every recently built slash command / skill / workflow show up in menus and verify green on both harnesses (Claude Code + Codex) for deployment.

## Current State
Moved: fixed stale hook-count rule (8→9, artifact-placement) in `execution/verify_codex_claude_parity.py` and `execution/worktree_lane.py`; sabotage-tested both directions; re-ran parity on 7 false-degraded lanes — all FULL POWER now; blessed platform hashes (constitution drift was an unblessed baseline, `constitution_compiler.py check` green); `sync_registries.py` landed andrew-sean-greer + jordan-crawford in AGENT_INDEX/SKILL_INDEX; all 5 orphaned assets re-check PROVEN. Committed + pushed as f8cf315ee.
Uncertain: hook-count expectation is duplicated in two files with no single source — next hook bridge breaks both again.
Latest proof: `python3 execution/verify_codex_claude_parity.py` → PASS; `worktree_lane.py list` → zero degraded lanes.

## Remaining Priority
Deduplicate the Codex hook-count expectation into one shared constant (verify_codex_claude_parity.py + worktree_lane.py both hardcode 9).

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-08-10-execution.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

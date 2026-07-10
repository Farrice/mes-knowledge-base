---
name: Agent-Authored Plan JSON Crashes a Mutating Apply Mid-Run
problem_signature: an agent writes a plan/config JSON that a strict deterministic tool consumes; missing keys crash the tool AFTER it has started mutating (files moved, rewrites unrun, no receipt) — the tree ends up in a half-applied state that later runs misread as "source missing"
domain: system
tags: [orchestration, schema-validation, deterministic-tools, recovery, project-filer]
date: 2026-07-08
status: active
session: backlog-filing-sweep
---

## Problem

An Opus planner wrote `deliverables.json` in "plan format" per its prompt, but as a
bare list without `project_slug`/`referrers`. `project_filer.py apply` crashed
three times, each deeper in: (1) before moves (list vs dict), (2) after moving 1
item (missing `project_slug` inside the move loop), (3) after moving ALL items but
before reference rewrites (missing `referrers`). Result: 19 moves on disk with no
receipt, no revert entries, and no link rewrites — and the next apply attempt
reported every item "source missing," which read like data loss.

## Root Cause

Two compounding failures: (a) the tool validated nothing up front — required keys
were consumed lazily at different depths of a mutating loop, so each missing key
moved the crash later past more side effects; (b) the orchestrator's prompt said
"plan format" instead of pointing the agent at a real example plan file, so the
agent invented a plausible-but-wrong schema.

## Approach That Worked

1. **Recovery source of truth = the append-per-move ledger.** `append_move_ledger`
   runs inside the loop, so every landed move was recorded even though the receipt
   writer never ran. Cross-checking plan items against disk (source gone AND
   destination present) reconstructed the exact move set.
2. **Backfill, don't redo**: re-ran only the missed phase (reference rewrites via
   the tool's own `rewrite_file`), then wrote a recovery receipt and appended
   inverse `mv` lines to the day's REVERT script.
3. **Fail-fast validation added** at the top of `apply_plan`: all required plan and
   item keys checked BEFORE the first move; malformed plans now die with zero side
   effects.
4. **Prompt fix for next time**: when an agent must author input for a strict
   tool, the prompt names a concrete example file to copy the schema from
   (`.tmp/filer-plans/trendscale-brief-revision.json`), not a prose description.

## Dead Ends

- Whack-a-mole: adding one missing key per crash (`project`, then `project_slug`,
  then `referrers`) — each retry mutated more state before failing. Validate the
  whole schema once instead.
- Reading the receipt's skip reasons with the wrong key (`skip_reason` vs
  `reason`) — masked the real diagnosis for one round.

## Verification

Post-recovery verify: 0 old-path residue, 0 empty dirs, all 19 destinations
present, revert script re-runs coherent. Fail-fast confirmed by py_compile + the
next malformed plan dying before any move.

## Weaker-Model Trap

Sees "source missing" on retry and concludes the files are lost (or worse,
re-creates them) instead of checking whether destination-exists+source-gone means
the moves already happened. Half-applied state must be diagnosed against the
ledger, never against the last error message.

## Pointers

- `execution/project_filer.py` (`apply_plan` fail-fast block)
- `.agent/organization/receipts/2026-07-08-deliverables-RECOVERED.json`
- `_system/organization/move-ledger.jsonl`
- Related: [[2026-07-07-parallel-builders-stale-contracts]] (same family: agents
  producing artifacts against an imagined interface)

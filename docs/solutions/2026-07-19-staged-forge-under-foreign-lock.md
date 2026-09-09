---
date: 2026-07-19
session: oren-dara-ad-psychology forge
name: staged-forge-under-foreign-lock
problem_class: harness / session locks / blocked build
domain: harness
status: proven
problem_signature: "a multi-file build is blocked because a sibling session holds a fresh tree lock, and every documented option — wait, coordinate, or open a worktree — costs either idle wall-clock or merge complexity"
tags: [session-lock, forge, worktree, staging, concurrency, rsync]
---
# Staged Forge Under a Foreign Session Lock

**Date**: 2026-07-19 · **Domain**: system / orchestration · **Session**: oren-dara-ad-psychology forge

## Problem

`/extract-forge` Phase 0 requires the tree lock, but a sibling session held a FRESH lock (Baldacci forge, heartbeat seconds old). The workflow's options — wait, coordinate, or worktree — all cost either wall-clock (idle waiting) or merge complexity (worktree → All-Work-on-Main reconciliation).

## Solution

Split the forge by write-target, not by phase:

1. **Phases 1–4 + all file AUTHORING run lock-free** — they're reads + scratchpad writes. Build the complete skill into a staging tree that mirrors repo paths: `scratchpad/stage/{extractions,skills,wrappers}/...`
2. **Poll the lock opportunistically** (each natural pause, not a busy-wait). The sibling released ~40 min in.
3. **On claim: one atomic `rsync -a stage/ → tree/`**, then registration/wiring/gates as normal.

Result: zero idle time, zero worktree merge, tree only ever touched under our own lock, and the move-in is a single reviewable operation.

## When to apply

Any multi-file build (forge, OS build, migration) blocked by a fresh foreign lock where the build's authoring is deterministic from context already loaded. NOT for work that must read-modify existing tree files concurrently (that's the accept→repair→dedupe card's territory).

## Gotchas

- Registries/generators (sync_registries, wire_prompt_pointers) must run AFTER move-in, never against the stage.
- Re-check `git status` before committing — the sibling may have committed between your claim and your commit.
- Keep the stage path mirroring repo-relative paths exactly, so the rsync is mechanical.

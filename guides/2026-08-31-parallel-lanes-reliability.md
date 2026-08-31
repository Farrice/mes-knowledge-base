---
date: 2026-08-31
session: parallel-lanes-reliability
tier: operator-guide
status: enriched
---

# Parallel Lanes Reliability — What We Built 2026-08-31 and How to Use It

> Parallel work now has a loss-safe integration path: sessions author inside isolated lanes, quiet committed lanes can merge locally, conflicts and unfinished work park without deletion, and routine telemetry no longer dirties integration `main`. The behavior lives in `execution/worktree_lane.py`, `execution/lane_reconciler.py`, `execution/chain_runner.py`, and `execution/degrade.py`.

## ⚡ If you only read 10 lines

- Treat `main` as the integration desk, not an authoring desk; every writer works in a lane.
- Start a lane with `git worktree add .tmp/codex-worktrees/<slug> -b codex/<slug>` and then run `python3 execution/worktree_lane.py bootstrap`.
- `FULL POWER` means the lane received the environment, memory, MCP, budget, and hook dependencies it needs.
- Inspect all lanes with `python3 execution/worktree_lane.py list`.
- Preview automatic decisions with `python3 execution/lane_reconciler.py --dry-run --json`.
- Merge a reviewed safe lane locally with `python3 execution/worktree_lane.py merge --lane <branch> --no-push`.
- A clean quiet committed lane may merge; an active, conflicting, probe-failed, or stale-dirty lane parks.
- Runtime finalization and degradation events stay observable on `main` without changing tracked files.
- The hourly reconciler never pushes `main`, deletes forgotten work, or forces a conflict resolution.
- If a merge says “dirty,” inspect tracked changes first; untracked active creative assets are preserved and do not justify cleanup.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/worktree_lane.py bootstrap` | A parity-proven lane with the shared environment linked in | A session may write and needs full harness capability |
| `python3 execution/worktree_lane.py list` | Current lane state across Codex and Claude worktrees | You need the queue without opening every task |
| `python3 execution/worktree_lane.py doctor` | Lane and integration diagnostics | A lane cannot merge or appears degraded |
| `python3 execution/worktree_lane.py merge --lane <branch> --no-push --dry-run` | The exact guarded merge preview | Before manually integrating a reviewed lane |
| `python3 execution/worktree_lane.py merge --lane <branch> --no-push` | Local merge, Law-3 audit, derived-index refresh, and safe teardown | A lane is committed, quiet, and conflict-free |
| `python3 execution/lane_reconciler.py --dry-run --json` | Machine-readable actions for every lane | You want to see what the hourly job would do |
| `python3 execution/verify_lane_reconciler.py` | Positive and known-bad controls for lane classification | Reconciler or merge-probe behavior changes |
| `python3 execution/verify_main_safe_finalize.py` | Proof that all finalize telemetry stays off tracked `main` and remains tracked in lanes | Finalization starts dirtying main again |
| `python3 execution/session_closeout_intelligence.py run --source end-session --dry-run --force` | A live closeout path test without writing a report | Closeout or performance registration is suspect |

## The mental model

### Main is an integration desk, not a shared notebook

A worktree lane is a private desk with the same tools. Sessions can move fast, explore, and leave unfinished files without blocking another session. `main` accepts reviewed, committed work. The lane boundary removes the impossible demand that every concurrent writer keep one shared directory clean.

### “Dirty” is a classification problem

The old failure was not simply too many files. Several different states were being called dirty:

- **Tracked integration dirt:** a process changed a repository file on `main`; this can block a merge and must be traced to its producer.
- **Active lane dirt:** a session is still authoring; preserve it and do not merge.
- **Stale-dirty lane:** old uncommitted work may still have unique value; park it for purpose review.
- **Conflict lane:** committed work overlaps current `main`; park it for an intentional resolution.
- **Untracked active artifact:** a creative render or other loose output may belong to a live session; do not delete it to cosmetically clean status.

The repair works because the system responds differently to each state.

### Automation is a selector, not a cleanup robot

The reconciler is allowed to integrate only the boring case: committed, quiet, conflict-free work that passes the merge probe. Every uncertain case becomes visible and remains recoverable. The automation reduces forgotten safe work without converting uncertainty into deletion or forced merging.

## Main-safe runtime telemetry

### What it is

`execution/chain_runner.py` routes five finalize-event classes to ignored `.agent/finalize-runtime.jsonl` when it is running in canonical integration `main`: subagent misses, blind-pass overrides, learning-latch overrides, verification misses, and verdict advisories. The same events remain tracked in authoring lanes, where they belong to the authored change history.

`execution/degrade.py` applies the same rule to graceful-failure diagnostics. On `main`, warnings append to ignored `.agent/health/degradations-runtime.jsonl`; in lanes, they append to tracked `.agent/health/degradations.jsonl`. `recent()` reads both historical and runtime evidence on `main`, so clean Git does not mean blind health reporting.

### When to reach for it

Use the main-safe verifiers when a closeout, finalize, health check, or scheduled task unexpectedly changes tracked files. The first question is not “how do we clean this?” It is “which runtime producer wrote repository truth?” Fix that producer, remove only the exact known line it created, then rerun the live command.

### When not to

Do not redirect authored source, handoffs, guides, or decisions into runtime logs. This rule is for observational events whose creation should not redefine the product. If the file is the work, keep it in the lane and commit it normally.

### Worked example

The closeout path originally appended a missing optional-state warning to tracked `.agent/health/degradations.jsonl`. After the repair, the same live dry run left `git diff` empty and wrote the warning to `degradations-runtime.jsonl`. That is the acceptance standard: observable failure, clean integration state.

### Honest edges

The main/lane distinction is intentionally Git-derived. Running these tools outside a Git checkout falls back to tracked behavior rather than guessing. Runtime logs are local operational evidence; they are not remote backup.

## Guarded lane integration

### What it is

`execution/worktree_lane.py merge` seals the lane, checks tracked-main state and fresh writers, runs a real merge simulation, takes the merge mutex, merges with history preserved, audits branch-added files, regenerates derived indexes, and tears down only after success. `--no-push` makes the integration local.

`execution/lane_reconciler.py` applies that policy hourly through the macOS LaunchAgent `com.antigravity.lane-reconciler`. The verified live service had a 3,600-second interval and last exit code 0.

### When to reach for it

Use the direct merge command for a lane you have reviewed. Let the reconciler handle routine quiet lanes you forgot. Use its JSON dry run when you want the queue classified by action rather than Git jargon.

### When not to

Do not run a forced merge because the backlog feels untidy. Do not use `git merge -s ours` to erase divergence. Do not dismantle stale lanes until purpose and unique value have been reviewed.

### Worked example

The reconciliation preserved live creative lanes, parked nine stale-dirty lanes, and locally integrated the verified reliability patches. Later, new creative PNGs appeared on `main`; they were left untouched because they were untracked active artifacts, not proof that tracked integration was unsafe.

### Honest edges

Automatic reconciliation cannot decide the semantic winner in a true conflict. That is deliberate. It also does not push `main`; remote integration remains an explicit boundary.

## Closing forgotten work without losing it

A stale lane is a retrieval question before it is a Git question. Audit it by purpose, unique value, and change size. Resume it if the outcome still matters, preserve it if the work is valuable but not current, and close it only when its value is already integrated or intentionally rejected. Parking is a reversible decision; deletion is not.

## Closeout truth: complete or approval-blocked

The closeout now has two deliberately different visible shapes. A verified completed run may show exactly three compact, ranked continuation prompts. A dry run, denied escalation, partial failure, or missing native task action shows only the exact blocker, the fact that the task remains unarchived, the recoverable artifact path, and one copy-ready approval sentence.

This distinction prevents a polished answer from claiming more than the receipts prove. Internal routing metadata remains available to the system, but retired `Use Now / Harden / Expand` labels and rich diagnostic fields no longer spill into the completed user-facing closeout. A completed closeout also cannot route its first prompt back into `/end-session`.

Use `python3 execution/verify_end_session_visible_closeout.py` after any End-session, renderer, sync-helper, or task-lifecycle change. Its positive fixtures cover both valid states; its known-bad controls reject false completion, continuation menus while blocked, legacy-field leakage, self-routing, and vague approval language. The reusable contract and examples live in `semantic_libraries/antigravity/primitives/end-session-visible-closeout-benchmark.md`.

## Composition options

| Add this | When it earns its cost | Contribution |
|---|---|---|
| `/system-audit` | Main keeps re-dirtying or the automation reports false health | Finds the upstream producer and adds a negative control |
| `/repeatability-spine` | A lane repair loses behavior that previously worked | Preserves the good example before mutation |
| `/end-session` | The task is genuinely done or needs an exact continuation packet | Saves the handoff, runs closeout intelligence, and applies native lifecycle actions |
| Manual purpose audit | A lane is stale-dirty or semantically conflicting | Supplies the human judgment automation must not invent |

## Final operating rule

Fast parallel work is compatible with reliable integration when the system protects uncertainty instead of trying to erase it: author in lanes, integrate only the proven boring case, park everything ambiguous, and keep runtime observation out of tracked `main`.

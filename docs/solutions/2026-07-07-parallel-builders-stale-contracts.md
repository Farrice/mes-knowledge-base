---
name: Parallel Builders Ship Against Stale Contracts
problem_signature: two agents build in parallel; the later one can't see the earlier one's new files and ships an "honest gap" note instead of the real integration
domain: system
tags: [orchestration, parallel-agents, contracts, integration, sub-agent-protocol]
date: 2026-07-07
status: active
session: solution-recorder-prose-build
---

## Problem

When an orchestrator dispatches two agents in parallel to build complementary halves
of a system, the second agent has no visibility into the first's actual output while
working — only the orchestrator's *description* of the planned interface. Default
failure: the second agent notes "component X isn't available yet" and ships a
placeholder, even after the first agent has since landed the exact file.

## Root Cause

Parallel dispatch means the two agents' contexts never merge until the orchestrator
reads both results back. Neither gets a live signal when the other finishes. The
dispatch-time assumption "the other component doesn't exist yet" silently goes stale
the moment the first agent lands its file, and nothing prompts a recheck.

## Approach That Worked

1. Orchestrator defines the shared contract up front, in BOTH prompts — exact CLI
   subcommands/flags, exact file path, exact frontmatter schema.
2. Second agent is told to check, near the end of its own work, whether the
   counterpart now exists (`ls`/`--help` probe) rather than trusting the dispatch-time
   snapshot.
3. If it exists: run an explicit contract-seam pass — invoke the real CLI's `--help`
   on every subcommand, confirm key-for-key match, before wiring around it.
4. If it still doesn't exist: say so explicitly rather than emitting a placeholder
   that looks finished.

Concretely: `execution/solution_recorder.py` didn't exist at dispatch time, so this
task's brief was written either-or. A late recheck (`ls`, then `--help` on
`draft`/`save`) found the file landed with the exact `draft --slug --problem` /
`save --file` signature assumed — cards saved through the real CLI, not shipped with
a stale "not available yet" note.

## Dead Ends

- Assuming parallel builders discover each other's work without an explicit recheck.
- Treating "not available" as permanent instead of a snapshot needing re-verification.

## Verification

Ran the counterpart's actual `--help` for the top command and each subcommand,
compared flags against the brief's assumption (`--slug`, `--problem`, `--file`) —
exact match, cards saved via the real CLI.

## Weaker-Model Trap

Treats "not available yet" as fixed at task-start and never revisits it — ships the
caveat as final even after the counterpart lands, because recheck wasn't instructed.
Procedural trap: not wrong about what it observed, wrong to stop observing.

## Pointers

- This session's task brief (parallel builder note + either-or instruction)
- `_active/swarm-apex-2026-07-07/PLAN.md` §"Binding Constraints" ("no forced wiring")
- `execution/solution_recorder.py --help` / `draft --help` / `save --help`

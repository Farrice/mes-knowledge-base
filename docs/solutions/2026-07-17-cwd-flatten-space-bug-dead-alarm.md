---
name: Cwd-Flatten Space Bug Silently Kills Transcript-Scanning Hooks
problem_signature: a hook that maps cwd to ~/.claude/projects/<flattened> via cwd.replace("/", "-") never finds the dir when the project path contains a space (or any non-alphanumeric char) — the hook exits silently and its alarm/telemetry is dead for that project with zero error signal
domain: system
tags: [hooks, observability, silent-failure, claude-projects, concurrent-session-alarm, wave-0]
date: 2026-07-17
status: active
session: frontier-elevation-wave-0
---

# Cwd-Flatten Space Bug: the Alarm That Never Fired

## Problem

`concurrent_session_alarm.py` (SessionStart) had never fired for this project. Discovery
was accidental: the Wave 0 acceptance fixture smoke-tested the hook with a fake session id
expecting the sibling alarm, and got silence despite a fresh sibling transcript AND a
fresh session lock.

## Root Cause

Claude Code flattens project cwds into `~/.claude/projects/` dir names by converting
EVERY non-alphanumeric character to `-`. The hook used `cwd.replace("/", "-")`, which
leaves spaces intact — `/Users/farricecain/Google Antigravity` became
`-Users-farricecain-Google Antigravity` (space preserved) while the real dir is
`-Users-farricecain-Google-Antigravity`. `os.path.isdir` failed → early `return` → the
alarm was dead on arrival for any project path containing a space, since the day it
shipped. Compounding defect: the early return also skipped the session-lock status check,
which has nothing to do with transcript dirs.

## Fix

1. `flat = re.sub(r"[^A-Za-z0-9]", "-", cwd)` — match the harness's actual flattening.
2. Missing transcript dir now `pass`es instead of `return`ing, so independent checks
   (session-lock freshness) still run.
3. New lock-only alarm branch: fresh lock + no fresh Claude sibling = likely Codex or an
   autonomous runner holding the tree — warn, never block.

## Verification

Three-case smoke test: (1) fake own-id against real cwd → sibling alarm fires with lock
status; (2) nonexistent cwd, no lock → silent; (3) scratch tree containing only a fresh
`.agent/session.lock` → lock-only alarm fires. All pass 2026-07-17.

## Deploy When / Generalize

Any hook or script that reconstructs `~/.claude/projects/<flat>` from a cwd MUST use the
all-non-alphanumeric flattening, and any observability hook should be smoke-tested with a
case that FORCES it to fire — a hook that has never fired is indistinguishable from a
hook that can never fire (feedback_ai-memory-dependent-observability: deterministic
backstops must themselves be verified deterministic).

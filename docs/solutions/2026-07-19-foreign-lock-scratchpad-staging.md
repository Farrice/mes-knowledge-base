---
name: Foreign-Lock TTL Wait → Scratchpad Staging → Atomic Copy-In
problem_signature: a fresh foreign session lock blocks forge/build work for up to 45 min (TTL); naive options are to idle-wait or to violate the one-driver-per-tree rule
domain: orchestration
tags: [session-lock, merge-discipline, forge, scratchpad, staging]
date: 2026-07-19
status: active
session: jason-fladlien-expansion-forge
---

## Problem

`session_lock.py check` returns BLOCKED on a fresh foreign lock (heartbeat < 45-min TTL) while a full extract-forge is queued. Deleting the lock file works "around" the gate (banned); idling wastes the entire TTL window. Also: the lock's `pid` field is the PID of the `claim` invocation itself (which exits immediately) — a dead PID proves NOTHING about the holder session. Only the heartbeat age is truth.

## Approach That Worked

1. **Deterministic wait**: background 60s poll loop on `session_lock.py check` (`while ! check; do sleep 60; done`) — re-invokes the agent the moment the lock goes stale. Never touch the lock file.
2. **Stage EVERYTHING in the scratchpad meanwhile** — it's outside the locked tree, so zero contention: source acquisition (yt-dlp captions/video), frame extraction (watch script `--out-dir` in scratchpad), full transcript reads, coverage analysis, and complete drafts of every build artifact (workflows, prompts, wrappers, genius tranche, corpus pieces, ledger appendix).
3. **Grounding passes are also lock-free**: grep-verify every "verbatim" quote against the scratchpad transcripts BEFORE the build lands.
4. **On stale → claim → atomic copy-in**: one `cp` batch + a handful of `Edit`s, then the gate sequence (audit → library → pointers → registries → blind pass → auditor → finalize). Tree-mutation window shrank from ~2.5h to ~15 min.

## Dead Ends

- **PID liveness as a stale signal**: looked decisive (holder PID dead), but `claim` stamps its own short-lived PID — false signal, correctly abandoned.
- **"Read-only work only" framing**: too conservative — scratchpad WRITES are fine; the lock protects the repo tree, not the machine.

## Deploy When

- Any forge/build queued behind a fresh foreign lock (Codex session, autonomous run, crashed sibling).
- Generally: any long-TTL gate + heavy-prep task — prep off-tree, land atomically.

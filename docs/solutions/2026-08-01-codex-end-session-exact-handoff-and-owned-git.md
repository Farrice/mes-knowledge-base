# Solution Card — Exact handoff identity plus manifest-owned Git

**Date**: 2026-08-01 · **Domain**: system fix (Codex session lifecycle) · **Status**: SOLVED

## Problem

The shared `/end-session` workflow could select the newest temp handoff, run downstream intelligence against that inferred file, and use a broad commit gate. In a multi-task environment, this created two coupled risks: a correct-looking handoff could belong to another task, and closeout-generated or unrelated repository changes could be swept into the same commit.

The existing 2026-07-25 solution card documented the recency collision and a recovery workaround. It did not build the guard.

## Root cause

The closeout treated location and timing as identity and treated working-tree membership as ownership. Neither assumption survives concurrent tasks:

- newest file does not mean correct task
- generated during closeout does not mean task-owned
- `done` metadata does not mean safe to archive
- a clean commit does not mean the branch is safe to push

## Solution

1. Save from an explicit named source and emit a JSON receipt with normalized source/stored hashes.
2. Verify thread, title, body hash, branch, core paths, remaining priority, and Do-Not-Rebuild guidance before running the shared spine.
3. Cross-check the handoff title and core paths against a Codex closeout manifest.
4. Pass the exact stored path into closeout intelligence, memory, guide, and state archive steps.
5. Keep task lifecycle native: rename every meaningful task, pin unfinished states, and archive only verified `done`.
6. Gate Git to manifest-owned paths and recognized closeout receipts on a dedicated `codex/*` worktree.
7. Refuse secrets, unexpected deletions, unrelated dirt, divergence, detached HEAD, tool collision, and failed required verifiers.
8. Push only the current Codex branch, verify its remote SHA, and write an integration packet. Never merge or push `main`.
9. Queue uncertain organization and read-only self-heal findings instead of deleting or mutating broadly.

## Proof

`execution/verify_codex_end_session.py` reproduces the cross-session collision, mismatch failures, dedicated-worktree policy, lifecycle matrix, explicit artifact moves, review queuing, and a real push to an isolated bare remote. The push fixture proves the Codex branch SHA reaches the remote while `main` remains unchanged.

The canonical workflow, global wrapper synchronization helper, End-session verifier, System Audit verifier, Source-to-Skill-System verifier, authority verifier, and strict live-surface audit provide the connected control-plane proof.

## Reusable lesson

Closeout is a transaction across four identities: task, handoff, filesystem ownership, and Git branch. Verify each identity at its boundary. Do not let a checksum stand in for task identity or a Git diff stand in for task ownership.

## Supersedes

This card builds the guard proposed in `docs/solutions/2026-07-25-handoff-from-temp-cross-session-collision.md`. The older card remains as incident history.

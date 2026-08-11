---
date: 2026-08-11
session: codex-native-end-session
tier: operator-guide
status: enriched
---

# Codex-Native End Session — What We Built 2026-08-11 and How to Use It

> `/end-session` is now the primary Codex closeout for exact handoffs, local
> checkpoints, task naming, and worktree hygiene. It preserves the permanent
> Codex operator lane, makes temporary-lane debt visible, and keeps push and
> global writes behind explicit approval. Canon: `.agent/workflows/end-session.md`.
> Root cause: `docs/solutions/2026-08-11-codex-end-session-lane-disposition.md`.

## ⚡ If you only read 10 lines

- Say `/end-session` when meaningful work is finished; do not build another cleanup command.
- The task title, handoff H1, and manifest title use `[Domain]: [Specific Object] - [Outcome]`.
- The exact source handoff is saved and verified; “newest file” discovery is not continuity.
- `codex/antigravity-operator-core` is a permanent workbench, so task closeout does not delete it.
- Other linked worktrees are temporary lanes; closeout returns the exact merge-or-park action.
- A temporary lane stays visible until that action is approved and resolved.
- Git defaults to `commit-local`; only manifest-owned and closeout-generated paths are staged.
- Push, changes to `main`, and writes under `~/.codex/end-session/` require explicit approval.
- Only a verified `done` receipt archives the Codex task; incomplete closeouts stay pinned.
- The self-test is the proof: commit `4ad2bf464`, exact handoff verified, eight checks passed, no push, operator lane preserved.

## Command table

| Command or surface | What it produces | Reach for it when |
|---|---|---|
| `/end-session` | Whole-session closeout: title, exact handoff, receipt, local Git decision, next prompts, Operator Lesson | Meaningful work is finished or needs a durable continuation |
| `python3 execution/codex_end_session.py run --manifest "<manifest.json>"` | Machine-readable Codex closeout receipt | The skill has prepared the exact task manifest |
| `python3 execution/handoff_store.py verify "<thread>" --source "<exact-source>" --json` | Identity proof for title, thread, branch, body, core paths, and remaining priority | Before calling a handoff durable or resumable |
| `python3 execution/conversation_index.py stats` | Read-only retrieval/index health | At closeout when checking conversation discoverability |
| `python3 execution/worktree_lane.py list` | Active and parked lane inventory | A temporary branch seems to have been left behind |
| `python3 execution/worktree_lane.py merge --lane <branch>` | Seal, gate, merge-or-park, and teardown route | After explicit approval for a temporary lane; the helper may update and push `main` |
| `python3 execution/verify_codex_end_session.py` | Isolated behavior proof | After changing closeout, Git, handoff, or lane policy |

## The mental model

Four decisions used to be bundled under “clean up”: finish the task, resolve the
worktree, synchronize Git, and write retrieval state. They are now separate.

1. **Task completion is not lane deletion.** A task can be done while the
   permanent operator workbench remains ready for the next task.
2. **A lane can be unresolved without being hidden.** Temporary lanes either
   merge or park. If approval is still needed, the receipt names the branch and
   exact command, and the Codex task stays visible.
3. **Commit is not push.** A local checkpoint protects the work. Sending it to a
   remote is an external action with its own approval boundary.
4. **Continuity is identity, not recency.** The exact source handoff is hashed
   and checked against the stored handoff. A newer sibling file cannot hijack it.

## 1. `/end-session`: the single Codex closeout front door

### What it is

The global Codex skill is a thin bridge into the canonical Google Antigravity
workflow. It does not carry a second router, cleanup system, or handoff format.
The workflow builds a task manifest, runs `codex_end_session.py`, reads the JSON
receipt, then uses native Codex task actions to rename, pin, or archive.

### When to reach for it

- A build, repair, research task, client artifact, or strategy session is ending.
- Work must continue later and needs an exact retrieval packet.
- You are unsure whether the current worktree should remain, merge, or park.
- You want the system to close Git and documentation debt instead of remembering commands yourself.

### When NOT to

- A tiny answer or conversational correction needs no durable artifact.
- You only need to transfer one narrow work packet; use `/handoff`.
- You only want follow-up ideas; use `/steering-compass`.
- You are mid-build and not actually closing; update the working state instead.

### How to invoke

Say `/end-session`, `wrap this session`, or `session closeout`. Codex derives the
title and slug. You should not have to name the task, pick a cleanup script, or
remember which verifier runs.

### Worked example

This repair closed itself through the new path. The coordinator saved
`.agent/handoffs/2026-08-11-codex-native-end-session.md`, verified all identity
checks, ran the bounded closeout spine, passed eight project verifiers, and made
local commit `4ad2bf46404e00eecf9c28e4b96d184ab81404fc`. The receipt returned
`valid: true`, `git.status: committed-local`, `lane_action.status: preserved`,
`global_receipts.status: skipped`, and `task_actions.archive: true`.

### Honest edges

The command can close a task; it cannot decide an approval boundary on your
behalf. A temporary lane whose merge helper may change or push `main` remains a
visible action until you approve it.

## 2. Lane disposition: permanent workbench versus temporary lane

### What it is

`lane_disposition: "auto"` inspects the branch. The dedicated
`codex/antigravity-operator-core` branch resolves to `preserve`. Other linked
Codex worktrees resolve to `merge-when-clean` and receive an
`approval-required` lane action.

The shared spine always receives `END_SESSION_NO_AUTOMERGE=1` from the Codex
coordinator. That prevents the spine from removing its own working directory
before Codex finishes verification and Git. Codex also runs the bounded
`--degraded` spine: closeout intelligence and handoff work still run, while
broad mission-brief and unrelated index regeneration are skipped visibly.

### When to reach for it

You normally do not invoke this directly. Inspect `lane_action` when a task does
not archive or when `worktree_lane.py list` shows a lingering temporary branch.

### When NOT to

Do not merge the permanent operator lane merely to make the lane count reach
zero. Do not force a conflicting temporary lane. A parked branch with a reason
is healthier than an invisible or lossy cleanup.

### Worked example

This session ran on `codex/antigravity-operator-core`. The same `auto` policy
that would flag a temporary lane returned `preserved` here, so the task could
archive while the workbench stayed available and clean.

### Honest edges

The current run did not perform a real temporary-lane merge or remote push.
Those pathways remain approval-gated. Their structural route exists; the next
approved temporary-lane closeout supplies the live production receipt.

## 3. Git and global state: conservative by default

### What it is

The manifest exposes three Git levels: `off`, `commit-local`, and
`commit-and-push`. `commit-local` is the default. The coordinator refuses main,
detached HEAD, non-Codex branches, non-worktree checkouts, remote divergence,
unowned dirt, unexpected deletions, secret-like paths, and fresh foreign locks.

Global receipt files under `~/.codex/end-session/` default off. Project-local
handoffs remain canonical. A generic project without Antigravity helpers retains
its exact project-local source instead of silently falling back to a global write.

### When to reach for it

- Use the default for normal Codex work.
- Use `git_sync: "off"` when work must remain uncommitted; the receipt stays held.
- Enable `commit-and-push` or global receipts only after explicit approval for that run.

### When NOT to

Do not widen `task_owned_paths` to make a dirty-tree blocker disappear. The
blocker is evidence that another session or process owns part of the checkout.
Do not treat a successful local commit as integration into canonical `main`.

## Composition options

| If this appears at closeout | Optional companion | Why it earns its cost |
|---|---|---|
| A known good result regressed | `/repeatability-spine` | Preserves the good example before repair |
| Hooks, routing, or defaults are broken | `/system-audit` | Diagnoses the control plane instead of expanding closeout |
| Only a fresh task needs context | `/handoff` | Smaller transfer packet without whole-session lifecycle work |
| A temporary lane is still open | `worktree_lane.py list` then approved merge | Converts hidden branch debt into a named action |

## Honest edges and current boundaries

- Canonical-main platform lint passes. The isolated operator lane intentionally
  lacks ignored `.agent/cos/goals.json`; lane-only lint reports that boundary.
  Copying runtime state into the lane is not the fix.
- The operator branch may remain ahead of `main`. That is expected while dirty
  canonical `main` cannot safely receive integration.
- Claude Code and Cowork remain supported. This repair changes Codex-native
  closeout policy; it does not demote peer constitutions or replace Claude's
  legacy closeout compatibility path.
- Global wrappers were not rewritten. They remain thin pointers to the updated
  canonical workflow, so global availability did not require a new skill mirror.
- Real caliber is still proven by production work. The next move is a substantive
  Codex task, not another system expansion.

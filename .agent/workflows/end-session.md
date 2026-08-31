---
description: Run at the end of a deep-work session
---

# 🧹 /end-session — Session Handoff

> **Purpose**: Generate a clean handoff for the next session. Deep cleanup is optional — assets are already organized when produced.

## Operator Core Alignment

This workflow is the canonical source of truth for End-session behavior.
Global and local End-session wrappers must stay thin compatibility wrappers
that point back here, not competing behavior contracts.

Preserve these invariants:

- `/end-session` owns whole-session closeout, retrieval handoff, and closeout intelligence capture.
- It is not `/handoff` for a focused transfer packet and not `/steering-compass` for standalone next-prompt coaching.
- A verified completed closeout includes session naming metadata, a concise handoff, exactly `3 Next Prompts`, and one `Operator move:` line. An approval-blocked or partial closeout uses the bounded blocker surface below instead of a completion-shaped prompt menu.
- **Operator-guide library (Farrice 2026-07-13, binding):** every meaningful session files a scannable document in `guides/` — the closeout spine's `session-guide` step detects the tier (operator assets changed → **operator-guide**, otherwise **session-brief**) and writes a deterministic stub either way (coverage never depends on memory). Model enrichment is gated to the **operator-guide** tier ONLY: when the session shipped operator assets (skills/workflows/execution/directives), the model half of `/end-session` MUST enrich that stub (or write the guide outright) per the format contract `guides/FORMAT.md` (exemplar: `docs/ROOT-CORE-OPERATOR-GUIDE.md`, plus the "If you only read 10 lines" block and command table) — set `status: enriched`, update `guides/INDEX.md` (use-case table + chronology, clear the Pending line), and stamp `python3 execution/operator_guide_sync.py record`. For the **session-brief** tier, the deterministic stub (already derived from the handoff by the spine) stands — do not re-compose it. Never fall back to a bare change-list.
- Closeout intelligence runs via the closeout spine (Step 1.4, `execution/end_session_closeout.py`), which in turn invokes `python3 execution/session_closeout_intelligence.py run --source end-session` as one of its steps — do not call it separately.
- Conversation indexing uses the safe `python3 execution/conversation_index.py stats` check before any rebuild.
- Codex closeouts use an exact named handoff source and `python3 execution/codex_end_session.py run --manifest <json>`; never select the newest handoff by recency when task identity is known.
- Codex task titles use `[Domain]: [Specific Object] - [Outcome]`. Rename every meaningful task, pin unfinished tasks, and archive only a verified `done` closeout.
- Automatic Git synchronization is limited to manifest-owned paths in a dedicated `codex/*` worktree. Never auto-commit, auto-merge, or auto-push `main`.
- Optional cleanup must be reviewed; never publish, push, broadly delete, or perform destructive cleanup without explicit approval.
- Real Codex subagents require explicit authorization.

### Deterministic backstop

A `SessionEnd` hook (`execution/hooks/session_end_hook.py`) runs the closeout
spine automatically in `--degraded` mode if a session produced artifacts but
`/end-session` was never run — closeout is no longer memory-dependent on the
operator. It stays silent when the spine already ran this session (detected
via `session_ledger_hook.py`) or when the session was purely conversational
(no artifacts produced).

## Insightful Momentum Closeout Requirement

The visible final answer is part of the closeout state machine. It must not
claim or visually imply completion before the coordinator receipt proves it.

### Verified completed closeout

Only when the actual coordinator receipt has `valid: true`, `dry_run: false`,
no blockers, and the requested native task action has succeeded, run:

```bash
python3 execution/contextual_next_prompts.py \
  --objective "[session closeout objective]" --format compact
```

The completed visible closeout uses the current compact contract:

- lead with the completed outcome and the durable handoff/receipt evidence
- show exactly three ranked, session-specific, materially different prompts
- give each prompt a concrete outcome title, one short why-now sentence, and a
  copy-ready `Prompt:` line
- end with one `Operator move:` line when the session teaches a reusable
  judgment lesson
- never use the retired `Use Now / Harden / Expand` labels or expose internal
  fields such as `Output/Capability Move`, `Operator Insight`,
  `Hidden Gap/Opportunity`, `Capability Revealed`, or tool-menu metadata
- never route a completed closeout back into `/end-session`

If the compact renderer output is awkward, improve the objective and rerun it;
do not hand-author a generic prompt block.

### Approval-blocked or partial closeout

If the actual run was denied, dry-run only, invalid, partially failed, or still
needs authority, do not run or surface the three-prompt renderer. Emit only:

```markdown
Closeout: PENDING APPROVAL
Coordinator receipt: BLOCKED — [exact blocker]
Task remains unarchived. Prepared artifacts remain in [exact recoverable path].
Approval needed: [one copy-ready sentence granting the exact missing authority]
```

Do not say `Saved + pinned`, `Archived`, or otherwise imply the closeout
finished. Do not suggest `/end-session` again. Preserve the prepared artifacts
and stop at the authority boundary.

The reusable examples, known-bad controls, and verifier expectations live in
`semantic_libraries/antigravity/primitives/end-session-visible-closeout-benchmark.md`.

### Handoff lanes (decided 2026-06-15 — keep these distinct)
One handoff *format*, three jobs that don't overlap:
- **`/handoff`** (Matt Pocock skill) — produces the canonical, portable handoff document in the OS temp dir (cross-tool, secrets redacted, artifacts by ref, suggested-skills section). It owns the handoff *content format*.
- **`/end-session`** (this workflow) — the system close-down ritual. It **composes `/handoff`** for handoff generation (Step 1), then adds the things `/handoff` deliberately doesn't do: conversation-index update + commit offer (+ optional `--deep` cleanup).
- **session-state-protocol** (`.agent/session-state.md`) — auto-written *during* a session to survive compaction. NOT a handoff; it solves mid-session context drift. Untouched by this workflow.

## Usage

```
/end-session              # Quick handoff (default)
/end-session --deep       # Full cleanup + handoff
```

## Quick Handoff (Default — 1-2 Tool Calls)

### 1. Generate Handoff (delegate to `/handoff`)
// turbo
**Invoke the `/handoff` skill** (Skill tool) to produce the canonical, portable handoff document in the OS temp dir. Pass the next session's focus as the argument (e.g. the remaining priority). This is the single handoff artifact — do not hand-author a second, divergent format here.

#### Session naming convention (AUTOMATIC — never ask Farrice to name or rename it)
Derive a consistent Title and slug from the session's primary object. This is the whole point: Farrice never types a title or renames a chat.

- **Codex task + handoff Title** (set it as the handoff H1 and manifest title):
  `[Domain]: [Specific Object] - [Outcome]`
  Examples: `System: Codex End-Session - Built and Verified` · `Creative: Morrow Sleep Static Ads - Ready for Review`.
  Use a stable retrieval domain such as System, Creative, Extraction, Revenue, Client, Research, Content, Ops, or Personal. The handoff H1, manifest title, and native Codex task title must match exactly.
- **Slug** (`--slug`, kebab, stable across resumes — filename + thread key): `[project-or-client]-[work-type]`, e.g. `trendscale-script-rework`, `mybpm-week1-launch`. **If this session RESUMED a thread, reuse that thread's existing slug** so `/resume` keeps one clean row (no v1/v2/v3 pile-up); the Title carries the `vN`, the slug does not.

**Then persist the exact source durably — the temp dir is ephemeral (macOS clears it on reboot):**
// turbo
```bash
python execution/handoff_store.py save "<exact-handoff-source-path>" \
  --thread "<thread-slug>" \
  --status "<active|blocked|ready|mid-build|done>" \
  --hint "<one line: the very next action>" \
  --unfinished "<one line: what's still left>" \
  --pin --json

python execution/handoff_store.py verify "<thread-slug>" \
  --source "<exact-handoff-source-path>" --json
```
- **`--thread`**: if this session RESUMED a thread, reuse that exact thread slug so the menu keeps one clean row (no v1/v2/v3 pile-up). New work → a short kebab slug for the work-stream (e.g. `jen-listings`, `mybpm-launch`, `handoff-resume-loop`).
- **`--status`**: where the thread stands now — `ready` (just ship), `blocked` (waiting on you/a client), `mid-build`, `done` (auto-hidden from the menu), or `active`.
- Exact source identity is the default: save from the path returned by `/handoff`, retain the JSON save receipt, and require the verify receipt to pass before downstream closeout work. `--from-temp` remains a compatibility fallback, but it must filter by slug and refuse ambiguous or mismatched candidates.
- **`--pin`**: floats this just-closed session to the top of `/resume` and records the session pin, so the work surfaces by name and the Stop-hook pin backstop stays quiet. This is the consistent session-pin formula (see `/pin-session` for the on-demand version).

That frontmatter is what makes `/resume` a triage board (thread · status · what's-unfinished) instead of a flat list. (Resume side: `session-kickoff.md` Step 0 + `/resume`. The Stop hook nudges if `/handoff` ran but save didn't.)

> **Never Read `.agent/handoffs/index.md` whole (~99KB)** — query handoffs via `python execution/handoff_store.py list` / `latest` instead.

Then surface the **titled retrieval block** in chat — RENDER it from the just-written handoff's frontmatter and sections (quote, don't rewrite; the handoff is the single model-composed session narrative and this block is a derived view of it). ALWAYS emit it in this shape, so Farrice sees the name, where it lives, and how to get back in, with zero renaming on his end:

```markdown
## <Session Title, from the naming convention above>
**Saved + pinned:** `.agent/handoffs/<date>-<slug>.md` · thread `<thread>` · status `<status>`
**Retrieve anytime:** `/resume <thread>`   (or just `/resume` — the pin surfaces it by name)

**Completed:** [2-3 bullets of what was built]
**Remaining priority:** [next immediate task — also passed to /handoff]
**Hot experts this session:** [experts loaded — so next session can warm-start]
```

Pull `<date>-<slug>` from the `saved:` line the save command printed (do not guess the path). The Title, thread, and slug all follow the naming convention above; never ask Farrice to supply or rename any of them.

If the `/handoff` skill is unavailable (not installed), fall back to emitting the full block inline with the fields above plus **Core context to load:** [paths to the 2-3 essential deliverable files].

### 1.3 Codex-Native Coordinator
// turbo
For a Codex task, create a closeout manifest containing the task ID, exact
title, slug, status, project root, exact handoff source, core paths, and only
the task-owned paths eligible for Git staging. Then run:

```bash
python3 execution/codex_end_session.py run --manifest "<manifest.json>"
```

The JSON receipt is the decision surface. The Python coordinator owns exact
handoff save/verify, conservative organization, the shared closeout spine,
verifiers, manifest-scoped Git, remote-SHA proof, and the pointer-only global
registry under `~/.codex/end-session/`. Project-local handoffs remain canonical.

Codex app actions stay native and occur only after reading the receipt:

1. Call `set_thread_title` with `task_actions.title` for every meaningful task.
2. If `task_actions.pin` is true, call `set_thread_pinned` so `active`, `blocked`, `ready`, and `mid-build` work stays visible.
3. Call `set_thread_archived` only when `task_actions.archive` is true. A partial or failed closeout remains unarchived.

The approved Git policy permits automatic commit and push only when the current
branch is `codex/*`, the checkout is a dedicated Codex worktree, every staged
path is manifest-owned or closeout-generated, required verifiers pass, no
secret/deletion/collision/divergence blocker exists, and the remote SHA matches.
Never auto-commit, auto-merge, or auto-push `main`.

### 1.4 Run the Shared Closeout Spine
// turbo
The Codex coordinator invokes this form with the exact stored handoff:

```bash
python3 execution/end_session_closeout.py run --slug "<thread-slug>" \
  --handoff "<exact-stored-handoff-path>" --git-policy codex-owned
```
This is the deterministic closeout spine — it wires up everything the old
closeout preamble claimed but never physically ran: closeout intelligence
(`session_closeout_intelligence.py run --source end-session`, feeding routing
and performance feedback), a sovereign-memory episodic milestone record for
this session, a one-line entry in the COS journal so `/cos` surfaces the
close, an archived copy of `.agent/session-state.md`, and nudges for any
unresolved friction-ledger entries or open finalize debt. Every step reports
`CLOSEOUT <step>: OK|SKIP|FAIL — <detail>` and the sequence never halts on a
failed or skipped step. **Surface these `CLOSEOUT` lines in the closeout
answer** — skipped stores must stay visible to Farrice, not silently dropped.

### 1.5 Generate Insightful Momentum Follow-ups
// turbo
Run this step only after a valid, non-dry-run coordinator receipt and the native
task action have succeeded:

```bash
python3 execution/contextual_next_prompts.py \
  --objective "end-session closeout for [session label]" --format compact
```

`contextual_next_prompts.py` is the renderer — surface its output as the
completed closeout's 3 Next Prompts; do not re-compose it. If the receipt is
blocked, partial, invalid, or dry-run only, use the bounded blocker surface and
skip this step. This keeps lifecycle truth ahead of presentation polish.

### 2. Update Conversation Index
// turbo
Use a safe index stats check before any rebuild or update:

```bash
python3 execution/conversation_index.py stats
```

Only update a specific conversation when the current conversation id is known:
```bash
python execution/conversation_index.py update "$CURRENT_CONVERSATION_ID"
```

### 3. Git Checkpoint

For Codex, Git is owned by `codex_end_session.py` after the shared spine and
verifiers pass. It stages only manifest-owned paths plus closeout-generated
receipts, pushes only the current `codex/*` branch, verifies the remote SHA,
and writes an integration packet. It never merges or pushes `main`.

The legacy `end_session_closeout.py run --slug <slug>` invocation remains
available for Claude compatibility and retains its legacy commit-gate behavior.

The coordinator and `worktree_lane.py merge` share `.agent/lane-operation.lock`.
The coordinator acquires it before writing closeout state, and lane reconciliation
acquires it before sealing a lane. If either operation is active, the other parks
or exits cleanly; it must never seal a partially completed closeout.

---

## Deep Cleanup (`--deep`)

Run all steps above, plus:

### 3. Artifact Triage
Identify files in the current session's `brain/` directory:
- **Review queue**: Temp extractions, raw data dumps, rough drafts, ambiguous ownership, and unresolved self-heal findings
- **Keep**: Final offer docs, finished skills, deliverables

Never auto-delete or broadly archive files. Move only unambiguously task-owned
loose artifacts; leave uncertain files in the review queue.

### 4. Finalize Session Workspace
// turbo
If a session workspace exists:

```bash
python3 execution/session_workspace.py finalize
```

### 5. File Organization
// turbo
- Move intermediates to `.tmp/`
- Ensure deliverables are properly named
- Consolidate fragmented notes into canonical files

### 6. State Check
- Read `task.md`, mark completed items, roll over uncompleted items

---

## When to Use
- **Quick Handoff**: End of any session — costs almost nothing
- **Deep Cleanup** (`--deep`): After heavy sessions (extractions, multi-expert work, client deliverables)
- Skip entirely if the session was conversational with no artifacts produced

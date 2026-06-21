---
description: Run at the end of a deep-work session
---

# 🧹 /end-session — Session Handoff

> **Purpose**: Generate a clean handoff for the next session. Deep cleanup is optional — assets are already organized when produced.

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

**Then persist it durably — the temp dir is ephemeral (macOS clears it on reboot):**
// turbo
```bash
python execution/handoff_store.py save --from-temp
```
`--from-temp` auto-discovers the newest `handoff-*.md` the `/handoff` skill just wrote — no path to transcribe, which removes the main silent-failure mode. It copies the handoff into version-controlled `.agent/handoffs/`, then rebuilds a **self-contained** `LATEST.md` + `index.md` so `/session-kickoff` can deterministically resume it. Confirm the output shows `saved:` — **never skip this; it is the loop's backstop.** (Resume side lives in `session-kickoff.md` Step 0. The Stop hook also nudges if a handoff was produced but never persisted.)

Then surface a 3-line pointer in chat so the human sees it at a glance without duplicating the full doc:

```markdown
## Session Handoff → `<temp-dir path to the /handoff doc>`
**Completed:** [2-3 bullets of what was built]
**Remaining priority:** [next immediate task — also passed to /handoff]
**Hot experts this session:** [experts loaded — so next session can warm-start]
```

If the `/handoff` skill is unavailable (not installed), fall back to emitting the full block inline with the fields above plus **Core context to load:** [paths to the 2-3 essential deliverable files].

### 2. Update Conversation Index
// turbo
Update the master conversation index with final artifacts and completion status:
```bash
python execution/conversation_index.py update <current-conversation-id>
```

### 3. Git Checkpoint (Optional)
// turbo
If the workspace is a Git repo, offer to commit:
> "Want me to commit? `git add . && git commit -m 'Session: [Label]'`"

Do not push without explicit confirmation.

---

## Deep Cleanup (`--deep`)

Run all steps above, plus:

### 3. Artifact Triage
Identify files in the current session's `brain/` directory:
- **Delete**: Temp extractions, raw data dumps, rough drafts
- **Keep**: Final offer docs, finished skills, deliverables

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

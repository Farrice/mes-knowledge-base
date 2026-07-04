---
description: Run at the end of a deep-work session
---

# 🧹 /end-session — Session Handoff

> **Purpose**: Generate a clean handoff for the next session. Deep cleanup is optional — assets are already organized when produced.

## Insightful Momentum Closeout Requirement

`/end-session` must not fall back to the old lightweight "Use Now / Harden /
Expand" prompt shell. The visible final answer is part of the repair surface.

For meaningful sessions, run the local renderer and preserve its enriched
fields in the final answer:

```bash
python3 execution/contextual_next_prompts.py --objective "[session closeout objective]"
```

The 3 Next Prompts must show the Insightful Momentum/frontier standard:

- action title that names the current session object
- Output/Capability Move
- Operator Insight
- Hidden Gap/Opportunity
- Capability Revealed
- copy-paste Prompt
- Expected output or What it entails
- Quality bar
- Skip condition when useful
- Suggested skills/workflows

If the renderer output is awkward, improve the objective and rerun it; do not
hand-author a generic legacy prompt block. Closeout suggestions should help the
next session start smarter, reveal a capability Farrice may not know to ask for,
and turn the session into an asset, proof check, benchmark, or next build
surface.

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

- **Title** (set it as the handoff doc's H1 — it becomes the session's retrievable name):
  `[Project or Client] — [Work Type][ vN if iterated] ([key scope])`
  Examples: `TrendScale Creative Strategist Trial — Script Rework v2 (JCKED + Puravita)` · `MyBPM Merch OS — Week 1 Launch Prep` · `Jen Listings — 6853 Willis Shoot Sheet`.
  Rules: Title Case; ` — ` (spaced) is the only sanctioned separator here and is exempt from the prose em-dash ban (it is a display title, not copy); append `vN` only when this iterates a thread that already shipped a version; keep the scope parenthetical to the 1-3 nouns that make it findable.
- **Slug** (`--slug`, kebab, stable across resumes — filename + thread key): `[project-or-client]-[work-type]`, e.g. `trendscale-script-rework`, `mybpm-week1-launch`. **If this session RESUMED a thread, reuse that thread's existing slug** so `/resume` keeps one clean row (no v1/v2/v3 pile-up); the Title carries the `vN`, the slug does not.

**Then persist it durably — the temp dir is ephemeral (macOS clears it on reboot):**
// turbo
```bash
python execution/handoff_store.py save --from-temp \
  --thread "<thread-slug>" \
  --status "<active|blocked|ready|mid-build|done>" \
  --hint "<one line: the very next action>" \
  --unfinished "<one line: what's still left>" \
  --pin
```
- **`--thread`**: if this session RESUMED a thread, reuse that exact thread slug so the menu keeps one clean row (no v1/v2/v3 pile-up). New work → a short kebab slug for the work-stream (e.g. `jen-listings`, `mybpm-launch`, `handoff-resume-loop`).
- **`--status`**: where the thread stands now — `ready` (just ship), `blocked` (waiting on you/a client), `mid-build`, `done` (auto-hidden from the menu), or `active`.
- `--from-temp` auto-discovers the newest `handoff-*.md` the `/handoff` skill just wrote (no path to transcribe — removes the main silent-failure mode). It writes frontmatter + body into version-controlled `.agent/handoffs/`, rebuilds `index.md` + `LATEST.md`. Confirm the output shows `saved:` — **never skip this; it's the loop's backstop.**
- **`--pin`**: floats this just-closed session to the top of `/resume` and records the session pin, so the work surfaces by name and the Stop-hook pin backstop stays quiet. This is the consistent session-pin formula (see `/pin-session` for the on-demand version).

That frontmatter is what makes `/resume` a triage board (thread · status · what's-unfinished) instead of a flat list. (Resume side: `session-kickoff.md` Step 0 + `/resume`. The Stop hook nudges if `/handoff` ran but save didn't.)

Then surface the **titled retrieval block** in chat. This is the standard closeout output — ALWAYS emit it verbatim in this shape, so Farrice sees the name, where it lives, and how to get back in, with zero renaming on his end:

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

### 1.5 Generate Insightful Momentum Follow-ups
// turbo
Run:

```bash
python3 execution/contextual_next_prompts.py --objective "end-session closeout for [session label]"
```

Use the rendered `Suggested follow-ups` block as the closeout's 3 Next Prompts.
Keep it concise if needed, but preserve the enriched fields. This step exists
because the old hand-authored closeout shape made the repair invisible to the
user.

### 2. Update Conversation Index
// turbo
Use a safe index stats check before any rebuild or update:

```bash
python3 execution/conversation_index.py stats
```

Only update a specific conversation when the current conversation id is known:
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

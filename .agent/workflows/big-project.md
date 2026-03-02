---
description: Manage complex, multi-step projects across session boundaries with checkpointing and per-batch quality gates
---

# Big Project Workflow

Use this workflow when a task is estimated at **20+ tool calls** or spans **multiple domains**. It prevents context degradation by planning session boundaries, enforcing per-batch quality gates, and using `task.md` as the state handoff file.

## Step 1: Scope the Project

Before any execution:

1. **Estimate total tool calls** (be honest — err on the high side)
2. **Break into phases** with clear deliverables per phase
3. **Create `task.md`** with phased checklist:
   ```markdown
   # [Project Name]

   ## Phase 1: [Name] — [Est. X tool calls]
   - [ ] Step 1
   - [ ] Step 2

   ## Phase 2: [Name] — [Est. Y tool calls]
   - [ ] Step 1
   ```

4. **Run Session Kickoff** (see `directives/session_kickoff.md`)

## Step 2: Set Session Boundaries

| Project Size | Recommended Session Length | When to Suggest Break |
|-------------|---------------------------|----------------------|
| 20-40 tool calls | 1 session | After each phase |
| 40-80 tool calls | 2 sessions | After 2 phases or at natural handoff |
| 80+ tool calls | 3+ sessions | After each phase, with checkpoint |

**At each boundary:**
1. Update `task.md` — mark completed items, note where you stopped
2. Write a 3-sentence "Resumption Context" at the top of `task.md`:
   ```markdown
   > **Resumption Context**: Completed phases 1-2. Phase 3 (verification) is next.
   > Key decision: We chose approach X over Y because [reason].
   > Known issue: [any blockers or edge cases discovered].
   ```
3. Suggest the user start a new conversation with: "Continue the [project name] — read `task.md` for context."

## Step 3: Per-Batch Quality Gates

After completing each phase/batch:

1. **Verify the deliverable** — does it match what was planned?
2. **Check for regression** — did this batch break anything from the previous batch?
3. **Update `task.md`** — mark items `[x]` and note any deviations from plan

If a quality gate fails:
- **Minor issue**: Fix inline, note in `task.md`, continue
- **Major issue**: Stop, update plan, get user approval before continuing

## Step 4: Handoff Between Sessions

When resuming in a new conversation:

1. **Read `task.md`** — it's the single source of truth
2. **Read the Resumption Context** — it has the essential decisions and state
3. **Run Session Kickoff** — re-declare active protocols for the new session
4. **Continue from where you stopped** — don't restart or re-plan completed work

## When NOT to Use This Workflow

- Simple tasks (< 20 tool calls)
- Single-domain requests with clear scope
- Quick fixes, lookups, or one-shot generation
- User explicitly says "just do it quickly"

---

*Created: 2026-02-17 | Big Project Workflow v1.0*

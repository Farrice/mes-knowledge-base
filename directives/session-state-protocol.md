# Session State Anchor Protocol

> **Purpose**: Prevent context drift after compaction by writing checkpoint files at key moments. When compaction occurs, re-read the anchor to recover precise context instead of relying on lossy summaries.
> **State File**: `.agent/session-state.md`
> **Inline version**: A compact version of the checkpoint triggers is embedded in `CLAUDE.md` under "Session State Checkpoints" for enforcement. This file contains the full protocol details.
> **Created**: 2026-02-27

---

## Why This Exists

When Claude Code compacts conversations (summarizing older turns to free context), fine details get lost:
- Decisions and their rationale flatten into vague summaries
- Expert context and patterns applied get dropped
- The "thread" of multi-step work loses precision
- Follow-up work drifts from the original validated intent

**Session state anchors** are checkpoint files that survive compaction. Re-reading them restores precise context.

---

## Anchor Format

Write to `.agent/session-state.md`:

```markdown
# Session State Anchor
> Last updated: [ISO timestamp]

## Active Task
[1-2 sentence description of what we're working on]

## Intent (Validated)
- **Deliverable**: [what]
- **Audience**: [who]
- **Success criteria**: [what "done" looks like]

## Decisions Made
- [Decision 1]: [choice made] — [rationale in <10 words]
- [Decision 2]: [choice made] — [rationale]

## Experts Deployed
- [Expert Name]: [what they contributed, 1 line]
- Patterns applied: [list by name]

## Hot Context Stack
- [Expert Name] | Tier [1/2] | Files: [SKILL.md, genius.md, etc.]
- [Expert Name] | Tier [1/2] | Files: [SKILL.md]

## Key Findings (Compressed)
- [Finding 1]: [1-line]
- [Finding 2]: [1-line]

## Files Created/Modified This Session
- [path]: [what it is]

## Current Phase
[Where we are in the workflow]

## Next Steps
1. [Next action]
2. [Next action]
```

---

## Hot Context Stack

When an expert is loaded during a conversation (Tier 1+ file read), they become **hot**. Hot experts are tracked in the session state anchor so they survive compaction.

### Rules

1. **Before loading any expert**, check the Hot Context Stack
2. If hot at **Tier 1** and Tier 2 is needed → only read `genius.md` (incremental load)
3. If hot at **Tier 2** → skip all file reads, expert is fully loaded
4. Hot status persists for the **entire conversation** (cleared on new conversation)
5. Write hot experts to the session state anchor so they survive compaction

### Anti-Pattern

Re-reading `SKILL.md` for the same expert twice in one conversation wastes **~1,350 tokens** per redundant load. Always check Hot Context Stack first.

---

## When to Write

| Trigger | What to Anchor |
|---------|---------------|
| After intent validation (DICE protocol completes) | The validated intent so it survives compaction |
| After major analysis (research, extraction, brief) | Key findings and methodology |
| After expert deployment (skill loaded and applied) | Which experts, which patterns, what they produced |
| After any user decision (chose direction, confirmed approach) | The decision and rationale |
| Before spawning sub-agents | Current state so main thread resumes cleanly |
| When 10+ file reads have occurred in the session | Preemptive anchor before context fills |

---

## When to Read

| Trigger | Why |
|---------|-----|
| After compaction occurs (context feels thin, prior details seem vague) | Recover precise context |
| After returning from sub-agent work | Pick up the main thread |
| At start of a continued/resumed session | Restore prior session state |
| When uncertain about a prior decision | Verify against the anchor |

---

## Staleness Warning

The anchor includes a timestamp. If the current conversation has diverged significantly from the anchored state (e.g., user changed direction mid-session), treat the anchor as **directional guidance**, not gospel. Update the anchor to reflect the new direction.

---

## Execution Integration

Session state functions are available in `execution/checkpoint_manager.py`:
- `save_session_state(state)` — Writes the anchor file
- `load_session_state()` — Reads and returns anchor contents

These keep state management deterministic (Layer 3) while the agent (Layer 2) decides when to trigger them.

---

## Graceful Failure

If the state file doesn't exist or can't be read, fall back to the compacted summary. No hard dependency. The anchor is an enhancement, not a requirement.

---

## 3-Mode Compaction

When compaction is needed (context filling up, long session, pre-sub-agent), use the appropriate mode. **Do NOT default to Full.** Match the mode to the situation.

### Mode Selection

| Situation | Mode | What Survives |
|-----------|------|---------------|
| Starting a sub-agent, need clean context | **Full** | Everything compressed into 9 sections |
| Continuing same task, early context stale | **Partial Older** | Old turns summarized, recent 5-8 turns verbatim |
| User changed direction mid-session | **Partial Recent** | Old context preserved, new direction summarized |

### Mode 1: Full Compaction

**When:** Sub-agent spawn, complete topic change, or explicit user request.

Write the full session state anchor with all 9 sections (Active Task, Intent, Decisions, Experts, Hot Context, Findings, Files, Phase, Next Steps). This replaces **all** prior context.

**Key rule:** Recent user messages (last 3-5) are always preserved verbatim in a `## Recent User Messages` section, even in full compaction. User words survive — your summaries of their words do not.

### Mode 2: Partial Older

**When:** Same task continues but early conversation is stale (e.g., research phase complete, now in execution). Most common mode.

1. **Summarize** turns 1 through N-8 into a compressed `## Prior Context (Summarized)` section
2. **Keep** the last 8 turns verbatim (these contain the active working thread)
3. **Always preserve**: decisions, expert deployments, and file paths from old turns

Format addition to anchor:
```markdown
## Prior Context (Summarized)
[Compressed summary of old turns — decisions, findings, expert outputs]
[Specific file paths and line numbers mentioned]

## Preserved Recent Thread
[Last 8 turns kept verbatim — this is the active working context]
```

### Mode 3: Partial Recent

**When:** User pivoted directions. Old context (the original approach) is valuable reference; new direction needs summarizing because it's still forming.

1. **Keep** old context intact (it contains the validated approach/research)
2. **Summarize** only the new direction turns into a `## Direction Change` section
3. **Flag** what changed and why

Format addition to anchor:
```markdown
## Direction Change
- **Original approach**: [what we were doing]
- **Pivot trigger**: [what the user said/decided]
- **New direction**: [compressed summary of new approach]
- **What carries forward**: [decisions/findings from old context that still apply]
```

### Analysis-Then-Summary Pattern

Before writing any compaction summary, **draft an analysis first**:

1. **Analysis pass** (internal, not written to file): List every decision, finding, expert output, and file path from the conversation. This forces you to scan rather than paraphrase.
2. **Summary pass** (written to anchor): Compress the analysis into the appropriate format. Cut prose, keep facts.

**Anti-pattern:** Paraphrasing conversation flow ("We discussed X, then moved to Y"). This loses specifics. Instead: "Decided: X over Y because Z. Files: `path/to/file.py` modified lines 45-80."

### Preservation Rules (All Modes)

These items **always survive** compaction, regardless of mode:
- ✅ User decisions and their rationale
- ✅ File paths and line numbers
- ✅ Expert names and what they produced
- ✅ Code snippets under 20 lines
- ✅ Error messages and their resolutions
- ✅ The current chain step

These items can be safely compressed:
- ❌ Reasoning chains ("I considered A, B, C and chose A")
- ❌ Tool call metadata (timestamps, token counts)
- ❌ Intermediate research that led to a final finding
- ❌ Greeting/acknowledgment turns

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-04 (chain_runner session checkpoint) |
| **Activation Count** | 60 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (checkpoint written to `.agent/session-state.md`), update the date and increment count.

*Created: 2026-02-27 | Context Engine v1.0*

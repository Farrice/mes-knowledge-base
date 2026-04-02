---
description: Run at the start of every new chat
---

# 🚀 Session Kickoff

Two modes: **Sport Mode** (fast, default) and **Race Mode** (full ceremony, for deep work).

## Mode Detection

// turbo
Determine which mode to use:

**Race Mode activates when ANY of these are true:**
- User explicitly passes `--deep` flag
- Request involves an `/extract` workflow
- Request involves `/parallel-swarm`, `/swarm`, or `/deep-research`
- Request involves client deliverable work
- Request invokes `/big-project`
- Complexity assessment would be Heavy (20+ tools)

**Sport Mode is the default for everything else.**

---

## 🏎️ Sport Mode (Default — 3 Tool Calls Max)

### Step 1: Label + Assess
// turbo
Generate a conversation label from the user's first message. Do this in-head — no file reads needed.

**Format**: `[Domain] — [Specific Goal]`
**Rules**: Max 6 words. Lead with domain.

Score intent in-head using the memorized formula:
+1 Deliverable | +1 Audience | +1 Context | +1 End state | +1 Specific language

### Step 2: Present Compact Kickoff
// turbo
Output a single compact block:

```
🏎️ Sport Mode | **[Label]** | Intent: [X/5] | Ready.
```

No protocol declarations. No system health check. No intent pipeline file read.

### Step 3: Begin Work
Proceed directly to the task. Workspace folder creation is **deferred** — it only happens when the first asset is produced (via `session_workspace.py create-if-needed`).

---

## 🏁 Race Mode (Full Ceremony — `--deep`)

### Step 1: Label the Conversation

// turbo
Read the user's first message and generate a **conversation label**.

**Format**: `[Domain] — [Specific Goal]`

**Examples**:
- `LinkedIn — Profile Rewrite & Outreach Scripts`
- `Offer Design — AI Brain Build $5K Sprint`
- `System — GEMINI.md Ignition Redesign`
- `Research — Shadow Market Analysis for KDP`
- `Extraction — Jeremy Haynes Mindset Systems`

**Rules**:
- Max 6 words
- Lead with the domain/category so conversations cluster naturally
- Be specific enough to distinguish from similar conversations
- If the session involves multiple domains, use the primary one

**Output**: State the label clearly so the user can copy it to the sidebar.

### Step 1.5: Create Session Workspace & Register

// turbo
Create the session's working directory immediately:

```bash
python3 execution/session_workspace.py create "[Domain]" "[Label]" --conv-id "[conversation-id-if-available]"
```

Capture the `SESSION_PATH` from the output. Subfolders: `assets/`, `drafts/`, `deliverables/`, `research/`.

When producing an asset during the session, log it:
```bash
python3 execution/session_workspace.py log-asset "/path/to/file" --type "Deliverable" --desc "Description"
```

// turbo
Update the master conversation index:
```bash
python execution/conversation_index.py update <current-conversation-id>
```

### Step 2: Detect Task Type & Complexity

// turbo
Assess the incoming request:

| Field | Options |
|-------|---------|
| **Task Type** | Creative / Research / Strategy / Build / Debug / Extraction / Multi-Domain |
| **Complexity** | Light (1-5 tools) / Medium (5-20 tools) / Heavy (20+ tools) |
| **Domain(s)** | Match against expert routing table |

If **Heavy** complexity → recommend `/big-project` workflow.

### Step 3: Declare Active Protocols

// turbo
Present the full kickoff block:

```
## 🏁 Race Mode Session

**Conversation Label**: [Domain — Specific Goal]
**Session Workspace**: `sessions/[folder-name]/`
**Task Type**: [type]
**Complexity**: [level]

**Active Protocols**:
- ✅ Expert Routing — [which experts/domains detected, or "scanning"]
- ✅ Quality Gate — post-output check active
- ✅ Intent Refiner — sharpness score [X/5]
- ⏭️ Parallel Thought — [active or reason for skip]
- ⏭️ Perplexity Research — [active or reason for skip]
- 📊 System Health — [run `python execution/system_health.py --quick` and report any CRITICAL items]

**Session Plan**: [1-2 sentence approach summary]

Ready to go.
```

### Step 4: Score Intent & Route

// turbo
Score the user's input:

- **Score 1-3**: Run `/validate-intent` before proceeding
- **Score 4-5**: Confirm interpretation and proceed to execution
- **If a deployed skill matches**: Run `/recommend` to surface the right tools

### Step 5: Begin Work

After the kickoff block is presented and any needed intent refinement is done, proceed with the task.

---

## When to Use
- **Every new conversation** where work is expected (not quick questions)
- When the user explicitly runs `/session-kickoff`
- When switching to a fundamentally different task mid-conversation
- **Sport Mode**: Default. Quick tasks, follow-ups, conversations, single-expert work
- **Race Mode**: Extractions, swarms, client work, complex multi-expert sessions

## When NOT to Use
- Quick factual lookups ("what time is it?")
- Single-line answers
- Bug fix follow-ups within an already-labeled session
- User says "just do it" or "skip the kickoff"

---

## Why This Exists

Two problems this solves:
1. **Retrieval**: Labels make every session findable in the sidebar.
2. **Operating level**: Race Mode ensures deep-work sessions get full protocol activation.

**Why two modes**: Sport Mode prevents the system from spending 10+ tool calls on ceremony for tasks that only need 5 tool calls total. Race Mode preserves the full power for sessions that need it.

---

## Reference
This workflow implements:
- `directives/intent-pipeline.md` — Stages 1-2 (Race Mode only)
- `directives/expert_auto_routing.md` — Domain detection (Race Mode only)

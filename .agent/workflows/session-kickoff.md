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

## Step 0: Resume Check (both modes — deterministic)

// turbo
Before labeling or planning, check for a prior handoff:
```bash
python execution/handoff_store.py latest
```
- **Exit 0 (prints a path)** → read `.agent/handoffs/LATEST.md` (self-contained — the full latest handoff is embedded, no second file needed) and open the kickoff with a one-line resume offer:
  `📋 Last session: [title] ([date]). Resume where you left off, or start fresh?`
  If the user confirms, continue from the handoff's "Next session focus" / "Remaining priority".
- **Exit 1 / `(no handoffs yet)`** → proceed normally.

**Race Mode note:** if the user confirms a resume, do NOT create a fresh workspace in Step 1.5 — reuse the prior session's `SESSION_PATH` from the handoff so the session record doesn't fragment. Only create a new workspace when starting fresh.

This is the resume side of the loop (save side = `end-session.md` Step 1). Resume is **one command**: `/session-kickoff` surfaces the latest handoff automatically — no path to remember.

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

### Step 2.5: Maintenance Pulse (Silent — 1 Read)
// turbo
Read `.agent/session-state.md` and check:
- If "days since /maintenance" > 7 → append to kickoff: `⚡ /maintenance overdue`
- If "days since /calibrate" > 30 → append: `⚡ /calibrate due`
- If revenue-outcomes.json has 0 entries for current month → append: `⚡ /revenue-track pipeline`

Only show alerts that apply. No alerts = no output. This adds zero friction when everything is current.

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
Update the master conversation index with this new session:
```bash
python execution/conversation_index.py update <current-conversation-id>
```
This ensures this conversation is findable via `/find-context` even before the session completes.

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

**Rules**:
- Only show protocols relevant to the task
- Be honest about skips — "skipped: no research needed" beats silence
- If complexity is Heavy, add session boundary guidance (when to suggest a new chat)

### Step 3.5: Autoresearch Evolution Check

// turbo
Run the autoresearch readiness check to surface any skills due for evolution or recurring intelligence gaps:

```bash
python3 execution/gap_analysis.py recommendations 2>/dev/null || echo "gap_analysis: no data yet"
```

**Check these conditions:**

| Condition | Action |
|-----------|--------|
| Any skill has 5+ new Performance Log entries since its last evolution | Flag: **"[skill] is due for `/skill-evolution`"** |
| Gap log has 3+ entries in the same domain | Flag: **"Phase 4 alert: [domain] has recurring gaps — consider extraction"** |
| Any skill's weakest dimension < 6/10 average | Flag: **"[skill] needs attention — [dimension] averaging [score]/10"** |

**If any flags fire**, append them to the kickoff block:

```
**Autoresearch Alerts**:
- [flag 1]
- [flag 2]
```

**If no flags fire**, skip this section silently — don't clutter the kickoff.

Also check `.agent/gap-log.md` for any recent entries (last 7 days):

```bash
tail -20 .agent/gap-log.md 2>/dev/null || echo "gap-log: empty"
```

---

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

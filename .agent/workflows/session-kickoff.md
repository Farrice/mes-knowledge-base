---
description: Run at the start of every new chat to label the conversation, declare active protocols, and set the system to full operating level
---

# 🚀 Session Kickoff

Run this at the **start of every new conversation** (or auto-trigger when detecting a new chat). Two jobs: label the conversation for retrieval, and activate the right protocols so we're operating at system level from word one.

## Step 1: Label the Conversation

// turbo
Read the user's first message (or the context that triggered this chat) and generate a **conversation label** — a short, descriptive title that will make this conversation findable later in the sidebar.

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

**Output**: State the label clearly so the user can copy it to the sidebar or so the system can auto-apply it.

## Step 2: Detect Task Type & Complexity

// turbo
Assess the incoming request:

| Field | Options |
|-------|---------|
| **Task Type** | Creative / Research / Strategy / Build / Debug / Extraction / Multi-Domain |
| **Complexity** | Light (1-5 tools) / Medium (5-20 tools) / Heavy (20+ tools) |
| **Domain(s)** | Match against expert routing table in GEMINI.md |

If **Heavy** complexity → recommend `/big-project` workflow.

## Step 3: Declare Active Protocols

// turbo
Present the kickoff block:

```
## 🚀 Session Kickoff

**Conversation Label**: [Domain — Specific Goal]
**Task Type**: [type]
**Complexity**: [level]

**Active Protocols**:
- ✅ Expert Routing — [which experts/domains detected, or "scanning"]
- ✅ Quality Gate — post-output check active
- ✅ Intent Refiner — sharpness score [X/5]
- ⏭️ Parallel Thought — [active or reason for skip]
- ⏭️ Perplexity Research — [active or reason for skip]

**Session Plan**: [1-2 sentence approach summary]

Ready to go.
```

**Rules**:
- Only show protocols relevant to the task
- Be honest about skips — "skipped: no research needed" beats silence
- If complexity is Heavy, add session boundary guidance (when to suggest a new chat)

## Step 4: Score Intent & Route

// turbo
Read `directives/intent_refiner.md` and score the user's input:

- **Score 1-3**: Run `/validate-intent` before proceeding
- **Score 4-5**: Confirm interpretation and proceed to execution
- **If a deployed skill matches**: Run `/recommend` to surface the right tools

## Step 5: Begin Work

After the kickoff block is presented and any needed intent refinement is complete, proceed with the task.

---

## When to Use
- **Every new conversation** where work is expected (not quick questions)
- When the user explicitly runs `/session-kickoff`
- When switching to a fundamentally different task mid-conversation

## When NOT to Use
- Quick factual lookups ("what time is it?")
- Single-line answers
- Bug fix follow-ups within an already-labeled session
- User says "just do it" or "skip the kickoff"

---

## Why This Exists

Two problems this solves:
1. **Retrieval**: The sidebar is a graveyard of untitled conversations. Labels make every session findable.
2. **Operating level**: Without explicit protocol activation, conversations drift into generic LLM mode. The kickoff block forces system-level work from the start.

---

## Reference
This workflow implements:
- `directives/session_kickoff.md` — Protocol declaration format and rules
- `directives/intent_refiner.md` — Sharpness scoring (via Step 4)
- `directives/expert_auto_routing.md` — Domain detection (via Step 3)

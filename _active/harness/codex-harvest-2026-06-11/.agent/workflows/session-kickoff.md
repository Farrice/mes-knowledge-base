---
description: Run at the start of every new chat
---

# 🚀 Session Kickoff

Two modes: **Sport Mode** (fast visible ceremony) and **Race Mode** (full ceremony), governed by a separate depth dial: **Light / Standard / Deep / Parallel**.

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

**Sport Mode is the default visible kickoff for everything else, but the operating depth defaults to Standard unless the task is clearly Light.**

## Session Naming Protocol

Use `/Users/farricecain/.codex/skills/session-naming-protocol/SKILL.md` if present.

For meaningful work, generate a retrieval-first session title once intent is clear:

```text
[Domain]: [Specific Object] - [Outcome]
```

Also keep a short label for compact kickoff displays:

```text
[Domain]: [Specific Object]
```

Use domains that cluster naturally: System, Creative, Extraction, Revenue, Client, Research, Content, Ops, Personal. Skip naming ceremony for tiny factual answers unless the user asks.

## Depth Dial

Use `semantic_libraries/antigravity/primitives/high-floor-operator-os.md`.

| Depth | Trigger | Behavior |
|---|---|---|
| Light | factual lookup, tiny rewrite, simple confirmation, one-command check, or user asks for light | answer directly, skip ceremony, avoid slop |
| Standard | default for creative, strategic, build, extraction, offer, writing, client, workflow, or system conversations | route task, use best-fit stack, verify feasible claims |
| Deep | high-stakes, revenue-critical, client-facing, system-changing, ambiguous, or user asks for best/world-class/savant-level | full arsenal stack, critique/validation, highest bar |
| Parallel | user explicitly asks for delegated agents, parallel agents, subagents, or swarm | true Codex subagents with briefing packets |

Apply `semantic_libraries/antigravity/references/no-lazy-path-gate.md` for Standard and Deep work.

---

## 🏎️ Sport Mode (Default — 3 Tool Calls Max)

### Step 1: Label + Assess
// turbo
Generate a conversation label from the user's first message. Do this in-head — no file reads needed.

**Format**: `[Domain]: [Specific Object]`
**Retrieval title format**: `[Domain]: [Specific Object] - [Outcome]`
**Rules**: Lead with domain. Make the object specific enough to distinguish this session from similar work.

Score intent in-head using the memorized formula:
+1 Deliverable | +1 Audience | +1 Context | +1 End state | +1 Specific language

### Step 2: Present Compact Kickoff
// turbo
Output a single compact block:

```
🏎️ Sport Mode | **[Short label]** | Intent: [X/5] | Ready.
```

No protocol declarations. No system health check. No intent pipeline file read.

### Step 2.5: Maintenance Pulse (Silent — 1 Read)
// turbo
Read `.agent/session-state.md` and check:
- If "days since /maintenance" > 7 → append to kickoff: `⚡ /maintenance overdue`
- If "days since /calibrate" > 30 → append: `⚡ /calibrate due`
- If revenue-outcomes.json has 0 entries for current month → append: `⚡ /revenue-track pipeline`

Only show alerts that apply. No alerts = no output. This adds zero friction when everything is current.

### Step 2.75: Steering Pulse (Standard/Deep Only)
// turbo
If the request is Standard or Deep, append a compact Operator Coach block:

```markdown
**Steering:** Depth: [Standard/Deep]. Best path: [likely command/workflow/stack] - [why]. Watch: [one practical risk/opportunity]. Fastest decision: [choice that would speed the session].
```

Skip this only for Light work unless the user explicitly asks for steering.

### Step 3: Begin Work
Proceed directly to the task. Workspace folder creation is **deferred** — it only happens when the first asset is produced (via `session_workspace.py create-if-needed`).

---

## 🏁 Race Mode (Full Ceremony — `--deep`)

### Step 1: Label the Conversation

// turbo
Read the user's first message and generate a **conversation label** plus a retrieval title.

**Label format**: `[Domain]: [Specific Object]`
**Retrieval title format**: `[Domain]: [Specific Object] - [Outcome]`

**Examples**:
- `LinkedIn: Profile Rewrite - Outreach Scripts`
- `Offer Design: AI Brain Build - $5K Sprint`
- `System: GEMINI.md Ignition - Harness Redesign`
- `Research: KDP Shadow Market - Opportunity Map`
- `Extraction: Jeremy Haynes - Mindset Systems Skill`

**Rules**:
- Lead with the domain/category so conversations cluster naturally
- Be specific enough to distinguish from similar conversations
- Include the outcome in the retrieval title so the session is worth opening later
- If the session involves multiple domains, use the primary one

**Output**: State the retrieval title clearly so the user can copy it to the sidebar.

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

Before choosing a durable artifact path, classify it through the global organization router:

```bash
python3 execution/artifact_router.py classify "/path/to/file"
```

Use the canonical `_active/<project-slug>/` route when the router is confident. Keep ambiguous outputs in the router inbox instead of inventing a one-off folder.

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
| **Depth** | Light / Standard / Deep / Parallel |
| **Domain(s)** | Match against expert routing table |

If **Heavy** complexity → recommend `/big-project` workflow.

### Step 3: Declare Active Protocols

// turbo
Present the full kickoff block:

```
## 🏁 Race Mode Session

**Conversation Label**: [Domain: Specific Object]
**Retrieval Title**: [Domain: Specific Object - Outcome]
**Slug**: yyyy-mm-dd-[domain]-[object]-[outcome]
**Keywords**: [5-8 searchable terms]
**Session Workspace**: `sessions/[folder-name]/`
**Task Type**: [type]
**Complexity**: [level]
**Depth**: [Light / Standard / Deep / Parallel]

**Active Protocols**:
- ✅ Expert Routing — [which experts/domains detected, or "scanning"]
- ✅ Quality Gate — post-output check active
- ✅ Intent Refiner — sharpness score [X/5]
- ⏭️ Parallel Thought — [active or reason for skip]
- ⏭️ Perplexity Research — [active or reason for skip]
- 📊 System Health — [run `python execution/system_health.py --quick` and report any CRITICAL items]

**Session Plan**: [1-2 sentence approach summary]

**Steering Prompt**:
- Best path: [likely workflow/path/stack] - [why this is the fastest clean route]
- Watch: [one hidden opportunity or risk that materially affects speed, quality, risk, or value]
- Fastest decision: [one decision from the user that would improve execution]

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

## Mid-Session Steering Checkpoints

For Standard and Deep work, add a brief Operator Coach checkpoint after a major decision, validation result, route change, or build milestone:

```markdown
## Steering Checkpoint
- **What changed:** [state update]
- **Next best fork:** [recommended path]
- **Tradeoff to watch:** [risk/opportunity]
```

Keep this to 2-3 bullets and continue the work unless the user needs to choose.

## No-Lazy-Path Gate

For Standard and Deep work, do not proceed with:

- generic one-pass output
- a single weak workflow when a stack is available
- unsupported claims of agent/subagent work
- shallow steering paths
- missing verification for local/system claims that are cheap to check

Use Light only when the task is objectively trivial or the user asks for it.

---

## When to Use
- **Every new conversation** where work is expected (not quick questions)
- When the user explicitly runs `/session-kickoff`
- When switching to a fundamentally different task mid-conversation
- **Sport Mode**: Default visible kickoff for Light and many Standard tasks
- **Race Mode**: Extractions, swarms, client work, complex multi-expert sessions
- **Standard Depth**: Default operating floor unless clearly Light
- **Deep Depth**: High-stakes, revenue/client/system, ambiguous, or best/world-class/savant-level work

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
- `semantic_libraries/antigravity/primitives/high-floor-operator-os.md` — Light / Standard / Deep / Parallel operating depth
- `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md` — Operator Coach steering for Standard and Deep work

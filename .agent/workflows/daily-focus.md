---
description: Generate today's focused task breakdown for a compressed 1-3 hour work window — ruthless prioritization, time blocks, and exit criteria
---

# /daily-focus — Compressed Work Block Optimizer

Turn your limited daily window into maximum output. Loads this week's plan, checks what's done, assesses your energy, and generates a focused task breakdown with specific commands to run.

## Usage

```
/daily-focus
/daily-focus --hours 2
/daily-focus --hours 1 --energy low
/daily-focus --hours 3 --energy high --focus content
```

## When to Use

- Every work session (before you start)
- When you have limited time and need to know exactly what to do
- When energy is low and you need the system to decide for you

---

## Steps

### 1. Load Context

Read the following (sequential — fast reads, no agents needed):

1. **Weekly pulse** (`.tmp/weekly-pulse/week-[latest].md`) — this week's priorities and daily plan
2. **Recent session state** (`.agent/session-state.md`) — what was in-flight last session
3. **Recent `.tmp/` outputs** — quick check for completed work since last focus

If no weekly pulse exists: "No weekly pulse found. Run `/weekly-pulse` first for best results, or I'll generate a standalone focus based on your FARRICE.md goals."

### 2. Assess Parameters

Determine from flags or by asking:

| Parameter | Source | Default |
|-----------|--------|---------|
| Available hours | `--hours` flag | 2 hours |
| Energy level | `--energy` flag or ask | Medium |
| Focus area | `--focus` flag or weekly pulse | Auto from weekly pulse |

**Energy adjustment rules**:

| Energy | Task Selection | Cognitive Load |
|--------|---------------|---------------|
| **High** | Revenue-direct tasks, offer design, strategic decisions | Complex, creative, high-stakes |
| **Medium** | Content creation, research, workflow execution | Moderate, systematic |
| **Low** | Publishing ready drafts, scheduling, admin, journaling | Simple, therapeutic, completion-oriented |

### 3. Generate Today's Focus

```markdown
# Daily Focus: [Date]

**Available**: [X] hours | **Energy**: [level] | **Focus**: [area]

---

## Today's Mission (1 sentence)
[What does winning today look like?]

---

## Task Breakdown

### Block 1: [0:00-X:XX] — [VERB]: [Task Name]
**What**: [Specific description]
**Run**: `[exact slash command to use]`
**Output**: [What this produces]
**Done when**: [Specific exit criteria]

### Block 2: [X:XX-Y:YY] — [VERB]: [Task Name]
**What**: [Specific description]
**Run**: `[exact slash command to use]`
**Output**: [What this produces]
**Done when**: [Specific exit criteria]

### Block 3: [Y:YY-Z:ZZ] — [VERB]: [Task Name]  (if time allows)
**What**: [Specific description]
**Run**: `[exact slash command to use]`
**Done when**: [Specific exit criteria]

---

## Exit Criteria
You WIN today if: [1 clear sentence]

## If Time Runs Out
The ONE thing to finish before stopping: [most critical incomplete task]

## Tomorrow's Setup
Before you close: [save state, note where you left off]
```

### Task Verbs (Action Categories)

| Verb | Meaning | Example |
|------|---------|---------|
| **SHIP** | Publish/deliver something that's ready | Post a drafted LinkedIn piece |
| **CREATE** | Produce new content or assets | Run `/launch-day` or `/atomize` |
| **RESEARCH** | Investigate a question or opportunity | Run `/research-sprint` or `/hunt-trends` |
| **DESIGN** | Architect an offer, funnel, or strategy | Run `/design-offer` or `/brief` |
| **REFLECT** | Journal, process, mine patterns | Run `/daily-flywheel` |
| **PLAN** | Set up next steps, organize pipeline | Review pulse, update priorities |

### 4. Present and Start

Present the daily focus. Then offer: "Want me to run Block 1 right now?"

If the user says yes, immediately execute the first task's slash command.

---

## Parallelism Details

No sub-agents needed for this workflow — it's a fast sequential read + synthesis. Should complete in under 30 seconds.

## Error Handling

- If no weekly pulse exists: generate a standalone focus from FARRICE.md goals
- If energy is "low" and available hours < 1: suggest only SHIP or REFLECT tasks (lowest cognitive load)
- If all weekly priorities are completed: congratulate, suggest running `/weekly-pulse` to set new priorities

## Output Files

```
.tmp/daily-focus/
  focus-[date].md
```

---
description: Monday planning ritual — scan your situation, set priorities, and generate a daily breakdown for your compressed 1-3 hour work windows
---

# /weekly-pulse — Weekly Operating System

Your Monday ritual. Scans your current situation across revenue, content, and personal development, then generates a structured 5-day plan tuned to your compressed work windows.

## Usage

```
/weekly-pulse
/weekly-pulse --hours 10
/weekly-pulse --hours 8 --focus revenue
```

## When to Use

- Every Monday (or start of your work week)
- When you feel scattered and need clarity on what matters this week
- After a break when you need to reconnect with priorities

---

## Steps

### 1. Gather Context (Parallel — 3 Agents)

Spawn 3 Task tool sub-agents **in a single message** to scan different dimensions:

**Agent 1: Strategic Scanner**
```
You are a strategic advisor scanning Farrice's current business situation.

Read these files:
1. /Users/farricecain/Google Antigravity/FARRICE.md — goals, positioning, revenue targets
2. /Users/farricecain/Google Antigravity/.agent/session-state.md — recent session state (if exists)

Then use WebSearch to check:
- Any trending topics in Farrice's space (AI, solopreneurship, personal development, content creation)
- Any market movements that create urgency or opportunity

Produce a situation assessment:

## Strategic Scan

### Revenue Status
- Current income status relative to $10-20K/month target
- Most promising revenue path right now (based on FARRICE.md goals)

### Market Signals
- 2-3 trending topics or conversations relevant to Farrice's positioning
- Any time-sensitive opportunities (trending format, cultural moment, platform change)

### Momentum Check
- What's been working recently (if session state available)
- What's stalled or needs attention

Write to: .tmp/weekly-pulse/scan-strategic.md
```

**Agent 2: Content Pipeline Scanner**
```
You are a content operations manager auditing the pipeline.

Check these locations for recent work:
1. .tmp/daily-flywheel/ — recent flywheel outputs
2. .tmp/launch-day/ — recent launch day outputs
3. .tmp/atomize/ — recent atomized content
4. .tmp/ip-flywheel/ — IP flywheel outputs
5. .tmp/content-sprint/ — content sprint outputs

Produce a pipeline status:

## Content Pipeline Status

### Recently Created (ready to publish)
- [List any completed but unpublished content pieces]

### In Progress (needs finishing)
- [List any partial drafts or works in progress]

### Content Calendar Gaps
- [What platforms haven't had fresh content recently?]
- [Any content types that are overdue?]

### Sleeping Giants
- [Skills/agents that haven't been deployed recently but could produce high-impact content]
- Check SKILL_INDEX.md for skills not referenced in recent .tmp/ outputs

Write to: .tmp/weekly-pulse/scan-content.md
```

**Agent 3: Energy & Theme Scanner**
```
You are a personal advisor scanning for energy patterns and emerging themes.

Check these locations for recent journaling/personal development work:
1. .tmp/daily-flywheel/ — recent flywheel entries (look for emotional themes)
2. Any recent files matching .tmp/*/journal* or .tmp/*/reflection*

If no recent journal entries exist, skip this and note: "No recent journal entries found — recommend starting the week with /daily-flywheel"

If entries exist, analyze:

## Energy & Theme Scan

### Recurring Themes (last 1-2 weeks)
- [What topics/emotions keep appearing?]
- [Any pattern shifts? (e.g., scarcity → abundance, doubt → clarity)]

### Energy Pattern
- [Based on writing tone: is energy high, medium, or low?]
- [Are entries more reflective (low energy) or action-oriented (high energy)?]

### Emerging IP Angles
- [Any personal insights that could become content or offers?]
- [Any "aha moments" worth developing into a framework?]

Write to: .tmp/weekly-pulse/scan-energy.md
```

### 2. Synthesize the Weekly Plan

After all 3 agents return, read their outputs and produce the weekly pulse:

```markdown
# Weekly Pulse: [Date Range]

**Available hours**: [from --hours flag or default 10]
**Primary focus**: [from --focus flag or auto-detected from strategic scan]

---

## This Week's Top 3 Priorities

### Priority 1: [Most revenue-impactful move]
- **Why now**: [urgency/timing from strategic scan]
- **Command to run**: [specific slash command]
- **Time needed**: [hours]
- **Exit criteria**: [what "done" looks like]

### Priority 2: [Content/IP building move]
- **Why now**: [from content pipeline scan]
- **Command to run**: [specific slash command]
- **Time needed**: [hours]
- **Exit criteria**: [what "done" looks like]

### Priority 3: [Personal/alignment move]
- **Why now**: [from energy scan]
- **Command to run**: [specific slash command]
- **Time needed**: [hours]
- **Exit criteria**: [what "done" looks like]

---

## Time Allocation

| Category | Hours | % | Focus |
|----------|-------|---|-------|
| Revenue/Funnel | [X] | [%] | [specific tasks] |
| Content/IP | [X] | [%] | [specific tasks] |
| Personal/Pattern | [X] | [%] | [specific tasks] |
| **Total** | [total] | 100% | |

---

## Daily Ritual Breakdown

### Monday (Today)
- [0:00-0:30] PLAN: Review this pulse, set intentions
- [0:30-X:XX] [Task based on energy + priority]

### Tuesday
- [Time blocks with specific tasks and commands]

### Wednesday
- [Time blocks]

### Thursday
- [Time blocks]

### Friday
- [0:00-0:30] REFLECT: Journal entry → /daily-flywheel
- [0:30-X:XX] [Ship/publish/finalize tasks]

---

## Sleeping Giants

Skills and agents you have but aren't using that could move the needle:
| Skill | What It Does | Opportunity |
|-------|-------------|-------------|
| [skill] | [capability] | [how it helps this week] |

---

## Market Signals Worth Watching
[From strategic scan — trending topics, format shifts, opportunities]
```

Save to `.tmp/weekly-pulse/week-[date].md`.

### 3. Present and Offer Immediate Action

Present the pulse and offer:
- "Want me to start on Priority 1 right now?"
- "Run `/daily-focus` tomorrow to get your specific task breakdown"
- "Run `/daily-flywheel` to start with a journal entry"

---

## Parallelism Details

| Stage | Tier | Agents | Why |
|-------|------|--------|-----|
| Context gathering | Tier 1 (Parallel Task Calls) | 3 | Strategic, content, and energy scans are independent |
| Synthesis | Sequential | Main orchestrator | Must combine all 3 scans |

## Error Handling

- If no recent `.tmp/` files exist: note "Fresh start — no pipeline history" and focus on strategic scan + market signals
- If no journal entries found: recommend starting the week with `/daily-flywheel` as Priority 3
- If strategic scanner can't find market signals: skip market section, focus on internal priorities

## Output Files

```
.tmp/weekly-pulse/
  scan-strategic.md
  scan-content.md
  scan-energy.md
  week-[date].md   (the weekly pulse)
```

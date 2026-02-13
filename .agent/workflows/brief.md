---
description: Generate a strategic brief — scans your situation against your full skill arsenal and recommends highest-ROI moves
---

# /brief — Strategic Intelligence Brief

Produce a Ciel-level strategic brief: scan Farrice's current situation, goals, and available capabilities, then recommend the highest-ROI moves with exact skills and agents to deploy.

## Usage

```
/brief [optional: specific focus area or question]
```

Examples:
- `/brief` — General strategic scan
- `/brief revenue` — Focus on income-generating moves
- `/brief content` — Focus on content strategy
- `/brief what should I focus on this week?`

## Steps

### 1. Gather Context
// turbo
Read the following files to understand the full picture:

- `FARRICE.md` — Current goals, positioning, avatar, emotional landscape
- `GEMINI.md` — Full skill and agent roster (the arsenal)
- Any recent `memory/context.md` files in active agent directories for project state

### 2. Situation Assessment

Produce a concise assessment:

```
CURRENT STATE
- Primary goal: [From FARRICE.md — what Farrice is optimizing for right now]
- Active projects: [Any in-flight work from recent conversations]
- Bottleneck: [What's currently limiting progress]
- Revenue status: [Where income stands relative to $20-30K/month target]
```

### 3. Arsenal Scan

Cross-reference the situation against ALL available skills and agents. For each relevant capability, assess:

- Is this skill being **actively deployed** or sitting unused?
- What would deploying it **unlock** right now?
- How does it **stack** with other available skills?

Flag any "sleeping giants" — high-impact skills that haven't been invoked recently.

### 4. Produce the Brief

```
STRATEGIC INTELLIGENCE BRIEF
Date: [Today]
Focus: [General or user-specified]

## Top 3 Highest-ROI Moves

### Move 1: [Action]
- **Why now**: [Timing/urgency rationale]
- **Deploy**: @[agent] using [skill/prompt]
- **Expected outcome**: [What this produces]
- **Time investment**: [Estimated hours]
- **Revenue potential**: [If applicable]

### Move 2: [Action]
[Same structure]

### Move 3: [Action]
[Same structure]

## Sleeping Giants
Skills/agents you have but aren't using that could change the game:
- [Skill]: [What it could do if deployed]

## Compound Plays
Multi-skill combinations that would produce outsized results:
- [Skill A] + [Skill B] → [What this creates]

## This Week's Focus
If you have 1-3 hours/day, here's the optimal allocation:
- [Day 1-2]: [Specific action]
- [Day 3-4]: [Specific action]
- [Day 5]: [Specific action]
```

### 5. Offer Execution

After presenting the brief, offer to immediately execute the top recommendation:

> "Want me to run Move 1 right now? I'll deploy @[agent] with [skill] and produce [deliverable]."

## Design Philosophy

This command exists to close the gap between extraction and deployment. Farrice has 70+ skills — this ensures they're being USED, not just collected. Every brief should surface at least one capability he forgot he had and show him exactly how to deploy it for revenue.

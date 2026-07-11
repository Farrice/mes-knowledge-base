---
name: "APEX-08: AI Employee Deployment System"
source_prompt: "skills/andrew-wilkinson-ai-entrepreneurship/references/prompts/apex-08-ai-employee-deployment.md"
skill: andrew-wilkinson-ai-entrepreneurship
standard: structure-pure-v2
refactored: 2026-07-11
---

# APEX-08: AI Employee Deployment System

Build a lean AI workforce for your operation.

## Role

You architect an "AI-as-employee" system that treats AI tools as staff assigned to specific recurring functions, using Claude Code and AI agents.

## Input Required

- **[BUSINESS_OPERATIONS]**: What you spend time on
- **[PAIN_POINTS]**: What tasks drain you
- **[SKILL_GAPS]**: What you can't do but need

## Execution Protocol

### Step 1: Operations Audit
Map all recurring tasks across:
- Content creation
- Customer service
- Research/analysis
- Admin/operations
- Product development

### Step 2: AI Employee Design
For each major function, design an AI "employee" with:
- Clear role description
- Specific tools/prompts
- Output expectations
- Supervision requirements

### Step 3: Deployment & Training
Create the actual implementations in Claude Code/agents

## Output Contract

Deliver an **AI Workforce Roster**:

- **Format**: Markdown roster plus scheduling tables
- **Length**: 500-700 words
- **Required components** (all must appear):
  1. Monthly AI Budget — tool costs broken down, totaled, and converted to a daily rate
  2. Workforce Roster — 3 or more AI "employees," each with function, time saved per week, implementation (tool + core prompt + output format), and supervision level
  3. Daily Automated Tasks table
  4. Weekly Automated Tasks table
  5. Human-AI Division of Labor — what stays human, what goes to AI
  6. Implementation Priority — sequenced across three weeks (Deploy / Refine / Expand), highest-impact first
  7. ROI Calculation — hours saved, value of those hours, AI cost, net monthly value, and cost per effective employee, with the arithmetic shown (not just final numbers)

## Output Skeleton

```markdown
# AI WORKFORCE: [Your Business]

## Monthly AI Budget
**Claude Pro/API**: $[X]
**Other tools**: $[X]
**Total**: $[X]/month = ~$[X]/day

## Workforce Roster

### AI Employee 1: [role name]
**Function**: [what they do — tied to a task from BUSINESS_OPERATIONS or PAIN_POINTS]
**Time saved per week**: [hours]
**Implementation**:
- Primary tool: [Claude Code/Custom GPT/Agent]
- Key prompt: [core instruction]
- Output format: [what they deliver]
**Supervision level**: [Daily/Weekly/As-needed]

### AI Employee 2: [role name]
[same structure, distinct function]

### AI Employee 3: [role name]
[same structure, distinct function]

## Automation Workflows

### Daily Automated Tasks
| Time | Task | AI Employee | Output |
|------|------|-------------|--------|
| [time] | [task] | [employee] | [output] |
| [time] | [task] | [employee] | [output] |

### Weekly Automated Tasks
| Day | Task | AI Employee |
|-----|------|-------------|
| [day] | [task] | [employee] |

## Human-AI Division of Labor
**You focus on**: [high-leverage activities]
**AI handles**: [everything else, named specifically]

## Implementation Priority

### Week 1: Deploy
1. [most impactful AI employee]
2. [second most impactful]

### Week 2: Refine
- [adjust prompts based on output quality]
- [add edge case handling]

### Week 3: Expand
- [add remaining employees]
- [connect workflows]

## ROI Calculation
**Hours saved per week**: [X]
**Value of those hours**: $[X] (= hours × hourly rate)
**AI cost per month**: $[X]
**Net monthly value**: $[X] (= gross value − AI cost)
**Cost per effective employee**: ~$[X]/day
```

## Quality Gate

- Every AI Employee entry maps to a real recurring task named in [BUSINESS_OPERATIONS] or [PAIN_POINTS] — not a generic, unattached role
- At least 3 distinct AI Employees are defined, each with a different function
- Supervision level is specified per employee, never left as a blanket "none needed"
- ROI Calculation shows its arithmetic (hours × rate = gross value; gross value − AI cost = net value), not just final figures with no derivation
- Daily and Weekly automation tables each contain at least two rows
- Implementation Priority sequences employees by stated impact, highest first, across the three-week arc

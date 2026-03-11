---
description: Audit any existing agent system's scaffolding for reliability gaps and harness design weaknesses
---

# /harness-audit — Agent Scaffolding Reliability Audit

Audit an existing agent or multi-agent system for harness design weaknesses using Nate B. Jones's "harness matters more than the model" methodology.

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-orchestration-intelligence/SKILL.md` and `skills/nate-b-jones-orchestration-intelligence/genius.md`.

Read `skills/nate-b-jones-orchestration-intelligence/workflows/harness-design-audit.md` for the specific audit workflow.

### Step 2: Gather System Details
Ask the user:
1. What agent system(s) are you running? (single agent, multi-agent, swarm)
2. Where are the failure modes showing up? (quality, consistency, cost, speed)
3. What model(s) are you using? What prompts/specs exist?
4. What verification/evaluation is currently in place?

### Step 3: Execute the Harness Design Audit
Follow the 4-phase audit process from the loaded workflow:
1. **Model-Harness Separation** — Identify what the model does vs. what the scaffolding does
2. **Scaffolding Gap Analysis** — Find missing verification, monitoring, or correction layers
3. **Complexity Audit** — Evaluate whether system complexity matches task complexity
4. **Improvement Roadmap** — Prioritized fixes for maximum reliability improvement

### Step 4: Produce Deliverable
Output a harness audit report:
- Current architecture diagram
- Gap analysis with severity ratings
- Specific improvement recommendations
- Priority-ordered implementation roadmap
- Cost-benefit analysis of recommended changes

### Step 5: Quality Gate
Score against: Intent Alignment, Expert Standard, Adversarial Resilience.
Composite < 7 → retry weakest section.

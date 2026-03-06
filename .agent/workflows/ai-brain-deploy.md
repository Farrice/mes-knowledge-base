---
description: Generate the AIOS Deployment Blueprint — phased rollout plan, 7-Day Sprint, and optimization protocol
---

# /ai-brain-deploy — AIOS Deployment Blueprint

Generate the phased deployment plan with rollout tracks, the 7-Day Sprint framework, and ongoing optimization protocol. This is **Workflow 04** — the final step that takes the AI Brain live.

## Prerequisites

Completed outputs from Discovery, Context Layer, and Intelligence & Automation workflows. If any are missing, prompt the user to run them first or provide equivalent context.

## Steps

### 1. Load Skill Context
// turbo
Read the following files in order:
1. `skills/liam-mley-ai-brain-builder/genius.md`
2. `skills/liam-mley-ai-brain-builder/workflows/04-aios-deployment-blueprint.md`

### 2. Load Agent Persona
// turbo
Read `agents/liam-mley/AGENT.md` and embody the Liam Mley persona throughout.

### 3. Locate Previous Outputs
// turbo
Check `_active/ai-brain/` for all previous workflow outputs. Read discovery, context, and intelligence files.

### 4. Execute Deployment Blueprint Workflow

Follow `workflows/04-aios-deployment-blueprint.md` exactly:
1. **Founder Readiness Assessment** — Tech comfort, available hours, team size
2. **Rollout Track Selection** — Accelerated (7 days), Moderate (30 days), or Gentle (90 days)
3. **7-Day Sprint Framework** — Day-by-day action plan for the first sprint
4. **Ongoing Optimization Protocol** — Weekly review cadence, monthly evolution, quarterly audit
5. **Success Metrics** — Define what "working" looks like in weeks 1, 4, 12

### 5. Deliver Output

Present the complete Deployment Blueprint:
- Founder readiness assessment
- Selected rollout track with rationale
- Day-by-day Sprint plan
- Optimization and maintenance protocols
- Success metrics and milestones

### 6. Save Output

Save all outputs to `_active/ai-brain/[client-or-business-name]/deployment/`.

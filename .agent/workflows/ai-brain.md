---
description: Run the full AI Brain Builder pipeline — Discovery through Deployment in one shot
---

# /ai-brain — Full AI Brain Builder Pipeline

Run the complete 4-workflow AI Brain Builder pipeline in a single session. Use this when you have **all the business context available upfront** and want to produce the entire AI Brain system in one pass.

> **When to use this vs. individual commands:**
> - `/ai-brain` → You have comprehensive business context and want the full build
> - `/ai-brain-discovery` → Starting from scratch, need the intake first
> - `/ai-brain-context` through `/ai-brain-deploy` → Building incrementally across sessions

## Prerequisites

The user must provide OR you must have access to comprehensive business context covering:
- Business model, revenue streams, products/services
- Team structure and key people
- Current tools and tech stack
- Daily/weekly recurring tasks and workflows
- Customer journey and sales process
- Brand voice and positioning
- Known pain points and bottlenecks

If this context is insufficient, redirect to `/ai-brain-discovery` instead.

## Steps

### 1. Load Full Skill Context
// turbo
Read ALL of the following files:
1. `skills/liam-mley-ai-brain-builder/SKILL.md`
2. `skills/liam-mley-ai-brain-builder/genius.md`
3. `skills/liam-mley-ai-brain-builder/workflows/01-ai-brain-discovery.md`
4. `skills/liam-mley-ai-brain-builder/workflows/02-context-layer-builder.md`
5. `skills/liam-mley-ai-brain-builder/workflows/03-intelligence-automation-engine.md`
6. `skills/liam-mley-ai-brain-builder/workflows/04-aios-deployment-blueprint.md`
7. `agents/liam-mley/AGENT.md`

### 2. Embody Liam Mley

Fully adopt the @liam-mley persona for the entire pipeline. Speak with founder-to-founder directness, practical conviction, and momentum-oriented pacing.

### 3. Context Assessment Gate

Before starting the build, quickly assess the available context:
- **Sufficient context** (Score 4-5 across 8 dimensions) → Proceed to full pipeline
- **Partial context** (Score 2-3) → Ask targeted questions to fill gaps, then proceed
- **Insufficient context** (Score 1) → Redirect: "Let's run `/ai-brain-discovery` first to get the foundation right."

### 4. Execute Full Pipeline

Run all 4 workflows in sequence, with each output feeding the next:

**PHASE 1: Discovery** (Workflow 01)
- Parse all available context against the 8-dimension Business DNA framework
- Run the Task Audit and generate the Automation Potential Matrix
- Determine Brain complexity tier (Simple/Standard/Enterprise)
- Output: Discovery Profile

**PHASE 2: Context Layer** (Workflow 02)
- Design the knowledge architecture based on Discovery output
- Build BRAIN.md (master context document)
- Create all supporting context files (SOPs, product docs, audience profiles)
- Establish maintenance protocol
- Output: Complete Knowledge Base

**PHASE 3: Intelligence & Automation** (Workflow 03)
- Map all data sources and design integration plan
- Design the customized Morning Brief template
- Build the phased automation roadmap (Quick Wins → Strategic)
- Add self-annealing failure-recovery to every automation
- Output: Intelligence + Automation Design

**PHASE 4: Deployment Blueprint** (Workflow 04)
- Assess founder readiness and select rollout track
- Generate the 7-Day Sprint action plan
- Define ongoing optimization cadence
- Set success metrics for weeks 1, 4, and 12
- Output: Deployment Plan

### 5. Compile & Deliver

Present the complete AI Brain as a unified deliverable:

```
AI BRAIN BUILD — [Business Name]

1. DISCOVERY PROFILE
   [Summary + Automation Potential Matrix]

2. CONTEXT LAYER
   [BRAIN.md + file tree + maintenance protocol]

3. INTELLIGENCE & AUTOMATION
   [Morning Brief template + automation roadmap]

4. DEPLOYMENT BLUEPRINT
   [Sprint plan + optimization protocol + success metrics]
```

### 6. Save Complete Build
// turbo
Create the full directory structure:
```
_active/ai-brain/[client-name]/
├── discovery.md
├── context/
│   ├── BRAIN.md
│   └── [supporting files]
├── intelligence/
│   ├── morning-brief-template.md
│   └── automation-roadmap.md
└── deployment/
    ├── sprint-plan.md
    └── optimization-protocol.md
```

### 7. Offer Next Steps

After delivery, suggest:
- "Want me to start implementing the Quick Win automations right now?"
- "Should we compound this with @nick-saraev for self-annealing automation architecture?"
- "Ready to productize this as a service? Run `/deploy-skill paul-james-ai-automation` for pricing."

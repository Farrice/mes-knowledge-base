---
description: Run the AI Brain Discovery intake — 8-dimension business diagnostic and automation potential audit
---

# /ai-brain-discovery — AI Brain Discovery (Intake)

Run the client intake and business diagnostic for building an AI Brain. This is **Workflow 01** of the AI Brain Builder skill — the starting point for any AI Brain engagement.

Can also be used **standalone** as a business diagnostic tool without committing to a full build.

## Steps

### 1. Load Skill Context
// turbo
Read the following files in order:
1. `skills/liam-mley-ai-brain-builder/SKILL.md`
2. `skills/liam-mley-ai-brain-builder/genius.md`
3. `skills/liam-mley-ai-brain-builder/workflows/01-ai-brain-discovery.md`

### 2. Load Agent Persona
// turbo
Read `agents/liam-mley/AGENT.md` and embody the Liam Mley persona throughout.

### 3. Gather Context

Check if the user has already provided business context (e.g., from a document, prior conversation, or inline description).

- **If context provided**: Parse it against the 8-dimension Business DNA framework from the workflow and identify gaps. Ask only about missing dimensions.
- **If no context**: Run the structured intake interview from the workflow. Ask across the 8 dimensions in a natural, conversational flow — not as a rigid form.

### 4. Execute Discovery Workflow

Follow `workflows/01-ai-brain-discovery.md` exactly:
1. Build the **Business DNA Profile** across all 8 dimensions
2. Run the **Task Audit** — categorize all recurring tasks by frequency, time cost, and automation potential
3. Generate the **Automation Potential Matrix** (Quick Wins / Medium Build / Strategic)
4. Produce the **Complexity Assessment** (Simple Brain, Standard Brain, or Enterprise Brain)

### 5. Deliver Output

Present the complete Discovery output:
- Business DNA Profile
- Task Audit + Automation Potential Matrix
- Recommended Brain complexity tier
- Clear next step: "When you're ready, run `/ai-brain-context` to start building the Context Layer."

### 6. Save to Working Directory

Save the discovery output to `_active/ai-brain/[client-or-business-name]/discovery.md` for use by subsequent workflows.

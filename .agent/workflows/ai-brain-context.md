---
description: Build the AI Brain Context Layer — structured knowledge base from discovery output
---

# /ai-brain-context — Context Layer Builder

Build the structured knowledge base (BRAIN.md + full file architecture) for an AI Brain. This is **Workflow 02** — requires a completed Discovery output.

## Prerequisites

A completed Discovery from `/ai-brain-discovery`. If no discovery exists, prompt the user to run it first or provide equivalent business context.

## Steps

### 1. Load Skill Context
// turbo
Read the following files in order:
1. `skills/liam-mley-ai-brain-builder/genius.md`
2. `skills/liam-mley-ai-brain-builder/workflows/02-context-layer-builder.md`

### 2. Load Agent Persona
// turbo
Read `agents/liam-mley/AGENT.md` and embody the Liam Mley persona throughout.

### 3. Locate Discovery Output
// turbo
Check `_active/ai-brain/` for existing discovery files. If found, read and use as input. If not found, ask user where the discovery context is.

### 4. Execute Context Layer Workflow

Follow `workflows/02-context-layer-builder.md` exactly:
1. **Audit existing context** — What documents, SOPs, brand guides, etc. already exist?
2. **Design the knowledge architecture** — File tree, naming conventions, cross-references
3. **Build BRAIN.md** — The master context document (identity, voice, processes, products, customers)
4. **Create supporting context files** — SOPs, product docs, audience profiles, brand voice guide
5. **Establish maintenance protocol** — How the context layer gets updated over time

### 5. Deliver Output

Present the complete Context Layer:
- BRAIN.md (master document)
- Full file tree with all context files
- Maintenance protocol
- Clear next step: "Run `/ai-brain-intelligence` to design the data integration and automation layers."

### 6. Save Output

Save all context layer files to `_active/ai-brain/[client-or-business-name]/context/`.

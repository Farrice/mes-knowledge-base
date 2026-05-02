---
name: LLMP Agent Architect
command: /mcclain-llmp-architect
expert: Corey McClain
category: Foundation
description: Full LLMP agent construction — Logic → Library → Memory → Persona, end-to-end
inputs: Agent purpose, target audience (optional), existing agent files (optional)
outputs: Complete 4-layer agent architecture with all files
---

# LLMP Agent Architect

Build a complete AI agent using Corey McClain's LLMP framework: Logic → Library → Memory → Persona. Each layer compounds the previous. The Persona layer envelops everything and elevates the entire system from "technically accurate" to "recognizably distinct."

## Workflow

### Step 1 — Agent Purpose Assessment

Define the agent's mission:
- What does this agent produce? (content, copy, analysis, design direction, strategy)
- Who consumes the output? (you, clients, audience segments)
- What existing Logic/Library/Memory assets already exist?
- What's the current quality floor? (generic, functional, good, distinctive)

### Step 2 — Layer 1: Logic Architecture

Design the governance layer:
1. Define the core workflow sequence — what steps does the agent follow, in what order?
2. Extract rules from best-practice examples — what constraints prevent bad output?
3. Set decision gates — where does the agent need to pause, evaluate, or branch?
4. Document quality control checkpoints — how does the agent know its output is good enough?

**Output**: `logic.md` — Router prompt + workflow steps + rules + quality gates

### Step 3 — Layer 2: Library Construction

Build the reference layer:
1. Gather templates — what does excellent output look like in this domain?
2. Collect examples — 3-5 few-shot demonstrations of the desired output quality
3. Curate references — knowledge base files, style guides, domain expertise
4. Set up tool access — what external tools or APIs does the agent need?

**Output**: `library/` directory with templates, examples, references, and tool configs

### Step 4 — Layer 3: Memory Architecture

Design the persistence layer:
1. Define what the agent needs to remember across sessions
2. Create a tagging system for relevant recall (not "read everything" — targeted retrieval)
3. Set up memory write triggers — when does the agent record new memories?
4. Define memory decay — what becomes less relevant over time?

**Output**: `memory/` directory with memory schema and initial state

### Step 5 — Layer 4: Persona Installation

Build the identity layer using `/mcclain-persona-forge`:
1. Create identity — name, age, location, craft, domain
2. Write backstory — origin, formation, struggles, achievements
3. Define worldview — 3-5 beliefs that filter all decision-making
4. Design voice — vocabulary, cadence, forbidden phrases, texture
5. Add messy details — 5-10 details with zero task relevance

**Output**: `persona.md` — Full life document in narrative prose

### Step 6 — Integration & Testing

Wire everything together:
1. Place persona reference in router prompt (first or last in context chain — test both)
2. Run identical task with and without persona installed
3. Controlled delete — clear conversation, regenerate, compare
4. If quality gap is meaningful → deploy. If not → refine persona depth.

**Output**: Deployed agent with all 4 layers active

### Step 7 — Compound Plan

Set the agent up for long-term improvement:
1. Schedule persona refinement — review and update after 10 conversations
2. Memory review cycle — prune irrelevant memories monthly
3. Logic updates — add new rules as edge cases emerge
4. Library expansion — add new examples as output quality benchmarks evolve

---

## Quality Gate

Before marking complete:
- [ ] All 4 LLMP layers are documented and installed
- [ ] Persona is narrative prose (not bullet specs)
- [ ] A/B test shows measurable quality gap vs. vanilla
- [ ] Agent outputs are distinct enough to pass a blind test
- [ ] Compound plan is documented for ongoing improvement

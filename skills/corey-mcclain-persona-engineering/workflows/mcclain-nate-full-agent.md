---
name: LLMP + Sovereign Memory Full Agent
command: /mcclain-nate-full-agent
expert: Corey McClain × Nate B. Jones
category: Stacking
description: LLMP + Sovereign Memory = complete agent architecture stack
inputs: Agent purpose, target audience, domain knowledge sources
outputs: Full 5-layer agent — Logic, Library, Memory (Sovereign), Persona, and Compression Blueprint
---

# LLMP + Sovereign Memory Full Agent

The complete agent architecture stack. McClain's LLMP framework provides the identity container that elevates output quality. Nate B. Jones's Sovereign Memory Architecture provides the persistence engine that makes the agent remember, decay, and sharpen across sessions. Together they produce an agent that is both distinctive AND durable.

**Why this combination matters**: LLMP without sovereign memory produces an agent that resets every session — the persona compounds, but only if someone manually refines it. Sovereign memory without persona produces an agent that remembers everything but sounds like everyone. The stack solves both problems simultaneously.

## Workflow

### Step 1 — Purpose and Constraint Map

Before building anything:
1. **Agent Mission**: What is this agent's singular purpose? (content, strategy, copy, analysis, design)
2. **Output Consumers**: Who reads/uses what this agent produces?
3. **Persistence Requirement**: How many sessions per week will this agent run? (This determines memory tier investment)
4. **Context Budget**: What's the token ceiling per invocation? (This drives compression strategy)

### Step 2 — Logic Layer (McClain L1)

Build the governance foundation:
1. Define workflow steps — the sequential process the agent follows
2. Extract rules from domain best-practices
3. Set decision gates — where does the agent branch or pause?
4. Create quality checkpoints — how does the agent self-evaluate?

**Output**: `logic.md` — Router prompt + workflow + rules + gates

### Step 3 — Library Layer (McClain L2)

Build the reference foundation:
1. Curate 3-5 few-shot exemplars of target output quality
2. Collect domain knowledge files, style guides, and frameworks
3. Set up tool access configurations
4. Create template structures for common output types

**Output**: `library/` — Templates, exemplars, references, tool configs

### Step 4 — Sovereign Memory Layer (Nate B. Jones Architecture)

Replace standard memory with the three-tier sovereign system:

**4a — Episodic Tier**:
- Raw interaction logs with timestamps
- 90-day retention before mandatory distillation
- Write triggers: task completion, user correction, quality gate failure

**4b — Semantic Tier**:
- Distilled patterns, rules, and preferences (vector-indexed)
- Ebbinghaus decay function: `freshness = base_value × (1 / (1 + k × days_since_last_access))`
- k-value tuning: 0.1 for slow-decay domains (brand voice), 0.5 for fast-decay domains (trending topics)

**4c — Procedural Tier**:
- Configurations, workflow modifications, and versioned settings
- No decay — these are permanent until explicitly updated
- Includes persona refinement history (what changed and why)

**Output**: `memory/` — Schema, decay parameters, write triggers, retrieval protocol

### Step 5 — Context Compression Blueprint (Nate B. Jones Five Vectors)

Apply compression to all layers before persona installation:

1. **Quantization**: Deduplicate instructions across logic/library files
2. **Eviction & Sparsity**: Distill verbose reference materials into rule-form
3. **Architectural Redesign**: Convert prose instructions to tables/rules where appropriate (but NOT the persona — persona stays narrative)
4. **Offloading & Tiering**: Classify all context as T0 (always loaded) through T3 (sub-agent retrieved)
5. **Attention Optimization**: Place critical instructions at context top/bottom, not middle

**Critical Exception**: The persona document is NEVER compressed. Narrative prose is the mechanism — compressing it destroys the container effect. All other layers get compressed to make room for the persona.

**Output**: Compression map showing token budget allocation across all layers

### Step 6 — Persona Layer (McClain L4)

Now build the identity container — with the memory architecture aware:

1. Run `/mcclain-persona-forge` to create the full life document
2. **Memory-Aware Additions**:
   - Include a "learning posture" in the persona — how does this person respond when they're wrong?
   - Include a "memory philosophy" — does this person hold grudges or forgive quickly? Do they remember details or big patterns?
   - Include "growth arcs" — what is this person actively trying to get better at?
3. Place persona at the top or bottom of the context chain (test both positions)
4. Ensure persona file is referenced in the router prompt but never summarized or compressed

**Output**: `persona.md` — Full life document with memory-integration extensions

### Step 7 — Integration and Validation

Wire the five layers together and stress-test:

1. **Layer Wiring**: Logic → Library → Memory (sovereign) → Compression → Persona (container)
2. **Vanilla Comparison**: Run identical task with and without the full stack. Controlled delete between tests.
3. **Memory Persistence Test**: Run 3 sessions, verify that session 3 output reflects learnings from sessions 1-2
4. **Compression Validation**: Run the Nate B. Jones 5-task parity test — compressed context must match original context output quality
5. **Identity Consistency Test**: Run 5 different tasks and verify the persona voice/worldview remains consistent across all of them

### Step 8 — Compound Maintenance Plan

Document the ongoing improvement protocol:
- **Weekly**: Review episodic memory, flag distillation candidates
- **Monthly**: Run semantic memory decay sweep, prune dead-weight entries
- **Quarterly**: Persona refinement — update backstory/worldview based on accumulated learnings
- **Per-Session**: Memory write triggers fire automatically on task completion and user correction

---

## Quality Gate

Before marking complete:
- [ ] All 4 LLMP layers + Sovereign Memory architecture are documented and installed
- [ ] Compression applied to Logic/Library/Memory — NOT to Persona
- [ ] Persona is narrative prose with memory-integration extensions
- [ ] A/B test shows measurable quality gap vs. vanilla
- [ ] Memory persistence verified across 3+ sessions
- [ ] 5-task parity test passed for compressed context
- [ ] Compound maintenance plan documented

## When to Use

- Building a primary agent you'll use 10+ times per month
- Creating client-facing agents that need to improve over time
- Any agent where "session amnesia" is currently degrading output quality
- Production agents where both distinctiveness AND durability matter

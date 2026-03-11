---
description: Reduce multi-agent system complexity without sacrificing capability — simplify instead of adding
---

# Bloat-to-Depth Optimizer

Optimize over-engineered multi-agent systems by removing unnecessary layers and redirecting resources to the layers that actually matter.

## When to Use
- Multi-agent system is slow, expensive, or fragile
- Adding more agents isn't improving results
- System is hard to debug or understand
- Coordination overhead exceeds productive work
- Cost is growing faster than quality

## Core Principle
> "Every layer added is a potential misinterpretation. Every handoff loses context. Every agent brings its own failure mode. The goal is the minimum viable architecture that achieves the quality threshold — then invest depth where it matters."

## Workflow

### Phase 1: Complexity Census

Map the current system:

1. **Agent Count**: How many agents are in the system?
2. **Layer Count**: How many hierarchical levels (planner → sub-planner → workers)?
3. **Handoff Count**: How many times does information pass between agents?
4. **Tool Count**: How many tools are exposed to each agent?
5. **Token Volume**: Total tokens consumed per run (input + output)
6. **Latency**: End-to-end time for a complete run
7. **Cost**: Dollar cost per run
8. **Error Rate**: How often does the system produce unusable output?

### Phase 2: Value-per-Layer Analysis

For each layer/agent in the system, answer:

1. **What does this layer produce?** (specific output)
2. **Who consumes this output?** (next layer or final user)
3. **What happens without this layer?** (skip test)
4. **What's the failure mode?** (how does it break)
5. **What's the cost?** (tokens, latency, complexity)
6. **Could this be handled by deterministic code?** (regex, templates, rules)

Score each layer: **Contribution Score (1-10) / Complexity Cost (1-10)**
Layers with low contribution but high cost are removal candidates.

### Phase 3: Removal Candidates

Identify layers to remove or consolidate:

| Pattern | Fix |
|---------|-----|
| **Router agent** that just picks the same expert every time | Replace with deterministic routing |
| **Summarizer agent** between two agents | Have the downstream agent handle raw input |
| **Validator agent** that almost never rejects | Remove or replace with regex/rule checks |
| **Sub-planner** that just passes through the planner's instructions | Merge into planner |
| **Duplicate workers** doing similar tasks | Consolidate into one worker with broader scope |
| **Judge agent** with no actual criteria | Define real criteria or remove |
| **Wrapper agents** that add context then call another agent | Merge the context into the downstream agent's prompt |

### Phase 4: Depth Investment

After removing bloat, invest freed resources (tokens, latency budget) into:

1. **Better prompts** for remaining agents (more examples, clearer criteria)
2. **Richer verification** for the domains that actually need it
3. **More iterations** on the work that matters (refinement over breadth)
4. **Better state management** for the critical path
5. **Human-readable audit trails** for debugging

### Phase 5: Simplification Test

Before shipping the simplified architecture:

1. Run the same benchmark tasks through old and new architecture
2. Compare: quality, cost, latency, error rate
3. Verify no quality regression on critical tasks
4. Stress-test edge cases
5. Get domain expert to blind-evaluate 5 outputs from each

## Deliverable

Complexity optimization report containing:
- Before/after architecture diagrams
- Layer-by-layer value analysis
- Specific removal/consolidation recommendations
- Depth investment plan (where to redirect freed resources)
- Expected impact on quality, speed, and cost
- Regression test plan
- Monitoring plan for post-optimization

---
description: Evolve a specific workflow's prompts, flow, and gates
---

# Harness Evolve

> Load `skills/self-evolving-systems/genius.md` first. This workflow evolves a single workflow file.

## When to Use
- A specific workflow consistently underperforms expectations
- You've manually tuned the prompts but hit diminishing returns
- You want to test alternate prompt structures, flow orders, or gate placements

## Input Required
- **Workflow file**: Absolute path to the `.md` workflow to evolve
- **Performance history**: Past quality gate scores or output samples
- **What to evolve**: Prompts only? Flow structure? Gates? Everything?
- **Iterations**: 3-5 for prompt tuning, 10+ for structural evolution

## Execution

### Phase 1 — Decompose the Harness
Read the workflow and identify evolvable components:
- **Prompt text**: Instructions, examples, framing
- **Flow structure**: Phase ordering, dependencies, gates
- **Retrieval logic**: What context is loaded and when
- **Output format**: Structure, length, style constraints

### Phase 2 — Build Search Set
1. Gather 5-10 past invocations of this workflow
2. Identify the weakest outputs (quality gate < 7, user complaints, retry triggers)
3. These become the search set — the cases evolution targets

### Phase 3 — Evolution Loop
For each iteration:
1. Read the current best variant + execution traces from weak cases
2. Hypothesize: "This prompt phrase causes X failure because Y"
3. Propose a targeted edit (not a full rewrite unless 3+ edits failed)
4. Run the variant against the search set
5. Log: variant code, scores, traces → `evolution_store/[workflow_name]/variant_NNN/`

### Phase 4 — Converge
1. After all iterations, identify the Pareto-optimal variant
2. Diff it against the original workflow
3. Present the change set with rationale for each modification
4. User approves or requests adjustments

## Output
1. **Evolved workflow** (full `.md` file, ready to replace original)
2. **Change log** — every modification with rationale
3. **Performance delta** — before/after scores on the search set
4. **Generalization check** — performance on 2-3 examples not in the search set

---
description: Audit existing agent scaffolding for reliability gaps — the harness matters more than the model
---

# Harness Design Audit

Audit any agent or multi-agent system's scaffolding to identify reliability gaps. Based on the principle that harness design determines outcome quality more than model intelligence.

## When to Use
- Agent system is underperforming despite using capable models
- Inconsistent output quality across runs
- High failure rates on specific task types
- Scaling issues when adding more agents or complexity
- Before investing in a more expensive model

## Workflow

### Phase 1: Model-Harness Separation
Identify what the model is responsible for vs. what the scaffolding handles.

**Questions to audit:**
1. What does the model receive as input? (prompt, context, tools)
2. What verification exists between model output and downstream action?
3. Where does the model make decisions vs. where does deterministic code decide?
4. What error recovery exists when the model produces bad output?
5. Is interpretation separated from execution?

**Output:** Architecture diagram showing model boundaries vs. harness boundaries

### Phase 2: Scaffolding Gap Analysis

Check for each of these harness components:

| Component | Present? | Quality | Notes |
|-----------|----------|---------|-------|
| **Input Validation** | Does the harness verify inputs before the model sees them? | | |
| **Output Parsing** | Does the harness validate model output structure? | | |
| **Interpretation Phase** | Is the model's understanding inspectable before action? | | |
| **Tool Gating** | Are high-consequence tools gated by verification? | | |
| **Retry Logic** | Does the system retry with better prompts on failure? | | |
| **Fallback Paths** | What happens when the model can't complete a task? | | |
| **State Management** | Where is intermediate state stored? Can it resume? | | |
| **Cost Controls** | Token budgets, retry limits, timeout caps? | | |
| **Audit Trail** | Are all model calls, inputs, and outputs logged? | | |
| **Human Escalation** | Can the system escalate to a human when uncertain? | | |
| **Disambiguation** | Does the system ask clarifying questions when needed? | | |
| **Invisible Guardrails** | Are unstated constraints explicitly enumerated? | | |

### Phase 3: Complexity Audit

Evaluate whether system complexity matches task complexity:

1. **Agent Count**: How many agents? Could fewer agents with better prompts achieve the same result?
2. **Coordination Overhead**: How much of the system's work is coordination vs. productive work?
3. **Layer Value**: For each coordination layer, what would happen if you removed it?
4. **Handoff Friction**: How much information is lost at each handoff between agents?

### Phase 4: Improvement Roadmap

Prioritize improvements by impact/effort:

| Priority | Improvement | Expected Impact | Effort |
|----------|------------|-----------------|--------|
| P0 | Critical safety gaps | ... | ... |
| P1 | High-impact reliability fixes | ... | ... |
| P2 | Quality improvements | ... | ... |
| P3 | Nice-to-have optimizations | ... | ... |

## Deliverable

Harness audit report containing:
- Current architecture diagram (model vs. harness boundaries)
- Gap analysis table with severity ratings
- Complexity assessment with simplification opportunities
- Priority-ordered improvement roadmap
- Specific implementation recommendations for top 3 improvements
- Cost-benefit analysis of recommended changes

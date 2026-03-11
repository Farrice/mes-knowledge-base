---
description: Audit a multi-agent system for coordination overhead, then produce a simplification plan that strips bloat while preserving or improving capability
---

# Bloat-to-Depth Optimizer

> Load `genius.md` first. This workflow diagnoses and resolves bloat in multi-agent systems.

## When to Use
- Multi-agent system is growing complex and showing diminishing returns
- "Lots of activity but not much progress" — high token burn, low output quality
- System has more than 3 coordination layers or roles
- Suspected overhead from unnecessary verification, communication, or synchronization
- Periodic maintenance: simplifying systems that have accrued complexity over time

## Input Required
- **System to audit**: The multi-agent workflow, pipeline, or orchestration system
- **Symptom description**: What's going wrong? (e.g., slow, expensive, inconsistent, producing safe-but-shallow work)
- **Architecture documentation**: Current roles, coordination protocols, and communication patterns (if available)
- **Performance data**: Token usage, completion rates, quality scores, time-to-output (if available)

## Execution

### Phase 1 — Bloat Detection Scan
Inspect the system for these bloat indicators:

**Role Bloat** 🔴
- [ ] Are there roles that overlap in responsibility?
- [ ] Are there roles that exist "just in case" but rarely fire?
- [ ] Are there more than 3 distinct agent roles? (Flag for review — Cursor's production system uses 3.)
- **Evidence**: Count distinct roles. If >3, each additional role must justify its existence with a unique, measurable contribution.

**Coordination Bloat** 🟡
- [ ] Do agents communicate with each other during execution? (They shouldn't need to.)
- [ ] Are there locks, synchronization mechanisms, or turn-taking protocols?
- [ ] Is there a coordination layer between workers? (Workers should be fully isolated.)
- **Evidence**: Map all inter-agent communication. Each communication channel is a potential bloat source.

**Verification Bloat** 🟠
- [ ] Are there multiple verification passes for the same output?
- [ ] Does verification take longer than execution?
- [ ] Are judges evaluating criteria that could be automated?
- [ ] Is the judge role still necessary? (Cursor dropped judges when agents followed instructions reliably.)
- **Evidence**: Time verification vs. execution. If verification > 30% of total time, investigate.

**Context Bloat** 🔵
- [ ] Are agents receiving more context than they need for their specific task?
- [ ] Is conversation history accumulating instead of being reset?
- [ ] Are handoff artifacts too large? (Carry only what's needed, not everything.)
- **Evidence**: Measure context window utilization per agent. If >70% is context (not task), bloat.

### Phase 2 — The Cursor Simplification Test
Apply Cursor's counter-intuitive finding: improvements often come from *removing* complexity.

For each component identified in Phase 1, answer:
1. **What happens if we remove this entirely?** (Not reduce — remove.)
2. **Does performance stay the same or improve?** (If yes: it was bloat. Remove permanently.)
3. **Does performance degrade?** (If yes: it's load-bearing. Keep but optimize.)

Run this test sequentially, removing one component at a time:
- Remove a communication channel → test
- Remove a verification layer → test
- Remove a role → test
- Simplify a handoff artifact → test

**Decision rule**: If the system performs equally well without a component, the component was overhead. Remove it.

### Phase 3 — Depth Preservation Check
After simplification, verify that depth (capability) was preserved:

| Capability | Before Simplification | After Simplification | Status |
|-----------|----------------------|---------------------|--------|
| [Capability 1] | [Quality level] | [Quality level] | ✅ Preserved / ⚠️ Degraded |
| [Capability 2] | ... | ... | ... |

If any capability degraded, selectively restore the minimum component needed to recover it.

### Phase 4 — Optimized Architecture
Produce the simplified architecture:

**Before**:
- [Full role list with coordination]
- [All communication channels]
- [All verification layers]
- Token cost per task: [estimate]

**After**:
- [Reduced role list]
- [Remaining (essential) communication]
- [Essential verification only]
- Token cost per task: [estimate]
- **Savings**: [% reduction in coordination overhead]

### Phase 5 — The "Clean Isolation" Redesign
If the system is fundamentally bloated (>50% overhead), consider a clean-room redesign using Cursor's proven minimal architecture:
1. **Planners** explore and decompose (no execution, no coordination with other planners)
2. **Workers** execute in complete isolation (no cross-worker communication)
3. **Judges** evaluate and restart (optional — only if workers aren't following instructions reliably)

Map the current system's actual work onto this 3-role architecture. What doesn't fit is likely overhead.

## Output
A Bloat-to-Depth Optimization Report containing:
1. **Bloat scan results** with evidence for each category (role, coordination, verification, context)
2. **Simplification test results** (what was removed, what happened)
3. **Depth preservation scorecard** (all capabilities tested before/after)
4. **Optimized architecture** with before/after comparison and savings estimate
5. **Clean-room redesign option** (if fundamental restructuring is warranted)
6. **Maintenance schedule** — when to re-run this audit (recommend: every 30 days for active systems)

## Anti-Pattern Warning
The most common mistake is *adding* a coordination layer to fix a coordination problem. This workflow enforces the opposite: simplify first, add only after proving simplification doesn't work. Trust the convergence evidence — the four labs that solved this all converged on simpler designs, not more complex ones.

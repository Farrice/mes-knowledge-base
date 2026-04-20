---
description: 5-layer prerequisite scorecard (context, trace, eval, sandbox, governance) with gap remediation plan. Assesses whether team/system is ready for auto-improvement.
---

# Auto-Improvement Readiness Audit

> Load `genius.md` first. "Auto improvement is like a graduate level capability when most orgs are struggling with agents 101." This workflow diagnoses which foundation layers exist and which must be built.

## Pre-Flight Gate (from genius.md)

> "If you're not capturing detailed traces from your agents, you have literally nothing for a meta agent to work on."

All 5 prerequisite layers must score ≥7. Missing layers = say NO to the loop and build foundations first.

## When to Use

- After triplet is approved (WF 01)
- Before architecture design (WF 03)
- When a team says "we're ready for auto-improvement" — validate the claim
- Consulting context: client wants to deploy auto-optimization

## Skill Acquisition

Load: `genius.md` (GP-10, HK-5, HK-6, SM-4, Anti-pattern #1)

## Input Required

- Approved triplet from WF 01
- Team/system context: existing infrastructure, team size, tooling
- Access to relevant systems for inspection (or interview access)

## Execution

### Layer 1 — Context Layer (Score 0-10)

**What to assess**: Does the system have structured external memory that persists goals, state, and constraints across sessions?

Scoring rubric:
- **0-3**: Session-only memory. Every run reinvents context.
- **4-6**: Some persistence (logs, configs) but unstructured.
- **7-8**: Structured memory with persistent state + constraint files.
- **9-10**: Full context layer: memory architecture, constraint propagation, session-to-session continuity.

**Evidence to collect**:
- Where is system state persisted?
- How does a new agent session inherit prior context?
- Are constraints (invisible guardrails) encoded in files the agent reads?

**Red flag (HK-5)**: if context layer <5, auto-improvement will degrade the system faster than improve it.

### Layer 2 — Trace Infrastructure (Score 0-10)

**What to assess**: Are reasoning trajectories logged, not just outcomes?

Scoring rubric:
- **0-3**: Score-only logging. No reasoning traces.
- **4-6**: Some reasoning captured but unstructured/incomplete.
- **7-8**: Full reasoning chains logged, tool calls recorded, decision points marked.
- **9-10**: Structured trace schema, queryable storage, analysis tooling for meta-agent consumption.

**Evidence to collect**:
- Can you show a trace from a recent agent run?
- Can you answer "where did the agent lose direction?" from the trace?
- Is there a trace schema, or ad-hoc logging?

**Red flag (HK-6)**: "The quality of your trace infrastructure ceilings the quality of your auto-improvement."

### Layer 3 — Eval Harness (Score 0-10)

**What to assess**: Scoring functions that accurately reflect business value?

Scoring rubric:
- **0-3**: Activity metrics (count of messages, runs, hours) without outcome correlation.
- **4-6**: Outcome-adjacent metrics but proxy nature not validated.
- **7-8**: Outcome metrics with validated business-value correlation.
- **9-10**: Outcome metrics + held-out test tasks + adversarial probes.

**Evidence to collect**:
- What is the eval function?
- Is it tested against held-out tasks?
- Does scoring correlate to business outcomes (revenue, retention, accuracy)?

**Red flag (GP-13)**: "Measuring activity instead of outcome" → agent optimizes wrong direction at inhuman speed.

### Layer 4 — Sandboxed Execution (Score 0-10)

**What to assess**: Can hundreds of experiments run without killing production or needing a human?

Scoring rubric:
- **0-3**: Only production or no sandbox exists.
- **4-6**: Sandbox exists but shared resources with prod.
- **7-8**: Isolated sandbox, auto-provisioned, version-controlled.
- **9-10**: Sandbox + automatic rollback + compute cost tracking + parallel experiment support.

**Evidence to collect**:
- Where do experiments run?
- How is production isolated?
- Can experiments be automatically reverted?

### Layer 5 — Governance (Score 0-10)

**What to assess**: Clear ownership, review, and promotion structures?

Scoring rubric:
- **0-3**: No defined ownership. "Who reviews experiments?" has no answer.
- **4-6**: Ownership exists but process is ad-hoc.
- **7-8**: Documented ownership, review criteria, promotion gates.
- **9-10**: All of above + audit trail + incident response protocol.

**Evidence to collect**:
- Who owns the output of auto-improvement?
- Who reviews the 47th experiment at 3am?
- Who decides what's promoted to production?
- Who gets paged if something degrades silently?

**Red flag**: "Organizations that struggle with who gets fired if AI makes a bad decision aren't going to suddenly develop clear ownership structures just because agents can now edit their own code."

---

### Phase 6 — Composite Assessment

| Layer | Score | Status |
|-------|-------|--------|
| Context Layer | [0-10] | ✅ ≥7 / ⚠️ 4-6 / ❌ <4 |
| Trace Infrastructure | [0-10] | ✅ ≥7 / ⚠️ 4-6 / ❌ <4 |
| Eval Harness | [0-10] | ✅ ≥7 / ⚠️ 4-6 / ❌ <4 |
| Sandboxed Execution | [0-10] | ✅ ≥7 / ⚠️ 4-6 / ❌ <4 |
| Governance | [0-10] | ✅ ≥7 / ⚠️ 4-6 / ❌ <4 |

**Decision Rules**:
- **All layers ≥7**: PROCEED to WF 03 (architecture design)
- **Any layer 4-6**: BUILD FIRST — remediation plan required, no loop until fixed
- **Any layer <4**: STOP — foundational rebuild required, 3-6 month horizon

### Phase 7 — Gap Remediation Plan (if any layer <7)

For each gap:

```markdown
### Gap: [Layer Name] — Score [N]/10

**Current state**: [what exists today]
**Target state**: [what needs to exist]
**Build tasks**:
1. [specific task with owner + deadline]
2. [...]
**Estimated effort**: [person-weeks]
**Dependencies**: [what must exist first]
**Validation criteria**: [how to know it's ≥7]
```

Sequence remediation by dependency order:
1. Context layer first (foundation for everything)
2. Trace infrastructure second (required for meta-agent interpretability)
3. Eval harness third (required for objective scoring)
4. Sandboxed execution fourth (enables volume)
5. Governance fifth (enables promotion)

## Content Type Adaptations

| System Type | Context Layer Example | Trace Depth Example | Governance Example |
|-------------|----------------------|--------------------|--------------------|
| Customer service agent | Customer history + SLA constraints | Conversation reasoning chain | On-call rotation + escalation SOP |
| Pricing engine | Market data + policy constraints | Pricing decision justification | Revenue ops review + CFO sign-off |
| Content pipeline | Style guide + brand constraints | Draft reasoning + edit rationale | Editor-in-chief promotion gate |
| Code-generation skill | Tech stack + repo conventions | Code reasoning + test selection | Senior eng review per KEPT variant |
| Internal research assistant | Team goals + project context | Search reasoning + synthesis path | PM approval for production use |

## Output Requirements

- 5-layer scorecard (each 0-10 with justification)
- Composite decision (PROCEED / BUILD FIRST / STOP)
- If BUILD FIRST: gap remediation plan with sequenced tasks
- If STOP: foundational rebuild scope + realistic horizon
- Document: `deliverables/readiness-audit-[system-name].md`

## Quality Gate (from genius.md rubric)

- **Prerequisite Completeness** (0-10): did the audit cover all 5 layers with evidence?
- **Trace Infrastructure Depth** (0-10): was trace assessment specific (not generic)?
- **Revert Capability** (0-10): did sandbox assessment test actual rollback?

Minimum: 7 on each. Composite: 7.0 avg, no dim below 6.

## Anti-Patterns

- ❌ Scoring optimistically to "unblock the project" (fails later, expensively)
- ❌ Treating layer scores as independent (they cascade: bad context → bad traces → bad optimization)
- ❌ Accepting "we'll fix governance later" as a plan
- ❌ Skipping evidence collection ("the CTO said it's fine")

## Hand-off

- PROCEED → `/nate-auto-architecture` (WF 03)
- BUILD FIRST → remediation plan owners, re-audit after completion
- STOP → scope separate foundational project

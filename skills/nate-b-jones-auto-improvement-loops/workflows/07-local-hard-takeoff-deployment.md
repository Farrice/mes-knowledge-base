---
description: End-to-end deployment plan for a local hard takeoff — system selection, infrastructure build, first 3 cycles, promotion, scale-out. Client-ready consulting deliverable.
---

# Local Hard Takeoff Deployment Plan

> Load `genius.md` first. "Each of these is a hard takeoff in the sense that the improvement trajectory is steep, sudden, compounding, and largely autonomous. But it's also local. It's bounded to a very specific domain."

## Pre-Flight Gate

Prerequisites for this workflow:
- Triplet approved (WF 01)
- Readiness audit passed (WF 02, all layers ≥7)
- Architecture designed (WF 03)
- Trace infrastructure built (WF 04)
- Affordances pre-loaded (WF 05)
- Safety audit passed (WF 06)

If ANY are missing, return to that workflow first. Deployment without foundations = Ferrari into a ditch.

## When to Use

- Full end-to-end rollout of auto-improvement to a team or client system
- Client consulting: "how do we actually deploy this?"
- Graduating from internal tooling to higher-stakes system
- Scaling from one loop to multiple

## Skill Acquisition

Load: `genius.md` (GP-9, GP-11, GP-16, GP-17, SM-5, SM-8, SM-9), `references/karpathy-loop-quotes.md` (Local Hard Takeoff, Small Team, Earning the Right sections)

## Input Required

- All prerequisite workflow outputs (WF 01-06)
- Team composition (must be 3-5 person team per GP-11)
- Compute budget (~$500-$5000 for first month)
- Executive sponsor (for red-tape cutting per GP-11)

## Execution

### Phase 1 — System Selection (Earn-the-Right Sequencing)

Per GP-16, order candidate systems by failure cost:

**Tier A — Cheap Failure (START HERE)**:
- Internal dev tooling
- Research optimization
- Data pipelines where failure is visible + reversible
- Content drafting (pre-human-review)

**Tier B — Moderate Failure (after 3+ Tier A successes)**:
- Operational dashboards
- Internal analytics
- Non-customer-facing workflows

**Tier C — Higher Stakes (after 6+ Tier B successes)**:
- Customer-facing systems with human review
- Revenue-adjacent systems with canary

**Tier D — Highest Stakes (after full governance maturity)**:
- Direct revenue systems (pricing, billing)
- Compliance workflows
- Trust & safety

Select ONE Tier A system for first deployment. Name it, commit to it.

### Phase 2 — Infrastructure Build Order

Map build tasks to team roles (3-5 people):

| Build Task | Owner Role | Duration | Blocking? |
|-----------|-----------|----------|-----------|
| Context layer persistence | Platform engineer | 1-2 weeks | Yes |
| Trace infrastructure | Platform engineer | 1-2 weeks | Yes |
| Eval harness | Domain expert + engineer | 2-3 weeks | Yes |
| Sandboxed execution | DevOps/platform | 1 week | Yes |
| Governance framework | Domain owner + manager | 1 week | Yes |
| Meta-agent + task-agent setup | Engineer | 1 week | No (after infra) |
| Affordance pre-load | Engineer | 1 week | No |
| Safety monitoring | Engineer + domain owner | 1-2 weeks | No |

Parallelize where possible. Total first-deployment timeline: **6-10 weeks** before first cycle runs.

### Phase 3 — The First 3 Cycles (Supervised)

Run the first 3 evolution cycles under direct human supervision. Not autonomous.

**Cycle 1** — Validate the loop mechanism
- Human writes first variant hypothesis (in program.md)
- Run meta-agent to generate variant
- Run task-agent on full benchmark (NOT spot-check; validate full pipeline)
- Review trace together (does it capture what meta-agent needed?)
- Decide KEEP/DISCARD manually
- **Learning**: does the infrastructure actually work end-to-end?

**Cycle 2** — Test the human judgment layer
- Meta-agent generates 3 variant options
- Human + meta-agent discuss which to test
- Run benchmark
- Compare meta-agent's decision recommendation vs human's decision
- **Learning**: is the meta-agent's judgment calibrated?

**Cycle 3** — First fully-automated cycle
- Meta-agent runs end-to-end autonomously
- Human reviews decision post-hoc, does not intervene
- **Learning**: does the autonomous cycle produce acceptable quality?

Gate to Phase 4: all 3 cycles completed, human confidence in loop mechanism.

### Phase 4 — Supervised Volume Sprint (Cycles 4-10)

Goal: reach ≥5 KEPT variants with zero regressions.

Practices:
- Daily review of trace samples (20% random)
- Weekly review of metric trajectory
- Safety flags checked every cycle (WF 06 mechanisms)
- Governance log maintained (who approved what, when)

Exit criteria to Phase 5:
- 5+ KEPT variants
- Zero regressions (per regression suite)
- Zero safety flags (or all resolved)
- Team confidence

If these aren't met after 20 cycles: **pause, diagnose, potentially rebuild**.

### Phase 5 — Promotion Criteria

What qualifies a KEPT variant for PRODUCTION deployment (not just KEPT in the evolution log)?

Criteria:
1. Composite score ≥ threshold (system-specific, typically 7.5)
2. Held-out benchmark score within 1.5 of seen-benchmark
3. Regression suite: zero failures
4. Canary deployment: 5% traffic for 24-48h, no downstream alerts
5. Human domain owner sign-off
6. Auditability: full trace + reasoning documented

Any failure → no promotion. Variant stays in KEPT log but doesn't reach production.

### Phase 6 — Scale-Out Protocol

After first system has 10+ production variants with zero incidents:

1. **Document what worked** — patterns, pitfalls, domain-specific insights
2. **Assess next candidate system** — preferably same Tier, adjacent domain
3. **Reuse infrastructure** — trace schema, affordances, safety audit template
4. **Team scale decision** — same team (preferred per GP-11) or parallel team?
5. **Cross-system coordination** — shared governance, separate eval sets (GP-12 contamination)

Do NOT scale to Tier B until Tier A has 3+ stable systems.

### Phase 7 — Program.md Authoring (The Direction Document)

Per GP-8 and SM-8, this is the human's primary deliverable.

Required sections:

```markdown
# Direction — [System Name]

## Current Priority
[What to evolve right now. Specific.]

## Constraints (Never Cross)
- [Non-negotiables: what cannot change]
- [Safety rules: what must always hold]
- [Business rules: what must always be true]

## Exploration Targets
- [Areas where variants should focus]
- [Hypotheses to test]

## Stopping Criteria
- [When to pause evolution]
- [Signals of exhaustion or degradation]

## Acceptance Threshold
- [Composite score minimum]
- [Required dimension floors]
- [Safety flag tolerance: 0]

## History
[Table of prior cycles — what was tried, what happened, what was learned]

## Research Directions (Future)
[Ideas for later cycles, not current commitments]
```

This document is the human's highest-leverage artifact. Treat it as such.

### Phase 8 — Monitoring + Governance Rhythm

| Frequency | Activity | Owner |
|-----------|----------|-------|
| Per cycle | Safety flag check | Engineer |
| Daily | Trace sampling | Engineer |
| Weekly | Metric trajectory review | Domain owner |
| Bi-weekly | Promotion decisions | Domain owner + manager |
| Monthly | Full 4-mode safety audit | Safety lead |
| Quarterly | Ground-truth calibration (compare to expert baseline) | Domain expert |
| Quarterly | Strategic direction update (program.md) | Domain owner |

### Phase 9 — Deployment Document Production

Final deliverable:

```markdown
# Local Hard Takeoff Deployment Plan — [System Name]

## System Selected
[Tier A candidate, justification]

## Team Composition
[3-5 roles + owners]

## Infrastructure Build Timeline
[Gantt of prerequisites, 6-10 weeks]

## First 3 Cycles Plan
[Supervised rollout]

## Supervised Volume Sprint
[Cycles 4-10 targets]

## Promotion Criteria
[6-point gate]

## Scale-Out Protocol
[When to expand, how]

## Program.md (Draft)
[First version of direction document]

## Monitoring Rhythm
[Frequency table]

## Success Metrics (90-Day Checkpoint)
- [5+ KEPT variants]
- [1+ production deployment]
- [Zero safety incidents]
- [Positive business-value correlation]

## Failure Response Plan
[What happens if goals missed: diagnose, rebuild, or sunset]
```

## Content Type Adaptations

| Client Type | Tier A Recommended | Timeline | Team Size |
|-------------|-------------------|----------|-----------|
| Startup (3-5 eng) | Internal content workflow | 8 weeks | 3 |
| Mid-market (20-50 eng) | Dev productivity tool | 10 weeks | 4-5 |
| Enterprise | Research/analytics pilot (isolated) | 12-16 weeks | 5 + exec sponsor |
| Solo founder | Personal workflow | 4 weeks | 1 |

## Output Requirements

- Full deployment plan document (9-phase structure)
- First version of program.md for the selected system
- Infrastructure build Gantt (or timeline)
- Team composition + roles
- 90-day success metrics
- Failure response plan
- Deliverable: `deliverables/takeoff-deployment-[system].md`

## Quality Gate

All 7 rubric dimensions from genius.md must score ≥7. Specifically:
- **Judgment Leverage** (0-10): program.md is substantive and specific, not generic
- **Revert Capability** (0-10): all promotion criteria include rollback path
- **Safety Monitoring** (0-10): monitoring rhythm covers all 4 modes

## Anti-Patterns

- ❌ Starting with customer-facing system (GP-16 violation)
- ❌ Enterprise team of 20 trying to run a Karpathy loop (GP-11 violation)
- ❌ Skipping first 3 supervised cycles ("we trust the loop")
- ❌ No program.md ("the evolution-direction.md is optional")
- ❌ Scale-out before first system has stable production variants
- ❌ "Set it and forget it" operation (GP-14 violation)

## Hand-off

- Plan approved by executive sponsor → begin infrastructure build
- Plan rejected → rescope (smaller system? fewer stakes? more prereq work?)
- Stuck on prereq gap → return to specific prior workflow

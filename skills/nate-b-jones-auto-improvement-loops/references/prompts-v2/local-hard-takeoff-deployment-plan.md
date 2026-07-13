---
name: "Nate B Jones — Local Hard Takeoff Deployment Plan"
source_prompt: born-v2
skill: nate-b-jones-auto-improvement-loops
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are producing the client-ready deployment plan the way Nate B Jones frames what a "local hard takeoff" actually is in a business context: "Each of these is a hard takeoff in the sense that the improvement trajectory is steep, sudden, compounding, and largely autonomous. But it's also local. It's bounded to a very specific domain. It's a specific metric. It's a specific sandbox. It doesn't escape. It doesn't generalize. It just gets really really good at one thing really fast." All six prior workflows (triplet, readiness audit at all-≥7, architecture, trace infrastructure, affordances, safety audit) are prerequisites for this one — if any is missing, deployment without foundations is "a Ferrari into a ditch," and the correct move is naming the gap and returning to that workflow, not producing a plan that papers over it.

## Input Required

- **[PREREQUISITE OUTPUTS]** — all six prior workflow outputs (triplet, readiness audit, architecture, trace infrastructure, affordances, safety audit)
- **[TEAM COMPOSITION]** — must be 3-5 people; the structural-advantage claim ("a three-person team with 500 bucks in compute can now run the same optimization loop that would take a 20 person enterprise team months to spec and approve and procure infrastructure for") depends on staying small
- **[COMPUTE BUDGET]** — typically $500-$5,000 for the first month
- **[EXECUTIVE SPONSOR]** — needed for red-tape cutting; enterprise default behaviors (approval gates, procurement, quarterly reviews) are structural anti-patterns for this kind of loop

## Execution Protocol

### Phase 1 — System Selection (Earn-the-Right Sequencing)
Order candidate systems by failure cost, and select exactly one Tier A system for the first deployment: Tier A (cheap failure, START HERE) — internal dev tooling, research optimization, data pipelines where failure is visible and reversible, content drafting pre-human-review; Tier B (moderate failure, after 3+ Tier A successes) — operational dashboards, internal analytics, non-customer-facing workflows; Tier C (higher stakes, after 6+ Tier B successes) — customer-facing systems with human review, revenue-adjacent systems with canary; Tier D (highest stakes, after full governance maturity) — direct revenue systems (pricing, billing), compliance workflows, trust & safety. Name the selected system and commit to it — do not leave the selection open-ended.

### Phase 2 — Infrastructure Build Order
Map build tasks to roles across the 3-5 person team: context layer persistence (platform engineer, 1-2 weeks, blocking); trace infrastructure (platform engineer, 1-2 weeks, blocking); eval harness (domain expert + engineer, 2-3 weeks, blocking); sandboxed execution (DevOps/platform, 1 week, blocking); governance framework (domain owner + manager, 1 week, blocking); meta-agent + task-agent setup (engineer, 1 week, non-blocking, sequenced after infra); affordance pre-load (engineer, 1 week, non-blocking); safety monitoring (engineer + domain owner, 1-2 weeks, non-blocking). Parallelize where dependencies allow. Total realistic first-deployment timeline before the first cycle runs: **6-10 weeks**.

### Phase 3 — The First 3 Cycles (Supervised, Not Autonomous)
Run these under direct human supervision, each with a distinct learning objective:
- **Cycle 1 — validate the loop mechanism**: human writes the first variant hypothesis in the direction document; run the meta-agent to generate a variant; run the task-agent on the FULL benchmark (not spot-check — validate the entire pipeline); review the trace together and check it captures what the meta-agent needed; decide KEEP/DISCARD manually. Learning target: does the infrastructure actually work end-to-end?
- **Cycle 2 — test the human judgment layer**: meta-agent generates 3 variant options; human and meta-agent discuss which to test; run benchmark; compare the meta-agent's recommendation against the human's decision. Learning target: is the meta-agent's judgment calibrated?
- **Cycle 3 — first fully-automated cycle**: meta-agent runs end-to-end autonomously; human reviews the decision post-hoc without intervening. Learning target: does the autonomous cycle produce acceptable quality?
Gate to Phase 4: all 3 cycles completed, human confidence in the loop mechanism established.

### Phase 4 — Supervised Volume Sprint (Cycles 4-10)
Goal: reach 5+ KEPT variants with zero regressions. Practices: daily review of a 20% random trace sample; weekly review of metric trajectory; safety flag checks every cycle (per the safety audit's mechanisms); governance log maintained (who approved what, when). Exit criteria to Phase 5: 5+ KEPT variants, zero regressions per the regression suite, zero unresolved safety flags, team confidence. If exit criteria aren't met after 20 cycles: pause, diagnose, and be willing to rebuild rather than push through.

### Phase 5 — Promotion Criteria
A KEPT variant qualifies for PRODUCTION deployment (distinct from merely KEPT in the evolution log) only when all six hold: (1) composite score ≥ system-specific threshold, typically 7.5; (2) held-out benchmark score within 1.5 of the seen-benchmark score; (3) regression suite shows zero failures; (4) canary deployment — 5% traffic for 24-48h with no downstream alerts; (5) human domain-owner sign-off; (6) full trace + reasoning documented for auditability. Any single failure blocks promotion — the variant stays in the KEPT log without reaching production.

### Phase 6 — Scale-Out Protocol
Only after the first system has 10+ production variants with zero incidents: (1) document what worked — patterns, pitfalls, domain-specific insights; (2) assess the next candidate system, preferably same-tier and adjacent domain; (3) reuse infrastructure — trace schema, affordances, safety audit template; (4) decide team-scale approach — same team preferred (small-team structural advantage), or parallel team; (5) coordinate cross-system governance while keeping eval sets separate (contamination prevention across loops). Do not scale to Tier B until Tier A has 3+ stable systems.

### Phase 7 — Program.md Authoring (The Direction Document)
This is the human's primary deliverable and highest-leverage artifact — treat it as such, not as optional documentation. Required sections: Current Priority (specific, not vague); Constraints (Never Cross) — non-negotiables, safety rules, business rules that must always hold; Exploration Targets — areas variants should focus on, hypotheses to test; Stopping Criteria — when to pause evolution, signals of exhaustion or degradation; Acceptance Threshold — composite score minimum, required dimension floors, safety flag tolerance (0); History — table of prior cycles, what was tried, what happened, what was learned.

### Phase 8 — Monitoring + Governance Rhythm
Specify the recurring cadence: per cycle (safety flag check, engineer); daily (trace sampling, engineer); weekly (metric trajectory review, domain owner); bi-weekly (promotion decisions, domain owner + manager); monthly (full 4-mode safety audit, safety lead); quarterly (ground-truth calibration against expert baseline, domain expert); quarterly (strategic direction update to the direction document, domain owner).

## Output Contract

- Full 9-phase deployment plan document
- First draft of the program.md/direction document for the selected system
- Infrastructure build timeline (Gantt-style or phase table), realistic 6-10 week window
- Team composition with named roles
- 90-day success metrics
- Failure response plan (what happens if 90-day goals are missed: diagnose, rebuild, or sunset)
- Document target: `deliverables/takeoff-deployment-[system].md`

## Output Skeleton

```markdown
# Local Hard Takeoff Deployment Plan — [System Name]

## System Selected
[Tier A candidate + justification]

## Team Composition
[3-5 roles, named owners]

## Infrastructure Build Timeline
[phased tasks, owners, durations, blocking status — 6-10 week total]

## First 3 Cycles Plan
[supervised rollout, learning target per cycle]

## Supervised Volume Sprint (Cycles 4-10)
[exit criteria, review cadence]

## Promotion Criteria
[6-point gate]

## Scale-Out Protocol
[when + how to expand]

## Program.md (Draft)
[Current Priority / Constraints / Exploration Targets / Stopping Criteria / Acceptance Threshold / History]

## Monitoring Rhythm
[frequency table, all 7 cadences]

## Success Metrics (90-Day Checkpoint)
- [5+ KEPT variants]
- [1+ production deployment]
- [Zero safety incidents]
- [Positive business-value correlation]

## Failure Response Plan
[diagnose / rebuild / sunset conditions]
```

## Quality Gate

- Does the plan confirm all 6 prerequisite workflows are complete before proceeding, or explicitly name which are missing and stop there?
- Is exactly one Tier A system selected and named — not a shortlist left open?
- Does the promotion criteria section include all 6 gates (composite score, held-out delta, regression suite, canary, human sign-off, auditability), with none silently dropped?
- Is the program.md draft specific to this system (named constraints, named exploration targets) rather than generic boilerplate?
- Does team composition respect the 3-5 person structural-advantage constraint, or explicitly flag the deviation and its expected cost?

## Deploy When

- Full end-to-end rollout of auto-improvement to a team or client system, after all six prerequisite workflows are complete
- Client consulting engagement answering "how do we actually deploy this?"
- Graduating a system from internal tooling to higher-stakes tiers
- Scaling from one proven loop to a second system

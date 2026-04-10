# Nate B. Jones (Agent Deployment Strategy) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Agent failures trace to specification quality, not AI capability. Start with high-frequency, low-stakes friction removal. Design every system with explicit approval gates, containment as a non-negotiable baseline, and external audit trails the agent cannot modify. The delta between best-case and worst-case defines your specification requirements.

---

## Genius Patterns (Compressed)

### GP1: The Specification Width Principle
Before deploying any agent, write a specification defining objective, constraints, communication channels, and failure modes. Test by asking: "If a literal-minded but creative employee followed this, what could go wrong?" Most agent failures trace to spec quality, not AI capability.

### GP2: Revealed Preference Engine
Read marketplace skill data as demand signals more reliable than surveys. Study what people build when given open-ended tools — top categories reveal actual demand vs. marketing assumptions. The AI industry builds for "better conversations" but revealed demand is almost entirely about ACTION.

### GP3: Friction-First Deployment
Start with high-frequency, low-stakes friction removal rather than ambitious autonomous operations. Identify top 3 daily friction points, deploy agents there first, build trust, then expand scope systematically.

### GP4: The Duality Frame
Present every agent capability through paired examples — one creating massive value, one causing massive damage. The delta between best-case and worst-case defines your specification requirements.

### GP5: The 70/30 Control Architecture
The 70% human control / 30% agent delegation finding is a product design requirement, not human weakness. Design every system with explicit approval gates. Plan for progressive delegation as trust builds.

### GP6: Containment as Non-Negotiable
Treat infrastructure isolation the way a biologist treats lab containment — baseline prerequisite, not optional hardening. Dedicated instances, throwaway accounts, no connection to irreplaceable data, external audit trails.

### GP7: The J-Curve Budgeting Pattern
Agents will make work harder before easier. Plan for 2-4 weeks of increasing friction. Communicate realistic timeline to stakeholders to prevent abandonment during the dip.

### GP8: External Audit Architecture
When the monitored system controls monitoring, you have no monitoring. Build logging and audit systems OUTSIDE the agent's scope of access. Agent cannot modify its own audit trail.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Action Over Chat — revealed demand (3,000+ skills) is almost entirely about ACTION, not conversation | Design agents for direct task execution, not conversational interfaces |
| HK2 | The Fake Log Problem — agents optimized for "appearance of task completion" without failure pathways produce deception as an emergent property | Build explicit failure acknowledgment pathways into every agent |
| HK3 | Capability-Control Gap Is the Platform Opportunity — delivering BOTH consumer-grade capability and enterprise-grade governance is the next platform play | Target the intersection of high capability and high control |
| HK4 | Early Adopter Risk Tolerance as Demand Signal — 100K+ users granting root access to hobby projects = massive demand for "agents that actually work" | The market for capable, governable agents is far larger than assumed |
| HK5 | The Shallow Emergence Pattern — open-ended social prompts produce predictable attractor states, not surprising emergence; real emergence comes from constrained, goal-directed tasks | Design for constrained goals, not open-ended simulation |
| HK6 | Culture Readiness as Deployment Prerequisite — organizations must prepare humans for agent collaboration BEFORE deploying agents | Include change management in every agent deployment plan |

---

## Signature Moves

1. **The "Literal-Minded Employee" Test** — Before deployment, draft a spec and simulate: "If a literal-minded but creative employee followed only this spec, what's the worst thing they could do?" Deploy when finalizing any agent specification.
2. **Friction Mapping First** — Conduct targeted interviews to identify top 3 daily "papercut" frustrations as prime candidates for initial deployment. Deploy when kicking off any new agent initiative.
3. **The "Air Gap" Audit** — Demand proof of strict infrastructural separation: dedicated isolated instances, throwaway credentials, no direct write access to irreplaceable data. Deploy when evaluating deployment readiness.
4. **Dual-Path Auditing** — Agent logs must be written to an entirely separate, immutable system managed by an independent team. Agent cannot report its own success. Deploy when designing monitoring frameworks.
5. **The J-Curve Pre-Mortem** — Before launch, explicitly communicate the expected 2-4 week dip in productivity to all stakeholders with specific navigation strategies. Deploy when planning any agent rollout.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Specification Precision | Objective stated but constraints and failure modes are vague | Objective, primary constraints, and basic failure scenarios outlined | Surgically defined objective with explicit negative constraints, detailed failure modes, and edge-case handling |
| Friction Point Alignment | Agent addresses a general problem, not a top-tier daily friction point | Targets a clear high-frequency friction point but scope may be too broad | Laser-focused on a high-frequency, low-stakes "papercut" directly impacting user productivity |
| Control Architecture | Basic human approval for critical steps but delegation points undefined | Human approval gates defined; some progressive delegation considered | Explicit 70/30 split with clear approval gates and documented trust-based progressive delegation plan |
| Audit Trail Immutability | Agent logs to its own modifiable internal database | Logs accessible but immutability mechanism weak or incomplete | Logs pushed to external, immutable system ensuring tamper-proof verification of all actions |
| Containment & Isolation | Agent operates within existing production environments with standard permissions | Dedicated resources but some direct connections to sensitive systems remain | Fully isolated environment with throwaway credentials, strict read-only access, no connection to irreplaceable data |

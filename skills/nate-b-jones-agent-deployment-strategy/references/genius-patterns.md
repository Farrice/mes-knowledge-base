# Genius Patterns — Nate B. Jones (Agent Deployment Strategy)

## 1. The Specification Width Principle
Attributes agent failures to specification quality rather than AI capability. Before deploying any agent, write a specification defining objective, constraints, communication channels, and failure modes. Test by asking: "If a literal-minded but creative employee followed this, what could go wrong?"

## 2. Revealed Preference Engine
Reads marketplace skill data as demand signals more reliable than surveys. When evaluating what agents should do, study what people build when given open-ended tools. The top categories reveal actual demand vs. marketing assumptions.

## 3. Friction-First Deployment
Starts with high-frequency, low-stakes friction removal rather than ambitious autonomous operations. Identify top 3 daily friction points. Deploy agents there first. Build trust. Then expand scope systematically.

## 4. The Duality Frame
Presents every agent capability through paired examples — one where it creates massive value, one where it causes massive damage. The delta between best-case and worst-case defines your specification requirements.

## 5. The 70/30 Control Architecture
Treats the 70% human control / 30% agent delegation finding not as human weakness but as a product design requirement. Design every system with explicit approval gates. Plan for progressive delegation as trust builds.

## 6. Containment as Non-Negotiable
Treats infrastructure isolation the way a biologist treats lab containment — baseline prerequisite, not optional hardening. Dedicated instances, throwaway accounts, no connection to irreplaceable data, external audit trails.

## 7. The J-Curve Budgeting Pattern
Sets expectations that agents will make work harder before easier. Plans for 2-4 weeks of increasing friction. Communicates realistic timeline to stakeholders to prevent abandonment during the dip.

## 8. External Audit Architecture
Identifies the critical vulnerability: when the monitored system controls monitoring, you have no monitoring. Builds logging and audit systems OUTSIDE the agent's scope of access. Agent cannot modify its own audit trail.

# Strategy Anchor: Expert Composition Standard

Created: 2026-05-10
Mission: expert-composition-standard

## Target Problem
The harness has a recurring "expert soup" failure mode: it can find many relevant experts, skills, commands, gates, and source patterns, but the final output can still feel generic because no single owner composes those inputs into one coherent result.

This is costly because the user is not asking for expert name-dropping. They need the system to deploy the arsenal end to end, decide which expertise matters, discard overlap, integrate the contributions, and prove what changed.

## Guiding Bet
The fix is a composition primitive, not a larger expert list.

The durable standard is: one owner, bounded experts, explicit handoffs. Every multi-expert task needs a function owner, contribution slots, skipped-expert reasons, and a Composition Ledger that shows evidence of integration.

## Audience
- Primary: Farrice, when using Autopilot, Mission, Orchestrate, and the broader Antigravity command library.
- Secondary: future Codex runs that need to choose among many possible workflows without turning the output into a pile of frameworks.
- Tertiary: client-facing, revenue, content, writing, strategy, and system outputs that must feel integrated, high-taste, and operational.

## Key Metrics Or Proof Signals
- `/expert-composition-governor` exists as a workflow, source command, and Codex-discoverable skill.
- Router queries for "expert soup," "full arsenal," and "hammer instead of scalpel" surface `/expert-composition-governor`.
- Autopilot, Mission, Orchestrate, the Agent Arsenal Routing Contract, and the Skill System Contract all reference the composition standard.
- `python3 execution/verify_expert_composition_standard.py` passes.

## Active Tracks
- T1. Codify the composition primitive.
- T2. Wire the route into command/workflow routing and global harness specs.
- T3. Add verification so the fix is testable.
- T4. Capture the solution as reusable system guidance.

## Source Strategy
- Root `STRATEGY.md` checked: not applicable for this mission.
- Mission-local strategy decision: Codify and implement the expert-soup detection and composition process as a system-wide primitive so Autopilot, Mission, Orchestrate, and operator agents can deploy the full Antigravity arsenal end-to-end without broad expert soup, hidden routing, or low-quality stacked outputs.

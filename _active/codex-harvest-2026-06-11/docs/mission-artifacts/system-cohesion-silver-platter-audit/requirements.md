# Requirements: System Cohesion Silver Platter Audit

Created: 2026-05-11
Mission: system-cohesion-silver-platter-audit

## Problem Frame
Audit the Codex Antigravity control plane through Mission OS, System Audit, Silver Platter, and Expert Composition lenses. The first pass must produce a unified operating tree, severity-ranked issue ledger, and 30-day build order without creating another standalone layer.

## Requirements
- R1. Produce a readable system cohesion map that shows one root operating tree across the hot control routes, cold library assets, evidence layer, and evolution loop.
- R2. Use the Silver Platter lens to separate Pantry data, Prep summaries, Plate outputs, activation status, gaps, owner layer, and verifiers.
- R3. Use Mission OS and existing solution docs as the governance layer instead of creating a new command surface.
- R4. Separate true broken behavior from dormant, blocked, unmeasured, and hygiene issues.
- R5. Run and record baseline proof for control-plane, Autopilot routing, skill-system, expert-composition, harness, and Silver Platter validation.
- R6. Test natural-language routing scenarios that represent the user's actual bottleneck and log failed scenarios as routing feedback.
- R7. Keep global Codex rules read-only and avoid external writes, destructive cleanup, connector writes, and real Codex subagents.
- R8. Use a Rendered Conversation Document as the user-facing surface and a Local Markdown Source only for persistence.

## Actors
- A1. Farrice, the operator who needs the system to choose and steer.
- A2. `/autopilot`, the root front door.
- A3. `/orchestrate`, the menu backend for deliberate comparison.
- A4. `/mission`, the governance backend for durable, multi-step system work.
- A5. `/system-audit`, the control-plane proof and repair route.
- A6. `/silver-platter`, the back-of-house data-map lens.
- A7. `/expert-composition-governor`, the anti-expert-soup composition layer.
- A8. `/knowledge-librarian`, `/routing-intelligence`, and `/self-evolve`, the reuse, feedback, and supervised improvement loop.

## Key Flows
- F1. Raw user context -> `/autopilot` intent lock -> chosen route -> support gates -> verifier -> steering closeout.
- F2. User asks for options -> `/orchestrate` menu -> user chooses -> `/autopilot` or `/mission` executes later.
- F3. System-changing or reusable work -> `/mission` charter -> librarian decision -> artifact contract -> validation -> handoff.
- F4. Built-but-not-firing symptoms -> `/system-audit` proof set -> activation map -> issue ledger -> repair proposal.
- F5. Too many experts or workflows -> `/expert-composition-governor` owner and contribution slots -> Composition Ledger.
- F6. User-route dissatisfaction -> `routing_intelligence.py misroute` -> queued supervised router fix -> verifier update.

## Acceptance Examples
- AE1. Given "silver platter audit my system", when command search runs, then `/silver-platter` is the top result.
- AE2. Given "not interwoven too many agents", when workflow routing runs, then `/expert-composition-governor` is the top result.
- AE3. Given "I have too many tools and don't know what to use", when routing runs, then the current failure is captured as an issue and logged as a misroute until repaired.
- AE4. Given "what should I use next?", when routing runs, then the current failure is captured as an issue and logged as a misroute until repaired.
- AE5. Given first-pass delivery, then the user receives a readable operating tree, issue ledger, and 30-day build order without being asked to choose a new command.

## Scope Boundaries
- In scope: audit artifacts, mission state, route evidence, issue ledger, local-first proof, and build order.
- Out of scope: patching router code in this first pass, changing global `~/.codex`, deleting legacy commands, publishing, connector writes, and spawning real Codex subagents.

## Open Questions
- Blocking: none.
- Deferred: whether to implement the router repairs immediately after the audit and whether to mirror any approved behavior globally after workspace proof.

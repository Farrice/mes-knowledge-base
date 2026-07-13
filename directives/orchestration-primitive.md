# Orchestration Primitive — Judge Up, Execute Down, Verify Everything

**Standing primitive (Farrice, 2026-07-10).** Farrice kept re-requesting this per session; it is now doctrine. Extracted from the Matt Pocock v1.1 merge (HITL/AFK split, frontier, two-axis review) fused with the existing `Fable orchestrates, Sonnet executes` memory binding.

## The split

Every substantial effort divides into two kinds of work:

- **HITL** (human in the loop): grilling, verdicts, taste calls, prototype reactions, approvals, anything felt-standard. Worked *with* Farrice, one at a time. **Never simulated** — an agent that answers its own grilling questions or calls its own taste verdicts has broken the primitive. *Facts* the agent digs up itself (memory facade, project files, receipts, code); *decisions* belong to Farrice.
- **AFK** (agent alone): research, drafts-at-volume, transforms, audits, mechanical builds. Dispatched to subagents/swarm (Sonnet-tier executors; raise effort, not tier), run in parallel, results judged by the orchestrator on return.

Fable is the map-holder and judge — routing, synthesis, taste, HITL. Executors do the grunt work to Fable's plan. (Opus fallback policy applies: never pin, degrade a tier.)

## Frontier discipline

Parallel work runs only on the **frontier** — unblocked, unclaimed units. Blocking edges are declared up front (tickets, workflow stages); no executor starts work whose inputs aren't closed. When fog exists — the way to the destination isn't visible — produce **decisions before deliverables**: chart a `/wayfinder-work` map instead of charging at the destination.

## Verify everything (the non-negotiable half)

Nothing ships on assertion. In order, as applicable:

1. **Deterministic checks** where they exist — `prose_classifier.py`, `verify_*` scripts, structural file checks, `skill_auditor.py`. Deterministic beats model judgment; run it first and hand the model layer its residue.
2. **Two-axis review** for taste-bearing or client-facing deliverables — `/two-axis-verify` (Voice ∥ Brief, parallel subagents, axes never merged). For code: the imported `/code-review` (Standards ∥ Spec).
3. **Adversarial verify** for findings/claims at scale — Workflow-engine patterns (independent skeptics, perspective-diverse lenses, judge panels).
4. **PoC gate** — new assets ship only with an in-session proof on live work.
5. **Faithful reporting** — failures reported with output, skips named, no hedged "should work."

## Where it lives

`/wayfinder-work` maps (HITL/AFK ticket types) · Workflow-engine scripts (pipeline/parallel + verify stages) · `/swarm` missions · fleet dispatches · `/operator-school` (Farrice is the HITL; the taste ladder is his verdict loop). Related bindings: `feedback_fable-orchestrates-sonnet-executes`, `feedback_opus-fallback-policy`, `directives/quality_gate.md`, `directives/verification-agent-protocol.md`.

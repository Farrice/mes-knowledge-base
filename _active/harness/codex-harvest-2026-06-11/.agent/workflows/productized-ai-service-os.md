---
description: DesignJoy-style Productized AI Service OS for turning a source, skill, or messy service idea into a dual-use service OS with intake, fast first value, production queue, quality gate, proof sprint, and client-facing offer package
---

# /productized-ai-service-os - DesignJoy-Style Productized AI Service OS

Build or apply a Productized AI Service OS: a clear service promise, no-call or low-call intake, AI-assisted production loop, quality gate, delivery handoff, proof sprint, and reusable offer assets.

Use this when the user wants to:

- turn a source into an internal operating system and client-facing service
- productize an AI-assisted service, audit, sprint, or retainer
- create a sellable delivery container rather than a generic workflow
- decide whether an AI service idea has enough proof to package

## Pre-Flight Reads

1. `semantic_libraries/antigravity/primitives/productized-ai-service-os-contract.md`
2. `extractions/video-context/bAzg8BugEVY/video-context-ledger.md` when grounding in the DesignJoy source
3. `extractions/video-context/bAzg8BugEVY/uncertainty-report.md`
4. `_active/productized-ai-service-os/02-research/small-proof-ledger.md` when evaluating market fit
5. `_active/productized-ai-service-os/04-deliverables/productized-ai-service-os-brief.md`
6. `_active/productized-ai-service-os/04-deliverables/farrice-ai-service-offer-proof-sprint.md`

## Route Stack

Before building a new surface, check existing routes:

```bash
python3 execution/command_menu.py search "[service/source/offer context]"
python3 execution/workflow_router.py search "[service/source/offer context]"
python3 execution/routing_governor.py evaluate "[service/source/offer context]"
python3 execution/expert_router.py route "[service/source/offer context]"
python3 execution/context_retriever.py search "[service/source/offer context]" --top 8
```

## Component Handoffs

Use these components rather than recreating their jobs:

| Need | Route |
|---|---|
| New source-to-system build | `/source-to-skill-system` |
| Build-shape decision | `/extraction-governor-agent` |
| First paid-proof path | `/service-first-productization` |
| Pricing and offer stack | `/revenue-offer-agent` |
| Productized asset package | `/24-assets-productized-service` |
| Delivery SOPs and client handoff | `/client-delivery-agent` |
| Validation sprint | `/ash-productized-validation` |

## Operating Loop

1. **Intent Lock**
   - Identify whether the run is internal, client-facing, or dual-use.
   - Name the service idea, buyer, desired proof, and constraints.

2. **Evidence Gate**
   - Cite source timestamps, local evidence packages, or supplied business context.
   - Separate observed source evidence from current market proof and operator inference.

3. **Fit Score**
   - Score recurring need, fast first value, standardized intake, scope containment, AI leverage, human moat, distribution wedge, pricing room, and risk control.
   - If score is below 12/18, produce a proof sprint instead of a full service build.

4. **Service OS Design**
   - Define buyer, promise, first value artifact, intake, queue rule, AI role, human judgment role, quality gate, delivery surface, pause/cancel rule, proof plan, and reuse hook.

5. **Offer Package**
   - Produce a plain-English offer one-liner, target buyer, v0 pricing hypothesis, included deliverables, excluded deliverables, proof assets, and "do not build yet" criteria.

6. **Delivery System**
   - Create the production board shape: intake -> triage -> requirements -> production -> QA -> handoff -> revision -> reusable asset capture.

7. **Validation**
   - Run router discovery checks, artifact guards, Markdown readability guard, and skill validation when command surfaces changed.
   - Use `chain_runner.py finalize` for local closeout.

## Output Contract

For a full run, return:

- **Routing Trace**: chosen route, reused routes, skipped routes, and verification.
- **Productized AI Service OS Brief**: source-backed mechanics and system design.
- **Offer + Proof Sprint**: buyer, promise, proof plan, pricing hypothesis, and first proof asset.
- **Starter Sequence**: exact next commands or actions.
- **Risk Notes**: unsupported claims, market assumptions, and what must not be promised.

## Quality Gate

Reject or revise if:

- it turns into a generic agency plan
- it creates a duplicate skill instead of using existing offer/client-delivery routes
- it uses source revenue as a promise
- it lacks a no-call intake, fast first value, quality gate, and proof plan
- it recommends broad buildout before buyer proof

## Default Starter

```bash
/productized-ai-service-os "AI Slop Cleanup as a productized service"
```

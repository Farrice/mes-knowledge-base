# Skill System Contract: Shared Creative Strategy Intelligence

## Contract

| Field | Decision-complete value |
|---|---|
| Source evidence | Two YouTube URLs plus local VTT, clean transcripts, transcript segments, metadata, and timestamped frames under `sources/`; limits in `uncertainty-report.md` |
| Objective | Make creative strategy compound across cold-start Claude and Codex sessions without cloning Alex's tools or allowing unreviewed evidence to rewrite expertise |
| Function owner | Shared Creative Strategy Intelligence Layer |
| First consumer | Alex Cooper Creative Strategy |
| Bounded consumers | Trigger-Event Creative Strategy, Dara review mining, future approved strategists |
| Components | Shared semantic primitive; trigger-event component skill; `review_miner.py`; `creative_intelligence.py`; `chain_runner.py`; revenue outcomes; flagged-review queue; sovereign memory; Claude/Codex recall hook |
| Step order | source evidence → trigger-event evidence → creative artifact → finalize/NO_EVENT → outcome or explicit feedback → synthesis → human review → semantic recall |
| Inputs | project scope, artifact, hypothesis, mechanic, customer evidence, human verdict or measured result, baseline/window/test design |
| Outputs | evidence bank, narrative brief, scale matrix, append-only event, reviewed memory candidate, approved recalled lesson |
| Handoff | Pass source paths, event ID, project, hypothesis, proof state, one candidate lesson, validation result, and open risk—not the full transcript or persona stack |
| Human checkpoint | Required before semantic approval and before any skill/agent doctrine change; already satisfied for local reversible implementation |
| Context policy | Hot: shared contract + approved scoped lessons; on demand: events/outcomes; cold: transcripts/frames/rejected evidence |
| Result surface | `/trigger-event-creative-strategy`, Alex/Dara workflow integrations, local status/recall commands, existing memory-review queue |
| Reuse hook | Creative and Strategy finalization plus existing Claude/Codex prompt-time semantic recall |
| Exclusions | external Alex skills/repos, Parker, new connectors, paid tools, dependencies, global mirrors, publishing, auto-editing doctrine |

## Promotion Rules

- Explicit taste: project-scoped candidate only.
- Descriptive result: hypothesis only.
- Project result: one controlled causal test or two independent comparative results, then human review.
- Shared lesson: eligible evidence from three independent projects/campaigns, no unresolved contradiction, then human review.
- Doctrine change: three independent production receipts, blind before/after, and explicit approval.

## Goal Packet

| Field | Value |
|---|---|
| target | Shared companion layer, trigger-event skill, first-consumer integration, deterministic verifier |
| scope | Workspace-local additive files and narrow finalize/review-miner/memory-review edits; no global or external changes |
| per-item criteria | Source-grounded, single owner, no duplicate DB, explicit proof state, human-gated promotion, cold-start parity |
| permitted side effect | Append local evidence, queue reviewed candidates, create workspace skill/bridges, add non-fatal finalize capture |
| proof artifact | `behavior-proof.md`, focused tests, verifier output, router and parity receipts |
| measurable stop | All focused tests and verifiers pass; negative controls reject false promotion; both harnesses expose the same route and recall path |
| turn cap | Two repair cycles per failing verifier before scope is parked for review |
| evaluator | Deterministic tests/verifier plus human memory review |
| wake-up check | `python3 execution/creative_intelligence.py status` |
| human checkpoint | First durable lesson approval and every doctrine edit |
| rollback/archive | Remove additive hook/bridges/script; archive-never-delete ledger and source evidence |

## Agentic Engineering Packet

| Field | Value |
|---|---|
| objective | Deliver one usable trigger-event skill plus a governed compounding loop |
| source truth | This source package, existing memory/finalize/outcome code, Alex/Dara workflows, router results |
| context plan | Load component workflow only; recall approved scoped lessons; fetch raw evidence on demand |
| work chunks | evidence package → adapter/tests → skill/prompts → integrations → verifiers/proof |
| review loop | Focused tests and verifier; stop at clean pass or two failed repair cycles |
| dependency gate | stdlib-only implementation; no new package or connector |
| structure pass | Confirm one shared owner, no agent duplication, no new DB/dashboard/reminder |
| use-now artifact | Trigger-Event Evidence Bank workflow and CLI status/recall |
| hardening proof | Negative controls, human-review veto, cross-harness hook parity, cold-start route test |

## Evolution Council Verdict

- **Forager:** The missing delta is not another Alex persona; it is trigger-event craft plus outcome-backed recall.
- **Architect:** Build one focused component skill and one shared companion layer.
- **Skeptic:** Auto-writing feedback or a single winning metric into doctrine would create creative drift.
- **Implementer:** Keep changes additive, stdlib-only, workspace-local, and fail-open at finalization.
- **Evaluator:** Require generic-benefit rejection, contradiction blocking, review veto, router parity, and cold-start proof.
- **Verdict:** Implement locally; preserve human approval before durable learning or doctrine promotion.

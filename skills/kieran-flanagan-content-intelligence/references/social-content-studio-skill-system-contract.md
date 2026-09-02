# Social Content Studio — Skill System Contract

## Contract

| Field | Value |
|---|---|
| Source evidence | `https://www.youtube.com/watch?v=hoVC2W0p0Zg`; `extractions/video-context/hoVC2W0p0Zg/`; 4,529 caption segments and 59 reviewed frames; product and performance claims limited by the uncertainty report |
| Objective | Turn one grounded seed into a surplus-backed, review-only social-content week while keeping context, selection, authorship, evidence, and publication human-governed. |
| Function owner | `kieran-flanagan-content-intelligence` |
| Components | Kieran conductor and content capabilities; Farrice Brand/Voice OS when applicable; Kallaway quality gate; AI Carousel and Video Studio downstream adapters; deterministic verifier |
| Step order | Prepare Brain → Focus → Style → Plan → Create → Package |
| Required inputs | Seed idea or queue ID; platform; context root or inline identity/audience/offer context |
| Optional inputs | Horizon, formats, cadence, performance evidence, firewall definition |
| Default | One week; generate 10–15 candidates and select 3–5; a month means inventory, never auto-publication |
| Outputs | Context Lock; Content Spine; surplus inventory; selected plan; review artifacts and format briefs; evidence/claim ledger; approval manifest |
| Handoff summary | Each stage passes only its compact contract, source paths, proof state, and open risk to the next stage. |
| Human checkpoints | Context approval; idea selection; final voice/taste review; every external or publishing action |
| Validation | `execution/verify_social_content_studio.py`; video-package verifier; command/skill validation; routing and cold-start fixtures |
| Behavior-changing proof | Frozen pre-change comparison plus generic cold-start and Farrice applied pilot |
| Result surface | Readable Markdown review pack with sidecar metadata and a machine-readable manifest |
| Context policy | Command/workflow stay hot; source transcript, frames, and specialist skills load on demand; no hidden chat state |
| Reuse hook | `/social-content-studio` |
| Goal Packet | Not required: this does not mutate maintenance, cleanup, or self-evolution behavior. |
| Agentic Engineering Packet | Included below because the build changes context policy, review loops, source truth, and use-now behavior. |

## Stage Handoffs

| From → To | Must survive | Stop condition |
|---|---|---|
| Prepare Brain → Focus | source paths, freshness, proof labels, privacy/refusal rules | stop if identity, audience, or offer is absent |
| Focus → Style | Person, Tension, Path, business job, claim boundary | stop if the spine requires invented facts |
| Style → Plan | voice register, visual grammar, platform rules, anti-style constraints | stop if no enforceable refusal exists |
| Plan → Create | 10–15 distinct candidates, 3–5 selections, decision reasons | stop if candidates are cosmetic variants |
| Create → Package | review-only drafts/briefs, specialist owner, evidence gaps | stop if an unsupported claim or unapproved private detail appears |
| Package → Human | manifest, approval state, unresolved inputs, next safe action | never publish, schedule, or send |

## Composition Ledger

| Slot | Owner | Contribution | Integration evidence |
|---|---|---|---|
| Conductor | Kieran Flanagan Content Intelligence | Context architecture, firewall, surplus, selection, ordered workflow | Owns the workflow and final manifest |
| Source evaluator | MES 3.0 | Cognitive archaeology and source-fidelity standard | `mastery-extraction.md` and evidence map |
| Voice adapter | Farrice Brand/Voice OS | Source language, privacy, voice, authorship and wince rules | Loaded only for Farrice or an equivalent supplied voice system |
| Quality gate | Kallaway Content OS | Buyer-quality authority and proof-bound selection | Reviews selected concepts; does not generate the full system |
| Format adapters | AI Carousel / Video Studio | Native execution briefs after selection | Receive one bounded brief each |

Skipped as owners: Alex Content Science already owns forensic content analysis, not this conductor; Brand OS is too broad; the retired Higgsfield factory is source evidence only.

## Agentic Engineering Packet

| Field | Decision |
|---|---|
| Objective | Ship one portable command that produces a reviewable week from grounded context. |
| Source truth | Video package, Kieran skill and a10 architect, current Farrice brand sources, relevant specialist skill files |
| Context plan | Keep the workflow and contract hot; load voice, carousel, video, Kallaway, transcript, and frames only at their stage. |
| Work chunks | source package; extraction; contract/workflow/prompt; wrapper/routing; verifier; pilot; closeout |
| Review loop | Deterministic verifier plus behavior comparison; maximum two repair passes; stop on PASS or a named human taste gate. |
| Dependency gate | No new dependencies or paid tools; use existing repository and watch tooling only. |
| Structure pass | Confirm one owner, no duplicate skill, no retired Higgsfield activation, no generated-index hand edits. |
| Use-now artifact | Farrice's local one-week LinkedIn review pack. |
| Hardening proof | Source verifier, command wrapper validation, positive/negative routing fixtures, generic cold start, and Farrice behavior proof. |

## Proof Ceilings

- Source package: `GROUNDED`
- Command after deterministic validation: `RUNNABLE`
- Farrice pilot after behavior comparison: `TRANSFERRED`
- Taste: `HUMAN_REVIEW_PENDING`
- Publishing, engagement, demand, and revenue: `NO EVENT`

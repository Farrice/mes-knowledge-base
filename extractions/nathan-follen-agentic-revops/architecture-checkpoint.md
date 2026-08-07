# Architecture Checkpoint: Nathan Follen Agentic RevOps

## Checkpoint Verdict

**Approve one connected, domain-specific skill system with a surgical `/deliberate` repair and a local-first deployment on Farrice’s live operating assets.**

The build will not create a second Model Council, generic autonomy doctrine, skill generator, or command center. Nathan’s layer will own RevOps application and compose the workspace’s existing capability owners.

## Evidence Base

- Primary source: [Inside Perplexity’s AI-Powered Go-To-Market Team](https://www.youtube.com/watch?v=DHc6NtoZzAM)
- Extraction evidence: [source ledger](source-ledger.md) and [Deep MES extraction](deep-mes-extraction.md)
- Revenue truth: [pipeline](../../_active/linkedin/05-lead-gen/pipeline.md), [proof tracker](../../_active/linkedin/05-lead-gen/proof-tracker.md), [cash scoreboard](../../_active/linkedin/05-lead-gen/CASH-SCOREBOARD-2026-07-29.md), and [Angle Map activation packet](../../_active/linkedin/02-offer/ANGLE-MAP-ACTIVATION-PACKET.md)
- Customer truth: [ICP Truth Map](../../_active/linkedin/04-deliverables/context-os/03-ICP-TRUTH-MAP.md) and [Proof Library](../../_active/linkedin/04-deliverables/context-os/06-PROOF-LIBRARY.md)
- Content truth: [Signal Loop README](../../_active/farrice-brand/content/signal-loop/README.md), [audience profile](../../_active/farrice-brand/content/signal-loop/audience-profile.md), [winning-content profile](../../_active/farrice-brand/content/signal-loop/profiles/winning-content-linkedin.md), [content queue](../../_active/farrice-brand/content/signal-loop/queues/content-queue.md), and [first idea run](../../_active/farrice-brand/content/signal-loop/runs/ideas-2026-07-30-linkedin.md)

## Skill System Contract

| Contract field | Decision |
|---|---|
| System name | Nathan Follen Agentic RevOps |
| System slug | `nathan-follen-agentic-revops` |
| Function owner | Nathan Follen expert layer |
| Job | Convert first-party revenue and customer context into staged, observable RevOps decisions, read-only reconciliations, exception queues, and customer-signal actions |
| Primary consumers | Farrice as operator; future revenue, customer-evidence, and content owners |
| Inputs | Canonical local records, customer verbatim, evidence status, requested outcome, current permission tier |
| Outputs | Decision packet, proposed delta, exception queue, action router, worker-promotion receipt, or portfolio review |
| Hard vetoes | Invented customer evidence; unlabeled source-reported claims; silent record mutation; external send/publish; treating pipeline activity as offer demand; promotion without replay evidence |
| Composition rule | Reuse existing decomposition, trust, deliberation, and skill-promotion capabilities; Nathan owns only RevOps application |
| Promotion rule | Read-only by default; mutations and external actions require a separate explicit approval at the consequential boundary |
| Success signal | Better decisions and shorter review time with visible evidence, contradictions, manual-review counts, and no hidden mutation |

## Exact Build Surface

### 1. Expert Layer

Create:

```text
agents/nathan-follen/
└── AGENT.md
```

The agent will contain:

- identity and attribution boundary,
- source-grounded operating judgment,
- owned versus composed capabilities,
- source-reported claim restrictions,
- RevOps-specific activation and veto rules,
- and direct links to the skill family.

It will not claim proprietary prompts, audited productivity gains, or universal staffing replacement.

### 2. Connected Skill Family

Create:

```text
skills/nathan-follen-agentic-revops/
├── SKILL.md
├── genius.md
├── references/
│   ├── source-ledger.md
│   ├── evidence-and-permission-contract.md
│   ├── farrice-deployment-map.md
│   └── prompts-v2/
│       ├── agentic-revops-conductor.md
│       ├── revops-decision-packet.md
│       ├── worker-promotion-review.md
│       ├── revops-control-brief.md
│       ├── source-of-truth-reconciliation.md
│       ├── pipeline-exception-sweep.md
│       ├── customer-signal-action-router.md
│       ├── worker-portfolio-review.md
│       ├── revenue-proof-control-loop.md
│       └── customer-evidence-content-handoff.md
└── workflows/
    ├── agentic-revops.md
    ├── revops-decision.md
    ├── worker-promotion-review.md
    ├── revops-control.md
    ├── revops-reconcile.md
    ├── pipeline-exceptions.md
    ├── customer-signal-router.md
    ├── worker-portfolio-review.md
    ├── revenue-proof-control-loop.md
    └── customer-evidence-content-handoff.md
```

## Workflow Tier Map

The system contains ten workflows. Seven receive direct command surfaces; three remain composed routes behind the front door.

| Tier | Workflow | What it produces | Stacking partner | Public route |
|---|---|---|---|---|
| Foundation | Agentic RevOps Conductor | Source-resolved run contract and route | Existing Antigravity router and receipt surfaces | `/agentic-revops` |
| Foundation | RevOps Decision Packet | Evidence, agreement, contradiction, assumptions, and decision field | `/deliberate` | `/revops-decision` |
| Foundation | Worker Promotion Review | Promote / hold / demote verdict with permission delta and rollback | Nate B. Jones + Riley Brown | Through `/agentic-revops` |
| Foundation | Source-of-Truth Reconciliation | Read-only match, conflict, exclusion, and manual-review receipt | Nate B. Jones trust tiers | `/revops-reconcile` |
| Practitioner | RevOps Control Brief | Needs-attention, blocked, scheduled, completed, and aging state | Existing run receipts | `/revops-control` |
| Practitioner | Pipeline Exception Sweep | Force-ranked revenue exceptions and one safe next action each | Current cash scoreboard and offer contract | `/pipeline-exceptions` |
| Practitioner | Customer Signal Action Router | Provenance-bearing evidence cards and owner/action candidates | Current ICP Truth Map and Proof Library | `/customer-signal-router` |
| Practitioner | Worker Portfolio Review | Keep / repair / demote / retire candidates | Existing automation and health surfaces | `/worker-portfolio-review` |
| Stacking | Revenue-Proof Control Loop | Pipeline, proof, payment-path, and exact-offer-demand control receipt | Pipeline Exception Sweep + Customer Signal Router | Through `/agentic-revops` |
| Stacking | Customer-Evidence Content Handoff | Evidence-backed content-signal candidates without queue mutation | Customer Signal Router + Content Signal Loop | Through `/agentic-revops` |

### 3. Command Surface

Expose one front door and six focused commands:

| Command | Role | Default side effect |
|---|---|---|
| `/agentic-revops` | Routes an outcome to the correct family workflow | Read-only |
| `/revops-decision` | Builds a first-party decision packet and optionally composes `/deliberate` | Read-only |
| `/revops-control` | Produces a compact needs-attention / scheduled / blocked brief | Read-only |
| `/revops-reconcile` | Compares sources and returns proposed matches, conflicts, exclusions, and review counts | Read-only |
| `/pipeline-exceptions` | Finds stale, unsupported, blocked, or misclassified revenue states | Read-only |
| `/customer-signal-router` | Converts grounded customer evidence into owner/action candidates | Read-only |
| `/worker-portfolio-review` | Reviews existing workers for evidence, ownership, usefulness, and retirement | Read-only |

`worker-promotion-review`, `revenue-proof-control-loop`, and `customer-evidence-content-handoff` remain composed workflows reached through `/agentic-revops`. They do not need more public commands.

Registry and command documentation will be regenerated through the workspace’s existing sync path. Index files will not be hand-edited if a generator owns them.

Generated command surfaces:

```text
.agent/workflows/<generated Nathan workflow wrappers>
AGENT_INDEX.md
SKILL_INDEX.md
SLASH_COMMANDS.md
```

The build will use `sync_registries.py` and `generate_slash_commands.py` as the owners of those files. It will inspect their diffs and reject unrelated registry churn.

## Capability Ownership and Composition Ledger

| Capability | Function owner | Nathan layer’s role | Integration proof required |
|---|---|---|---|
| Process decomposition | `rachel-woods-ai-operations` | Apply stage contracts to RevOps outcomes | Workflow references the existing decomposition owner and does not restate its generic doctrine |
| Permission and trust tiers | `nate-b-jones-trust-architecture` | Translate tiers into read/propose/draft/schedule/send/mutate RevOps permissions | Promotion receipt names old tier, new tier, evidence, and rollback |
| Cross-model deliberation | `/deliberate` | Add first-party GTM evidence and decision framing | Decision workflow invokes or hands off to `/deliberate`; no second council implementation |
| Skill and schedule promotion | `riley-brown-marketing-automation` plus existing skill infrastructure | Supply RevOps replay and quality criteria | Promotion review links to repeated runs and stops before unapproved scheduling |
| Global control plane | Existing Antigravity execution/status surfaces | Produce a domain control brief compatible with current receipts | No new global scheduler, mission store, or health framework |
| RevOps application | `nathan-follen-agentic-revops` | Own decision packets, reconciliation, pipeline exceptions, customer-signal routing, and RevOps worker review | Bespoke fixtures and live local deployment receipts |

## Extraction-to-Workflow Trace

| Source-derived move | Owning workflow | Required visible proof |
|---|---|---|
| Short request rests on connected context | Agentic RevOps Conductor | Source inventory, access gaps, consumer, and run contract |
| Agreement and disagreement are decision inputs | RevOps Decision Packet | Independent positions, evidence matrix, contradiction, and resolution field |
| Trust grows one inspected stage at a time | Worker Promotion Review | Stage history, replay evidence, permission delta, and rollback |
| Read-only comparison precedes mutation | Source-of-Truth Reconciliation | Proposed matches, exclusions, conflicts, and manual-review counts |
| Human attention belongs on exceptions | RevOps Control Brief | Needs-attention, blocked, scheduled, completed, and aging states |
| Pipeline state must preserve business truth | Pipeline Exception Sweep | Canonical metric state, freshness, blocker, and next safe action |
| Customer themes must reach owners and actions | Customer Signal Action Router | Verbatim, interpretation, evidence status, owner, and action candidate |
| Workers can become obsolete after business change | Worker Portfolio Review | Current owner/source/permission fit and keep/repair/demote/retire verdict |
| Operating activity is not exact-offer demand | Revenue-Proof Control Loop | Payment-path status, proof boundary, cash state, and demand verdict |
| Customer evidence can inform content without becoming copy | Customer-Evidence Content Handoff | Provenance, audience fit, belief shift, missing felt verdict, and no queue write |

## Workflow Contracts

### Agentic RevOps Conductor

**Input:** requested RevOps outcome, available sources, consumer, and permission boundary.  
**Behavior:** resolve source truth, select one family workflow, state assumptions, and produce a run contract.  
**Output:** chosen route, inputs, missing evidence, approval boundary, and expected receipt.  
**Veto:** no “full arsenal” deployment and no route that invents missing source access.

### RevOps Decision Packet

**Input:** consequential decision, first-party evidence, alternatives, and decision owner.  
**Behavior:** assemble evidence; compose `/deliberate` when independent model disagreement would improve the decision.  
**Output:** recommendation, agreement, disagreement, evidence, assumptions, unresolved questions, and human decision field.  
**Veto:** no model vote presented as proof.

### Worker Promotion Review

**Input:** repeated task or long thread, run evidence, failures, and requested permission.  
**Behavior:** evaluate readiness across thread → prompt → personal skill → scheduled worker → shared asset.  
**Output:** promote / hold / demote verdict, evidence, next test, permission delta, and rollback.  
**Veto:** no promotion from one polished run.

### RevOps Control Brief

**Input:** one or more workflow receipts.  
**Behavior:** compress state into needs attention, blocked, scheduled, completed, and aging exceptions.  
**Output:** a decision-first operator brief with source links.  
**Veto:** no hidden failures or activity-only success language.

### Source-of-Truth Reconciliation

**Input:** two approved source sets, field mapping, conflict policy, and mutation permission.  
**Behavior:** compare records and classify confirmed, proposed, excluded, conflicted, and manual-review items.  
**Output:** read-only diff, counts, conflict reasons, and proposed mutation plan.  
**Veto:** mutation is never implicit; the build stops at the diff unless separately approved.

### Pipeline Exception Sweep

**Input:** canonical pipeline, cash scoreboard, proof tracker, current offer contract, and freshness threshold.  
**Behavior:** locate missing next actions, stale states, unsupported proof, demand-category confusion, and revenue blockers.  
**Output:** force-ranked exception queue with one next safe action per item.  
**Veto:** `sent`, `held`, `sold`, and `collected` retain their canonical meanings; prepared work cannot increment them.

### Customer Signal Action Router

**Input:** customer verbatim or approved customer evidence, evidence status, current owners, and allowed destinations.  
**Behavior:** classify signal, attach provenance, distinguish fact from interpretation, and propose owner/action routes.  
**Output:** evidence card plus product, revenue, proof, enablement, or content candidates.  
**Veto:** no synthetic voice-of-customer and no queue insertion without the destination workflow’s approval rule.

### Worker Portfolio Review

**Input:** current worker/automation inventory, receipts, owner map, business state, and review window.  
**Behavior:** assess value, failure noise, evidence freshness, ownership, permission, and strategic fit.  
**Output:** keep / repair / demote / retire candidates with reasons.  
**Veto:** no destructive cleanup or schedule change without separate approval.

### Revenue-Proof Control Loop

**Input:** pipeline exceptions, cash scoreboard, proof state, offer contract, and payment-path status.  
**Behavior:** reconcile operating activity with exact-offer demand and proof maturity.  
**Output:** revenue control receipt, force-ranked blocker, proof-capture opportunity, and next safe action.  
**Veto:** no prepared artifact, historical receipt, or generic category demand can validate the current offer.

### Customer-Evidence Content Handoff

**Input:** customer-evidence cards, audience profile, winning-content formulas, and current queue rules.  
**Behavior:** translate evidence into proposed signals with belief shift, audience fit, and missing judgment.  
**Output:** candidate handoff with provenance and promotion recommendation.  
**Veto:** no invented customer language and no canonical queue mutation.

## `/deliberate` Factual Repair

Patch only:

```text
skills/deliberate/SKILL.md
skills/deliberate/genius.md
skills/deliberate/references/source-ledger.md
```

The repair will remove or qualify the unsupported claim that Perplexity necessarily hides model disagreement. It will preserve `/deliberate`’s genuine distinction:

- an explicit first take is committed before the second model call,
- the second opinion comes from a separate model call,
- raw divergence is retained,
- and the operator must resolve or preserve the contradiction.

Add a regression fixture that fails if the deprecated “opaque/hidden disagreement” claim returns without new evidence. This is a factual repair, not a redesign.

## Post-Build Deployment on Farrice’s Real Assets

Create a local deployment surface:

```text
_active/farrice-brand/agentic-revops/
├── README.md
├── deployment-receipt.md
├── revenue-pipeline-exceptions.md
├── customer-evidence-router.md
├── content-signal-handoff.md
└── worker-control-brief.md
```

Each substantial artifact receives a metadata sidecar. The deployment is read-only against the canonical inputs below.

### Revenue Pipeline Deployment

Canonical inputs:

- `_active/linkedin/05-lead-gen/pipeline.md`
- `_active/linkedin/05-lead-gen/proof-tracker.md`
- `_active/linkedin/05-lead-gen/CASH-SCOREBOARD-2026-07-29.md`
- `_active/linkedin/02-offer/ANGLE-MAP-ACTIVATION-PACKET.md`

Required output:

- force-ranked pipeline exceptions,
- evidence and freshness for each exception,
- exact `sent`, `held`, `sold`, and `collected` state,
- category-demand versus exact-offer-demand distinction,
- one safe next action per exception,
- and a prominent hard blocker if a real payment/invoice URL is still absent.

The deployment must not send messages, change lead status, create an invoice, or imply that prepared outreach validates the offer.

### Customer Evidence Deployment

Canonical inputs:

- `_active/linkedin/04-deliverables/context-os/03-ICP-TRUTH-MAP.md`
- `_active/linkedin/04-deliverables/context-os/06-PROOF-LIBRARY.md`
- revenue artifacts listed above

Required output:

- evidence inventory by VERIFIED / LIKELY / UNCONFIRMED,
- customer-language cards using only available verbatim,
- proof gaps and capture opportunities,
- owner/action candidates,
- and separation between Angle Map proof and unrelated historical paid work.

The deployment must not convert hypothesized buyer bands, practitioner reactions, or prepared teardowns into customer proof.

### Content System Deployment

Canonical inputs:

- `_active/farrice-brand/content/signal-loop/README.md`
- `_active/farrice-brand/content/signal-loop/audience-profile.md`
- `_active/farrice-brand/content/signal-loop/profiles/winning-content-linkedin.md`
- `_active/farrice-brand/content/signal-loop/queues/content-queue.md`
- `_active/farrice-brand/content/signal-loop/runs/ideas-2026-07-30-linkedin.md`
- the customer-evidence deployment output

Required output:

- proposed evidence-backed signal candidates,
- evidence link and confidence for every candidate,
- audience and winning-formula fit,
- belief shift and revenue relevance,
- missing factual or felt judgment,
- and a handoff recommendation.

The deployment will not mutate the canonical content queue. A candidate can enter that queue only after Farrice supplies the required felt verdict and the Signal Loop’s own gate is satisfied.

## Deployment Baseline the Build Must Preserve

The current live evidence says:

- The [pipeline](../../_active/linkedin/05-lead-gen/pipeline.md) contains 15 research-backed candidates and 7 contact-verified candidates.
- The [cash scoreboard](../../_active/linkedin/05-lead-gen/CASH-SCOREBOARD-2026-07-29.md) records `sent: 0`, `held: 0`, `sold: 0`, and `collected: $0`.
- The [pipeline](../../_active/linkedin/05-lead-gen/pipeline.md) keeps exact-offer demand **UNCONFIRMED**.
- The [proof tracker](../../_active/linkedin/05-lead-gen/proof-tracker.md) records no paid Angle Maps.
- The [Proof Library](../../_active/linkedin/04-deliverables/context-os/06-PROOF-LIBRARY.md) records no client case studies for the offer.
- The [Signal Loop README](../../_active/farrice-brand/content/signal-loop/README.md) keeps the current content system **PROVISIONAL** because live performance evidence is absent.

Historical tracked paid receipts may support Farrice’s practitioner history, but they are not proof that the $750 Angle Map sells. The deployment verifier will fail if any artifact collapses that distinction.

## Verification Contract

The build is complete only if all of the following pass:

1. Skill and agent structure validators.
2. YAML/frontmatter and command-route validation.
3. Registry sync/check without hand-created index drift.
4. Source-ledger coverage for every source-derived claim in the new expert layer.
5. Bespoke fixtures for decision packets, worker promotion, reconciliation, pipeline exceptions, customer routing, and portfolio review.
6. `/deliberate` regression proving the unsupported comparison was removed while contradiction preservation remains.
7. Live Farrice deployment verifier proving:
   - no invented send, meeting, sale, collection, or payment URL;
   - no prepared work converted into proof;
   - no historical receipt converted into Angle Map proof;
   - no content queue mutation;
   - no external write or publish action.
8. Prose classifier and export-format guard for written artifacts.
9. A blind replay on frozen inputs.
10. Chain finalize with an explicit verification receipt.

Create:

```text
execution/verify_nathan_follen_agentic_revops.py
execution/fixtures/nathan_follen_agentic_revops/
├── missing-payment-path/
├── prepared-not-sent/
├── historical-receipts-not-angle-map-proof/
├── hypothesized-buyer-band/
├── customer-verbatim-and-interpretation/
├── content-queue-mutation-veto/
├── unapproved-write-request/
├── model-disagreement-visible/
├── one-run-promotion-hold/
└── ownerless-worker-review/
```

The bespoke verifier will be local, deterministic, and read-only. Its job is to validate system-specific truth boundaries that generic Markdown and frontmatter checks cannot see.

## Frozen Acceptance Cases

| Fixture | Input pressure | Required result |
|---|---|---|
| Missing payment path | Outreach is prepared and the next message is ready | Block revenue activation before the second message; do not invent a URL |
| Prepared, not sent | A proof artifact exists but no outreach was sent | Keep `sent: 0` and label the artifact prepared |
| Historical receipts | Prior paid client work totals $4,650 | Preserve practitioner history but reject it as Angle Map demand or proof |
| Hypothesized buyer band | ICP file names a $1M–$15M founder range | Keep the band as a hypothesis until customer evidence confirms it |
| Customer language boundary | A source contains verbatim plus analyst interpretation | Store them separately and quote only the verbatim as customer language |
| Queue mutation veto | A grounded content candidate scores well | Produce a handoff; do not edit the canonical queue without the felt verdict |
| Unapproved write | Reconciliation finds a clean match | Return the proposed delta and stop before mutation |
| Visible model disagreement | The source shows agreement and disagreement | Preserve `/deliberate`’s differentiation without claiming Perplexity hides disagreement |
| One polished run | A workflow succeeds once | Return HOLD with the next replay test, not promotion |
| Ownerless worker | A scheduled worker has no current consumer | Recommend repair, demotion, or retirement; do not change the schedule |

## Build Sequence

1. Create the expert layer and connected skill family.
2. Implement the seven public/internal workflow contracts.
3. Add source and permission references.
4. Apply the surgical `/deliberate` correction.
5. Register commands through the canonical generator/sync route.
6. Run structural and fixture verification.
7. Deploy read-only on Farrice’s three real asset systems.
8. Run the live deployment verifier and produce the control brief.
9. Stop before any external send, publish, CRM mutation, invoice creation, or canonical queue mutation.

## Exact Approval

Approval authorizes the local build, registry wiring, verifier work, and read-only post-build deployment described above.

It does **not** authorize:

- outreach or follow-up sends,
- publishing,
- CRM or connector writes,
- invoice or checkout creation,
- canonical content-queue mutation,
- scheduling a recurring worker,
- global `~/.codex` changes,
- destructive cleanup,
- or promotion based on unverified results.

**Decision requested:** `Approve architecture` or name the exact change.

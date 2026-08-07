# Expert Practice OS: Architecture Checkpoint

## Checkpoint Status

**Status: cold build complete; detached runtime proof and registration approval still required.**

Expanded Vision is approved. This checkpoint authorizes no production build by itself. It defines the smallest connected system that could be built next, the evidence it must produce, and the conditions that keep it cold.

Source anchors for the new behavior are the video's [transformation and validation sequence](https://www.youtube.com/watch?v=4HqO0h13MX4&t=167s), [paid founding POP](https://www.youtube.com/watch?v=4HqO0h13MX4&t=1557s), [capacity-aware sales design](https://www.youtube.com/watch?v=4HqO0h13MX4&t=1581s), [live delivery system](https://www.youtube.com/watch?v=4HqO0h13MX4&t=1721s), and [delivery-to-proof progression](https://www.youtube.com/watch?v=4HqO0h13MX4&t=1869s). Revenue and outcome claims in the source remain `SOURCE_REPORTED`.

## Architecture Decision

Build a two-component, cold system:

1. **Sunny Profitable Offer Prototype workflow:** an additive workflow inside the existing Sunny Lenarduzzi skill. It owns the sequence from a validated transformation to one paid founding engagement, live delivery, evidence capture, and an `ADVANCE / REVISE / HOLD` decision.
2. **Expert Practice OS:** a thin conductor. It collects a Practitioner / Protocol Packet, checks qualification and risk, identifies the practice type and proof stage, and routes to exactly one lane owner. It does not invent the protocol, design every offer, deliver coaching, or perform consulting work itself.

Do not create a new expert persona, mega-skill, public command, registry entry, global mirror, or economics module at this checkpoint.

## First Public Configuration

The first public lane is:

> **The Final 10% Diagnostic:** a paid AI-powered authority and business-system diagnosis for established experts with a visibility or referral-ceiling bottleneck.

Public posture: **execution architect**. AI is part of the mechanism, not a generic enterprise-automation category.

Internal consulting owner: `skills/andrew-dun-vibe-consulting/`.

This route reuses Andrew Dun's diagnosis-before-prescription, process mapping, evidence, proposal, implementation, adoption, and proof discipline. It does not inherit his default enterprise buyer, sample pricing, examples, ROI assumptions, or source-reported conversion statistics.

The current Final 10% buyer, bottleneck, offer range, scope, and proof state remain the concrete hypothesis. Exact-offer demand is `UNTESTED` until paid buyer events occur.

## Universal Client Boundary

The system is universal at the **intake, proof, capacity, stage, and handoff layers**. It is not universal at the positioning, protocol, promise, delivery, or evidence layers.

Life coaching, life design, solopreneurship, and other qualified practices remain cold adapters. Each new run requires a fresh Packet and a fresh route decision. Farrice's positioning, proof, economics, and method may not transfer to a client by default.

```text
Practitioner / Protocol Packet
        |
Qualification + claims + capacity gate
        |
Practice type + proof-stage diagnosis
        |
One lane owner only
        |
Paid POP contract
        |
Live delivery + evidence + permission
        |
ADVANCE / REVISE / HOLD
        |
RUNTIME_OBSERVED gate
        |
Annual or monthly economics module, when operating inputs support it
```

## System Responsibilities

### Expert Practice OS owns

- Packet completeness and explicit unknowns.
- Qualification, scope-of-practice, claims, and high-stakes risk checks.
- Practice type, stage, proof state, capacity, target, and bottleneck classification.
- Selection of one active lane owner and only the bounded context that owner needs.
- A route receipt with accepted assumptions, missing evidence, forbidden next moves, and the next checkpoint.
- Proof-stage enforcement and the activation decision for later economics.

### Expert Practice OS does not own

- Farrice's or a client's intellectual property.
- Domain protocols or claims.
- Offer writing, consulting diagnosis, coaching delivery, content production, sales, or implementation.
- Earnings guarantees or universal pricing.
- Outreach, publishing, payment creation, client communication, or any other external action.
- Promotion, registration, self-modification, or route learning.

### Sunny POP owns

- A specific transformation with assumption and evidence labels.
- One paid founding-offer contract: buyer, problem, outcome, scope, price status, terms, and paid-event gate.
- The bridge from interviews to a paid offer without counting interviews as demand.
- A live-delivery plan suited to the actual practice type.
- Capacity-aware sales and delivery limits.
- Separate evidence and permission ledgers.
- Actual counters: `sent / held / sold / collected`.
- One terminal verdict: `ADVANCE_TO_REPEATABILITY`, `REVISE_POP`, or `STOP_OR_HOLD`.

The source's Three Cs are not a universal template. Curriculum, coaching, and community are included only when each has a necessary delivery function. A diagnostic or consulting engagement does not inherit a community by default.

## Workflow Architecture

The stages below describe the connected system. Only stages 1 and 4 add new workflow behavior. The others are bounded handoffs to existing assets or future proof-gated modules.

| # | Stage | Function owner | Build state | Required output or gate |
|---:|---|---|---|---|
| 1 | Diagnose practitioner and practice | Expert Practice OS `01-diagnose-and-route-practice` | **NEW, cold** | Complete Packet, one lane, stage, proof state, capacity, target, risk boundary, and route receipt |
| 2 | Lock life and capacity constraints | Taki `01-lifestyle-blueprint` or `06-profit-floor-architecture` | Reused, bounded | Available hours, delivery ceiling, enough number, and margin floor |
| 3 | Configure first public hypothesis | Existing Final 10% offer assets | Reused payload | One buyer, one bottleneck, one paid Diagnostic; no competing public entry offer |
| 4 | Design paid proof loop | Sunny `04-profitable-offer-prototype` | **NEW, additive, cold** | Founding contract, delivery plan, proof ledger, counters, and terminal decision |
| 5 | Reach first buyer | Andrew `09-first-client-engine` plus current revenue front door | Reused, adapted | One primary acquisition path and actual `sent / held / sold / collected` events |
| 6 | Diagnose before prescribing | Andrew `01-diagnostic-discovery-sprint` | Reused, adapted | Authority/business-system current state and verified bottleneck |
| 7 | Map and quantify evidence | Andrew `02-process-mapping-engine` and `03-roi-quantification-calculator` | Reused, adapted | Bottleneck map and attributable evidence; no invented dollar causality |
| 8 | Prioritize and present | Andrew `04-opportunity-matrix-builder` and `05-diagnostic-presentation-architect` | Reused, adapted | Ship Map, one bottleneck, one-page architecture sketch, and Sprint go/no-go |
| 9 | Scope and implement next engagement | Andrew `12-proposal-sow-architect`, then `06-implementation-partnership-blueprint` and `07-change-management-playbook` | Reused, conditional | Signed scope before technical implementation; adoption evidence during delivery |
| 10 | Close the POP loop | Andrew `15-value-demonstration-engine` plus Sunny exit gate | Reused + new handoff | Permissioned diagnostic or process proof, method revision, and `ADVANCE / REVISE / HOLD` |
| 11 | Run repeatable annual practice | Andrew `08-advisory-retainer-builder`, `14-consulting-pipeline-dashboard`, then Growth Ecosystems `09-reverse-engineered-scaling` | Deferred until runtime and operating proof | Repeatable acquisition, delivery, retention, capacity, margin, and several comparable clients |
| 12 | Model six figures monthly | Growth Ecosystems plus a future organization-capacity module | Deferred until runtime and company-stage proof | Team, QA, management, non-founder delivery, unit economics, cash, risk, and retention math |
| 13 | Activate life-coaching adapter | Taki + Luisa + Coaching Business OS + one qualified protocol owner | Cold, swappable | Fresh Packet and coaching-specific route; Andrew explicitly rejected |
| 14 | Activate solopreneur adapter | One appropriate solopreneur owner | Cold, swappable | Fresh Packet and one niche philosophy; alternatives never blended by default |
| 15 | Activate another qualified practice | Domain owner selected from evidence | Cold, closed adapter route | Fresh proof and claims boundary; no silent transfer from another practice |

## Component Ownership and Composition Ledger

| Slot | Owner | Accepted contribution | Rejected transfer |
|---|---|---|---|
| System governance | `/source-to-skill-system` | Contract, cold-state boundary, fixtures, validation, checkpoints | A new competing behavior contract |
| Conductor | Expert Practice OS | Packet, stage/risk diagnosis, one-owner route, bounded handoff | Lane work, expert synthesis, self-learning |
| Paid proof mechanism | Sunny Lenarduzzi | Paid POP, live-learning loop, proof and permission, terminal decision | YouTube-first launch, forced Three Cs, source outcome claims |
| Active consulting lane | Andrew Dun | Diagnosis, process map, evidence, proposal, implementation, adoption, value proof | Enterprise ICP, enterprise language, generic AI-audit positioning, unsupported statistics |
| Active public offer | Final 10% Diagnostic | Specific buyer, bottleneck, bounded first step, Ship Map | A second readiness audit or simultaneous public entry offer |
| Life/capacity constraint | Taki Moore | Enough number, founder hours, delivery ceiling, profit floor | Lifestyle doctrine as a public offer |
| Coaching adapter | Luisa Zhou + Coaching Business OS + one protocol owner | First offer, first-session delivery, business and transformation lanes | AI consulting language or an unqualified protocol |
| Scale math | Growth Ecosystems | Reverse-engineering from real initial conditions | Source-reported results as forecast assumptions |
| Revenue truth | Current revenue front door | `sent / held / sold / collected` actuals | Interviews, interest, or proposals counted as cash |

**Composition rule:** one function owner per stage. The conductor loads itself plus only the selected lane owner and the minimum required references. Expert names are not proof of integration.

## Proposed Cold File Map

Files in this section are proposals, not present production assets.

```text
skills/sunny-lenarduzzi-youtube/
├── SKILL.md                                      # bounded routing addition
├── genius.md                                     # source-specific method delta
├── workflows/
│   └── 04-profitable-offer-prototype.md
└── references/
    ├── source-delta-4HqO0h13MX4.md
    └── prompts-v2/
        └── profitable-offer-prototype.md

skills/expert-practice-os/
├── SKILL.md
├── genius.md
├── workflows/
│   └── 01-diagnose-and-route-practice.md
├── references/
│   ├── practitioner-protocol-packet.md
│   ├── route-ownership-map.md
│   ├── proof-state-schema.md
│   ├── economics-activation-contract.md
│   ├── adapters/
│   │   ├── ai-consulting.md
│   │   ├── life-coaching.md
│   │   ├── solopreneurship.md
│   │   └── claims-safety.md
│   └── prompts-v2/
│       └── expert-practice-routing-receipt.md
└── tests/
    ├── verify_skill_system.py
    ├── verify_behavior_run.py
    ├── test_verify_behavior_run.py
    └── fixtures/
        ├── acceptance-cases.jsonl
        ├── final-10-ai-consulting/
        └── life-design-coach-pop/
```

The Sunny workflow must carry:

```yaml
menu_exempt: pending detached behavior proof and Verification approval
```

No command bridge, agent persona, public workflow alias, registry entry, global mirror, plugin, or economics workflow is part of the cold build.

### Cold-State Implementation Clarification

The approved map places `expert-practice-os` under `skills/`, but the repository's broad registry sync does not honor a cold status. This build therefore uses a snapshot-cold exception: the files are loadable by exact path and may appear in the generated prompt-asset catalog, but no skill index, command shim, workflow alias, automatic route, agent, or global mirror may be created. Do not run broad registry sync before detached runtime proof and registration approval. The structural verifier fails if authority surfaces appear.

## Runtime Input Contract

Every run must provide or explicitly mark unknown:

| Input group | Required fields |
|---|---|
| Practitioner | Identity, experience, credentials, scope, repeated results, exclusions |
| Protocol | Named mechanism, steps, evidence, dependencies, claims limits |
| Buyer | Specific person, observable problem, desired outcome, alternatives, disqualifiers |
| Offer | Current hypothesis, scope, format, price status, terms, paid-event gate |
| Proof | Practitioner evidence, demand events, delivery evidence, outcome evidence, permissions |
| Stage | `STAGE_0_PAID_PROOF`, `STAGE_1_REPEATABLE_PRACTICE`, `STAGE_2_PRODUCTIZED_PRACTICE`, or `STAGE_3_SCALED_COMPANY` |
| Economics | Target, price, capacity, acquisition path, conversion actuals, retention, margin, timeline |
| Risk | Regulated domain, high-stakes claims, privacy, testimonial and reuse permissions |
| Truth counters | Actual `sent`, `held`, `sold`, and `collected` values with dates |

## Proof Classes and Advancement Gates

| Proof class | What it can support | What it cannot support |
|---|---|---|
| Source evidence | Method attribution and source-grounded mechanics | Farrice or client outcomes |
| Practitioner evidence | Credible expertise, scope, and protocol hypothesis | Offer demand |
| Demand evidence | Actual buyer events and collected payments | Client transformation |
| Delivery evidence | The promised unit occurred and revealed friction | Repeatable outcomes or scale |
| Outcome evidence | Permissioned client change within the measured scope | Broad causality or universal claims |
| Repeatability evidence | Comparable clients, stable delivery, known capacity and margin | Company-scale economics without team proof |
| Runtime evidence | Correct route and behavior observed in a detached run | Market demand or business success |

Valid provenance values are `RUNTIME_OBSERVED`, `ORCHESTRATOR_ATTESTED`, and `OPERATOR_ATTESTED`. Only `RUNTIME_OBSERVED` may set `registration_eligible=true` or permit economics implementation.

## Deferred Economic Models

### Module A: Six-Figure Annual Practice

Build only after runtime proof and real Stage 1 operating inputs exist.

Required inputs:

- Annual owner-income and business-revenue targets, modeled separately.
- Current cash, runway, tax reserve, and margin floor.
- Offer prices, delivery hours, preparation and support hours, and client concurrency.
- Leads, conversations, proposals, sales, collections, acquisition cost, and cycle length.
- Retention, renewal, expansion, refund, and churn actuals where relevant.
- Founder working weeks, time off, non-selling time, and energy constraints.

Required output:

- Offer-mix scenarios and exact client counts.
- Weekly acquisition and delivery load.
- Capacity ceiling and waitlist or price trigger.
- Gross revenue, delivery cost, contribution margin, owner pay, tax reserve, and cash buffer.
- Base, conservative, and stress cases using labeled assumptions.
- The smallest paid next action and the evidence needed to update the model.

### Module B: Six-Figure Monthly Company

Build only after runtime proof and real Stage 2 or Stage 3 evidence exists. This is a company redesign, not a larger solo target.

Required additions:

- Role map, hiring sequence, employee or contractor costs, utilization, and management load.
- Sales capacity, founder and non-founder close rates, acquisition cost, payback period, and cash runway.
- Delivery capacity by role, client-to-practitioner ratios, QA sampling, escalation, and rework.
- Retention, expansion, churn, cohort performance, and service-level commitments.
- Founder dependency, documentation coverage, risk concentration, and non-founder delivery proof.

Required output:

- Monthly P&L and cash scenarios at the required run rate.
- Headcount and utilization math by role.
- Capacity limits across acquisition, sales, client setup, delivery, retention, and QA.
- The break-even point, cash required to operate, and a downside case.
- A founder-dependency test that rejects impossible solo models.
- `BUILD`, `DELAY`, or `REJECT` verdict with the limiting constraint.

Neither module may produce a guarantee. A Stage 0 run requesting six-figure-month math must return `HOLD_PREMATURE_SCALE_MODEL` and name the missing proof.

## Behavior-Proof Fixtures

### Fixture A: Farrice / Final 10% Diagnostic

Expected behavior:

- Route to the AI-consulting lane with Andrew Dun as internal owner.
- Preserve the Final 10% Diagnostic as the only public entry offer.
- Classify the proof stage as Stage 0 and demand as `UNTESTED` until payment is collected.
- Reject life-coach, generic solopreneur, generic enterprise AI, and YouTube-channel routes.
- Adapt Three Cs into the actual diagnostic delivery functions rather than forcing a community.
- Produce no annual or monthly scale economics and take no external action.

### Fixture B: Qualified Life-Design Coach

Expected behavior:

- Require a real 1:1 protocol, credible scope, and constrained weekly capacity.
- Route to Sunny POP plus one appropriate coaching or life-design owner.
- Explicitly reject Andrew Dun and the Final 10% payload.
- Produce one paid founding engagement, live delivery, evidence capture, and permission handling.
- Do not assume a course, cohort, or community is required.
- Produce no scale math before paid proof.

### Adversarial Mutations

The verifier must reject or hold missing credentials, generic buyers, vague outcomes, free activity labeled as paid proof, interviews counted as sales, unverified guarantees, multiple acquisition paths, forced community, source examples transferred as client proof, blended lane owners, premature scale math, and unauthorized external action.

## Validation Design

### Structural verifier

`verify_skill_system.py` must check:

- exact cold file inventory and complete contract,
- source-row references and truth labels,
- closed adapters and bounded lane owners,
- workflow and born-v2 prompt parity,
- Sunny `menu_exempt` state,
- absence of agent personas, wrappers, registries, global mirrors, and economics modules, and
- continued passage of the canonical source-package verifier.

### Behavior verifier

`verify_behavior_run.py` must derive its verdict from hashed run artifacts rather than trusting a declared pass flag. It checks input completeness, expected and forbidden routes, proof stage, evidence classes, one paid POP unit, actual counters, one acquisition path, capacity, claims, permission, one terminal verdict, no future-event inflation, and no premature economics.

`test_verify_behavior_run.py` must include both divergent valid runs and a mutated failure for every adversarial condition.

The generic Skill System Contract verifier is a control-plane check, not sufficient behavior proof for this source-specific build.

## Human Checkpoints

1. **Vision approval:** complete.
2. **Architecture approval:** complete.
3. **Cold-build review:** complete at `ORCHESTRATOR_ATTESTED`; structural and fixture behavior checks passed.
4. **Runtime checkpoint:** pending. Detached `RUNTIME_OBSERVED` runs must show correct routing and additive POP behavior in both fixtures.
5. **Registration decision:** separate approval after runtime proof.
6. **Economics build decision:** separate implementation after runtime proof and stage-appropriate operating inputs.
7. **External-use checkpoint:** separate approval for price changes, terms, payment, outreach, public release, or client use.

## Deferred Surfaces

Until `RUNTIME_OBSERVED`, do not create or modify:

```text
agents/expert-practice-os/AGENT.md
.agent/workflows/expert-practice-os.md
.claude/commands/expert-practice-os.md
.agents/skills/source-command-expert-practice-os/
global ~/.codex mirrors
agent, skill, command, or workflow registries
public routing aliases
plugin packaging
skills/expert-practice-os/workflows/02-annual-practice-economics.md
skills/expert-practice-os/workflows/03-monthly-scale-economics.md
```

## Routing Trace

- **Objective:** convert credible expertise or a qualified protocol into one paid founding engagement, live learning, permissioned proof, and a proof-gated next decision.
- **Existing-route check:** Sunny, Andrew Dun, Taki Moore, Luisa Zhou, Coaching Business OS, Growth Ecosystems, the Final 10% offer assets, and the current revenue front door cover the lane work.
- **Named gap:** none owns the paid POP as a complete evidence-producing loop or the universal intake-to-one-owner handoff.
- **Chosen build shape:** additive Sunny workflow plus thin Expert Practice OS conductor.
- **Rejected shapes:** new Authority.io persona, all-in-one business skill, generic AI consultancy, simultaneous public lanes, content-first launch, economics-first modeling, and hot promotion.
- **First public route:** Final 10% Diagnostic, with Andrew Dun as the internal consulting owner.
- **Cold adapters:** life coaching, life design, solopreneurship, and other qualified practices.
- **Stop state:** cold files and deterministic tests are complete; runtime proof, registration, economics, and production use remain inactive.

## Current Checkpoint Decision

Reply with one of these:

- **Approve detached runtime proof:** run both clean-context fixtures and bind the observed results to hashes.
- **Adjust cold build:** name the component, ownership boundary, public posture, file map, fixture, or proof gate to change.
- **Preserve cold build and stop:** keep the local diagnostic system unregistered and take no further action.

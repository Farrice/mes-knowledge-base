# Vision Checkpoint: Nathan Follen Agentic RevOps

## Content Assessment

| Field | Assessment |
|---|---|
| Source | [Inside Perplexity’s AI-Powered Go-To-Market Team](https://www.youtube.com/watch?v=DHc6NtoZzAM), Marketing Against the Grain |
| Primary expert | Nathan “Nate” Follen, presented as Revenue Operations / Enterprise Operations & Systems at Perplexity |
| Hosts | Kipp Bodnar and Kieran Flanagan |
| Published | 2026-07-08 |
| Runtime | 25:43 |
| Capture | Native captions, 5,536-word clean transcript, 100-frame full-video pass, and 118 focused scene/cue frames across three demonstration windows |
| Linked timestamp | 06:08, the Model Council request using open opportunities from the team’s CRM context |
| Source depth | Practitioner-rich single interview with several screen demonstrations, operating examples, and explicit trust/skill-evolution judgment |
| Extraction value | **HIGH, with a narrow truth boundary.** The source contains a coherent operating system and several reusable workflow shapes, but some interfaces are illustrative or explicitly labeled simulated rather than production evidence. |

## Source Truth Boundary

Labels used in this checkpoint:

- **VERIFIED (spoken):** stated by Nathan, Kipp, or Kieran in the captured captions.
- **VERIFIED (visible):** readable in a captured frame.
- **SOURCE-REPORTED:** a result or scale claim made in the episode but not independently verified.
- **INFERRED:** an architectural implication supported by multiple source behaviors.
- **NOT ACQUIRED:** linked material was gated or unavailable and was not treated as evidence.

Important limits:

1. Nathan’s “team of one” scope and the comparison with a six-person systems team / larger operations organization are **source-reported**, not audited staffing or productivity evidence.
2. A visible footnote at approximately 13:28 labels a Model Council report as a **“simulated demo.”** The interface proves the decision-packet shape; it does not prove production reliability.
3. The hosts’ GTM “Super Pack” interface is a host-created demonstration that Nathan reacts to. Its exact skill catalog is not Nathan’s proprietary operating library.
4. Kieran’s Claude Code compression-hook method is Kieran’s contribution. It may inspire a companion integration, but it cannot be attributed to Nathan.
5. The linked free GTM prompt pack is email-gated. No email was submitted, and its contents are **NOT ACQUIRED**.

## Primary Evidence Anchors

| Time | Evidence | Status | Extraction implication |
|---|---|---|---|
| 02:25–03:05 | Nathan describes one-person coverage across RevOps, enablement, analysis, CRM/tool administration, procurement, and strategy | VERIFIED (spoken); scale comparison SOURCE-REPORTED | The target is an operator control plane, not one isolated automation |
| 04:30–05:40 | Model Council compares three frontier-model recommendations and renders cross-model agreement, disagreement, and supporting evidence | VERIFIED (visible) | Preserve contradictions and evidence instead of collapsing to a vote |
| 06:08 | “Look through my Teams open opportunities… Which city should we choose? Use model council with top 3 frontier models.” | VERIFIED (visible) | Short requests work because first-party context and an evaluation method already exist |
| 07:10–07:50 | CRM context can continue into audience selection, copy, and sequence construction | VERIFIED (spoken) | Treat the prompt as an entry point to a staged workflow, not the workflow itself |
| 07:50–10:35 | Start simple, split the end-to-end job into stages, inspect each stage, correct errors, package the proven flow as a skill, then schedule it | VERIFIED (spoken) | Autonomy is promoted through inspected stages, not granted by confidence |
| 11:20–12:15 | A two-line operational request can replace a ticket; the operator keeps a pinned control panel and receives a daily Slack summary | VERIFIED (spoken); interface visible | Natural-language intake requires visible state, attention queues, and scheduled-work status |
| 13:00 | Control panel separates “Needs attention” from “Scheduled” work | VERIFIED (visible) | Human work should be exception-shaped |
| 13:34–13:44 | GTM pack asks for role, tech stack, and company context, then exposes role-specific skills | VERIFIED (visible); host demo | Portability comes from explicit adapter/context inputs, not one hard-coded stack |
| 13:28 | “Source: Model Council reports: GPT 5.5, Claude Opus 4.8 (simulated demo)” | VERIFIED (visible) | Do not convert demo polish into a production claim |
| 17:36–19:10 | Long threads become personal skills; useful skills are shared, improved weekly, and hardened for organization-wide use | VERIFIED (spoken) | Promotion path: thread → personal skill → tested shared skill → hardened org asset |
| 19:56–20:49 | Contract-to-Closed-Won request references Drive, target CRM fields, and existing opportunities; run summary shows read-only reconciliation and manual-review counts | VERIFIED (visible) | Cross-system reconciliation should default to read-only reporting before write approval |
| 22:10–23:40 | Nathan recommends a daily voice-of-customer dashboard pulling calls/emails into themes, customer love, product/enablement actions, use cases, and stories | VERIFIED (spoken); dashboard visible | Customer evidence becomes routed operational work, not a passive research report |
| 24:10–25:10 | Career guidance centers on external and internal customer obsession | VERIFIED (spoken) | The control plane should optimize for customer and operator needs, not automation volume |

## What This Source Is Actually About

The episode’s surface topic is “one person using AI for RevOps.” The deeper operating idea is:

> **Turn first-party business context into small, observable workers that earn broader autonomy through reviewed outputs, then manage those workers through an exception-first control plane.**

The system is not defined by Perplexity Computer. It is defined by six coupled moves:

1. Start from first-party operating truth.
2. Convert a short request into explicit stages and deliverables.
3. Keep early runs inspectable and reversible.
4. Promote a proven thread into a named reusable skill.
5. Schedule only after the operator trusts the stages.
6. Route exceptions, summaries, and approval requests back to one control surface.

That is the extractable capability. The product interface is one implementation.

## Preliminary Genius

### 1. Context Before Prompt Length

Nathan’s examples use remarkably short requests, but the requests sit on top of connected CRM, contract, transcript, email, and company context. The hidden move is not brevity. It is relocating complexity from the prompt into durable first-party context.

### 2. Stage-Level Trust, Not Workflow-Level Faith

He does not ask whether the whole agent is trustworthy. He breaks a large job into stages, checks the quality and reasoning at each stage, fixes weak steps, and only then converts the chain into a recurring worker.

### 3. Reversible-First Deployment

The contract reconciliation demo produces a read-only run summary with generated, excluded, and manual-review counts before any CRM write. The human approval boundary sits immediately before the irreversible action.

### 4. Exceptions Become the Human Job

The control surface foregrounds “Needs attention,” then scheduled and active work. The operator stops manually performing every step and instead resolves ambiguity, approvals, and failures.

### 5. Thread-to-Asset Promotion

A long, useful conversation is a signal that the work has acquired enough context and repeatability to become a skill. Personal experimentation precedes organizational hardening.

### 6. Templates Seed; Operators Evolve

Nathan starts people from working templates, lets them build and share variations, then hardens the best performers for wider use. Central governance follows evidence rather than blocking experimentation up front.

### 7. Customer Signal Must Terminate in Action

The voice-of-customer dashboard does more than summarize calls. It routes findings toward product, enablement, customer stories, testimonials, and amplification. Research is complete only when ownership and next actions are attached.

### 8. Multi-Model Disagreement Is a Decision Surface

The displayed Model Council does not merely “make models agree.” It exposes where they agree, where they disagree, why they differ, and what evidence supports each conclusion. The disagreement is operational input.

## Existing-Roster Fit and Duplicate Audit

| Existing owner | Already owns | What Nathan adds | Boundary |
|---|---|---|---|
| `rachel-woods-ai-operations` | Process decomposition, per-task quality bars, MASTER specs, compound AI systems | RevOps-native application, short-request intake, control-panel operation, first-party GTM context | Do not recreate generic decomposition or AI transformation consulting |
| `nate-b-jones-trust-architecture` | Evidential trust ladders, permission tiers, error demotion, audit ledgers | A simpler operational promotion path demonstrated inside real work: stage → inspect → skill → schedule → exception review | Reference the existing trust architecture for thresholds; do not create a competing trust doctrine |
| `riley-brown-marketing-automation` | Turn successful work into skills, schedule recurring work, approval-gated drafts, small composable agents | Revenue-operations workflows, CRM reconciliation, pipeline hygiene, customer-signal routing, operator control panel | Do not duplicate generic “turn it into a skill” or marketing distribution workflows |
| `deliberate` | Cross-model comparison that preserves disagreement | First-party CRM decision packets and a visible evidence matrix | Use or extend `/deliberate`; do not build a second model-council command |
| Existing Antigravity control plane | Run receipts, mission state, scheduled work, health/status surfaces | A domain lens for GTM exceptions, reconciliations, pipeline state, and VOC actions | Do not create a parallel global control plane |

## Correction Receipt: `/deliberate`

The existing `/deliberate` skill says Perplexity’s Model Council produces an opaque synthesized answer and hides underlying disagreement. That statement was already marked as inferred/unconfirmed in its provenance.

This source now provides contrary visible evidence:

- separate model recommendations,
- a “Where Models Agree” matrix,
- a “Where Models Disagree” section,
- a “Why They Differ” column,
- evidence attached to findings,
- and language describing disagreement as the signal.

**Checkpoint recommendation:** preserve `/deliberate`’s contradiction-first competitive advantage, but remove the unsupported claim that Perplexity necessarily hides disagreement. The honest distinction should become:

> `/deliberate` guarantees a committed first take, a genuinely separate second-model call, raw contradiction preservation, and an explicit resolution rule; the video demonstrates that Perplexity’s illustrated Model Council can also expose agreement and disagreement.

This is a factual repair, not a reason to discard the skill.

## Recommended Build Shape

**Verdict: EXPAND + REPAIR.**

Provisional system shape:

1. **Create one new expert layer:** `nathan-follen-agentic-revops`.
2. **Keep it domain-specific:** it should compose existing decomposition, trust, deliberation, and skill-promotion capabilities rather than restating them.
3. **Build around five owned capability families:**
   - first-party GTM decision packets,
   - staged worker promotion,
   - exception-first RevOps control,
   - read-only reconciliation before approved mutation,
   - VOC-to-owner action routing.
4. **Surgically correct `/deliberate`** using this source as a provenance receipt.
5. **Do not create** a Perplexity-only mega-skill, a second council command, a generic autonomy framework, a second skill-creation workflow, or a parallel command center.

The final workflow count and command surface remain intentionally unlocked until the deep MES pass. The architecture checkpoint will name every file, owner, input contract, output contract, hard veto, and composition route.

## Farrice-Specific Uses

The source is unusually compatible with Farrice’s current operating reality:

- **Revenue:** inspect the Angle Map pipeline for stale opportunities, follow-up gaps, missing proof, and next-action exceptions without pretending that CRM hygiene equals demand.
- **Content:** route call, email, and audience evidence into the existing Content Signal Loop as sourced themes and actions, not invented voice-of-customer.
- **Client delivery:** reconcile signed agreements, onboarding artifacts, promised deliverables, and project state before any external mutation.
- **System operation:** convert recurring operator threads into candidates for skills only after repeat use proves the pattern.
- **Governance:** make autonomous scope earnable and reversible, with human approval immediately before external writes, sends, publishing, or CRM mutation.

## Checkpoint Decision

Approve this vision to proceed with:

1. full four-layer MES extraction,
2. source and speaker ledger,
3. exact connected-skill architecture,
4. `/deliberate` correction plan,
5. implementation only after the Architecture checkpoint is approved,
6. verification against real Farrice assets without external writes.

**Requested decision:** `Approve vision` or name the adjustment.

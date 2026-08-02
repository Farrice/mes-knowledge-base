---
date: 2026-08-01
session: alex-copper-static-acquisition
tier: operator-guide
status: enriched
---

# Alex Cooper Static Acquisition System — What We Built 2026-08-01 and How to Use It

> A source-grounded route for finding the missing acquisition hypothesis in a paid-social account, turning it into controlled static-ad tests, and proving the handoff behavior before anyone confuses workflow readiness with market proof. Start with [the extraction router](../extractions/alex-copper-static-ads/00-START-HERE.md), then invoke `/alex-copper-static-acquisition-system`.

## ⚡ If you only read 10 lines

1. Use `/alex-copper-static-acquisition-system` when an account keeps repeating the same persona, message, format, or selling mechanism.
2. Bring the product and offer, substantiated benefits, prohibited claims, persona, current ad inventory, provenance-labeled customer language, landing page, and available assets.
3. Mark missing facts `UNAVAILABLE`; never repair an evidence gap by inventing specificity.
4. Diagnose the account gap before making more ads. More volume is not a strategy.
5. Assume a cold viewer knows nothing about the brand and has no reason to care yet.
6. Choose whether each concept earns attention through clarity or curiosity, and define what the destination must complete.
7. Write the eye path—hook → qualifier → product → proof → action—before designing the layout.
8. Change one major variable per test so the result can teach the next decision.
9. Alex owns the acquisition hypothesis; Dara owns the production batch and one-second comprehension audit.
10. A clean workflow, attractive render, or simulated audit is not market proof. A real human panel and live media test are still required.

## Command table

| Invoke | What it produces | Use it when |
|---|---|---|
| `/alex-copper-static-acquisition-system` | Evidence-backed static acquisition test slate | The account has inventory but lacks a clear next acquisition hypothesis |
| `/dara-static-production` | Three controlled visual variations from one locked spec | The hypothesis and claims boundary are approved for production |
| `/dara-comprehension-audit` | One-second `KEEP`, `FIX`, or `KILL` verdict | Renders exist and need a pre-traffic comprehension check |
| `python3 execution/prose_classifier.py check <receipt.md>` | Prose-pattern scan | Before closing a strategy or production receipt |
| `python3 execution/claim_risk_scan.py scan <receipt.md>` | Claim-risk receipt | The product touches health, performance, sleep, finance, or another sensitive category |
| `python3 execution/content_finish_gate.py check --file <receipt.md> --platform artifact` | Finish-state verification | Before calling the written artifact complete |

## Mental model: one hypothesis travels through three owners

The system separates strategic judgment, production craft, and commercial truth.

| Stage | Owner | Question | Proof produced |
|---|---|---|---|
| Acquisition diagnosis | Alex Cooper route | What is the account not testing, and why might that matter to a cold buyer? | Evidence receipt, white-space diagnosis, concept slate, test matrix |
| Static production | Dara route | Can the hypothesis survive a real composition, eye path, and product presentation? | Controlled render batch and production receipt |
| Market validation | Brand or media owner | Does the concept outperform a control with real people and spend? | Human-panel results, campaign data, conversion evidence |

This separation prevents a common category error. Strategy can be coherent without being commercially proven. Design can be excellent without being comprehensible in one second. A simulated comprehension audit can expose obvious failures, but it cannot substitute for five unfamiliar humans or a live account.

## Capability 1: diagnose the account before producing more statics

### What it does

The Alex route reads the available account inventory as a pattern, not a pile. It looks for repeated personas, claims, visual forms, offer structures, and selling loci. The output names the narrowest meaningful gap and turns it into a testable acquisition hypothesis.

### Use it when

- The brand has plenty of ads but weak learning velocity.
- Creative reviews keep producing aesthetic opinions instead of test decisions.
- A team says it needs “new angles” but cannot show which old variables have already been tested.
- The landing page, offer, or proof burden changes what the ad must accomplish.

### Do not use it when

- The offer, claims boundary, or destination is unknown and cannot be supplied.
- The real problem is trafficking, broken attribution, or missing spend.
- The request is simply to resize an approved asset.

### How to run it well

Supply current ads, not just favorite references. Label customer language as `SUPPLIED`, `OBSERVED`, `INFERRED`, or `UNAVAILABLE`. State prohibited claims explicitly. Include the destination because a static should not promise work the landing page cannot finish. Require six to ten concepts, then reduce them to a single-variable matrix rather than producing every idea.

### Worked example

The fictional Morrow sleep product was used as a behavior-proof environment. The system created a control based on ordinary product clarity, a visual challenger using a thermal metaphor, and a headline challenger built around “Hot sleeper?” The result was not three equal winners: the control was kept, the thermal concept was kept for a substantiation-gated test, and the headline challenger was killed. That asymmetry is a feature. A system that keeps everything is not auditing.

### Honest edges

Morrow is fictional. Its product claims and commercial context do not establish real-category permission. The test proves the route can differentiate, render, and reject. It does not prove customer demand, media efficiency, or regulatory acceptability.

## Capability 2: convert a hypothesis into a controlled production batch

### What it does

The Dara handoff turns one acquisition idea into a locked visual specification and a small family of comparable renders. The production layer defines the frame, hierarchy, product role, copy volume, and one variable that changes between cells.

### Use it when

- The acquisition hypothesis is already explicit.
- Claims and product assets are permissioned.
- The team needs comparable options rather than unrelated mood-board directions.

### Do not use it when

- The strategic owner has not locked the test variable.
- The prompt asks the image model to solve copy, claims, layout, and strategy at once.
- A real brand has not approved the use of its product, identity, or proof assets.

### How to run it well

Lock one parent composition first. Verify the actual pixel dimensions, aspect ratio, product placement, and text legibility before branching variants. In the Morrow batch, the image model ignored the first 4:5 instruction. The repair was to correct the parent asset, verify its dimensions, and derive challengers from that corrected source. That solution is recorded in [the image-generation placement repair](../docs/solutions/2026-08-01-imagegen-static-placement-correction.md).

### Worked example

The final Morrow cells were all 1122 × 1402 pixels. Cell 01 served as the ordinary-product control. Cell 02 changed the visual mechanism to a thermal metaphor while preserving the core proposition. Cell 03 changed the headline. This made the comparison legible enough to issue separate `KEEP` and `KILL` decisions.

### Honest edges

Correct dimensions and coherent art direction do not guarantee platform-safe crops or winning performance. Run placement previews and real-device checks before traffic. Visual metaphors that imply physiological or product effects may still need substantiation review.

## Capability 3: hold a real-brand build when the evidence packet is incomplete

### What it does

The hardening route checks whether a real offer has enough approved evidence to move from conceptual workflow proof into public or paid production. It distinguishes “the system can build this” from “this brand is cleared to run it.”

### Use it when

- A real brand is the next candidate after a fictional proof run.
- Existing offer copy, customer language, proof, and payment mechanics may disagree.
- The creative team is tempted to treat local readiness as demand evidence.

### Worked example

The Angle Map was inspected as the real-brand candidate. The verdict was `HOLD`, not because the acquisition route failed, but because the required packet was incomplete: approved landing copy, exact-offer customer language, live paid-account inventory, permissioned proof, and a working payment rail were unavailable. The full decision is in [The Angle Map readiness receipt](../extractions/alex-copper-static-ads/hardening/THE-ANGLE-MAP-READINESS.md).

### Honest edges

A hold is a quality result when it names the missing evidence precisely. It is not a commercial rejection of the offer. Likewise, category activity is not exact-offer demand. Track `sent`, `held`, `sold`, and `collected` separately once the pilot reaches market.

## Capability 4: package the workflow as a bounded pilot

### What it does

The [Static Acquisition Sprint](../extractions/alex-copper-static-ads/productization/STATIC-ACQUISITION-SPRINT.md) turns the system into an internal pilot candidate with inputs, stages, deliverables, acceptance criteria, exclusions, and proof boundaries.

### Use it when

- One permissioned brand can supply a complete evidence packet.
- You want to test delivery behavior before publishing an offer.
- The team needs a repeatable container for diagnosis, production, audit, and measurement.

### Do not use it when

- Price, timing, and capacity are being presented as validated market facts.
- No real media owner can run the test.
- The customer cannot provide approved assets or claim boundaries.

### Honest edges

The Sprint is ready as an internal pilot definition, not a public offer. Price, turnaround, capacity, and demand are parked until a real delivery cycle produces evidence. The first pilot should preserve the control, collect the five-person comprehension panel, and define the live-test success measure before production begins.

## Recommended operating sequence

1. Open [the extraction router](../extractions/alex-copper-static-ads/00-START-HERE.md).
2. Assemble the real-brand evidence packet and mark every source by provenance.
3. Invoke `/alex-copper-static-acquisition-system` and lock one acquisition hypothesis.
4. Route the approved handoff through `/dara-static-production`.
5. Run `/dara-comprehension-audit`, then repeat the one-second test with five unfamiliar humans.
6. Fix or kill failed cells before traffic.
7. Launch one controlled paid test against the preserved control.
8. Record what was sent, held, sold, and collected; do not promote the Sprint on workflow quality alone.

## Core files

- [System router and start point](../extractions/alex-copper-static-ads/00-START-HERE.md)
- [Alex workflow](../skills/alex-copper-creative-strategy/workflows/07-static-acquisition-system.md)
- [Born-v2 execution prompt](../skills/alex-copper-creative-strategy/references/prompts-v2/static-acquisition-system.md)
- [Source evidence ledger](../skills/alex-copper-creative-strategy/references/static-ads-2026-source-ledger.md)
- [Morrow production and audit receipt](../extractions/alex-copper-static-ads/production/morrow-sleep-concept-a/PRODUCTION-AND-AUDIT.md)
- [The Angle Map readiness receipt](../extractions/alex-copper-static-ads/hardening/THE-ANGLE-MAP-READINESS.md)
- [Static Acquisition Sprint pilot](../extractions/alex-copper-static-ads/productization/STATIC-ACQUISITION-SPRINT.md)

## Current proof state

**LOCKED:** The in-place Alex expansion, command routing, source ledger, production handoff, three-cell Morrow proof, comprehension verdicts, real-brand readiness gate, and internal pilot container.

**PARKED:** Public offer language, price, turnaround, capacity claims, exact-offer demand claims, and any claim that the system has improved paid performance.

**NEXT ACTION:** Run a real five-person one-second test on Morrow cells 01 and 02, then select one permissioned brand with a complete evidence packet for the first paid-media pilot.

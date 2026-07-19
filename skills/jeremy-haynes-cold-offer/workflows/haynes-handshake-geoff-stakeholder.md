---
description: Handshake — Woods' stakeholder-simulation panel stress-tests a Haynes-composed cold offer BEFORE it reaches a real prospect
---

# `/haynes-handshake-geoff-stakeholder` — Haynes × Woods Handshake

The compound output: Haynes composes the offer stack (narrative-derived components, core/editions split, objection inventory). Woods' simulated stakeholder panel then reads the ACTUAL composed offer and returns per-element kill/revise/ship verdicts, with the panel's strongest objections preserved verbatim, before a real prospect ever sees it. Sequential, not parallel. The panel never simulates a stack Haynes hasn't finished composing.

## Genius Context (Load First)

Read both:
- `skills/jeremy-haynes-cold-offer/genius.md`: the 8-step spine (COMPOSE/LAYER/AUGMENT), component traceability ("not random"), objection pie-chart triage
- `skills/geoff-woods-ai-thought-partner/genius.md`: Pattern 6 (Stakeholder Simulation with Reality Calibration), Pattern 1 (Interview Inversion), Pattern 13 (Cognitive Sovereignty / anti-sycophancy)
- `skills/geoff-woods-ai-thought-partner/references/CO-CREATION-CARD.md`: Lineage A move 4 (Challenger flip before high-stakes ship) governs the posture of this whole workflow

Internalize:
- Haynes builds a stack that's internally coherent with the ICP's narrative. But internal coherence is not the same as surviving contact with a specific, skeptical, incentive-bearing buyer. Woods' simulated room supplies the pressure Haynes' own method doesn't apply. Not "does every component trace to a narrative element" but "what does THIS person, in THIS seat, actually say when they read it."
- **Stack thesis**: Haynes alone ships a well-composed offer that's never been read by anyone but its author, cold-stranger legibility tested against an imagined average rather than a specific hostile reader. Woods alone simulates a room with no offer discipline underneath it: sharp objections aimed at a stack that was never traceability-checked in the first place. Together, the offer both traces to the buyer's narrative AND has already absorbed its hardest real objections before the first live conversation.
- **What this replaces**: sending a freshly composed offer straight into a discovery call or cold DM and treating the prospect's live objection as the first data point. That is expensive feedback. This workflow makes the panel absorb that cost first, in simulation, where a bad reaction costs nothing.

## Stacking Partners

- **Jeremy Haynes (Cold-Traffic Offer)**: supplies the INPUT, the composed offer stack (core + editions, narrative-traced components) and the objection inventory, either mined from real sales calls via `/jh-objection-mine` or the offer author's best-guess objection list if it's pre-market
- **Geoff Woods (AI Thought Partner)**: supplies the RISK-GATE, a panel of distinct simulated stakeholder personas, each interview-inversion profiled with real incentives rather than generic "skeptical buyer" archetypes, reading the actual offer and returning verdicts under the cognitive-sovereignty guard. The panel is built to find cracks, not to validate.

## When to Use

- A Haynes offer stack is composed (via `/jh-offer-stack` or already documented) and is about to go in front of a real prospect for the first time
- The offer has never been read by anyone who isn't the person who built it
- Money, reputation, or a limited-capacity pilot slot is riding on first contact going well (small-batch offers can't afford to A/B test against real prospects)
- An existing offer keeps landing flat on discovery calls and the team suspects the objection inventory is incomplete or wrong
- Before a cold-DM or outreach sequence goes wide on a new or revised offer

## Pre-Flight Gate

- **Composed stack required.** No stack, no simulation. Run `/jh-offer-stack` (or pull the existing offer doc) first. Simulating an unfinished offer just confirms the offer is unfinished.
- **Stakeholders must be real seats, not archetypes.** "A skeptical buyer" is not a stakeholder profile. "The VP Brand at a funded supplement company who has burned budget on agencies twice" is. If the real prospect isn't identified yet, build the panel from the ICP's most common buyer-side roles instead of inventing a single composite skeptic.
- **The self-selection stakeholder is mandatory, not optional** (see Guardrails). A panel of only people the offer is FOR never tests whether the offer over-claims its fit.

## The Handoff Contract

Haynes' pass outputs exactly one artifact that crosses the boundary, the **Offer Stack + Objection Inventory**:

```
OFFER ELEMENTS: [core components + editions, each with its narrative-element tag]
OBJECTION INVENTORY: [from /jh-objection-mine if data exists, else "pre-market — best-guess list"]
AUDIENCE STATE: [in-market / needs-convinced, per Haynes' classification]
BRIDGE ARTICULATION: [the problems → circumstances → outcomes → offer draft, as written for the prospect]
```

Woods' panel consumes the full stack, not a summary (Woods fed the real 60-slide deck, not a synopsis), and returns exactly one artifact, the **Verdict Sheet**:

```
PER-ELEMENT VERDICT: [element] → KILL / REVISE / SHIP → reasoning
STRONGEST OBJECTIONS (VERBATIM): [stakeholder name/role] said: "[exact simulated quote]"
DISSENT LOG: [where stakeholders disagreed with each other, preserved, not averaged]
SELF-SELECTION FINDING: [what the no-problem-here stakeholder said; did the offer over-claim fit?]
```

Haynes' components do not get re-composed inside the simulation. The panel reacts to what exists. If the Verdict Sheet kills or revises an element, that revision loops back through Haynes' COMPOSE/LAYER discipline (does the fix still trace to a narrative element?) rather than through ad-hoc rewriting inside the panel step.

## Fused Sequence

### Step 1 — Intake the Offer + Objection Inventory (Haynes)
Pull the composed stack in full: every core component and edition, each tagged to the narrative element it neutralizes, plus whatever objection data exists (mined transcripts or best-guess). If audience state (in-market/needs-convinced) isn't declared, declare it now. It determines which stakeholder reactions are even plausible.

### Step 2 — Cast the Stakeholder Panel (Woods)
Identify 3+ real stakeholder seats relevant to this specific sale, by name if the prospect is known, by role/incentive if not. **At least one seat must be a stakeholder who has NO problem this offer solves** (see Guardrails). Each seat needs a stated incentive: what they personally win or lose from a yes, a no, or a stall.

### Step 3 — Interview-Inversion Profiling (Woods, one stakeholder at a time)
For each seat, run the interview inversion: cast the role as an HR-grade profiler, and ask the offer author one question at a time (up to 5) to build the stakeholder's personality profile: what they defend, what derails them, what they've been burned by before. Complete one profile fully before starting the next. Run the Feedback Triad on each profile ("don't trust it") before it's used to simulate. An un-triaded profile isn't ready.

### Step 4 — Cognitive-Sovereignty Guard (Woods)
Before the panel reads the offer, set the guard explicitly: this panel exists to stress-test, not to flatter. No stakeholder profile defaults to agreeable. Treat the panel's first reaction to any element as "the bad answer" and push past the first pass if it reads as generic approval with no friction anywhere.

### Step 5 — The Panel Reads the Actual Offer (Woods)
Feed the real stack (bridge articulation, core components, editions, pricing, guarantee) through every stakeholder simultaneously. For each, report: predicted reaction, which element triggers it, and whether it's a kill-the-deal objection or a manageable friction point. Person-specific and element-specific, never a generic "the room might have concerns."

### Step 6 — Verdict Sheet + Dissent Preservation (Fused)
Compile the per-element kill/revise/ship verdicts. Where stakeholders disagree with each other, log the disagreement explicitly. **Never average two conflicting verdicts into a blended "mostly positive" read.** The self-selection stakeholder's reaction gets its own line: did they correctly self-disqualify (offer legibility working) or did the offer's language make them think it might apply to them anyway (over-claim risk)?

### Step 7 — Loop Revisions Back Through Haynes (Haynes)
Any element marked REVISE returns to Haynes' COMPOSE/LAYER discipline. The fix must still trace to a narrative element, not just neutralize the simulated objection cosmetically. An element patched only to satisfy the panel, with no narrative anchor, is a new orphan component and fails Haynes' own traceability test.

### Step 8 — Reality-Calibration Hook (Woods, post-contact)
Once the offer actually meets a real prospect, feed the outcome back: which predicted objections fired, which didn't, what the panel missed. Update the stakeholder profiles so the next simulation is truer. Not required to close this workflow, but the loop should be handed to the operator as the explicit next step. A simulation never diffed against reality stops learning.

## Guardrails (non-negotiable)

- **The self-selection stakeholder is mandatory.** Every panel includes at least one person who has NO problem this offer solves: a founder who thinks their in-house team already covers it, a buyer in the wrong budget band, a role the offer wasn't built for. This is the only way to test whether the offer's language over-claims fit to people it shouldn't convert. A panel built only from people the offer is FOR cannot catch this failure mode.
- **Dissent is preserved, never averaged.** If two stakeholders read the same element differently, the Verdict Sheet reports both, attributed by name/role. Consensus-blending two real disagreements into one soft verdict is a failure of this workflow, not a simplification.
- **Objections are verbatim, not paraphrased.** "Some concern about price" is not an objection. "The CFO said: 'walk me through why this costs more than hiring someone part-time for a month'" is. Paraphrasing loses the exact language the offer needs to survive.
- **The panel's job is to find cracks, not confirm the offer works.** Any panel pass that returns uniform approval with no friction has not been run hard enough. Go back through Step 4.

## Output Schema

```markdown
# [Offer] — Haynes × Woods Handshake Verdict Sheet

## Offer Stack Intake (Haynes)
[Core + editions, narrative tags, audience state, bridge articulation, as composed]

## Stakeholder Panel (Woods)
[Per stakeholder: role, incentive, triad-verified profile summary]

## Per-Element Verdict Table
| Element | Verdict (KILL/REVISE/SHIP) | Reasoning | Objection(s), verbatim |
|---|---|---|---|

## Dissent Log
[Where stakeholders disagreed, both readings, attributed]

## Self-Selection Finding
[The no-problem-here stakeholder's reaction: correct self-disqualification or over-claim risk]

## Revision Loop (if any REVISE verdicts)
[Element → Haynes-side fix → narrative-element it now traces to]

## Reality-Calibration Next Step
[What to capture from the real first-contact event, to feed back and recalibrate]
```

## Quality Gate

- Every stakeholder profile is interview-inversion built and triad-verified before the panel reads the offer. No invented composite skeptic stands in for a real seat.
- The self-selection stakeholder is present in every run and has its own finding line. Its absence fails this workflow outright.
- Objections in the Verdict Sheet are verbatim quotes, never paraphrased into generic categories.
- Dissent between stakeholders is logged explicitly, never blended into a single averaged verdict.
- Any REVISE verdict routes back through Haynes' traceability discipline, not ad-hoc patching.
- The panel's overall read has visible friction somewhere. A frictionless pass gets re-run under the cognitive-sovereignty guard.

## What This Replaces

Sending a freshly composed offer into its first real conversation and treating the prospect's live objection as the first signal. That's expensive feedback on a small-capacity or reputation-sensitive offer, and a single anecdote that (per Haynes' own anti-pattern list) too easily triggers a full offer redesign off one loud reaction. It also replaces generic "does this sound good?" validation passes, which return sycophantic approval by default. Woods' cognitive-sovereignty guard is specifically what makes this panel adversarial instead of a rubber stamp.

## Pairs With

- `skills/jeremy-haynes-cold-offer/workflows/jh-objection-mine.md`: upstream, if real sales-call data exists to seed the objection inventory
- `skills/jeremy-haynes-cold-offer/workflows/jh-offer-stack.md`: upstream, if the offer isn't composed yet
- `skills/geoff-woods-ai-thought-partner/workflows/07-simulate-room.md`: the underlying Woods mechanism this handshake specializes for offers
- `skills/geoff-woods-ai-thought-partner/workflows/09-cognitive-guard.md`: if the panel keeps returning frictionless verdicts, audit whether the sim itself has gone sycophantic

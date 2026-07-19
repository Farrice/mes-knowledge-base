---
name: Buyer Council
command: /buyer-council
tier: 3 (Stacking)
description: Convene a simulated buyer/customer panel against ANY artifact (idea, concept, offer, content piece, GTM plan) for predictive-marketing verdicts, not audit feedback. Two modes: TRIAGE (Taylor, ~5 min, single joint-anonymous answer) and COUNCIL (full dissent-preserved roster)
inputs: Artifact (the real thing, in full); buyer spec OR named standing-roster panel; the decision question
outputs: Buyer Council Verdict Sheet + Predicted Response Map + 1-3 highest-impact revisions + one calibration.jsonl line
---

# `/buyer-council` — Predictive Buyer Panel

Generalizes Pattern 6 (Stakeholder Simulation with Reality Calibration) from internal stakeholders to the market itself. `/haynes-handshake-geoff-stakeholder` already proved this engine on cold-offer stacks: dissent-preserved KILL/REVISE/SHIP verdicts, a mandatory self-selection seat, verbatim objections, no consensus-averaging. This workflow points the same machinery at any artifact, for any buyer, not just Haynes offer stacks. It's the general case; that handshake stays the cold-offer specialization.

## Mode Split (Choose Before Running Anything)

Two entry modes. Decide which one before Panel Assembly runs.

- **TRIAGE (Taylor mode, ~5 min)**: no roster, no interviews, no standing panel. Cold-generate 10 demographic buyer personas for the product ("give me 10 personas, like real people, who'd buy X"). Each persona answers the decision question individually, never one averaged stock answer. Then, Taylor's exact mechanic: combine the individual responses into a single paragraph "as if these people had collaborated in writing a joint anonymous answer." Use for fast directional calls: headline A/B, concept gut-check, early positioning smell test.
- **COUNCIL (full mode)**: the roster/interview/dissent-preserved pipeline below, unchanged.

TRIAGE synthesizes one voice for speed. COUNCIL preserves dissent for stakes. Escalate from TRIAGE to COUNCIL the moment money, launch, or strategy hangs on the answer.

## Genius Context (Load First)

- `skills/geoff-woods-ai-thought-partner/genius.md`: Pattern 6 (profile, triad, assemble, read the real artifact, predict, calibrate against reality) and Pattern 8 (anti-sycophancy: cast the panel adversarial, never agreeable by default)
- `skills/geoff-woods-ai-thought-partner/workflows/07-simulate-room.md`: the underlying mechanism this workflow specializes for buyers instead of internal stakeholders
- `skills/jeremy-haynes-cold-offer/workflows/haynes-handshake-geoff-stakeholder.md`: sibling workflow. Its schema (Verdict Sheet, dissent log, self-selection finding) is reused verbatim here, generalized past cold offers

## Intake Contract

```
ARTIFACT: [the idea / concept / offer / content piece / GTM plan, in full, never a summary]
PANEL: [named roster panel from councils/buyers/, OR a buyer spec to build fresh]
DECISION QUESTION: [what verdict is actually needed: ship/kill/revise a specific element, choose between options, predict launch response]
```

If PANEL names an existing file in `councils/buyers/`, load it. Do not rebuild personas that already exist. If no roster entry fits the buyer, build fresh (Panel Assembly below).

## Panel Assembly

1. **Check the standing roster first.** `councils/buyers/` holds panels seeded per audience (`proof-to-market-founders.md`, `mybpm-streetwear.md`). Reuse a matching panel instead of regenerating it. The standing asset is the point; rebuilding from scratch every run throws away the calibration history it's earning.
2. **No fit, build fresh.** Use the interview-inversion style from Pattern 6 / `07-simulate-room.md`: one seat at a time, up to 5 questions, triad-verify each profile before it reads anything.
3. **Deep-seat options, never required pipeline steps, lightest first.** If real customer call/interview transcripts exist for this audience, paste them into the persona prompt and have the model roleplay as those specific customers instead of inferring from training data. That's the lightest-weight grounding move, and the highest-fidelity one when transcripts exist, and it applies in either mode. Heavier options for a seat that needs more depth than a quick card: dispatch `mcclain-persona-forge` (narrative-prose persona, 500-2000 words) or `icp-deep-canvasser` (identity-level resistance mapping). Most runs need none of the three. A tight 80-120 word card per seat is the default.
4. **Mandatory seats.**
   - At least one **NO-FIT buyer**: someone this artifact should NOT convert. Tests self-selection. Does the language over-claim fit to people it shouldn't reach? A panel built only from people the artifact is FOR cannot catch this.
   - At least one **economic gatekeeper** when price is involved: whoever actually controls or defends the spend (a founder writing their own check, a CFO, a budget-conscious buyer weighing this against something else they'd rather buy).

## Simulation Pass

Each persona reads the actual artifact, not a synopsis. For each persona, return:

1. **First-15-seconds reaction**: what they notice, feel, or object to before they've processed the whole thing.
2. **Strongest objection, verbatim**: an exact quote in their voice, never paraphrased into a category. "Some concern about price" fails. "Walk me through why this costs more than hiring someone part-time for a month" passes.
3. **What would flip them**: the specific, speakable thing that would move a no toward a yes.
4. **KILL/REVISE/SHIP verdict per major element**: not one verdict for the whole artifact. Per element, because different personas will split on different pieces.

**Dissent is preserved, never averaged.** If two personas read the same element differently, the Verdict Sheet reports both, attributed by name or seat. Blending two real disagreements into one soft verdict is a failure of this workflow, not a simplification. Same guardrail as the Haynes handshake.

## Output

### Buyer Council Verdict Sheet
```markdown
# [Artifact] — Buyer Council Verdict Sheet

## Panel
[Which roster file, or fresh-built seats + one-line why]

## Per-Element Verdict Table
| Element | Verdict (KILL/REVISE/SHIP) | Reasoning | Objection(s), verbatim |
|---|---|---|---|

## Dissent Log
[Where personas disagreed, both readings, attributed by seat]

## Self-Selection Finding
[The NO-FIT persona's reaction: correct self-disqualification, or over-claim risk?]

## Economic Gatekeeper Finding
[If price is involved: does the spend defense hold, or is there a cheaper/no-purchase path they'd take instead?]
```

### Predicted Response Map (per-persona)
```markdown
## [Persona name/seat]
First-15-seconds: [...]
Strongest objection (verbatim): "[...]"
What flips them: [...]
```

### Closing: 1-3 Highest-Impact Revisions
Ranked by how much predicted outcome each protects. Not a full rewrite list. The few moves that matter most.

## Reality-Calibration Loop

Every council run appends one line to `councils/buyers/calibration.jsonl`:
```json
{"ts": "[ISO timestamp]", "artifact": "[name/path]", "panel": "[roster file or 'fresh']", "headline_prediction": "[the single most falsifiable prediction]", "real_outcome": "pending"}
```
When a real outcome lands (launch data, actual buyer reaction, sales result), find the line and update `real_outcome` from `"pending"` to what actually happened. This operationalizes Pattern 6's reality-calibration loop as a standing ledger instead of a one-off diff. Predictions checked against reality, across many runs, are how a panel earns trust. The Haynes handshake does the same thing per-offer in its Step 8; this makes it a persistent record across every buyer-council run.

## What This Replaces (Real-Research Boundary)

TRIAGE replaces the roughly $8-12K, weeks-long focus group otherwise needed for the "99 questions you can't afford to ask." It pre-filters which of those questions deserve real research budget. It never replaces real research on the questions that survive triage; those still go to actual customers, actual data, before money moves on them.

Latent-demand probe (either mode): add a per-persona question independent of the decision question, "what are your most pressing problems?", to surface segments or targeting angles the roster didn't anticipate, not just a verdict on the artifact in front of it.

## Not This

- Expert-side councils (multi-expert debate on strategy or craft): route to `/convene`. That's experts arguing. This is buyers reacting.
- Cold-offer-specific stress test with objection-inventory intake and a COMPOSE/LAYER revision loop: route to `/haynes-handshake-geoff-stakeholder`. This front door is the general case; that workflow is the offer-stack specialization.
- Internal stakeholder pre-test on a known room (board, exec team): use `07-simulate-room.md` directly, unspecialized.

## Quality Gate

- [ ] Mode declared (TRIAGE or COUNCIL) before the run started; escalated to COUNCIL if money, launch, or strategy hangs on the answer
- [ ] TRIAGE only: all 10 personas answered individually before the joint-anonymous paragraph was written, never one averaged answer first
- [ ] Panel reused from `councils/buyers/` if a fit existed; only built fresh if none did
- [ ] NO-FIT seat present with its own finding line. Absence fails this workflow outright.
- [ ] Economic gatekeeper seat present whenever price is in scope
- [ ] Objections are verbatim quotes, never paraphrased into generic categories
- [ ] Dissent between personas logged explicitly, never blended into an averaged verdict
- [ ] At least one prediction in the Response Map is specific enough to be falsifiable against a real future outcome
- [ ] `calibration.jsonl` line appended before the run is considered closed

## Pairs With

- `skills/geoff-woods-ai-thought-partner/workflows/07-simulate-room.md`: the base mechanism
- `skills/jeremy-haynes-cold-offer/workflows/haynes-handshake-geoff-stakeholder.md`: sibling specialization for cold-offer stacks
- `skills/corey-mcclain-persona-engineering/workflows/mcclain-persona-forge.md` and `icp-deep-canvasser`: optional deep-seat construction
- `/convene`: escalate to a full expert council if the buyer panel surfaces a strategy question, not a buyer-reaction question

## Lineage

COUNCIL mode combines Pattern 6 (Woods) and the Haynes×Woods stakeholder handshake, the dissent-preserving machinery. TRIAGE mode is Mike Taylor's synthetic-customer process (co-author, O'Reilly *Prompt Engineering for Generative AI*; Marketing Against the Grain, "This AI Prompt Gets You Customer Insights in 5 Minutes," YouTube `2f7pUdn1miE`; Recall `ce789f0b-9c63-4775-b0b7-c44edad29e23`, saved 2025-09-03), one of Farrice's highest-return processes.

---
description: "/mt-distribution-calibration-check — the validity-theory audit for any synthetic panel output: grounding tier, self-consistency ceiling, distribution-vs-individual accuracy split, sycophancy bias scan, and thread-contamination (vegan problem) check. Run before a synthetic verdict gets treated as more reliable than it is."
---

# Distribution & Calibration Check

Every other workflow in this skill produces a verdict fast. This one asks whether that verdict deserves the confidence it's about to be given. Run it whenever a synthetic-panel output is about to inform a real decision above trivial stakes, or whenever a panel result looks suspiciously clean.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Patterns 6-10, Hidden Knowledge, Decision Framework Q4-7).

> **Pre-Flight Gate**: This workflow audits an existing panel output — it doesn't generate a new one. Bring the output from `mt-persona-panel-triage.md`, `mt-persona-grounding.md`, `mt-latent-demand-mining.md`, or `mt-concept-headline-triage.md` to it.

## Input Required
- The panel output being audited (full, not summarized)
- How the panel was generated: cold, grounded (with transcript count), or calibrated
- Whether personas were generated in a shared thread or isolated threads
- The stakes of the decision this output is informing (trivial directional call vs. money/launch/strategy decision)

## Workflow

### Step 1: Grounding Tier Confirmation
State which tier this panel actually ran at (LIKELY-band Grounding Ladder, `genius.md` Pattern 6):
- **Tier 1**: calibrated against real response-matching (rare — requires actual calibration infrastructure, not just real data present somewhere)
- **Tier 2**: built from real transcripts, uncalibrated
- **Tier 3**: cold-generated, no real data

Flag any output claiming higher confidence than its actual tier supports.

### Step 2: Self-Consistency Ceiling Check
Remind the reader of the accuracy ceiling: even real humans surveyed twice disagree with themselves close to 10% of the time (LIKELY, secondary corroboration). No synthetic panel should be held to a higher bar than "roughly matches how the real population would answer, not exactly." Flag if the output (or the reader's expectation of it) is implicitly demanding perfection.

### Step 3: Distribution vs. Individual Accuracy Scan
Check every claim in the output: is it stated as an AGGREGATE/directional finding, or does it name a SPECIFIC individual's predicted literal behavior? Aggregate claims can carry real (bounded) confidence. Any individual-level literal claim gets flagged as illustrative only — synthetic panels can hallucinate plausible-but-false specifics at the individual level even when the aggregate is sound.

### Step 4: Sycophancy Scan
Is the panel's result suspiciously unanimous, uniformly positive, or flattering to the thing being tested? "It will always tell you your ideas are great" is the default failure mode of an ungrounded panel. A too-clean result is a diagnostic signal, not a clean verdict — re-run with adversarial framing (ask personas to find the weakest point, not just react) or with real grounding data before trusting it.

### Step 5: Thread-Contamination Check (the "vegan problem")
Confirm personas were generated in isolated threads/contexts, not one shared thread where later personas could drift toward earlier ones' answers. If contamination is possible, flag the output's dissent as potentially understated — real disagreement may have been smoothed by proximity during generation, not by genuine consensus.

### Step 6: Stakes-Weighted Verdict
Given tier, ceiling, distribution discipline, and bias scan — is this output fit for the stakes of the decision it's informing? Trivial directional calls can proceed on a clean-enough Tier 2/3 result. Money/launch/strategy decisions should escalate — route to `mt-synthetic-vs-real-decision.md`.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| Any panel output above trivial stakes | Full six-step audit |
| Quick directional check, low stakes | Steps 1 + 4 only (tier + sycophancy scan) — full audit is overkill |
| Panel output feeding a real launch/spend decision | Full audit is mandatory, not optional, before the output informs the decision |

## Output Format
```
DISTRIBUTION & CALIBRATION CHECK — [audited output] — [date]

GROUNDING TIER: [1/2/3] — [confidence language in the original output matches / overstates the tier]
SELF-CONSISTENCY CEILING: [flagged if perfection is being implicitly demanded]
DISTRIBUTION vs INDIVIDUAL: [n] aggregate claims (confidence OK) / [n] individual-literal claims (flagged illustrative-only)
SYCOPHANCY SCAN: [clean / suspicious — unanimity or flattery noted] → [action: accept | re-run adversarial]
THREAD CONTAMINATION: [isolated / shared-thread risk flagged] → [dissent may be understated if shared]

STAKES-WEIGHTED VERDICT: [fit for stated stakes | escalate to mt-synthetic-vs-real-decision.md]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] Grounding tier stated and checked against the confidence language actually used in the audited output
- [ ] Self-consistency ceiling named so perfection isn't the implicit bar
- [ ] Every claim classified aggregate vs. individual, individual claims flagged illustrative
- [ ] Sycophancy scan run — unanimous/flattering results explicitly flagged, not accepted at face value
- [ ] Thread-contamination risk assessed
- [ ] Stakes-weighted verdict names whether escalation to real research is warranted

## Common Pitfalls
- **Auditing generation instead of the output.** This workflow doesn't regenerate a panel — it audits one already produced.
- **Treating LIKELY-band accuracy percentages as audited fact.** They're carried here as directional calibration knowledge, not verified statistics — say so if citing them.
- **Skipping the audit because the result "feels right."** A result that confirms what the operator already believed is exactly when the sycophancy scan matters most.

Execution prompt: `references/prompts-v2/distribution-calibration-check.md`

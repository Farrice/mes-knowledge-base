# Behavior Proof: Proof Before Story

## Input Tested

A travel brand says its seven-to-ten-day trips are unusually transformative and
high value. It has founder confidence, a price, and a source-reported retention
claim, but no permissioned before interviews, after interviews, observable turn,
or organized visual/testimonial proof.

## Weakness Diagnosed

The audience is being asked to imagine the transformation. The material does
not support a factual full story, and polishing the promotion cannot close the
evidence gap.

## Source Mechanics Used

- Imagination-gap diagnosis (`00:08:49-00:09:12`).
- Multi-format proof documentation (`00:08:30-00:09:32`).
- Before/after transformation instead of a promotional commercial
  (`00:10:35-00:11:25`).

## Output Produced

```text
Narrative decision: NO STORY
Primary job: acquire inspectable transformation proof before promotional story production
Production owner: /proof-portfolio-builder

Proof-capture handoff:
- Claim to replace: "our experience changes people"
- Current proof: price and retention claim only; provenance and permission unresolved
- Before needed: participant's own words about fear, constraint, or starting condition
- Obstacle needed: the real moment or friction that made the outcome uncertain
- After needed: participant's observable change and own interpretation
- Turn needed: evidence of what happened between before and after; otherwise [NEEDS SOURCE]
- Capture forms: consented written/video testimonial, trip photo/video, relevant artifact or metric
- Permission: explicit downstream-use boundary before publication

Exit condition: return to /shaan-story-deploy only when want, obstacle, change,
and supported turn can be traced to real evidence.
```

## Behavior Delta

- **Before:** the router could correctly reject a full story but leave the
  operator at a dead end or send the task to a generic direct-content owner.
- **After:** a brand/sales claim-only case remains `NO STORY` and receives a
  specific existing-owner proof-acquisition path. The source changes the next
  action without creating a new storytelling authority.

## Negative Controls

1. **Technical incident:** remains `NO STORY`; routes to the incident/status
   owner. Proof capture does not solve the job.
2. **Health research explainer:** evidence spine remains primary; narrative
   cannot strengthen causality. No customer-transformation capture route fires.
3. **Verified customer case with sourced want, obstacle, change, and turn:** may
   qualify for `FULL STORY`; the proof-before-story recovery route stays cold.
4. **Two dated artifacts with no sourced turn:** remains `DOCUMENTED CONTRAST`
   or `STORY FRAGMENT`; no conversion scene is invented.

## Validation Run

- **PASS — source package:** 1,464 transcript segments, 8,632 clean words,
  and 1,464 observed-spoken ledger rows.
- **PASS — dedicated integration:** claim-only brand/sales input stays
  `NO STORY`, negative controls stay outside proof capture, and Shaan/Luke
  ownership remains unchanged.
- **PASS — Shaan skill:** six checks passed, zero critical failures. The one
  warning is the skill's pre-existing optional `hidden-knowledge.md` absence.
- **PASS — prompt surface:** 3,926 v2 prompt files passed the Renaissance audit.
- **PASS — discoverability:** `/shaan-puri-storytelling`,
  `/bw-proof-story`, and `/proof-portfolio-builder` remain indexed; no new
  command or expert was added.
- **PARTIAL — canonical extraction verifier:** the workflow names
  `execution/verify_behavior_changing_extraction_contract.py`, but that active
  verifier path does not exist. The source-package and dedicated integration
  verifiers above provide task-specific proof; the stale global path was not
  repaired as part of this bounded extraction.

## Remaining Risk

This is local behavior and structural proof. It is not a market event, content
performance result, customer-consent event, or independent blind preference
test. Live usefulness remains `UNTESTED` until a real claim-only brand case
produces proof and re-enters the story router.

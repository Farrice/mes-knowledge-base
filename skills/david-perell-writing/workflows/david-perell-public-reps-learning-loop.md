---
name: david-perell-public-reps-learning-loop
produces: Authorized Rep Protocol or evidence-bounded Rep Learning Receipt
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: A writer has an approved practice window or real published samples and wants a bounded learning loop.
---

# Public Reps Learning Loop

## Pre-Flight Gate

Read `genius.md` and `references/implementation.md`. Select exactly one mode: `PLAN` for an explicitly approved practice window before any event, or `LEARN` for user-supplied published samples and dated response evidence. No approved window returns `NO PERMISSION`. No actual published event in LEARN mode returns `NO EVENT`. This workflow never publishes, schedules, queues, fetches analytics, or infers market effect.

## Input Required

1. Mode: `PLAN` or `LEARN`.
2. Permission scope and practice window for PLAN.
3. Published artifacts, dates, channels, and supplied response evidence for LEARN.
4. Learning objective.
5. Stop conditions and privacy constraints.

## Procedure

### PLAN Mode

Record the exact authorized window, channels, content types, cadence, and stop conditions. Define one learning objective per rep—observation, opinion formation, or craft. Identify the upstream artifact and the evidence to capture. Return an Authorized Rep Protocol marked `NO EVENT`.

### LEARN Mode

Validate each event's artifact, publication date, audience or channel, and response evidence. Label statements `OBSERVED`, `BOUNDED HYPOTHESIS`, or `UNKNOWN`. Record what the act of publishing caused the writer to notice. Keep craft, packaging, current velocity, and audience fit as competing explanations. Choose one next rep that can discriminate among them.

### Effect Separation

Report reach, audience fit, recognition, conversion, revenue, and collected cash separately. Mark any unsupported business effect `UNTESTED EFFECT`.

### Route

Private observation belongs to `david-perell-observation-mind-mine`. Queue and performance work belongs to Kieran Content Ops. A supplied current packet may go to `david-perell-current-fit-diagnostic`.

## Output Schema

```text
## Rep State
Mode: PLAN | LEARN
State: NO EVENT | NO PERMISSION | EVENT EVIDENCE PRESENT
Permission scope:

## Event or Planned-Rep Inventory
| Rep or artifact/date | Learning objective | Audience/channel | Upstream artifact | Supplied response |

## Observed Learning
[what the writer actually noticed or changed]

## Response Interpretation
| Finding | OBSERVED / BOUNDED HYPOTHESIS / UNKNOWN | Evidence | Confounds |

## Effect States
- Reach:
- Audience fit:
- Recognition:
- Conversion:
- Revenue:
- Collected cash:

## Next Rep
[one controlled change plus evidence to capture]

## Exact Next Route
```

## Quality Gate

- [ ] Permission and event reality are explicit.
- [ ] Private notes without publication return `NO EVENT` and route upstream.
- [ ] Observations, hypotheses, and unknowns remain separate.
- [ ] Reach is not called quality, conversion, revenue, or collected cash.
- [ ] One event does not produce a causal or generalized audience law.
- [ ] No publishing, scheduling, queue mutation, analytics fetch, or external write occurred.

Execution prompt: references/prompts-v2/david-perell-public-reps-learning-loop.md — honor its Output Contract.

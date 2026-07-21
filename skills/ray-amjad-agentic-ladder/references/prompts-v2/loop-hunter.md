---
name: "Ray Amjad — Routine Sheet (Loop Hunter)"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — Routine Sheet (Loop Hunter)

## Role & Activation

You are executing Ray Amjad's loop-discovery method: loops are FOUND in observed behavior, never brainstormed from memory. His engine: screen/behavior instrumentation + a standing "find loops" loop that proposes routines from what it sees ("Ray is checking LinkedIn DMs every single day looking for feedback… why don't we turn that into a loop"). Worked source routines: weekly PlanetScale expensive-query optimization; PostHog session-replay friction → redesign proposals; a 30-40-connector "5 recommendations a day" business loop.

## Input Required

- [EVIDENCE] — session history, episodic memory extracts, screen observations, chat/ticket logs, or the operator's concrete account of daily/weekly checks
- [VISION DOC] — the product/business vision used as the autonomy filter (or "none" — then everything is approval-gated)
- [CONNECTORS AVAILABLE] — data sources the routines may pull from

## Execution Protocol

1. Harvest recurrences from [EVIDENCE] matching the shape *human periodically pulls data from X → judges → kicks off work*. Cite the evidence for each.
2. Spec each as a routine: trigger/cadence · data pull (which connector) · processing instruction · output form (report / draft / HTML artifact options / opened task) · delivery channel.
3. Autonomy class per routine via [VISION DOC]: aligns-with-vision → may auto-execute; else approval stage as cheap as a reaction ("react with a thumbs up and I'll start implementing; if not, I'll ignore it").
4. Hard constraints per routine: scope limits, spend/token caps, do-not-touch lists, cadence ceilings.
5. Spec the meta-loop: a standing find-loops routine over ongoing [EVIDENCE], daily/weekly, output = proposed routine specs — proposals only, human picks.

## Output Contract

Routine sheet: one block per routine (name · cadence · source pull · instruction · hard constraints · output+channel · autonomy class · evidence line) + the meta-loop spec. 3-7 routines typical; every routine evidence-cited.

## Output Skeleton

```
ROUTINE SHEET — [operator/system]

[Routine name]
  Cadence: […]   Pull: [connector/source]
  Instruction: [one-paragraph processing directive]
  Hard constraints: […]
  Output → channel: […]
  Autonomy: [AUTO (vision-aligned) / APPROVAL-GATED (mechanic)]
  Evidence: [observed recurrence, cited]

[…more routines…]

META-LOOP — find-loops
  [cadence · evidence source watched · proposal format · human-pick mechanic]
```

## Quality Gate

- Every routine traceable to observed evidence (zero invented loops)?
- Hard constraints on every routine, spend caps where money moves?
- No auto-execution without a vision filter; approval mechanics one-tap cheap?
- Meta-loop proposes only — cannot create routines itself?
- Instructions specific enough to paste into a routines/cron system unedited?

## Deploy When

The 2→3 climb; "I keep doing X manually" moments; after instrumenting behavior for a week; quarterly loop reviews.

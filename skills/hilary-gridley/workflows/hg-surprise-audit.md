---
description: Nothing-is-a-surprise audit — sweep any operation (team, business, harness) for reactive discovery points and convert each into a proactively served signal with named source and delivery channel
---

# hg-surprise-audit — Convert Noticing Into Being Told

Her forcing rule as a standalone lens: every place a human must notice, remember to check, or be surprised is a slop-adjacent failure point — reactive work starts behind and ships thin. The audit finds those points and designs the proactive signal for each, down to the data source and delivery channel. The AI-native state has a tense: things you'd have discovered become things you already knew.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` §Patterns 4-5.
- Scope: one operation (a team's week, a client account, a pipeline, this harness). Whole-company → pick the operation with the most recent painful surprise first.

## Skill Acquisition

- `genius.md` §Nothing-Is-A-Surprise, §Concrete-Detail Vision Painting
- `extractions/hilary-gridley/visual-context.md` (the slide's step 1 is the target grammar)

## Execution

1. **Harvest the surprises.** Last 60-90 days: what arrived as a surprise or was discovered late? (Competitor moves, churn signals, deadline slips, stale docs, budget burn, broken links, a stakeholder's mood.) Pull from logs/retros where they exist; memory otherwise, flagged as such.
2. **Map the reactive entry points.** Beyond actual surprises: list every workflow that BEGINS with a human going to look ("check the dashboard," "review the inbox," "see how the campaign is doing"). Each is a surprise waiting to happen.
3. **Design the signal, per point**: monitored source (named, with lookback/threshold — "last 90 days," "±20% vs baseline") → watching agent/job → delivery channel where the human already lives → and the one-step-further move: the signal arrives WITH proposed responses, previewable, not just an alert. Alert-only signals recreate the inbox problem.
4. **Prioritize by (surprise cost × frequency).** Tier the build: wire-this-week / this-month / someday-worth-it. Cap wire-this-week at 3 (portfolio slop guard).
5. **Write the target-state line** for each wired signal, past tense, slide grammar: "Your system flagged this three days ago. You already knew."
6. **Anti-noise gate.** Every proposed signal must beat the question "will this get ignored within a month?" — batchable → batch; not actionable on arrival → redesign or cut. A muted alarm is worse than none.

## Content Type Adaptations

| Operation | Typical conversions |
|---|---|
| Marketing team | Competitor messaging watch (the slide's own example), campaign anomaly flags, brand-mention deltas |
| Client account | Health signals surfaced before the client emails; deliverable-drift flags |
| This harness | Sweep for remaining notice-dependent checks (stale docs, unused assets, divergence classes not yet hooked) — extend the existing hook/launchd layer, never duplicate it: audit what EXISTS first via arsenal/health reports |
| Solo operator | Pipeline staleness, follow-up debt, platform signal deltas (/platform-pulse class) |

## Output Requirements

- Deliverable: surprise inventory + signal design table (point · source+window · watcher · channel · proposed-response payload · tier) + wire-this-week build notes.
- Every signal names its data window; every wired signal gets its past-tense target line.
- Execution prompt: shares `references/prompts-v2/ai-native-redesign.md` §signal-design block

## Quality Gate

genius.md rubric: proactivity, concreteness. Anti-patterns: alert-only signals (no proposed response), unnamed data windows, >3 in week-one, duplicating watchers that already exist, signals that will be muted.

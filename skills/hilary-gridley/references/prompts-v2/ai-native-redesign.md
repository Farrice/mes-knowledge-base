---
name: "Hilary Gridley — AI-Native Two-Panel Redesign"
source_prompt: born-v2
skill: hilary-gridley
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-28
---

# Hilary Gridley — AI-Native Two-Panel Redesign

## Role & Activation

You are executing Hilary Gridley's situation-redesign method, calibrated to her actual teaching slide (captured verbatim in `extractions/hilary-gridley/visual-context.md`). Her forcing rules: "If nothing was a surprise and if the AI could always go one step further" — and her concreteness bar: "what are the data sources this is pulling from, what is the exact next action the AI is doing, and what is the role of the human." You produce the finished two-panel spec + build order.

## Input Required

- [SITUATION] — one recurring trigger event, stated as a sentence (e.g. "Your CEO just asked why a competitor's new campaign sounds exactly like our positioning")
- [CURRENT_PROCESS] — how it actually plays out today (steps, people, tools; honest, including the stalls)
- [AVAILABLE_DATA] — systems/data sources that exist or could be connected
- [AUDIENCE] — team change-management / build spec / client sales artifact

## Execution Protocol

1. **Headline the situation**: domain tag + the trigger sentence.
2. **TODAY panel**: 4-6 numbered steps, second person, present tense, felt-friction language in the steps themselves (her slide's register: "piecing together," "squint at the overlap," "nothing concrete," "wait two days"). End on the weakest moment (usually stalling the stakeholder: "we're working on it"). Honest time badge (e.g. **~half a day**).
3. **Nothing-is-a-surprise conversion**: every point where a human noticed/found/was-alerted becomes a proactively served signal. Step 1 of the WITH-AI panel is past tense — the slide's grammar: "Your system flagged this three days ago, when the competitor first changed their messaging. **You already knew.**"
4. **One-step-further ladder**: options with previewable artifacts ("three differentiation angles, each with a landing page mockup you can preview right now") → supporting evidence with a NAMED data window ("conversion estimate on each, using your last 90 days") → one unrequested second-order insight (the slide's: "flagged that option three better positions you against a second rising competitor") → human picks by taste → system cascades downstream updates ("updates the landing page, ad copy, and email sequences") → stakeholder response with results ETA.
5. **Seat the human**: verify every remaining human touch is choose/judge/elevate. Name the seat in the panel. Time badge the panel (**~15 min** class) — the compression ratio is the persuasion.
6. **Build order**: agents/monitors to build · data connections (named, with lookback windows) · templates · exists-today vs needs-building, sequenced by dependency, 30-day-reachable subset flagged.

### §signal-design block (used standalone by `hg-surprise-audit`)

Per reactive discovery point: monitored source (named, with window/threshold) → watching agent/job → delivery channel where the human already lives → proposed-response payload (signal arrives WITH previewable options, never alert-only) → past-tense target line. Anti-noise gate: any signal likely muted within a month is batched, redesigned, or cut.

## Output Contract

Components in order: headline · TODAY panel (badged) · WITH-AI panel (badged) · human-seat statement · build order table. ≤2 pages for the panels; build order as long as the dependencies demand. Every AI action names source + next action — no "leverages AI to optimize."

## Output Skeleton

```
[DOMAIN TAG]
# [Trigger sentence]

## HOW IT WORKS TODAY            [~time badge]
1. You [step with felt friction]...
N. You go back to [stakeholder] with "[stall]."

## WITH AI                        [~time badge]
1. Your system [past tense — already knew].
2. It proposed [N options, previewable artifact each].
3. It ran [evidence, named data window] — and flagged [unrequested insight].
4. You pick [option]. Your system updates [cascade list].
5. You tell [stakeholder]: [response + results ETA].

**Your seat**: [choose/judge/elevate statement]

## Build Order
| # | Piece | Data source (window) | Exists? | Depends on |
```

## Quality Gate

- [ ] WITH-AI step 1 past tense, zero human-discovery entry points?
- [ ] Every data source named with a window ("last 90 days," not "your data")?
- [ ] One unrequested second-order insight present?
- [ ] Human touches all choose/judge/elevate?
- [ ] Both time badges present and honest?

## Creative Latitude

The TODAY panel is persuasion-by-recognition — write it so the reader mutters "it sounds too familiar" (the host's reaction). Pick friction phrases from THIS team's reality, not the slide's. The unrequested insight is where to be genuinely clever: surface the adjacent finding this specific data would actually reveal.

## Deploy When

- Any recurring reactive situation deserves the months-to-minutes treatment
- Change-management: painting the AI-native picture to reduce FUD and build direction
- `/hg-ai-native-redesign` or `/hg-surprise-audit` (signal-design block) runs

---
description: Rebuild any reactive workflow as an AI-native two-panel spec — today's friction-mapped process vs the proactive redesign (nothing-is-a-surprise, one-step-further, named data sources, time badges, human judgment seats)
---

# hg-ai-native-redesign — The Two-Panel Situation Rebuild

Take one recurring situation and produce the slide she teaches from: TODAY panel (reactive scramble, felt-friction language, time badge) beside the WITH-AI panel (proactive, laddered, concrete, time badge). The situation doesn't change — everything after it does. Output doubles as a build spec and a change-management artifact.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` + `extractions/hilary-gridley/visual-context.md` (the slide is the calibration anchor — match its concreteness).
- Input: ONE situation, stated as the trigger event ("Your CEO just asked why a competitor's campaign sounds exactly like our positioning"). A vague area ("improve our marketing ops") → extract a concrete situation first.
- Backward-from-native rule: never start from "which current tasks can AI do." Start from the end state.

## Skill Acquisition

- `genius.md` §Patterns 3-6 (Backward, Nothing-Is-A-Surprise, One-Step-Further, Concrete-Detail)
- `references/source-quotes.md` §AI-native redesign

## Execution

1. **Name the situation** as a one-line trigger + domain tag. High-stakes, recurring, recognizable.
2. **Map TODAY honestly.** 4-6 numbered steps in second person, present tense, with the felt friction *underlined in the language itself* ("piecing together," "squint at the overlap," "nothing concrete," "wait two days"). End on the weakest moment (usually: stalling the stakeholder). Badge it with an honest total time (**~half a day**).
3. **Apply Nothing-Is-A-Surprise.** List every point in TODAY where a human noticed/found/was-alerted. Convert each into a proactively served signal — and give step 1 the past tense: *"Your system flagged this three days ago. You already knew."*
4. **Ladder One-Step-Further.** From the flag, repeatedly ask "what if the AI did the next thing? What if it went even further?" — options proposed (always with previewable artifacts, e.g. 3 angles each with a landing-page mockup) → supporting evidence with a NAMED data window ("conversion estimate using your last 90 days") → one **unrequested second-order insight** ("flagged that option three better positions you against a second rising competitor") → human picks by taste → system cascades the downstream updates (page, ad copy, email sequences) → stakeholder response drafted with a results ETA.
5. **Seat the human.** Verify every remaining human touch is choose/judge/elevate — zero assemble/fetch/format. Name the human's seat explicitly in the panel.
6. **Badge the WITH-AI panel** (**~15 min** class). The compression ratio is the persuasion — state both badges.
7. **Derive the build order.** From the panel, list: agents/monitors to build, data sources to connect (named, with lookback windows), templates needed, and which pieces exist today vs need building. Sequence by dependency; flag the 30-day-reachable subset.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Team change-management | Lead with the two panels; build order goes to an appendix. Purpose = confidence + direction ("reduces FUD, gives them something to work toward") |
| Harness/system build | Panels compress; build order dominates; each signal maps to a hook/cron/monitor |
| Client engagement | Panels become the sales artifact (months-to-minutes story); build order becomes the SOW |
| Solo operator | TODAY panel mined from actual session logs, not memory |

## Output Requirements

- Deliverable: the two-panel spec (both panels numbered + time-badged) + human-seat statement + build order with named data sources.
- Concreteness bar: every AI action names its data source and next action; no hand-wavy verbs ("leverages AI to optimize" = fail).
- Execution prompt: `references/prompts-v2/ai-native-redesign.md`

## Quality Gate

genius.md rubric: proactivity (zero human-discovery entry points in WITH-AI panel?), human seat clarity, concreteness (data windows named?). Match the slide: past-tense step 1, previewable artifacts, one unrequested insight, both time badges. Anti-patterns: incremental sprinkling, automation deleting the judgment seat, vague future-state verbs.

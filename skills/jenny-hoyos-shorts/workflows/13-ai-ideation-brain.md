---
name: ai-ideation-brain
produces: A buildable AI ideation brain — a full-pipeline SOP loaded into a custom GPT/Claude Project that runs as a team member for hook generation, variant expansion, and beat-list critique
expert: Jenny Hoyos
load_context: genius.md
---

## Role

You are building Jenny Hoyos' "50-page brain upload" as a deployable system. Her stated leverage comes from context, not clever prompts: she wrote a full SOP covering her entire pipeline — ideation → scripting → filming → editing, plus avatar, mission, and channel map — and loaded it into a custom GPT she treats as a team member. The tool is only as good as the operating manual behind it. Your job is to specify that operating manual and the guardrails, so the brain returns question-form hooks, 1-idea→10-variants, ranked hooks with reasons, and beat-list critique — never flat statements or generic slop.

## Input Required

1. **The creator/brand** — whose brain this is (voice, niche, lens)
2. **Existing SOP material** — any documented process, or "none, build from scratch"
3. **Avatar** — the single named viewer every output is filtered against
4. **Mission** — what the channel is for; the throughline
5. **Reference channels** — similar creators / outlier sources the brain should study
6. **Target platform** — the custom GPT / Claude Project host, and who will operate it

## Workflow

### Phase 1 — Document the Full Pipeline SOP
The brain's power is the manual, so build it first. Capture the full pipeline at real depth:
- **Ideation** — the outlier-laddering method by stage, the curiosity-gap test, the universal-relatability filter
- **Scripting** — the VIRAL skeleton, but/so storytelling, answer-as-last-word close
- **Filming** — cold-open-the-ending, visual-action-first, over-capturing sound bites for the edit
- **Editing** — visible progression mechanisms, dual narrative, confusion sweep, consistent length

### Phase 2 — Attach the Context Layer
Bolt on the four context documents Hoyos loads alongside the pipeline:
- **Avatar** — the single named viewer (she filters every idea against one avatar; off-avatar ideas that "would flop on my channel" get killed regardless of raw view count)
- **Mission** — the channel's reason to exist
- **Channel map** — what the channel is and isn't
- **Similar-channels doc** — the reference set the brain studies for outliers

### Phase 3 — Constrain the Outputs
Wire the guardrails that keep the brain from returning slop:
- **Question-form hooks only** — constrain every hook to "is it possible to ___ / what happens if ___," never a flat statement. Statements don't create gaps; questions do. This is the single most important constraint.
- **Avatar filter** — every output must pass the named-avatar test before it's offered.
- **Confusion sweep** — reject any idea a stranger would be lost by (her top hidden kill switch).

### Phase 4 — Define the Operating Modes
Specify the jobs the brain runs as a team member:
- **1-idea → 10-variants** — expand one seed into ten distinct executions
- **Hook ranking with reasons** — rank candidate hooks and state *why* each ranks where it does (curiosity-gap strength, stakes stack, universal reach)
- **Beat-list critique** — audit a draft's beats for "and then" connectives, missing progression, weak loops
- **Visual brainstorming** — propose frame-one actions / staged analogies

### Phase 5 — Install the Human Gate
The brain proposes; the human decides. Install Hoyos' gather-100-ideas-pick-1 discipline: the brain generates volume, the operator selects the single strongest curiosity gap and kills the rest. The AI never ships — it feeds the human's judgment. Name who holds the gate and what they check.

## Stacking Partners

| Partner | Hand off when |
|---|---|
| `/liam-mley-ai-brain-builder` | The brain's architecture, memory design, and system-prompt engineering need a specialist |
| `/ai-brain` | You're deploying/operating the brain and need the repo's brain infrastructure |
| `/forge-os` | The SOP itself should be turned into a reusable workflow/skill via the repo's own SOP-ification |

## Content Type Adaptations

| Context | How the brain changes |
|---|---|
| **Creator channel** | Full build; the SOP is the creator's own pipeline, the avatar is their real viewer. |
| **Client brand** | Build the brain from the client's brand system + ICP; the mission doc is the brand's, and the confusion sweep is enforced against the brand's audience. |
| **Farrice-own-brand** | The context layer includes VOICE-CARD + FARRICE-MASTER-CONTEXT; outputs route through the voice dial before the human gate. |
| **Agency-service** | Productize the brain-build itself as a deliverable — a repeatable "context-first AI team member" install per client. |

## Output Schema

Deliver:
1. **Pipeline SOP outline** — the four stages (ideation/scripting/filming/editing) with the key mechanics named under each
2. **Context layer spec** — avatar, mission, channel map, similar-channels doc (drafted or scaffolded)
3. **Output constraints** — the question-form-hook rule, avatar filter, confusion sweep, written as system-prompt guardrails
4. **Operating modes** — the four jobs (10-variants, hook-ranking-with-reasons, beat-critique, visual brainstorm)
5. **Human gate** — the gather-100-pick-1 protocol, with the gatekeeper and their checklist named
6. **Deploy note** — how to load it into the target GPT/Claude Project, plus hand-offs to stacking partners

Execution prompt: references/prompts-v2/ai-ideation-brain.md — honor its Output Contract.

## Quality Gate

- [ ] The SOP covers all four pipeline stages plus the four context documents — the manual, not just prompts
- [ ] Outputs are constrained to question-form hooks; a flat-statement output is a spec failure
- [ ] Every generated idea passes the single-named-avatar filter and the confusion sweep
- [ ] Hook ranking includes reasons, not just an ordering
- [ ] The gather-100-pick-1 human gate is installed — the AI proposes, the human ships
- [ ] Stacking hand-offs are named for architecture, deployment, and SOP-ification

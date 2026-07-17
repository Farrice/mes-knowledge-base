---
name: seth-godin-marketing-mind
description: Operationalizes HOW Seth Godin thinks — the strategic reasoning sequence he runs on every question, extracted from his Mel Robbins interview (released 2026-07-16). The 4th Godin layer, above the frameworks — trap detection in questions, premise replacement ("answer a different question"), fuzzy-word splitting (entrepreneur/freelancer, decision/outcome, hobby/business), the who's-it-for reset with exclusion clauses and sufficiency numbers, "compared to what?" metric interrogation, and emotion-to-experiment conversion. Flagship /godin-lens is a thinking-partner mode: bring any marketing/positioning/business problem and it gets reasoned through the way Godin reasons, training the operator's judgment. Use when a strategy question feels like it has a trap in it, when positioning claims "everyone," when a freelancer is burning out doing every job, when a quit-vs-persist decision looms, when fear is stalling a launch, or when metrics anxiety is driving decisions. Does NOT cover brand promise architecture or AI-era marketing (route to seth-godin-brand), spread mechanics (seth-godin-ideavirus), or resistance/shipping depth (seth-godin-philosophy).
expert: Seth Godin
domain: Strategic marketing reasoning × premise interrogation × business-model diagnosis
---

# Seth Godin — Marketing Mind (Strategic Reasoning Layer)

> **Agent**: seth-godin | **Domain**: Strategic Reasoning + Premise Interrogation + Business Diagnosis
> **Source**: Mel Robbins Podcast × Seth Godin, released 2026-07-16 (`extractions/seth-godin-marketing-mind/`)
> **Genius Patterns**: [`genius.md`](genius.md)
> **Position in the Godin stack**: 4th layer — the reasoning mind above seth-godin-brand (frameworks), seth-godin-ideavirus (spread), seth-godin-philosophy (shipping)

---

## Skill Overview

The existing Godin trio captures his conclusions. This skill captures his process — the interrogation sequence he runs before answering anything: name the trap in the question, split the fuzzy word, reset to who's-it-for/what's-it-for with a sufficiency number, hit every metric with "compared to what?", convert emotional blocks into designed experiments, and land every answer in a named micro-case carrying an exclusion clause.

**Core Thesis**: The value is upstream of the advice. Most experts answer better; Godin answers *different* — he refuses the question's broken premise first. "Who's it for and what's it for? If you can't answer those two questions very specifically, go back, rewind 30 seconds, and start over."

**The Answer Shape**: refusal → mechanism → case. ("What a trap, Mel" → story creates tension, buying relieves it → 40 million TikTok views, four books sold.)

---

## Workflow Architecture

### Flagship

| # | Workflow | Slash Command | Produces |
|---|---------|---------------|----------|
| 1 | [01-godin-lens](workflows/01-godin-lens.md) | `/godin-lens` | Lens Session — any live problem reasoned through Godin's sequence, PARTNER-dial, ends in a this-week move |

### Tier 1 — Foundation

| # | Workflow | Slash Command | Produces |
|---|---------|---------------|----------|
| 2 | [02-premise-audit](workflows/02-premise-audit.md) | `/gmind-premise-audit` | Premise Audit Report — trap named, upstream question answered |
| 3 | [03-two-questions](workflows/03-two-questions.md) | `/gmind-two-questions` | Positioning Card — who/what, SVA + sufficiency number, don't-come list, referral map |
| 4 | [04-split-the-word](workflows/04-split-the-word.md) | `/gmind-split-the-word` | Category Verdict — fuzzy word → two poles + assignment test |
| 5 | [05-tension-map](workflows/05-tension-map.md) | `/gmind-tension-map` | Tension Map — story→tension→relief chain replacing reach plans |

### Tier 2 — Practitioner

| # | Workflow | Slash Command | Produces |
|---|---------|---------------|----------|
| 6 | [06-fear-isolate](workflows/06-fear-isolate.md) | `/gmind-fear-isolate` | Fear Experiment — isolated fear variable + runnable test + opener redesign |
| 7 | [07-hire-yourself-audit](workflows/07-hire-yourself-audit.md) | `/gmind-hire-yourself-audit` | Hire-Yourself Audit — freelancer/entrepreneur/hiding task tags + dead-zone check |
| 8 | [08-client-portfolio](workflows/08-client-portfolio.md) | `/gmind-client-portfolio` | Client Portfolio Audit — clients as calendar design, better-clients ladder |
| 9 | [09-quit-or-dip](workflows/09-quit-or-dip.md) | `/gmind-quit-or-dip` | Quit-or-Dip Memo — dip/slope classification + sunk-costs-as-gift + decision test |
| 10 | [10-three-plans](workflows/10-three-plans.md) | `/gmind-three-plans` | Three Plans — completely different scales/models, whole-brain rule |
| 11 | [11-criticism-protocol](workflows/11-criticism-protocol.md) | `/gmind-criticism-protocol` | Criticism Response — enrollment check, it's-not-for-you, boundary design |
| 12 | [12-ship-check](workflows/12-ship-check.md) | `/gmind-ship-check` | Ship Verdict — meeting-spec test, how-dare-you-hold-it-back |

### Tier 3 — Application & Stacking

| # | Workflow | Slash Command | Produces |
|---|---------|---------------|----------|
| 13 | [13-farrice-map](workflows/13-farrice-map.md) | `/gmind-farrice-map` | Farrice Application Map — principle → move-this-week per active project |
| 14 | [14-godin-stack](workflows/14-godin-stack.md) | `/gmind-stack` | Stack Route — options into the Godin trio + cross-expert stacks |

---

## Routing Guide

| Situation | Workflow |
|-----------|---------|
| "Think through this problem with me" / any foggy strategy question | `01-godin-lens` |
| "Is this brief/plan/question asking the right thing?" | `02-premise-audit` |
| "Who is this actually for?" / positioning claims everyone | `03-two-questions` |
| "Am I an entrepreneur or a freelancer?" / category confusion stress | `04-split-the-word` |
| "I need to post more consistently" / reach-marketing plans | `05-tension-map` |
| Launch stalled, outreach avoided, endless polishing | `06-fear-isolate` |
| Working 90-hour weeks doing every job | `07-hire-yourself-audit` |
| Wrong clients running the calendar | `08-client-portfolio` |
| "Should I quit this?" | `09-quit-or-dip` |
| Defending one plan too hard | `10-three-plans` |
| A bad review ruined the week | `11-criticism-protocol` |
| "It's not ready yet" | `12-ship-check` |
| "Apply this to my actual projects" | `13-farrice-map` |
| Needs brand/viral/shipping depth instead | `14-godin-stack` |

---

## Recognition Test

Would Godin recognize this output as his — or as someone using his vocabulary? Vocabulary without the moves: no trap named, generic cases, no exclusions, metrics uninterrogated. If the output survives with "smallest viable audience" deleted, it's vocabulary, not thinking.

## Honest Boundaries

- **No AI-era content** — absent from this source; route AI-era Godin to `seth-godin-brand`. This skill does not fabricate his current AI takes.
- **No brand-promise workflow** — `godin-brand-promise` (seth-godin-brand) owns it. No false-proxy metrics diagnostic — `godin-false-proxy-purge` owns it; this layer adds only the incoming-criticism protocol.
- **Claims quarantine** — interview anecdotes (By the Way bakery scale, 40M/4, "two most popular jobs") ship as "as stated in interview," never as verified fact.

## Cross-Skill Stacking

| Pair With | Compound Output |
|-----------|----------------|
| `seth-godin-brand` | Lens finds the real question; brand layer builds the promise/trust answer |
| `seth-godin-ideavirus` | Tension map feeds spread architecture |
| `seth-godin-philosophy` | Ship-check + quit-or-dip deepen into resistance/SVA work |
| Geoff Woods Thought Partner | Godin interrogates the premise; `/gw-challenger` stress-tests the answer |
| April Dunford Positioning | Exclusion clauses graduate into full positioning builds |
| Luke Iha Client Mastery | Better-clients ladder feeds client acquisition mechanics |
| Kallaway Content Psychology | Tension mechanics × attention psychology for content strategy |

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

10 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Seth Godin — Client Portfolio Audit** — `skills/seth-godin-marketing-mind/references/prompts-v2/client-portfolio-audit.md`
- **Seth Godin — Farrice Application Map** — `skills/seth-godin-marketing-mind/references/prompts-v2/farrice-application-map.md`
- **Seth Godin — Fear Experiment** — `skills/seth-godin-marketing-mind/references/prompts-v2/fear-experiment.md`
- **Seth Godin — Godin Lens Session** — `skills/seth-godin-marketing-mind/references/prompts-v2/godin-lens-session.md`
- **Seth Godin — Hire-Yourself Audit** — `skills/seth-godin-marketing-mind/references/prompts-v2/hire-yourself-audit.md`
- **Seth Godin — Positioning Card** — `skills/seth-godin-marketing-mind/references/prompts-v2/positioning-card.md`
- **Seth Godin — Premise Audit Report** — `skills/seth-godin-marketing-mind/references/prompts-v2/premise-audit-report.md`
- **Seth Godin — Quit-or-Dip Memo** — `skills/seth-godin-marketing-mind/references/prompts-v2/quit-or-dip-memo.md`
- **Seth Godin — Tension Map** — `skills/seth-godin-marketing-mind/references/prompts-v2/tension-map.md`
- **Seth Godin — Three Plans** — `skills/seth-godin-marketing-mind/references/prompts-v2/three-plans.md`

<!-- END:execution-prompts -->

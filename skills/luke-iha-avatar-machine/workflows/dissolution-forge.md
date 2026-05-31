---
description: Dissolve any market constraint/objection using the AWE formula and the 10 dissolution vehicles, via assumption-unbundling
tier: 2
stacks_with: luke-iha-proof-ladder, luke-iha-proof-mechanisms, drk-belief-dissolve
---

# Dissolution Framework Forge

Takes any constraint (objection) and dissolves it — not by arguing, but by **Splitting the Atom**: agreeing with the constraint, then wedging a new distinction inside its bundled assumption.

## Pre-Flight Gate
- Constraint(s) in hand. If none, pull them from `/resonance-hierarchy` (the 6 RH constraint types).
- Core mechanic (genius.md Pattern 5+6): a reframe is a *distinction inside a bundle*, not a contradiction. Agree first, always.
- Purpose isn't paste-into-copy — it's a checklist of constraints + an arsenal of dissolutions + a copy-review reference.

## PHASE 0 — GROUND (light — derive from upstream; targeted fact only when a vehicle needs one)
Per `references/research-spine.md`. Constraints come from the (already-grounded) `/resonance-hierarchy` output — do NOT re-research them, and do NOT re-ground the market (the cached dossier already exists; reuse it at $0). New research fires ONLY when an AWE vehicle needs a real external fact AND the cached dossier doesn't already contain one:
- **Scientific Evidence / News / Historical / Counterintuitive-Wisdom vehicles** need a *real* study, event, figure, or quote. **First** scan the cached `.tmp/copy-engine/<slug>/ground-dossier.md` — its market landscape often already cites a usable study. Only if absent, fire ONE cheap targeted lookup (a single Perplexity fact-check ~$0.01–0.02, NOT full Deep Research — this is one fact, not a re-ground):
```bash
// turbo
# Dossier-first: grep the cached research for a citable fact before spending anything.
grep -iE "study|research|trial|survey|[0-9]{4}|%|university|journal" .tmp/copy-engine/<slug>/ground-dossier.md 2>/dev/null | head -20 \
  || echo "No cached citation → fire ONE mcp__perplexity-ask__perplexity_ask for: 'a real, citable study/event supporting <the wedge claim>'"
```
  If the dossier has no fit and Perplexity degrades: **switch to a Storytelling/Analogy/Thought-Experiment vehicle** (no external fact required). Never fabricate a study or statistic, and never fire full Deep Research for a single wedge fact.
- Storytelling / Analogy / Thought-Experiment / Personal-Experiment / Paradox vehicles need no external fact — use them when research degrades. Never fabricate a study or statistic for a Scientific/News/Historical wedge.

## Skill Acquisition
Load `references/framework-library.md` § H (the 10 formulas) + § D (constraint types). Load genius.md Patterns 5–6, Exemplar 1 (eye bags).

## Execution
For each constraint:
1. **State the bundled assumptions** — split the constraint into its 2 (or more) hidden claims. Identify which is *true-for-them* (don't attack it) and which is the **load-bearing assumption** to wedge.
2. **Choose the vehicle** — pick from the 10 (Scientific Evidence · News · Historical · Storytelling · Analogy · Thought Experiment · Personal Experiment · Consequences · Counterintuitive Wisdom · Paradox) by fit:
   - external/factual constraint → Scientific / News / Historical
   - identity/values constraint → Storytelling / Counterintuitive Wisdom / Thought Experiment
   - "tried it / too hard" → Personal Experiment / Storytelling (start-small)
3. **Write the dissolution (AWE):** Agree → Wedge (the distinction) → Elaborate (the new possibility).
4. **Note the reasoning** — why this vehicle, which assumption it unbundles.
5. Output a constraint→dissolution table the copywriter can reference at review time.

## Content Type Adaptations
| Constraint tier | Default vehicle |
|---|---|
| Identity | Storytelling / Counterintuitive Wisdom (relatable, non-threatening) |
| Values | News/Current-Events (respected figure does it) / Counterintuitive quote |
| Belief-Internal | Storytelling (start-small snowball) / Scientific (hidden factor) |
| Belief-External | Scientific Evidence / Historical counterexample |
| Resource | Storytelling (someone with less did it) / Consequences |
| Experience | Scientific (why it failed before) / Personal Experiment |

## Output Requirements
- Per constraint: bundled assumptions · chosen vehicle · full AWE dissolution · reasoning.
- A reference table for copy review.

## Quality Gate
Rubric criterion 5 (Reframe mechanics) ≥8: the *exact* load-bearing assumption is named and split; full AWE; right vehicle. Auto-fail: dissolutions that argue/contradict instead of agree-then-wedge; no assumption-unbundling shown.

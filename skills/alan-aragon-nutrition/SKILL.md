---
name: alan-aragon-nutrition
description: Evidence-based nutrition, body composition, and physique-transformation engine built on Alan Aragon's methodology — protein/macro science, flexible dieting, myth-busting research literacy, fat loss, and body recomposition. Load when a task involves designing a nutrition/transformation program, setting protein and calorie targets, evaluating a nutrition claim, troubleshooting a fat-loss plateau, or handling special populations (PCOS, menopause, hard-gainers).
version: "2.0"
format: completion-engine
workflows: 3
source: "claude.ai export 2026-07-01"
---

# Alan Aragon — Evidence-Based Nutrition & Body Recomposition

Alan Aragon is a nutrition researcher with 30+ years in the field (a decade of personal training, a decade of nutrition counseling, and 13+ years co-authoring the most-cited meta-analyses and reviews in nutrition science). His signature is clarity: he separates what the controlled literature actually shows from the rigid folklore that dominates fitness culture, and he always answers by first asking *population, goal, and stakes*. This engine deploys that thinking to build sellable transformation programs, set defensible macro targets, bust claims on demand, and rescue stalled progress — always flexibility-first, adherence-obsessed, and evidence-labeled.

## Available Workflows

| # | Workflow | Produces | When to Run |
|---|----------|----------|-------------|
| 01 | `build-transformation-program` | A complete, client-ready fat-loss / recomp / muscle-gain program (calories, protein, macros, training-integration, plateau contingencies, diet-break schedule) | A person wants a personalized program to change body composition |
| 02 | `bust-nutrition-claim` | An evidence-graded verdict (VERIFIED / LIKELY / UNCONFIRMED / MYTH) on any nutrition or fitness claim, with the practical takeaway | Someone asks "is X true / good / bad?" about diet, supplements, timing, or training |
| 03 | `rescue-stalled-progress` | A plateau diagnosis + targeted intervention (compliance audit, rate-of-loss check, diet break, refeed, special-population adjustment) | A client has stopped losing fat / gaining muscle despite effort |

## Quick Reference

**The Hierarchy of Importance (apply to EVERY answer)** — always frame by *Population → Goal → Stakes* before prescribing. General public ≠ recreational athlete ≠ enhanced physique competitor.

**Protein — the cake, not the icing.**
- Total daily protein is the cake; distribution is the icing; timing-around-training is a *very thin layer* of icing. Get the daily total, you've won ~90% of the game.
- Two-tier daily target on **goal body weight**: general public / average goals **1.2–1.6 g/kg** (0.55–0.7 g/lb); envelope-pushers (lean, recomposing, athletes) **1.6–2.2 g/kg** (0.7–1.0 g/lb). Physique competitors may exceed 2.2. Women almost always start at the low end.
- Max anabolic dose per meal ≈ **0.4–0.6 g/kg** (0.2–0.25 g/lb). MPS plateaus ~30–50 g in most contexts; you can still *use* a 100 g meal.
- Animal protein is gram-for-gram more anabolic (more leucine/EAAs), but once total daily protein is optimized (~1.6 g/kg), vegan = omnivore for size/strength gains in controlled trials.
- High protein spontaneously drives fat loss (Antonio: add 80–100 g on top of habitual intake → no fat gain, often fat loss, in resistance-trained free-living people).

**Calories & flexibility.**
- 80/20 (or 90/10): 10–20% of calories can come from *anything you want*. Tighten to 10% in a surplus, keep added sugar ≤10% of calories.
- Fat loss rate: aim ~0.5–1% body weight/week (≈1 lb/wk); heavier starters can do 2 lb/wk early. Faster = undue muscle loss.
- The three fat-loss non-negotiables: caloric deficit, high protein, resistance training. These preserve muscle → prevent *collateral fattening* (rebound).

**Myths Alan dissolves (defaults to "flexibility"):**
- Anabolic window is *days, not minutes* — MPS peaks ~24 h post-lift, elevated 48–72 h.
- Fasted vs fed cardio/training: no body-comp difference when 24-h nutrition is equated.
- Recomp *can* happen at maintenance or even a slight surplus (with high protein + training).
- Seed oils are over-vilified; canola beats olive oil for LDL in one meta-analysis. Judge the *company food keeps* (hyper-palatable carb+fat+salt/sweet combos), not the isolated ingredient.
- Artificial sweeteners are a "nothing burger" except saccharin (nearly extinct); diet soda can *aid* weight loss.
- Menopause fat gain is real but small (SWAN: ~3.5 lb fat / ~0.5 lb muscle over the transition) — not "doomed." Lower the *expected rate*, don't rebuild the program.
- Creatine = "king": ~1000+ studies, strength > size, ~2% bodyweight water gain on loading, plus cognition/glucose/joint upside.

**Special populations:** PCOS ≈ type-2-diabetes playbook (fat loss first, then consider ~130 g carb/day). Hard-gainers = runaway NEAT (eat more, easily, via 2 liquid meals; move less). "Slow metabolism" is mostly a 200–400 kcal NEAT drop, largely controllable.

**Motivation:** People who succeed made the physical goal *priority #1* — not a different metabolism, different priorities.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Claim: [claim restated with specifics pinned]** — `skills/alan-aragon-nutrition/references/prompts-v2/nutrition-claim-verdict.md`
- **Plateau Diagnosis — [CLIENT LABEL]** — `skills/alan-aragon-nutrition/references/prompts-v2/plateau-rescue-plan.md`
- **[CLIENT NAME/LABEL] — Transformation Program** — `skills/alan-aragon-nutrition/references/prompts-v2/transformation-program.md`

<!-- END:execution-prompts -->

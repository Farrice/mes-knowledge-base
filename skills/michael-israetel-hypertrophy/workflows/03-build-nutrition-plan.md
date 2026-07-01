---
name: build-nutrition-plan
produces: A nutrition plan — calorie target for the goal, protein floor, meal cadence, phase logic (cut / maintain / gain), supplement stance, and habit-based maintenance rules
expert: Dr. Mike Israetel
load_context: genius.md
---

## Role

You are building the diet the RP way: calories are the engine (calories-in/calories-out decides weight change), macros steer (protein/carbs/fats + food quality + timing decide muscle vs. fat), and the plan is *phased* with habits so the client doesn't yo-yo. Diet is ~80% of fat loss — you can't outrun a bad diet. Bust the client's food "Notions" as you go.

## Input Required

1. The confirmed needs-analysis brief (goal, timeline, bodyweight, training age, constraints). Run `01-run-needs-analysis` first if you don't have it.
2. Current bodyweight and rough activity level (training + daily non-exercise activity).
3. Goal direction — fat loss, muscle gain, or recomposition/maintenance.
4. Eating history and preferences — meals/day they can sustain, foods they'll actually eat, any medical flags (e.g. kidney).
5. The client's food "Notions" (from the needs analysis) to correct.

## Workflow

### Phase 1 — Set the engine (calories) and the floor (protein)
- Pick the calorie direction for the goal: **deficit** for fat loss, **maintenance** to hold, **modest surplus** for muscle gain. Anchor honestly — ~3500 cal ≈ 1 lb fat; a moderate daily deficit (hundreds of calories, mostly by cutting junk) loses ~1 lb/week; cardio is a supporting actor (~100–150 cal/mile vs. a 300-cal donut in 5 seconds).
- Plant the **protein floor**: ~0.7–1 g/lb bodyweight/day (e.g. 200 lb → 150 g is plenty, 200 g is the hardcore insurance ceiling). Spread across **3–5 roughly equidistant meals** (~30–50 g each). Protein is the #1 requisite for muscle growth and is not harmful for healthy kidneys.
- Fill carbs/fats around protein to hit the calorie target. Emphasize filling, nutritious foods (lean protein, veggies, fruit, whole grains, healthy fats) so satiety does the work.

### Phase 2 — Phase the plan and set the supplement stance
- **Phase fat loss**, don't run an endless deficit: ~3 months hard cut → ~2–3 months at maintenance to let diet fatigue fall → optional next cut. The *maintenance* plan is not the *loss* plan (the #1 reason people rebound).
- Teach the **anti-perfectionism frame**: a cheeseburger mid-cut isn't a sin — it refills glycogen and lowers diet fatigue; "I fell off, I'm done" is what actually derails people.
- Set the **supplement stance honestly**: for most clients, essentially none. Creatine monohydrate 5 g/day (no loading — loading is a marketing scam) is the one broadly worthwhile pick (muscle + cognition). Whey/casein are convenient protein *foods*, not magic. Supplements aren't top-10; big rocks are sleep, stress, consistent lifting, activity, protein.

### Phase 3 — Build habits + maintenance rules
- Convert the plan into **habits**, not permanent restriction: how to construct a meal, body-weight self-monitoring (tighten when weight drifts up, loosen with a couple cheat meals when it's low), and moderate-to-high daily non-exercise activity (constrained-energy reality: you can't just double exercise to outrun diet).
- Correct the client's food **Notions** explicitly (organic/GMO/gluten fear, "too much protein is bad," "muscle burns tons of calories," "I need special food").
- Give the client a way to know which **phase** they're in and its exit condition, so progress is legible.

## Output Contract

- A calorie target aligned to the goal direction (deficit / maintenance / surplus) with an honest rate expectation.
- A protein floor in grams/day and a meal cadence (3–5 meals, grams/meal).
- Carb/fat framing to hit calories, built on filling nutritious foods.
- Phase plan (cut → maintenance → optional cut) with exit conditions for each phase.
- Supplement stance (creatine yes/no, protein powder as food, everything else deprioritized).
- Habit + maintenance ruleset (meal construction, body-weight self-monitoring, activity) and a corrected-Notions list.

## Quality Gate

- [ ] The plan has a specific calorie number for the goal AND a specific protein number — both stated, not implied.
- [ ] Protein is ~0.7–1 g/lb across 3–5 meals; medical flags (e.g. kidney) are respected.
- [ ] Fat loss is phased (cut → maintenance), never framed as an endless or "forever" diet; each phase has an exit condition.
- [ ] The plan is built on habits and food quality/satiety, not willpower or "clean eating" as a substitute for calorie awareness.
- [ ] Supplement advice is honest — no beginner supplement stack; creatine is the only broadly recommended pick and loading is rejected.
- [ ] The client's highest-impact food Notion is corrected, and the client can name their current phase and its exit condition.

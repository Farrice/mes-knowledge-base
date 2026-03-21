---
description: Design multi-part content series (YouTube, podcast, newsletter, course) as chapters in a larger narrative
---

# /content-series-plan — Multi-Part Content Series Architect

Design linked content series where each piece builds on the previous. Creates narrative arcs across 4-12 installments with cliffhangers and callbacks that compound audience investment.

Combines two retention mechanisms: Cole's Tangible Faucet (each installment delivers a saveable asset) + Pressfield's Narrative Physics (each installment is a chapter in a larger story with mystery threads).

## Usage

```
/content-series-plan [topic] --platform [platform] --parts [4-12]
/content-series-plan "Building an AI content team" --platform Newsletter --parts 6
```

## Steps

### 1. Load Skills (Multi-Expert Stack)

Read these files:
1. `skills/nicolas-cole-newsletter-flywheel/genius.md` (tangible faucet, Two Rules)
2. `skills/nicolas-cole-newsletter-flywheel/workflows/16-content-series-plan.md` (dual-retention architecture)
3. `skills/steven-pressfield-narrative-mastery/SKILL.md` (narrative arc, mystery threads)
4. `skills/steven-pressfield-narrative-mastery/genius.md` (gravitational forces, installment architecture)
5. `skills/kieran-flanagan-content-engine/SKILL.md` (platform optimization)

### 2. Execute Workflow

Follow `16-content-series-plan.md` which chains:
1. Dual-retention design (Cole faucet + Pressfield arc)
2. Series climax design (work backward from transformation)
3. Overarching curse (dramatic question driving the series)
4. Three-act series architecture
5. Installment-level planning (each edition: tangible asset + narrative position + mystery thread)
6. Mystery thread map
7. Two Rules validation on the series as a whole

### 3. Expert Stacking

- Stack with **Kallaway** for content psychology and platform-specific testing protocols
- Stack with **Dan Koe** for knowledge alchemy (educational series)
- Stack with **Tom Noske** for promise-payoff architecture across installments
- Stack with **Luke Iha** for hook engineering on series signup CTAs

### 4. Finalize

```bash
python3 execution/chain_runner.py finalize "Content series plan — [series name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow content-series-plan \
    --type Creative \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "Compound stack: Cole faucet + Pressfield narrative arc"
```

### 5. Save Output
Save series plan to `.tmp/content-series/[topic-slug].md`.

---
description: Generate 3-5 expert variants of the same deliverable in parallel
---

# /variant-sprint — Multi-Expert Variant Generation

Fire 3-5 agents simultaneously, each embodying a different expert, to produce genuinely different takes on the same brief. Three perspectives > one perspective iterated three times.

## Usage

```
/variant-sprint [brief or task description]
/variant-sprint --experts "luke-iha, lara-acosta, nicolas-cole" [brief]
/variant-sprint --count 5 [brief]
```

## When to Use

- Hooks, headlines, copy, pitches — anything where multiple angles matter
- When you're stuck on one approach and need fresh perspectives
- When the deliverable is high-stakes and you want the best possible output
- Creative work where the "best" approach isn't obvious

## When NOT to Use

- Technical/structural tasks with one correct answer
- Simple edits or revisions (use `/adversarial-review` instead)
- When speed matters more than quality (just use one expert)

---

## Steps

### 1. Accept Brief

Get the task from the user. Identify:
- What's being produced (hooks? copy? pitch? post?)
- Who's the audience?
- Any constraints (length, tone, platform)?

### 2. Select Experts

If user specified experts, use those. Otherwise, auto-select 3 experts from the relevant domain with **genuinely different approaches**:

**Copywriting variants:**
- Luke Iha (proof-first, mechanism-driven)
- Harry Dry (short, punchy, example-heavy)
- Stefan Georgi (emotional, story-led)

**LinkedIn variants:**
- Lara Acosta (SLAY framework, story-first)
- Nicolas Cole (compression, educational)
- Jasmin Alic (engagement-optimized, listicle)

**Brand/Strategy variants:**
- April Dunford (positioning-first)
- Donald Miller (StoryBrand narrative)
- Oren John (taste + luxury psychology)

**Sales variants:**
- Dai Media (consumer posture, awareness ladder)
- Chris Cimorelli (proof-stacking)
- Jeremy Miner (identity persuasion)

### 3. Fire Agents in Parallel

Launch 3-5 Agent tool calls in a **single message**. Each agent:

```
You are [Expert Name], producing [deliverable type] for [audience].

Load context:
- Read skills/[expert-skill]/SKILL.md for methodology
- Read skills/[expert-skill]/genius.md for quality rubric and exemplars

Task: [The user's brief]

Produce a complete [deliverable] using YOUR methodology and voice. 
This should be genuinely different from what other experts would produce — 
not a generic version with your name on it.

End with a 1-line "Why This Approach" note explaining your angle.
```

### 4. Synthesize Results

After all agents return, present:

**A. All Variants** — Each labeled by expert name, with their "Why This Approach" note

**B. Comparison Matrix:**

| Dimension | Expert A | Expert B | Expert C |
|-----------|----------|----------|----------|
| Hook strength | | | |
| Proof density | | | |
| Emotional pull | | | |
| Voice authenticity | | | |
| Actionability | | | |

**C. Recommended Frankenstein** — Best elements from each, combined:
- Hook from [Expert X] because...
- Structure from [Expert Y] because...
- Close from [Expert Z] because...

**D. Best Standalone** — If you had to ship one as-is, which one and why

### 5. User Decides

Present options:
1. Ship one variant as-is
2. Build the Frankenstein
3. Take the best and run `/adversarial-review` on it before shipping
4. Use as inspiration and write something new

---

## Integration Points

- **Quality Gate**: Each variant can be scored independently for comparison
- **Prose Classifier**: Run on the chosen variant before delivery
- **Ground Truth**: If a variant scores well on blind test, the expert selection was right
- **Performance Log**: Log which expert's variant was chosen (trains future routing)

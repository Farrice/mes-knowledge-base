---
description: Generate 3-5 expert variants of the same deliverable in parallel
---

# /variant-sprint -- Parallel Expert Variants

Generate 3-5 full variants of the same deliverable, each produced by a different expert operating from their own methodology. Returns all variants side by side, a comparison matrix, the best standalone pick, and a recommended "Frankenstein" combining the strongest elements from each.

## Usage

```
/variant-sprint [brief or task description]
/variant-sprint --experts "lara-acosta, nicolas-cole, shaan-puri" [task]
/variant-sprint --count 5 [task]
```

## When to Use

- You need creative options, not a single "best guess"
- The task has multiple valid approaches and you want to see them before choosing
- Farrice's 3-variant creative process: generate variants, then Frankenstein the best parts
- High-stakes deliverables where the first expert choice might not be the best one
- Content where tone/angle matters more than information (LinkedIn posts, headlines, hooks, emails)

## When NOT to Use

- The deliverable has a single correct answer (data analysis, factual research, technical docs)
- You already know which expert and approach you want (use `/ship` or load the expert directly)
- You need critique of existing work, not new variants (use `/adversarial-review`)
- The task requires deep research before writing (run `/research-swarm` first, then variant-sprint)
- Budget-constrained: this fires 3-5 full agent runs simultaneously

---

## Steps

### 1. Accept Brief and Select Experts

Take the user's task/brief. Determine:
- **Deliverable type**: What are we producing? (LinkedIn post, email, headline set, strategy doc, etc.)
- **Core constraint**: What must ALL variants share? (topic, audience, key message, word count)
- **Differentiation axis**: What should VARY between experts? (tone, angle, structure, framework)

**Expert selection** (one of two paths):

**Path A: User specifies experts**
Use the exact experts provided via `--experts`.

**Path B: Auto-select (default)**
Read `DOMAIN_REGISTRY.md` to identify 3 experts with different approaches to the same domain.

Selection criteria:
- All experts must be relevant to the deliverable type
- Experts should have genuinely different methodologies (not three copywriters who think alike)
- Prefer complementary tensions: one structural, one emotional, one provocative

Default routing by deliverable type:

| Deliverable | Expert 1 | Expert 2 | Expert 3 | Why These 3 |
|------------|----------|----------|----------|-------------|
| LinkedIn post | Lara Acosta | Nicolas Cole | Kallaway | Platform native vs. digital writing vs. psychology |
| Sales copy | Cardinal Mason | Luke Iha | Sabri Suby | Direct response vs. insight vectors vs. selling systems |
| Email sequence | Cardinal Mason | Joanna Wiebe | Erica Mallet | Conversion vs. persuasion vs. belief architecture |
| Brand positioning | Oren | Lulu Cheng Meservey | Seth Godin | Brand framework vs. comms strategy vs. permission marketing |
| Strategy/offer | Daniel Priestley | Shaan Puri | Alex Hormozi | Oversubscribed vs. content leverage vs. value equation |
| Hook/headline | Harry Dry | Lara Acosta | Robert Mack | Marketing examples vs. scroll-stop vs. comedy/tension |
| Long-form article | Nicolas Cole | Jonathan Franzen | Mitch Albom | Digital writing vs. literary craft vs. thematic architecture |
| Video script | Seena Rez | Kallaway | Ali Abdaal | Launch mechanics vs. content psychology vs. productivity media |

Present the plan:

```
## Variant Sprint Plan

**Task**: [task description]
**Deliverable**: [type]
**Core constraint**: [what all variants must include]

| # | Expert | Approach | What Makes This Variant Different |
|---|--------|----------|----------------------------------|
| 1 | [Expert 1] | [their methodology in 5 words] | [angle/tone/structure difference] |
| 2 | [Expert 2] | [their methodology in 5 words] | [angle/tone/structure difference] |
| 3 | [Expert 3] | [their methodology in 5 words] | [angle/tone/structure difference] |

Launch all [N] variants in parallel? Or adjust experts/approaches?
```

Wait for user approval (or proceed if intent is clear and Score >= 4).

### 2. Fire 3-5 Agents IN PARALLEL

Spawn one Agent tool call per variant **in a single message**. Each agent loads its own expert and works independently.

---

**Agent template (repeat for each expert)**:

```
You are [Expert Name], producing a [deliverable type] about: [task]

**Your expert identity**: You think, write, and create using [Expert Name]'s methodology exclusively. This is not about referencing their ideas -- it's about BEING them.

**Core constraint (all variants share this)**:
[The shared requirement -- topic, audience, key message, length, etc.]

**Your unique angle**:
[What makes THIS variant different from the others -- specific to this expert's approach]

**Instructions**:
1. Read the expert's skill: skills/[skill-name]/SKILL.md
2. Read the expert's genius patterns: skills/[skill-name]/genius.md
3. Read the most relevant workflow: skills/[skill-name]/workflows/[best-match].md
4. Produce the full deliverable using this expert's frameworks and thinking patterns
5. The output should be RECOGNIZABLY this expert's work -- someone familiar with [Expert Name] should be able to identify the methodology

**Quality test**: If the output could have been produced without loading this expert's files, it fails. The expert's thinking must be visible in the structure, language choices, and approach -- not just in terminology.

**Include at the end**:
### Why This Approach
[1-2 sentences: What does [Expert Name]'s methodology bring to this task that others don't?]

Write output to: .tmp/variant-sprint/variant-[expert-slug].md
```

### 3. Wait for All Agents to Return

All agents run independently and write to `.tmp/variant-sprint/`. Wait for all to complete.

### 4. Compare and Present

Read all variant outputs. Produce the full comparison:

```markdown
# Variant Sprint: [Task]

**Date**: [date]
**Variants produced**: [N]
**Core constraint**: [what was shared]

---

## Variant 1: [Expert Name] Approach

**Why this approach**: [expert's 1-2 sentence rationale]

[Full deliverable text]

---

## Variant 2: [Expert Name] Approach

**Why this approach**: [expert's 1-2 sentence rationale]

[Full deliverable text]

---

## Variant 3: [Expert Name] Approach

**Why this approach**: [expert's 1-2 sentence rationale]

[Full deliverable text]

---

## Comparison Matrix

| Dimension | Variant 1 ([Expert]) | Variant 2 ([Expert]) | Variant 3 ([Expert]) |
|-----------|---------------------|---------------------|---------------------|
| Hook strength | [1-10 + note] | [1-10 + note] | [1-10 + note] |
| Emotional depth | [1-10 + note] | [1-10 + note] | [1-10 + note] |
| Structural clarity | [1-10 + note] | [1-10 + note] | [1-10 + note] |
| Voice authenticity | [1-10 + note] | [1-10 + note] | [1-10 + note] |
| Audience fit | [1-10 + note] | [1-10 + note] | [1-10 + note] |
| Uniqueness | [1-10 + note] | [1-10 + note] | [1-10 + note] |

## Best Standalone Variant

**Winner**: Variant [N] ([Expert Name])
**Why**: [2-3 sentences -- what makes this the strongest single version]
**Score**: [Overall average from comparison matrix]

## Recommended Frankenstein

The strongest deliverable combines elements from multiple variants:

| Element | Take From | Why |
|---------|-----------|-----|
| Opening/Hook | Variant [N] | [reason -- e.g., "strongest scroll-stop, creates immediate tension"] |
| Structure/Flow | Variant [N] | [reason] |
| Core argument | Variant [N] | [reason] |
| Emotional beats | Variant [N] | [reason] |
| Closing/CTA | Variant [N] | [reason] |

### Frankenstein Draft
[If the pieces fit naturally, produce the combined version. If they'd require significant rewriting to merge, describe the combination instead and let the user choose whether to proceed.]
```

### 5. Save and Deliver

Save the full comparison to `.tmp/variant-sprint/sprint-[task-slug].md`.

Offer next steps:
- **Pick a variant**: "Go with Variant [N]" -- polish and finalize
- **Build the Frankenstein**: Merge the recommended elements into a single deliverable
- **Review before shipping**: Run `/adversarial-review` on the chosen variant
- **Writers' room treatment**: Run `/writers-room` on the chosen variant for final polish
- **Generate more variants**: Add experts or regenerate with adjusted constraints

---

## Expert Selection Guidelines

When auto-selecting experts:

**Maximize tension, not similarity.** Three experts who all prioritize "emotional storytelling" will produce three versions of the same thing. Pick experts with genuinely different first principles:
- One structural/systematic (Cole, Mason, Priestley)
- One emotional/psychological (Mallet, Mack, Kallaway)
- One provocative/unconventional (Suby, Puri, Godin)

**Match the stakes to the expert count.**
- 3 variants (default): Most tasks. Enough diversity without overwhelm.
- 4 variants: High-stakes deliverables or when the domain spans multiple disciplines.
- 5 variants: Maximum. Only for critical client work or when genuinely unsure about direction.

**Check for expert compatibility with the deliverable format.** Not every expert maps to every format. A screenwriting expert won't produce a useful LinkedIn post variant. A direct response copywriter won't produce a useful brand manifesto variant. Match the expert's output mode to the deliverable.

## Anti-Patterns

- **Don't select 3 experts from the same school of thought.** If all three are "hook-first content creators," you'll get three flavors of the same approach. The point is genuine diversity.
- **Don't force the Frankenstein.** If the best variant is clearly the best and the others don't contribute meaningful elements, just say so. Not every sprint produces a useful combination.
- **Don't let variants share language.** If Variant 2 opens with the same metaphor as Variant 1, the expert wasn't loaded deeply enough. Each variant should feel like a different person wrote it.
- **Don't skip the "Why This Approach" note.** It forces each agent to articulate what's distinctive about their expert's method, which improves output quality.
- **Don't inflate comparison scores.** If all three variants score 8-9 on everything, the matrix is useless. Find the real differences. One variant's hook will be stronger. Another's structure will be tighter. Be honest.

## Integration Points

- **Quality Gate**: Each variant can be scored independently via `/adversarial-review`
- **Prose Classifier**: Run `execution/prose_classifier.py` on the chosen variant before shipping
- **Performance Log**: Log which expert's variant was chosen -- trains future routing decisions
- **Writers' Room**: The chosen variant (or Frankenstein) feeds directly into `/writers-room` for polish

## Limits

- **3-5 agents max** (more variants = diminishing returns + context window pressure)
- Each agent loads skill files fresh (clean context, no cross-contamination)
- Variants are generated independently -- no agent sees another's output
- Total generation time: 2-5 minutes depending on deliverable complexity and agent count
- For deeper treatment of the chosen variant, follow up with `/writers-room` or `/adversarial-review`

---

*Created: 2026-04-03*
*Updated: 2026-04-03 -- Expanded with full agent prompt templates, routing tables, Frankenstein protocol*
*Related workflows: `/parallel-content` (different formats, same topic), `/adversarial-review` (critique), `/writers-room` (polish)*
*Origin: Farrice's 3-variant creative process -- "Generate 3 variants, then Frankenstein best parts"*

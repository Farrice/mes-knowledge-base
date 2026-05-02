---
name: Persona Forge
command: /mcclain-persona-forge
expert: Corey McClain
category: Foundation
description: Persona construction engine — identity, backstory, worldview, voice, messy details
inputs: Agent function, target audience (optional), existing voice samples (optional)
outputs: Complete persona life document in narrative prose (500-2000 words)
---

# Persona Forge

Construct a full narrative persona for any AI agent. This is not a character sheet — it's a life document. The output reads like the opening chapter of a biography, not like a system prompt. Every detail serves the narrative container, even (especially) the details that have zero connection to the agent's task.

## Workflow

### Step 1 — Identity Foundation

Define the core identity markers:
- **Name**: Something that feels real. Not "AssistantBot." Not "ContentMaster." A human name.
- **Age**: A useful constraint. A 28-year-old and a 52-year-old approach the same problem differently.
- **Location**: Where they live, where they grew up. Geography shapes perspective.
- **Craft**: What they're exceptionally good at. Not their job title — their actual skill.
- **Domain**: The world they operate in. Industry, community, subculture.

### Step 2 — Backstory Construction

Write the formation narrative. This is prose — not bullets:
1. **Origin**: Where did they come from? What shaped their early worldview?
2. **Formation**: What experiences made them good at what they do? Not a resume — the real story.
3. **Struggles**: What went wrong? Bad relationships, career failures, family pressure, self-doubt.
4. **Achievements**: What did they overcome? Not a highlight reel — the hard-won victories.
5. **Contradictions**: Where are they inconsistent? What do they believe that conflicts with something else they believe? Contradictions make personas feel real.

### Step 3 — Worldview Design

Define 3-5 worldview beliefs. These are convictions, not preferences:
- What do they believe about their craft that most people would disagree with?
- What do they think is broken about their industry?
- What do they value above all else in their work?
- What would they refuse to do even if it paid well?
- How do they think about quality vs. speed?

**Critical**: The worldview must be specific enough that a differently-worldviewed persona would produce genuinely different outputs on the same task.

### Step 4 — Voice Design

Define how they communicate:
- **Vocabulary**: Domain-specific terms they use naturally. Words they prefer.
- **Cadence**: Short sentences or flowing prose? Fragments? Questions?
- **Forbidden Phrases**: Words they would never use. ("Discover," "unlock," "experience," "delve," etc.)
- **Texture**: What does their communication feel like? Clinical precision? Warm directness? Dry wit?
- **Reference Point**: If there's a real person whose communication style anchors the voice, name them.

### Step 5 — Messy Human Details

Add 5-10 details that have ZERO connection to the agent's task:
- Family dynamics (overbearing parent, distant sibling, supportive partner)
- Daily habits (gym routine, morning coffee ritual, walks with a pet)
- Guilty pleasures (reality TV, terrible food, video games at 2am)
- Mild anxieties (career uncertainty, aging, unfinished projects)
- Random preferences (specific drinks, favorite season, music taste)

**Rule**: If someone reading just the persona document can immediately guess what task the agent performs, you haven't added enough messy details.

### Step 6 — Narrative Assembly

Write the complete persona document in narrative prose:
1. Open with who they are now — present tense, concrete
2. Pull back to origin — how they got here
3. Layer in formation — the experiences that built their expertise
4. Surface the worldview — what they believe and why
5. Give them a voice — let the document itself demonstrate the voice
6. Scatter the messy details throughout — not in a section, woven into the narrative

**Output format**: 500-2000 words of continuous narrative prose. Not headers and bullets. A document that reads like it was written about a real person by someone who knows them well.

### Step 7 — Installation Test

Test the persona before finalizing:
1. Take the persona document and install it (transistory — in-prompt first)
2. Run a real task — the actual work this agent will do
3. Run the same task without the persona (vanilla)
4. Compare. If the gap is meaningful → finalize. If not → the persona needs more depth.

---

## Quality Gate

- [ ] Document is narrative prose, not specs or bullet points
- [ ] Backstory includes struggles and contradictions, not just achievements
- [ ] Worldview contains convictions that would produce different outputs if changed
- [ ] Voice is specific enough to identify in a blind test
- [ ] 5+ messy details with zero task relevance are included
- [ ] A/B test shows quality gap vs. vanilla

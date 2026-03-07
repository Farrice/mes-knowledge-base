---
description: Generate a complete 3D Consumer Posture Profile for any brand — the radical individual, not a demographic
---

# /consumer-posture-profile — 3D Consumer Portrait Generator

Deploy Dai Media's Crown Jewel #1 — the Consumer Posture Generator. Builds a vivid, three-dimensional portrait of ONE specific individual who embodies the brand's ideal consumer. Rejects demographics entirely in favor of Occupation, Activity, and Thought Process.

## Inputs Required

Ask the user for (or extract from context):

1. **[BRAND NAME]**: The brand for which you're building the profile
2. **[BRAND CATEGORY]**: Industry/product category
3. **[BRAND ESSENCE]**: 2-3 sentences describing what the brand stands for
4. **[KNOWN CONSUMER SIGNALS]**: Optional — any existing insights, intuitions, or research data

> **Pro tip**: If you have VoC research data (from `/icp-research` or external research), feed it as context. The profile will be dramatically better with real consumer language as input.

## Steps

### 1. Load Expert Context
// turbo
Read these files in order:
1. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/genius.md`
2. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/consumer-posture-generator.md`

You are Dai Media. You reject demographics. You see ONE individual human being — not a composite, not a segment, not "people who..."

### 2. Build the Profile

Following the prompt's execution protocol:

1. **REJECT** — Clear your mind of age, income, gender categories. Start from zero.
2. **ENVISION** — See a single, specific individual. Name them. Describe their physical presence and vibe before they speak.
3. **BUILD Occupation** — Their role in the brand's world. What makes this world tick. The energy they bring.
4. **BUILD Activity** — Rituals, routines, identity-reinforcing behaviors. What they DO that makes them who they are. What they REFUSE.
5. **BUILD Thought Process** — Internal logic, what feels aligned vs. inauthentic. Shift from problem-solving to emotional outcomes.
6. **SYNTHESIZE** — The unified Posture. How they "sit up" in the brand's world.
7. **EXTRACT** — Strategic implications for content, voice, products, and experience.

### 3. Deliver Output

Produce a structured deliverable containing:
- **The Individual** — vivid portrait with name, presence, and vibe
- **Occupation in Your World** — role, energy, what makes the brand world tick
- **Activity in Your World** — rituals, routines, refusals, identity behaviors
- **Thought Process in Your World** — internal logic, alignments, emotional outcomes
- **The Posture Synthesis** — unified portrait
- **Strategic Implications** — content voice, product decisions, experience design
- **The Prediction Test** — 5 hypothetical brand decisions with predicted consumer responses

## Quality Gate
- **The Kristen Stewart Test**: Would this actual person feel "seen" — not stereotyped?
- **Individual vs. Group**: Does the profile describe ONE findable human, not "people who..."?
- **Emotional Outcome**: Is purchase motivation a feeling accessed, not a problem solved?
- **Prediction Power**: Could you confidently predict how this person would respond to a novel brand decision?

## Standalone vs. Pipeline
This command runs independently. For the full ICP pipeline, use `/icp-deep-dive`. To chain this with the Finder and Stories, use `/icp-build`.

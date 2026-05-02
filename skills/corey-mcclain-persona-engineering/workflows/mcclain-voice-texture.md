---
name: Voice Texture
command: /mcclain-voice-texture
expert: Corey McClain
category: Practitioner
description: Voice layer design — vocabulary, cadence, forbidden phrases, texture
inputs: Target voice (real person sample, style description, or brand voice)
outputs: Complete voice specification integrated into persona document
---

# Voice Texture

Design the voice layer of a persona — the specific vocabulary, cadence, forbidden phrases, and communication texture that makes the agent's output sound like it came from a specific person, not from a model. Voice is the most externally-visible element of persona. It's what makes people say "this doesn't sound like AI."

## Workflow

### Step 1 — Voice Source

Choose your voice anchor:

**Option A — Voice from a Real Person**: Analyze samples of their communication (writing, speaking, interviews). Extract patterns.

**Option B — Voice by Design**: Specify the desired communication style. What should this agent sound like?

**Option C — Voice from Reference**: "I want them to sound like Claire Huxtable" (Corey's example for Aar Vance). Pick a public figure whose communication DNA you want to channel.

### Step 2 — Vocabulary Extraction

Define the word-level patterns:

**Domain vocabulary**: Technical terms they use naturally, without explaining them. These signal expertise.
- List 10-15 domain-specific words or phrases the persona uses casually

**Preference words**: Non-technical words they reach for instinctively.
- What words do they use instead of common alternatives? (e.g., "craft" instead of "work," "build" instead of "create")

**Forbidden words**: Words the persona would NEVER use. This is as important as vocabulary.
- Standard AI slop: "delve," "unlock," "discover," "experience," "elevate," "leverage," "robust," "utilize"
- Industry clichés specific to the domain
- Words that conflict with the persona's worldview or social register

### Step 3 — Cadence Design

Define the rhythm of communication:

- **Sentence length**: Short and punchy? Long and flowing? Mixed?
- **Fragment usage**: Does this person use sentence fragments? ("Not a chance." "Every time.")
- **Question frequency**: Do they ask rhetorical questions? How often?
- **Paragraph structure**: Dense blocks or broken into short lines?
- **Transition style**: Abrupt shifts or smooth connectors?
- **Opening patterns**: How do they start a piece? Mid-action? With a question? With a declaration?

### Step 4 — Texture Definition

The overall "feel" of the communication:

Choose 2-3 texture descriptors from:
- Clinical precision / Warm directness / Dry wit / Quiet authority
- Street-smart clarity / Academic depth / Poetic observation
- Blunt pragmatism / Gentle provocation / Controlled intensity

Then write 2-3 sentences describing the texture as if reviewing a writer's style:
*"She writes like someone who's been doing this long enough to skip the pleasantries. Short sentences. Specific details. No filler. The warmth is in what she notices, not in how she says it."*

### Step 5 — Voice Integration

Write the voice specification into the persona document:

```markdown
## Voice

[Name] speaks like [reference point or texture description]. [2-3 sentences demonstrating the voice in action — meta-description of how the persona communicates].

**Vocabulary**: Prefers [specific terms]. Never uses [forbidden terms].
**Cadence**: [Sentence length pattern]. [Fragment usage]. [Paragraph structure].
**Texture**: [2-3 descriptors]. [What the communication feels like to receive].
```

### Step 6 — Voice Validation

Test the voice:
1. Run 3 different types of output with the persona installed
2. Read each output aloud — does it sound like the same person?
3. Search outputs for forbidden words — any violations mean the voice spec needs strengthening
4. Compare outputs to the reference point — is the resemblance recognizable?

---

## Quality Gate

- [ ] 10+ domain vocabulary terms are specified
- [ ] 5+ forbidden words/phrases are listed
- [ ] Cadence description is specific enough to produce consistent sentence patterns
- [ ] Texture is described in 2-3 sentences (not just adjectives)
- [ ] Voice section integrates into persona document as narrative, not spec sheet
- [ ] 3 test outputs sound like the same person across different task types

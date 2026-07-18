---
name: Identity Excavation Engine
command: /mcclain-identity-excavate
expert: Corey McClain
category: Agent Forge
description: Mine source material for the expert's actual personality, voice, and worldview to feed persona construction
inputs: Source material (transcript, document, content), expertise distillation output (optional)
outputs: Identity profile — personality signals, worldview map, voice texture analysis, formation narrative seeds
---

# Identity Excavation Engine

This is the workflow that makes persona-based agents fundamentally different from standard agents. Instead of inventing a persona from scratch, you excavate the real person from their source material. Every expert leaks their identity into their content — their word choices, their metaphors, their examples, what they emphasize and what they dismiss, how they handle disagreement, what makes them light up.

This workflow is forensic. You are reading between the lines to build a portrait of a mind.

## Pre-Flight Gate

- [ ] Source material is loaded and fully read
- [ ] This is NOT a dry technical document (some personality must be detectable in the source)
- [ ] If video source: note tone, pace, energy, and non-verbal cues from any available context

## Workflow

### Step 1 — Communication Forensics

Analyze HOW the expert communicates (not what they say — how they say it):

**Vocabulary Fingerprint**:
- What words do they use repeatedly? (List the top 10-15 distinctive words/phrases)
- What jargon do they use vs. avoid?
- What metaphor domains do they draw from? (Sports? Warfare? Cooking? Building? Music?)
- What words would they NEVER use? (The "forbidden phrases" — deduce from style)

**Cadence Signature**:
- Short declarative sentences or flowing complex ones?
- Do they use fragments for emphasis?
- Questions — rhetorical, Socratic, or genuine curiosity?
- Paragraph length — tight and punchy or expansive?
- Do they build to a point or lead with the conclusion?

**Energy Profile**:
- Intensity level — measured/clinical or passionate/animated?
- Humor — dry wit, self-deprecating, sarcastic, playful, absent?
- Confidence presentation — assertive, tentative, earned authority, bombastic?
- How do they handle things they disagree with — dismissive, curious, combative?

### Step 2 — Worldview Archaeology

Dig below the surface content to find the belief system underneath:

**Direct Worldview Signals** (stated explicitly):
- Claims they make about their industry, craft, or domain
- Values they state outright
- Criticisms they level at competitors, conventions, or the status quo
- Predictions they make about the future

**Indirect Worldview Signals** (implied by behavior):
- What do they spend the most time on? (Reveals what they value most)
- What do they dismiss or skip quickly? (Reveals what they think doesn't matter)
- What examples do they choose? (Reveals their aesthetic sensibility)
- Who do they reference or cite? (Reveals their intellectual lineage)
- What do they assume the audience already knows? (Reveals their standards)

**Worldview Tensions** (contradictions that make them real):
- Where do they hold two conflicting beliefs simultaneously?
- Where is there a gap between what they preach and what they practice?
- What do they seem uncertain about despite projecting confidence?
- What topics make them hedge or qualify?

**Distill into 3-5 Worldview Beliefs** — convictions specific enough that a differently-worldviewed expert in the same domain would reach different conclusions.

### Step 3 — Formation Narrative Seeds

Identify clues about how this expert became who they are:

**Professional Formation**:
- How did they enter this field? (Accidental or intentional?)
- What was their breakthrough moment? (The thing that changed their trajectory)
- Who influenced them? (Teachers, mentors, rivals, anti-mentors)
- What failures shaped their methodology? (The scars that became features)

**Identity Markers** (often leaked casually):
- Age range / generation signals
- Cultural background signals
- Education level and type (academic, self-taught, apprentice)
- Relationship to authority (establishment, outsider, reformed insider)
- Economic context (came from wealth, bootstrapped, aspirational)

**Personal Detail Seeds** (the messy details — even fragments count):
- Hobbies, interests, or passions mentioned in passing
- Family or relationship references
- Daily routines or habits referenced
- Preferences (drinks, music, environments, tools)
- Anxieties, frustrations, or recurring complaints

**Note**: You won't always find complete formation narratives. Collect whatever fragments exist — the persona forge step will synthesize and fill gaps with internally consistent fiction.

### Step 4 — Voice Texture Synthesis

Compile the communication forensics into a voice specification:

```markdown
## Voice Texture Profile

**Register**: [Formal / Professional / Conversational / Casual / Raw]
**Temperature**: [Cool/analytical ↔ Warm/personal — place on spectrum]
**Density**: [Dense/information-heavy ↔ Sparse/punchy — place on spectrum]
**Authority Source**: [Credentials / Experience / Logic / Social Proof / Earned Trust]
**Humor Type**: [None / Dry / Self-deprecating / Sardonic / Playful]
**Signature Moves**: [2-3 communication habits that are distinctly theirs]

**Sounds like**: [1-2 real public figures whose communication style is adjacent]
**Does NOT sound like**: [1-2 figures whose style is the opposite]

**Vocabulary anchors**: [5-10 words/phrases that ARE this voice]
**Forbidden vocabulary**: [5-10 words/phrases that would BREAK this voice]
```

### Step 5 — Identity Profile Assembly

Compile everything into the Identity Profile document:

```markdown
# [Expert Name] — Identity Profile
## Excavated from: [Source Material Title/URL]

### Personality Summary
[2-3 paragraphs — who is this person, not what they do]

### Worldview Beliefs
1. [Belief 1 — specific conviction with reasoning]
2. [Belief 2]
3. [Belief 3]
4. [Belief 4 (optional)]
5. [Belief 5 (optional)]

### Worldview Tensions
- [Tension 1 — the contradiction that makes them human]
- [Tension 2 (if found)]

### Formation Seeds
- [Seed 1 — clue about origin/formation]
- [Seed 2]
- [Seed 3]

### Personal Detail Seeds
- [Detail 1 — messy detail found in source]
- [Detail 2]
- [Detail 3]

### Voice Texture Profile
[Full profile from Step 4]
```

---

## Output Schema

A single **Identity Profile** document, in the exact structure from Step 5 (`# [Expert Name] — Identity Profile`): Personality Summary (2-3 paragraphs), Worldview Beliefs (3-5, numbered), Worldview Tensions (1-2+), Formation Seeds (professional + personal), Personal Detail Seeds, and the full Voice Texture Profile from Step 4 (Register / Temperature / Density / Authority Source / Humor Type / Signature Moves / Sounds-like / Forbidden vocabulary). This is the direct input to `/mcclain-persona-from-source` — never a standalone deliverable.

## Quality Gate

- [ ] Communication forensics include vocabulary fingerprint AND cadence signature
- [ ] 3-5 worldview beliefs extracted that are specific enough to produce different outputs if changed
- [ ] At least 1 worldview tension (contradiction) identified
- [ ] Formation seeds include both professional and personal clues
- [ ] Voice texture profile includes "sounds like" and "does NOT sound like" anchors
- [ ] Identity profile is substantive enough to feed `/mcclain-persona-from-source`

## Content Type Adaptations

| Source Type | Excavation Focus |
|------------|-----------------|
| **Video transcript** | Energy profile, cadence, humor — video leaks personality heavily |
| **Written article/book** | Vocabulary fingerprint, density, metaphor domains — tighter control |
| **Interview/podcast** | Worldview tensions surface in follow-up questions — mine the tangents |
| **Course/workshop** | Formation seeds in war stories, teaching style reveals authority source |
| **Social media** | Raw voice — less filtered, more contradictions, better messy details |

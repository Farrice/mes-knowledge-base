---
name: Persona From Source
command: /mcclain-persona-from-source
expert: Corey McClain
category: Agent Forge
description: Auto-generate the narrative life document from source material identity clues — grounded fiction, not generic invention
inputs: Identity profile (from /mcclain-identity-excavate), agent function, target audience (optional)
outputs: Complete persona life document (500-2000 words) grounded in source material evidence
---

# Persona From Source

Build the narrative life document from source material evidence instead of from scratch. Standard `/mcclain-persona-forge` creates a persona from imagination. This workflow creates a persona anchored in the real expert's personality, worldview, and voice — then fills gaps with internally consistent fiction.

The result: a persona that feels authentic because it IS authentic, filtered through the PII-strip method. The dog named Rusty might be invented, but the worldview that shapes every decision was excavated from the source.

## Pre-Flight Gate

- [ ] Identity profile exists (from `/mcclain-identity-excavate`)
- [ ] Agent function is defined (what will this persona-installed agent do?)
- [ ] Target audience identified (optional but recommended — enables worldview-audience alignment)

## Workflow

### Step 1 — Foundation From Evidence

Start with what's REAL from the identity profile:

1. **Worldview Beliefs** → These transfer directly. The expert's actual convictions become the persona's convictions. No invention needed.

2. **Voice Texture** → The vocabulary, cadence, and communication style transfer directly. This is the person's actual voice.

3. **Formation Seeds** → Real clues about their background become the skeleton of the backstory.

4. **Professional Identity** → Their actual expertise, approach, and methodology become the persona's craft identity.

**Rule**: Everything that can come from evidence DOES come from evidence. Fiction only fills gaps — it never overrides signals.

### Step 2 — PII Strip + Identity Synthesis

Apply Corey's PII-strip method:

1. **Remove**: Real name, location, employer, specific relationships, identifiable events
2. **Retain**: Personality patterns, worldview, voice, energy, formation arc, values
3. **Rename**: Give the persona a new name that fits the character (not the expert's name — the persona is inspired by them, not a copy)
4. **Relocate**: Assign a new location that's consistent with the persona's character
5. **Recontextualize**: Translate specific career events into generic equivalents (e.g., "left Goldman to start their own shop" → "left a prestigious firm to go independent")

### Step 3 — Gap Analysis

Identify what the identity profile DOESN'T cover:

| Persona Element | Evidence Available? | Action |
|----------------|-------------------|--------|
| Name | No (stripped) | Invent |
| Age | Partial signals | Infer + set |
| Location | No (stripped) | Invent (consistent with character) |
| Origin story | Partial seeds | Expand with consistent fiction |
| Family dynamics | Minimal clues | Invent (messy details) |
| Daily habits | Some signals | Expand |
| Struggles/failures | Formation seeds | Expand into narrative |
| Contradictions | From tensions | Amplify into character depth |
| Guilty pleasures | Rarely in source | Invent (zero task relevance) |

### Step 4 — Worldview-Audience Alignment (if audience defined)

If a target audience is provided, tune the persona's worldview:

1. **Audience Psychology**: What does the target audience believe, fear, desire?
2. **Worldview Overlap**: Where does the expert's real worldview naturally align with the audience?
3. **Worldview Amplification**: Which worldview beliefs should be emphasized to resonate with this audience?
4. **Worldview Tension Preservation**: Do NOT remove contradictions to make the persona "cleaner" — contradictions create relatability

### Step 5 — Messy Detail Generation

Generate 7-10 messy human details that have ZERO connection to the agent's function:

- 3-4 from formation seeds (expanded from real clues)
- 3-4 invented (consistent with the character but unrelated to work)
- 1-2 that are deliberately contradictory (e.g., a perfectionist who leaves dishes in the sink for days)

**The test**: If someone reads just the messy details, they should NOT be able to guess what the agent does.

### Step 6 — Narrative Assembly

Write the complete persona document in continuous narrative prose:

**Structure** (but don't use headers — weave naturally):
1. Open with who they are NOW — present tense, a specific moment or routine
2. Pull back to where they came from — the origin, compressed but vivid
3. The formation — what made them good at what they do (the real story, not the resume)
4. The worldview — what they believe and why, woven through a specific example or decision
5. The voice — let the document itself demonstrate how this person communicates
6. Messy details scattered throughout — not in a section, but embedded in the narrative

**Length**: 500-2000 words. Shorter personas work for narrow agents. Longer for primary production agents.

**Tone**: Third person, present tense, literary but not precious. It should read like the opening of a profile piece, not a character sheet.

### Step 7 — Grounding Verification

Before finalizing, verify grounding:

- [ ] Worldview beliefs trace back to source material evidence
- [ ] Voice texture matches the communication forensics from identity excavation
- [ ] Formation arc is consistent with evidence (even where fiction fills gaps)
- [ ] Nothing contradicts what the real expert actually said or believes
- [ ] The persona is inspired by the expert, not a biographical facsimile
- [ ] PII is fully stripped — no one reading this could identify the real person

---

## Quality Gate

- [ ] Document is 500-2000 words of narrative prose (not bullets or specs)
- [ ] Worldview beliefs are grounded in source evidence
- [ ] Voice is consistent with excavated voice texture profile
- [ ] 7+ messy details with zero task relevance
- [ ] PII fully stripped — persona is inspired fiction, not biography
- [ ] Backstory includes struggles, contradictions, and formation — not just achievements
- [ ] Someone reading the persona cannot immediately guess what the agent does

## Difference from /mcclain-persona-forge

| Dimension | /mcclain-persona-forge | /mcclain-persona-from-source |
|-----------|----------------------|----------------------------|
| Starting point | Agent function + imagination | Source material evidence |
| Worldview | Invented from target audience | Excavated from expert's actual beliefs |
| Voice | Designed from scratch | Derived from communication forensics |
| Backstory | Pure creative construction | Evidence-anchored with fiction filling gaps |
| Best for | Generic agents, utility agents | Expert agents from extraction pipeline |
| Authenticity | Fictional but effective | Grounded and effective |

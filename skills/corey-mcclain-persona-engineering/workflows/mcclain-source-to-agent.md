---
name: Source-to-Agent Pipeline
command: /mcclain-source-to-agent
expert: Corey McClain
category: Agent Forge
description: Master pipeline — raw source material to fully deployed persona-based expert agent in one command
inputs: Source material (YouTube URL, transcript, document, pasted content), optional creative direction
outputs: Complete persona-based agent with LLMP stack, skill architecture, and deployment files
---

# Source-to-Agent Pipeline

The master command. Feed it a YouTube video, a transcript, a course module, a blog post, a book chapter — anything with expert knowledge in it — and it builds a world-class, persona-based AI agent from the source material. One invocation. One session. One complete agent.

This is not `/extract-forge` + `/create-agent` stitched together. It's a fundamentally different pipeline because the persona isn't cosmetic — it's discovered from the source itself. The expert's actual personality, worldview, contradictions, and voice become the architectural container that elevates everything the agent produces.

## Usage

```
/mcclain-source-to-agent [source material — YouTube URL, transcript, file, or pasted content]
```

**Optional flags:**
- `--audience [description]` — reverse-engineer the persona worldview from a target audience
- `--stack [expert-name]` — pre-plan cross-expert stacking chains
- `--light` — produce a 3-5 workflow agent instead of full mastery-depth (8-15)

## Pre-Flight Gate

Before starting, verify:
- [ ] Source material is substantive (5,000+ words or 20+ minutes of video)
- [ ] Expert is not already in `AGENT_INDEX.md` (if they are → this becomes an expansion, not a new build)
- [ ] The domain is worth an agent (not just a single workflow — does this expert have enough depth for a full LLMP stack?)

## Pipeline

### Phase 1 — Source Acquisition & Comprehension

1. **If YouTube URL**: Fetch transcript
```bash
// turbo
python3 execution/fetch-transcript.py "<url>" "<expert-name>"
```

2. **Read the complete source material**. Not a skim. Not key takeaways. Full comprehension. You are about to build a person from this material — you need to know them.

3. **Initial Assessment** — answer internally:
   - Who is this expert? What are they actually good at (not their title — their gift)?
   - What is their worldview? What would they disagree with most people about?
   - What's the texture of their communication? Clinical? Passionate? Understated? Combative?
   - How deep is the methodology? (3-5 workflows or 8-15?)

### Phase 2 — Expertise Distillation (`/mcclain-expertise-distill`)

Run the expertise distillation engine to extract raw intelligence:

1. Extract genius patterns (aim for 8+)
2. Surface hidden knowledge (the stuff between the lines)
3. Identify signature moves (the repeatable techniques)
4. Collect Hall of Fame exemplars (minimum 3)
5. Build the quality rubric (7+ criteria)
6. Map the methodology architecture (what are the distinct phases/stages of their approach?)

**Output**: Raw extraction document — the intellectual raw material

### Phase 3 — Identity Excavation (`/mcclain-identity-excavate`)

Run the identity excavation engine to extract the person behind the expertise:

1. Mine personality signals from communication patterns
2. Surface worldview beliefs from stated and implied positions
3. Map voice texture from diction, cadence, and structural choices
4. Identify contradictions and tensions in their thinking
5. Extract formation clues — what shaped them, what they've overcome

**Output**: Identity profile — the personality raw material

**CHECKPOINT 1**: Present the expertise distillation + identity profile. Wait for approval before building.

### Phase 4 — Skill Architecture (`/mcclain-skill-architect`)

Design the complete skill structure from the extracted intelligence:

1. Define workflow tiers (Foundation, Practitioner, Stacking)
2. Name and describe each workflow
3. Map cross-expert stacking chains
4. Design the genius.md structure
5. Plan reference files and knowledge organization

**CHECKPOINT 2**: Present the skill architecture table. Wait for approval before building.

### Phase 5 — Persona Construction (`/mcclain-persona-from-source`)

Build the narrative life document from the identity excavation:

1. Synthesize identity markers into a coherent character
2. Write the backstory in narrative prose (not from thin air — grounded in source clues)
3. Crystallize worldview beliefs into 3-5 decision-shaping convictions
4. Design the voice layer with vocabulary, cadence, and forbidden phrases
5. Add messy human details that create the narrative container
6. Produce the complete 500-2000 word life document

**Output**: `persona.md` — The narrative container

### Phase 6 — Agent Assembly (`/mcclain-agent-assemble`)

Wire all layers into a deployable agent:

1. Build Logic layer (router prompt, workflow steps, rules, gates)
2. Build Library layer (exemplars, templates, reference files)
3. Build Memory layer (schema, write triggers, retrieval protocol)
4. Install Persona layer (life document integration)
5. Apply context compression to Logic/Library/Memory (NOT persona)
6. Create all skill files (SKILL.md, genius.md, all workflows)
7. Create agent files (AGENT.md, memory/context.md)
8. Register slash commands

**CHECKPOINT 3**: Present one sample workflow + the AGENT.md for review. Wait for approval.

### Phase 7 — Stress Testing (`/mcclain-agent-stress-test`)

Validate the agent before declaring it production-ready:

1. Vanilla comparison — same task with and without persona
2. Identity consistency — 3 different tasks, verify voice/worldview holds
3. Worldview filtering — give the agent a decision that tests its convictions
4. Output distinction — could you identify this agent's output in a blind test?

### Phase 8 — Registration & Finalization

1. Register in `AGENT_INDEX.md` and `SKILL_INDEX.md`
2. Create all `.agent/workflows/` slash command wrappers
3. Run chain finalization

```bash
python3 execution/chain_runner.py finalize "[Expert] — Persona-based agent (source-to-agent)" \
    --expert [expert-name] --skill [skill-dir] --workflow mcclain-source-to-agent \
    --type Agent --intent 9 --expert-score 9 --adversarial 8 \
    --notes "[workflow count] workflows, persona-based LLMP stack, source-to-agent pipeline"
```

**CHECKPOINT 4**: Final summary — present agent capabilities, stacking opportunities, and activation instructions.

---

## Checkpoints (4 total)

| # | After Phase | What You Approve |
|---|-------------|-----------------|
| 1 | Phase 3 | Expertise + Identity extraction — is the intelligence accurate? |
| 2 | Phase 4 | Skill architecture — are the right workflows planned? |
| 3 | Phase 6 | Sample workflow + AGENT.md — is the quality production-grade? |
| 4 | Phase 8 | Final summary — is the agent ready for deployment? |

## Quality Gate

- [ ] All 4 LLMP layers are built and installed
- [ ] Persona is narrative prose grounded in source material (not generic fiction)
- [ ] Vanilla comparison shows measurable quality gap
- [ ] Identity consistency holds across 3+ different task types
- [ ] All workflows are registered as slash commands
- [ ] Stacking chains are documented
- [ ] Agent is registered in system indices

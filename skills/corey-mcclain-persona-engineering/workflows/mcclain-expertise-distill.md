---
name: Expertise Distillation Engine
command: /mcclain-expertise-distill
expert: Corey McClain
category: Agent Forge
description: Extract genius patterns from any source and convert them into LLMP-ready Logic + Library layers
inputs: Source material (transcript, document, pasted content), expert name
outputs: Structured extraction — genius patterns, hidden knowledge, signature moves, methodology map, quality rubric
---

# Expertise Distillation Engine

Extract the intellectual architecture from any source material. This is not a summary — it's a structural decomposition of how an expert thinks, decides, and produces. The output feeds directly into LLMP Logic and Library layer construction.

The difference between this and standard `/extract`: this workflow is designed to produce output shaped for agent construction. Every pattern extracted is tagged with its LLMP layer destination. Every signature move becomes a potential workflow. Every piece of hidden knowledge becomes a Library reference.

## Pre-Flight Gate

- [ ] Source material is loaded and fully read (not skimmed)
- [ ] Expert identity is confirmed (the actual practitioner, not the interviewer or platform)
- [ ] Domain is identified (what category does this expertise belong to?)

## Workflow

### Step 1 — First-Pass Decomposition

Read the source material and extract raw intelligence into four streams:

**Stream A — What They Know (Declarative Knowledge)**:
- Frameworks, models, and named methodologies
- Definitions and distinctions they make that others don't
- Industry-specific terminology they use or coined
- Numbers, benchmarks, and thresholds they reference

**Stream B — What They Do (Procedural Knowledge)**:
- Step-by-step processes (even if they describe them casually)
- Decision trees — when do they choose Option A vs. Option B?
- Quality standards — what do they consider good enough vs. not good enough?
- Workflow sequences — what order do they do things in?

**Stream C — What They Believe (Worldview Knowledge)**:
- Contrarian positions — where do they disagree with their industry?
- Values hierarchy — what do they prioritize above what?
- Assumptions — what do they take for granted that others might not?
- Predictions — where do they think their domain is headed?

**Stream D — What They've Seen (Experiential Knowledge)**:
- Case studies and examples they reference
- War stories — specific failures and what they learned
- Pattern recognition — things they notice that others miss
- Edge cases and exceptions they've encountered

### Step 2 — Genius Pattern Extraction

From the four streams, synthesize 8-15 genius patterns. Each pattern follows this structure:

```markdown
### Pattern [N]: [Pattern Name]
**Execute**: [1-2 sentence imperative — what to do]
**Deploy when**: [When this pattern is most valuable]
**LLMP Destination**: [Logic | Library | Memory | Persona — which layer does this feed?]
**Success Metric**: [How to know the pattern was applied correctly]
```

**Extraction rules**:
- Patterns must be actionable, not observational
- Each pattern must be distinct — no overlapping patterns
- Prioritize patterns that produce different outputs when applied vs. not applied
- Tag each pattern with its LLMP layer destination for later assembly

### Step 3 — Hidden Knowledge Mining

Extract the knowledge that lives between the lines:
- Things they assume the audience already knows
- Implications of what they say that they don't spell out
- Contradictions in their methodology that reveal deeper truths
- The "why behind the why" — their reasoning about their reasoning

Format as numbered entries with a brief explanation of why this is hidden (not obvious from surface reading).

### Step 4 — Signature Move Identification

Identify 5-8 repeatable techniques that could each become a standalone workflow:

```markdown
### Signature Move [N]: [Move Name]
**The Move**: [What they do — described as a specific action]
**When**: [The trigger condition — what situation makes this move appropriate]
**Workflow Potential**: [High | Medium | Low — could this sustain a full workflow?]
```

### Step 5 — Methodology Architecture Map

Draw the structural map of how their expertise organizes:

1. **Core Loop**: What is the central repeating process? (Every expert has one)
2. **Entry Points**: Where does someone start when using this methodology?
3. **Phase Progression**: How does the work evolve? (Stages, tiers, levels)
4. **Decision Nodes**: Where does the methodology branch based on context?
5. **Output Types**: What distinct deliverables does the methodology produce?

### Step 6 — Quality Rubric Construction

Build a 7-10 criterion rubric from the expert's own standards:

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| [Criterion from expert's values] | [Minimum standard] | [Professional standard] | [Expert standard] |

### Step 7 — LLMP Layer Mapping

Sort all extracted intelligence into its destination layer:

| LLMP Layer | Content | Token Estimate |
|-----------|---------|---------------|
| **Logic** | [Rules, workflow steps, decision gates from patterns] | ~[N] |
| **Library** | [Exemplars, frameworks, templates from hidden knowledge + case studies] | ~[N] |
| **Memory** | [What the agent should track/remember from methodology map] | ~[N] |
| **Persona** | [Worldview beliefs, voice patterns, identity clues — hand off to identity excavation] | ~[N] |

---

## Output Schema

A single **structured extraction document** with five required sections, in this order:

1. Genius Patterns (8-15, each in the `### Pattern [N]: [Name]` format from Step 2 — Execute / Deploy when / LLMP Destination / Success Metric)
2. Hidden Knowledge (numbered entries with a "why this is hidden" note, Step 3)
3. Signature Moves (5-8, `### Signature Move [N]` format — The Move / When / Workflow Potential, Step 4)
4. Methodology Architecture Map (Core Loop, Entry Points, Phase Progression, Decision Nodes, Output Types, Step 5)
5. Quality Rubric (7-10 criteria table, Step 6) + LLMP Layer Mapping table (Step 7)

This feeds `/mcclain-identity-excavate` (Persona layer) and `/mcclain-skill-architect` (workflow design) directly — save as a source document, not a final deliverable.

## Quality Gate

- [ ] 8+ genius patterns extracted, each with LLMP layer destination
- [ ] Hidden knowledge includes at least 3 non-obvious insights
- [ ] 5+ signature moves identified with workflow potential rating
- [ ] Methodology architecture map shows core loop and decision nodes
- [ ] Quality rubric has 7+ criteria derived from expert's own standards
- [ ] LLMP layer mapping shows all content categorized by destination

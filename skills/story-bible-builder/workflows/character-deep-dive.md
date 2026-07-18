---
name: "Character Deep-Dive"
slug: "character-deep-dive"
produces: "One locked character section (section 8 format) per pass — the bible's biggest and highest-value section"
skill: "story-bible-builder"
load_context: "genius.md"
---

# Story Bible Builder — Character Deep-Dive

## Role
You are running Build-Flow Step 3 of Story Bible Builder: the character interview. This is the single most important workflow in the skill — "most of the bible lives" here (`SKILL.md`, line 106). **One character at a time. Never batch** (`SKILL.md`, line 107).

## Input Required
1. Which character is up next (from the Step 0 character count).
2. Full run through `references/character-interview.md`'s nine parts for that one character: Function, Visual lock, Backstory, Present-tense psychology, Speech, Movement, Stillness, Musical voice (music scope only), Sub-beats (optional).
3. Whether the story is in music scope (Suno descriptor applies only if yes — `references/character-interview.md`, line 105).

## Workflow

### Step 1 — Function first, not looks
Ask for role/function before anything visual (`references/character-interview.md`, lines 9–17). Push past a job description ("the leader") to an actual function ("the one who feels most for the humans they're saving," same file, line 17). This becomes the italicized role tag in the header.

### Step 2 — Visual lock interview
Walk hair, skin (with a "never" clause), face structure, eyes, signature identity markers, body/posture, default expression, and locked "never" clauses in that order (`references/character-interview.md`, lines 21–32). Every character needs at least one signature identity marker (line 29).

### Step 3 — Backstory and present-tense psychology
Backstory: push for one small, specific formative detail over a biography summary (`references/character-interview.md`, line 44). Present-tense psychology: push for the internal contradiction — "the thing the character is doing versus the thing they're actually feeling. That gap is where the drama lives." (same file, line 54).

### Step 4 — The four quoted prompt-ready descriptors
Interview Speech, Movement, Stillness, and (if music scope) Suno as separate sub-questions each, then assemble each into ONE quoted string (`references/character-interview.md`, lines 58–117). **Never use the character's name inside any of the four quoted descriptors** — trait language only (`references/character-section-format.md`, line 41).

### Step 5 — Optional sub-beats
Only include a bold sub-beat if the user names a specific locked narrative thread — never force one (`references/character-interview.md`, line 124).

### Step 6 — Assemble, show back, iterate
Compress the Visual block into one dense line (`references/character-section-format.md`, line 43). Assemble the full section in the exact structure at `references/character-section-format.md`, lines 9–29. Show it back verbatim and ask: "Here's [character name]'s section. Anything to add, cut, or sharpen? Once you approve, this is locked canon in your bible." (`references/character-interview.md`, line 135). Iterate until locked before starting the next character.

## Output Schema

One character section per delivered turn, in the exact order and bolding of `references/character-section-format.md`:
```
### [NAME] — *[Role tag]*
**Visual:** [one dense line]
**Function in the story:** [...]
**Backstory:** [one short paragraph or a few tight bullets]
**Present-tense psychology:** [...]
**Speech:** "[quoted descriptor, no name]"
**Movement:** "[quoted descriptor, no name]"
**Stillness:** "[quoted descriptor, no name]"
**Suno (if music scope):** "[quoted descriptor, no name]"
[optional bold sub-beat]
```

## Quality Gate

1. **Function precedes backstory** in both interview order and output order (`references/character-section-format.md`, line 45).
2. **All four prompt-ready descriptors are single quoted strings**, never a free paragraph, and contain zero instances of the character's own name.
3. **Visual block is one line**, not a bulleted list.
4. **At least one locked "never" clause** exists somewhere in the section (skin, expression, or a physical trait).
5. **Stranger test** — could a reader who has never heard of this story write a scene with only this section, and get the character right? (`references/example-bible-excerpts.md`, line 113).
6. **No batching** — this workflow output is exactly one character; a multi-character dump in a single turn fails the gate regardless of section quality.

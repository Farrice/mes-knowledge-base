---
description: "Etymological depth deployment — take the 5 most important words in any piece, trace their full OED lineage, and let the root meanings reshape how you use them. Pattern 14: Definition is the enemy of imagination."
---

# /etymology-engine — Etymological Depth Engine

Deploy Pattern 14 from Ocean Vuong's extraction: "Definition is the enemy of imagination." Every word has a history longer and stranger than its dictionary entry. This workflow mines that history and lets the etymological depth reshape how you write about anything.

## The Chain

1. **SCORE**: Intent Score 5
2. **ROUTE**: Ocean Vuong (perceptual writing)
3. **LOAD**: Tier 1 — `skills/ocean-vuong-perceptual-writing/SKILL.md` + Pattern 14
4. **PRODUCE**: Execute phases below
5. **FINALIZE**: chain_runner.py

## Execution

### Phase 1: Select the 5 Key Words

From the piece (or subject), identify the 5 words carrying the most weight. These are usually:
- The word that names the subject
- The word that names the problem
- The word that names the solution or transformation
- The 2 most repeated words in the piece (repetition signals importance AND potential dictionary-shallowness)

### Phase 2: Etymological Mining

For each word, trace the full history:

| Word | Dictionary Definition | Etymology (Root Language) | Root Meaning | Physical/Behavioral Origin | Surprising Connection |
|------|----------------------|--------------------------|--------------|---------------------------|----------------------|
| "Comprehend" | To understand | Latin *comprehendere* | To seize, grasp together | Physically grabbing something with your hands | Understanding is an act of physical seizure |
| "Disaster" | A sudden calamity | Italian *disastro* | Bad star | Literally: the stars are against you | Every disaster is cosmic in its etymology |
| "Courage" | Bravery | Old French *corage* | Heart | Not "bravery" but "from the heart" | Courage isn't fearlessness — it's heartfulness |

**Sources**: OED, Webster's 1913 (pre-standardization), Etymonline.com, Wiktionary etymology sections.

### Phase 3: The Depth Rewrite

For each key word, write one sentence that uses the word at its ETYMOLOGICAL depth rather than its dictionary-shallow definition:

- **Dictionary-shallow**: "She comprehended the situation quickly."
- **Etymologically deep**: "She comprehended the situation — seized it with both hands the way you seize a child running toward traffic."

The etymological version doesn't just MEAN more — it DOES more. The physical root creates a sensory experience inside a cognitive statement.

### Phase 4: Integration

Revise the piece (or write the new piece) using the etymologically deepened versions. Not every word needs etymological treatment — only the 5 key words. The rest of the prose operates at standard depth, creating contrast that makes the deep words LAND.

### Phase 5: The Depth Test

- [ ] Does knowledge of the etymology change what the sentence DOES (not just what it means)?
- [ ] Would a reader who doesn't know the etymology STILL receive something extra from the usage?
- [ ] Does the etymological depth feel natural or forced? (If forced, the word isn't ready — try a different depth.)

## Output

1. The 5 Key Words table with full etymological mining
2. Depth Rewrite sentences (one per key word)
3. The revised piece with etymological depth integrated
4. Depth Test results

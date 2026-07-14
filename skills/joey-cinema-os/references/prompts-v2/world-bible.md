---
name: "Joey — Story/World/Brand Bible"
source_prompt: born-v2
skill: joey-cinema-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Joey's CANON layer (Noisy Group / Control World — professional filmmaker who built Control (CTRL), a fully AI-generated K-pop group with published music videos, and gave the pipeline away as free Claude skills). The bible is the expensive, permanent context every downstream prompt reads for free: who the characters are, how they speak and move, what each era looks like, and the production rules the owner has hard-earned. The bible **refuses cinematography** — camera, lens, and grade language belong to the stills and video layers, never here. Execute per `skills/story-bible-builder/SKILL.md` (this prompt runs its build flow; it does not replace it) with the joey-cinema-os canon discipline held throughout (genius.md patterns 15-19).

## Input Required

- `[WORLD_TYPE]` — story world / brand world / client brand world / music-video world / ad-campaign world (changes the interview per the adaptations below)
- `[OWNER_ANSWERS]` — the owner's interview answers, in their own words. **This deliverable is interview-driven: a bible written without the owner's answers violates the never-invent rule.** If answers are missing, the protocol's job is to ask, not to fill.
- `[OWNING_PROJECT]` — where the bible lives (`projects/<name>/bible/` or `_active/<client>/bible/`); no home named → ask before starting
- `[EXISTING_BIBLE]` — path if one exists (then this is a REFRESH: re-interview only changed/thin sections; existing locks are canon, never softened without the owner reopening them)
- `[PROMPT_TOOLS]` — which tools future scenes use (Seedance, Banana Pro, Suno, …) — decides which production rules bake in

## Execution Protocol

Run story-bible-builder's build flow (Steps 0-7), producing the 12-section structure IN ORDER — this is THE STRUCTURE OF THE OUTPUT, never re-ordered:

1. One-line premise · 2. Thesis · 3. World timeline · 4. Aesthetic era differentiation · 5. Factions/powers · 6. Bases/locations · 7. Rules of the world · 8. Characters (one deep section each) · 9. Relationships & ensemble dynamics · 10. Structural engines · 11. Production rules · 12. "When this skill is active"

**The spine (sections 1-4).** Premise compressed to ONE sentence — the compression is the value. Thesis is theme, not plot: the question every scene answers. Timeline walked era by era. The aesthetic-per-era block is where most bibles are weakest — "dark and moody" is not a lock; push for colors, lighting quality, texture, grain per era, hex values where the owner has them.

**Factions, locations, world rules (5-7).** Short declarative bullets. Locations get visual tags of three to seven words — "Berlin bunker" is not a location; *concrete walls, monitor light, cable spaghetti, one warm amber pocket* is. For factions: name, belief, and how they read visually (uniform, silhouette, color signature).

**Characters (8) — one at a time, never batch.** Per character, run the interview in `skills/story-bible-builder/references/character-interview.md`: visual lock, story function, backstory beats, present-tense psychology, speech pattern, movement pattern, stillness pattern, musical voice if music is in scope. Four hard disciplines:
- **"Never" clauses on every visual lock** — when a trait locks, name the wrong-answer drift: "warm fair skin — never pale porcelain, never tan." A lock without its exclusions won't hold over hundreds of renders.
- **[TBD] over plausible** — the owner doesn't know → mark `[TBD]` and move on. Invented canon becomes locked canon becomes prompt drift.
- **Prompt-ready quoted payloads** — Speech, Movement, and Stillness descriptors must paste VERBATIM into their downstream slot (Speech → Sound Bed, Movement/Stillness → Subject Lock). If a descriptor can't be pasted as written, it's written wrong; rewrite until it can. No character names inside the quotes — refer by trait.
- **Depth beats count** — three deep characters beat eight shallow ones; offer to hold the rest for a follow-up pass.

**Ensemble, engines, production rules (9-11).** Ensemble dynamics as short declarative sentences ("who fills silence, who watches, which pairings are charged"). Structural engines = the recurring chapter shapes, one line each, noting that engines stack. Production rules bake in the AI-filmmaker defaults (no character names in prompts, every prompt standalone, code-block output, no aspect ratio in the prompt body, locked traits restated verbatim) plus everything the owner has hard-earned — **their exact phrasing, quoted**.

**Assembly (12).** The closing section instructs future Claude in BOTH modes — standalone canon reference AND paired with a director skill (Speech → Sound Bed, Movement/Stillness → Subject Lock, aesthetic era → World Plate/grade, production rules → rule layer). Name the production companion skills explicitly (in this workspace: `banana-pro-director` and `cinema-worldbuilder-pro` unless the owner names others). Save to the owning project's `bible/` folder — never loose in the repo root, never inside the skill directory.

**The stranger-test gate (before shipping):** *"Could a stranger who has never heard of this story write a scene in it, using only this bible, and get it right?"* Walk one hypothetical scene against the doc. Anything the stranger would have to invent is a gap — fill it or mark `[TBD]` visibly.

World-type adaptations: **brand world** — "characters" = products + brand avatars, visual locks become material/construction/palette locks WITH a colors-to-avoid row (KY method), factions → product lines, thesis → brand promise. **Client brand world** — save to `_active/<client>/bible/`, absorb the client's voice/constraint docs by pointer. **Music-video world** — musical voice section mandatory per character (Suno-ready). **Ad-campaign world** — slim build: premise, ICP-facing thesis, one aesthetic era, in-frame products/avatars, production rules; skip factions/engines cleanly.

## Output Contract

- One dense SKILL.md-format bible, ≤500 lines, exact 12-section order, with YAML frontmatter (name + pushy auto-load description)
- Every character visual lock carries its "never" clauses; every unknown is `[TBD]`, never filled
- Speech/Movement/Stillness (and Suno where in scope) descriptors quoted and verbatim-pasteable into their downstream slots
- Zero cinematography language anywhere in the doc
- Density register: greppable bullets and bold labels, owner's phrasing kept verbatim where it was good — not prose paragraphs
- Saved to `[OWNING_PROJECT]/bible/<slug>.md`; path reported

## Output Skeleton

```
---
name: [world-slug]
description: "[pushy one-paragraph description that makes future sessions auto-load this world]"
---

[H1 title line: the working title — Bible]

## 1. One-line premise
[one sentence]

## 2. Thesis
[the question every scene answers]

## 3. Timeline
[era — years — what defines it, per era]

## 4. Aesthetic era differentiation
[per era: palette (hex where known), lighting quality, texture, grain]

## 5. Factions / powers
[per faction: name · belief · visual signature]

## 6. Locations
[per location: name · 3-7 word visual tag · story function]

## 7. Rules of the world
[declarative bullets: technology, powers-as-they-LOOK, social systems, forbidden things]

## 8. Characters
### [Name]
Visual lock: [traits, each with its "never" clause]
Function / backstory beats / present-tense psychology: [...]
Speech: "[quoted, name-free, paste-ready descriptor]"
Movement: "[quoted descriptor]"   Stillness: "[quoted descriptor]"
[Musical voice: "[Suno-ready descriptor]" — if in scope]
[TBD]: [list or none]
[repeat per character]

## 9. Relationships & ensemble dynamics
[short declarative sentences]

## 10. Structural engines
[engine — one line, per engine]

## 11. Production rules
[AI-filmmaker defaults + the owner's hard-earned rules, their phrasing quoted]

## 12. When this skill is active
[standalone-mode instructions + paired-with-director slot mapping + named companion skills]
```

## Quality Gate

- [ ] Stranger test passed on at least one walked scene — nothing the stranger would have to invent?
- [ ] Zero invented canon — every fact traces to the owner's answers or is marked `[TBD]`?
- [ ] Every visual lock excludes as well as includes (a "never" clause wherever drift is known)?
- [ ] Test-paste passed: one Speech line drops verbatim into a Sound Bed frame, one Stillness line into a Subject Lock frame, no rewording, no names inside quotes?
- [ ] No cinematography in the doc — any camera/lens/grade language found was cut and noted for the worldbuilder layer?
- [ ] Saved to the owning project (not the skill directory), path reported?

## Creative Latitude

The 12 sections are the floor, not the ceiling. The bible's voice should be the owner's world at full temperature — the thesis can be genuinely strange, the ensemble dynamics can read like the best line in a writers' room ("Owen and Iris cannot be in the same kitchen without one of them leaving"), and the structural engines should surprise. Push the owner past their first vague answer: the follow-up question that turns "dark and moody" into a lockable palette is where the interviewer earns the credit. Where the world genuinely warrants a section the structure doesn't name (a mythology appendix, a slang lexicon), add it after section 11 rather than diluting the locked order.

## Deploy When

- A new persistent world is starting — characters, brand, music-video universe, client campaign world — and multi-scene work is coming
- An existing bible needs a refresh (new era, new characters, hard-earned production rules)
- Voice/persona drift traces back to missing canon (`/jcin-voice-lock`'s upstream fix)
- Invoked via `/jcin-world-canon` or the pipeline conductor's CANON checkpoint

---
description: Build or refresh a story/world/brand bible via story-bible-builder — scope check, interview flow, one character at a time, "never" clauses, [TBD] discipline, saved to the owning project, gated by the stranger test
---

# `/jcin-world-canon` — World Canon (Bible Build)

Builds the CANON layer: one dense, locked, prompt-ready bible document. The bible carries who/voice/era/rules so no downstream prompt ever re-invents them. The bible **refuses cinematography** — camera language belongs to Banana Pro and the worldbuilder.

## Pre-Flight Gate

- [ ] **Existence Question:** does a bible already exist for this world? Check `projects/<name>/bible/` and `_active/<client>/bible/` before interviewing. Exists → this is a REFRESH (ask for the current file, work from it); never rebuild from scratch.
- [ ] **Owning project identified** — every bible has a home. No home named → ask before Step 0.
- [ ] **World type known:** story world, brand world, or client brand world (adaptations table below changes the interview).
- [ ] **Farrice available for the interview.** This workflow is interview-driven — a bible written without the owner's answers violates the never-invent rule. No owner in the loop → stop and say so.

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 15-19 (canon/context discipline)
2. `skills/story-bible-builder/SKILL.md` — full file (it is small); this workflow runs its build flow, it does not replace it
3. story-bible-builder `references/character-interview.md` — load only when Step 3 (characters) is active
4. story-bible-builder `references/example-bible-excerpts.md` — load only if the user needs to see target density

## Execution

Run story-bible-builder's build flow (its Steps 0-7) with the house principles held throughout. The section order of the output is the 12-section structure in story-bible-builder — THE STRUCTURE OF THE OUTPUT. Do not re-order it.

### Step 1 — Scope check (fast, one compact block)

Per story-bible-builder Step 0: working title, main character count, genre/vibe references, exists-in-head vs building-from-scratch, and **which prompt tools future scenes use** (Seedance, Banana Pro, Suno, etc. — this decides which production rules bake in at Step 6). If the user only wants part of the bible ("just nail the characters"), jump to that step — the full flow is the default, not a requirement.

### Step 2 — The spine

Premise, thesis, timeline, aesthetic-per-era (sections 1-4). Push hard: premise compressed to one sentence; thesis is theme, not plot. The aesthetic-era block is where most bibles are weakest — "dark and moody" is not a lock. Ask for colors, lighting quality, texture, grain per era. Hex values where the user has them.

### Step 3 — Factions, locations, world rules

Sections 5-7, covered together. Locations get visual tags (three to seven words) — "Berlin bunker" is not a location; concrete walls, monitor light, cable spaghetti, one warm amber pocket is. Short declarative bullets.

### Step 4 — Characters: one at a time, never batch

The biggest section. Per character, run the interview in `references/character-interview.md`: visual lock, story function, backstory beats, present-tense psychology, speech pattern, movement pattern, stillness pattern, musical voice if music is in scope.

Discipline per character:
- **"Never" clauses on every visual lock** (genius.md pattern 16): when a trait locks, ask what the wrong-answer drift looks like. "Warm fair skin — never pale porcelain, never tan." A lock without its exclusions won't hold over hundreds of renders.
- **[TBD] over plausible** (pattern 17): the user doesn't know → mark `[TBD]` and move on. Invented canon becomes locked canon becomes prompt drift.
- **Prompt-ready quoted payloads** (pattern 18): Speech, Movement, and Stillness descriptors must paste verbatim into their downstream slot — Speech → Sound Bed, Movement/Stillness → Subject Lock. If a descriptor can't be pasted as written, it's written wrong. Rewrite until it can.
- After each character: show the section, ask "add anything, cut anything, sharpen anything?", iterate to lock, then move on. Depth beats count — three deep characters beat eight shallow ones; offer to hold the rest for a follow-up pass.

### Step 5 — Ensemble, engines, production rules

Sections 9-11 per story-bible-builder Steps 4-6. Production rules bake in the AI-filmmaker defaults (no character names in prompts, every prompt standalone, code-block output, locked traits restated verbatim) plus everything the user has hard-earned — **their exact phrasing, quoted**.

### Step 6 — Assembly + "when this skill is active"

Assemble the full SKILL.md per story-bible-builder Step 7, closing section instructing future Claude in **both modes** (standalone canon reference / paired with a director skill). Name the production companion skills explicitly — in this workspace that is `banana-pro-director` and `cinema-worldbuilder-pro` unless the user names others.

**Save to the owning project:** `projects/<name>/bible/<working-title-slug>.md` or `_active/<client>/bible/<slug>.md`. Never leave a bible loose in the repo root or inside `skills/joey-cinema-os/`.

### Refresh mode (existing bible)

When the Pre-Flight Gate found an existing bible, do not re-run the full interview:

1. Read the current file end to end; list its `[TBD]` markers and any sections thinner than the example-excerpt density
2. Ask what changed in the world since the last pass — new characters, new era, retired canon, production rules learned the hard way
3. Re-interview ONLY the changed/thin sections, one at a time, same discipline as a fresh build ("never" clauses, [TBD], paste-ready payloads)
4. Existing locks are canon — never soften or rewrite a lock the user hasn't reopened; drift repair means restating the lock, not renegotiating it
5. Re-run the stranger test on the updated doc before saving over the old version (keep the prior version via git, not a `-v2` filename)

### Step 7 — Stranger-test gate, then optional install

Run the stranger test (genius.md pattern 19) before calling it shipped: **"Could a stranger who has never heard of this story write a scene in it, using only this bible, and get it right?"** Walk one hypothetical scene against the doc. Any answer the stranger would have to invent = a gap; fill it or mark `[TBD]` visibly.

Then offer (never force) install-as-skill: copy to `skills/<world-slug>/SKILL.md` with the pushy frontmatter description so future sessions auto-load it, or zip as an installable `.skill`. The on-disk bible in the project stays the source of truth either way.

## Content Type Adaptations

| World type | What changes in the interview |
|---|---|
| Character / story world | Full 12-section flow as written |
| Product / brand world (MyBPM) | "Characters" = products + brand avatars; visual locks become material/construction/palette locks **with a colors-to-avoid row** (KY method); factions → product lines; thesis → brand promise |
| Client brand world (Jen, TrendScale) | Save to `_active/<client>/bible/`; production rules absorb the client's existing voice/constraint docs by pointer; flag anything colliding with the client CLAUDE.md |
| Music video / band world | Musical voice section mandatory per character (Suno-ready descriptor); era palettes get per-era grade language the worldbuilder can quote |
| Ad campaign world | Slim build: premise, ICP-facing thesis, one aesthetic era, the products/avatars in frame, production rules. Skip factions/engines cleanly |

## Output Requirements

- One dense SKILL.md-format bible, ≤500 lines, matching story-bible-builder's 12-section order
- Every character lock carries its "never" clauses; every unknown carries `[TBD]`
- Speech/Movement/Stillness descriptors quoted and paste-ready for Sound Bed / Subject Lock
- Saved to the owning project's `bible/` folder; path reported to Farrice
- Closing section names the paired production skills for future sessions

Execution prompt: references/prompts-v2/world-bible.md — honor its Output Contract.

## Quality Gate

- [ ] Stranger test passed on at least one walked scene (rubric: world believability ≥7 requires era/palette locks a stranger could apply)
- [ ] Zero invented canon — every fact traced to the user's answers or marked `[TBD]` (anti-pattern: inventing canon to fill a gap)
- [ ] Every visual lock excludes as well as includes (anti-pattern: locks without "never" clauses)
- [ ] Descriptors paste verbatim into their downstream slots — test-paste one Speech line into a Sound Bed frame and one Stillness line into a Subject Lock frame
- [ ] No cinematography in the bible — camera/lens/grade language found = cut it and note it for the worldbuilder layer
- [ ] Density: greppable bullets and bold labels, not prose paragraphs; user's own phrasing kept verbatim where it was good
- [ ] Saved to the owning project, not the skill directory

Fail any box → fix in the bible now; a bible shipped with gaps drifts every downstream prompt that reads it.

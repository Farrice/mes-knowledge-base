# Story Bible Builder — Genius Context

> Load this before any workflow. This is a **method/meta-skill**, not a person-extraction skill — it's a locked interview-and-assembly grammar for compiling a story world into one installable canon `SKILL.md`, authored by Joey (YouTube channel "JOEY," ~25,000 subscribers, Higgsfield-sponsored via credit giveaways, builder of the fully AI-generated K-pop group **Control (CTRL)** under the community brand **Noisy Group**, per `extractions/joey-cinema/VISION.md`, line 7). It shipped as the third skill — new in this drop — alongside `banana-pro-director` and `cinema-worldbuilder-pro`, per the companion doc harvested 2026-07-13: "story-bible-builder — the new one." (`extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 23). Grounded in the skill's own `SKILL.md` (200 lines, read in full) plus its three reference files. Every claim below is anchored — see `references/source-ledger.md` for VERIFIED/LIKELY/UNCONFIRMED labels claim-by-claim.

---

## How to Use This Skill (Model Calibration)

These are intuition primitives for an interview-driven canon-compiler, not a checklist to march through. Absorb the never-invent discipline and the one-character-at-a-time density, then run the interview conversationally — never dump all eight interview questions at once, never caption a turn with the section number you're filling. If the output narrates its own scaffolding — "Now moving to Section 4: Aesthetic Era Differentiation" — or ships a character with a bulleted feature list instead of one dense Visual line, it has failed. The test: would Joey — or a story-bible-builder user reading his own Jul 12/13, 2026 companion notes on this exact drop — **recognize this as** production-grade canon compilation, or as someone filling out a generic worldbuilding questionnaire template with the labels left visible? If it's the second, rebuild toward the locked structure.

Specifically:
- Do NOT batch characters through the interview to save turns. The skill is explicit: "One character at a time. Never batch." (`skills/story-bible-builder/SKILL.md`, line 107). A bible with eight thin character passes has failed even if every section technically exists.
- Do NOT accept the user's first vague answer on aesthetic, voice, or visual locks. "'Dark and moody' isn't an aesthetic lock. 'Cool voice' isn't a voice profile. 'Powerful' isn't a description." (`skills/story-bible-builder/SKILL.md`, line 178). Push for the color, the register, the committed shape before moving on.
- This skill's specific texture is the **quoted, prompt-ready descriptor** — Speech, Movement, Stillness, and (music-scope) Suno lines are written as one assembled quoted string with the character's name never inside it, because "Names drift models. Names live in the header only." (`skills/story-bible-builder/references/character-section-format.md`, line 41). A bible that describes a character's voice in a free paragraph instead of one copy-pasteable quoted line has missed the entire point of the skill.
- Polish is the tell for this class of skill: a character section that reads like a pitch-deck bio ("she is fierce, mysterious, and unforgettable") instead of a working reference with a "never" clause is decoration, not canon. The skill's own density discipline: "The user should be able to grep this doc." (`skills/story-bible-builder/SKILL.md`, line 174).

---

## Anti-Patterns (Sourced)

- **Batching multiple characters through one interview pass** instead of running each to full depth before moving on — "One character at a time. Never batch. Each character gets a deep dedicated pass." (`skills/story-bible-builder/SKILL.md`, line 107).
- **Leaving names inside the quoted Speech/Movement/Stillness/Suno descriptors** instead of pure trait language — "Never use the character's name inside the quoted descriptors... Refer by trait ('low-register voice,' 'cocked-hip stance'). Names drift models. Names live in the header only." (`skills/story-bible-builder/references/character-section-format.md`, line 41).
- **Accepting a vague aesthetic or voice answer without pushing for specificity** — "Push on the vague. 'Dark and moody' isn't an aesthetic lock. 'Cool voice' isn't a voice profile. 'Powerful' isn't a description." (`skills/story-bible-builder/SKILL.md`, line 178).
- **Locking a physical or vocal trait without its "never" clause** — "Locks exclude as much as they include... 'Warm fair skin — never pale porcelain, never tan.' The 'never' clause is what stops model drift over hundreds of future renders." (`skills/story-bible-builder/SKILL.md`, line 180).
- **Cramming eight-plus shallow characters into one bible pass** instead of depth-first triage — "Character depth matters more than character count. Better to ship a bible with three deep characters than eight shallow ones." (`skills/story-bible-builder/SKILL.md`, line 182).
- **Writing the Visual block as a bulleted feature list** instead of one flowing dense line — "Visual block is one dense line. Not a bulleted list of features." (`skills/story-bible-builder/references/character-section-format.md`, line 43).
- **Naming a real artist or song in a Suno vocal-casting descriptor** — "Never use artist names or song references in Suno prompts — that gets rejected." (`skills/story-bible-builder/references/character-interview.md`, line 116).
- **Saving the assembled bible to the claude.ai sandbox path instead of a repo path** — the original zip's install defect, caught and already corrected in this installed copy (`skills/story-bible-builder/SKILL.md`, line 166 now reads `projects/<project>/bible/[working-title-slug].md`), flagged so a future edit doesn't regress it: "Saves output to `/mnt/user-data/outputs/` (claude.ai sandbox path)... Repoint to a repo path." (`extractions/joey-cinema/skill-files-analysis.md`, line 296).

---

## Verbatim Exemplars

> "instead of burning memory slots on world context, or re-explaining the story every chat, the user gets one file that lives as a skill and auto-loads every time they work on their world." — `skills/story-bible-builder/SKILL.md`, line 10 (the founding problem statement).

> "Invented canon becomes locked canon becomes prompt drift." — `skills/story-bible-builder/SKILL.md`, line 176 (House Principle 2, Never Invent).

> "could a stranger who has never heard of this story write a scene in it, using only this bible, and get it right?" — `skills/story-bible-builder/references/example-bible-excerpts.md`, line 113 (the universal density-doneness test, "the universal signal").

> "The bible builder interviews you — premise, timeline, factions, locations, characters with voice and movement locks, ensemble dynamics, plot engines, production rules — and outputs a SKILL.md you install. After that, every image prompt, every video prompt, every lyric, every line of dialogue already knows your world. No memory tax. No re-explaining." — Joey, "The AI Cinema Claude skills got a BUFF!" companion doc, harvested 2026-07-13, `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, lines 77–79.

---

## Person, Tool & Cross-Skill Facts (Grounding)

Real production context this skill routes against, per `extractions/joey-cinema/VISION.md` (line 7): Joey is a professional filmmaker (brand/ad work) turned AI filmmaker running the ~25,000-subscriber channel "JOEY," building **Control (CTRL)**, a fully AI-generated K-pop girl group with published music videos, under the community brand **Noisy Group**. `story-bible-builder` is described in his own words as "the new one" in the v3 drop and "the one I'd install first if I were starting over" (`extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, lines 23, 81) — positioned as the upstream canon layer that stops the other two visual-production skills (`banana-pro-director`, `cinema-worldbuilder-pro`) from drifting: "This is the one that makes the other two stop drifting." (same doc, line 23).

Design thesis, in the extraction's own framing: "Story/Outfit/Voice Bibles as model context — consistency lives in context, not the model." (`extractions/joey-cinema/VISION.md`, line 26). The extraction also names the exact cross-skill stack this composes with on the narrative side: "Joey × **Ben Watkins / Stanton / Hawley** (story spine feeding the Story Bible — narrative layer above the visual pipeline)" (`extractions/joey-cinema/VISION.md`, line 41) — meaning `ben-watkins-storytelling`, `andrew-stanton-audience-engineering`, and `noah-hawley-storytelling-mastery` are the craft-layer skills that supply the *narrative spine* (premise, thesis, character function) this skill's interview compiles into locked canon; story-bible-builder itself does not originate story craft — it locks whatever the user (optionally aided by those skills) already has.

**Gap checked, not silently resolved:** `extractions/joey-cinema/transcript.txt` (15,915 bytes, one of three general-pipeline video transcripts in the `joey-cinema` folder) was grepped for `story.bible|story bible|bible builder` and returned **zero matches** — that transcript covers the general canonical-asset-sheet pipeline, not story-bible-builder-specific interview content. Confirmed absent by a real grep, not assumed. `extractions/joey-cinema/VISION.md` line 13 additionally names three source videos (x5nP-3t6R9o, 0YhhPQVXA7c, yb0RWQ0mbXg) whose content maps to `banana-pro-director` and `cinema-worldbuilder-pro`, not to this skill specifically — the skill's own 200-line `SKILL.md` and its three reference files remain the only text source that is story-bible-builder-specific.

---

## Source Ledger Pointer

Full claim-by-claim VERIFIED / LIKELY / UNCONFIRMED breakdown lives in `references/source-ledger.md` — every source consulted for this repair pass (the skill's own 15,023-byte `SKILL.md` and its three reference files totaling 17,710 bytes, the 13,796-byte Notion companion doc, the extraction's `VISION.md`, the cross-check `skill-files-analysis.md`, and the checked-absent `transcript.txt`) is logged there with file path, byte size (`wc -c`), and verification status.

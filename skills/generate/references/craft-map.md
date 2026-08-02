# Craft Map — which master loads before which generation (BINDING, Farrice 2026-08-02)

**The rule: no generation — paid or free, draft or final — fires with a freehand prompt.**
Every prompt is authored through the matching craft layer below, then gets a doctor pass.
Scar this exists for: the 2026-08-02 Seedance teaser take 1 — prompt written freehand while
`cinema-worldbuilder-pro` sat extracted on the shelf; output was slop. Take 2 through the
grammar, same model, same price: production-usable. The knowledge was never the gap;
loading it mechanically is.

| Output | Load FIRST | Doctor pass |
|---|---|---|
| Seedance video (any) | `skills/cinema-worldbuilder-pro/SKILL.md` — mode select (M1–M5), Write-the-Visible, FOV table, block structure | Read the prompt back as the shot: every word renders a pixel or gets cut |
| Kling video / multi-shot | `skills/fantastic-posters/workflows/kling-multishot.md` + cinema-worldbuilder cut grammar | Cut list explicit, continuity held across cuts |
| AI-video direction / film craft | `/pj-accetturo-ai-video` · `/tao-prompts-ai-video` | Story beat before shot beat |
| Stylized image (catalog style) | `skills/fantastic-posters/SKILL.md` style picker + the style's own build notes | Style fields (title/subtitle/footer/subject) filled deliberately, never defaulted |
| Open art direction (direct lane) | `/art-direct` or `/creative-prompt` (creative-direction skill) + relevant style card from `skills/generate/styles/` | Prompt is a full production document: subject, composition, light source+direction+temp, lens language, palette anchored to surfaces, finish register |
| Photoreal people | `higgsfield-soul` lane via `creative_router.py` (BINDING) + `/banana-pro` for character builds | Face/identity locked to reference, never freehand |
| Persistent character/world | `/jcin-pipeline` (bible → locks → plates) + `jcin-prompt-doctor` | Canon checked against the bible |
| Anime/manga (his lane) | direct lane + his style cards (`manga-ink`, `shonen-ui-glow`, `alchemist-blaze`, …) + character ref once locked | Register named (which anime grammar), text minimal and intentional |
| Vector/text-heavy (recraft) | recraft recipe notes + `/kittl` typography judgment for lockups | Text content exact, style param deliberate ($0.04 vs $0.08 vector) |
| Audio TTS/music | recipe notes; voice/tone brief written like a VO director's note (pace, register, where the emphasis lands) | Read the text aloud mentally — punctuation drives the read |
| Mood boards / visual development | `/mood-board` (creative-direction skill) | Board argues ONE direction, not a collage of maybes |
| **Image art direction — look undecided, aesthetic sweeps, style banks** (the pre-generation decision layer, model-agnostic) | `skills/nick-st-pierre/SKILL.md` — five pillars (layered build · controlled sweeps not rerolls · style-code library · reference-over-adjective · image-as-substrate); sweep = `workflows/01`, build = `workflows/02`, bank = `workflows/03`. Tool syntax is quarantined in `references/era-bound-mechanics.md` — verify before use | Run the ten-check critique pass. Two that fail most: is the light **named and placed** (not "beautiful lighting"), and **what is in tension** — an image where every element agrees with every other is the definition of slop. Then: would this have looked the same without me? |
| **Image OPERATIONS — many on-brand images, not one** (style-handle sweeps, style/moodboard libraries, brand-consistent asset systems, batch production graphs) | `skills/rory-flynn/SKILL.md` — nine Image Elements, frozen-backbone/variable-head split, then the matching workflow: `moodboard-sweep.md` (characterize handles: null run → solo→stack ladder → weight sweep → named recipes) · `style-code-library.md` (backbone + handle inventory + handoff signature) · `photorealism-language.md` (photography vocabulary, left-anchor swap, imperfection pass) | Two checks. **(1) No element silently delegated** — every one of the nine is decided or marked deliberately open; unspecified = model-chosen = drift. **(2) The handoff test** — "any \<input\> goes in, \<output\> comes out"; if only you can operate it, it isn't a system. Style handles never enter production uncharacterized (no null run = no card = don't ship it) |
| Cinematic direction / "why does this look flat?" | `skills/dave-clark/SKILL.md` + `genius.md` — the eight causes of flat, look card (light / black point / palette / atmosphere / capture register), coverage pairs, cadence plan. Shot list BEFORE prompt; hybrid work → `workflows/02-hybrid-pipeline-plan.md` | Run the flat-to-cinematic audit: name one motivated light source, a real black point, atmosphere in the mid-ground, ≥5 takes composited, uneven cut rhythm, one global capture layer. **No finding may be answerable with "switch models."** |

**Intent mirror (creative asks):** before generating from a raw dump, reflect back in ≤5 lines:
deliverable + format, felt standard ("cinematic macro, matte, no gloss"), references in play,
budget, and the ONE thing that would make it his ("what's the detail that makes this yours?").
Proceed on his confirm or visible non-objection; never silently guess taste on new ground.

**Show craft with the quote:** for paid video, the crafted prompt is presented WITH the cost
quote — one look approves money and craft together.

This map extends as masters are extracted (see the master-hunt mission). New master → new row.

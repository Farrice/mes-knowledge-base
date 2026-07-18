# Banana Pro Director — Genius Context

> Load this before any workflow. This is not a person-extraction skill — it's a locked image-prompt grammar for Higgsfield's Nano Banana Pro, Soul Cinema, and GPT-2 tools, engineered against the platform's own documented behavior. Grounded in `skills/banana-pro-director/SKILL.md` (the locked grammar itself, 1,118 lines) cross-checked against Higgsfield's own published prompt-engineering guidance (Rus Syzdykov, Head of Prompt Engineering at Higgsfield, "NANO BANANA PRO: Expert Use Cases with Prompts," Nov 21, 2025, https://higgsfield.ai/blog/Nano-Banana-Pro-Expert-Use-Cases) and Higgsfield's own tool-ecosystem documentation. Every claim below is anchored — see `references/source-ledger.md` for VERIFIED/LIKELY/UNCONFIRMED labels claim-by-claim.

---

## How to Use This Skill (Model Calibration)

These are intuition primitives for a tool-grammar skill, not a checklist to stamp. Absorb the mode discipline and the flat-grade physics, then compose originally inside them. If the output mechanically announces "Mode 0, Step 0.A, Bucket 3" to the user, or narrates its own reasoning ("here's why I'm using the flat grade"), it has failed. The test: would a Higgsfield power user — or Rus Syzdykov's own Nov 21, 2025 prompt-engineering guide — recognize this as production-grade Nano Banana Pro grammar, or as someone reciting generic AI-image buzzwords over a diffusion prompt? If it's the second, rebuild toward the locked grammar.

Specifically:
- Do NOT narrate the six silent buckets (Shot DNA, Subject, Detail, World, Light, Camera spec) or the X/Y coordinate planning into the delivered prompt. `skills/banana-pro-director/SKILL.md` is explicit that these are "a thinking tool, not an output structure" (SKILL.md, line 782) — the model composes with them, never shows them.
- Do NOT skip the pre-prompt confirmation to look efficient. The locked format is narrow on purpose: "Format: clean bullet points only. No quote blocks, no em-dash prose lines, no narrative wrapper" (SKILL.md, line 109). Over-explaining the check *is* the polish tell for this skill — a padded, hedged pre-prompt check reads as an AI apologizing for itself, not a director confirming a shot.
- This tool's specific texture is economy under strong references: "A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time" (SKILL.md, line 278). Padding a prompt with re-described identity that a reference image already carries is the single most common failure mode this skill exists to prevent.
- Photoreal is not a mood to reach for — it's the floor. Every mode closes with either the locked flat grade or the cinema-prose closing paragraph; there is no "in-between" stylized register unless the user explicitly overrides it.

---

## Anti-Patterns (Sourced)

- Baking X/Y coordinate notation (`X: 30–55% / Y: 25–95%`) directly into a delivered Mode 3 prompt body instead of using it as a silent planning tool. Deprecated per `skills/banana-pro-director/SKILL.md` § "THE OLD COORDINATE GRAMMAR (DEPRECATED)" (SKILL.md, line 967): "That grammar is deprecated for prose composition. It made the model overcorrect and confuse spatial relationships."
- Defaulting new character-work backdrops to pure white seamless instead of 18% gray. Reversed by the skill's own locked default in `skills/banana-pro-director/SKILL.md` § "18% GRAY SEAMLESS + FLAT GRADE" (SKILL.md, line 228): "Pure white seamless is now the explicit-request exception... When in doubt, default to gray."
- Writing numeric aspect ratios ("16:9," "3:4," "21:9") into the prompt text instead of leaving them to the Higgsfield UI. Universal Prompt Rule 13 in `skills/banana-pro-director/SKILL.md` (line 1077): "The user sets aspect ratio in the Higgsfield UI directly."
- Skipping Soul Cinema's Step 1B.1 outfit plate and compositing straight onto the locked character in one pass. `skills/banana-pro-director/SKILL.md` § Mode 1B (line 527): "Soul Cinema is a two-step process. Do not skip Step 1B.1 and jump straight to compositing."
- Proposing the 6-panel character sheet as a default option instead of the 3-panel. `skills/banana-pro-director/SKILL.md` § Mode 2B (line 696): "Never propose this format. It only runs when the user names it."
- Re-describing a character's full face and wardrobe in the prompt body when a strong reference image is already attached. `skills/banana-pro-director/SKILL.md` § lean-prompt rule (line 278): "A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time."
- Stacking heavy negative-prompt blocks onto a Nano Banana Pro request out of habit from older diffusion tools. Contradicts Higgsfield's own framing of the model per Rus Syzdykov, Head of Prompt Engineering at Higgsfield, Nov 21, 2025 (source: `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md`): "Nano Banana Pro represents a fundamental shift in diffusion technology. The model prioritizes comprehension and logical interpretation of the prompt." This is also why `skills/banana-pro-director/SKILL.md` Universal Rule 7 states plainly: "This skill does not output negative prompt blocks."

---

## Verbatim Exemplars

> "The flattering-realism ceiling (LOCKED — applies to every face, every mode). Full skin realism is always on... But realism never means *unflattering*." — `skills/banana-pro-director/SKILL.md`, line 143 (the flat-grade / photoreal governing clause).

> "A cinematic anamorphic still photograph captured handheld on a real cinema set — a Dutch-tilted intimate over-the-shoulder hero composition of a young Korean man standing alone in a dim converted private garage lounge at pre-dawn..." — `skills/banana-pro-director/SKILL.md`, line 897 (the canonical Mode 3 cinema-prose register example).

> "Nano Banana Pro represents a fundamental shift in diffusion technology. The model prioritizes comprehension and logical interpretation of the prompt." — Rus Syzdykov, Head of Prompt Engineering, Higgsfield, Nov 21, 2025, https://higgsfield.ai/blog/Nano-Banana-Pro-Expert-Use-Cases (per `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md`).

---

## Tool Facts (Grounding)

Real Higgsfield tools this skill routes against, confirmed against platform documentation captured 2026 in `extractions/creative-direction/`: Nano Banana Pro / Nano Banana 2 (high-clarity image generation), Soul 2.0 / Soul Cinema / Soul Cast / Soul ID Character (character-consistency tooling), GPT Image 1.5 (OpenAI image-model integration), Higgsfield Popcorn (AI storyboard/keyframe tool that "locks tone and composition"), Recast (character replacement that preserves motion, lighting, and atmosphere), Seedance 2.0, Kling 3.0, WAN 2.6, and Cinema Studio 3.0 (per `extractions/creative-direction/higgsfield_notes.md` and `higgsfield_pipeline.md`). Higgsfield is headquartered at 535 Mission St, 14th floor, San Francisco, CA, 94105 (per `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md`, footer capture).

**Naming gap worth flagging (not silently resolved):** `skills/banana-pro-director/SKILL.md` names "GPT-2" throughout as one of its three Higgsfield tool-fork options (e.g., line 350, line 390). None of the five Higgsfield source captures in `extractions/creative-direction/` list a Higgsfield product literally named "GPT-2" — the closest confirmed real product is "GPT Image 1.5" (per `extractions/creative-direction/higgsfield_notes.md`, line 16, and `higgsfield_pipeline.md`, line 16). Whether "GPT-2" is this skill's internal shorthand for that product or an unverified label is UNCONFIRMED — see `references/source-ledger.md`. Out of scope for this repair pass (SKILL.md content is untouched per the additive-first rule); gap named for the conductor.

---

## Source Ledger Pointer

Full claim-by-claim VERIFIED / LIKELY / UNCONFIRMED breakdown lives in `references/source-ledger.md` — every source consulted for this repair pass (5 Higgsfield extraction captures, the skill's own 1,118-line SKILL.md, and a negative-result check against `extractions/` for any dedicated Banana Pro Director source folder, confirmed absent by directory listing, not assumed) is logged there with file path and verification status.

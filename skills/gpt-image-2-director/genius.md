# GPT Image 2.0 Director — Genius Context

> Load this before any workflow. This is not a person-extraction skill — it's a locked image-prompt grammar for OpenAI's GPT Image 2.0, engineered against the model's own documented behavior. There is no dedicated `extractions/` folder for this model (confirmed by directory search, not assumed — see `references/source-ledger.md` row 6). Ground truth instead comes from two places: this skill's own locked `SKILL.md` (217 lines, three-format grammar), and real usage-policy documentation captured elsewhere in this repo for the *same underlying model* accessed via Fal's `openai/gpt-image-2` endpoint — `directives/fal-usage-policy.md`, `directives/fal-edit-mode-guide.md` (patterns harvested from `robonuggets/gpt-image-2-skill`, MIT license, 2026-04-30), and `skills/fantastic-posters/README.md` + `genius.md`, which run production jobs against this exact model. Every claim below is anchored — see `references/source-ledger.md` for VERIFIED/LIKELY/UNCONFIRMED labels claim-by-claim.

---

## How to Use This Skill (Model Calibration)

These are intuition primitives for a tool-grammar skill, not a checklist to stamp. Absorb the three-format routing logic and the model's real strengths/weaknesses, then write the prompt like a director who already knows which lens to use — never like someone filling in a template. If the delivered prompt announces its own reasoning ("I chose Format A because...") or hedges between two formats in the same output, it has failed.

The test: would a working GPT Image 2.0 prompt engineer — or the model's own documented text-rendering and layout-following behavior (the ~6-word title ceiling, the delta-only edit instruction pattern, the 3:1/multiples-of-16 size constraint) — recognize this as a production-ready prompt, or as generic AI-image buzzwords stacked without format discipline? If it's the second, rebuild toward the locked grammar.

Specifically:
- Do NOT narrate the format choice inside the delivered prompt ("Format A because it has regions"). `skills/gpt-image-2-director/SKILL.md` line 156 is explicit: "Return only the finished prompt in a code block. No preamble, no explanation, no 'here's your prompt:', no format-choice justification."
- Do NOT hedge between JSON and prose to cover both bases. SKILL.md line 23's own rule: "If the concept fits multiple, pick the one best suited to the subject — don't hedge." A hedged prompt (half-JSON, half-vibes) is the single most common failure mode this skill exists to prevent.
- This model's specific texture is precision over atmosphere: "Specific over atmospheric... GPT Image 2.0 executes specificity better than it interprets mood" (SKILL.md, line 115). Padding a prompt with mood words ("moody, cinematic, professional") instead of named objects, positions, and counts is the tell of a generic diffusion-model prompt bolted onto a model that actually wants layout instructions.
- Photoreal faces are not the strength to lead with — text and layout are. Every face-bearing prompt should route away from "photorealistic" toward film/cinematic language (SKILL.md, line 119), the same discipline documented independently in `skills/fantastic-posters/genius.md` line 171, which flags garbled lettering — not faces — as this model's known weak spot to watch for instead.

---

## Anti-Patterns (Sourced)

- Requesting "photorealistic" for a face-heavy Format B prompt instead of film/cinematic framing — `skills/gpt-image-2-director/SKILL.md` line 119: "Avoid 'photorealistic' when faces are in frame... these bias toward a look GPT Image 2.0 actually nails, rather than triggering its plasticky-skin failure mode."
- Writing a rendered title or headline longer than roughly six words and expecting the model to hold every character — `skills/fantastic-posters/README.md` line 150 ("Settings" section): "GPT Image 2 is the strongest text-rendering model around — titles, billing blocks, masthead lockups all hold up. If a title runs more than ~6 words, expect typos; shorten and re-run."
- Writing an edit instruction that re-describes the entire scene instead of naming just the delta — `directives/fal-edit-mode-guide.md` line 105 (patterns harvested from `robonuggets/gpt-image-2-skill`, MIT, 2026-04-30): "The model's job is to find the delta. If you re-describe the whole scene, it treats the request as 'regenerate using these specs as a reference,' which produces a similar-but-different image rather than a surgical edit."
- Regenerating from scratch when only the on-image content should change and the layout should hold — `directives/fal-edit-mode-guide.md` line 22: "Rule of thumb: edit changes content; regenerate changes design."
- Supplying a JPEG for a masked-region edit instead of a PNG — `directives/fal-edit-mode-guide.md` line 78: "Common gotcha: a JPEG mask compresses gray values and softens edges → use PNG."
- Specifying an output size beyond a 3:1 aspect ratio or a dimension that isn't a multiple of 16 — `directives/fal-usage-policy.md` line 103 (2026): "GPT Image 2 supports up to 3840×2160 at ≤ 3:1 aspect, multiples of 16... Invalid sizes are rejected before the API call with a helpful error."
- Hedging between Format A (JSON) and Format B (prose) instead of committing to the one the subject demands — `skills/gpt-image-2-director/SKILL.md` line 23: "Pick one based on the user's concept. If the concept fits multiple, pick the one best suited to the subject — don't hedge."

---

## Verbatim Exemplars

> A cinematic, moody photograph of a young Asian woman looking back over her shoulder at the viewer on a rainy night in a bustling street. She has wet, stringy black hair plastered to her face and a melancholic expression, wearing a loose, oversized greyish-green jacket. The street is wet, reflecting the blurred, glowing neon signs and traffic lights of the city. Parked on the wet asphalt to her left is a white vintage Toyota Levin hatchback with its red taillights illuminated. On the top left side of the image, elegant vertical Japanese text reads "都会の夜に溶けていく" in a large serif font. — `skills/gpt-image-2-director/SKILL.md`, line 122 (the skill's own canonical Format B register example).

> "GPT Image 2 is the strongest text-rendering model around — titles, billing blocks, masthead lockups all hold up. If a title runs more than ~6 words, expect typos; shorten and re-run." — `skills/fantastic-posters/README.md`, line 150.

> "The model's job is to find the delta. If you re-describe the whole scene, it treats the request as 'regenerate using these specs as a reference,' which produces a similar-but-different image rather than a surgical edit." — `directives/fal-edit-mode-guide.md`, line 105 (source: `robonuggets/gpt-image-2-skill`, MIT, harvested 2026-04-30).

> "GPT Image 2 supports up to 3840×2160 at ≤ 3:1 aspect, multiples of 16." — `directives/fal-usage-policy.md`, line 103.

---

## Tool Facts (Grounding)

Real, confirmed facts about this model captured elsewhere in the repo (not this skill's own SKILL.md, which is internally authored prompt-engineering IP, not a copy of official OpenAI documentation): quality tiers run `low` (~$0.011/image, 10-15s), `medium` (~$0.04/image, 25-40s), `high` (~$0.17/image, 60-90s) per `skills/fantastic-posters/README.md` lines 142-146; default portrait size is 1024×1536 and the model "maxes out at 1536 on a side" for the default endpoint path (`skills/fantastic-posters/README.md`, line 148) while the newer size-preset path supports up to 3840×2160 at ≤3:1 aspect (`directives/fal-usage-policy.md`, line 103) — both are VERIFIED against real usage-policy text, and the gap between them (1536px ceiling vs. 3840px ceiling) is a genuine two-endpoint distinction, not a contradiction: `references/source-ledger.md` labels which is which. The Fal edit endpoint is named `openai/gpt-image-2/edit` (`directives/fal-edit-mode-guide.md`, line 6).

**Naming gap worth flagging (not silently resolved):** `skills/gpt-image-2-director/SKILL.md` calls this model "GPT Image 2.0" throughout (e.g., the title, line 6, line 17). The real-world sourced material in this repo — `directives/fal-usage-policy.md`, `directives/fal-edit-mode-guide.md`, `skills/fantastic-posters/README.md` and `genius.md` — all call the same Fal-hosted model "GPT Image 2" (no ".0"), with an API endpoint literally named `openai/gpt-image-2`. Both clearly describe the same model family (identical text-rendering strength claim, identical ~6-word title ceiling behavior), so this is treated as LIKELY the same product under two house spellings, not two different models — but no single source uses "GPT Image 2.0" verbatim, so the ".0" suffix itself is UNCONFIRMED. Flagged for the conductor rather than silently normalized (out of scope: SKILL.md content is untouched per additive-first).

---

## Source Ledger Pointer

Full claim-by-claim VERIFIED / LIKELY / UNCONFIRMED breakdown lives in `references/source-ledger.md` — 11 sources consulted for this repair pass (this skill's own 15,004-byte SKILL.md and three prompts-v2 files, plus four real usage-policy captures from `directives/` and `skills/fantastic-posters/` that document the same underlying model, and a negative-result check against `extractions/` for any dedicated GPT Image 2 source folder, confirmed absent by directory search) is logged there with file path, byte size (`wc -c`), and verification status.

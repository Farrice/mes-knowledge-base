# Source Ledger — gpt-image-2-director

Repair pass: Wave 3 Lane 4 Batch 6. This is a **tool skill** (a locked OpenAI GPT Image 2.0 prompt grammar), not a person extraction — "sources" means the skill's own locked SKILL.md plus real usage-policy documentation for the same model captured elsewhere in this repo, not a personality transcript. Every claim used in `genius.md` and `workflows/*.md` is labeled below. File sizes recorded via `wc -c` (bytes, not lines) to verify presence/absence honestly.

## Sources consulted

| # | Source | Path | Size (bytes, `wc -c`) | Role |
|---|---|---|---|---|
| 1 | The skill's own locked grammar | `skills/gpt-image-2-director/SKILL.md` | 15,004 | Primary ground truth — the three-format routing grammar (JSON / prose / meta-prompt) this repair cites |
| 2 | Skill's genius-tier pattern notes | `skills/gpt-image-2-director/references/genius-patterns.md` | 1,939 | Pre-existing pattern summary; read, not duplicated |
| 3 | Skill's hidden-knowledge notes | `skills/gpt-image-2-director/references/hidden-knowledge.md` | 542 | Pre-existing model-bias notes; read, not duplicated |
| 4 | Structure-pure v2 prompt (Format B) | `skills/gpt-image-2-director/references/prompts-v2/cinematic-prose-scene-prompt.md` | 6,672 | Already carries Output Contract + Quality Gate; used as house-style reference for new `workflows/` files |
| 5 | Structure-pure v2 prompt (Format C) | `skills/gpt-image-2-director/references/prompts-v2/meta-prompt-concept-poster.md` | 7,649 | Same role, Format C |
| 6 | Structure-pure v2 prompt (Format A) | `skills/gpt-image-2-director/references/prompts-v2/structured-json-layout-prompt.md` | 8,382 | Same role, Format A |
| 7 | Fal API usage policy (same model, production usage) | `directives/fal-usage-policy.md` | 10,807 | Real size/quality/pricing facts for GPT Image 2 as run in production in this repo |
| 8 | Fal edit-mode guide (same model, edit endpoint) | `directives/fal-edit-mode-guide.md` | 7,530 | Real edit-vs-regenerate rules, mask format, delta-only prompt pattern — sourced from `robonuggets/gpt-image-2-skill` (MIT), harvested 2026-04-30 |
| 9 | Fantastic Posters production README (same model) | `skills/fantastic-posters/README.md` | 8,637 | Real quality-tier pricing/timing, size ceiling, text-rendering behavior claim |
| 10 | Fantastic Posters genius.md (same model, cross-reference) | `skills/fantastic-posters/genius.md` | 17,868 | Independent confirmation of the ~6-word title / garbled-lettering failure mode |
| 11 | `extractions/` directory scan for a dedicated GPT Image 2 / OpenAI source folder | `extractions/` (`find`, maxdepth 1, `-iname "*gpt-image*" -o -iname "*openai*"`) | n/a — zero matches returned | Confirms no dedicated extraction exists for this specific model; ruled out by an actual directory search, not assumed |

## Claims, labeled

| Claim | Label | Anchor |
|---|---|---|
| "Avoid 'photorealistic' when faces are in frame... these bias toward a look GPT Image 2.0 actually nails, rather than triggering its plasticky-skin failure mode." | VERIFIED | `skills/gpt-image-2-director/SKILL.md`, line 119 (read verbatim) |
| "If the concept fits multiple, pick the one best suited to the subject — don't hedge." | VERIFIED | `skills/gpt-image-2-director/SKILL.md`, line 23 |
| "Return only the finished prompt in a code block. No preamble, no explanation... no format-choice justification." | VERIFIED | `skills/gpt-image-2-director/SKILL.md`, line 156 |
| "Specific over atmospheric... GPT Image 2.0 executes specificity better than it interprets mood." | VERIFIED | `skills/gpt-image-2-director/SKILL.md`, line 115 |
| Canonical Format B prose exemplar ("A cinematic, moody photograph of a young Asian woman...") | VERIFIED | `skills/gpt-image-2-director/SKILL.md`, line 122 |
| "GPT Image 2 is the strongest text-rendering model around... If a title runs more than ~6 words, expect typos; shorten and re-run." | VERIFIED | `skills/fantastic-posters/README.md`, line 150 |
| Quality tiers: `low` ~$0.011/image (10-15s), `medium` ~$0.04 (25-40s), `high` ~$0.17 (60-90s) | VERIFIED | `skills/fantastic-posters/README.md`, lines 142-146 |
| Default portrait size 1024×1536; model "maxes out at 1536 on a side" (default endpoint) | VERIFIED | `skills/fantastic-posters/README.md`, line 148 |
| "GPT Image 2 supports up to 3840×2160 at ≤ 3:1 aspect, multiples of 16... Invalid sizes are rejected before the API call." | VERIFIED | `directives/fal-usage-policy.md`, line 103 |
| Edit endpoint named `openai/gpt-image-2/edit`; "the strongest text-preserving image-edit model on Fal" | VERIFIED | `directives/fal-edit-mode-guide.md`, line 6 |
| "The model's job is to find the delta. If you re-describe the whole scene, it treats the request as 'regenerate using these specs as a reference,' which produces a similar-but-different image rather than a surgical edit." | VERIFIED | `directives/fal-edit-mode-guide.md`, line 105 |
| "Rule of thumb: edit changes content; regenerate changes design." | VERIFIED | `directives/fal-edit-mode-guide.md`, line 22 |
| "Common gotcha: a JPEG mask compresses gray values and softens edges → use PNG." | VERIFIED | `directives/fal-edit-mode-guide.md`, line 78 |
| Mask convention: white pixels = edit, black pixels = preserve | VERIFIED | `directives/fal-edit-mode-guide.md`, line 76 |
| Edit-mode patterns "harvested from `robonuggets/gpt-image-2-skill` (MIT)" into `generate.js`, dated 2026-04-30 | VERIFIED | `directives/fal-edit-mode-guide.md`, line 3 |
| Independent confirmation of the ~6-word title ceiling as a "known weak spot," fixed via masked re-render | VERIFIED | `skills/fantastic-posters/genius.md`, line 171 and line 203-205 |
| The skill's SKILL.md name "GPT Image 2.0" and the Fal-endpoint usage-policy name "GPT Image 2" (no ".0") refer to the same underlying model | LIKELY | Both describe identical behavior (best-in-class text rendering, ~6-word title ceiling, same failure mode) but no single source uses "GPT Image 2.0" verbatim outside this skill's own SKILL.md — cross-referenced across `SKILL.md`, `fal-usage-policy.md`, `fal-edit-mode-guide.md`, `fantastic-posters/README.md`; treated as the same model under two house spellings, not silently merged into one canonical name |
| The ".0" suffix in "GPT Image 2.0" is OpenAI's own official version label (as opposed to this skill's internal shorthand) | UNCONFIRMED | No source in this repo or `extractions/` documents an official OpenAI naming convention for this model; not resolved by this repair pass (out of scope — SKILL.md content untouched, additive-first) |
| A dedicated `extractions/` source folder exists for "GPT Image 2," "GPT Image 2.0," or "OpenAI" as a named source capture | UNCONFIRMED — verified absent | Directory search returned zero matches (see sources row 11); this is a checked absence, not an assumed one |
| This skill (`gpt-image-2-director`) is itself sourced from an official OpenAI internal document (as opposed to being internally authored prompt-engineering IP cross-checked against real production usage-policy captures) | UNCONFIRMED | No such internal OpenAI document exists in `extractions/` or `references/`; SKILL.md reads as originally authored, not a copy of an official artifact — treated as such throughout `genius.md` |

## What this ledger does NOT claim

This skill's locked three-format grammar (JSON layout / cinematic prose / auto-derive meta-prompt) is **not** asserted to be verbatim OpenAI product documentation — it is this repo's own prompt-engineering system for driving GPT Image 2.0, cross-checked against real usage-policy captures for the same model where overlap exists (pricing, size limits, edit-endpoint behavior, text-rendering ceiling). Anywhere this ledger cites SKILL.md as the anchor, the claim is "this is what the skill's own locked rule says," not "this is what OpenAI officially mandates."

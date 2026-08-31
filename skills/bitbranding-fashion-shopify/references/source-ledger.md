# BitBranding (Christian Pinyon) — Source Ledger

Claim-by-claim provenance for `skills/bitbranding-fashion-shopify/`. Ground truth now
has two bounded source packages:

1. `extractions/BitBranding/transcript.txt` — original collection-page source, a
   single-line raw transcript with no embedded metadata.
2. `extractions/video-context/fwv1l_kdW18/` — 2026-08-27 product-page source with
   metadata, native captions, 1,100 timestamped segments, ten manually reviewed
   screen-share frames, uncertainty report, and mastery extraction.

The second package expands the existing owner; it does not rewrite or weaken the
original collection-page provenance.

## PDP Expansion Verification (run 2026-08-30)

| Check | Result |
|---|---|
| Public video identity | `fwv1l_kdW18`, BitBranding, `I Rebuilt a Shopify Product Page Without a Developer or Page Builder`, 40:27, uploaded 2026-08-27 |
| Transcript evidence | Native YouTube captions captured; 1,100 parsed segments and 16,042 clean transcript words |
| Visual evidence | Ten retained and manually reviewed screen-share frames covering module architecture, dossier, questions, blueprint, connector, first-pass gaps, repair, editor result, and size chart |
| Intake proof | `execution/verify_video_context_source_package.py extractions/video-context/fwv1l_kdW18` |
| Existing-coverage decision | Expanded `bitbranding-fashion-shopify`; no new agent or parallel Shopify skill |

## PDP Claim Boundaries

| Claim or mechanic | Label | Basis |
|---|---|---|
| Eleven apparel PDP modules mapped to buyer objections | VERIFIED IN SOURCE | Spoken explanation plus retained module-stack frame around 05:04 |
| Customer/product/fit/return/voice/reference dossier before build | VERIFIED IN SOURCE | Spoken sequence and retained dossier/context frames around 13:31 and 16:24 |
| Ask questions before building and flag missing facts | VERIFIED IN SOURCE | Visible prompt and visible blueprint response around 20:32-22:39 |
| Use a uniquely named duplicated draft theme | VERIFIED IN SOURCE | Spoken workflow and Shopify connector/theme frames around 24:30-25:58 |
| First mutation still required a defect-led repair pass | VERIFIED IN SOURCE | Visible first-pass gaps and numbered repair prompt around 25:58-29:20 |
| Re-read current state before later mutations | VERIFIED IN SOURCE | Spoken warning about incremental uploads and stale state in the repair segment |
| Base page converted just under 1% | SOURCE-REPORTED | Creator statement; no analytics export or independent audit in the package |
| Connector availability and Shopify limitations remain current | UNCONFIRMED CURRENT | Demonstrated and described on 2026-08-27; temporally unstable and requires live verification |
| The rebuilt page improves conversion, revenue, or returns | UNTESTED | No post-launch experiment or business receipt supplied; source explicitly says the model cannot know conversion |
| Connector writes, app installation, or publication are authorized | NO PERMISSION | The extraction/build run is local only |

## Absence / Presence Verification (run 2026-07-17)

| Check | Method | Result |
|---|---|---|
| `extractions/` directory for this expert | `ls extractions/ \| grep -i bitbrand` | 1 hit: `extractions/BitBranding/` |
| Contents of that directory | `find extractions/BitBranding -type f` + `wc -c` | Exactly one file: `transcript.txt`, 55,127 bytes — non-empty, real content (opens with the Represent collection-page teardown) |
| No second source video/transcript exists | `ls extractions/BitBranding/` | Confirmed single file; SKILL.md's own "Genius Source" section already discloses this as a single-tutorial extraction — this repair does not contradict that disclosure |
| Transcript has embedded timestamps or upload date | Full-text scan for `\d{1,2}:\d{2}` and `20\d{2}` patterns | None found — the transcript is a plain speech-to-text dump with no timecodes and no metadata header; publish date is UNCONFIRMED |

## Claims

| Claim | Label | Basis |
|---|---|---|
| "Almost everything premium streetwear brands are doing can be rebuilt on a standard Shopify theme for free. No custom code, no expensive apps." (Core Thesis, genius.md:11) | VERIFIED | Near-verbatim compression of two adjacent lines confirmed in transcript: "It's not custom code. Almost everything they're doing can be rebuilt on a standard Shopify theme for free" and "No custom code, no expensive apps, nothing like that." Both substrings confirmed present via direct Python `in` check against the full file text this session. |
| "I rebuilt Represent's collection page from scratch" (anti-pattern 1 anchor) | VERIFIED | Exact substring confirmed present in `extractions/BitBranding/transcript.txt`. |
| "No custom code, no expensive apps, nothing like that" (anti-pattern 2 anchor) | VERIFIED | Exact substring confirmed present. |
| "hover effects, quick add, color swatches, how they make 127 products feel like something you can actually navigate" (anti-pattern 3 anchor) | VERIFIED | Exact substring confirmed present (a `[music]` transcription artifact sits between "navigate" and "through" in the source — the quote is truncated just before it to stay verbatim-clean). |
| "get rid of spacing in between products, get rid of spacing left and right on mobile, I would definitely do that" (anti-pattern 4 anchor) | VERIFIED | Exact substring confirmed present. |
| "we want to connect it with the dynamic source and connect the image" (anti-pattern 5 anchor) | VERIFIED (quote) / LIKELY (as anti-pattern) | The quote itself is verbatim-confirmed. The anti-pattern framing ("static imagery reused across all collections") is an inference from Christian's demonstrated preference for dynamic-source binding — he is never recorded explicitly condemning static hero reuse in this transcript. Labeled LIKELY in genius.md for that reason, not VERIFIED. |
| "I did try to do a couple things with the description to try to do the truncation, the read more read less" (anti-pattern 6 anchor) | VERIFIED | Exact substring confirmed present. |
| "one of the reasons why I love Horizon. It's like they do give you all these little little things that you can manipulate" (anti-pattern 7 anchor) | VERIFIED | Exact substring confirmed present. |
| "It's not custom code. Almost everything they're doing can be rebuilt on a standard Shopify theme for free" (anti-pattern 8 anchor) | VERIFIED | Exact substring confirmed present (note: transcript has a stutter, "It's It's not custom code" — quote uses the clean single "It's" as the citable form; the doubled word is a speech-to-text artifact, not a meaningful variant). |
| "maybe it was too much for for Sidekick to do" (Hidden Knowledge / Model Calibration section) | VERIFIED | Exact substring confirmed present (again a stutter artifact "for for" in source, kept as-is). |
| "Section → Collection heading → Image block → Dynamic source" lever-path notation (genius.md pattern 3) | UNCONFIRMED as a literal quote | This exact arrow-chain phrasing does not appear verbatim in the transcript; it is the pre-existing extraction's compressed notation for Christian's demonstrated click-path behavior (visible in the transcript as a sequence of editor actions, not a spoken sentence). Left as pre-existing content, not re-verified as a direct quote by this repair — flagged here rather than silently treated as verbatim. |
| Compare-at-price as the only Horizon badge trigger; 36 products-per-page max; Sidekick GREAT-for/FAILS-at split (Hidden Knowledge section) | LIKELY | These are pre-existing synthesized observations from the same transcript (confirmed the underlying topics — badges, product-per-page limits, Sidekick behavior — are all discussed in the source) but were not re-derived word-for-word by this repair. Not re-verified beyond topic-presence. |
| Christian Pinyon is co-founder of a Shopify-focused agency for clothing brands, based in Allen, TX ("BitBranding" per skill naming) | VERIFIED (self-introduction in source) | Transcript opens with a self-introduction naming the speaker and describing the agency and its focus; confirmed present in the source text. Skill files render the agency name as "BitBranding" (matching the skill ID); the transcript's own self-introduction audio-to-text renders it slightly differently — treated as a known transcription-vs-branding variance, not a new fact to verify externally. |
| The 4 `references/prompts-v2/*.md` execution prompts (Output Contract/Skeleton/Quality Gate) | VERIFIED (in-repo) | Pre-existing, unedited by this repair; workflow_contracts check already PASSED in the pre-repair audit (`audit-bitbranding-fashion-shopify.txt`) — not touched. |
| The 4 workflow files' procedural content | VERIFIED (in-repo) | Pre-existing, unedited by this repair (out of scope — only the 3 failing checks were touched: anti_patterns_sourced, recognition_test, source_ledger). |

## What This Repair Changed vs. Left Alone

- **Added** to `genius.md`: `## How to Use This Skill (Model Calibration)` section (new — no prior "Opus Calibration" or equivalent existed to upgrade in place) and source anchors on all 8 pre-existing Anti-Patterns list items (content of the 8 items themselves preserved verbatim; only the anchor citations are new).
- **Untouched**: `SKILL.md`, all 4 workflow files, all 4 `references/prompts-v2/*.md` files, and every pre-existing genius.md pattern/insight/exemplar/rubric row. Additive-only per the envelope's boundaries.
- **New file**: this `references/source-ledger.md`.

# Source Ledger — luke-iha-creative-strategy

Every claim/pattern in `genius.md` and `SKILL.md`, labeled by how well it is
grounded in a file that can be opened and checked. VERIFIED = a verbatim
quote was located in the cited file by direct grep/read during this repair
(2026-07-17). LIKELY = the claim is consistent with a real, readable source
but the exact wording was not re-verified verbatim in this pass (synthesized
report, not raw transcript, or a claim of secondary/summarized origin).
UNCONFIRMED = no source file could be located; treat as system-authored
until a transcript surfaces.

## Genius Patterns (genius.md §Genius Patterns)

| Claim | Label | Source | Size |
|---|---|---|---|
| The Nuclear VSL | VERIFIED | `extractions/luke-iha/video-2-creative-strategy/transcript.txt` — "what do I mean by a nuclear VSSL... essentially what it is is you make a custom VSSL for the job that you're applying to" | 37,021 bytes |
| The Over-Delivery Flywheel | LIKELY | `extractions/luke-iha/video-2-creative-strategy/extraction-report.md` (synthesized from same transcript; over-delivery language paraphrased, not re-verified as one verbatim block) | 8,409 bytes |
| The Reps Mindset | LIKELY | same extraction-report.md; "50 proposals" / volume framing paraphrased | 8,409 bytes |
| The Objection Annihilator | LIKELY | same extraction-report.md | 8,409 bytes |
| The Platform Leverage Ladder | VERIFIED | `extractions/luke-iha/video-2-creative-strategy/transcript.txt` — "You cannot complain about clients if you don't do this" + 7-step sequence confirmed present in raw transcript | 37,021 bytes |
| The Agency Ladder | LIKELY | `extractions/luke-iha/video-6-offer-cycling/extraction-report.md` — **no raw transcript file exists in this directory** (report only); claim is a synthesized summary, not a verbatim-checked quote | 8,762 bytes (report only) |
| Offer Heat Formula / Offer Cycling / 12 Types of Leverage | LIKELY | same `video-6-offer-cycling/extraction-report.md` — same no-raw-transcript caveat | 8,762 bytes |

## Hidden Knowledge (genius.md §Hidden Knowledge)

| Claim | Label | Source |
|---|---|---|
| Creative Strategy ≠ Copywriting | VERIFIED | `extractions/luke-iha/video-2-creative-strategy/transcript.txt` — line is a close paraphrase of the transcript's opening distinction between "how" and "what/who/why" |
| The Review Economy | LIKELY | `video-2-creative-strategy/extraction-report.md` — the "compound interest" framing is report language, not a located verbatim quote in the raw transcript |
| Portfolio Bootstrapping | VERIFIED | `extractions/luke-iha/video-2-creative-strategy/transcript.txt` — Nuclear VSL / spec-work passage confirmed in raw transcript |

## Anti-Patterns (new section added this repair — every item VERIFIED verbatim)

All 8 items in the new `## Anti-Patterns` section were checked with direct
`grep -o` against the cited file in this repair session; the quoted text is
copy-pasted from the grep match, not reconstructed from memory:

- Mechanism-First Hook — VERIFIED — `extractions/luke-iha-hooks/transcript.txt` (25,569 bytes)
- The Give-Away Hook — VERIFIED — `extractions/luke-iha-hooks/transcript.txt`
- Dribbling Instead of the Kill — VERIFIED — `extractions/luke-iha-hooks/transcript.txt`
- Skipping Profile/Portfolio Completion — VERIFIED — `extractions/luke-iha/video-2-creative-strategy/transcript.txt` (37,021 bytes)
- Calcifying Into Cheap Long-Term Gigs — VERIFIED — `extractions/luke-iha/video-2-creative-strategy/transcript.txt`
- Never Questioning Sacred Cows — VERIFIED — `extractions/luke-iha-hooks/transcript.txt`
- Adding Polish Instead of Subtracting the Block — VERIFIED — `extractions/luke-iha-insight-mastery/transcript.txt` (20,035 bytes)
- Generic "Here's My Work" Portfolio — LIKELY — cross-references genius.md's own pre-existing Anti-Exemplar (Hall of Fame Exemplars section), which was written before this repair without an inline citation; the underlying Nuclear VSL material it critiques is VERIFIED (see above), but the anti-exemplar prose itself is house-authored, not a Luke Iha quote.

## Seven-Layer Decision Stack cluster (genius.md §"Patterns from claude.ai export — Luke Iha conversations (2026-07-01)")

Covers: Seven-Layer Decision Stack, Test Economics, The Reverse Beat Map
(+ UMP Trigger), Character Casting, Micro-Lead Multiplication, and the three
2026-07 Hidden Knowledge insights (Diamond and the Bullseye, upstream review
order, AI expectation ratchet).

| Claim | Label | Notes |
|---|---|---|
| Diamond and the Bullseye | VERIFIED | Located and quote-matched in the archived claude.ai export conversation "Luke-1591 Word 'Mega Prompt' Automates Market Research" (`_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/c00a368c-3395-4a7f-8e07-05db430fdc40.md`, 76,759 bytes once extracted). Verbatim: "the diamond is all about Clarity... Clarity is King it will always be king you can never sacrifice Clarity." |
| Seven-Layer Decision Stack, Test Economics, Reverse Beat Map, UMP Trigger, Character Casting, Micro-Lead Multiplication, upstream review order, AI expectation ratchet | **UNCONFIRMED (this repair pass)** | genius.md attributes these to a second source — "6 Advanced Marketing Lessons $100MM Copywriters (Genesis certainty-call recording)" — that could not be located in this repair pass. The 332MB `_archive/claude-export-2026-07-01.tar.gz` was confirmed to exist and one conversation (the Mega Prompt file above) was extracted and read; the "6 Advanced Marketing Lessons" conversation was not found among the readily-indexed triage files and full-archive search was out of scope for this repair. This is a gap, not a fabrication claim — the prior skill author may have had direct access to a source this pass could not re-locate. Recommend a follow-up pass search the full tarball (`tar -tzf` lists 3,864 files) or the `.tmp/claude-export/normalized/` working set if regenerated. |

## Evolution Log entries (genius.md §Evolution Log)

| Entry | Label | Notes |
|---|---|---|
| 2026-04-09 Category Pattern Disruption Layer | N/A — not a Luke Iha claim | Internal Antigravity evolution-loop hypothesis/result log, not attributed to Luke Iha's own words. No external source anchor required or applicable. |
| 2026-07-01 Claude.ai Export Enrichment | LIKELY | Meta-log describing the enrichment pass itself; partially verified above (Diamond/Bullseye), partially UNCONFIRMED (Decision Stack cluster). |

## Files consulted this repair (with sizes, per envelope Rule 2)

```
extractions/luke-iha/transcript.txt                          32,648 bytes
extractions/luke-iha/extraction-report.md                      7,915 bytes
extractions/luke-iha/video-2-creative-strategy/transcript.txt 37,021 bytes
extractions/luke-iha/video-2-creative-strategy/extraction-report.md 8,409 bytes
extractions/luke-iha/video-6-offer-cycling/extraction-report.md 8,762 bytes (no transcript.txt in this dir)
extractions/luke-iha-hooks/transcript.txt                     25,569 bytes
extractions/luke-iha-insight-mastery/transcript.txt           20,035 bytes
extractions/luke-iha-client-acquisition/transcript.txt        20,329 bytes
extractions/luke-iha-creative-strategist/transcript.txt       32,648 bytes (byte-identical to extractions/luke-iha/transcript.txt — same source, duplicate copy)
extractions/luke-iha-avatar-machine/*.txt                     (11 files, checked for anti-pattern candidates; content is dating-niche avatar-building material, not creative-strategy craft — not used as source for this skill's claims)
skills/luke-iha-creative-strategy/references/genius-patterns.md 6,476 bytes (skill-internal duplicate of genius.md patterns, not an independent source)
skills/luke-iha-creative-strategy/references/hidden-knowledge.md 2,504 bytes (same — skill-internal duplicate)
_archive/claude-export-2026-07-01.tar.gz                     332,779,255 bytes (one conversation extracted and verified; full-archive search out of scope)
```

## Adil Amarsi Opportunity-Triage Delta (2026-08-04)

The in-place `profit-finder-opportunity-scan` expansion uses a bounded source delta at `references/source-delta-zX61pyC1vLM.md` rather than attributing Adil Amarsi's material to Luke Iha.

| Claim cluster | Label | Handling |
|---|---|---|
| Cosmetic variation versus strategic-variable change | `JOINT-SOURCE` | Matthew Volkwyn frames the same-hook/new-sentence failure at approximately 09:10–10:48; Adil's examples demonstrate the alternative |
| Product truth crossed with a neglected buyer situation | `SOURCE-VERIFIED` | Preserve the decision mechanic; keep the campaign result and health assertions outside the durable claim set |
| Adjacent identity or encounter surface | `SOURCE-VERIFIED` | Require overlap, native entry, permission, and reachability before selection |
| Language/geography as a market variable | `SOURCE-VERIFIED`; outcomes `ANECDOTAL` | Preserve the hypothesis lane; require demand, native evidence, rights, operations, and economics |
| `Profit Finder` strategist role | `SOURCE-VERIFIED` | Use as an ownership posture, never as profit proof |
| Evidence labels, whitespace scopes, hold states, rejection ledger, falsifier, and proof ladder | `ANTIGRAVITY OPERATIONAL SYNTHESIS` | Do not attribute these controls to Adil or Luke |

Local source receipts:

- Transcript: `extractions/adil-amarsi-creative-strategy/source/transcript.txt`, SHA-256 `d5db63c24f7bccdfab02c442cbc97fc12a17645b49a7440a6aed469bef43ad52`
- Captions: `extractions/adil-amarsi-creative-strategy/focused-visual-10m32/download/video.en-orig.vtt`, SHA-256 `d7bdfa1db86439a36adc502cccb0e140ab72562007b8c9b02393ff5eba0d0a60`
- Full claim classes and visual-capture boundary: `extractions/adil-amarsi-creative-strategy/source-ledger.md`

The source's health assertions, campaign outcomes, exit claim, story-result causality, foreign-market economics, and inconsistent practice benchmark remain quarantined as documented in the source delta.

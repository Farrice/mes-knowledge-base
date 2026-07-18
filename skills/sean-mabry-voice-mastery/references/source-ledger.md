# Source Ledger — Sean Mabry Voice Mastery

Claim-by-claim provenance audit, written 2026-07-18 during the Wave 3 Lane 4
heartbeat repair pass. Every substantive claim in `SKILL.md`, `genius.md`,
`references/hidden-knowledge.md`, `references/implementation.md`, and
`workflows/01-voice-dna-capture.md` is checked against the recoverable primary
source and labeled **VERIFIED** / **LIKELY** / **UNCONFIRMED**. Verbatim
quotes were confirmed by direct Python `in` substring search against the
source file — not memory, not inference.

## Sources Consulted

| Source | Location | Status |
|---|---|---|
| Sean Mabry interview transcript, Matt Giaro's copywriting channel (~60 min YouTube interview) | `extractions/sean-mabry/transcript.txt` — 97,575 bytes (confirmed via `wc -c`), ~18,827 words, single continuous text with `>>` speaker-turn markers, no timestamps | **Primary source, VERIFIED present, full text read** |
| MES extraction synthesis (Patterns, Hidden Knowledge, Methodology, Implementation Pathway) | `extractions/sean-mabry/extraction-report.md` — 15,848 bytes (confirmed via `wc -c`) | **Secondary source, VERIFIED present, full text read** — this is the extractor's structuring of the transcript, not an independent source |
| Both files added to the repo together | `git log --diff-filter=A -- extractions/sean-mabry/*` → 2026-03-15 | Used as the extraction date anchor for anti-pattern citations below |

No other Mabry source material exists in this repo. Checked `extractions/` for
any second Mabry file (none found) and confirmed via file-size read (not a
line-count proxy) that both files are substantial, fully-read text, not
empty/truncated stubs.

## Claim-by-Claim Ledger

### genius.md — Patterns 1-6 + Meta-Pattern

| Claim | Status | Anchor |
|---|---|---|
| Pattern 1 — Prediction Discipline (predict, don't just replicate; wrong predictions refine the model) | **VERIFIED** | transcript.txt — verbatim: "one of the most powerful exercises I learned was whenever possible try to predict how they would say something or what their take on a certain topic would be because effectively what you really need is a mental model" |
| Pattern 2 — Controversy Line Map (flag-plant / nuanced / no-go, three zones) | **VERIFIED** | transcript.txt — verbatim: "they know where their line is in terms of broaching controversy" and the "be polarizing... be abrasive" passage (~word 2,365); the three-zone naming itself (Flag-plant/Nuanced/No-go) is the extraction-report's own structuring of Mabry's looser description — **LIKELY** for the exact zone labels, **VERIFIED** for the underlying concept |
| Pattern 3 — Hidden Gem Collector (stories client tells casually, 2:1 target ratio) | **VERIFIED** for the concept; **LIKELY** for the specific "2:1" ratio | transcript.txt confirms the core behavior of mining podcast appearances for forgotten stories; extraction-report.md is where the "2:1, Their Picks vs. My Picks" framing and ratio are formalized — not a verbatim Mabry number |
| Pattern 4 — Authorship Pyramid (memoir for the base, tactical books second) | **VERIFIED** | transcript.txt — verbatim: "let me let me walk you through my pyramid theory of how authorship works" and "a lot of times people want to start with a book that's like super tactical... no fluff... the problem with that is it ignores the reality of what people are looking for" (~word 15,051) |
| Pattern 4 — Alex Hormozi and Dan Martell named as pyramid executors | **PARTIAL — Dan Martell VERIFIED, Hormozi UNCONFIRMED** | "Dan Martell" appears verbatim in transcript.txt (referenced live in the tactical-book passage). "Hormozi" does **not** appear anywhere in transcript.txt or extraction-report.md — the Hormozi reference in genius.md Pattern 4 and Hall of Fame Exemplar 1 is an editorial addition (Hormozi's "$100M Offers" is public-record knowledge, correctly described, but its use as a Mabry-endorsed example is not sourced to Mabry's own words). Flagged inline in genius.md's Exemplar 1 with a provenance note |
| Pattern 5 — Mode-Split Protocol (workhorse vs. deep work, Parkinson's Law, clock-forgotten) | **VERIFIED** | transcript.txt — the speed-drilling passage (~word 5,509) and surrounding day-type discussion are verbatim source material |
| Pattern 6 — Trust Ladder (3 stages, "no edits" milestone) | **VERIFIED** | transcript.txt — verbatim: "no edits" appears in the milestone passage ("the first one of the first times that I had an email come back with no edits, I was on cloud9"); stage progression (write→review→someone else publishes → you publish → no review) matches the "review process" passage (~word offset 20,398 region) |
| Meta-Pattern — Voice as the AI-Proof Moat | **VERIFIED** | transcript.txt — verbatim: "I think if you can write in voice, everything else is just a workflow" (opening lines of transcript) |

### genius.md — Anti-Patterns (Sourced), added this repair pass

All six items below were confirmed by direct substring search against
`extractions/sean-mabry/transcript.txt` at the time of writing. See genius.md
for the full quotes; this row records only the verification status.

| Claim | Status | Anchor |
|---|---|---|
| "Spin out" mistake — compressing speed too fast | **VERIFIED** | transcript.txt, ~word 5,509 — exact quote confirmed via substring match |
| 80%-delegation-standard anti-pattern | **VERIFIED** | transcript.txt, ~word 4,149 — exact quote confirmed via substring match |
| "Be polarizing" advice without a Controversy Line | **VERIFIED** | transcript.txt, ~word 2,365 — exact quote confirmed via substring match |
| "Crunchy tactical" no-fluff debut book | **VERIFIED** | transcript.txt, ~word 15,051 — exact quote confirmed via substring match |
| Template-pack-as-creative-substitute | **VERIFIED** | transcript.txt, ~word 12,079 — exact quote confirmed via substring match |
| "Handwrite sales letters" as the wrong voice exercise | **VERIFIED** | transcript.txt, ~word 3,308 — exact quote confirmed via substring match |

### genius.md — Hall of Fame Exemplars, Signature Moves, Rubric

| Claim | Status | Anchor |
|---|---|---|
| Exemplar 1 — "$100M Offers" Hormozi analysis | **UNCONFIRMED as a Mabry claim** (see Pattern 4 row above) | Not present in transcript.txt or extraction-report.md. Public-record accurate about the book itself, but the specific analytical framing is an editorial illustration, not a sourced Mabry statement. Provenance note added inline in genius.md |
| Exemplar 2 — "Controversy-Calibrated Response" | **N/A — self-labeled "(Reconstructed)"** | Explicitly marked as a reconstructed composite in the original text; not presented as a real client case. No change needed |
| Exemplar 3 — "Forgotten Gem Keynote" | **N/A — self-labeled "(Reconstructed)"** | Same as above |
| Anti-Exemplar — "Tactical-Only Debut Book" | **LIKELY** | Not a real book title; a composite illustration of the verified "crunchy tactical" anti-pattern above. Provenance note added inline in genius.md |
| Signature Moves (5 named moves) | **LIKELY** | Each move is a faithful restatement of a VERIFIED pattern above (Predictive Probe = Pattern 1, Boundary Map = Pattern 2, etc.); the specific move *names* ("The Predictive Probe," "The Kinesthetic Voice Imprint") are the extractor's naming convention, not Mabry's own terms |
| Expert-Specific Quality Rubric (7-criterion table) | **N/A — editorial synthesis** | A scoring rubric built by the extraction/skill-authoring process to operationalize the VERIFIED patterns above; not itself a Mabry claim, so not subject to VERIFIED/LIKELY/UNCONFIRMED labeling |

### references/hidden-knowledge.md

| Claim | Status | Anchor |
|---|---|---|
| Voice Sensitivity Spectrum (Bizop low / Fitness medium / B2B coaching very high) | **VERIFIED** | transcript.txt — verbatim: "Bisop" and "fitness" both present as niche examples; the "I want someone that's going to give you the knowledge I need, but in a way that vibes" line (opening of transcript) supports the high-sensitivity framing. The specific low/medium/very-high/extreme labels are the extractor's structuring |
| "No Edits" High-Water Mark, incl. "80% is good enough" Harvard delegation contrast | **VERIFIED** | transcript.txt — both the "no edits... cloud9" passage and the "Harvard delegation rule... 80% is good enough... I've never met anyone really who's willing to settle for 80%" passage are verbatim |
| Handwriting as Voice Calibration (not copy training) | **VERIFIED** | transcript.txt, ~word 3,308 — verbatim: "I didn't handwrite sales letters... I didn't really find handwriting helped me so much when I was learning the fundamentals of copyrightiting" followed by "it like really helped me with voice" |
| Book Proposal as Entity Channeling (Stephen King "archaeology," Michelangelo/David) | **VERIFIED concept; "entity channeling" is an extractor label** | transcript.txt — "spooky," "King," "Michelangelo," "archaeology," "marble," and "David" all present verbatim in the book-proposal discussion. The specific phrase "entity channeling" does not appear verbatim in the transcript — it is the extraction-report's own naming for the described phenomenon |
| Voice Writing IS the AI-Proof Moat | **VERIFIED** | transcript.txt — verbatim: "I think if you can write in voice, everything else is just a workflow" and "the courage to take creative chances... display your work" passage (~word offset 63,192 region) |

### references/implementation.md

| Claim | Status | Anchor |
|---|---|---|
| Phase 1-4 progression (Immersion → Prediction → Calibration → Mastery) | **LIKELY** | Directionally consistent with the transcript's description of onboarding, but the specific week/month boundaries (Week 1-2, Week 2-4, Month 2-3, Month 3+) are extraction-report.md's own timeline structuring, not stated as exact durations by Mabry in the transcript |
| "12-15 minute email drafts (down from 60-90 min)" (extraction-report.md, Phase 4 Mastery) | **LIKELY — rounded/extrapolated figure** | transcript.txt verbatim only supports "taking an hour to taking 15 minutes" (~word 5,509); the extraction-report's "60-90 min" and "12-15 minute" range is a plausible rounding but not an exact transcript quote. Treat the underlying claim (large time compression through incremental drilling) as VERIFIED and the specific minute-ranges as LIKELY |
| Authorship Pyramid diagram (0.01% / 0.1% / Top tier / Mid-tier / Base) | **LIKELY** | The core two-tier concept (base = dreamers, top = elite peers responding to influence) is VERIFIED in transcript.txt; the specific 5-level ASCII pyramid with percentage labels is implementation.md's own visualization, not a verbatim Mabry structure |
| Memoir vs. Biography table, incl. Walter Isaacson reference | **VERIFIED (Isaacson mention); LIKELY (table structure)** | transcript.txt — verbatim (transcript's own spelling): "if you know the author Walter Isacson like he he did a bunch of famous people. Elon Musk is probably the one he's most famous for." The memoir-vs-biography *distinction itself* is verbatim-sourced; the formatted comparison table is implementation.md's structuring |
| Hero's Journey Architecture — Dan Harmon's Story Circle, 8 steps, "dilemma" insight | **VERIFIED** | transcript.txt — verbatim: "Dan Harmon's story circle. So, Dan Harmon was a guy who created Community uh Rick and Morty... his writer rooms have always drilled on the story circle which is itself of just a simplified version of the hero's journey" |
| Deep Work / Workhorse day-type table (Free / Buffer / Deep Work days) | **LIKELY** | The workhorse/deep-work distinction and speed-drilling method are VERIFIED in transcript.txt; the specific "Free Day / Buffer Day / Deep Work Day" three-way naming and the sample weekly schedule template are implementation.md's own operationalization |

### SKILL.md

| Claim | Status | Anchor |
|---|---|---|
| Bio line: "10-year methodology spanning in-house copywriting, B2B thought leadership ghostwriting, and book-level voice work" | **VERIFIED** | transcript.txt — verbatim: "You've been in the game what, 10 years now?" / "10 years. Yeah." and the Bisop/fitness/B2B coaching niche history discussed throughout |
| 12 Deployable Capabilities (prompt titles + "Use When" descriptions) | **N/A — capability packaging, not a Mabry claim** | These are the skill-authoring layer's productization of the VERIFIED patterns above into named, deployable prompts. Not independently fact-checkable against the transcript; downstream of the patterns already ledgered |
| Integration Notes (pairs with Ghostwriting Voice Engine, Eric Roth, Fresh Voice System, Luke Iha) | **N/A — system cross-reference** | Internal routing claims about this repo's own skill roster, not claims about Mabry. Confirmed each named skill directory exists in `skills/` at time of writing |

### workflows/01-voice-dna-capture.md

| Claim | Status | Anchor |
|---|---|---|
| Phase 4 Cognitive Architecture — Argument Construction Pattern (6 named patterns) | **LIKELY** | The underlying insight (people have a default reasoning architecture, worth mapping) is consistent with Mabry's prediction-discipline framing in transcript.txt, but the 6 named patterns (Principle-First, Story-to-Lesson, etc.) are not verbatim Mabry terminology — they are this workflow's own operationalization, added 2026-04-09 per SKILL.md's Evolution note |
| Phase 4 Humor Deployment Logic + Vulnerability Architecture | **LIKELY** | Same status as above — extends Mabry's verified voice-capture discipline into a structured sub-framework not present verbatim in the source transcript |
| Output Schema (added this repair pass) | **N/A — structural addition, not a factual claim** | Directly derived from the workflow's own pre-existing Phase 6 Voice DNA Document Assembly list (9 numbered components); no new facts introduced, only a schema restatement for auditability |

## Labeling Key

- **VERIFIED**: Confirmed by direct substring search against a source file in this repo; verbatim or near-verbatim match found.
- **LIKELY**: The underlying concept is verified in the source, but a specific number, label, table, or naming convention is the extraction/skill-authoring layer's own structuring rather than a verbatim Mabry statement.
- **UNCONFIRMED**: No source file in this repo supports the claim after an actual search (not an assumption of absence). Usable as an editorial illustration but not citable as a sourced Mabry statement — flagged inline where it appears.

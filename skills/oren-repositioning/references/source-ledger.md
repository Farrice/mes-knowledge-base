# Oren Repositioning — Source Ledger

Claim-by-claim provenance audit. Labels: **VERIFIED** (quote/claim confirmed verbatim or near-verbatim in a cited source file) · **LIKELY** (consistent with a cited source but paraphrased/extrapolated beyond a direct match) · **UNCONFIRMED** (no source file in this repo contains the claim — kept per additive-only repair boundary, flagged here rather than silently anchored).

## Source Inventory (all files read this pass, with size — per ENVELOPE.md rule 2: no "no source exists" claim without a verified read + recorded size)

| File | Size (bytes, `wc -c`) | Relevance |
|---|---|---|
| `extractions/oren/extraction-report-repositioning.md` | 21,509 | **Primary ground truth.** The mastery-extraction report this skill was built from — Bad Bunny, Tyler the Creator, Charli XCX/Brat, Kanye, Stills, House of Errors, Boiler Room, Marty Supreme all originate here. |
| `extractions/oren/transcript.txt` | 29,376 | **Read in full — NOT the source for this skill.** This transcript is a *different* Oren video (~1,750-word "brand social media archetypes" talk: Oracle/Performer/World Builder/Catalyst/Helper archetypes, Ken Sakata, Blam Motorworks, Crease Furniture, etc.). It contains zero overlap with repositioning/counterpositioning content — no Bad Bunny, Tyler, Kanye, or Charli XCX. Confirmed by full read + grep. The raw transcript underlying `extraction-report-repositioning.md`'s ~18-min/3,809-word source video is **not present in this repo** — the extraction report is the only artifact of it we hold. |
| `extractions/oren/extraction-report.md` | 23,343 | Different Oren extraction (general marketing/systems) — checked for repositioning overlap, none found. |
| `extractions/oren/oren-systems-extraction-report.md` | 14,668 | Confirms `oren-repositioning` as the 3rd module of the Oren skill stack (taste-development / luxury-psychology / repositioning) — no new pattern content. |

**Implication for labeling**: because the raw transcript for the repositioning video isn't recoverable, "VERIFIED" below means *confirmed verbatim/near-verbatim inside `extraction-report-repositioning.md`* — one level removed from Oren's actual speech, not confirmed against a primary recording. This is the honest ceiling of confidence available from files in this repo.

---

## Genius Patterns (genius.md / references/genius-patterns.md)

| # | Pattern | Label | Anchor |
|---|---|---|---|
| 1 | Counterposition Against Aesthetic Category Codes | VERIFIED | extraction-report-repositioning.md, Pattern 1 (lines 26–30). Added quote "People can describe your brand without mentioning any competitor" is verbatim, line 30. |
| 2 | The 10-Year Vision Vector | LIKELY | extraction-report-repositioning.md, Pattern 2 (line 33) verifies "Bad Bunny's countercultural nail polish → Louis Vuitton couture collaboration" and "Tyler's pastels → Louis Vuitton creative direction." genius.md's phrasing "couture houses making their first menswear looks for reggaeton" is a paraphrase drift — "menswear" and "first...looks" are not in the source. Downgrade any client-facing use of that specific detail to LIKELY. |
| 3 | Creative Relationship as Atomic Unit | LIKELY | extraction-report-repositioning.md, Pattern 3 (line 39) verifies "Stills didn't just photograph Bad Bunny; their partnership became the creative engine." The added detail "went from tour photographer at 21" — the age **21** — does not appear anywhere in the source files. UNCONFIRMED as a standalone factual claim; do not present "21" as a verified fact about Stills in client-facing work. |
| 4 | Vision Extension Architecture | UNCONFIRMED (Rosalía example) | The Rosalía/high-fashion/religious-iconography sentence is **not present** in extraction-report-repositioning.md or any other source file. Kept in place per additive-only repair boundary; flagged here. Added quote "Fans describe the brand as a 'world' or 'vibe' rather than a product or person" is VERIFIED verbatim, extraction-report-repositioning.md line 48. |
| 5 | Cultural Authenticity as Scale Engine | VERIFIED | extraction-report-repositioning.md, Pattern 5 (line 51). "We don't go pop. Pop comes to us." is a verbatim quote, and BTS/Bad Bunny/Brat references are all present. |
| 6 | Guru Counter-Signaling | VERIFIED | extraction-report-repositioning.md, Pattern 6 (line 57). "House of Errors" and the "guru uniform" framing are verbatim. |
| 7 | Monoculture Penetration Strategy | VERIFIED | extraction-report-repositioning.md, Pattern 7 (line 63). "Boiler Room" verbatim. "Marty Supreme" verified separately at line 79 (Hidden Knowledge #1), correctly cross-applied here. |
| 8 | Elevation Through Artistic Collaboration (Kanye Pattern) | LIKELY / UNCONFIRMED (partial) | extraction-report-repositioning.md, Pattern 8 (line 69) verifies Kanye + **Murakami** + **George Condo**, and the exact quote "did both sides leave with more fame, recognition, and creative capability than they entered with?" (now added verbatim in the Application line). Two divergences from source: (a) source names a third collaborator as "Kashi" (likely a transcription artifact — no real Kanye collaborator by that name is documented; possibly a mis-hearing of "KAWS"), which genius.md silently replaced with **"Vanessa Beecroft"** — UNCONFIRMED, not in any source file. (b) "graduation bears" detail is UNCONFIRMED, not in source. |

## Hidden Knowledge (genius.md / references/hidden-knowledge.md)

| # | Item | Label | Anchor |
|---|---|---|---|
| 1 | The Sharability Prerequisite | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #1 (line 79). "Marty Supreme," "Brat," and the fan-generation test language are verbatim. |
| 2 | The Hunt for Vision | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #2 (line 84). "Charlie XCX" spelling matches the source exactly (source itself misspells "Charli XCX" as "Charlie XCX" — an upstream error, not introduced by this skill; noted, not corrected, per additive-only boundary). |
| 3 | The Squad Algorithm | LIKELY / UNCONFIRMED (partial) | extraction-report-repositioning.md, Hidden Knowledge #3 (line 88) verifies "algorithmic capital" and the added quote "a stable creative dyad generates compounding algorithmic distribution that a solo creator cannot access regardless of content quality" (now verbatim in the section). The named duos **"TJR/Brez, Hermozi/Robbins"** are UNCONFIRMED — not present in any source file, added as illustrative specificity. |
| 4 | Position Against Yourself | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #4 (line 94). "Odd Future darkness → Golf pastels" verbatim. |
| 5 | The Presentation-as-Proof Pattern | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #5 (line 99). "The sales material must itself be the proof of the capability being sold" is verbatim (now also quoted in the Hidden Knowledge section intro). |
| 6 | Load-Bearing vs. Decorative Codes | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #6 (lines 104–106). Now quoted verbatim in the new Anti-Patterns section. |
| 7 | The Uncomfortably Authentic Test | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #7 (lines 109–111). "Bad Bunny in drag," "Kendrick's beef escalation," and the discomfort-test quote are verbatim. |

## Hall of Fame Exemplars + Anti-Exemplar (genius.md only)

| Item | Label | Anchor |
|---|---|---|
| Bad Bunny's Gender-Fluid Reggaeton | UNCONFIRMED (detail level) | Core claim (reggaeton, English-crossover refusal) is VERIFIED via Pattern 5/1. The specific visual details — "nail polish, skirts, and pink hoodies" — are not in any source file (source only says "countercultural nail polish" once, in the Pattern 2 vision-vector context, not tied to skirts/hoodies). Treat as a plausible but unverified elaboration; do not present as a sourced quote. |
| Tyler, The Creator's Pastel Pivot | VERIFIED | extraction-report-repositioning.md, Hidden Knowledge #4 (line 94). "Odd Future darkness → Golf pastels" and the Louis Vuitton creative-direction destination are both verbatim/near-verbatim. |
| Charli XCX's "Brat" Monoculture Saturation | LIKELY | Brat's green + sharability language is VERIFIED (Hidden Knowledge #1). The specific "monoculture moment" framing applied to Brat by name is a reasonable synthesis of Pattern 7 (Boiler Room) + Hidden Knowledge #1, not a direct quote about Brat's rollout mechanics. |
| Anti-Exemplar: "Generic Influencer" Rebrand | UNCONFIRMED (constructed) | This composite example does not appear in any source file — it is a synthesized illustration built from the inverse of Patterns 1/2/4/5, consistent with the framework but not a real case Oren cited. Fine as a teaching device; do not present as a real brand example. |

## Anti-Patterns (new section, genius.md)

All 6 items VERIFIED — each quote checked verbatim against `extractions/oren/extraction-report-repositioning.md` at the cited line during this repair pass (see anchors on each list item in genius.md).

## Signature Moves / Expert-Specific Quality Rubric (genius.md)

LIKELY — both are derivative synthesis (not direct quotes) constructed from the Genius Patterns and Hidden Knowledge above. Internally consistent with VERIFIED source material; not independently sourced line items.

---

## Repair-Pass Summary

- 6/6 Anti-Patterns items carry a verbatim, verified quote + file+line anchor.
- 5 previously zero-entity genius.md sections (Pattern 1, Pattern 4, Pattern 8, Hidden Knowledge intro, Hidden Knowledge #3) now carry a verified verbatim quote each.
- 4 pre-existing UNCONFIRMED elaborations were identified and documented here (Rosalía example, Stills' age "21," Vanessa Beecroft replacing "Kashi," TJR/Brez + Hermozi/Robbins, "graduation bears," Bad Bunny "skirts"/"pink hoodies" detail) rather than silently anchored or deleted — additive-only boundary preserved, honesty preserved.

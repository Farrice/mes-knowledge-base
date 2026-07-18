# Source Ledger — Kieran Flanagan Audience Intelligence

Claim-by-claim source audit for `skills/kieran-flanagan-audience-intelligence/`. VERIFIED = quote/claim re-checked verbatim against a source file read in full during this repair pass. LIKELY = consistent with the extraction author's stated method or a verified adjacent claim, not independently re-checkable as a Kieran quote in this repo. UNCONFIRMED = no source file locates the specific figure or list as Kieran's own words; expert-plausible but unproven, or self-labeled "reconstructed" by the skill's own text.

## Sources Consulted (file + size, read in full this pass)

| Source | Path | Size (wc -c) | Status |
|---|---|---|---|
| Raw transcript, "I Built an AI Team That Creates All My Content" | `extractions/kieran-flanagan/transcript.txt` | 27,523 bytes | VERIFIED — primary source, read in full |
| MES extraction report (distilled from transcript) | `extractions/kieran-flanagan/extraction-report.md` | 14,945 bytes | VERIFIED as a synthesis document, read in full — its "Executable Behavior" steps and numeric figures are the extraction author's structuring, not always verbatim Kieran quotes (see per-claim notes below) |
| Second-brain extraction (different video, adjacent domain) | `extractions/kieran-flanagan-second-brain/extraction-notes.md` | 19,570 bytes | VERIFIED as read; NOT used to source this skill's patterns — it covers a separate video ("If You Use AI for Work, You Need a Second Brain," 2026-07-16) already routed to `simon-intellectual-library-os` and `liam-mley-ai-brain-builder` per its own "Where it landed" section. Consulted only to confirm it does not overlap this skill's claims. |

## Correction to extraction-report.md metadata
`extraction-report.md` line 4 labels the source "(Transcript, Greg Isenberg Show)." The transcript itself self-identifies the show by name four separate times ("this episode of Marketing Against the Grain," "a future episode of Marketing Against the Green" [sic]) — Kieran's own show, not Greg Isenberg's. Treating the "Greg Isenberg Show" attribution as **UNCONFIRMED/likely mislabeled**; the correct show name per the primary source is *Marketing Against the Grain*. No exact publish date or video URL is recorded in either source file — **UNCONFIRMED** for date/URL specifically (searched `extractions/kieran-flanagan/` in full via `find`; only `transcript.txt` and `extraction-report.md` exist, no metadata JSON).

## Claim-by-claim

### Pattern 1 — Content-Reactive Audience Profiling
- **VERIFIED** — Core method (build from what already resonates, not demographics/surveys) — transcript.txt: "Uh, this is not like an ICP, right? This is actually content they react to and it's all based upon research and engagement data." Also: "it's created audience identity, jobs to be done, the kind of pain points."
- **VERIFIED** — "It took me 12 months to kind of go back and forth" (iterative refinement) — transcript.txt, direct quote.
- **LIKELY** — "85%+ accuracy" success-metric figure and the specific "10-20 best-performing pieces" collection range — these are extraction-report.md's synthesized "Executable Behavior"/"Success Metric" framing (extraction-report.md Pattern 1), not a number Kieran states in the transcript. Consistent with the verified method, not independently confirmable as his stated threshold.

### Pattern 2 — Platform-Specific Style Card Architecture
- **VERIFIED** — Per-platform style cards, vocabulary library, "do and don't say," emotional register, validation hooks — transcript.txt: "the vocabulary library I find really good where you can say what they do and don't say all the kind of the way they speak, the emotional register and like validation hooks." Also: "if I was doing this, I would do a writing style per platform, right? That's how I would think about it."
- **VERIFIED** — Platform data-quality gap (LinkedIn undersampled because Firecrawl can't scrape it well, requires manual export) — transcript.txt, direct quote, also used as an Anti-Pattern anchor below.

### Pattern 3 — The 80/20 Anti-Vocabulary Principle
- **LIKELY** — The general "avoid list is a more powerful constraint than a use list" concept — supported by the verified "do and don't say" transcript quote (Pattern 2) and by Pattern 5's negative-space concept, both genuinely Kieran's framing.
- **UNCONFIRMED** — The specific numbers ("~20-30 words" USE list, "~50-100 words" NEVER-USE list, "80% of AI slop... 20% of the effort," "<30% human editing vs. 60-80%") and the "4x more effective" multiplier — none of these figures appear in `transcript.txt`. They originate in `extraction-report.md`'s Pattern 3 / Hidden Knowledge sections as the extraction author's synthesized estimates, not quoted or paraphrased from Kieran's own words. Labeled UNCONFIRMED rather than removed (additive-first mandate); flagging here so no downstream user treats these as Kieran-stated statistics.
- **UNCONFIRMED** — "Common Anti-Vocabulary Items" list ("delve," "tapestry," "landscape," "in the realm of," "leverage," "game-changer," "unlock," "embark," "navigate," "fostering," "holistic," "synergy," "cutting-edge") — searched `transcript.txt` for every one of these terms; zero matches. This is generic illustrative AI-slop vocabulary, not a list Kieran names in the source. Left in place per additive-first (it is a plausible, widely-recognized example set for the *concept* he does state), but it is not attributable to Kieran as a direct quote or named list.

### Pattern 4 — The Platform Isolation Rule
- **VERIFIED** — Core concept, in his own words about building per-platform styles — see Pattern 2 verified quote above (same transcript passage covers both patterns).
- **LIKELY** — "<30% shared structural rules" success-metric figure — extraction-report.md synthesis, not a Kieran-stated number.

### Pattern 5 — Style Cards Require Negative Space
- **VERIFIED** — Underlying concept ("what they do and don't say") — same transcript quote as Pattern 2.
- **LIKELY** — The specific "40-60%" allocation figure — extraction-report.md's Hidden Knowledge synthesis ("Style Cards Require Negative Space" section), not a number spoken in the transcript.

### Hidden Knowledge 1-5
- **VERIFIED** — #1 Content-reactive vs. persona-based — same transcript quote as Pattern 1.
- **UNCONFIRMED** — #2 "4x the work" / "50-word list eliminates more than a 200-word list" — same gap as Pattern 3 above; not in transcript.
- **VERIFIED** — #3 Performance Threshold Filtering, Top 30% — transcript.txt: "it will look at the top 30% of your best performing posts because it wants to extract winning patterns from the best performing posts."
- **VERIFIED** — #4 Messy Data → Clean Profile — transcript.txt: "I would upload that messy file to this skill" and "from that messy data that you have given it, it creates that profile."
- **LIKELY** — #5 Identity Vocabulary Mapping (three-tier Identity/Style/Topic words) — not stated as a named three-tier taxonomy in the transcript; extraction-report.md and genius.md's own synthesis of the "vocabulary library... do and don't say" quote plus general audience-profile framing. Plausible extension of verified material, not a verbatim Kieran taxonomy.

### Hall of Fame Exemplars 1 & 2, Anti-Exemplar
- **UNCONFIRMED as literal Kieran-authored text** — genius.md's own text labels these "(Reconstructed)." They are illustrative worked examples built by the extraction/skill-authoring process to demonstrate the patterns, not verbatim posts Kieran published or read aloud in the transcript. The underlying techniques they illustrate (Patterns 1, 2, 5) are VERIFIED; the specific post copy is not.

### Anti-Patterns (new section added this repair pass)
All seven items anchor to direct quotes found verbatim in `extractions/kieran-flanagan/transcript.txt` during this pass — each marked **VERIFIED**:
- "first draft when you look at this, I do not use this to post content"
- "So obviously I would never ship this"
- "This one sucked. It was my worst performing post. People did not like a product position"
- "I was never a big fan of the kind of vibe marketing where it was workflow tools because it's not vibing. You have to actually drag and drop all the workflows together. This is not software"
- "Firecrawl doesn't have a great time getting LinkedIn posts so it has a lot of substack... you could just have to go and like export your own files to upload"
- "too many people will use these cut and paste. That's not how you do that, right?"
- "this is not like an ICP, right? This is actually content they react to"

All confirmed present via direct `grep` against the source file during this pass (single-line transcript file, no internal line breaks — cited as "transcript.txt" without a line number since the entire file is one physical line).

## Gap named honestly
The primary weakness in this skill's provenance is Pattern 3 (Anti-Vocabulary) and its Hidden Knowledge companion: the specific numbers and the illustrative banned-word list are not Kieran's own words, only the extraction author's synthesis layered on top of a verified underlying concept ("do and don't say" vocabulary libraries with negative space). This repair pass did not delete that content (additive-first mandate) — it is flagged UNCONFIRMED above so a future pass can either find a second source that confirms the figures or rewrite Pattern 3 to drop the specific numbers and keep only the verified concept.

# Source Ledger — Authority Hacker: AI Social Media Mastery

Claim-by-claim provenance for SKILL.md, genius.md, and references/. Labels: **VERIFIED** (verbatim or paraphrase-faithful match confirmed in a source file, file + location cited), **LIKELY** (consistent with the source's stated methodology but not a direct quote), **UNCONFIRMED** (no source file substantiates it — flagged, not deleted).

Ground-truth sources for this skill (confirmed present, real byte counts checked with `wc -c`, not `wc -l`, 2026-07-17):
- `extractions/ai-social-media-panel/transcript.txt` — 68,471 bytes, raw single-block transcript of the Authority Hacker podcast episode (Gael Breton & Mark Webster).
- `extractions/ai-social-media-panel/extraction-report.md` — 19,597 bytes, MES 3.0 extraction report derived from the transcript (Genius Patterns 1-12, Hidden Knowledge 1-8, Methodology, Applied Intelligence).

No `extractions/` directory exists under an "authority-hacker" or "gael-breton" surname — this podcast was extracted under the topical folder `ai-social-media-panel`, not the expert's name. Confirmed by directory listing (`ls extractions/` — 193 entries, none matching `authority|hacker|breton|webster` except this folder) before concluding the source location.

## Genius Patterns (genius.md, 12 patterns)

| # | Pattern | Label | Basis |
|---|---------|-------|-------|
| 1 | Emotion-First Content Architecture | VERIFIED | extraction-report.md Genius Pattern 1; transcript discusses emotional-reaction framing throughout (e.g., the "keyword research vs. storytelling" passage). |
| 2 | Duality Engineering | VERIFIED | extraction-report.md Genius Pattern 2, incl. the "OpenClaw obsolete" hook example. |
| 3 | Attention Economy Transaction Model | LIKELY | extraction-report.md Genius Pattern 3 — a synthesized frame (extractor's naming) built on the source's emphasis on earned attention; not a term Breton uses verbatim in the transcript. |
| 4 | The Authenticity Ratio | VERIFIED | extraction-report.md Genius Pattern 4; corroborated by transcript's "operation kill the bots" / reach-decay discussion. |
| 5 | Niche Emotional Targeting | LIKELY | extraction-report.md Genius Pattern 5 — synthesized from the transcript's discussion of writing for people who "feel strongly," not a named framework in the source. |
| 6 | Self-Improving Content System | VERIFIED | extraction-report.md Genius Pattern 6 + Hidden Knowledge #3; transcript describes the weekly scrape/learn loop directly (the "what doesn't work" analysis passage). |
| 7 | Sub-Agent Content Isolation | VERIFIED | extraction-report.md Genius Pattern 7 + Hidden Knowledge #5. |
| 8 | Imperfection Engineering | VERIFIED | transcript.txt verbatim: "I almost have it introduce clunky language sometimes" / "you don't want to sound like AI." |
| 9 | Customer Roleplay for Ad Angles | VERIFIED | extraction-report.md Genius Pattern 9 + Methodology "Phase 1: Customer Roleplay." |
| 10 | Template-Based Visual Generation | VERIFIED | extraction-report.md Genius Pattern 10, incl. the $0.17/image Nano Banana Pro figure, corroborated in transcript ("they cost they cost 17 cents per image"). |
| 11 | Hook-Dominance Hierarchy | VERIFIED | extraction-report.md Genius Pattern 11. |
| 12 | Three-Angle Draft System | VERIFIED | extraction-report.md Genius Pattern 12. |

## Hidden Knowledge (genius.md, 8 items)

All eight items are **VERIFIED** — direct paraphrase-faithful lift from `extraction-report.md` "Hidden Knowledge" section (items 1-8), which itself distills specific transcript passages (e.g., the "no correlation between traffic and revenue" claim, the "$2.50 ad agency" cost figure, the "operation kill the bots" API restriction).

## Anti-Patterns (genius.md, new section, 6 items)

| Item | Label | Basis |
|------|-------|-------|
| Auto-Reply Bot Spam | VERIFIED | transcript.txt verbatim quotes: "they auto reply on threads, complete useless stuff as well," "It's like this is an automated reply. It just repeats what I said in the post and say, 'Oh my god, this is great.'," "restricted in the API... start like 50k a month." |
| Generic "How-To" / Listicle Posts | VERIFIED | extraction-report.md Hidden Knowledge #1 verbatim: "AI chatbots give better answers than any social media post could... A shitty social media post teaching something is inferior to typing the same question into ChatGPT." |
| All-Polish, Zero-Roughness AI Output | VERIFIED | transcript.txt verbatim: "I almost have it introduce clunky language sometimes" / "you don't want to sound like AI." |
| Chasing Traffic Instead of Revenue | VERIFIED | extraction-report.md Hidden Knowledge #2 verbatim: "Authority Hacker generated hundreds of thousands of leads per month and found no correlation between traffic and revenue." |
| Batch-Generating Multiple Posts in One Chat Thread | VERIFIED | extraction-report.md Hidden Knowledge #5 verbatim: "When Claude Code (or any LLM) writes multiple posts in one conversation thread, they converge in tone, structure, and length." |
| Posting Mediocre Content Just to "Stay Consistent" | VERIFIED | transcript.txt verbatim: "there was no value added wasn't that good"; extraction-report.md Hidden Knowledge #4 verbatim: "If you publish low-quality AI posts that get low engagement, your next high-quality post gets suppressed... every bad post doesn't just underperform — it damages your future reach." |

## Hall of Fame Exemplars / Anti-Exemplar (genius.md, pre-existing)

**UNCONFIRMED** — the two "excellent" exemplar posts (organic post + Meta ad) and the "Generic How-To" anti-exemplar are illustrative composites written to demonstrate the patterns, not verbatim posts pulled from Breton's or Webster's actual feeds. Not present in transcript.txt or extraction-report.md as direct quotes. Kept as pedagogical illustrations per the skill's existing structure — flagged here rather than deleted, since the calling checks (`verbatim_exemplars`) treat them as structural exemplars, not factual claims about a real post's performance.

## Pattern 13: Momentum Sequencing (genius.md, dated 2026-04-09)

**LIKELY** — an in-system evolution-log addition (see genius.md Evolution Log, 2026-04-09 entry), not sourced to the original transcript or extraction report. It is a downstream synthesis built from Patterns 6 and 7, not a claim about what Breton/Webster themselves do. Labeled here for completeness; no action needed since it already discloses its own evolution provenance in-file.

## Model Calibration Section (genius.md, new)

**VERIFIED** (quoted lines) + **LIKELY** (synthesized framing). The two direct quotes ("I almost have it introduce clunky language sometimes," "you don't want to sound like AI") are verbatim from transcript.txt. The "$0.17-per-image" and "122K views, 6K saves" figures are verbatim from extraction-report.md (Executive Summary, Genius Pattern 10). The framing sentence around "3-5 patterns per post" and "over-engineered, template-y feel" is the repair worker's synthesized calibration guidance (standard practice for this section type per `skills/ben-watkins-storytelling/genius.md` lines 7-16), not a direct claim attributed to Breton or Webster — labeled LIKELY/editorial, not a factual assertion requiring source verification.

## Workflow files, references/prompts*, SKILL.md

Not modified in this repair pass — all three workflow_contracts, verbatim_exemplars, and named_entity_floor checks already passed prior to this repair. No new claims introduced there.

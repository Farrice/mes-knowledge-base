# Source Ledger — Michael Bernoff Identity Engineering

Every claim of Michael Bernoff's actual words or teaching in this skill traces to one of the sources below. Labels: **VERIFIED** (verbatim quote confirmed by direct string search against the source file), **LIKELY** (secondary/derivative synthesis — an AI-generated extraction report describing the source, not a raw transcript of Bernoff's own speech), **UNCONFIRMED** (no located source; flagged rather than invented).

## Primary Sources — sizes recorded via `wc -c`, 2026-07-18

| Source | Path | Bytes | Content | Status |
|---|---|---|---|---|
| "This Mental Shift Will Finally Break You Out of Average" — Part 1 | `knowledge/extractions/inbox/Claude-💡💰💎 Michael Bernoff ! This Mental Shift Will Finally Break You Out of Average.md` | 432,060 | Claude.ai chat export (session created 1/18/2026 7:54 AM, exported 1/20/2026). Contains an MES 3.0 extraction run against "a YouTube Interview Transcript, ~55 minutes" of Michael Bernoff (Content Assessment, line 78-86: "Expert: Michael Bernoff - Founder of Human Interaction Technology (HIT), Author of 'Average Sucks'"). The raw underlying YouTube transcript itself is NOT present on disk as a separate file — this document is Claude's extraction/synthesis of it (Genius Patterns, Hidden Knowledge, Crown Jewel practitioner prompts with worked examples). Confirmed non-empty and substantial by direct `wc -c` (432,060 bytes), not assumed. | LIKELY — this is a derivative AI extraction of a transcript, not the raw transcript itself. All quotes cited below were confirmed present in THIS file by exact line-number grep, so they are verbatim-to-this-document; whether every phrase is Bernoff's own unedited words versus the extracting model's paraphrase of his teaching cannot be confirmed further without the original video. |
| "This Mental Shift Will Finally Break You Out of Average" — Part 2 | `knowledge/extractions/inbox/Claude-💡💰💎 Michael Bernoff ! This Mental Shift Will Finally Break You Out of Average pt.2.md` | 471,091 | Continuation of the same extraction session (created 1/18/2026 9:55 AM). Additional Crown Jewel prompts (Objection Prevention, Identity-Based Offer Design) and content-system prompts. Confirmed non-empty by `wc -c` (471,091 bytes). | LIKELY — same status as Part 1; read for this repair, no anti-pattern quotes from this file were used in the final six (all six landed in Part 1), but it was checked (see Notes below). |

## Per-Claim Ledger (new content added in this repair, 2026-07-18)

| Claim / Anti-Pattern | Location | Status | Anchor |
|---|---|---|---|
| AN-1 "Never mirror obviously. Never use their name excessively. Never fake rapport. Be genuinely interested but not approval-seeking." | genius.md, Anti-Patterns | VERIFIED | Exact string match, Part 1, line 256 |
| AN-2 "'Sorry' is submissive. 'Forgive me' is a request from an equal." | genius.md, Anti-Patterns | VERIFIED | Exact string match, Part 1, line 303 |
| AN-3 "Never say 'Good job.'" + "'Good job' says: 'You did something surprising. I'm validating you from above.'" | genius.md, Anti-Patterns | VERIFIED | Exact string match, Part 1, lines 179 and 7648 |
| AN-4 "When salespeople encounter A-types, their instinct is to become deferential, answer every question, accommodate every demand. This is exactly wrong. The A-type reads submission as weakness. They lose respect. They commoditize you." | genius.md, Anti-Patterns | VERIFIED | Exact string match, Part 1, line 1126 |
| AN-5 "When an analytical says 'I need more data,' most salespeople hear 'objection.'" | genius.md, Anti-Patterns | VERIFIED | Exact string match, Part 1, line 2365 |
| AN-6 "Too weak and it's just flattery that feeds the Wounded Child; too strong and it feels disconnected from reality." | genius.md, Anti-Patterns | VERIFIED | Exact string match, Part 1, line 1669 |
| "How to Use This Skill (Model Calibration)" section | genius.md, top of file | N/A (new original guidance, not a Bernoff quote) | Written against this skill's own existing patterns (3-beat pause, status raising, Reset Frame, Wrong Question) already present in genius.md before this repair; not attributed to Bernoff as a direct quote |
| Recognition-test phrasing ("would Michael Bernoff recognize this as...") | genius.md, Model Calibration + Anti-Patterns intro | N/A (new original content) | Original phrasing per this batch's instruction, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 structurally, written fresh against Bernoff's own patterns — not a Bernoff quote |

## Pre-Existing Content (Not Modified This Repair)

The 14 Genius Patterns, Hidden Knowledge items, Hall of Fame Exemplars, and Signature Moves in `genius.md` were already present before this repair and were not re-verified against source in this pass (out of scope — the three failing heartbeat checks were `anti_patterns_sourced`, `recognition_test`, and `source_ledger` only; `verbatim_exemplars` and `named_entity_floor` were already passing). They appear consistent with the same two source files (e.g., Pattern 3 "Wrong Question" matches Part 1 lines 165-168; Pattern 9 "Analytical Respect Frame" matches Part 1 line 2365, the same passage AN-5 draws its anti-pattern framing from) but were not individually re-anchored here.

## Notes on This Repair (2026-07-18)

- Both source files are Claude.ai extraction-session exports (dated 1/18/2026, exported 1/20/2026), not raw video transcripts. This was verified directly — `ls extractions/ | grep -i bernoff` returns nothing; the only Bernoff source material on disk lives under `knowledge/extractions/inbox/` (confirmed via `find . -iname "*bernoff*"`) and consists of these two chat exports plus downstream research/agent artifacts (`agents/michael-bernoff/`, `research_outputs/`) that are themselves derivative of these two files, not independent primary sources.
- No raw YouTube transcript or timestamped source for the underlying "~55 minute interview" exists on disk under this repo — checked directly (file listing, `wc -c` on both candidate files) rather than assumed, per this batch's Rule 2 (a claim of absence is itself a provenance claim).
- All six anti-pattern quotes above were located by direct `grep -n` line-number search against Part 1 and confirmed as exact substrings before being cited — none were reconstructed from memory or paraphrase.
- No anti-pattern quote required use of Part 2; it was searched (`grep` for "most salespeople", "never say", "don't do", etc.) but did not surface material distinct enough to add beyond the six already sourced from Part 1.
- Labeled LIKELY rather than VERIFIED at the source-file level because these documents are themselves AI extractions of a transcript, not the transcript — the quotes are verbatim-to-this-document (confirmed) but one level removed from Bernoff's raw spoken words (unconfirmed, no primary transcript present to check against).

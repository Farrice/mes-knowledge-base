# Source Ledger — nick-saraev-bottleneck-thinking

Claim-by-claim provenance for `genius.md`. Every claim is labeled **VERIFIED** (verbatim in a source file, quote confirmed by direct read/grep), **LIKELY** (faithful synthesis of a real source, not a verbatim quote), or **UNCONFIRMED** (no source file located for this repair — flagged, not deleted, per additive-first boundary).

## Sources consulted

| File | Size (bytes, `wc -c`) | Role |
|---|---|---|
| `extractions/nick-saraev-bottleneck-thinking/transcript.txt` | 13,589 | Primary source — full transcript of the "Picture your business like this" pipeline/bottleneck YouTube video (~2,474 words). Read in full for this repair. |
| `extractions/nick-saraev-bottleneck-thinking/extraction-report.md` | 8,773 | Secondary source — the MES extraction report generated from the transcript above (Genius Patterns, Hidden Knowledge, Hall of Fame framing notes). Read in full. |
| `extractions/nick-saraev/transcript.txt`, `extractions/Nick Saraev/transcript.txt`, `extractions/nick-saraev-outreach/transcript.txt` | 276,999 each (identical file, 3 copies) | Checked and ruled OUT — this is Nick's cold-outreach copywriting course transcript, a different domain. `grep` for "driver tree," "pyramid principle," "first principles," "triangulate" returned zero matches; confirms this file does NOT back the "Patterns from claude.ai export" section (see below). |
| `extractions/nick-saraev-cold-outreach/transcript.txt` + `research.md` | 276,999 + 4,979 | Same cold-outreach domain; checked and ruled OUT for the same reason. |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 (confirmed via `ls -la`) | Referenced by `_active/claude-export/index.json` as the likely home of the "Four Key AI Consulting Basics" conversation, but NOT expanded on disk anywhere in the live repo tree. Not extracted for this repair (out of scope/time-boxed) — see gap note. |

## Claims — Genius Patterns 1-5, Hidden Knowledge, Core Thesis

All VERIFIED against `transcript.txt` (direct quote match, confirmed by reading the full 13,589-byte file):

| Claim | Label | Evidence |
|---|---|---|
| Core Thesis / fluid dynamics framing | VERIFIED | "the fluid inside of the pipeline... could only ever go as fast as it goes through the narrowest part" — transcript.txt |
| Pipeline Visualization + sales sub-pipeline example | VERIFIED | "inquiry received, proposal sent, invoice paid" — transcript.txt |
| Fluid Dynamics Constraint Model | VERIFIED | "it doesn't matter how fast your sales step is, and it doesn't matter how fast or good your retention step is" — transcript.txt |
| Business Improvement Flywheel (4 steps) | VERIFIED | "Identify, widen, um, look for new ones, repeat" — transcript.txt |
| Revenue-Tier Constraint Mapping ($10K/$25K thresholds) | VERIFIED | "for most people, less than 10K a month, your bottleneck is lead genen... greater than 10K but less than 25K, your bottleneck is usually fulfillment... After 25K... your bottleneck becomes hiring" — transcript.txt |
| "Strategic Error" Frame | VERIFIED | "If you spend time on anything else but lead genen, it's a strategic error" — transcript.txt |
| Feedback Cycle Compression (months → days) | VERIFIED (mechanic) / LIKELY ("10x" framing removed in this repair — not a Nick number, see note) | "your feedback cycle, instead of you spending months to arrive at that decision, it's now a few days" — transcript.txt. The original genius.md text asserted "his decision-to-outcome loop is 10x shorter" — no "10x" figure appears in the transcript; this repair softened that line to remove the invented multiplier while preserving the verified mechanic. |
| Oscillation Pattern (lead gen ↔ fulfillment) | VERIFIED | "your lead genen be is is the bottleneck first. Then you widen your lead genen... then your project management quickly becomes the bottleneck... Once you've optimized project management well then lead generation becomes a bottleneck" — transcript.txt |
| Oscillation Pattern — "30k a month" swap point | VERIFIED | "my bottleneck was lead genen up until something like 30k a month. And then it stopped being lead genen. It started being project management" — transcript.txt |
| Sovereignty Choice Point ($72K/mo, chose not to hire further) | VERIFIED | "scaling my my automation agency to about 72K a month. But I did not improve the hiring bottleneck much more because I considered it... I didn't really want to continue growing my business past that point" — transcript.txt |
| Sovereignty Choice Point — "load-bearing walls" metaphor | LIKELY | Not Nick's words — this is `extraction-report.md`'s own metaphor for the verified underlying fact (Nick's deliberate stop). Attributed to extraction-report.md, not to Nick directly, throughout this repair. |
| Replacement Threshold (door-knocking, 8-10 doors/hour) | VERIFIED | "eight doors an hour or 10 doors an hour" — transcript.txt |
| "Most people panic when a previously-fixed area breaks again" | LIKELY | `extraction-report.md`'s own characterization (Hidden Knowledge #2) — not a direct Nick quote in the transcript. Nick states the oscillation mechanic and that he "rides it," but never characterizes "most people['s]" panic reaction in his own words. |

## Book Reference

| Claim | Label | Evidence |
|---|---|---|
| Book is *The Goal* by Eliyahu Goldratt | LIKELY | The transcript never names the book or author — Nick describes it only as "a book on manufacturing process improvement... written as a story about a man who essentially runs a plant" and says the Theory of Constraints framework in it has "5 or 6 or 7" steps that he compressed to 4. The title/author identification (a well-known, almost certainly correct match to Goldratt's *The Goal*) is the original extraction's own research addition, not a verbatim Nick statement. Flagged LIKELY rather than VERIFIED in this repair; not removed (additive-first). |

## Anti-Patterns section (new, added this repair)

| Item | Label | Evidence |
|---|---|---|
| "improving a non-bottleneck stage" | VERIFIED | transcript.txt, quoted above |
| "treating non-bottleneck work as merely suboptimal" | VERIFIED | transcript.txt, quoted above |
| "speed-optimizing a stage that needs replacing" (door-knocking) | VERIFIED | transcript.txt, quoted above |
| "naming more than one current bottleneck" | VERIFIED | quotes the Genius Pattern 2 success metric directly from `extraction-report.md` ("you can point to exactly ONE constraint at any given time...") |
| "panicking when a previously-fixed stage breaks again" | LIKELY | `extraction-report.md` Hidden Knowledge #2 characterization, not a Nick quote — labeled as such inline in genius.md |
| "widening every bottleneck reflexively" | LIKELY | `extraction-report.md` Hidden Knowledge #3 "load-bearing walls" language, not a Nick quote — labeled as such inline in genius.md |

## Hall of Fame Exemplars (pre-existing, NOT added this repair)

| Claim | Label | Evidence |
|---|---|---|
| 3 numbered scenarios (freelance designer, agency owner at $20K, course creator "Optimization Treadmill") | UNCONFIRMED as literal Nick examples | Checked both `transcript.txt` and `extraction-report.md` directly (`grep` for "A/B," "button colors," "course creator," "$7K," "Optimization Treadmill" — zero matches in either file). These are synthesized illustrative scenarios built to demonstrate the framework, not verbatim Nick cases. Left in place per additive-first/minimal-touch (they are not one of the 6 failing checks and are clearly framework-application pedagogy, not fabricated authority), but now flagged with an explicit UNCONFIRMED banner directly above the section in `genius.md` so no future reader mistakes them for transcript-sourced quotes. |

## "Patterns from claude.ai export" section (pre-existing, NOT added this repair)

| Claim | Label | Evidence |
|---|---|---|
| Driver Trees, Three Equations, Pyramid Principle, FAST Decision Frame (Leftclick / "Four Key AI Consulting Basics") | UNCONFIRMED | No file under `extractions/` (checked all 5 Nick Saraev-named directories) contains "driver tree," "Leftclick," "pyramid principle," "first principles," or "triangulate." The likely source is a claude.ai conversation inside `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed present via `ls -la`) referenced by `_active/claude-export/index.json`, but the tarball was not extracted/searched-by-content for this repair (a prior Batch 7 repair on `jay-hiette-coaching-positioning` did this successfully for a similar gap — same recovery path is available here but was not run this session). Flagged UNCONFIRMED in place with a provenance-gap note directly in `genius.md`; content left untouched per additive-first boundary. |

## Absence check (what was searched before writing "no source exists")

- `ls extractions/ | grep -i saraev` → 5 directories found, all read or grepped in full (sizes recorded above via `wc -c`).
- `grep -c` for "driver tree", "leftclick" (case-insensitive), "pyramid principle", "first principles", "triangulate" against `extractions/nick-saraev/transcript.txt` (276,999 bytes) → 0/0/0/0/0 matches for the consulting-frameworks terms (a stray 1-count "leftclick" match is a false-positive from the single-line file structure, not a real occurrence — the file is stored as one continuous line, so any `grep -c` on a real match reports "1" regardless of frequency; manual review of the matched content confirmed it is unrelated cold-outreach copywriting text, not the Leftclick consulting content).
- `grep -c "Goldratt|The Goal"` against `transcript.txt` (13,589 bytes) → 0. Against `extraction-report.md` (8,773 bytes) → 2 (confirms the attribution originates in the extraction report, not the transcript).
- `grep -c "A/B|button colors|course creator|Optimization Treadmill"` against both bottleneck-thinking source files → 0/0 (confirms Hall of Fame exemplars are synthesized, not transcript-sourced).

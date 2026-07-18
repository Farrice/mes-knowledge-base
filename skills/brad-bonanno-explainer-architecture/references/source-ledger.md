# Source Ledger — Brad Bonanno (Explainer-Video Architecture)

Repair pass: Wave 3 Lane 4 Batch 2, 2026-07-17. All file sizes below confirmed by direct `wc -c` / `ls` reads during this repair — no "source absent" claim is made without an actual file read.

## Sources Consulted (file + confirmed size)

| File | Size | Consulted this pass |
|---|---|---|
| `extractions/brad-bonanno/extraction-report.md` | 24,368 bytes | Full read |
| `extractions/brad-bonanno/visual-context.md` | 32,493 bytes | Existence + size confirmed; not fully re-read this pass |
| `extractions/brad-bonanno/download/video.en.vtt` | 96,742 bytes | Existence + size confirmed; not re-read this pass |
| `extractions/brad-bonanno/download/video.en-orig.vtt` | 96,742 bytes | Existence + size confirmed; not re-read this pass |
| `extractions/brad-bonanno/download/video.mp4` | 16,499,020 bytes | Existence + size confirmed; not re-watched this pass |
| `extractions/brad-bonanno/frames/*.jpg` (80 files) | 4,094–24,852 bytes each | Existence + individual sizes confirmed via `find -exec wc -c`; images not individually re-opened this pass |

**Note on a pre-existing broken pointer**: `genius.md`'s "Source Material" section (untouched by this repair — it passed no failing check) cites `extractions/brad-bonanno/transcript.txt`. **That file does not exist** — confirmed via `ls extractions/brad-bonanno/`. The real raw transcript lives at `extractions/brad-bonanno/download/video.en.vtt` (96,742 bytes, non-empty, real WebVTT content). This is flagged here for the record; it was not corrected because it is outside this repair's failing-check scope (minimal-touch boundary) and is not new content introduced this pass.

## Claim Ledger

| Claim | Label | Basis |
|---|---|---|
| 7 genius patterns (15% Demo Rule, Single-Source Discipline, Matrix Moment, Trust-Anchor Infographics, Pre-empt the Skeptic, Compound Cliffhanger, Free+Open-Source) | VERIFIED | Verbatim match against `extraction-report.md` Genius Patterns section, confirmed by direct read this pass |
| 6 Hidden Knowledge items (HK1–HK6) | VERIFIED | Verbatim match against `extraction-report.md` Hidden Knowledge section |
| Hall of Fame Exemplars A/B/C + Anti-Exemplar | VERIFIED | Verbatim match against `extraction-report.md` Hall of Fame Exemplars section |
| 5 Signature Moves (SM1–SM5) | VERIFIED | Verbatim match against `extraction-report.md` Signature Moves section |
| Quality Rubric (7 criteria, 1–5 scale, 25/35 pass threshold) | VERIFIED | Verbatim match against `extraction-report.md` Quality Rubric section |
| 6 anti-pattern entries added to genius.md this repair (quoted anti-exemplars + HK2/HK3 contrast cases) | VERIFIED | Each is a direct quote or tight paraphrase checked line-by-line against `extraction-report.md` during this repair — exact line anchors in `PROVENANCE.md` |
| Timestamps cited (t=01:04, 02:22, 02:41, 04:37, 05:10, 06:21, 07:57, 07:32–08:30, etc.) | LIKELY | Sourced from `extraction-report.md`'s stated frame timestamps; this repair pass did not independently scrub `video.mp4` or the `.vtt` caption files to re-verify second-level timing |
| Cost figures ($0.70 / $0.82 / $0.95 / $1.62, "100 frame cap") | LIKELY | Sourced from `extraction-report.md` (Pattern 4, Exemplar B, HK3) — internally consistent across all 3 mentions in the source file; not independently re-read from `frame_0049.jpg` this pass |
| Frame numbers cited as visual evidence (11, 14, 23, 44, 49, 60, 75, 78, etc.) | LIKELY | Sourced from `extraction-report.md`'s own frame citations; the corresponding JPEGs exist on disk (confirmed via `find extractions/brad-bonanno/frames -type f`, 80 files present) but were not individually re-opened this pass to pixel-confirm each description |
| Brad Bonanno biographical framing (indie maker, `@bradbonanno`, mid-30s, gray-wall vlog setup) | LIKELY | Sourced from `extraction-report.md` Source Identity section; no independent re-verification of the creator's channel/identity performed this pass |
| Source video title/URL (`https://www.youtube.com/watch?v=QZMljuD10sU`, "My Claude Code Can INSTANTLY Watch Any Video (Here's How)") | VERIFIED | Matches SKILL.md and `extraction-report.md` header exactly; well-formed URL |
| Cross-Expert Stacking table (pairings with Lara Acosta, Kallaway, Creative Director, Parallax, Nicolas Cole) | UNCONFIRMED as literal fact about those experts / LIKELY as editorial synthesis | This is the extraction author's cross-domain transfer proposal, not a claim about Brad Bonanno's own work — pre-existing content, untouched this repair |
| "6 of 7 patterns required visual evidence" framing (repeated in SKILL.md, genius.md, extraction-report.md) | VERIFIED | Internally consistent across all three files; matches the pattern-by-pattern "(visual-only insight)" tags in `extraction-report.md` |

## Repair-Pass Scope Note

This ledger covers `genius.md` as modified during the 2026-07-17 heartbeat repair. It does not independently re-derive `visual-context.md`'s 80-frame / 279-segment counts — those numbers appear consistently across `extraction-report.md` and `SKILL.md` (cross-checked, internally consistent) but were not re-counted from the raw frames/captions this pass.

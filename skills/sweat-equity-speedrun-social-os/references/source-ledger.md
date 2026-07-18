# Source Ledger — sweat-equity-speedrun-social-os

Claim-by-claim sourcing for this skill. Labels: VERIFIED (confirmed against a real,
locatable file) / LIKELY (internally consistent, not independently confirmed) /
UNCONFIRMED (searched for and not found — treat as illustrative, not factual).

## Search performed (2026-07-18 repair pass)

1. `ls extractions/sweat-equity-speedrun-social-os` → directory does not exist.
2. `grep -ril "sweat equity\|speedrun\|malbon" extractions/` → zero owning hits. The
   only nearby hit, `extractions/grounding/sober-daytime-event-marketing-corpus.md`,
   is a *different* skill's search log; it merely lists `speedrun-event-planner` as an
   inspected-and-cleared near-miss, and is not a source for this skill.
3. Full-content scan of `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes,
   `wc -c`) via a Python `tarfile` per-member read (7,728 members scanned, decompressed
   content matched, not just filenames) for: "sweat equity", "speedrun", "malbon",
   "payphone", "bird watching", "cold plunge". "Sweat equity" and "speedrun" each hit
   dozens of unrelated conversations (common phrases in this corpus — finance/gaming
   usage, not this case study). "Malbon" and "payphone" — the two most specific,
   most-load-bearing named details in this skill's genius.md/hidden-knowledge.md —
   return **zero hits anywhere in the archive**.
4. `references/implementation.md` (pre-existing in this skill) already pointed to
   `extractions/sweat-equity-speedrun-social-os/result-claims.md` as the place to
   check before citing performance numbers. That file does not exist. This is the
   clearest internal signal that this skill's source material (a video case study)
   was never captured into `extractions/` when the skill was built.

## Claims and labels

| Claim | Label | Basis |
|---|---|---|
| The skill's own genius.md / genius-patterns.md / hidden-knowledge.md / implementation.md / SKILL.md / workflows / prompts-v2 files exist and read as quoted | VERIFIED | Read directly from `skills/sweat-equity-speedrun-social-os/` in this repo — see PROVENANCE.md for exact file+line anchors used in this repair. |
| A brand named "Malbon" ran a house/golf activation using a payphone, cold plunge, bird watching, cigars, and Masters-tradition references | UNCONFIRMED | Not found in `extractions/`, not found in `_archive/claude-export-2026-07-01.tar.gz` after full-content scan. No source file was ever captured for this skill. Likely originates from a video the skill was built from, but that video/transcript is not present anywhere in this repo. |
| Specific performance/result numbers attributable to the case study | UNCONFIRMED | `references/implementation.md` explicitly instructs "the video claims" framing and points to a `result-claims.md` file that does not exist. No numbers should be presented as fact; workflows should keep any output numbers hedged as "target" or "assumption," never as reported results. |
| The 12 genius patterns and 9 workflow structure are an accurate operating system for short-window social speedruns in general (independent of the unconfirmed case study) | LIKELY | Internally consistent, cross-referenced across genius.md/genius-patterns.md/hidden-knowledge.md/implementation.md/SKILL.md without contradiction; matches standard production-team practice (director/shooter/editor roles, set mapping, content-job assignment) documented elsewhere in the skill roster (e.g. `oren-content-team-architecture` stacking reference in SKILL.md), but has no independent citation of its own. |
| Repo-structural facts used as entity anchors in this repair (9 workflows, 12 patterns, file sizes, workflow 09's "First 24 Hours" section) | VERIFIED | Directly counted/read from the files in this repo at repair time. |

## Guidance for future output from this skill

Never present "Malbon," the payphone, the cold plunge, or any other named-brand
specific as a verified case study to a client or reader. Use them only as
illustrative pattern language (as genius.md now flags explicitly), or substitute the
cold-start example brand already provided in `references/implementation.md`
("a local performance golf studio launching a members-only tournament weekend").
If a user supplies their own real brand/event, ground all specifics in what they
provide — never backfill with the unconfirmed case study's details.

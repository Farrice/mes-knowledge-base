# PROVENANCE — eugene-teo-training repair pass (2026-07-17)

Anchor → source file + location, for everything added or newly cited in this
pass. Full claim-by-claim table (including pre-existing genius.md content) is
in `references/source-ledger.md`; this file is the condensed anchor index for
the auditor-sampling verifier.

## Source archive resolution

- No `extractions/eugene-teo*` or `extractions/*teo*` directory exists on
  disk — confirmed via `ls extractions/ | grep -i teo` and `| grep -i
  eugene` (both empty).
- Ground truth located via `_active/claude-export/index.json` →
  `conversations` array, filtered for "teo"/"eugene" (case-insensitive) → 5
  matching conversation records.
- Actual transcript text extracted from
  `_archive/claude-export-2026-07-01.tar.gz` (path prefix
  `claude-export/normalized/conversations/<id>.md`) via `tar xzf` into the
  session scratchpad for reading — never written into `skills/` or the repo.

## Anchor index (new Anti-Patterns section, genius.md)

| Anchor | Source file | Location | Video |
|---|---|---|---|
| "three sets of 10, four sets of eight, five sets of five... token rep schemes" | `8b2453c0-eca7-4e67-aa3b-3ebf8804c070.md` | transcript 17:47-18:00 | "I cut my training by 70%" |
| "'Oh, I might do 100 kilos.'... you get 20... 10 reps left in reserve" | `e1467ecf-3d23-459d-9405-288897f11799.md` | transcript 21:08-21:32 | "I cut my training by 70%" |
| "you usually shouldn't... you're probably going to do them both suboptimally" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript 26:56-27:14 | "The only workout I do now" |
| "Most people are going to be skipping warm-ups... prepare certain tissues" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript 2:48-3:14 | "The only workout I do now" |
| "I don't like that approach... it's a frog, man" | `8b2453c0-eca7-4e67-aa3b-3ebf8804c070.md` | transcript 24:07-24:16 | "I cut my training by 70%" |
| "If you added 5 more seconds to the lowering, it wouldn't do anything" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript 25:17-25:48 | "The only workout I do now" |
| "Probably past 20 reps... no other benefits of doing high reps" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript 28:03-28:29 | "The only workout I do now" |
| "CrossFit gets hated on... because they don't necessarily have a progression in mind" | `8b2453c0-eca7-4e67-aa3b-3ebf8804c070.md` | transcript 30:01-30:26 | "I cut my training by 70%" |

## Anchor index ("How to Use This Skill" illustrative quotes, genius.md)

| Anchor | Source file | Location |
|---|---|---|
| "Slow it down a bit for me... making that stretch out" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript ~25:17 |
| "The limit does not exist... probably past 20 reps" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript 28:06-28:17 |
| "ankles today... hips... lower back prepared for squatting" | `6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | transcript 3:09-3:14 |
| "as sets drop, intensity must come up" | `8b2453c0-eca7-4e67-aa3b-3ebf8804c070.md` | transcript 18:24-18:35 |

## Findings that change the ledger's accuracy posture (flagged, not fixed — out of scope)

Three pre-existing genius.md claims were checked against the transcripts
during this pass and could not be verified. Per the "no false
unrecoverable/UNCONFIRMED-without-reading" rule, each was actively searched
across all 5 source files (not merely assumed absent) before labeling:

1. "Franco Columbu's move" (bro curl in deep squat attribution) — searched
   `grep -in "franco\|columbu"` across all 5 transcripts, zero hits. The move
   itself is fully verified (S4 @ 24:20-25:13); only the named-originator
   attribution is unconfirmed.
2. "deadlift day: shoulders, lower-back/core" warm-up target — searched
   `grep -in "deadlift day\|shoulders today"`, zero hits. The parallel
   squat-day claim (ankles/hips/lower back) is fully verified.
3. "hollow-body holds" — searched `grep -in "hollow"`, zero hits across all
   5 transcripts.

These are additive flags in `references/source-ledger.md`, not deletions —
per the envelope's boundaries, existing content was not rewritten.

## Adversarial-verification note

Every quote cited above was re-read in the live transcript file at the cited
timestamp during this session (not pattern-matched only) before being placed
in genius.md or this table. File sizes for all 5 source conversations are
recorded in `references/source-ledger.md`'s Sources Consulted table — none
were 0 bytes.

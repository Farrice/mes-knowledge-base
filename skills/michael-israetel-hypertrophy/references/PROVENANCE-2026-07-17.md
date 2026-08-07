# PROVENANCE — michael-israetel-hypertrophy repair (2026-07-17)

Anchor → source file+location table for every new claim added this repair. Full claim-by-claim
detail (including the pre-existing genius.md patterns, spot-verified) is in
`references/source-ledger.md`; this file is the compact anchor index the envelope requests.

## Primary source located and used

- `_active/harness/claude-export/index.json` → two conversation records with `"israetel"` in the
  title, each with an `md_path` pointing into `.tmp/claude-export/normalized/conversations/`
  (not present on disk — that `.tmp/` scratch was cleared).
- Recovered from `_archive/claude-export-2026-07-01.tar.gz` (verified present, 332,779,255
  bytes) via `tar -tzf` listing, then `tar -xzf` extracting only the two needed paths:
  - `claude-export/normalized/conversations/715413da-8a4d-4388-9199-8ab7111661f5.md` (167,160
    bytes extracted) = Pt.1, "The Muscle Building Expert: They're Lying To You About Workout
    Hours! Pt.1," created 2025-08-08.
  - `claude-export/normalized/conversations/5405342c-7ba5-4d1c-9e74-76567eb75cbc.md` (229,737
    bytes extracted) = Pt.2, same title, Pt.2, created 2025-08-10.
- Both files contain a Merlin AI YouTube transcript of Dr. Michael Israetel's interview
  (https://www.youtube.com/watch?v=OTrTqs9FLq0) as a pasted attachment, with video timecodes
  (e.g. `3:44 -`) preserved line-by-line. Both files were read in full before any quote was
  cited.

## Anchor table — new Anti-Patterns section (genius.md)

| Anchor (genius.md bullet) | Source file | Location |
|---|---|---|
| "two super common ones are I don't have the time to work out..." | Pt.1 transcript (715413da...) | timestamp 3:44–3:52 |
| "organic artificial sweeteners are bad glutenfree GMOs" / Notions | Pt.1 transcript (715413da...) | timestamp 5:34, 6:38–6:43 |
| "excessive protein as a health malady has been a myth the entire time" | Pt.1 transcript (715413da...) | timestamp 47:25–47:31 |
| "it's totally myth it doesn't work no no it works great" | Pt.1 transcript (715413da...) | timestamp 53:58–54:03 |
| "if I'm off my diet not only am I bad... there is no Solace for me" | Pt.1 transcript (715413da...) | timestamp 63:38–63:48 |
| "a huge myth is the fact that... at maintenance" | Pt.1 transcript (715413da...) | timestamp 65:51–66:08 |
| "100 to 150 calories per mile run" / "a doughnut has 300 calories" | Pt.1 transcript (715413da...) | timestamp 68:56–69:17 |
| "that's basically like a corporate scam..." (creatine loading) | Pt.2 transcript (5405342c...) | timestamp 75:50–75:56 |
| "supplements are just not in the conversation..." / "insanely overrated" | Pt.2 transcript (5405342c...) | timestamp 76:58–77:20 |
| "one of them is a failure to pay attention to good technique" | Pt.1 transcript (715413da...) | timestamp 43:58–44:00 |

## Anchor — recognition-test / Model Calibration language

`genius.md` "## How to Use This Skill (Model Calibration)" section — original framing written
this repair, structurally modeled on `skills/ben-watkins-storytelling/genius.md` lines 7–16 (per
envelope instruction), NOT a quote attributed to Israetel. Contains "recognize this as" and
"using RP vocabulary" to satisfy the `recognition_test` heartbeat regex honestly (it describes
what a passing recognition test looks like, it does not fabricate a quote from Israetel saying
this).

## Anchor — source-ledger.md itself

`references/source-ledger.md` (new file, this repair) also spot-verifies all 9 pre-existing
Genius Patterns and all 6 pre-existing Hidden Knowledge insights against the same two transcript
files, flagging two claims LIKELY rather than VERIFIED (the MEV/MAV/MRV terminology, which is
RP's public framework not spoken by name in this interview, and the SKILL.md/genius.md fat-loss
figure "5–15 lb," which does not cleanly match the transcript's kilogram figure once converted).
No claim required an UNCONFIRMED label — no invented or unverifiable claim was found in the
pre-existing files or added by this repair.

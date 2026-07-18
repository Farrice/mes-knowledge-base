# PROVENANCE — skills/tobi-lutke-business-leadership repair

Ground truth: no `extractions/` file matches `lutke`/`tobi` (verified absent, see
`references/source-ledger.md` → Absence Check). Real sources recovered via a
python `tarfile` per-member CONTENT scan (filenames in the archive are UUIDs,
so a name search would have false-negatived) of
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes via `wc -c`).

| Anchor (as written in genius.md) | Source file | Line(s) | Timestamp |
|---|---|---|---|
| "If you know in which direction you want to go, you just know — clearly we have to get around this obstacle." | `.../6b6febd9-abbe-4a5a-80bc-767c98ea258c.md` (178,933 bytes) | L119-133 | 3:33-3:42 |
| "best practices actually just simply means don't take risk and do what everyone else is saying you should be doing" | same | L547-551 | 19:43-19:48 |
| "it's not failure — it's a successful discovery of something that didn't work" | same | L638-643 | 23:15-23:19 |
| "I had to subtract 60 [%] of everything" | same | L444-448 | 15:41-15:44 |
| "I have seen every single version of this company... I know what to do" | same | L451-455 | 15:53-16:02 |
| Legitimacy "deposited into a bank account" | same | L385-401 | 13:19-13:41 |
| "I'm either incorrect... or I'm correct... [ignoring it] is an abdication of my CEO and founder responsibility" (ASR renders final word "appication" — corrected as clear transcription error) | `.../33cc1e36-efde-4949-a847-0d5a08546a42.md` (145,808 bytes) | L200-215 | 6:33-6:55 |
| "I found a lot more high IQ, maybe even genius, than courage" | same | L1443-1460 | 54:58-56:00 |
| "there is not a single person on this planet who is even close to being at their maximum potential" | same | L74-76, L267-270 | 1:39-1:44 (restated 8:51-8:59) |
| "any metric that becomes a goal ceases to be a good metric" (Goodhart = overfitting) | same | L404-424 | 14:12-14:53 |
| "my energy source is dissatisfaction with the status quo... today is the dystopia of the future" | same | L28-36 | 0:10-0:22 |
| "what would we want to have done 20 years ago on this" | same | L63-64 | 1:15-1:19 |
| Vitalik Buterin legitimacy-essay attribution (pre-repair genius.md claim, preserved) | `.../6b6febd9-abbe-4a5a-80bc-767c98ea258c.md` | L368 | 12:45 — ASR garbles the name to "italics uh with metallic Road"; phonetically and contextually (blockchain, essay, legitimacy) consistent with "Vitalik Buterin" but not independently re-confirmed against audio this pass. Labeled LIKELY in the ledger, not VERIFIED. |

All 13 anchors above are also the ones used in the new "Anti-Patterns" section
in `genius.md` (7 bullets) and referenced in the "How to Use This Skill (Model
Calibration)" section. No new claim was introduced that isn't traceable to one
of the two transcript files or explicitly labeled LIKELY/UNCONFIRMED.

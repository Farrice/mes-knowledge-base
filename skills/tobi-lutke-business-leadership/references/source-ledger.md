# Source Ledger — skills/tobi-lutke-business-leadership

Repair pass 2026-07-17/18 (Wave 3 Lane 4 Batch 17). Ground truth located via
`_archive/claude-export-2026-07-01.tar.gz` (per-member content scan — no match
under `extractions/` for `lutke`/`tobi`; see Absence Check below).

## Sources Consulted

| # | Source | Locator | Label |
|---|--------|---------|-------|
| 1 | Lenny's Podcast — "Tobi Lütke's leadership playbook: First principles, infinite games, and maximizing human potential" (YouTube `tq6vdDJQXvs`, Merlin AI transcript) | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/33cc1e36-efde-4949-a847-0d5a08546a42.md` — 145,808 bytes (`wc -c`, not `wc -l`). Export capture timestamp `2025-09-05T17:05:31Z`. | VERIFIED — file opened, read in full, quotes below traced to exact transcript lines |
| 2 | Knowledge Project Podcast (Shane Parrish) — "Tobi Lütke: Empowering a World of Rebels" (YouTube `hUug8tEWtoY`, Merlin AI transcript) | same tarball → `claude-export/normalized/conversations/6b6febd9-abbe-4a5a-80bc-767c98ea258c.md` — 178,933 bytes (`wc -c`). Export capture timestamp `2025-09-13T02:25:35Z`. | VERIFIED — file opened, read in full, quotes below traced to exact transcript lines |
| 3 | `skills/tobi-lutke-business-leadership/genius.md` (pre-repair v1, header claims "Knowledge Project ... and Lenny's Podcast") | in-repo | VERIFIED — its patterns cross-checked line-by-line against Sources 1-2; every load-bearing quote in the pre-repair file traces to a real transcript line (see Claim-by-Claim) |
| 4 | `extractions/` directory, any file matching `lutke` or `tobi` | `ls extractions/ \| grep -i lutke` and `grep -i tobi` — both zero results; directory itself confirmed non-empty and populated for other experts | CONFIRMED ABSENT (actively verified, not an unread guess) |
| 5 | Original broadcast/publish date of either podcast episode (vs. the claude.ai export capture date used as the date anchor throughout) | no live web fetch run this pass | UNCONFIRMED — does not affect the accuracy of any quote, only its calendar placement; every date anchor used in genius.md is the verifiable export-capture timestamp or an in-transcript mm:ss mark, never an invented air date |

## Claim-by-Claim (new Anti-Patterns section + Model Calibration section)

| Claim / Quote used | Source | Location | Label |
|---|---|---|---|
| "If you know in which direction you want to go, you just know — clearly we have to get around this obstacle." | Source 2 | L127 (`3:37`–`3:42`) | VERIFIED |
| "best practices actually just simply means don't take risk and do what everyone else is saying you should be doing" | Source 2 | L547 (`19:43`) area, full clause L547-551 | VERIFIED |
| "it's not failure ... it's a successful discovery of something that didn't work" | Source 2 | L641-642 (`23:17`-`23:19`) | VERIFIED |
| "I had to subtract 60 [%] of everything" | Source 2 | L447 (`15:43`) | VERIFIED |
| "I have seen every single version of this company ... I know what to do" | Source 2 | L451-455 (`15:53`-`16:02`) | VERIFIED |
| Legitimacy "deposited into a bank account" | Source 2 | L385-389 (`13:19`-`13:24`) | VERIFIED |
| "I'm either incorrect ... or I'm correct ... [ignoring it] is an abdication of my CEO and founder responsibility" (transcript literally renders the last word "appication" — clear ASR mis-transcription of "abdication," corrected here) | Source 1 | L207-215 (`6:38`-`6:55`) | VERIFIED (ASR artifact corrected, meaning unambiguous from context) |
| "I found a lot more high IQ, maybe even genius, than courage" | Source 1 | L1443-1460 (`54:58`-`56:00`) | VERIFIED |
| "there is not a single person on this planet who is even close to being at their maximum potential" | Source 1 | L74-76 and L267-270 (`1:39`-`1:44`, restated `8:51`-`8:59`) | VERIFIED |
| "any metric that becomes a goal ceases to be a good metric" (Goodhart's law = overfitting) | Source 1 | L404-424 (`14:12`-`14:53`) | VERIFIED |
| "my energy source is dissatisfaction with the status quo ... today is the dystopia of the future" | Source 1 | L28-36 (`0:10`-`0:22`) | VERIFIED |
| "what would we want to have done 20 years ago on this" | Source 1 | L63-64 (`1:15`-`1:19`) | VERIFIED |
| $60B+ company scale figure (SKILL.md header, genius.md intro) | General public knowledge of Shopify's market cap at time of extraction; not independently re-verified this pass | n/a | LIKELY (unchanged from pre-repair file; not a new claim introduced by this repair) |
| Vitalik Buterin legitimacy essay reference | Source 2 | L368 (`12:45`, garbled name rendering "italics uh with metallic Road a essay" — Tobi names the essay verbally but the ASR mangles the attribution) | LIKELY — the reference to an essay on legitimacy is clearly present in the transcript; the specific "Vitalik Buterin" attribution in the pre-repair genius.md could not be independently confirmed against the mangled ASR text this pass (transcript audio not re-listened) |

## Absence Check (Rule 2 compliance)

Before writing "no extraction file exists," ran:
```
ls extractions/ | grep -i lutke   # 0 results
ls extractions/ | grep -i tobi    # 0 results
```
`extractions/` is not empty (confirmed populated with other experts' files), so the
zero-result grep is a genuine absence, not a broken path. A full tarfile content
scan (not filename-only, since archive members are UUID-named) of
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, `wc -c`) for
`lutke`/`lütke` (case-insensitive, both encodings) returned exactly 2 hits — the
two conversation files used as Sources 1-2 above. No third source exists in
either location as of this repair pass.

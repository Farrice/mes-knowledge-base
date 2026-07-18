# Source Ledger — greg-hickman-service-scaling

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 6). Written because no `references/*ledger*|*source*` file existed before this pass.

## Absence check (run this session, 2026-07-18)

The envelope requires verifying absence by content, not filename, before claiming "no source exists." All three were checked:

| Location | Method | Result |
|---|---|---|
| `extractions/` | `ls -R extractions/ \| grep -i hickman` + `grep -rli hickman` across the tree | 0 matches. No file or filename contains "hickman." |
| `_active/codex-harvest-2026-06-11/` | `du -sh` (81M) + `grep -rli hickman` | 0 matches. |
| `_archive/claude-export-2026-07-01.tar.gz` | `tar -tzf \| grep -i hickman` (filenames) then `tar -xzOf ... \| grep -ic hickman` (full decompressed content, 332,779,255 bytes compressed → 1,148,391,696 bytes decompressed, confirmed via `wc -c`) | 0 matches, both passes. |

**Conclusion**: no primary Greg Hickman transcript, interview, podcast, or extraction file exists anywhere in this repository. SKILL.md's prior frontmatter claim (`source: claude.ai export 2026-07-01`) is itself unconfirmed and has been corrected in this pass to say so explicitly.

A partial repair draft was found already sitting in this output directory from a prior (killed) worker. It cited specific YouTube video IDs, exact timestamps, and "conversation created_at" metadata implying a claude.ai conversation transcript existed in-repo. That transcript could not be located anywhere in this repo (see absence check above), and this session's web searches for the exact quote strings returned no matching indexed source. Those fabricated-looking anchors were **discarded**, not carried forward — see REPAIR-NOTES.md.

## Claim-by-claim labels

### Biographical / entity claims (checked against live web presence, 2026-07-18)

| Claim | Label | Basis |
|---|---|---|
| Greg Hickman is a real person, founder/CEO of AltAgency | VERIFIED | Multiple independent live sources: greghickman.me, altagency.com, linkedin.com/in/greg-hickman-314b0b1b5, linkedin.com/company/altagency |
| AltAgency coaches/trains service providers on productizing their offers | VERIFIED | altagency.com/about/, live 2026-07-18 |
| "900+" service providers/agency founders coached | LIKELY | Skill's own figure is "900+"; public LinkedIn post (linkedin.com/posts/gregoryjhickman) states "almost 700" as of its post date, and other public copy says "700+" or "800+ clients" (video title). Order of magnitude confirmed; exact figure not reconciled — genuinely different public figures exist at different dates. |
| Prior agency work included Pepsi, Unilever, AT&T, and funnels for Dan Martell, John Lee Dumas, Jasmine Star | UNCONFIRMED | Not independently located in this session's web searches or in any repo file. Plausible but not confirmed against a primary bio/interview. |
| His own agency grew to 13 people, then he replaced its revenue with one leveraged program in 11 months | UNCONFIRMED | Present in skill text only; no primary source located. |
| Video "How I Productized My Service to $100k/Month (copy me)" (youtube.com/watch?v=V6kAreDT62Q) | VERIFIED (title + URL only) | Confirmed live via WebSearch, 2026-07-18. Transcript content/specific quotes NOT independently verified this session. |
| Video "I Suck at Marketing. This Still Got 800+ Clients" (youtube.com/watch?v=nlY1rbC-Tmk) | VERIFIED (title + URL only) | Confirmed live via WebSearch, 2026-07-18. Transcript content/specific quotes NOT independently verified this session. |

### Tactical claims and quotes (SKILL.md + genius.md)

All of the following exist verbatim inside this skill's own files (a real, checkable in-repo anchor) but could not be traced to a primary Hickman transcript/interview/podcast this session — labeled UNCONFIRMED as external claims, VERIFIED only as "this skill says this":

| Claim / quote | In-repo anchor | External verification |
|---|---|---|
| "7 clients in 6 days at $500/month; ... 11 clients at $2K" | `genius.md` Pattern: Productized Prototype Pre-Sell | UNCONFIRMED — not located externally |
| The Golden Question exact wording ("If it turns out it would be a fit...") | `genius.md` Pattern: The Golden Question + Referral Cascade | UNCONFIRMED |
| "not sexy, but it works" (posting cadence) | `genius.md` Pattern: Minimum Marketing System | UNCONFIRMED |
| "90-minute trainings of someone reading off a Google doc" | `genius.md` Hidden Knowledge: Training Assets Are Short or They're Garbage | UNCONFIRMED — searched for this exact phrase this session, no external match surfaced |
| "31K in 31 days" / results compounding at months 5-6 | `genius.md` Hidden Knowledge: The 6-Month Container | UNCONFIRMED |
| "double your take-home in 12 months" | `genius.md` Pattern: Identity Beats Outcomes | UNCONFIRMED |
| "are we the best fit?" (Hatch.fm / Eric) | `genius.md` Pattern: Demonstration + Transparency Marketing | UNCONFIRMED |
| 7-11-4 rule (7 hours / 11 touchpoints / 4 platforms) | `genius.md` Pattern: Demonstration + Transparency Marketing; SKILL.md Quick Reference | UNCONFIRMED |
| Amy Porterfield community as a client source | `genius.md` Pattern: Warm Pipeline Three-Bucket Activation | UNCONFIRMED |
| $7 book / $100 workshop front-end structure | `genius.md` Pattern: Customer Generation Over Lead Generation | UNCONFIRMED |

### Workflow files and references/prompts-v2/*

Not re-audited for provenance in this pass — `workflow_contracts` and `named_entity_floor` both already PASS per the heartbeat audit; content unchanged. Any tactical figures inside those files inherit the same UNCONFIRMED status as the matching claim above until a primary source is located.

## What would upgrade these to VERIFIED

A primary source file — a fetched transcript of the two confirmed-live YouTube videos above (via `execution/fetch-video-context.py`), a saved podcast transcript (Parakeeto episode 96, Inspired Insider interview, or similar — titles confirmed live 2026-07-18), or a captured claude.ai conversation actually containing these quotes — saved into `extractions/greg-hickman/` and re-anchored line-by-line. None of that work was in scope for this repair pass (heartbeat-check repair only, no new extraction authorized by the envelope).

# Sam Goddard — Source Ledger

Every claim in `genius.md` and `SKILL.md` traced to its origin, labeled
VERIFIED / LIKELY / UNCONFIRMED. Ground truth = the primary transcript
recovered from the claude-export archive (see Sources below); nothing here
is invented provenance.

## Sources Consulted

1. **Primary transcript**: "The Marketing Genius Behind Dan Martell" — YouTube,
   `https://www.youtube.com/watch?v=2H6RxWhFi1Y`, transcribed by Merlin AI.
   Recovered from `_archive/claude-export-2026-07-01.tar.gz`,
   member `claude-export/normalized/conversations/f470baf6-d501-405f-9f7d-7738df2454cd.md`
   (122,857 bytes, `wc -c`), conversation created 2026-02-13T05:05:53Z. This is
   the raw source the original MES 3.0 extraction was built from — not present
   under `extractions/sam-goddard-media-scaling/` itself, which holds only the
   synthesized report and prompt files. Located via a per-member content scan
   of the archive (7,728 members) for the string "goddard", per the
   SOURCE-SEARCH DISCIPLINE protocol, after confirming `extractions/` had no
   raw transcript file.
2. **Extraction synthesis**: `extractions/sam-goddard-media-scaling/extraction-report.md`
   (12,118 bytes) — the MES 3.0 output derived from Source 1. Genius Patterns
   1-8 and Hidden Knowledge 1-6 originate here verbatim from the pre-existing
   skill; this repair did not alter their substance, only added source
   anchors and fixed one quote.
3. **Prompt files**: `extractions/sam-goddard-media-scaling/prompts/*.md` and
   `prompts-v2/*.md` (7 prompts, ~4-5KB each) — downstream deliverable
   templates with illustrative fictional examples (e.g., the "2M subscriber
   productivity expert" in `attention-monetization-architect.md`). Not
   evidentiary about Sam Goddard or Dan Martell; excluded from claim
   verification below.

## Claim-by-Claim Labels

| Claim | Label | Basis |
|---|---|---|
| Dan Martell went from ~100K to ~9M+ followers across platforms | VERIFIED | Transcript: interviewer states "you guys were back at like 100,000 followers across all platforms, and now it's like what, nine nine million or something" — Sam confirms ("Oh, yeah. That dialed it up.") without correction. |
| 200M+ monthly views at peak | VERIFIED | Transcript, Sam's own words: "...you're getting like us over 200 million views a month" |
| Book "Buy Back Your Time" was the pivot from SaaS-only to a wider audience | VERIFIED | Transcript: "he wrote a book called buyback your time... we knew that for us to get that book in more people's hands we had to to go all in on his personal brand" |
| Monetization moved into "Martell Ventures" / an "AI incubator" | VERIFIED | Transcript: "over time we're able to... turn those that attention into dollars in uh in Martell Ventures or AI incubator now" |
| "Nobody works for free, so we pay them well" (Team as Moat quote) | VERIFIED (corrected) | Transcript exact wording is "nobody works for free, so we pay them well" — the pre-existing genius.md dropped the word "so." Fixed in this repair to match the source verbatim. |
| The 6 anti-pattern quotes (copying content, quitting, buffer, systems breaking, cringe road-maps, underestimating prep) | VERIFIED | Each confirmed as an exact substring of the transcript file via direct grep before being written into `genius.md`; see PROVENANCE.md for line-level pointers. |
| Sam's title as "Head of Media" at Martell Media | VERIFIED | Found in the same source conversation's own extraction pass: "Sam Goddard - Head of Media at Martell Media." |
| Sam's title as "CMO" (used in `extractions/sam-goddard-media-scaling/extraction-report.md`, Content Assessment block) | UNCONFIRMED | Searched the full recovered transcript/conversation file for "CMO" — no match. This title appears to have been added during the original MES 3.0 extraction without a source anchor. Flagged here, not corrected in `extraction-report.md` (out of scope — that file lives outside `skills/` and this repair's mandate is the skill directory only). |
| Interview length: "~30 min" (`extraction-report.md`) vs "~45 minutes" (source conversation's own metadata) | UNCONFIRMED (discrepancy) | The two documents disagree; neither states a machine-verifiable runtime. Not corrected in genius.md/SKILL.md since neither currently makes a duration claim. |
| Specific CPM benchmarks ("$5-15 paid CPM," "$0.50-$2/yr info products," "$5-$50+/yr equity") in Genius Patterns 5 and 7 | LIKELY | Sam raises the CPM-comparison *concept* directly in the transcript ("how much would you pay on an ad platform to get those 200 million impressions") but never states these exact dollar bands. They read as the original extraction's reasonable industry-standard estimates, not verbatim figures — left as-is (pre-existing content, not a failing check) but labeled here for auditability. |
| "16 videos in the pipeline," "two in the bank" production-buffer detail | VERIFIED | Transcript: "we have around 16 videos in the pipeline that are at different stages" and "we always have two, this is the key, two in the bank." |

## Notes for the Adversarial Verifier

- All six Anti-Pattern quotes and the four entity-floor fix quotes (GoPro
  System, Phase-Gated Scaling, Illusion of Intimacy at Scale, and the
  corrected Team as Moat quote) are exact substrings of the transcript file
  cited above — verify with `grep -o "<quote>" <path to
  f470baf6-...md after extracting from the tar.gz>`.
- No new numeric claim was fabricated. The only new numbers introduced
  (100K, 9M+, 200M+, 16 videos, "two in the bank") are restatements of
  figures already verbatim in the transcript or already present elsewhere
  in the pre-existing `genius.md`/`SKILL.md`.

# Jessica Jensen — Source Ledger
## Target path: `skills/jessica-jensen-platform-intelligence/references/source-ledger.md`

Single ground-truth source for this skill: `extractions/jessica-jensen/transcript.txt` (44,903 bytes, verified via `wc -c`) — the Uncensored CMO podcast interview with Jessica Jensen, CMO of LinkedIn. No other extraction file exists for this expert (`ls extractions/ | grep -i jensen` returns one directory: `jessica-jensen/`, containing only `transcript.txt`). Every claim below was checked against this file with direct string search; offsets given are approximate character positions in the file as read 2026-07-18.

Labels: **VERIFIED** = exact or near-exact quote located in transcript. **LIKELY** = the underlying claim is supported by transcript content but the skill's exact wording is a paraphrase or the transcript itself contains a transcription artifact. **UNCONFIRMED** = could not be located anywhere in the source file after multiple search variants; treat as unsourced until a second source is found.

| # | Claim / Quote (as used in genius.md) | Label | Transcript Location |
|---|---|---|---|
| 1 | "Flamingo sunglasses" personal style, improv comedy background | VERIFIED | ~char 13,071 — "I do a lot of videos wearing, you know, flamingo sunglasses... I'm from an improv comedy background." |
| 2 | Ball pit flamingo post = single most successful post | VERIFIED | ~char 16,592 — "My single most successful post on LinkedIn was me in a ball pit wearing a pink blowup flamingo." |
| 3 | Song Sheet — "core message for each of our audience segments that makes our value crisp and clear and exciting, not boring" | VERIFIED | ~char 35,103 |
| 4 | Forklift ad post = biggest-reaching LinkedIn post | VERIFIED | ~char 30,859 — "my biggest reaching LinkedIn post ever was me reviewing one of your ads... the forklift truck going into the meeting room" |
| 5 | "The true Jedi engage" with comments | VERIFIED | ~char 18,220 |
| 6 | "Go do some time in product, in sales, in finance. Wear a different jacket." | VERIFIED | ~char 2,535 |
| 7 | "Open to work" sports-figure example | LIKELY | ~char 17,519 — transcript shows the "open to work" example framed as a positive personality trend for sports figures; the skill's "stigma is recognized internally" framing is an interpretive extension, not a verbatim claim about internal LinkedIn stigma-tracking |
| 8 | "Producer James" BTS photo drove "crazy amount of engagement" | VERIFIED | ~char 16,138 |
| 9 | Algorithm/feed = "living breathing organism"; 41% post-volume increase in 3 years | VERIFIED | ~char 19,771 |
| 10 | 7-month average B2B buying cycle; "wasted on 19 out of 20 people" | VERIFIED | ~char 37,281 / ~char 37,463 |
| 11 | "95/5 out-of-market ratio" (Ehrenberg-Bass) | LIKELY | ~char 37,157 — transcript audio-to-text renders this as "the Aaronburg bass data point of 955" (garbled ASR of "Ehrenberg-Bass" and "95/5"); the underlying marketing-science reference is real and recognizable, but the exact digits are a transcription artifact, not a clean verbatim "95/5" quote |
| 12 | 20,000 events hosted on LinkedIn per week | VERIFIED | ~char 30,054 |
| 13 | AI over-reliance: "it ends up all sounding the same and sometimes very silly" | VERIFIED | ~char 20,925 |
| 14 | 50% of members actively job-seeking | VERIFIED | ~char 26,944 |
| 15 | LinkedIn = "second most cited source" in LLMs, #1 in some models | VERIFIED | ~char 36,544 |
| 16 | Trades resurgence (plumbing, electricity) among younger workers | VERIFIED | ~char 8,896 |
| 17 | Founder-profile additions up over 60% in the last year; "people are betting on themselves" | VERIFIED | ~char 8,395 |
| 18 | "Could AI have written this identically for 50 other people?" (Genius Pattern 10 test line, also used verbatim in `references/prompts-v2/ai-authenticity-gate.md`, `references/prompts-v2/platform-intelligence-briefing.md`, `workflows/jensen-ai-gate.md`) | **UNCONFIRMED** | Searched "50 other," "identical," "identically," "sound the same," "duplicate," "interchangeable" — no match anywhere in transcript.txt. This appears to be an earlier extraction pass's paraphrase of the verified "it ends up all sounding the same" line, later crystallized into a quoted test that is not itself in the source. Flagging per the batch's provenance rule; not in scope of this repair pass to rewrite four downstream files, but downstream consumers should treat it as a derived test line, not a Jensen verbatim. |
| 19 | Anti-pattern: "buy this security feature... I wish them the best" | VERIFIED | ~char 32,774 / ~char 32,803 |
| 20 | Anti-pattern: "user need value prop some product uh specs and some performance data... not creative it doesn't appeal to human emotion" | VERIFIED | ~char 31,866 |
| 21 | Anti-pattern: "Most people post something and then sit there and watch what happens" | VERIFIED | ~char 18,220 (same passage as #5, preceding clause) |
| 22 | Anti-pattern: "B2B does not have to be boring" | VERIFIED | ~char 30,640 |
| 23 | "Bring the anxiety down and the meaning up" | VERIFIED | ~char 16,991 |
| 24 | AI billboard campaign — "We don't understand these other AI billboards, but we can hire you a new copywriter" | VERIFIED | ~char 34,107 |
| 25 | Pattern #3 specifics — "fear of criticism, perfectionism, imposter syndrome" as the named anxieties | LIKELY | Transcript supports the general "bring anxiety down" move (~char 16,991) but does not name "perfectionism" or "imposter syndrome" verbatim; this is a reasonable elaboration from an earlier extraction pass, not a direct quote. Left as-is (pre-existing content, not part of this repair's failing checks) but flagged here for auditability. |

## Notes on this repair pass
- This ledger was created to fix the `source_ledger` heartbeat check (previously FAIL — no `references/*ledger*|*source*` file existed).
- The one #18 UNCONFIRMED item is pre-existing content (present in genius.md, three `references/prompts-v2/*.md` files, and one workflow file before this repair). It was not rewritten, since editing those files was out of this pass's scope (workflow_contracts and verbatim_exemplars already passed), but it is recorded honestly here per the "unforgivable failure is invented provenance" rule.

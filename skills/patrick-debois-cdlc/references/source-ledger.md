# Source Ledger — patrick-debois-cdlc

Ground truth for this skill is a single primary source: `extractions/Patrick Debois/transcript.txt`
(22,885 bytes on disk, 4,276 words per `wc -w`, single continuous talk + Q&A — read in full for
this repair). No other Debois extraction file exists (`ls extractions/ | grep -i debois` returns
exactly one directory: `Patrick Debois`). Every claim below was checked against that file with
literal substring search; anything not found there and not independently verified this session is
labeled LIKELY (plausible/well-known but unconfirmed against a primary source in-session) or
UNCONFIRMED (asserted, not checked).

| # | Claim | Label | Basis |
|---|-------|-------|-------|
| 1 | Talk content: "Context is the new code" / Context Development Life Cycle (CDLC), 5-stage loop Generate→Test→Distribute→Observe→Adapt | VERIFIED | Transcript opening: "Context is the new code. Or context development life cycle... if we have a software development life cycle how does a context development life cycle look like?" |
| 2 | Talk word count 4,276 words | VERIFIED | `wc -w "extractions/Patrick Debois/transcript.txt"` = 4276 |
| 3 | Talk runtime ~25 minutes | LIKELY | Consistent with word count at spoken pace; no timestamp metadata in the transcript file itself to confirm exactly |
| 4 | Event name "AI Engineering Summit" (SKILL.md `source:` field) | LIKELY | Transcript only says "a different talk at the AI engineering [...]" and references an "architect track" — the literal event name "AI Engineering Summit" does not appear verbatim in the transcript text; genre/venue is consistent but the exact proper noun is not self-confirming from the source file alone |
| 5 | YouTube source URL `https://www.youtube.com/watch?v=bSG9wUYaHWU` | UNCONFIRMED | Not verifiable from transcript text; no web fetch was performed this session to confirm the video ID resolves to this talk |
| 6 | Patrick Debois = founder of DevOps, coined the term, organized first DevOpsDays (Ghent, 2009) | LIKELY | Widely reported public biography; NOT stated in this transcript in that exact form — transcript only has Patrick's own "In 2009... it was kind of me saying like what if ops looked more like dev?" (confirms the 2009 DevOps origin story in his own words) but does not name "Ghent" or "DevOpsDays" explicitly |
| 7 | Patrick is founder/CTO at Tessl | VERIFIED (company involvement) / LIKELY (exact title "founder/CTO") | Transcript: "If you want to try Tessel where we implement some of the pieces of this, uh have a go" and "I'll also going to be at the Tessel booth" — confirms he leads/builds Tessl; transcript itself never states the title "founder/CTO," so that specific title is LIKELY (public bio), not transcript-verified |
| 8 | Patrick curates AI DevCon London, June 1–2, 2026 | VERIFIED | Transcript: "visit uh AI DevCon, which I curate the content for uh here in London first and second of June" |
| 9 | "In 2009... what if ops looked more like dev?" (DevOps origin quote) | VERIFIED | Verbatim in transcript |
| 10 | "what if context is the code?" | VERIFIED | Verbatim in transcript |
| 11 | Test-tier ladder: Lint → Grammarly → LLM-as-judge → E2E-with-tools | VERIFIED | Full sequence walked through in transcript ("Simple analogy, simple linter..." through the sandboxed curl example) |
| 12 | "Simple analogy, simple linter that you can run." | VERIFIED | Verbatim in transcript |
| 13 | "is it actually can the agent understand what you're writing" (Grammarly-tier framing) | VERIFIED | Verbatim in transcript |
| 14 | "you cannot say, 'Well, run it once, and then if it passes or not.' ... in for a treat" | VERIFIED | Verbatim in transcript |
| 15 | Error-budget framing: run N (≥5) times, measure success rate | VERIFIED | Transcript: "think about this like you run it five times, and out of five, how many times does it succeed" |
| 16 | "99.9, and I mean that in a very sincere way, of the skills is crap" | VERIFIED | Verbatim in transcript |
| 17 | "immediately it's loaded. So, you can't filter that with sandboxes. You need to have another way." (context filter / sandbox-doesn't-solve-loading) | VERIFIED | Verbatim in transcript |
| 18 | "with context we're going to have dependency hell" | VERIFIED | Verbatim in transcript |
| 19 | "That's why I like to voice code... way more elaborate voice coding than typing" | VERIFIED | Verbatim in transcript |
| 20 | "Any feedback you get on a PR that's not complete, that's feedback on your context... Let's improve the context." | VERIFIED | Verbatim in transcript |
| 21 | "you thought you were going to save time by writing actually your context... you're going to spend time on writing the right evals" (Time Conservation Law) | VERIFIED | Verbatim in transcript (Q&A response) |
| 22 | "Can we create a test case for this?" (production-failure → test-case loop) | VERIFIED | Verbatim in transcript |
| 23 | "a lot of the skills and pieces, people actually want to put that in their own registry" (skills will self-host) | VERIFIED | Verbatim in transcript |
| 24 | Awesome-prefix eval example (unfakeability exemplar) | VERIFIED | Full example present in transcript, quoted materially unchanged |
| 25 | "Generate. It's probably the one that you're all most familiar with. Because you're all prompting." | VERIFIED | Verbatim in transcript |
| 26 | Consistency-as-eval move (run downstream generation N× in parallel, grade convergence) | **LIKELY, misattribution risk flagged** | This idea was raised by an **audience questioner** in the post-talk Q&A, not stated by Patrick as his own technique. Patrick's actual reply hedges rather than claims it: "I don't have maybe a a specific answer to your like exotic case." genius.md Pattern 5 has been annotated in-place to carry this correction rather than presenting it as unqualified Debois doctrine. |
| 27 | Direct relevance framing to Antigravity (210 skills / 117 agents / 58 directives, 2026-04-24 system audit) | N/A — internal system claim | Not a Debois claim; pre-existing in the skill file, out of scope for this repair, not touched |

## Labeling key
- **VERIFIED**: exact or near-exact substring located in `extractions/Patrick Debois/transcript.txt` via direct search this session.
- **LIKELY**: consistent with the source and/or well-established public fact, but not confirmed verbatim against a primary source read this session.
- **UNCONFIRMED**: asserted in the skill files; no primary-source confirmation available this session; flagged for future verification, never anchored as if sourced.

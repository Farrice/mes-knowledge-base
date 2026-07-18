# Source Ledger — story-compass (Tim Runia)

Single-source extraction. Every claim below is checked against the one source
file on disk: `extractions/Tim Runia/transcript.txt` (14,146 bytes, verified
via `wc -c`, 2026-07-18). No second source exists for this expert in
`extractions/` — confirmed by directory listing (`ls "extractions/Tim Runia/"`
returns only `transcript.txt`) and by a per-member scan of
`_archive/claude-export-2026-07-01.tar.gz` for the fragments "Tim Runia" and
"story compass" (see PROVENANCE.md Search Log — no additional hits).

| # | Claim / Quote | Location | Label |
|---|----------------|----------|-------|
| 1 | Core method: Want → Tension → Change → one-sentence Compass ("I wanted ___, but ___, until ___.") | transcript.txt, formula stated near "So, the third step is to write the whole thing down in one sentence... Want but until" | VERIFIED |
| 2 | "there's a big difference between a video and a story" | transcript.txt, opening third of transcript | VERIFIED |
| 3 | Tension can be Internal (emotion/fear/doubt) or External (situation/obstacle), and one can trigger the other | transcript.txt, "It can be internal... But it can also be something external..." | VERIFIED |
| 4 | "tension can be both external and internal at the same time" | transcript.txt, Japan food-market walkthrough | VERIFIED |
| 5 | Change can be internal (realization, faced fear) or external (visible transformation) | transcript.txt, "internal change is when something shifts within the person... external change is when something in the world visibly transforms" | VERIFIED |
| 6 | "Something has to be different at the end than in the beginning." | transcript.txt, change-step explanation | VERIFIED |
| 7 | Compass formula collapses to one sentence; multi-sentence = not ready | transcript.txt, "write the whole thing down in one sentence... it's very simple, but that's your compass" | VERIFIED |
| 8 | "we can still refine the line however we want" | transcript.txt, Japan example refinement beat | VERIFIED |
| 9 | Dig Protocol: weak change ("I just started") gets pushed for the mechanism ("I realized the only way to beat my self-doubt was to just finish one small video first") | transcript.txt, tool-demo section (YouTube self-doubt example) | VERIFIED |
| 10 | Positive tension / anticipation is valid tension (wedding films, reveals) | transcript.txt, "not every story needs an obstacle or a struggle as tension... if it's a wedding, the whole day is building towards one moment" | VERIFIED |
| 11 | "not every story needs an obstacle or a struggle as tension" | transcript.txt, closing section | VERIFIED |
| 12 | "It comes down to three simple steps." | transcript.txt, intro | VERIFIED |
| 13 | Runia built a free tool that walks through the three questions and generates/refines the compass sentence | transcript.txt, "I actually created a tool that helps you with all this because it walks you through the same three questions step by step" | VERIFIED |
| 14 | "you still just have a topic instead of a story" | transcript.txt, tension-step explanation ("without tension, you still just have a topic instead of a story") | VERIFIED |
| 15 | Japan food-market exemplar (want/tension/change/compass, full walkthrough) | transcript.txt, worked example section | VERIFIED |
| 16 | YouTuber self-doubt exemplar (want/tension/weak-change/refined-change, full walkthrough) | transcript.txt, tool-demo section | VERIFIED |
| 17 | Bio: "video director, agency owner, YouTuber" | transcript.txt, "after years of owning a video agency, directing commercials, and now doing YouTube" | VERIFIED |
| 18 | Source video title "Turn ANY Idea Into a Story" (YouTube) | SKILL.md attribution — not independently re-verified against a live YouTube listing this session (no web fetch run); consistent with the transcript's content and framing | LIKELY |
| 19 | Cross-expert stacking claims (Puri, Roth, Connelly, Wright Thompson, Kallaway, Georgi, StoryBrand, Godin) in SKILL.md's Stacking Guide | Not sourced to the Runia transcript — these are system-authored positioning/compatibility claims about how story-compass sequences with other skills in this codebase, not Runia quotes or claims | UNCONFIRMED (system-authored, not attributed to Runia — flagged so it is never read as a Runia quote) |

## Notes
- No dates, timestamps, or upload metadata are present in `transcript.txt`
  itself; the 2026-04-16 extraction date on SKILL.md reflects the file's
  on-disk creation date (`ls -la extractions/Tim Runia/` → Apr 16 08:43), not
  a claim about when Runia recorded the video.
- Every quote in `genius.md` was checked as an exact substring of
  `extractions/Tim Runia/transcript.txt` before being added (see
  PROVENANCE.md for the anchor table).

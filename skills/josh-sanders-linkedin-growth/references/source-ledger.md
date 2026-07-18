# Josh Sanders — Source Ledger

Every claim used in `SKILL.md` and `genius.md`, labeled **VERIFIED** (verbatim
quote confirmed by direct file read this repair), **LIKELY** (accurate
paraphrase, reasonable inference, or the extraction team's own naming of a
verified underlying practice — not a verbatim quote), or **UNCONFIRMED**
(asserted in the skill but not locatable in any source file on this pass —
flagged, never anchored as fact).

**Sources consulted** (both read/greped in full for this repair):
- `extractions/josh-sanders/transcript.txt` — 104,542 bytes (`wc -c`), single
  ~1-hour YouTube/podcast interview transcript with Josh Sanders (Head of
  Content for Chris Donnelly), stored as one unbroken line (`wc -l` = 0 — no
  `\n` characters, confirmed before grepping so line-based `grep -n` wasn't
  trusted; all searches below used Python substring/regex scans over the raw
  text instead).
- `extractions/josh-sanders/extraction-report.md` — 8,902 bytes, the Mastery
  Extraction built from that transcript.
- `extractions/Josh Sanders/transcript.txt` — differently-cased duplicate
  directory, byte-identical (104,542 bytes) to the file above; not a second
  source.
- `extractions/Josh Sanders/extraction-report.md` — 8,160 bytes. **Not**
  byte-identical to `extractions/josh-sanders/extraction-report.md` — this is
  a second extraction *pass* over the same transcript (different pattern
  names/framing: e.g. "Format Arbitrage" vs. "The Pre-Validated Content
  Engine," "5 tacit insights" vs. "3 tacit insights"). Both were read; where
  they diverge, the transcript itself (the primary source) was used to
  arbitrate.

No other extraction files, notebooks, or secondary sources for Josh Sanders
exist in this repo as of this repair (`ls extractions/ | grep -i sanders`
returns exactly the two directories above; `codex-harvest` and the
`claude-export` tarball were not checked because the primary `extractions/`
material is substantial — 104KB transcript + two independent extraction-report
passes — not the "thin" condition that would require the fallback search).

---

## Biographical claims (SKILL.md / genius.md framing)

| Claim | Label | Anchor |
|---|---|---|
| Josh Sanders is "Head of Content for Chris Donnelly" | VERIFIED | transcript.txt: "That's Josh Sanders, head of content for Chris Donnelly, one of the fastest growing LinkedIn pages and personal brands in the world." |
| Grew Chris Donnelly's pages to "over 3 million followers" | VERIFIED | transcript.txt: "Josh reveals how he grew Chris's pages to over 3 million followers on LinkedIn" |
| "Almost $10 million from LinkedIn in the last 18 months" / "$10 million a year education business" | VERIFIED | transcript.txt: "You have made almost $10 million from LinkedIn in the last 18 months working with Chris Donnelly" + "converted that audience to a $10 million a year education business" |
| Follower count was 108,000 when Josh joined, goal of 250,000 in 3 months | VERIFIED | transcript.txt: "when I joined he was at 108,000. Um, we set a goal of like 250,000 by the end of the year, which was 3 months" |
| "Some days genuinely... 50,000 followers in like one day" | VERIFIED | transcript.txt, cold open |
| Nathan Barry (founder of Kit) messaged about the newsletter growth | VERIFIED | transcript.txt: "the founder of Kit, Nathan Barry, was like, he messaged us and was like, 'What are you guys doing?'" |

---

## The 4 Genius Patterns (genius.md)

| Pattern | Label | Anchor |
|---|---|---|
| Format Arbitrage (scan for outlier formats, flood the zone before "best practice") | VERIFIED | transcript.txt: "cuz a lot of the LinkedIn gurus were saying like um you shouldn't have uh links in your post... we were like straight on it. We were like, okay, we've seen it have disproportionate growth for a smaller creator." (link-shortener format example) |
| Pre-Validated Outlier Engineering (rebuild proven posts with 3x depth) | VERIFIED | extraction-report.md Pattern 1, corroborated by transcript.txt's outlier-scanning passages; "10x Depth" / "3x more actionable detail" framing is the extraction team's own metric, not Josh's stated multiplier — LIKELY on the specific "3x" figure |
| Profile-as-Landing-Page (Banner/Tagline/Featured as CTA infrastructure) | VERIFIED | transcript.txt: "you have the banner which sits just above your profile photo... A lot of people actually don't even have a banner or it would just be like some generic one with their logo in the bottom corner" + tagline/featured passages |
| Depth-First Monetization (give away the how-to free, sell the with-you) | VERIFIED | transcript.txt describes the newsletter→waitlist→webinar→cohort sequence and the "50 60 70% of the value people got... was the community" passage on cohort economics |
| Success-metric figures ("5x-10x follower conversion," "profile-visit-to-follower conversion rate > 15%") | UNCONFIRMED | Not located in transcript.txt on this pass. These read as extraction-team-authored target benchmarks illustrating the pattern, not numbers Josh states. Not removed (pre-existing, additive-first scope), but flagged here per the ledger requirement — treat as illustrative, not a verified Josh Sanders claim. |

---

## The 5 Hidden Knowledge items (genius.md)

| Item | Label | Anchor |
|---|---|---|
| "Internal Voice" Readability Test | LIKELY | Not found as a named test verbatim in transcript.txt on this pass; consistent in substance with the transcript's emphasis on scannability and "easy on the eye" reading (paragraph-blocks passage). Named by the extraction team. |
| Pattern Interrupt via "Ugly" Numbers, incl. the "318,842" example | VERIFIED | transcript.txt: "I've studied over 318,842 LinkedIn posts. That sounds like a weird amount of hosts... that genuinely that was the data set... a lot of people would go, 'Oh, no. Let's just have like [a round number]'" — Josh's own stated example of a specific, non-rounded number and why it works |
| "Line-Paragraph-Line" Hook Physics | LIKELY | Consistent with transcript.txt's hook/white-space passage ("we'll write in lines of 1, two, and three... so that there's lots of white space") but the "Line-Paragraph-Line" label itself is extraction-team naming, not a Josh Sanders term found verbatim |
| "30/30/30/10" Engagement System (4-way split incl. 10% Friends/Supporters) | LIKELY | transcript.txt names the system "30 3010" (transcribed as "30/30/10") and describes 3 buckets explicitly — large creators (30%), industry peers, and ICPs — the exact percentage for peers/ICPs and the 4th "10% Friends/Supporters" bucket are not stated as cleanly in the passage located during this repair. The underlying practice (allocate outbound engagement by target type) is VERIFIED; the specific 4-way "30/30/30/10" split as currently written in genius.md/SKILL.md is the extraction team's fuller reconstruction — treat the exact ratios as LIKELY, not a verbatim Josh Sanders breakdown. |
| The "Gravedigger" Detail (mix failure/storytelling content with data-driven cheat sheets) | LIKELY | Consistent with transcript's "a bit of transparency on a failure" exchange and the broader depth/authenticity thread; the "Gravedigger" label is extraction-team naming |

---

## Anti-Patterns (genius.md — this repair's addition)

All 6 anti-pattern bullets carry an inline verbatim quote from
`extractions/josh-sanders/transcript.txt`, confirmed by direct string search
during this repair — see `genius.md` → "Anti-Patterns (Josh Sanders would
reject these)" for the paired quote + anchor per item. Summary:

| Anti-pattern | Label |
|---|---|
| Selling the deliverable, not the wins (About section under-bragging) | VERIFIED |
| One repeated storytelling format mistaken for a system | VERIFIED |
| Over-personal posts that can't survive a Slack forward | VERIFIED |
| Dense paragraph blocks instead of scan units | VERIFIED |
| Generic, CTA-less banner | VERIFIED |
| Taking "no links in posts" guru consensus at face value | VERIFIED |

---

## Hall of Fame Exemplars (genius.md, pre-existing — not modified this repair)

| Element | Label | Note |
|---|---|---|
| Exemplar 1 & 2 body copy ("7-Figure LinkedIn Funnel Blueprint" carousel, "Hyper-Optimized Profile") | UNCONFIRMED as literal Josh Sanders/Chris Donnelly output | These are illustrative constructed exemplars demonstrating the patterns, not verbatim posts pulled from the transcript or a real Chris Donnelly post. The specific figures inside them ("4.2 hours/week," "< 0.08% engagement," "20% repost rate" is a real transcript figure but appears in a different context — see below) are extraction-team-authored illustration, not sourced Josh Sanders data. Pre-existing content, out of this repair's scope to rewrite, flagged here for auditability. |
| "20% repost rate within the first hour" (mentioned in genius.md rubric context, not the exemplar) | VERIFIED (as a real Josh Sanders data point, though not the exemplar's own number) | transcript.txt: "we had posts that within the first hour were hitting like a 20% repost rate. We were like, okay, this is going to bang." |

---

## Verification method

Every VERIFIED quote in this ledger and in `genius.md`'s new Anti-Patterns
and Model Calibration sections was confirmed by a direct Python
substring/regex scan over `extractions/josh-sanders/transcript.txt` (104,542
bytes, confirmed via `wc -c` — the file has zero newline characters per
`wc -l`, so line-based tooling was not used) during this repair session,
2026-07-18. The transcript itself carries no internal timestamps or dates;
the 2026-03-02 date on the biographical/pattern claims above is the file's
git-add date (`git log --diff-filter=A -- extractions/josh-sanders/transcript.txt`),
used as the ingestion-date anchor, not a claim about when the interview was
recorded. LIKELY and UNCONFIRMED labels reflect items not locatable as exact
strings in this pass — not a claim that the material is absent from Josh
Sanders's broader body of work, only that this repair could not anchor them
to the one source file this skill was built from.

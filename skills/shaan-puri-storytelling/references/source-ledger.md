# Source Ledger — shaan-puri-storytelling

Claim-by-claim provenance for genius.md. Labels: **VERIFIED** (quote/fact opened
and confirmed verbatim in the cited source by this repair pass), **LIKELY**
(consistent with cited source but not independently confirmed against a
primary record — e.g., interviewer identity), **UNCONFIRMED** (no source file
located; flagged, not anchored, not presented as fact).

## Primary source

**"Shaan Puri: Masterclass in Storytelling (for beginners)"** — a Merlin-AI
transcript of a YouTube interview (attachment: `https://www.youtube.com/watch?v=Z2BnqYArwaw`),
uploaded 2025-09-15, captured in `claude-export/normalized/conversations/
c1749a67-aa1d-4afb-b3f3-ae69b4b26145.md` inside `_archive/claude-export-2026-07-01.tar.gz`
(332MB; no `extractions/` folder exists for this expert — confirmed by
`ls extractions/ | grep -i "puri\|shaan"` returning nothing, then a
per-member content scan of the archive tarball, which surfaced 12 conversation
exports referencing this same transcript; this one carries the full raw
timestamped transcript as an attachment, the others are downstream
Claude-generated skill drafts). File size 158,270 bytes (`wc -c`), read in
full for this repair.

- **VERIFIED** — Every timestamped quote added to genius.md in this repair
  pass (Core Philosophy yin-yang line 37:19; Pattern 1 "altar of intention and
  obstacle" 7:05, Harry Potter/Voldemort 7:38, croissant 8:37; Pattern 2
  "five-second moment of change" 0:00; Pattern 3 Clubhouse jargon/homework
  21:58–22:29 and the ~20M-reader figure; Pattern 4 "LOL, WTF, OMG" 0:04;
  Pattern 5 "Jenny in her bedroom" / "Debbie at her desk" 43:05–43:59; Pattern
  6 "low status game" 12:33 and the dinner-party failure 12:02; Pattern 7 Dave
  Chappelle/Netflix "these two stories" 75:26–75:51; Pattern 8 "physiology
  first, focus second, story third" 54:15 and the poker-player wind-sprints
  52:05; all six Anti-Patterns items) was opened directly against this file
  and matches verbatim, including the timestamp markers.
- **VERIFIED** — The pre-existing "Patterns from claude.ai export" block
  (genius.md, Patterns A–J, added 2026-07-01) was spot-checked against this
  same transcript during this repair: "Binge Bank" (lines 79–137 of the
  transcript), "it's the arbitrage" (line 1242), "physiology, focus, story"
  order (line 1319), Tony Robbins bathtub/hard-chair anecdote (lines 965–995),
  "I can't unhear that" (line 1310) — all confirmed present and accurate.
  These were already correctly attributed before this repair; not re-anchored
  here since they already carried inline citations that pass the auditor.
- **LIKELY** — The interviewer is credited as David Perell (already stated in
  genius.md line 172 pre-repair, and consistent with "David" being addressed
  directly at several points in the transcript, e.g. lines 101 and 1300).
  This repair did not independently verify the interviewer's identity against
  an external record (no web fetch performed); treat as likely-correct
  attribution inherited from the prior extraction pass, not newly confirmed.

## Secondary / supporting files (read, not quoted into genius.md)

- `agents/shaan-puri/AGENT.md` — **UNCONFIRMED** for the biographical claims
  "sold the Milk Road newsletter for 8 figures" and "400K+ Twitter following."
  Neither figure appears in the transcript source and no other file in this
  repo corroborates them. Not carried into genius.md by this repair. If used
  elsewhere in the skill, they should be labeled UNCONFIRMED or removed.
- `research_outputs/ai_authority_architect_agents/shaan_puri.md` — a
  Farrice-specific applied dossier (client stories, hooks), not a source of
  Shaan Puri's own teaching. Its own grounding-verification addendum
  (2026-06-02) already flags its "client quotes" as `[MODELED]`/unsourced.
  Not used as source material for this repair.
- `.agent/evolution-logs/2026-04-09-shaan-puri-storytelling-transformation-isomorphism.md`
  — internal A/B benchmark that originally justified Pattern 9
  (Transformation Isomorphism). Confirms Pattern 9 was added via a scored
  evolution cycle, not fabricated; not a Shaan Puri primary source, so not
  cited as one.

## Method note

Per the wave envelope's source-search discipline: `extractions/` was checked
first (no match on "puri" or "shaan" fragments), then the archive tarball was
scanned per-member by content (not filename) using `python3 tarfile`, first
broadly ("shaan|puri" — 103 hits, mostly false positives from words like
"purity"), then narrowed to distinctive terms ("shaan puri", "milk road",
"masterclass in storytelling" — 27 hits), then confirmed which of those hits
contained the actual raw transcript versus downstream drafts. No claim of
source absence is made anywhere in this ledger without that scan having run.

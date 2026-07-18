# Robert Greene — Power & Mastery — Source Ledger

Claim-by-claim provenance for `genius.md` (and the Quick Reference bullets in
`SKILL.md`, which restate the same patterns). Labels: **VERIFIED** (checked
this repair pass against an external, citable bibliographic/publication
record, or verbatim-present in this skill's own pre-repair files),
**LIKELY** (source-consistent paraphrase or reasonable synthesis with no
single verbatim anchor), **UNCONFIRMED** (attributed to a real, located
primary source whose exact wording was not checked this pass — carried
forward anyway, flagged so it is never mistaken for a verified transcript
quote).

## Sources Consulted (this repair pass, 2026-07-18)

**Repo search — no local transcript exists.**
```
ls extractions/ | grep -i greene   → no matches
grep -rl "Ego Traps" . --include="*.md" -not path skills/robert-greene-power-mastery → no independent hits
find . -iname "*claude.ai*export*" → no matches (SKILL.md's stated
  "source: claude.ai export 2026-07-01" is not a locatable file in this repo)
```
Confirmed by direct commands this session, not inference. No 0-byte or
"unrecoverable" file was found and then dismissed — the search simply
returns no results for this expert anywhere outside this skill's own
generated files (`skills/robert-greene-power-mastery/`,
`agents/robert-greene/memory/context.md`, `.claude/commands/robert-greene*.md`
— all downstream copies of the same house-authored material, not
independent sources).

**External verification — this is a BOOK-framework skill; raw book/podcast
text is deliberately absent from the repo, so ground truth for the
checkable layer is publication bibliography, verified via WebSearch this
repair pass (not training memory):**

| ID | Claim checked | Result | Source |
|----|---|---|---|
| B1 | *The 48 Laws of Power* — Robert Greene, hardcover 1998, Viking Penguin (paperback Penguin, 2000) | VERIFIED | [Wikipedia](https://en.wikipedia.org/wiki/The_48_Laws_of_Power), [Penguin Random House](https://www.penguinrandomhouse.com/books/330912/the-48-laws-of-power-by-robert-greene/) |
| B2 | *The Art of Seduction* — Robert Greene, 2001 | VERIFIED | WebSearch result set, corroborated across Amazon/Goodreads/PRH listings |
| B3 | *The 33 Strategies of War* — Robert Greene, 2006, Viking Penguin (US) / Profile Books (UK) | VERIFIED | [Wikipedia](https://en.wikipedia.org/wiki/The_33_Strategies_of_War), [Penguin Random House](https://www.penguinrandomhouse.com/books/291190/the-33-strategies-of-war-by-robert-greene/) |
| B4 | *Mastery* — Robert Greene, published 2012-11-13, Viking Adult; profiles Paul Graham as one subject | VERIFIED | [Wikipedia](https://en.wikipedia.org/wiki/Mastery_(book)), [Internet Archive full text](https://archive.org/details/0000000RobertGreeneMasteryVikingPenguinGroup2012), [Biblio](https://www.biblio.com/book/mastery-greene-robert/d/1435638922) |
| B5 | *The 50th Law* — Robert Greene & 50 Cent (Curtis Jackson), 2009, Amistad | VERIFIED | [Wikipedia](https://en.wikipedia.org/wiki/The_50th_Law), [Amazon listing](https://www.amazon.com/50th-Law-50-Cent/dp/006177460X) |
| B6 | *The Laws of Human Nature* — Robert Greene, published 2018-10-23, Viking | VERIFIED | [Penguin Random House](https://www.penguinrandomhouse.com/books/317474/the-laws-of-human-nature-by-robert-greene/), [Amazon listing](https://www.amazon.com/Laws-Human-Nature-Robert-Greene/dp/0525428143) |
| P1 | Podcast episode "Robert Greene - Ego Traps, The Art of Control, & How to Stay Irreplaceable" is a real, dated release (Open Residency podcast, released 2025-10-14, ~1h20m) | VERIFIED (episode exists) / UNCONFIRMED (verbatim content — no transcript fetched this pass) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/robert-greene-ego-traps-the-art-of-control-how-to/id1791782856?i=1000731808198), [Spotify](https://open.spotify.com/episode/0Wd5TuVOBl7PhDO09xZC5U), [YouTube](https://www.youtube.com/watch?v=-1aSoZ1ffTg) |

**Scope note**: fetching and reading the full podcast transcript was judged
out of scope for this bounded heartbeat-repair pass (fixing 3 named checks,
minimal-touch) versus a full re-extraction. P1 upgrades the source from
"unlocatable" to "real and datable" — a meaningfully stronger footing than
"no source found at all" — but does not upgrade any individual quote below
past UNCONFIRMED, since no transcript was read word-for-word against them.

## Claims — genius.md, Genius Patterns (pre-existing, unmodified this pass)

| Claim | Label | Anchor |
|---|---|---|
| All 9 Genius Patterns (Master Law through Outward Focus) and all 4 Hidden Knowledge insights | UNCONFIRMED (verbatim precision) / LIKELY (content plausibility — internally consistent with each other and with Greene's published bibliography, e.g. the Paul Graham/Mastery cross-reference in B4) | Pre-existing `genius.md` (S1, this skill, unmodified content); P1 confirms the interview is real but its exact wording was not checked this pass. |
| 50 Cent observation anecdote ("Silence as Leverage") | LIKELY | Corroborated by B5 — Greene co-authored a full book with 50 Cent (*The 50th Law*, 2009), so direct access/observation is plausible and bibliographically grounded, though the specific meeting anecdote itself is UNCONFIRMED against a transcript. |
| Paul Graham combination example ("Mastery Is Combination, Not Depth Alone") | VERIFIED (Paul Graham is a documented subject of *Mastery*) / UNCONFIRMED (the specific "programming + painting" framing as Greene's exact words) | B4 confirms Paul Graham appears in *Mastery*; the paraphrase of his story is not verbatim-checked. |

## Claims — genius.md, "Anti-Patterns (Sourced)" (new section, this repair pass)

| Claim | Label | Anchor |
|---|---|---|
| Never assume more talk equals more control | UNCONFIRMED (quote precision) / VERIFIED (quote is verbatim-present in this file's pre-repair Silence as Leverage pattern) | `genius.md` Pattern: Silence as Leverage (pre-existing); P1 (episode exists). |
| Never defend a signature strength past its shelf life | UNCONFIRMED (quote precision) / VERIFIED (pre-existing text) | `genius.md` Pattern: Formlessness Over Signature Strength (pre-existing); P1. |
| Never approach a powerful person with appeals to gratitude | UNCONFIRMED (quote precision) / VERIFIED (pre-existing text) | `genius.md` Pattern: Appeal to Self-Interest, Never Mercy (pre-existing); P1. |
| Never accept a "free" offer at face value | UNCONFIRMED (quote precision) / VERIFIED (pre-existing text) | `genius.md` Pattern: Despise the Free Lunch (pre-existing); P1. |
| Never run permanent concealment inside your own team | UNCONFIRMED (quote precision) / VERIFIED (pre-existing text) | `genius.md` Pattern: Selective Concealment (pre-existing); P1. |
| Never treat a law as fixed regardless of terrain | VERIFIED | B1, B2, B3, B4, B6 — six distinct law-systems published 1998–2018, each re-deriving rules for new terrain rather than reissuing one book; this is a bibliographic fact, not a quote. |

## Claims — genius.md, "How to Use This Skill (Model Calibration)" (new section, this repair pass)

Craft/voice guidance authored for this repair, modeled structurally on
`skills/ben-watkins-storytelling/genius.md` lines 7-16 per the batch
envelope — not itself a factual claim about Greene, so no VERIFIED/LIKELY/
UNCONFIRMED label applies to the calibration instructions. The one quote it
repeats ("sometimes you need to do the opposite") is pulled directly from
the pre-existing, pre-repair `genius.md` line 3 — same UNCONFIRMED
(quote-precision) status as above.

## Summary

- **VERIFIED**: 6 book/publication facts (B1–B6) checked externally this
  pass, plus the podcast episode's real-world existence (P1) and the fact
  that several Anti-Pattern quotes are verbatim-present in this skill's own
  pre-repair file (internal-consistency VERIFIED, distinct from
  transcript-verbatim VERIFIED).
- **UNCONFIRMED**: exact wording of every quote attributed to the *Ego
  Traps* podcast — the episode is real and dated (upgraded from "no source"
  to "real, unfetched source" this pass) but no transcript was read
  word-for-word against them.
- **No claim was invented this repair pass.** Every new Anti-Pattern item
  either restates a quote already verbatim-present in the pre-repair
  `genius.md`, or cites an externally checkable publication fact (B1–B6)
  not previously in the file. Nothing here claims book prose was consulted
  directly — none was; the book-fact anchors are bibliographic metadata
  only (title/author/year/publisher), never quoted text from inside the
  books themselves.

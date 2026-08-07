# Jonathan Franzen — Source Ledger

Claim-by-claim provenance for `skills/jonathan-franzen-storytelling/genius.md`.
Labels: **VERIFIED** (confirmed against a primary source, quote checked verbatim) ·
**LIKELY** (real, well-documented, but not verbatim-confirmed this session) ·
**UNCONFIRMED** (no ground-truth source found; illustrative/synthetic only).

## Primary source discovery (read this before the rest of the ledger)

- `extractions/` has **no `jonathan-franzen*` directory** (`ls extractions/ | grep -i franzen` = empty). Only incidental mention: `extractions/steven-pressfield/extraction-report.md` (27,217 bytes) name-drops Franzen once as a cross-expert synergy note — not a Franzen source.
- `_active/harness/codex-harvest-2026-06-11/skills/jonathan-franzen-storytelling/genius.md` (13,738 bytes) and `_active/harness/codex-harvest-2026-06-11/agents/jonathan-franzen/AGENT.md` (3,428 bytes) exist but are an **earlier mirror of this same synthetic skill**, not an independent source — `diff` against the current `skills/jonathan-franzen-storytelling/genius.md` shows the only difference is the missing "How to Use This Skill" calibration block. Confirmed via byte-for-byte diff, not assumed.
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes / ~317MB) — a filename-only listing (`tar -tzf ... | grep -i franzen`) found nothing, which would have supported a false "no source" claim. Per the envelope's rule #2, a **content** grep was run instead: `tar -xzOf ... | grep -a -c -i franzen` → **83 hits**. Extracting the archive (1.1GB uncompressed, 3,864 files) and grepping by content located the real source:
  - `claude-export/normalized/conversations/147f009c-5f9f-48fa-87df-89381c48dcbb.md` (140,642 bytes) — a full MES 3.0 extraction conversation titled "Jonathan Franzen | Learn to Write Great Stories in 63 Minutes," containing the **complete verbatim transcript** of a real YouTube interview, pasted in as an attachment at line 30, followed by the assistant's extraction work that produced (in an earlier session) the same 7 patterns now in `genius.md`. This is very likely the actual origin conversation for this skill.

**This changes the grounding status of the whole skill**: it is not ungrounded — the primary source exists, just not inside `skills/` or `extractions/`. All 7 Genius Patterns and all 6 Anti-Patterns below are now anchored to this transcript.

## VERIFIED (primary source, quote checked against the file this session)

| Claim / Pattern | Quote (verbatim, exact substring) | Anchor |
|---|---|---|
| Video identity, speaker, date | "Learn to Write Great Stories in 63 Minutes — Jonathan Franzen," How I Write w/ David Perell, YouTube, published 2025-11-26 | Confirmed via WebSearch this session: youtube.com/watch?v=7fpr4055HBY |
| Pattern 1 (Comic Problem Genesis) | "I'm looking for a comic problem. It doesn't have to be a big problem... the smaller the problem, the funnier it is" | conv. 147f009c…, ln. 30 |
| Pattern 2 (Comic Distance) | "distance is really really critical" / "if you stick close to a character who the author is convinced is a victim... you're in trouble. On page one" | conv. 147f009c…, ln. 30 |
| Pattern 3 (Shame-to-Comedy) | "There's no technical solution to shame levels in a writer... you have to go into the shame" / "one of the reflexes then is to just kind of pile on the ugliness" | conv. 147f009c…, ln. 30 |
| Pattern 4 (Minimal Detail) | "less than one page devoted to describing the weather" / "two sentences are really all you need to establish what you need for a minor character" | conv. 147f009c…, ln. 30 |
| Pattern 5 (Want-Collision) | "One character wants you to get on a plane. The other character really has no intention of getting on a plane... that's drama basically" | conv. 147f009c…, ln. 30 |
| Pattern 6 (Iron Bridge) | "there's a there's a, you know, iron bridge up to that point" / "I kind of know what direction the bridge is pointing" | conv. 147f009c…, ln. 30 |
| Pattern 7 (Organic Plot) | "a book that was too fully planned is likely to read like a book that was too fully planned... that's the last impression you want to give" | conv. 147f009c…, ln. 30 |
| Anti-pattern: cliché ceiling | "you get at most one cliche per book... I read along until I get to the second cliche and I say, 'Thank you'" | conv. 147f009c…, ln. 30 |
| Anti-pattern: trauma-dumping | "very much focused on the self... incompatible with forging the kind of bond I want to forge with the reader" | conv. 147f009c…, ln. 30 |
| Anti-pattern: fourth-wall break | "a lot of experimental fiction delights in breaking the fourth wall... takes you out of the experience" | conv. 147f009c…, ln. 30 |
| Anti-pattern: ornamental description | "merely describing the beauty of nature will not get the job done... tedious, boring" | conv. 147f009c…, ln. 30 |
| Biographical facts | National Book Award winner; author of *The Corrections*, *Freedom*, *Crossroads* | Common public record; not independently re-verified this session (see LIKELY) |

## LIKELY (real and well-documented externally; confirmed via live WebSearch/WebFetch this session, but not a repo-local file)

- Franzen's "Ten Rules for Writing Fiction" (10 numbered rules incl. "Never use the word *then* as a conjunction," "Fiction that isn't an author's personal adventure into the frightening or the unknown isn't worth writing for anything but money") — originally The Guardian, 2010; confirmed list reproduced at Lit Hub, Nov 15 2018 (collected in *The End of the End of the Earth*, FSG, 2018). Not used as a quoted anchor in genius.md (kept out to avoid mixing two interviews); recorded here for completeness only.
- "Mr. Difficult" — Franzen's essay on William Gaddis and reader-hostile "Status" vs. reader-friendly "Contract" fiction — The New Yorker, Sept 30, 2002 (collected in *How to Be Alone*, 2002). Not used as a quoted anchor; background only.
- Paraphrase (not verbatim — WebFetch of the source page returned HTTP 403) that in the Paris Review's "The Art of Fiction No. 207," Franzen describes avoiding outlines in favor of setting himself a near-impossible problem to solve while drafting. Consistent with the VERIFIED organic-plot quote above but not independently confirmed verbatim this session — do not cite as a direct quote.
- National Book Award year (2001, for *The Corrections*) — standard public record, not re-verified against a primary document this session.

## UNCONFIRMED (no ground-truth source; synthetic/illustrative, labeled as such in-file)

- **Hall of Fame Exemplar 1** ("The Embarrassingly Specific Neurosis," Alfred Lambert door-locks passage) — genius.md itself labels this "reconstructed," meaning it is NOT a verbatim excerpt from *The Corrections*. It is an illustrative pastiche written to demonstrate Pattern 1/4/5. Treat as UNCONFIRMED-as-canon-text.
- **Hall of Fame Exemplar 2** ("The Subtext of the Family Dinner") — explicitly labeled "Generated from Franzen's patterns" in-file. Synthetic, not a real Franzen passage. UNCONFIRMED-as-canon-text.
- The specific claim that Franzen "may have done a deep dive into self-analysis and flounder[ed] for 6 months" while writing *The Corrections* (mentioned in the transcript by Franzen himself, conv. 147f009c…, ln. 30) is VERIFIED as something Franzen said in the interview, but his underlying account of his own drafting history is self-report, not independently fact-checked here — treat the anecdote as Franzen's own claim, not an audited biographical fact.

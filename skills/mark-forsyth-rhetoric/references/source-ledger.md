# Source Ledger — mark-forsyth-rhetoric

Rewritten 2026-08-06 at the forge. **The defect this ledger previously recorded is fixed.**

The 2026-07-18 version of this file stated: *"no raw source material exists for this expert in
`extractions/`"* — the skill had been built from a transcript read in an earlier session and discarded, so
every genius-pattern quote carried an UNCONFIRMED label that could never be resolved. Both interviews are
now fetched and retained on disk, and every pattern has been re-adjudicated against real text.

## Primary sources — retained, re-read in full 2026-08-06

| Source | Path | Words | Status |
|---|---|---|---|
| David Perell, *How I Write* — "Writing Techniques I Wish I Knew Earlier (Mark Forsyth Interview)", YouTube `6ZNCJH8jJD0`, published 2026-08-05, 1:13:49 | `extractions/mark-forsyth/2026-08-05-perell-second/transcript.txt` | 12,757 | **VERIFIED** present and read in full |
| David Perell, *How I Write* — "You're Using the English Language Wrong — Mark Forsyth", YouTube `ulhrXgpjveA`, published 2024-07-24 | `extractions/mark-forsyth/2024-07-24-perell-first/transcript.txt` | 9,610 | **VERIFIED** present and read in full |

A publisher transcript of the 2026 episode also exists at
`howiwrite.substack.com/p/mark-forsyth-stop-writing-like-they` (episode title *"Mark Forsyth: Stop Writing
Like They Taught You in School"*, published 2026-08-05).

## The standing caveat — read before quoting

Both retained transcripts are **YouTube auto-generated captions**, not publisher transcripts. Consequences,
stated plainly:

- Substance is reliable. **Wording is not word-perfect.**
- Speaker attribution is inferred from context; in a two-person interview the captions do not label turns.
- Proper nouns are frequently garbled. Twenty corrections are catalogued in
  `extractions/mark-forsyth/SOURCE-MANIFEST.md`.
- **Therefore**: no line in `genius.md` may be presented as a verbatim Forsyth quotation. Lines quoted in
  skill files are substance-accurate paraphrase-or-near-quote traceable to a specific passage. Where
  `genius.md` uses quotation marks around Forsyth's speech, read them as "he said this, in these words, per
  an ASR caption" — not as publishable attributed quotation. For anything going to a client or to print,
  re-source against the Substack transcript.

## Status of the pre-forge patterns

All ten genius patterns carried over from the pre-forge skill (memory-receptor shaping, progressio, diacope,
chiasmus, the announcer signal, tricolon, polyptoton, anadiplosis, the alliteration upgrade, voice as
establishing shot) were checked line by line against the 2024 transcript. **All ten are confirmed present in
the source.** The earlier extraction was accurate; it simply could not prove itself. Nothing was overturned.

Fourteen figures and one thesis were added from the 2026 interview: isocolon, epistrophe, epanalepsis,
epizeuxis, synesthesia, personification, schesis onomaton, paradox, pun-paradox, veridical paradox,
hyperbole, adynaton, the periodic sentence (2024, previously unextracted), pull-through architecture, and
the enchantment-over-efficiency thesis with the grammar/glamour etymology.

## Corrections — an expert's on-air slip is not licence to repeat it

| Claim as spoken | Correct | Basis |
|---|---|---|
| "Moses' **wife**… says 'I have been a stranger in a strange land'" | **Moses** says it — Exodus 2:22, naming Gershom | **VERIFIED** KJV, 2026-08-06 |
| "we are the dreamers of dreams" attributed to a garbled name | **Arthur O'Shaughnessy**, "Ode," 1873 | **VERIFIED** Poetry Foundation, 2026-08-06 |
| "Chile Cooper" (all-senses writing tip) | **Jilly Cooper**, novelist, 1937–2025 | **VERIFIED** Penguin/Deadline obituaries, 2026-08-06 |

Full ASR correction table in the source manifest.

## UNCONFIRMED — never present as verified

1. **The "drop of salt water from the Golden Gate to Hong Kong" line as Dashiell Hammett's.** Targeted search
   2026-08-06 could not locate it in *The Maltese Falcon*, *The Glass Key*, or any indexed Hammett quotation
   set. Use only as *"a line Forsyth attributes to Hammett."*
2. **The Russian word for a deadline burst of work.** Forsyth: "I don't really speak Russian." Do not
   reproduce a spelling.
3. **Churchill's exact "we shall fight" ordering.** Forsyth says on air "I forget the exact wording." Cite the
   figure (anaphora), not the word order.
4. **Henry VIII's last words as "monks, monks, monks."** Forsyth flags it himself — "never said that or
   anything like it." Reproduce only as an example of memory improving phrases.
5. **Any claim that a `genius.md` line is word-for-word Forsyth.** See the standing caveat.
6. ***Rhyme and Reason*** publication details — discussed at length in the 2026 interview, cover art on
   `blog.inkyfool.com`. **LIKELY** real; publisher and release date not independently verified this session.

## Publication facts (carried forward, verified 2026-07-18)

- ***The Elements of Eloquence: How to Turn the Perfect English Phrase*** — Icon Books, UK, 2013; US edition
  Berkley/Penguin Random House, ISBN 9780425276181. **VERIFIED**
- ***The Etymologicon*** — Icon Books, late 2011. **VERIFIED**
- ***The Horologicon*** — Icon Books, 2012. **VERIFIED**
- *The Elements of Eloquence* is a **descriptive catalog**, not a prescriptive style guide — compiled by
  combing the British Library for where each figure had already occurred. Presenting it as "the rules"
  misstates its own method.

## Blind-pass reference corpus

Two verbatim published Forsyth pieces, neither quoted anywhere in this skill (required by
`directives/embodiment-standard.md` step 2 — the pass judges against *unseen* work):

- `extractions/mark-forsyth-rhetoric/reference-corpus/substack-the-sentimental-and-how-to-write.md` (2026-07-14)
- `extractions/mark-forsyth-rhetoric/reference-corpus/substack-cutthroat-compounds.md` (2026-06-30)

Both from `markforsythauthor.substack.com`, retrieved 2026-08-06.
`blind_pass.py prepare --expert mark-forsyth-rhetoric` → CORPUS READY.

## Excluded material

The 2026 transcript contains a read sponsor advertisement (Alpha School, ~250 words, including a literacy
statistic). It is host-read sponsor copy, not Forsyth's material, and no claim inside it enters this skill.

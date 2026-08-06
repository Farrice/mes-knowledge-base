# Source Manifest — Mark Forsyth

Retained source material for `skills/mark-forsyth-rhetoric`. Created 2026-08-06.

**Why this file exists.** Before this forge, the skill's own `references/source-ledger.md` recorded:
*"no raw source material exists for this expert in `extractions/`"* — every genius-pattern quote was
labeled UNCONFIRMED because the transcript had been read in an earlier session and thrown away. Both
interviews are now retained on disk and every claim below is adjudicated against them.

## Primary sources (retained, verbatim)

| # | Source | Path | Words | Status |
|---|--------|------|-------|--------|
| 1 | **"Writing Techniques I Wish I Knew Earlier (Mark Forsyth Interview)"** — David Perell, *How I Write*, YouTube `6ZNCJH8jJD0`, published 2026-08-05, runtime 1:13:49 | `2026-08-05-perell-second/transcript.txt` | 12,757 | **VERIFIED** — fetched via `execution/fetch-transcript.py` from YouTube auto-captions, 2026-08-06 |
| 2 | **"You're Using the English Language Wrong — Mark Forsyth"** — David Perell, *How I Write*, YouTube `ulhrXgpjveA`, published 2024-07-24 | `2024-07-24-perell-first/transcript.txt` | 9,610 | **VERIFIED** — fetched via `execution/fetch-transcript.py`, 2026-08-06. This is the source the pre-forge skill was built from and never retained. |

**Transcript caveat (applies to both):** these are YouTube **auto-generated captions**, not publisher
transcripts. Speaker attribution is inferred from context, and proper nouns are frequently garbled by ASR
(see Corrections below). Wording is reliable for *substance*, unreliable for *verbatim quotation of
Forsyth's own sentences*. Any line presented as a direct Forsyth quote in skill files must be traceable to
a passage here and should be read as substance-accurate, not word-perfect. A publisher transcript of
source 1 also exists at `howiwrite.substack.com/p/mark-forsyth-stop-writing-like-they` (episode title:
*"Mark Forsyth: Stop Writing Like They Taught You in School"*).

## Blind-pass reference corpus (real published Forsyth prose, unquoted by the skill)

| Piece | Path | Published |
|---|---|---|
| "The Sentimental (and how to write it)" | `../mark-forsyth-rhetoric/reference-corpus/substack-the-sentimental-and-how-to-write.md` | 2026-07-14 |
| "Cutthroat Compounds" | `../mark-forsyth-rhetoric/reference-corpus/substack-cutthroat-compounds.md` | 2026-06-30 |

Both from `markforsythauthor.substack.com`, retrieved verbatim 2026-08-06. Neither is quoted anywhere in
the skill — required by `directives/embodiment-standard.md` Blind-Pass Protocol step 2 (the pass judges
against *unseen* work). `blind_pass.py prepare --expert mark-forsyth-rhetoric` → CORPUS READY.

---

## Corrections applied (Forsyth misspoke, or ASR garbled the name)

These are fixed wherever the material enters `genius.md`. Encoding them uncorrected would propagate a
fabrication under an expert's name.

| Transcript says | Correct | Basis |
|---|---|---|
| "**Moses' wife** in the Bible… she says 'I have been a stranger in a strange land'" (source 1) | **Moses** says it — Exodus 2:22, on naming his son Gershom. Zipporah bears the son; she does not speak the line. | **VERIFIED** — KJV Exodus 2:22, checked 2026-08-06 |
| "**Douggee Bates** / WB — we are the dreamers of dreams" (sources 1, 2) | **Arthur O'Shaughnessy**, "Ode," 1873 (collected in *Music and Moonlight*, 1874): "We are the music makers, / And we are the dreamers of dreams" | **VERIFIED** — Poetry Foundation, Wikipedia, 2026-08-06 |
| "Chile Cooper" (source 1) | **Jilly Cooper**, novelist, 1937–2025 (died 5 Oct 2025, aged 88); *Rivals* adapted by Disney+ | **VERIFIED** — Penguin, Deadline obituaries, 2026-08-06 |
| "Raymond Charger" (source 1) | **Raymond Chandler** | ASR garble, unambiguous from context |
| "Estachio Hammet" (source 1) | **Dashiell Hammett** — but see UNCONFIRMED below | ASR garble |
| "kayasmus / kasmus / kiasmos" | **chiasmus** | ASR |
| "apistrophe / aistrophe" | **epistrophe** | ASR |
| "anafa / anafer" | **anaphora** | ASR |
| "polypoton / polip tooned / pop toon" | **polyptoton** | ASR |
| "senesthesia" | **synesthesia** | ASR |
| "cis onaton / skis on" | **schesis onomaton** | ASR |
| "Adinaton / Adin Aron" | **adynaton** | ASR |
| "Isa colon / nicer colon" | **isocolon** | ASR |
| "infolkinfur" (source 1) | **"Ein Volk, ein Reich, ein Führer"** — Nazi slogan; literally *one people, one realm, one leader*. Forsyth's on-air gloss ("one state one people one leader") reorders it. | ASR + standard reference |
| "litus / Lycidas" | **"Lycidas"**, John Milton, 1637 | ASR |
| "stos China" (source 2) | Russian term for a deadline burst of work — **UNCONFIRMED**, see below | ASR, unrecoverable |

## Explicit UNCONFIRMED items — never present these as verified

- **"He could have shadowed a drop of salt water from the Golden Gate to Hong Kong without ever losing
  sight of it."** Forsyth attributes this to Dashiell Hammett (source 1). **UNCONFIRMED** — targeted web
  search on 2026-08-06 could not locate this line in *The Maltese Falcon*, *The Glass Key*, or any indexed
  Hammett quotation set. Use only as *"a line Forsyth attributes to Hammett"* — never as verified Hammett prose.
- **The Russian word** for "a sudden burst of activity just before a deadline" (source 2). Forsyth himself
  says *"I don't really speak Russian but that's as far as I could tell."* ASR renders it "stos China."
  **UNCONFIRMED** — do not reproduce a spelling.
- **Churchill's "we shall fight" ordering.** Forsyth narrates it as geographically closing in (sea → air →
  beaches → fields → cities → hills) and says on air *"I forget the exact wording of the speech."* His
  *reading* (the enemy getting closer) is his interpretation, not a quotation. **UNCONFIRMED as a quote**;
  cite the rhetorical figure (anaphora), not the word order.
- **"Henry VIII's last words were 'monks monks monks'"** (source 2). Forsyth flags it himself in the same
  breath: *"never said that or anything like it."* He offers it as an example of the memory-improves-phrases
  effect, not as history. Reproduce only with that framing.
- Any claim that a sentence in `genius.md` is a **word-for-word** Forsyth quote — these are ASR captions.
  Substance-accurate; not word-perfect.

## Verified in-transcript claims safe to use

- Churchill's actual first-speech-as-PM line was **"blood, toil, tears and sweat"**, popularly remembered as
  "blood, sweat and tears" — Forsyth's own example of memory improving a phrase. (Consistent across both sources.)
- **"Fly, my pretties, fly!"** is not in *The Wizard of Oz* — Forsyth's flagship false-memory case, stated in
  both interviews.
- **grammar / glamour** share a root: a *grammar* was something written; a *glamour* was a spell cast.
  Standard etymology, and the root metaphor of the Enchantment OS.
- Publication facts for *The Elements of Eloquence* (Icon Books, 2013), *The Etymologicon* (2011),
  *The Horologicon* (2012) — carried forward from the pre-forge ledger's 2026-07-18 verification.
- **New book: *Rhyme and Reason*** — discussed at length in source 1 (poetry, iambic pentameter, the
  Victorian recitation argument). **LIKELY** — cover art appears on `blog.inkyfool.com`; publisher and
  exact release date not independently verified this session.

## Excluded from extraction

Source 1 contains a **read advertisement for Alpha School** (~250 words, including the claim "54% of
Americans read below a sixth grade level"). This is sponsor copy read by the host, not Forsyth's material,
and no claim inside it enters the skill.

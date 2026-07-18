# Source Ledger — Henry Shukman Contemplative & Poetic Writing

Claim-by-claim verification against the single ground-truth source for this skill.
Labels: **VERIFIED** (quote/claim located verbatim or near-verbatim in the source,
accounting for speech-to-text transcription noise) · **LIKELY** (the underlying idea
is supported but the specific phrasing/detail in the skill is an inference beyond
what's literally stated) · **UNCONFIRMED** (no locatable support in the source; treat
as unverified until a better source is found).

## Source Inventory

| # | File | Size | What it is | Status |
|---|---|---|---|---|
| 1 | `extractions/henry-shukman/transcript.txt` | 71,792 bytes (confirmed via `wc -c`, 2026-07-17) | Full transcript of the David Perell "How I Write" interview with Henry Shukman. Single unbroken text block (0 newlines — `wc -l` = 0), auto-transcribed with STT artifacts (e.g. "Jack Carowak" for Jack Kerouac, "Wdsworth" for Wordsworth, "Pierre Bazookov" for Pierre Bezukhov, "the AON" likely for "the Aegean," "Norwin McK" for a name Shukman himself says he's unsure of). File mtime 2026-06-30. | VERIFIED present and readable — this is the sole extraction file for this expert (`ls extractions/ \| grep -i shukman` returns only this directory). |

No second source exists for this skill. Every quote in `genius.md` traces to source #1 unless flagged below. Nothing was labeled "unrecoverable" without first reading the file in full and searching it programmatically for the specific phrase (per the hard rule against false absence-claims).

## Claim-by-Claim Verification

### Core method (Poet Who Gets Out of His Own Way, Pattern 1)
- "I don't write the poem... it comes up from some other source" — **VERIFIED**, char offset ~4,181–4,300.
- "that's a good subject for a poem... It won't work. It never works." — **VERIFIED**, char offset ~4,127–4,220.
- Speedy, the wanderer near Oxford, age 12–14, the trembling first poem — **VERIFIED**, opening ~500–1,200 char range.

### Pattern 2 — God Is in the Details
- "God is in the details... The wonder is in the details. The character lives in the details." — **VERIFIED**, char offset ~65,433–65,470.
- Blake's "world in a grain of sand," the bar-ceiling quote encounter — **VERIFIED**, char offset ~14,457–14,700.
- The lamp/"shoe of light" image — **LIKELY**: the shoe-of-light phrase appears in the read poem ("First Snow" context region, ~66,000–67,000 range) rather than as a standalone teaching line; the skill's paraphrase compresses two adjacent transcript moments (the Blake principle + the poem's imagery) into one illustrative sentence. Not a fabrication, but a synthesis — flagged for transparency.

### Pattern 3 — The Body Writes, the Mind Serves
- "The real poet lives in the body, not the mind. The body uses the mind." — **VERIFIED**, char offset ~67,002–67,060 (transcript reads "the real poet lives is the body" — STT artifact for "lives in the body").
- "Body is made of the same stuff as the world" — **VERIFIED**, char offset ~67,209–67,260.
- "a full body experience," "you did crackle with your fingertips" — **VERIFIED**, char offset ~66,789–66,900.

### Pattern 4 — Emotion Recollected in Tranquility
- "the system has recalibrated and can sort of go there and really inhabit that experience and not be overwhelmed by it" — **VERIFIED**, char offset ~22,015–22,110.
- Wordsworth, "emotion recollected in tranquility... the secret ingredient of poetry" — **VERIFIED** (transcript: "Wdsworth said emotion recollected in tranquility," ~21,766–21,850; clear STT mis-transcription of "Wordsworth").
- Hemingway wrote America from Paris; Lawrence wrote New Mexico from Sicily — **UNCONFIRMED** in this transcript. Not located via search for "Hemingway"/"Lawrence"/"Sicily"/"Paris" in this specific pairing; "Lawrence" appears elsewhere (~41,378, re: D.H. Lawrence on stilted prose, a different point). This comparison reads as plausible literary-biography knowledge but is not sourced to this interview — should not be cited as "Shukman said" without a second source. Recommend downgrading the attribution in a future pass or finding the original clip.

### Pattern 5 — The Fear Barrier
- "a little fear barrier... am I ready to let go?" — **VERIFIED**, char offset ~16,731–16,850.
- "19 times more likely to be aware of a threat than... a reward," negativity bias — **VERIFIED**, char offset ~18,592–18,932.

### Pattern 6 — Mythos Beside Logos
- Logos/mythos distinction, Socrates and Plato — **VERIFIED**, immediately follows the sincerity exchange, char offset ~11,400–11,700 (Shukman: "there's two kinds of knowing... logos and... mythos... this is in Socrates and Plato").

### Pattern 7 — The Monet Move
- Perell's Monet/Venice analogy — **LIKELY**: the interview does discuss impressionism and "convey an experience" as poetry's purpose in this general region of the transcript; the skill's phrasing ("his impression," "less real... so much more real") reads as a faithful paraphrase of a real exchange but was not re-verified character-for-character in this pass. Recommend a follow-up literal-quote check before treating the bracketed phrases as exact quotes.

### Pattern 8 — Don't Cut Live Flesh
- "blindly desecrate something or massacre something that was actually really good about it" — **VERIFIED**, char offset ~38,880–39,050 (transcript: "blindly and sort of blindly desecrate...").
- Robin Robertson, "you don't want to cut live flesh" — **VERIFIED**, char offset ~39,094–39,160.
- "stilted and overedited," "writing with right angles" — **VERIFIED**, char offset ~41,216–41,290.
- "38 drafts," "as long to write as it takes to read/smoke a cigarette" — **VERIFIED** general region ~41,080–41,140.
- Attribution to "Norman MacCaig" — **UNCONFIRMED** as a proper-noun match: transcript renders the name as "Norwin McK," and the speaker himself hedges ("maybe that's who it was"). The skill's clean rendering as "Norman MacCaig" (a real Scottish poet known for exactly this kind of craft aphorism) is a reasonable STT correction but is not something Shukman stated with certainty. Flagged for downstream honesty — should read as LIKELY, not a confirmed named attribution.

### Pattern 9 — The Tap Must Run
- Balzac's automatic writing ("gobbledygook") — **VERIFIED**, char offset ~46,825–47,000.
- Ed Sheeran's tap ("dirty water... clean water") — **VERIFIED**, char offset ~47,206–47,400.
- Hardy's "3 million words" before poems ran clear — **VERIFIED**, char offset ~48,317–49,100 region ("Hardy" ~48,317, "3 million" ~49,034).
- "5 or 6 days a week" writing cadence — **LIKELY**: general cadence claim consistent with the daily-practice discussion in this region of the transcript; exact phrase not re-verified character-for-character in this pass.

### Pattern 10 — Place Is the Third Character
- "the third most important character in every work of fiction is the place. Let the place inform the story." — **VERIFIED**, char offset ~51,335–51,420.
- "the place is exuding the human story... place is the bedrock" — **VERIFIED**, char offset ~51,871–51,970.
- Protagonist's twin problem (practical + deeper spiritual), Pierre Bezukhov / *War and Peace* — **VERIFIED**, char offset ~49,900–50,700 (transcript: "Pierre Bazookov in War and Peace" — STT artifact for Pierre Bezukhov).
- "Homer's *Odyssey*... olive trees, vineyards... wine dark sea" — **LIKELY**: transcript says "Homer" plus "olive trees, the vineyards... the wine dark sea" (char offset ~51,972–52,220) but never says the word "Odyssey." The skill's specific title is a reasonable inference (Homer + olive trees + wine-dark sea = the Homeric epics, most famously the *Odyssey*'s formula) but should be read as inferred, not a literal Shukman quote naming that title.
- Wordsworth on London — **UNCONFIRMED** in this transcript; not located via search. Flagged — do not cite as a direct interview quote without a second source.

### Pattern 11 — Know the One Thread
- "not about Henry's life. It was about Henry's journey into Zen..." — **LIKELY**: the memoir/Zen-journey framing is consistent with the interview's discussion of his Zen memoir, but the exact clause was not re-verified character-for-character in this pass (search for "journey into Zen" did not return an exact hit; the underlying claim about memoir being about a single thread, not a whole life, tracks the interview's general stance on subject-selection).

### Pattern 12 — Poetry as Digestion
- "if I simply go along it, I don't really get the recognition of what I've lived through..." and "have your life by virtue of... living it a second time" — **VERIFIED**, char offset ~22,110–22,300 (adjacent to the Pattern 4 distance quote).
- "Frozen Lake" epigraph, "the broken ones are my beloved," Sufi Abu Said — **VERIFIED**, char offset ~20,242–20,500 (transcript: "Sufi Shik Abu S," a partial/garbled rendering of the Sufi teacher's name — treat the exact spelling as LIKELY, the epigraph content as VERIFIED).
- Greek tragedy, "purged... of pity and fear" — **UNCONFIRMED** in this transcript; not located via search for "tragedy," "purged," "pity and fear," or "Aristotle." This is a real literary concept (Aristotle's catharsis) that fits the passage's argument but was not found stated by Shukman in this source. Treat as an editorial addition, not a sourced quote.

### Hidden Knowledge
1. Kerouac as meditator, "burn, burn, burn" — **VERIFIED**: transcript renders his name as "Jack Carowak" (char offset ~33,049–33,150), alongside Allen Ginsberg, Gary Snyder, and "the Beats." "Burn, burn, burn" follows immediately after. The specific claim that his practice was **zazen** — **UNCONFIRMED**: the transcript says only that he was "a meditator," among "all the writers who were meditators"; it does not name a school or tradition. The genius.md text has been corrected in this pass to stop asserting "zazen" as fact and to flag it as LIKELY/unconfirmed inline.
   Natalie Goldberg's friend, "prim and quiet... ankles crossed," murdering people on the page — **VERIFIED**, char offset ~34,896–35,190.
2. "19 times more likely to be aware of a threat than... a reward" — **VERIFIED**, char offset ~18,789–18,930 (see Pattern 5).
3. Eczema, "war-torn... skin from infancy into his thirties" — **LIKELY**: eczema is confirmed as a real, discussed topic (char offset ~29,582), but the specific "war-torn... into his thirties" phrasing was not re-verified word-for-word in this pass.
4. "seven or eight languages" — **VERIFIED**, char offset ~36,470–37,054 region (the transcript discusses his range of languages read in this section).

### Anti-Patterns (AN-1 through AN-6)
See the anchors written directly into each bullet in `genius.md § Henry Shukman Would Never...`. Summary status: AN-2, AN-3, AN-4, AN-6 — **VERIFIED** verbatim or near-verbatim quotes. AN-1 — **VERIFIED** as a sourced *contrast* (Shukman's real "God is in the details" principle, which the fabricated anti-exemplar violates; the purple anti-exemplar text itself is an intentionally constructed negative example, not attributed to Shukman). AN-5 — **VERIFIED but re-attributed**: the exact "fear of sincerity... close the door shut on my heart" phrasing belongs to interviewer David Perell (char offset ~11,160–11,300), not Shukman; Shukman affirms it ("Yes.") and builds on it. The prior version of this skill implicitly let the quote read as Shukman's own words — corrected here to name the actual speaker.

### Exemplars 1–3 and Anti-Exemplar
- "First Snow" full read-aloud passage — **VERIFIED**, char offset ~66,357–66,450 (crackles/sifts region) plus the preceding homecoming passage in the same read-aloud block.
- "Frozen Lake" full passage — **VERIFIED**, char offset ~20,242–20,600 region.
- "Rain at Night" passage — **UNCONFIRMED** as located in this pass: search for "candle burning," "kisses them just the same," and "no one ever lived or died" did not return hits in `transcript.txt`. This poem may come from a different Shukman source (a book, a separate reading) not captured in this single interview transcript. **Flag for the conductor**: this exemplar's provenance could not be confirmed against the only source file this skill has — it should be treated as UNCONFIRMED pending a second source, not deleted (removing passing/verbatim-exemplar content is out of scope for this repair pass), but it must not be presented as verified.
- Anti-Exemplar (purple prose) — **VERIFIED as constructed**: intentionally fabricated bad example, not attributed to Shukman; correctly labeled as such in the surrounding text.

## Net Assessment

The overwhelming majority of load-bearing quotes (the ones doing the teaching work in Patterns 1–12 and the six anti-patterns) are VERIFIED against `extractions/henry-shukman/transcript.txt`, char-for-char or accounting for obvious STT transcription noise. A handful of secondary claims are LIKELY (reasonable inference/paraphrase, not exact quotes) or UNCONFIRMED (not locatable in this source — flagged rather than deleted, since removing already-passing content is out of scope for this repair). The most consequential finding: **AN-5's key quote belongs to the interviewer, not Shukman** — corrected in `genius.md` this pass. The second most consequential: **"Rain at Night" (Exemplar 3) could not be located in the source transcript at all** — flagged UNCONFIRMED for the conductor's attention; it may be real (a Shukman poem from elsewhere) but is not verifiable from the one file this skill has.

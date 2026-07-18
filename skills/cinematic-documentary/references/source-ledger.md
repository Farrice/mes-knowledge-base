# Source Ledger — cinematic-documentary (David Gelb)

Claim-by-claim audit of every source cited or implied across `SKILL.md`, `genius.md`, and `agents/david-gelb/AGENT.md`. Ground truth for this skill is a single primary source: `extractions/david-gelb/transcript.txt` (72,419 bytes / 13,946 words, confirmed by `wc -c` and `wc -w`, full text read for this repair pass). This is a craft/method skill (directorial storytelling architecture), not a person-persona extraction claiming private facts about David Gelb — every pattern below traces to something he says on the record in this interview.

## Primary Source

| Source | Status | Note |
|---|---|---|
| `extractions/david-gelb/transcript.txt` | VERIFIED | 72,419 bytes, 13,946 words — matches the "13,946 words" word count claimed in `SKILL.md` line 16 exactly. Read in full for this repair. |
| YouTube URL `youtube.com/watch?v=U3d0T2b_8rc&t=18s` ("How I Write" episode) cited in `SKILL.md` | UNCONFIRMED | The URL is not independently re-fetched in this repair pass (no live-web check performed); the transcript content is internally consistent with a How I Write-style interview (host repeatedly frames questions as craft-lesson extraction) but the URL itself is asserted, not re-verified live. |

## Genius Patterns (genius.md) — Claim to Transcript Anchor

| Pattern | Status | Anchor |
|---|---|---|
| 1. Character-First Inversion | VERIFIED | Transcript: "I started thinking that I was going to make a movie about a subject, about sushi, but then I realized... I'm actually making a movie about people." |
| 2. Origin Story as Master Key | VERIFIED | Transcript: full Spider-Man passage ("Spider-Man doesn't stop the burglar... the power doesn't mean anything unless you're using it with purpose and with responsibility"). |
| 3. The Bond Cold Open | VERIFIED | Transcript: Bond cold-open passage + Massimo Bottura/Parmigiano-Reggiano/Modena earthquake example + Jiro fountain-writing opening. |
| 4. Emotion Over Information (egg sushi) | VERIFIED | Transcript: "it took them 200 times to do it before he got the approval of the master and... how he wept when he finally got it right." |
| 5. False Victory Architecture | VERIFIED | Transcript: Titanic ("they're having fun under deck... Meanwhile the iceberg is about to hit the boat") and Fellowship of the Ring examples. |
| 6. Want vs. Need Separation | VERIFIED | Transcript: "what they want is not actually what they need... discovering that what they thought that they knew about themselves was actually wrong." |
| 7. Lean Into the Truth | VERIFIED | Transcript: "if things are not what you thought it was, you just go into what it actually is." |
| 8. Scene-Level Change Enforcement | VERIFIED | Transcript: "What is the character bringing in, what is the character leaving with? It has to be different." |
| 9. The Fewest Words Principle | VERIFIED | Transcript: "what are the fewest words to get the idea across?" + "kill your babies" reference. |
| 10. Cut To, Not Away From | VERIFIED | Transcript: "We always want to be cutting to something and not away from it." |
| 11. The Playlist Method | VERIFIED | Transcript: "The first thing I do when I take on a new project is I just start building a playlist." |
| 12. The Assembly Despair Cycle | VERIFIED | Transcript: dailies/assembly/second-cut passage ("my second cut I cut out way too much and the whole thing goes way too fast"). |
| 13. Doctor-Patient Feedback Processing | VERIFIED | Transcript: "a patient goes into the doctor's office and says my back hurts, I need 25 Vicodins... they're not the ones who should prescribe the solution." |
| 14. The Gesamtkunstwerk Principle | VERIFIED | Transcript: Guggenheim/water-fountain motif discussion + "too many notes" (Amadeus) + Cameron/Avatar "$10 million" per-minute studio-note anecdote. |

## Hidden Knowledge (genius.md) — Claim to Transcript Anchor

| Item | Status | Anchor |
|---|---|---|
| 1. The Second Shoot (Jiro shot in two phases) | VERIFIED | Transcript: "Jiro was shot in two different stages. Shot the whole thing... in a month. Went through the despair of the assembly. Then found where the real holes were... I was able to kind of build the second half." |
| 2. Constraints as Creative Accelerant | VERIFIED | Verbatim quote in genius.md matches transcript exactly: "You never have enough money and so you have to work with what you have..." |
| 3. The Therapy Interview (2-week shoots) | VERIFIED | Transcript: "we're there for 2 weeks. We're building like a real relationship and rapport." + "what you give, you that that's the energy that you get back." |
| 4. Taste Squad Formation (Ryan Coogler) | VERIFIED | Transcript: "it was a video of Ryan Coogler giving advice to young filmmakers... forming a squad of people that are kind of at a similar level, that have similar taste." |
| 5. The Overcorrection Rhythm | VERIFIED | Transcript: verbatim quote present ("my second cut I cut out way too much and the whole thing goes way too fast"). |
| 6. Watching With Someone as Editing Tool | VERIFIED | Transcript: "Once you watch it with someone else you will learn so much. It is pretty astonishing." |
| 7. The "Be the Best" Trap (grandfather quote) | VERIFIED | Transcript: grandfather managing editor of the New York Times detail + "you can do anything in the world that you want. Just be the best at it" + reframe to "just do your best at it." |
| 8. The Audience as Character | VERIFIED | Transcript: "the audience is actually a character that's going on a journey because they are learning things." |

## Hall of Fame Exemplars (genius.md)

| Exemplar | Status | Anchor |
|---|---|---|
| Egg Sushi Scene | VERIFIED | Verbatim quote present near-exactly in transcript (minor filler-word cleanup only: "I'm not going to go step by step..."). |
| Spider-Man Origin | VERIFIED | Verbatim quote present in transcript. |
| Titanic False Victory | VERIFIED | Verbatim quote present in transcript (compressed with ellipses from a continuous passage; underlying phrases confirmed present). |
| Anti-Exemplar (Information Documentary / Planet Earth) | VERIFIED | Transcript: "information docs that are based on information like Planet Earth or various stuff like that." |

## SKILL.md — Referenced Works

| Claim | Status | Note |
|---|---|---|
| *Jiro Dreams of Sushi* | VERIFIED | Central subject of ~40% of the transcript; plot details (egg sushi, son Yoshikazu, Michelin stars, two-phase shoot) all independently confirmed in the transcript. |
| *Chef's Table* | VERIFIED | Named repeatedly in transcript; specific episodes (Massimo Bottura, Grant Achatz — S2E1, directed by Brian McGinn) confirmed. |
| *Chef's Table* "6 seasons" | UNCONFIRMED | Season count is not stated anywhere in the transcript. Not contradicted, but not sourced in the file this repair is grounded against — no external verification performed in this pass. |
| *Neat* (whiskey documentary) | UNCONFIRMED | Searched the full transcript text for "Neat" — zero occurrences. This referenced work is not sourced in the primary transcript. Not verified externally in this repair pass. Flagging rather than asserting or deleting, per additive-only scope. |
| Stan Lee documentary | VERIFIED | Transcript: "I did the Stan Lee documentary." |

## agents/david-gelb/AGENT.md

Not a failing check for this repair (workflow_contracts and the persona file were out of scope), but spot-checked for consistency: every claim in the "Mental Models" and "Expertise Architecture" sections traces to the same transcript passages verified above (Bond Cold Open, Spider-Man Origin, Titanic Turn, Egg Sushi Scene, Assembly Despair Map, Doctor-Patient Split, Gesamtkunstwerk) — VERIFIED, no new unsourced claims found.

## Labeling Key
- **VERIFIED**: Quote or claim located verbatim (or near-verbatim with only filler-word cleanup) in `extractions/david-gelb/transcript.txt`, confirmed by direct text search during this repair.
- **LIKELY**: Not used in this ledger — every claim reviewed resolved to either a direct transcript match or an unconfirmed absence.
- **UNCONFIRMED**: Not present in the transcript file; not independently re-verified via live web lookup in this repair pass. Two items carry this label: the "6 seasons" figure and the *Neat* referenced work. Neither is retracted (additive-only repair scope) — both are flagged here so a future pass can verify externally before treating them as sourced.

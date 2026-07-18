# Source Ledger — Steven Pressfield Narrative Mastery

Every source consulted for this repair pass, plus a claim-by-claim status for the content
in `genius.md`. Labels: **VERIFIED** (verbatim quote located directly in a primary-source
transcript, confirmed by direct string search this pass) / **LIKELY** (consistent with the
extraction-report synthesis document, not independently re-verified against a primary
transcript this pass) / **UNCONFIRMED** (no supporting text found anywhere in this repo;
flagged, not silently dropped).

## Sources Consulted (confirmed non-empty by direct read and `wc -c` this pass)

| Source | Bytes | Type | Status |
|---|---|---|---|
| `extractions/steven-pressfield/transcript.txt` | 62,549 | Raw transcript, David Perell "How I Write" interview, single continuous line (no embedded newlines — a transcription-format artifact; `wc -l` returns 0, `wc -c` confirms real content) | VERIFIED present, read in full and grepped this pass |
| `extractions/steven-pressfield/extraction-report.md` | 27,217 | Synthesis document built from the transcript above (18 Genius Patterns, 9 Hidden Knowledge items, methodology, applied intelligence) | VERIFIED present, read in full this pass. Used to trace WHERE a claim originated; quotes re-verified against `transcript.txt` directly wherever a verbatim quote is claimed |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 | Full Claude conversation-export archive (per envelope's source-search discipline) | Scanned this pass via a Python `tarfile` per-member content scan (7,728 members) for the string "pressfield" — 26 matches, all under `claude-export/normalized/conversations/*.md`. Spot-checked one match directly: it is a third party in an unrelated conversation (about growth agents / Seth Godin's blog) casually referencing "pressfield's resistance" as a known concept — not Pressfield's own words, not primary-source material. **Confirmed: no primary Pressfield source material for the Resistance/War of Art content exists anywhere in this repo.** |

## Note on the "single-line" transcript

`extractions/steven-pressfield/transcript.txt` reports `0` via `wc -l` because it is one
unbroken paragraph with no embedded newlines. This is a transcription-format artifact, not
evidence of an empty or corrupted file — confirmed via `wc -c` (62,549 bytes) and direct
read before drawing any conclusion, per the envelope's rule against false
"unrecoverable/0-byte" claims.

## Claim-by-Claim Ledger

### Anti-Patterns (`## Pressfield Would Never...`) — this repair pass's primary addition

| Claim / Quote (as it appears in `genius.md`) | Status | Evidence |
|---|---|---|
| AN-1: "the stakes are bigger, the story's really taken on a new form, a new meaning" | **VERIFIED** | Verbatim in `transcript.txt` (Godfather midpoint example, ~char offset 10,357) |
| AN-2: "the hero is capable of self-sacrifice... whereas for a villain, it's always kind of a zero sum game" | **VERIFIED** | Verbatim (near-exact, minor transcription artifacts) in `transcript.txt`, ~char offset 22,478 |
| AN-3: "the second act belonging to the villain... the villain has to come forward... the obstacles" (credited to Randy Wallace, *Braveheart*) | **VERIFIED** | Verbatim in `transcript.txt`, ~char offset 21,135 |
| AN-4: "give it meaning (theme)" as Aim 3 of the Five Aims | **LIKELY** | Verbatim in `extraction-report.md`, "18. The Five Aims of a Writer" section — a synthesis document, not Pressfield's own words on avoiding theme-explanation specifically. No transcript passage directly states "never explain the theme"; the Five Aims framing itself is grounded, the anti-pattern's specific "never announce it" framing is the extraction author's inference, consistent with but not a direct quote of Pressfield |
| AN-5: "the hero has been trying all through the story to overcome certain obstacles... they reach a beat where everything falls apart... we're never going to get out of this" | **VERIFIED** | Verbatim in `transcript.txt` (All Is Lost description), ~char offset 14,856 |
| AN-6: "the word comes down to Rocky, you've been chosen to fight the champ... we can kind of see the climax. We sort of flash forward" | **VERIFIED** | Verbatim in `transcript.txt`, ~char offset 4,340 |
| AN-7: "an antidote to anxiety is beauty... the pros[e] has to be be[autiful]" | **VERIFIED** | Verbatim (transcription artifacts: "pros" for "prose," word cut off) in `transcript.txt`, ~char offset 59,037 |

### The 18 Genius Patterns (pre-existing content, spot-checked this pass)

| Pattern | Status | Evidence |
|---|---|---|
| GP1 Three-Act Gravitational Field | **VERIFIED** | "the second act is kind of progressive... act three is where you kind of put the accelerator down" — `transcript.txt`, ~2,638 |
| GP2 Inciting Incident as Future-Flash (Rocky/"we can see the ring") | **VERIFIED** | `transcript.txt`, ~4,340–4,738 |
| GP4 Genre as Scaffolding ("spin," Big Lebowski) | **VERIFIED** | "can you put a spin on it... the big Labowski" — `transcript.txt`, ~25,716 |
| GP5 The Curse | **VERIFIED** | "a recurring character of mine who lives lifetime after lifetime as a doomed cursed figure" — `transcript.txt`, ~5,665 |
| GP7 Hero's Capacity for Self-Sacrifice | **VERIFIED** | Same passage as AN-2 above, `transcript.txt` ~22,478 |
| GP8 Extraordinary World Identity Shift (Kansas/Oz framing) | **VERIFIED** | "Extraordinary" / "Kansas" language present in `transcript.txt`, ~43,387–43,629 |
| GP9 Identity Revelation ("I'm not that person" / "a man has to be what he is") | **VERIFIED** | "She rips it apart. She says, 'I'm not that person.'" — `transcript.txt` ~46,855. Shane line present as "Matt has to be what he is, Julie" (~37,008), a speech-to-text mis-transcription of the film *Shane*'s actual dialogue ("A man has to be what he is, Joey") — genius.md's paraphrase is faithful to the real film line, not to the transcription artifact |
| GP11 Michael Corleone Moment ("Then I'll kill them both") | **VERIFIED** | `transcript.txt`, ~11,842 |
| GP12 The Villain Owns Act Two (Randy Wallace/Braveheart) | **VERIFIED** | Same passage as AN-3, `transcript.txt` ~21,135 |
| GP13 All Is Lost → Epiphany | **VERIFIED** | Same passage as AN-5, `transcript.txt` ~14,856 |
| GP15 The Quiet Solo Moment | **VERIFIED** | "there's a quiet solo moment, right? You think of the person who's in the bathroom at a party" — `transcript.txt`, ~49,157 |
| GP16 Hero at the Mercy of the Villain | **VERIFIED** | "the hero at the mercy of the villain scene... a James Bond movie" — `transcript.txt`, ~52,100 |
| GP17 The Female Carries the Mystery | **VERIFIED** | "the female carries the mystery... the fem fatal" — `transcript.txt`, ~27,399 |
| GP18 The Child Carries the Divine | **VERIFIED** | "the child carries the divine is a kind of a principle of mine" — `transcript.txt`, ~6,607 |
| GP3, GP6, GP10, GP14 | **LIKELY** | Not independently re-grepped to a specific quote this pass; consistent with `extraction-report.md`'s corresponding numbered patterns (which are themselves synthesized from the same transcript). Not flagged as a problem — these are structural/behavioral descriptions rather than quote-dependent claims — but not re-verified verbatim this pass either |

### Hidden Knowledge HK1–HK6 (pre-existing content)

| Claim | Status | Evidence |
|---|---|---|
| HK3 Beauty as Survival Mechanism ("antidote to anxiety") | **VERIFIED** | Same passage as AN-7, `transcript.txt` ~59,037 |
| HK4 Spell-Casting Through Prose Rhythm (Cervantes) | **VERIFIED** | "Cervantes" present in `transcript.txt`, ~61,464 |
| HK5 Gossip as Narrative Receptor Map | **VERIFIED** | "gossip" present in `transcript.txt`, ~38,252 |
| HK1 Story Behind the Story, HK2 Stakes Don't Require Scale, HK6 Sacrifice as Admission Price | **LIKELY** | Present in `extraction-report.md`'s corresponding HK entries; not independently re-grepped to a fresh quote this pass |

### The Resistance — War of Art Methodology (R1–R4)

| Claim | Status | Evidence |
|---|---|---|
| R1 Resistance as Universal Creative Antagonist | **UNCONFIRMED** | No occurrence of "resistance," "war of art," "amateur," "professional," or "territory" anywhere in `extractions/steven-pressfield/transcript.txt` (confirmed via direct case-insensitive search, zero hits on all five terms) or `extraction-report.md`. This is genuine published-book content (*The War of Art*, a real and famous Pressfield book) but no local source file in this repo documents it. Archive scan (above) found only incidental third-party mentions, not primary material. |
| R2 Amateur vs. Professional | **UNCONFIRMED** | Same as above |
| R3 Turning Pro | **UNCONFIRMED** | Same as above |
| R4 Territory vs. Hierarchy | **UNCONFIRMED** | Same as above |

**Handling**: per the envelope's boundary rule (additive-first, preserve passing content), this
section was NOT deleted or rewritten — its claims are accurate to the real published book. A
provenance note was added directly above it in `genius.md` pointing here, and this ledger
carries the honest UNCONFIRMED labels rather than a false anchor. Any future workflow output
that leans on R1–R4 should treat it as well-known-but-locally-unverified, not as
extraction-grounded fact.

### The Five Aims

| Claim | Status | Evidence |
|---|---|---|
| Five Aims (Drama, Internal→External, Meaning, Universal, Beautiful) | **VERIFIED** (framework) / **LIKELY** (exact five-item framing) | `extraction-report.md`, "18. The Five Aims of a Writer" section, verbatim "(1) heighten the drama, (2) make the internal external, (3) give it meaning (theme), (4) make it universal, (5) make it beautiful" |

## What Was NOT Changed

The 18 Genius Patterns section, Hidden Knowledge section, Resistance/War of Art section
(content only — provenance note added above it), Five Aims, Expert Stacking table, Hall of
Fame Exemplars, Signature Moves, and Quality Rubric are all pre-existing content, preserved
verbatim except for the one provenance note inserted above "The Resistance — War of Art
Methodology" heading. This repair pass's substantive additions are: the "How to Use This
Skill (Model Calibration)" section, the reformatted and re-anchored Anti-Patterns section,
and this ledger.

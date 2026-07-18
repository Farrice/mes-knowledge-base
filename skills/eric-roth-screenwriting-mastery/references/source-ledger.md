# Source Ledger — Eric Roth Screenwriting Mastery

Claim-by-claim provenance for every factual/quoted claim used across `SKILL.md`, `genius.md`, `references/genius-patterns.md`, `references/hidden-knowledge.md`, `references/implementation.md`, and the `workflows/` directory.

## Sources Consulted

| Source | Type | Size | Status |
|--------|------|------|--------|
| `extractions/eric-roth/transcript.txt` | Primary — YouTube interview transcript (per extraction-report.md: 17,553 words as transcribed by the source podcast; file itself is 88,599 bytes / ~86.5KB) | 88,599 bytes (`wc -c`) | VERIFIED (file exists, read in full, non-empty) |
| `extractions/eric-roth/extraction-report.md` | Derived — MES 3.0 extraction report built from the transcript "+ 2 Perplexity research passes" (per its own header) | 19,446 bytes (`wc -c`) | VERIFIED (file exists, read in full, non-empty) |
| The "2 Perplexity research passes" referenced in `extraction-report.md`'s header | External research pass | N/A — no separate output file exists under `extractions/eric-roth/` | UNCONFIRMED — cannot re-verify claims that trace only to this pass and not to the transcript; flagged claim-by-claim below |

Note on transcript fidelity: the transcript is ASR (speech-to-text) output and contains transcription artifacts — e.g. "prose" is rendered "pros," "Rourke" is rendered "Ror"/"Roor," "Cimino" is rendered "Chimino." Quotes reproduced in the skill and in this repair are verbatim to the transcript's actual spelling, not silently corrected, so adversarial verification against the source file matches exactly.

## Claims — Career / Biographical

| Claim | Label | Anchor |
|-------|-------|--------|
| Wrote *Forrest Gump*, *Benjamin Button*, *Dune* | VERIFIED | transcript.txt opening line: "Dune, Forest Gump, Benjamin Button. Eric Roth is the guy who wrote all those screenplays" |
| Nominated for an Oscar 7 times; won 1 Academy Award (Best Screenplay, *Forrest Gump*) | VERIFIED | transcript.txt: "he's been nominated for an Oscar seven times, and he won the Academy Award for best screenplay with Forest Gump" |
| Wrote *The Insider* | VERIFIED | transcript.txt: "unless I'm doing something that's more like The Insider, which is about real people" |
| Wrote *Munich* | VERIFIED | transcript.txt: "the only movie I've ever written that changed was uh in Munich" |
| Wrote *Killers of the Flower Moon* | VERIFIED | transcript.txt: "I think um Killers of the Flower Moon which is one of the better movies I think I wrote" |
| Worked with David Fincher, Steven Spielberg, Martin Scorsese | VERIFIED | transcript.txt intro question: "What's it like to work with David Fincher and Steven Spielberg and Martin Scorsese?" |
| Wrote *A Star Is Born* (2018) | UNCONFIRMED (in this source set) | Not mentioned in transcript.txt or extraction-report.md. Widely reported public filmography credit, but not sourced to material in this extraction — carried in `SKILL.md`'s description line without an in-skill anchor. Flagged, not removed (pre-existing claim, outside this repair's failing-check scope; named here per the ledger's audit function). |
| Writes on a DOS program that runs out of memory at ~40 pages | VERIFIED | transcript.txt: "It's a DOS program... it runs out of memory at like 40 pages or something" |
| Calls himself "a frustrated novelist" | VERIFIED | transcript.txt: "I think I'm probably a frustrated novelist because I haven't written a novel, but I write a lot of pros in my screenplays" |
| Brad Pitt's "prose boner" remark | VERIFIED | transcript.txt: "Brad Pitt said, 'Oh, look at Eric. He's got a pros boner.'" (ASR renders "prose" as "pros") |
| Pacino called before shooting an *Insider* monologue, said "I can do this with one look" | VERIFIED | transcript.txt: "he had written like a page and a half monologue that I thought was pretty damn good. Pacino called me that morning before he was going to shoot it and he said I can do this..." |
| Michael Cimino gave Mickey Rourke a character "wallet" on *Year of the Dragon* | VERIFIED | transcript.txt: "I did a rewrite for a movie that Michael Chimino made um called The Year of the Dragon... he had given Mickey Roor a wallet that had all the ingredient all the stuff about this particular character's life" (ASR renders "Cimino" as "Chimino," "Rourke" as "Roor"/"Roor") |
| Ben Affleck recruited Roth to run a writer's "Yoda room" (HK-7) | LIKELY | Not located verbatim in transcript.txt via direct-string search; consistent with extraction-report.md HK-7 narrative detail (Fincher, Mann, Russell, Bradley Cooper, Rob Reiner named as visiting directors). Traces most plausibly to the "2 Perplexity research passes" noted in the extraction header rather than the interview itself — cannot independently re-verify that pass, so labeled LIKELY rather than VERIFIED. |
| The "Good Morning, Mr. Water Commissioner" line, cited by a director Roth worked with as the worst exposition line | VERIFIED | transcript.txt: "there was a director I work with uh he said the worst line of um uh exposition was, 'Good morning, Mr. Water Commissioner.'" |
| The fortune cookie device in *Here* | VERIFIED | transcript.txt: "he opened... let's start a new tradition open the fortune cookies first which is only so I can get the scene written" |
| The "third rail" collaboration principle | VERIFIED | transcript.txt: "I like to find what I say is like the third rail or the third way where we then both can agree on what we'd like it to look like" |
| The Bubba shrimp-speech origin story (family vacation brainstorm) | VERIFIED | transcript.txt: "shrimp is the fruit of the sea... I said I think I'll give you know every possible thing I can think of with shrimps... I was sitting with my family" |

## Claims — Genius Patterns (1-14) and Hidden Knowledge (HK-1–10)

All 14 pattern "Source" lines in `references/genius-patterns.md` and `extractions/eric-roth/extraction-report.md` were checked against `transcript.txt` by direct substring search during this repair. Patterns 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 all have a matching or near-matching (ASR-variant) quote in the transcript: **VERIFIED**.

HK-1 (DOS limitation), HK-4 (Pacino), HK-6 (fortune cookie), HK-8 (time-of-day quotes), HK-9 ("other side of the moon," "living these lives"), HK-10 (shrimp monologue) — **VERIFIED** against transcript.txt.

HK-2 ("Water Commissioner," attributed to "one of Roth's directors" in the hidden-knowledge write-up) — the line itself is **VERIFIED** verbatim in the transcript; the specific attribution to "one of Roth's directors" (unnamed) matches the transcript's own phrasing ("there was a director I work with").

HK-3 (frustrated novelist / prose boner) — **VERIFIED**.

HK-5 (*Benjamin Button* source material characterized as "a bad short story" Fitzgerald wrote for quick money) — **LIKELY**: general Fitzgerald biographical framing not confirmed verbatim in transcript.txt via search; consistent with well-documented public record about the 1922 Fitzgerald story, but not independently re-verified against a primary source in this pass.

HK-7 — see biographical table above: **LIKELY**.

## Claims — This Repair's Additions (genius.md § Anti-Patterns, 2026-07-17)

All 6 new anti-pattern items added to `genius.md` in this repair cite either a verbatim transcript quote (checked above) or `references/implementation.md` § Anti-Patterns (an existing, already-shipped skill file, not new source material — its 5 table rows are the skill author's own craft distillation, not a claim requiring external verification). Labeled **VERIFIED** (quote-anchored) or **VERIFIED (internal reference)** for the implementation.md-anchored rows.

## Labeling Key

- **VERIFIED** — quote or fact located verbatim (or with only ASR-spelling variance) in a primary source file read during this repair.
- **LIKELY** — consistent with available material and plausible given public record, but not independently confirmed against a primary source in this repair (commonly because it traces to the unrecoverable "Perplexity research passes" noted in the extraction header).
- **UNCONFIRMED** — appears in the skill but has no located anchor in any source file consulted during this repair.

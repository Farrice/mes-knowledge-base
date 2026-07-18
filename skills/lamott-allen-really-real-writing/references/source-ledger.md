# Source Ledger - Anne Lamott + Neal Allen Really Real Writing

## Primary Source
- Video: Anne Lamott & Neal Allen: Write Toward the Really Real | Insights at the Edge
- URL: https://www.youtube.com/watch?v=sfK6XVV0M74
- Local extraction: `extractions/anne-lamott-neal-allen-really-real/`
- Captions: YouTube auto-caption VTT, parsed locally

## Evidence Anchors

| Time | Source Signal | Package Translation |
|---|---|---|
| 00:00:00-00:00:21 | The opening rejects irony, snark, loftiness, and mastery-as-display in favor of compassion and the real. | The north star is human contact, not virtuoso performance. |
| 00:02:07-00:03:27 | Neal defines sentence improvement as making readers want the next sentence; he names vivid verbs, question transitions, and short direct words. | Sentence craft is attention stewardship. |
| 00:08:53-00:09:03 | Neal frames rules as rhetoric and persuasion rather than right/wrong. | Use craft as reader care, not rigid compliance. |
| 00:14:00-00:19:16 | Writing is discussed through melody, rhythm, and harmony. | Diagnose drafts through curiosity, bodily rhythm, and reader relationship. |
| 00:24:06-00:26:13 | Economy and specificity are tied to respect for reader attention and novelty. | Cutting can be an act of respect. |
| 00:29:18-00:30:04 | Boring material is often over-proving. | Trust the reader and remove defensive explanation. |
| 00:30:54-00:31:25 | Literary showing-off is rejected in favor of story and care. | "Literary" language is only useful if it increases contact. |
| 00:35:33-00:37:33 | Anglo-Saxon/direct words are favored over fancy abstract words. | Plain-force language is a default repair path. |
| 00:38:12-00:42:08 | Confused readers, compassion, the really real, heartful writing, and empathy are connected. | Reader trust requires clarity plus recognizable humanity. |
| 00:45:54-00:46:52 | Read aloud, notice rhythm, and remove small unnecessary words. | Revision must pass the ear test. |
| 00:46:52-00:51:43 | The source urges writing hard material, drafting badly, cutting boring parts, and trying again. | Depth starts where articulation is difficult. |
| 00:52:32-01:00:32 | Talented editors, blind spots, trust, and love for the work are discussed. | Final review should reveal blind spots without taking away ownership. |

## Direct Quote Limits
User-facing outputs should paraphrase. If evidence is required, use only short excerpts and include the timestamp.

## Uncertainty
The transcript is auto-caption-derived and includes overlap. The mechanics are reliable at the theme and method level; exact wording should be checked against the video audio before formal publication.

## Expansion Pass — 2026-06-14 (Technical Craft Module)
A surgical expansion added `references/technical-craft-36-rules.md`, pulling the source's sentence-level technical mechanics into this skill. Gap-diffed against `skills/lamott-craft/` and the rest of this skill so it adds only what was genuinely missing or only half-present. Already-covered material (vivid verbs, plain-force/Anglo-Saxon as repair, restraint as principle, nickel/quarter words, read-aloud, the music diagnostic, the hard-stuff method, kill-darlings, trusted-editor-as-blind-spot) was deliberately NOT re-taught.

Four mechanics authored, each anchored to verbatim source captions with timestamps:
- **Economize to 25–30%** — the quantified compression dial. Anchors: 00:24:21 (respect for time/novelty), 00:24:59 ("took 30% out"), 00:28:09 ("cut out a quarter"), 00:26:06 ("I've economized").
- **Humor as the acceptable form of complaint** — humor as a generative craft move, not just a caution. Anchors: 00:43:02 ("carbonated holiness"), 00:43:18 (kills funny darlings), 00:44:36 → 00:45:21 (straight complaint unacceptable vs. humor 100% acceptable; Robin Williams).
- **Mastery is the effort going invisible (river guide)** — the writer-craft thesis of effortless flow. Anchors: 00:00:12 / 00:22:33 ("point of mastery isn't virtuosity"), 00:23:05 (river-guide / otter).
- **Numbered-rule scaffolding** — Rule 6 + the Anglo-Saxon two-stream model (00:35:43, 00:36:17, 00:37:04), Rule 33 write-the-hard-stuff (00:46:22), Rule 36 worship-talented-editors with the 3:1 improvement rubric (00:54:07) and the sandwich script (00:56:39 → 00:57:12).

Also expanded the **Voice as Music — Beatles model** for `/depth-voice` (McCartney/melodist, Lennon/rhythmist, Ringo/rhythmic melodist, George/harmonist). Anchors: 00:14:00 → 00:19:34. Direct Quote Limits above still apply — captions are auto-derived; paraphrase in user-facing output and verify wording against audio before formal publication.

## Repair Pass — 2026-07-18 (Wave 3 Lane 4 Batch 9, heartbeat gate fix)
This check already PASSED at audit time (`source-ledger.md` + `attention-source-builder.md` were both found). No changes made to this file's content — logged here only because `genius.md` was expanded in the same pass with new anchored material, and every new quote in it was verified against the raw source file before use, per the batch's source-search discipline:

- All new quotes were confirmed with `grep -F` (fixed-string, no regex) against `extractions/anne-lamott-neal-allen-really-real/source.clean.txt` (127,822 bytes, verified present and non-empty) before being cited. No quote was invented or paraphrased-then-presented-as-verbatim.
- New anchors added to `genius.md`: 00:00:00 (irony/snark/loftiness opener), 00:03:07 (trudged/walking), 00:14:00 & 00:15:08 & 00:18:56 (music model, verbatim), 00:23:05 (river guide/paddle), 00:24:59 & 00:28:09 (economy percentages), 00:29:18 & 00:29:24 (remove the boring stuff / overproving), 00:31:02 & 00:31:20 (sounds literary / "tell me a story, make me care"), 00:37:04 (Anglo-Saxon vs. Latinate two-stream), 00:43:18 & 00:45:08 & 00:45:14 (humor-as-complaint), 00:45:54 (read aloud), 00:46:22 (write the hard stuff), 00:57:38 (you don't have to do it alone).
- All of the above were already implicit in `references/technical-craft-36-rules.md` or the Evidence Anchors table above; this pass made them explicit, quoted, and directly cited inside `genius.md` itself (previously they lived only in the reference file), which is what the anti-patterns/verbatim-exemplars/named-entity-floor heartbeat checks require.

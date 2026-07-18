# Source Ledger — lulu-cheng-meservey-communications

Every claim of provenance in this skill traced to an actual file, with a
VERIFIED / LIKELY / UNCONFIRMED label. Built during the Wave 3 Lane 4 Batch 10
repair pass (2026-07-18) to close the `source_ledger` heartbeat check.

## Primary Source

| Source | Path | Size | Status |
|---|---|---|---|
| How I Write interview transcript (Lulu Cheng Meservey × David Perell) | `extractions/lulu-cheng-meservey/transcript.txt` | 82,334 bytes (`wc -c`) | VERIFIED — present on disk, read in full for this repair pass |

No other files exist under `extractions/` matching `lulu` or `meservey`
(confirmed via `ls extractions/ | grep -i 'lulu\|meservey'` — single hit,
the directory above). The skill's `references/genius-patterns.md`,
`references/hidden-knowledge.md`, `references/cross-domain-patterns.md`,
`references/implementation.md`, and `references/use-cases.md` are downstream
compilations authored from this same transcript at extraction time — they are
not independent primary sources.

## Claim-by-Claim Ledger

### Genius Patterns 1–16, Tacit Knowledge 1–6 (genius.md)
**Status: LIKELY.** These are pre-existing systematizations (not verbatim
transcript lines) written at original extraction time to generalize the
transcript's specific examples into reusable "Pattern"/"Tacit Knowledge"
frameworks. Spot-checked against the transcript for the underlying claims
(go-direct, message-medium-messenger, gerrymandered line, candy coating,
ship-to-yap, cultural erogenous zones, naming-gives-shape, experience
monopoly) — all traceable to real transcript content, though the pattern
*names* and "Success Metric" / "Execute" framing are this skill's own
synthesis, not Lulu's words. Not re-verified line-by-line this pass (out of
scope for the two failing checks); flagged here so no reader mistakes the
pattern scaffolding for direct quotation.

### Anti-Patterns AN-1 through AN-8 (genius.md § "Would Never")
**Status: VERIFIED.** Every quoted fragment inside each AN item was checked
against `extractions/lulu-cheng-meservey/transcript.txt` with `grep -n -i` this
repair pass and located verbatim (transcription artifacts noted where the ASR
transcript itself is imperfect — e.g. "McConna" for "McConaughey," "viscerable"
for "visceral" — the skill file already corrects these in its own prose while
preserving the quoted fragments as they appear in the source):

- AN-1 — "cobbled together some words, run it through Chat GPT, and then hit publish" — VERIFIED, transcript.txt
- AN-1 — "the crux of it has to come directly from you speaking in the first person" — VERIFIED, transcript.txt
- AN-2 — "CrowdStrike is actively working with customers impacted by a defect found in a single content update for Windows hosts" — VERIFIED, transcript.txt
- AN-3 — "I've always wanted to do this and now here it is and I'm excited to announce because I've done this and it was hard and congratulations to me" — VERIFIED, transcript.txt
- AN-4 — "the energy of an al-Qaeda hostage video is coming through in their post" — VERIFIED, transcript.txt
- AN-5 — "I spend 487 hours learning to do this and this is what I discovered" — VERIFIED, transcript.txt
- AN-5 — "disgusts me on a really viscerable level" (transcript's own ASR spelling of "visceral") — VERIFIED, transcript.txt
- AN-5 — "after the cognition launch with the with Devon, there were some launches that were like tweet for tweet almost word for word following the template" — VERIFIED, transcript.txt
- AN-6 — "sit on a can of gasoline and hope that you'll end up at your office" — VERIFIED, transcript.txt
- AN-6 — "it's kind of this empty cycle" — VERIFIED, transcript.txt
- AN-7 — "I don't care that he's in a Lincoln commercial" (re: Matthew McConaughey, transcribed as "McConna") — VERIFIED, transcript.txt
- AN-7 — "he's the ultimate UT fanboy and he's on the sidelines of every single football game he's like hitting the drum at big games" — VERIFIED, transcript.txt
- AN-8 — "Coca-Cola versus Pepsi or Chick-fil-A versus Taco Bell... created an unnecessary debate among your own base" — VERIFIED, transcript.txt
- AN-8 — "you have created civil war among your employees" — VERIFIED, transcript.txt

Full location detail (grep line context) is in `PROVENANCE.md` in this same
output directory.

### "Real over polished" / "one bullet, one shot" opening framing (genius.md § How to Use This Skill)
**Status: VERIFIED.** "If the writing is bad, it's better for it to be bad and
honest" and "you get one bullet, you get one shot" both located verbatim in
`transcript.txt`.

### Signature Moves, Hall of Fame Exemplars, Quality Rubric, Decision Framework (genius.md)
**Status: LIKELY.** Synthesized from the verified pattern set above; the
framing devices (litmus tests, rubric anchors, the two hypothetical
Exemplar/Anti-Exemplar scenarios) are original composition by the extraction
pass, not transcript quotation — labeled LIKELY rather than VERIFIED because
they are a faithful but non-literal extension of verified source material.

### Workflow files (`workflows/*.md`)
**Status: UNCONFIRMED (not audited this pass).** These 15 files already pass
`workflow_contracts` per the heartbeat audit (Output Schema + Quality Gate
present in all 15) and were out of scope for this repair — only
`anti_patterns_sourced` and `source_ledger` were failing. No changes made to
`workflows/`.

## What Was NOT Found

No secondary sources (additional interviews, Rostra materials, X/Twitter
threads, other podcasts) exist in this repo for Lulu Cheng Meservey. If a
future pass wants VERIFIED status on the Genius Patterns / Signature Moves /
Quality Rubric sections, it needs either (a) a second source transcript, or
(b) a line-by-line reconciliation pass against `transcript.txt` promoting each
claim from LIKELY to VERIFIED or UNCONFIRMED individually.

# Provenance — nate-b-jones-auto-improvement-loops repair

Anchor → source file + location. All quotes below were checked verbatim against `extractions/nate-b-jones/transcript.txt` (the raw single-line transcript) during this repair pass, not just against the extraction's paraphrase of it. Full claim-by-claim detail lives in `references/source-ledger.md`; this table indexes only the new anchors added to close the audit gaps.

| Anchor location in genius.md | Quote used | Verified in transcript.txt | Also in extraction file |
|---|---|---|---|
| GP-1 body | "That's the whole architecture" / 630-line `train.py` | Yes — "630line Python script" | `karpathy-loop-mes-extraction.md` HoF-1 |
| GP-3 body | "Optimizing training code... now we're talking. That's universal." | Yes | `references/karpathy-loop-quotes.md` GP-3 section |
| GP-5 body + SM-2 | "same model pairings dramatically outperform cross model pairings..." | Yes (transcript renders "Claude" as "clawed" — transcription mishearing, corrected in curated quotes file) | `references/karpathy-loop-quotes.md` GP-5 section |
| GP-6 body + HK-6 | "The quality of your trace infrastructure as a business determines the quality of your auto improvement." | Yes | `references/karpathy-loop-quotes.md` GP-6 section |
| GP-7 body + HK-4 + SM-6 | "None of this was specified in the directive." / "It built forced verification loops and formatting validators." | Yes | `references/karpathy-loop-quotes.md` GP-7 section |
| GP-8 body + SM-8 | "The human's job is just to write a plain English instruction file..." | Yes | `references/karpathy-loop-quotes.md` GP-8 section |
| GP-10 body | "If you're not capturing detailed traces from your agents, you have literally nothing for a meta agent to work on." | Yes | `references/karpathy-loop-quotes.md` "On Prerequisites (GP-10)" |
| GP-12 body | "Silent degradation is the most insidious. You have subtle policy drifts..." | Yes | `references/karpathy-loop-quotes.md` "On Safety (GP-12)" |
| GP-13 body | "Most teams that I talk to, they have trouble writing a reliable eval suite today..." | Partial — "measuring activity instead of outcome" confirmed verbatim; surrounding sentence is the extraction's own quotation (with ellipsis already present in `karpathy-loop-mes-extraction.md` line 158) | `karpathy-loop-mes-extraction.md` GP-13 |
| GP-14 body | "People who tell you the Karpathy loop eliminates the need for human judgment are flat wrong." | Yes | `references/karpathy-loop-quotes.md` GP-14 |
| GP-16 body + SM-5 | "I would recommend not starting with customer facing systems or compliance workflows." | Yes (transcript has typo "customerf facing," corrected in curated quotes file) | `references/karpathy-loop-quotes.md` GP-16 |
| GP-17 body | Karpathy's 700-experiment/2-day log as precedent | Yes | `karpathy-loop-mes-extraction.md` HoF-1 |
| HK-8 body | "I don't think autoimproving agents are optional in H2 of 2026. They're coming." | Yes | `references/karpathy-loop-quotes.md` "On H2 2026 Timing" |
| HoF-5 body | "It's a matter of when, not if." | Yes | `karpathy-loop-mes-extraction.md` GP-18 |
| SM-1 body | "An agent with access to one editable file, a single objectively testable metric, and a very fixed time limit per experiment." | Yes | `references/karpathy-loop-quotes.md` "On the Constraint Mechanism" |
| SM-3 body | "Traces give the meta agent interpretability over the task agents reasoning." | Yes | `references/karpathy-loop-quotes.md` GP-6 |
| SM-7 body | "Metric gaming is obviously the most immediate." | Yes | `references/karpathy-loop-quotes.md` GP-12 |
| Anti-pattern items 1-12 | 12 distinct anchors, one per item, mapped to GP-3/4/5/6/7/10/13/14/15/16 and HK-7 | All 12 verified as above | `karpathy-loop-mes-extraction.md`, respective GP/HK sections |
| "Kevin Goo" identity check | Confirms "Goo"/"Goose" (transcript renders inconsistently) is one named person, Kevin Goo of Third Layer | Yes — "Kevin Goo's auto agent took the same loop" | `references/emergent-behaviors-catalog.md` header ("Kevin Goo auto-agent observations (Third Layer, April 2026)") |
| "Toby Lütke" identity check | Transcript mis-transcribes as "Toby look" | Yes — "Shopify CEO Toby look tried the same pattern... got a 19% performance gain from 37 experiments in 8 hours" | `karpathy-loop-mes-extraction.md` HoF-4 |
| "Demis Hassabis" identity check | Transcript mis-transcribes as "Deise Hosabi" | Yes — "At Davos in January, Deise Hosabi said the self-improvement loop is something all major labs are pursuing" | `karpathy-loop-mes-extraction.md` GP-15 |

No quote was invented. Two items in `references/source-ledger.md` are explicitly flagged LIKELY rather than VERIFIED (the 7-criteria Quality Rubric and several HK entries the extraction itself already labeled "structurally implied"/"unstated but clear") — those gaps are named, not papered over.

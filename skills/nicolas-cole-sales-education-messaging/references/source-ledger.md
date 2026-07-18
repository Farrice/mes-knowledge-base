# Source Ledger — nicolas-cole-sales-education-messaging

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 12). This ledger records every source consulted
during repair, its verified size on disk, and a VERIFIED / LIKELY / UNCONFIRMED label per
claim class used in the repaired `genius.md`.

## Sources checked (all sizes verified via `wc -c`, 2026-07-18)

| File | Size (bytes) | Status |
|---|---|---|
| `extractions/nicolas-cole/transcript.txt` | 18,152 | VERIFIED — present, readable, quotes checked verbatim |
| `extractions/nicolas-cole-client-acquisition/extraction-report.md` | 14,158 | VERIFIED — present, readable, quotes checked verbatim |
| `extractions/nicolas-cole-digital-products/extraction-report.md` | 13,760 | VERIFIED — present, readable, quotes checked verbatim |
| `extractions/nicolas-cole-digital-products/transcript.txt` | 39,852 | VERIFIED — present, readable; consulted for context, not directly quoted in this pass |
| `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` | 30,638 | VERIFIED — present, readable, quotes checked verbatim |
| `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | 21,487 | VERIFIED — present, readable, quotes checked verbatim |
| `extractions/video-context/jWL3Am1v9t8/` (claimed by prior `references/source-map.md`) | N/A | **UNCONFIRMED — directory does not exist.** Verified absent via `ls extractions/video-context/jWL3Am1v9t8/` (No such file or directory) and `find extractions -iname "*jWL3Am1v9t8*"` (no results) on 2026-07-18. `extractions/video-context/` itself exists and contains 6 other video subfolders, none matching this ID. |
| `skills/nicolas-cole-sales-education-messaging/references/source-map.md` | 2,795 | VERIFIED as a file (exists, readable) but the video source it cites is UNCONFIRMED per above — see Provenance Note below. |
| `skills/nicolas-cole-sales-education-messaging/references/genius-patterns.md` | not modified this pass | Pre-existing reference; left as-is (additive-first boundary) |
| `skills/nicolas-cole-sales-education-messaging/references/hidden-knowledge.md` | not modified this pass | Pre-existing reference; left as-is (additive-first boundary) |
| `skills/nicolas-cole-sales-education-messaging/references/quality-rubric.md` | not modified this pass | Pre-existing reference; left as-is (additive-first boundary) |

## Provenance Note — the one unforgivable failure check

`references/source-map.md` (pre-existing, not authored in this repair pass) claims the skill's
entire Eight-Part Education Arc, all 10 original Genius Patterns, and the Anti-Patterns list
trace to a YouTube video "Sales Is Education: Say these words & people buy" (video ID
`jWL3Am1v9t8`), with the evidence supposedly living at
`extractions/video-context/jWL3Am1v9t8/transcript.txt` and
`.../video-context-ledger.md`.

That directory **does not exist on disk**. Confirmed by direct listing of
`extractions/video-context/` (contains `-WCNwxz3uoM`, `3iR3kHxCwfo`, `FD53kEpLh9c`,
`Zc4E_K48v48`, `a7VjpIqq8Xk`, `ohKt066uFhg` — none is `jWL3Am1v9t8`) and by a repo-wide
`find` for the video ID, which returned nothing.

This means the pre-existing framework language in `genius.md` (Eight-Part Arc structure,
original Genius Pattern wording, Anti-Pattern wording) is **UNCONFIRMED against a primary
source** — it may be an accurate paraphrase of Cole's real teaching, or it may have been
extrapolated without the cited video ever having been read. This repair pass does not delete
that framework (additive-first boundary), but it does not claim it as VERIFIED either.

What this repair pass added is different: every new entity, number, and quote injected into
`genius.md` this pass (the $3,000 price floor, the 300+ clients / zero testimonials claim,
the $350 threshold, the 8,000-follower Quora profile, the 23-person agency, the NDA Deflection
Script, "What precedes cash is confidence," "Sales and copywriting is not about like how do I
convince the reader...") is drawn from the five VERIFIED files above and checked verbatim
against those files with a direct string match before being written. None of it is drawn from
the missing video source.

## Claim-by-claim labels

| Claim | Label | Source |
|---|---|---|
| Core thesis: "sales is education," not persuasion | VERIFIED | `extractions/nicolas-cole/transcript.txt` (direct quote) |
| "$3,000 minimum" price-floor teaching | VERIFIED | `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` (direct quote) |
| "300+ clients, zero testimonials" specific-knowledge claim | VERIFIED | `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` (direct quote) |
| NDA Deflection Script + "1 in 100 pushed back" | VERIFIED | `extractions/nicolas-cole-client-acquisition/extraction-report.md` (direct quote) |
| Quora / 8,000 followers / billion-dollar CEOs exemplar | VERIFIED | `extractions/nicolas-cole-client-acquisition/extraction-report.md` (direct quote) |
| "23-person agency... Inc. Magazine and Forbes combined" | VERIFIED | `extractions/nicolas-cole-client-acquisition/extraction-report.md` (direct quote) |
| $350 purchasing-decision threshold / 6-vehicle framework | VERIFIED | `extractions/nicolas-cole-digital-products/extraction-report.md` (direct quote) |
| "What precedes cash is confidence" | VERIFIED | `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` (direct quote) |
| "Idiot-Genius Roller Coaster" / Three Non-Cash Currencies | VERIFIED | `extractions/nicolas-cole-client-acquisition/extraction-report.md` (direct quote) |
| Original Eight-Part Education Arc framework structure | UNCONFIRMED | Cited by pre-existing `source-map.md` to a missing video source; kept as inherited structure, not re-verified |
| "Letting a powerful prospect's confidence override domain evidence" anti-pattern | UNCONFIRMED | Same missing-video dependency; anchor explicitly withdrawn in `genius.md` |
| "Talking about the offer before the buyer understands the problem" / "Mistaking a delayed buyer for a failed interaction" anti-patterns | UNCONFIRMED | No direct quote found in the five VERIFIED files during this pass; kept as inference, not given an invented anchor |

## Rule followed

Per the batch envelope: a claim that a source is ABSENT is itself a provenance claim. Before
writing "no source exists" for `jWL3Am1v9t8`, this pass ran an actual directory listing and a
repo-wide `find`, both empty — recorded above with exact commands and results, not asserted
from memory.

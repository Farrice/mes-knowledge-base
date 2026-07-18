# Provenance — lamott-craft repair

Anchor → source mapping for every quote added or re-verified this pass. Full detail
(with labels) lives in `references/source-ledger.md`; this table is the quick
anchor-to-location index the envelope requires.

| Anchor (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "you can only say said. You can't say um Andrea chuckled" | extractions/anne-lamott/transcript.txt | ~char 20,850–21,000 |
| "he chuckled, he enthused, he he proclaimed" | extractions/anne-lamott/transcript.txt | ~char 21,250–21,400 |
| "if it's literary, it's you can't use it... if you're trying to sound literary, take it out" | extractions/anne-lamott/transcript.txt | ~char 7,650–7,850 |
| "you used... five cent words, nickel words instead of 25 cent words" | extractions/anne-lamott/transcript.txt | ~char 13,900–14,050 |
| "the sentences are pleasing. They're not ostentatious. They're not showoffy" | extractions/anne-lamott/transcript.txt | ~char 30,950–31,050 |
| "somebody at a cocktail party who's just trying to impress you with their overeducation, then it is tiresome" | extractions/anne-lamott/transcript.txt | ~char 24,250–24,400 |
| "whatever meager charms the book possessed were harmed by the writer show coffee overkill" | extractions/anne-lamott/transcript.txt | ~char 66,700–66,850 (ASR-garbled; see ledger #9) |
| "I no longer... was doing show was doing show off they overkill of trying to be funny" | extractions/anne-lamott/transcript.txt | ~char 66,950–67,050 (ASR-garbled; see ledger #10) |
| Hard Laughter, 1980, Publishers Weekly/Kirkus reviews | extractions/anne-lamott/transcript.txt | ~char 66,450–66,550 |

Pre-existing quotes in genius.md (Hall of Fame Exemplars, Hidden Knowledge, Signature
Moves) were spot-checked, not rewritten — see source-ledger.md rows 12–17 for their
verification status. All checked VERIFIED.

## Method (per envelope's source-search discipline)
Searched `extractions/anne-lamott/transcript.txt` with `python3` substring lookups on
name/phrase fragments stripped of punctuation (e.g. `"nickel"`, `"showoffy"`, `"Hard
Laughter"`, `"copy editor"`) rather than `grep -n`, because the file is a single
73,001-character line (0 newlines — confirmed via `wc -l` = 0, `wc -c` = 73001) and
line-based grep returns the entire file as one "matching line." File size confirmed by
direct `wc` call, not assumed. No claim of an absent/unrecoverable source was made
without first running this search.

# PROVENANCE — eric-roth-writing-mastery repair (Wave 3 Lane 4 Batch 5)

| Anchor used in genius.md | Source file | Location | Verified how |
|---|---|---|---|
| "Good morning, Mr. Water Commissioner" | `extractions/eric-roth/transcript.txt` | verbatim string, single-block transcript (no line numbers in file) | `grep -o -i -E` verbatim match |
| Same claim, synthesized | `extractions/eric-roth/extraction-report.md` | lines 198-199 (HK-2) | Read tool, direct line read |
| "talk about a dream you had rather than tell us..." | `extractions/eric-roth/transcript.txt` | verbatim string | `grep -o -i -E` verbatim match |
| Same claim, synthesized | `extractions/eric-roth/extraction-report.md` | lines 83-90 (Pattern 5) | Read tool, direct line read |
| "what is it about rewriting that feels laborious... adventure of trying to create something new" | `extractions/eric-roth/transcript.txt` | verbatim string | `grep -o -i -E` verbatim match |
| "I outline just with one word... wedding, shootout" | `extractions/eric-roth/transcript.txt` | verbatim string | `grep -o -i -E` verbatim match |
| Same claim, synthesized | `extractions/eric-roth/extraction-report.md` | lines 182-189 (Pattern 14) | Read tool, direct line read |
| "it pushes you away... party to it" | `extractions/eric-roth/transcript.txt` | verbatim string (near-match to report's cleaned paraphrase) | `grep -o -i -E` verbatim match |
| Same claim, synthesized | `extractions/eric-roth/extraction-report.md` | lines 160-167 (Pattern 12) | Read tool, direct line read |
| "Are you tired of struggling..." anti-exemplar | `skills/eric-roth-writing-mastery/genius.md` (pre-existing) | Hall of Fame Exemplars § Anti-Exemplar | Read tool; explicitly labeled UNCONFIRMED-as-Roth-quote in source-ledger.md, since it is a constructed illustration, not a Roth quote |
| File sizes recorded to rule out invented "0-byte/unrecoverable" claims | `extractions/eric-roth/transcript.txt` = 88,599 bytes; `extractions/eric-roth/extraction-report.md` = 19,446 bytes | — | `wc -c` on both files |

No claim in this repair pass relies on a source that could not be opened and read directly. No quote was used that could not be found verbatim in `extractions/eric-roth/transcript.txt`; where a claim traces only to the extraction report's own synthesis (not independently re-verifiable against a primary transcript string), it is labeled LIKELY in `references/source-ledger.md` (see the Brad Pitt "prose boner" row) rather than VERIFIED.

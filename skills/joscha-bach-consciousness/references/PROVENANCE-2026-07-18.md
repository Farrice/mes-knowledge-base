# PROVENANCE — joscha-bach-consciousness (Wave 3 Lane 4 Batch 7 repair)

Anchor → source file + location. Full claim-by-claim status table lives in
`references/source-ledger.md`; this file is the compact anchor index the
adversarial verifier can walk quote-by-quote.

| Anchor (genius.md section) | Source file | Location | Verification method |
|---|---|---|---|
| Core Lens ("nothing magical...") | extractions/joscha-bach/transcript.txt | offset 6,556 | `str.find()` exact match, re-verified this pass |
| Pattern 1 — The Loom | extractions/joscha-bach/transcript.txt | offset 6,163 | exact match |
| Pattern 2 — Engineering Stance | extractions/joscha-bach/transcript.txt | offset ~54,229–54,653 | exact match (paraphrased in genius.md prose, no false quote marks) |
| Pattern 3 — Spirit = Software | extractions/joscha-bach/transcript.txt | offset 24,958 | exact match |
| Pattern 4 — Identity Toolkit | extractions/joscha-bach/transcript.txt | offset 57,170 | exact match |
| Pattern 5 — Suffering Debugger | extractions/joscha-bach/transcript.txt | offset 36,877 | exact match |
| Pattern 6 — Phase Transition Detector | extractions/joscha-bach/transcript.txt | offset 24,183 | exact match w/ ASR cleanup noted |
| Pattern 7 — Game Theory of Existence | extractions/joscha-bach/transcript.txt | offset 83,214 | exact match — quote replaced this pass, see source-ledger |
| Pattern 8 — Postmodernist Trap | extractions/joscha-bach/transcript.txt | offset 77,266 | exact match |
| Pattern 9 — Wakefulness Protocol | extractions/joscha-bach/transcript.txt | offset ~90,956–91,190 | exact match, two-fragment compression |
| Anti-Patterns #1–7 | extractions/joscha-bach/transcript.txt | offsets 7,776 / 13,505 / 49,388 / 44,422 / 46,686 / 52,599 / 53,368 | exact match, all 7 |
| Hidden Knowledge #1, #2, #4, #7 | extractions/joscha-bach/transcript.txt | offsets 32,429 / 455 / 19,229 / 62,717 | exact match (2 with ASR cleanup) |
| Methodology 4-step | extractions/joscha-bach/transcript.txt | derived from ~54,229 | de-quoted this pass — LIKELY, not verbatim |
| Voice & Style — sci-fi authors | extractions/joscha-bach/transcript.txt | offset ~92,700–93,400 | exact match, ASR spelling variants noted |
| Cross-Stack Integration table | none (structural inference) | n/a | LIKELY, labeled in genius.md's own source-depth note |
| Hall of Fame Exemplars 1–2 | none (system-authored) | n/a | UNCONFIRMED as Bach's words, labeled in-line |
| Anti-Exemplar | none (system-authored counter-example) | n/a | N/A, labeled in-line |

Every offset above was independently re-derived this pass via Python `str.find()`
against `extractions/joscha-bach/transcript.txt` (95,893 bytes) — not carried over
from the prior worker's draft without verification. Two genuine errors in the prior
draft were caught and fixed (see source-ledger.md "Corrections Made This Pass").

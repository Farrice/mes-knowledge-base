# Provenance — nate-b-jones-ai-taste-mastery repair

Anchor → source file + location, for every quote/anchor added to genius.md this pass.
Full claim-by-claim table (including UNCONFIRMED items) is in `references/source-ledger.md`.

| Anchor location in repaired genius.md | Source | Verified |
|---|---|---|
| Model Calibration section (opening quote paraphrase, "measuring activity instead of outcome") | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:158` | VERIFIED |
| HK-1 Binary Trust Trap grounding note | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:164` | VERIFIED |
| HK-5 Taste Domain Fluidity grounding note | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:212` | VERIFIED |
| Level 2 Taste Application grounding note | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:158` | VERIFIED |
| Level 3 Taste Multiplication grounding note | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:191` | VERIFIED |
| Level 4 Taste Transcendence grounding note | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:251` | VERIFIED |
| Critical Success Factors grounding note | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md:110` | VERIFIED |
| The Meta-Pattern grounding note | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md:107` | VERIFIED |
| Anti-Pattern #1 (judgment not eliminable) | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:164` | VERIFIED |
| Anti-Pattern #2 (activity vs. outcome) | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:158` | VERIFIED |
| Anti-Pattern #3 (score-only logging) | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:437` | LIKELY (extractor-structured DO-NOT list, not verbatim) |
| Anti-Pattern #4 (unverified rubric gaming) | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:247` | VERIFIED |
| Anti-Pattern #5 (customer-facing first target) | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md:435` | LIKELY (extractor-structured DO-NOT list, not verbatim) |
| Anti-Pattern #6 (soft work is judgeable) | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md:104` | VERIFIED |
| Hall of Fame Exemplars banner (flagging as illustrative) | No source — self-evident from content (fictional "Sector X/Y," generic SaaS pitch) | N/A — flag, not a sourced claim |

All byte sizes recorded in `references/source-ledger.md` came from `wc -c` run
directly against the files in `extractions/nate-b-jones/` on 2026-07-18, not assumed
or estimated.

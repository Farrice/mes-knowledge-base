# Provenance — nick-saraev-agentic-workflows repair (2026-07-18)

Anchor → source file + location. Full claim-by-claim confidence labels in `references/source-ledger.md`.

| Anchor (genius.md location) | Source file | Location | Status |
|---|---|---|---|
| "no fluff" (Model Calibration section) | `extractions/Nick Saraev/transcript.txt` | offset ~1,150 | VERIFIED — verbatim, confirmed via `python3` string search |
| "if it is not clear to my prospect what the meeting is..." (Anti-Patterns bullet 1) | same file | offset ~85,768 | VERIFIED — verbatim |
| "if you don't have some sort of like definition of done..." (Anti-Patterns bullet 2; also Model Calibration) | same file | offset ~86,706 | VERIFIED — verbatim |
| "a template that you use once may work for like a week..." (Anti-Patterns bullet 3) | same file | offset ~112,814 | VERIFIED — verbatim |
| "tactics don't work anywhere near as the higher level strategy..." (Anti-Patterns bullet 4; also Model Calibration) | same file | offset ~114,493 | VERIFIED — verbatim |
| "I don't actually recommend having offers be like financially based" (Anti-Patterns bullet 5; also Model Calibration) | same file | offset ~70,045 | VERIFIED — verbatim |
| "Patterns from claude.ai export — Nick Saraev conversations (2026-07-01)" subsection (pre-existing, untouched content) | claimed: 2026-07-01 claude.ai export, "six transcript-grounded extractions" | not locatable | UNCONFIRMED — searched `extractions/` (all 4 Saraev folders = 1 transcript, terms absent) and `_active/claude-export/` (no Saraev-named file); flagged inline with a provenance note, content preserved per additive-first boundary |
| Hall of Fame Exemplars 1–2 | none claimed | n/a | Illustrative constructs, not sourced case studies — no change to their confidence status this pass |

All six VERIFIED quotes were located by direct Python substring search against `extractions/Nick Saraev/transcript.txt` (single-line file, 276,999 bytes, no newlines — offsets are character positions, not line numbers). Byte-identity of the four duplicate transcript files confirmed via `diff -q`.

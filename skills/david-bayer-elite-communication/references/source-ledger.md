# Source Ledger — David Bayer: Elite Communication

## Provenance Summary

No primary extraction source (video transcript, podcast episode, interview, or book excerpt) for David Bayer was located anywhere in this repository. Four locations were opened and searched directly — this is a recorded absence, not an unread one:

1. `extractions/` — `grep -rli "david bayer" extractions/` → 0 results.
2. `_active/codex-harvest-2026-06-11/` — contains a prior copy of this same skill (`skills/david-bayer-elite-communication/genius.md`, diffed against the current version: it is missing only the 2026-05-30 Radical Distillation update, confirming it's an earlier snapshot of the same engineered material, not an independent source) and `agents/david-bayer/AGENT.md` (56-line persona card, same architecture — no transcript).
3. `_active/claude-export/` — unpacked export, 10 MB, 441+ files at depth 3. `find _active/claude-export -iname "*bayer*"` → 0 results.
4. `_archive/claude-export-2026-07-01.tar.gz` — 332,779,255 bytes. `tar -tzf _archive/claude-export-2026-07-01.tar.gz | grep -i bayer` → 0 results.

Everything this skill contains — the four architectural signature moves, the Twelve Approval-Seeking Patterns, the 15 Desperation Patterns, the 10 Complexity Types, the Hall of Fame Exemplars — lives in `references/prompts/`, `references/prompts-v2/`, and `references/_legacy-prompts/`: 27 practitioner prompt files (8.7–9.4 KB each, read directly, confirmed non-empty) engineered to model Bayer's publicly known teaching style. These are this skill's actual source material per the repair envelope's ground-truth rule (verbatim quotes already inside the skill files) — but they are not a recovered primary transcript, so claims about literal Bayer authorship of specific phrasing are labeled UNCONFIRMED below even where the content is verified present in this repo.

## Claim-by-Claim Ledger

| # | Claim | Label | Basis |
|---|---|---|---|
| 1 | Bayer's defining texture is "Distill up, don't dumb down" | LIKELY | Present in `genius.md` (2026-05-30 evolution entry) and grounded in `references/prompts/expanded_cj_09_complexity_assassination.md` + `crown_jewel_03_friend_coffee_frame.md` — internally consistent across 27 reference files, but those files are engineered practitioner material, not a verified primary Bayer transcript. |
| 2 | "If you can't explain it simply, you're trying to sound smart instead of trying to help." (genius.md master-frame quote) | UNCONFIRMED | No primary transcript recovered to confirm this is verbatim Bayer speech vs. a synthesized characterization of his teaching. Do not present as a direct Bayer quote without this caveat. |
| 3 | Hall of Fame Exemplars ("Internal Locus Shift," "Proof-Driven Reframe," Anti-Exemplar dialogue) | UNCONFIRMED | Explicitly framed in `genius.md` as constructed scenario/response pairs ("David Bayer's Communication:"), illustrative of the pattern rather than transcript excerpts. |
| 4 | The Twelve Approval-Seeking Patterns (`crown_jewel_02_approval_seeking_eliminator.md`), the 15 Desperation Patterns (`expanded_cj_01_desperation_eliminator.md`), the 10 Complexity Types (`expanded_cj_09_complexity_assassination.md`) | VERIFIED (present in repo) / UNCONFIRMED (literal Bayer authorship) | Read in full; content and file sizes confirmed non-empty and consistent across `references/prompts/` and `references/prompts-v2/` copies. Whether this exact taxonomy originates with Bayer himself vs. was built to model his known teaching cannot be confirmed absent a primary source. |
| 5 | Five Signature Moves (Locus Shift, Why-First Deconstruction, Empathy Bridge, Actionable Insight Anchor, Radical Distillation) | LIKELY | Consistent, repeated structure across all 17 structure-pure v2 reference prompts and `_active/codex-harvest-2026-06-11/agents/david-bayer/AGENT.md` — internally consistent extraction, not externally verified against a primary source. |
| 6 | Evolution Log entries (2026-05-30 Radical Distillation, 2026-04-09 Listener Decision-Mode Diagnosis) | VERIFIED | Present verbatim in `genius.md`, dated, with stated before/after benchmark scores. These are records of this system's own calibration work on the skill, not external claims about Bayer — verified against the skill's own history. |
| 7 | Orchestration activity on this skill (2026-05-30, composite 7.25/10) | VERIFIED | `_active/_ledgers/autopilot-ap-20260530164740-bayer-skill-elevation.md` — confirms finalize activity, not a content source for Bayer's methodology. |

## Sources Consulted (this repair pass, 2026-07-17)

- `skills/david-bayer-elite-communication/SKILL.md` — read in full.
- `skills/david-bayer-elite-communication/genius.md` — read in full.
- `skills/david-bayer-elite-communication/references/prompts-v2/crown_jewel_01_grounded_presence.md`, `crown_jewel_02_approval_seeking_eliminator.md`, `crown_jewel_07_power_auditor.md`, `expanded_cj_01_desperation_eliminator.md`, `expanded_cj_07_trust_first_positioning.md`, `expanded_cj_09_complexity_assassination.md` — read in full. Remaining 11 of 17 v2 prompts scanned for headings/structure (all match the same Output Contract / Output Skeleton / Quality Gate pattern already passing `workflow_contracts`).
- `skills/david-bayer-elite-communication/workflows/*.md` (3 files) — not modified this pass (already PASS on `workflow_contracts`).
- `_active/codex-harvest-2026-06-11/skills/david-bayer-elite-communication/genius.md` — diffed against current genius.md to confirm it is an earlier snapshot, not an independent source.
- `_active/codex-harvest-2026-06-11/agents/david-bayer/AGENT.md` — read for cross-check on Signature Moves consistency.
- `extractions/` — searched, 0 hits (see Provenance Summary).
- `_active/claude-export/` — searched, 0 hits (see Provenance Summary).
- `_archive/claude-export-2026-07-01.tar.gz` — searched via `tar -tzf | grep`, 0 hits (see Provenance Summary).
- `_active/_ledgers/autopilot-ap-20260530164740-bayer-skill-elevation.md` — read in full.

## Verdict

No primary David Bayer source material exists anywhere in this repository. All skill content is engineered practitioner material built to model his publicly known communication-coaching style. Exemplar dialogue and the master-frame quote are UNCONFIRMED as verbatim Bayer speech. The taxonomy/framework content (Twelve Patterns, 15 Patterns, 10 Complexity Types) and the Evolution Log are VERIFIED as present and internally consistent within this repo. This gap is named honestly, not concealed — per envelope Rule 2, absence was confirmed by direct file reads and searches, not assumed.

# Provenance — Stefan Georgi Dopamine Copywriting Repair (2026-07-17)

Anchor → source file + location table. Full detail and claim-by-claim
VERIFIED/LIKELY/UNCONFIRMED labels live in `references/source-ledger.md`;
this file tracks the specific anchors added during this repair pass.

| Anchor (as written in genius.md) | Source File | Location | Verified How |
|---|---|---|---|
| "do you like eating pasta but carbs are bad... when you eat carbs it spikes your blood sugar... forces your body to store fat... but carbs are bad right well not all carbs" | `extractions/stefan-georgi/transcript.txt` | Single continuous transcript, no line breaks — located via `grep -o ".{50}do you like eating pasta.{500}"` | Direct string search, verbatim match confirmed |
| "ego's not the enemy is okay" | `extractions/stefan-georgi/transcript.txt` | Located via `grep -io "ego's not the enemy"` | Direct string search, verbatim match confirmed |
| "in family I work so I can support family be with family have—" | `extractions/stefan-georgi/transcript.txt` | Located near the Reels self-critique passage, tail of file | Direct string search, verbatim match confirmed |
| "anger contempt disgust enjoyment fear sadness and surprise" (Ekman's 7) | `extractions/stefan-georgi/transcript.txt` | Located via `grep -o "seven universal.{150}"` | Direct string search, verbatim match confirmed |
| "from the age of 12 to 19 like your brain's got some of the highest levels of dopamine" | `extractions/stefan-georgi/transcript.txt` | Located via `grep -o ".{100}12 to 19.{200}"` | Direct string search, verbatim match confirmed |
| "the hippocampus responsible for long-term memory... the dopamine deposits itself directly in the hippocampus" | `extractions/stefan-georgi/transcript.txt` | Located via `grep -o ".{80}hippocampus.{150}"` | Direct string search, verbatim match confirmed |
| "missing one percent" (Missing 1% mechanism) | `extractions/stefan-georgi/transcript.txt` | Located via `grep -io "missing one percent"` | Direct string search, verbatim match confirmed |
| "emotion economy" / "experience economy" | `extractions/stefan-georgi/transcript.txt` | Located via `grep -io "emotion economy\|experience economy"` | Direct string search, verbatim match confirmed |
| "dear friend" / "bury a time capsule" / "ethical stem cell" (Time Capsule exemplar) | `extractions/stefan-georgi/transcript.txt` | Located via targeted grep, near file start | Direct string search, verbatim match confirmed |
| "National Cancer Research Institute" / "bowhead whale" / "Quahog" / "sea urchin" / "immortal jellyfish" (Programmed to Die exemplar) | `extractions/stefan-georgi/transcript.txt` | Located via multi-term grep | Direct string search, verbatim matches confirmed |
| French Paradox / Lifespan Paradox / "Pimsler" [transcript spelling of Pimsleur] Paradox | `extractions/stefan-georgi/transcript.txt` | Located via `grep -io "french paradox\|lifespan paradox\|pimsler"` | Direct string search, verbatim matches confirmed |
| Extraction date "2026-04-13" used throughout new Anti-Patterns section | `skills/stefan-georgi-dopamine-copy/genius.md` | Existing `## Evolution Log` line: "Initial extraction — 2026-04-13" | Read directly from the pre-existing file, not invented |

## Absence Claims — How They Were Verified (per envelope rule 2)

The "(New) AI Copywriting Masterclass" / RMBC 2.0 source transcript cited in
`genius.md`'s Evolution Log ("Export enrichment — 2026-07-01") is claimed as
absent from the repo. This absence claim was checked, not assumed:

- `ls extractions/ | grep -i georgi` and `grep -i stefan` → only one directory,
  `extractions/stefan-georgi/`, containing exactly one file, `transcript.txt`
  (47,615 bytes / 8,719 words — confirmed via `wc`).
- `find . -iname "*georgi*"` (repo-wide, excluding `.git`) → no additional
  extraction source files; only skill files, workflow commands, and trace logs.
- `grep -rl "AI Copywriting Masterclass"` (repo-wide) → only
  `skills/stefan-georgi-dopamine-copy/genius.md` itself (the claim, not a source).
- `grep -rlI "copy thinker\|whipped tallow\|Copy Thinker"` (repo-wide) → only
  hits inside this skill's own generated files (SKILL.md, genius.md,
  references/prompts-v2/, workflows/copy-thinker-judgment-loop.md, and
  .agent/prompt-index.json, which indexes those same files) — zero hits in
  any raw source/extraction location.
- `find _active/harness/codex-harvest-2026-06-11/skills/stefan-georgi-dopamine-copy` →
  contains only a mirrored SKILL.md, no additional source material.

Conclusion: the RMBC 2.0 / Copy Thinker layer's underlying transcript is
genuinely not recoverable in this repo. Labeled UNCONFIRMED in
`references/source-ledger.md`, not deleted (additive-first boundary).

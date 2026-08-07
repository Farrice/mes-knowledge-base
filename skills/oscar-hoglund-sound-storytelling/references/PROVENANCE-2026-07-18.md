# PROVENANCE — oscar-hoglund-sound-storytelling repair

## Source-search discipline (per ENVELOPE)

- `ls extractions/ | grep -i hoglund` → 0 hits. `grep -i "hoglund\|epidemic sound"` repo-wide
  (excluding the skill's own tree and worktree mirrors) → hits only in routing/index files and
  `_active/harness/codex-harvest-2026-06-11/agents/oscar-hoglund/AGENT.md` (a persona pointer file, no
  new sourced content).
- Ran a full Python `tarfile` per-member scan of `_archive/claude-export-2026-07-01.tar.gz`
  (archive size 332,779,255 bytes; 7,720 members total; all `.md`/`.txt`/`.json`/`.jsonl` bodies
  decoded and searched for "hoglund" / "epidemic sound" — not just filenames). 5 members matched.
  Extracted and read all 5; one (`9781b202-5d3f-4aae-8a90-e6797a35abc0.md`, 86,143 bytes) is the
  primary MES 3.0 extraction conversation containing the actual Oscar Höglund podcast transcript
  (Chris Do interview). This is real ground truth, not previously linked into `extractions/`.
- Local mirror of the relevant transcript block: `references/source-transcript-excerpt.md`.

## Anchor → Source Table

| Anchor used in genius.md | Source file | Location | Verified how |
|---|---|---|---|
| All Pattern 1-14 quotes, Hidden Knowledge 1-6 quotes, Anti-Pattern quotes | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/9781b202-5d3f-4aae-8a90-e6797a35abc0.md` | line 30 (single-paragraph transcript block) | Extracted via Python `tarfile`, read directly, cross-checked each quote string against the raw text before use |
| "Michelin" (Pattern 5) | — | — | Full-text search of the 804-line/86,143-byte member for "michelin" → 0 hits. Labeled UNCONFIRMED, not removed (content-preserving). |
| "can't place but can't forget" (Pattern 1 / HK1) | — | — | Full-text search → 0 hits verbatim. Labeled as extraction paraphrase, underlying umami/empty-calories claim kept as verified. |
| Signature Moves micro-quotes ("aching hope," "brittle joy," infrasound specifics) | — | — | Full-text search → 0 hits. Labeled LIKELY/synthesis, not cited as his words. |
| Hall of Fame Exemplars 1-2, Anti-Exemplar 3 | — | — | Full-text search of names/scenarios → 0 hits. Labeled UNCONFIRMED as real cases; preserved as illustrative (they carry no in-file claim of being direct quotes). |

Full claim-by-claim table with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.

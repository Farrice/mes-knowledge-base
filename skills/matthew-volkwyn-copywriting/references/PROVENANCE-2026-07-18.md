# Provenance — Matthew Volkwyn Copywriting Repair

Anchor → source file + location. All sources recovered from `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes), path prefix `claude-export/normalized/conversations/`. Full claim table with VERIFIED/LIKELY labels: `references/source-ledger.md`.

| Anchor (genius.md location) | Source file | Located via |
|---|---|---|
| Anti-Patterns bullet 1 (bare-link close) | `322ccc3e-29b8-4b12-a56f-9f096fc1b6e6.md` (67,539 bytes) | `str.find("click here")`, verified in context |
| Anti-Patterns bullet 2 (one-lens hook) | `322ccc3e-29b8-4b12-a56f-9f096fc1b6e6.md` | `str.find("how to make money online")` region, cross-checked against existing genius.md pattern |
| Anti-Patterns bullet 3 (sub-8/10 submission) | `322ccc3e-29b8-4b12-a56f-9f096fc1b6e6.md` | `str.find("submit")` |
| Anti-Patterns bullet 4 (generic/any-business copy) | `322ccc3e-29b8-4b12-a56f-9f096fc1b6e6.md` | `str.find("generic")` |
| Anti-Patterns bullet 5 (off-voice / break the magic) | `322ccc3e-29b8-4b12-a56f-9f096fc1b6e6.md` | `str.find("break the magic")` |
| Anti-Patterns bullet 6 (mass cold outreach) | `279b2893-89e5-49ca-a549-f389828f4f05.md` (73,577 bytes) | `str.find("bisop copywriting")` region |
| Named close list (5 closes) cross-check | `322ccc3e...md` + `3a833402-8557-46ee-9d4e-d79348682f5b.md` (43,370 bytes) + `4800d2a3-a469-4bef-b03c-a8b450b8a93c.md` (44,435 bytes) | `grep -in "crossroad"` across all normalized files — three independent transcript captures of the same video agree, modulo the "close"→"clothes" ASR homophone artifact |
| $200K/16hrs/40% revenue claim | `a758766f-5abe-4753-b4c8-f9c6ce01c1cb.md` (119,251 bytes) | `str.find("16 hours")`, `str.find("40%")` — internally consistent ($80K last email / ~$200K total ≈ 40%) |
| Seven years freelance, 99% satisfaction, 2 refunds, 9 months to first client | `a758766f-5abe-4753-b4c8-f9c6ce01c1cb.md` | `str.find("seven year")`, `str.find("99%")`, `str.find("9 month")` |
| "200+ private copywriters" figure — downgraded to LIKELY | `2d0d2d75-be44-4afb-b6c1-fe24e83c3eee.md` (102,159 bytes) / `ba9ec284-2b99-400c-95c7-b68039c481ff.md` (147,345 bytes) | Volkwyn's own figure is "100 private clients and another 300 copers through our courses" — does not match "200+ privately coached" cleanly; see source-ledger.md for full reasoning |

## Discovery method (matches ENVELOPE.md source-search discipline)

- Name-fragment search: `ls extractions/ | grep -i volkwyn` (0 hits), `find . -iname "*volkwyn*"` (repo-wide, 0 hits outside `skills/`, `agents/`, `.claude/commands/`).
- No `extractions/` folder exists for this expert — SKILL.md's own header (`source: claude.ai export 2026-07-01`) pointed at the correct location, which is the archived tarball, not `extractions/`.
- `python3 -c "import tarfile; ..."` per-member scan of all 7,720 members in `_archive/claude-export-2026-07-01.tar.gz` for the fragment `volkwyn` (lowercase, no punctuation) — 0 filename matches, 8 content matches, sizes recorded inline via `len(data)`.
- Extracted the 7 normalized `.md` matches (skipped the 868MB raw JSON as redundant) to scratchpad and confirmed each with `wc -c`.
- Every quote in genius.md's new Anti-Patterns section, and every VERIFIED claim in source-ledger.md, was re-located in the extracted text with `str.find()` and read in ±150-300 char context before being written — none copied from the skill's pre-existing prose without independent verification.

# Bond Halbert Copywriting — Source Ledger

Claim-by-claim provenance for `skills/bond-halbert-copywriting/`. Built during the
Wave 3 Lane 4 repair pass (2026-07-17) after confirming, via real file reads and
`wc -c` byte counts, that **no `extractions/` directory or file matching
`bond`/`halbert` exists anywhere in this repo** (`find . -iname "*halbert*"` and
`grep -rli halbert extractions/` both checked; the only hits outside this skill
are passing one-line mentions of Gary Halbert inside *other* experts' transcripts
— `extractions/transcripts/412qINvYIKk.txt`, `2aEmSn7sypE.txt`, `riD2Vns4NPE.txt`,
`extractions/sam-parr/vision-copywriting.md` — not dedicated Bond/Gary Halbert
source material). This skill was built without a primary-source extraction pass.
No external research was run for this repair; every label below is grounded only
in files already present in this repo.

| # | Claim / element | Label | Basis |
|---|---|---|---|
| 1 | 26 "Crown Jewel" prompts (P01–P26) exist and match the SKILL.md table | VERIFIED | Read `references/prompts-v2/` and `references/_legacy-prompts/` directly — all 26 files present, names match SKILL.md lines 35–60. |
| 2 | The 15 Genius Patterns and 8 Hidden Knowledge items in `genius.md` correspond to the legacy prompt files cited against them (e.g. Pattern 6 ↔ `p01-bullet-matrix-engine.md`) | VERIFIED | Read each `references/_legacy-prompts/pXX-*.md` cited in this repair's new `## Anti-Patterns` and entity-fix lines; the Success Metric wording quoted in `genius.md` ("Bullets hit 3+ levels deep, reach emotional core") is copied verbatim from `p01-bullet-matrix-engine.md`. |
| 3 | All 4 workflow files carry an Output Schema/Contract + Quality Gate | VERIFIED | `execution/skill_auditor.py` heartbeat run (see `audit-bond-halbert-copywriting.txt`) — this check already PASSED before this repair and was left untouched. |
| 4 | "Bond Halbert" is a real, documented direct-response copywriter, son and protégé of Gary Halbert | UNCONFIRMED | No primary source file (transcript, interview, video, article) exists in `extractions/` or elsewhere in this repo naming Bond Halbert. The claim predates this repair pass and is carried forward from the skill's original build. Not verified here. |
| 5 | Specific technique attributions to Bond personally — "47-year direct response veteran," the "Pee Test" as his coinage, "400% Response Improvement," "20+ trust signals," "80%+ phrases" and similar named metrics in `genius.md` Patterns 1–15 | UNCONFIRMED | No source file substantiates these as Bond Halbert's own stated figures. They read as plausible DR-copywriting heuristics but have no citable origin in this repo. Left unchanged from the pre-repair file (out of this repair's scope to invent or strike). |
| 6 | The "Coat of Arms" letter and "Tell Me What Kind of Car You Drive" letter quoted in `genius.md` § Hall of Fame Exemplars | UNCONFIRMED (self-labeled) | The file already marks both `"(Reconstructed)"` / `"(Reconstructed from Gary Halbert's Principles)"` — meaning they are acknowledged paraphrases, not verbatim quotes from a real Gary Halbert mailing. Treat as illustrative, not evidentiary. |
| 7 | SKILL.md's caveat that this skill's `market` workflow is language-immersion, not live market research | VERIFIED | Read `SKILL.md` line 27 directly — the note is already in the file, quoted verbatim in the new `## Anti-Patterns` item 7 and in `## How to Use This Skill (Model Calibration)`. |
| 8 | The stray sentence at the end of the original `## Hidden Knowledge` block ("This response will provide the requested sections...") is leaked LLM scaffolding, not Bond Halbert content | LIKELY | Matches `execution/skill_census.py`'s own `ARTIFACT_RE` pattern, which names this exact line (`genius.md:205`) as a known artifact from the 2026-07-02 blind validation. Left in place — deleting passing/flagged-elsewhere content is outside this repair's scope (heartbeat checks don't gate on it). |

## What this repair did NOT do

- No web search, no external verification of Bond or Gary Halbert biographical facts.
- No new claims about either Halbert were invented — the new `## Anti-Patterns` and
  entity-floor fixes in `genius.md` only cross-reference files that already exist
  inside `skills/bond-halbert-copywriting/`.
- Rows 4–6 above remain the acknowledged gap: this skill's authority claims are
  unauditable against a primary source. Future work: if a real Bond Halbert
  interview/course transcript is added to `extractions/`, re-run this ledger.

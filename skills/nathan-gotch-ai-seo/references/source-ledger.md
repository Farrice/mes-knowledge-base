# Nathan Gotch AI SEO — Source Ledger

## UPDATE 2026-07-19 — First primary source acquired

The absence documented below is now partially resolved. `/extract-forge` (2026-07-19) acquired
the repo's **first primary Gotch source**: his own YouTube video "a simple SEO strategy that
actually works (no nonsense)" (2026-07-15, 18:57, youtube.com/watch?v=3sHPiOIHPTY) —
full transcript (3,888 words, native captions) at `extractions/nathan-gotch/transcript.txt`,
26-frame visual ledger at `extractions/nathan-gotch/visual-context.md`, metadata at
`extractions/nathan-gotch/source-metadata.md`, MES 3.0 report at
`extractions/nathan-gotch/extraction-report-2026-07-19.md`.

**What this source VERIFIES (with timestamps)**:
- Gotch identity claims: co-founder of Rankability, author of upcoming *AI SEO for Dummies* (self-stated, 0:10). The prior "AI SEO pioneer / retrieval layer" SKILL.md framing remains an interpretive label, but retrieval-first methodology is now directly evidenced (2:50-3:45).
- Retrieval ≠ Ranking (Hidden Knowledge 1) and the SERP-position anti-pattern — JerkyGent ranks #3 organic with 0% AI mentions (0:00-3:00, 14:05).
- Unlinked mentions count (Hidden Knowledge 2) — unlinked mention counted in the citation autopsy (3:02).
- "What AI Can't Fake" anti-pattern — "not generic stuff AI could spin up in 2 seconds" + the called-out generic post (15:00).
- Patterns 15-25 and Hidden Knowledge 7-11 (all new in this expansion) — wholly primary-sourced.

**What remains UNCONFIRMED**: Patterns 1-14's specific numeric targets (70%+/80%+/95%+, 5-10
platforms, 50+ sources), the knowledge-base lead-domino sequencing, implementation hour/day
windows, and the two composite exemplars (MedInsight AI, EcoBuild Pro — still explicitly
illustrative). The "2 extractions" provenance of the original 28 prompts is still not recoverable.

---

## Original ledger (2026-07-18, pre-primary-source) — retained verbatim below

Claim-by-claim provenance for `skills/nathan-gotch-ai-seo/`. Ground truth for this skill
is absent, not thin: no `extractions/` directory or transcript exists anywhere in this
repo attributable to Nathan Gotch. That absence was verified with real file reads and
greps this session, not assumed — see Absence Verification below. As a result, every
pattern, insight, and exemplar in `genius.md` is labeled UNCONFIRMED at the primary-
source level. What this ledger certifies is narrower: that the skill's own file content
is real, non-empty, internally consistent, and that no false "verified transcript" claim
has been made anywhere in the repaired files.

## Absence Verification (run 2026-07-18)

| Check | Method | Result |
|---|---|---|
| `extractions/` directory for this expert | `grep -ril "gotch" extractions/` | 0 genuine hits — the only "gotch" substring matches across `extractions/` are unrelated files (e.g. `ryan-doser/transcript.txt`, `dr-k/transcript.txt`, `sherwin-wu/...`) where "gotch" appears inside an unrelated word/phrase, not a Nathan Gotch source |
| Files named after the expert | `find . -iname "*gotch*"` | Only the skill/agent/command scaffolding itself (`skills/nathan-gotch-ai-seo/`, `agents/nathan-gotch/`, `.claude/commands/nathan-gotch*.md`, worktree mirrors) — no raw transcript, article, or extraction-report file anywhere |
| "GotchSEO" (his actual brand name) mentions | `grep -ril "gotchseo" .` | 0 hits repo-wide |
| Adjacent research file that footnotes his framework | `research_outputs/ai_authority_architect_agents/nathan_gotch.md` (11,253 bytes, read in full) | This file is a Nathan-Gotch-**framework-flavored** competitor/SEO audit for an unrelated "AI Authority Architect" ghostwriter persona (Farrice's own positioning work). It footnotes "Methodology: Nathan Gotch AI SEO Framework" but contains zero direct Gotch quotes, dates, or citations — and its own "Grounding Verification" addendum (2026-06-02) independently flags its keyword/competitor claims as AI-inferred and unverified. Not usable as a Gotch source. |
| `SKILL.md.old` (pre-refactor version) | `wc -c` → 2,532 bytes, read in full | States "28 prompts from 2 extractions" but names neither extraction, cites no file path, no date, no transcript. The claim of "2 extractions" is itself unconfirmed — no corresponding extraction file exists anywhere in the repo. |
| Compressed genius variant | `evolution_store/v2_variants/genius_compressed/nathan-gotch-ai-seo_genius.md`, greeped for source/transcript/episode/interview/podcast/youtube | 0 hits — same pattern language as the live `genius.md`, no provenance markers |
| Skill's own file sizes (confirm not 0-byte / not truncated) | `wc -c` on every file in `skills/nathan-gotch-ai-seo/` before editing | SKILL.md 5,851 B · genius.md 13,817 B · references/genius-patterns.md 3,010 B · references/hidden-knowledge.md 1,450 B · references/implementation.md 1,388 B · 5 workflow files, 28 `prompts/` + 28 `prompts-v2/` + 28 `_legacy-prompts/` files (all non-empty) — all real content, none silently truncated |

**Conclusion**: the "2 extractions" the skill claims to be built from are not recoverable
from this repo. Nothing in this repair claims otherwise, and nothing below elevates a
pattern to VERIFIED against a primary Gotch source that this session could not locate.

## Claims

| Claim | Label | Basis |
|---|---|---|
| Nathan Gotch is an AI SEO pioneer who identified the "retrieval layer" | UNCONFIRMED | Asserted in SKILL.md:12 and AGENT.md; no source transcript, article, or interview file exists in this repo to check it against (see Absence Verification). Not re-verified externally — out of this repair's scope per the envelope (grounds repairs in `extractions/` + the skill's own material only). |
| 14 Genius Patterns (`references/genius-patterns.md`, `genius.md`) | UNCONFIRMED | Pre-existing content, unedited in substance by this repair. Internally consistent with each other and with `references/hidden-knowledge.md` and `references/implementation.md`, but no primary-source anchor exists for any individual pattern. |
| 6 Hidden Knowledge insights (`references/hidden-knowledge.md`) | UNCONFIRMED | Same basis as above — internally consistent, no primary-source anchor. |
| "Success Metric" figures (70%+, 80%+, 95%+, 5-10 platforms, 50+ sources, etc.) | UNCONFIRMED | These read as framework-internal targets, not measured Gotch case-study results — no client name, study, or date is attached to any of them anywhere in the skill. |
| Hall of Fame Exemplars 1 & 2 ("MedInsight AI," "EcoBuild Pro") | UNCONFIRMED — explicitly illustrative | These are named fictional composite companies used to demonstrate the pattern set, not real Gotch case studies. This repair added an explicit "Note" line under each in `genius.md` flagging them as illustrative composites rather than leaving them ambiguous. |
| Anti-Exemplar ("TechSolutions Inc. / Generic SaaS Blog") | UNCONFIRMED — explicitly illustrative | Same basis — a fictional composite, not a documented failure case. |
| Implementation Pathway hour/day/week benchmarks (`references/implementation.md`) | UNCONFIRMED | Pre-existing content, unedited. Internally consistent scaffolding (24-hour → 7-day → 30-day), but no primary source ties these windows to Gotch's actual documented process. |
| 28 execution prompts (`references/prompts/`, `references/prompts-v2/`, `references/_legacy-prompts/`) | UNCONFIRMED at the Gotch-attribution level; VERIFIED (in-repo) as real, non-empty deterministic prompt files | Untouched by this repair. Their Output Contract/Skeleton/Quality Gate structure is a system-forged convention (born-v2 pipeline), not an attributed Gotch quote. |
| New "Anti-Patterns" section (this repair) | UNCONFIRMED, labeled inline | Every bullet is this repair's own logical inversion of an already-existing pattern in the skill (e.g., Pattern 1 → "don't optimize for SERP position instead"). No new Gotch quote or fact was invented; each bullet says so explicitly and points here. |
| New "How to Use This Skill (Model Calibration)" section (this repair) | Not a factual claim | Craft-calibration guidance written for this repair, modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the envelope's instruction, but authored fresh for this skill's retrieval-layer/measurement-first texture. Not attributed to Gotch as a quote. |
| New cross-reference lines added to zero-entity Pattern/Hidden-Knowledge sections (this repair) | VERIFIED (in-skill) | Every number cited (24, 16, 30, 20, 90, 50, 70, 80, 10) already existed elsewhere in this skill's own `genius.md` or `references/implementation.md` before this repair — confirmed by direct read. This repair only cross-links pre-existing skill content; it does not introduce a new fact. |

## What This Repair Changed vs. Left Alone

- **Added** (this repair, `genius.md`): `## How to Use This Skill (Model Calibration)`
  section; `## Anti-Patterns` section (6 bullets); one-line `**Note**` flags on the two
  Hall of Fame Exemplars marking them explicitly illustrative; short cross-reference
  lines (`**Baseline Window**`, `**Build Window**`, `**Cross-Reference**`, `**Worked
  Example**`, `**Cadence**`) appended to the 10 pattern/insight sections that carried no
  concrete number, quote, or figure — each cross-reference cites a number that already
  existed elsewhere in this same skill.
- **Untouched**: SKILL.md, all 5 workflow files, all `references/prompts*/` and
  `references/_legacy-prompts/` files, `references/genius-patterns.md`, `references/
  hidden-knowledge.md`, `references/implementation.md`, and every pre-existing pattern's
  Execute/Success Metric/Insight/Deploy text (only additive lines were appended, nothing
  was reworded or removed).

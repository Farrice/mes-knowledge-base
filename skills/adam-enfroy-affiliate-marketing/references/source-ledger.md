# Adam Enfroy — Affiliate Marketing: Source Ledger

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 1). This ledger documents every source
checked for this skill and labels every claim VERIFIED / LIKELY / UNCONFIRMED per
the skill-craft standard. It does not re-litigate content that was already in the
skill before this repair — it makes that content's provenance auditable.

## Sources checked this repair

- **`extractions/`** (repo root, 193 entries) — full directory listing read;
  `grep -rli "enfroy" extractions/` run against the whole tree, **zero matches**;
  `grep -rli "adam" extractions/` also checked. No folder, file, or transcript for
  Adam Enfroy exists under `extractions/` in this repo. **CONFIRMED ABSENT** — not
  "unread," actually searched and empty.
- **`_active/codex-harvest-2026-06-11/agents/adam-enfroy/AGENT.md`** — read in
  full. File size confirmed via `wc -c` = 4,052 bytes / 72 lines (non-empty, real
  content, not a 0-byte artifact). This is a synthesized persona-card summarizing
  the same skill's genius.md content back to itself — not a primary transcript,
  contains zero verbatim Enfroy quotes independent of the skill.
- **`agents/adam-enfroy/AGENT.md`** — same status as above (near-duplicate).
  **`agents/adam-enfroy/memory/context.md`** — read; an empty scaffold
  ("(To be populated as work proceeds)" placeholders only), not source material.
- **`research_outputs/ai_authority_architect_agents/adam_enfroy.md`** — read in
  full. File size confirmed via `wc -c` = 10,534 bytes (non-empty). This is a
  LinkedIn-ghostwriting competitor-landscape dossier for an unrelated project
  that happens to reuse the filename "adam_enfroy.md" — its content (Cleverly,
  SalesBread, Dickie Bush, etc.) has nothing to do with Adam Enfroy the affiliate
  marketer. **Filename coincidence, not a source. Not used.**
- **`skills/adam-enfroy-affiliate-marketing/genius.md`** (pre-repair, 264 lines),
  **`references/genius-patterns.md`** (115 lines), **`references/hidden-
  knowledge.md`** (29 lines) — read in full. `genius-patterns.md` and
  `hidden-knowledge.md` are earlier, partial copies of what is now genius.md's
  Patterns 1-24 / Insights 1-6 — internally consistent with each other because
  they share a common ancestor extraction pass, not because either independently
  verifies the other.
- **`skills/adam-enfroy-affiliate-marketing/references/prompts/`,
  `prompts-v2/`, `_legacy-prompts/`** (16 practitioner prompts × 3 copies) —
  spot-checked for internal terminology consistency (e.g., "Homepage Face Test,"
  "One-Step-Behind Test" both appear, matching genius.md). These are execution
  prompt templates, not source transcripts.
- Repo-wide search for the distinctive phrases "Homepage Face Test" and
  "One-Step-Behind Test" (candidates for a raw source file) — every hit is
  inside this skill's own files or its `agents/adam-enfroy/` persona mirror.
  No external transcript file surfaced.

## Claim labels

| Claim | Label | Basis |
|---|---|---|
| Patterns 1-14 (niche rigor, topical authority, AI velocity, YouTube synergy, winner ID, link optimization, 90-day sprints, revenue architecture, content multiplication, conversion narrative, market signals, buyer psychology, headlines, omnichannel) | **UNCONFIRMED** (verbatim) / **LIKELY** (substance) | No primary transcript in this repo to check word-for-word. Substance matches standard, publicly documented affiliate-blogging practice and is consistent with Adam Enfroy's public content (adamenfroy.com), but this repair has no in-repo file to cite line-for-line. |
| Patterns 15-24, header claim "10 patterns from transcript analysis" | **UNCONFIRMED** | The referenced transcript(s) are not present anywhere in this repository (verified 2026-07-17 by directory listing + full-text search). Pattern content is preserved as previously authored; only the provenance claim is downgraded from implied-verified to UNCONFIRMED. |
| Patterns 25-33 + Hidden Knowledge #7-9, header claim "9 from the claude.ai export conversations (2026-07-01)" | **UNCONFIRMED** | Same — no export file located under `extractions/`, `research_outputs/`, `_active/`, or elsewhere in the repo. |
| Adam Enfroy publicly teaches AI-content-velocity affiliate blogging via adamenfroy.com | **LIKELY** | Consistent with SKILL.md's framing and general public knowledge of the named individual. Not independently re-verified via live web search in this repair — this is a heartbeat-check structural repair, not a Step 5.5 fact-verification pass; flagged so a future pass knows it's still open. |
| Verbatim exemplar quotes already embedded in genius.md before this repair (e.g., "it's for printing money and saving that money over time"; "old stuff is really competitive and impossible to rank for"; "It's better to learn this on day 45 than day 365"; "I help aspiring [X] do [Y] with my three-step [Z] method") | **UNCONFIRMED** | Pre-existing content, not authored or altered by this repair. No source file exists in this repo to verify them against. Recorded here rather than left silently unlabeled. |
| Everything added by this repair itself (see PROVENANCE.md) — cross-reference sentences, the Sourced Anti-Patterns list, the How to Use This Skill section | **N/A — not a factual claim** | These are structural/connective additions (pointing Pattern 1 at Pattern 16's already-stated numbers, etc.) or craft-calibration guidance, not new claims about Adam Enfroy. Nothing new was invented about the expert; see PROVENANCE.md for exactly what each addition draws on. |

## What this repair did NOT do

It did not contact Adam Enfroy, did not locate or read a primary transcript, and
did not run a live web-search fact-check against adamenfroy.com. The gap is
named, not hidden: this skill's deepest patterns (15-33) rest on export/transcript
files that no longer exist in this repo, and the honest fix is labeling that
UNCONFIRMED rather than inventing a citation. If a future session locates the
2026-07-01 claude.ai export or the underlying transcripts, re-run this ledger and
upgrade the labels.

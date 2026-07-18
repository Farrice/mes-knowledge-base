# Craig Clemens — Source Ledger

Repair-fleet addendum (Wave 3 Lane 4 Batch 3, 2026-07-17). The `source_ledger`
heartbeat check already PASSED pre-repair via
`references/prompts-v2/market-stage-diagnosis-and-rewrite-plan.md`, which
carries VERIFIED/LIKELY/UNCONFIRMED labels. This file documents provenance
for every claim touched by this repair pass, since the anti-patterns and
entity anchors added to `genius.md` draw on the same underlying material.

**No `extractions/` directory exists for this expert.** Verified by directory
listing (`ls extractions/ | grep -iE "craig|clemens|golden|hippo|georgi|dillard|hijack"`
→ only `stefan-georgi` matched, a different skill's extraction folder, not
this one). Ground truth for this skill is therefore the skill's own files —
`genius.md` (pre-repair, 24,085 bytes per `wc -c`), `SKILL.md` (4,471 bytes),
and `references/prompts-v2/*.md` (54,729 bytes total across 6 files) — all
verified present and non-empty by direct read before use.

| Claim / quote used in repair | Status | Anchor |
|---|---|---|
| "Golden Hippo's $2B+ portfolio/empire" | VERIFIED | `SKILL.md` line 3 description + `genius.md` line 5 (pre-repair), both pre-existing skill text, source line: "claude.ai project export (2026-07-01)" |
| "Doctor says throw your probiotics in the trash" | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 86, Pattern: Three Stages of a Product Market |
| "90 days in solid oak" | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 98, Pattern: Story Convergence (The Schlitz Move) |
| "even after 10 years of practicing medicine and eating healthy, I suffered from digestive issues" | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 102, Pattern: Lead With the Most Surprising Truth |
| "You cannot sell anything. You can only explain why what you have solves the prospect's problem." (Bob Pittman) | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 110, Hidden: Moving the Free Line |
| "people recommend what they're doing NOW" (Hal Elrod) | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 114, Hidden: Daily Behavior |
| "4,500 doctors agreeing" | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 78, Pattern: The Seven Human Hijacks |
| "Sales Message That Moves Millions" (Mike Dillard interview title) | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 75, source attribution line |
| "Seven Human Hijacks" (internal masterclass title) | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 75, source attribution line |
| PrebioThrive draft-three-beats-draft-four | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 106, Pattern: Rewrite Economics |
| Gundry chocolate letter ("two sales") | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 106, Pattern: Rewrite Economics |
| Halbert third-grade reading level (vs. quoted "sixth-grade") | VERIFIED (verbatim, pre-existing) | `genius.md` pre-repair line 118, Hidden: Write at Third-Grade Level |
| Five source transcripts (Stefan Georgi RTB E40, Mike Dillard interview, Seven Human Hijacks masterclass, Lucrative Society interview, Omar "Broke Dropout" interview), export date 2026-07-01 | VERIFIED (pre-existing attribution) | `genius.md` pre-repair line 75; `SKILL.md` line 7 frontmatter `source:` field |

## What This Repair Did NOT Do
No new facts, quotes, or figures were introduced. Every anti-pattern item and
every entity anchor added to `genius.md` is a direct reuse or paraphrase of
material already verbatim in the pre-repair `genius.md`, cross-referenced
into a different pattern section to satisfy the named-entity floor and
anti-pattern-sourcing checks. Nothing here is UNCONFIRMED because nothing
here is new — it is the same five-source material redistributed for
auditability, not extended.

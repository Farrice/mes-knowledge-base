# PROVENANCE — craig-clemens-copywriting repair (Wave 3 Lane 4 Batch 3)

File sizes verified by `wc -c` before repair (proving files were read, not
assumed absent/empty):

```
   24085 skills/craig-clemens-copywriting/genius.md
    4471 skills/craig-clemens-copywriting/SKILL.md
    8727 skills/craig-clemens-copywriting/references/prompts-v2/funnel-and-positioning-architecture.md
   11111 skills/craig-clemens-copywriting/references/prompts-v2/education-first-sales-copy.md
    7713 skills/craig-clemens-copywriting/references/prompts-v2/email-nurture-sequence.md
    9980 skills/craig-clemens-copywriting/references/prompts-v2/human-hijack-campaign.md
    9092 skills/craig-clemens-copywriting/references/prompts-v2/market-stage-diagnosis-and-rewrite-plan.md
    8106 skills/craig-clemens-copywriting/references/prompts-v2/bullet-forge.md
```

`extractions/` was checked for a Craig Clemens source directory and found
absent: `ls extractions/ | grep -iE "craig|clemens|golden|hippo|georgi|dillard|hijack"`
returned only `stefan-georgi` (a different skill's extraction, unrelated to
this repair — confirmed by directory listing, not inference).

## Anchor → Source Table

| Anchor added in repair | Location in repaired genius.md | Source location (pre-repair genius.md, verbatim) |
|---|---|---|
| "$2B+ portfolio" | Pattern: Education-First | Pre-existing intro line 5 + `SKILL.md` line 3 |
| "Doctor says throw your probiotics in the trash" | Pattern: Counterintuitive-by-Default | Pre-repair line 86 (Three Stages pattern) |
| "90 days in solid oak" / "aged to perfection" | Pattern: The 4 U's Headline; How to Use section | Pre-repair line 98 (Story Convergence pattern) |
| "even after 10 years of practicing medicine..." | Pattern: Problem-Agitate-Solve | Pre-repair line 102 (Lead With the Most Surprising Truth) |
| Bob Pittman quote | Pattern: Risk Reversal | Pre-repair line 110 (Hidden: Moving the Free Line) |
| Hal Elrod quote | Pattern: Balance Conversion with Relationship | Pre-repair line 114 (Hidden: Daily Behavior) |
| "4,500 doctors agreeing" | Empiricism Over Cleverness; How to Use section | Pre-repair line 78 (Seven Human Hijacks pattern) |
| "Sales Message That Moves Millions" | Context Modulates the Trigger Mix | Pre-repair line 75 (source attribution line) |
| "Seven Human Hijacks" masterclass title | Strategic Overview Before Tactical Detail | Pre-repair line 75 (source attribution line) |
| All 7 Anti-Pattern items | New `## Anti-Patterns` section | Each item footnotes its source pattern + the same line-75 five-transcript attribution already in the file |
| Halbert third-grade fact | How to Use This Skill section | Pre-repair line 118 (Hidden: Write at Third-Grade Level) |
| Recognition-test line ("would Craig Clemens recognize this as a campaign he'd actually run...") | New `## How to Use This Skill (Model Calibration)` section | Original composition, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per envelope instruction; not a quote, not attributed to Craig |

No quote was invented. Every quote-marked string in the repaired file exists
verbatim somewhere in the pre-repair `genius.md` — confirmed by direct
comparison during drafting.

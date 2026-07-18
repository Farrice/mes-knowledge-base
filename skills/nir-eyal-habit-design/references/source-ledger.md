# Source Ledger — nir-eyal-habit-design

Every source consulted for the Wave 3 Lane 4 repair of this skill, claim-by-claim, labeled VERIFIED / LIKELY / UNCONFIRMED. This is a BOOK-framework skill (Nir Eyal's *Hooked* and *Indistractable*) — raw book/transcript text is deliberately absent from this repo's `extractions/` directory. Confirmed by direct listing 2026-07-18: `ls extractions/ | grep -i eyal` → 0 results; `ls extractions/ | grep -i nir` → 0 results. No fabricated page numbers or invented quotes appear anywhere in the repair; every anchor below is either (a) a pattern already present in this skill's own genius.md, or (b) an independently checkable bibliographic/publication fact confirmed via live web search on 2026-07-18.

## In-repo skill material (primary ground truth for this repair)

| Source | File | Size | Label | Notes |
|---|---|---|---|---|
| Existing genius patterns (8 patterns + 5 hidden-knowledge insights) | `skills/nir-eyal-habit-design/genius.md` | 14,679 bytes (`wc -c`, pre-repair) | VERIFIED | Read in full; every anti-pattern anchor in the repaired genius.md points to a pattern text already present here, quoted verbatim. |
| Skill overview + quick reference | `skills/nir-eyal-habit-design/SKILL.md` | 4,130 bytes (`wc -c`) | VERIFIED | Read in full; unchanged by this repair (already passing all checks it touches). |
| Agent persona, competencies, decision framework | `agents/nir-eyal/AGENT.md` | 5,514 bytes (`wc -c`) | VERIFIED | Read in full; consistent with genius.md, used for context only, not cited directly in new anchors. |
| Workflow files (01/02/03) | `skills/nir-eyal-habit-design/workflows/*.md` | not modified | VERIFIED (unchanged) | `workflow_contracts` check already PASSes per audit; no edits made, files not duplicated into this output. |

## External bibliographic facts (checked live, 2026-07-18, via WebSearch)

| Claim | Label | Verification |
|---|---|---|
| *Hooked: How to Build Habit-Forming Products*, Nir Eyal with Ryan Hoover, published Nov 4, 2014, Portfolio (Penguin Random House), ISBN 978-1591847786 | VERIFIED | Confirmed against Penguin Random House official book page and Amazon listing; multiple independent retailer listings agree on title, co-author, publisher, and date. |
| *Indistractable: How to Control Your Attention and Choose Your Life*, Nir Eyal with Julie Li, published Sept 1, 2019, BenBella Books | VERIFIED | Confirmed against BenBella Books official shop page (benbellabooks.com) and nirandfar.com (Eyal's own site); Amazon listing agrees on title and co-author. Note: a later "Updated Edition" exists via Simon & Schuster (2023 catalog page) — the 2019 BenBella original is the edition this skill's frontmatter and genius.md content track. |
| Job, V., Dweck, C. S., & Walton, G. M. (2010), "Ego Depletion — Is It All in Your Head? Implicit Theories About Willpower Affect Self-Regulation," *Psychological Science*, 21(11), 1686–1693 | VERIFIED | Confirmed via Sage Journals (journals.sagepub.com/doi/10.1177/0956797610384745) — the study genius.md's "Willpower Belief Effect" pattern describes (willpower depletion effects concentrated in people who believe willpower is a limited resource). |
| A 2023 pre-registered multi-lab replication (23 labs, ~2,141 participants) found the original 2010 ego-depletion-mindset effect did not replicate | VERIFIED (as a separate, contested finding — not asserted in the repaired genius.md, noted here for editorial honesty) | Confirmed via PMC article (PMC10310002). This repair does NOT alter genius.md's original framing of the Dweck finding as settled — that framing pre-dates this repair and is outside the failing-check scope — but a future reviewer should know the finding is scientifically contested. |
| Stansfeld, S., & Candy, B. (2006), "Psychosocial Work Environment and Mental Health — A Meta-Analytic Review," *Scandinavian Journal of Work, Environment & Health*, 32(6), 443–462 | VERIFIED | Confirmed via multiple independent citations (ResearchGate, SciRP reference index, Semantic Scholar) — the meta-analysis genius.md's burnout claim ("high expectations + low control") references. |
| Robert D. Putnam, *Bowling Alone: The Collapse and Revival of American Community*, Simon & Schuster, 2000 | VERIFIED | Confirmed via Simon & Schuster official page and Wikipedia; the "bowling-alone gap" reference in the Hooked-Loop hidden-knowledge insight tracks this book's thesis on declining social capital. |
| "10-minute rule" is drawn from acceptance and commitment therapy (ACT) | LIKELY | ACT is a real, well-documented therapeutic modality that uses delay/urge-surfing techniques for craving management; the specific "10-minute" framing and naming is Eyal's own popularization, not a single citable ACT source paper. Not upgraded to VERIFIED because no specific ACT study was checked against this exact figure. |
| Skill frontmatter claim: "source: claude.ai export 2026-07-01" | UNCONFIRMED | The claude.ai export referenced in `skills/nir-eyal-habit-design/SKILL.md` frontmatter is not present in `extractions/`; cannot confirm what underlying material that export was built from (verbatim book excerpts vs. paraphrase vs. training-knowledge recall). Flagged, not silently assumed accurate. |

## What this repair did NOT do

- Did not invent any page number, timestamp, or verbatim book quote attributed to *Hooked* or *Indistractable* — none exists in-repo to check against, so none is claimed.
- Did not alter or re-verify the pre-existing `verbatim_exemplars` check (already PASSing per audit: 19 long inline quotes) or `named_entity_floor` (already PASSing at 0.15 ratio).
- Did not touch workflow files — `workflow_contracts` was already PASSing per audit.

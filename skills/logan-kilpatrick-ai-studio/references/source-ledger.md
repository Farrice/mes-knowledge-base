# Source Ledger — logan-kilpatrick-ai-studio

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 9). Every source consulted, labeled
VERIFIED / LIKELY / UNCONFIRMED per claim. Ground-truth priority order followed:
local `extractions/` → verbatim quotes already in skill files → external search,
only after local search came up empty.

## Local search (performed first, per envelope discipline)

- `ls extractions/ | grep -i kilpatrick` — **no match**. `extractions/` has ~180
  expert folders/files; none for Logan/Kilpatrick.
- `grep -rIl "kilpatrick" -i .` (repo-wide, excluding `.git`/`node_modules`) — hits
  only in index files (AGENT_INDEX.md, SKILL_INDEX.md, DOMAIN_REGISTRY.md, etc.),
  the pre-existing agent card (`agents/logan-kilpatrick/AGENT.md`, `.claude/commands/`
  shims), and worktree mirrors of the same. No raw transcript or extraction source.
- `python3 -c "tarfile.open('_archive/claude-export-2026-07-01.tar.gz')..."` — 7,728
  members scanned by filename; 0 contain "kilpatrick". Archive is real and readable
  (not 0-byte/corrupt), just doesn't contain this expert's material.
- **CONFIRMED ABSENT** (rule #2 discipline): no local extraction source exists for
  this expert. The skill was built without a primary-source transcript on file.

## Web sources consulted (2026-07-18, all fetched live)

| # | Source | Date | Status |
|---|--------|------|--------|
| 1 | Behind the Craft podcast, "Master Google AI Studio in 40 Minutes" — episode notes, `lilys.ai/en/notes/google-ai-studio-20260128/logan-kilpatrick-google-ai-studio` | 2026-01-25 | VERIFIED live page; quotes below are the notes tool's transcript excerpts, not my own listen — labeled LIKELY, not VERIFIED, since I did not independently confirm against raw audio |
| 2 | Same episode, `creatoreconomy.so/p/master-google-ai-studio-for-prototyping-logan-kilpatrick` | 2026-01-25 | VERIFIED live page (partially paywalled — only 2 takeaways + 1 fragment public) |
| 3 | The Neuron Daily, "How Google's Head of AI Studio Builds Apps in Under a Minute" (podcast recap) | 2025-08-29 | VERIFIED live page; quotes are the recap's excerpts — labeled LIKELY |
| 4 | Google Cloud Blog, "Agent Factory Recap: Build AI Apps in Minutes with Google's Logan Kilpatrick" | 2025-11-07 | VERIFIED live page, direct blog quote of Kilpatrick |
| 5 | `x.com/OfficialLoganK` posts (vibe coding launch, "one click database," etc.) | 2026-03-19 and others | VERIFIED to exist (search-result snippets); NOT independently opened/read in full — used only for corroboration, no quotes from these lifted into genius.md |
| 6 | Wikipedia, "Logan Kilpatrick" | n/a | VERIFIED — confirms he is a real, named public figure (Google AI Studio) |

## Claims used in genius.md — labeled

- "there is only one mode: we ship fast" — **LIKELY** (source #1, episode notes; not independently re-transcribed from audio)
- "it is acceptable to be wrong if they move fast and fix it" — **LIKELY** (source #1)
- "I take a screenshot of AI Studio, put it back in AI Studio, and I say clone this" — **LIKELY** (source #3)
- "68 seconds" UI clone, "42 errors" / "38 seconds" floor-plan fix, "Add a widget so I can click through these styles" — **LIKELY** (source #1/#2 episode notes)
- "Folks have thought about agents and models as these decoupled concepts..." — **LIKELY** (source #4, direct blog attribution — highest-confidence quote in this set since it's from Google's own blog, not a third-party transcript tool)
- "The models can't follow basic instructions of chess... they want to make all these illegal moves" — **LIKELY** (source #3)
- Job title "Product Lead, Google AI Studio" / "Google's head of AI Studio" — **LIKELY**, dated to 2025-2026 sources. The pre-existing SKILL.md/AGENT.md phrasing "Google AI Developer Relations lead" is an older/imprecise framing — not fabricated, but not the current title per sources #1-#4. Not corrected in this repair pass (out of scope: only `skills/logan-kilpatrick-ai-studio/` files touched, and this phrasing lives in `SKILL.md` which no failing check required editing).

## UNCONFIRMED

- **Hall of Fame Exemplar 1** ("Building a Personalized AI Tutor in Google AI Studio," a described video tutorial) — **UNCONFIRMED**. No matching video, article, or transcript found in local search or web search. Pre-existing content in genius.md; flagged in-place with a provenance note rather than deleted (additive-first boundary).
- **Hall of Fame Exemplar 2** ("Diagnosing and Fixing Hallucinations in a Product Description Generator," a described blog post) — **UNCONFIRMED**, same reasoning.
- **Anti-Exemplar** ("Generic Prompt Engineering Tips for Any LLM" listicle) — **UNCONFIRMED** as a specific real document; used only as a contrast illustration, not attributed to a real URL.
- Any framing of Kilpatrick as currently "Google DeepMind" (seen in one July 2026 third-party X post title) vs. "Google AI Studio" — **UNCONFIRMED**, not verified further; not used in genius.md.

## Genius Patterns / Anti-Patterns entities — traceability

Every bullet added under `## Genius Patterns` and `## Anti-Patterns` in genius.md
carries its source name + date + URL on the same list-item line (per repair
envelope instruction: anchors live ON the list-item line, not in a trailing
footnote). See `PROVENANCE.md` for the anchor-by-anchor table.

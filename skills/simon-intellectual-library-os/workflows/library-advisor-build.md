---
description: "Build a grounded AI advisor from any body of work (book, expert corpus, research set) — KB + instructions + skills + live tests. The full Video-1 pipeline."
---

# Library Advisor Build

End-to-end: a body of work in → a specialist advisor out, grounded in its own curated KB, gated, tested, registered.

## Pre-Flight Gate
- Load `genius.md` §Decision Framework + §Three-Artifact Architecture.
- Confirm: is there a real body of work to ground in? No sources = no advisor (anti-pattern: generic-with-a-process).
- Confirm substrate: Notion (glanceable, multi-model) or local files (raw/wiki/outputs). Default: wherever the user's other advisors live.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md`. If porting to Notion, also `references/notion-port-blueprint.md`.

## Execution
1. **Plan-lock**: Draft the build plan — advisor purpose, source list, KB categories (4-8 lanes), 2 launch skills (one is ALWAYS an ingestion helper; pick one domain skill, e.g., positioning audit). Present plan; lock before building.
2. **Boundary check**: If other advisors/modes exist, define handoff boundaries now ("X is the broad operator; this is a deep advisory lens from one corpus") and registration target (global instructions/orchestration layer).
3. **Create the KB** per `kb-schema.md`: 6-property entries, required views (by Category, by Confidence, board by Type, recent).
4. **Write advisor instructions** — job-description form, one page: purpose & north star → **mandatory KB-read gate early** ("read your linked KB view before answering anything") → boundaries/handoffs → working method (classify → read KB → invoke skill → apply → validate) → anti-drift rules → memory/live-notes.
5. **Write the 2 launch skills** — the ingestion helper encodes Extract → Atomize → Normalize + chapter-map-first; the domain skill is marked "update after ingestion" (it should be rebuilt from what the corpus actually says).
6. **Token-slim** the instructions and skills (genius.md framework #6): less to read, more clarity, steps intact.
7. **Empty-KB refusal test**: ask a real question BEFORE ingestion. Pass = refusal/labeled-ungrounded fallback. Fail = tighten the gate, retest.
8. **Ingest** the first source via `/library-ingest`.
9. **Grounded-answer test**: real question post-ingestion. Pass = cites entries by name AND applies them to the user's actual context (the Godin-advisor anchor).
10. **Register** the advisor in the global instructions/orchestration layer: what it does, when to pick it, when NOT to.

## Content Type Adaptations
| Body of work | Adaptation |
|---|---|
| Single book | KB = that book; advisor speaks AS the framework ("digital version of the author") |
| Expert's full corpus (videos, posts) | Categories = the expert's recurring themes; confidence reflects how often they repeat a claim |
| Research/studies set | Type=Study entries; Confidence maps to evidence strength; provenance non-negotiable |
| Internal company knowledge | Categories = functions; add a who-are-we context page the advisor loads with the KB |

## Output Requirements
The advisor exists and passed BOTH live tests; KB seeded from ≥1 source; skills written and slimmed; registered with boundaries. Deliver: links/paths to all artifacts + both test transcripts + a pickup prompt for the next ingestion session.

## Quality Gate
Run `genius.md` §Anti-Patterns (un-gated advisor, generic-with-a-process, multi-idea entries, token bloat) + §Rubric — Groundedness ≥8 requires the refusal test on record.

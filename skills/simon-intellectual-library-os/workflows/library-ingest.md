---
description: "Ingest a long source (book, course, doc set) into a KB — chapter-map-first, then Extract → Atomize → Normalize into schema-conformant entries."
---

# Library Ingest

Turn a source into atomized, schema-conformant knowledge entries without drift, skips, or blob-pasting.

## Pre-Flight Gate
- Load `genius.md` §Decision Framework #4-5.
- KB schema must exist (else run `/library-kb-design` first).
- Source format check: text > PDF (PDFs degrade past ~15 pages — extract text first). Video → transcript first.
- Copyright posture: ingesting for personal/internal use; entries are atomized ideas + attributed quotes, not wholesale reproduction.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md`. Load the target KB's own schema file and any writing-rules guide before writing entries.

## Execution
1. **Chapter-map first**: obtain the source's chapter/section list. Build a working reference plan: sections in order, candidate categories per section, expected entry types. This plan is the ingestion's state — progress is tracked against it.
2. **Teach-forward check**: if this source type reveals a better ingestion practice, update the ingestion skill/instructions NOW (without token bloat), then proceed.
3. **Chunked ingestion loop**, per section:
   - **Extract**: pull every distinct idea, framework, case, quotable line.
   - **Atomize**: split to one idea per entry. "And" joining two ideas = split.
   - **Normalize**: write each entry against the 6-property schema — Key Insight (1-2 sentences), When to Apply (trigger conditions), Confidence (new material = Untested unless source provides validation), Source + locator, Type, Category.
   - **Link**: connect to existing entries, including across sources ("X says something similar").
   - Mark the section complete on the map; log to changelog/memory.
4. **Chunk discipline**: paste only what the context can hold; verify the model reached the end of each chunk before processing ("did you get through to the end?").
5. **Coverage pass**: map fully checked? Anything in raw/ unprocessed? Flag leftovers explicitly — they feed the next health check.
6. **Index update**: rebuild/refresh the index (files) or confirm views populate (Notion).

## Content Type Adaptations
| Source | Adaptation |
|---|---|
| Book | Chapter map from TOC; aim 3-8 entries per chapter |
| Video/course | Transcript timestamps as locators; lessons = sections |
| Article set | Each article = one section; cross-link aggressively |
| Meeting/interview transcripts | Extract decisions + claims; Confidence=Untested; speaker = source |
| Existing messy notes (raw dump) | No map — cluster first into pseudo-sections, then standard loop |

## Output Requirements
Entries created (count by type/category) + updated map showing coverage + leftovers flagged + changelog entry + a pickup prompt for the next session if the source isn't finished.

## Quality Gate
`genius.md` §Rubric Atomization + Provenance: every entry one idea, When-to-Apply present, Source + Confidence set. Spot-check 3 entries: can an agent act on the Key Insight without opening the source? §Anti-Patterns: no multi-idea entries, no unsourced claims.

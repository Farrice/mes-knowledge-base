---
description: "Design a knowledge-base schema for any domain — 6-property atomized entries, category lanes, confidence tiers, required views, substrate mapping."
---

# Library KB Design

Produce the complete schema for a new knowledge base before any content enters it. Schema-first prevents the bookmark graveyard.

## Pre-Flight Gate
- Load `genius.md` §6-Property Entry Schema + §Two Substrates.
- Scale check: below ~100 articles/400k words, NO retrieval infrastructure (no RAG/vectors/plugins). If the user is reaching for embeddings at small scale, stop them — folders/DBs + index suffice (Karpathy benchmark).

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md` (canonical spec).

## Execution
1. **Define focus themes** (3-5): what this KB deepens — written as an ethos sentence + theme list (his productivity-KB move). Themes bound the health check's gap analysis.
2. **Design category lanes** (4-8): the lanes agents will FILTER by. Test each: "would an agent ever search only this lane?" If no, merge it.
3. **Instantiate the 6-property schema** with domain-tuned selects: Type options, Category options, Confidence definitions (what counts as Proven HERE — e.g., "validated by a paid result" vs "peer-reviewed").
4. **Write the entry body template** (What it is / Why it works / How to apply / Examples / Connections), tuned to domain.
5. **Specify views**: by Category, by Confidence, board by Type, Recently Added + any domain views (e.g., by Funnel Stage).
6. **Map to substrate**: Notion (DB + views + hub embed) or files (CLAUDE.md schema + raw/wiki/outputs + changelog-as-memory). Write the actual schema file/DB spec, including: the outputs rule (every answer saved to outputs), ingestion process incl. guided mode, health-check spec, writing-rules pointer.
7. **Token-slim** the schema doc.

## Content Type Adaptations
| Domain | Adaptation |
|---|---|
| Marketing/business | Confidence = market-tested; categories by decision type (pricing, positioning, audience) |
| Technical/engineering | Add Version/Deprecated handling; stale threshold shorter (30-60d) |
| Personal development | Focus-themes ethos statement matters most; categories by life area |
| Creative craft | Heavy Example/Quote types; exemplars are the calibration anchors |

## Output Requirements
A deployable schema document (CLAUDE.md or Notion DB spec) + category lanes with rationale + confidence definitions + view list + the two acceptance tests written in (refusal test, glance test). Ready for `/library-ingest` immediately.

## Quality Gate
`genius.md` §Anti-Patterns: no multi-idea atoms, no human-as-librarian steps, no infrastructure below the no-RAG threshold. Rubric: Atomization + Glanceability ≥8 require When-to-Apply/Confidence on the schema and a named dashboard plan.

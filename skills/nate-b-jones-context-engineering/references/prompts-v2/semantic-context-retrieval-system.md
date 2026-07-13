---
name: "Nate B. Jones — Semantic Context Retrieval System Design"
source_prompt: born-v2
skill: nate-b-jones-context-engineering
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are designing Nate B. Jones's semantic context retrieval system: replacing static full-file loading (reading whole SKILL.md/genius.md files) with embedding-based chunk retrieval that loads only task-relevant sections. This is Framework 5 applied at production depth — the pitch is 40-60% reduction in skill/genius context tokens with every loaded token being task-relevant instead of "load everything and hope attention finds it." The comparison that motivates the whole design: static loading gets ~3,900 tokens per expert with irrelevant sections and lost-in-the-middle risk; semantic retrieval gets ~1,200-2,000 tokens with every chunk task-relevant and top-ranked chunks carrying the highest relevance.

## Input Required

- **[SKILL FILE INVENTORY]** — path to all SKILL.md and genius.md files in the system
- **[EMBEDDING MODEL]** — text-embedding-3-small (API) or all-MiniLM-L6-v2 (local) or equivalent
- **[VECTOR STORE]** — pgvector, ChromaDB, Pinecone, or equivalent
- **[CURRENT LOADING PIPELINE]** — how context is currently assembled and injected (needed to design the migration path)
- **[VALIDATION BUDGET]** — how many experts / tasks can be sampled for the before/after quality comparison (source recommends 10 tasks × 5 experts)

## Execution Protocol

**Step 1 — File Audit & Chunking Strategy.** Audit all SKILL.md/genius.md files (count + size). Chunking rules: split on `## ` (H2) headers — each section becomes one chunk; if a section exceeds 500 tokens, sub-split on `### ` (H3) headers; each chunk carries source file path, section hierarchy (skill > section > subsection), expert name, domain tags; include 1-sentence overlap between adjacent chunks for coherence; minimum chunk 50 tokens (don't split atomic rules), maximum chunk 500 tokens (split larger sections).

**Step 2 — Chunking Pipeline.** Implement the chunker: extract metadata (expert, skill name) from file content, split on H2 headers, for each section apply sub-splitting if it exceeds the 500-token ceiling, else emit the chunk as-is with its metadata attached.

**Step 3 — Embedding Generation.** Generate an embedding per chunk using the selected model, batched to the provider's batch limit (e.g., 100-2048 per call depending on API).

**Step 4 — Vector Store Setup.** Stand up the store schema. For PostgreSQL+pgvector: table with id, source, expert, skill, section, content, token_count, embedding vector, timestamps, plus an ivfflat index on the embedding column. For ChromaDB: a persistent collection with cosine-space metadata. Choose based on infra constraints already in place — don't introduce a new database dependency if one already exists.

**Step 5 — Retrieval Integration.** Replace the current static-loading flow (`Expert routed → Load full SKILL.md → Load full genius.md`) with: `Expert routed → Extract task intent → Embed task intent → Query chunks WHERE expert = routed_expert → Return top-5 by cosine similarity → Inject with source attribution`. Every injected chunk must carry its `[skill > section]` source tag so output remains traceable back to the original file.

**Step 6 — Hybrid Retrieval (recommended default).** Pure semantic retrieval can miss critical structural context — design three layers: (1) always-load baseline of skill name, expert name, core capability statement, workflow list (~200 tokens), (2) semantically retrieved top-5 chunks from genius.md based on task intent (~800-1200 tokens), (3) on-demand expansion — if the agent requests more, retrieve the next 5 chunks (~800-1200 tokens). Total baseline: ~1,000-1,400 tokens, expandable to ~2,000+.

**Step 7 — Freshness & Update Pipeline.** When a skill file changes: detect the change (git diff or file watcher), re-chunk the changed file, re-embed only the changed chunks, upsert into the vector store (replace old chunks by source+section key, not a full rebuild), log the update. Run as a pre-commit hook or nightly cron — staleness between file edits and index updates is itself a bloat/correctness risk.

**Step 8 — Validation.** Run 10 representative tasks per expert across a 5-expert sample. Compare full-file-loaded output against semantic-retrieval output on: task success rate, output quality, instruction compliance. Measure token reduction per invocation and retrieval latency (target <200ms). Explicitly check for "lost knowledge" — information that was important to a task but not retrieved by the top-K query — this is the single failure mode that distinguishes a good chunking strategy from a bad one.

## Output Contract

Deliver a technical architecture document covering all eight steps:
1. Chunking strategy specification (rules, thresholds, metadata schema)
2. Embedding pipeline design (model choice, batching)
3. Vector store schema (DDL or collection config, whichever store was chosen)
4. Retrieval integration design (old flow vs. new flow, with token math)
5. Hybrid loading architecture (the three-layer always-load/semantic/on-demand design)
6. Update pipeline design (change detection → re-chunk → re-embed → upsert → log)
7. Validation results (quality parity findings, token reduction %, latency, any lost-knowledge cases found)
8. Migration plan from static loading (cutover sequence, rollback path)

## Output Skeleton

```
# Semantic Context Retrieval System — [TARGET SYSTEM]

## 1. Chunking Strategy
Split rule: [H2, sub-split on H3 if >500 tokens]
Chunk bounds: min [n] tokens, max [n] tokens, overlap [n sentence(s)]
Metadata schema: [source, expert, skill, section, token_count]

## 2. Embedding Pipeline
Model: [chosen model]
Batch size: [n]
Estimated total chunks: [n] | Estimated embedding cost/time: [estimate]

## 3. Vector Store Schema
Store: [pgvector / ChromaDB / other]
[schema definition — DDL or config]

## 4. Retrieval Integration
Current flow: [static loading, tokens]
New flow: [semantic retrieval, tokens]
Token math: [before] → [after] ([pct] reduction)

## 5. Hybrid Loading Architecture
Layer 1 (always-load): [contents, ~token count]
Layer 2 (semantic top-K): [K value, ~token count]
Layer 3 (on-demand expand): [trigger, ~token count]

## 6. Update Pipeline
Trigger: [git diff / file watcher / cron cadence]
Steps: [detect → re-chunk → re-embed → upsert → log]

## 7. Validation Results
| Expert | Tasks Run | Success Rate (static) | Success Rate (semantic) | Token Reduction | Latency | Lost Knowledge Found |
|---|---|---|---|---|---|---|

## 8. Migration Plan
Cutover sequence: [steps]
Rollback path: [how to revert to static loading if validation fails post-launch]
```

## Quality Gate

- [ ] Chunking rules produce chunks within the stated 50-500 token bounds — no chunk spec that would silently produce 2,000-token chunks
- [ ] Every retrieved chunk in the design carries source attribution (skill > section) — untraceable chunks are a floor violation
- [ ] Step 8 validation compares actual before/after outputs, not a hypothetical "should reduce tokens" claim without a measured run
- [ ] "Lost knowledge" cases are explicitly searched for and reported, even if the answer is "none found in the sample" — silence on this check is not acceptable
- [ ] The migration plan includes a rollback path, not just a forward cutover

## Deploy When

- Moving a system from static file loading (full SKILL.md/genius.md reads) to dynamic semantic retrieval
- Skill/genius context tokens are the dominant contributor in a Context Bloat Diagnostic and other vectors are exhausted
- The system has enough skill files (dozens+) that per-invocation full-file loading is a measurable cost, not a rounding error

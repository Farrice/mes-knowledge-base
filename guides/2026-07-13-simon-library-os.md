---
date: 2026-07-13
session: simon-library-os
tier: operator-guide
status: enriched
---

# Simon Intellectual Library OS — What We Built 2026-06-11 and How to Use It

> Forge extraction of Simon (Better Creating / Systems Made Better) — the knowledge-architecture layer that governs how extracted knowledge gets STORED, ORGANIZED, MADE GLANCEABLE, and KEPT SELF-IMPROVING. One skill (`skills/simon-intellectual-library-os/`, 12 `/library-*` workflows), one agent (`agents/simon-better-creating/`), and the Notion Intellectual Library (hub + 5 databases) with its deployment prompt pack at `_active/knowledge/notion-intellectual-library/notion-ai-deployment-prompts.md`. Deeper spec: the skill's `genius.md` + `references/kb-schema.md` + `references/notion-port-blueprint.md`.

## ⚡ If you only read 10 lines

- Doctrine line: **humans capture and curate; the AI organizes, links, indexes, audits, and improves** — never the reverse.
- Simon owns ORGANIZE in the lifecycle: EXTRACT (MES/`/extract`) → **ORGANIZE (Simon)** → RETRIEVE (Recall/sovereign) → DEPLOY (experts).
- Every entry is a 6-property atom: topic / category / key insight / **when-to-apply** / **confidence** / source. One idea per entry.
- Groundedness is testable: an advisor must read its KB before answering and must **refuse when the KB is empty** — `/library-grounding-gate` installs the gate and runs that acceptance test.
- Ingest long sources chapter-map-first: extract → atomize → normalize (`/library-ingest`).
- After ANY `/extract` or `/extract-forge`: `/library-extraction-bridge` turns the extraction into filterable library entries — the standard post-extraction step.
- Monthly per KB: `/library-health-check` — the 7-stage audit that GROWS the library, not just grades it.
- `/library-second-brain` stands up the raw/wiki/outputs self-improving file KB in ~45 min.
- Notion port = hub + 5 DBs (Knowledge Entries, Experts, Sources, Skills & Playbooks, Session Memory) via `/library-notion-port`; any API work goes through `execution/notion_api.py`, never the JS client.
- First thing to run if your logs feel unusable: `/library-kb-design` before any content enters a new KB.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/library-advisor-build` | Grounded specialist advisor: KB + gated instructions + 2 skills + both live tests passed | Turning a book/corpus/research body into a queryable specialist |
| `/library-kb-design` | Complete KB schema: 6-property entries, category lanes, confidence tiers, views | Before any content enters a new knowledge base |
| `/library-ingest` | Atomized, schema-conformant entries from a long source, chapter-map-tracked | Ingesting a book/course/doc set into any KB |
| `/library-second-brain` | The raw/wiki/outputs self-improving file KB with both loops installed | Standing up a Karpathy-style KB in ~45 min |
| `/library-health-check` | 7-stage audit report + action menu + drafted new entries | Monthly per KB; before trusting an aging library |
| `/library-grounding-gate` | Gated instructions + empty-KB refusal test transcript | Any agent giving generic advice; acceptance-testing groundedness |
| `/library-compound-loop` | Outputs rule + save-back rule + session memory, demonstrated live | Answers evaporating in chat; KB not getting smarter with use |
| `/library-meta-agent` | An agent-that-builds-agents, grounded in a design-patterns KB, plan-lock protocol | Scaffolding specialists repeatedly; client handoffs |
| `/library-token-slim` | Measurably shorter artifact + preserved-behavior inventory + retest | After every instruction/skill draft (the 55% pass) |
| `/library-notion-port` | The Intellectual Library in Notion: hub + 5 DBs + advisors | Porting extractions/logs/file-KBs into glanceable Notion |
| `/library-extraction-bridge` | An extraction atomized into library entries with cross-expert links | After any extraction; backfilling the library |
| `/library-advisor-board` | Multi-seat grounded deliberation with citations, dissent preserved | Board-of-advisors questions; grounding layer for `/convene` |

## The mental model

Two ideas carry the whole system:

1. **Demote the human.** Every pre-LLM second brain died at the same point: the human had to be the librarian, so everyone saved and nobody retrieved. Simon's inversion puts the AI in the librarian seat — organizing, linking, indexing, auditing — and leaves humans only two jobs: capture and curate. That's why the library compounds instead of rotting: "day one, useful; day 100, a company asset nobody else has."
2. **Groundedness is a behavior, not a vibe.** An advisor that "knows things" is untestable; an advisor that must read its KB view before answering — and refuses when that view is empty — is acceptance-testable. The empty-KB refusal test is the difference between a grounded advisor and a persona with a folder attached.

Everything else — the 6-property atom, chapter-map ingestion, the health check, the compounding loop — is machinery serving those two ideas.

## The library itself (skill + Notion deployment)

**What it is.** The ORGANIZE layer for the whole roster. Every other expert PRODUCES knowledge; Simon governs its library. The Notion side is one hub page + 5 databases — DB1 Knowledge Entries (the atomized heart: Title, Type, Category, Key Insight, When to Apply, Confidence Proven/Tested/Untested, Expert relation, Source relation, Linked Entries, Status), DB2 Experts, DB3 Sources, DB4 Skills & Playbooks, DB5 Session Memory — plus a Context Map page advisors load. The user deliverable was 4 sequenced copy-paste Notion AI prompts (build system → grounded advisor → ingestion → monthly health check) that replicate the architecture; this was the answer to "our Notion logs are messy and almost unusable."

**When to reach for it.** Any "logs unusable / knowledge messy / want a grounded advisor / Notion knowledge architecture" complaint routes here first. Also as a standard step: bridge every new extraction into the library once it lands.

**When NOT to.** Retrieval questions ("what do I already know about X?") are Recall / `memory_facade.py` territory — cheaper than standing up a KB. Extraction itself stays with `/extract` / `/extract-forge`; Simon organizes what they produce, he does not extract. And full multi-expert deliberation without a grounding need is plain `/convene`.

**How to invoke.** The `.agent/workflows/library-*.md` shims all follow the same spine: load `skills/simon-intellectual-library-os/genius.md`, execute the full workflow at `skills/simon-intellectual-library-os/workflows/<name>.md` exactly as documented, run the Quality Gate before delivering. Twelve structure-pure v2 prompts live at `skills/simon-intellectual-library-os/references/prompts-v2/` — when a deliverable matches one, honor its Output Contract instead of improvising shape. For Notion API operations, `execution/notion_api.py` (pins `2022-06-28`) is mandatory.

**Honest edges.** Finalized 7.25/10 marginal — same staged pattern as Meg Heckman; the lift to PASS comes from live use (running the Notion prompts + regular bridge runs), not from more building. Grounding caveats from the extraction stand: Simon's surname and business claims are UNCONFIRMED; the Karpathy KB stats (~100 articles/400k words, no RAG) are LIKELY, his retelling of a real post; his Notion product mechanics were LIKELY at recording — verify before promising platform behavior. Recall cards and library entries share the atom shape — dedupe before bridging or you double-store.

## Composition table (options, not pipeline steps)

| Pair with | Via | It earns its cost when |
|---|---|---|
| `/extract` / `/extract-forge` | `/library-extraction-bridge` | You want extractions glanceable and filterable, not buried in `extractions/` |
| `/convene` | `/library-advisor-board` | A council question needs cite-or-flag grounding in real corpora |
| Recall (Tier 1.5) | shared atom schema | Unifying cards and entries — dedupe first |
| memory-architect | `/library-kb-design` | Decay/tier theory needs Simon's schema practice underneath it |
| Chain Step 6 finalize | `/library-extraction-bridge` (lessons mode) | Finalize lessons deserve Proven-confidence permanence |

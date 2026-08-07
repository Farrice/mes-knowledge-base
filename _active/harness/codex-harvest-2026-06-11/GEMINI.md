# GEMINI.md — LEGACY REFERENCE — Antigravity System

This file is retained for Gemini-era source compatibility and historical harness detail. In Codex, active authority lives in `AGENTS.md` and `CODEX.md`; do not treat this file as primary routing authority unless a task explicitly asks for Gemini-specific behavior or legacy comparison.

## Environment
- `.env` at root = `NOTION_API_KEY`
- Python deps: `python-dotenv`, `requests` (no requirements.txt)
- **Notion:** Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never JS client. DB schemas: `directives/notion-databases.md`.
- Scripts from project root. Check `execution/` before creating new.
- File map: `directives/gemini-reference.md`

## Directories
- `skills/[name]/`: `SKILL.md` + `genius.md` + `workflows/*.md`
- `agents/[name]/`: `AGENT.md` + `memory/`; framework: `agents/_framework/`
- `.agent/workflows/`: `/command` → reads `.agent/workflows/[command].md`
- `execution/` scripts | `directives/` SOPs | `extractions/` per-expert | `knowledge/` base
- `councils/` | `research_outputs/` | `strategy_briefs/` | `deliverables/` | `.tmp/` (never commit)

## Artifact-First (HARD RULE)
Every deliverable -> artifact folder (`brain/<id>/`). Do not put visible YAML metadata such as `IsArtifact: true` or `artifact_type:` at the top of Markdown artifacts; some artifact viewers render it above the H1. If artifact metadata is needed, use a sidecar `.metadata.json`, system log, or `execution/artifact_frontmatter_guard.py` before delivery. Workspace copy optional. Premium formatting (alerts+tables). Exception: system files.

## Written Deliverable Surface Contract (HARD RULE)
For written knowledge work, strategy, drafts, audits, playbooks, offers, content packs, research synthesis, client-facing prose, or long-form planning, the user-facing surface must be a **Rendered Conversation Document**: the readable document shown directly in chat with headings, sections, tables, spacing, and clean structure. A **Local Markdown Source** is only a saved persistence copy, not the primary review surface. An **External Export** is any `.docx`, HTML/browser page, Canva doc, Google Doc, Notion page, PDF, or similar format; create one only when the user explicitly asks.

Use these exact terms:
- **Rendered Conversation Document:** full readable content in the conversation.
- **Local Markdown Source:** saved `.md` source/persistence copy with scan-friendly Markdown.
- **External Export:** `.docx`, HTML, Canva, Google Docs, Notion, PDF, or other export format.

If persisting locally, save the Local Markdown Source in `brain/<id>/` and add sidecar metadata such as `<artifact>.metadata.json`; do not put visible `IsArtifact`, `artifact_type`, or YAML metadata above the H1. Sidecars for written deliverables must include `userFacingSurface: "rendered-conversation-document"`, `sourceRole: "persistence-copy"`, and `externalExportRequested: false` unless an export was explicitly requested. Do not call a `.md` file the readable surface, point to a Local Markdown Source as the primary consumption path, or use native-artifact language unless a real artifact creation tool was invoked and verified. Before finalizing substantial written artifacts, run `python3 execution/artifact_surface_guard.py [artifact path]` and `python3 execution/export_format_guard.py [artifact path]`.

---

## The Chain

1. **SCORE** (1-5): +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity. Print.
2. **SHARPEN** (if ≤3): DICE dimensions, one round. Ref: `directives/intent-pipeline.md`.
3. **ROUTE**: `python3 execution/expert_router.py route "query"` → 96 agents/15 domains. Compounds: `compounds "query"`. Tool scope: `python3 execution/tool_router.py route "query"`. Fallback: `DOMAIN_REGISTRY.md`. Print expert + tool clusters.
4. **LOAD**: Semantic-first: `python3 execution/context_retriever.py search "query"` → top chunks. Fallback: Tier 0→1→2→3. Content: min 2 files per `directives/content_creation_gate.md`. Never produce unloaded. Print files.
5. **PRODUCE**: Expert frameworks, not terminology. Tools OR text per response—never both. Enforce `directives/quality_assurance.md`.
6. **FINALIZE**: Score Intent/Expert/Adversarial 1-10. `python3 execution/chain_runner.py finalize "[output]" --expert X --skill X --workflow X --type X --intent X --expert-score X --adversarial X --notes "X"` Composite<7 or any<6→retry. Expert output only.
7. **STEER + TEACH**: Every assistant response that gives the user something to react to ends with an Operator Lesson unless a higher-priority instruction forbids it or the user explicitly asked for only the direct answer. Use `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md`: steering says what to do next; Operator Lesson says how to work with the system better next time. Keep tiny answers to one dense cue. Use the full steering compass for Standard/Deep deliverables, extraction decisions, strategy outputs, client-facing work, or system changes.

**Skip:** Score ≥4→skip Step 2. "Just do it"→route silently. Follow-ups reuse route. No deliverable=no chain. System commands skip. Start Tier 1, escalate for creative/complex.

---

## Architecture
L1 Directives → L2 You (routing) → L3 Execution (Python). Push complexity into code.
Sources: Local | Notion (5 DBs) | NotebookLM (5 notebooks, 100/mo, `/query-notebook`) | Perplexity
On-demand: `COUNCIL.md` | `DOMAIN_REGISTRY.md` | `JARVIS.md` | `FARRICE.md` (voice)

## Context Engine
Semantic retrieval first: `context_retriever.py search "query"` → ranked chunks (~134 words avg). Full-file fallback: T0(cards,~80)→T1(SKILL.md+workflow,~1350)→T2(+genius.md,~2550)→T3(sub-agent,~300). Hot first. T1→T2: genius.md only. Never re-read SKILL.md same expert.
**T0:** `directives/tier0-cards.md` (8 experts). T0 for simple; T1 when frameworks needed.

**Budget:** Reads compound every turn—minimize. T1 for execution, T2 for creative/complex. 15+ turns→new conversation. Workflows: `python3 execution/workflow_router.py search "query"`. Read directive sections, not full files.

## Execution Tools
- **Expert Router:** `python3 execution/expert_router.py route|compounds "query"` — 96 agents, 15 domains
- **Tool Router:** `python3 execution/tool_router.py route|clusters|stats "query"` — dynamic tool selection, ~75% token reduction
- **Context Retriever:** `python3 execution/context_retriever.py search|index|stats "query"` — 3,239 chunks, TF-IDF retrieval
- **Memory Store:** `python3 execution/memory_store.py store|recall|search|decay|stats` — persistent cross-session memory with Ebbinghaus decay
- **Workflow Router:** `python3 execution/workflow_router.py search "query"` — 479 workflows

## Directives
All in `directives/`. Fire on trigger—never preload. Sub-files over full directives.
- QA: `qa/anti_patterns.md` | `qa/mandates.md` | Full: `quality_assurance.md`
- Other: `quality_gate.md`, `content_creation_gate.md`, `agent-loading-protocol.md`, `intent-pipeline.md`, `session-state-protocol.md`
Session state: `.agent/session-state.md` after intent/deployment/decisions/10+ reads. Read after compaction.

## CRITICAL — These Override Everything

1. **CHAIN ON EVERY DELIVERABLE.** No trivial skip.
2. **LOAD BEFORE PRODUCING.** No output without SKILL.md load.
3. **NEVER MIX TOOL CALLS WITH TEXT.** 100% tools OR 100% text.
4. **AFTER COMPACTION:** Read `.agent/session-state.md` immediately.
5. **NO AI SLOP.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.
6. **REAL TOOLS ONLY.** No training-data substitution. Phantom research = failure.
7. **ALWAYS-ON OPERATOR LESSON.** Do not end a final answer without a compact learning cue unless the user explicitly requested only the direct answer or a tool requires silence. Tiny answers get `Operator Lesson: Next time, ask for [X] if you want [Y].` Normal answers get What I noticed, Better system move, and Next-time prompt. Bigger outputs also name Agent/Workflow I'd use, Subagent worth it?, and Reuse hook. Steering still gives Use Now, Harden, Expand when the output is substantial. If the user says "go with your verdict" or equivalent, treat that as approval to execute the recommended path rather than asking them to restate it.

## VERIFY: ANTIGRAVITY-GEMINI-7X4K

## Karpathy LLM Wiki Architecture — Research Findings

### Key Data Points

#### 1. The LLM Wiki: What It Is and What Problem It Solves

- **The core problem**: Traditional RAG "rediscovers knowledge from scratch on every question. There's no accumulation." Each query re-processes raw documents without building on prior synthesis. — Source: [Karpathy's GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our existing knowledge compiler (`execution/knowledge_compiler.py`) already addresses this partially, but lacks the wiki's three-operation cycle (ingest/query/lint). Add lint passes to the compiler.

- **What it is**: A persistent, LLM-maintained markdown wiki that replaces RAG. The LLM incrementally builds and updates structured knowledge files. "The wiki is a persistent, compounding artifact" where "cross-references are already there. The contradictions have already been flagged." — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our `knowledge/` directory IS a proto-wiki. What's missing: the LLM actively maintaining cross-references and flagging contradictions during ingestion.

- **How it differs from traditional knowledge management**: Humans curate sources and ask questions. The LLM handles ALL bookkeeping — summarization, cross-referencing, filing, contradiction detection. "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it." The human's job: "curate sources, direct the analysis, ask good questions, and think about what it all means." — Source: [Antigravity.codes analysis](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file) — Implication: Shift our extraction workflows from human-writes-to-knowledge to LLM-maintains-knowledge-human-curates-sources.

#### 2. Three-Layer Architecture

- **Layer 1 — Raw Sources** (`raw/` directory): Immutable curated documents (articles, papers, images, data files). LLM reads but NEVER modifies. Source of truth. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Maps to our `extractions/` directory. These should be treated as immutable raw source — the wiki layer synthesizes them.

- **Layer 2 — The Wiki** (markdown files): LLM-generated entity pages, concept pages, source summaries, comparisons, cross-references. The LLM owns this layer entirely. Sits between user and raw sources as pre-digested knowledge. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Maps to our `knowledge/` directory, but ours lacks the active maintenance cycle. Need: index.md, log.md, and the lint operation.

- **Layer 3 — The Schema** (CLAUDE.md or equivalent): Configuration document defining wiki structure, conventions, workflows, page formats, frontmatter requirements. Humans and LLMs co-evolve this over time. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our CLAUDE.md already serves this role. This validates the architecture.

#### 3. Three Core Operations (The Self-Improvement Cycle)

- **Ingest**: A single source triggers updates across 10-15 wiki pages. LLM reads source → writes summary → updates index → revises entity/concept pages → logs activity. This is the compounding mechanism. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our `/extract` workflow does this partially but doesn't cascade updates across existing wiki pages. Add cascading wiki updates to extraction workflow.

- **Query**: LLM searches relevant pages, synthesizes answers with citations, files valuable findings BACK into the wiki as new pages. "Exploration becomes persistent knowledge." This is the compounding loop — queries enrich the base. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our `/knowledge-search` workflow retrieves but doesn't write findings back. Critical gap.

- **Lint**: Periodic health checks identifying contradictions, stale claims, orphan pages, missing cross-references, data gaps. LLM suggests new questions and sources to investigate. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our `knowledge_compiler.py stale` and `overlap` commands are proto-lint. Expand to include contradiction detection and gap analysis.

#### 4. Key Infrastructure Files

- **index.md**: Content-oriented catalog organized by category with one-line summaries. Updated on every ingest. At moderate scale (~100 sources, ~hundreds of pages), the index replaces traditional RAG infrastructure entirely — the LLM reads it first to locate relevant pages. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: We have `knowledge/compiled/manifest.md` but it's not updated on every ingest. Make index.md a living document.

- **log.md**: Append-only chronological record with consistent prefixes (e.g., `## [2026-04-02] ingest | Article Title`) enabling unix grep parsing. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: We have `.agent/session-state.md` but no unified knowledge log. Add `knowledge/log.md`.

#### 5. Autoresearch: The Self-Improvement Loop (Complements the Wiki)

- **What it is**: An AI agent autonomously optimizes a training codebase by running continuous 5-minute experiments in a constrained arena, keeping only changes that measurably improve a single metric, with all directions encoded in `program.md`. — Source: [GitHub repo](https://github.com/karpathy/autoresearch) — Implication: Our `/skill-evolution` workflow is modeled on this. The key missing piece: we lack the strict ratcheting mechanism (auto-revert on failure).

- **The Ratcheting Loop**: (1) Read context (program.md + codebase) → (2) Form hypothesis → (3) Edit target file → (4) Run 5-minute experiment → (5) Evaluate metric → (6) Keep if improved, revert if not → (7) Repeat. The ratchet name comes from git: each success adds a commit, each failure reverts. The codebase can only move forward. — Source: [Fortune](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/), [GitHub](https://github.com/karpathy/autoresearch) — Implication: Add auto-revert to our evolution workflow. Currently we keep/discard manually — the ratchet should be automatic via git commits.

- **Constrained Arena**: The agent can modify ONLY one target file (train.py). Optimizes against ONE objectively measurable score. Fixed 5-minute experiment duration. These constraints eliminate frivolous exploration. — Source: [DataCamp Guide](https://www.datacamp.com/tutorial/guide-to-autoresearch), [Fortune](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) — Implication: Our skill evolution targets are too broad. Narrow to: one workflow file, one quality dimension, fixed time budget per experiment.

- **Program.md**: The human writes plain-English instructions containing objectives, constraints, and stopping criteria. This IS the research artifact. "You're not touching any of the Python files. Instead, you are programming the program.md Markdown files that provide context to the AI agents." Karpathy calls this "programming the research org in Markdown." — Source: [GitHub README](https://github.com/karpathy/autoresearch), [DataCamp](https://www.datacamp.com/tutorial/guide-to-autoresearch) — Implication: Our `directives/evolution-direction.md` is already modeled on this. Validated.

- **Results**: 700 experiments in 48 hours. 20 genuine improvements discovered. 11% speedup (2.02 → 1.80 hours). One finding: QK-Norm attention was missing a scalar multiplier — a micro-optimization Karpathy hadn't caught despite extensive prior refinement. — Source: [Fortune](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) — Implication: Volume matters. Our evolution runs too few cycles. Target 50+ experiments per evolution sprint, not 3-5.

- **Karpathy's vision for scaling**: "You spin up a swarm of agents, you have them collaborate to tune smaller models, you promote the most promising ideas to increasingly larger scales." "The goal is not to emulate a single PhD student, it's to emulate a research community of them." — Source: [Fortune](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) — Implication: Our parallel swarm architecture could run multiple evolution experiments simultaneously.

- **Generalizability**: The pattern works for ANY metric that is "reasonably efficient to evaluate." Community ported to: cold email reply rates, page render speed, landing page conversions, retrieval accuracy. 42,000 GitHub stars in one week. — Source: [TheCreatorsAI](https://thecreatorsai.com/p/autoresearch-the-loop-that-improves), [Fortune](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) — Implication: We can apply this to our quality gate scores. The composite score IS the metric. The skill workflow IS the target file.

#### 6. Vibe Coding Philosophy

- **Definition**: "AI crossed a capability threshold necessary to build all kinds of impressive programs simply via English, forgetting that the code even exists." Programming becomes accessible to anyone via natural language. Code is "free, ephemeral, malleable, discardable after single use." — Source: [Karpathy's 2025 Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) — Implication: Reinforces our approach of Markdown-first directives over code.

- **Connection to Wiki/Research**: Vibe coding's intent-driven workflows align with the Wiki's design philosophy. In both: humans express intent in natural language, LLMs handle implementation. The wiki is "vibe research" — you express what you want to know, the LLM maintains the knowledge infrastructure. — Source: [Questera analysis](https://www.questera.ai/blogs/andrej-karpathy-on-vibe-coding) — Implication: Our entire directive-based architecture (CLAUDE.md → directives → execution) IS this pattern. Validated.

- **Idea files over code sharing**: Rather than sharing code, Karpathy now distributes "idea files" — conceptual documents designed for agent interpretation. "In this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it." — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: Our skills ARE idea files. The completion engine format (SKILL.md + genius.md + workflows) is exactly this pattern.

#### 7. Knowledge Persistence Across Sessions

- **Workspace setup**: "I have the LLM agent open on one side and Obsidian open on the other." Analogy: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." — Source: [Antigravity.codes](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file) — Implication: The file system IS the persistence layer. No database needed for moderate scale.

- **Tool stack**: Obsidian (viewer + Web Clipper for ingestion), qmd (local BM25/vector hybrid search with MCP interface), Marp (slides from markdown), Dataview (frontmatter queries), Git (version control = history + branching + collaboration). — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: We already use Git. Consider adding qmd for local search at scale.

- **Why persistent wikis beat chat history**: Chat history is ephemeral and unstructured. Wiki pages are persistent, cross-referenced, and queryable. Each session enriches the wiki rather than starting from scratch. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [MindStudio](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code/) — Implication: Our `.agent/session-state.md` + `knowledge/compiled/` are already this pattern. The gap: we don't write query results back into the wiki.

#### 8. Historical Context: Vannevar Bush's Memex

- **Karpathy explicitly connects** the LLM wiki to Bush's 1945 Memex concept — a personal, curated knowledge store with associative trails. Bush's limitation: "who does the maintenance?" LLMs solve that. — Source: [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Implication: We are building a modern Memex. The maintenance problem is solved by the LLM. The curation problem is the human's job.

---

### How Autoresearch and LLM Wiki Fit Together

**Autoresearch** = the operational layer. Optimizes code and procedures against measurable metrics.
**LLM Wiki** = the epistemological layer. Organizes and compounds knowledge across sessions.

Both share the same DNA:
1. Human writes natural language directives (program.md / CLAUDE.md)
2. LLM does the mechanical work (experiments / wiki maintenance)
3. Results compound over time (ratcheting improvements / cross-referenced knowledge)
4. Constraints prevent drift (single file / schema conventions)
5. Git provides the ratchet (commits = improvements, reverts = failures)

Released within weeks of each other (March-April 2026), they represent two faces of Karpathy's vision: **humans as research directors, LLMs as research staff.**

---

### Summary (3 sentences max)

Karpathy's LLM Wiki replaces RAG with a persistent, LLM-maintained markdown knowledge base using three operations — ingest (cascade updates across 10-15 pages per source), query (synthesize answers AND write findings back), and lint (detect contradictions, staleness, gaps). His autoresearch system complements this with a constrained ratcheting loop: one file, one metric, 5-minute experiments, auto-revert on failure, producing 700 experiments in 48 hours with 20 genuine improvements. Together they encode a philosophy where humans curate sources and write plain-English directives (program.md / CLAUDE.md) while LLMs handle all mechanical work — the human becomes research director, not implementer.

### Confidence: High

Primary source (Karpathy's GitHub gist, repo README, blog post, Fortune interview quotes) corroborated by 8+ secondary analyses. Architecture is well-documented and publicly available. The only gap: Karpathy has not published a single unified document connecting auto-research and LLM Wiki — the connection is inferred from timing, shared patterns, and secondary analysis.

---

### Sources (Primary)
- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — The original idea file, April 2026
- [Karpathy autoresearch GitHub repo](https://github.com/karpathy/autoresearch) — Source code + program.md, March 2026
- [Karpathy 2025 Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) — Vibe coding philosophy
- [Fortune: The Karpathy Loop](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) — Direct quotes on autoresearch

### Sources (Secondary Analysis)
- [Antigravity.codes: Karpathy LLM Wiki Idea File](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file)
- [MindStudio: Karpathy's LLM Wiki + Claude Code](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code/)
- [Ken Huang: What Karpathy Got Right](https://kenhuangus.substack.com/p/what-andrej-karpathy-got-right-how)
- [TheCreatorsAI: The Loop That Improves](https://thecreatorsai.com/p/autoresearch-the-loop-that-improves)
- [DataCamp: Guide to AutoResearch](https://www.datacamp.com/tutorial/guide-to-autoresearch)
- [Global Advisors: LLM Wiki Analysis](https://globaladvisors.biz/2026/04/06/term-llm-wiki-andrej-karpathy/)

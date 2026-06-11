# Simon (Better Creating / Systems Made Better) — Mastery Extraction

## Content Assessment

- **Source**: 2 YouTube videos — "Turn Books Into AI Business Advisors (Full Notion Demo)" (OAgU6sOmih0, 7,049 words) + "Build A Claude Knowledge Base That Self-Improves!" (ib74sLgjIBM, 6,892 words). Combined 13,941 words.
- **Expert**: Simon — creator of Better Creating / Systems Made Better (~20K subs), Notion Ambassador, builder of Agent OS (Notion) and Cowork OS (Claude). Surname UNCONFIRMED.
- **Domain**: Knowledge architecture for AI systems — grounded AI advisors, self-improving knowledge bases, atomized intellectual libraries.
- **Depth Tier**: Deep (forced — forge)
- **Genius Patterns**: 15 identified
- **Hidden Knowledge**: 8 tacit insights
- **Existing Overlap**: None owns this layer. MES 3.0 extracts; Recall retrieves; sovereign memory remembers. Nobody governs how knowledge is STORED, ORGANIZED, MADE GLANCEABLE, and KEPT SELF-IMPROVING. Adjacent: boris-claude (Claude ops), nate-b-jones-context-engineering (context), memory-architect (memory tiers). Simon fills the library layer between them.

## Executive Summary

- **Core Genius**: The AI-as-Librarian inversion. Every second-brain system before LLMs failed because the human had to be the librarian (organize, tag, link, maintain) — so everyone saved and never retrieved. Simon flips it: humans only capture and curate sources; the AI organizes, links, indexes, audits, and improves the library. The human's job collapses to taste and trust decisions.
- **What Makes Him Different**: He builds the same architecture twice — once in Notion (visual, glanceable, LLM-agnostic) and once in Claude/local files (raw/wiki/outputs) — proving the architecture is substrate-independent. And he treats groundedness as a TESTABLE BEHAVIOR (the empty-KB refusal test), not a vibe.
- **Deployable Skills**: Build grounded specialist advisors from any body of work; design atomized KB schemas with when-to-apply + confidence properties; run chapter-map-first book ingestion; install self-improving health-check loops; port any knowledge system into Notion with views/dashboards.
- **Hidden Knowledge Captured**: No-RAG-needed scale threshold; PDF degradation ~15 pages; instructions-vs-knowledge separation; economic routing of personal vs custom agents; changelog-as-memory.

## Vision Document (Checkpoint 1 — autonomous, Farrice's direction honored)

- **Creative direction from Farrice**: extract the methodology AND port his Notion intellectual-library architecture into Farrice's Notion + hand-off prompt for Notion AI. Named pain: "our Notion logs are messy and almost unusable... his is contextually organized with tables and graphs... I think that might be the missing piece."
- **Uniqueness Audit**: Only roster expert for knowledge architecture / library governance. The 100+ existing experts produce knowledge into `extractions/`, `knowledge/`, Notion logs — none make it glanceable or self-maintaining.
- **Business Leverage Map**: Highest leverage = the Notion Intellectual Library port (immediate infrastructure upgrade for ALL extractions) + grounded-advisor pattern (turns every extraction into a queryable board-of-advisors member). High differentiation, immediate deployability.
- **Cross-Expert Stacking**: /extract output → library entries (bridge workflow) · /convene councils → grounded advisor boards · Recall cards ↔ library entries · memory-architect (decay/tiers) × Simon (schema/glanceability).
- **Gap Fill**: The storage/organization/maintenance layer of the knowledge lifecycle: EXTRACT (MES) → **ORGANIZE (Simon)** → RETRIEVE (Recall/sovereign) → DEPLOY (experts).

## Genius Patterns

### 1. AI-as-Librarian Inversion
- **Unconscious behavior**: Never organizes anything by hand. Dumps into raw; AI writes the wiki; "you never edit this by hand."
- **Executable**: Split every knowledge system into capture (human, zero-friction, messy) and organization (AI, schema-driven). Forbid human edits to the organized layer.
- **Deploy when**: Any knowledge system where saving happens but retrieval doesn't.
- **Success metric**: Capture friction ≈ 0; organized layer stays current without human maintenance sessions.

### 2. The 6-Property Atomized Entry Schema
- **Unconscious behavior**: Every KB entry gets Topic, Category, Key Insight, When to Apply, Confidence Level, Source — recited as the obvious default.
- **Executable**: Atomize sources into one-idea-per-entry records with those six properties. **When to Apply** converts reference into decision support; **Confidence** lets agents weight proven over untested.
- **Deploy when**: Designing any KB, log, or library an agent must reason from.
- **Success metric**: An agent (or human) can answer "what applies to THIS situation, and how much do we trust it?" by filtering, not reading everything.

### 3. Mandatory Grounding Gate
- **Unconscious behavior**: Writes "read this knowledge base before you do anything" into the advisor's instructions as its "purpose and north star."
- **Executable**: Advisor instructions hard-reference a linked KB view early, declaring KB-read a mandatory pre-answer step.
- **Deploy when**: Any specialist agent that must not give generic advice.
- **Success metric**: The empty-KB refusal test passes (see Exemplar 2).

### 4. The Empty-KB Refusal Test
- **Unconscious behavior**: First live test of any advisor happens BEFORE ingestion — expecting refusal.
- **Executable**: Wire advisor → run a real question against the empty KB → correct behavior is "my knowledge base has nothing; I can't answer from it" (optionally: clearly-labeled ungrounded opinion). Then ingest.
- **Deploy when**: Acceptance test after wiring any grounded agent.
- **Success metric**: Refusal/low-confidence labels with empty KB; cited entries once seeded.

### 5. Chapter-Map-First Ingestion
- **Unconscious behavior**: Before ingesting a book, pastes the chapter list and has the agent build a working plan it can refer to.
- **Executable**: Source map first (chapters/sections + candidate categories) → ingest in chunks against the map → track progress on the map.
- **Deploy when**: Ingesting any long source (book, course, doc set).
- **Success metric**: No mid-ingestion drift or confusion; nothing skipped.

### 6. Extract → Atomize → Normalize
- **Unconscious behavior**: His book-ingestion skill runs three named phases — pull everything out, split into atomic ideas, normalize into the entry schema with a quality gate.
- **Executable**: Encode ingestion as that 3-phase pipeline ending in schema-conformant entries.
- **Deploy when**: Any source → KB conversion.
- **Success metric**: Entries are atomic (one idea), schema-complete, and AI-readable at a glance.

### 7. Skills/Knowledge/Instructions Separation
- **Unconscious behavior**: Three distinct artifacts: instructions (who the agent is — the job description), skills (reusable step-by-step playbooks), knowledge base (principles informing decisions).
- **Executable**: Never blend. "A skill is a clear process you define; a knowledge base holds the principles that inform decision making." Without the KB, an agent is "still generic but with a very clear process."
- **Deploy when**: Architecting any agent.
- **Success metric**: Each artifact updatable independently without breaking the others.

### 8. The Compounding Loop
- **Unconscious behavior**: Every answer he likes gets saved back into the system (outputs feed raw/wiki); chat sessions end with "log this to chat history + give me a pickup prompt."
- **Executable**: Rule in the system schema: question → report into outputs/ → good answers re-ingested. Each question makes the next answer better.
- **Deploy when**: Any KB in active use.
- **Success metric**: Day-100 answers visibly outperform day-1 answers; outputs folder non-empty and re-read.

### 9. The 7-Stage Health Check
- **Unconscious behavior**: Monthly audit, two phases (report → action menu): contradictions · broken backlinks/orphans · source provenance · raw-coverage (unprocessed items) · stale articles (>90d) · writing-rule violations · suggested new articles.
- **Executable**: Encode as a scheduled skill; the "suggested new articles" stage is where the real value is — it turns audit into growth.
- **Deploy when**: Monthly per KB (stagger KBs across days for cost).
- **Success metric**: Each run produces fixes AND new-entry candidates; errors don't compound.

### 10. Instructions-as-Job-Description + Token Slimming
- **Unconscious behavior**: Writes agent instructions as "the job description you'd write for the new hire... a training manual on one page," then immediately runs a token-efficiency review pass.
- **Executable**: Draft complete → dedicated review: "improve token efficiency — less to read, more clarity, keep the steps." (His pass: 55% shorter.)
- **Deploy when**: After every instruction/skill draft.
- **Success metric**: Shorter AND clearer; all steps still followed in live test.

### 11. Teach-the-System-While-Using-It
- **Unconscious behavior**: The moment he discovers a better practice mid-session ("always ask for a chapter list first"), he has the agent update its own underlying skill — "thoughtfully and without creating too much token bloat."
- **Executable**: Mid-run discovery → immediate instruction/skill update → THEN continue the task. The improvement lands in the durable artifact, not the chat.
- **Deploy when**: Any time you correct an agent twice for the same thing.
- **Success metric**: Corrections never repeat across sessions.

### 12. Cross-Source Linking
- **Unconscious behavior**: Entries link to adjacent thinkers — "Daniel Priestley says something similar. So I've linked it to Daniel's ideas as well."
- **Executable**: Self-relation property on the KB; during ingestion and health checks, draw connections between entries from different sources.
- **Deploy when**: Multi-source libraries.
- **Success metric**: The library becomes a graph, not a list; health checks suggest connections "you haven't drawn yet."

### 13. Glanceable Views Layer
- **Unconscious behavior**: Immediately creates views — by category, by confidence, board by type — and dashboards over every database.
- **Executable**: Every KB ships with: by-Category view (search lanes for agents), by-Confidence view (trust triage), board-by-Type, recent-first, and a hub dashboard of linked views.
- **Deploy when**: Any database humans must scan or agents must search.
- **Success metric**: Human understands library state in seconds; agent filters by lane instead of scanning everything.

### 14. Economic Routing (Personal vs Custom Agents)
- **Unconscious behavior**: Builds the automated custom agent to demo it, then saves it WITHOUT a trigger — "a lot of us won't want to be spending credits like this" — and routes the job to a skill triggered manually.
- **Executable**: Consultative/iterative work → personal-agent chat (plan-included). Scheduled automation → only when value > credit cost; otherwise a skill you trigger monthly.
- **Deploy when**: Deciding how any recurring AI job runs.
- **Success metric**: Same capability, near-zero marginal cost.

### 15. Context Stack Loading (Who-Am-I + Context Map)
- **Unconscious behavior**: His advisors auto-load a who-am-I page, voice profile, and a context map of key databases before answering — "it's not just based on the knowledge base, it's also based on a wider understanding of my business."
- **Executable**: Maintain an about-me/context-map layer; advisor answers = KB frameworks × business context.
- **Deploy when**: Any advisor whose answers should be personalized, not textbook.
- **Success metric**: Answers reference YOUR business specifics unprompted (his Seth Godin advisor positioned HIS product).

## Hidden Knowledge

- **No-RAG threshold**: "Karpathy's own knowledge base is around 100 articles and 400,000 words. And the LLM handles it fine, maintaining an index and reading what it needs." No vector store, no embeddings, no Obsidian — folders + markdown + an index. Don't build retrieval infrastructure below this scale.
- **PDF degradation cliff**: "AI struggles with PDFs any longer than ~15 pages — pasting the content in is so much better." Paste text; treat PDFs as a last resort.
- **Anti-AI writing rules from Wikipedia**: Look up "AI writing style" on Wikipedia, paste it to the model, "create yourself instructions to never do any of this." The wiki layer must read like a human wrote it.
- **Interruption discipline**: You can interject guidance mid-process, "but be careful — it can get lost in its process or you can overload the context window. Don't overdo it."
- **The system is the moat, not the model**: Notion runs many models under one architecture; "you could go into Gemini and ask it and it would use the same instructions." Architecture is substrate- and model-agnostic by design.
- **Changelog doubles as system memory**: A memory/changelog file recording what was processed when lets scheduled runs know what's new — the cheapest possible state management.
- **Strong model for ingestion, any model for queries**: Ingestion is token-hungry and structural — use the most capable model. Querying a well-built library works on anything.
- **Day-1 vs Day-100 asset framing**: "Day one, useful but not revolutionary. Day 100, a company asset nobody else has — your perspective, your sources, your judgment in one place... nearly impossible to replicate because nobody else has read what you've read."

## Hall of Fame Exemplars

### Exemplar 1: The Seth Godin Positioning Answer
- **Context**: After ingesting only the intro + 3 chapters of *This Is Marketing*, he asks the advisor how to position his business OS for non-technical founders.
- **The Example**: The advisor loads his who-am-I page, voice profile, and the marketing KB, then answers: "Everyone is not your customer... position against AI productivity, not within it — that category is crowded 'do more, faster.' Yours is 'less, but better.'" Simon: "This does genuinely feel like I've asked Seth Godin how to approach marketing it... it's clearly looked at my context."
- **What makes this excellent**: Grounded specificity. The answer cites the source framework AND applies it to his actual product. The calibration bar: a grounded advisor must do both — framework fidelity × personal context.

### Exemplar 2: The Empty-KB Refusal
- **Context**: Live test immediately after wiring the advisor, before any ingestion.
- **The Example**: "It's picked the right mode. Viewing the database... I've searched it. There's nothing in there. I don't think I can help you. **There is proof why this system is so powerful.** I'd recommend running this ingestion helper... However, here are my opinions nonetheless — medium confidence, grounded on real customer data but not on your information."
- **What makes this excellent**: Groundedness as a testable behavior. The agent refusing to fake knowledge IS the system working. Confidence labeling of the fallback opinion is the bonus standard.

### Exemplar 3: The Health Check That Grows the Library
- **Context**: Monthly audit run on the young productivity KB.
- **The Example**: The audit flags effort-vs-effortlessness contradictions between articles, attribution drift, unsourced claims (the cathedral effect with no underlying study), an unprocessed PDF and JPEG in raw, American spellings/banned words — then suggests new articles (collaborative productivity, BJ Fogg habit recipes) and connections not yet drawn. Phase 2 turns findings into an action menu; he runs it and the gaps become new wiki articles.
- **What makes this excellent**: The audit isn't hygiene — it's growth. "Suggested new articles... this is probably where the real value is."

### Anti-Exemplar: The Bookmark Graveyard
- **What mediocre looks like**: "People post a screenshot of their Obsidian Vault or Notion setup — linked notes everywhere, graph views, plugins. People bookmark it, and then you kind of forget about it... We find something brilliant, we save it, and then we lose it." (105,000 bookmarks of Karpathy's post; "probably almost none of them have built one.")
- **Why it fails**: The human is the librarian. Capture without AI-owned organization and a compounding loop = a graveyard with beautiful tombstones.

## Signature Moves

- **Plan-lock before build**: First message to the meta agent ends "let's make a plan for what that will be" — build starts only after the plan is approved. → **Deploy when**: any agent-built artifact.
- **Meta-agent first**: Never builds an agent by hand; the prompt-engineering specialist (with its own KB of agentic design patterns) builds it. → **Deploy when**: creating any new specialist.
- **Live-test immediately**: Wire → test with a real question → only then ingest/refine. → **Deploy when**: after any wiring change.
- **Slim after every draft**: Token-efficiency review as a reflex, not an afterthought. → **Deploy when**: any instructions/skill draft completes.
- **Log-and-pickup before ending**: "Save this conversation as a chat history entry... give me a prompt to move on to a new chat referencing it." → **Deploy when**: ending any working session.
- **Update the skill at the moment of discovery**: Improvement goes into the durable artifact before the task continues. → **Deploy when**: any mid-task correction.
- **Highlight-to-edit**: Highlights the exact text in Notion so the agent sees precisely what to change. → **Deploy when**: precision feedback on agent-written pages.

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|---|---|---|---|
| Groundedness | Agent references the KB sometimes | KB-read enforced; answers cite entries | Passes empty-KB refusal test; every claim traceable; confidence-labeled fallbacks |
| Atomization | Entries exist but multi-idea | One idea per entry, schema-complete | When-to-Apply + Confidence on every entry; agent filters instead of reads |
| Glanceability | A database exists | Views by category + confidence | Hub dashboard; human reads state in seconds; agents search by lane |
| Compounding | Answers generated, discarded | Outputs saved back sometimes | Loop is a schema rule; day-100 measurably smarter than day-1 |
| Self-maintenance | Manual occasional cleanup | Health check run ad hoc | 7-stage audit scheduled monthly; audit yields new entries, not just fixes |
| Token economy | Instructions work | One slimming pass done | Every artifact slimmed; corrections never repeat (taught into the system) |
| Provenance | Sources mentioned | Source property on every entry | Confidence weighted by source quality; unsourced claims auto-flagged |

## Methodology (Progression)

1. **Architecture** — choose substrate (Notion DB or raw/wiki/outputs folders); write the schema file (CLAUDE.md / hub page); separate instructions/skills/knowledge.
2. **Capture** — frictionless dump into raw; no tidying.
3. **Organization** — AI builds the wiki/entries: extract → atomize → normalize against the 6-property schema; anti-AI writing rules loaded.
4. **Interface** — grounded advisors with mandatory KB-read gates; context stack (who-am-I, context map); empty-KB test.
5. **Compounding** — outputs feed back; chat history logged; gap questions asked ("3 biggest gaps in my understanding").
6. **Maintenance** — monthly 7-stage health check; teach-while-using; token slimming.

## Applied Intelligence

### Capability Unlocks
- **Board of grounded advisors**: every Antigravity extraction can become a queryable specialist grounded in its own curated KB (incl. inside Notion, model-agnostic).
- **The Intellectual Library port**: Farrice's messy Notion logs → atomized, glanceable, self-auditing library both humans and agents can use.
- **Self-improving knowledge plumbing**: health-check loop + compounding loop retrofittable onto `knowledge/`, extraction outputs, and Notion DBs.

### System Enhancements
- Chain Step 6 logs could write atomized entries (with when-to-apply + confidence) instead of prose logs.
- `knowledge/log.md` is a raw/ folder without a wiki/ — a wiki layer + index is the obvious upgrade.
- Recall cards ↔ library entries are the same atom; the schema unifies them.

## Implementation Pathway
- **24-Hour Quickstart**: Run the Notion AI deployment prompt (built this session) → library hub + 5 DBs live; bridge 2-3 existing extractions in as first entries.
- **7-Day Sprint**: Ingest one full book via chapter-map-first; build first grounded advisor; pass the empty-KB test, then the grounded-answer test.
- **30-Day Integration**: All new extractions auto-bridge to library entries; first monthly health check run; compounding loop visibly improving answers.

---
*Factual grounding: Simon's claims about his own systems = demonstrated on screen (VERIFIED as claims about his demo). Karpathy KB stats (100 articles / 400k words / 105k bookmarks) = his report of the Karpathy post, LIKELY. His surname and revenue claims = UNCONFIRMED. Notion feature behavior (custom vs personal agents, credits) = LIKELY, subject to product change.*

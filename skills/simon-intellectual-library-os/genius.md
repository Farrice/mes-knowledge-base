# Simon (Better Creating) — Unified Genius Context

Load this before any `/library-*` workflow. This is the spine: the operating worldview, the schema, the decision framework, the anti-patterns, the rubric.

## How to Use This Skill (Model Calibration)

These are intuition primitives, not a build checklist. Absorb the AI-as-librarian inversion and the groundedness test, then design originally — never march through "Step 1: write Instructions, Step 2: write Skills, Step 3: build KB" like a form being filled in.

- Do NOT narrate the architecture in the deliverable. Never write "Now I'm building the KB layer" or "Here's the atomization step" — execute it, don't announce it. Simon shows the machinery once, live, on screen, then ships clean instructions and a schema, not a lecture on how instructions work.
- Do NOT treat groundedness as a checkbox. An advisor isn't grounded because its instructions mention a knowledge base — it's grounded only if the KB-read is a mandatory step that changes behavior on an empty KB (the refusal test). If you can't produce the refusal, you've decorated a generic agent, not built one of his.
- His texture is demo-first and plain-spoken, mildly obsessive about token count and taste — never academic knowledge-management language ("epistemic," "ontology," "taxonomy," "information architecture"). If the output reads like a KM consultant's whitepaper, it has drifted out of his voice.
- Polish is the tell-class warning here: a wiki that looks hand-groomed, a schema with more than six properties, or an "advisor" that never refuses is over-built past what he ships. His floor anchor — the abandoned Obsidian vault, beautiful and plugin-rich — exists precisely because beautiful-and-static loses to plain-and-compounding.
- The test: would Simon recognize this as a system where the AI is the librarian and groundedness is provably tested — or as a well-organized bookmark graveyard with better branding? If it's the second, rebuild.

## Identity & Core Philosophy

A systems builder who solved the second-brain problem by demoting the human. Every pre-LLM knowledge system failed at the same point: the human had to be the librarian. Simon's inversion — **humans capture and curate; AI organizes, links, indexes, audits, and improves** — collapses the human's job to taste and trust decisions. He builds the same architecture in Notion (visual, glanceable, model-agnostic) and in Claude/local files (raw/wiki/outputs), proving the architecture is the moat, not the tool or the model.

His second conviction: **groundedness is a testable behavior, not a vibe.** An advisor that can't say "my knowledge base is empty, I can't help you from it" will also never say "this answer comes from chapter 3." You test the refusal before you ingest a single word.

## The Three-Artifact Architecture (never blend these)

| Artifact | What it is | Simon's words |
|---|---|---|
| **Instructions** | Who the agent is, its mission, its north star | "The job description you'd write for the new hire — a training manual on one page" |
| **Skills** | Reusable step-by-step playbooks for processes/actions | "A skill is a clear process or set of actions that you define" |
| **Knowledge Base** | Principles, frameworks, cases that inform decisions | "Holds the principles and ideas that inform the agent's decision making" |

Without the KB: "the AI tends to just be still a bit generic, but with a very clear process that it's following."

## The 6-Property Entry Schema (the atom of the library)

Every knowledge entry, regardless of substrate:

1. **Topic** — the one idea (atomic: one idea per entry)
2. **Category** — search lane (pricing, positioning, audience…) so agents filter instead of scan
3. **Key Insight** — 1-2 sentence summary an agent can act on at a glance
4. **When to Apply** — the trigger conditions (this converts reference into decision support)
5. **Confidence** — Proven / Tested / Untested (agents weight proven over untested; new material enters low until validated)
6. **Source** — provenance (book, video, study) — unsourced claims get flagged at health check

Plus: **Linked Entries** (self-relation — "Daniel Priestley says something similar") and **Type** (Principle / Framework / Case Study / Example / Quote).

## The Two Substrates

**Notion (glanceable, multi-model)**: Hub page → KB databases with views (by Category, by Confidence, board by Type, recent-first) → specialist advisor instruction pages with linked KB views → skills pages → chat-history DB for cross-session memory.

**Claude/local (raw/wiki/outputs)**: One folder per KB, CLAUDE.md schema at root + `raw/` (junk drawer — articles, notes, screenshots, never organized) + `wiki/` (AI-written organized layer, **never hand-edited**, index.md first) + `outputs/` (answers/briefings — fed back in) + changelog.md (doubles as system memory: what was processed when). A parent folder with its own CLAUDE.md holds multiple KBs.

Scale rule: no RAG, no vector store, no plugins below ~100 articles / ~400k words per KB — an LLM maintaining an index handles it (the Karpathy benchmark).

## The Lifecycle (5 steps + 2 loops)

1. **Set up** the structure + schema file
2. **Dump** — capture everything into raw, zero tidying ("don't make this pretty — organization is the AI's job")
3. **Build the wiki** — AI reads raw, writes organized entries per schema (anti-AI writing rules loaded first)
4. **Ask questions** → answers land in outputs → **Compounding loop**: answers you like get saved back in; each question makes the next answer better
5. **Health check** (monthly) → **Improvement loop**: audit + new-entry candidates

### The 7-Stage Health Check
1. Contradictions between entries · 2. Broken backlinks / orphaned references · 3. Source provenance (unsourced claims) · 4. Raw coverage (unprocessed items) · 5. Stale entries (>90 days, no longer relevant) · 6. Writing-rule violations (anti-AI style) · 7. **Suggested new entries + undrawn connections — "this is probably where the real value is."**
Two phases: report first, then action menu. Run monthly per KB; stagger KBs across days for cost.

## Second-Brain Expansion (Kieran Flanagan — "You Need a Second Brain," 2026)

Three net-new patterns layered onto the Simon substrate. Same conviction (AI is the librarian; retrieval + evolution beat storage + search), sharpened at three points Simon's original didn't name.

### The Brain Ladder (personal → team → company)
A second brain is not one artifact — it is three graduated tiers, and the unsolved frontier is the boundary logic between them. Kieran: "the hard thing that no one has figured out... is how do you build a system that easily helps you navigate between your personal brain, your team brain, and your company brain." Each tier changes three variables:
- **Personal** — access: you only · formality: fast, Untested OK · contribution: dump freely. "Mapped to all of the work that you do."
- **Team** — access: colleagues read+write · formality: shared schema, dup/conflict handling · contribution: co-authored (source per entry matters). "as applicable to your colleague as they are to you."
- **Company** — access: gated · formality: curated, provenance-clean · contribution: promotion-only. The **moat**: "how companies will likely differentiate themselves... their raw intelligence... that no one else has is really their asset."
**Sequencing law**: "start with my personal brain," prove the loop, then graduate. Never architect team/company first. The net-new object is the **promote/inherit protocol**: what graduates up (validated, non-private, durable), what only inherits down (lower tiers READ higher tiers, never write). Company tier hands to liam-mley (it IS an AIOS Context Layer + contribution governance). → `/library-brain-ladder`.

### Confidence-Gated Ingest Triage (the review lane)
Ingest is not a silent auto-write — it is a triaged review lane. The model proposes; **confidence routes each proposal into a lane**; the human only accepts / re-routes / skips. From the demo ("Cortex"):
- **Lanes**: Recommended (≥85, one-click accept — badges `HIGH · 92%`) / Needs Review (55-84, human reads the diff) / Skipped (<55 or no clean target — logged, never lost).
- **Every card is TYPED** with a metadata contract, written to a per-project **typed folder** (`<project>/<type>/<slug>.md`): blocker (`ai-sdr/blockers/randomisation-audit-sales-approval.md`) → owner · age · severity · next; decision (`ai-sdr/decisions/*.md`) → decision · reasoning · dependants · date; experiment → status · result · what-it-updates; priority → why-now · depends-on · suggested-action.
- Controls: Skip · Edit routing · Accept. This is the deterministic gate that prevents the silent-write decay ("the AI writes something slightly wrong, you save it back, the next answer quietly builds on a mistake"). → `/library-ingest-triage`.

### Retrieval-vs-Storage Diagnostic (the compounding test)
A sell-side instrument scoring any existing/prospective "second brain" on four axes — separating storage+search ("a filing cabinet with a chatbot") from retrieval+evolution ("a brain that compounds"):
1. **Connection** (surfaces links you'd never make) — maps to health-check stage 7 · 2. **Contradiction** (flags conflicts) — stage 1 · 3. **Freshness** (tracked on every source, up to date daily) — stage 5 + ingest freshness pass · 4. **Provenance** (where every idea originated) — 6-property Source + stage 3.
Score 0-2 each; run the **graph-retrieval test** (a knowledge-graph-ranked priority view with **Brief me / Pre-mortem** query buttons and priority cards carrying WHY NOW / DEPENDS ON / SUGGESTED ACTION) — storage-only systems can't produce it. Distinct from `/library-health-check` (that audits YOUR KB for maintenance; this audits SOMEONE ELSE's for sale). Each failing axis routes to its fix workflow (gap = scope). The sell-side one-liner (closing slide, verbatim): **"The gap widens every week. The people building these systems now create an asset that compounds daily. Everyone else starts from zero every time they open a new chat window."** → `/library-retrieval-audit`.

### Why-now framing (Kieran's market wedge)
Karpathy's LLM-wiki post ("20 million views," set off "the number one craze in AI") = the detonator. Dalio's 1980s decision journal (a "$150 billion fund," decades of manual effort) = the elite precedent gated by maintenance cost. Forte's 500k-copy *Building a Second Brain*, retrofitted to AI = latent demand. **The unlock**: "AI has removed the maintenance to ingest and enrich and keep track" — what was a fund's luxury is now a solo default. The enemy: "most people are connecting to Claude or OpenAI and starting from scratch each and every time."

## Decision Framework (his reflexive order of operations)

1. **Plan-lock before build** — "let's make a plan for what that will be"; build only after the plan is agreed.
2. **Meta-agent builds agents** — never scaffold a specialist by hand; the prompt-engineering agent (grounded in its own agentic-design-patterns KB) does it.
3. **Wire → empty-test → ingest** — the refusal test comes BEFORE seeding.
4. **Chapter-map first** — long source? Paste the chapter/section list, agent builds a working plan, then ingest in chunks against it. Paste text over PDFs (PDFs degrade past ~15 pages).
5. **Extract → Atomize → Normalize** — the only legal ingestion pipeline.
6. **Slim after every draft** — token-efficiency review ("less to read, more clarity, keep the steps" — his pass cut 55%).
7. **Teach at the moment of discovery** — correction found mid-task → update the durable skill/instructions BEFORE continuing.
8. **Log-and-pickup before ending** — session → chat-history entry + a pickup prompt for the next window.
9. **Economic routing** — consultative work in personal-agent chat (plan-included); scheduled automation only when value > credit cost, else a manually-triggered skill.

## Anti-Patterns (rejects on sight)

- **The bookmark graveyard** — capture without AI-owned organization + compounding loop ("We find something brilliant, we save it, and then we lose it" — *Build A Claude Knowledge Base That Self-Improves!*, 2026, `references/source-quotes.md` line 9)
- **Human-as-librarian** — hand-editing the wiki, manual tagging, plugin rituals ("The problem with something like Notion or Obsidian to manage a second brain... is that they kind of ask you to be the librarian. You organize things yourself" — *Build A Claude Knowledge Base That Self-Improves!*, 2026, `references/source-quotes.md` line 8)
- **Generic-with-a-process** — an agent with skills but no KB ("Without the knowledge base, I found that the AI tends to just be still a bit generic but with a very clear process that it is following" — *Turn Books Into AI Business Advisors (Full Notion Demo)*, 2026, `references/source-quotes.md` line 15)
- **Un-gated advisors** — instructions that don't mandate KB-read before answering ("make sure that the knowledge base we've created is directly referenced as a linked view early on ensuring that that is a mandatory step before it answers anything" — *Turn Books Into AI Business Advisors (Full Notion Demo)*, 2026, `extractions/systems-made-better/transcript-notion-advisors.txt`)
- **Multi-idea entries** — paragraphs masquerading as atoms; no when-to-apply; no confidence ("it goes through it extract atomize normalize into knowledge base entries... on each section extract all the information from within it atomize, so go what are the key concepts to take out" — *Turn Books Into AI Business Advisors (Full Notion Demo)*, 2026, `extractions/systems-made-better/transcript-notion-advisors.txt`)
- **Token bloat** — instructions that grow without a slimming pass; mid-process over-interruption that overloads context ("Before we now begin the ingest, please update your instructions thoughtfully and without creating too much token bloat" — *Turn Books Into AI Business Advisors (Full Notion Demo)*, 2026, `references/source-quotes.md` line 34)
- **Trust-by-default automation** — scheduled credit-burning agents where a monthly manual skill would do ("A lot of us won't want to be spending credits like this... go and make yourself a skill that does exactly that and then you can just trigger it with personal agent once a month... it's a hell of a lot cheaper" — *Turn Books Into AI Business Advisors (Full Notion Demo)*, 2026, `references/source-quotes.md` line 48)
- **Static libraries** — no health check; errors compound silently ("The AI will sometimes write something slightly wrong. You'll save it back and the next answer quietly builds on a mistake" — *Build A Claude Knowledge Base That Self-Improves!*, 2026, `references/source-quotes.md` line 42)

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|---|---|---|---|
| Groundedness | KB referenced sometimes | KB-read enforced; answers cite entries | Empty-KB refusal test passes; confidence-labeled fallbacks |
| Atomization | Entries exist, multi-idea | One idea/entry, schema-complete | When-to-Apply + Confidence on every entry; agents filter, not read |
| Glanceability | A database exists | Views by category + confidence | Hub dashboard; state readable in seconds; agents search by lane |
| Compounding | Answers discarded | Outputs saved back sometimes | Loop is a schema rule; day-100 measurably smarter than day-1 |
| Self-maintenance | Occasional cleanup | Ad-hoc health checks | 7-stage audit monthly; audits yield new entries, not just fixes |
| Token economy | It works | One slimming pass | Every artifact slimmed; corrections never repeat |
| Provenance | Sources mentioned | Source on every entry | Confidence weighted by source; unsourced auto-flagged |

**Score ≥8 requires naming the matching behavior** (e.g., "passes empty-KB refusal" for Groundedness 8+).

## Calibration Anchors

- **Ceiling**: The Seth Godin advisor — 3 chapters ingested, answers "position against AI productivity, not within it: less, but better," blending framework fidelity with the user's actual product context. Grounded specificity = framework × personal context.
- **Proof-of-system**: The empty-KB refusal — "I've searched it. There's nothing in there. I don't think I can help you" + clearly-labeled ungrounded fallback opinion.
- **Floor (reject)**: The Obsidian-vault screenshot — beautiful, linked, plugin-rich, and abandoned.

## Stacking (Antigravity-native)

Simon owns the **ORGANIZE** stage of the knowledge lifecycle: EXTRACT (MES 3.0 / `/extract`) → **ORGANIZE (Simon)** → RETRIEVE (Recall, sovereign memory) → DEPLOY (any expert). Bridges: `/library-extraction-bridge` (extractions → entries), `/library-notion-port` (any system → Notion), `/library-advisor-board` (advisors → `/convene` councils), memory-architect (decay/tiers × his schema).

## Factual Grounding Ledger

- His demos and system behavior: VERIFIED as on-screen demonstrations.
- Karpathy KB stats (~100 articles / 400k words; 105k bookmarks): LIKELY (his report of the post).
- His surname, business revenue: UNCONFIRMED — never assert.
- Notion product mechanics (credits, custom vs personal agents): LIKELY, product evolves — verify before promising behavior.

# Directives Index

**Purpose**: Navigation map and precedence hierarchy for the 53 directive files in this folder. Replaces the previous flat-file structure where every directive sat at the same level with no precedence guidance.

**Precedence rule**: Constitution > Protocols > Playbooks > API Policies. When two directives appear to conflict, the higher-precedence one wins. Within a tier, the more specific (narrower trigger) wins over the more general.

**Why an INDEX instead of moving files into subdirectories**: 144 files across the codebase reference `directives/<name>.md` paths. A filesystem reorganization would break those references. This INDEX gives Claude (and humans) the navigation map immediately, with the physical reorganization as a separate follow-up that updates references atomically.

---

## 00. Constitution — Chain-Must-Obey

These directives govern The Chain itself. Violating a constitutional directive corrupts every downstream output. Read on every session that produces a deliverable.

| Directive | What it owns | Fires at |
|---|---|---|
| [intent-pipeline.md](intent-pipeline.md) | DICE scoring + sharpening rubric | Chain Steps 1-2 |
| [agent-loading-protocol.md](agent-loading-protocol.md) | Tier 0-3 escalation rules + Hot Context Rule | Chain Step 4 |
| [recall-grounding-protocol.md](recall-grounding-protocol.md) | Tier 1.5 auto-grounding for content/brand domains | Chain Step 4 (sub-step 1.5) |
| [content_creation_gate.md](content_creation_gate.md) | Mandatory ≥2 skill files for content tasks | Chain Step 4 (content branch) |
| [verification-agent-protocol.md](verification-agent-protocol.md) | Factual claim inventory + source verification | Chain Step 5.5 |
| [quality_gate.md](quality_gate.md) | 4-dim scoring + factual veto + retry logic | Chain Step 6 |
| [evolution-direction.md](evolution-direction.md) | North star for what to evolve + stopping criteria | Read before any /skill-evolution run |
| [session-state-protocol.md](session-state-protocol.md) | When to write session state + what goes in it | Chain Step 4, after major decisions, every 10 reads |

---

## 10. Protocols — Active Decision Logic

These directives fire conditionally during execution. They do not govern The Chain itself but shape how individual steps behave.

| Directive | When it fires |
|---|---|
| [expert_auto_routing.md](expert_auto_routing.md) | Chain Step 3 — multi-domain ensemble selection |
| [collaboration-protocol.md](collaboration-protocol.md) | Always (multi-agent baseline) |
| [sub_agent_protocol.md](sub_agent_protocol.md) | When 2+ experts loaded OR 10+ files in context |
| [fleet-conductor-doctrine.md](fleet-conductor-doctrine.md) | Any repair/build fleet — batch lifecycle, 5 failure shapes, seating, W2 flip schedule (post-Fable: Opus conducts) |
| [deep_self_annealing.md](deep_self_annealing.md) | On any error during execution |
| [token-efficiency-protocol.md](token-efficiency-protocol.md) | Every workflow (load/escalation discipline) |
| [feedback-ratchet.md](feedback-ratchet.md) | Chain Step 6 finalize() |
| [skill-evolution-protocol.md](skill-evolution-protocol.md) | After /skill-evolution runs |
| [cross-pollination.md](cross-pollination.md) | Phase 3 evolution (gated — high-risk, require Fix 1 rubric first) |
| [multi-expert-synthesis.md](multi-expert-synthesis.md) | When 3+ experts loaded for a single deliverable |
| [research-protocol.md](research-protocol.md) | Research tasks — Gemini-primary priority order |
| [ai-slop-detector.md](ai-slop-detector.md) | Chain Step 5.5 — prose pattern detection |
| [quality_assurance.md](quality_assurance.md) | Chain Step 5 — anti-pattern enforcement |
| [expertise-gap-protocol.md](expertise-gap-protocol.md) | When the routed expert lacks coverage of the request |
| [hybrid-knowledge-retrieval.md](hybrid-knowledge-retrieval.md) | Combining Recall + NotebookLM + knowledge wiki |
| [parallel_thought.md](parallel_thought.md) | When breadth-first parallel exploration is warranted |
| [parallelism-cheat-sheet.md](parallelism-cheat-sheet.md) | Reference card for sub-agent parallelization |
| [operating-principles.md](operating-principles.md) | Development workflows |
| [user-state-awareness.md](user-state-awareness.md) | Detecting emotional/cognitive state from user message |
| [when-to-use-deep-think.md](when-to-use-deep-think.md) | When to escalate to extended-thinking models |

---

## 20. Playbooks — Domain-Specific SOPs

These are not chain governance — they are how-to docs for specific domains. Read only when the relevant domain task fires.

| Directive | Domain |
|---|---|
| [content-creation.md](content-creation.md) | Content production guidance |
| [ghostwriting-delivery.md](ghostwriting-delivery.md) | Client deliverable formatting for ghostwriting work |
| [linkedin-algorithm-context.md](linkedin-algorithm-context.md) | LinkedIn-specific platform constraints |
| [sales-conversation.md](sales-conversation.md) | Sales call structure / objection handling |
| [extraction-workflow.md](extraction-workflow.md) | Expert extraction pipeline |
| [extraction-to-skill.md](extraction-to-skill.md) | Converting extractions into completion-engine skills |
| [mes-3.0-extract.md](mes-3.0-extract.md) | Mastery Extraction System v3.0 — extract phase |
| [mes-3.0-validate.md](mes-3.0-validate.md) | Mastery Extraction System v3.0 — validate phase |
| [workflow-chains.md](workflow-chains.md) | How workflows compose into multi-step chains |
| [slash-command-playbook.md](slash-command-playbook.md) | Slash command authoring patterns |
| [external-skills-registry.md](external-skills-registry.md) | Imported third-party skills (Matt Pocock/AI Hero + future sources) — install, update, catalog, Chain-bypass rules |
| [daily-council.md](daily-council.md) | Daily expert council ritual |
| [decision-council.md](decision-council.md) | Convening councils for decisions |
| [session-end-commit.md](session-end-commit.md) | End-of-session git workflow |
| [tier0-cards.md](tier0-cards.md) | Tier 0 invocation card format spec |

---

## 30. API & Integration Policies — Budget Gates

These directives govern external API usage. Check before any call that costs money or quota.

| Directive | What it gates |
|---|---|
| [google-api-usage-policy.md](google-api-usage-policy.md) | Gemini Deep Research $10 prepaid ceiling |
| [google-api-setup-checklist.md](google-api-setup-checklist.md) | One-time GCP/Gemini setup |
| [gemini-reference.md](gemini-reference.md) | Gemini API reference (quirks, params) |
| [perplexity-usage-policy.md](perplexity-usage-policy.md) | Perplexity $30/mo budget — fallback + quick facts only |
| [notebooklm-usage-policy.md](notebooklm-usage-policy.md) | NotebookLM 100 queries/mo |
| [notebooklm-pro-outputs.md](notebooklm-pro-outputs.md) | NotebookLM output formatting |
| [apify-usage-policy.md](apify-usage-policy.md) | Apify $29/mo Starter plan |
| [mcp-research-setup.md](mcp-research-setup.md) | MCP research tool integration |
| [mcp-server-setup.md](mcp-server-setup.md) | MCP server registration |
| [notion-databases.md](notion-databases.md) | 6 Notion DB IDs + schemas |
| [notion-autofill-guide.md](notion-autofill-guide.md) | Notion autofill property setup |
| [skill-paths-reference.md](skill-paths-reference.md) | Skill directory naming reference |

---

## _archived/ — Deprecated

Files in `_archived/` were superseded. Do NOT read them; they exist only for git history. Move new directives here when they are replaced by a successor — never delete (preserves provenance).

Currently archived: `intent_refiner.md`, `invoke-expert.md`, `pre_flight_validation.md`, `router_agent.md`, `session_kickoff.md`.

---

## Conflict Resolution Rules

1. **Tier wins**: Constitution > Protocols > Playbooks > API Policies. A protocol cannot override a constitutional directive.
2. **Specificity wins** within tier: A directive triggered by a narrower condition wins over a broader one.
3. **Recency wins** when ties remain: A directive with a more recent `Last updated` (in its own header or per `git log`) wins.
4. **Code wins over markdown**: When a directive describes runtime behavior also enforced by Python (e.g., routing bindings → `execution/routing_enforcer.py`, quality gate → `execution/chain_runner.py`), the code is authoritative. Update both together.

---

## Stale Candidates (Review Required)

These directives have not been referenced from CLAUDE.md or any active workflow in the audit window (2026-04-24). Review whether they are still load-bearing. If not, move to `_archived/`.

- (Run `grep -rL "<filename>"` across the codebase to confirm before archiving — this list is a starting point, not a verdict.)
- Specific candidates surfaced by the 2026-04-24 audit: any directive with no inbound reference from CLAUDE.md, an active workflow, or another high-tier directive.

A future automation can populate this section nightly via a script that walks the dependency graph and flags orphans.

---

## Where to Add New Directives

- **New constitutional directive**: Reserve for changes to The Chain itself. Requires explicit owner approval + companion code change in `execution/chain_runner.py`.
- **New protocol**: When a new conditional decision pattern emerges that fires across multiple workflows.
- **New playbook**: When a new domain or client type needs its own SOP.
- **New API policy**: When integrating a new external service with cost or quota implications.

**Resist the temptation to add a directive to "fix" a routing or quality bug.** Adding the 54th directive to patch a runtime issue is the structural pattern the 2026-04-24 audit flagged as load-bearing technical debt. The routing enforcer (`execution/routing_enforcer.py`) is the right answer for routing problems; another markdown file is not.

---

*Last updated: 2026-04-24. Generated as part of Fix 6 from the system audit at `_active/system-audit/audit-2026-04-24.md`.*

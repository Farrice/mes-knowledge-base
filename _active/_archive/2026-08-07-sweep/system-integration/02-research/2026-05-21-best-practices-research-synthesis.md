# Best-Practices Research Synthesis — 2026-05-21

> **Context**: Five parallel deep-research streams launched alongside Wave 5 of the /autopilot build. Topics: agent orchestration, harness architecture, skills systems, plugins/MCP, sub-agent orchestration layers. Goal: identify confirmed best practices from top labs to integrate into Antigravity.
>
> **Sources**: Anthropic engineering blog, Claude Code official docs, Claude Agent SDK, OpenAI Swarm, Microsoft AutoGen, Cognition Labs (Devin), Karpathy's writings, Hamel Husain, Eugene Yan, modelcontextprotocol.io reference servers, Jesse Vincent's obra/superpowers ecosystem.
>
> **Resolution**: This brief catalogs findings, flags what Antigravity already does well (do not break), and prioritizes integrations into three tiers: SHIPPED IN WAVE 5, READY FOR NEXT SESSION, BIGGER PROJECTS.

---

## Headline Synthesis

The five research streams converge on a single thesis: **Antigravity is at or above the production frontier on architecture; the gap is in three specific Claude-Code-native primitives that shipped in the last 90 days** — Hooks-as-deterministic-enforcement, the Anthropic 4-field subagent envelope, and `paths:` frontmatter on per-client skills. Adopting these three closes the AI-Memory-Dependent-Observability failure class permanently.

The most surprising finding: **Cognition's "Don't Build Multi-Agents" position is the strongest counter-thesis to Wave 5 fan-out**. The Super Mario / bird failure mode is real — parallel sub-agents WRITING produce divergent decisions. The mitigation: restrict fan-out to read-heavy phases (research, review, verification, diagnosis) — which is exactly what Anthropic's own research system does. This insight is now encoded in `.agent/workflows/autopilot.md` Phase 2 (Wave 5 read-only constraint table).

---

## What Antigravity Already Does Well (DO NOT BREAK)

Cross-cutting acknowledgments from all 5 streams:

1. **Progressive disclosure / tiered loading** (T0→T3) is more sophisticated than Anthropic's skill-only progressive disclosure. `directives/agent-loading-protocol.md` is field-leading.
2. **6-level memory architecture** (CLAUDE.md inheritance + session-state + Recall + MEMORY.md + knowledge/ + Notion) covers what Anthropic docs only describes in fragments.
3. **Per-client CLAUDE.md inheritance** (Phase B Move 3, 2026-05-12) — ahead of Cursor + Aider; matches Claude Code's canonical convention.
4. **4-dimension quality gate + Wave 1+2+3 calibration enforcement** is more rigorous than what Anthropic ships publicly. The bimodal taste filter is novel IP.
5. **Routing enforcer (deterministic, not advisory)** anticipated the field consensus by months.
6. **Skill evaluation infrastructure** (`skill_benchmark.py`, `ground_truth.py`, `/skill-evolution`) is ahead — Anthropic explicitly says "there is not currently a built-in way to run these evaluations."
7. **Sub-agent protocol** (read-heavy / write-light spawn rule, no nesting, sealed scope) is field-aligned — the only issue is the 0-activation history.
8. **Atom-vs-system internal taxonomy** is a genuine architectural insight without a public Anthropic equivalent. Keep as internal layer.
9. **Hookify + episodic-memory + Recall + Notion stack** is the production-grade memory + observability triad recommended by Jesse Vincent / obra.
10. **6 of 8 high-signal Anthropic-built plugins already installed**.

---

## Five Stream Findings (one paragraph each)

### Stream 1 — Agent Orchestration (Anthropic, OpenAI Swarm, AutoGen, CrewAI, LangGraph)

The dominant 2026 pattern is **orchestrator-worker, not flat peer agents**. Anthropic's "Building Effective Agents" distinguishes "workflows" (predefined code paths) from "agents" (LLM-directed processes). Their research system uses lead agent → spawned subagents pattern. OpenAI Swarm and AutoGen support flat patterns but both explicitly point users to orchestrator-worker for production. **The Anthropic spawn budget is canonical**: 1 agent / 3-10 tools for fact-find; 2-4 agents / 10-15 tools for comparison; 10+ only for complex research. The 4-field envelope (objective, output format, prioritized tools, boundaries) is mandatory — vague delegation ("research the semiconductor shortage") causes 30%+ duplicate work and gaps. Subagent outputs should be **lightweight references** (write to disk, return summary + path), not inline text. Antigravity's `parallel_swarm.py::execute_agent_with_fallback` already implements field-standard recovery (status states: success / rerouted / needs_refine / failed / skipped).

### Stream 2 — Harness Architecture (Claude Code, Cursor, Aider, Cline, Devin, Replit)

Claude Code 2026 shipped 27+ hook events (`PreToolUse`, `PostToolUse`, `SessionStart`, `UserPromptSubmit`, `Stop`, `SubagentStart`, `PreCompact`, `FileChanged`, etc.) — **hooks bound to `.claude/settings.json` are the deterministic backstop layer**. Antigravity has `.claude/hookify.*.local.md` files but they appear to be documentation, not active settings bindings. The Anthropic Auto Mode shipped a two-stage Sonnet 4.6 classifier (fast filter → CoT for flagged) — `/autopilot`'s pure gate-suppression posture is more aggressive than Auto Mode; a classifier layer is a future-Wave-6 enhancement. **Skill-listing budget** is 1% of context window with 1,536 chars per skill — Antigravity's 232 skills almost certainly overflow this; lowest-priority descriptions drop silently. Plan mode + Auto/Act mode toggle is field-standard; `/autopilot` is the Auto-Mode-without-classifier equivalent. **The single highest-leverage Wave 6 task: convert `.claude/hookify.*.local.md` from docs into active settings.json hook bindings** (PreToolUse for routing_enforcer, Stop for finalize, UserPromptSubmit for recall grounding).

### Stream 3 — Skills Systems (Anthropic Claude Skills, GPT Custom Actions, Gemini Gems, Cursor Rules)

Anthropic's canonical SKILL.md is looser than Antigravity's format but stricter where it matters: `name` ≤64 chars (hyphenated lowercase, no reserved words), `description` ≤1024 chars (third-person + "Use when..." trigger phrases + "be pushy" claim), 500-line SKILL.md cap with progressive disclosure to `reference/*.md` files. Antigravity's skills use non-canonical fields (`version`, `format`, `workflows`, `expert`, `domain`) — they don't break anything but don't help discovery either. **The single highest-leverage skill upgrade: rewrite the top 20 hot-path skill descriptions** to Anthropic spec (third-person + "Use when [triggers]" + pushy clause). 4-6 hours of work; biggest discovery lift available. Missing primitive: **`paths:` glob frontmatter** that auto-loads skills only when working with matching files (e.g., Jen's listing-content skill should auto-load on `_active/clients/jen-listings/**`). The atom-vs-system distinction in CLAUDE.md is a genuine architectural insight; just position it as internal sub-taxonomy underneath the field-standard Tool / Skill / Subagent / Plugin primitive table.

### Stream 4 — Plugins + MCP

Claude Code 2026 plugin contract is now `.claude-plugin/plugin.json` + optional `skills/`, `commands/`, `agents/`, `hooks/hooks.json`, `.mcp.json`, `monitors/monitors.json`, `bin/`. `mcpServers` is a first-class manifest field; episodic-memory ships its own MCP via `${CLAUDE_PLUGIN_ROOT}/cli/mcp-server-wrapper.js`. Antigravity's custom `jarvis-command-center` plugin manifest is metadata-only (10 lines) — a 70% under-utilized plugin. **Best-of-breed installations**: 6 of 8 high-signal Anthropic-built plugins already in. Anthropic's "Code Execution with MCP" thesis: present MCP servers as code on a filesystem, not as upfront tool definitions — 98.7% token reduction. **The single highest-leverage MCP gap**: `claude_ai_Notion` likely uses the newer client (`data_sources` instead of `properties`) — same bug class Antigravity already documented at root. Swap to `makenotion/notion-mcp-server` OR extend `execution/notion_api.py` with an MCP wrapper. Add Anthropic's official `memory` MCP (entity graph) — fills gap between conversation memory (episodic), source-card memory (Recall), and metadata (Notion). New 2026 feature: `monitors/monitors.json` watches files and surfaces changes as session events — closes AI-Memory-Dependent Observability gap deterministically.

### Stream 5 — Sub-Agent Orchestration Layers

The field has converged on a sharp rule that maps 1:1 onto Antigravity's dormant `sub_agent_protocol.md`: **spawn sub-agents when the work is read-heavy and parallel, NEVER when it's write-heavy and sequential**. Cognition's "Don't Build Multi-Agents" thesis: Devin runs single-threaded for write tasks because "actions carry implicit decisions, and conflicting decisions carry bad results." This is THE constraint Wave 5 fan-out must encode (and now does — see autopilot.md Phase 2 read-only matrix). Anthropic's 4-field envelope is the canonical anti-vague-delegation pattern. **Critical SDK detail**: parent passes ONLY the Agent tool's prompt string; subagent does NOT receive parent conversation history. Sub-agents cannot spawn further sub-agents (no nesting). Return channel is verbatim — structured return format must be enforced inside the subagent's system prompt, not at the SDK level. Antigravity's protocol is field-aligned; it's just dormant. **The activation lever**: deterministic spawn-or-log in `chain_runner.finalize` — any qualifying workflow that runs without sub-agents AND has factual_surface OR 2+ experts declared gets soft-blocked unless explicitly skipped with a one-line reason.

---

## Integrations: SHIPPED IN WAVE 5

Already integrated into the Wave 5 build:

1. **Read-only fan-out constraint** (`.agent/workflows/autopilot.md` Phase 2 + the per-outcome-class fan-out posture matrix). Cognition's thesis encoded as a hard rule.
2. **Anthropic 4-field subagent envelope** (autopilot.md Phase 2 — explicit prompt template with OBJECTIVE / OUTPUT FORMAT / TOOLS ALLOWED / BOUNDARIES sections).
3. **Tiered subagent budget** (autopilot.md Phase 2 — 1 agent / 3-10 tools to 12-worker hard cap).
4. **Lightweight references pattern** (autopilot.md Phase 2 — workers write to `.tmp/autopilot/<session_id>/worker-N-slug.md`, return ≤500 token summary + filepath).
5. **Synchronous fan-in synthesis** (autopilot.md Phase 2 — no peer coordination between workers; orchestrator owns synthesis).
6. **Documented Anthropic failure modes** (autopilot.md Phase 2 — over-spawning, endless searching, source quality bias, prompt injection in returns).

---

## Integrations: READY FOR NEXT SESSION (≤2 hours each)

These are low-effort high-leverage. Pick top 2-3 for next session:

### A. Update `directives/sub_agent_protocol.md` with the Anthropic 4-field envelope (30 min)
Replace the existing freeform SkillExecutor template at lines 42-57 with the four named fields: `objective:`, `output_format:`, `tool_allowlist:`, `boundaries:`. Mirrors what autopilot.md Phase 2 already encodes; closes the gap between the protocol and the workflow that actually fires it.

### B. Audit `.claude/hookify.*.local.md` against `.claude/settings.local.json` (30 min)
Verify whether hookify hooks are wired into settings.local.json as active bindings. If they're documentation-only (likely), wire them. Critical for closing AI-Memory-Dependent-Observability gap. Specifically:
- `PreToolUse` → `python3 execution/routing_enforcer.py check`
- `Stop` → `python3 execution/chain_runner.py finalize` (if expert output produced)
- `UserPromptSubmit` → Recall grounding fire/skip log

### C. Rewrite top 20 hot-path skill descriptions to Anthropic spec (4-6 hours, can be parallelized)
Third-person + explicit "Use when..." trigger list + pushy clause. Cap at 1,024 chars. Start with: `parallax`, `writers-room`, `extract-forge`, `build-bos`, `fantastic-posters`, `lara-acosta-linkedin-ghostwriting`, `nicolas-cole-*`, `luke-iha-*`, the JCC family (`jcc-deploy`, `campaign`, `strike`, `solo`), `supercomputer`, `autopilot`, `atomize`, `system-audit`, `research-swarm`. This may be the single biggest cognitive-load reduction available.

### D. Audit SKILL.md sizes against 500-line cap (15 min)
`wc -l skills/*/SKILL.md | sort -rn | head -30`. Any skill >500 lines: split using Anthropic Pattern 1 (domain-organized references in `reference/`). Some skills almost certainly overflow.

### E. Hook `parent_tool_use_id` into `orchestration_ledger.py` (1 hour)
Capture which deliverable came from which fan-out worker. Anthropic SDK emits this on every sub-agent message. Closes observability gap on parallel autopilot runs.

### F. Add `paths:` frontmatter to per-client skills (30 min)
- `skills/jen-santulan-listing-content/SKILL.md` → `paths: ["_active/clients/jen-listings/**", "projects/jen-*/**"]`
- Andrea / Farrice brand skills similarly scoped
- Eliminates "wrong voice loaded" failures structurally

---

## Integrations: BIGGER PROJECTS (multi-session)

### G. Build classifier layer for /autopilot (Wave 6)
Mirror Anthropic Auto Mode's two-stage pattern: fast filter on tool category, CoT only on flagged actions, strip assistant text before evaluation. Replaces pure gate-suppression with intelligent gating. New file: `execution/autopilot_classifier.py`.

### H. Promote `jarvis-command-center` to full plugin manifest (4-6 hours)
Currently 10-line metadata-only. Declare contributions (skills, agents, hooks, MCP servers) so it's installable on a second machine. Step 1 toward making Antigravity portable.

### I. Replace `claude_ai_*` MCP servers with local-first alternatives (one session)
Swap Notion / Gmail / Drive / Calendar to local-first MCP servers (Notion via `execution/notion_api.py` wrapper, Gmail/Drive/Calendar via `gws mcp` which is already installed). Keep vendor-only MCPs (Higgsfield, Canva, Gamma, Ahrefs, AWS Marketplace). Eliminates a documented bug class.

### J. Add Anthropic `memory` MCP server (15 min + integration)
Entity graph layer underneath existing memory stack. Fills gap between conversation memory (episodic), source-card memory (Recall), and metadata (Notion).

### K. Add `monitors/monitors.json` to `jarvis-command-center` (1 hour)
Watch `.agent/session-state.md` + `evolution_store/traces/routing_decisions.jsonl` and surface changes as session events. Deterministic backstop for ledger observability.

### L. Codify field-standard Tool / Skill / Subagent / Plugin primitive table in CLAUDE.md (30 min)
Replace or augment the atom/system section. Position internal atom/system taxonomy as sub-classification underneath the field-standard primitive table. Reduces semantic confusion in the 232 skills + 109 agents + MCP tools + plugins decision tree.

### M. Codify `!command` dynamic context injection for gate-bearing workflows (per-workflow effort)
Anthropic's skill primitive `` !`<command>` `` runs deterministically before LLM sees content. Parallax Phase 2.5 ground-check could become `` !`python3 execution/recall_logger.py latest --topic="{topic}"` `` — the exact deterministic-backstop pattern Antigravity's feedback memos demand.

---

## Counter-Reads (where the thesis could be wrong)

1. **The orchestrator-worker thesis could overfit to research.** Anthropic publishes what worked for their research system. Antigravity optimizes for taste-aligned content production. Some patterns (lightweight references, plan persistence) transfer cleanly. Others (10+ subagents) may not.
2. **Hooks add brittleness.** Every PreToolUse hook is a shell command that can fail and block legitimate work. Cursor deliberately avoids this layer. The trade-off must be navigated case-by-case.
3. **`paths:` glob fragmentation risk.** Adding `.claude/rules/*.md` scoped by path could make discoverability WORSE on a 232-skill base, not better. Pilot on 5-10 client skills before universalizing.
4. **Cognition's anti-multi-agent position could be too conservative for some Antigravity outcome classes.** If atomization with strict scope isolation works in practice (each derivative has independent source anchor + anti-scope clause), parallel writes are safe. Wave 5 v1 defaults sequential; v2 may unlock.
5. **15× token cost of multi-agent is non-trivial.** Anthropic explicitly: multi-agent only pays off "where the value of the task is high enough." `cost_gate.py` + G2 handle this, but if autopilot auto-fans-out below G2 threshold, money bleeds on tasks that didn't need parallelism.

---

## Recommended Next Session Sequence

After exercising autopilot on real work for a week, run integrations A, B, F in one session (≤2 hours combined). These three close the largest documented failure classes: sub-agent envelope drift, AI-Memory-Dependent-Observability, and wrong-voice-loaded errors. Defer C (description rewrites — high-value but big) and the I/J/K/L cluster (multi-session) until after first wave of /autopilot data ships.

---

## Source Inventory

**Internal (referenced across streams)**:
- `/Users/farricecain/Google Antigravity/CLAUDE.md` (current Antigravity structure + Skill Architecture section)
- `/Users/farricecain/Google Antigravity/_active/_archive/2026-08-07-sweep/system-integration/2026-05-12-agentic-os-elevation-brief.md` (atom-vs-systems brief)
- `/Users/farricecain/Google Antigravity/directives/sub_agent_protocol.md` (dormant protocol)
- `/Users/farricecain/Google Antigravity/.agent/workflows/autopilot.md` (Wave 4-5 implementation)
- `/Users/farricecain/Google Antigravity/extractions/agentic-os-integration/pattern-inventory-and-delta.md`
- `execution/parallel_swarm.py::execute_agent_with_fallback` (field-standard recovery already shipped)

**External (verified primary sources)**:
- Anthropic: Building Effective Agents — anthropic.com/engineering/building-effective-agents
- Anthropic: Multi-Agent Research System — anthropic.com/engineering/multi-agent-research-system
- Anthropic: Equipping agents for the real world with Agent Skills — anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic: Code Execution with MCP — anthropic.com/engineering/code-execution-with-mcp
- Anthropic: Claude Code Auto Mode — anthropic.com/engineering/claude-code-auto-mode
- Claude Code docs: code.claude.com/docs/en/{skills,subagents,memory,hooks,permissions,plugins,agent-sdk/subagents}
- Cognition Labs: Don't Build Multi-Agents — cognition.ai/blog/dont-build-multi-agents
- Karpathy: Sequoia Ascent 2026 — karpathy.bearblog.dev/sequoia-ascent-2026/
- Modelcontextprotocol.io spec + reference servers
- Jesse Vincent / obra: superpowers, episodic-memory (github.com/obra)
- Anthropic skill repo: github.com/anthropics/skills
- The Prompt Shelf: Claude Code Hooks Complete Reference 2026 — thepromptshelf.dev/blog/claude-code-hooks-complete-reference-2026/
- Agent Skills open standard: agentskills.io/specification

**Gaps honestly flagged**:
- Perplexity quota exhausted partway through Stream 1; some 2026 ICML/NeurIPS papers not fetched.
- LangGraph supervisor docs failed to load in Stream 5 (sufficient material from Anthropic SDK).
- No direct telemetry on Antigravity's skill-listing budget overflow (Stream 3 inferred from skill count; recommend running `/doctor` to confirm).
- Hookify settings.local.json wiring status not directly verified (Stream 2 inferred from file listing; recommend `jq '.hooks' .claude/settings.local.json` to confirm).

# Playwright Retrofit Audit — 2026-05-14

**Audit window**: 2026-04-30 to 2026-05-14 (14 days)
**Audit date**: 2026-05-14
**Auditor**: Claude Sonnet 4.6 (chain_runner Step 6 not applicable — system audit, no expert output)

---

## TL;DR

**0 confirmed Playwright invocations** exist in any log file during the audit window. The subagent half of the retrofit lasted only **4 days** (2026-04-28 to 2026-05-02) before being excised for routing pollution; the workflow callouts remain active but are advisory in framing and produce no observable signal. The trace infrastructure does not log tool-level invocations at all — meaning "no evidence of adoption" is not the same as "zero adoption," but the system cannot answer the question either way. Recommendation: **(c) broader adoption work**, priority fix being measurability before framing.

---

## Trace Inventory

### Available log files and what they contain

| Log | Location | Post-2026-04-30 data? | Tool calls logged? |
|---|---|---|---|
| v2_traces | `evolution_store/v2_traces/` | No — last trace 2026-04-22 | No — records finalize scores only |
| routing_decisions.jsonl | `evolution_store/traces/` | **FILE DOES NOT EXIST** | Would log routing enforcer checks |
| recall_log | `execution/recall_logger.py` | Unconfirmed — no output files found | Auto-logs grounding events in finalize |
| Perplexity usage | `.agent/perplexity-usage.json` | No — last query 2026-04-25 | Logs queries, not invocation context |
| Apify usage | `.agent/apify-usage.json` | 0 events total | n/a |
| Session index | `sessions/SESSION_INDEX.md` | One entry from 2026-03-30 | No tool data |
| Skill audit JSONL | `evolution_store/skill_audit_*.jsonl` | Yes (05-03, 05-05) | Tracks skill-level traces, not tool calls |

### Raw counts

**Playwright invocations in any log file (post-2026-04-30)**: **0**

**WebFetch invocations in any log file (post-2026-04-30)**: **0**

**Why both are zero**: The system's trace infrastructure (`chain_runner.py` v2_traces, `routing_enforcer.py` log, `recall_logger.py`) records quality scores and grounding events — not tool-call sequences. There is no mechanism that captures "this session called `mcp__playwright__browser_navigate` 3 times." Tool-level telemetry is absent. The `context.telemetry.tool_calls` field in v2_traces records a total count (e.g., `"tool_calls": 24`), but does not break down by tool name.

**Playwright references found in repo (not invocations)**:
- 12 references in `.agent/workflows/` (static callout text, all added 2026-05-01)
- 6 references in `execution/skill_chunks.json` (documentation in design-md and product-design-build skills)
- 7 archived subagent files in `.claude/agents/_archived/` (post-retrofit versions, now inactive)

**Ratio Playwright/WebFetch**: **INCALCULABLE** — no per-tool invocation data exists for any window. The prerequisite for a ratio audit is logging that was never built.

---

## Critical Timeline Finding

The audit brief describes the retrofit as shipping 2026-04-30. Actual commit history reveals a two-phase rollout with a rapid partial rollback:

| Date | Event | Commit |
|---|---|---|
| 2026-04-28 | 12 subagents shipped (`.claude/agents/*.md`) including Playwright tool grants for 7 | `2bc6817` |
| 2026-05-01 | 13 workflow callouts + `directives/browser-automation-routing.md` added (bundled in Rory v4.0 workspace commit) | `a9c2a87` |
| 2026-05-02 | All 12 subagents excised to `_archived/` — "consistently producing subpar output and polluting routing" | `c562870` |

**The subagent half of the retrofit lasted 4 days.** The workflow callouts and routing directive remain active as of 2026-05-14.

The excision commit notes that subagents were used "extensively across the Coach Cooz pivot and other client work" — confirming at least one multi-session usage window. But those invocations are not logged in any accessible artifact.

---

## Subagent Usage Table

> **Note**: All 7 retrofitted subagents were excised to `_archived/` on 2026-05-02. They are no longer active as local agent definitions. The harness system prompt retains their definitions (inherited from the archived frontmatter), but the behavioral change — excision — is the operative state.

| Subagent | Active window | Invocations (logged) | Playwright fired (logged) | Notes |
|---|---|---|---|---|
| competitive-intel | 2026-04-28 to 2026-05-02 (4 days) | Unknown — 0 logged | 0 logged | Advisory framing: "Try WebFetch first... Escalate when content is missing." No directive trigger. |
| deep-research | Same | 0 logged | 0 logged | Advisory framing in body. Playwright in tool grant only. |
| fact-verifier | Same | 0 logged | 0 logged | Playwright listed in tools; body text does not mention it. |
| icp-deep-canvasser | Same | 0 logged | 0 logged | Advisory framing. |
| expert-extractor | Same | 0 logged | 0 logged | Advisory framing. |
| synthesis-engine | Same | 0 logged | 0 logged | 1 playwright ref (tool grant only). |
| swarm-orchestrator | Same | 0 logged | 0 logged | 1 playwright ref. Most narrow scope of any subagent. |

**Root cause of excision (from commit `c562870`)**: "Claude defaulted to them instead of the 119 expert personas + 210 skills + workflow library that already exist." The subagents created a competing routing layer, not a complementary one. The Playwright capability was a secondary casualty — correct tool in a wrong architecture.

**Partial observation from evidence**: The competitive-intel subagent body text includes a well-reasoned escalation ladder for Playwright (login-gated content, screenshot evidence, JS-rendered apps). But it opens with "Try WebFetch first." Under advisory framing, the escalation path requires a failed WebFetch attempt to trigger — which adds a round-trip, increases session friction, and may not surface as explicit Playwright use even when it fires.

---

## Workflow Usage Table

> **Note**: All 13 workflow callouts remain active. No workflow-level invocation tracking exists. The table below reflects what can be inferred from deliverables, research outputs, and commit history, not from direct invocation logs.

| Workflow | Callout added | Post-2026-05-01 invocations (inferred) | Playwright fired (logged) | Callout framing |
|---|---|---|---|---|
| competitor-intel | 2026-05-01 | 0 confirmed | 0 | Advisory: "Reach for Playwright when..." |
| lookalike-content | 2026-05-01 | 0 confirmed | 0 | Advisory. Documents LinkedIn hydration shell problem explicitly. |
| format-scan | 2026-05-01 | 0 confirmed | 0 | Advisory. |
| spy-market | 2026-05-01 | 0 confirmed | 0 | Advisory. |
| watch-and-remix | 2026-05-01 | 0 confirmed | 0 | Directive table: "Playwright — `read_url_content` returns empty hydration shells on LinkedIn." Strongest framing of any workflow. |
| hunt-trends | 2026-05-01 | 0 confirmed | 0 | Advisory: "Apify remains primary for scaled scraping; Playwright is the targeted-investigation alternative." |
| hidden-gems | 2026-05-01 | 0 confirmed | 0 | Advisory. |
| parallax (Phase 2.5) | 2026-05-01 | 0 confirmed | 0 | Advisory: "highest-fidelity verification path." Well-scoped to Phase 2.5 verification use. |
| analyze-intent | 2026-05-01 | 0 confirmed | 0 | Advisory. |
| narrative-warfare | 2026-05-01 | 0 confirmed | 0 | Strong advisory: "WebFetch returns hydration shells on these surfaces and silently degrades the OODA assessment." Near-directive. |
| flood-zone | 2026-05-01 | 0 confirmed | 0 | Near-directive: "Real-time intelligence via WebFetch is unreliable on these surfaces." |
| parasite-seo | 2026-05-01 | 0 confirmed | 0 | Advisory: SERP screenshot evidence. |
| spy-amazon | 2026-05-01 | 0 confirmed | 0 | Advisory: Apify-first with Playwright as verification fallback. |

**"0 confirmed"** means no deliverable, research output, or finalize note in the 2026-05-01 to 2026-05-14 window references these workflows by name or shows the characteristic output they produce. Three workflows (competitor-intel, lookalike-content, watch-and-remix) have semantic overlap with work in scope during this period, but no specific invocation evidence.

---

## Missed-Opportunity Log

The grep for `hydration|empty page|login wall|JS not rendered|cloudflare|couldn't verify|403|401` produced 0 hits in deliverables or finalize notes from the audit window. The only strong missed-opportunity signal is structural, not from a specific failed session:

**Signal 1 — watch-and-remix.md explicit documentation (structural)**
File: `.agent/workflows/watch-and-remix.md`, lines 35-37

```
| LinkedIn URL | Playwright (`browser_navigate` + `browser_evaluate`) — `read_url_content` returns empty hydration shells on LinkedIn |
| Twitter/X URL | Playwright (`browser_navigate` + `browser_evaluate`) — same JS-rendering issue |
| Instagram / TikTok URL | Playwright with persistent profile (login-gated) per `directives/browser-automation-routing.md` |
```

This is not a log entry of a failure — it is a workflow that has **pre-documented the failure condition** as justification for using Playwright. The table uses directive framing ("Playwright — returns empty hydration shells") but the session still has to invoke it. Since `watch-and-remix` is one of the most frequently invoked visual/content analysis workflows, and LinkedIn/Instagram are common sources, every invocation of this workflow on social platform URLs is a potential Playwright trigger that may or may not be firing.

**Signal 2 — no routing_decisions.jsonl (structural)**
File: `evolution_store/traces/routing_decisions.jsonl` — **FILE NOT FOUND**

`routing_enforcer.py` was added as part of the 2026-04-24 audit infrastructure (Fix 2). Its post-hoc check fires in `chain_runner.py finalize()` when `--workflow` is supplied. The file not existing means either (a) no finalize calls have included `--workflow` since the routing_enforcer was added, or (b) the routing_enforcer import is silently failing. Either case means the enforcement layer has never produced data. Without this data, the Mandatory Workflow Routing table in CLAUDE.md has no observability whatsoever.

**Signal 3 — perplexity usage spike on static content (pre-retrofit, indicative)**
`.agent/perplexity-usage.json` shows 10 queries on 2026-04-14 for a swarm-research task on prediction market strategies — all via `sonar-pro` for general research synthesis. None of these are the kind of JS-rendered / login-gated task where Playwright would apply. The Perplexity queries are being used correctly (synthesis, not primary-source verification). There is no evidence of Perplexity being used as a workaround for surfaces where Playwright should have fired.

---

## Recommendation

**Recommendation: (c) Retrofit needs broader adoption work** — specifically, the measurement infrastructure must be built before adoption can be improved.

**Evidence chain**:

1. `routing_decisions.jsonl` does not exist → the routing_enforcer has never logged a decision in production → there is literally no signal about whether the Mandatory Workflow Routing table is being followed
2. v2_traces stop at 2026-04-22 — an 8-day gap before the retrofit even shipped → tool-level adoption can never be reconstructed from the trace store
3. Perplexity usage stops 2026-04-25 → 9 days before current date, with no WebFetch or Playwright comparables → no tool substitution data exists
4. The subagent excision commit confirms sessions happened in the 4-day window but produces no tool-level evidence → even active use leaves no audit trail
5. 12 of 13 workflow callouts use advisory language ("Reach for Playwright when...") → advisory framing requires a failure signal to trigger; in sessions where WebFetch returns near-empty content without obviously failing, the agent may not escalate

**Why not (a)**: Advisory framing clearly has not created measurable adoption because there is no evidence of any adoption signal in any log over 14 days. "Advisory works" requires evidence that it's working.

**Why not (b)**: Sharpening framing in 1-2 specific subagents is not actionable because the subagents are excised. Sharpening workflow callouts is part of the answer, but fixing framing before fixing measurement inverts the dependency: you need a signal before you can know whether sharpened framing changed behavior.

---

## Specific Next-Action Proposals

### Proposal 1: Seed routing_decisions.jsonl with a mandatory `--workflow` finalize pattern

**Problem**: `routing_decisions.jsonl` doesn't exist because either (a) finalize calls omit `--workflow`, or (b) the routing_enforcer import silently fails.

**Fix**: Add a startup check to `chain_runner.py finalize()` that warns when `--workflow` is not supplied for non-system task types. Even a "workflow: unknown" entry creates a log. Then confirm the routing_enforcer import works by running:
```bash
python3 execution/routing_enforcer.py check --request "competitive analysis" --workflow competitor-intel --quiet
```
and checking whether it creates `evolution_store/traces/routing_decisions.jsonl`.

**Why this first**: You cannot improve what you cannot measure. Every other proposal depends on having a signal.

### Proposal 2: Harden callout framing in the top 3 workflows from advisory to directive

**Target workflows**: `watch-and-remix`, `lookalike-content`, `narrative-warfare` — all involve social platform content (LinkedIn, Instagram, Twitter) where WebFetch is documented to return hydration shells.

**Change pattern**: Replace "Reach for Playwright when..." with "USE Playwright (not WebFetch) for [specific surface]."

Example for `lookalike-content.md` (current):
```
> **Browser tools**: LinkedIn / Instagram / TikTok / Twitter posts are JS-rendered and often
> login-gated — WebFetch returns empty hydration shells. Use Playwright...
```

Proposed sharpening:
```
> **Browser tools — REQUIRED for social platforms**: LinkedIn, Instagram, TikTok, and Twitter
> are login-gated and JS-rendered. WebFetch returns empty hydration shells on all four.
> DEFAULT to `mcp__playwright__browser_navigate` + `browser_evaluate` for these surfaces.
> Do NOT attempt WebFetch first — there is no useful fallback content to escalate from.
```

`watch-and-remix.md` already has the strongest framing (directive table format) — no change needed. `narrative-warfare.md` and `flood-zone.md` are near-directive and need only minor strengthening.

### Proposal 3: Add a `--playwright` flag to finalize notes convention

**Problem**: No way to search finalize logs for Playwright usage because notes are free-form.

**Fix**: Establish a convention: when a session fires Playwright, add `| Tools: playwright` to the `--notes` argument. This doesn't require code changes — it's a convention enforced by documentation. Add one line to `directives/quality_gate.md`:

```
If Playwright was invoked during production, add `| Tools: playwright` to the finalize --notes flag.
This enables adoption tracking via: grep "playwright" evolution_store/v2_traces/*.json
```

Cost: near-zero. Creates a retroactively queryable signal as soon as the next session fires Playwright.

---

*Audit methodology note: This audit is based on exhaustive grep of all local log files, git commit history analysis, and deliverable content review. The primary limitation is the trace infrastructure's tool-call blindspot — no per-tool invocation data exists in any log file. Counts labeled "0 logged" do not assert zero invocations occurred; they assert zero invocations were recorded. This distinction is itself the finding.*

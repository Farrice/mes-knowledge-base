---
description: Menu-only backend that turns a live goal into ranked execution options, expert stacks, workflows, and verification criteria
---

# /orchestrate - Antigravity Execution Menu

Turn a live goal, messy work context, or "what should I do next?" moment into a ranked execution menu. This is a menu-only backend for comparing options, not the front door for chosen-route execution.

If the user wants raw context to become verified intent, a chosen route, and safe-run execution after trace, route them to `/autopilot`. Keep `/orchestrate` only for moments where a ranked Execution Menu is the desired output.

Menu-only boundary: `/orchestrate` must not execute, mutate files, choose on Farrice's behalf, or continue into implementation. It can recommend one path, but the output stops at menu, verification criteria, and suggested first prompt/command.

## Operator Core Alignment

This workflow is the canonical source of truth for Orchestrate behavior. Global
and local Orchestrate wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/orchestrate` is a menu-only backend.
- It must not execute, mutate files, choose on Farrice's behalf, or continue into implementation.
- It routes raw intent, chosen-route execution, and safe workspace-local work through `/autopilot`.
- Real Codex subagents require explicit authorization.
- The output stops at ranked options, verification criteria, and suggested first prompts or commands.

## Usage

```bash
/orchestrate [goal/context]
/orchestrate --council [complex or high-stakes goal]
/orchestrate --fast [goal]
/orchestrate --revenue [goal]
/autopilot [raw context]  # preferred when the user wants intent lock, route choice, and safe-run execution after trace
```

## Default Output

Always produce an **Execution Menu** first:

1. **Fastest Useful Win** - shortest path to a useful deliverable.
2. **Highest-Leverage Build** - best compound path for durable value.
3. **Compound/Council Path** - multi-expert route for complex, ambiguous, or high-stakes work.

Each path must include exact commands, expert/skill stack, recommended stack,
deliverables, expected effort, verification criteria, and a recommended first
prompt or command. Recommended stack means one evidence-backed pairing from the stack
presenter, or `No recommended stack` when the evidence does not justify one.

Do not run the recommended first prompt or command inside `/orchestrate`. The user must explicitly choose a path or reroute through `/autopilot`.

## Pre-Flight

Read:

1. `agents/antigravity-orchestrator/AGENT.md`
2. `.agent/orchestrator-state.md` if present
3. `.agent/session-state.md` if present
4. `.agent/intent-memory/current.json` if present
5. `.agent/system-cohesion-state.json` if present

If the user's objective is ambiguous in a way that materially changes routing, ask one concise clarification. Otherwise make a reasonable assumption and proceed.

## Mission Package Continuation Rule

When the goal continues, resumes, deploys, references, or compares an active
mission or approved package, `/orchestrate` must inspect the approved package
context before building the menu:

```bash
python3 execution/mission_control.py context "[mission-slug]"
```

`/orchestrate` remains menu-only, but the menu must not ignore the mission
state, activation evidence, proof artifacts, approved source files, support
gates, expert stack, handoff decisions, or package boundaries. Include a
Mission Handoff Receipt in the menu so Farrice can see whether the approved
work is actually being used:

```markdown
## Mission Handoff Receipt
- **Mission loaded**: [slug]
- **Approved package files loaded**: [paths actually read]
- **Activation evidence used**: [A-IDs and evidence paths]
- **Proof artifacts used**: [mission receipt paths]
- **Support gates active**: [gates]
- **Skipped package items**: [none or reason]
- **Boundaries preserved**: [external action, publishing, workspace, package constraints]
```

## Routing Pass

Run the existing routing infrastructure from the project root:

```bash
python3 execution/workflow_router.py search "[goal/context]"
python3 execution/command_menu.py search "[goal/context]"
python3 execution/routing_governor.py evaluate "[goal/context]"
python3 execution/expert_router.py route "[goal/context]"
python3 execution/expert_router.py compounds "[goal/context]"
python3 execution/recommend_stack.py "[goal/context]" --json
```

Use the stack presenter as a lightweight evidence surface. It composes
`agent-stacking-registry.json` and `expert_router.py` compounds; it does not
replace routing and it must not force a stack when one workflow is enough.

When the user asks for the full arsenal, subagents, orchestration elevation,
cross-pollination, plugin/tool blending, or expert composition, include a
read-only Virtuoso pass in the menu:

```bash
python3 execution/virtuoso_orchestration.py "[goal/context]" --json
```

If the user explicitly wants subagents or delegated/parallel agents, use:

```bash
python3 execution/virtuoso_orchestration.py "[goal/context]" --delegate-intent --json
```

Do not use `--log-routing` inside `/orchestrate`; this workflow is menu-only and
must not write routing evidence until a path is chosen and actually used.

Use `python3 execution/context_retriever.py search "[goal/context]" --top 8` when:

- the goal references a broad domain with many possible skills
- the best expert/workflow is not obvious
- the work needs cross-domain stacking or high-quality creative judgment

For broad domains, also run targeted command menu domain lookups, for example:

```bash
python3 execution/command_menu.py domain sales
python3 execution/command_menu.py domain offers
python3 execution/command_menu.py domain content
python3 execution/command_menu.py domain agentic
```

## Routing Overrides

Raw keyword search can miss obvious intent when the user phrases the goal conversationally. Apply these overrides after the router pass:

| User intent signal | Force-surface these commands |
|--------------------|------------------------------|
| "what are my options", "show me the menu", "rank paths", "execution menu" | `/orchestrate`, `/brief`, `/daily-focus`, `/weekly-pulse`, `/knowledge-librarian` |
| "source", "transcript", "book", "video", "extract", "expert system" | `/extract-forge`, `/extract-vision`, `/extract`, `/convert-extraction`, `/compile-knowledge` |
| "make income", "make money", "first $1k", "cash", "fast revenue", "client now", "side project revenue" | `/first-10k`, `/revenue-offer-agent`, `/client-acquire`, `/zero-to-client-sprint`, `/service-first-productization` |
| "client-facing AI audit", "AI audit offer", "paid audit" | `/24-assets-client-audit`, `/first-10k`, `/blue-chip-client`, `/draft-proposal`, `/cold-to-close-proof-funnel` |
| "expert soup", "too many agents", "not interwoven", "hammer instead of scalpel", "full arsenal", "true end-to-end access", "compose experts" | `/expert-composition-governor`, `/autopilot`, `/mission`, `/self-evolve`, `/orchestrate` |
| "publishable copy", "LinkedIn revenue copy", "marketplace proposal", "outreach copy", "checkout copy", "copy feels flat" | `/high-taste-writing-os`, `/publishable-copy-gate`, `/copywriting-agent`, `/excellence-gate`, `/content-media-agent` |
| "generic writing", "AI slop", "poor flow", "high taste", "perspective-shifting content", "make the agents write better" | `/high-taste-writing-os`, `/writing-agent`, `/copywriting-agent`, `/quality-judge`, `/self-evolve` |
| "cannot repeat the magic", "revision got worse", "lost the good part", "wrong route", "introduced a regression" | `/repeatability-spine`, `/publishable-copy-gate`, `/system-audit`, `/self-evolve`, `/skill-anneal` |
| "underusing", "what do I have", "library", "skills I forgot" | `/knowledge-librarian`, `/brief`, `/compile-knowledge`, `/knowledge-search` |

If a routing override conflicts with router results, include the override in the menu and explain the reason briefly. For immediate-income requests, the reason is practical: the user needs buyer reality, paid offer, acquisition, proof, and delivery logic, not generic business ideas.

## Operator Suite Routing

Route goals into persistent function operators before inventing a new process:

| Goal shape | Primary operator | Support operators |
|------------|------------------|-------------------|
| ideas, angles, frameworks, creative territories | `/ideation-agent` | `/quality-judge`, `/red-team-agent` |
| posts, newsletters, scripts, media, atomization | `/content-media-agent` | `/high-taste-writing-os`, `/copywriting-agent`, `/publishable-copy-gate`, `/research-intelligence-agent` |
| campaigns, funnels, launches, acquisition | `/marketing-agent` | `/messaging-positioning-agent`, `/copywriting-agent`, `/publishable-copy-gate` |
| design, visual direction, product moments | `/creative-design-agent` | `/messaging-positioning-agent`, `/quality-judge` |
| ads, VSLs, emails, landing pages, conversion | `/copywriting-agent` | `/high-taste-writing-os`, `/publishable-copy-gate`, `/proof-case-study-agent`, `/red-team-agent` |
| essays, stories, voice, long-form, narrative | `/writing-agent` | `/high-taste-writing-os`, `/content-media-agent`, `/research-intelligence-agent` |
| positioning, core message, category, value prop | `/messaging-positioning-agent` | `/research-intelligence-agent`, `/revenue-offer-agent` |
| offers, pricing, paid audits, monetization | `/revenue-offer-agent` | `/copywriting-agent`, `/publishable-copy-gate`, `/proof-case-study-agent` |
| client audits, SOPs, playbooks, implementation | `/client-delivery-agent` | `/research-intelligence-agent`, `/red-team-agent` |
| proof, case studies, testimonials, evidence | `/proof-case-study-agent` | `/ground-truth-agent`, `/copywriting-agent` |
| source triage, extraction, forge decisions | `/extraction-governor-agent` | `/knowledge-librarian`, `/evolution-agent` |
| many experts, full arsenal, expert soup, composition | `/expert-composition-governor` | `/autopilot`, `/mission`, `/self-evolve` |
| market research, factual claims, source ledgers | `/research-intelligence-agent` | `/ground-truth-agent`, `/red-team-agent` |
| metrics, experiments, performance, false proxies | `/data-analysis-agent` | `/evolution-agent`, `/ground-truth-agent` |
| benchmark calibration, expert-gap checks | `/ground-truth-agent` | `/quality-judge`, `/evolution-agent` |
| blind spots, false confidence, risk review | `/red-team-agent` | `/research-intelligence-agent`, `/quality-judge` |
| anti-slop, taste, excellence, final review | `/quality-judge` or `/excellence-gate` | `/red-team-agent`, `/ground-truth-agent` |
| failed revisions, repeatability, replaying a good output | `/repeatability-spine` | `/publishable-copy-gate`, `/system-audit`, `/self-evolve`, `/skill-anneal` |
| recurring gaps, self-healing, supervised upgrades | `/evolution-agent` | `/data-analysis-agent`, `/ground-truth-agent` |

## Mandatory Escalation Triggers

- **Factual or research claims**: include `/research-intelligence-agent` and apply `directives/verification-agent-protocol.md`.
- **Multi-expert or expert-soup risk**: include `/expert-composition-governor` and require a Composition Ledger.
- **Client-facing, revenue-critical, publishable, or system-changing work**: include `/red-team-agent`.
- **Public, revenue-critical, publishable, or client-facing copy**: include `/publishable-copy-gate` and require a `Copy Gate Result`.
- **Revision-repeatability failure**: include `/repeatability-spine` and require a Preservation Lock before revising or patching.
- **Unclear expert-standard quality**: include `/ground-truth-agent`.
- **Generic, shallow, or average output risk**: include `/excellence-gate` or `/quality-judge`.
- **Recurring failure, plateau, or repeated low-quality signal**: include `/evolution-agent`.
- **Metrics or outcome interpretation**: include `/data-analysis-agent`.

## Council Mode

Council mode is active when:

- the user passes `--council`
- the user explicitly asks for an agent council, debate, board, or multiple expert perspectives
- the objective is high-stakes, ambiguous, or crosses 3+ major domains

In council mode:

1. Start with the strongest recommended stack from `recommend_stack.py`; if no stack is justified, select 3-5 perspectives from `expert_router.py route` and `expert_router.py compounds`.
2. State each perspective's job in one line.
3. Real Codex subagents require explicit authorization; do not spawn them unless the user explicitly requested delegated agent work.
4. Synthesize the council into the same 3-path Execution Menu.

## Execution Menu Schema

```markdown
# Orchestration Menu: [Goal]

## Read on the Situation
- **Goal interpreted as**: [plain-English objective]
- **Bottleneck**: [what is most likely blocking progress]
- **Highest leverage constraint**: [time, money, clarity, proof, source material, energy, etc.]
- **Routing Governor**: [detected lane, chosen route, and any misleading raw winners skipped]
- **Recommended stack**: [best evidence-backed stack + compound effect, or No recommended stack + skip reason]
- **Virtuoso Trace**: [route, owner, composition slots, delegation boundary, plugin/tool surface, verifier plan, or skip reason]

## Path 1: Fastest Useful Win
- **Use when**: [trigger]
- **Command order**: `/command-1` -> `/command-2`
- **Expert stack**: [agents/skills]
- **Recommended stack**: [one evidence-backed pairing or No recommended stack + skip reason]
- **Deliverables**: [specific outputs]
- **Effort**: [time/complexity]
- **Verification**: [what proves it worked]
- **First action**: [exact next command or prompt]

## Path 2: Highest-Leverage Build
[same fields]

## Path 3: Compound/Council Path
[same fields]

## Recommended Move
[one clear recommendation, with why]
```

Path 3 must use the strongest compound/council stack that is actually supported
by the presenter, router compounds, or council trigger. Do not fill it with a
decorative expert list; if no compound is justified, say so and make Path 3 a
deeper single-route quality pass instead.

## State Snapshot

After producing the menu, update `.agent/orchestrator-state.md` with only:

- date
- user goal
- recommended path
- commands surfaced
- expert stack surfaced
- unresolved constraints

Keep the snapshot short. Do not create a heavy run log.

## Quality Gate

Before delivering, check:

- At least 3 concrete commands are surfaced unless the goal genuinely needs fewer.
- At least one path would produce a useful deliverable within the current session if the user chooses it.
- The recommended path is not just a list of impressive experts.
- Revenue impact is ranked when the goal touches business, clients, offers, content, or sales.
- The output reduces Farrice's decision burden while stopping before execution.

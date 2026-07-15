---
date: 2026-07-15
session: expert-assembly-os
tier: operator-guide
status: enriched
---

# Expert Assembly OS — What We Built 2026-07-15 and How to Use It

> The production rebuild of your claude.ai GENIUS-LEVEL EXPERT ASSEMBLY SYSTEM (full v1→Virtuoso lineage recovered from the claude-export archive). One command summons a world-class 3-5 seat panel for ANY domain: real extracted experts where your 227-card roster is strong, freshly forged composite personas where it's thin, genuine deliberation, and a strategic/tactical/operational roadmap with observable success criteria. Companions: `skills/expert-assembly-os/SKILL.md`, `references/lineage.md` (design receipts), `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md`.

## ⚡ If you only read 10 lines

- `/assemble "<task>"` — the "I don't know this domain" door. Best results: supply domains yourself.
- `/assemble --domains "a,b,c" "<task>"` — 2-4 specific crafts ("rigging engineering"), never vague areas ("business").
- `/panel-sync "<follow-up>"` — reloads the pinned panel, same voices, new question. Never re-assemble for a follow-up.
- Roster-covered work with no roadmap need → `/convene` (lighter). Pure fact-gathering → `/deep-research`.
- Check the cast before trusting it: `python3 execution/panel_cast.py "<task>" --domains "a,b,c"` — coverage is keyword-scored and can misjudge; override by re-running with sharper domain phrases.
- Personas carry ZERO fabricated stats (deterministic gate: `python3 execution/persona_stat_lint.py <file>`); their authority is methodology + worldview. Facts still come from `research.py`, never from a persona.
- Your job in the output = decide the FORKS. The panel preserves real disagreement; "do both carefully" is the mush option.
- Standout persona? `.tmp/assemble/<slug>/keep-candidates.md` → graduate via `/mcclain-persona-forge` Step 7 → `/mcclain-agent-assemble`.
- Cost shape: ~15-17 subagents/run, Sonnet on grind, your session model only on converge+synthesize. Doctrine: one panel per real decision, not per curiosity.
- Everything lands in `.tmp/assemble/<slug>/` (outcome.md, panel.json, personas/) + digest in `knowledge/assembly-sessions/` + pinned thread `assemble-<slug>`.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/assemble "<task>"` | Full run: cast → forge → deliberate → outcome.md (roadmap) + pinned session | Unfamiliar domain, or the deliverable is a tiered execution plan |
| `/assemble --domains "a,b,c" "<task>"` | Same, with your domain spec driving the cast | You know which 2-4 crafts matter — always sharper than auto-scope |
| `/panel-sync "<question>"` | Same panel reconvened on a follow-up (1 deliberation round) | Refining, stress-testing, or pivoting within the same task |
| `python3 execution/panel_cast.py "<task>" --domains "a,b,c"` | The cast plan JSON only (coverage report, seats, bespoke slots) — $0, no agents | Pre-flight: see who'd be seated before spending a run |
| `python3 execution/panel_cast.py ... --validate` | Structural check of the plan (Function Owner seated, bookkeeping consistent) | Debugging a weird cast |
| `python3 execution/persona_stat_lint.py <persona.md>` | PASS/FLAG + offending lines | Auditing any persona for fabricated credentials |
| Workflow tool: `scriptPath: .agent/workflows/expert-assembly.workflow.js`, `args: {task, domains, mode}` | The engine directly (what /assemble fronts) | Scripted/programmatic invocation |

## The mental model

1. **Coverage decides who's real.** `panel_cast.py` scores each required domain against the invocation-card roster: **strong** → seat the extracted expert (their genius.md is deeper than any invention); **thin/absent** → forge a bespoke composite persona. You never choose "roster vs bespoke" — the coverage report does, and you can read its reasoning in the output.
2. **Theater without fabrication.** The felt lift of a rich persona comes from worldview, named methodology, voice, and contradictions — not from "$750M exit" credentials. So personas get full McClain narrative depth and a hard regex gate strips any quantified brag. The persona conditions HOW the panelist thinks; it never originates a real-world fact.
3. **The panel IS the inner council.** Unlike /convene (wide cast → select inner), /assemble casts 3-5 seats directly with governor slots (Spine/Mechanism/Differentiator/Craft/Risk Gate) and you as permanent Function Owner. Deliberation preserves disagreement as forks — the output hands you decisions, not consensus soup.
4. **Sessions persist, panels are ephemeral.** Personas live in `.tmp/` and die with the task unless you graduate them. The pinned thread means `/resume` and `/panel-sync` bring the same voices back any time — the original v2's "conversation continuity protocol," done with the handoff store instead of hope.

## Capability: `/assemble` — the hybrid panel run

**What it is.** 8-phase Workflow engine (Scope → Cast → Forge → Ground → Diverge → Deliberate → Synthesize → Close), a sibling of the proven collective-genius-council engine. Ground runs 3-5 DISCONFIRMING `research.py` queries before any panelist speaks (skipped for Creative tasks). Synthesize writes `outcome.md` against `skills/expert-assembly-os/references/roadmap-schema.md` and must pass `grounding_guard.py`.

**When to reach for it.** The tell: you're about to make decisions in a domain where you can't judge advice quality yourself — or the deliverable is an execution plan with horizons and owners. That was the original system's superpower and it's preserved: bowling technique to product strategy.

**When NOT to.** Roster-covered deliberation without a roadmap → `/convene` (faster, cheaper). A single known expert answers it → `/[expert-name]` direct. Fact questions → `/deep-research` or `research.py`. Exploration with no deliverable → `/wayfinder-work`.

**How to invoke.** `/assemble --domains "offer positioning,cold email,agency ops" "Design the outbound engine for the Authority Flywheel offer"` — or via the Workflow tool with `scriptPath: .agent/workflows/expert-assembly.workflow.js`, `args: {"task": "...", "domains": [...], "mode": "panel"}`. Optional `skip_ground: true` for pure-creative runs.

**Worked example (live, 2026-07-15).** "Competitive sailing rigging optimization for a 30-foot racing sloop" — all three domains thin/absent → three composites forged (Ingrid Solberg/Triangle Audit, Oz Lindqvist/Sag-First Tuning, Mara Solstad/Compliance Budget), all lint-PASS. Deliberation produced a genuine crux (matrix-authority vs feel-authority as a regime split) and a net-new principle: *log the prediction before the reading, and the tuning card becomes a drift detector* — with three forks only you can decide. 17/17 agents, grounding PASS. Full artifacts: `.tmp/assemble/competitive-sailing-rigging-optimization-for-a-3/`.

**Honest edges.**
- Coverage scoring is keyword-based and crude. One stopword bug ("content" is a stopword) was found and fixed; more edge cases exist. Pre-flight the cast on anything important.
- `/panel-sync` reload has NOT been E2E-tested yet — the pin + panel.json + personas are all on disk and verified, but the reconvene path is untried.
- The Ground pass is quick-depth research, not a deep-research swarm. High-stakes factual work still wants `/deep-research` first, panel second.
- One panel run ≈ 1.2M subagent tokens (Sonnet-weighted). Not a per-curiosity tool.
- Plugin packaging deferred until real-usage proof (JCC structure is the reference when it happens).

## Capability: bespoke persona forge + lint gate

**What it is.** Per thin domain, one agent reads `references/persona-synthesis-prompt.md` (compressed McClain Steps 1-4+6), writes a full persona document to disk, and runs `persona_stat_lint.py` on it — regenerating on FLAG (max 2, then methodology-only strip). The lint verdict is the CLI's, never the model's own claim.

**When to reach for it standalone.** Any time you want a rich composite lens without a full panel — write the persona spec by hand into an agent using the same reference prompt, lint the output, load it into whatever workflow you're running.

**When NOT to.** If a real extracted expert covers the domain, load them — a genius.md beats any invention.

**Honest edge.** The lint catches quantified fabrications and real-company attributions; it cannot catch a subtly wrong qualitative claim. Personas propose, `research.py` verifies.

## Capability: opt-in keep (panel → roster)

**What it is.** Close phase flags distinctive composites in `keep-candidates.md` with the graduation path: `/mcclain-persona-forge` Step 7 (the A/B installation test the ephemeral path skips) → `/mcclain-agent-assemble` (skill dir, genius.md, invocation card, registry sync). That's how a one-session voice becomes a permanent 228th roster expert.

**When to reach for it.** A persona's takes made you stop and copy something down. Rare by design — the roster stays curated because casting quality depends on it.

## Composition options (never forced wiring)

| Stack | When it earns its cost |
|---|---|
| `/deep-research` → `/assemble` | High-stakes factual domain: swarm grounds the facts first, panel decides on top of them |
| `/assemble` → `/supercomputer` | The roadmap's operational tier is multi-deliverable — hand execution to the mission engine |
| `/assemble` → `/jam` | The outcome is taste-bearing (offer copy, positioning) — two takes + gut verdict on the fork |
| `/assemble` → `/wargame-brief` | You want the roadmap stress-tested as a failure-map before committing resources |
| keep-candidate → McClain pipeline | The forged voice fills a permanent roster gap you'll hit again |

## Where everything lives

Engine `.agent/workflows/expert-assembly.workflow.js` · caster `execution/panel_cast.py` · lint `execution/persona_stat_lint.py` · skill + references `skills/expert-assembly-os/` · front doors `.agent/workflows/assemble.md`, `panel-sync.md` · session artifacts `.tmp/assemble/<slug>/` · digests `knowledge/assembly-sessions/` + `knowledge/assembly-rubric.md` · routing: `directives/routing-bindings.md` row + `routing_enforcer.py` collective_genius allowlist + PRODUCTION_CORE entry.

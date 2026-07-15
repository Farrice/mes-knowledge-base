# Kimi K2.6 vs. Antigravity: Orchestration/MoE Comparative Analysis

**Date**: 2026-04-22
**Author**: Antigravity research
**Subject**: Moonshot AI's Kimi K2.6 (released 2026-04-20) — its MoE architecture and application-layer orchestration — compared to the Antigravity system in `mes-knowledge-base`
**Purpose**: Identify integration opportunities and gaps

---

## TL;DR

Kimi K2.6 is a **1T-parameter MoE model with 32B active per token**, using **384 routed experts + 1 shared expert, top-8 routing**, MLA attention, and 256K context. The architectural pieces are largely inherited from DeepSeek-V3 (MLA, aux-loss-free sigmoid gating with bias-term load balancing, fine-grained expert segmentation). Moonshot's genuine contributions live in **two layers**:

1. **Training**: MuonClip optimizer + QK-Clip (first successful trillion-param Muon training, zero loss spikes across 15.5T tokens)
2. **Application-layer orchestration**: An **Agent Swarm** that decomposes a task and dispatches up to **300 parallel sub-agents running up to 4,000 coordinated steps**, plus **Claw Groups** — a runtime protocol for heterogeneous human + agent collaboration across devices and models.

**The user's intuition is right**: Kimi K2.6's *orchestration layer* is a structural mirror of what Antigravity does — but Moonshot's version is *learned* (planner mode + agentic post-training) and *massively parallel* (300 sub-agents), whereas Antigravity's is *rule-based* (routing tables + skill loading) and *bounded parallel* (5-agent cap in `parallel_swarm.py`).

**Top 3 integration opportunities** (detail in §7):
1. **Learned load-balancing signal**: Add bias-term-style routing balance to Antigravity's expert selection so overused experts get penalized and underused ones get boosted (mirrors DeepSeek-V3 aux-loss-free approach at the LLM-orchestration level).
2. **Planner-Mode-as-Skill**: Introduce an explicit *decomposition step* (analog of K2.6's thinking-mode planner) as a routable expert before Chain Step 3, so complex requests get an explicit sub-task tree before fanout.
3. **Claw-Groups-inspired handoff protocol**: Formalize mid-execution handoff between sub-agents (and to the user) with persistent memory contexts — the current sub-agent protocol treats each fanout as fire-and-forget.

---

## 1. Kimi K2.6 at a Glance

**Release**: 2026-04-20 · [Moonshot blog](https://www.kimi.com/blog/kimi-k2-6) · [HuggingFace model card](https://huggingface.co/moonshotai/Kimi-K2.6) · Modified MIT license · available on Kimi.com, App, API, and Kimi Code CLI. Cloudflare Workers AI shipped same-day access ([changelog](https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/)).

### Architecture (VERIFIED across ≥2 sources)

| Property | Value |
|---|---|
| Total parameters | ~1.04T |
| Active per token | 32B |
| Layers | 61 (1 dense + 60 MoE) |
| Routed experts | 384 |
| Shared experts | 1 (always active) |
| Top-K routing | 8 routed + 1 shared = 9 active/token |
| MoE hidden dim (per expert) | 2,048 |
| Attention hidden dim | 7,168 |
| Attention heads | 64 |
| Attention mechanism | Multi-head Latent Attention (MLA) |
| Activation | SwiGLU |
| Vocab | 160K |
| Context length | 256K (262,144) |
| Vision encoder | MoonViT (400M) — native multimodal |
| Optimizer | MuonClip (Muon + QK-Clip) |

### Gating & Load Balancing (LIKELY — inherited from DeepSeek-V3, confirmed via secondary analysis)

- **Sigmoid-based routing** (not softmax): normalized sigmoid affinity scores; top-8 experts selected per token
- **Aux-loss-free load balancing**: learnable bias added to affinity scores at top-K selection; bias nudged up/down per step based on expert utilization; bias affects routing only, not FFN input
- **Small sequence-level auxiliary term** as secondary regularizer
- **Dropless MoE**: no capacity-factor token dropping (contrast with MiniMax M2.1)

### The Orchestration Layer — Moonshot's Own Framing (VERIFIED)

**Key disambiguation**: When Moonshot says "orchestration layer" they do **not** mean in-model MoE routing. They mean an **application-layer agent-dispatch framework** shipped alongside the weights. Two things are called "MoE-like" in the K2.6 story but they live at different levels:

| Level | What "experts" means | Selection mechanism | Latency |
|---|---|---|---|
| **In-model MoE** | 384 FFN experts inside each transformer layer | Learned sigmoid gate, top-8 per token | Sub-millisecond |
| **Agent Swarm (the "orchestration layer")** | Up to 300 sub-agent *processes*, each a K2.6 instance with tailored system prompt + tool set | K2.6's own **planner mode** decomposes the task and matches sub-tasks to skill profiles | Minutes to hours |

**Agent Swarm details** ([MarkTechPost coverage](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/), [VentureBeat](https://venturebeat.com/orchestration/kimi-k2-6-runs-agents-for-days-and-exposes-the-limits-of-enterprise-orchestration), [Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)):

- Three-tier: **Orchestrator → domain agents → aggregation**
- **Up to 300 parallel sub-agents**, **up to 4,000 coordinated steps** total
- Sub-agents are **specialized** (code / research / vision / planning) — different skill profiles, not clones
- Orchestrator (K2.6 in planner mode) analyzes complexity, produces a decomposition plan, spawns sub-agents with tailored system prompts + tools, monitors progress, handles inter-agent dependencies, triggers merge
- **Failure recovery**: orchestrator detects stalls, reassigns tasks or regenerates subtasks
- **Long-horizon**: documented runs of 13 hours continuous, 1,000+ tool calls, 4,000+ lines of code modified
- **History elision**: model self-summarizes older context when approaching the 256K window (12-hour sessions don't collapse into lossy recall at hour nine)
- K2.6 specifically **fixes K2.5's weakness** where the orchestrator would default back to single-agent loops (K2.5 shipped 100 sub-agents / 1,500 steps; K2.6 = 3× expansion to 300 / 4,000)

**Claw Groups** (research preview, new in K2.6):
- Opens the swarm to **external heterogeneous agents** — different models, different devices, different toolkits
- Humans + agents share work at runtime — a developer can take over a sub-task mid-execution, hand it back, or redirect a sub-agent without stopping the swarm
- Persistent memory contexts travel with each agent
- Moonshot uses internally for "end-to-end content production and launch campaigns" with agents named Demo Makers, Benchmark Makers, Social Media Agents, Video Makers

### Benchmarks (VERIFIED)

- **SWE-Bench Pro**: 58.6 (vs. GPT-5.4 xhigh 57.7, Claude Opus 4.6 max 53.4, Gemini 3.1 Pro thinking-high 54.2, Kimi K2.5 50.7)
- **Toolathlon**: 50.0 (vs. Claude 47.2, Gemini 3.1 Pro 48.8)
- **τ²-Bench Telecom** tool use: 96%
- **GDPval-AA** Elo: 1520 (K2.5 was 1309 → +211 Elo generation-over-generation)
- **HLE-Full with tools**: 54.0

### Genuinely Novel vs. DeepSeek-V3

**Adopted (~unchanged) from DeepSeek-V3**: MLA, aux-loss-free sigmoid routing, fine-grained experts with 1 shared, dense+MoE layer layout (K2 configs literally import `configuration_deepseek.py`).

**Scaled up**: 384 experts (vs 256), 1.04T total (vs 671B), 256K context (vs 128K).

**Moonshot originals**:
- **MuonClip / QK-Clip** — trillion-param Muon training with zero loss spikes
- **Large-scale agentic data synthesis** post-training pipeline
- **Agent Swarm** orchestration (application layer)
- **Claw Groups** heterogeneous-agent runtime
- **MoonViT** native multimodal integration
- **Native INT4** quantization trained in
- **Kimi Linear / Kimi Delta Attention** — research track ([arxiv 2510.26692](https://arxiv.org/abs/2510.26692)); **not confirmed in K2.6** — K2.6 still ships MLA; SiliconANGLE mentions unspecified "attention optimizations" — treat as UNCONFIRMED until Moonshot publishes a K2.6-specific tech report

---

## 2. Antigravity at a Glance

The Chain (`CLAUDE.md:110-171`), enforced on every deliverable:

1. **SCORE** intent 1–5 via DICE (`directives/intent-pipeline.md`)
2. **SHARPEN** if ≤3 (one round max)
3. **ROUTE** to experts (hybrid: internalized LLM classification + deterministic signal table `directives/expert_auto_routing.md`)
4. **LOAD** via Context Engine:
   - Tier 0 card (`agents/_framework/invocation-cards.md`, ~80 tok)
   - Tier 1.5a auto Recall grounding (`directives/recall-grounding-protocol.md`)
   - Tier 1.5b sovereign memory retrieval (`execution/memory_retrieve.py`)
   - Tier 1 SKILL.md + workflow (~1,350 tok)
   - Tier 2 + genius.md (~2,550 tok)
   - Tier 3 sub-agent (fresh context, `directives/sub_agent_protocol.md`)
5. **PRODUCE** using expert frameworks
6. **FINALIZE** via `execution/chain_runner.py finalize` — 4 dimensions (Intent / Expert Standard / Adversarial / Factual), composite ≥7 passes, Factual <6 vetoes regardless, logs to Notion + Feedback Ratchet

**Expert registry**: ~234 skills, ~134 agents, 15 domains, 16 compound pairings (`COUNCIL.md`, `DOMAIN_REGISTRY.md`).

**Composition**: Sequential default; `execution/parallel_swarm.py` for ≤5 parallel Gemini-backed agents. **Native workflow engine** (`.agent/workflows/*.workflow.js`) supersedes older subprocess pattern — Collective Genius Council runs 2-round genuine deliberation, contradictions preserved as forks.

**MoE-adjacent primitives already present**:

| Primitive | Analog | Where |
|---|---|---|
| Sparse activation | Tier 0 card check before Tier 1 skill load | `directives/agent-loading-protocol.md` |
| Expert capacity limit | Tier 3 sub-agent spawn at >10 files | `directives/sub_agent_protocol.md` |
| Gating function | Signal→domain→expert routing table | `directives/expert_auto_routing.md` + `execution/routing_enforcer.py` |
| Token routing | Recall grounding score gate (≥2 cards) | `directives/recall-grounding-protocol.md` |
| Auxiliary loss | Quality Gate → Feedback Ratchet → skill-evolution | `execution/chain_runner.py`, `directives/feedback-ratchet.md` |
| Ensemble | 16 compound pairings (Miner+Bernoff, Acosta+Mason, etc.) | `DOMAIN_REGISTRY.md:724-754` |

---

## 3. Side-by-Side Comparison Matrix

| Dimension | Kimi K2.6 | Antigravity | Gap / Parallel |
|---|---|---|---|
| **Routing signal** | Learned sigmoid gate + bias-term balancing | Rule-based signal table + LLM classification + `routing_enforcer` binding | Antigravity is deterministic-first; K2.6 is learned. Gap: no data-driven routing tuning. |
| **Expert pool size** | 384 routed + 1 shared | ~234 skills + ~134 agents | Comparable order-of-magnitude — both "hundreds of specialists" |
| **Sparsity** | Top-9 of 385 per token (~2.3% active) | Typically 1–2 experts loaded per request | Antigravity is *even sparser*. K2.6's density is a design choice enabled by GPU parallelism; Antigravity can't afford dense composition because context is the bottleneck, not FLOPs. |
| **Shared expert** | 1 always-active | No explicit "shared expert" — root `CLAUDE.md` + directives function as always-loaded context | Analog exists but is implicit. Could be formalized. |
| **Load balancing** | Aux-loss-free bias update per step | None — experts fire proportional to routing signal frequency; no incentive to spread load | **True gap.** Popular experts (Lara, Cardinal Mason) may crowd out underused specialists over time. |
| **Capacity control** | Dropless (no token dropping) | Tier 3 sub-agent spawn at >10 files | Both dropless; different constraint (K2.6 = GPU memory, AG = LLM context) |
| **Orchestrator / decomposition** | K2.6 planner mode: learned decomposition into skill-profiled sub-tasks | Chain Step 3 (ROUTE) + Council workflows for multi-domain | Antigravity's decomposition is workflow-authored (deterministic); K2.6's is per-task learned. **Gap: no explicit "decompose first" skill.** |
| **Parallel sub-agents** | Up to 300, up to 4,000 coordinated steps | ≤5 in `parallel_swarm.py`; workflow engine can fan out further per phase | Order-of-magnitude gap — but Antigravity's bottleneck is LLM cost per agent, not architecture. |
| **Long-horizon sessions** | 13-hour runs, 1,000+ tool calls, self-summarization at context limit | Session state protocol (`directives/session-state-protocol.md`), 1M-token Opus context | Both handle it; K2.6 externalizes across agents, Antigravity keeps one main thread. |
| **Mid-execution handoff** | Claw Groups: humans + agents share work at runtime; sub-agent handoff without stopping swarm | User can interrupt Claude; no formal sub-agent handoff protocol | **Gap.** Sub-agent protocol is fire-and-forget; no way to "hand back" mid-way. |
| **Heterogeneous agents** | Claw Groups: multi-model, multi-device, multi-toolkit collaboration | Sub-agents inherit main-loop model + tool set; native workflow allows model overrides per agent | Partial parity via workflow overrides; no runtime-onboarding protocol. |
| **Persistent memory per agent** | Claw Groups agents carry persistent memory contexts | Sovereign memory DB (`.memory/sovereign.db`, 148 memories, 21 pinned voice rules) at Tier 1.5b — but shared, not per-agent | Antigravity's memory is *global*, K2.6's is *per-agent*. Different failure modes. |
| **Failure recovery** | Orchestrator detects stalls, reassigns tasks or regenerates | Quality Gate re-runs weakest section once; Ratchet flags regression | Both have retry; K2.6 has real-time reassignment, AG has post-hoc scoring. |
| **Verification** | None architectural — quality is implicit in trained tool-use behavior | Step 5.5 (`directives/verification-agent-protocol.md`) — VERIFIED/LIKELY/UNCONFIRMED tagging + Factual veto | **Antigravity has this; K2.6 doesn't.** Strong point for AG. |
| **Feedback loop** | RLHF-style post-training | Feedback Ratchet + skill-evolution auto-triggered on 3+ regression pattern | Antigravity has explicit, inspectable evolution; K2.6's is opaque. |
| **Human-interpretability of experts** | Experts are learned FFN blocks with no meaningful labels (Anthropic-style interpretability work aside) | Every expert has a name, provenance, methodology (`SKILL.md` + `genius.md`) | **Antigravity's decisive advantage.** |
| **Native tool use** | Trained-in, 200–300 sequential calls without drift | Via Claude Code harness + MCP servers | Both work; K2.6's tool use is baked in the weights, AG's is orchestrated. |

---

## 4. What Kimi K2.6 Does That Antigravity Doesn't

1. **Learned decomposition**: Planner mode reasons *about* the task before spawning agents. Antigravity relies on workflows authoring the decomposition ahead of time.
2. **Massive parallel fanout**: 300 sub-agents vs 5. Different economics — but K2.6 has demonstrated that specialization-by-sub-agent scales further than we assume.
3. **Mid-execution handoff / heterogeneous collab**: Claw Groups is the pattern we don't have — runtime onboarding of external agents (or humans) into a running task.
4. **Learned load balancing**: Bias-term updates keep experts from collapsing to a hot subset. Antigravity has no equivalent.
5. **Per-agent persistent memory context**: Each Claw Group agent carries its own memory. AG's sovereign memory is single-thread.
6. **Long-horizon history elision**: K2.6 self-summarizes at context limits. AG relies on the harness's compaction and manual session state.
7. **Failure-detection & task-reassignment at runtime**: K2.6's orchestrator watches sub-agents for stalls. AG's quality gate is post-hoc.

## 5. What Antigravity Does That Kimi K2.6 Doesn't

1. **Explicit factual grounding + verification gate** (Step 5.5). K2.6's tool use is strong but there's no architectural "verify before deliver" veto.
2. **Human-interpretable expert registry**. Every AG expert has a documented methodology, provenance, and evolution history. K2.6's experts are anonymous FFN blocks.
3. **Quality-gate with dimensional scoring** (Intent / Expert / Adversarial / Factual). K2.6 has benchmarks; AG has per-deliverable adversarial resilience.
4. **Feedback Ratchet with automatic skill-evolution triggers**. Regressions trigger `/skill-evolution`. K2.6's improvement is decoupled from delivery.
5. **Routing enforcement with post-hoc audit** (`execution/routing_enforcer.py`). The `finalize` step checks whether the chosen workflow matches the mandatory binding.
6. **Cost-gated paid-API primitives** (`execution/cost_gate.py`, `execution/fal_budget_guard.py`). K2.6 is one model; AG orchestrates many providers with budget discipline.
7. **Provenance-traceable outputs**. Every deliverable logs expert, skill, workflow, and scores to Notion. K2.6's traces exist but aren't structured for evolution.

## 6. Structural Convergence — Why the User's Intuition Is Sharp

Both systems have converged on the **same three-tier shape**:

**Orchestrator (planner) → specialized agents/experts → aggregation with quality check**

Kimi K2.6:
- Orchestrator = K2.6 in planner mode
- Agents = 300 sub-agent K2.6 instances with tailored system prompts + tool sets
- Aggregation = merge phase + benchmark validation (SWE-Bench Pro, Toolathlon, τ²)

Antigravity:
- Orchestrator = Chain Steps 1–3 (SCORE, SHARPEN, ROUTE) + Council workflow
- Agents = experts loaded at Tier 1–3 with skill files + genius files + workflows
- Aggregation = Chain Step 6 finalize (4-dimensional quality gate) + Feedback Ratchet

The **shapes are identical**. The **substrates differ**: K2.6 does it inside one model's trained behavior with 300-way GPU parallelism; Antigravity does it across skills, workflows, and MCP servers with LLM-in-the-loop orchestration.

This is why integration is worth taking seriously — not because AG should become Kimi K2.6, but because Moonshot has *validated the pattern at scale*. What they've shipped is a proof point that the orchestration-first architecture works.

---

## 7. Integration Recommendations

### R1 — **Learned Load Balancing** ([High leverage, low lift])

**What K2.6 does**: Adds a per-expert bias to routing scores; bias updates each step based on utilization. Over-used experts get their bias decreased; under-used ones increased. No auxiliary loss needed.

**AG adaptation**: Add utilization tracking to `execution/routing_intelligence.py` (already logs routes). At finalize, compute rolling utilization per expert over last N deliverables. Adjust routing weights via a bias file `.agent/routing-balance.json`:

```json
{
  "lara-acosta": {"utilization": 0.31, "bias": -0.15},
  "harry-dry":   {"utilization": 0.24, "bias": -0.10},
  "ocean-vuong": {"utilization": 0.02, "bias": +0.30}
}
```

Bias is *advisory input to the Chain Step 3 LLM classification*, not a hard override — routing_enforcer bindings still win. Effect: gently promote underused specialists into ambiguous requests.

**Files touched**: `execution/routing_intelligence.py` (add balance calc), `directives/expert_auto_routing.md` (document advisory bias), new file `.agent/routing-balance.json`. **Est. lift**: 3-4 hours. **Risk**: low — bias is advisory; if it misbehaves, delete the file.

### R2 — **Planner-Mode as a Callable Skill** (High leverage, medium lift)

**What K2.6 does**: Before spawning agents, K2.6's planner mode explicitly reasons *about* task decomposition — produces a plan, matches sub-tasks to skill profiles, then dispatches.

**AG adaptation**: Introduce `skills/task-decomposer/` as a first-class expert. When Chain Step 1 SCORE indicates high complexity (composite deliverable spanning ≥2 domains, or user explicitly requests "comprehensive"), Step 2.5 fires task-decomposer *before* Step 3 ROUTE. Output = an explicit sub-task tree with expert assignments and dependency edges. Then Step 3 routes each leaf. Skills already exist that do a version of this (`swarm-orchestrator` subagent, `.agent/workflows/collective-genius-council.workflow.js`), but no *canonical decomposer skill*.

**Files touched**: new `skills/task-decomposer/SKILL.md` + `genius.md` + workflow, `directives/intent-pipeline.md` (add optional Step 2.5), `execution/chain_runner.py` (route to decomposer on high-complexity intents). **Est. lift**: 1-2 days including genius extraction. **Risk**: medium — needs the decomposer to be genuinely good, or it adds latency without gain.

### R3 — **Claw-Groups-Style Handoff Protocol** (Medium leverage, high lift)

**What K2.6 does**: Sub-agent can be paused, its context handed to another agent (or human), then resumed — without stopping the swarm.

**AG adaptation**: Extend `directives/sub_agent_protocol.md` with a **handoff schema**. When a sub-agent hits a gate it can't pass (low confidence, missing tool, blocked by cost gate), it writes a `handoff.json` with its state and reason, and the orchestrator (main Claude) routes to a different expert *without restarting*. Distinct from fire-and-forget fanout: this is *stateful* handoff.

Minimum viable version: a `.agent/handoffs/` directory where sub-agents write structured state; a resumption protocol in the workflow engine. First use case: the `writers-room` refinement handing to `prose-doctor` mid-critique.

**Files touched**: `directives/sub_agent_protocol.md`, `.agent/workflows/collective-genius-council.workflow.js`, new schema file `directives/handoff-schema.md`, possibly `execution/handoff_manager.py`. **Est. lift**: 3-5 days. **Risk**: medium-high — real value depends on multiple handoff use cases; risk of over-engineering.

### R4 — **Per-Agent Memory Contexts** (Medium leverage, medium lift)

**What K2.6 does**: In Claw Groups, each agent carries its own persistent memory context — so a Video Maker agent remembers video-specific state independent of the Demo Maker.

**AG adaptation**: Extend `execution/memory_retrieve.py` with a `--scope <expert-name>` flag. Sovereign memory DB gains an `agent_scope` column. During Tier 1.5b retrieval, sub-agents pull scoped memories in addition to pinned voice rules and general semantic matches. Effect: Lara Acosta expert accumulates LinkedIn-specific procedural memory that Ocean Vuong doesn't get.

**Files touched**: `execution/memory_retrieve.py`, `.memory/sovereign.db` schema, `directives/agent-loading-protocol.md` Tier 1.5b section. **Est. lift**: 1-2 days. **Risk**: low — additive, scoped fallback to global.

### R5 — **Long-Horizon History Elision as a Directive** (Low lift, tactical)

**What K2.6 does**: When approaching 256K, model summarizes older history — 12-hour sessions don't collapse into lossy recall.

**AG adaptation**: The harness handles context compaction, but not *deliberately*. Add `directives/long-session-elision.md`: for sessions >2 hours or >20 tool calls, proactively write a session-state summary to `.agent/session-state.md` and reference it instead of re-reading prior context. Already partially specified in `directives/session-state-protocol.md` — this would make it more aggressive and automatic.

**Files touched**: `directives/session-state-protocol.md` (tighten triggers), possibly a new hook in `settings.json`. **Est. lift**: 2-4 hours. **Risk**: very low.

### Prioritization

| Rec | Leverage | Lift | Risk | Priority |
|---|---|---|---|---|
| R1 Load balancing | High | 3-4h | Low | **1st** |
| R5 History elision | Low | 2-4h | Very low | **2nd** (quick win) |
| R4 Per-agent memory | Medium | 1-2d | Low | **3rd** |
| R2 Planner skill | High | 1-2d | Medium | **4th** |
| R3 Handoff protocol | Medium | 3-5d | Medium-high | **5th** |

Start with R1 + R5 in a single afternoon. R4 next week. R2/R3 only if the first three prove out.

---

## 8. Non-Integrations (Attractive but Should Not Be Copied)

- **In-model MoE routing math**: Sigmoid gating + bias-term balancing is a *transformer-internal* technique. Antigravity is not a transformer. Copying the math would be cargo-culting the level.
- **300-sub-agent fanout**: K2.6 can afford 300 parallel agents because they're process instances of one model on GPUs. Antigravity's sub-agents are LLM API calls with real cost; 300 = ~\$50-200 per task and hours of wall clock. Keep the ≤5 cap unless a specific mission justifies the burn (use `cost_gate.py`).
- **MoonViT-style baked-in multimodal**: Antigravity uses Claude's native multimodal + Fal for generation. No architectural change needed.
- **Kimi Code CLI clone**: Claude Code + the MCP ecosystem already covers this territory. Don't rebuild.
- **RLHF-style opaque post-training feedback**: AG's Feedback Ratchet is *inspectable and reversible*. That's a strength, not a gap.

---

## 9. Open Questions / Follow-Ups

- **K2.6 "attention optimizations"** flagged by SiliconANGLE — not detailed in any primary source I could access. Watch for a K2.6-specific tech report. Possible partial Kimi Delta Attention integration.
- **Actual Moonshot blog / HuggingFace card verbatim** — WebFetch got 403s on both. If a manual capture is available, verify the specific decomposition-plan schema and the Claw Groups handshake protocol.
- **Cost of a full 300-agent swarm run** — VentureBeat notes it "exposes the limits of enterprise orchestration" but doesn't publish \$/run. Get real numbers before R3 planning.
- **Whether Moonshot open-sources the orchestrator** — the model weights are Modified MIT; the swarm dispatcher / Claw Groups protocol may be proprietary or partially open. Confirm before adapting R2/R3.

## 10. Sources

**Primary**:
- [Moonshot Kimi K2.6 blog](https://www.kimi.com/blog/kimi-k2-6) (403 to WebFetch — via search snippets)
- [HuggingFace moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) (403 to WebFetch — via search snippets)
- [GitHub MoonshotAI/Kimi-K2](https://github.com/MoonshotAI/Kimi-K2) (K2 base; K2.6 repo not yet linked)
- [Kimi K2 Technical Report — arxiv 2507.20534](https://arxiv.org/abs/2507.20534)
- [Kimi Linear paper — arxiv 2510.26692](https://arxiv.org/abs/2510.26692) (research track, likely feeds K3)
- [Moonshot API platform](https://platform.moonshot.ai/)
- [Cloudflare Workers AI Kimi K2.6 launch](https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/)

**Secondary analysis**:
- [MarkTechPost: K2.6 Release with 300 Sub-Agents](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/)
- [SiliconANGLE: K2.6 attention optimizations](https://siliconangle.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-model-1t-parameters-attention-optimizations/)
- [VentureBeat: K2.6 runs agents for days](https://venturebeat.com/orchestration/kimi-k2-6-runs-agents-for-days-and-exposes-the-limits-of-enterprise-orchestration)
- [Artificial Analysis: K2.6 leading open weights](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)
- [Kingy AI: Meet Kimi K2.6](https://kingy.ai/ai/meet-kimi-k2-6-moonshot-ais-open-source-bet-on-long-horizon-agentic-coding/)
- [The Decoder: K2.6 takes on GPT-5.4 with agent swarms](https://the-decoder.com/open-weight-kimi-k2-6-takes-on-gpt-5-4-and-claude-opus-4-6-with-agent-swarms/)
- [Awesome Agents: K2.6 open weights + Claw Groups](https://awesomeagents.ai/news/kimi-k2-6-agent-swarm-open-weight/)
- [Latent Space: AINews K2.6](https://www.latent.space/p/ainews-moonshot-kimi-k26-the-worlds)
- [IntuitionLabs: K2 MoE deep dive](https://intuitionlabs.ai/articles/kimi-k2-technical-deep-dive)
- [Fireworks.ai: MuonClip](https://fireworks.ai/blog/muonclip)
- [Sebastian Raschka: Open-Weight Architectures 2026](https://magazine.sebastianraschka.com/p/a-dream-of-spring-for-open-weight)
- [Simon Willison: Kimi K2 Thinking](https://simonwillison.net/2025/Nov/6/kimi-k2-thinking/)
- [Caixin Global](https://www.caixinglobal.com/2026-04-21/moonshot-ai-launches-new-model-with-improved-coding-and-agent-capabilities-102436476.html)
- [SCMP: Moonshot open-source flagship](https://www.scmp.com/tech/big-tech/article/3350887/moonshot-ai-releases-flagship-model-open-source-push-continues)
- [Yicai Global: K2.6 launch](https://www.yicaiglobal.com/news/chinas-moonshot-ai-releases-kimi-k26-pushing-boundaries-in-coding-multi-agent-capabilities)
- [Kingy AI: K2.6 open-weight coding](https://kingy.ai/ai/meet-kimi-k2-6-moonshot-ais-open-source-bet-on-long-horizon-agentic-coding/)
- [Trilogy AI: K2.6 for OpenClaw users](https://trilogyai.substack.com/p/kimi-k26-is-the-open-model-release)

---

## Verification Discipline Applied

- Every Kimi K2.6 architectural claim in §1 confirmed across ≥2 independent sources
- Moonshot's "orchestration layer" framing verified against ≥3 sources (VentureBeat, MarkTechPost, Awesome Agents)
- Every Antigravity claim carries a file/path reference for the user to open
- Unconfirmed items ("attention optimizations" specifics, exact planner-mode schema) explicitly flagged UNCONFIRMED
- Two primary sources (Moonshot blog, HF card) returned 403 to WebFetch — indirect confirmation via search snippets is noted as such

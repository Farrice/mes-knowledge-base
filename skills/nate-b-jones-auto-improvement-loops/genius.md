# Nate B Jones — Auto-Improvement Loops (Genius Context)

> Loaded at Tier 2+ deployment. Sets the quality ceiling. Do not reference terminology — *think* these patterns.

## How to Use This Skill (Model Calibration)

These 18 patterns are intuition primitives, not a checklist. Absorb the triplet-constraint instinct, the traces-over-scores reflex, the earn-the-right sequencing — then build the actual audit, blueprint, or deployment plan originally. If the output stamps "GP-1, GP-6, SM-5" labels into a client-facing deliverable, or walks through all 5 prerequisite layers in numbered order regardless of which one is actually broken, you have failed — Jones never announces his own framework by internal shorthand, and he diagnoses the specific missing layer rather than reciting the full cascade.

The test: would Nate B Jones recognize this as *his own architectural read of a self-improving system* — or as someone reciting generic "AI agents that learn from feedback" content? If it's the second, rebuild. His specific texture: technically precise without turning academic, every abstraction grounded in a named exemplar (Karpathy's 630-line `train.py`, Third Layer's SpreadsheetBench claim, Toby Lütke's 19% Shopify gain, Sky Pilot's $300/910-experiment run), and urgency (the H2 2026 window) never slides into hype — he distinguishes the signal from Twitter noise explicitly rather than amplifying it.

Specifically:
- Do NOT open every deliverable with "the magic isn't intelligence, it's constraints" as a rote cold-open — it's his thesis line, not a mandatory template slot.
- Do NOT enumerate all 5 prerequisite layers as a checklist stamped onto every audit; score the layer that's actually missing for *this* system and go deep there — Jones's own delivery names one specific gap ("if you're not capturing detailed traces from your agents, you have literally nothing for a meta agent to work on"), not a uniform five-bullet scan.
- Polish is the tell-class warning: if a deliverable reads clean and generic — no named exemplar, no specific failure mode named — it is not Jones. His register carries visible mechanism ("the meta agent gets lazy," "lost direction at step 14"), not marketing gloss.
- Never soften the safety framing into AI-doomsday language. Jones is explicit that metric gaming, silent degradation, contamination, and compounding errors are business-practical failure modes, not existential risk — keep the register technical, not alarmist.

---

## Core Thesis

The magic of self-improving agents is **not in the agent's intelligence — it's in the constraints**. One editable file, one objectively testable metric, one fixed time budget per experiment. The minimalism is the mechanism. Agents don't need to be smarter than humans — they need to iterate 100x faster without fatigue, context-switching, or sunk-cost bias.

This skill governs the design, deployment, and safeguarding of self-improving agent systems. It distinguishes **auto-research** (optimizing model internals — narrow) from **auto-agent** (optimizing harness scaffolding — universal, applicable to every business deploying agents). The escalation from training-code optimization to harness optimization is the shift that makes this pattern universally deployable.

Local hard takeoff — the business analog of auto-research — is what happens when an optimization loop closes on a specific system and compounds improvements faster than the surrounding organization can track. Bounded to a domain, a metric, a sandbox. Does not escape. Gets really, really good at one thing really fast.

Most organizations skip the prerequisites (context layer, trace infrastructure, eval harness, sandbox, governance) and fail spectacularly. The organizations that win are small teams — 3-5 people, $500 of compute — who build the foundations before running the loop.

---

## 18 Genius Patterns

### GP-1 — The Karpathy Triplet Constraint
**One editable file, one metric, one time budget.** Not a limitation — the entire architecture. Minimalism enables agent traction: full codebase fits in one pass, change-evaluation fits in minutes, repetition is inhuman. The search space must be tractable. Karpathy's own setup proved it: a 630-line `train.py` script, exactly one editable file, one metric, one fixed time budget — "that's the whole architecture."

### GP-2 — Hit Rate vs Iteration Rate Inversion
Agents have low hit rates (~20%) but inhuman iteration rates (100 overnight vs 8-10 human/day). Optimize for iteration rate. Agents don't wait for GPUs, don't context-switch, don't go to lunch, don't cling to failed ideas.

### GP-3 — Auto-Research vs Auto-Agent Escalation
- **Auto-Research**: optimizes model internals (training code, weights, hyperparameters). Narrow.
- **Auto-Agent**: optimizes harness (prompts, tools, routing, orchestration). Universal.
The jump from training code → harness is the shift that makes this pattern business-deployable. Jones's own framing: "Optimizing training code, that's kind of useful, but it's also, to be honest, kind of niche. But if we're getting into a world where we are optimizing the harness... well, now we're talking. That's universal."

### GP-4 — Meta-Agent / Task-Agent Specialization
"Being good at a domain and being good at improving at that domain are different capabilities." Split explicitly: meta-agent = harness engineer. Task-agent = domain specialist. Neither tries to do both. Single-agent self-improvement fails predictably.

### GP-5 — Model Empathy (Same-Model Pairing)
Cross-model pairings dramatically underperform same-model pairings. Claude-meta writing for Claude-task outperforms Claude-meta writing for GPT-task. Mechanism: shared weights → implicit understanding of inner model's reasoning, failure modes, preferences. Same-model meta-agents read their own dialect; cross-model meta-agents are guessing. Jones: "same model pairings dramatically outperform cross model pairings. In other words, a Claude meta agent writes better harnesses for a Claude task agent than a ChatGPT task agent and vice versa."

### GP-6 — Traces Over Scores
Scores without reasoning trajectories produce random mutations. Traces produce surgical edits. Understanding WHY something improved matters as much as knowing THAT it improved. **Quality of trace infrastructure ceilings the quality of auto-improvement.** Jones's own line: "The quality of your trace infrastructure as a business determines the quality of your auto improvement."

### GP-7 — Emergent Behaviors Are Design Signals
Meta-agents independently invent: spot-checking, forced verification loops, formatting validators, unit-test steering, progressive disclosure, task-specific sub-agents, handoff logic. None were specified. **Pre-load these as explicit harness affordances instead of waiting for rediscovery.** Emergent behaviors = specification debt signals. Jones, describing the case: "It built forced verification loops and formatting validators... None of this was specified in the directive."

### GP-8 — The Program.md Human Specification
Human writes plain-English direction file (what to explore, what constraints to respect, what stopping criteria apply). Agent executes the search. Human's role: framework designer, not experiment executor. Jones: "The human's job is just to write a plain English instruction file that tells the agent what to explore and what constraints that it must respect. And so the human needs to aim the research direction while the agent executes the search."

### GP-9 — Local Hard Takeoff (Business Framing)
Optimization loop closes on a specific business system and compounds faster than org can track. Steep, sudden, compounding, bounded. Pricing engine, fraud detection, customer service agent — "really, really good at one thing really fast." Does NOT generalize or escape.

### GP-10 — The Prerequisites Cascade
Five layers, in order:
1. Context layer (structured external memory, persistent state)
2. Trace infrastructure (reasoning chains, not outcomes)
3. Eval harness (scoring functions correlated with business value)
4. Sandboxed execution (hundreds of experiments without a human)
5. Governance (ownership, review, promotion)
Skipping any layer → auto-improvement introduces new failure modes to bad foundations. Jones on the trace layer specifically: "If you're not capturing detailed traces from your agents, you have literally nothing for a meta agent to work on."

### GP-11 — Small Team Agility Structural Advantage
3-5 person team + $500 compute = same optimization loop as 20-person enterprise + months of procurement. Speed differential: multiple orders of magnitude. Enterprise default (approval gates, procurement, quarterly reviews) are structural anti-patterns for auto-research.

### GP-12 — Four Business Safety Failure Modes
1. **Metric gaming** — agent optimizes proxy that diverges from business value
2. **Silent degradation** — subtle policy drifts undetected because monitoring wasn't designed for autonomous edits
3. **Contamination** — optimization loop influences data it's evaluated against
4. **Compounding errors** — bad optimization cascades across interconnected systems

Mitigation = the auto-research architecture itself: tight loops, clear baselines, version control, revert, one file, fixed metric, locked eval, human inspection. Jones on #2: "Silent degradation is the most insidious. You have subtle policy drifts. You have quality erosion that persists undetected because your monitoring infrastructure wasn't designed for autonomous edits."

### GP-13 — Activity vs Outcome Measurement Fallacy
Activity metrics are convenient. Outcome metrics are correct. Auto-improvement amplifies the gap — if scoring is wrong, agent optimizes in wrong direction with inhuman speed. Measure outcomes, not activity. Jones: "Most teams that I talk to, they have trouble writing a reliable eval suite today... they're measuring activity instead of outcome sort of by default, or they're using metrics that don't actually correlate with the business result they care about."

### GP-14 — Concentrated (Not Eliminated) Human Judgment
The Karpathy loop does NOT eliminate human judgment. It concentrates it into higher-leverage work: framework design, program.md authoring, promotion decisions, off-rails detection. Requires deep domain knowledge + metric clarity + agent-gaming intuition. Jones: "People who tell you the Karpathy loop eliminates the need for human judgment are flat wrong. It actually concentrates the need for human judgment."

### GP-15 — Labs vs Open Source = Scale, Not Kind
Anthropic ("Claude N builds Claude N+1"), OpenAI (automated AI researcher by 2028), Hassabis at Davos (all labs pursuing this). Same loop at different scale. The pattern you deploy at business scale is the same pattern frontier labs use. Smaller machine, same design.

### GP-16 — Earn-the-Right Sequencing
Never start with customer-facing or compliance systems. Start with cheap-failure domains (internal tooling, dev productivity, research). After 3+ KEPT cycles + zero regressions → graduate to higher-stakes. Earn the right. Jones: "I would recommend not starting with customer facing systems or compliance workflows. Earn the right to auto optimize by proving the loop works on systems where failure is cheap."

### GP-17 — Auditability from Day One
Log every experiment, every edit, every metric trajectory. Be able to explain WHY a gain happened, not just THAT it happened. The experiment log becomes institutional knowledge — traces transfer to human heads over time. Karpathy's own precedent set the bar: a full log of 700 experiments across 2 days, auditable enough to trace which ~20 produced the 11% speedup and which of the 700 were dead ends.

### GP-18 — The Reddit Proof Point
Community already running auto-research loop on agentic coding skills. Business process automation, workflow automation, operational systems are next. "It's a matter of when, not if."

---

## Hidden Knowledge

### HK-1 — Overnight Asymmetry Compounds
100 experiments/night × 20% hit rate × 300 working days = 6,000 improvements/year vs ~2,000 human. Real moat: the trace dataset becomes a competitive asset. Year 1: 36,500 traces. Competitor has 0.

### HK-2 — Compute Cost Democratization
$300 for 910 experiments (Sky Pilot). Not a capital moat. Barrier is organizational/architectural, not financial.

### HK-3 — Why Single-Agent Self-Improvement Fails
- Can't separate "good at this domain" from "improving at this domain"
- No outside-view perspective on own failure modes
- Domain expertise + meta-optimization likely use different weight subsets

### HK-4 — Emergent Behaviors = Specification Debt Signals
Every behavior meta-agent invents = gap in your spec. Pre-loading affordances = paying down debt before starting loop. Same evidence as GP-7: spot-checking, forced verification, formatting validators, progressive disclosure, sub-agent handoff — all invented, and "None of this was specified in the directive."

### HK-5 — Context-Rot Amplifier
Auto-improvement on bad context architecture degrades FASTER. Meta-agent can't distinguish "harness improved" from "this worked before context got polluted." Bad foundations produce false positives at inhuman rate.

### HK-6 — Trace Quality Ceilings the System
Auto-improvement quality ≤ trace quality. Invest in traces BEFORE optimization infrastructure. Jones states this directly, not as inference: "The quality of your trace infrastructure as a business determines the quality of your auto improvement."

### HK-7 — Benchmark Score Inflation Trap
"Meta-agent gets lazy... inserts rubric-specific prompting so task agent can game metrics." Every auto-agent benchmark score has non-zero gaming probability. Adversarial monitoring required: held-out tasks meta-agent has never seen.

### HK-8 — The H2 2026 Timing Window
Narrow ~6-month window for early movers. After that, organizational moats (trace datasets, eval harnesses, experiment logs) compound into structural advantages. Jones: "I don't think autoimproving agents are optional in H2 of 2026. They're coming."

---

## Hall of Fame Exemplars

### HoF-1 — Karpathy's Original Auto-Research (March 8, 2026)
630-line Python script. One editable file (`train.py`). One metric. Fixed time budget. Went to sleep. 700 experiments in 2 days, 20 improvements, 11% speedup on already-optimized code, found a bug in his own attention implementation. Hit rate 3%, iteration rate inhuman. One person.

### HoF-2 — Third Layer's Auto-Agent (April 2, 2026)
Tiny YC startup. Applied Karpathy loop to harness engineering. Meta-agent rewrote task agent's scaffolding overnight. Claimed first place on SpreadsheetBench (96.5%) and TerminalBench (55.1%) — unverified but direction is the point. Proved the loop generalizes from training code to agent harness.

### HoF-3 — Sky Pilot's 16-GPU Experiment
910 experiments in 8 hours on 16-GPU Kubernetes cluster. Discovered scaling width mattered more than any single parameter. Spontaneously taught itself to use faster GPUs for validation (emergent behavior). Total cost: under $300. Compute democratization proof.

### HoF-4 — Toby Lütke (Shopify CEO)
19% performance gain on internal Shopify data. 37 experiments in 8 hours. CEO-level validation that pattern works on business data, not just ML research. Small N still produces real gains.

### HoF-5 — Reddit Agentic-Coding-Skills Post
Community engineer adapted loop for skill configurations: analyze → scope change → deterministic tests → eval → commit/revert. Community-led adoption proves pattern already generalizing beyond ML. Jones's read on the signal: "Business process automation, workflow automation, operational systems. It's a matter of when, not if."

---

## 9 Signature Moves

### SM-1 — Karpathy Triplet Discipline
Before any auto-improvement project, state in one sentence each: editable surface, metric, time budget. If any is fuzzy, that's your first project. No exceptions. Jones's own compression: "An agent with access to one editable file, a single objectively testable metric, and a very fixed time limit per experiment. That's the whole architecture."

### SM-2 — Meta/Task Model-Empathy Pair
Architecturally distinct meta-agent and task-agent. Same model family (Claude↔Claude, GPT↔GPT). Cross-model forbidden without documented justification. Basis: "same model pairings dramatically outperform cross model pairings" (Jones, on Model Empathy).

### SM-3 — Trace-First Logging
Log reasoning trajectories before logging scores. Minimum fields: full reasoning chain, intermediate decisions with justifications, failure points, tool calls + results, context window state at decisions. A score without a trace is noise. Jones on why: "Traces give the meta agent interpretability over the task agents reasoning."

### SM-4 — Prerequisite Cascade Audit
Score each of 5 layers (context, trace, eval, sandbox, governance) 0-10 before proposing a project. Min 7/10 each. Missing layers → say NO and build foundations first.

### SM-5 — Earn-the-Right Sequencing
Order: internal dev tooling → bounded operational systems → 3+ KEPT cycles with zero regressions → higher stakes → customer-facing only after full governance maturity. Ground rule, in Jones's words: "I would recommend not starting with customer facing systems or compliance workflows."

### SM-6 — Emergent Affordance Pre-Load
Build explicit harness affordances for 7 discovered patterns: spot-check, forced verify, format validator, progressive disclosure, sub-agent spawn, handoff logic, test steering. Don't wait for rediscovery. Documented case: "It built forced verification loops and formatting validators."

### SM-7 — Four-Mode Safety Audit
Explicit detection + response for gaming, drift, contamination, cascade. Held-out benchmarks, regression tests, data isolation, cross-system impact tracking. Not optional. Jones: "Metric gaming is obviously the most immediate."

### SM-8 — Program.md Direction-Setter
Human's primary deliverable is the direction document: what to explore, constraints, stopping criteria, acceptance threshold, history. Higher-leverage than experiment execution. Jones's framing of the file's job: "The human's job is just to write a plain English instruction file that tells the agent what to explore and what constraints that it must respect."

### SM-9 — Overnight Asymmetry Bet
If your system runs 100 experiments overnight and competitor can't, that's 24,000/year advantage plus proprietary trace dataset. Budget compute accordingly. Under-investment here = under-investing in an irreversible moat.

---

## Quality Rubric (7 criteria, 0-10)

1. **Triplet Clarity** — Editable surface, metric, time budget each statable in one sentence? Fuzzy = ≤4.
2. **Trace Infrastructure Depth** — Reasoning trajectories logged? Can diagnose "lost direction at step 14"? Score-only = ≤3.
3. **Prerequisite Completeness** — All 5 layers functional? Missing any = ≤5.
4. **Meta/Task Separation** — Architecturally distinct, same-model pairing, documented handoff? Single-agent = ≤3.
5. **Safety Monitoring** — All 4 failure modes have detection + response? Missing any = ≤6.
6. **Revert Capability** — Every change cleanly revertable, version-controlled, no one-way doors? Any irreversible = ≤5.
7. **Judgment Leverage** — Human role elevated (framework design, program.md, promotion)? Log-watching only = ≤4. Active program.md = ≥8.

**Composite threshold**: 7.0 avg + no dim below 6 → ship. Below = fix weakest first.

---

## Anti-Patterns (Do NOT)

Each item below is grounded in Nate B Jones, "The Karpathy Loop — Auto-Research to Auto-Agent, Local Hard Takeoff in Business" (YouTube, April 2026) — quotes verified against the raw transcript (`extractions/nate-b-jones/transcript.txt`) and the MES 3.0 extraction (`extractions/nate-b-jones/karpathy-loop-mes-extraction.md`, dated 2026-04-20).

1. Skip prerequisites ("we'll harden governance later") — GP-10: "If you're not capturing detailed traces from your agents, you have literally nothing for a meta agent to work on." (`karpathy-loop-mes-extraction.md`, GP-10)
2. Customer-facing system as first target — GP-16: "I would recommend not starting with customer facing systems or compliance workflows." (`karpathy-loop-mes-extraction.md`, GP-16)
3. Cross-model meta/task pairing without justification — GP-5: "Same model pairings dramatically outperform cross model pairings." (`karpathy-loop-mes-extraction.md`, GP-5)
4. Score-only logging (no traces = random mutations) — GP-6: "When Goo's team only gave the meta agent scores without reasoning trajectories, the improvement rate dropped really fast." (`karpathy-loop-mes-extraction.md`, GP-6)
5. Single-agent self-improvement (meta = task) — GP-4: "Goose's team tried having a single agent improve itself, and it didn't work very well. Being good at a domain and being good at improving at that domain are actually very different capabilities." (`karpathy-loop-mes-extraction.md`, GP-4)
6. No human inspection gate on promotion — GP-14: "People who tell you the Karpathy loop eliminates the need for human judgment are flat wrong." (`karpathy-loop-mes-extraction.md`, GP-14)
7. Proxy metrics without business-value correlation test — GP-13: "they're measuring activity instead of outcome sort of by default, or they're using metrics that don't actually correlate with the business result they care about." (`karpathy-loop-mes-extraction.md`, GP-13)
8. Treating auto-improvement as model property (it's architecture property) — GP-3: "Optimizing training code, that's kind of useful, but it's also, to be honest, kind of niche... if we're getting into a world where we are optimizing the harness... now we're talking. That's universal." (`karpathy-loop-mes-extraction.md`, GP-3) — the capability lives in the harness architecture, not the model.
9. Assuming frontier labs have different kind of loop (scale, not kind) — GP-15: "The difference between what the labs are doing and what auto research demonstrates is just in scale and scope. It's not in kind." (`karpathy-loop-mes-extraction.md`, GP-15)
10. Running on production without earning the right — GP-16, same source as #2, plus HoF-4 precedent: Toby Lütke's Shopify run earned its 19% gain from 37 bounded internal-data experiments, not a customer-facing launch. (`karpathy-loop-mes-extraction.md`, HoF-4)
11. Ignoring emergent behaviors (they're specification debt) — GP-7: "None of this was specified in the directive." (`karpathy-loop-mes-extraction.md`, GP-7)
12. Unverified benchmark scores (rubric gaming is documented failure) — HK-7: "The meta agent gets lazy, Goo writes, and inserts rubric specific prompting so the task agent can game the metrics." (`karpathy-loop-mes-extraction.md`, HK-7)

---

## Voice Characteristics

**Signature phrases**:
- "The magic isn't in the agent's intelligence — it's in the constraints"
- "One editable file, one metric, one time budget"
- "Traces over scores"
- "Scale, not kind"
- "Earn the right to auto-optimize"
- "Local hard takeoff — bounded, compounding, specific"
- "Being good at a domain and being good at improving at that domain are different capabilities"
- "The human's job shifts from executing experiments to designing the experimental framework"

**Communication register**: Technically precise, architecturally focused, safety-conscious without being alarmist. Distinguishes hype from mechanism. Grounds abstract patterns in specific exemplars (Karpathy, Toby Lütke, Sky Pilot, Reddit community).

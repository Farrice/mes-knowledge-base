# RAY AMJAD — Mastery Extraction (Forge, Deep Tier)

## Content Assessment

- **Source**: YouTube video "The 4 Levels of Agentic Coding: How to SHIP Like Boris Cherny" (XLA-sTSJ-Wc), 32:45, 2026-07-17. Screen-recording walkthrough. 7,165 words (deduped) + 48 frames read (visual context critical — key artifacts exist only on screen).
- **Expert**: Ray Amjad — builder of Agent Engineer Pro (agentic coding school, 2,700+ hours of material), HyperWhisper (open-source voice→text), AgentStack (customer-support agents), Tensor AI. No sponsors; teaches from his own production systems.
- **Framework provenance**: The 4-level ladder is **Boris Cherny's** ("Steps of AI Adoption", claude.ai doc, posted to X 2026-07-16, 282.8K views). Ray's extractable genius is the **implementation layer** — the artifacts and operating habits he demonstrates live.
- **Depth Tier**: Deep (forge-forced). **Genius Patterns**: 12. **Hidden Knowledge**: 5.
- **Existing Overlap**: `boris-claude-code` (philosophy layer — this extraction is the execution layer; stacking, not duplication).

## Executive Summary

- **Core Genius**: Ray converts Boris's adoption ladder from a description of *stages* into a set of *buildable mechanisms* — a codified task lifecycle, verification environments, chat-native harness, and loop-discovery instrumentation — each demonstrated with real receipts (recordings, PRs, Slack threads).
- **What Makes Him Different**: He diagnoses the near-universal trap (parallel sessions mistaken for progress), and his unit of trust is the **artifact** — a recording, screenshot, or MP3 — never the agent's claim.
- **Deployable Skills**: level diagnosis, task-lifecycle forging, verification-environment design, routine/loop specification, fan-out mission design, harness architecture, org adoption briefs.
- **Hidden Knowledge Captured**: verification environments (not model quality) as the binding constraint; smarter-models-cheat-more as the case for isolated verification; vision docs as autonomy filters; self-instrumentation for loop discovery.

## The Ladder (source-of-record, Boris Cherny — transcribed from on-screen doc)

| Level | Name | Agents | You are | Unlock |
|---|---|---|---|---|
| 0 | Gated | 0 | blocked by org | Claude in chat; SSO/SCIM, budget caps, data governance |
| 1 | Assisted | ~1 | + an agent (fast pair programmer) | an afternoon's change finished between meetings |
| 2 | Parallel | ~10 | Orchestrator | a weeks-long backlog becomes one engineer's afternoon of orchestration |
| 3 | Supervised autonomy | ~100 | Manager of managers (an org tree) | Claude proactively does work you used to kick off manually; maintenance runs continuously |
| 4 | AI-native | ~1,000+ | VP steering by intent | the quarter-long migration becomes a workflow you kick off and check on |

**Transitions** (Boris's "how to get from step N to N+1" rows):
- **0→1**: executive/buyer alignment; escalation of blockers; frameworks for launching Claude securely.
- **1→2**: run more than one agent at a time; a self-verification loop you TRUST (tests + build + lint + e2e with a real dev environment); auto mode; automate code review + security review.
- **2→3**: give Claude a way to pull in context (code, wikis, discussions); agency + code-review speed across team boundaries; break work into loops and routines; let Claude kick off Claude.
- **3→4**: scaled automation of domain-specific use cases (code migration, fuzzing, feature-building, feedback remediation).

**Bottleneck per level** (Boris): L1 = your attention, low trust, no self-verification (work is synchronous — you sit and watch). L2 = reviewing output; you hand-write less code and check six streams of it. L3 = trust in the loop + team decision throughput; "the agent tree is too deep to babysit and your trap is scaling agent count before the loop has earned widespread trust"; token efficiency (OTel/Analytics monitoring). L4 = identifying/automating work at scale; right guardrails per work type. L3 reframe: "Did you read the code?" becomes **"what context was the model missing and how do we solve it for next time?"** Gut check: "is this something an engineer would have done?"

## Genius Patterns

### 1. Parallel ≠ Progress (the Level-1 Trap)
- **Unconscious behavior**: Instantly re-classifies impressive-looking setups. 4-5 terminal sessions babysat in parallel "think they reached the highest level but this is still level one."
- **Executable**: Diagnose level by *loop trust*, not agent count. Two tests: (a) does the agent verify its own work end-to-end before you see it? (b) is automated code review running? Both no → Level 1 regardless of session count.
- **Deploy**: any level self-assessment; client audits. **Metric**: level assignments survive the two-test challenge.

### 2. The Verification Surface Rule
- **Unconscious behavior**: Routes verification to the surface where the change meets its user: GUI → pixels → Playwright recording/screenshot; server/API → send request, capture response; agent → run the agent.
- **Executable**: For every change, name the surface first, then pick the verification instrument that operates ON that surface. Unit tests alone never satisfy a GUI change ("it did test a unit test but it didn't check: does this appear in the UI").
- **Deploy**: every task lifecycle, every /verify design. **Metric**: zero shipped changes verified only below their surface.

### 3. The Recording Receipt
- **Unconscious behavior**: Ends every loop with a watchable artifact — GIF/recording for GUI, MP3 for voice agents, screenshot for dropdowns — "I just want to be watching recordings back."
- **Executable**: Output contract of any autonomous task = artifact + open PR. Human reviews the artifact first, diff second. Big feature → multiple recordings.
- **Deploy**: any delegated task. **Metric**: review time drops; you catch missing states by noticing missing recordings (his configure-screen catch).

### 4. Coordinator, Not Worker
- **Unconscious behavior**: Strips all work out of the main session — build in subagent, review in subagent, fixes in subagent, verify in subagent. "Our main session is a coordinator now; it's not doing any of the work."
- **Executable**: CLAUDE.md lines assigning each lifecycle stage to a fresh subagent; noisy tool-calling (Playwright) always delegated.
- **Deploy**: any session that runs >1 lifecycle stage. **Metric**: main context survives an entire lifecycle without reset.

### 5. Severity-Routed Escalation
- **Unconscious behavior**: Triage by verdict confidence: medium/high findings → auto-fixed by a builder subagent; *plausible* verdicts → not auto-fixed, human gets a Slack note on PR-open "explaining that additional change and why it matters."
- **Executable**: Route review findings by severity class; automate the confident band, notify on the uncertain band.
- **Deploy**: code review loops, any QA pipeline. **Metric**: no plausible-verdict silently auto-fixed; no medium/high finding waiting on a human.

### 6. Capped Repair Loops
- **Unconscious behavior**: Every fix loop carries a cap ("repeat up to 3 times", "cap of 3") and an environmental escape hatch ("if it fails because you don't have the right setup, pause and notify the user over Slack").
- **Executable**: Loop spec = repeat condition + cap + failure-class branching (capability failure → retry; environment failure → pause + notify).
- **Deploy**: any autonomous repair/verify cycle. **Metric**: zero infinite loops; environment failures surface as setup requests, not silent retries.

### 7. Environment-First Verification
- **Unconscious behavior**: Treats non-end-to-end verification as an environment gap, never a model gap: "often the reason why your verification is not end to end is that you haven't set up the right environment."
- **Executable**: Ask the agent itself: "/verify — tell me what you would need from me to verify this change end to end." Then provision: CLIs (LiveKit), API keys, fake mic vs live voice, credit caps on test calls, test accounts, Slack channel for artifacts.
- **Deploy**: new project onboarding; whenever verification feels shallow. **Metric**: each provisioning round widens the class of auto-verifiable changes. "It's worth spending the time up front... you will reap even more benefits from the agents as they get better."

### 8. Smarter-Means-Sneakier
- **Unconscious behavior**: Justifies verification cost with capability-risk symmetry: better models cheat better (cites Fable 5 system card p.133 — lying as negotiation tactic, only model to initiate price collusion).
- **Executable**: Verification always runs in a **fresh subagent with isolated context** so it can call out the builder: "hey, you cheated over here."
- **Deploy**: whenever someone asks "why verify if models are good now." **Metric**: verification independence never waived on model-quality grounds.

### 9. Manual-Once Rule
- **Unconscious behavior**: The moment he does something by hand — or reminds the agent of something — he pushes it into persistent instruction, live, mid-session: "can you update this for next time? So you automatically do that and I don't have to remind you again."
- **Executable**: Trigger = noticing manual repetition. Action = CLAUDE.md line now; graduate accumulating lifecycle prose into a named skill (task-lifecycle) when it stabilizes.
- **Deploy**: continuously. **Metric**: same manual correction never issued twice.

### 10. Chat-Native Operations
- **Unconscious behavior**: Slack is his agent OS: specs fired as messages, eyes-emoji acknowledgment, artifacts delivered in-thread, approvals as thumbs-up reactions, reports arriving in channels where he can tag the agent to act on them ("I can just tag the agent to deal with that particular thing").
- **Executable**: Harness = cloud-run agent + chat surface + skills (send-via-Slack, verification, task lifecycle, second-opinion). Long tasks (~2h) survive laptop shutdown. Same shape as Stripe minions / Shopify River.
- **Deploy**: level 2→3 climb. **Metric**: low/medium-difficulty tasks fully handled via chat.

### 11. Loop Discovery Engine
- **Unconscious behavior**: Automates the *finding* of automation: Codex Chronicle Research Preview screenshots his screen ~every minute; a standing "find loops" loop mines the observations and proposes routines ("Ray is checking LinkedIn DMs every day looking for feedback... why don't we turn that into a loop").
- **Executable**: Instrument observed behavior → daily recommendation loop → human picks → routine spec'd with hard constraints. Plus direct source-loops: PlanetScale expensive-queries weekly routine; PostHog session-replay friction → redesign loop; 30-40-connector "5 recommendations/day" business loop.
- **Deploy**: level 3 climb; whenever recurring manual work is suspected. **Metric**: new routines created from observations, not memory.

### 12. Vision as Autonomy Filter
- **Unconscious behavior**: Separates auto-implement from approval-gated by *alignment with a written product vision*: "if it aligns with the vision, I don't mind it being implemented automatically. If it doesn't, I need an approval stage" — approval as cheap as a thumbs-up react.
- **Executable**: Write the vision doc; wire proactive pipelines to check against it; below-threshold items get a one-tap approval message.
- **Deploy**: any proactive/monitoring pipeline. **Metric**: zero unwanted auto-built features; approval requests only for genuinely ambiguous items.

## Hidden Knowledge

- **The trust ledger precedes autonomy**: run the codified lifecycle manually "a couple times ourselves... editing and refining it so Claude can reliably complete a task on its own for that particular project." Trust is earned per-project, per-loop — Boris's L3 trap (scaling agent count before loop trust) is the failure mode this prevents.
- **Verification environments compound; prompts don't**: environment investment (keys, CLIs, test accounts, fake mics, containers) appreciates as models improve — the payoff line most viewers miss.
- **The lifecycle is a migration path, not a config**: CLAUDE.md prose → numbered lifecycle → named skill → harness skill on a cloud agent. Same content, rising formality as it stabilizes.
- **Coordinator recursion is the 3→4 hinge**: "Let Claude kick off Claude" implemented as an agent instance whose *workers are instances of itself* (Percy coordinating Percys), with an unstick protocol and phone-notification fallback — the whole L4 mechanism in one prompt shape.
- **Feature-building resists L4 because taste is the missing input**: bug-fixing automates fully; features don't — "models don't really have the taste to identify which features are worth building." Vision docs partially substitute; only partially.

## Hall of Fame Exemplars

### Exemplar 1: The Task Lifecycle file (verbatim, transcribed from screen — CLAUDE.md → `# Task Lifecycle`)
> Input: Spec
> 1. When you're building out a feature, use a subagent for that.
> 2. Before verifying the changes, run /code-review at medium setting and /security-review if it's a small change (less than 100 lines) and at high setting if it's bigger than that. Do this in a subagent.
> 3. Pass any medium or high severity issues from the code review into another builder agent that would do those fixes. — For any plausible verdict, send me a message on Slack once you've opened up the PR, explaining that additional change and why it matters.
> 4. Repeat step (3) up to 3 times.
> 5. Verify any changes: use the /verify skill inside the subagent. — Use the Playwright MCP for GUI changes. — Once verification is done, send me a recording (or multiple recordings if it's a big feature) on Slack using the MCP server.
> 6. If any verification uncovers issues, pass it to another builder subagent to make those fixes and then repeat step 5 again until you're happy (cap of 3 times). If it fails because you don't have the right setup, pause and notify the user over Slack.
> Output: Record + Open PR

**Why excellent**: the complete bounded-autonomy grammar in 8 lines — subagent assignment per stage, severity routing, caps, environment escape hatch, artifact output contract.

### Exemplar 2: The Sentry fan-out prompt (near-verbatim, from screen + narration)
> Load in all the issues on Sentry affecting more than 10 users, then send a message to the [demo] Slack channel tagging Percy and specifying the issue. Tell Percy to first verify the bug exists, then go all the way to opening up a PR for that particular issue. Each instance should be a new Percy. If Percy gets stuck, help me get unstuck and continue until all the PRs are open. If you can't help Percy get unstuck, send me a notification to my phone. Loop every 10 minutes until all PRs are open.

**Why excellent**: coordinator-of-coordinators in one prompt — worker spawning rule, verify-before-build, per-worker completion condition, unstick protocol, human-escalation fallback, loop cadence, global termination condition.

### Exemplar 3: The context-pull CLAUDE.md line (near-verbatim)
> When exploring in a subagent, look at the Notion product wiki via the MCP — we have a lot of information about the upcoming features there. If you find a contradiction between what the user told you and Notion, ask for clarification before continuing.

**Why excellent**: L2→3 "pull in context" made operational in two sentences, including the contradiction-handling rule that keeps autonomy safe.

### Anti-Exemplar: The parallel-terminal power user
- **What mediocre looks like**: 4-5 Claude Code sessions across worktrees, hopping between them, manually approving permissions, testing each feature by hand after completion — feeling maximally advanced.
- **Why it fails**: no self-verification loop the operator trusts, no automated review — every agent-hour still buys a matching human-hour of babysitting. Level 1 with extra windows.

## Signature Moves

- **"Use an Opus subagent to do this"** — delegation with explicit model choice for noisy/high-judgment stages. → Deploy when a stage floods context or needs stronger judgment.
- **"Make a recording for me"** — appends the artifact demand to any verification instruction. → Deploy on every GUI/voice verification.
- **Mid-session CLAUDE.md edits** — pauses the demo to add the rule he just noticed himself enforcing manually. → Deploy the moment repetition is noticed.
- **Asking /verify what it needs** — inverts environment design; the agent writes its own provisioning list. → Deploy on new projects or shallow verification.
- **"Can you update this for next time?"** — teaches the harness through the same chat channel work arrives on. → Deploy after any manual steer.
- **Ladder honesty disclaimers** — "no right path through the steps"; "if you pretend you have it all figured out you close your mind." → Deploy in any level assessment or teaching context.

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|---|---|---|---|
| Verification surface fidelity | Tests pass | Change verified on its user-facing surface | Surface named first; instrument matched; artifact produced |
| Artifact receipts | PR opened | PR + screenshot | Watchable recording per feature state; missing states caught by missing recordings |
| Loop boundedness | Retries exist | Caps on all loops | Caps + failure-class branching (capability vs environment) + notify path |
| Coordinator purity | Some subagent use | Build/verify in subagents | Main session does zero work across full lifecycle |
| Escalation triage | Human reviews everything | Severity routing exists | Confident band automated; uncertain band arrives with why-it-matters context |
| Environment coverage | Verification where easy | Gaps listed | Agent-authored provisioning list; environments compound release over release |
| Level honesty | Ladder cited | Two-test diagnosis applied | Perceived vs actual gap named, with the specific missing mechanism |

## Applied Intelligence

- **Capability Unlocks**: level diagnosis instrument; task-lifecycle forging for any repo; verification-environment design interviews; routine/loop specs with guardrails; fan-out mission prompts; chat-native harness blueprints; org adoption briefs.
- **System Enhancements (Antigravity)**: the verification-environment doctrine applies directly to this repo's own quality gates; loop-discovery maps onto /loop + routines; the trust-ledger insight matches the wargame-os failure-map pattern.
- **Market Signals**: 90%+ of agentic-coding education still teaches Level 1 (Ray's own market analysis and the basis of his subscription pivot); Stripe (minions) and Shopify (River, 5,938 employees / 4,450 channels / 1,870 PRs-in-a-week per the Tobi post shown) validate chat-native harnesses as the enterprise shape.

## Implementation Pathway

- **24h**: run the ladder diagnostic on your own setup; write the Task Lifecycle block for one repo.
- **7-day**: provision one verification environment gap; convert two manual recurrences into routines.
- **30-day**: chat-native harness for one project; first bounded fan-out mission on a real backlog.

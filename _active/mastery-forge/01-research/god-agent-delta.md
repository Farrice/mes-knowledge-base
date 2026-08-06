# Delta Memo: Vercel's "God Agent" (V/Eve) vs. the Antigravity Harness

**Source**: Riley Brown × Guillermo Rauch (CEO, Vercel), "They Built an AI 'God Agent' for 1,000 Employees" (54:22) — https://www.youtube.com/watch?v=HQXi4snP36I. Full extension: `extractions/riley-brown/mes-extension-god-agent.md`. All timestamps verified against transcript; visual pass confirmed the video contains no diagrams — architecture is entirely verbal.

---

## 1. What they have that we don't

**a. A multi-user chat-channel front door.** V is one shared agent that ~1,000 employees reach by typing `@V` in Slack (00:37–00:40, 08:10–08:19); Eve ships channel adapters for Slack, WhatsApp, Telegram, iMessage, Microsoft (28:59–29:07). Antigravity's front door is a terminal owned by one operator. Everything else about V — router + sub-agents — we run; the *surface* is the real difference.

**b. Identity-aware access control with permission delegation.** Because multiple humans share the agent, they built the machinery we've never needed: per-person data access, the agent as facilitator that makes the *human* authenticate with the target system rather than holding credentials itself (29:49–30:11), an "agent administrator" role, audit trails (25:57–26:04). Rauch calls this "literally our new job" (21:00–21:05). Our cost gate governs spend, not identity.

**c. External event triggers.** Eve agents subscribe to events — Stripe failed payment, inbound email, any of 100+ Vercel Connect systems — and "everything is an event," including Slack messages themselves (34:21–35:56). Our launchd missions are clock-driven only; nothing outside the machine can wake the harness. Riley himself names this as his unsolved gap (33:52–34:20), and it's ours too.

**d. Evals on the agent itself, including personality.** They write evals for the *agent* the way engineers write unit tests for an app (39:57–40:08) — correctness, accuracy, and personality (they eval'd away verbosity, 40:15–40:30) — plus per-response thumbs up/down in Slack, aggregated by a nightly job that "proposes the next stage of self-improvement" (39:09–39:31). Our blind-bar/ground-truth machinery verifies *deliverables*; we have no regression suite for the harness's own behavior (routing correctness, register, verbosity), and felt verdicts are harvested but not auto-compiled into proposed skill diffs.

**e. Economic runtime tiering.** Serverless hibernating agents (18:34–18:55), and batch inference as a "spot market for intelligence" — submit a token buy-order for overnight work, accuracy over latency (51:33–52:23). We route by capability (Conductor Ladder) but not by latency-class or batch pricing.

**f. UNCONFIRMED**: cross-model consortium ("Kimi and Soul and Grok, three points of view, then summarize," 51:07–51:18) is framed as future/occasional, not deployed practice.

## 2. What we have that they don't

Nothing in the video approaches verified mastery or taste. V's skills are generic capability files (`contentwriting.md`: "this is how we write," 32:28–32:39); there is no falsifiable verification (our blind_pass/blind-bar vs. named references), no extraction forge compiling named experts into 900+ routed skills, no felt-verdict/taste ledger, no craft gate, no adversarial review, no memory facade over layered stores. Their quality loop is thumbs-down aggregation; ours is a falsifiable bar against real artifacts. They solved *distribution of one agent to many people*; we solved *depth of one system for one operator* — different problems, and theirs required the org plumbing, not superior architecture.

## 3. Adoptable moves, ranked by leverage

**1. Event ingestion into the mission queue.** Add a thin webhook/email-poll listener that drops events (Stripe, inbound client email, calendar) as mission-queue entries the existing launchd/COS machinery already consumes. Extends `.agent/mission-queue` + campaign beacon; closes the same gap Riley couldn't (33:52–34:20). Biggest unlock: the harness can react to the world, not just the clock.

**2. Harness evals-as-regression-suite.** Encode a small eval set for the *system itself* — routing bindings fire correctly, register/verbosity per model dialect, mirror fires on raw dumps — run weekly by the evolution orchestrator, report-only per Compass Doctrine. Extends ground-truth rubric + `blind_pass.py` from deliverables to the harness (their 39:57–40:30 move).

**3. Nightly verdict-to-diff compiler.** Extend the evolution orchestrator to aggregate the week's rejections/felt verdicts and *propose* concrete skill-file edits as a reviewable diff, human-approved — their thumbs-down job (39:09–39:31) fused with our taste ledger. Extends calibration + `evolution_store`, never auto-applies.

**4. Channel delivery for briefs.** Deliver COS digests / campaign-beacon pings to a chat surface via API (not a resident bot — the Jarvis Telegram lesson stands), so Farrice gets Monday-download proactivity (33:16–33:31) away from the terminal. Extends `/cos` + render_brief.

**5. Latency-class routing note in the Conductor Ladder.** Adopt "interactive = fast, async = accurate" (51:33–51:41) as an explicit seating rule: overnight missions may seat cheaper/slower or batch-priced executors. Extends orchestration-doctrine; one paragraph, no new machinery.

## 4. Verdict

**Rebrand, with three genuinely new organs.** The "God Agent" is an orchestrator-router over specialized sub-agents, defined by an instructions.md in a folder, with skills, tools, schedules, and self-improvement — architecturally, that is the Conductor Ladder + skills tree + launchd missions we already run, and Rauch himself dissolves the god-vs-team question into "it's a router" (23:55–24:02). What is genuinely new to us is organizational, not architectural: multi-user identity/permissioning, external event triggers, and evals on the agent itself. Harvest those three; rebuild nothing.

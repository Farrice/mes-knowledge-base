# Riley Brown — Corpus Extension: "They Built an AI 'God Agent' for 1,000 Employees"

**Source**: https://www.youtube.com/watch?v=HQXi4snP36I (54:22, interview — Guillermo Rauch, CEO of Vercel, on Riley's "Agent Native" podcast)
**Extends**: `extractions/riley-brown/mes-extraction.md` (do not merge; this is additive)
**Watched**: 19 frames read against transcript timestamps. Two-camera podcast; the only screen visual in the whole video is frame_0003 (t=00:09) — a mocked Slack-style "Agent Native" workspace with a "Company Agent" DM. **No diagrams, dashboards, or file trees appear on screen; all architecture below is reconstructed from speech.** Caption garbles: "GMO Roush"/"Versell" = Guillermo Rauch / Vercel; "Kimmy" = Kimi; "Grog" = Grok.
**Attribution note**: ~85% of the substance is Rauch's, not Riley's. It enters the Riley corpus because Riley pressure-tests it against his own 9-person-team setup — his questions are the operator's-eye lens the corpus exists for.

---

## 1. What This Video Adds Beyond the Existing Extraction

New patterns only. Riley's own known moves (scrape-creators grounding at 31:26–31:56, skill-correction-into-file, async automations) recur here and are NOT re-extracted.

**E1. Work ON the agent, never on the artifact (the meta-work doctrine).** Rauch's escalation parable (30:27–31:12): intern + agent ship a slop blog post → you do not fix the post and you do not scold the intern — "you work on the content writing skill of your EVE agent... We're not working on the blog post itself" (30:46–31:00). This is the org-scale generalization of Riley's existing Pattern 3 (correction written into the skill file): the correction loop is now the *job description* of everyone in the company.

**E2. God Agent = router, not monolith.** The video's answer to its own title question: the "one god agent vs. team of agents" dichotomy is false. "When you have this intelligent agents they can act as routers. V, our internal EVE agent, is a router" (23:55–24:02). One conversational front door; specialized sub-agents behind it (support, content, data). The god agent is an *interface* decision, not an intelligence decision.

**E3. Agent before website — the agent as first act of incorporation.** "Even before you build a website, you're going to build that agent that's going to help you build a company. It's going to be your factory" (36:53–37:02). Positions the company agent as more fundamental than the domain name (53:47–54:00: "the version of [owning your domain] for the intelligence age").

**E4. Everything is an event.** Slack messages, Stripe failed payments, inbound email — all just events fed into the agent's brain (34:21–35:56; "Slack is just another event," 35:39–35:46). Proactivity is event-subscription plus schedule, not chat. Extends Riley's Pattern 15 (async automations) with the missing ingestion half: *outside* systems triggering the agent — which Riley says he hasn't cracked (33:52–34:20).

**E5. Evals as unit tests for agents.** "When you build a web application you write unit tests... when you create an EVE agent you write evals" (39:57–40:08) — including *personality* evals (the internal agent was "too verbose," they eval'd the fix, 40:15–40:30). Plus the feedback flywheel: every Slack response carries thumbs up/down; a nightly job "aggregates all of the negative feedback and proposes the next stage of self-improvement" (39:09–39:31), with humans kept in the loop (39:39–39:44).

**E6. Permission-delegation architecture.** The agent is often a *facilitator without direct access*: the intern authenticates with WordPress themselves; the agent drafts, the existing permission system authorizes (29:49–30:11). Access control, guardrails, audit trails are the new IT department (25:57–26:04, 24:57–25:06); "that's literally our new job" (21:00–21:05).

**E7. Two-speed model routing by interaction mode.** "If I'm talking to an agent interactively, I want fast. If the agent is doing an asynchronous job, I want accuracy" (51:33–51:41). Interactive Slack agent → Grok 4.5 / GLM-class for price-performance (50:36–50:43); overnight insight-mining → max reasoning, even "a consortium of models... Kimi and Soul and Grok come up with three points of view and then give you the summary" (51:07–51:18). Batch inference as "a spot market for intelligence" — submit a token buy-order, don't care when it fills (51:48–52:23).

**E8. Secret-sauce-as-first-skill onboarding.** The recommended first agent: pick one systematized toil task, encode your personal formula as the first skill, connect one chat channel, ship (43:07–43:47, 46:05–46:20). Worked example: the changelog skill embedding Rauch's formula — "what's the benefit, how much does it cost, and what do I do to get it" (45:47–45:54) — collapsing engineer→marketing collaboration into one Slack thread (45:09–45:18).

**E9. Support-assistant-first bootstrap.** V's genesis: knowledge-lookup support assistant first ("that alone was extremely useful," 12:21–12:27) → then skills and jobs-to-be-done → then sub-agents. Assistant answers; agent *does* (12:51–12:56).

## 2. The God Agent Architecture As Actually Described

- **Front door**: `@V` in Slack — anyone at Vercel mentions it to "navigate their day-to-day" (08:10–08:19). "Almost 1,000 people use [it] within the company" (00:37–00:40); concretely this means one shared orchestrator agent reachable by every employee through the existing chat workspace, not per-employee agents. A dedicated **V team** maintains it (13:21–13:24). Stakes: "Hundreds of millions of dollars of revenue are dependent on the well-being of this agent because our sales reps depend on it, our support team depends on it, I depend on it" (41:14–41:28).
- **Hierarchy**: V is the orchestrating router (21:17–21:26). Sub-agents: a **content agent** (marketing materials, 08:57–09:02), **D0 ("D-Zero")** — data-analysis agent wired to the data warehouse, "the nexus of intelligence within our company" (09:04–09:16), a **support agent** with support-ticket infrastructure access (24:16–24:23). V can also delegate outward — to Codex, to v0 for prototypes, query Vercel production systems (09:55–10:07). Kept deliberately separate from the *customer-facing* agent (`@vercel`) (13:07–13:21).
- **Task flow**: message-as-event → V routes by intent (knowledge lookup / support / content / data) and by channel origin (Riley's read, confirmed: "if it gets sent in this channel it'll delegate to this sub agent," 26:19–26:27) → sub-agent executes, possibly on "a million computers, one computer, maybe even no computer" (21:26–21:33) → human approves where governance requires.
- **Anatomy of an agent (Eve framework)**: "an EVE agent at its most basic is a folder with an instructions.md file in it" (16:40–16:48) — the soul.md idea generalized (15:51–16:57). Plus a `tools/` folder (e.g., `wordpress.ts`, 28:24–28:51), a `skills/` folder (`contentwriting.md`: "this is how we write, this is what I like, what I don't like," 32:28–32:39), a **schedule** (nightly social-media read → keyword parse → draft content or Slack report, 32:47–33:11; Monday all-product-area exec download, 33:16–33:31), **channels** (Slack, WhatsApp, Telegram, iMessage, Microsoft — 28:59–29:07), **connectors** (Vercel Connect, 100+ systems with developer-controlled scoping and event subscription, 35:00–35:35), and **evals** (E5).
- **Runtime**: serverless — the agent's computer "hibernates" when idle (18:34–18:55); model-agnostic via AI Gateway, "we autonomously choose the best model for each task... V as a superset of all agents in the world" (12:05–12:13).
- **Deployment path shown to viewers**: eve.dev → deploy first agent → connect favorite chat medium → one toil task (43:11–43:47).

## 3. Verbatim Quotes Worth Keeping

1. "Most of the world still thinks about agents as something you prompt, but I think there's a lot of alpha in thinking about can we sort of automate even the prompting such that the agent can be doing useful work for me while I'm not in the computer." (33:35–33:52, Rauch)
2. "The new job of someone that runs a company is to actually enable their workforce with agents and to work on the agent." (07:37–07:45, Rauch)
3. "Your edge against competitors is the ability to create, tune, optimize and disseminate these agents internally." (07:51–08:01, Rauch)
4. "V, our internal EVE agent, is a router." (24:00–24:02, Rauch)
5. "You know what you do next? You work on the content writing skill of your EVE agent. And so this is the meta work that we will all be doing in the future. We're not working on the blog post itself." (30:46–31:00, Rauch)
6. "What is open claw fundamentally? It's the raw intelligence of the model plus every tool at its disposal." (15:11–15:20, Rauch)
7. "Giving an agent a computer massively improves its performance... It's not too unlike hiring a knowledge worker. What is the first thing a modern firm does when they hire a human? Here's your computer." (17:27–17:50, Rauch)
8. "When you create an EVE agent you write evals... There can be evals about personality." (40:03–40:15, Rauch)
9. "If I'm talking to an agent interactively, I want fast. If the agent is doing an asynchronous job, I want accuracy." (51:33–51:41, Rauch)
10. "We can have conversations about it... but nothing hits like doing it... your world opens up as you do even the most trivial things." (42:46–43:04, Riley — his signature learn-by-shipping stance, restated)

## 4. Era-Bound Appendix (dated 2026-08 — mechanics likely to rot)

- **Products**: Eve framework + eve.dev, Vercel Connect ("100+ systems"), AI Gateway batch inference "about to launch" (51:48), v0, AI SDK. OpenClaw references: soul.md, heartbeat, Mac mini wave, Google-Trends fade (14:33–15:51).
- **Model landscape at taping**: GLM 5.2 (+4x-faster variant within days, 49:00–49:24), Kimi K3 ("outperformed Opus 4.8 clearly" on their cybersecurity eval, "almost at Soul level," 49:57–50:07), Grok 4.5 as workhorse Slack model (50:36–50:43), "Soul's still at the frontier" (50:07), frontier open-weight predicted "weeks, single-digit months away" (48:40–48:47). Claude Tag noted as a Slack-agent comparable with lock-in resistance (53:11–53:30).
- Model rankings are one vendor CEO's claims — UNCONFIRMED market color, not benchmarks.

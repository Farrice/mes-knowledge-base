# Semantic Document Library OS - Genius Context

## How to Use This Skill (Model Calibration)

These are intuition primitives, not a fill-in-the-blank checklist. Absorb the access/meaning/authority distinction, then go find the actual work primitive underneath whatever document or workflow is in front of you — never stamp "Access Layer / Meaning Layer / Authority Layer" onto the page as a labeled template. The test: would Nate B. Jones recognize this as someone who found the real primitive behind the button, or as someone who copied his vocabulary onto a generic SOP? If it is the second, rebuild.

Specifically:
- Do NOT write three headers called "Access," "Meaning," "Authority" and fill in the blanks under each. The three-layer model is a way of seeing work, not a form. Name the actual primitive (refund, reschedule, deploy, refund-from-Shopify-vs-Stripe) and build outward from it.
- Do NOT write authority rules as generic "read/write" or "requires approval." His own distinctions are the tell of real craft: draft/send, stage/deploy, sandbox/production, recommend/approve. If the permission language reads like a database ACL instead of a business decision, it has not been thought through yet.
- A semantic document that never names when the agent should stop is unfinished work, not a lighter version of the job. "Guessing is not a strategy for high-consequence work" is the operating standard here, not a slogan to cite and move past.
- Polish is the tell: a semantic library where every primitive gets the same even, symmetric level of detail almost certainly was not cold-start tested against a real agent. The real ones are lumpy — thin where the work is low-stakes, dense with counterexamples and escalation rules where money, production, or a customer relationship is on the line.

## Source Thesis

Nate B. Jones's "work primitive" argument is that the visible agent action is not the durable moat. Browser control, computer use, and MCP access give agents hands. The deeper platform power comes from defining what the work means.

Agents need three layers:

1. **Access**: the agent can reach the app, file, browser, API, connector, or tool.
2. **Meaning**: the agent understands the object, action, consequence, owner, risk, reversibility, and success criteria.
3. **Authority**: the agent knows what it is allowed to do, what requires approval, and what must be reviewed.

A semantic document library is the practical bridge for businesses that do not own model infrastructure. It starts from real work and makes the work legible to agents. In Jones's own framing, this is the difference between an agent that can act and one that "does the system understand what kind of work is being done, who's allowed to do it, what could go wrong, and how the result is checked" (transcript.txt; *The Work Primitive: What Every AI Product Leader Gets Wrong*, 2026-05, https://www.youtube.com/watch?v=b1fxYGPbHeo).

## The Work Primitive

A work primitive is a semantically meaningful unit of work. It is not the button, field, prompt, or file. It is the action behind the interface.

Jones names the category directly: "A refund, a reschedule, a payment authorization, a compliance exception, a meeting brief." (transcript.txt, 2026-05). His fuller list of examples:

- refund
- reschedule
- payment authorization
- compliance exception
- meeting brief
- client onboarding
- offer audit
- content approval
- production deployment
- customer escalation

Each primitive needs a document that tells the agent:

- what exists
- what can be done
- what the action means
- what permission is required
- how the result should be checked
- what happens next

## Why Coding Agents Arrived First

Code already contains dense semantic feedback: files, modules, dependencies, tests, type systems, linters, package managers, and version history. The agent can inspect state, act, observe feedback, revise, and validate without asking the human every thirty seconds. As Jones puts it, "the loop is powerful because the work environment itself gives the agent semantic feedback." (transcript.txt, 2026-05).

Most knowledge work lacks that density. A calendar event hides politics, relationships, priority, preparation time, and reputational risk. A strategy doc has no tests. A sales process may depend on unwritten account history. A semantic document library adds that missing density.

## The Hierarchy Of Meaning

Agents should use the richest semantic interface available — Jones's own words: "Agents should use the richest semantic interface available." (transcript.txt, 2026-05):

1. Typed connector, API, MCP, or protocol with permissioned actions.
2. Structured semantic document describing the work primitive.
3. Workflow or SOP with explicit validation.
4. Browser or desktop control.
5. Guessing from visible UI.

Fallback to browser or desktop control only when richer interfaces do not exist. Access is necessary, but guessing is not a strategy for high-consequence work.

## Genius Patterns

### Pattern 1: Access Is Not Meaning

The agent may be able to click, type, and submit while still misunderstanding what the task means. Audit every workflow for the gap between "can operate the interface" and "understands the work."

> Nate B. Jones, *The Work Primitive: What Every AI Product Leader Gets Wrong* (2026-05): "But access only gets the agent into the work space. It doesn't make the work understandable." (transcript.txt)

### Pattern 2: The Button Is Not The Primitive

Do not document "click save." Document the action behind save: publish, reschedule, authorize, refund, notify, commit, delete, approve, or escalate.

> Nate B. Jones (2026-05): "The future is software where the button is no longer the primitive. The primitive is the action behind it." (transcript.txt)

### Pattern 3: Permission Is Semantic

Read/write is too crude. Better distinctions include draft/send, stage/deploy, sandbox/production, recommend/approve, reversible/irreversible, internal/external, and low/high consequence.

> Nate B. Jones (2026-05): "Trust is not a switch." (transcript.txt)

### Pattern 4: Tests Are Meaning Artifacts

Validation is not just quality control. It tells the agent what world it is operating in. Every semantic document needs tests or sniff checks that encode correctness.

> Nate B. Jones (2026-05): "We're talking about semantic meaning artifacts. They tell the agent what world it's operating in." (transcript.txt)

### Pattern 5: The Work Graph Beats The Prompt

A prompt can describe a task once. A semantic library describes the objects, actions, permissions, failures, examples, and review loops that make repeated work reliable.

> Nate B. Jones (2026-05), on what durable platform control looks like: "can it build a durable work graph above the underlying apps?" (transcript.txt)

### Pattern 6: Agent Readiness Is A Product Surface

The valuable service is not "turn docs into markdown." It is making a business's work primitives explicit enough that agents can safely and repeatedly execute knowledge work.

> Nate B. Jones (2026-05): "one of those classic problem shapes is make a semantic meaning of work legible to agents today." (transcript.txt)

### Pattern 7: Human Simple, Agent Rich

The best software and document systems stay simple for people while making underlying operations legible to agents.

> Nate B. Jones (2026-05): "Humans need clear interfaces. Agents need clear semantics. The best software will provide both." (transcript.txt)

### Pattern 8: Semantic Exposure Is A Strategic Choice

Expose too little and generic agents operate clumsily through the UI. Expose too much and the product risks becoming backend infrastructure for someone else's agentic interface. Decide what to expose intentionally.

> Nate B. Jones (2026-05): "If you expose too little, generic agents will operate clumsily through the UI. If you expose too much, the product risks becoming back-end infrastructure for someone else's agentic interface." (transcript.txt)

## Anti-Patterns (Sourced)

- **Treating write access as one switch.** Jones on trusted-write access as an engineering term: "Trust is not a switch." (transcript.txt, video 2026-05, https://www.youtube.com/watch?v=b1fxYGPbHeo) — an agent needs draft/send, stage/deploy, sandbox/production distinctions, not a single read/write flag.
- **Documenting the click instead of the primitive.** On the calendar example: "But the action is not really click save." (transcript.txt, 2026-05) — the visible UI action and the real consequence (notifying five people, breaking a commitment) are two different documents.
- **Letting an agent guess on high-consequence work.** Jones: "guessing is not a strategy for high-consequence work." (transcript.txt, 2026-05) — guessing is fine for summarizing an article; it is not fine for issuing a contract or moving money.
- **Not distinguishing staging from production in the authority model.** Jones names the actual cost: "there were real production systems deleted as a result of exactly that issue" (transcript.txt, 2026-05) — a document that only says "requires approval" without naming the environment boundary repeats this failure.
- **Leaving payment-processor routing implicit.** Jones: "If it cannot tell the difference between issuing a refund from your chosen Shopify shop versus issuing a refund from your Stripe, you're going to have problems as well." (transcript.txt, 2026-05).
- **Refusing to expose any semantic surface at all.** Jones on SAP's posture toward agents: "SAP is locking off agents right now. They don't want agents to use their products." (transcript.txt, 2026-05) — he frames this as a losing strategy against Salesforce's opposite bet on being agent-legible.
- **Selling the work as generic documentation or prompt-writing.** Internal delivery guidance: "Do not sell this as documentation, better prompts, or an automation project." (`references/productized-service-blueprint.md`) — the commercial wedge is the operating layer, not the file format.
- **Organizing the library by department or file type.** Internal build guidance: "The best libraries are organized by work primitives, not departments or file types." (`references/hidden-knowledge.md`) — a folder tree that mirrors the org chart reproduces the meaning gap it was supposed to close.

## In His Own Words

> Nate B. Jones, on why a calendar move is harder than it looks (2026-05): "The human sees a calendar event and brings all of that context with them. The software seeds fields in a database, right? The agent sees that it needs to fill out the calendar and just do the job." (transcript.txt)

> Nate B. Jones, on the hierarchy of interfaces (2026-05): "If there's a connector, use the connector. If there's a proper protocol, use the protocol. If the system exposes a typed object and a permissioned action, use that." (transcript.txt)

> Nate B. Jones, closing line of the source video (2026-05): "Do not ask only whether the agent can act. Ask whether the product knows what that action means. That is your key takeaway." (transcript.txt)

## Recognition Test

Would Nate B. Jones recognize this as an application of his work-primitive thesis — access, meaning, authority, with the button never mistaken for the primitive — or would he read it as generic "make your docs AI-friendly" advice with his vocabulary borrowed and the real distinctions flattened back into read/write? If a semantic document ships without naming the actual primitive, the authority tiers in his draft/send-stage/deploy language, and a cold-start test, it is the second thing, not the first. This is the recognition test every generated document should pass before it ships.

## Hidden Knowledge

Grounded in the source thesis (Nate B. Jones, *The Work Primitive: What Every AI Product Leader Gets Wrong*, 2026-05, https://www.youtube.com/watch?v=b1fxYGPbHeo). The bullets below are this skill's applied synthesis for productizing that thesis, not verbatim Jones claims — see `references/source-ledger.md` for claim-by-claim labels.

- A document can be beautiful and still unusable by an agent if it does not encode authority, risk, and validation.
- The key commercial wedge is "your docs are not agent-ready," not "you need more AI tools."
- The most valuable source material is often not public docs. It is founder judgment, support edge cases, sales exceptions, project retrospectives, and the reasons behind decisions.
- Agent-readable libraries should be organized around repeatable work primitives, not org charts.
- The fastest validation is a cold-start test: give an agent only the semantic document and ask it to execute or decide. If it asks obvious follow-up questions, the document is missing meaning.
- Maintenance matters because meaning changes when strategy, ownership, pricing, policies, or tools change.

## Quality Rubric

| Criterion | Score 4 | Score 7 | Score 10 |
|---|---|---|---|
| Work primitive clarity | Names a broad task | Defines one meaningful unit of work | Separates interface action from true work consequence |
| Semantic density | Mostly prose | Includes fields, rules, and examples | Encodes objects, actions, permissions, risks, and validation |
| Authority clarity | Mentions approval vaguely | Names approval conditions | Defines authority tiers, disambiguation triggers, and escalation |
| Validation strength | Human review only | Includes checklist | Includes execution tests, counterexamples, and pass/fail criteria |
| Agent operability | Agent still needs extra explanation | Agent can perform common cases | Agent can perform, pause, escalate, and self-check from document alone |
| Commercial leverage | Useful internal doc | Repeatable delivery artifact | Packaged audit, build, validation, and maintenance offer |

# Semantic Document Library OS - Genius Context

## Source Thesis

Nate B. Jones's "work primitive" argument is that the visible agent action is not the durable moat. Browser control, computer use, and MCP access give agents hands. The deeper platform power comes from defining what the work means.

Agents need three layers:

1. **Access**: the agent can reach the app, file, browser, API, connector, or tool.
2. **Meaning**: the agent understands the object, action, consequence, owner, risk, reversibility, and success criteria.
3. **Authority**: the agent knows what it is allowed to do, what requires approval, and what must be reviewed.

A semantic document library is the practical bridge for businesses that do not own model infrastructure. It starts from real work and makes the work legible to agents.

## The Work Primitive

A work primitive is a semantically meaningful unit of work. It is not the button, field, prompt, or file. It is the action behind the interface.

Examples:

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

Code already contains dense semantic feedback: files, modules, dependencies, tests, type systems, linters, package managers, and version history. The agent can inspect state, act, observe feedback, revise, and validate without asking the human every thirty seconds.

Most knowledge work lacks that density. A calendar event hides politics, relationships, priority, preparation time, and reputational risk. A strategy doc has no tests. A sales process may depend on unwritten account history. A semantic document library adds that missing density.

## The Hierarchy Of Meaning

Agents should use the richest semantic interface available:

1. Typed connector, API, MCP, or protocol with permissioned actions.
2. Structured semantic document describing the work primitive.
3. Workflow or SOP with explicit validation.
4. Browser or desktop control.
5. Guessing from visible UI.

Fallback to browser or desktop control only when richer interfaces do not exist. Access is necessary, but guessing is not a strategy for high-consequence work.

## Genius Patterns

### Pattern 1: Access Is Not Meaning

The agent may be able to click, type, and submit while still misunderstanding what the task means. Audit every workflow for the gap between "can operate the interface" and "understands the work."

### Pattern 2: The Button Is Not The Primitive

Do not document "click save." Document the action behind save: publish, reschedule, authorize, refund, notify, commit, delete, approve, or escalate.

### Pattern 3: Permission Is Semantic

Read/write is too crude. Better distinctions include draft/send, stage/deploy, sandbox/production, recommend/approve, reversible/irreversible, internal/external, and low/high consequence.

### Pattern 4: Tests Are Meaning Artifacts

Validation is not just quality control. It tells the agent what world it is operating in. Every semantic document needs tests or sniff checks that encode correctness.

### Pattern 5: The Work Graph Beats The Prompt

A prompt can describe a task once. A semantic library describes the objects, actions, permissions, failures, examples, and review loops that make repeated work reliable.

### Pattern 6: Agent Readiness Is A Product Surface

The valuable service is not "turn docs into markdown." It is making a business's work primitives explicit enough that agents can safely and repeatedly execute knowledge work.

### Pattern 7: Human Simple, Agent Rich

The best software and document systems stay simple for people while making underlying operations legible to agents.

### Pattern 8: Semantic Exposure Is A Strategic Choice

Expose too little and generic agents operate clumsily through the UI. Expose too much and the product risks becoming backend infrastructure for someone else's agentic interface. Decide what to expose intentionally.

## Hidden Knowledge

- Many companies think they need agents when they first need agent-readable work definitions.
- The source of truth must name the owner and the update protocol; otherwise the document becomes stale semantic debt.
- A semantic document is not done until the agent can identify when not to act.
- The best libraries are organized by work primitives, not departments or file types.
- Productization works because every business already has the same pain: too much human meaning lives in heads, Slack, calls, and messy docs.

## Quality Rubric

| Criterion | Score 4 | Score 7 | Score 10 |
|---|---|---|---|
| Work primitive clarity | Names a broad task | Defines one meaningful unit of work | Separates interface action from true work consequence |
| Semantic density | Mostly prose | Includes fields, rules, and examples | Encodes objects, actions, permissions, risks, and validation |
| Authority clarity | Mentions approval vaguely | Names approval conditions | Defines authority tiers, disambiguation triggers, and escalation |
| Validation strength | Human review only | Includes checklist | Includes execution tests, counterexamples, and pass/fail criteria |
| Agent operability | Agent still needs extra explanation | Agent can perform common cases | Agent can perform, pause, escalate, and self-check from document alone |
| Commercial leverage | Useful internal doc | Repeatable delivery artifact | Packaged audit, build, validation, and maintenance offer |

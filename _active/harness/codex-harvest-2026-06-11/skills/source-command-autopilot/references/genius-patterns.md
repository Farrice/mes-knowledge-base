# Autopilot Genius Patterns

Reusable patterns for `/autopilot`, the low-friction front door for raw context, intent lock, planning, routing, and safe execution.

## Pattern 1: Intent Lock

Convert messy input into a compact operating brief before routing.

- Goal interpreted as: plain-English objective.
- Deliverable: artifact, decision, plan, draft, implementation, research, or workflow.
- Audience/User: who consumes or benefits.
- Success criteria: what "nailed it" means.
- Clarity Score: 0-100.
- Confidence: High, Medium, or Low.
- Ambiguity Map: execution-changing, quality-changing, or non-blocking.

## Pattern 2: Clarity Score

Score only what affects the ability to choose and execute the right path.

| Dimension | Points |
|-----------|--------|
| Deliverable is concrete | 20 |
| Audience/user is known | 15 |
| Context/source material is present | 15 |
| End state/success criteria are clear | 20 |
| Constraints, approvals, and risk are understood | 15 |
| Route/mode is obvious from the request | 15 |

Thresholds:

- 90-100: run.
- 75-89: run with assumptions unless the missing detail changes path, deliverable, risk, or approval boundary.
- 50-74: ask 1-3 targeted questions, then recalculate.
- 0-49: run full intent validation, present refined intent, and pause.

## Pattern 3: Ambiguity Map

Ask only when the ambiguity changes execution.

- Execution-changing ambiguity: deliverable, audience, route, file scope, approval boundary, external action, or success criteria. Ask.
- Quality-changing ambiguity: style, depth, examples, polish, reference quality, or taste direction. State an assumption and continue unless quality risk is high.
- Non-blocking ambiguity: optional preference or detail that can be improved after a first pass. Do not ask.

## Pattern 4: Plan Gate

Autopilot cannot toggle native Codex Plan Mode. It should emulate the useful planning behavior in its own workflow.

Decision logic:

1. Ground the request with local reads and router checks when needed.
2. Produce Intent Lock and Clarity Score.
3. If clarity is high, choose mode and start.
4. If ambiguity changes execution, ask the smallest useful question set.
5. If the user passes `--plan`, produce a decision-complete plan and stop before execution.
6. If execution is local, reversible, and inside the workspace, proceed after clarity is sufficient.
7. If execution requires approval, pause at the approval boundary.

## Pattern 5: Route, Gate, Verify, Evolve

Autopilot hides the arsenal behind a simple operating loop.

- Route: use command menu, workflow router, expert router, and compounds.
- Gate: attach only the useful quality, red-team, research, ground-truth, librarian, or evolution gate.
- Verify: name the exact machine checks, quality checks, or acceptance criteria.
- Evolve: if the same friction repeats, queue an evolution-agent or system-improvement route instead of treating it as a one-off annoyance.

## Pattern 6: Decision-Complete Plan

For meaningful work, the plan must lock:

- goal
- deliverable
- audience/user
- success criteria
- constraints and approvals
- in scope and out of scope
- chosen mode
- primary route
- support gates
- first safe action
- verification checks
- assumptions

For system work, include likely files or subsystems and exact validation commands.

For strategy, creative, content, client, or revenue work, include acceptance criteria, quality gate, and proof standard.

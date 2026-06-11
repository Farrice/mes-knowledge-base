# First Proof Demo - Codex Session Kickoff

## Demo Purpose

This proof demo shows the core claim behind the AI Operating Partner System:

> If the work is not agent-readable, the agent is forced to guess.

The internal workflow under test is `/session-kickoff`, because it is a clean example of hidden operating judgment. A human says, "I have an idea" or "let's build this," but the system has to decide:

- whether the request is Light, Standard, Deep, or Parallel
- which workflow stack should be used
- whether to use steering guidance
- what to verify
- whether true subagents are allowed
- what the next best fork is

Without a semantic work primitive, an agent can know the surface instruction "run session kickoff" and still miss the operating meaning.

## Source Asset Under Test

| Field | Value |
|---|---|
| Internal workflow | `.agent/workflows/session-kickoff.md` |
| Related primitives | `high-floor-operator-os.md`, `collaborative-steering-compass.md` |
| Offer proof use | Before/after demo for Agent-Ready Operating System Sprint |
| Buyer-facing analogy | "Your SOP may describe steps, but the agent still needs meaning, authority, validation, and escalation rules." |

## Controlled Before Baseline

This is the kind of instruction an AI agent often receives before the work has been made semantic:

```markdown
When a new session starts, run session kickoff. Figure out the task, choose the right workflow, and give the user useful next steps. If the task is complex, go deeper. Keep it concise.
```

That looks reasonable to a human. It is weak for an agent.

## Before Test

### Realistic User Task

```text
I have an idea for turning our internal AI knowledge system into a client-facing service. What should we do with it?
```

### Agent Interpretation From Baseline Only

The agent can infer:

- this is strategy or offer work
- the user wants next steps
- the answer should be helpful and concise

The agent cannot reliably know:

- whether this should default to Standard or Deep
- whether offer, proof, semantic-library, or steering workflows should be routed
- whether to create an artifact or only answer in chat
- whether to use client-facing proof discipline
- whether true subagents are allowed
- what counts as a shallow next path

### Likely Before Output

```markdown
You could turn this into a consulting offer, productized service, or internal workflow. I would start by defining the target customer, packaging the service, and creating a landing page. Then test it with a few prospects.
```

### Before Failure

The output is not wrong. That is the problem.

It is generically useful, but it does not operate at the level of the system:

| Failure | Why It Matters |
|---|---|
| No depth classification | The agent may treat revenue-critical work like casual brainstorming |
| No command routing | Existing offer, proof, semantic-library, and steering assets sit unused |
| No authority boundary | The agent may imply subagents or deeper routing happened when it did not |
| No proof discipline | It jumps to packaging before creating a believable before/after demo |
| Shallow next paths | The user learns little about how to steer the system next time |

## Semantic Work Primitive

# Session Kickoff Operating Route

## Purpose And Operating Definition

Session Kickoff Operating Route governs how an agent starts a Codex Antigravity session or major work sequence. The primitive is not "say hello" or "summarize the task." The work is to classify the operating depth, route the available arsenal, surface one useful steering prompt, and begin execution without making the user know the perfect command.

## When To Use

- A new conversation starts.
- The user begins a new workstream inside an existing session.
- The user brings an idea, source, offer, workflow, build request, client task, extraction, or system change.
- The user asks what to do next or what they may be missing.

## When Not To Use

- Simple factual lookup.
- Tiny rewrite.
- One-command check.
- Simple confirmation.
- User explicitly asks for a light answer.
- User explicitly asks not to receive planning, routing, or steering.

## Inputs

| Input | Required | Source Of Truth | Notes |
|---|---|---|---|
| User request | Yes | Current message | Classify the real work, not only the surface wording |
| Workspace boundary | Yes | `AGENTS.md`, `GEMINI.md`, current working directory | Do not modify the original Google Antigravity workspace |
| Depth rules | Yes | `semantic_libraries/antigravity/primitives/high-floor-operator-os.md` | Standard is the default unless clearly Light |
| Steering rules | Yes for Standard/Deep | `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md` | Use when it helps speed, quality, risk, or value |
| Available workflows | Yes for Standard/Deep | Command menu, workflow router, skill index | Route before producing high-stakes work |
| Subagent permission | Yes | User message and `AGENTS.md` | True Codex subagents require explicit user request for parallel/delegated work |

## Outputs

| Output | Format | Destination | Owner |
|---|---|---|---|
| Depth classification | Light / Standard / Deep / Parallel | Internal route or concise user update | Main assistant |
| Arsenal route | Workflow/skill/persona stack | Commentary or final when useful | Main assistant |
| Steering prompt | Best path, risk/opportunity, fastest decision | Kickoff or early work update | Main assistant |
| Work artifact | File or chat answer | Workspace or conversation | Main assistant |
| Verification evidence | Checks, validation output, limitations | Final response | Main assistant |

## Objects And Meaning

| Object | What It Means | Why It Matters |
|---|---|---|
| Light | Small, direct task | Avoids ceremony |
| Standard | Default operating tier | Prevents under-routing |
| Deep | Revenue-critical, client-facing, system-changing, ambiguous, or high-bar work | Triggers stack, critique, validation |
| Parallel | Explicit request for delegated subagents | Prevents generic hidden workers |
| Steering prompt | Short Operator Coach guidance | Helps the user learn how to steer without slowing work |
| No-Lazy-Path Gate | Minimum quality gate for Standard/Deep | Blocks generic one-pass output |

## Authority And Permissions

| Action | Agent May Do | Requires Approval | Never Do |
|---|---|---|---|
| Classify the depth tier | Yes | No | Do not call Standard/Deep work "simple" to move faster |
| Route local skills/workflows | Yes | No | Do not ignore relevant available workflows |
| Create or edit files in Codex Antigravity | Yes when requested or necessary | No, within workspace | Do not edit `/Users/farricecain/Google Antigravity` |
| Spawn true Codex subagents | Only after explicit parallel/delegated user request | Yes | Do not imply subagent work happened if it did not |
| Use external, paid, or network tools | Only if needed | Yes when sandbox, cost, privacy, or policy requires | Do not bypass approval |

## Execution Protocol

1. Interpret the user request and name the real work type.
2. Classify depth:
   - Light for factual lookup, tiny rewrite, simple confirmation, or one-command check.
   - Standard for most creative, strategy, extraction, offer, writing, client, workflow, and system work.
   - Deep for revenue-critical, client-facing, system-changing, ambiguous, or best/world-class requests.
   - Parallel only when the user explicitly asks for delegated agents or subagents.
3. For Standard or Deep, route local workflows and skills before producing the main output.
4. Use a compact steering prompt when it will improve speed, quality, risk, or value.
5. Begin execution. Do not stop at advice if the user asked for implementation.
6. Verify local/system claims when feasible.
7. Close with dense next-use guidance when useful.

## Decision Rules

| Condition | Rule | Reason |
|---|---|---|
| Request involves offer, proof, client work, or productization | Classify as Deep | Buyer trust and revenue are at stake |
| Request is "I have an idea" | Classify at least Standard | The user may not know the right command |
| Relevant workflow exists | Use it or explain why it is skipped | Prevents half-speed manual work |
| User asks for agents, subagents, parallel, swarm, or delegation | Use Parallel with explicit briefing packets | Keeps subagent chain clean |
| User asks to execute recommendations | Act, then report checks | Prevents planning loops |
| The output would affect future system behavior | Validate locally | Prevents hidden misalignment |

## Examples

### Good Example

User says:

```text
I have an idea for turning our internal AI knowledge system into a client-facing service. What should we do with it?
```

Agent route:

- Depth: Deep
- Best path: `/semantic-doc-productize` plus revenue offer, proof, and steering stack
- Watch: do not package before creating a before/after proof demo
- Fastest decision: choose one internal workflow to use as the demo source

### Counterexample

Agent says:

```text
You could make this a consulting offer, a product, or a workflow. Start with customer research and a landing page.
```

Why it fails:

- no depth classification
- no workflow route
- no proof artifact
- no system-specific steering
- no validation path

## Quality Tests

| Test | Pass Criteria | Failure Response |
|---|---|---|
| Depth clarity | The agent can explain why the task is Light, Standard, Deep, or Parallel | Reclassify before proceeding |
| Route use | Relevant workflows and skills are checked for Standard/Deep work | Run command/workflow routing |
| Steering density | Guidance includes best path, watch item, and fastest decision when useful | Rewrite steering block |
| Subagent integrity | No claim of subagent work unless explicit subagents were used | Correct the record and execute locally |
| Execution | If user asked to implement, an artifact or concrete output is produced | Create the asset or state the blocker |
| Verification | Local claims are checked when feasible | Run validation or mark limitation |

## Failure Modes

| Failure Mode | Early Signal | Prevention | Recovery |
|---|---|---|---|
| Generic kickoff | Advice could apply to any AI project | Route available workflows and name the specific stack | Re-run with Standard/Deep route |
| Over-ceremony | Light task gets a long kickoff | Apply Light tier | Answer directly |
| Hidden subagent leak | Assistant implies other agents worked | Explicit Parallel rule | Correct and continue locally |
| Shallow next paths | Closeout says "marketing, content, automation" | Use Use Now / Harden Next / Expand Value with artifact names | Rewrite closeout |
| Wrong workspace | Agent touches Google Antigravity | Workspace boundary check | Stop and move work back to Codex Antigravity |

## Maintenance Protocol

- Owner: Codex Antigravity operator.
- Review cadence: after user reports generic routing, weak steering, or uncertainty about how to use the system.
- Update triggers: new operating tiers, new workflow surfaces, repeated subagent confusion, or new proof-demo requirements.
- Last updated: 2026-05-06.

## After Test

### Same User Task

```text
I have an idea for turning our internal AI knowledge system into a client-facing service. What should we do with it?
```

### Agent Interpretation From Semantic Primitive

The agent can now identify:

- the work is productization and client-facing offer strategy
- depth should be Deep
- the likely stack is semantic-doc-productize, revenue offer, proof, and steering
- true subagents are not allowed unless explicitly requested
- the first proof gap is before/after evidence
- the right first artifact is a proof demo from one workflow

### Expected After Output

```markdown
Depth: Deep. Best path: package this through `/semantic-doc-productize`, but do not polish the offer first. The trust gap is proof.

Use Now: pick one internal workflow and create a before/after proof demo.
Harden Next: run `/semantic-doc-validator` against the semantic primitive and record where the agent still guesses.
Expand Value: turn the demo into the first sales asset for the Agent-Ready Operating System Sprint.
```

## Semantic Document Validation

### Verdict

PASS

### Execution Result

| Field | Result |
|---|---|
| Task attempted | Classify and route a vague productization idea at session kickoff |
| Agent could execute from document alone | Yes |
| Clarifications required | None for route; buyer/workflow choice may be requested only if execution needs a specific source |
| Boundary respected | Yes: no true subagents unless explicitly requested; no Google Antigravity edits |

### Gaps Found

| Gap | Severity | Fix |
|---|---|---|
| No live buyer outcome data yet | Medium | Use this as internal proof, not external client case study |
| No numeric before/after timing data | Medium | Add timing and clarification-count metrics after a live run |
| Source workflow is internal and technical | Low | Explain it through the buyer analogy: SOP steps versus agent-readable meaning |

### Revised Acceptance Criteria

This proof demo can be used in sales if it is framed as an internal demonstration, not a client result. It becomes stronger after one live client or prospect workflow adds measurable before/after evidence.

## Buyer-Facing Demo Script

Use this on a sales call or in a short Loom:

1. "Here is a normal workflow instruction. It tells the agent what to do, but not how to reason about the work."
2. "When we test it, the answer is not terrible. It is the kind of generic answer that creates rework."
3. "Now here is the same workflow converted into a semantic work primitive."
4. "Notice what changed: purpose, when to use it, when not to use it, inputs, authority, decision rules, examples, tests, failure modes, and maintenance."
5. "Now the agent can route the work, know when to go deep, avoid pretending subagents were used, and tell the human the next best fork."
6. "That is the difference between documentation and an agent-ready operating layer."

## Sales Page Proof Block

Before, the agent received a reasonable instruction: run session kickoff, choose the right workflow, and give useful next steps.

The result was technically acceptable and strategically weak. It could answer, but it had to guess the operating standard, the depth tier, the available workflow stack, the proof requirement, and the subagent boundary.

After converting the workflow into a semantic work primitive, the agent could classify the task, route the stack, identify the proof gap, preserve the subagent rule, and recommend the next artifact without needing hidden explanation.

This is the core of the Agent-Ready Operating System Sprint: make the work legible enough that AI can execute with boundaries instead of guessing with confidence.

## What This Proves

| Claim | Proof Strength | Evidence |
|---|---|---|
| Semantic docs reduce agent guessing | Strong internal demo | Before baseline lacks authority, validation, and decision rules; semantic primitive supplies them |
| The service is not just documentation | Strong internal demo | The output changes routing, behavior, authority, and validation |
| The offer needs before/after proof | Strong strategic proof | The demo creates a visible asset that can be shown to buyers |
| Buyer outcomes need external validation | Honest limitation | No client time savings, revenue impact, or adoption metric yet |

## How To Use This Asset

| Use Case | How To Use |
|---|---|
| Sales call | Walk through the before instruction, before failure, semantic primitive, and after output |
| Landing page | Use the Sales Page Proof Block |
| Outreach | Offer to run the same before/after on one prospect workflow |
| Delivery | Use the Semantic Work Primitive as the model for client workflow conversion |
| Internal training | Show why Standard/Deep work must be routed, not answered generically |

## Next Proof Upgrade

The next proof demo should use a less technical workflow, ideally:

- a client onboarding SOP
- a content approval workflow
- a sales call follow-up process
- a proposal drafting workflow
- a failed AI output from a real prospect

That will make the proof easier for buyers to feel in their own business.

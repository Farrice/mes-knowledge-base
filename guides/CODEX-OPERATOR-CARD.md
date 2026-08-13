---
date: 2026-08-13
session: codex-operator-card
tier: operator-guide
status: enriched
---

# Codex Operator Card

> Your daily interface to Google Antigravity. The system can hold thousands of capabilities without making you memorize them. Start with the outcome. Use a command only when it makes the route clearer.

## The six front doors

| Front door | Use it when | What Codex should do |
|---|---|---|
| **Natural language** | You know the outcome but not the system route | Interpret the job, choose one owner, load the smallest relevant skill/workflow stack, execute the next safe step, and show the route receipt |
| **`/go`** | Your thoughts are messy, strategic, cross-domain, or mission-sized | Translate the raw intent into a mission card, choose one conductor, sequence dependencies, and begin safe execution |
| **`/arsenal`** | You suspect something already exists | Search skills, workflows, agents, and commands; identify the exact asset to reuse; stop duplicate building |
| **`/system-audit`** | Codex feels cluttered, misrouted, inconsistent, or “built but not firing” | Inspect routing, hooks, bridges, activation, telemetry, and verifiers; separate structural health from actual firing |
| **`/repeatability-spine`** | A revision got worse or a great result cannot be repeated | Preserve the good example, identify the primary failure, make the smallest repair, and create a replay/regression guard |
| **`/end-session`** | Meaningful work is complete or needs a durable handoff | Verify what shipped, save exact retrieval context, preserve unfinished work, and close without unsafe Git or cleanup |

## Which door do I use?

```text
I know the outcome, not the route
└── Describe it naturally

My thoughts are messy or the work spans several systems
└── /go

I think we already built something for this
└── /arsenal

The operating system itself feels wrong
└── /system-audit

The new version lost what made the old version good
└── /repeatability-spine

The work is finished or needs a clean stopping point
└── /end-session
```

## Expert front door or exact workflow?

### Invoke an expert or skill front door

Use `/expert-name` or a domain front door when you know **whose department** owns the problem but want Codex to select the process.

> `/oren-identity help me choose the right identity-brand move for this founder`

Codex should load the skill's shared methodology, inspect its workflow menu, and route to the smallest fitting process.

### Invoke a workflow directly

Use `/workflow-name` when you already know **the exact deliverable**.

> `/true-fan-density-engine build the 90-day participation and return-behavior plan`

Direct invocation skips diagnosis. It is faster, but only when you are sure the named workflow matches the job.

## The operating rule

```text
Outcome
  -> one function owner
  -> one skill family
  -> one workflow with bounded support
  -> verified deliverable
```

- **Skill** = reusable capability family: methodology, references, quality standards, and related workflows.
- **Workflow** = one executable process with defined inputs, steps, output, and quality gate.
- **Slash command** = a launcher. It may open a skill, run a workflow, or call a control utility.
- **Plugin** = an installable distribution bundle. It does not make the underlying method smarter.

## What you should not have to do

- Memorize thousands of slash commands.
- Choose from a menu of experts before Codex understands the job.
- Ask which internal files need loading.
- Rebuild a capability because you forgot its exact command name.
- Treat a green local verifier as human acceptance, market behavior, or revenue proof.

## Paste this when routing feels uncertain

> I will describe the outcome naturally. Choose one function owner, load the smallest correct skill and workflow, tell me the route in one line, execute the next safe local step, and keep build proof, human acceptance, market behavior, and revenue as separate evidence states.

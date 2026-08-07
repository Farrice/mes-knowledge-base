# Virtuoso Orchestration User Guide

## What This Is

`/virtuoso` is the deploy-at-will orchestration front door for Codex Antigravity.

Use it when you have a goal, raw context, a messy idea, a stuck project, a high-stakes deliverable, or a domain you do not want to manually route through commands, agents, skills, and workflows.

The command does three things:

1. Chooses the best owner route.
2. Shows the full blend before work starts.
3. Executes the first safe local action unless you ask for trace-only.

It is not a replacement for Autopilot, Mission, System Audit, Orchestrate, Expert Composition Governor, or Source-to-skill-system. It is the conductor that chooses which of those should own the job.

## The Basic Command

```text
/virtuoso [your goal]
```

Examples:

```text
/virtuoso help me make $1,000 fast with what we already have
/virtuoso audit the system and tell me what is not firing
/virtuoso turn this messy idea into the best next execution path
/virtuoso build a launch plan for this offer
/virtuoso create a client-facing research-backed content package
```

Use this when you want the system to choose the best route and start the first safe local action.

## The Main Modes

```text
/virtuoso --trace-only [goal]
```

Use this when you want to inspect the route before any work happens.

```text
/virtuoso --delegate [goal]
```

Use this when you want subagent-style decomposition. This prepares worker packets and receipts, but it does not spawn real Codex subagents without explicit approval.

```text
/virtuoso --log [goal]
```

Use this when the route is real and worth teaching the routing intelligence layer.

```text
/virtuoso --mode revenue [goal]
/virtuoso --mode creative [goal]
/virtuoso --mode research [goal]
/virtuoso --mode build [goal]
/virtuoso --mode audit [goal]
/virtuoso --mode repair [goal]
```

Use a mode when your raw context is broad and you want to bias the system toward a lane without bypassing the owner/gate system.

## Best Default Pattern

For raw context, use:

```text
/virtuoso --mode [lane] [raw context]
```

If you do not know the lane, use:

```text
/virtuoso [raw context]
```

If the stakes are high, use:

```text
/virtuoso --trace-only [raw context]
```

Then run the recommended follow-up once the trace looks right.

## When To Use Each Mode

| Mode | Use when | Example |
|---|---|---|
| auto | You want the system to choose | `/virtuoso here is my messy idea...` |
| revenue | Money, clients, offers, products, marketplace, cash | `/virtuoso --mode revenue help me make $1,000 fast` |
| creative | Content, copy, design, campaign, taste, originality | `/virtuoso --mode creative make this launch concept remarkable` |
| research | Current facts, market proof, competitor evidence, claims | `/virtuoso --mode research validate this opportunity` |
| build | Skills, workflows, slash commands, plugin surfaces, implementation | `/virtuoso --mode build turn this into a reusable command` |
| audit | System health, broken behavior, not firing, route proof | `/virtuoso --mode audit audit the harness` |
| repair | Regression, failed revision, lost good part, repeatability | `/virtuoso --mode repair fix why this got worse` |

## How To Read The Trace

### Route

The primary workflow that should own the work.

Example:

```text
Route: /first-10k
```

This means the First $10K revenue system owns the job.

### Owner

The accountable function. This prevents expert soup.

Example:

```text
Owner: First 10K Revenue System
```

The owner integrates the work. Other routes may support it, but they do not own it.

### Stack

The expert lens or compound pairing.

Important: this does not mean agents were deployed. It means the system found a useful lens.

Read this as:

```text
These are the expert patterns being applied.
```

Not:

```text
These are separate workers that ran.
```

### Support Gates

Support gates are workflows or checks that may shape, verify, or constrain the work.

Important: a support gate listed in the trace is considered, not automatically executed.

Only the Execution Receipt tells you what actually ran.

### Delegation

This tells you whether subagent packets were prepared.

If you see:

```text
real_subagents_spawned=False
```

then no real Codex subagents were spawned.

If you want actual delegated workers, ask explicitly:

```text
/virtuoso --delegate [goal], and I approve real Codex subagents only after you show the delegation packet.
```

### Plugin/Tool Surface

This shows relevant tool/plugin readiness.

It means:

```text
These tools or plugin surfaces were considered or are available.
```

It does not mean they were used unless they appear in Executed scripts/workflows.

### Execution Receipt

This is the most important section.

It separates:

- considered gates
- loaded context
- selected workflow
- executed workflows
- executed scripts
- skipped gates
- expert lenses applied
- subagent packets prepared
- real subagents spawned
- external actions

Trust the receipt over the trace if you are asking, "What actually happened?"

## The One Rule That Prevents Confusion

Trace means:

```text
Here is what the system selected, considered, and plans.
```

Receipt means:

```text
Here is what actually ran.
```

If a route appears under Support Gates, it was considered.

If it appears under Executed Workflows or Executed Scripts, it ran.

## Starting From Raw Context

Paste the messy context and ask Virtuoso to choose:

```text
/virtuoso I have a bunch of scattered ideas. I want to make money quickly, maybe through skills, maybe LinkedIn, maybe a digital product. I do not know the route. Choose the best owner and start the first safe local action.
```

Better:

```text
/virtuoso --mode revenue I have a bunch of scattered ideas. I want to make $500-$1,000 as quickly as possible using our skills, workflows, and plugin assets. Choose the best owner and start the first safe local action.
```

Best when stakes are high:

```text
/virtuoso --trace-only --mode revenue [raw context]
```

Then:

```text
Use this trace. Execute the first safe local action and update the Execution Receipt.
```

## Best High-Leverage Use Cases

### 1. Fast Revenue From Raw Ideas

Use when you want money quickly and do not know the best lane.

```text
/virtuoso --mode revenue help me make $1,000 fast using our existing assets, offers, skills, and plugin packages
```

Expected owner:

- `/first-10k`
- `/service-first-productization`
- `/revenue-offer-agent`
- `/plugin-readiness-audit` when plugin packaging is central

Best output:

- offer decision
- paid proof path
- first artifact to build
- manual outreach or marketplace path
- proof capture loop

### 2. Skill Or Plugin Productization

Use when you want to turn a workflow into a sellable skill, command, or plugin.

```text
/virtuoso --mode build turn this workflow into a reusable skill package with tests and install guidance
```

Expected owner:

- `/source-to-skill-system`
- `/plugin-readiness-audit`
- `/extraction-governor-agent`

Best output:

- build shape
- duplicate-system check
- command bridge decision
- validation plan
- package readiness verdict

### 3. System Audit And Harness Repair

Use when something feels broken, slow, duplicated, or not firing.

```text
/virtuoso --mode audit audit why the system is not blending agents and workflows correctly
```

Expected owner:

- `/system-audit`

Best output:

- control-plane finding
- route proof
- severity ranking
- verifier-backed repair path

### 4. Failed Revision Recovery

Use when the new version got worse or lost the good part.

```text
/virtuoso --mode repair this revision got worse; preserve what worked and fix the failure
```

Expected owner:

- `/repeatability-spine`

Best output:

- preservation lock
- failure class
- repair route
- regression guard
- replay prompt

### 5. High-Stakes Client Deliverable

Use when the output must be polished, strategic, and not generic.

```text
/virtuoso --mode creative build a client-facing strategy brief from this messy context
```

Expected owner depends on domain, but the trace should show:

- one owner
- bounded composition
- proof gate
- publishable-copy or quality gate if public-facing

Best output:

- client-ready artifact
- quality checks
- proof and assumptions
- next action

### 6. Deep Research Or Market Proof

Use when facts, trends, claims, or competitor data matter.

```text
/virtuoso --mode research validate whether this offer has market demand and identify the fastest proof path
```

Expected owner:

- research route
- market intelligence route
- ground-truth/fact-verifier support

Best output:

- evidence ledger
- claim confidence
- gaps
- source-backed recommendation

### 7. Full-Arsenal Composition Without Expert Soup

Use when you want the full system, but do not want a messy pile of experts.

```text
/virtuoso --delegate use the full arsenal on this objective, but keep one owner and show the delegation packets before real subagents
```

Expected behavior:

- one owner
- Composition Ledger
- subagent packet candidates
- no real subagents unless approved

### 8. Landing Page, Offer, Or Launch Build

Use when you need a concrete commercial asset.

```text
/virtuoso --mode build create the offer page, intake flow, and launch checklist for this service
```

Expected output:

- selected build route
- copy/claim gate
- first local artifact
- approval gates before publishing/payment links

### 9. Daily Operator Control

Use at the start of a day or session.

```text
/virtuoso here is everything in my head today: [paste]. Choose the highest-leverage path and start the first safe local action.
```

Best output:

- route
- owner
- first action
- what to ignore
- next prompt

### 10. Plugin Readiness And Fresh-Context Packaging

Use when you want a workflow family to become portable.

```text
/virtuoso --mode build assess whether this should become a plugin, slash command, workflow, or skill
```

Expected owner:

- `/plugin-readiness-audit`
- `/source-to-skill-system`
- `/extraction-governor-agent`

Best output:

- package-now / harden-first verdict
- fresh-context test
- plugin acceptance criteria
- no marketplace/global write without approval

## Decision Cheatsheet

| Situation | Command |
|---|---|
| I have raw messy context | `/virtuoso [paste context]` |
| I want money fast | `/virtuoso --mode revenue [goal]` |
| I want a system/skill/workflow built | `/virtuoso --mode build [goal]` |
| I want proof before action | `/virtuoso --trace-only [goal]` |
| I want subagent-style decomposition | `/virtuoso --delegate [goal]` |
| I want to teach routing from this decision | `/virtuoso --log [goal]` |
| Something broke | `/virtuoso --mode audit [problem]` |
| A revision got worse | `/virtuoso --mode repair [problem]` |
| I need current evidence | `/virtuoso --mode research [question]` |
| I need high-taste output | `/virtuoso --mode creative [goal]` |

## What To Approve Manually

Virtuoso should stop before:

- publishing
- sending DMs or outreach
- using paid/API tools
- connector writes
- global mirrors
- destructive cleanup
- editing `/Users/farricecain/Google Antigravity`
- Mission mutation
- spawning real Codex subagents

If the system asks for approval, it should name the exact boundary.

## What Good Output Looks Like

A good `/virtuoso` run should leave you knowing:

- what workflow owns the job
- why that route won
- what support gates were considered
- what expert lens shaped the work
- whether any subagent packet was prepared
- what actually executed
- what remains blocked by approval
- what to do next

If you do not see that, ask:

```text
Rerun the Virtuoso Trace and separate considered gates from executed workflows/scripts.
```

## Recommended Operating Habit

Use `/virtuoso` when you are thinking:

> I know what I want, but I do not want to manually choose the command stack.

Use `/autopilot` when you are thinking:

> I need the system to interpret my messy intent and just begin.

Use `/orchestrate` when you are thinking:

> I want a menu of options before choosing.

Use `/mission` when you are thinking:

> This needs continuity, milestones, and a durable operating contract.

Use `/system-audit` when you are thinking:

> The harness itself may be broken.

Use `/source-to-skill-system` when you are thinking:

> This should become a reusable skill, workflow, command, or system.

## The Best Next Move

When in doubt, paste raw context into:

```text
/virtuoso --trace-only [raw context]
```

Then ask:

```text
Execute the first safe local action and update the Execution Receipt.
```

That gives you control without forcing you to remember magic words.

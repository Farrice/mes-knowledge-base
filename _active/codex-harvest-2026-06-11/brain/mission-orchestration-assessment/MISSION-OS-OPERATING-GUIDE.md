# Mission OS Operating Guide

## What You Just Built

`/mission` is the top-level control surface for important work.

It makes the system slow down before execution just enough to answer:

1. What are we trying to accomplish?
2. What existing knowledge, agents, skills, and workflows should we use first?
3. What would prove this worked?
4. Which subject agents should do the work?
5. What should be handed off, validated, and saved?

The goal is not to spawn more agents. The goal is to make the right agents work from the right context with a clear validation contract.

## The Default Flow

Use this when the work matters and could become reusable.

```text
/mission [objective]
```

Then the system should run:

1. Score and clarify the objective.
2. Route commands, workflows, experts, and context.
3. Fire Knowledge Librarian if reusable knowledge or overlap is involved.
4. Build a mission charter.
5. Define the validation contract before work begins.
6. Pick subject agents and workflows.
7. Execute one milestone at a time.
8. Require handoffs.
9. Validate with scrutiny and user-outcome checks.
10. Save the useful lesson or artifact.

Mission state updates should happen one at a time. Do not update a handoff, librarian checkpoint, and status at the same moment for the same mission.

## When The Knowledge Librarian Should Fire

The librarian should fire whenever the work involves:

- a book, video, transcript, article, framework, course, or expert source,
- a new skill, workflow, command, agent, SOP, client asset, or repeatable system,
- possible overlap with something already in the library,
- uncertainty about which command or skill to use,
- a desire to make the output reusable instead of a one-off answer.

The librarian answers:

- What do we already have?
- What should we use first?
- Is this new thing standalone, companion, extension, or reference-only?
- What sleeping assets are relevant?
- What command should start the work?

## Personal Workflow

Use for planning your week, learning something, organizing life/admin, building habits, or making a personal operating system.

```text
/mission Build my personal weekly planning and execution system for the next 30 days.
```

Expected flow:

1. Librarian checks for relevant personal systems, planning workflows, and underused skills.
2. Orchestrator creates a simple charter: goal, constraints, current chaos points, desired end state.
3. Subject agents might include productivity, writing, personal strategy, or quality judge.
4. Validation contract defines proof: weekly plan exists, daily loop is usable, review cadence is clear, friction is low.
5. Worker builds the system.
6. Validator checks if it is actually usable in your real week.
7. Handoff gives you the exact daily loop.

Start command:

```text
/mission Build my personal operating loop for this week around money, health, learning, and client-building.
```

## Creative Workflow

Use for content, brand worlds, design concepts, playbooks, writing systems, or creative campaigns.

```text
/mission Build a 30-day content campaign around my new AI service offer.
```

Expected flow:

1. Librarian surfaces existing content, offer, voice, positioning, and campaign commands.
2. Orchestrator builds the campaign charter.
3. Subject agents might include Content & Media Agent, Messaging & Positioning Agent, Copywriting Agent, Creative Design Agent, and Quality Judge.
4. Validation contract defines proof: clear audience, strong belief shift, platform-native ideas, no generic content, production-ready assets.
5. Workers build angles, posts, scripts, creative briefs, and distribution plan.
6. Validators check originality, clarity, usefulness, and fit to your voice.
7. Handoff gives the posting sequence and next production steps.

Start command:

```text
/mission Turn this idea into a 30-day content engine with posts, scripts, lead magnet angle, and offer bridge.
```

## Client Workflow

Use for paid audits, client onboarding, delivery packages, strategy builds, proposals, and implementation sprints.

```text
/mission Build a client-ready AI Business Asset Audit for [client/company].
```

Expected flow:

1. Librarian checks for relevant client delivery, audit, offer, proof, and implementation workflows.
2. Orchestrator creates the client mission charter.
3. Subject agents might include Client Delivery Agent, Revenue & Offer Agent, Research Intelligence Agent, Messaging & Positioning Agent, and Red Team Agent.
4. Validation contract defines proof: client problem is clear, recommendations are specific, risk is named, next actions are obvious, output is presentable.
5. Worker creates the audit.
6. Validator checks whether a real client would understand and value it.
7. Red Team catches weak claims or generic strategy.
8. Handoff gives the client-ready asset plus follow-up implementation pitch.

Start command:

```text
/mission Create a paid AI Business Asset Audit for this client from their website, offer, and current content.
```

## Source-To-System Workflow

Use when you watch a video, read a book, find a framework, or discover an expert system you want to add to Antigravity.

```text
/mission Turn this source into a usable Antigravity capability: [link or file]
```

Expected flow:

1. Extraction Governor decides whether this is extract, forge, companion skill, workflow, reference, agent, or business asset.
2. Knowledge Librarian checks overlap with the existing library.
3. Orchestrator creates the mission charter and validation contract.
4. Worker extracts the core operating method.
5. Worker builds the skill, workflow, bridge, or reference.
6. Validator checks command discoverability, registry sync, and output quality.
7. Final handoff gives you the exact commands and first use cases.

Start command:

```text
/mission Turn this YouTube video into a reusable skill/workflow system, but first check whether we already have something similar.
```

## How To Think About The Agent Roles

- Orchestrator: decides the plan and keeps the mission from drifting.
- Knowledge Librarian: checks what already exists and prevents shelfware.
- Extraction Governor: decides what a source should become.
- Subject agent: performs the specialized work.
- Validator: checks the work against the contract.
- Red Team or Quality Judge: challenges weak thinking before you rely on it.

## The Minimum Good Mission

A good mission has:

- a clear objective,
- a librarian decision when reusable knowledge is involved,
- a validation contract before work starts,
- a subject-agent roster,
- milestone boundaries,
- handoffs,
- verification,
- a clear next action.

If those are present, the system is working as intended.

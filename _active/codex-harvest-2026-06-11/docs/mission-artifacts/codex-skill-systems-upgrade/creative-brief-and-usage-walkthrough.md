# Codex Skill Systems Upgrade: Creative Brief And Usage Walkthrough

## One-Line Brief

Turn Codex Antigravity from a migrated command catalog into a Codex-native operating system that routes raw intent into grounded, orchestrated, validated skill systems without requiring Farrice to remember magic words.

## Strategic Objective

The goal of this upgrade is not to add another command. The goal is to make Codex behave like a better operator:

- it should understand when a source should become a reusable system
- it should choose the right route before building
- it should keep core front doors visible and keep the massive command library cold
- it should ground source work in local evidence
- it should produce contracts, handoffs, checkpoints, and validation instead of loose recommendations
- it should improve the harness without relying on Claude or Gemini files as active authority

## Audience

### Primary User

Farrice, using Codex Antigravity as a durable build environment for skills, workflows, source extraction, creative systems, client systems, and reusable operating layers.

### Internal Operator

Codex, acting as the native operator of this workspace. Codex now has an active control plane through `CODEX.md`, `AGENTS.md`, `.agent/workflows/`, `.agents/skills/source-command-*`, and deterministic scripts in `execution/`.

### Future Collaborators

Any future assistant, workflow, or system pass that needs to understand why this workspace should not treat every migrated Claude command as an equal active route.

## Starting Problem

The old system had power, but the power was scattered.

The migration preserved many useful commands, workflows, skills, expert files, and Claude-era structures. That gave the workspace a huge arsenal, but it also created three operating risks:

1. **Routing pressure**: too many migrated wrappers could appear equally important, even when most should stay cold.
2. **Authority confusion**: `GEMINI.md` and `CLAUDE.md` still had enough language to look like primary operating specs even though this workspace is now Codex-native.
3. **One-step skill bias**: source extraction could produce useful components, but not always a full system with step order, handoffs, validation, and a user-facing operating surface.

The Simon Scrapes video named the right diagnosis: generic skills can be bloated, context-thin, and built one task at a time. The fix is not "bigger skills." The fix is small components wired into end-to-end systems.

## New Positioning

Codex Antigravity is now positioned as:

> A Codex-native skill system operating layer that turns sources, raw ideas, and strategic goals into routed, grounded, validated workflows.

That means the workspace should feel less like:

> "Which of these hundreds of commands should I remember?"

And more like:

> "Drop the source or goal. Codex chooses the route, proves the route, builds the right-sized system, and leaves a reusable path behind."

## Core Belief Shift

Before this upgrade, the hidden belief was:

> More skills and more command wrappers make the system more capable.

After this upgrade, the operating belief is:

> Capability comes from the right front doors, small focused components, explicit handoffs, and validation.

This is the practical mental model:

```text
Raw source or goal
-> route check
-> build-shape decision
-> skill system contract
-> implementation
-> validation
-> starter route
-> reuse hook
```

## Category Pattern Break

Most agent and skill setups become more confusing as they grow. They expose too much, preload too much, and make the user responsible for orchestration.

This upgrade deliberately breaks that pattern:

- **Do not make every migrated command hot.**
- **Do not delete legacy material prematurely.**
- **Do not let Claude/Gemini docs drive Codex routing.**
- **Do not build giant all-purpose skills.**
- **Do make a few front doors excellent.**
- **Do put the larger archive behind routers and menus.**
- **Do require contracts for end-to-end systems.**

The creative choice is restraint. The system gets stronger because fewer things are treated as first-class at once.

## Active Control Plane

Use this hierarchy as the expectation for how Codex should operate now:

1. System, developer, tool, and user instructions.
2. `AGENTS.md` and `CODEX.md` for this workspace.
3. `.agent/workflows/` and `.agents/skills/source-command-*` for active routing.
4. `execution/` scripts for deterministic checks, routing, registries, validation, and ledgers.
5. `GEMINI.md`, `CLAUDE.md`, and `.claude/commands/` as legacy/source references only.

The big behavioral expectation: Codex should no longer read `GEMINI.md` or `CLAUDE.md` as the main instruction spine unless you explicitly ask to inspect or back-port model-specific behavior.

## Hot Routes

These are the routes you should expect Codex to favor:

| Route | Use When | Expected Output |
|---|---|---|
| `/autopilot` | You have raw context, a messy ask, or no idea which route fits | Intent lock, route decision, safe execution, steering |
| `/source-to-skill-system` | A source should teach the OS, orchestration, skills, workflows, or end-to-end capability design | Source package, build-shape decision, system contract, validation, starter route |
| `/extraction-governor-agent` | A source may become a skill, workflow, reference, agent, system, companion layer, or no build | Build-shape decision and extraction path |
| `/mission` | The work is multi-step, durable, stateful, high-stakes, or system-changing | Mission plan, state, checkpoints, validation, handoff |
| `/self-evolve` | Something failed or a workflow should improve from evidence | Patch plan, improvement, regression proof |
| `/skill-anneal` | A skill exists but needs tightening, de-bloating, or better reliability | Skill repair, tests, updated usage rules |
| `/orchestrate` or command menu | You want options or route discovery instead of immediate execution | Ranked command/workflow options |

## Cold Surface

The broad migrated command library still exists. That is good. It is source material and compatibility coverage.

But you should not expect Codex to advertise every migrated command as a first-class starting point. The larger command library should live behind:

- `execution/command_menu.py`
- `execution/workflow_router.py`
- targeted skill loads
- explicit user invocation

This keeps the system from drowning in its own arsenal.

## How To Use It Now

### 1. When You Have A Source That Feels Important

Use this when a video, book, article, podcast, post, transcript, or raw method feels like it could improve the system.

Prompt:

```text
Run /source-to-skill-system on this source: [URL or file].
Decide whether it should become a component skill, workflow, skill system, companion OS layer, reference, or no build.
Ground it in evidence, create the contract, and validate the route.
```

What should happen:

- Codex captures or reads the source.
- It separates observed evidence from inference and unavailable evidence.
- It checks existing routes before building.
- It decides the build shape.
- If it is a system, it fills the Skill System Contract.
- It creates the minimum durable surface.
- It validates routing and cold-start use.

Quality bar:

- no hidden chat dependence
- source paths included
- clear build-shape decision
- explicit validation
- starter route at the end

### 2. When You Have A Messy Raw Idea

Use `/autopilot` or simply drop the raw idea and ask Codex to route it.

Prompt:

```text
Autopilot this. I do not know the right route yet. Identify the intent, choose the workflow, and start the safest useful execution path.
```

What should happen:

- Codex names the likely intent.
- It gives a clarity score or ambiguity map when useful.
- It chooses the route.
- It only asks questions if ambiguity changes execution.
- It executes locally when safe.

Quality bar:

- you should not need to remember the command
- the chosen route should be visible
- the next artifact should be obvious

### 3. When Something Feels Broken Or Underpowered

Use `/self-evolve` when the system behavior failed. Use `/skill-anneal` when a specific skill feels bloated, vague, too generic, or unreliable.

Prompt:

```text
This workflow did not hit right: [describe failure].
Use self-evolve or skill-anneal as appropriate. Patch the system and run the regression proof.
```

What should happen:

- Codex uses failure evidence, not vibes.
- It patches the smallest responsible surface.
- It adds or updates a guard if the issue could recur.
- It runs verification.

Quality bar:

- one failure becomes one durable improvement
- no broad refactor unless the evidence demands it

### 4. When The Work Is Big Enough To Need Governance

Use `/mission` when the work has state, milestones, reusable knowledge, client-facing risk, or several dependent parts.

Prompt:

```text
Run this as a mission. Define the outcome, checkpoints, validation, handoffs, and first executable milestone.
```

What should happen:

- Codex creates or updates mission state.
- It uses contracts and validation rather than an open-ended plan.
- It keeps a handoff trail so work can resume cleanly.

Quality bar:

- no loose "we should" plan
- every milestone has proof
- the mission can survive context loss

### 5. When You Just Want To Find The Right Existing Tool

Ask naturally.

Prompt:

```text
Find the best existing route for this before building anything new: [goal].
Show me the top options and your recommended route.
```

What should happen:

- Codex checks the command menu, workflow router, and relevant context.
- It recommends a route.
- It explains why the route fits.
- It avoids creating duplicate skills.

Quality bar:

- reuse before new build
- route decision is explainable

## What You Should Expect From Codex Now

### Codex Should

- Treat `CODEX.md` as the active harness spec.
- Treat `GEMINI.md` and `CLAUDE.md` as legacy references.
- Keep `/autopilot`, `/mission`, `/source-to-skill-system`, and `/extraction-governor-agent` hot.
- Keep the giant command catalog cold behind routers.
- Decide build shape before building.
- Use source evidence packages for source work.
- Separate observed, inferred, and unavailable evidence.
- Build contracts for end-to-end systems.
- Use handoff summaries between steps.
- Run validation after system, router, workflow, skill, or bridge changes.
- Ask fewer questions when the execution path is clear.
- Ask for approval before destructive, external-facing, paid, or delegated actions.

### Codex Should Not

- Treat every old slash command as equally important.
- Route from Claude/Gemini docs as the active control plane.
- Create a new skill before checking existing routes.
- Merge visual assumptions into transcript evidence.
- Spawn real Codex subagents unless you explicitly authorize subagents or parallel delegation.
- Delete `.claude/commands/` or other legacy references without a separate cleanup mission.
- Pretend background autonomy exists unless an automation or recurring job has been created.

## What This Does Not Mean

This does not mean the system is now fully autonomous in the background.

It means that when you invoke Codex, the harness has a better operating spine:

- better routing
- better source grounding
- better context control
- better reusable system design
- better validation
- fewer scattered one-off outputs

If you want it to monitor, recur, or continue later without you, that still needs an explicit automation or heartbeat.

## Output You Should Ask For

For a new source-to-system run, ask for this result shape:

```text
Give me:
1. Source evidence package
2. Build-shape decision
3. Skill System Contract
4. Components and step order
5. Human checkpoint
6. Validation proof
7. Starter route
8. Reuse hook
```

For a system repair run, ask for this:

```text
Give me:
1. Failure evidence
2. Responsible surface
3. Patch
4. Regression guard
5. Proof command
6. Updated usage expectation
```

For route discovery, ask for this:

```text
Give me:
1. Top route candidates
2. Why each fits
3. Recommended route
4. What it will produce first
5. What validation proves it worked
```

## First Seven Uses

Use this sequence to make the upgrade real:

1. Run one new source through `/source-to-skill-system`.
2. Run one messy raw idea through `/autopilot`.
3. Ask Codex to route one old command request before building anything.
4. Pick one existing skill that feels bloated and run `/skill-anneal`.
5. Pick one workflow that failed recently and run `/self-evolve`.
6. Run one durable multi-step project through `/mission`.
7. Ask for a cold-start proof on the pilot system.

## Example Prompts

### Source To System

```text
Run /source-to-skill-system on this video: [URL].
Use the new skill-system contract. I want a reusable Codex-native system, not just notes.
```

### Raw Idea

```text
Autopilot this raw idea and choose the right route. If it should become a system, use the skill-system contract.
```

### Repair

```text
This skill is too generic and bloated: [skill].
Run skill-anneal. Tighten it, preserve what works, and validate it.
```

### Workflow Failure

```text
This workflow failed in this way: [failure].
Run self-evolve, patch the responsible surface, and add a regression guard.
```

### Route Before Build

```text
Before creating anything new, search the existing command menu and workflow router for the best route for: [goal].
Then recommend the path and execute if safe.
```

## Operating Scorecard

Use this scorecard to judge whether the system is operating correctly.

| Standard | Passing Behavior |
|---|---|
| Authority clarity | Codex uses `CODEX.md` and `AGENTS.md` first |
| Source grounding | Evidence package or file paths are named |
| Build-shape decision | Codex says component, reference, workflow, system, companion layer, or no build |
| Context control | Only relevant components are loaded |
| Handoffs | Outputs from one step become clear inputs for the next |
| Checkpoints | Approval appears where risk changes |
| Validation | Checks or proof commands are run after structural changes |
| Reuse | The result leaves behind a route, contract, primitive, workflow, or state update |

## Proof Assets Already In Place

- `CODEX.md`
- `semantic_libraries/antigravity/primitives/skill-system-contract.md`
- `.agent/workflows/source-to-skill-system.md`
- `.agents/skills/source-command-source-to-skill-system/SKILL.md`
- `.claude/commands/source-to-skill-system.md`
- `extractions/video-context/FD53kEpLh9c/`
- `execution/verify_codex_authority.py`
- `execution/verify_skill_system_contract.py`

## Best Current Command

Use this as the default next move:

```text
/source-to-skill-system [source URL or source package]
```

If you do not know whether that is the right command, say:

```text
Autopilot this and route it. If it teaches systems, orchestration, source extraction, or workflow design, use /source-to-skill-system.
```

## Final Expectation

The upgrade should make Codex feel less like a pile of imported tools and more like an operator with a spine:

- it knows where authority lives
- it knows which doors stay hot
- it knows when to keep the archive cold
- it knows how to convert sources into systems
- it knows how to prove the system works
- it leaves you with the next route instead of another thing to remember


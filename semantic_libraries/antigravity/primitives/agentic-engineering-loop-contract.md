# Agentic Engineering Loop Contract

## Purpose

Use this primitive when a source, workflow, skill, or harness repair should make Codex Antigravity more agentic without becoming vague "vibe coding" or a new mega-system.

Agentic engineering means the operator keeps ownership of the thinking while the harness does bounded execution: thin context, exact source truth, small work packets, review loops with finish lines, dependency safety, and a bias toward usable output.

This contract is grounded in the transcript-backed source package:

- YouTube: `https://www.youtube.com/watch?v=PzVV4X37ihg`
- Local evidence: `extractions/video-context/PzVV4X37ihg/`
- Evidence limit: transcript-backed spoken evidence only; frame extraction and OCR were skipped.

## When To Use

- A source teaches agent harnesses, context engineering, AI coding loops, review loops, or dependency safety.
- A workflow asks Codex to improve a system, skill, prompt, router, package, or codebase.
- A task risks overloading context instead of giving exact files and source evidence.
- A task may install packages, fetch external source, or rely on fast-moving dependencies.
- A build or repair needs a usable first artifact followed by hardening rather than endless private polish.

## Loop Rules

| Rule | Requirement |
|---|---|
| Human-owned thinking | Define the objective, constraints, quality bar, and stop condition before execution. Do not let the model invent the goal. |
| Context sweet spot | Load exact files, source packages, commands, and short handoffs. Avoid bulk-loading broad libraries or whole histories when targeted search can find the needed surface. |
| Source truth first | Prefer code, configs, schemas, transcripts, and local artifacts over remembered docs or model assumptions. Use source paths in handoffs. |
| Plan then shrink | Draft the work shape, then split it until each unit can be reviewed, tested, and resumed without hidden context. |
| Small chunks | Keep implementation units narrow enough for a focused verifier, review, or cold-start prompt. Large changes need a staged plan. |
| Structure cleanup | After a feature or system patch, check for duplicated mechanics, unclear ownership boundaries, and future-agent readability. |
| Review-until-stop | Feedback loops need a measurable finish line: passing verifier, score threshold, fixed issue count, or turn cap. |
| Dependency safety | New packages, repos, and external tools require age/reputation/source inspection when practical, no silent install, and explicit override for unusually new or risky dependencies. |
| Ship earlier, harden faster | Produce the smallest usable artifact first, then harden with proof. Do not keep polishing if real use or validation would teach more. |

## Outcome Ownership And Explain-Or-Recover (SHADOW)

Use the `Own` decision from
`systems-thinking-expertise-intelligence-overlay.md` whenever an agent creates
code, analysis, content, or system changes with meaningful consequences. Name
one human or operator as the outcome owner. The owner must be able to defend
the problem choice, review boundary, quality judgment, and recovery path. Tool
use is not sufficient fluency when nobody can explain, diagnose, or repair the
result.

## Default Agentic Engineering Packet

Before mutation-capable work, fill this compact packet or reference an existing Goal Packet that covers it:

| Field | Requirement |
|---|---|
| Objective | One concrete outcome the operator owns. |
| Source truth | Exact paths, URLs, transcripts, code, configs, schemas, or router output used as evidence. |
| Context plan | What stays hot, what is searched on demand, and what is deliberately skipped. |
| Work chunks | The smallest implementation/review units. |
| Review loop | Verifier, score, or review surface plus the stop condition. |
| Dependency gate | Package/tool age, source/repo check, install boundary, and override rule if relevant. |
| Structure pass | Cleanup/readability check after the main build. |
| Use-now artifact | The first artifact or behavior that can be used immediately. |
| Hardening proof | Commands, tests, router checks, or cold-start prompt that prove it works. |

## Dependency Safety Gate

Use this gate before installing or relying on a new package, repo, MCP server, plugin, CLI, or external automation:

1. Identify the package/tool and why it is needed.
2. Check age, repository/source, maintainer signal, popularity or adoption, and recent suspicious churn when practical.
3. Prefer source inspection for open-source packages when the package is core to the build.
4. Do not silently install unusually new packages. Use a 14-day caution window by default unless the user explicitly approves or the package is already trusted in the project.
5. Record the override reason when the build proceeds despite risk.

This is a safety gate, not a blanket ban. Existing project dependencies and established tooling can proceed through normal sandbox approval, but the agent must not hide risky novelty.

## Review Loop Standard

A review loop is valid only when it has:

- the target artifact or behavior,
- the reviewer or verifier,
- the pass condition,
- the turn or iteration cap,
- the no-regression check,
- the next action when the loop fails.

If any field is missing, return a queue-only diagnosis or a missing-field packet rather than starting an open-ended loop.

## Relationship To Existing Contracts

| Contract | Relationship |
|---|---|
| `skill-system-contract.md` | Use when the loop becomes a reusable orchestrated capability. |
| `source-to-skill-extraction.md` | Use when the loop is harvested from source material. |
| `goal-loop-maintenance-contract.md` | Use when self-improvement can mutate workflows, skills, routers, prompts, or maintenance surfaces. |
| `expert-composition-contract.md` | Use when many experts or workflows could help and one owner must integrate them. |
| `repeatability-spine-contract.md` | Use when a good result needs preservation and replay across future sessions. |

## Validation

Run:

```bash
python3 execution/verify_agentic_engineering_loop_contract.py
```

When workflow, router, skill, or system files changed, also run the relevant control-plane checks from `CODEX.md`.

## Last Updated

2026-08-08

# Daily Operator Command Kit

## Purpose

Use this primitive for small daily commands that help an operator steer, coordinate, critique, branch, and improve Codex sessions without turning every interaction into a full workflow.

## Source Evidence

- Source package: `extractions/video-context/xC6N_TNR8wA/`
- Source video: `https://www.youtube.com/watch?v=xC6N_TNR8wA&t=373s`
- Evidence type: transcript-grounded, with no private skill files available.

## Shared Rules

- Keep outputs compact, numbered, and action-oriented.
- Prefer recommended defaults when the user has not provided enough detail.
- Do not publish, message, purchase, scrape private dashboards, or take external action.
- Do not spawn real Codex subagents unless the user explicitly authorizes subagents or parallel agents.
- Do not modify `/Users/farricecain/Google Antigravity`.
- Use local files and project context only when the command specifically calls for them.
- Default to read/propose behavior. Mutate files only when the command explicitly includes an apply/create/update step and the target is inside the allowed workspace.

## Command Family

| Command | Job |
|---|---|
| `/session-calibrate` | Convert session learnings into proposed system improvements. |
| `/project-coordinate` | Create or update a shared project context home. |
| `/project-onboard` | Load a project context home and brief the current session. |
| `/align` | Ask clarifying questions before meaningful execution. |
| `/devil` | Challenge assumptions, risks, and weak options. |
| `/burst` | Generate distinct options and recommend a path. |
| `/tweak` | Turn design feedback into controlled parameters and patch plans. |

## Output Contract

Each command should return:

- **Read/Context Used**: what was loaded or assumed.
- **Output**: the command's primary result.
- **Recommended Move**: the next action with a reason.
- **Risk/Limit**: one specific caveat when relevant.

For tiny uses, collapse the contract into a short numbered list.

## Context Policy

- Keep this primitive hot enough for the command family.
- Keep the transcript package cold; load only `timestamp-map.md` or `operator-kit-extraction.md` unless source fidelity is in question.
- For project coordination, pass file paths and short summaries between sessions rather than whole transcripts or large logs.


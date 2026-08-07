# Matt Pocock Handoff Skill Reference

## Source

- Video: `/handoff is my new favourite skill`
- Creator: Matt Pocock
- URL: `https://www.youtube.com/watch?v=dtAJ2dOd3ko`
- Local transcript package: `extractions/video-context/dtAJ2dOd3ko/`
- Repository: `https://github.com/mattpocock/skills`
- Skill path: `skills/productivity/handoff/SKILL.md`
- License: MIT License, copyright 2026 Matt Pocock

## Verified Mechanics

The source skill is intentionally small:

- Summarize the current conversation into a handoff document for a fresh agent.
- Save disposable handoffs to the operating-system temp directory, not the active workspace.
- Include suggested skills.
- Reference existing artifacts by path or URL instead of duplicating them.
- Redact sensitive information.
- Tailor the handoff to the user's stated next-session purpose.

## Antigravity Adaptation

Codex Antigravity should not import this as a generic replacement for
`/end-session`. The useful pattern is a focused transfer branch:

- Parent session stays clean.
- One bounded slice moves to another session, tool, prototype, or agent.
- The handoff points to receipts, status files, source packages, and artifacts.
- The next session gets a copy-paste prompt and suggested routes.
- The main thread remains integration owner unless real Codex subagents were explicitly authorized.

## Reuse Hook

Use this reference for `/handoff`, `/steering-compass`, `/end-session`, and
source-to-skill work where the user needs continuity without dragging the whole
conversation forward.

---
name: "source-command-farrice-content-os"
description: "Run farrice-content-os when Farrice wants raw concepts turned into an end-to-end content operating system with research, brandjacking, hook room, writers' room, voice, taste, packaging, and engagement."
---

# source-command-farrice-content-os

Use this skill when the user asks for `/farrice-content-os`, wants content done end to end, asks to turn raw concepts into publish-ready content packages, wants Diandra's system combined with Farrice's voice and writers' room, or needs research + brandjacking + top-tier hooks + anti-slop gates in one operating system.

## Command Template

Read and execute the workflow at `.agent/workflows/farrice-content-os.md`.

## Routing Notes

- This is the orchestrator. Do not replace it with `/diandra-linkedin-system`, `/publishable-copy-gate`, or `/writers-room` when the request asks for the whole content OS.
- Use Diandra workflows as internal engines.
- Load Farrice context and the writers' room before public-facing drafts.
- Run Hook Room before polish.
- Use true Codex subagents only when the user explicitly asks for delegated, parallel, or subagent work.


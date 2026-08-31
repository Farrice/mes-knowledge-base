---
name: "source-command-cos"
description: "Run /cos through the canonical Chief of Staff OS Standing Board workflow. Auto-routes to daily, weekly offer, onboarding, or read-only status from live COS state."
---

# source-command-cos

Use this skill when the user invokes `/cos`, asks for the COS check-in, or asks to run the Standing Board.

## Command Contract

Read and execute `.agent/workflows/cos.md` first. Follow its state-based routing into `skills/chief-of-staff-os/SKILL.md`, load `skills/chief-of-staff-os/genius.md`, and then run the selected canonical COS workflow.

Do not duplicate the COS workflow in this bridge. All COS behavior, state, privacy rules, and quality gates remain owned by the Google Antigravity project files referenced above.

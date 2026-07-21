---
name: "Ray Amjad — Chat-Native Harness Blueprint"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — Chat-Native Harness Blueprint

## Role & Activation

You are executing Ray Amjad's harness-design method, modeled on Percy — his own Claude Tag equivalent: Claude Code + Codex on cloud, addressed by Slack tag, delivering recordings in-thread, taking approvals as reactions. His build-vs-buy reason, stated plainly: customization ("I can use stuff like Codex, add LiveKit CLI, Playwright… essentially I can build my own custom harness") and cloud persistence ("a whole task lifecycle may take about 2 hours… better that it happens in the cloud"). Enterprise-validated shape: Stripe minions, Shopify River.

## Input Required

- [PLATFORM] — chat platform and workspace realities
- [PROJECTS] — repos the harness serves + their lifecycle/verification skills (existing or to forge)
- [BUY-VS-BUILD FACTS] — what off-the-shelf (Claude Tag class) covers vs the custom tooling actually needed

## Execution Protocol

1. **Honest gate first**: if off-the-shelf covers the need, recommend it and stop — custom harness only when customization is the point.
2. **Runtime**: cloud-run executor(s); name them (dual-executor pattern gives second opinions — Percy's codex-second-opinion skill).
3. **Skill loadout** (Percy's four, adapted): send-messages-via-chat · verification (surface-matched, artifact-producing) · full task lifecycle · second-opinion review — plus project tools from the verification-environment plan (Playwright, LiveKit-class CLIs).
4. **Channel topology**: per-project work channels · artifact/verification channel · report channels (routine outputs land actionable — tagging the agent on any report delegates it) · exception channel for monitor-by-exception.
5. **Interaction grammar**: tag+spec kicks a lifecycle · acknowledgment signal (eyes emoji) · artifacts in-thread · reaction = approval · follow-ups steer mid-run · "can you update this for next time?" writes steers into the harness permanently.
6. **Autonomy wiring**: vision-doc filter for proactive work; approval fallback; PR monitoring window; phone notification as final escalation hop.
7. **Acceptance test**: define the first end-to-end demo mission (spec message → PR + recording in-thread).

## Output Contract

One-page harness blueprint: buy-vs-build verdict (one line) · runtime + executors · skill loadout table · channel topology · interaction grammar card · autonomy wiring · acceptance-test mission.

## Output Skeleton

```
HARNESS BLUEPRINT — [name]
Buy-vs-build: [verdict + one-line reason]
Runtime: [cloud target · executors]
Skills: | skill | purpose | exists/forge |
Channels: [topology list with each channel's role]
Grammar: [kick · ack · artifact · approval · steer · persist]
Autonomy: [vision filter · approval mechanic · monitoring window · escalation hop]
Acceptance test: [demo mission spec]
```

## Quality Gate

- Buy-vs-build gate answered before any design?
- Runtime survives laptop shutdown (cloud, not local)?
- Verification skill in the loadout with artifact delivery in-thread?
- Approval and escalation mechanics both present?
- Every skill/tool justified by a named project need, none decorative?

## Deploy When

The 2→3 climb once lifecycles are trusted; low/medium-difficulty task classes ready to leave the terminal.

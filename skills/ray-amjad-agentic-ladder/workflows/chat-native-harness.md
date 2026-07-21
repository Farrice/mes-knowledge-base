---
description: Design a Percy-style chat-native agent harness — cloud agent + chat surface + skills + approval mechanics + artifact flow
---

# Chat-Native Harness — Your Own Claude Tag

Designs the harness that moves task lifecycles off your laptop and into chat: a cloud-run agent addressed by tag, delivering artifacts in-thread, taking approvals as reactions. Modeled on Ray's Percy; enterprise-validated shape (Stripe minions, Shopify River).

## Pre-Flight Gate

Load `genius.md` (patterns 3, 9, 10, 12). Require: chat platform, project repo(s), which lifecycle skills already exist (task lifecycle, verification), and the buy-vs-build posture. **Honest gate**: if off-the-shelf (Claude Tag or equivalent) covers the need without custom tooling (extra CLIs, second-opinion models, custom verify rigs), recommend it and stop — custom harness only when customization is the point (Ray's stated reason for Percy).

## Skill Acquisition

- `genius.md` — Chat-Native Operations, Recording Receipt, Manual-Once Rule
- `extractions/ray-amjad/reference-corpus/` — both artifacts (the lifecycle the harness runs; the fan-out it enables)

## Execution

1. **Runtime**: agent(s) on cloud (lifecycles run ~2h; must survive laptop shutdown). Name the executor(s) — Ray runs Claude Code + Codex side by side for second opinions.
2. **Skill loadout** (Percy's four, adapted): send-messages-via-chat · verification (surface-matched, artifact-producing) · full task lifecycle · second-opinion review. Add project-specific tools (Playwright, LiveKit CLI, etc.) from the verification-environment plan.
3. **Channel topology**: per-project work channels · verification/artifact channel · report channels (routine outputs land here) · exception channel for monitor-by-exception. Reports arriving in-channel are *actionable*: tagging the agent on any report delegates it.
4. **Interaction grammar**: tag + spec message kicks a lifecycle · acknowledgment signal (eyes emoji) · artifacts in-thread · thumbs-up = approval · follow-up messages steer mid-run · "can you update this for next time?" writes the steer into the harness (Manual-Once over chat).
5. **Autonomy wiring**: vision doc as auto-implement filter; approval-stage fallback; PR monitoring window after delivery; phone notification as the final escalation hop.
6. **Prove it**: define the first end-to-end demo mission (spec → PR + recording in-thread) as the harness's acceptance test.

## Content Type Adaptations

| Setup | Adaptation |
|---|---|
| Slack | Full grammar as specified (Ray's platform) |
| Other chat (Discord/Teams) | Map reactions/threads to platform equivalents; keep the grammar |
| No chat platform (solo CLI) | Skip harness; agent-view/desktop session management suffices until L2→3 |
| Enterprise | Add observability layer (Stripe's differentiator: per-tool-call visibility); cross-team channel permissions |

## Output Requirements

Harness blueprint: runtime + executors · skill loadout table · channel topology · interaction grammar card · autonomy wiring · acceptance-test mission. One page.
Execution prompt: `references/prompts-v2/chat-native-harness.md` — honor its Output Contract.

## Quality Gate

Reject if: buy-vs-build gate skipped; harness runs on a laptop; artifacts not delivered in-thread; no approval mechanic; no exception/escalation path; skill loadout missing verification.

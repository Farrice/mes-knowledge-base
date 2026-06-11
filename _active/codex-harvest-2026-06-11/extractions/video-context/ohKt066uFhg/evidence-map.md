# Evidence Map: Viktor AI Coworker

Source: `https://www.youtube.com/watch?v=ohKt066uFhg&t=195s`

Use this map as the compact source evidence surface for `/ai-employee-os`. It references transcript timestamps in `transcript.txt` and observed rows in `video-context-ledger.md`.

## Evidence Anchors

| Timestamp Range | Source Claim | OS Lesson |
|---|---|---|
| 00:00:46-00:01:10 | Viktor is framed as an AI employee that lives in Slack, without a separate web app, and participates in threads and channels. | AI employee systems should start from the native work surface, not a new destination. |
| 00:01:10-00:02:06 | It has access to tools/integrations and broad context across the company. | Execution ability and context access are inseparable; access must be mapped explicitly. |
| 00:03:20-00:04:12 | Earlier browser agents reached only a few steps at about 60 percent reliability, with reliability compounding downward across steps. | Multi-step agent work needs reliability gates, progress states, and fallback paths. |
| 00:04:29-00:05:14 | Email-agent loop had context, triggered on events, connected to tools, and gated actions like refunds with approvals. | Event-driven agents need approval boundaries for consequential actions. |
| 00:05:30-00:06:28 | Company agents differ from personal agents: one integration can serve the team and the agent can work across roles. | Shared integration design is a team OS problem, not a personal assistant setting. |
| 00:06:44-00:08:15 | Memory and access become harder across many users/channels; context must not leak between growth, executive, engineering, support, and DMs. | Memory isolation and access boundaries are first-class requirements. |
| 00:08:23-00:10:06 | Slack is chosen because human employees work there and ten-minute tasks feel better inside an async team interface. | Match latency expectations to the surface and use status/checkpoint language. |
| 00:10:13-00:11:51 | Slack events include DMs, channels, threads, reactions, edits, deletes, and conversation drift that must be linearized for the agent. | Build an event ledger before trusting ambient agent behavior. |
| 00:11:55-00:13:00 | A cheaper model looked strong on tool calling/codegen but users objected to personality changes. | Model swaps require personality and trust regression checks. |
| 00:13:02-00:14:24 | Proactive workflow suggestions are powerful, but broad day-one proactivity triggers security concerns. | Proactivity must be earned through staged trust. |
| 00:14:35-00:17:00 | Shared context and one connected integration reduce friction, but personal email leakage showed the need for scoped integrations. | Integration scope, ownership, and auditability matter more than raw connector count. |
| 00:17:06-00:17:51 | The summary pillars are: helps get work done, knows the company/context, and is friendly. | Score AI employees on execution, context/access, and trust/experience. |

## Unavailable Evidence

- OCR evidence is unavailable.
- Frame evidence exists as sampled images only. Do not describe slide contents or visual details from the frames unless a vision/human review pass is added.

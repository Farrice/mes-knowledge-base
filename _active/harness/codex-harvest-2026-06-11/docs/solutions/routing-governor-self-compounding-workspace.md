# Routing Governor Self-Compounding Workspace

Use this pattern when Antigravity has the right workflows on disk but raw routing still chooses generic, impressive, or irrelevant paths.

## Problem

A large agent workspace can contain good skills, workflows, memories, and performance logs while still failing at the moment of use. The user asks for an outcome, the router finds keyword-adjacent workflows, and the system returns generic output instead of the asset or action path that would actually solve the problem.

## Source Signal

Source: [Why Codex? Build Agentic Workspaces That Improve Over Time](https://www.youtube.com/watch?v=t8j8_rB6EQo)

The useful mechanic is not "make another agent." The source pattern is: durable instructions, reusable skills, external capability, memory, scheduled review, isolated experimentation, and human-approved diffs. A workspace compounds only when real usage produces reviewable improvements.

## Working Solution

Add a routing governor above raw keyword rank:

- classify high-risk intent before trusting router order
- force-surface required workflows for that lane
- show raw candidates, chosen route, and skipped misleading routes
- log misroutes as feedback without requiring manual routing IDs
- let the System Governor queue supervised router fixes from negative or mixed feedback

For immediate-income requests, the required stack is:

- `/first-10k`
- `/revenue-offer-agent`
- `/client-acquire`
- `/zero-to-client-sprint`
- `/service-first-productization`

Use:

```bash
python3 execution/routing_governor.py evaluate "[request]"
python3 execution/routing_intelligence.py misroute --request "[request]" --wrong "[wrong-workflow]" --correct "[right-workflow]" --notes "[why]"
```

## Why It Works

It preserves Antigravity's existing routers, commands, and workflow bridge while adding the missing intent guardrail. The system does not auto-mutate itself; it gathers evidence, proposes concrete fixes, and keeps the user in the approval loop.

## Prevention Rule

When a user says an answer was generic, useless, or routed to the wrong workflow, log it as a misroute immediately. Do not treat it as a one-off quality complaint. The correction is routing evidence.

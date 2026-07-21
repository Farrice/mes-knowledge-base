# Boris Cherny — "Steps of AI Adoption" (source-of-record)

> Transcribed from Boris Cherny's claude.ai doc as read on screen in Ray Amjad's walkthrough (video XLA-sTSJ-Wc, 2026-07-17; Boris's X post 2026-07-16). Attribution: this table is **Boris's**, not Ray's. Quote it as the canonical ladder; do not extend it with invented levels or cells.

## The Ladder

| Level | Name | ~Agents | You are | Description | Unlock |
|---|---|---|---|---|---|
| 0 | Gated | 0 | — | Org blocks or tightly gates coding agents (security/approval process; no IT buy-in) | Claude in chat; SSO/SCIM plus role-based access; budget caps; data governance |
| 1 | Assisted | ~1 | You + an agent (a fast pair programmer) | One engineer, one agent, mostly supervised. One session at a time; review almost every change before it merges. Work is synchronous: you sit and watch while Claude works, then move to the next task | A change that used to fill an afternoon becomes something you finish between meetings |
| 2 | Parallel | ~10 | Orchestrator | One engineer orchestrates 5–10 agents at once, each on its own worktree or git checkout, jumping between them. Claude checks its own work — tests, build, lint, security scan — before you see it. Auto mode always on. Automated code review and security review on by default. You review final diffs rather than keystrokes; backlog of maintenance work starts shrinking. Claude writes most of the code | A backlog that used to take the team weeks becomes one engineer's afternoon of orchestration |
| 3 | Supervised autonomy | ~100 | Manager of managers (an org tree) | Claude writes all or nearly all of the code. "Did you read the code?" becomes "what context was the model missing and how do we solve it for next time?" Claude proactively does work you would have had to kick off manually. Maintenance and cleanup that used to wait for someone to find the time now runs continuously in the background | Proactive work + continuous background maintenance |
| 4 | AI-native | ~1,000+ | VP steering by intent | The loop is fully closed and most agents are kicked off by Claude. Hundreds to thousands of agents run per day; you steer by intent and monitor by exception | The quarter-long migration becomes a workflow you kick off and check on |

## Bottlenecks per level

- **L1**: Your attention and the need to inspect each response and code edit. Low trust in the model's output; lack of self-verification.
- **L2**: Reviewing output. You're hand-writing less code and instead checking six streams of it — this takes up more of your time. Prompting and steering the model as you juggle sessions.
- **L3**: Trust in the loop and your team's decision throughput. "The agent tree is too deep to babysit and your trap is scaling agent count before the loop has earned widespread trust." Ensuring tokens are used efficiently as usage increases — requires monitoring (via OTel or Analytics) and a culture that encourages experimentation while controlling costs once internal use cases find PMF. Ask yourself: "is this something an engineer would have done?"
- **L4**: Identifying and automating work at scale, and enforcing the right guardrails for each type of work.

## Transitions ("How to get from step N to N+1")

- **0→1**: Executive/buyer alignment and escalation of blockers; frameworks for launching Claude securely.
- **1→2**: Run more than one agent at a time; a self-verification loop you trust (tests + build + lint + e2e testing with a real dev environment); auto mode, permission prompts; automate code review.
- **2→3**: Give Claude a way to pull in context (let Claude read code, wikis, discussions); agency and code review speed (agents may touch code owned by other teams); break up your work into loops and routines; let Claude kick off Claude.
- **3→4**: Scaled automation of domain-specific use cases (eg. code migration, fuzzing, feature-building, feedback remediation).

## Tooling column (per level, as listed)

- **L1**: Claude Code in the Desktop, CLI, or IDE; Claude Cowork / Claude Design; Anthropic API, Bedrock, Vertex, Microsoft Foundry; analytics dashboard + Analytics API; Compliance API for Claude Enterprise; plan mode to review intent before edits.
- **L2**: Auto mode; Agent view; Claude Code Review; Claude Security Review; Claude on mobile, cloud execution in Desktop; Claude Teams / Claude Enterprise; Claude Tag (do a single task); worktree isolation in CLI and Desktop; remote control — monitor your agents from your phone.
- **L3**: Subagents with worktree isolation (so parallel agents don't collide); Routines, /loop, /batch, and /goal to fan out repetitive work; dynamic workflows; Claude Tag (have it monitor a channel or data source and kick off tasks proactively); automatic code review + security review; agent sandboxing; CLAUDE.md and Skills to encode standards; tune Auto mode classifier; manage token use with model selection, advisors, LSPs.
- **L4**: Claude Agent SDK to programmatically build and schedule agents; Claude Tag active in most Slack channels, auto-responding to posts.

## Boris's framing (from the X post)

"I talk to engineers at other companies every day and hear the same thing: one person is 10x'ing their output with Claude but the rest of the org hasn't caught up. Watching teams adopt AI, I keep seeing the same 4 steps."

Context markers: Boris said he personally *just* hit level 4 (Ray's note: likely on internal models beyond Fable 5). Most engineers sit between 1 and 2; ~80-90% of practitioners are at level 1.

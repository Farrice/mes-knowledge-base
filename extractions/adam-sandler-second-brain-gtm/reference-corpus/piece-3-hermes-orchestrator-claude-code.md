---
SOURCE URL: https://www.viableedge.com/blog/hermes-agent-claude-code-orchestration
RETRIEVED: 2026-07-16
CONTENT TYPE: Blog article (viableedge.com owned site, published blog post) with embedded
  interactive tool ("Orchestration Stack Builder") and paid downloadable pack offer
PUBLISHED DATE (per page schema.org metadata): 2026-07-05
AUTHORSHIP CONFIRMATION: Page's embedded schema.org JSON-LD BlogPosting metadata declares
  "author":{"@type":"Person","name":"Adam Sandler"}. On-page byline: "Adam Sandler / Marketing
  strategist applying AI and ML principles to marketing systems. Founder of The Viable Edge."
  First-person operator voice throughout ("I run a consulting and build practice on this
  stack... Nothing below is a thought experiment"). Retrieved via direct HTTP GET (curl, static
  Next.js SSR HTML, no login wall).
WHY IT QUALIFIES: His own site, his own byline, schema.org author attribution, sustained
  first-person operator voice. NOT the Ryan Doser interview transcript (disqualified per task
  spec). Chosen as a third, topically distinct piece (agentic orchestration / Claude Code
  workflow, rather than marketing-context-engineering or consulting-scoping) to give the blind
  pass genuine voice-and-topic range.
NOTE ON VERBATIM STATUS: Text below is the raw extracted body copy stripped of HTML tags via a
  mechanical script (HTML entities decoded). No paraphrasing, no summarizing, no rewording.
  Boilerplate nav/footer chrome included at top/bottom for transparency; the substantive content
  runs from the byline through the "Grab the Orchestration Pack" close.
---

Hermes as an Orchestrator for Claude Code: The Operator’s Guide (2026) | The Viable Edge
Knowledge base
Competitor tracking
Pricing
Work with us
Advisory
Custom builds
Resources
Second Brain Course
Blog
Knowledge Hub
Community
Newsletter
Members
Get started
Get started
Navigate
Knowledge base
What it builds
Competitor tracking
Market watch
Pricing
$29/mo, one plan
Advisory
Work with us
Custom builds
Work with us
Members
Your workspace
Resources
Second Brain Course
Sell second brain delivery
Blog
Deep dives
Knowledge Hub
Guides & answers
Community
Join the lab
Newsletter
One idea, weekly
Home
/
Blog
/
Hermes as an Orchestrator for Claude Code: The Operator’s Guide
ai-era-strategy
12
min read
Hermes as an Orchestrator for Claude Code: The Operator’s Guide
Setup guides for Hermes are everywhere. What almost nobody shows is a real operation running on the stack: an always-on orchestrator delegating to Claude Code, a board as the work queue, memory as the source of truth, and verification gates that keep it honest. This is the way of working, from someone who ships client work on it every day.
AS
Adam Sandler
Marketing strategist applying AI and ML principles to marketing systems. Founder of The Viable Edge.
Share:
To use Hermes as an orchestrator for Claude Code, run Hermes as the always-on layer that holds your memory, schedule, and channels, and hand execution-heavy work to Claude Code through short delegation briefs with explicit done-criteria and verification gates.
Hermes plans, remembers, and reports. Claude Code reads the repo, writes the code, and runs the checks. The split works because each tool is kept where it is strong, and the discipline that connects them is written down, not improvised per session.
One honest note before the method. I run a consulting and build practice on this stack, plus a small production SaaS. Client deliverables, site builds, research, back-office routines: the stack does real billable work every day. Nothing below is a thought experiment, and nothing below requires a big operation to copy. It requires the discipline more than the tooling.
What is Hermes?
Hermes is an open-source, MIT-licensed AI agent from Nous Research. It connects any capable model to messaging platforms like Telegram, Discord, and Slack, runs on local machines, Docker, or a VPS, schedules recurring work with cron, and keeps persistent memory across sessions, with a built-in learning loop that turns experience into reusable skills. It also ships a first-party skill for delegating coding work to the Claude Code CLI, which is the seam this whole guide is built on.
Why put an orchestrator above Claude Code at all?
The most common question in the Hermes community is some version of: what does this do that Claude Code alone cannot? Fair question, because for a single coding session the answer is nothing. The orchestrator earns its place the moment your work stops fitting inside one session:
It is always on.
On a VPS, Hermes works while your laptop is closed. Scheduled routines run at 6am, a build kicked off from your phone finishes while you are at dinner, and the completion ping arrives either way.
It remembers.
Claude Code starts each session from the repo plus whatever context files you maintain. Hermes carries durable memory across every session and channel: who your clients are, what was decided last week, which approach failed before and why.
It reaches you where you are.
A messaging gateway turns your phone into the command line. Assign work, answer the one fork question that needs you, and approve the result without opening a terminal.
It holds the queue.
One layer owns what should happen next across many projects. Individual Claude Code sessions execute one card at a time; the orchestrator sequences them.
If none of those apply, you do not need an orchestrator yet. Close this tab and keep shipping. If two or more apply, the rest of this guide is the operating manual.
What does the stack actually look like?
Four roles, each held by the simplest thing that can hold it:
Role
Held by
What it does
Orchestrator
Hermes (always-on)
Plans, sequences, remembers, schedules, reports to your channel
Execution engine
Claude Code
Reads the repo, writes code and content, runs builds and tests
Work queue
A markdown kanban board in the repo
Single source of truth for what is Ready, In flight, Blocked, Done
Source of truth
Durable memory files
Who you are, what the business is, hard rules, decisions and their reasons
The two unglamorous rows are the ones that compound. The board and the memory files are plain markdown in version control, readable by every agent and every human, no database, no SaaS dependency. When people show off their agent stacks they screenshot the messaging gateway. The board and the memory files are where the leverage lives.
How do you delegate work from Hermes to Claude Code?
The bundled claude-code skill gives Hermes two modes, and picking the right one per task is most of the craft:
Print mode
runs a one-shot task and exits. No terminal session to manage, output captured cleanly. This is the default for anything you can specify up front: implement this card, write this draft, run this migration against staging.
Interactive mode
keeps a live session in tmux that Hermes can send follow-ups to and read output from. Reserve it for genuinely exploratory work, because a supervised session multiplies cost and attention.
Either way, the handoff artifact is a
delegation brief
, and its shape matters more than its length: the objective in one sentence, why it matters, the done-criteria the work will be verified against, and the boundaries. The unit of delegated work is a board card, one coherent outcome, small enough to verify in one review. Vague cards produce vague pull requests.
The rule that keeps the whole loop honest:
the worker never grades its own homework unchecked
. Every brief includes done-criteria that are mechanically checkable, and the orchestrator confirms them from evidence: exit codes, test output, a diff, a live URL. An agent report that says it is done, without a green check attached, is treated as not done.
How do you route models so this does not get expensive?
An always-on orchestrator plus long-running coding sessions can burn real money if every token runs on the premium tier. The pattern that works is the one several practitioners have independently converged on:
a smart controller directing cheaper workers
.
The orchestrator reads a lot and writes a little.
Planning, judgment, and review are input-heavy and output-light, which is the cheap direction on every price sheet. This is where the capable model belongs.
Workers are verbose.
Code, drafts, and test output are output-heavy, which is the expensive direction. This is where the mid-tier model belongs, and where a fast cheap model handles the mechanical subtasks.
Escalate on failure, not on anxiety.
Route by task difficulty. When a cheap tier fails its own verification, bump the task up one tier automatically instead of shipping a bad result or defaulting everything to the top.
The dial that matters is the ratio: most volume on the cheap tiers, judgment on the capable one, and the top-tier model reserved for the genuinely hard calls. When we published our guide to
prompting Claude Fable 5
, the core of it was exactly this selection discipline.
Here is the whole method as a tool. Pick what your stack should do, and the builder assembles a setup checklist in the right order plus a first delegation brief you can paste into Hermes the day the stack is live.
🧭
Orchestration Stack Builder
Pick what your stack should do and copy a setup checklist plus a first delegation brief. Runs in your browser.
What is this stack for?
Ship client and agency work faster
Run my whole operation on it
Build a side project
Optimized for repeatable deliverables: delegation briefs, per-client memory, cost discipline.
Where does Hermes run?
VPS (24/7, machine-off operation)
My machine (start simple)
Docker (isolated, portable)
Command channel
Telegram
Discord
Slack
Terminal only
Scheduled routines
Morning briefing (news, metrics, what needs you today)
Finance watch (revenue, costs, anomalies)
Site or product health check
Overnight backlog grooming
Operating discipline
Cost-routed models: smart orchestrator, cheaper workers
Markdown kanban board as the shared work queue
Durable memory files (persistent context across sessions)
Verification gates: done means green build and tests
Your stack plan + first brief
# Hermes orchestration stack: Ship client and agency work faster
## 1. Foundation
- Install Hermes on a VPS and run it as a systemd service. It works 24/7 with your machine off, which is the point of an orchestrator.
- Install Claude Code on the same machine. Hermes delegates coding work to it through the bundled claude-code skill.
## 2. Model routing (your cost control)
- Orchestrator: a top-tier model for planning, judgment, and review. It reads a lot and writes a little, which is the cheap direction.
- Workers: cheaper, faster models for execution-heavy subtasks. Claude Code sessions and subagents do the verbose work at the lower rate.
- Rule: route by task difficulty, not by habit. Escalate a task only when the cheap tier fails its own verification.
## 3. Memory (the part most setups skip)
- Enable persistent memory and skill generation in the Hermes config. Without these it behaves like any single-session agent.
- Keep a small set of durable context files the agent reads at session start: who you are, what the business is, current goals, hard rules.
- One fact per memory entry, linked liberally. Review what the agent writes, since memory it gets wrong compounds as fast as memory it gets right.
- Keep a plain-markdown kanban board in the repo as the shared work queue. The orchestrator reads Ready, works cards, moves them to Done. Every unfixed issue becomes a card, always.
## 4. Channels
- Connect the Telegram gateway. Your phone becomes the command line: assign work, approve forks, get completion pings.
- Keep interrupts for real milestones only: a long run finishing or a hard block. Progress noise trains you to ignore the channel.
## 5. Scheduled routines
- Morning briefing (news, metrics, what needs you today).
- Site or product health check.
- Every routine reports to your channel with evidence, not vibes: numbers, links, diffs.
## 6. Verification gates (non-negotiable)
- Done means verified: a green build and passing tests before anything ships, judged on exit codes, not on the agent saying it looks fine.
- Every progress claim must point at a real tool result. If a step failed or was skipped, the report says so plainly.
- If a check fails the same way twice, the agent stops retrying variations and re-reads the code.
---
## Delegation brief (paste into Hermes)
Use Claude Code for the following task. Run it in print mode unless it needs supervision.
## Objective
[One sentence. The outcome, not the activity.]
## Why this matters
[The larger goal and who it is for, so the model can make judgment calls that match intent.]
## Work queue
- Take the top card from Ready on the board. Move it to In flight while you work and to Done only when the done-criteria hold.
## Done-criteria
- [Concrete checks.] Build green and tests passing, judged on exit codes.
## Boundaries
- Do the simplest thing that works. No scope creep, no refactors beyond the task.
- Pause only for destructive or irreversible actions, or decisions only I can make.
- Delegate mechanical subtasks to cheaper-model subagents and keep working while they run.
## Report
- When finished or blocked, message me on Telegram: outcome first, evidence attached, one line on anything you decided along the way.
The checklist is your setup order. The brief is what you paste into Hermes the first time you hand it a real task for Claude Code.
🧭
Free download
Take the whole operating model with you
Get the Hermes Orchestration Pack: the setup checklist, the delegation brief template, the model routing table, the board template, the memory scaffold, and example cron routines. Enter your email and the download starts right away.
Get the Orchestration Pack
No spam, ever
Unsubscribe anytime
What memory discipline makes this compound?
Persistent memory is the reason to run Hermes, and it is also the first thing that rots without rules. Three that have held up:
Keep a small set of durable context files the agent reads at session start.
Who you are, what the operation is, current goals, hard rules that override everything else. Not a wiki, a page or two of load-bearing facts.
One fact per memory entry, and review what the agent writes.
Memory the agent gets wrong compounds exactly as fast as memory it gets right. A weekly skim of new entries costs minutes and prevents the slow drift where your agent confidently operates on last month's reality.
The board is memory too.
Every issue found and not fixed becomes a card, always. This one rule means nothing relies on anyone, human or agent, remembering anything overnight.
What scheduled routines are worth running?
Cron is where the orchestrator pays rent. The routines that have earned their slot for me, roughly in order of value:
A morning briefing
: what needs you today, pulled from the board, the inbox, and the numbers, delivered to your channel before you sit down.
A health check
on whatever you have in production: sites up, builds green, error rates normal, anomalies flagged with evidence attached.
A finance watch
: revenue events, cost anomalies, anything that moved. Agent stacks have a failure mode where a runaway loop quietly spends money; the watch exists so a human hears about it the same day, not at invoice time.
Overnight backlog grooming
: consolidate duplicate cards, resequence Ready by dependency, surface the decisions only a human can make into a short digest.
The standard for every routine:
evidence, not vibes
. A report that says all good is noise. A report that says all good with the three numbers it checked is a system you can trust while you sleep.
What are the anti-patterns?
Skipping verification gates.
The single most common failure. An agent that reports done without a mechanical check attached will eventually report done on something broken, and you will find out from a client. Done means verified, judged on exit codes and test output, never on the agent's confidence.
Running everything on the premium model.
The most expensive delegation brief is the one a cheaper model would have executed identically. Route by difficulty, escalate on failure.
Memory sprawl.
An agent allowed to write unlimited unreviewed memory builds a confident, wrong model of your operation. Small durable files, one fact per entry, human review.
Interrupt noise.
If the gateway pings you on every step, you will mute it, and then you will miss the one ping that mattered. Milestones and blocks only.
Orchestrating for its own sake.
If your work fits in one Claude Code session at a time, one Claude Code session is the better stack. Add the layer when the queue, the schedule, or the memory genuinely outgrows a session, not before.
What operational quirks should you plan for?
Enable persistent memory and skill generation explicitly.
Without those config flags, Hermes behaves like any single-session agent and the whole premise collapses quietly.
Use profiles to isolate contexts.
Client work, personal automation, and experiments should not share memory, secrets, or skills. Profiles give each its own boundary, which is also the clean answer to confidentiality when you run client work through the stack.
In group channels, gate on mentions.
The gateway can sit in a shared channel and respond only when addressed, which is the difference between a useful teammate and a chatty liability.
The part the tooling guides skip
Every layer of this stack runs on written-down context: the memory files, the board, the briefs. The agents are interchangeable and getting cheaper every quarter. The context is the asset, and it is the part most operations never write down.
That is exactly as true for a brand as it is for a codebase. Your positioning, your voice, your proof, the decisions behind them: if they live in your head, no agent, and no freelancer, and no new hire can act on them. Brand Architect exists to fix that specific gap. Ophelia, the always-on brand strategist inside it, interviews you and builds your brand's living source of truth, the knowledge base every AI tool and team member can work from, kept current the same way this stack keeps a codebase current: one canonical source, verified changes, everything downstream projected from it.
If this guide's way of working appeals to you, that is the same discipline pointed at your brand.
See how Ophelia works inside Brand Architect
. The first knowledge-base build is free, and it is $29 a month to keep it current.
🧭
Free download
Grab the Orchestration Pack before you go
Everything above as a single download you can keep: the checklist, the brief template, the routing table, the board, the memory scaffold, and the cron routines.
Get the Orchestration Pack
No spam, ever
Unsubscribe anytime
The Viable Edge · Brand Architect
Give your brand a single source of truth
Ophelia builds your complete knowledge base so every AI tool, freelancer, and team member works from the same brand truth. Runs in your browser.
✓
Free first build · no credit card needed
✓
Keep building for $29/mo · cancel anytime, keep everything
✓
Ophelia builds your knowledge base and keeps watch over your market
✓
Runs in your browser · nothing to install · no per-seat fees
✓
Exportable markdown and JSON · shareable link · you own everything it generates
Build your knowledge base free
→
Watch the 2-minute demo
Free first build, no credit card needed. Keep building for $29/mo, cancel anytime, keep everything.
Related Articles
Getting Started with Hermes: The Complete Guide
The setup layer under this guide: installation, memory, skills, Telegram, and first workflows.
How to Prompt Claude Fable 5 Well
The prompting discipline your orchestrator hands down to its most capable worker: select hard, prompt for autonomy, verify.
View All Articles →
Your brand’s knowledge base for the AI era.
Explore
Agents
Agent Benchmarks
Partner
Advisory
Community
Resources
Blog
Knowledge Hub
Skill Packs
Company
About
Contact
FAQ
©
2026
The Viable Edge. All rights reserved.
Privacy
Terms

# Ray Amjad — Genius Context (Agentic Coding Ladder)

> Builder of Agent Engineer Pro (2,700+ hrs of agentic-coding material), HyperWhisper, AgentStack. This skill = the **implementation layer** of Boris Cherny's "Steps of AI Adoption" ladder (source table: `references/boris-ladder-source.md`). Boris supplies the stages; Ray supplies the buildable mechanisms, each demonstrated with receipts (recordings, PRs, Slack threads). Load this before any `ray-*` workflow.

## Core Philosophy

The unit of trust is the **artifact** (recording / screenshot / MP3 / open PR), never the agent's claim. The binding constraint at every level is a **loop you trust**, not agent count. Environments compound; prompts don't. "When you notice yourself doing something manually, make it automatic by adding it to your CLAUDE.md."

## The 12 Patterns (compressed — full detail: `extractions/ray-amjad/extraction-report.md`)

1. **Parallel ≠ Progress** — N babysat sessions is still Level 1. Two-test diagnosis: (a) trusted end-to-end self-verification? (b) automated code review? Both no → L1 regardless of setup theater.
2. **Verification Surface Rule** — verify on the surface where the change meets its user: GUI → pixels → Playwright recording; API → request/response; agent → run the agent. Unit tests never satisfy a GUI change.
3. **Recording Receipt** — every autonomous task ends in a watchable artifact + open PR. Review artifact first, diff second. Big feature → multiple recordings; a missing state shows up as a missing recording.
4. **Coordinator, Not Worker** — main session does zero work: build, review, fixes, verify each in fresh subagents; noisy tool-calling always delegated.
5. **Severity-Routed Escalation** — medium/high findings auto-fixed by a builder subagent; *plausible* verdicts never auto-fixed — human gets a Slack note on PR-open explaining the change and why it matters.
6. **Capped Repair Loops** — every loop: repeat condition + cap (typically 3) + failure-class branch (capability failure → retry; environment failure → pause and notify).
7. **Environment-First Verification** — shallow verification is an environment gap, not a model gap. Ask the agent: "tell me what you would need from me to verify this change end to end," then provision (CLIs, keys, fake mic, test accounts, credit caps, artifact channel).
8. **Smarter-Means-Sneakier** — better models cheat better (Fable 5 system card p.133: lied as negotiation tactic; initiated price collusion in testing). Verification therefore runs in an **isolated-context subagent** that can tell the builder "you cheated here."
9. **Manual-Once Rule** — any manual step or repeated reminder becomes a CLAUDE.md line immediately, mid-session; stabilized lifecycle prose graduates into a named skill.
10. **Chat-Native Operations** — Slack (or equivalent) as the agent OS: spec in, eyes-emoji ack, artifacts in-thread, thumbs-up approvals, tag-to-delegate on incoming reports. Cloud-run so 2-hour lifecycles survive laptop shutdown. (Enterprise validation: Stripe minions, Shopify River.)
11. **Loop Discovery Engine** — instrument observed behavior (screen capture / logs) + a standing "find loops" loop proposing routines from what it sees; human picks; routine ships with hard constraints.
12. **Vision as Autonomy Filter** — a written product vision separates auto-implement from approval-gated; approval as cheap as a thumbs-up react.

## Hidden Knowledge

- **Trust ledger precedes autonomy**: run the codified lifecycle manually several times, refining, before widening autonomy — per project, per loop. Boris's L3 trap (scaling agents before loop trust) is exactly what this prevents.
- **Lifecycle migration path**: CLAUDE.md prose → numbered Task Lifecycle → named skill → harness skill on a cloud agent. Rising formality as it stabilizes.
- **Coordinator recursion is the 3→4 hinge**: an agent whose workers are instances of itself, with an unstick protocol, loop cadence, and phone-notification fallback.
- **Feature-building resists L4**: bug-fixing automates fully; features need taste the models lack — vision docs substitute only partially.
- **L3 reframe**: "Did you read the code?" → "What context was the model missing and how do we solve it for next time?" Gut check: "Is this something an engineer would have done?"

## Hall of Fame Exemplars (calibration anchors — quote, don't paraphrase away)

**Task Lifecycle file** (his real CLAUDE.md artifact): `extractions/ray-amjad/reference-corpus/task-lifecycle.md`
**Sentry fan-out prompt** (coordinator-of-coordinators in one prompt): `extractions/ray-amjad/reference-corpus/sentry-fanout-prompt.md`
**Context-pull line**: "When exploring in a subagent, look at the Notion product wiki via the MCP… If you find a contradiction between what the user told you and Notion, ask for clarification before continuing."
**Anti-exemplar**: the parallel-terminal power user — 4-5 sessions, manual approvals, hand-testing; Level 1 with extra windows.

## Signature Moves

- "Use an Opus subagent to do this" (explicit model choice for noisy/high-judgment stages)
- "Make a recording for me" (artifact demand appended to every verification)
- Mid-session CLAUDE.md edits the moment repetition is noticed
- Asking /verify to write its own provisioning list
- "Can you update this for next time?" (teach the harness in the work channel)
- Ladder honesty: "no right path through the steps"; pretending mastery closes your mind

## Quality Rubric (score outputs against this; reject <6 on any)

| Criterion | 10 looks like |
|---|---|
| Verification surface fidelity | Surface named first; instrument matched; artifact produced |
| Artifact receipts | Watchable recording per feature state |
| Loop boundedness | Caps + capability/environment branching + notify path |
| Coordinator purity | Main session does zero work across the lifecycle |
| Escalation triage | Confident band automated; uncertain band arrives with why-it-matters |
| Environment coverage | Agent-authored provisioning list; environments compound |
| Level honesty | Perceived-vs-actual gap named with the specific missing mechanism |

## Anti-Patterns (reject on sight)

- Level claims based on session count or tool inventory — source: Ray at ~03:05, "they may have like four or five sessions on the screen… and they basically think they reached like the highest level but unfortunately this is still level one"
- Verification below the change's surface — source: Ray at ~03:45, "it did test a unit test but it didn't actually check like, hey, does this appear in the UI"
- Uncapped repair loops / retrying environment failures — source: his Task Lifecycle step 6 (video ~12:45), "cap of 3 times. If it fails because you don't have the right setup, pause and notify the user over Slack"
- Auto-fixing "plausible"-confidence findings — source: ~11:56, "it would not be fixed automatically because it's plausible and not like medium or high"
- Main-session building while also reviewing — source: ~12:12, "our main session is a coordinator now, it's not doing any of the work"
- Proactive pipelines with no vision filter and no approval stage — source: ~26:58, "if it aligns with the vision I don't mind it being implemented automatically. But if it doesn't… I would need some kind of approval stage"
- Inventing levels/mechanics not in the source ladder — Boris's table (2026-07-16 post) is the closed canon; Ray at ~01:57: a level five only exists "if there ends up being a level five that we end up uncovering together"

## Recognition Test

Before shipping any output from this skill, ask: **would Ray recognize this as his?** Specifically — would he see his own grammar in it (subagent stages, caps, severity routing, an artifact receipt at the end), and would he catch the tells he calls out in others (session-count bragging, tests-pass-for-GUI, uncapped loops)? If the output could belong to a generic "AI automation tips" post, it fails.

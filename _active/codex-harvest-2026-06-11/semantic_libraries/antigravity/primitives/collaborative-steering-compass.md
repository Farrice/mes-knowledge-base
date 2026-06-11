# Collaborative Steering Compass

## Purpose And Operating Definition

This primitive governs proactive Operator Coach guidance and the always-on Operator Lesson. The work is not "add suggestions." The work is helping the user steer the system at full speed by surfacing high-value paths, unknown unknowns, tradeoffs, next decisions, and one practical learning cue without turning every reply into a menu.

## When To Use

- Starting Standard or Deep work: creative, strategy, extraction, offer, writing, client, workflow, build, or system-design sessions.
- A major decision, milestone, fork, validation result, or build-shape choice appears mid-session.
- Closing out Standard or Deep work where the user will benefit from knowing what to use now, harden next, or expand.
- Every final assistant answer that gives the user something to react to should include the right-size Operator Lesson unless explicitly forbidden.
- The user asks "what should we do next," "what am I missing," or "how do I use this?"
- The user says "go with your verdict," "do your recommended path," or similar after a verdict or recommendation.

## When Not To Use

- When the user explicitly asks for only a direct answer.
- When guidance would distract from urgent execution.
- When the next action is already obvious and no meaningful tradeoff exists.
- When a special tool action requires silence, such as image generation.

## Inputs

| Input | Required | Source Of Truth | Notes |
|---|---|---|---|
| Current objective | Yes | User message and session context | Name what the user is trying to accomplish |
| Work type | Yes | Task shape and command routing | Build, extraction, client, strategy, workflow, system |
| Depth tier | Yes | `high-floor-operator-os.md` and user depth signal | Light, Standard, Deep, or Parallel |
| Current state | Yes | Files, validation output, artifacts, or conversation | What changed or exists now |
| Available paths | Yes | Command menu, workflows, semantic primitives, expert stack | Prefer concrete command/artifact paths |
| Risk or opportunity | Yes | Operator judgment | Surface only practical high-value unknown unknowns |

## Outputs

| Output | Format | Destination | Owner |
|---|---|---|---|
| Kickoff steering prompt | 2-3 bullets | Session kickoff or early response | Implementing agent |
| Midpoint checkpoint | Short status + fork | Commentary during Standard/Deep work | Implementing agent |
| Closeout compass | 3 Next Prompts | Final response or `/end-session` | Implementing agent |
| Operator Lesson | Micro, standard, or full lesson | Every final answer unless explicitly skipped | Implementing agent |
| Optional command menu | 2-3 choices | When user needs steering | Implementing agent |
| Fast approval execution | Continue the recommended path | Same conversation | Implementing agent |

## Objects And Meaning

| Object | What It Means | Why It Matters |
|---|---|---|
| Best path | The likely workflow or operating route | Prevents half-speed manual steering |
| Hidden opportunity | A valuable move the user may not know to ask for | Creates compounding value |
| Hidden risk | A misfire, missing validation, or wrong path risk | Prevents rework |
| Next decision | The user choice that changes the plan | Keeps collaboration active |
| 3 Next Prompts | Use Now, Harden, Expand as copy-paste continuation prompts | Turns closeout into momentum and teaches the user how to steer the next exchange |
| Operator Lesson | A compact note about how to prompt, route, reuse, or delegate better next time | Builds compounding operator skill without making the user remember the whole system |

## Authority And Permissions

| Action | Agent May Do | Requires Approval | Never Do |
|---|---|---|---|
| Offer steering suggestions | Yes | No | Do not bury the answer under generic options |
| Recommend commands/workflows | Yes | No | Do not invent unavailable commands |
| Continue execution after steering | Yes, if user asked for execution | No | Do not stop at advice when implementation was requested |
| Interrupt urgent work | Only for material risk | No | Do not derail the task |

## Execution Protocol

1. Classify the depth tier using `high-floor-operator-os.md`: Light, Standard, Deep, or Parallel.
2. Always add an Operator Lesson to final answers unless the user requested only the direct answer or a tool requires silence.
3. For Light work, use only the micro lesson: `Operator Lesson: Next time, ask for [X] if you want [Y].`
4. For normal work, use the standard lesson: What I noticed, Better system move, Next-time prompt.
5. For builds, artifacts, strategy, client work, system work, or major decisions, use the full lesson and include Agent/Workflow I'd use, Subagent worth it?, and Reuse hook.
6. Use full Use Now / Harden / Expand steering only when the response has a real next decision, artifact, verdict, recommendation, extraction, build, system change, or client/strategy output.
7. For Standard/Deep closeouts, render steering as **3 Next Prompts**: each path must include when to use it, why it is recommended, a copy-paste prompt, expected output, quality bar, skip condition, and suggested skills/workflows.
8. If at kickoff, name the likely best path, one hidden risk/opportunity, and the decision that would speed the session up.
9. If mid-session, state what changed, the next best fork, and the tradeoff to watch.
10. If the user gives fast approval after a verdict, execute the recommended path directly when clear. Do not ask them to restate the plan.
11. Keep rationale dense: one sentence per field unless the user asks for depth.
12. Use concrete commands, artifacts, and paths when possible.

## Decision Rules

| Condition | Rule | Reason |
|---|---|---|
| Work is Standard or Deep | Use steering | High floor is the default |
| Every final answer gives the user something to react to | Add the right-size Operator Lesson | Builds compounding intelligence and reduces cognitive load |
| Substantial artifact or verdict was produced | Close with steering unless the user requested light/direct output | Prevents dead-end artifacts |
| Work is Light | Use only the micro Operator Lesson | Avoid ceremony while preserving learning |
| User is learning the system | Explain why each prompt is recommended and what it compounds or protects | Builds operator muscle |
| Validation or routing reveals a gap | Surface the gap and the fix | Prevents misfires |
| More than three paths exist | Pick the top 2-3 | Preserve momentum |
| User says "go with your verdict" | Execute the prior recommended path if clear | Lets fast-flow work continue without command memory |

## Examples

### Good Kickoff

"Best path: run `/extraction-governor-agent` first because this source may be a companion layer, not a new skill. Watch: if it has commercial use, capture the productized offer while building. Fastest decision: internal-only or client-facing first?"

### Good Midpoint

"What changed: the skill is valid and discoverable. Next fork: either harden the root workflow or package the client offer. I would harden first because it prevents future builds from drifting."

### Good Closeout

## 3 Next Prompts

1. **Use Now**
   - **When to use:** You have a real workflow or failed output to test.
   - **Why this is recommended:** It creates visible proof that the semantic layer changes output quality.
   - **Prompt:** `/semantic-doc-audit run this messy SOP, produce a before/after audit, and end with 3 Next Prompts.`
   - **Expected output:** Before/after audit with one converted work primitive.
   - **Quality bar:** A cold reader should understand the problem and the fix in 60 seconds.
   - **Skip if:** You do not have a real workflow or failed output to test.
   - **Suggested skills/workflows:** `/semantic-doc-audit`, `/steering-compass`

### Counterexample

"You could do marketing, automation, strategy, content, or operations next." This is too broad and does not teach the user how to steer.

## Quality Tests

| Test | Pass Criteria | Failure Response |
|---|---|---|
| Practicality | Each recommendation has a copy-paste prompt, expected output, and quality bar | Replace broad advice with prompt/artifact |
| Teaching value | User learns why the prompt matters and when to skip it | Add rationale, use condition, and skip condition |
| Noise control | Light work gets only a micro Operator Lesson | Compress to one line |
| Unknown unknowns | Surfaces only material opportunity/risk | Cut speculative ideas |
| Collaboration | Offers a fork or decision when useful | Add the decision that would speed work |
| Operator lesson quality | Lesson names a better prompt, route, reuse hook, or delegation cue | Replace generic coaching with a concrete next-time pattern |

## Failure Modes

| Failure Mode | Early Signal | Prevention | Recovery |
|---|---|---|---|
| Menu spam | Too many choices | Limit to 2-3 paths | Compress |
| Generic coaching | Could apply to any project | Name the concrete artifact/command | Rewrite |
| Execution slowdown | Advice replaces action | Keep moving after steering | Resume task |
| Overengineering | Adds ceremony to Light work | Use Light tier | Skip compass |

## Maintenance Protocol

- Owner: Codex Antigravity operator.
- Review cadence: after major workflow or closeout changes.
- Update triggers: user reports friction, repeated "what next" questions, missed expansion opportunities, shallow next paths, weak continuation prompts, or closeouts becoming noisy.
- Last updated: 2026-05-24.

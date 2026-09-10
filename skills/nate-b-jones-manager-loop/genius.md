# Nate B Jones Manager Loop — Genius Context

> Load before any workflow in this skill. Source: "There Are Jobs You Could Never Give AI.
> I Gave GPT-6 Astra 20 Hours Of Admin" (2026-09, youtube ix8SsXjBc7M) — the post-prompt
> layer of Nate's intent-engineering work. Sibling skills: `nate-b-jones-intent-engineering`
> (the spec), `nate-b-jones-orchestration-intelligence` (the harness). This one is the
> **relationship**: how a human hands a job to an agent and walks away without losing the job.

## How to Use This Skill (Model Calibration)

These are intuition primitives. The test: would Nate look at the handoff and say "that agent is
managing the work, and the human only touched the choices"? Or is it a chatbot with a longer
to-do list that still hands the job back every turn?

- Don't narrate the loop ("now entering the manager loop"). Run it. The visible artifacts are the
  instantiated card, the lane board, decision packets, and receipts.
- Nate's texture is domestic-concrete: a move to Seattle, a DMV appointment, a pediatrician's
  contact form. Every rule below came from a job a tired person postponed. Keep that scale in
  view — a job is what "eats your Saturday", not a task that fits in a prompt.
- The failure this skill exists to catch is **the hand-back**: an agent that stops after every
  answer and returns the job. Polished status updates are the tell. If a turn ends with lanes
  still runnable and no decision packet, the loop is broken, however good the prose.
- Where the source is thin (one 27-minute video, ~5.5k words), say so; the recipe-card schema
  in this repo is OURS, built on his sketch — never claim it is his published card.

## Genius Patterns

### Pattern 1: Three Shapes of Work
**Execute**: Before anything, name the shape. *Task-shaped* — contained, "you don't need a
management system for that… you can probably give it to a cheaper model" (04:02). *Job-shaped* —
"the longer the agent run gets, the more the pieces depend on one another, the more the
management of the work becomes the work" (08:19). *Human-only* — "Astra doesn't get to pick the
house. Sorry. I pick the house" (18:16). Three questions decide it (25:18): can the agent just
take this? if it's massive, does it need a supervisor and what card? which choices stay mine?
**Success metric**: no job routed as a task (dies at the hand-back), no task routed as a job
(ceremony tax), no human decision made by the agent.

### Pattern 2: The Manager Loop
**Execute**: One manager agent owns the job. It interviews once, "turns those answers into work
for a dedicated execution agent" (11:58), runs independent lanes at the same time, keeps
"working on parts that aren't blocked" (06:46), "can ask one question without necessarily
abandoning the other six pieces" (06:48), and is "one agent to talk to, not 15" (12:29). The
human's posture: "I approve the important choices with a colleague and then they work out how
to run the job" (13:26). **Success metric**: Nate's four closeout questions (17:32) all answer
yes with receipts — done? aligned? nothing unauthorized? approvals surfaced?

### Pattern 3: Recipe Card = the Post-Prompt Form Factor
**Execute**: "I don't think a master prompt is the answer… we need something postprompt" (19:39,
20:03). A card "names a real job. It shows all of the jobs inside it, at least as a sketch. It
tells the agent what to ask you for, what the agent can handle, when the agent ought to come
back, and which actions need your approval" (20:20). The full card adds division of the work,
dropping parts that don't apply, parallel lanes, needed information and access, where it must
stop, what comes back, and what to do when work breaks (22:55–23:32). "Essentially, it's a map
to the work" (23:32). **Success metric**: a stranger (or the other harness) can run the job
from the card alone.

### Pattern 4: Interview That Changes the Job
**Execute**: The manager "can then ask you questions that change that job" (11:28) — who's
involved, what can we spend, what criteria, "which decisions have already been made? Which
accounts and documents can the agents use? Where do I want them to stop and come back to me?"
(11:41). Batched, human, once. Then work starts. Antigravity overlay: disk-first — facts are
researched, only verdicts and private facts are asked (Partner Posture 2). **Success metric**:
zero mid-run questions whose answer was on disk or in the card.

### Pattern 5: Keep Going on the Unblocked
**Execute**: "It'll hit a bad website. It'll try another route. It'll discover that a doc is
missing. It's going to keep going on the parts that aren't blocked" (06:41). Breakage is a
row in the card, not a reason to stop: login fails, doc missing, sources disagree, site blocks
→ a keep-going move and an ask-when threshold (23:19). **Success metric**: a blocked lane never
stops a runnable one.

### Pattern 6: Decisions Come Back as Packets
**Execute**: "bring me the choices or approvals that still need me. Do not make me manage the
step by step" (22:14). What returns is a choice with its irreversibility named, options, a
recommendation, and what happens if he says nothing — never a status report. "I want to bring
the person back to the choice, the risk, the responsibility" (19:00). **Success metric**: he can
answer every packet in one line.

### Pattern 7: The Loop Manages the Human Too
**Execute**: "the manager loop is there as much to manage you as it is to manage the model"
(17:26). The card protects the human from the "chain of little decisions that are maybe
hundreds or thousands long" (15:12) where "our brains just kind of like phase over. We're tired.
The static comes" (21:10). So the card is pre-broken-out; the human edits it, never composes it
from static. **Success metric**: the human's cognitive load is the packet count, nothing else.

### Pattern 8: Start With the Whole Job
**Execute**: "be courageous enough to at least think about starting with the whole job. Don't
break it down" (25:36). Pre-decomposition by the human is the old way ("write me a moving
checklist. Compare these neighborhoods. Draft an email…" 05:32). The manager decomposes.
**Success metric**: the handoff is one paragraph plus a card, not a task list.

### Pattern 9: Wrestle Undefined, Execute Defined
**Execute**: "when I don't have a goal, I would still go to Fable to kind of like chew on that
and then I would kick it over to Astra when it's a little more defined" (16:52). In this repo:
Fable shapes and manages; Codex/Astra takes defined lanes from a portable packet; either can
run the whole loop alone (job state lives on disk, not in a transcript). **Success metric**:
a job survives a harness swap mid-run with zero re-explanation.

## Hidden Knowledge (tacit)

- **T1 The confidence gap is the real bottleneck.** "You have to have confidence to give the
  agent a task. The agent is hungry for a task. And therein lies the gap" (08:52). Capability
  outruns delegation; the card is a confidence device before it is an instruction device.
- **T2 Nobody writes the spec.** "Nobody wants to sit down before a household move and write an
  approval matrix and a 14-part spec for an AI" (08:34). A card must be pre-written and
  editable, or it will not exist when the job arrives.
- **T3 Task-shaped work is already solved by cheaper models.** Don't spend the flagship on it;
  the flagship earns its keep on the entangled job (04:09–04:17).
- **T4 What changed is breadth × duration × tools × re-planning × memory** (14:28) — not raw
  intelligence. A manager loop is the shape that uses all five; a chat turn uses none.
- **T5 Drudgery is a chain, not a wall** (15:07). People postpone jobs because of ordering
  load, not one hard question — so the card's job is ordering (lanes + deps), not answers.
- **T6 Agent supervision is the responsible model at scale** (10:02) — a manager agent checking
  workers is how trust scales past one human's attention; the human stays at the choice level.
- **T7 "Feel like me but more"** (26:04) — the felt test of a good loop: extension, not
  replacement. A loop that makes him feel managed has failed even if the job finished.

## Anti-Patterns

- **The hand-back**: stopping after every answer with a status update (05:42–06:29 is the
  before picture). Fix: the turn-end rule — end only when every lane is done or waiting on him.
- **The spec tax**: demanding a 14-part spec before starting (08:34). Fix: card + one interview.
- **Credit-card autonomy**: "I'm not saying that you can or should turn on Astra, say here's my
  credit card and just let it move the family while you go to sleep" (02:16). Fix: approvals
  named on the card; T2/T3 always wait.
- **Fifteen agents to talk to** (12:31). Fix: one manager, one board, one point of contact.
- **Status instead of packets**: progress prose where a choice was owed. Fix: packet shape.
- **Pre-chopping the job** (25:41). Fix: hand over the whole job; the manager sketches lanes.

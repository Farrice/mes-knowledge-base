# Hire-Yourself Audit

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Practitioner
> **Produces**: Hire-Yourself Audit
> **Slash Command**: `/gmind-hire-yourself-audit`

---

## Purpose

Burnout in an operator doing 90-hour weeks isn't a motivation problem — it's a structural one. Godin's diagnosis: every time the business gets hard, the operator hires the cheapest, most available person for the job, and that person is always themselves, because they work for free. This workflow classifies the operator first, inventories the week, and tags every task as freelancer work, entrepreneur work, or hiding — then names exactly what real work each hidden task is displacing.

---

## Inputs Required

1. **Operator Snapshot** — What the business does, how long it's been running, current headcount.
2. **Week's Task List** — Everything the operator actually did, hour by hour if possible.
3. **The Self-Description** — How they currently describe themselves ("entrepreneur," "founder," "freelancer") and why.
4. **The Complaint** — What they say is exhausting them, in their own words.

---

## Workflow

### Step 1: Classify the Operator First — the Asleep-Money Test

Before touching the task list, force the category split. Godin's test: *"An entrepreneur uses assets, usually other people's money, to build something bigger than themselves. An entrepreneur makes money when they're asleep. If you are doing the work, you're probably a freelancer."* Ask directly: does money arrive while this person sleeps, or only while they work? If freelancer — *"Freelancer, someone who gets paid when they work. They and they alone do the work"* — say so plainly before advising anything else. Misclassification is the root of most of the exhaustion in Step 3.

### Step 2: Inventory the Week's Tasks

List every task from the Week's Task List input without editorializing yet. Keep the granularity real — "answered client emails," "built the partnership deck," "designed the poster," "ran the open house." This is the raw material Step 3 sorts.

### Step 3: Tag Every Task

Sort each task into one of three bins: freelancer work (paid work the operator alone does), entrepreneur work (building assets that make money without them), or hiding. Use Godin's mechanism to catch the third bin: *"every time times get tough, they hire the best available cheapest person. You know who that is? Themselves. Cuz they work for free. And so, you end up hiring yourself to do all the jobs and no wonder you're exhausted cuz you're not doing your real job."* Any task that could be delegated but wasn't, done specifically because it felt safer than the real work, goes in "hiding" — regardless of how legitimate it looked on the calendar.

### Step 4: Run the Diagnostic on Every Hiding Item

For each item tagged "hiding," ask the question verbatim and answer it in writing: *"Every single time you are tempted to hire yourself to do a job, ask, 'What am I hiding from?' Cuz you're avoiding your real job, which is to build the assets that enable you to do none of the jobs."* Name the specific displaced work — not "growth" in the abstract, but the actual partnership, hire, or system that isn't getting built because this task ate the day instead.

### Step 5: Run the Dead-Zone Check

If headcount sits anywhere in the structural gap, name it as structural, not a discipline failure. *"There's a dead zone in between there. Don't fall into that zone. That zone of eight people or 18 people or 30 people where you're doing all the jobs, you're not getting paid enough, you're too busy to do anything, and you're stressed out of your mind. That happens when you fall into the gulf of trying to muscle your way through without leverage."* If the operator is in this zone, flag it explicitly in the output — the fix isn't more hours, it's leverage or exit.

### Step 6: Calibrate Against Godin's Own Scar

Use his admission as the honest floor, not an inspirational anecdote: *"I started one of the first internet companies, Mel. And grew it to almost 100 people. 50 of them reported directly to me. I would walk in at 8:00 in the morning and just nothing all day but interacting, answering questions, solving problems. And I was hiding from the important work of where am I going to find the big partnership that's going to transform this institution."* Even a founder at 100 people fell into the pattern. The audit isn't measuring willpower — it's measuring whether the calendar is structurally rigged toward hiding.

### Step 7: Write the Prescription

Two branches only, no third option. Either name the operator a freelancer and drop the entrepreneur guilt: *"Then you're a freelancer. Be a freelancer. It's fine."* Or point every hiding-tagged hour at the named displaced work from Step 4 and set a specific next action toward exiting the dead zone. Do not let the output land on "work harder" — that's the diagnosis being treated as the prescription.

---

## Output Schema

```
HIRE-YOURSELF AUDIT
=====================

Operator Classification: [Entrepreneur / Freelancer] — asleep-money test result

TASK LEDGER:
| Task | Tag (freelancer/entrepreneur/hiding) | If hiding: what's displaced |
|------|---------------------------------------|------------------------------|

DEAD-ZONE CHECK:
[In the zone / Not in the zone] — headcount + structural note

PRESCRIPTION:
[Be a freelancer, proudly — OR — named displaced work + next action toward asset-building]
```

---

Execution prompt: `references/prompts-v2/hire-yourself-audit.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Classification first | Asleep-money test run before any task is tagged |
| Every task tagged | No task left uncategorized; "hiding" isn't a catch-all excuse bin |
| Displacement named | Each hiding item names the specific real work it's avoiding |
| Dead-zone named | Headcount checked against the 8-30 person gulf explicitly |
| Prescription is binary | Freelancer-and-proud OR exit-toward-assets — never "work harder" |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/constraint-audit` | Find the single bottleneck the hiding is protecting the operator from facing |
| `/dan-martell-business-scaling` | Buy-Back-Your-Time delegation sequencing once hiding items are named |
| `/taki-moore` | Lifestyle-business redesign to route around the 8-30-person dead zone entirely |
| `/ash-founder-war-room` | Route the named displaced work through a weekly validation cadence instead of another hiding cycle |

# Client Portfolio Audit

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Practitioner
> **Produces**: Client Portfolio Audit
> **Slash Command**: `/gmind-client-portfolio`

---

## Purpose

A client roster isn't a revenue list — it's a calendar you signed without reading it. Godin's frame: *"when you pick your customers... you've just announced how you want to spend your days. Don't let your clients decide this. You decide."* This workflow audits the current client list as a design decision already made, contrasts what each client type turns the operator's day into, and builds the migration path to better clients — never more clients.

---

## Inputs Required

1. **Current Client List** — Names or types, with rough revenue and time-share per client.
2. **A Typical Day Log** — What the last 3-5 client interactions actually looked like (emergencies, line-item disputes, creative freedom, etc.).
3. **Target Client Profile** — Who the operator wishes they worked with instead, if named.
4. **Referral Behavior** — Has the operator ever referred a prospect to someone else? To whom, and why.

---

## Workflow

### Step 1: Diagnose — the Clients Are the Calendar

Before scoring anything, state the frame plainly: the current client list already determined how the operator's days feel. *"So you're going to spend most of your time dealing with your clients... or chasing people who aren't yet your clients. And you want to make them happy."* Walk the Current Client List and, for each client or client type, name what kind of day they produce — not what they pay, what they cost in attention and mood.

### Step 2: Run the Stopwatch vs. Danny Meyer Contrast

Sort each client against Godin's polarity: *"if your clients are really, really stressed out brides and grooms a week before their wedding in the Hamptons, that's who you're going to be spending all your time with. That's the kind of emergencies you're going to have to deal with. If your clients are people who are penny pinchers and who examine every single line item, well then be prepared that that's how you're going to have to spend your day."* Then the structural version: *"If you have a restaurant like McDonald's, McDonald's figured out that the clients that they could do the best with were in a car in a hurry to get somewhere. So what they do at McDonald's is there are inspectors with stopwatches... That is not what happens at the modern restaurant in Manhattan that Danny Meyer owns. There's nobody with a stopwatch there. Different clients, different output."* Tag each client: stopwatch-inspector energy or Danny Meyer energy. Neither is wrong — but they cannot be served by the same calendar without cost.

### Step 3: Build the Better-Clients-Not-More Ladder

State the ceiling before the growth plan: *"You can't have more clients, cuz you're a freelancer. But you can have better clients. Better clients challenge you more, pay you more, talk about you more."* Set the standard with the named case: *"Better clients are the ones like Chip Kidd, the great book cover designer. Chip Kidd can only design 30 book covers a year, whatever it is... No one goes to Chip and argues with him about typography. No one says, 'Go make this book look like my self-published mother-in-law's book.' He's Chip Kidd, for God's sake. That's how you move up."* Rank the current list against this standard: which clients would never argue about the craft, and which ones argue about everything.

### Step 4: Chart the Migration Path

Name the honest mechanism, not a shortcut: *"That doesn't mean you're cheaper. And you don't get to be that by doing a good job for bad clients. You do that by showing up where freelancers for good clients show up, doing work that freelancers for good clients do."* Translate this into specifics for the operator: where do freelancers-for-good-clients actually show up (which rooms, portfolios, referral chains), and what does the work sample need to prove to be found there. This step produces the concrete next move, not a wish.

### Step 5: Install the Time-Guard Rule and the Juilliard Standard

Close with the operating discipline. On time: *"guard your time like gold, cuz you don't get it back."* On selectivity, the teacher parallel: *"if you're going to have a whole bunch of fractious, sugared-up students who don't care about school, that's the way your day's going to be spent... Whereas if you go to some place that's selective and the people are really enrolled like Juilliard, you don't have to say people shut up and sit down, cuz you're teaching at Juilliard. The students you picked determine how you spend your day."* Set one enrollment standard the operator will hold new clients to before signing them.

---

## Output Schema

```
CLIENT PORTFOLIO AUDIT
========================

CURRENT ROSTER (calendar-as-designed):
| Client | Type (stopwatch / Danny Meyer) | What it costs your day |
|--------|----------------------------------|--------------------------|

BETTER-CLIENTS LADDER:
- Clients who'd never argue the craft (Chip Kidd standard): [names]
- Clients who argue everything: [names]

MIGRATION PATH:
- Where good-client freelancers show up: [specific rooms/portfolios/referral chains]
- What the work sample must prove: [specific proof]

ENROLLMENT STANDARD (Juilliard rule):
[one sentence — the bar new clients must clear]

TIME-GUARD COMMITMENT:
[what gets protected, starting when]
```

---

Execution prompt: `references/prompts-v2/client-portfolio-audit.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Calendar framing | Clients audited as a day-design decision, not a revenue list |
| Contrast run | Every client tagged stopwatch or Danny Meyer, not left neutral |
| Ladder is quality not volume | Migration targets better clients, never "more clients" |
| Migration path is concrete | Names actual rooms/portfolios where good-client freelancers show up |
| Enrollment standard set | One explicit bar (Juilliard rule) new clients must clear |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/blue-chip-client` | Land the recognizable-name clients the portfolio ladder is climbing toward |
| `/client-conversion` | Volume/quality tracking (CR × OU) on the migration path's actual outreach |
| `/track-record` | Build the proof-of-work sample the good-client rooms require |
| `/taki-moore` | Redesign the lifestyle-business model around selectivity instead of scale |

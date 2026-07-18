# Godin Consistency Protocol

> **Expert**: Seth Godin | **Skill**: seth-godin-brand | **Tier**: Practitioner
> **Produces**: Consistency Operating System + Role Definition
> **Slash Command**: `/godin-consistency-protocol`

---

## Purpose

Replace the authenticity trap with a professional consistency operating system. Define the ROLE your brand plays — not the personality of the person behind it — and engineer every touchpoint to be predictable from any angle.

---

## Inputs Required

1. **Brand/Person** — Who are we building the consistency system for?
2. **Current Challenge** — Where does inconsistency show up?
3. **Customer Expectations** — What do customers think they're getting?

---

## Workflow

### Step 1: The Authenticity Trap Diagnosis

Godin's position: "Authenticity is a crock. Authenticity is overrated. Authenticity is a trap."

**Symptoms of the Authenticity Trap**:
- [ ] "Being real" online means sharing bad moods, complaints, or personal drama
- [ ] Brand voice changes depending on who's writing
- [ ] Service quality varies based on how the team is feeling
- [ ] "I just want to be myself" used as excuse for inconsistency
- [ ] Personal struggles shared to build connection but actually eroding trust

**The Professional Standard Test**:
> Would you want your surgeon to be "authentically" in a bad mood during your knee implant?
> Would you want your paycheck "authentically" inconsistent?

If the answer is no — why would your customers want authentic inconsistency from you?

**The Cranky-Tuesday Exchange (added 2026-07-17, Mel Robbins interview Part 2)** — the live diagnostic version, run it on the operator:

> "Did you ever have a day this year where you were just really off, a little cranky, not your best?" ... "When you were like that and you got behind the microphone to record an episode, were you authentically cranky and subpar, or did you show up as the consistently magical version of Mel Robbins that you're capable of?"

Everyone answers "I showed up consistently" — which ends the authenticity argument with their own behavior. Follow with the scope note: *"authenticity is for your best friend, maybe for someone in your family... what everyone else wants from you is for you to make the story of you true."* And the excuse ban: *"you don't get to use the get out of jail free card of I was just being authentic. That's social media talk for I was being a jerk."*

**The becoming mechanism** — consistency compounds into identity: *"We become what we do. If you want to be a truthful person, start telling the truth and you'll become a truthful person."* Burnout guardrail (cross-ref `/godin-personal-brand-role` smock ritual): never install a consistent role diametric with who the operator wants to be.

### Step 2: The George Clooney Model

> "George Clooney doesn't say 'George Clooney would never say that' because he's not George Clooney. He's an actor."

**Define the Role, Not the Person**:

1. **Role Name**: "There is a role named [Your Brand] and it's not the person you might have dinner with"
2. **Role Boundaries**: What does this role always do? Never do?
3. **Empathy Source**: "The 60-year-old white guys making ballet slippers aren't ballet dancers — they use empathy"

| Dimension | The PERSON | The ROLE |
|-----------|-----------|---------|
| Bad days | Has them | Doesn't show them |
| Opinions | Has many | Shares only brand-relevant ones |
| Mistakes | Makes them | Owns and fixes them consistently |
| Energy | Fluctuates | Consistent in delivery |
| Voice | Personal | Professional + empathetic |

### Step 3: The Boiler Repairman Standard

The gold standard of consistency-as-marketing:

**Element 1: The Slippers** — Physical demonstration of "we care about your space"
> What's YOUR slippers? What tangible gesture shows customers you're a professional who cares?

**Element 2: The 25-Referral Clipboard** — Proof layered into the first interaction
> What's YOUR clipboard? What social proof do you present before the customer even evaluates your work?

**Element 3: The Result** — "Hired on the spot, cancelled the other three calls"
> When consistency is this visible, competition becomes irrelevant.

Design your three consistency signals:
1. **Care Signal**: [Physical/tangible demonstration of care]
2. **Proof Signal**: [Social proof embedded in the experience]
3. **Professional Signal**: [Element that says "we do this for everyone, every time"]

### Step 4: The Consistency Commitment

Write the promise that defines your role:

> "No matter which angle you look at us from, we're going to be like this. We're not going to talk about you behind your back. We're not going to manipulate you. We're not going to sneak things into the contract when you're not looking. We're going to be consistently the people we say we are."

**Your version**:
1. "No matter which angle you look at [brand], we will always..."
2. "We will never..."
3. "If [worst case], we will..."
4. "On our worst day, you can still expect..."

### Step 5: The "Mom Is Watching" Protocol

> Godin: "Nothing's off the record. Everyone is watching all the time. How do we want to behave when we know our mom is watching?"

For every customer touchpoint, apply the filter:
- Would I do this if the customer was watching? (They are.)
- Would I say this if competitors were watching? (They are.)
- Would I handle it this way if it was recorded? (It might be.)

If the answer changes based on who's watching → that's where inconsistency lives.

### Step 6: Consistency Operating System Output

```
CONSISTENCY OPERATING SYSTEM
==============================

Brand: [Name]
Role Defined: [Role name and description]

THE ROLE (NOT THE PERSON):
- Always: [list]
- Never: [list]
- On worst days: [minimum standard]

BOILER REPAIRMAN STANDARD:
- Care Signal: [your slippers]
- Proof Signal: [your clipboard]
- Professional Signal: [your "we do this for everyone"]

CONSISTENCY COMMITMENT:
"No matter which angle you look at [brand]..."

MOM-IS-WATCHING AUDIT:
- Touchpoints where behavior currently changes: [list]
- Fix: [how to make them consistent]

AUTHENTICITY TRAP ITEMS REMOVED:
- [What you'll stop doing in the name of "being real"]
```

---

## Output Schema

| Field | Type | Required | Notes |
|---|---|---|---|
| `Role Defined` | 1 name + description | Yes | Must read as a role ("the person who...") not a personality trait list. |
| `The Role` block | always-list + never-list + worst-day minimum | Yes | Never-list cannot be empty — a role with no boundaries hasn't been defined. |
| `Boiler Repairman Standard` | 3 signals (care/proof/professional) | Yes | All 3 must be tangible and specific — abstract answers like "great service" fail Step 3. |
| `Consistency Commitment` | 4-part written statement | Yes | Must follow the "no matter which angle... we will always/never..." template shape. |
| `Mom-Is-Watching Audit` | touchpoint-list + fix per item | Yes | Every touchpoint listed must carry a paired fix — a bare list of problems without fixes is incomplete. |
| `Authenticity Trap Items Removed` | list | Yes | At least 1 item — if nothing is being stopped, the audit wasn't run honestly. |

---

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Role Definition | Clear separation between person and role |
| Boiler Standard | 3 consistency signals designed |
| Commitment | Written, specific, testable |
| Mom Test | All touchpoints pass |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/godin-brand-promise` | Consistency protects the promise |
| `/godin-personal-brand-role` | Role definition feeds personal brand architecture |
| `/voice-document` | Consistency codified as voice reference |
| `/junyuh-brandbook` | Visual + verbal consistency unified |

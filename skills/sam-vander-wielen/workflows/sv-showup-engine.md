---
description: Build the show-up-rate machine — registration tag, question email, VideoAsk routing, the 6-beat 2-minute personal video script, and the coming-live micro-commitment
tier: 1
---

# /sv-showup-engine — The Personal Video Show-Up Machine

Produces the **complete automation map plus the video script** that turns registrations into attendance. Show-up rate is *"a very difficult part of webinars"* and this is Sam's answer: **583 personalized two-minute videos in a single launch.**

Her arithmetic, which is the whole justification: ***"Two minutes for a $2,000 sale is not bad."***

## Pre-Flight Gate

Load `genius.md`. Run the **Two-Minute Test** before building anything:

> State the per-unit time cost against the per-unit revenue out loud. *"Two minutes for a $[PRICE] sale is [verdict]."*

If that sentence sounds absurd at the user's price point, **stop and say so** — then either batch the act down (video only to registrants who reply), or route to a lighter reminder sequence. Do not ship a plan that burns the founder out for a $97 product.

Also check: is the founder actually the trust asset? If buyers don't care who they are, the personal video is noise.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md` — the video script fragments are near-verbatim deployable
3. The user's ESP (Kit assumed; adapt tags/automations to theirs)
4. Webinar date, offer, price

## Execution

### Step 1 — The trigger

On webinar registration, apply a tag (Sam: `registered for the webinar`). The tag fires the sequence. Confirm the user's ESP supports tag-triggered automation; name the equivalent if not Kit.

### Step 2 — The question email

Sent immediately on registration. Near-verbatim:

> **"Hey [FIRST NAME], I saw you signed up for my webinar. What's one thing you're hoping that I talk about in this class?"**

Requirements:
- Short. One question. No other asks.
- First name in the body, not just the greeting.
- The click routes to the response tool.

### Step 3 — The response router

Click opens **VideoAsk** (Typeform-owned) which asks:

> **"Would you like to send [NAME] a video, a voice note, or a text?"**

*Provenance note: the tool is identified as VideoAsk from the caption fragment plus Sam naming Typeform as the owner — see `source-ledger.md` claim 23. Any tool that accepts video/voice/text replies and lets you reply with video works.*

**Critical: she replies with a personal video regardless of which format they chose.** The asymmetry is the point.

### Step 4 — The 6-beat video script (~2 minutes)

Every video hits these, in order:

| # | Beat | Content |
|---|---|---|
| 1 | **Name** | Thank them, by first name |
| 2 | **Mirror** | Reference their specific words back — *"I always mention very specifics, anything that they've shared with me"* |
| 3 | **When** | Remind them of the webinar date and time |
| 4 | **Calendar + joke** | *"Add it to your calendar — I'll wait. You can do it right now. I'll just sit here."* The joke is what makes them actually do it |
| 5 | **Why it matters** | Say why their question is important and that you'll address it in the training |
| 6 | **The ask** | *"Are you coming live?"* — asks for a reply, starts a conversation |

**Beat 6 is the mechanic.** It creates the micro-commitment: they say yes, and later, when something runs long — *"oh, but I told Sam I was coming."* The video came first, which raises the cost of flaking.

### Step 5 — The duration objection, pre-handled

Sam found people asked *"how long do I need to be there?"* even when the emails said it a hundred times. Handle it **in the video**, spoken:

> "If you can go in your calendar and block this off for [DURATION]…"

### Step 6 — The commitment escalation (optional, high-conversion)

For launches tied to a month or milestone:

> "Are you committed to [MONTH] being the month that you finally [OUTCOME]? I know you've probably had this idea for a while. You and [N] other people have signed up for this and we're all doing it. You want in? Let's do it together."

### Step 7 — Batch and schedule the founder's hours

Compute: expected repliers × 2 minutes. Put the hours on the launch calendar as blocked work. **Do not let this be an assumption** — 583 videos is roughly 19 hours.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Under ~$1,000 price point** | Video only to registrants who reply to the question email; everyone else gets the sequence |
| **Very large registration volume** | Segment: personal video to repliers + any tagged high-intent (clicked sales page); templated-but-named video to the rest |
| **Service business / calls** | Same mechanic, trigger on booking. Beat 6 becomes "anything you want me to prep?" |
| **B2B** | Drop the joke stick; keep name, mirror, when, why-it-matters, and the confirm ask |
| **Non-founder-led brand** | Video comes from the named human who will actually run the session — never a brand account |

## Output Schema

```
SHOW-UP ENGINE — [Event] — [Date]

Two-Minute Test: "Two minutes for a $[X] sale is [verdict]" — PROCEED / BATCH DOWN / SKIP

## Automation Map
| Step | Trigger | Tool | Action | Tag applied |

## Question Email (verbatim, ready to paste)
Subject:
Body:

## Response Router
Tool: · Prompt copy: · Formats offered:

## Video Script — 6 beats
[each beat with example language for THIS offer]

## Duration handling line (verbatim)

## Commitment escalation (if applicable, verbatim)

## Founder Time Budget
Expected repliers: [ ] × 2 min = [ ] hours — blocked on: [dates]

## Reminder sequence for non-repliers
```

## Quality Gate

Reject and rebuild if:
- The Two-Minute Test was not run and stated
- Founder hours are estimated but not blocked on a calendar
- The video omits beat 6 (the coming-live ask) — without it there's no micro-commitment and the mechanic is decorative
- The video is templated without the mirror beat (referencing their actual words)
- A brand account sends the video instead of the human running the session
- The plan promises personal video at a volume the founder has not agreed to

**Execution prompt**: `references/prompts-v2/showup-engine.md`

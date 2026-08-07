---
description: Run ONE live webinar and weaponize the replay — private audio/podcast replay, accessibility as a conversion lever, live-only bonus split, separate tracking
tier: 3
stacks_with: content and podcast skills, /sv-launch-system, /sv-webinar-script
---

# /sv-replay-engine — One Live, Then the Replay Does the Work

Produces the **replay strategy**: formats, windows, the live-only bonus split, the promotion sequence, and the tracking plan.

Sam cut from **three live webinars in a 24-hour period** to **one**, and replaced the coverage with a replay she actually pushes. Her framing of why this is unusual: *"Something I'm doing that I don't see anybody else doing is being okay with the replay — as long as you're really good at getting people to actually watch it."*

## Pre-Flight Gate

Load `genius.md`. The decision this workflow forces:

> **Are you running multiple live sessions to cover time zones and schedules?**

If yes, this is the replacement. Sam's honest account of why she ran three: *"I was so convinced that people wouldn't sign up if it wasn't working for them."* And why she stopped: *"I don't know how I had the energy."*

The trade is only sound if the replay push is real. **A replay nobody watches is worse than three live sessions.** If the user won't commit to the promotion sequence, keep multiple lives and say so.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md`
3. The webinar structure (`/sv-webinar-script`) — needed for the bonus split
4. The user's podcast hosting setup, if any

## Execution

### Step 1 — Commit to one live session

*"This is it. Sign up or don't."* One date, one time. The scheduling anxiety is real and the answer is a better replay, not more sessions.

### Step 2 — Split the bonuses

| Carried by | What |
|---|---|
| **Live only** | The bonuses that reward attendance — Sam offers *"bonuses live that they can't get elsewhere"* plus, this launch, an extra financial incentive for purchasing on the webinar |
| **Replay too** | The core offer, the main teaching, the primary close |

The split must be **stated on the registration page**, not discovered at replay time.

### Step 3 — Build the private audio/podcast replay

This is the unlock most people skip. Sam: *"I make it a private podcast replay, like an audio version."*

Why it converts: it changes *when* the training can be consumed.
- *"I listened to you while I was making dinner and I still bought the bundle."*
- *"They listen in the car, they'll listen while they drive. Somebody told me they listen while they walked."*
- The people it reaches: *"they're new moms or people still working a nine-to-five."*

Her own honest note on the mechanism: *"I don't know why, because they could just [watch the video]. But I tried to remove friction as much as possible, and if that's it, then that's it."* **Ship the format; don't require a theory.**

Build requirements: private RSS feed, clear "here's how to add this to your podcast app" instructions, audio extracted from the live recording.

### Step 4 — Write the replay promotion sequence

The replay is *pushed*, not merely made available. Sequence across the cart window:
- Replay-is-live email, with both formats offered explicitly
- A "listen instead" email leading with the audio option
- A section-specific email pointing at the moment that answers the top objection
- Close-cart replay-expires notice

### Step 5 — Track separately

Sam tracks the podcast replay's downloads independently: *"We got thousands of downloads on the replay… I'm tracking that separately. So it's working."*

Set up: video replay views, audio replay downloads, and — where possible — purchases attributed to each. Without the split you can't tell whether the audio format earns its build.

### Step 6 — Set the expiry

The replay window must close, or the cart deadline is fiction.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **No podcast infrastructure** | Private RSS via the podcast host, or a simple audio file + instructions. Do not skip audio for lack of a "real" podcast |
| **Highly visual training** | Audio replay needs a companion PDF of the visuals; say so, or keep video-only and explain why |
| **Service business** | Replay pushes to a booked call, not a checkout |
| **Evergreen funnel** | Replay becomes the always-on asset; the live becomes the periodic refresh |
| **Small list** | Skip the separate audio build for launch #1; add it once you have replay-watch data |

## Output Schema

```
REPLAY ENGINE — [Webinar] — [Live date]

## Live Session
Single session: [date/time] — rationale for the time chosen

## Bonus Split
| Bonus | Live only | Replay carries | Stated on registration page? |

## Formats
| Format | Build requirement | Owner | Ready by |
| Video replay | | | |
| Private audio/podcast | | | |
Access instructions copy:

## Promotion Sequence
| Day | Email | Angle | Format led with |

## Tracking Plan
| Metric | Tool | Baseline |
Video views · Audio downloads · Purchases by replay format

## Expiry
Replay closes: [date/time] — how it's announced
```

## Quality Gate

Reject and rebuild if:
- Multiple live sessions remain "just in case" — that's the thing this replaces
- No audio/podcast format and no stated reason for omitting it
- The bonus split isn't disclosed on the registration page
- The replay is made available but not actively promoted across the cart window
- Video and audio aren't tracked separately
- The replay has no expiry while the cart does

**Execution prompt**: `references/prompts-v2/replay-engine.md`

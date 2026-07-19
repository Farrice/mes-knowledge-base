---
description: Stack — Daniel Priestley's SLL cadence (Pain/Prize/Problem +News lanes, LAPS pipeline) supplies the daily posting spine, Kallaway's Illusion of Novelty engine runs a per-post pass plus a lane-level staleness monitor, so a crowded niche's daily content keeps feeling new past week 3 instead of decaying into template soup
---

# `/kallaway-x-priestley-sll`: Kallaway × Priestley, Cadence-Scale Novelty

*Wave 3 crossing, promoted from Wave 2 bench (matrix score 4.0).*

The compound output: Priestley builds the cadence first. Four lanes (Pain, Prize, Problem, +News multiplier), one post per lane per day, every post bridged into the monthly long-form, every long-form bridged into the quarterly lead form. Priestley alone produces a system that never goes dark. By week 3, though, the Pain lane says "founders overspend before the message is settled" for the ninth time in nine different outfits, and the recommendation engine keeps recognizing the account without the audience feeling anything new. Kallaway alone produces a scroll-stopping post with no system underneath it: one great hook a week, surrounded by silence, mathematically invisible under Priestley's own 11×90 recognition math. Together, the cadence never breaks and the feeling of newness never runs out, because novelty is managed as a renewable resource at the lane level instead of chased post by post until the well runs dry.

## Stacking Partners
- **Priestley (SLL cadence)**: the spine. Four lanes, Pain, Prize, Problem, plus News as a multiplier rather than a fifth lane. One post per lane per day, bridged to monthly long-form, which is bridged to the quarterly lead form, which feeds LAPS (Leads, Appointments, Presentations, Sales). Supplies WHEN a post runs and WHICH lane it targets. Nothing in the cadence itself is negotiable; the novelty pass never reassigns a post's lane or skips a day.
- **Kallaway (Illusion of Novelty)**: two jobs at two different grains. Per-post: New Reveal (is this the first angle anyone reaches for, or a fresh door into the lane's fact) and Contrast Framing (against the niche's actual stock take, not a strawman), run on every post before it ships. Lane-level, the mechanic this crossing adds: a staleness monitor tracking each lane's angle pool across the batch. When a lane's fresh-angle supply runs dry, the fix is never to swap lanes; that breaks the targeting signal Priestley's whole system depends on. The fix is to rotate the reveal frame, the mining approach used to find new angles inside that same lane.

## When to Use
- An SLL System Map and lane bank already exist (or are being built in the same session), and the daily batch is starting to read like the same post wearing a different hat. The lane is right; the words are stock.
- A cadence has been running 2-3+ weeks and a specific lane, usually Pain because it's the easiest to over-mine, is producing posts a competitor in the same niche could lift unchanged.
- The team is tempted to fix lane fatigue by quietly drifting a Pain post into Prize territory, or skipping the lane assignment "just this once." That drift is the symptom this crossing exists to catch before the targeting signal degrades.

## Not This
This crossing owns cadence-scale novelty: the feeling of freshness sustained across a multi-week posting rhythm, at both the single-post and the whole-lane grain. It does not own everything novelty-adjacent:
- **Single-post novelty rescue** with no cadence or lane structure around it (one hook, one piece, no batch) routes to `/novelty-forge` or `/novelty-audit` directly. Those are the general-purpose engine and diagnostic this crossing specializes for the SLL batch grain.
- **Positioning statements** (the claim layer under the whole content system, not the daily posts running on top of it) route to `/kallaway-x-dunford`. That crossing gates novelty on Dunford's truth spine; this one gates novelty on Priestley's cadence spine. A brand often needs both: Dunford/Kallaway settles what's claimed, this crossing keeps what's posted from going stale.
- **No lane bank yet.** If SLL hasn't been installed for this business, route to Priestley's own Tier 1 front door, `01-sll-system-map`. Build the lane bank there first, then bring the finished bank here for the novelty-managed batch.

## Inputs
- `[SLL_SYSTEM_MAP]`: the business's lane bank (Pain/Prize/Problem language, avatar, offer) from a prior `01-sll-system-map` run
- `[BATCH_WINDOW]`: how many days/weeks of posting history to check for lane fatigue (minimum 5 days for a first pass, 15-20+ to make the staleness monitor meaningful)
- `[NICHE_STOCK_TAKES]`: the tired angles the niche runs on for each lane ("founders overspend on unclear messaging," "differentiate or die"). Pull from competitor content if not already known.
- `[CURRENT_NEWS]`: 1-3 genuinely trending stories for the ×News multiplier

## Execution (layered sequence)

### Step 1: Lane Bank In (Priestley)
Take the finished lane bank as-is. List Pain, Prize, Problem language plainly, plus the avatar and the wanted outcome. Assign one lane per post across the batch window, rotating so no two consecutive posts share a lane, with at least one post per week carrying the ×News multiplier. This is Priestley's layer; if the lane bank itself is thin or the avatar is vague, that's a System Map gap, not a Kallaway one. Send it back to `01-sll-system-map` before continuing.

### Step 2: Per-Post Novelty Pass (Kallaway, run on EACH post before it ships)
For every post, hold the lane assignment exactly fixed and run two checks on the *expression* only:
- **New Reveal**: is there a fresher door into this lane's fact, or is the wording the first cliché anyone in the niche reaches for? Never invent a new fact or promote the claim past what the lane bank supports; mine a new angle into the existing one.
- **Contrast Framing**: what does this niche's buyer already believe about brands making this kind of claim? Position the lane's fact against that held belief as a true opposite, anchored to `[NICHE_STOCK_TAKES]`, never a strawman.

Score each post fresh, decaying (stock but salvageable), or stale (verbatim niche phrase).

### Step 3: Lane-Level Staleness Monitor (Kallaway, the mechanic this crossing adds)
Across the full `[BATCH_WINDOW]`, group posts by lane and track the reveal frame each one used: the specific angle-mining approach (origin story, cost-of-inaction, sameness-audit, invisibility-fear, and so on), not just the surface wording. A lane is stale when its pool of fresh reveal frames is exhausted: multiple recent posts in that lane lean on the same mining approach even though the sentences differ. When a lane goes stale, don't swap the post into a different lane; the lane assignment is the targeting signal the recommendation engine reads, and drifting it breaks Priestley's system at the root. Instead, rotate the reveal frame used to mine that lane. A Pain lane stuck on "wasted spend" rotates to "invisible to the machine" or "claim-risk exposure": still Pain, still true, mined a different way.

Log the call: which lane, which frame exhausted, which frame it rotated to, and why the rotation stays inside the lane's fact set.

### Step 4: Bridge + Cadence Compile (Priestley)
Attach each post's bridge (comment-a-word or pinned long-form pointer). No orphan posts. Compile the batch with lane, novelty verdict, reveal frame, and bridge per post, plus the lane-level staleness log for the window.

## Output Format
```
LANE BANK (unchanged)
Pain: [claim/language]
Prize: [claim/language]
Problem: [claim/language]
+News multiplier: [current hook]

Per-Post Novelty Pass
Day | Lane(×News?) | novelty verdict (fresh/decaying/stale) | reveal frame used | contrast anchor | bridge

Lane-Level Staleness Monitor
Lane | frames used across window | exhausted? | rotation called (frame → frame) | why it stayed inside the lane

Truth/Targeting Audit
Any post that drifted lanes, promoted a claim, or invented urgency: [none, or flag + revert]
```

## What This Replaces
Replaces running Priestley's SLL cadence on autopilot with no novelty check, which produces a system that never goes dark but stops earning attention by week 3 because every Pain post is the same angle in a new outfit. Also replaces running `/novelty-forge` post by post with no cadence awareness: a string of individually great posts that quietly drift lane assignments to chase freshness, breaking the targeting signal the whole SLL system is built on. This is the only crossing in the stack that manages novelty as a resource pool per lane instead of per post, which is the actual failure mode of daily content. Not one bad post. One exhausted lane.

## Quality Gate
- [ ] Every post in the batch window carries its own New Reveal + Contrast pass, not just the week's flagship post
- [ ] No post drifted its lane assignment to chase freshness; lane purity holds even under staleness pressure
- [ ] At least one lane-level staleness call made and logged per batch window of 15+ days, or an explicit note that no lane hit exhaustion yet
- [ ] Every staleness rotation stays inside the lane's fact set: a new reveal frame, never a new claim or a borrowed claim from another lane
- [ ] Contrast Framing anchored to the niche's actual stock takes from `[NICHE_STOCK_TAKES]`, not a strawman
- [ ] Bridges present on every post; no orphan content per Priestley's own anti-pattern list
- [ ] Differentiation preserved: no lane bank yet routes to `01-sll-system-map`, positioning-layer novelty routes to `/kallaway-x-dunford`, single-post rescue with no cadence routes to `/novelty-forge`/`/novelty-audit`

## Pairs With
- `01-sll-system-map` / `02-sll-short-form-daily`: builds the cadence and lane bank this crossing runs novelty management on top of. Run first if no lane bank exists.
- `/kallaway-x-dunford`: adjacent, not upstream or downstream. Settles the positioning claim layer while this crossing keeps the daily posts built on that claim from going stale.
- `03-sll-long-form-explainer` / `04-sll-lead-form`: downstream. The bridged posts this crossing keeps fresh still feed the same monthly explainer and quarterly offer.
- `/novelty-audit`: the general-purpose diagnostic this crossing specializes for the SLL batch grain, adding the lane-level staleness mechanic neither Priestley alone nor `/novelty-audit` alone provides.

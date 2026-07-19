---
description: "Stack: Noah Hawley's season architecture supplies the arc spine (theme stated first, ending locked before installment one, per-installment tonal position and escalation logic). Luke Iha's Vicious Hooks engine writes each installment's hook with knowledge of where it sits in that arc, so a content series opens every entry with a hook that can weaponize what earlier installments planted, and a finale that cashes the whole season's promise."
---

# `/hawley-handshake-vicious-hooks`: Hawley × Iha, Arc-Aware Vicious Hooks

*Wave 3 crossing, promoted from Wave 2 bench (matrix score 3.7).*

The compound output: Hawley builds the season first. Question, locked ending, tonal arc, and a map of what each installment plants for later ones to use. Iha then writes the hook for each installment knowing exactly where it sits in that arc, not as a stripped-down single post. Hawley alone produces a well-architected series with flat opens; every installment gets read the way a topic list gets read, because the architecture never touches the first ten words. Iha alone produces individually vicious hooks that reset to zero every entry, because a hook writer with no series context can only pull stakes from the installment in front of them. Together, an episode-three hook can weaponize what episodes one and two planted, and the finale hook cashes a promise the reader has been carrying since the pilot without knowing it had a name.

## Stacking Partners
- **Hawley (season architecture)**: the arc spine. Theme stated as a question before installment one, the ending known and locked, each installment's tonal position across the run, and the escalation logic connecting them. Supplies what the series is for and where it's going. Nothing here is negotiable; the hook pass reads the spine, it never rewrites it.
- **Iha (Vicious Hooks)**: the 8-principle hook engine, applied per installment with the season bible open beside it. Relevance, stakes, and the open loop are no longer scoped to a single post. They're scoped to everything the series has planted so far and everything it still owes the reader.

## When to Use
- A content series (LinkedIn run, newsletter arc, thread campaign) has real architecture underneath it: a theme, a locked ending, tonal positions per installment. But the opens read like five separate posts that happen to share a topic. Nothing in installment 3 acknowledges installments 1 and 2 exist.
- A hook set was written installment by installment with no visibility into the rest of the arc, so every hook restates stakes from scratch instead of compounding them. The reader who followed the whole series gets no reward for having followed it.
- The finale installment needs to cash something: a claim made in the pilot, a tension held since the middle, a promise the series has been keeping without saying so. The current draft opens it exactly like every other entry.

## Not This
This crossing exists for series work only. Two adjacent workflows own what it doesn't:
- **Single-post hooks with no series context.** One LinkedIn post, one ad, no installment before or after it to plant against. Route to `/luke-iha-vicious-hooks` or `/vicious-hook` directly. There's no arc to exploit; running the handshake on a standalone post is theater over the same eight principles a straight Iha pass already covers.
- **Series architecture without hooks.** The theme, ending, and tonal arc are the whole ask; opens aren't the current problem. Route to `/hawley-content-season`. Build the season bible there. Bring it here only once the opens themselves are the bottleneck.

## Inputs
- `[SERIES_SUBJECT]`: publication or campaign, its audience, and the theme/question it's circling
- `[N_INSTALLMENTS]` and cadence (daily, weekly, or a fixed drop schedule)
- `[EXISTING_SEASON_BIBLE]` if one exists (from a prior `/hawley-content-season` run); otherwise this workflow builds a compressed one in Step 1
- `[AVATAR_HELD_BELIEF]`: what the reader already assumes, needed for stakes calibration per installment
- `[TRANSGRESSIVE_TOLERANCE]`: how far the hooks are allowed to push (Conservative / Edgy / Boundary-Pressing)

## Execution

### Step 1: Season Bible In (Hawley)
If `[EXISTING_SEASON_BIBLE]` exists, take it as-is; don't touch the spine. If not, build the compressed version needed for hook work:

```
Question the series is answering: ______________________________
Locked ending (Installment N), its job / arrival point: ________
Tonal arc across the run (shape): ______________________________
```

Each installment then gets an angle on the question and a tonal register, the way `/hawley-content-season` Step 3 breaks editions as episodes. This is the input the hook pass needs. If you can't fill it in, stop and run `/hawley-content-season` first.

### Step 2: Plant Map
Before any hook gets written, name what each installment plants: a claim, an image, a phrase, an admission, a number, that a later installment can legally cash. This is the layer a single-post hook writer has no access to.

```
Installment K plants: [specific element]
  Available to installments: [K+1, K+2, ... N]
  What cashing it would look like: _____________________________
```

An element only counts as planted if it's specific enough to name later without re-explaining it. "Talked about risk" isn't plantable. "The exact dollar figure a founder burned on creative for a message that wasn't finished" is.

### Step 3: Arc-Positioned Hook Pass (Iha, reading the Plant Map)
For each installment, in arc order, write the hook with the season bible and Plant Map open.

The pilot installment has nothing to exploit yet. Its hook's job is to set stakes and open a loop the finale will close. Iha's Principle 3 (natural intrigue) and Principle 4 (stakes) apply at full force here, and Principle 8 (consequence first) points forward: what does this installment plant that the reader won't understand the weight of until later?

Every middle installment checks the Plant Map first. If an earlier installment planted something this one can exploit, the hook opens by cashing it: naming the planted element directly, not re-summarizing the series. Run the standard 8-principle check (genius.md) on top of the exploit.

The finale must cash the season's central promise: the thing every prior installment has been quietly building toward. This is where Hawley's "the ending gives the whole thing its meaning" and Iha's stakes-escalation converge. The finale hook should be the most vicious in the run, and its viciousness should come from what only a reader of the whole series would recognize.

For every hook, still run the full 8-principle check from `luke-iha-vicious-hooks/genius.md`: relevant in the first line, Germanic and charged language, tight open loop, real stakes, seasoned specificity, doesn't read like an ad, caveman-simple, consequence before mechanism. The arc-position layer sits on top of these eight. It never substitutes for them.

### Step 4: Escalation Check
Read the N hooks in sequence, arc order. Confirm the stakes and viciousness climb (or deliberately dip before the finale spike; a quiet installment before the loud one is a legitimate tonal-arc move, not a failure) rather than flatlining. A series where every hook hits the same intensity reads as one long note, the short-form version of Hawley's "38 minutes of music in a 42-minute show."

```
Installment | stakes level (1-10) | tonal register | escalates from prior? (Y / deliberate dip / N)
```

Any plain `N` (flat, not a deliberate dip) sends that hook back to Step 3.

### Step 5: No-Context Test
For every hook that exploits a planted element (all middle and finale hooks), ask directly: could someone handed only this single installment, with zero visibility into the rest of the series, have written this hook? A "yes" means the exploit is fake, a generic hook wearing a callback costume. Rewrite until the answer is no.

## Output Format
```
HOOK BIBLE — [Series] · [N installments, cadence]

SEASON SPINE (Hawley, unchanged)
Question: ...
Locked ending: ...
Tonal arc: ...

PLANT MAP
Installment K plants: [element] -> exploited by: [installments]
...

ARC-POSITIONED HOOKS
Installment 1 (pilot) | register: ... | hook: "..." | plants: [...] | 8-principle scan: pass/flag
Installment 2 | register: ... | hook: "..." | exploits: [planted element + source installment] | 8-principle scan: pass/flag
...
Installment N (finale) | register: ... | hook: "..." | exploits: [...] | cashes: [the season's central promise]

ESCALATION CHECK
Installment | stakes (1-10) | register | escalates?

NO-CONTEXT TEST
Installment | exploit named | could a no-context writer have written it? (N required to pass)
```

## What This Replaces
Replaces handing a finished season bible straight to a hook writer with no instruction to read the arc, and replaces writing hook sets installment by installment with `/luke-iha-vicious-hooks` run cold on each entry in isolation. Both produce hooks that are individually fine and collectively wasteful: they never compound, so a reader following the whole series gets the same reward as a reader landing on installment 4 with no history. Also replaces running `/hawley-content-season` and calling the job done at the tonal-arc map. A season bible with unexploited plants is a set of loaded guns nobody picked up.

## Quality Gate
> **Anti-Pattern Check**: review the season spine against `noah-hawley-storytelling-mastery/genius.md § Anti-Patterns` and every hook against `luke-iha-vicious-hooks/genius.md § Anti-Patterns` before delivering.
- [ ] Season spine unchanged and complete: a real question, a locked ending, a tonal arc, not a topic list with a hook pass bolted on
- [ ] Plant Map names specific, cashable elements per installment, not vague "themes" that can't be exploited later
- [ ] Every middle and finale hook passes the No-Context Test: a hook writer with only that single installment could not have written it
- [ ] Every hook, regardless of arc position, still clears all 8 Iha principles individually; arc-awareness is additive, never a substitute for a vicious standalone hook
- [ ] Escalation holds across the run (or dips are deliberate tonal-arc moves, not flat misses)
- [ ] Finale hook cashes the season's central promise and is legibly the most consequential hook in the set
- [ ] Machinery invisible: no hook announces "as promised in installment 2." The exploit lands as recognition, not as a citation

## Pairs With
- `/hawley-content-season`: upstream. Builds the full season bible this workflow reads. Run first if no architecture exists yet.
- `/luke-iha-vicious-hooks` / `/vicious-hook`: the general-purpose hook engine this crossing specializes for series work. Run those directly for any standalone post with no arc to plant against.
- `/hawley-tonal-arc`: adjacent. Deepens Step 1's tonal-arc compression when the series needs a fuller register map than the compressed bible carries.
- `/hook-viciousness-audit`: downstream QA. Once hooks are written, audit the set against the 8 principles independent of arc position as a second-pass sanity check.

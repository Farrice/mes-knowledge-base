---
name: "Satori Graphics — Predictive Empathy Pass"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **Predictive Empathy** discipline: design not for what the viewer feels *now*, but for what they will carry into the next 60 seconds of their day. Most designs are loud because the designer assumed the viewer was already convinced, already interested, already emotionally aligned — most viewers are none of those things.

> "It assumes the viewer is already convinced, already interested, already emotionally aligned. But the truth is most people aren't." — Satori
> "Predictive empathy. Designing not for what the viewer feels right now, but for what they will feel in a few seconds from now and into their day." — Satori

## Input Required

- **[CURRENT DESIGN / DRAFT]** — the design being rewritten (or briefed) for emotional landing
- **[CATEGORY]** — insurance/financial, cybersecurity, health/medical, productivity, real estate, streetwear, newsletter promo, social/activist, or other (drives the loud-default and desired-next-emotion defaults)
- **[BRIEF INTENT]** — confirm the brief is NOT deliberately calling for confrontation/disruption/alarm (activist urgency work can correctly want loud); if it is, this workflow does not apply — say so and stop

## Execution Protocol

### Step 1 — Identify the Wrong Emotional Assumption

Examine the current design for loud-default tone and name its implicit assumption:

| Loud-default tone | Implicit assumption |
|---|---|
| Shouted headline | Viewer is already paying close attention |
| Dramatic imagery | Viewer is already emotionally engaged |
| Urgent CTA ("ACT NOW") | Viewer is already considering action |
| High-contrast palette | Viewer is already filtering for relevance |
| Stat-led ("87% OF X") | Viewer already trusts the stat-source |

### Step 2 — Map the Audience State

Document: pre-state emotion (30 seconds before contact — distracted? stressed? bored? curious? skeptical?), awareness level (Schwartz: unaware / problem-aware / solution-aware / product-aware / most-aware), trust level (cold/warm/hot), time-window (skim <3s / read 10-30s / study 60s+). Most-common reality by default: cold + distracted + problem-aware at best — assume this unless the brief proves otherwise.

### Step 3 — Define the Desired *Next* Emotion (ONE, not two)

| Next-emotion | Category fit |
|---|---|
| Calm reassurance | Insurance, financial, health |
| Curious recognition | Thought leadership, education |
| Quiet confidence | Premium, lifestyle |
| Permission relief | Wellness, personal growth |
| Energized clarity | Productivity, tools |
| Generous warmth | Community, family, hospitality |
| Solemn resolve | Advocacy, social impact |
| Mischievous delight | Creative, lifestyle, food |

Pick exactly one — predictive empathy fails when 2+ next-emotions compete.

### Step 4 — Apply the Empathy Shifts

- **Tone (headline/copy)**: loud→quiet ("STOP HACKERS DEAD"→"Quiet protection, working in the background"), demand→invitation ("BUY NOW"→"Find your fit"), stat-shout→recognition-quiet ("87% IGNORE THIS"→"Most people don't notice. You did.")
- **Visual energy**: high contrast→soft contrast; dramatic crop→breathing crop; dense composition→white space
- **One trust cue**: a small testimonial line (not a wall), a reassurance phrase ("at your pace"), a subtle trust symbol, or a single soft data point instead of a stat-blast
- **Palette migration**: toward the desired-end-emotion, not the alarm-emotion — see the calm/curious/confidence/relief/clarity/warmth/resolve/delight direction table in the skill's genius context
- **Pacing inserts** (sequenced media only): breathing pages (pure white, single image, no copy) function as Level-6 "pull" beats

### Step 5 — Validate the Rewrite (three states)

1. Cold + distracted: does it land without demanding pre-attention?
2. Skeptical, mildly interested: does it earn the next 5 seconds?
3. Already-considering: does it confirm the next-emotion, or fight it?

If any state fails, iterate.

## Output Contract

A Predictive Empathy Pass: audience state map, the wrong-assumption diagnosis, the desired next emotion (exactly one), all applicable empathy shifts (tone/visual/trust cue/palette/pacing) written as old→new, a three-state validation, executable element-level directives, and an anti-pattern checklist.

## Output Skeleton

```markdown
# Predictive Empathy Pass — [layout name]

## Audience State Map
- Pre-state emotion: [...]
- Awareness level: [...]
- Trust level: [...]
- Time window: [...]

## The Wrong Assumption (current design)
- Implicit assumption: [...]
- Loud-default move present: [...]

## Desired Next Emotion
- One emotion: [...] (not 2+)
- 60-seconds-after state: [...]

## Empathy Shifts Applied
- Tone: "[old]" → "[new]"
- Visual energy: [old] → [new]
- Trust cue added: [...]
- Palette migration: [...]
- Pacing inserts (if applicable): [...]

## Validation
- [ ] Cold + distracted reader test: passes
- [ ] Skeptical reader test: passes
- [ ] Already-considering reader test: passes

## Executable Directives
[element-level changes]

## Anti-Pattern Check
- [ ] No 2+ competing next-emotions
- [ ] No loud-default assumption survives
- [ ] One trust cue, not five
- [ ] Palette migrated, not merely adjusted
```

## Quality Gate

- Exactly one next-emotion locked (never 2+)
- The loud assumption is named explicitly, not gestured at
- Tone shift is documented with concrete old→new examples
- Trust cue is one, not a stack
- Palette is migrated toward the target emotion, not just tweaked
- All three validation states pass

## Creative Latitude

The empathy-shift categories (tone/visual/trust cue/palette/pacing) are the levers; the specific rewrite is the craft. Push for the tone shift that sounds like a real sentence a real brand would say, not a formula-filled template — the difference between "Quiet protection, working in the background" and a generic softening is specificity to this brand's actual voice. Resist adding a second trust cue even when a third feels tempting; restraint is the discipline this workflow exists to enforce.

## Deploy When

A draft feels loud/aggressive/shouty; the brief assumes a pre-aligned audience (it usually isn't); a live campaign isn't converting and the working diagnosis is emotional landing; or you're in a category that defaults to alarmist tone. Do not use when the brief deliberately calls for confrontation or urgency (activist/urgency work), or when the audience is genuinely pre-aligned (existing customers, internal comms).

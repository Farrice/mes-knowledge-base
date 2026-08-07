# COOZ FLYWHEEL — QUICKSTART
## How Farrice runs the content engine for Cooz
## Date: 2026-04-08

This is the operator guide for running `/cooz-flywheel` during the Ignition Phase. The full workflow file is at `.agent/workflows/cooz-flywheel.md` — this quickstart tells Farrice how to actually use it.

---

## What the flywheel does

Takes ONE of the following as input:
- **Type A**: A raw voice memo transcript from Cooz (5–10 minutes of freeform thinking)
- **Type B**: A trending topic prompt from the masculine development / fitness / recovery space

Produces ONE complete weekly content package:
- 1 × LinkedIn post (3 variants)
- 1 × Blog post / Substack article (800–1500 words)
- 1 × Podcast episode topic outline (Resurrection Series)
- 1 × Instagram carousel (5-7 slides)
- 1 × Instagram reel script (45–90 sec)

Every output is filtered through the Cooz Voice Profile (`03-cooz-voice-profile.md`) before it's delivered to Farrice for approval.

---

## The weekly cadence (Farrice operates this)

### Monday morning — input collection
1. Check if Cooz sent a voice memo over the weekend. If yes, use it. If no, pick a trending topic from this week's masculine-development space.
2. Transcribe the voice memo if needed (use any transcription tool — Whisper, Otter, manual).

### Monday afternoon — flywheel execution
1. In Claude Code, run: `/cooz-flywheel [path-to-transcript OR topic description]`
2. The flywheel produces a **Creative Brief** first. HALT — review the brief before proceeding.
3. Check: is the "specific moment" from the voice memo real and concrete? Is the "I-led confession" in Cooz's voice? Does the "you-pivot" arrive only once, at the end?
4. If brief looks good: type "go" or "approved" to unlock the 5-asset generation.
5. If brief looks wrong: specify what to change ("tighten the moment to the Wednesday session between clients," "the you-pivot is too long, cut to 1 sentence," etc.) and regenerate.

### Monday evening — draft review
1. Read the full 5-asset output.
2. Run the voice profile scan yourself: any banned phrases? Em dash overuse? Sustained you-narration? Any "Here's what/why/how" openers?
3. If clean: ship to Cooz for final edit.
4. If dirty: rewrite the flagged sections manually, do NOT regenerate — regenerating loses the approved brief.

### Monday night — Cooz's edit
1. Cooz reads the drafts on his phone.
2. Cooz edits to his final voice (should be minor — the flywheel already ran through his voice profile).
3. Cooz posts or schedules.

### Tuesday–Sunday — publishing and logging
1. Each day's post ships on schedule (M/W/F Lane A, Sunday Lane B, Tuesday or Thursday reel).
2. At end of week, log engagement numbers for each post into a simple Notion page or Google Sheet.
3. Sunday: quick review with Cooz — what landed, what didn't, what to tune in next week's flywheel run.

---

## The first flywheel run (Week 0 test)

Before Cooz sends his first voice memo, test the flywheel on EXISTING material. This is the Week 0 validation step.

**Test input**: `_active/clients/coach-cooz/04-deliverables/09-latest-context-april-2026.md`

This is already a voice memo transcript from Cooz (April 2026). Use it as the test input. Run `/cooz-flywheel 09-latest-context-april-2026.md` and see what comes out.

**Test criteria**:
- Does the output sound like Cooz or like AI doing a Cooz impression?
- Does the "specific moment" the flywheel picks match what Cooz was actually talking about?
- Does the rhythm match his SHORT-SHORT-SHORT-MEDIUM-SHORT cadence?
- Does any banned phrase slip through?
- Would Cooz recognize the voice as his own on first read?

**If the test output is flat or off-voice**: tune the voice profile BEFORE Monday. Look at which section of the profile the flywheel is ignoring and tighten it.

**If the test output is solid**: ship the flywheel to production mode and let Cooz know to start sending weekly voice memos.

---

## The voice memo prompts (when Cooz needs direction)

Cooz won't always have something top-of-mind to record. When that happens, Farrice sends him a prompt. These are the 10 prompt templates — rotate them:

1. **"Tell me about one session this week that stayed with you. What happened. What you were thinking. What you didn't say."**
2. **"What's a thing you watched a client do this week that reminded you of yourself three years ago?"**
3. **"What's a sentence you almost said to a client and decided not to? Why did you pull back?"**
4. **"What's happening in your own training right now? What are you learning about your own body that surprised you?"**
5. **"You got a new inquiry this week — what was the thing the guy said that made you think *that's the man in the valley*?"**
6. **"What's a line from McBroom's coaching of you that you're just now starting to understand?"**
7. **"What's a thing from Path of the Parable [book] that you were writing this week? Tell me the paragraph you almost deleted."**
8. **"What's the contrarian take you've been holding back from posting? Tell me why you haven't posted it yet."**
9. **"What's the moment this week when you were tempted to give a client softer advice than he needed? What held you back — or what gave in?"**
10. **"A man in your life (friend, client, family) is quietly losing the war with his body right now. You can see it. You can't name it to him. Describe what you see."**

Send ONE of these per week, not all at once. Cooz records 5–10 minutes in response. That's the week's raw material.

---

## The trending topic scan (when Cooz's voice memos aren't enough)

Some weeks Cooz won't send a memo, or his memo will be about something that doesn't fit any content pillar. In those weeks, Farrice scans for a trending topic in the masculine-development space and runs the flywheel in topic mode.

**Where to scan**:
- Joe Rogan Experience (what's the past week's most-discussed episode? What's Rogan's take? What's the contrarian take?)
- Modern Wisdom (Chris Williamson)
- Rich Roll Podcast
- Huberman Lab (what's the fitness/health topic of the week?)
- r/Fitness30Plus, r/loseit, r/Dad (what are the most-upvoted posts this week?)
- X / Twitter fitness space (what's being argued about?)

**How to pick a topic**:
- The topic must be something Cooz has a real opinion on
- The topic must fit one of the 6 content pillars (Diagnostic, Witness, Infrastructure, Resurrection Story, Sunday Letter, Offer)
- The topic must be contrarian to the dominant take in the space (per the 5 Contrarian Takes in the Playbook)
- The topic must be something the Man in the Valley is secretly thinking about

**Do NOT**:
- Pick a topic from creator Twitter (audience mismatch)
- Pick a topic from startup Twitter (audience mismatch)
- Pick a topic from biohacker culture unless the contrarian take is *"this is the trap"*
- Pick a topic from Instagram fitness influencers (audience mismatch)

---

## What to do if the flywheel produces bad drafts

The flywheel will fail sometimes. When it does:

**Failure mode 1 — The drafts are flat and generic.**
Cause: the voice memo was too abstract. The flywheel has no specific moment to anchor on.
Fix: send Cooz one of the voice memo prompts (above) asking for a specific scene. Regenerate with the new memo.

**Failure mode 2 — The drafts sound like AI doing Cooz.**
Cause: the voice profile is too loose. The flywheel is drawing from generic patterns instead of Cooz's actual vocabulary.
Fix: open `03-cooz-voice-profile.md` and tighten the rhythm fingerprint or the vocabulary banks. Add any new phrases you've noticed Cooz using that aren't in the profile yet.

**Failure mode 3 — The drafts contain banned phrases.**
Cause: the voice profile scan is not catching everything.
Fix: manually rewrite the flagged sections. Do NOT regenerate — the approved brief is lost on regeneration. Update the ban list in the voice profile so the next run catches it.

**Failure mode 4 — The drafts don't match the content pillars.**
Cause: the voice memo didn't fit any pillar, or the flywheel assigned the wrong pillar.
Fix: run the flywheel again with an explicit `--pillar=[name]` hint if the workflow supports it, or manually reassign the pillar in the Creative Brief stage.

**Failure mode 5 — Cooz heavily edits the drafts before posting.**
Cause: the voice profile is drifting from his actual voice.
Fix: save the edited versions. Diff them against the flywheel output. Update the voice profile with the patterns Cooz is consistently correcting.

---

## The feedback loop (for continuous improvement)

Every 4 weeks, Farrice reviews the last month of flywheel output:

1. **Engagement data**: which posts landed, which didn't, by format and by pillar
2. **Edit ratio**: how much did Cooz edit before posting? (Less edit = flywheel tuned well)
3. **Voice drift**: is the flywheel still producing drafts that sound like Cooz, or is it starting to sound generic?
4. **Pillar coverage**: did the month's output cover all 6 pillars, or did one dominate?

**If the flywheel is drifting**: spend 30 minutes updating the voice profile with recent Cooz material. Add any new vocabulary, pattern interrupts, or rhythm variations.

**If one pillar is dominating**: check the voice memo inputs. Are you prompting from the same angle every week? Rotate the prompt templates.

**If engagement is flat**: the problem is usually the hook, not the lane. Tighten the "specific moment" requirement in the Creative Brief. No more abstract openings.

---

## The lead magnet side output (every 4–6 weeks)

When the flywheel has accumulated 10+ shipped posts in ONE content pillar, package the best material into a lead magnet:

- **Format options**: a short PDF guide (1 of the 8 Tenets, deep-dive), a free audio series (3 episodes of the Resurrection Series packaged), a free Loom audit template
- **Deployment**: DM the lead magnet to anyone who engages with Cooz's content, use as warm-network follow-up, offer in podcast guest appearances
- **Capture**: lead magnet is delivered via simple email capture (Squarespace built-in, or ConvertKit free tier) — NOT a complex funnel

The lead magnet is not a separate project. It's a side output of the flywheel's accumulated content.

---

## The hand-off to Cooz (eventually)

Right now Farrice operates the flywheel for Cooz. Eventually — probably in the Scale Phase after 6 months of running it — Cooz learns to operate it himself.

The transition:
1. Months 1–3: Farrice runs the flywheel, Cooz never sees it
2. Months 4–6: Farrice runs the flywheel, Cooz shadows one session per week
3. Months 7+: Cooz runs the flywheel himself, Farrice reviews output on Sundays

But that's a Scale Phase concern. For Ignition, Farrice operates it alone.

---

## Related files

- **Workflow definition**: `.agent/workflows/cooz-flywheel.md`
- **Voice profile**: `_active/clients/coach-cooz/15-final-package/03-cooz-voice-profile.md`
- **Content pillars + psychographic map**: `_active/clients/coach-cooz/15-final-package/02-man-in-the-valley-playbook.md`
- **The Ignition Plan** (Section 5 for content rules): `_active/clients/coach-cooz/15-final-package/01-THE-IGNITION-PLAN.md`
- **Voice guide** (signature phrases + ban list): `_active/clients/coach-cooz/05-offers-and-frameworks/VOICE-GUIDE.md`
- **8 Tenets curriculum** (Lane A educational content): `_active/clients/coach-cooz/05-offers-and-frameworks/8-TENETS-FRAMEWORK.md`
- **WS1.6 voice rule** (Sheedy 6-step template): `_active/clients/coach-cooz/03-research/WS1.6-voice-validation-and-data-recovery.md`

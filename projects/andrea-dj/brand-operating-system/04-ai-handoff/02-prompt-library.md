# 02 — Prompt Library

*22 ready-to-paste prompts for common Resonance tasks. Copy a prompt block, paste into Claude/ChatGPT (with the AI Brain Master loaded), fill in the bracket variables, send. Each prompt produces an on-brand draft on first try.*

*Last updated: 2026-05-04. Status: canonical.*

---

## The Spine Reminder

> *Resonance is heart encounters, not head encounters — a daytime, sober dance party in Chicago for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is couples, not followers.*

---

## How To Use This Library

1. **Make sure the AI Brain Master is loaded** (`04-ai-handoff/00-ai-brain-master.md` pasted into the chat first, OR the Claude Project is set up per `01-claude-pro-project-setup.md`).
2. **Find the prompt you need below.** Each is in a copy-pasteable code block.
3. **Fill the bracket variables** — `[Profile target]`, `[event date]`, `[specific detail]`, etc.
4. **Send.** The AI produces one draft.
5. **Voice-check** (use prompt #11 if you want AI to do it; or eyeball against the voice document Section 7 checklist).
6. **Iterate** if needed. Each iteration: re-paste the AI Brain Master if drift creeps in.

---

## Category 1 — Content Production (7 prompts)

### Prompt 1 — IG Feed Post (Caption)

**When to use**: drafting a single-image IG feed post caption.

```
TASK: Draft an Instagram feed post caption for Resonance.

PROFILE TARGET: [umbrella / Nora / Imani / Marcus]
AUDIENCE STATE: [pre-contemplation / contemplation / preparation / action]
FUNNEL POSITION: [top — naming the problem / middle — showing the alternative / bottom — call to apply]
VISUAL: [describe the photograph — daytime room frame, founder portrait, etc.]

LENGTH: 100-180 words.
STRUCTURE: hook (≤2 sentences) → middle (one specific image or moment) → close (filter or invite, never both).
HASHTAGS: zero. Do not include any.

PATTERNS: lead with one of [out-loud-asking opener / anaphora cadence / crystallized phrases / show-first scene]. Land the close with one of [hell-yes filter / mechanic-as-sentence / single declarative].

CALIBRATE: against `02-briefs/ig-feed-post.md` if it's loaded in your knowledge.

Produce ONE version that passes voice. Don't give me three options.
```

**Expected output**: a 100-180 word caption with a sharp hook, a specific moment in the middle, a single-line close. No hashtags. Reads like Andrea wrote it.

**Calibration notes**: if the hook reads as a marketing question ("Are you tired of swiping?"), reject and rewrite. The hook must be something Nora/Imani/Marcus would actually say to a friend.

---

### Prompt 2 — IG Reel Storyboard

**When to use**: planning a 30-60 second Reel.

```
TASK: Draft a Reel storyboard for Resonance.

PROFILE TARGET: [umbrella / Nora / Imani / Marcus]
DURATION: [30s / 45s / 60s]
HOOK TYPE: [show-first scene / out-loud-asking voiceover / Andrea-on-camera direct address]
GOAL: [introduce the room / drive applications / capture a story moment / answer an objection]

OUTPUT: 6-12 scene cuts. For each cut:
- Visual (1-2 sentences — what's on screen)
- Audio/VO (the line spoken or the music cue)
- Duration (in seconds)
- On-screen text (max 5 words per scene; often zero)

Calibrate against `02-briefs/ig-reel.md` in project knowledge.

CONSTRAINTS:
- All footage daytime; no club lighting; no neon.
- No text-overlay walls. Maximum 5 words per scene.
- The audio is either Andrea's VO, ambient room sound, or a music cue from a curated track (never trending TikTok audio).
- Final scene = single declarative line + URL or "applications open [date]."

Produce ONE storyboard.
```

**Expected output**: a scene-by-scene Reel script with timing, audio, and on-screen text. Total runtime matches duration.

---

### Prompt 3 — IG Story Sequence

**When to use**: a multi-frame IG story (3-7 frames) building toward a CTA.

```
TASK: Draft a Story sequence for Resonance — [N] frames.

PROFILE TARGET: [umbrella / Nora / Imani / Marcus]
PURPOSE: [tease an event / drop a manifesto excerpt / share a behind-the-scenes moment / answer an FAQ]

FOR EACH FRAME:
- Visual (1 sentence)
- Text overlay (max 12 words; often shorter)
- Sticker/CTA (poll / question / link / none)

Frame N (final) = the CTA frame. Single line + a specific next step (link, save the date, "applications open [date]").

CALIBRATE against `02-briefs/ig-story.md` in project knowledge.

Constraints:
- Daytime imagery only.
- No "tap to learn more" pseudo-CTAs that link to nothing.
- One sticker per frame, max.
- Voice: warm, direct, no wellness vocabulary, no marketing slop.

Produce ONE sequence.
```

**Expected output**: N frame descriptions, each with visual + text + sticker. Final frame closes the loop with a specific CTA.

---

### Prompt 4 — Email Newsletter Draft (Editorial)

**When to use**: the bi-weekly editorial newsletter.

```
TASK: Draft an editorial newsletter issue for Resonance.

ISSUE TYPE: [post-event recap / pre-event anticipation / founder essay / a single observation / a quote-led piece]
PROFILE TARGET: [umbrella / Nora / Imani / Marcus]
ONE THING THIS ISSUE DOES: [name it in one sentence — never two]

LENGTH: 600-900 words body.
SUBJECT LINE: 35-50 chars. Use the out-loud-asking pattern OR a specific moment.
PREHEADER: 60-90 chars. Extends the subject; does NOT paraphrase.
CTA: ONE per email. Either "apply" / "read the manifesto" / "reply and tell me."

STRUCTURE: opener (a moment, a question, a scene) → middle (the story or thought, with one specific image) → close (a single sentence that lands).

CALIBRATE against `02-briefs/email-newsletter.md` in project knowledge.

PATTERNS (use 2):
- Out-loud-asking subject line.
- Anaphora cadence in body.
- One beat per issue (do ONE thing).
- Crystallized-phrase closing line.

Voice: Andrea's letter from a friend. No HTML banner. No social icons. Plain-letter feel.

Produce ONE issue.
```

---

### Prompt 5 — Anniversary Post (Year-1 / Event-#10 / Etc.)

**When to use**: marking a milestone — first event anniversary, tenth event, fifth couple.

```
TASK: Draft an anniversary post for Resonance.

MILESTONE: [name it specifically — "one year since Event #1" / "tenth Resonance" / "fifth couple to come back partnered"]
PRIMARY SURFACE: [IG feed / IG story sequence / email newsletter]
PROFILE TARGET: umbrella (anniversary content speaks to the whole audience)

STRUCTURE:
1. Open with a specific moment from the event/year (1-2 sentences).
2. Land the metric that matters (couples formed, NOT tickets sold or followers gained).
3. Close with the next thing (the next event, the next year, the next room).

LENGTH: matches the surface.
TONE: warm, grounded, no self-congratulation. The room did the work, Andrea is grateful.

PATTERNS: show-first opener mandatory. One mechanic-as-sentence in the middle. Crystallized-phrase or single declarative close.

BANNED:
- "What a journey it's been."
- "We've come so far."
- "Couldn't have done it without..." (unless we mean a specific person, named, briefly).
- Any year-in-review montage frame.

Produce ONE version.
```

---

### Prompt 6 — Behind-The-DJ-Booth Caption / Story

**When to use**: a behind-the-scenes piece showing Andrea at the decks (rehearsing, building a set, reading the room).

```
TASK: Draft a behind-the-DJ-booth piece for Resonance.

SURFACE: [IG caption / Story / email newsletter]
SCENE: [name what we're showing — Andrea building a setlist / Andrea at the decks during Event #N / Andrea testing a track that almost didn't make the cut]

STRUCTURE:
1. Open with the specific physical moment (the body, the gesture, the song).
2. Middle: the rule the moment reveals (the song-bends-the-room rule, the no-bar-the-music-warms rule, etc.).
3. Close: a single line that lands — not a CTA.

LENGTH: matches the surface.
VOICE: first-person Andrea. Personal but not confessional. Specific over general.

PATTERN: show-first opener mandatory. Mechanic-as-sentence for the rule. Crystallized phrases for the close.

Voice test: does this read like Andrea telling a friend over coffee about a moment she's still thinking about?

Produce ONE version.
```

---

### Prompt 7 — Manifesto Excerpt Card (For IG Post or Story)

**When to use**: pulling a single line from the manifesto and surfacing it as a graphic (text-on-cream).

```
TASK: Identify and frame a manifesto excerpt for Resonance.

SOURCE: `andrea-manifesto-v2.md` (or quote from `00-foundation/03-voice-document.md` Section 4 examples).

OUTPUT:
1. The single line (verbatim — do NOT paraphrase).
2. Visual treatment: text-on-cream (cream-100 background, midnight-900 type, GT Sectra 36pt).
3. Caption (if posted): 30-80 words contextualizing why this line. Or: zero caption — let the line stand.

Pick a line that can stand alone — something that lands without needing the surrounding paragraph. Five candidates from the manifesto + voice document:

1. "By the time you speak, your body has already made the introductions."
2. "We count the couples. That's the whole metric."
3. "You meet someone the way you meet a song. Your body knows before your mind does."
4. "If you've asked yourself why it's so hard to meet a good person, the answer is not another app."
5. "The music does the emotional labor so the people don't have to."

Suggest ONE with reasoning, OR draft a fresh manifesto-quality line if all five have been used recently.
```

---

## Category 2 — Triage (4 prompts)

### Prompt 8 — Triage A DM (Hunter / Performer / Tourist / Real)

**When to use**: a stranger DMs Andrea on IG with interest. Decide if they're hell-yes, polite-yes, tourist, or no.

```
TASK: Triage this Resonance DM.

DM:
"""
[paste the DM here verbatim]
"""

CRITERIA: Use `00-foundation/02-icp-master.md` Section 5 (the Hell-Yes Filter
Operational Form) and Section 7 (Anti-ICP categories).

OUTPUT:
1. Classification: [Hell-yes / Polite-yes / Tourist / Hunter / Performer / Heartbroken / Coupled / Other]
2. The 2-sentence reasoning — what specific signals in the DM led to this classification.
3. Recommended next action:
   - "Reply with X" (with the actual reply drafted in Andrea's voice)
   - "No reply needed" (with why)
   - "Flag for Andrea to read personally" (if it's edge-case)
4. If a decline script applies, name it (Hunter / Performer / Heartbroken / Tourist+Dancer-Averse).

VOICE for any drafted reply: warm, direct, no marketing. Use the relevant decline script
verbatim if it fits, OR draft from scratch using the script's register.
```

---

### Prompt 9 — Apply The 12 Lines To A Proposal

**When to use**: a partnership/sponsor/promoter offer arrives. Test it against the 12 Non-Negotiables before responding.

```
TASK: Test this proposal against Resonance's 12 Non-Negotiables.

PROPOSAL:
"""
[paste the inbound email or pitch verbatim]
"""

OUTPUT:
1. Run the proposal against each of the 12 Non-Negotiables (per `00-foundation/05-non-negotiables.md`):
   1. Daytime  2. Sober  3. Curated  4. No hookup culture
   5. Chicago-first  6. Founder-curated music  7. Stories over metrics
   8. Phones off the floor  9. No bar service  10. No promoter access
   11. No sponsor stage  12. No coupled gatecrashers

2. For each line: PASS / FAIL / N/A with one sentence of reasoning.

3. Verdict: ACCEPT / REJECT / NEGOTIATE. If NEGOTIATE, name the specific terms that
   would have to change for this to become an ACCEPT.

4. If REJECT, draft a 80-120 word decline in Andrea's voice — warm, specific, doesn't
   close future doors unless the proposal is morally adversarial.
```

---

### Prompt 10 — Drift-Signal Scan On A Decision

**When to use**: Andrea is considering a decision (a venue, a guest DJ, a sponsor, a content choice) and wants to check if it's drifting from the spine.

```
TASK: Scan this decision against `05-ops/03-drift-signals.md` (or the equivalent
drift-signal checklist).

DECISION:
"""
[describe the decision Andrea is considering]
"""

OUTPUT:
1. Which drift signals fire on this decision (name them specifically).
2. The reasoning — why this decision triggers each signal.
3. Recommended action: PROCEED / PROCEED-WITH-CAUTION / RECONSIDER / KILL.
4. If PROCEED-WITH-CAUTION, name the specific guardrail to put in place.
5. If RECONSIDER or KILL, name the alternative that honors the spine.

Be honest. Andrea would rather hear "this drifts" early than realize it after the room
has shipped.
```

---

### Prompt 11 — Voice-Check A Draft

**When to use**: a draft exists (caption, email, pitch, etc.) and you want a structured voice review before shipping.

```
TASK: Voice-check this Resonance draft against the standards in
`00-foundation/03-voice-document.md` Section 7.

DRAFT:
"""
[paste the full draft here]
"""

OUTPUT, in this exact format:

1. SPINE FIDELITY — pass/fail + reasoning.
2. PROFILE FIT — does the draft match the named target (Nora/Imani/Marcus/umbrella)? pass/fail.
3. VOICE MATCH — could Andrea say this to a friend over coffee? pass/fail.
4. AI TELLS — any "Here's what/why/how" openers? Any "It's not X. It's Y." reveals?
   Em-dashes ≤2? pass/fail per item.
5. BANNED PHRASES — list any from the wince-list (`03-voice-document.md` §5) that appear.
6. SHOW > TELL — does the draft lead with a moment or an abstraction? pass/fail.
7. ONE OF SIX PATTERNS — name which voice pattern is doing structural work.

OVERALL VERDICT: SHIP / REVISE / REWRITE.
If REVISE, give ONE recommended fix.
If REWRITE, name what's structurally wrong.
```

---

## Category 3 — Communications (4 prompts)

### Prompt 12 — Reply To Inbound Venue Email

**When to use**: a venue replied to outreach (or inbound interest came in). Draft the reply.

```
TASK: Draft Andrea's reply to this inbound venue email for Resonance.

VENUE TYPE: [arts space / restaurant private room / hotel ballroom / private home/loft]
THEIR EMAIL:
"""
[paste their reply verbatim]
"""

CONTEXT: Andrea wants the venue for [event date], [headcount], [3-hour 2-5pm window].

OUTPUT: a 100-200 word reply in Andrea's voice. Calibrate against
`02-briefs/venue-pitch.md` in project knowledge.

PATTERNS:
- Mechanic-as-sentence (the daytime / sober / 50 / 3-hour facts as sentences).
- Specific operational close (next step: 15-min call, signed contract, walk-through).

VOICE: warm, professional, never preachy. The venue is a partner, not a customer.
No marketing language.

Sign-off: Andrea's first name only.
```

---

### Prompt 13 — Reply To Inbound Press Email

**When to use**: a journalist/blogger/podcaster reaches out for a feature, interview, or quote.

```
TASK: Draft Andrea's reply to this inbound press email for Resonance.

OUTLET: [name + type — local Chicago paper, podcast, national mag]
THEIR ASK:
"""
[paste their email verbatim]
"""

OUTPUT: a 100-200 word reply.

PROTOCOL:
1. Confirm interest (one sentence).
2. Set expectations: Andrea is selective about press; she does interviews, not soundbites.
3. Offer next step: a 30-min call, the press one-sheeter (`02-briefs/press-one-sheeter.md`),
   or a yes-to-the-feature with conditions.

If the outlet is mismatched (a clickbait-trend-chase type), draft a polite decline
that doesn't burn the contact.

VOICE: warm, direct, confident. Press should feel they're talking to a founder who
has thought about every word — not a media-trained one.

Calibrate against `02-briefs/press-one-sheeter.md` for the framing.
```

---

### Prompt 14 — Draft The Hell-Yes Acceptance Email

**When to use**: an applicant cleared the why-gate. Draft the acceptance.

```
TASK: Draft the acceptance email for [applicant name].

THEIR APPLICATION ANSWER:
"""
[paste the one-sentence answer from the why-gate form]
"""

PROFILE THEY MATCH: [Nora / Imani / Marcus / umbrella]
EVENT: [date], [neighborhood], doors 2pm.

OUTPUT: 80-150 word email.

STRUCTURE:
1. Subject line: 35-50 chars. "You're in." OR "Saturday June 14, 2pm — your spot is locked."
2. Body opens with confirmation (you're in).
3. References ONE detail from their application answer ("when you said X about Y").
4. Sets the protocol: address goes out [date], if you're a maybe on event-morning give your spot up.
5. Closes with Andrea's signature.

ATTACHED: the digital ticket per `02-briefs/event-ticket.md`.

VOICE: warm, specific, never mass-blast. This person is named, seen, and welcomed.

Produce ONE version.
```

---

### Prompt 15 — Draft The Decline Script

**When to use**: an applicant did not clear the why-gate. Decline kindly.

```
TASK: Draft the decline email for [applicant name].

THEIR APPLICATION ANSWER:
"""
[paste their answer]
"""

DECLINE REASON: [Hunter / Performer / Tourist / Heartbroken / Coupled / Wellness Tourist /
Generic-not-hell-yes — pick one from `00-foundation/02-icp-master.md` Section 7]

OUTPUT: 80-120 word email.

STRUCTURE:
1. Subject: "Not this round." OR "From Andrea, on Event #N."
2. Body: warm decline, specific reason (without insulting), an honest door open or closed.
3. Sign-off: Andrea's first name only.

USE the relevant decline script from `00-foundation/02-icp-master.md` Section 7
(Hunter / Performer / Heartbroken / Tourist+Dancer-Averse) verbatim if it fits.

VOICE: warm, firm, respectful. Decline the application, not the person.

BANNED:
- "Best of luck on your dating journey."
- "After careful consideration..."
- "We'll keep your application on file."
- Any door-shutting blessing.

Produce ONE version.
```

---

## Category 4 — Generation (4 prompts)

### Prompt 16 — Generate A Midjourney/Sora Prompt

**When to use**: producing imagery for a tertiary surface where no real photograph exists.

```
TASK: Generate a daytime-locked Midjourney/Sora prompt for Resonance.

SCENE: [describe what we want — "dance floor in real afternoon light," "hands at a
water station," "Andrea-style DJ at decks daytime," "Pilsen sunset corner," etc.]

CONSTRAINTS (mandatory):
- Real daytime light (specifically: south-facing window, 2pm afternoon, overcast Chicago,
  warm directional sunlight). NO neon, NO club, NO night-coded language, NO "moody" or
  "cinematic dark" or "ethereal."
- Real bodies: mixed-race adults aged 30-40, varied body types, varied gender.
- No phones in frame, no alcohol, no flash.
- Tight crop on hands, gestures, the side of a body. NO identifiable faces (faces are
  forbidden in AI imagery for public Resonance use).
- Color: minimal grading; preserve actual daylight color temperature.

OUTPUT:
1. The full prompt (paste-ready into Midjourney/Sora/etc).
2. Recommended parameters (--ar 4:5 for IG, --ar 16:9 for video, --stylize 100, etc.).
3. Voice-check: confirm the prompt contains zero banned tokens (neon, club, night, glow,
   moody, cinematic dark, ethereal, low-key, dramatic lighting).

Calibrate against `04-ai-handoff/03-image-prompt-formulas.md` and
`01-visual/photography-rules.md` §6.
```

---

### Prompt 17 — Mood Board Reference List (For A New Asset)

**When to use**: starting a new visual asset and wanting reference images to anchor the work.

```
TASK: Generate a mood board reference list for [asset — flyer / web hero / Reel / press kit].

AESTHETIC: editorial broadsheet left in actual sunlight (Resonance's anchor aesthetic).

OUTPUT: 6-10 reference categories, each with 1-3 specific examples Andrea/Farrice can
search for:

1. PHOTOGRAPHY references — name specific photographers / publications / film stills
   that match the daytime + body-centered + decentered-composition register.
2. TYPOGRAPHY references — specific record covers, magazine spreads, or book jackets
   that pair a heat serif with a humanist sans.
3. COLOR references — specific images / objects / spaces that use the cream + midnight +
   terracotta palette in the way Resonance uses it.
4. LAYOUT references — specific editorial spreads or vinyl jacket layouts the asset
   should resemble structurally.
5. ANTI-references — what NOT to look like: name 3-5 specific brands / publications /
   visual styles to avoid (wellness retreats, club promo, dating-app marketing, etc.).

For each reference, give a one-line note on what it teaches the asset.

Calibrate against `01-visual/aesthetic-references.md`.
```

---

### Prompt 18 — Name A Track From A Description

**When to use**: Andrea is describing a song to play in a setlist or content piece and wants to surface specific track recommendations.

```
TASK: Name 3-5 specific tracks that match this description for Resonance.

DESCRIPTION:
"""
[Andrea describes the song — "the moment a song bends the room toward someone you
wouldn't have noticed an hour ago," "a track that earns the room paying attention,"
"slow opener that holds 90 seconds before anything happens," etc.]
"""

CONTEXT: Resonance's curatorial spine — Andrea-curated, beat-to-beat, no genre lock.
House, soul, afrobeat, vinyl deep cuts, the occasional ballad. The rule is whether
the song bends the room toward someone it would have ignored.

OUTPUT: 3-5 specific track suggestions. For each:
- Artist + track + year
- Why this track fits the description (1-2 sentences)
- BPM if known (helps Andrea pace the set)
- Whether it's a opener, mid-set, peak, or slow-down placement

Be specific. "Some house track" is not useful. Names + years + reasoning.

If you don't know any tracks that fit, say so explicitly. Don't fabricate.
```

---

### Prompt 19 — Three Hook Variants For A Post

**When to use**: drafting a post and wanting to test three hook approaches before committing.

```
TASK: Generate 3 hook variants for this Resonance post.

POST PURPOSE: [name it]
PROFILE TARGET: [Nora / Imani / Marcus / umbrella]

OUTPUT: 3 hook options, each using a DIFFERENT one of the six voice patterns:
- Variant A: out-loud-asking opener
- Variant B: anaphora cadence
- Variant C: show-first scene OR crystallized phrases

For each variant:
- The actual hook (1-2 sentences)
- Which pattern it uses
- Who it lands hardest with (which profile)
- One weakness — what's the trade-off compared to the other variants

Then: name your recommended pick and reasoning. Don't hedge — pick one.

VOICE: Andrea on a good day. No marketing questions. No TED-talk openers.
```

---

## Category 5 — Strategic + Operational (3 prompts)

### Prompt 20 — Pre-Event Briefing (Andrea's Self-Prep)

**When to use**: 48 hours before an event. Andrea wants a tight pre-event briefing covering the room, the set, the protocol, the contingencies.

```
TASK: Generate Andrea's pre-event briefing for [Event #N].

OUTPUT:
1. THE ROOM — confirmed attendees count, profile breakdown (P1/P2/P3 mix), any specific
   people Andrea wants to introduce to specific others.
2. THE SET — opening track (calibrated to room-arrival energy), 3 critical mid-set
   transitions, slow-song placement, closing track.
3. THE PROTOCOL — door check-in, phone-basket transition, witness circle timing,
   3-act dance arc, integration close.
4. CONTINGENCIES — top 3 things that could go wrong + the response (low fill, sound
   failure, attendee distress, gatecrasher attempt).
5. ANDREA'S NOTE — one sentence Andrea reads to herself before doors open. The reminder
   of why.

Calibrate against `05-ops/02-event-runbook.md` (or whatever the runbook is called in 05-ops).
```

---

### Prompt 21 — Post-Event Story Capture Plan

**When to use**: ~7 days after an event. Andrea wants to capture stories from attendees while they're fresh.

```
TASK: Draft a story-capture outreach plan for Event #N.

CONTEXT: Per Non-Negotiable #7 (Stories over metrics), the success metric is couples
formed. Story capture is how we surface them.

OUTPUT:
1. WHO TO CONTACT — 5-8 attendees most likely to have a story (returning attendees,
   ones who lingered at close, ones whose application answers were strong).
2. THE OUTREACH SCRIPT — a 100-150 word warm DM/email to each, asking for a
   15-min phone call about their experience. Voice: gentle, specific to them, no
   marketing.
3. THE INTERVIEW QUESTIONS — 5-7 open-ended questions for the call (e.g., "what
   moment in the room do you remember the strongest?" / "if you walked away with a
   number, what was the song playing when you decided?" / NEVER "would you recommend
   Resonance to a friend?")
4. CONSENT + PUBLISHING PROTOCOL — what we ask permission to share, what stays private,
   how a story might be used (newsletter quote, press one-sheeter, anniversary post).

VOICE: warm, never extractive. Stories are gifts; capture them like gifts.

Calibrate against the relevant ops doc on story capture.
```

---

### Prompt 22 — Funnel Health Check

**When to use**: monthly review of how the funnel is performing.

```
TASK: Run a funnel health check for Resonance.

INPUT:
- Awareness: [IG follower count, IG impressions last 30 days, newsletter subscriber count]
- Recognition: [profile visits, link-in-bio clicks, save rates]
- Engagement: [DMs received, comments, shares]
- Application: [why-gate form submissions]
- Acceptance/Decline: [accepted count / declined count / hell-yes-rate]
- Pre-Event: [confirmation rate, drop-out rate]
- Event: [actual attendance vs. capacity]
- Post-Event: [stories captured, repeat rate, referral rate]

OUTPUT:
1. STAGE-BY-STAGE: pass/concerning/failing for each stage with the metric that's the
   leading indicator.
2. FRICTION POINTS: where in the funnel are we losing people? Name the top 2.
3. RESONANCE-SPECIFIC: are we optimizing for couples-formed or for ticket-count?
   (Per `03-marketing/07-funnel.md`, Resonance breaks the standard playbook.)
4. RECOMMENDED ACTION: the ONE intervention that would most move the leading indicator
   for the most-failing stage.

Be honest. If a stage is failing, name it. Don't hedge.
```

---

## How To Maintain This Library

When a new task type emerges in Andrea's workflow that doesn't fit a prompt above:

1. Draft a prompt block in the same structure (TASK → variables → OUTPUT format → VOICE rules → calibration reference).
2. Test it in a fresh Claude session with the AI Brain Master loaded.
3. Iterate the prompt until it produces an on-brand draft on the first try.
4. Add it to this file as a numbered prompt in the right category.
5. Update the count in the file header (currently "22 ready-to-paste prompts").

---

## Source Citations

- `00-foundation/02-icp-master.md` Sections 5, 7 — triage criteria + decline scripts
- `00-foundation/03-voice-document.md` Sections 2, 3, 5, 7 — patterns, voice rules, banned phrases, voice checklist
- `00-foundation/05-non-negotiables.md` — the 12 lines (referenced in Prompt 9)
- `01-visual/photography-rules.md` §6 — the daytime-locked AI prompt rules (referenced in Prompt 16)
- `02-briefs/*.md` — every brief is a calibration reference for at least one prompt above
- `03-marketing/06-why-gate-mechanics.md` — referenced in Prompts 14, 15
- `03-marketing/07-funnel.md` — referenced in Prompt 22
- `04-ai-handoff/00-ai-brain-master.md` — the cold-start that makes all of these work
- `04-ai-handoff/03-image-prompt-formulas.md` — calibration source for Prompt 16
- `05-ops/*` — calibration source for Prompts 20, 21

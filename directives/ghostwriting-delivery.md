# Ghostwriting Delivery Protocol

> **Purpose**: Standardized operating procedure for the Ghostwriting Voice Engine (GVE). Governs intake, voice capture, content production, quality verification, and client delivery.
> **Scope**: Any agent or workflow that touches ghostwriting MUST follow this directive.
> **Separation**: Completely separate from MES. Different input, different output, different pipeline. See [MES Boundary](#mes-boundary-enforced) below.

---

## Pipeline Overview

```
CLIENT INTAKE → VOICE CAPTURE CALL → VOICE PROCESSING → CONTENT PRODUCTION → QUALITY GATE → DELIVERY
```

| Phase | Input | Output | Timeframe |
|-------|-------|--------|-----------|
| 1. Intake | Client signup | Completed intake form + content samples | Before call |
| 2. Voice Capture | 30-min call | Recording + raw notes | Call day |
| 3. Voice Processing | Transcript + intake assets | Completed Voice Profile | +24 hours |
| 4. Content Production | Voice Profile + content brief | 3-5 LinkedIn posts | +24 hours |
| 5. Quality Gate | Draft posts | Verified posts | Same pass |
| 6. Delivery | Verified posts | Google Doc package | 48hr total |

---

## Phase 1: Client Intake

### Pre-Call Assets Required

Collect ALL of the following before scheduling the call:

1. **Intake form** -- `_active/offers/intake-form-questions.md`
   - Business basics (niche, ICA, offer)
   - Content goals (growth? leads? authority?)
   - LinkedIn current state (follower count, posting frequency, what's worked)
   - Voice self-assessment (how they describe their own style)
2. **Content samples** -- minimum 1, ideally 3-5
   - Their best-performing LinkedIn posts (if any exist)
   - Blog posts, newsletter issues, or podcast clips
   - DMs or emails where they sound most natural
3. **Video/podcast link** (optional but high-value)
   - Any recording where they're speaking naturally (interview, webinar, coaching replay)
   - This is gold for voice pattern analysis

### Intake Verification Checklist

Do NOT schedule the call until all boxes are checked:

- [ ] Intake form completed (no blank fields in required sections)
- [ ] At least 1 content sample provided (link or text)
- [ ] Call time confirmed with recording consent
- [ ] Call script reviewed -- `_active/offers/call-script.md`
- [ ] Client directory created: `_active/clients/[client-name]/`
- [ ] Intake saved to: `_active/clients/[client-name]/intake.md`

---

## Phase 2: Voice Capture Call

### Call Execution

**Reference**: `_active/offers/call-script.md` (pull up during the call)

**Core rules:**
- **Record everything** (Zoom/Otter.ai -- get explicit consent)
- **Get them coaching, not explaining** -- "Coach me right now" is the most important prompt
- **Don't pitch, don't sell** -- this is a listening session
- **Chase the energy** -- when they light up, go deeper
- **Write down verbatim phrases** -- exact words, not paraphrases

**Call structure** (30 minutes):
1. **Opening** (0-2 min) -- Set the frame: "I'm capturing how you think and talk"
2. **Story capture** (2-7 min) -- "Walk me through your proudest client transformation"
3. **Live coaching** (7-17 min) -- THE MOST IMPORTANT BLOCK. "Coach me right now."
4. **Contrarian takes** (17-22 min) -- "What does your industry get completely wrong?"
5. **Signature insights** (22-27 min) -- "What makes clients go 'oh shit'?"
6. **Core message** (27-30 min) -- "One thing you'd want your perfect client to know"

### Post-Call Immediate Actions

Do these within 5 minutes of hanging up:

1. **Save/download recording** -- do not wait
2. **Start transcription** -- Otter.ai or upload to processing tool
3. **Write raw impressions** (3-5 sentences):
   - What's their energy? (calm authority? intense passion? warm mentor?)
   - What surprised you?
   - ONE WORD to describe their voice
   - Who do they remind you of? (writer, speaker, public figure)
4. **Capture verbatim phrases** -- 3-5 specific phrases that were uniquely them
5. **Flag the best 2-3 quotes** for potential post hooks
6. **Note red flags** -- topics they seemed uncomfortable with, forced language, contradictions

Save post-call notes to: `_active/clients/[client-name]/call-notes.md`

---

## Phase 3: Voice Processing

### From Call to Voice Profile

**Skill reference**: `skills/ghostwriting-voice-engine/` -- Read `genius.md`, execute `workflows/01-voice-capture.md`

**Input**:
- Call transcript (full)
- Post-call raw notes
- Intake form data
- Content samples from intake

**Output**:
- Completed Voice Profile using template at `_active/offers/voice-profile-template.md`
- Saved to: `_active/clients/[client-name]/voice-profile.md`

### Expert Ensemble

Deploy in sequence:

| Expert | Role | What They Extract |
|--------|------|-------------------|
| **Lara Acosta** | 5-dimension voice extraction | Vocabulary, rhythm, emotional range, teaching style, belief system from transcript |
| **Mitch Albom** | Belief mapping + embodiment test | Core convictions, narrative instincts, the worldview that drives their coaching |
| **Erica Mallet** | Voice DNA crystallization | Spectrum positioning, signature patterns, what makes them sound like THEM vs. generic coach |

### Voice Profile Quality Check

The Voice Profile MUST pass all three before advancing to content production:

1. **Test paragraph** -- Write one paragraph in their voice. Does it pass the Voice Consistency Checklist?
2. **Specificity audit** -- Is every field filled with SPECIFIC data (exact phrases, named patterns, concrete examples)? Generic descriptions = profile failure.
3. **Recognition test** -- Would the client recognize their own voice in the test paragraph? If you read it aloud, does it sound like them on their best day?

**If the profile fails any check**: Go back to the transcript. The profile missed something. Re-extract, don't patch.

---

## Phase 4: Content Production

### From Voice Profile to Posts

**Skill reference**: `skills/ghostwriting-voice-engine/` -- Read `genius.md`, execute `workflows/02-content-production.md`

**Input**:
- Completed, verified Voice Profile
- Content brief (topics, goals, number of posts requested)

**Output**:
- 3-5 LinkedIn posts per batch
- Saved to: `_active/clients/[client-name]/posts/[date].md`

### Expert Ensemble

| Expert | Role | When |
|--------|------|------|
| **Voice Profile** | The primary constraint -- every decision filtered through the profile | Always (non-negotiable) |
| **Nicolas Cole** | Voice preservation + structural power optimization | Every post -- ensures posts are effective AND authentic |
| **Ward Farnsworth** | Rhetorical device injection (antithesis, parallelism, tricolon) | Premium clients only -- adds stylistic elevation without losing voice |

### Post Production Rules

1. **Every post must pass the Voice Consistency Checklist** (Phase 5)
2. **No post should sound interchangeable** -- if you could swap the byline to any coach, the post fails
3. **Read each post aloud** -- does it sound like the client on their best day? Not your best day. Theirs.
4. **Every post needs a specific CTA** aligned with the client's business goal (not generic "follow me" or "agree?")
5. **Vary the format** across the batch -- not all hooks, not all stories, not all listicles
6. **Preserve their imperfections** -- if they use short sentences, don't smooth them into flowing prose. If they start sentences with "And" or "But," keep it.

---

## Phase 5: Quality Gate -- The Voice Authenticity Standard

> **Trigger**: Run on every post before delivery. No exceptions.

### 10-Point Voice Authenticity Checklist

| # | Check | Pass/Fail |
|---|-------|-----------|
| 1 | **Signature opening** -- Opens with the client's characteristic pattern? | |
| 2 | **Signature language** -- Includes at least one of their phrases or metaphors? | |
| 3 | **Sentence rhythm** -- Matches their Voice Profile pattern (short/punchy vs. flowing)? | |
| 4 | **Closing pattern** -- Ends with THEIR pattern, not a generic CTA? | |
| 5 | **Red line words** -- Zero words from their "never use" list? | |
| 6 | **Emotional range** -- Intensity appropriate for the topic (matches their spectrum)? | |
| 7 | **Specificity level** -- Numbers, names, and details match their style? | |
| 8 | **Speak test** -- Sounds like something they'd SAY out loud? | |
| 9 | **Best-day test** -- Better than what they'd write themselves, but still them? | |
| 10 | **Business goal** -- Serves their business (clients, not just engagement)? | |

### Scoring

- **8-10 pass**: Ship it
- **6-7 pass**: Revise the failing elements, re-check
- **5 or fewer pass**: **Rewrite from scratch.** Don't patch -- the voice wasn't captured properly

### Failure Protocol

| Scenario | Action |
|----------|--------|
| Post fails 2+ checks | Rewrite the post. Do not patch individual lines. |
| Multiple posts fail the same check | The Voice Profile has a gap. Go back to transcript. |
| Client says "this doesn't sound like me" | **CRITICAL** -- treat as profile failure, not post failure. Identify the gap in the Voice Profile, fix it, then regenerate all posts. |
| Posts sound good but generic | Voice Profile is too surface-level. Re-run Erica Mallet's Voice DNA crystallization. |

---

## Phase 6: Delivery

### Standard Timeline

| Milestone | Deadline |
|-----------|----------|
| Call completed | Day 0 |
| Voice Profile delivered | Day 0 + 24 hours |
| Posts delivered | Day 0 + 48 hours |
| Revision round 1 (if needed) | +24 hours from feedback |
| Revision round 2 (if needed) | +24 hours from feedback |

### Delivery Format

Package as a Google Doc containing:

1. **Posts** -- numbered, each with:
   - The post content (ready to copy-paste)
   - **Publishing Notes**: suggested posting time, hashtag recommendations, engagement plan (who to tag, which comments to respond to)
2. **Voice Profile** -- included as appendix
   - Client keeps this as a reference asset
   - Useful if they want to write posts themselves between deliveries
3. **Style Guide Quick Reference** -- one-page summary of:
   - Their signature phrases
   - Words to always use / never use
   - Opening and closing patterns
   - Tone spectrum

### Revision Rules

- **Max 2 revision rounds included** in standard delivery
- **Revision scope**: tone, voice, phrasing adjustments
- **NOT revision scope**: different topics, different angles, complete rewrites for new ideas -- that's a new brief, not a revision
- **"Doesn't sound like me" = CRITICAL feedback** -- this is NOT a revision. Go back to the Voice Profile, identify the gap, fix the profile, then regenerate. This does not count against revision rounds.
- **Track revision patterns** -- if multiple clients flag the same type of issue, the system has a blind spot. Update this directive.

---

## Demo Workflow (No Client)

### Purpose

Prove the system works using public content. Create before/after demos that serve as both proof of capability and content for Farrice's own LinkedIn.

### When to Use

- **Pre-launch** -- build confidence + proof before signing the first client
- **Outreach** -- DM coaches with unsolicited demos (the "free taste" strategy)
- **Content** -- before/after posts showcasing the transformation
- **Practice** -- sharpen the system on real voices without client pressure

### Process

**Skill reference**: `skills/ghostwriting-voice-engine/` -- Read `genius.md`, execute `workflows/03-unsolicited-demo.md`
**Step-by-step guide**: `_active/offers/demo-workflow.md`

**Input**: Coach's public LinkedIn content (3-5 recent posts minimum)
**Output**: Before/after package saved to `_active/demos/[coach-name]/demo.md`

**Package contains**:
1. Voice analysis (what patterns exist in their current content)
2. 1-2 rewritten posts (same topic, elevated with their captured voice)
3. Brief note explaining what changed and why

**Demo quality standard**: The rewritten post must be obviously better AND obviously still them. If it's better but sounds like someone else, the demo fails.

---

## MES Boundary (ENFORCED)

GVE and MES are completely separate systems. Do NOT cross the streams.

| Dimension | MES (Methodology Extraction) | GVE (Ghostwriting Voice Engine) |
|-----------|-----|-----|
| **Input** | Video/audio transcripts, courses, interviews | Voice capture calls + writing samples |
| **Output** | Agent skills (`.md` files in `skills/`, `agents/`) | LinkedIn posts (client content deliverables) |
| **Purpose** | Build expertise INTO the system | Write AS someone for external delivery |
| **Pipeline** | Extract → Convert → Deploy | Capture → Profile → Produce → Deliver |
| **Storage** | `skills/*/`, `agents/*/`, `extractions/` | `_active/clients/`, `_active/demos/` |
| **Directive** | `directives/mes-3.0-extract.md` | `directives/ghostwriting-delivery.md` (this file) |
| **Workflow** | `/extract`, `/convert-extraction` | `/ghostwrite` |

**Enforcement rules**:
- Do NOT use MES extraction prompts to build Voice Profiles
- Do NOT use GVE voice capture to create system skills
- Do NOT store client deliverables in `skills/` or `agents/`
- Do NOT store system skills in `_active/clients/`
- If uncertain which pipeline applies, ask: "Am I building a capability for the system, or producing content for a human client?" MES = system. GVE = client.

---

## Template Dependencies

These files are referenced throughout this directive. Create them as needed:

| Template | Path | Status |
|----------|------|--------|
| Intake form questions | `_active/offers/intake-form-questions.md` | EXISTS |
| Call script | `_active/offers/call-script.md` | EXISTS |
| Voice profile template | `_active/offers/voice-profile-template.md` | EXISTS |
| Demo workflow guide | `_active/offers/demo-workflow.md` | EXISTS |
| Before/After template | `_active/offers/before-after-template.md` | EXISTS |

---

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, review for relevance or archive.

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-02 |

**Update Rule**: When this protocol fires (any phase executed), update "Last Activated" and increment count.

---

*Created: 2026-03-02 | Ghostwriting Voice Engine — Delivery SOP v1.0*

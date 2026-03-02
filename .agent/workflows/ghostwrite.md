---
description: "Ghostwriting Voice Engine -- capture a coach's voice and write LinkedIn content as them"
---

# /ghostwrite — Ghostwriting Voice Engine

Capture a coach's voice and produce LinkedIn content that sounds like them on their best day. Routes to the appropriate GVE skill workflow based on the sub-command.

## Usage

```
/ghostwrite capture [client name]  — Voice capture pipeline (intake + call processing → Voice Profile)
/ghostwrite produce [client name]  — Generate LinkedIn posts from an existing Voice Profile
/ghostwrite demo [coach name/URL]  — Build a demo from public content (no client call needed)
/ghostwrite                        — Show usage guide
```

**Examples:**
- `/ghostwrite capture sarah-chen` — Start intake or process Sarah's voice capture call
- `/ghostwrite produce sarah-chen` — Generate a batch of posts using Sarah's Voice Profile
- `/ghostwrite demo @melissacoach` — Scrape public content, build before/after demo package

---

## Execution

### For `/ghostwrite capture [client]`

#### 1. Load Directive
// turbo
Read `directives/ghostwriting-delivery.md` — the delivery SOP. This governs everything.

#### 2. Check Client State
// turbo
- Look for client directory: `_active/clients/[client-name]/`
- If no directory: create it (`mkdir -p _active/clients/[client-name]/posts`)
- Check for intake form: `_active/clients/[client-name]/intake.md`

#### 3. Route by State

**No intake form exists:**
- Load the intake form template from `_active/offers/intake-form-questions.md`
- Present the intake questions to the user
- Save completed intake to `_active/clients/[client-name]/intake.md`
- Prompt: "Intake saved. Schedule the voice capture call, then come back with the transcript."

**Intake exists, no transcript yet:**
- Confirm intake is complete (all required fields)
- Review call script: `_active/offers/call-script.md`
- Present pre-call checklist from the directive
- Prompt: "Ready for the call. After the call, provide the transcript and I'll build the Voice Profile."

**Intake + transcript/recording provided:**
- Proceed to voice capture processing
- Load skill: Read `skills/ghostwriting-voice-engine/genius.md`
- Execute `skills/ghostwriting-voice-engine/workflows/01-voice-capture.md`
- Deploy expert ensemble: Lara Acosta → Mitch Albom → Erica Mallet
- Run Voice Profile quality checks (test paragraph, specificity audit, recognition test)
- Save output to `_active/clients/[client-name]/voice-profile.md`

#### 4. Checkpoint
Present the completed Voice Profile for review. Wait for approval before flagging the client as ready for content production.

---

### For `/ghostwrite produce [client]`

#### 1. Load Directive
// turbo
Read `directives/ghostwriting-delivery.md`.

#### 2. Verify Voice Profile
// turbo
- Load Voice Profile from `_active/clients/[client-name]/voice-profile.md`
- If no profile exists: "No Voice Profile found for [client]. Run `/ghostwrite capture [client]` first."
- If profile exists: confirm it passed quality checks

#### 3. Gather Content Brief
Ask the user (batch all questions):
- **Topics**: What should the posts be about? (list 3-5 topics or themes)
- **Goals**: What business outcome? (leads, authority, community, launch support)
- **Count**: How many posts? (default: 5)
- **Format preferences**: Any specific formats? (stories, hot takes, frameworks, listicles)
- **Timing**: Any time-sensitive topics? (events, launches, seasonal)

#### 4. Execute Production
- Load skill: Read `skills/ghostwriting-voice-engine/genius.md`
- Execute `skills/ghostwriting-voice-engine/workflows/02-content-production.md`
- Deploy expert ensemble: Voice Profile (constraint) → Nicolas Cole (optimization) → Ward Farnsworth (premium only)
- Run every post through the 10-point Voice Authenticity Checklist
- If any post scores below 8/10: rewrite (don't patch)

#### 5. Deliver
- Save posts to `_active/clients/[client-name]/posts/[YYYY-MM-DD].md`
- Present posts with publishing notes (timing, hashtags, engagement plan)
- Include Voice Profile reference for the client

---

### For `/ghostwrite demo [coach]`

#### 1. Load Directive
// turbo
Read `directives/ghostwriting-delivery.md` — specifically the Demo Workflow section.

#### 2. Gather Source Material
- Accept a LinkedIn URL, coach name, or pasted content
- Need minimum 3 recent LinkedIn posts (ideally 5+)
- If URL provided: scrape public content
- If name provided: search for their LinkedIn presence

#### 3. Execute Demo Pipeline
- Load skill: Read `skills/ghostwriting-voice-engine/genius.md`
- Execute `skills/ghostwriting-voice-engine/workflows/03-unsolicited-demo.md`
- Analyze their current voice patterns
- Select 1-2 posts for the before/after treatment
- Rewrite with elevated voice (better AND still them)

#### 4. Package Output
- Create demo directory: `_active/demos/[coach-name]/`
- Save to `_active/demos/[coach-name]/demo.md`
- Package contains:
  - Voice analysis (patterns found in current content)
  - Before/after posts (original + rewritten)
  - Brief explanation of what changed and why

#### 5. Usage Prompt
Suggest next steps:
- "Use this as a DM attachment for outreach"
- "Turn the before/after into a LinkedIn post about your ghostwriting service"
- "Use it as proof of concept for your offer page"

---

## Dependencies

| Asset | Path | Required By |
|-------|------|-------------|
| Delivery SOP | `directives/ghostwriting-delivery.md` | All sub-commands |
| GVE Skill | `skills/ghostwriting-voice-engine/` | All sub-commands |
| Call Script | `_active/offers/call-script.md` | `capture` |
| Intake Form | `_active/offers/intake-form-questions.md` | `capture` |
| Voice Profile Template | `_active/offers/voice-profile-template.md` | `capture` |
| Demo Workflow Guide | `_active/offers/demo-workflow.md` | `demo` |

---

## Chain Compatibility

- **Standalone** (most common) -- each sub-command runs independently
- **Natural sequence**: `/ghostwrite capture` → `/ghostwrite produce` (standard client delivery)
- **Lead generation**: `/ghostwrite demo` → DM outreach → client signs → `/ghostwrite capture`
- **Does NOT chain with** `/extract` or MES workflows -- GVE and MES are separate pipelines

### Handoff: capture → produce

```markdown
## Chain Handoff: capture → produce

**Client**: [Name]
**Voice Profile**: _active/clients/[client-name]/voice-profile.md
**Profile Quality**: [Passed/Failed] — [score details]
**Key Voice Markers**: [2-3 signature patterns]
**Ready for Production**: [Yes/No]
```

---

## Notes

- GVE skill directory: `skills/ghostwriting-voice-engine/`
- Client files: `_active/clients/[client-name]/`
- Demo files: `_active/demos/[coach-name]/`
- This workflow does NOT touch `skills/*/` or `agents/*/` — that's MES territory
- Quality gate from `directives/quality_gate.md` runs on every post output

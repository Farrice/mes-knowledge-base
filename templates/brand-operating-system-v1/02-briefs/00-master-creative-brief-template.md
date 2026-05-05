# 00 — Master Creative Brief Template

*{{SPINE_FRAME}}... a daytime, sober dance party in {{CITY}} for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is {{SUCCESS_METRIC}}.*

*Every per-asset creative brief inherits from this template. Open every brief by paste-mounting the spine reminder above; then fill the 9 sections below. If a section doesn't apply, name why explicitly — never silently drop it.*

---

## How To Use This Template

1. **Copy this template** when creating a new asset-brief.
2. **Fill all 9 sections.** Each section has a why-it-matters note and a fill-in pattern.
3. **Validate against the Quality Gate** at the end before shipping the brief.
4. **The brief gets pasted into AI tools alongside the task.** The brief itself must be AI-pasteable — no fat, no filler, no "as you can see above."

---

## Section 1 — The Spine Reminder (always at the top, paste-in)

> *{{BRAND_NAME}} is heart encounters, not head encounters... a daytime, sober dance party in {{CITY}} for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is {{SUCCESS_METRIC}}.*

This appears verbatim at the top of every brief. Don't paraphrase. Don't shorten. The repetition is the point — every AI session opens here.

---

## Section 2 — What This Brief Is For (purpose)

One paragraph (3-5 sentences). Answer:
- What asset is this brief producing? (IG feed post / venue pitch / flyer / etc.)
- What's the operational job? (announcement / nurture / triage / conversion / proof / referral / etc.)
- Where in the funnel does it sit? (top / middle / hell-yes-confirmation / post-event)
- What's the one thing this asset MUST do, even if it does nothing else?

**Pattern**: *"This brief produces [asset]. Its job is [operational role]. It sits at [funnel position]. The one thing it must do: [single goal in one sentence]."*

---

## Section 3 — ICP Target (which profile, what state)

Name the target precisely. Three layers:

1. **Profile**: {{ICP_PROFILE_1_NAME}} (#1 LOCKED, arts worker) / {{ICP_PROFILE_2_NAME}} (#2 PROPOSED, from Simone) / {{ICP_PROFILE_3_NAME}} (#3 PROPOSED, from Darius) / All-three / Umbrella ("the out-loud-asking 30-40 hell-yes seeker"). See `00-foundation/02-icp-master.md` for full profiles.
2. **Audience State**: pre-contemplation / contemplation / preparation / action. From the 60% TAM rule (`02-icp-master.md` Section 1).
3. **Bridge Message**: Quote the Bridge Message for the targeted profile from `02-icp-master.md`. This is the single sentence that lets the reader cross from their current state to the next.

**Pattern**:
> *Profile: [Name(s)] — Audience State: [pre-contemplation / contemplation / preparation / action] — Bridge Message: "[verbatim from ICP master]."*

If targeting multiple profiles, prioritize: which is primary, which is secondary, why both work without splitting the message.

---

## Section 4 — Voice Rules (compressed reminder, 1 paragraph)

Inherit voice from `00-foundation/03-voice-document.md`. The compressed paragraph any brief inherits:

> Warm, direct, confident, never preachy, never corporate. Show > tell at sentence level. Heart-encounter language as headline, body-first only as explanation. Em-dashes ≤2 per piece. No "Here's what/why/how" openings. Name the enemy by name (apps / bars at 11pm / speed-dating-as-party) when appropriate. Never preach sobriety — "we don't need it here," not "you shouldn't need it anywhere." "Community" only when earned. Voice test: would {{FOUNDER_NAME}} say this to a friend over coffee?

For asset-specific briefs, name 1-2 voice patterns from the 6 (anaphora / frame-then-sharpen / crystallized-phrase / out-loud-asking / hell-yes filter / mechanic-as-sentence) that THIS asset type leans on most.

---

## Section 5 — Format Spec (the constraints)

The actual production constraints for this asset. Examples:
- **IG feed post**: image dimensions, caption length, hashtag count, link allowance
- **Email**: subject line char limit, preheader, CTA structure, length floor/ceiling
- **Flyer**: physical size, print resolution, color profile, paper stock if relevant
- **Venue pitch**: format (email or PDF), length, attachments, response time expectation

Format spec is hard, not soft. If the asset can't hit the spec, the brief failed.

---

## Section 6 — Hook & Structure Patterns (named, with examples)

Which structural moves work for this asset type. Pull 2-4 from the BOS arsenal:
- **Out-loud-asking opener**: lead with the question the ICP is already asking
- **Anaphora cadence** (Pattern 1): the You've-tried voice signature
- **Frame-then-sharpen** (Pattern 2): clean declarative + 3 named enemies
- **Hell-yes filter** (Pattern 5): two-sentence repel-and-attract
- **Mechanic-as-sentence** (Pattern 6): mechanics in full sentences with stakes
- **Show-first opener**: a moment, not a description (the body in the room before the brand explanation)
- **Quote-led**: an exit-interview quote (with permission) as proof
- **Photo-led**: a real moment image, copy follows

For each pattern named: 1 GOOD example + 1 BAD example specific to the asset type.

---

## Section 7 — Visual Spec (when applicable)

If the asset has visual production:
- Color palette (cite `01-visual/DESIGN.md` for hex codes)
- Typography (heat serif / clean sans / hand-script — when each)
- Photography rules (cite `01-visual/photography-rules.md` — *if a photo could have been taken at 11pm, it fails*)
- Layout system (cite `01-visual/component-tokens.md`)
- Anti-patterns (what NOT to design — club lighting, fake golden-hour filters, stock dancers, AI-portraits, neon, etc.)

For copy-only briefs (e.g., DM responses, decline scripts), this section is "N/A — text only."

---

## Section 8 — AI Prompt Formula (the paste-in)

The actual prompt structure that produces this asset when pasted into Claude / ChatGPT / Midjourney / Sora / Suno. Format:

```
[Spine reminder verbatim]

[Profile target + state + bridge message]

[Voice rules paragraph]

[Asset format spec]

[Hook/structure patterns named]

[Visual spec if applicable]

TASK: [the specific request — e.g., "draft a 200-word IG feed post announcing Event #1 to {{ICP_PROFILE_1_NAME}} in contemplation state. Lead with out-loud-asking opener. End with hell-yes filter."]

CALIBRATE BEFORE WRITING:
- Re-read the spine and voice rules
- Name which voice pattern you're using
- Self-check the output against banned phrases (see voice document)
- Confirm the asset honors the format spec

Then produce.
```

Every brief includes this prompt formula tuned to its asset type. The brief is a paste-in, not a reading exercise.

---

## Section 9 — Self-Check Questions (the gate)

Before shipping any asset produced from this brief, the human reviewer (or AI in a separate self-review pass) answers:

1. **Spine fidelity**: Does this honor heart-encounter, daytime, sober, curated? Or does any line drift?
2. **Profile fit**: Would the targeted profile ({{ICP_PROFILE_1_NAME}}/{{ICP_PROFILE_2_NAME}}/{{ICP_PROFILE_3_NAME}}) recognize themselves? Or is this generic?
3. **Voice match**: Could {{FOUNDER_NAME}} say this to a friend over coffee? If no, rewrite.
4. **AI tells**: Any "Here's what/why/how" openings? Any "It's not X. It's Y." reveals? Em-dashes ≤2?
5. **Banned phrases**: Any wince-list words from the Language Map? (Manifest, sacred container, vibrational, conscious singles, sober-curious, etc.)
6. **Specificity**: Show > tell at sentence level? Concrete moments and details, not abstract benefits?
7. **Self-correction**: Are any drift signals firing on this asset? (See `05-ops/03-drift-signals.md`.)

Answer all 7 before the asset ships. If any answer is no, revise.

---

## Section 10 — Source Citations

Every brief cites:
- Which BOS docs informed it (foundation, voice, ICP, visual, ops)
- Which {{FOUNDER_NAME}} source docs (anchor / manifesto v2) the spine pulls from
- Any examples from prior assets that succeeded (post-Event #1, this becomes a richer reference layer)

This isn't bureaucracy — it's how amendments cascade. When {{FOUNDER_NAME}} names an amendment, the cited docs surface and the brief updates.

---

## Quality Gate (before saving any brief)

A creative brief is shippable only if:

- [ ] Section 1 spine reminder is verbatim from the canonical string
- [ ] Section 2 names the asset's job in one sentence
- [ ] Section 3 names the profile, audience state, and Bridge Message
- [ ] Section 4 voice paragraph is inherited (not rewritten)
- [ ] Section 5 format spec is hard, not soft
- [ ] Section 6 names 2-4 patterns with GOOD + BAD examples
- [ ] Section 7 visual spec cites DESIGN.md and photography-rules
- [ ] Section 8 AI prompt formula is paste-in ready (test it once before saving)
- [ ] Section 9 self-check questions are listed in order
- [ ] Section 10 citations are complete

If any item is missed, the brief is not finished.

---

## Notes for Brief Authors

### What this template is NOT
- Not a creative brief itself — it's the FRAME for briefs
- Not the only structure that works — but it's the one {{BRAND_NAME}} uses to keep coherence across 9+ asset types
- Not a static doc — it amends as we learn what's missing

### What it IS
- The skeleton that prevents brief-drift across asset types
- The paste-in source for AI sessions producing assets
- The single document a new author or AI reads to get up-to-speed on the brief structure

### When to deviate
- If the asset is novel and doesn't fit the structure, name why and propose an amendment
- If 2 sections collapse into 1 cleanly for a specific asset type, that's fine — note it
- If something's missing from the template that recurs across briefs, propose an amendment

The Constitution principle holds: amend, don't rewrite. And amend in writing, not in drift.

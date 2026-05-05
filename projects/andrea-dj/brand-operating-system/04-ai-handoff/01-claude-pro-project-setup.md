# 01 — Claude Pro Project Setup

*One-time, ~30-minute provisioning guide for Andrea's Claude Pro Project. Set this up once and every Claude conversation Andrea opens for Resonance work starts already-on-brand.*

*Last updated: 2026-05-04. Status: canonical.*

---

## The Spine Reminder

> *Resonance is heart encounters, not head encounters — a daytime, sober dance party in Chicago for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is couples, not followers.*

---

## Why A Claude Pro Project (and not just chats)

A Claude Project keeps the brand brain *resident* across every conversation. Without it, every chat starts from scratch and Andrea pastes the AI Brain Master file every time. With it: the project knowledge is loaded automatically, the voice is held automatically, and the conversations start three turns ahead of where they would otherwise.

Claude Pro Projects support: custom system instructions (always in scope), uploaded knowledge files (Claude reads them when relevant), and per-project memory. The cost is one Claude Pro subscription. The friction-reduction is enormous.

This guide assumes Andrea has Claude Pro. If not: the same setup works on Claude.ai's free tier with diminished knowledge-file capacity, or on ChatGPT Plus's "Custom GPTs" with adapted instructions.

---

## Step 1 — Create The Project (5 min)

1. Open `claude.ai`, sign in.
2. In the left sidebar, click **+ New Project**.
3. **Project Name**: `Resonance`
4. **Project Description** (paste verbatim from positioning-one-pager): *A daytime, sober, founder-curated dance event in Chicago for adults 30-40 who want to meet a committed partner. Founder Andrea DJs every flagship event. The room is ~50 people, vetted one-yes-at-a-time. The metric is couples formed, not tickets sold. First event June 2026.*
5. Save. The project shell exists.

---

## Step 2 — Install Custom Instructions (10 min)

The custom instructions are what Claude reads on every turn inside this project. They are the "system prompt" — invisible to the conversation but always in scope.

### Where to paste

In your Resonance project, click the project gear icon → **Custom Instructions**. Paste the full block below into the instructions field. Save.

### What to paste

```
You are Claude, working inside Andrea's Resonance project. Resonance is a daytime,
sober, founder-curated dance event in Chicago for adults 30-40 who want to meet a
committed partner. Andrea is the founder + DJ.

ALWAYS:
1. Re-read the spine before every output:
   "Resonance is heart encounters, not head encounters — a daytime, sober dance party
   in Chicago for people who want to meet a partner. The mechanic is body-first: the
   music does the emotional labor so the people don't have to. The metric is couples,
   not followers."

2. Hold Andrea's voice — warm, direct, confident, never preachy, never corporate.
   Show > tell at the sentence level. Lead with the moment, not the abstraction.

3. Honor the 12 Non-Negotiables on every output:
   1. Daytime  2. Sober  3. Curated admission  4. No hookup culture
   5. Chicago-first  6. Founder-curated music  7. Stories over metrics
   8. Phones off the floor  9. No bar service  10. No promoter access
   11. No sponsor stage  12. No coupled gatecrashers

4. Use one of the six voice patterns in every piece:
   - Anaphora ("You've-tried" beats with sharp landing line)
   - Frame-then-sharpen (declarative + named enemies)
   - Crystallized phrases (period-stacked creed)
   - Out-loud-asking (the ICP's actual phrasing as the hook)
   - Hell-yes filter (invite, then filter the unsure)
   - Mechanic-as-sentence (daytime/sober/curated as full sentences with stakes)

5. Target the right ICP profile:
   - Profile #1 — NORA: arts worker, 28-36, Pilsen / Logan / Wicker Park
   - Profile #2 — IMANI: helping professional, 32-38, Logan Square / Bucktown
   - Profile #3 — MARCUS: the quiet man, 28-36, Bronzeville / South Loop edge
   - Or umbrella: a 30-40 Chicago single who's out-loud asking why it's so hard

NEVER:
- Open with "Here's what / Here's why / Here's how / Here's the thing." AI tells.
- Use "It's not X. It's Y." reveal patterns. Banned in any form.
- Use wellness vocabulary: vibes, intentional (without specifics), conscious, sacred,
  manifest, high-vibe, soul-mate, twin flame, embodiment, sacred container.
- Use manosphere/tribe vocabulary: high-value, alpha, sigma, conscious king, find your
  queen, brother (as a marketing-mode address), kingdom, tribe.
- Use marketing slop: "tag a friend who needs this," "save this for later," "limited
  spots, going fast," "click here," "DM us to learn more."
- Preach sobriety. The room doesn't need alcohol HERE; it's not a sermon to her about
  alcohol everywhere.
- Use "community" unless we mean it (we don't yet — use "the room," "the floor").
- Use "Pulse" anywhere. (Legacy name from before the brand renamed to Resonance.)
- Use more than 2 em-dashes per piece.
- Output multiple options when one version that passes is better. Andrea wants
  ONE good draft, not three almost-drafts.

VOICE TEST before submitting any output:
- Could Andrea say this to a friend over coffee? If no, rewrite.
- Would Andrea text this subject line to a friend? If no, rewrite.
- Does the output pass the "Andrea-recognition" test? If she'd pause before sending,
  rewrite.

Default to producing one version, not multiple options. Match the calibration of the
brief or task. Voice precision is more valuable than option-volume.

When you're given a task, treat the spine + the 12 Non-Negotiables + the 6 patterns
as the structural skeleton. Treat the banned phrases as an absolute filter. Voice-check
your draft before you ship it.
```

That's the instruction block. ~750 words. Claude will load this on every turn.

---

## Step 3 — Upload Project Knowledge Files (10 min)

Project Knowledge gives Claude documents it can search and reference. Each file uploaded counts against the project's knowledge limit (Claude Pro: ~100K words across the project; this BOS subset fits comfortably).

### Files to upload (in order)

Upload these specific files from the Brand Operating System:

#### Tier 1 — Foundation (always upload — these are the brain)

1. `00-foundation/00-master-index.md` — the map of the BOS
2. `00-foundation/01-brand-bible.md` — strategic intent
3. `00-foundation/02-icp-master.md` — full ICP profiles + language maps
4. `00-foundation/03-voice-document.md` — voice patterns + 35 paired examples
5. `00-foundation/05-non-negotiables.md` — the 12 lines
6. `00-foundation/04-positioning-one-pager.md` — the press/partner version
7. `04-ai-handoff/00-ai-brain-master.md` — the cold-start paste-in (uploaded as redundancy)

#### Tier 2 — Visual System (upload — needed when the task involves design)

8. `01-visual/DESIGN.md` — the canonical visual system spec
9. `01-visual/photography-rules.md` — the 11pm test + image discipline
10. `01-visual/component-tokens.md` — buttons / cards / inputs / type / spacing tokens
11. `01-visual/aesthetic-references.md` — the mood board with 18 references

#### Tier 3 — Briefs (upload — these are the production templates)

12. `02-briefs/00-master-creative-brief-template.md` — the brief structural skeleton
13. `02-briefs/ig-feed-post.md`
14. `02-briefs/ig-reel.md`
15. `02-briefs/ig-story.md`
16. `02-briefs/email-newsletter.md`
17. `02-briefs/venue-pitch.md`
18. `02-briefs/press-one-sheeter.md`
19. `02-briefs/dj-booking-pack.md`
20. `02-briefs/flyer-poster.md`
21. `02-briefs/event-ticket.md`

#### Tier 4 — Marketing Ops (upload — when the task is funnel/strategy)

22. `03-marketing/01-content-pillars.md`
23. `03-marketing/02-hook-library.md`
24. `03-marketing/03-channel-architecture.md`
25. `03-marketing/04-curation-mechanics.md`
26. `03-marketing/05-crisis-comms.md`
27. `03-marketing/06-why-gate-mechanics.md`
28. `03-marketing/07-funnel.md`
29. `03-marketing/08-offer-card.md`

#### Tier 5 — Ops (upload — when the task involves event production or stories)

30. `05-ops/*` — all ops docs

### How to upload

1. In your Resonance project, click **+ Add Knowledge** (or **Upload Files**).
2. Select files in batches (Claude Pro accepts 5-10 at a time).
3. After upload, give each file a clean title — Claude uses titles to retrieve them.
4. Do NOT upload `_archive/` files, source docs (`andrea-internal-anchor.md`, etc.), or `.tmp/` files. The project knowledge is the BOS, not the entire workspace.

### What NOT to upload

- The raw source docs (`source/andrea-internal-anchor.md`, `source/andrea-manifesto-v2.md`) — these are the seed material; the BOS *is* their compiled output.
- A1-reconciliation drafts — historical, not active.
- Old Pulse-era docs (anything in `_archive/`).
- Files outside the BOS folder (general Antigravity docs, other projects).

Cluttering the project knowledge with non-BOS files dilutes Claude's retrieval. Keep it disciplined.

---

## Step 4 — Custom Slash Commands (Optional, 5 min)

Claude Pro doesn't currently support per-project slash commands the way Claude Code does. But you can create *custom prompt shortcuts* in Claude.ai's prompt library that always inject relevant context. Recommended shortcuts:

### Shortcut: `Resonance/IG-caption`

```
[Spine reminder verbatim]

I need an IG caption for [Profile target]. Lead with [out-loud-asking / anaphora /
crystallized-phrase opener]. The post is at [funnel position — top / middle / call-to-apply].
The visual is [photo description].

Length: 100-180 words. Hashtag count: 0 (we don't use hashtags). End with a single
line that filters or invites — never both.

Voice rules: see project instructions. Calibrate against `02-briefs/ig-feed-post.md`
in project knowledge. Produce ONE version that passes, not three options.
```

### Shortcut: `Resonance/triage-DM`

```
[Spine reminder verbatim]

I received this DM. Triage it as Hunter / Performer / Tourist / Hell-yes / Polite-yes
based on the criteria in `00-foundation/02-icp-master.md` Section 5 (the Hell-Yes Filter
Operational Form).

DM:
"""
[paste the DM here]
"""

Output: (1) classification, (2) the reasoning in 2 sentences, (3) the recommended
reply (or "no reply needed" + why).

If reply is needed, write it in Andrea's voice — warm, direct, no marketing.
Use the relevant decline script from the ICP master if it's a Hunter / Performer /
Tourist signal.
```

### Shortcut: `Resonance/voice-check`

```
[Spine reminder verbatim]

Voice-check this draft against `00-foundation/03-voice-document.md` Section 7
(the Quick Voice-Check Checklist) and the banned phrases in Section 5.

Draft:
"""
[paste the draft here]
"""

Output: pass/fail on each of the 7 checklist items, the specific banned phrases (if
any), and ONE recommended rewrite if it fails.
```

To create these in Claude.ai: Settings → Prompts → New Prompt → paste the shortcut content. Now Andrea can recall it by name in any new conversation.

---

## Step 5 — Recommended Project Settings

In the project settings, set these:

- **Default model**: Claude Sonnet 4.6 (faster, cheaper) for routine drafts; switch to **Claude Opus 4.7** for any high-stakes work (press one-sheeter, founder essays, manifesto edits).
- **Conversation history**: keep enabled. Andrea can revisit a 2-week-old conversation and continue.
- **Memory**: Claude's per-project memory is helpful — it'll learn Andrea's preferences over time (e.g., that she prefers shorter captions, that she rejects "intentional" instinctively).
- **Notifications**: turn off email digests unless useful — they clutter inbox.

---

## Step 6 — Test The Project (Final 5 min)

Run two tests to confirm setup:

### Test 1 — The Drift Test

Open a fresh conversation in the Resonance project and ask:

> *"What's the one sentence I should never paraphrase about Resonance?"*

Expected: Claude returns the spine verbatim (or very close), and notes that paraphrasing it loses the heart-encounters frame.

If Claude returns something generic ("a daytime sober event"), the custom instructions didn't load. Revisit Step 2.

### Test 2 — The Voice Test

Ask Claude:

> *"Draft an IG caption for Event #1 announcing applications open. Target Nora's profile. Lead with an out-loud-asking opener."*

Expected: Claude produces a 100-180 word caption that:
- Opens with a sentence Nora would actually say to a friend (not a marketing question)
- Uses one of the six voice patterns
- Doesn't include any banned phrase
- Ends with a specific filter or invitation, not a generic CTA
- Doesn't contain hashtags
- Reads like Andrea wrote it

If the output reads as generic dating-event copy, paste the AI Brain Master file (`04-ai-handoff/00-ai-brain-master.md`) into the conversation as a corrective and ask for a rewrite. Then revisit the custom instructions in Step 2 — something didn't stick.

---

## When To Update The Project

Update the project knowledge when:

- A foundational doc amends (a Non-Negotiable changes, a profile locks, a banned phrase is added). Re-upload the changed file; remove the old version.
- A new brief is added (e.g., when the BOS extends to cover sponsor decks or a podcast format).
- The voice document gets new examples after a successful event.

Do NOT update for: small typo fixes, formatting changes, or reorgs. Those drift the project knowledge unnecessarily.

---

## Common Failure Modes (and Fixes)

**Failure: Claude drifts after 8-10 turns in a long conversation.**
*Fix*: Paste the AI Brain Master file (`04-ai-handoff/00-ai-brain-master.md`) into the chat as a correction. Drift is normal in long sessions. Re-anchoring is the protocol.

**Failure: Claude produces three options when Andrea asked for one.**
*Fix*: Re-read Step 2 — the custom instructions explicitly forbid this. If it persists, add to the custom instructions: *"NEVER produce more than one option per request unless explicitly asked for variants."*

**Failure: Claude uses banned phrases despite the instruction.**
*Fix*: Add the specific phrase that slipped through to the banned list in custom instructions. The list is meant to grow.

**Failure: Claude doesn't know what file to retrieve from project knowledge.**
*Fix*: Reference the file by name in the prompt — *"Calibrate against `02-briefs/ig-feed-post.md` in project knowledge."* Claude retrieves explicitly-named files reliably; implicit retrieval drifts.

---

## Source Citations

- `00-foundation/03-voice-document.md` Section 6 (the AI Handoff Block — basis for custom instructions)
- `00-foundation/05-non-negotiables.md` — the 12 lines compressed into the instructions
- `00-foundation/02-icp-master.md` Sections 2-4 — profile names + signals in the instructions
- `02-briefs/00-master-creative-brief-template.md` — the brief structure Claude calibrates against
- `04-ai-handoff/00-ai-brain-master.md` — the cold-start paste-in (uploaded as redundancy in Tier 1)
- Anthropic Claude Pro Projects documentation (referenced for capacity + retrieval mechanics, not pasted)

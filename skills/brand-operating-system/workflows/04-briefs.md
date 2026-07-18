# Phase D — Creative Briefs

**Duration**: ~1 day. 9 briefs in parallel after master template lands.

## Required inputs

From Phase B:
- `00-foundation/01-brand-bible.md`, `02-icp-master.md`, `03-voice-document.md`, `05-non-negotiables.md`

From Phase C:
- `01-visual/DESIGN.md`, `01-visual/photography-rules.md`, `01-visual/component-tokens.md`

## Steps

### D1 — Master Creative Brief Template

Direct copy from template (already substituted by scaffold).

The template has 10 sections:
1. **Spine Reminder** (verbatim paste-in)
2. **What This Brief Is For** (purpose, asset, funnel position, single must-do)
3. **ICP Target** (profile + audience state + Bridge Message)
4. **Voice Rules** (compressed paragraph + 1-2 named patterns this asset leans on)
5. **Format Spec** (hard production constraints — dimensions, lengths, char limits)
6. **Hook & Structure Patterns** (2-4 named patterns with GOOD + BAD examples)
7. **Visual Spec** (hex codes, typography, photography rules — or "N/A — text only")
8. **AI Prompt Formula** (paste-in structure: spine + ICP + voice + format + visual + task + calibration)
9. **Self-Check Questions** (7-point gate before shipping)
10. **Source Citations** (which BOS docs informed this brief)

Output: `02-briefs/00-master-creative-brief-template.md`.

### D2-D10 — 9 per-asset briefs (PARALLEL)

Spawn 9 parallel `agents/master-copywriter/` invocations, one per asset type. Each consumes the master template + foundation + visual layers and produces a per-asset brief.

The 9 asset types:

| File | Asset | Voice patterns it leans on most | Format spec specifics |
|---|---|---|---|
| `ig-feed-post.md` | IG square post | Out-loud-asking opener, hell-yes filter | 1080×1080, ≤2200 chars caption, ≤30 hashtags |
| `ig-reel.md` | IG vertical video | Show-first opener, mechanic-as-sentence | 9:16, ≤90s ideal, hook in first 3s |
| `ig-story.md` | IG ephemeral | Anaphora cadence, frame-then-sharpen | 9:16, ≤15s per frame, polls/questions allowed |
| `email-newsletter.md` | Email broadcast | Out-loud-asking opener, story → moral arc | Subject ≤50 chars, preheader ≤100 chars, 400-1200 words body |
| `flyer-poster.md` | Print/digital flyer | Crystallized phrases, hierarchy | A4 + IG square versions, print-ready (300 DPI) + screen (72 DPI) |
| `event-ticket.md` | Per-attendee ticket | Crystallized phrases, sub-brand naming | Square or vertical, QR code, name field, date/venue |
| `venue-pitch.md` | B2B venue cold email/pitch | Frame-then-sharpen, mechanic-as-sentence | Email or PDF, ≤300 words email or 2-page PDF, attachment-ready |
| `press-one-sheeter.md` | Journalist asset | Frame-then-sharpen, crystallized phrases | 8-block structure, 1 page, photo-ready, fact-verified |
| `dj-booking-pack.md` | Guest DJ onboarding | Mechanic-as-sentence, hell-yes filter | PDF or shared doc, includes vibe brief + room mechanics + expectations |

**Save pattern for parallel execution**:
```python
# Spawn 9 master-copywriter agents in parallel
# Each returns content inline → main thread saves to <output>/02-briefs/<filename>
import asyncio
briefs = await asyncio.gather(
    spawn_master_copywriter(ig_feed_post_brief),
    spawn_master_copywriter(ig_reel_brief),
    # ... 7 more
)
for filename, content in zip(BRIEF_FILES, briefs):
    Path(output / "02-briefs" / filename).write_text(content)
```

Each brief follows the master template's 10 sections. Each Section 6 (Hook & Structure Patterns) MUST include 1 GOOD + 1 BAD example specific to the asset type — not generic patterns.

## Output Schema

**Inputs**: 
- `00-foundation/*` — All Foundation docs (voice, positioning, non-negotiables, ICP)
- `01-visual/*` — All Visual docs (DESIGN.md, photography rules, components)

**Outputs**:
- `02-briefs/00-master-creative-brief-template.md` — Locked parent brief (10 sections: Spine Reminder, Purpose, ICP Target, Voice Rules, Format Spec, Hook & Structure Patterns, Visual Spec, AI Prompt Formula, Self-Check Questions, Source Citations). All downstream per-asset briefs inherit this structure.
- `02-briefs/01-ig-feed-post.md` — Instagram square feed post brief (inherited sections 1-5 locked, sections 6-7 customized for IG feed: 1080×1080, ≤2200 chars caption, ≤30 hashtags)
- `02-briefs/02-ig-reel.md` — Instagram vertical video brief (inherited sections 1-5 locked, sections 6-7 customized for IG reel: 9:16, ≤90s, hook in first 3s)
- `02-briefs/03-ig-story.md` — Instagram ephemeral story brief (inherited sections 1-5 locked, sections 6-7 customized for IG story: 9:16, ≤15s per frame, polls/questions allowed)
- `02-briefs/04-email-newsletter.md` — Email broadcast brief (inherited sections 1-5 locked, sections 6-7 customized for email: subject ≤50 chars, preheader ≤100 chars, 400-1200 words body)
- `02-briefs/05-flyer-poster.md` — Print/digital flyer brief (inherited sections 1-5 locked, sections 6-7 customized for print: A4 + IG square versions, 300 DPI print + 72 DPI screen)
- `02-briefs/06-event-ticket.md` — Per-attendee event ticket brief (inherited sections 1-5 locked, sections 6-7 customized for tickets: square or vertical, QR code, name field, date/venue)
- `02-briefs/07-venue-pitch.md` — B2B venue cold pitch brief (inherited sections 1-5 locked, sections 6-7 customized for pitch: email or PDF, ≤300 words email or 2-page PDF)
- `02-briefs/08-press-one-sheeter.md` — Journalist press brief (inherited sections 1-5 locked, sections 6-7 customized for press: 8-block structure, 1 page, photo-ready, fact-verified)
- `02-briefs/09-dj-booking-pack.md` — Guest DJ onboarding brief (inherited sections 1-5 locked, sections 6-7 customized for booking: PDF or shared doc, vibe brief + room mechanics + expectations)

**Purpose**: Lock the creative briefing system. Inheritance pattern ensures Foundation voice and Visual standards cascade to every per-asset brief. Each brief's Section 8 (AI Prompt Formula) enables cold-paste generation into Claude: paste section 8 + request asset type → on-brand output without re-prompting.

**Quality Gate Checkpoint**: 
- [ ] Master template (D0) exists with all 10 sections locked
- [ ] All 9 per-asset briefs (D1-D9) exist and follow master's section structure
- [ ] Each brief's Section 8 (AI Prompt Formula) is genuinely paste-in ready (tested: paste into Claude cold → on-brand output without revision)
- [ ] Each brief's Section 6 has ≥1 GOOD + 1 BAD example specific to the asset type (not generic)
- [ ] Each brief's Format Spec (Section 5) has hard numeric constraints (dimensions, char limits, lengths)
- [ ] No brief paraphrases the spine (Section 1 must be verbatim from Foundation canonical)

If any unchecked, halt. Parallel briefs are easy to ship sloppy because no single human reviews all 9 carefully. Phase G1 adversarial review will catch this; better to catch it now.

---

## Quality gate (Phase D → E)

Before advancing to Phase E:
- [ ] Master template exists with all 10 sections
- [ ] All 9 per-asset briefs exist and follow the master's section order
- [ ] Each brief's Section 8 (AI Prompt Formula) is genuinely paste-in ready (test once: paste into Claude, ask for asset, output should be on-brand without re-prompting)
- [ ] Each brief's Section 6 has ≥1 GOOD + 1 BAD example specific to the asset type
- [ ] Each brief's Format Spec has hard numeric constraints (dimensions, char limits, lengths)
- [ ] No brief paraphrases the spine (Section 1 must be verbatim from canonical)

If any unchecked, halt. Parallel briefs are easy to ship sloppy because no single human reviews all 9 carefully. Phase G1 adversarial review will catch this; better to catch it now.

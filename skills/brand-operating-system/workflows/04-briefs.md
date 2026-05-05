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

## Quality gate (Phase D → E)

Before advancing to Phase E:
- [ ] Master template exists with all 10 sections
- [ ] All 9 per-asset briefs exist and follow the master's section order
- [ ] Each brief's Section 8 (AI Prompt Formula) is genuinely paste-in ready (test once: paste into Claude, ask for asset, output should be on-brand without re-prompting)
- [ ] Each brief's Section 6 has ≥1 GOOD + 1 BAD example specific to the asset type
- [ ] Each brief's Format Spec has hard numeric constraints (dimensions, char limits, lengths)
- [ ] No brief paraphrases the spine (Section 1 must be verbatim from canonical)

If any unchecked, halt. Parallel briefs are easy to ship sloppy because no single human reviews all 9 carefully. Phase G1 adversarial review will catch this; better to catch it now.

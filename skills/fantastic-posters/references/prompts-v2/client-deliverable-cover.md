---
name: "Fantastic Posters — Client Deliverable Cover Frame"
source_prompt: born-v2
skill: fantastic-posters
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are generating the cover frame for a client-facing written deliverable — a strategy brief,
council report, expert extraction package, or McKinsey-grade strategic dossier. The cover's job is
to signal the *category of thinking* inside the document, not to summarize its content or carry its
literal title. This is a premium, client-facing surface: default quality is `high`, never `medium` —
the quality gap is visible at print/screen.

## Input Required

- **[DELIVERABLE_THESIS]** — the central thesis in one line (the *idea*, not the title).
- **[AUDIENCE]** — who reads this (executives, founders, CMOs, technical CEOs, etc.).
- **[MOOD]** — urgent / authoritative / contemplative / provocative.
- **[VISUAL_ANCHOR]** — one concrete metaphor, object, or geometric form the image builds around.
- **[STYLE_OVERRIDE]** — a specific style id if already chosen, or AUTO (pick from the native-fit table).
- **[OUTPUT_DESTINATION]** — the deliverable folder the cover lands in (`strategy_briefs/[slug]/`, `councils/[slug]/`, `extractions/[slug]/`, `deliverables/[slug]/`).

## Execution Protocol

1. **Pick the style from the native-fit table** (or honor `[STYLE_OVERRIDE]`):

   | Style ID | When |
   |---|---|
   | `corporate-report` | McKinsey-grade strategic dossiers, business intelligence |
   | `swiss-minimal-typo` | Frameworks, methodology breakdowns, IP packaging |
   | `editorial-fashion` | Premium personality-led briefs (founder profiles, brand audits) |
   | `minimal-tech-keynote` | Tech council reports, AI brain build deliverables |
   | `tech-conf-darkmode` | Modern dark-themed briefs (memory architecture, agentic workflows) |
   | `saul-bass-minimal` | Iconic, mark-driven covers (manifesto-style deliverables) |
   | `art-deco` | Premium positioning briefs, luxury-brand work |

2. **Construct the brief.** It must contain all four: the thesis in one line, the audience, the mood, and one concrete visual anchor. A brief missing any of these produces a generic cover — do not proceed without all four.

   > Example shape: "Cover for strategic brief on [thesis]. Audience: [audience]. Mood: [mood].
   > Visual anchor: [concrete metaphor/object/form], [palette notes], no people."

3. **If the right style is unclear, explore cheap first** — a low-quality 3-variant pass ($0.033) before committing to the $0.17 high-quality final:
   ```bash
   python3 execution/fal_budget_guard.py check --quality=low --n=3
   ./gen.sh "<brief>" --n=3 --quality=low
   python3 execution/fal_budget_guard.py log --quality=low --n=3 --status=success
   ```
4. **Generate the final cover** (standard run, `high` quality, `portrait` size):
   ```bash
   python3 execution/fal_budget_guard.py check --quality=high --n=1
   cd "skills/fantastic-posters/" && ./gen.sh "<brief>" --style=<style-id> --quality=high --size=portrait
   python3 execution/fal_budget_guard.py log --quality=high --n=1 --status=success --style=<style-id>
   ```
5. **Never put the deliverable's literal title in the generation prompt** — GPT Image 2's typography is unreliable for this use; add the title in Canva post-generation instead.
6. **Never render recognizable real people** — likeness issues, and GPT Image 2 will distort faces.
7. **Deliver to the destination folder.** Cover lands in `skills/fantastic-posters/out/` first, then moves to `[OUTPUT_DESTINATION]/cover.png`. If the deliverable ships as a Google Doc, insert as the page-1 full-bleed image; if it ships as a PDF, use as the cover page.

## Output Contract

The style chosen (or override honored) + the four-part brief (thesis / audience / mood / visual
anchor); the exact gated command sequence (pre-flight → generate → log); the cost envelope stated
($0.17 standard, $0.20 with exploration); the final destination path.

## Output Skeleton

```markdown
**Style**: [style-id]
**Brief**:
- Thesis: [one line]
- Audience: [who]
- Mood: [urgent | authoritative | contemplative | provocative]
- Visual anchor: [concrete metaphor/object/form]
**Exploration pass?**: [yes → 3× low, $0.033 | no]
**Command**: `./gen.sh "[full brief]" --style=[id] --quality=high --size=portrait`
**Cost**: $[0.17 | 0.20]
**Destination**: [strategy_briefs|councils|extractions|deliverables]/[slug]/cover.png
```

## Quality Gate

- [ ] The brief carries all four required parts (thesis, audience, mood, visual anchor) — not just a style label.
- [ ] Quality is `high`, never `medium`, for the client-facing final.
- [ ] The deliverable's literal title is NOT in the generation prompt.
- [ ] No recognizable real person appears in the cover.
- [ ] The image signals the category of thinking, not a summary of the content — reject a generic stock-art result.
- [ ] Cost was pre-flighted and logged; total stays within the $0.17-$0.20 per-cover envelope.

## Creative Latitude

The visual anchor is where the craft lives — a strong anchor is a specific, concrete object or
geometric relationship that carries the thesis metaphorically ("layered translucent planes
intersecting at sharp angles" for a memory-architecture brief), not a mood-word collage. Push toward
an anchor a stranger could describe back after seeing the cover once; reject anything that reads as
generic corporate stock art or a literal illustration of the topic.

## Deploy When

A strategy brief, council report, expert extraction package, or strategic dossier needs a cover;
NOT for a poster's own market-facing use (route to Quick Poster Generation) and not when the
deliverable's audience is social/consumer rather than a document reader.

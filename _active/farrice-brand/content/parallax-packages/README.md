# Parallax Package System

One file per Edition. Top-to-bottom review. Copy-paste to Substack. Sync to Notion. Move on.

## What's in here

```
parallax-packages/
├── README.md           # this file
├── _template.md        # the reusable template (copy this for every new edition)
├── 01-manifesto.md     # Edition 01 — fully assembled
├── 02-[name].md        # next ones, as they're built
└── ...
```

## What a package contains (in scroll order)

1. **Header metadata** — edition #, status, publish date, source links
2. **Ship checklist** — gates that must be ✅ before publish
3. **Substack post block** — subject line, preview text, full body (edition + prompt pack), section assignment
4. **Notes batch** — 5 Notes scheduled across launch week with format labels and posting cadence
5. **Notion sync checklist** — what gets logged where, and when
6. **Voice + structural-tells audit notes** — quick gut-check before publish

## How to use this system

### When building a new edition

1. **Copy `_template.md`** to a new file: `0N-[slug].md` (e.g., `02-anti-hustle.md`)
2. Fill the header metadata at top
3. Pull the edition body from `_active/farrice-brand/content/substack-v2-drafts/0N-[slug].md`
4. Pull the prompt pack from `_active/farrice-brand/content/prompt-packs/0N-[slug].md`
5. Generate the Notes batch (or ask me — I'll draft 5 Notes that follow the high-conversion format mix from the 2026-04-24 Substack research)
6. Run the structural-tells audit (banned moves listed at the bottom of the template)
7. Walk the ship checklist — when all gates are ✅, publish

### When shipping

1. **Open the package file** in your editor
2. **Substack**: Copy the post block (subject → preview → body) into a new Substack post. Assign to `Editions` section. Schedule or publish.
3. **Notes**: Copy each Note block into Substack Notes scheduling. Use the "Schedule" timing noted next to each Note.
4. **Notion**: Walk the Notion sync checklist — log to Content Pipeline DB on schedule, log to Knowledge Vault DB after publish, log Performance DB after 48h.
5. **Mark the package's status** at the top: `draft → review → scheduled → published`.

## Why this format

- **One file** = one scroll, one review, no hopping between drafts and prompt packs and Notes scratch files
- **Inline content** = no copy-paste sourcing across 3 files at ship time
- **Substack blocks pre-formatted** = paste, don't compose
- **Notes scheduled with timing** = no improvising the launch week cadence
- **Notion sync inline** = the same package drives the database state

## Cadence reminders (from Substack 2026 research)

- **Notes ratio per week**: 10-5-1 (10 thoughtful comments on adjacent pubs, 5 original Notes, 1 promo Note)
- **Notes daily formula** (when ramping): 3-2-1 (3 value, 2 engagement, 1 soft promo)
- **Pre-edition rhythm**: Tease → drop announcement → quotable extract → engagement question → bridge to next
- **Notes drives 70-90% of new subs** for growing publications — these aren't optional

Source: [research_outputs/2026-04-24-substack-2026-growth-tactics-gemini.md](../../../../research_outputs/2026-04-24-substack-2026-growth-tactics-gemini.md)

## Conventions

- **File naming**: `0N-[slug].md` matches the existing draft naming in `substack-v2-drafts/` and `prompt-packs/`
- **Status values**: `draft` → `review` → `scheduled` → `published` → `archived`
- **Date format**: `YYYY-MM-DD` everywhere
- **Note timing**: Use `T-N` (days before drop) and `T+N` (days after drop) so the package works regardless of which day you publish

## When this system is wrong

If you find yourself fighting the structure for a specific edition (e.g., a multi-part edition, a special drop, a guest piece), don't force it — just adapt the template. The system serves the work, not the other way around.

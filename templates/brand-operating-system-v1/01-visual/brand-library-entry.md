# {{BRAND_NAME}} — Brand Library Entry

*Entry for `knowledge/design-libraries/brands/{{BRAND_NAME_LOWER}}/`. Format-matches the existing 59 entries in the brand library (Apple, Stripe, Linear, Aimé Leon Dore, etc.). Used by the design-md tooling, by future Creative Director sessions, and by any agent that needs {{BRAND_NAME}} context loaded as a Tier 1 reference.*

*Last updated: 2026-05-04. Source: `01-visual/DESIGN.md`. Authority: A1-reconciliation.md + Brand Bible.*

---

## Brand Identity

| Field | Value |
|---|---|
| **Brand name** | {{BRAND_NAME}} |
| **Founded** | 2026 (first event: June 2026) |
| **Founder** | {{FOUNDER_NAME}} ({{CITY}}-based DJ; full name + bio in founder docs) |
| **Location** | {{CITY}}, IL — {{CITY}}-first, no expansion until {{CITY}} model is undeniable (Anchor §3.10) |
| **Domain** | resonanceroom.com (placeholder; confirmed handle TBD per RISKS.md) |
| **Stage** | Pre-launch / Event #1 in production |

## Category & Positioning

**Category:** Live event / curated experience design. Sub-category: daytime sober dance event for partner-seeking adults.

**One-line positioning:** *{{SPINE_FRAME}} — a daytime, sober dance party in {{CITY}} for people who want to meet a partner.* (Manifesto v2 epigraph.)

**Paragraph positioning:** {{BRAND_NAME}} is a curated daytime dance room for 30-to-40-year-old single Chicagoans who want a committed partner and are tired of formats that make that harder, not easier. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is {{SUCCESS_METRIC}}. The brand's enemy is not a competitor — it is the culture of head-first, transactional, alcohol-mediated meeting that the ICP is already exhausted by.

**The wedge:** {{BRAND_NAME}} is the only daytime, sober, curated-music, curated-crowd dance event in {{CITY}} that explicitly measures itself by couples formed (25% target per event), not by attendance or followers. Every other daytime-dance brand in the category (Daybreaker, Morning Gloryville-era sober raves) is wellness-coded; every other singles-event brand is bar-coded. {{BRAND_NAME}} refuses both costumes.

## Voice Tags

`warm` · `direct` · `declarative` · `specific` · `recognition-not-pitch` · `body-first` · `chicago-rooted` · `never-preachy` · `never-corporate`

## Visual Tags

`daytime` · `golden-hour-actual-not-filtered` · `photo-led` · `editorial-broadsheet` · `1978-vinyl-jacket-serif` · `cream-canvas` · `terracotta-accent` · `midnight-blue-anchor` · `gold-rare` · `hand-script-only-for-human-moments` · `documentary-photography-only` · `no-AI-faces` · `no-club-lighting`

## Description (DESIGN.md `description` field)

> A daytime, sober dance party in {{CITY}} for people who want to meet a partner — rendered as an editorial broadsheet that has been left in actual sunlight. Warm terracotta and midnight blue, set on cream that breathes, with a 1978-record-jacket serif carrying the headlines and a clean humanist sans carrying the body. Photography is the protagonist; type is the caption. If a photo could have been taken at 11pm, it does not belong here.

## Color Tokens (paste from DESIGN.md)

```yaml
# Atomic shades — sourced from real {{CITY}} daylight, not stylized warm filters
terracotta-700: "#9A3A22"   # button-primary hover (WCAG-tuned)
terracotta-600: "#B8492E"   # primary CTA, accent
midnight-900:   "#0F1A2E"   # secondary, body anchor, badge
cream-50:       "#FBF7F0"   # surface (one step lighter)
cream-100:      "#F5EFE3"   # neutral (canvas)
ink-900:        "#1A1814"   # headlines, ink
ink-700:        "#3A332B"   # body text
slate-500:      "#7A6F62"   # muted — captions, metadata, photo credits
gold-600:       "#8C6526"   # tertiary — couples' names, story moments (WCAG-tuned)

# Semantic roles
primary:    "{colors.terracotta-600}"
secondary:  "{colors.midnight-900}"
tertiary:   "{colors.gold-600}"
neutral:    "{colors.cream-100}"
surface:    "{colors.cream-50}"
ink:        "{colors.ink-900}"
body:       "{colors.ink-700}"
muted:      "{colors.slate-500}"
on-primary:   "#FBF7F0"
on-secondary: "#FBF7F0"

# State
border-hairline: "#E1D6C2"
```

**Contrast story (WCAG — all verified by `npx @google/design.md lint`, 0 errors / 0 warnings):**
- `ink-900` (#1A1814) on `cream-100`: 14.2:1 (AAA)
- `ink-700` (#3A332B) on `cream-100`: 11.4:1 (AAA)
- `slate-500` (#7A6F62) on `cream-100`: 4.7:1 (AA — passes for normal text)
- `gold-600` (#8C6526) on `cream-100`: 4.7:1 (AA — used in pull-quote)
- `cream-50` on `terracotta-600` (button-primary): 4.6:1 (AA large — used at ≥ 18px or ≥ 14px bold)
- `cream-50` on `terracotta-700` (button-primary-hover): 6.0:1 (AA)
- `cream-50` on `midnight-900`: 14.8:1 (AAA)

## Typography Tokens (paste from DESIGN.md)

```yaml
# Display + headline — GT Sectra (1978 vinyl-jacket serif)
hero-display:    {family: GT Sectra,    size: 64px, weight: 500, lineHeight: 1.05, letterSpacing: -0.015em}
headline-lg:     {family: GT Sectra,    size: 44px, weight: 500, lineHeight: 1.1,  letterSpacing: -0.01em}
headline-md:     {family: GT Sectra,    size: 32px, weight: 500, lineHeight: 1.15, letterSpacing: -0.005em}
headline-sm:     {family: GT Sectra,    size: 24px, weight: 500, lineHeight: 1.2}

# Body + label — Inter
lead:            {family: Inter,        size: 20px, weight: 400, lineHeight: 1.55}
body-lg:         {family: Inter,        size: 18px, weight: 400, lineHeight: 1.6}
body-md:         {family: Inter,        size: 16px, weight: 400, lineHeight: 1.6}
body-sm:         {family: Inter,        size: 14px, weight: 400, lineHeight: 1.55}
label-caps:      {family: Inter,        size: 12px, weight: 600, lineHeight: 1.0,  letterSpacing: 0.12em}
caption:         {family: Inter,        size: 13px, weight: 400, lineHeight: 1.5}

# Hand-script — Caveat (rare punctuation only — {{FOUNDER_NAME}}'s signature, couples' quotes)
hand-script:     {family: Caveat,       size: 28px, weight: 500, lineHeight: 1.2}
```

**Substitution stack:**
- GT Sectra → Mortise → IBM Plex Serif → Georgia (web-safe fallback)
- Inter → Plus Jakarta Sans → system-ui (web-safe fallback)
- Caveat → Homemade Apple → cursive

## Spacing & Geometry Tokens

```yaml
spacing:
  xs: 4px, sm: 8px, md: 12px, base: 16px, lg: 24px, xl: 32px, 2xl: 48px, 3xl: 64px

rounded:
  none: 0px, sm: 2px, md: 4px, lg: 8px, full: 9999px

# Editorial sharpness — most surfaces use rounded.sm (2px) or rounded.md (4px)
# rounded.full only for round photo crops, never for buttons (pills read as consumer SaaS)
```

## Reference Links (BOS Spine)

| Document | Path | Purpose |
|---|---|---|
| **Source mechanic** | `_working/A1-reconciliation.md` §3 conflict #4, §6 cascade #1 | Daytime-as-mechanic ruling — the single rule the visual system is built on |
| **Strategic intent** | `00-foundation/01-brand-bible.md` §8 | Visual strategic intent (paragraph form); this brand-library entry executes it |
| **Brand foundation** | `00-foundation/01-brand-bible.md` (full) | Full brand foundation — manifesto, voice, ICP, lines |
| **Manifesto** | `source/andrea-manifesto-v2.md` | Canonical public-facing manifesto |
| **Founder anchor** | `source/andrea-internal-anchor.md` | Internal anchor — 12 Lines, drift signals, ICP, success target |
| **Executable spec** | `01-visual/DESIGN.md` | The full design tokens + 8 markdown sections |
| **Photography brief** | `01-visual/photography-rules.md` | Standalone photographer brief, AI-prompt rules |
| **Aesthetic mood** | `01-visual/aesthetic-references.md` | 28 references grouped by daytime, palette, typography, do-NOT |
| **Production components** | `01-visual/component-tokens.md` | IG, flyer, ticket, email, press, web specs |

## How to Use This Entry (for the design-md tooling)

When an AI session loads {{BRAND_NAME}} via `python3 execution/design_md_brand_lookup.py use {{BRAND_NAME_LOWER}}`, the system inherits:

1. **The full DESIGN.md** at `01-visual/DESIGN.md` — tokens + markdown rationale
2. **The photography rules** — non-negotiable gate on every image decision
3. **The aesthetic references** — positive mood board + kill list
4. **The component tokens** — production specs for repeating assets

For Creative Director chains, this entry is the Tier 1 brand context. Pair it with the Brand Bible §8 (strategic intent) and the Manifesto v2 (voice and phrases) to do any {{BRAND_NAME}} creative work.

## Quality Bar (the discipline this entry holds)

Every {{BRAND_NAME}} design decision must clear:

1. **The 11pm test.** *Could this image have been taken at 11pm in a club?* If yes, kill it.
2. **The wellness test.** *Does this look like an AI render of a wellness retreat?* If yes, kill it.
3. **The voice test.** *Could {{FOUNDER_NAME}} show this to a friend who lives the room and have them recognize it?* If no, kill it.
4. **The ecosystem test.** *Does this honor the heart-vs-head frame, with body-first as the mechanism underneath?* If the answer is unclear, return to A1-reconciliation.md §1 — The Unified Spine — and re-anchor.

## Cross-references

- A1-reconciliation.md §1, §3 conflict #4, §6 cascade #1
- Brand Bible §8 (Visual Direction)
- Manifesto v2 (full text)
- `01-visual/DESIGN.md` (executable spec)
- `01-visual/photography-rules.md` (photography brief)
- `01-visual/aesthetic-references.md` (mood board)
- `01-visual/component-tokens.md` (production components)
- `knowledge/design-libraries/brands/` (the corpus this entry joins)

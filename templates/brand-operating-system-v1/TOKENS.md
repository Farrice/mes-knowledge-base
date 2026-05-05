# Brand Operating System v1 — Token Manifest

This file enumerates every `{{TOKEN}}` used across the 43 template files and what each represents. The `bos_scaffold.py` script reads this manifest, prompts for or accepts a JSON file of values, and substitutes throughout the template tree before writing to the target project location.

**Two classes of tokens:**
1. **Identity tokens** — universal, single-value, auto-substituted. Things every brand has (name, founder, spine, city). Listed under "Required" and "Recommended" below.
2. **Content blocks** — multi-line structured placeholders that the user fills in *after* scaffolding (during Phase A-B of the build). These are NOT substituted by the scaffold script — they're guidance comments inside templates that get replaced by real content when the workflow runs.

---

## Required Identity Tokens (no scaffold without these)

| Token | Purpose | Example (Resonance) |
|---|---|---|
| `{{BRAND_NAME}}` | The brand's display name. Capitalized. Appears in titles, headers, body. | `Resonance` |
| `{{BRAND_NAME_LOWER}}` | Lowercase / slug-safe variant. Used for hashtags, handles, file paths. | `resonance` |
| `{{FOUNDER_NAME}}` | The founder's first name (or primary stakeholder name). | `Andrea` |
| `{{SPINE_LINE}}` | The single sentence that names the brand's core promise + how it delivers. Shows up at the top of every doc. ≤25 words. | `Heart encounters, not head encounters. A daytime, sober dance party in Chicago for people who want to meet a partner.` |
| `{{ONE_LINER}}` | Short pitch — what the brand IS in one breath. Often a subset of the spine. | `A daytime, sober dance party in Chicago for people who want to meet a partner.` |
| `{{SUCCESS_METRIC}}` | What success looks like in 4 words or less. The "we measure X, not Y" line. | `couples, not followers` |

## Recommended Identity Tokens (scaffold prompts but allows blank)

| Token | Purpose | Example (Resonance) |
|---|---|---|
| `{{FOUNDER_FULL_NAME}}` | Full name for press, contracts, formal references. | `Andrea [Last]` |
| `{{CITY}}` | Primary city / market. | `Chicago` |
| `{{REGION}}` | Broader region for context. | `Midwest` |
| `{{LAUNCH_DATE}}` | Public launch / first-event date. | `June 2026` |
| `{{EVENT_TYPE}}` | The product/format in one phrase. | `daytime, sober dance party` |
| `{{SPINE_FRAME}}` | The conceptual frame (the "X not Y" framing). | `Heart encounters, not head encounters` |
| `{{SPINE_MECHANISM}}` | The underlying mechanism (the "how"). | `body-first` |
| `{{KILL_CONDITION}}` | The condition that triggers a pivot or walk-away. Specific. | `12 events of sub-25% couple-formation` |
| `{{PATIENCE_WINDOW}}` | How many cycles before kill condition triggers. | `12 events` |
| `{{SUCCESS_RATE_TARGET}}` | Numeric target for the success metric. | `25% couple-formation rate` |

---

## Content Blocks (filled during Phase A-B, not at scaffold time)

These are NOT identity tokens — the scaffold script does not substitute them. They appear inside templates as structured guidance comments. The workflow replaces them with real content as Phase A-B outputs land.

| Block | Lives In | Filled During | Format Spec |
|---|---|---|---|
| `<!-- BLOCK: NON_NEGOTIABLES_LIST -->` | `00-foundation/05-non-negotiables.md`, `04-ai-handoff/00-ai-brain-master.md` | Phase A0 (port from canonical inputs) | Numbered list, each line: bold name + 1-3 sentence description |
| `<!-- BLOCK: ICP_UMBRELLA -->` | `00-foundation/02-icp-master.md` | Phase A2 | Single paragraph defining the broad audience |
| `<!-- BLOCK: ICP_PROFILE_1 / 2 / 3 -->` | `00-foundation/02-icp-master.md` | Phase A2 | Per-profile: name + status + demographic + psychographic + language map + bridge message |
| `<!-- BLOCK: VOICE_PATTERNS -->` | `00-foundation/03-voice-document.md`, `04-ai-handoff/00-ai-brain-master.md` | Phase B3 | 4-8 named patterns, each with definition + 2-4 GOOD/BAD examples |
| `<!-- BLOCK: ENEMY_LIST -->` | `00-foundation/01-brand-bible.md`, `04-ai-handoff/00-ai-brain-master.md` | Phase B1 | Sharpened "we are not X" lines naming the alternatives the brand explicitly refuses |
| `<!-- BLOCK: CRYSTALLIZED_PHRASES -->` | `00-foundation/01-brand-bible.md`, `04-ai-handoff/00-ai-brain-master.md` | Phase B1 | 5-10 verbatim-use phrases — the brand's signature language |
| `<!-- BLOCK: BANNED_PHRASES -->` | `00-foundation/03-voice-document.md` | Phase B3 | Wince-list — language the brand never uses, with 1-line reasoning |
| `<!-- BLOCK: COLOR_PALETTE -->` | `01-visual/DESIGN.md` | Phase C1 | Hex codes with role labels (primary / accent / surface / text / etc.) |
| `<!-- BLOCK: TYPOGRAPHY -->` | `01-visual/DESIGN.md` | Phase C1 | Font pairings + when each is used |
| `<!-- BLOCK: PHOTOGRAPHY_RULE -->` | `01-visual/photography-rules.md`, `01-visual/DESIGN.md` | Phase C3 | The single sentence that gates every image (e.g., "If a photo could have been taken at 11pm, it fails") |
| `<!-- BLOCK: DRIFT_SIGNALS -->` | `05-ops/03-drift-signals.md`, `04-ai-handoff/00-ai-brain-master.md` | Phase A0 (port from canonical inputs) | 5-12 named signals: each is a sentence describing an early warning of brand drift |
| `<!-- BLOCK: CONTENT_PILLARS -->` | `03-marketing/01-content-pillars.md` | Phase E1 | 5-7 pillars with proportions + posting frequency |
| `<!-- BLOCK: SUCCESS_DEFINITION -->` | `05-ops/04-success-metrics.md` | Phase A0 | What success looks like at: per-event / per-quarter / per-year / per-5-years horizons |
| `<!-- BLOCK: CANONICAL_SOURCE_REF -->` | All foundation docs | Phase A0 | Reference to the source document(s) that this doc derives from |

---

## Scaffold Behavior

**When `bos_scaffold.py` runs:**
1. Read `TOKENS.md` to load token catalog.
2. Read `tokens.json` (if `--tokens-file` supplied) OR prompt interactively for each Required + Recommended identity token.
3. Walk every `*.md` file under the template tree.
4. Replace `{{TOKEN}}` matches with the corresponding values.
5. Leave `<!-- BLOCK: ... -->` comments untouched — these are filled during the build workflow itself.
6. Copy file (with substitutions) to the target output path, preserving directory structure.
7. Skip `TOKENS.md` itself (don't copy this file to the target).

**Output expectation**: a target project directory mirroring the template structure, with identity tokens substituted and content-block guidance comments preserved for the build workflow to fill.

---

## Token Validation Rules

- **Brand name conflicts**: Scaffold halts if `{{BRAND_NAME}}` matches a known TM-conflicted name in `directives/trademark-watchlist.md` (if exists). Override with `--force`.
- **Spine line length**: Halts if `{{SPINE_LINE}}` exceeds 30 words. Force with `--force`.
- **Empty required token**: Halts with the list of unset required tokens.
- **Unrecognized token in template**: Logs warning at end of run listing any `{{X}}` that wasn't in the catalog (template drift indicator).

---

## Adding New Tokens

When future BOS instances reveal a new universal identity dimension (e.g., `{{INDUSTRY}}` or `{{PRICING_TIER}}`), add to this manifest first, then run a one-time backfill across the template tree. New tokens default to Recommended unless they break the scaffold without a value.

# Skill Description Rewrite — Follow-up Batch

> **Context**: 2026-05-22 audit found 21 of 234 skills (9%) had NO `description:` field in their SKILL.md frontmatter — completely invisible to Anthropic's skill-discovery layer (which matches user intent against the `description` field). The 2026-05-21 best-practices research synthesis identified description rewrites as the single highest-leverage discoverability lift available.
>
> **Status (2026-05-22, end of session): COMPLETE — 21 of 21 fixed.**
> - Commit `22130da1`: first 6 (luke-iha-cross-domain, nicolas-cole-niche-positioning, kallaway-addictive-storytelling, jason-fladlien-marketing, new-media-ghostwriting, seth-godin-brand).
> - This commit: remaining 15 (Batch 1: stefan-georgi-dopamine-copy, kallaway-ai-content-engine, kallaway-social-commerce, luke-iha-insight-vectors, evan-spiegel-distribution-architecture · Batch 2: new-media-kingmaker, chase-hughes-conversational-influence, corey-mcclain-persona-engineering, darrel-wilson-ai-affiliate, creative-campaign-strategy · Batch 3: cinematic-documentary, lamott-craft, story-compass, velocity-scaling, wright-thompson-mastery).
>
> Post-audit verification: 0 SKILL.md files missing the `description:` field (was 21).

## NEW Finding RESOLVED (2026-05-23)

The 11 YAML-parse files were repaired in commit `d1000857` (2026-05-22) — frontmatter now parses cleanly. **Description quality upgraded to Anthropic spec in commit `<TBD>` (2026-05-23)**. All 11 now satisfy the 5-rule spec: third-person verb opening, ≤1024 chars (max observed 1019), explicit "Use when…" trigger phrases, "Trigger proactively even when…" pushy claim, and anti-scope clauses where siblings exist (the nate-b-jones triplet, the context-engineering pair Lance/Nate, and the self-improvement pair Nate/self-evolving-systems all now carve clean trigger surfaces).

Post-rewrite verification: `Total: 234  Errors: 0  Missing-desc: 0`.

| File | Chars | Sibling anti-scope added |
|---|---:|---|
| `alex-content-science` | 731 | n/a |
| `alex-m-smith-natural-strategy` | 831 | n/a |
| `brand-operating-system` | 956 | vs design-md / voice-document / icp-deep-dive / creative-brief-gen |
| `fantastic-posters` | 997 | n/a |
| `lance-yichao-context-engineering` | 934 | vs nate-b-jones-context-engineering |
| `nate-b-jones-auto-improvement-loops` | 978 | vs nate-orchestration + nate-context + self-evolving |
| `nate-b-jones-context-engineering` | 936 | vs lance-yichao + nate-auto-improvement |
| `nate-b-jones-orchestration-intelligence` | 969 | vs nate-context + nate-auto-improvement |
| `ross-mckay-premium-at-scale` | 787 | n/a |
| `self-evolving-systems` | 1019 | vs nate-b-jones-auto-improvement-loops |
| `sharran-srivatsaa-scaling` | 980 | n/a |

## NEW Finding (original — pre-resolution, kept for historical reference)

11 SKILL.md files have **description text present** but **broken YAML** that `yaml.safe_load` cannot parse — meaning Anthropic's skill-discovery layer almost certainly cannot read them either. These files were NOT in the original 21-skill audit because the audit checked for missing `description:` lines, not for valid YAML.

Files affected (pre-existing — NOT caused by this batch):
- `skills/alex-content-science/SKILL.md` — unquoted name with spaces
- `skills/alex-m-smith-natural-strategy/SKILL.md` — unquoted colon mid-description
- `skills/brand-operating-system/SKILL.md` — unquoted colon mid-description
- `skills/fantastic-posters/SKILL.md` — unquoted colon mid-description
- `skills/lance-yichao-context-engineering/SKILL.md` — nested quotes in name
- `skills/nate-b-jones-auto-improvement-loops/SKILL.md` — unquoted name with em-dash
- `skills/nate-b-jones-context-engineering/SKILL.md` — nested quotes + em-dash
- `skills/nate-b-jones-orchestration-intelligence/SKILL.md` — unquoted name with em-dash
- `skills/ross-mckay-premium-at-scale/SKILL.md` — unquoted colon
- `skills/self-evolving-systems/SKILL.md` — unquoted colon
- `skills/sharran-srivatsaa-scaling/SKILL.md` — unquoted name with em-dash

**Fix pattern**: convert name to hyphenated-lowercase (no em-dashes, no spaces, no nested quotes), and either quote the entire description value or escape internal colons. This is a separate 30-60 minute batch and should be the immediate follow-up.

**Verification command**:
```bash
python3 -c "
import yaml; from pathlib import Path
for s in sorted(Path('skills').glob('*/SKILL.md')):
    t = s.read_text()
    if not t.startswith('---'): continue
    try: yaml.safe_load(t.split('---', 2)[1])
    except yaml.YAMLError as e: print(s, '->', str(e)[:120])
"
```

## What's Done (commit-ready)

| Skill | Description style |
|---|---|
| `luke-iha-cross-domain` | Third-person, "Use when..." triggers, pushy clause |
| `nicolas-cole-niche-positioning` | Same |
| `kallaway-addictive-storytelling` | Added full YAML frontmatter (had none) |
| `jason-fladlien-marketing` | Added full YAML frontmatter |
| `new-media-ghostwriting` | Added full YAML frontmatter |
| `seth-godin-brand` | Added full YAML frontmatter |

## What's Remaining (15 skills)

| # | Skill | Notes |
|---|---|---|
| 1 | `chase-hughes-conversational-influence` | Behavioral influence expert |
| 2 | `cinematic-documentary` | Visual storytelling skill |
| 3 | `corey-mcclain-persona-engineering` | Persona-engineering methodology |
| 4 | `creative-campaign-strategy` | General creative-campaign skill |
| 5 | `darrel-wilson-ai-affiliate` | AI affiliate-site building |
| 6 | `evan-spiegel-distribution-architecture` | Spiegel's distribution philosophy |
| 7 | `kallaway-ai-content-engine` | Kallaway's AI-content production system |
| 8 | `kallaway-social-commerce` | Kallaway's social-commerce mechanics |
| 9 | `lamott-craft` | Anne Lamott's writing-craft methodology |
| 10 | `luke-iha-insight-vectors` | Luke Iha's insight-vector framework |
| 11 | `new-media-kingmaker` | New-media kingmaker compound skill |
| 12 | `stefan-georgi-dopamine-copy` | Georgi's dopamine-copy framework |
| 13 | `story-compass` | Story-compass methodology |
| 14 | `velocity-scaling` | Velocity-scaling skill |

(Note: confirmed count 14 actionable; one in the original audit had only minor description gap.)

## The Anthropic-spec Pattern (verbatim — apply to each)

```yaml
---
name: <skill-name-hyphenated-lowercase>
description: <third-person verb, what it does in concrete terms>. <Specific use cases — "Use when X, Y, or Z"> Trigger proactively even when <a specific implicit signal that should auto-fire this skill without the user naming it>.
expert: <Expert Name>
domain: <One-line domain summary>
---
```

### Rules from Anthropic best-practices doc
- **Third-person**: "Engineers neurochemical retention..." (NOT "I engineer..." or "You can use this to...")
- **≤1024 chars** total description field. Front-load the most important use case — Claude Code truncates at 1,536 chars in skill listing.
- **Explicit trigger phrases**: "Use when..." block listing user-utterance patterns that should fire this skill.
- **Be pushy**: claim trigger phrases aggressively. "Trigger this proactively even when the user just X — the [skill-pattern] applies to [broader-class] than [narrow-explicit-mention]."
- **Anti-scope when useful**: for skills with a sibling that handles adjacent work, name what NOT to use this for. Example from `lara-acosta-linkedin-mastery`: "Do NOT use for general copywriting (use Luke Iha), short-form video (use Brock Johnson), or non-LinkedIn social platforms."

## Recommended Order for Next Session

Process in this order — highest discoverability lift first:

1. **`stefan-georgi-dopamine-copy`** — high-traffic copy expert
2. **`kallaway-ai-content-engine`** — sibling of the already-fixed Kallaway skill; should be findable from same trigger surface
3. **`kallaway-social-commerce`** — same Kallaway family
4. **`luke-iha-insight-vectors`** — Luke Iha family completeness
5. **`evan-spiegel-distribution-architecture`** — distribution doctrine, foundational
6. **`new-media-kingmaker`** — companion to new-media-ghostwriting (already fixed)
7. **`chase-hughes-conversational-influence`** — high-leverage influence expert
8. **`corey-mcclain-persona-engineering`** — persona engineering, valuable for client work
9. **`darrel-wilson-ai-affiliate`** — AI affiliate, growth surface
10. **`creative-campaign-strategy`** — foundation
11. **`cinematic-documentary`** — niche but valuable for content variety
12. **`lamott-craft`** — writing craft, evergreen
13. **`story-compass`** — story methodology
14. **`velocity-scaling`** — scaling work

## Verification (after each rewrite)

```bash
# Confirm description field present + non-empty:
grep "^description:" skills/<skill-name>/SKILL.md

# Confirm YAML frontmatter still parses:
python3 -c "import yaml; f=open('skills/<skill-name>/SKILL.md').read(); print(yaml.safe_load(f.split('---')[1]))"

# Audit overall progress:
for s in skills/*/SKILL.md; do grep -q "^description:" "$s" || echo "MISSING: $s"; done | wc -l
```

## Time Estimate

~5-8 minutes per skill (read body, draft Anthropic-spec description, edit, verify). 14 skills × ~6 min average = 80-100 minutes total. Best run as a single focused session.

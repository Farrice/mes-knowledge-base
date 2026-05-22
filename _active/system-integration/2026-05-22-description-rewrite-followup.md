# Skill Description Rewrite — Follow-up Batch

> **Context**: 2026-05-22 audit found 21 of 234 skills (9%) had NO `description:` field in their SKILL.md frontmatter — completely invisible to Anthropic's skill-discovery layer (which matches user intent against the `description` field). The 2026-05-21 best-practices research synthesis identified description rewrites as the single highest-leverage discoverability lift available.
>
> **Done this session (2026-05-22)**: 6 of 21 fixed.
> **Remaining**: 15.

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

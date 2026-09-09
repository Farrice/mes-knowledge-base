---
description: Read six months of an agent's own posts, isolate the outliers, name the attribute that made them work, and hand back a double-down hypothesis with a data window — the first move for any stuck account
---

# /alyssa-stalker-outlier-audit — "It's Just Data"

The first move Alyssa Stalker makes with a stuck agent: "take a deep breath... it's just data" [01:58–02:04]. Then look for the post that broke the flatline and name why. Eric Simon's AI line pulled ~800 comments and reshaped his whole mix to 70% opinionated talking head [03:43–04:20]; Alyssa's repeatable carousels outperformed everything for 18 months and grew her account 50% in a year [16:25–17:12]. Neither started from a template.

## Pre-Flight Gate

Load `skills/alyssa-stalker-agent-content-playbook/genius.md` Patterns 1, 5, 11 and the heuristics. Confirm you have the agent's actual posts (metrics export, screenshots, or at minimum a list with rough performance). **If no performance data exists, stop and ask for it.** Never invent an outlier. If the agent has fewer than ~20 posts in the window, say so and shorten the audit to what exists.

## Skill Acquisition

- `genius.md` — Pattern 1 (outlier audit), Pattern 5 (specificity is distribution), Pattern 11 (goal tags, so authority posts aren't misread as flops)
- For Jen: `_active/clients/jen-listings/CLAUDE.md` register ladder, so a luxury-listing outlier isn't mistaken for a FTHB signal

## Diagnose Before Treat

Establish the flatline first. Median views, likes, saves, shares, comments, follows across the window. An "outlier" is only an outlier relative to this agent's own baseline — a 900-view post is a signal on a 300-view account and noise on a 30,000-view one.

## Execution

1. **Baseline** — compute or estimate the median per metric. Note the posting cadence and format mix (reels / carousels / single image / text post / stories).
2. **Isolate outliers** — any post ≥2× baseline on any metric that matters for the agent's goal (follows and shares for growth; saves and DMs for conversion). Rank by the goal metric, not by likes alone.
3. **Tag each outlier's goal** — local / listing / authority (Pattern 11). An authority post with high saves and low likes is doing its job; do not flag it as a failure.
4. **Diagnose the attribute** — for each outlier, name what changed: topic, format, hook framing (did it carry a who-clause? a lens?), audience addressed, opinion strength, timing, personal-lens signal. Quote the hook.
5. **Cross-check the flatline** — what do the flatline posts share that the outliers lack? Usually: no specific person, no take, broad hook.
6. **Write the hypothesis** — one sentence: "This account moves when [attribute] because [audience response]." Eric's: "opinionated talking-head takes on industry talking points."
7. **Design the 30-day test** — the next 8–12 posts built on the attribute, one variable changed at a time (Kallaway's 4-of-5 rule may load here). Declare the data window and the pivot/double-down rule: "narrow down something to try, get data, try it for a while, learn from it, and either pivot... or double down" [35:52–36:03].
8. **Name the bit** — if an outlier line can recur (Eric's AI line became a running joke in his comments [04:03–04:08]), flag it as a candidate recurring bit.

## Content Type Adaptations

| Agent situation | Adaptation |
|---|---|
| Reels-only account | Outliers are usually hook framing; test the same hook on a carousel and a single image |
| Carousel-heavy account | Outliers are usually the first-slide feeling; test the feeling on a create-mode text post |
| Listing-heavy grid | Expect low outlier count; the hypothesis often becomes "add local + comfort content" |
| Mixed with stories | Stories metrics are separate; use replies and DMs as the story signal |
| Luxury + FTHB (Jen) | Split the audit by register; never merge a $2M listing outlier into the FTHB hypothesis |

## Output Schema

```markdown
# OUTLIER AUDIT — [agent] — [window]

## Baseline
| Metric | Median | Cadence | Format mix |

## Outliers (ranked by goal metric)
| # | Date | Format | Hook (verbatim) | Goal tag | Metric vs baseline | Attribute |

## Flatline pattern
[what the non-performers share]

## Hypothesis
"This account moves when [attribute] because [audience response]."

## 30-Day Test
- Posts 1–N: [attribute held constant, one variable changed]
- Data window: [dates]
- Pivot / double-down rule: [threshold]

## Candidate recurring bit
[line or angle, or "none"]

## Handoff → 02-one-person-niche / 03-hook-reframe
- Source evidence: [rows used]
- Output produced: Outlier Audit Card
- Next input: the attribute + the audience it spoke to
- Validation: baseline computed from real data [yes/no]
- Open risk: [sample size, missing metrics]
```

Execution prompt: `references/prompts-v2/outlier-audit.md` — honor its Output Contract.

## Quality Gate

- Is the baseline computed from the agent's real numbers, not assumed?
- Is every outlier's attribute named specifically (quoted hook, who, lens), not "it resonated"?
- Is each outlier goal-tagged so authority posts aren't misread?
- Is the hypothesis one sentence and testable inside 30 days?
- Is exactly one experiment declared, with a data window and a pivot rule?
- Anti-pattern check: no template prescribed before the data was read.

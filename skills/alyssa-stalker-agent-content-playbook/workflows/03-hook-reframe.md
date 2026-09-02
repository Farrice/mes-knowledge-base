---
description: Rewrite any broad local or educational hook as Topic + Who + Lens so the post lands in front of the one person it's for — the cheapest fix in the 2026 playbook
---

# /alyssa-stalker-hook-reframe — Topic + Who + Lens

The host called this "the clip right there" [13:49–13:51]. Agents post a beautiful B-roll or a Coffee & Contracts template "but they haven't adjusted the hook so that it actually creates that right framing" [11:42–11:47]. The fix: "three things to do this weekend in city name" → "...that you've probably never heard of, especially if you're a mom of two" [12:12–12:27]. Specificity is reach: Instagram tests by interest for a day after one search, so "you don't have to fight for those views as hard" [12:35–13:05].

## Pre-Flight Gate

Load `genius.md` Patterns 4, 5, 8 and `references/hook-reframe-bank.md`. Input required: the broad hook or topic, and the person (from `02-one-person-niche`, an ICP brief, or the agent's one-line description). If no person exists, produce reframes for two candidate persons and mark the card DRAFT.

## Skill Acquisition

- `genius.md` — Patterns 4, 5, 8; anti-patterns 2, 3, 5
- `references/hook-reframe-bank.md` — mechanisms and fair-housing filter
- For Jen: `_active/clients/jen-listings/CLAUDE.md` register ladder (FTHB = calm-warm lowercase; luxury = Quiet Flex Elite Advisor) and `skills/jen-santulan-listing-content/genius.md` §4 sentence patterns

## Diagnose Before Treat

Name what the broad hook is missing. Three failure shapes: (a) no who ("3 things to do in Spokane"), (b) who but no lens ("...if you're a mom" — targeted but flat), (c) lens but no who (an opinion aimed at nobody). Fix the missing part first; do not rewrite the topic.

## Execution

1. **Hold the topic** — the topic is rarely the problem. Local content "always performs" [11:02–11:04].
2. **Append the who** — one clause, one person, from the card. Housing-safe when the post touches housing.
3. **Add the lens** — the agent's take, insider framing, or a private-state acknowledgement: "that you've probably never heard of," "the one everyone recommends that I'd skip," "if you're quietly running the numbers at midnight."
4. **Generate 5–7 reframes** across mechanisms: life stage, timing, private state, habit/place, insider lens, contrarian lens. Tag each.
5. **Add one comfort variant** — the feeling-first version (Pattern 8), offer withheld.
6. **Run the AI rule** — if AI is used, it reframes an existing hook "for your audience, for your ideal client, from your point of view" [36:21–36:33]; it does not write the post.
7. **Pick and say why** — one RECOMMENDED, with the distribution rationale in one line and the expected reader reaction ("that's me, I'll keep swiping" [20:28–20:32]).
8. **Voice check** — would the agent say this out loud? For Jen, the coffee-table test.

## Content Type Adaptations

| Format | Where the reframe lives |
|---|---|
| Reel (B-roll) | On-screen text hook, first 1–2 seconds; caption repeats the who |
| Carousel | Slide 1, ≤12 words; the lens can spill to slide 2 |
| Single image | The whole post; caption carries the lens |
| Create-mode text post | The hook IS the post — compress to one sentence |
| Story | Who-clause as the first line of the sticker text |
| Caption-only (broad video kept) | Katie Day route: keep the video broad, put the opinion in the caption [38:19–38:23] |

## Output Schema

```markdown
# HOOK REFRAME SET — [agent] — [topic]

## Diagnosis
- Broad hook: "[verbatim]"
- Missing: [who / lens / both]
- Person: [one line from the card]

## Reframes
| # | Reframe | Who | Lens | Mechanism | Format fit |
| 1 | … | … | … | life stage | carousel slide 1 |
…
| C | [comfort variant — feeling first, offer withheld] | … | … | private state | carousel |

## Recommended
"[reframe]" — because [distribution rationale, one line]. Expected reaction: "[that's me…]".

## Voice check
[agent would say it: yes / rewrite needed] · Fair-housing: [clear / adjusted]

## Handoff → jen-engine Stage 3 / 04-comfort-content-engine
- Output produced: Hook Reframe Set
- Next input: the recommended hook + format fit
- Validation: who + lens present in every row [yes/no]
- Open risk: [person unconfirmed / register]
```

Execution prompt: `references/prompts-v2/hook-reframe-set.md` — honor its Output Contract.

## Quality Gate

- Does every reframe carry a who-clause AND a lens?
- Is the topic preserved, not swapped?
- Would the named person stop scrolling because the hook describes them?
- Is the comfort variant feeling-first with the offer withheld?
- Is the fair-housing frame clear on anything housing-related?
- Anti-pattern check: no FOMO, no rent-shaming, no "before it's too late."

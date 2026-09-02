---
description: Build feeling-first comfort carousels that make one person feel seen and land the agent's offer last as permission — connection content, not transactional content
---

# /alyssa-stalker-comfort-content-engine — Comfort Creator

"Nobody comes to my account for tips anymore... they follow along my content because they actually feel seen" [16:35–16:43]. The consumer version: "Self-care as someone in their mid-30s who's yet to buy a house... in the end you're offering them a solution by saying, 'Don't worry, you're not behind.' Lots of people are like that and guess what? That's exactly who I help" [20:10–20:51]. It beats "FOMO or rent shaming or 'you have to do this now before school starts'" [20:52–20:59].

## Pre-Flight Gate

Load `genius.md` Patterns 7, 8, 10 and `references/comfort-content-exemplars.md`. Required: the person and their private feeling (from `02-one-person-niche` or a verbatim pain script). If the feeling is generic ("stressed about buying"), stop and sharpen it; comfort content built on a generic feeling is a tip in a costume.

## Skill Acquisition

- `genius.md` — Patterns 7, 8, 10; anti-patterns 3, 5
- `references/comfort-content-exemplars.md` — the three hooks, the flip structure, the share test
- For Jen: `skills/jen-santulan-listing-content/genius.md` §3 "Midnight on Zillow" (verbatim pain script: "I'll never own in LA at this rate," "we make good money but still can't afford. It's humiliating") and `_active/clients/jen-listings/CLAUDE.md` (calm-warm lowercase for FTHB; emojis are voice; no urgency)
- `jen-engine` Stage 4 carousel spec (5–7 slides, 1080×1350, ≤12-word hook slide, one idea per slide) when the output goes to production

## Diagnose Before Treat

Identify which of three states the person is in: **over-lectured** (they've heard every tip), **ashamed** (they think they're behind), or **exhausted** (they've stopped looking). The hook names the state; the middle answers it; the payoff gives permission. Pick one state per carousel.

## Execution

1. **Hook slide — name the private state** in the person's own words, no offer, no stat. Shape options from source: "Self-care as [person who hasn't done X yet]"; "People only post their wins. Here are my [flops/false starts]"; "It's crazy what [small thing] can do for [private need]."
2. **Slide 2 — recognition** — the "that's me, I'll keep swiping" beat [20:28–20:32]. One specific detail from the scene (the midnight scroll, the closed tab, the rent number).
3. **Slides 3–5 — cheeky, then supportive** — "something funny at first, something cheeky, something supportive" [20:35–20:38]. Small mindset or process moves they can actually do; no acronyms, no five statistics.
4. **Payoff slide — permission as offer** — "you're not behind. [Lots of people are here.] That's exactly who I help" [20:43–20:51]. The agent's offer appears only here, as the natural end of recognition.
5. **CTA** — low pressure, one routing question or keyword reply. Never "act now."
6. **Share test** — would this person send it to their partner with "this is us"? Would an agent reshare it to look good to clients? [23:36–23:46]. If neither, rebuild slide 1.
7. **Lo-fi spec** — camera-roll photo or plain background, basic type, one message per slide [05:44–05:51], [37:14–37:18]. No motion graphics.
8. **Voice check** — the agent's register. For Jen FTHB: calm-warm lowercase, "you CAN do this" never "you SHOULD" (Jen genius Pillar C).
9. **Produce three** — three carousels, three states or three angles on one state, so the agent can A/B [10:37–10:41].

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| Carousel (default) | 5–7 slides as above |
| Single image + caption | Hook slide as image; slides 2–payoff compressed into the caption |
| Create-mode text post | Hook + payoff fused into one sentence → hand to `05-create-mode-text-post` |
| Reel (talking head) | Hook spoken in first 2 seconds; payoff is the last line; 20–30 seconds [25:46–25:49] |
| Agent-to-agent (Alyssa's own use) | Same structure; payoff is solidarity, not an offer |

## Output Schema

```markdown
# COMFORT CAROUSEL PACK — [agent] — [person]

## Person + state
- Person: [one line]
- Private feeling (verbatim or near): "…"
- State addressed: over-lectured / ashamed / exhausted

## Carousel 1 — [working title]
| Slide | Text (≤25 words; slide 1 ≤12) | Beat |
| 1 | … | private state |
| 2 | … | recognition |
| 3 | … | cheeky |
| 4 | … | supportive |
| 5 | … | supportive |
| 6 | … | permission as offer |
| 7 | … | CTA (low pressure) |
- Caption:
- Visual spec (lo-fi):
- Share test: [partner-send / agent-reshare: yes/no + why]
- Anti-FOMO check: [clear]

## Carousel 2 — …
## Carousel 3 — …

## Handoff → jen-engine Stage 4 / SEND package
- Output produced: Comfort Carousel Pack
- Next input: approved carousel(s) + caption
- Validation: feeling-first + offer-last in all three [yes/no]; voice check [pass]
- Open risk: [feeling unverified against real ICP language]
```

Execution prompt: `references/prompts-v2/comfort-carousel-pack.md` — honor its Output Contract.

## Quality Gate

- Does slide 1 name a private feeling with zero offer and zero stat?
- Does the offer appear only on the payoff slide, phrased as permission?
- Would the person send this to someone with "this is us"?
- Is it producible from a camera roll and basic type?
- Does it pass the agent's voice test and the fair-housing filter?
- Anti-pattern check: no FOMO, rent-shaming, deadlines, or "five things you need to know."

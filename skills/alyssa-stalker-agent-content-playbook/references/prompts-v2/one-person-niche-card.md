---
name: "Alyssa Stalker — One-Person Niche Card"
source_prompt: born-v2
skill: alyssa-stalker-agent-content-playbook
standard: structure-pure-v2
forged: born-v2
refactored: 2026-09-02
fidelity: medium
---

## Role & Activation

You are running Alyssa Stalker's niche move. She rejects "upsizer or downsizer" as too broad and asks where the person eats, where they hang out, whether Friday is pickleball and a social club or "couch rot on the weekend and have a beautiful living room all to themselves." The rule: "you have to start with one person to get to that point" where people call because they like you. You also run her flipped question — not what does the audience want to see, but "what does the audience need to know about me in order to like me, trust me, and then work with me" — and her one-slide test: if the whole message had to fit one single image post and a caption, who is it for?

## Input Required

```text
[AGENT: name, market]
[AGENT'S OWN WORDS: who I am / what I represent / who I immediately connect with / what I want people to know about me]
[EXISTING ICP MATERIAL, optional: brief, pain script, strategy doc path]
[HOUSING CONTEXT: will this content touch housing? yes/no]
```

If AGENT'S OWN WORDS is empty, produce a five-question interview (one question per turn) and stop. Never invent the agent's interests or convictions.

## Execution Protocol

1. **Personal brand first** — capture the agent's answers verbatim.
2. **Pick one person** — from the "immediately connect with" answer; the one the agent lights up about, not the largest segment.
3. **Write the scene** — life stage; weekday evening, Friday night, Sunday morning; where they eat, hang out, scroll; what they've stopped saying out loud. Alyssa's prompts: early parenting, dog parents, relocating professionals.
4. **Housing-safe frame** — if content touches housing, frame the person by life situation, habit, or feeling; never protected class. State the frame explicitly.
5. **Private feeling** — one sentence they'd never post but would recognize instantly.
6. **Personal-lens inventory** — 5–8 real signals from the agent (Eric's: Star Wars, USC, baseball cards, the book he wrote, Yankees, the new baby, a bet at the end of broadcast posts).
7. **One-slide test** — the whole message as one image text + caption, ≤40 words. If it won't fit, the person is too broad; narrow and retry.
8. **Five seed topics** — each already carrying who + lens.

## Output Contract

Markdown card, 200–400 words. Sections: Agent in their words; The person (scene, housing-safe frame); Private feeling; Personal-lens inventory; One-slide test; Five seed topics; Handoff block. Person written as a scene, not a segment. Card marked DRAFT until the agent confirms "that's them."

## Output Skeleton

```markdown
# ONE-PERSON NICHE CARD — [agent] — [DRAFT / CONFIRMED]

## Agent, in their words
- Who I am / what I represent:
- Who I immediately connect with:

## The person
- Life stage:
- Weekday evening / Friday night / Sunday morning:
- Where they eat, hang out, scroll:
- What they've stopped saying out loud:
- Housing-safe frame:

## Private feeling
"…"

## Personal-lens inventory
1. …

## One-slide test
[image text] / [caption] (≤40 words total)

## Five seed topics (topic + who + lens)
1. …

## Handoff → 03-hook-reframe / 04-comfort-content-engine
- Output produced: One-Person Niche Card
- Next input: [person line + private feeling]
- Validation: agent confirmed [yes/no]
- Open risk: [unverified interests / stale brief]
```

## Quality Gate

- Can you picture this person at one table on one night?
- Personal-lens signals are agent-supplied, not generated?
- One-slide test fits ≤40 words?
- Housing-safe frame stated?
- No "upsizer/downsizer," "buyers and sellers," or "everyone"?

## Creative Latitude

The scene is where this card earns its keep. Choose the one detail that makes the agent say "yes, her" — the specific coffee order, the tab they close at midnight, the group chat they're in. The five seed topics should surprise: at least one should come from the personal-lens inventory, not from real estate.

## Deploy When

- The agent says "I'll work with anybody."
- An ICP brief exists but every hook still reads generic.
- Before `/alyssa-stalker-hook-reframe` or `/alyssa-stalker-comfort-content-engine` when no person card exists.

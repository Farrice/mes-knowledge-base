---
name: "Alyssa Stalker — Create-Mode Text Post Set"
source_prompt: born-v2
skill: alyssa-stalker-agent-content-playbook
standard: structure-pure-v2
forged: born-v2
refactored: 2026-09-02
fidelity: medium
---

## Role & Activation

You are producing the zero-production format The Broke Agent pulled up on air: Ricky Carruth's all-black create-mode text posts — "If your real estate agent is still answering the phone at 9:00 p.m. on Saturday, you don't have an agent. You have someone who cares about your family's future" (~11,000 likes); "Real estate agents wake up knowing they have zero guaranteed income, but they show up anyway. That's called courage" (~12,000 likes). Alyssa Stalker's read on why they work: they're written for agents through the agent's lens, so agents reshare them "so that their potential clients see it and it would make them look good." Production rule: "tweet it out, screenshot it, and then post it." One true sentence. No design.

## Input Required

```text
[AGENT: name, voice notes or verbatim lines]
[AUDIENCE: agent-to-agent / consumer / both]
[CONVICTIONS: 2–5 things the agent actually believes, in their words]
[PERSON, if consumer: one line]
```

If CONVICTIONS is empty, stop. This format is an opinion or a recognition; it cannot be generated from nothing.

## Execution Protocol

1. **Name the resharer** and what resharing says about them ("I work this hard"; "we're not crazy for waiting"; "this is what my agent is like").
2. **Find the true sentence** — from the agent's words, a client's words, or a lived moment. Structures in source: contrast ("you don't have an agent. You have someone who…"), redefinition ("that's called courage"), trait reframe ("confidence isn't arrogance. It's…").
3. **Compress** — ≤25 words, one message. Cut qualifiers.
4. **Write 5–7 lines** — vary structure; at least two per audience when AUDIENCE is both.
5. **Reshare test per line** — who reshares and what it makes them look like. Kill lines that only inform.
6. **Production note** — create mode, all-black, default type; or tweet → screenshot → post.
7. **Voice check** — the agent would say it aloud; rough beats smooth.

## Output Contract

Markdown set, 150–300 words. Sections: Resharer; Lines table (5–7 rows: line, structure, audience, reshare test); Production; Voice check; Handoff block. Every line ≤25 words. No tips, no stats, no award or listing announcements.

## Output Skeleton

```markdown
# CREATE-MODE TEXT POST SET — [agent]

## Resharer
- Who reshares:
- What the reshare says about them: "…"

## Lines
| # | Line (≤25 words) | Structure | Audience | Reshare test |
| 1 | … | contrast | consumer | … |

## Production
Create mode · all-black · default type · no design

## Voice check
[yes / lines flagged]

## Handoff → posting queue / 07-content-mix-planner
- Output produced: Create-Mode Text Post Set
- Next input: [approved lines + slot]
- Validation: every line passes reshare test [yes/no]
- Open risk: [conviction unverified]
```

## Quality Gate

- Every line one message, ≤25 words?
- Each line names a resharer and what resharing says about them?
- Opinion or recognition, not tip or stat?
- Producible in create mode with zero design?
- The agent would say it out loud?
- No AI-generated voice, no "look at me" line?

## Creative Latitude

The best lines in this format redefine a thing the reader is quietly ashamed of — the 9 p.m. call, the no-guaranteed-income morning, the mid-30s rental — as evidence of something they'd be proud of. Look for that inversion. Let one line be plain and one be almost too blunt; the set should feel like a person with opinions, not a quote generator. Rhythm matters: a short second sentence after a long first one is the source's signature cadence.

## Deploy When

- One true sentence exists and no production time does.
- A comfort carousel's slide 1 wants to stand alone.
- Filling a local or authority slot in under five minutes.

---
name: "Alyssa Stalker — Hook Reframe Set"
source_prompt: born-v2
skill: alyssa-stalker-agent-content-playbook
standard: structure-pure-v2
forged: born-v2
refactored: 2026-09-02
fidelity: high
---

## Role & Activation

You are running the move The Broke Agent called "the clip right there." Alyssa Stalker's fix for agents whose templates look great but go nowhere: adjust the hook so it frames who the post is for. "Three things to do this weekend in city name" is broad. "Three things to do this weekend in city name that you've probably never heard of, especially if you're a mom of two" adds the who and the lens. Her rationale: Instagram tests content by interest for roughly a day after one search, so "the more specific you are, the more likely now you are to land in front of the right people. You don't have to fight for those views as hard." You hold the topic, append the who, add the lens.

## Input Required

```text
[AGENT: name, market, register notes]
[BROAD HOOK OR TOPIC: verbatim]
[PERSON: one line from the One-Person Niche Card, or candidate persons]
[FORMAT: reel / carousel / single image / text post / story / caption-only]
[HOUSING CONTEXT: yes/no]
```

If PERSON is missing, produce reframes for two candidate persons and mark the set DRAFT.

## Execution Protocol

1. **Diagnose the gap** — no who, who without lens, or lens without who. Fix only the missing part.
2. **Hold the topic** — local topics "always perform"; do not swap the subject.
3. **Append the who** — one clause, one person. Housing-safe if the post touches housing (life situation, habit, feeling; never protected class).
4. **Add the lens** — insider ("that you've probably never heard of"), take ("the one everyone recommends that I'd skip"), or private state ("if you're quietly running the numbers at midnight").
5. **Generate 5–7 reframes** across mechanisms — life stage, timing, private state, habit/place, insider lens, contrarian lens — and tag each.
6. **Add one comfort variant** — feeling first, offer withheld ("you're not behind" structure).
7. **AI rule** — if a model helps, it reframes the existing hook for the audience from the agent's point of view; it does not write a new post.
8. **Recommend one** — with a one-line distribution rationale and the expected reader reaction ("that's me, I'll keep swiping").
9. **Voice + fair-housing check** — would the agent say it aloud; is the frame clear.

## Output Contract

Markdown set, 200–400 words. Sections: Diagnosis; Reframes table (5–7 rows + one comfort row, columns: reframe, who, lens, mechanism, format fit); Recommended with rationale and expected reaction; Voice check and fair-housing status; Handoff block. Every row carries a who and a lens. No FOMO or deadline language.

## Output Skeleton

```markdown
# HOOK REFRAME SET — [agent] — [topic]

## Diagnosis
- Broad hook: "[verbatim]"
- Missing: [who / lens / both]
- Person: [one line]

## Reframes
| # | Reframe | Who | Lens | Mechanism | Format fit |
| 1 | … | … | … | … | … |
| C | [comfort variant] | … | … | private state | … |

## Recommended
"[reframe]" — because [rationale]. Expected reaction: "[…]".

## Voice check
[yes / rewrite] · Fair-housing: [clear / adjusted]

## Handoff → jen-engine Stage 3 / 04-comfort-content-engine
- Output produced: Hook Reframe Set
- Next input: [recommended hook + format]
- Validation: who + lens in every row [yes/no]
- Open risk: [person unconfirmed / register]
```

## Quality Gate

- Every reframe carries a who AND a lens?
- Topic preserved?
- Would the named person stop because the hook describes them?
- Comfort variant is feeling-first with offer withheld?
- Fair-housing frame clear on housing content?
- Zero FOMO, rent-shaming, or "before it's too late"?

## Creative Latitude

The lens is the creative act. The who narrows; the lens makes it *this agent's*. Reach for the agent's real opinion, a local detail only a resident knows, or the private feeling nobody says out loud. A reframe that is precise but flat ("...if you're a first-time buyer") has done half the job. Vary the rhythm across rows — a fragment, a question, a flat declarative — so the set reads like one person thinking, not a formula spinning.

## Deploy When

- A planned post's hook reads like a listicle title.
- A template or B-roll is ready but "the hook wasn't adjusted."
- Before `jen-engine` Stage 3 ships its RECOMMENDED hook.

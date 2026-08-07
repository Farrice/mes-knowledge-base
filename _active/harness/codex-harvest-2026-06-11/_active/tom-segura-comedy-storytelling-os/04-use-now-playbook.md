# Tom Segura Use-Now Playbook

## Fast Social Punch-Up

Use when a post is correct but flat.

1. Name the audience and what they privately recognize.
2. Identify the draft's neutral sentence.
3. Rewrite it as an opinion, irritation, or oddly specific observation.
4. Add a reason-for-telling if the post uses a story.
5. Cut any setup the audience already knows.
6. Replace accurate-but-dead words with accurate-and-vivid words.
7. Run humor fit if the post sells, advises, or claims authority.

Output:

```markdown
## Tom Social Punch-Up
- Audience:
- Original weak line:
- Charge found:
- Way in:
- Rewrite:
- Source mechanics:
- Behavior delta:
- Next gate:
```

## Story-To-Bit Compression

Use when a story has good material but wanders.

1. Tell the long version without editing.
2. Write one sentence answering: "Why am I telling this?"
3. Mark the moment where pressure appears.
4. Cut everything not needed for that pressure or payoff.
5. Add one or two punch points.
6. End on the clearest surprise, not the chronological ending.

Output: long draft, reason-for-telling, cut draft, punch draft.

## Funny-Vs-Flat Diagnosis

Use when a line is trying to be funny but does not land.

Check:

- Is there an opinion, or is the line indifferent?
- Is the observation too generic?
- Is the punch expected?
- Is the audience missing the setup?
- Is the risk too early for the relationship?
- Is the word choice accurate but dull?
- Is this a joke beside the real tension?

Output: keep, cut, or rewrite with the reason.

## Marketing And Copywriting Use

Use Tom only as the observation/story layer. Then hand off to Sam Parr or `/publishable-copy-gate` when the copy must convert.

Best sequence:

1. Tom layer: find recognition, way in, word choice, and surprise.
2. Sam Parr layer: check proof, reader action, curiosity, and humor fit.
3. Publishable gate: check punch, proof, voice, CTA, anti-slop, and risk.

## General Writing Use

Use when a personal essay, newsletter, or long-form piece needs more life.

- Find the ordinary thing everyone has experienced.
- Make the stakes explicit.
- Compress the story after drafting.
- Encode timing in the prose because the reader cannot hear delivery.
- Use callbacks as signs of attention, not decorations.

## Replay Prompt

```text
Use the Tom Segura comedy-storytelling layer on this draft.
Audience: [who it is for]
Desired reader action or feeling: [what should change]
Trust risk: [low/medium/high]
Draft: [paste]

Do not imitate Tom's persona. Diagnose the weak link, find the charge, identify the way in, rewrite the smallest useful section, explain the behavior delta, and send it to the next gate if it is public or conversion-oriented.
```

# /lynch-receive-the-draft — Flow-State Drafting Protocol (Ron Lynch)

> Ron Lynch's actual writing method, extracted from how he described it to Kathleen Kennedy and Steven Spielberg: know the character, know the beginning and the end, do NOT plot the middle — sit down, receive it, and take dictation. Plus the two guard systems that keep the channel open: the "I can't" alarm and the doors-in-the-pool protocol for agonizing first reps. This is the process layer under every other Lynch workflow — how the drafts actually get written.

Source anchors: `extractions/ron-lynch/transcript.txt` — verbatim quotes cited per step; ledger in `references/source-ledger.md`.

## When to Use
- Drafting anything substantial: sales copy, scripts, editions, campaign creative, screenplay-shaped content
- When a draft is stalling because the writer is trying to engineer the middle
- When "I can't" / "I would never come up with that" language appears in a creative session (the alarm bell — treat it as a trigger for this workflow)
- First rep of any new format (first VSL, first creative brief, first script) — the doors-in-the-pool case

## When NOT to Use
- Editing/refinement passes (this is a GENERATION protocol; refine with `/lynch-copy-pass` or craft experts)
- Work that is genuinely assembly, not creation (reports, compilations)

## Inputs Required
1. The character (who this piece is for/about — a Voice Card if one exists)
2. The beginning (the opening image/claim/scene)
3. The end (where the reader/viewer must land — belief, action, feeling)
4. Honest inventory: any "I can't" statements in the room

## Execution Steps

### Step 1: Flip the Filter (pre-writing, mandatory)
Verbatim standard: *"You will never come up with that as long as you say I can never do that because you've now turned off a filter of acceptance in your mind. All great art comes from beyond."*

- Catch every "I can't / I'd never come up with that" in the session. Each one is an alarm bell, verbatim: *"If I hear an I can't, that's an alarm bell to me."*
- Replace each with the receptive form: "I absolutely could come up with that if I was open to it." Then ask the receptive question: "What is the most innovative thing I could do here?"
- Companion phrase, verbatim: *"With risk comes reward."* If an idea registers as risky, that is a reason to look harder at it, not away from it.

### Step 2: Fix the Endpoints, Free the Middle
Verbatim standard: *"I sit down and I know the character and I know where I want them to go. Like I know the beginning and the end, but I don't know the middle."*

- Write the beginning in full (the opening 1-3 lines / the opening image).
- Write the end in full (the closing beat — where the reader lands).
- Explicitly refuse to outline the middle. The middle is received, not planned. An outlined middle produces engineered copy; a received middle produces alive copy.

### Step 3: Take Dictation
Verbatim standard: *"I start writing and... the movie's there. And I take dictation... I'm not writing the movie, I'm watching the movie, taking notes on the movie... you have to have the courage to step in and say I'll receive the written movie and then write that movie."*

- Draft in one continuous sitting, no editing mid-stream, no backtracking. Watch the piece happen and transcribe it.
- When a character/example/scene "walks in" unplanned, let it in — that is the mechanism working, not a digression to prune (pruning is the NEXT pass's job).
- Flow-state conditions, verbatim: *"Flow state is magic... it's completely accessible to all of us all the time. It's just we don't opt into it."* Lynch's binary: *"It's that or it's rest."* If the state won't come, rest — do not grind a middle into existence.

### Step 4: The First-Rep Protocol (when this format is new)
Verbatim standard: *"The first one is always agonizing. But once you get that son of a bitch open, the water starts flooding in. The second one's really easy to do and the third one's even easier and then it becomes part of your identity."*

- Name it out loud: this is a first rep; agonizing is the expected cost, not a verdict on ability.
- Ship the first rep anyway — the door only opens under pressure. Schedule rep two within days (the flood depends on proximity).
- Defiance check, verbatim: *"You have to have an internal defiance. Otherwise, you're complacent."* The "I can't"s *"have to piss you off."*

### Step 5: Only Then, Edit
Hand the received draft to the appropriate refinement pass (`/lynch-copy-pass` for the identity/register filters, or the piece's owning expert). Never edit during reception — the two modes kill each other.

## Output Format
```
## RECEIVED DRAFT — [Piece Name]

### Endpoints
- Character: [who]
- Beginning: [written in full]
- End: [written in full]

### Filter log
[Any "I can't" caught and flipped — before/after]

### The draft
[The full received middle + endpoints, unedited]

### First-rep note (if applicable)
[Which door this opened; when rep two is scheduled]

### Handoff
[Which refinement pass this goes to next]
```
Execution prompt: `references/prompts-v2/lynch-receive-the-draft.md`

## Quality Gate
- Beginning and end were written BEFORE the middle
- The middle was drafted in one continuous pass — no mid-stream editing artifacts
- Every "I can't" in the session is logged and flipped, not ignored
- Unplanned arrivals were kept in the draft (pruning deferred to the edit pass)
- If flow didn't come, the output says "rested, not ground out" instead of shipping an engineered middle as received

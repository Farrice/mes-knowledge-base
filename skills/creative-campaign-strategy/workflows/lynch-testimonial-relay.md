# /lynch-testimonial-relay — Little Red Riding Hood Social Proof (Ron Lynch)

> Lynch's testimonial architecture: five people each tell a SNIPPET of one story, sequenced along the customer journey, so the audience perceives unanimous identical experience. Verbatim: *"If I build the testimonials correctly, it'll feel like five people are telling Little Red Riding Hood and they all only have to tell a snippet of the story... you know they all experienced the same experience."* The anti-pattern it replaces: stacking full testimonials (repetitive, skimmed, dead).

Source anchor: `extractions/ron-lynch/transcript-2-dOM.txt`; ledger in `references/source-ledger.md`.

## When to Use
- Any asset that carries social proof: VSLs, landing pages, sales pages, case-study sections, webinar proof blocks, retail pitch decks
- Existing testimonials that repeat each other or run too long
- Thin proof inventories — the relay makes 5 fragments outperform 5 essays
- Client work: turning raw reviews/interviews into a proof section

## When NOT to Use
- Proof-tier strategy (what KINDS of evidence, ranked) — that's proof-hierarchy work (Luke Iha proof ladder, P2M Stage 4)
- Single-testimonial features (one long-form story is a different tool)

## Inputs Required
1. The story arc being proven (the customer journey: state → decision → use → result → reaction)
2. Raw proof inventory (reviews, interviews, messages, case notes)
3. The asset the relay ships in (format constraints)

## Execution Steps

### Step 1: Write the One Story
Define the single narrative all voices will jointly tell, in 5-6 beats: the before-state, the skeptical moment, the first use, the result, the reaction of others (GP-15's layer: "People are going to love you for this"). This is Red Riding Hood — cape, basket, woods, house, wolf.

### Step 2: Cast the Relay
Assign each beat to ONE voice from the proof inventory. Match voice to beat: the skeptic gets the skeptical beat, the enthusiast gets the reaction beat. 4-6 voices; never two voices on the same beat.

### Step 3: Cut to Snippets
Each voice speaks 1-2 sentences MAX, in their real language (mine it, never polish it into brand-speak). The fragment must be unintelligible as a full story alone — that's what forces the viewer to assemble it and perceive unanimity.

### Step 4: Sequence and Seam
Order strictly along the arc. Check the seams: each snippet should pick up roughly where the last left off. No snippet may restate a prior beat.

### Step 5: The Unanimity Test
Read the relay end-to-end as a cold viewer: do you come away believing everyone had the same complete experience? If any voice reads as a different story (different product promise, different journey), recast or cut it.

## Output Format
```
## TESTIMONIAL RELAY — [Asset]

### The one story (beats)
1. [before] 2. [skeptic] 3. [first use] 4. [result] 5. [reaction]

### The relay
| # | Beat | Voice (who) | Snippet (verbatim-grade) |
|---|---|---|---|

### Placement note
[Where in the asset + format adaptation]
```
Execution prompt: `references/prompts-v2/lynch-testimonial-relay.md`

## Quality Gate
- One story, 5-6 beats, each beat owned by exactly one voice
- Snippets are 1-2 sentences, real mined language, incomplete alone
- Sequence follows the journey arc with clean seams, no restated beats
- The reaction-of-others beat is present (the ultimate sell layer)
- Cold-read produces "they all had the same experience"

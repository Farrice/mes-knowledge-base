# /lynch-copy-pass — The Lynch Lens on Any Copy (Ron Lynch)

> The general-purpose deployment of Ron Lynch's copywriting genius on a single piece of copy — a post, an email, a landing section, an ad, a VSL block. Not campaign architecture (→ `/lynch-identity-campaign`), not sentence-level polish (→ Joanna Wiebe, Alen Sultanic). This is the identity-and-register layer between the two: what the reader becomes, whose voice carries it, how authority lands without intimidation, and what the eye sees while the words run.

Source anchors: `extractions/ron-lynch/transcript.txt` — verbatim quotes cited per step; ledger in `references/source-ledger.md`.

## When to Use
- Any copywriting task where Farrice wants Lynch's approach applied to a single piece (daily content, client copy, emails, ads, sales pages)
- Existing copy that is feature-led, brand-voiced, or "impressive" instead of mind-reading
- Expert/authority content that intimidates instead of encouraging
- Copy that sells the product instead of the transformation
- As the final expert pass after another expert drafted the piece (Lynch is the lens, not the author swap — one author per body still holds)

## When NOT to Use
- Full campaign design (→ `/lynch-identity-campaign`, `/lynch-campaign-ecosystem`)
- Sentence-level rhythm/craft surgery (→ Wiebe, Sultanic, Sam Parr)
- Pieces where the customer voice is unknown — run `/lynch-customer-voice-mine` first

## Inputs Required
1. The copy (draft or brief for a new piece)
2. Who receives it (even rough — the pass sharpens it)
3. What the piece must cause (click, reply, buy, believe)

## Execution Steps — The Five-Filter Pass

Run the copy through all five filters IN ORDER. Each filter either passes or rewrites.

### Filter 1: Identity — What does the reader BECOME?
Verbatim standard: *"When advertising works really well, you're not selling a product to a customer. You're selling an identity to a customer. So, in GoPro, we didn't sell cameras. We sold bravery."*

- Name the identity shift this piece offers in ONE word (bravery, sophistication, mastery, freedom).
- If the piece has no identity payload — it describes a thing instead of who the reader becomes — rewrite the frame before touching anything else.
- Counter-identity check (GP-11): is this the aspirational identity, or an accurate-but-unglamorous mirror? Sell what the best 5% of users become.

### Filter 2: Customer's Voice — Whose head is this written inside?
Verbatim standard: *"The trick is actually to write in the customer's voice because you're trying to get in their head. How do I write inside the head of the person who will be receiving this?"*

- Read the piece as the recipient. Score: does it produce "it's like they were reading my mind" or "that's impressive"? "Impressive" = wrong voice, rewrite.
- Pull the customer's actual vocabulary (from a Voice Card if one exists) into the load-bearing lines: the hook, the turn, the close.

### Filter 3: Chess-to-Checkers — Authority without intimidation
Verbatim standard: *"How does a chess player talk to a checkers player to get them information and to level up so they don't feel intimidated or talked down to or belittled, but they feel encouraged? How would my professional talk to somebody with just the edge of authority, but the compassion and empathy to get them to make the decisions?"*

- Assume the authority — never perform it. Delete credentials-flexing; keep the edge of authority in HOW things are said.
- Every expert concept gets translated DOWN one sophistication level without condescension. The reader should feel leveled up, not lectured.

### Filter 4: Metaphor Compression — One complicated idea → one graspable form
Verbatim standard: *"A smart person takes a complicated idea and brings it into metaphor form for a person outside to get in... That's when you become excellent."*

- Find the piece's most abstract or technical claim. Compress it into ONE concrete metaphor drawn from the reader's world (not the writer's).
- One metaphor per piece, carried through — not a metaphor per paragraph. Lynch's metaphors are load-bearing, not decorative.

### Filter 5: The Right Column + Transformation Close
Verbatim standards: *"I write the right side of the script. I write the visuals."* and *"It's never buy the appliance to make this. It's you want to make this. Oh, you need the appliance to do it."*

- Right column: even for text-only copy, write what the reader SEES — the mental footage each section runs. If a section produces no picture, it's dead weight; cut or concretize.
- Close transformation-first: the CTA offers the result, and the product/action is revealed as the way to get it. Never "do X to get Y" — always "want Y? X is how."

## Output Format
```
## LYNCH COPY PASS — [Piece Name]

### Verdict per filter
| Filter | Pass/Rewrite | The issue (one line) |
|---|---|---|
| 1 Identity | ... | ... |
| 2 Customer's voice | ... | ... |
| 3 Chess-to-checkers | ... | ... |
| 4 Metaphor | ... | ... |
| 5 Right column + close | ... | ... |

### The identity word: [one word]

### Revised copy
[The full piece after the pass — one author's hand, Lynch's filters]

### Right column notes (if the piece will carry visuals)
[What the viewer/reader should SEE, section by section]
```
Execution prompt: `references/prompts-v2/lynch-copy-pass.md`

## Quality Gate
- Identity shift named in one word, and the piece's frame actually carries it
- The mind-reading test beats the impressive test on the load-bearing lines
- No credential-performing; authority is assumed in register, not claimed in content
- Exactly one load-bearing metaphor, drawn from the reader's world
- Close is transformation-first ("want this? here's the way"), never product-first
- The pass preserves the original author's voice — Lynch is a lens here, not a body-snatcher (one author per body)

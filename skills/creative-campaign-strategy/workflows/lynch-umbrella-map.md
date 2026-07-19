# /lynch-umbrella-map — The Strategist's Bible (Ron Lynch)

> Lynch's definition of what a strategist actually does — the piece he says most "strategists" skip: parse the whole crowd into distinct audiences, pick three benefits per audience aimed at their pain, sequence which audience to win FIRST by earliest financial success, match offers to each audience's personal economics, and connect everything under one brand story. All roads lead to Rome. This is the layer ABOVE `/lynch-media-match` (channels) and `/lynch-identity-campaign` (a single identity) — the full-market map both plug into.

Source anchors: `extractions/ron-lynch/transcript.txt` — verbatim quotes cited per step; ledger in `references/source-ledger.md`.

## When to Use
- A product/brand with multiple plausible audiences and no sequencing decision
- "Who do we win first?" questions — beachhead selection with a financial lens
- Turning one offer into segment-specific messaging without fragmenting the brand
- Any engagement where the client calls data-mining "strategy" (the anti-pattern below)
- Business verticals beyond marketing: the parse works for service lines, content pillars, and product roadmaps

## When NOT to Use
- Single-audience, single-message pieces (→ `/lynch-copy-pass`)
- Channel pairing for already-chosen segments (→ `/lynch-media-match`)
- Positioning-category decisions (→ April Dunford skills — stack AFTER positioning is set)

## The Anti-Pattern This Replaces
Verbatim: *"There's definitely many copywriters that they think strategy means looking at existing campaign data and deciding which winners were the winners and then writing more like that... That's copywriting."* Optimizing winners is not strategy. The umbrella map is.

## Inputs Required
1. The product/offer and its actual margin structure (even rough)
2. Everything known about who could buy (research, Voice Cards, sales data)
3. The brand story (or a draft of it — the umbrella everything hangs under)
4. Current offer(s) and price points

## Execution Steps

### Step 1: Parse the Crowd
Verbatim standard: *"Now strategist is I'm going to write a Bible. I understand how the whole crowd works. I understand the crowd is parsed of different types of people."*

- List every distinct audience that could buy — target 6-10 (Lynch's own count: *"I'm going to do that 10 times with 10 different audiences"*).
- Distinct = different pain or different identity, not different demographics. Two segments with the same pain are one audience.

### Step 2: Three Benefits × One Pain per Audience
Verbatim standard: *"I'm going to pick three benefits and one audience and focus on their pain and solution."*

- For each audience: their ONE dominant pain, the THREE benefits (of everything the product does) that answer it, and the solution frame in their language.
- Discipline: the product may have 15 benefits — each audience only ever hears three. Fifteen benefits at once is a catalogue, not a message.

### Step 3: Sequence by Earliest Financial Success
Verbatim standard: *"Which one has the highest chance of financial success earliest on to get us here for day two... This is the customer we have to win first because they're more likely to spend and give us success. Here's the second most likely. Here's the third most likely."*

- Rank audiences by: likelihood to spend NOW × ease of reach × margin contribution. The winner is the beachhead; day-two audiences wait.
- Verbatim frame for why this ordering exists: *"It is a financial game as much as it is a creative game."*

### Step 4: Offers Matched to Personal Economics
Verbatim standard: *"And I might have three different offers to match their personal economics."*

- Design up to three offer tiers so no ready audience is priced out and no premium audience is underpriced. Tiers differ by depth/access, never by watered-down promise.

### Step 5: The Umbrella — All Roads Lead to Rome
Verbatim standard: *"And all of those are going to connect under a brand story. And all roads lead to Rome. I come to the ultimate solution."*

- Write the one brand story every segment message must reinforce. Test each Step 2 message: does it ladder up to the umbrella? A message that wins its segment but contradicts the story is cut.
- Then backfill the language, verbatim: *"and then backfill to here's the language that gets them here to the purchase"* — the copy comes LAST, after parse, sequence, offers, and umbrella.

### Step 6: First-Business Check
Verbatim standard: *"Everybody who's in a business is first in the marketing business of their business... If you're selling soap, you're not in the soap business. You're in the marketing-soap business."*

- Close by naming what "the marketing business of this business" is — the one sentence the founder must accept before any of the map executes.

## Output Format
```
## UMBRELLA MAP — [Brand/Product]

### The umbrella (brand story, one paragraph)

### The parse
| # | Audience | Dominant pain | 3 benefits | Solution frame (their language) |
|---|---|---|---|---|

### The sequence
1. WIN FIRST: [audience] — [why: spend likelihood × reach × margin]
2. Day two: [audience] — [trigger to activate]
3. ...

### Offer tiers
| Tier | Offer | Price logic | Which audiences |
|---|---|---|---|

### Backfilled language (beachhead only)
[Hook + message spine for audience #1 — the rest wait for day two]

### The first-business sentence
[What the marketing business of this business is]
```
Execution prompt: `references/prompts-v2/lynch-umbrella-map.md`

## Quality Gate
- 6-10 audiences parsed by pain/identity, not demographics
- Each audience gets exactly three benefits — no catalogue messaging
- Beachhead chosen on financial-success-earliest logic, stated explicitly
- Every segment message ladders to the umbrella story; contradictions cut
- Copy/language written LAST, and only for the beachhead
- The map would survive Lynch's test: is this strategy, or winners-data copywriting wearing the title?

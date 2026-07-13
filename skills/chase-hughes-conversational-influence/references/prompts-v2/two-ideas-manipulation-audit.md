---
name: "Chase Hughes — Two-Ideas-No-String Manipulation Audit"
source_prompt: born-v2
skill: chase-hughes-conversational-influence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Chase Hughes's manipulation-detection technique: ideas placed close together without an explicit causal connector trigger the brain's pattern-completion machinery — the audience builds the connection itself and treats it as its own conclusion, which makes the technique nearly resistance-proof. Hughes tells his kids this is one of only two things they should fear (the other: any adult who asks them to keep a secret) — both are signals of cognitive engineering without consent. This audit runs both defensively (spot manipulation being done to you) and offensively (audit your own copy for conclusions you're engineering without the audience's consent).

## Input Required

- `[TEXT]` — the full artifact to audit: news segment, ad copy, social post, courtroom argument, sales page, pitch deck, press release, content piece. Pasted or fetched in full — audit-grade analysis requires the actual text, not a summary.
- `[MODE]` — Defensive (analyzing someone else's text to expose the architecture) or Offensive (auditing your own draft before shipping it)
- `[STAKES]` — optional: what happens if a manipulative pair ships unaddressed (reputational, legal, ethical, conversion)

## Execution Protocol

### Step 1 — Inventory Every Claim Pair Without an Explicit Connector

Walk the full text. Identify every pair of factual claims that:
1. Sit in close proximity (same sentence, adjacent sentences, same paragraph, adjacent paragraphs)
2. Share no explicit causal connector ("because," "therefore," "this is why," "as a result," "which means," "due to")
3. Imply a connection the brain's pattern-matcher would naturally produce

For each pair, capture: Claim A, Claim B, spatial proximity, and the implied connection (name the connector the brain silently supplies).

### Step 2 — Identify the Engineered Audience Action

For each pair, name what the implied connection nudges the audience toward:
- Belief change ("I now think X is true")
- Person/entity evaluation ("I now distrust/trust/fear/admire X")
- Emotional shift ("I now feel anger/fear/urgency about X")
- Behavioral nudge ("I now want to buy/vote/share/call/leave")

### Step 3 — Apply the Ethics Flag

Hughes's framework distinguishes legitimate inference-work from manipulation. For each pair, mark exactly one:
- **Legitimate** — the implied connection is a true causal claim the author could and should have stated explicitly; the pattern-completion is an aesthetic choice (subtext, "show don't tell"); the reader is not harmed by the invisibility.
- **Manipulative** — the implied connection is unsupported, contested, or false, and the author is using proximity to bypass the skepticism explicit causation would trigger; the reader IS harmed by the architecture being invisible.
- **Ambiguous** — cannot be determined from the text alone; depends on facts outside the artifact.

### Step 4 — Stack Rank by Force

Identify the 2-3 strongest pairs — the ones doing the heaviest persuasive lifting. Prioritize pairs that sit at high-attention positions (headline + first paragraph, ad lead + close, opening + final argument), pairs where an emotional claim borrows neutrality from an adjacent factual one, and pairs producing person-evaluation (distrust, fear) rather than mere belief change.

### Step 5 — Produce Mode-Specific Output

- **Defensive**: deliver the audit so a reader can see the manipulation architecture and decide, informed, whether to consent to it.
- **Offensive**: for each Manipulative-flagged pair in your own copy, resolve one of three ways — (a) add an explicit connector if the implication is true, (b) cut one of the two claims if the implication is unsupported, (c) restructure to break the proximity. Re-flag after the fix.

## Output Contract

- Full pair inventory (every qualifying pair found, not a sample)
- Ethics flag per pair with justification
- Stack rank of the 2-3 strongest pairs
- A verdict statement on whether the text as a whole is doing legitimate inference-work or manipulating
- Mode-appropriate recommendations (defensive read-guidance, or offensive specific edits)

## Output Skeleton

```
TEXT AUDITED:
[source / context / length]

PAIR INVENTORY:

Pair 1
- Claim A: [verbatim or close paraphrase]
- Claim B: [verbatim or close paraphrase]
- Proximity: [same sentence / adjacent sentences / same paragraph / adjacent paragraphs]
- Implied connection: [the connector the brain supplies]
- Engineered action: [belief change / person-evaluation / emotional shift / behavioral nudge]
- Ethics: [Legitimate / Manipulative / Ambiguous]
- Notes: [why this flag]

Pair 2
[same format]

[continue for every pair found]

STACK RANK (heaviest persuasive lift):
1. [pair #] — [one-line summary of what it engineers]
2. [pair #] — [...]
3. [pair #] — [...]

VERDICT:
[is this text doing legitimate inference-work or manipulating — and why]

RECOMMENDATIONS:
[Defensive: what a reader should be aware of]
[Offensive: specific per-pair edits — add connector / cut claim / restructure]
```

## Quality Gate

- Was the FULL text walked, not a sample — are all qualifying pairs captured, not just the obvious ones?
- Does every ethics flag carry a stated reason, not just a label?
- Is the stack rank limited to 2-3 pairs and justified by attention-position or emotional-borrowing logic, not arbitrary?
- Does the verdict address the text as a whole, not just restate the strongest pair?
- In Offensive mode, does every Manipulative-flagged pair get one of the three resolutions (connector / cut / restructure)?

## Creative Latitude

This is a diagnostic deliverable — the floor is completeness and honesty of the ethics call, not creative expression. The judgment call that matters most: distinguishing legitimate subtext ("show don't tell," a defensible aesthetic choice) from manipulation (bypassing skepticism the audience would otherwise apply). When a pair is genuinely ambiguous, say so rather than forcing a Legitimate/Manipulative binary — false precision on the ethics flag is worse than an honest Ambiguous.

## Deploy When

- Reading a news piece, ad, or political message that "feels" persuasive and you can't say why
- Auditing your own ad/copy/content for places you're engineering conclusions the audience hasn't consented to
- Teaching media literacy — the workflow itself is the curriculum
- Diagnosing why a competitor's content converts harder than yours despite weaker claims
- Stress-testing a press release, pitch deck, or persuasive memo before it ships

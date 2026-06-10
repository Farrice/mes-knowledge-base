---
description: "/hawley-campaign-coherence — turns a multi-deliverable campaign or brand system into one voice across every maker and touchpoint; outputs a coherence kit (voice logic + per-touchpoint tone containers + deliverable check)."
---

# Campaign Coherence

A campaign with many makers is a writers' room with the same problem Hawley solves every season: eight writers, one voice. The fix is never a thicker style guide. You codify the generative logic — the question the brand answers, the feelings it induces — so a stranger can write a new episode in voice, then you make every touchpoint *be* the experience instead of describing it.

## Pre-Flight
Read these files before executing:
1. `skills/noah-hawley-storytelling-mastery/genius.md`
2. `skills/noah-hawley-storytelling-mastery/references/cross-domain-patterns.md` (Translation 3)
3. `skills/noah-hawley-storytelling-mastery/references/genius-patterns.md` (Patterns 1, 10, 15)

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md § Decision Framework` — confirm you can answer the question (what is the brand answering?), the ending (what end-state does the campaign land the audience in?), and the assumption being taken for granted (which category default the campaign accepts that could become its differentiator).

## Input Required
- The brand or campaign name + what it sells, and to whom.
- The full deliverable set (every touchpoint: ads, emails, landing page, DMs, social, packaging, etc.) and who/what makes each (designer, copywriter, the operator, AI agents).
- Any existing voice material — brand bible, prior campaigns, hero lines. If none, say so.
- The campaign's destination: the single feeling or shift the audience should leave with.
- The constraint set (budget, channel limits, timeline) — these become wedges, not excuses.

---

## Workflow

### Step 1: Codify the voice as generative logic
A style guide tells a maker which fonts and which banned words. It cannot tell them how to write a sentence they've never seen. Codify the engine instead: the question the brand is answering and the paint swatch of feelings it induces. Theme-first, not surface-first — spirit, not mannerism.

Fill this before anything else:

| Layer | Prompt | Capture |
|-------|--------|---------|
| The question | What question does this brand answer for the audience, in their words? (Not the mission — the *tension* they live in.) | |
| The feeling swatch | Name 3–4 feelings every touchpoint must produce. Not adjectives for the logo — felt states in the reader's body. | |
| The recipe | What are the 3–5 ingredients that, mixed in proportion, *are* this brand? (Hawley reads the Coens as comedy + violence + philosophy + Judaism. Find yours.) | |
| The forbidden register | What feeling, if the audience ever felt it from us, means we failed? | |

Test the logic: hand it to a maker who has never seen the brand. Can they write a net-new line in voice? If they need an example to copy, you've written a style guide, not generative logic. Rebuild.

### Step 2: Build tone-embodying containers per touchpoint
The pitch had the same tone as the show. Every artifact must *be* the experience, not summarize it. A welcome email that "describes a warm brand" in chilly transactional copy has already broken voice. The container's job is to give a stranger the feeling before they read a word of content.

For each touchpoint, specify the container — the structural move that makes the format embody the recipe:

| Touchpoint | The feeling on arrival | The container move (how the format itself carries it) |
|-----------|------------------------|-------------------------------------------------------|
| Landing page | | (e.g. the first scroll *withholds* the offer the way a cold open withholds the threat) |
| Email | | (e.g. the subject line is tension; the P.S. is the dry-then-score release) |
| DM / outreach | | (e.g. it refuses the sales scene — opens as the recipient's world, not ours) |
| Ad / social | | (e.g. one tension→release unit; the hook builds, the last frame releases) |
| Packaging / physical | | |

Where music doesn't go: name the touchpoint where the brand should go quiet so a louder one detonates. A campaign that performs at full volume everywhere has no dynamics — and no impact.

### Step 3: Originality-through-adaptation, per deliverable
Each deliverable brings full original intensity *and* stays unmistakably on-brand. The recipe is remixed in new proportions — never copy-pasted, never diluted. A maker shouldn't reskin a hero line across five formats; they should reconstruct the *feeling* of the brand natively in each.

For each deliverable, run the two-sided check:

- **Unmistakably the brand**: which ingredients of the recipe are present, in what proportion?
- **Original intensity**: what did this maker invent here that no other deliverable has? (If nothing, it's a copy servicing a slot, not an episode.)

The failure to catch: the deliverable that honors the surface (right colors, approved words) while producing the forbidden register. Pass the surface; fail the spirit; cut or rebuild.

### Step 4: Coherence check across the full set
Now read the campaign as one object, the way a showrunner reads a season. The enemy is service creep — the deliverable that exists to fill a channel slot rather than to serve the campaign. Hawley brooms the C-story nobody cares about; here you broom the email you sent because it was Tuesday.

For every deliverable, ask the single question: *Does this serve the campaign, or is it servicing the channel?* If it's only there because the channel exists and would otherwise be empty, broom it, pause it, or rebuild it to earn its place. Better a tight set than a complete one.

Then read the set as a sequence: does a stranger moving across touchpoints feel one voice deepening — or many makers in the same costume? Flag any seam where the feeling changes hands.

## Content Type Adaptations
| Format | Adaptation |
|--------|-----------|
| Brand / campaign | The native case — full coherence kit across every maker and touchpoint. Voice logic governs; containers carry; the broom keeps the set tight. |
| Multi-channel launch | Treat the launch window as a season. The destination feeling is the finale; sequence touchpoints so each deepens the question rather than restating it. |
| Newsletter / Substack series | Each edition is an episode of one show; the voice logic is the editorial spine. Stack with `/hawley-content-season` for arc, this for cross-edition voice integrity. |
| Short-form set (LinkedIn/X) | Each post is one tension→release container in the same voice; check that the set has dynamics (quiet posts that let loud ones land), not uniform volume. |
| AI-agent-assisted production | The voice logic *is* the system prompt. If an agent can't generate in-voice from the logic alone, the logic is underspecified — fix it here, not downstream. |

## Output Format
```
CAMPAIGN COHERENCE KIT — [Brand / Campaign]

I. VOICE LOGIC (the generative engine)
   The question the brand answers: ...
   Feeling swatch (3–4 felt states): ...
   The recipe (3–5 ingredients + proportions): ...
   Forbidden register: ...
   Stranger test: [PASS / REBUILD] — a maker can/can't write net-new in voice from this alone

II. TONE CONTAINERS (per touchpoint)
   [Touchpoint] → feeling on arrival → container move
   [Touchpoint] → feeling on arrival → container move
   ...
   Where music doesn't go: [the touchpoint that goes quiet so another detonates]

III. DELIVERABLE CHECK (per deliverable)
   [Deliverable] → on-brand: [ingredients present] | original intensity: [what it invents] | verdict: KEEP / REBUILD / BROOM
   ...

IV. COHERENCE READ (the set as one season)
   Service-creep cuts: [deliverables broomed for servicing a channel, not the campaign]
   Seams flagged: [where the voice changes hands across the set]
   Sequence note: [does moving across touchpoints feel one voice deepening?]
```

## Quality Gate
> **🛡️ Anti-Pattern Check**: review output against `genius.md § Anti-Patterns` and the § Expert-Specific Quality Rubric. Flag and fix any violation before delivering.
- **Voice logic is generative, not descriptive.** A stranger can write a net-new line in voice from the logic alone — no example to copy. If not, it's a style guide; rebuild (Pattern 1).
- **Containers embody, not describe.** Every touchpoint *gives* the feeling on arrival rather than asserting the brand is warm/bold/premium. No artifact summarizes its own tone (Pattern 10).
- **No service creep survived.** Every kept deliverable serves the campaign; nothing exists only to fill a channel slot. The broom column is non-empty if the set was loose (Coherence over Continuity).
- **On-brand without copy-paste.** Each deliverable shows original intensity *and* the recipe — not the same hero line reskinned five ways (Pattern 15).
- **The machinery stays off the page.** The kit instructs makers without lecturing the audience; no touchpoint labels its own theme or names the feeling it's engineering.

## Common Pitfalls
- **Style-guide masquerade.** The voice logic lists fonts, colors, and banned words but can't generate a sentence. Recovery: throw it out, write the question + feeling swatch + recipe, then re-run the stranger test.
- **Describe-the-tone container.** A "warm, human" email that reads cold and transactional. Recovery: rebuild the container so the format's own structure carries the feeling — the subject line is tension, the close is the release — before touching word choice.
- **Uniform volume.** Every touchpoint performs at full intensity, so nothing lands. Recovery: pick where music doesn't go; make at least one touchpoint go quiet so the climactic one detonates (Pattern 16).
- **The complete-but-incoherent set.** Every channel filled, no through-line — many makers in matching costumes. Recovery: broom the channel-servicing deliverables, then read the survivors as a sequence and fix the seam where the voice changes hands.

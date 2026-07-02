# Workflow 09: Controlling Idea Cascade

> **Produces**: The controlling idea (the filter sound bite) + a cascade map propagating it verbatim across every touchpoint
> **Use When**: Messaging exists in fragments (website says one thing, sales deck another, ads a third) or a new campaign/pitch needs ONE idea that governs all downstream language
> **Genius Context**: Load `genius.md` before executing — especially XP1 (Controlling Idea), XP3 (One-Thing Rule), XP5 (Story-Loop Match)

## Pre-Flight

**Required Inputs:**
- The business/campaign and what it sells
- The one problem it owns (from BrandScript element 2 — run `01-brandscript-generator` first if none exists)
- Inventory of live touchpoints (website, deck, sales scripts, ads, product listings, emails, UI copy)
- (Optional) Existing one-liner and sound bites

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. If the request is a single-channel rewrite, route to `02-narrative-copy-transformer` instead — this workflow is for the idea ABOVE the channels.

## Execution

You are Donald Miller in his highest-leverage mode: not the copywriter, the **strategist who chooses the words once**. Miller's $100K engagements work exactly this way — the controlling idea is born in the pitch deck, then he walks the CMO, the ad agency, and the product team through one question: "This is the controlling idea. Where can we get this language in the user interface? On your website? In your sales scripts? In product copy on Amazon?" The value is not the deck. The value is one idea, everywhere, verbatim.

### Step 1: Extract the One Thing

Apply the concentric-circle rule (XP3): at market distance, this brand is known for exactly ONE thing. Name it in under 6 words. If multiple product lines exist, name the umbrella promise every product delivers on (Ramsey: financial peace; Apple: easy-to-use technology; Miller: clear messages).

### Step 2: Draft the Controlling Idea

One sentence that fuses the one thing with the customer's transformation. Rules:
- It is a FILTER, not a tagline — it may never appear publicly verbatim, but every public sentence must be its child
- It must contain the problem's story-frame (XP5: the loop all downstream copy will keep opening and closing)
- Zero cognitive load — if it needs explaining, it can't govern anything

Generate 3 candidates. Test each: could this sentence veto an off-brand headline? If it can't reject anything, it's too vague to be a filter.

### Step 3: Derive the Governed Sound Bites

Confirm the SB7 sound bites (+ one-liner + identity transformation, XP2) each trace back to the controlling idea. Any sound bite that can't = rewrite the sound bite, not the idea. Output the locked set — these exact words, no synonyms ("every good marketing effort is an exercise in memorization").

### Step 4: Build the Cascade Map

Table with one row per live touchpoint: Touchpoint → Where the language lands (header, first slide, opening line, subject line) → Which sound bite verbatim → Owner. Minimum coverage: website header, pitch deck slide 1, sales-rep opening script, top ad, primary product listing, email signature/nurture opener. Flag every touchpoint currently carrying language that fails the filter.

### Step 5: Stress Test the Cascade

- **The Veto Test**: Feed 3 real existing headlines through the controlling idea — does it cleanly accept/reject each?
- **The Memorization Test**: Can a new sales hire recite the controlling idea + one-liner after one reading?
- **The 10-Circle Test** (XP4): Does the cascaded homepage now yield 10+ problem/solution circles?
- **The Mall Yell Test**: Yelled in a crowded mall, does the ICP turn around?

## Output Schema

```yaml
deliverable: "Controlling Idea Cascade"
components:
  controlling_idea:
    description: "The one filter sentence + 2 rejected candidates with reasons"
  one_thing:
    description: "The <6-word market-distance identity"
  governed_sound_bites:
    description: "Locked verbatim set traceable to the controlling idea"
    includes: [sb7_set, one_liner, identity_transformation]
  cascade_map:
    description: "Touchpoint → placement → verbatim sound bite → owner"
  violations:
    description: "Current live language that fails the filter, with replacement"
  stress_test_results:
    tests: [veto_test, memorization_test, ten_circle_test, mall_yell_test]
```

## Quality Gate

- [ ] Controlling idea can VETO real off-brand copy (it's a filter, not a platitude)
- [ ] Every sound bite traces to it; no orphan messages survive
- [ ] Cascade map covers minimum 6 touchpoints with verbatim language (no "adapt as needed")
- [ ] Problem noun and product noun share one story-frame (XP5)
- [ ] Passes all 4 stress tests

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. The cascade's most common failure is AN-1 in disguise — a controlling idea about the brand's greatness instead of the customer's transformation.

## Example Output

**Context**: "Harbor Books" — an independent bookstore chain with cafés, events, and an online shop; messaging currently fragments across "community hub," "curated selection," and "shop local."

**CONTROLLING IDEA**: "We turn 'I never have time to read anymore' into a reading life people actually keep."
- Rejected: "Where book lovers belong" (can't veto anything — accepts all copy)
- Rejected: "The best-curated shelves in the city" (brand-as-hero; curation is the mechanism, not the transformation)

**ONE THING** (market distance): "Getting you reading again."

**GOVERNED SOUND BITES (locked):**
- Problem: "You used to read all the time. Now the books just pile up."
- One-liner: "Most people miss reading but can't seem to start again. Harbor matches you with the right next book and a standing time to read it — so reading becomes part of your week, not your someday list."
- Identity transformation: "From person who used to read to reader again."

**CASCADE MAP (excerpt):**
| Touchpoint | Placement | Verbatim language | Owner |
|---|---|---|---|
| Website header | H1 | "You used to read all the time. Now the books just pile up." | Web |
| Staff script | Greeting follow-up | "What's the last book you actually finished?" → one-liner | Store mgrs |
| Meta ad | Hook line | Problem sound bite + "Get your next right book" | Agency |
| Email nurture | Opener, every send | "Reader again" identity line in P.S. | Marketing |

**VIOLATIONS FLAGGED**: "A community hub for the literary-minded" (header, fails veto — brand-as-hero, 25-lb load) → replaced with problem sound bite.

**STRESS TESTS**: ✓ Veto ✓ Memorization ✓ 10-Circle (13 circles post-cascade) ✓ Mall Yell ("the books just pile up" turns exactly the lapsed-reader ICP around)

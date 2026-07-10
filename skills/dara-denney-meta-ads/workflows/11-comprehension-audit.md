---
description: The 1-second comprehension + visual-hierarchy kill-gate for a static ad. Audit an existing or draft static and return KEEP / FIX / KILL with specific fixes.
---

# `/dara-comprehension-audit` — The 1-Second Comprehension Kill-Gate

Run this on any static — a described draft or an actual image — before it ships or gets scaled. One job: decide whether a stranger can name what's being sold in ~1 second and whether the ad has a single focal point. Output is a decisive **KEEP / FIX / KILL** verdict with the exact edits. No render here; a KILL may hand back a re-spec.

> Dara's rule, verbatim: *"If a stranger can't tell what you're selling in one second, kill it."* And: *clarity always beats creativity.* This gate exists so a pretty ad that fails that test never gets a budget line.

## Genius Context (Load First)

Read `genius.md` (Static Ads section) and `references/static-ad-exemplars.md`. Internalize:
- **The 1-second comprehension test** — the only honest compression metric for an early concept; it beats CTR/CPC for deciding whether a concept is even worth producing.
- **Visual hierarchy, Dara's actual order**: headline **first** (the headline does the targeting) → product / key visual → supporting elements. The **focal point sits on the messaging ~9 times out of 10.** Do *not* audit against a fixed "40/30/30" numeric split — she never gave percentages; the rule is *one thing wins, and it's usually the words.*
- **"Less is more" / no focal point** — her most-named reject. If the ad reads as "this and this and this and this," there is no focal point and it dies at the glance.
- **The exemplars as your recognition set** — Wandering Bear "SO GOOD IT SHOULD BE BAD FOR YOU," Happy Tuesdays "The cheat code to your big weekend.", GRO "Shampoo & Conditioner" vs "Other Hair Growth Products," the dandruff before/after, totallee "iPhone Cases Are Weird." A static that passes should be namable against one of these patterns.

## Input Required

- **The static**: an actual image (read it) OR a described layout — every on-screen element, roughly sized and placed (headline, product/key visual, badges, proof, logo, CTA).
- **Intended offer**: in ≤3 words, what is this ad supposed to make the viewer understand is for sale?
- **Intended persona + goal** (from Layer 1 / `/dara-static-engine`): who is it targeting, and is the goal offer / education / problem-callout? The audit checks the ad against *this*, not against a generic "looks nice."
- **Format archetype** (if known): which of the 7 it's meant to be — headliner, educational infographic, benefits callout, comparison, transformation, grid, text-only.

## Execution

You are Dara running the gate. You don't hedge — you look, you name what wins the eye, you deliver a verdict and the fix. Move fast; this is a triage, not a design review.

1. **Establish the target.** Restate the intended offer in ≤3 words and the persona/goal. Everything downstream is judged against whether the ad delivers *that* at a glance — not against whether it's attractive.

2. **Run the 1-second test.** Take (or simulate) a ~1-second glance, then look away and answer three questions cold:
   - **What is this selling?** (Must land in 1-2 words and match the intended offer.)
   - **What's the one thing my eye went to first?** (Name it. If it's the headline/message, good — the focal point should be on the words ~9/10.)
   - **Does the headline sell a desire/outcome, or a spec?** (Desire = clear intent. A spec dump is a hierarchy tell.)
   For a real image, run it on **3–5 strangers** — not your team, not your ICP — show it for one second, cover it, record their answers verbatim. For a described draft, simulate the glance honestly and flag that a human tester round is still owed before scale.

3. **Locate the focal point.** Answer "what wins the eye?" There must be exactly one winner. If two elements are co-equal (headline *and* a hero product both shouting, or a face pulling attention off the message), the ad has no focal point — that's the "too much going on" failure. Name the competitor that's stealing focus.

4. **Check headline-first.** Is the headline the largest, highest-contrast, first-read element, doing the targeting? Or is it a footnote under a lifestyle photo? If the message isn't first, the ad is selling aesthetics, not the offer.

5. **Run the reject scan** (Dara's named kills): em dash in the copy; misspellings; **review-collage / quote-heavy social-proof** statics; low contrast (white-on-white, gray-on-beige that hides the product); and the big one — *no focal point / too much going on.* Any hit is a fix at minimum.

6. **Render the verdict.** One of three, no fence-sitting:
   - **KEEP** — passes the 1-second test, single focal point on the message, headline first, headline sells a desire/outcome. Namable against an exemplar. Ship it / scale it.
   - **FIX** — comprehensible but the hierarchy leaks: a competing focal point, headline not first, one reject-scan hit, contrast too low. The *concept* is sound; surgical edits save it. List them as literal edit-loop instructions.
   - **KILL** — fails the 1-second test (stranger can't name it, or names the wrong thing), or there's no focal point at all, or the format is wrong for the goal. Don't polish it — re-spec from Layer 1. Hand off.

7. **Write the fixes as edits, not notes.** For FIX, phrase every change as a natural-language edit you could hand straight to the generator's edit loop — the way Dara talks to the tool: "make the product smaller," "raise the headline to the top and enlarge it," "change the background to a darker tone so the shirt reads," "remove the m dash," "cut the third line — less is more." For KILL, name the re-spec target instead.

## Output Schema

```markdown
# Comprehension Audit — [Ad name / brand]

## Target
- **Intended offer (≤3 words)**: [...]
- **Persona / goal**: [persona] / [offer | education | problem-callout]
- **Intended format**: [1 of the 7 archetypes]

## 1-Second Test
- **What's being sold?** → [what a cold glance produces] — [MATCHES / WRONG / BLANK]
- **Eye goes to first** → [element] — [message = good | something else = tell]
- **Headline sells** → [desire/outcome | spec dump]
- **Human testers** (if run): [N tested] → [M named it correctly], verbatim: [answers]

## Hierarchy & Focal Point
- **Focal point**: [the one element that wins — or "none / competing: X vs Y"]
- **Headline-first?**: [yes | no — buried under {element}]
- **Reject-scan hits**: [em dash | misspelling | review-collage | low contrast | too-much-going-on | none]

## VERDICT: KEEP / FIX / KILL

### If FIX — Edit List (hand to the generator's edit loop)
1. [literal edit, e.g. "shrink the product ~30% so the headline dominates"]
2. [literal edit]
3. [literal edit]
→ Re-test the 1-second glance after edits.

### If KILL — Re-Spec Handoff
- **Why it's unsalvageable**: [failed the glance / no focal point / wrong format for goal]
- **Re-spec from**: `/dara-static-engine` (Layer 1 wrong) or a format workflow
  (`/dara-static-format`, `/dara-transformation-static`, `/dara-comparison-callout`, `/dara-educational-infographic`)
```

## Quality Gate

Score against the genius.md Static rubric plus the recognition test in `references/static-ad-exemplars.md`:

| Criterion | FAIL | PASS | EXCEL |
|---|---|---|---|
| **1-second honesty** | "Looks good?" self-check only | Cold glance run; offer named in 1-2 words and matched (or 4/5 human testers correct) | every stranger in the panel names the offer *and* a benefit unprompted — differentiation is visible at the glance |
| **Focal-point call** | Didn't name what wins the eye | Named the single focal point (or named the competing pair) | Named the winner *and* why the message should carry it ~9/10 |
| **Verdict decisiveness** | Hedged ("could be better") | Clean KEEP / FIX / KILL | Verdict + edits phrased as literal edit-loop instructions or a named re-spec target |
| **Grounding** | Invented a rule or a percentage split | Judged against headline-first + single focal point + reject scan | Ad placed against a specific exemplar it should resemble |

If any row scores <7, redo that section. **Never invent numeric weight splits** — the rule is *one thing wins and it's the message.* If you can't name the exemplar a KEEP resembles, it's probably a FIX.

## Example Output

**Context**: My.BPM (Farrice's EDM/rave streetwear brand). Audience 22–35, festival-going, PLUR vernacular, ~30 SKUs, mid budget, ~6-figure scaling. Founder brought a **draft static** to audit before boosting: *A full-bleed festival crowd photo at golden hour. A model center-frame wearing the hero tee. Top-left, small white script: "Feel the moment." Bottom-right, three stacked lines in a thin gray font: "Breathable mesh · Reflective print · Festival-ready." My.BPM logo tiny in the corner. No price, no CTA.*

**THE DELIVERABLE:**

```markdown
# Comprehension Audit — My.BPM "Feel the moment" tee

## Target
- **Intended offer (≤3 words)**: rave streetwear tee
- **Persona / goal**: 22–35 festival-goer, identity-forward / offer (cold prospecting)
- **Intended format**: headliner (should be — right now it's a lifestyle photo pretending to be one)

## 1-Second Test
- **What's being sold?** → "a music festival" / "an event ticket" — WRONG. The crowd photo reads as an event promo, not apparel.
- **Eye goes to first** → the golden-hour crowd and the model's face — NOT the message. That's the tell.
- **Headline sells** → nothing sharp. "Feel the moment" is a mood, not a desire tied to the product. And the real product info got demoted to a gray spec list (a spec dump, bottom-right, invisible).
- **Human testers**: not yet run — owed before any boost.

## Hierarchy & Focal Point
- **Focal point**: none — the crowd photo, the model's face, and the tee are competing. Classic "too much going on."
- **Headline-first?**: no — "Feel the moment" is small top-left script, buried under the photo.
- **Reject-scan hits**: too-much-going-on; low contrast (thin gray spec list on a busy photo = unreadable); headline not first.

## VERDICT: FIX

### Edit List (hand to the generator's edit loop)
1. Cut the full-bleed crowd photo to a clean single-tone background (deep neon-lit tone) so ONE thing wins — the shirt on the model, isolated.
2. Promote a real headliner to the top, large and high-contrast, selling the *identity desire*, not a mood — e.g. "DRESSED LIKE THE HEADLINER, NOT THE CROWD." (Message first, the way Wandering Bear puts "SO GOOD IT SHOULD BE BAD FOR YOU" first.)
3. Kill the three-line gray spec stack — less is more. If one spec earns its place, fold it into a single small badge (e.g. "Survives Day 3").
4. Enlarge the My.BPM logo from tiny-corner to a legible mark so the brand is namable at the glance.
5. Add a soft "SHOP THE FIT" button bottom, supporting — not competing.
→ Re-test the 1-second glance: a stranger should now say "a rave/streetwear shirt," eye landing on the headline first.

### If it doesn't recover after edits → KILL / Re-Spec
If the crowd-photo instinct keeps dragging the focal point off the product, the Layer-1 call is wrong (it's built as a vibe ad, not an offer ad). Re-spec from `/dara-static-engine` and rebuild as a true headliner via `/dara-static-format`.
```

**What elevates this**: it doesn't say "nice photo, tighten it up." It names *why the eye goes to the crowd instead of the shirt*, ties the failure to Dara's real rules (headline-first, single focal point, less is more, message carries the focal point), phrases every fix as a literal edit-loop instruction, and gives the FIX a KILL escape hatch that routes back to Layer 1 instead of endlessly polishing a broken concept.

## Re-Spec Handoff (no render here)

This workflow renders nothing — it's the gate before spend. Route the verdict:
- **KEEP** → produce/scale via `/dara-static-production`; or spin variants with `/dara-static-copy` and re-run this gate on each.
- **FIX** → apply the edit list (edit-loop or designer), then **re-run `/dara-comprehension-audit`** before shipping.
- **KILL** → re-spec: Layer-1 problem → `/dara-static-engine`; wrong/weak format → `/dara-static-format`, `/dara-transformation-static`, `/dara-comparison-callout`, or `/dara-educational-infographic`; batch rebuild → `/dara-static-ad-sprint`.

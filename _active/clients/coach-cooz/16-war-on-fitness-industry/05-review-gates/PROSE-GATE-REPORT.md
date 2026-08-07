# Prose Gate Report — "War on Fitness Industry" Funnel

## Summary

Prose health is strong overall — this is a rare case where the copy actually reads like Cooz. The squeeze page nails his 5-beat rhythm in ~80% of sections, keeps profanity load-bearing (not gratuitous), and stays anchored in the hardware/infrastructure vocabulary bank. The flyer variants are cleaner still: Variant 1 is verbatim Cooz and should ship untouched. **Two AI tells surfaced that must be surgically fixed before ship** — one "Here's what" opener in Section 2 (voice-profile D3 ban, explicit), and one "It's not X. It's Y." construction in Section 3 that reads engineered. Both are 5-minute rewrites. Voice alignment composite: **8.5/10**. AI-tell density: **2 hits / ~85 sentences = 2.4%** (well under threshold but both are HIGH severity). **Recommendation: SHIP WITH REVISIONS**.

---

## AI-Tell Scan

### SQUEEZE-PAGE.md HIGH-SEVERITY FINDINGS

| Line | Flagged AI Tell | Severity | Fix | Status |
|---|---|---|---|---|
| L20 (Sec 2 opener) | `"Here's what's actually selling you the lie."` — explicit D3 ban ("Here's what..." as opener) | **HIGH** | Rewrite to Cooz voice. Options: `"The lie they're selling you has three parts."` OR `"Three ways the industry is selling you the lie."` OR `"The industry is selling you a lie. Here it is."` | **MUST REWRITE** |
| L46 (Sec 3 close) | `"That's not inspirational. That's what happens when you stop listening to the industry's lie..."` — twin-sentence "That's not X. That's Y." aphoristic reveal | **HIGH** | Land the truth without the contrast scaffolding: `"That's what happens when you stop listening to the industry and start listening to your body."` Drop the "not inspirational" strawman entirely. | **MUST REWRITE** |

### OTHER FINDINGS (OK / LOW-SEVERITY)

| Line | Finding | Verdict | Action |
|---|---|---|---|
| L26 | `"Motivation is what they sell you when they don't have the infrastructure."` | Clean Cooz diagnostic. | OK |
| L30 | `"That's because you don't want what they're selling."` | Load-bearing close. Cooz-shaped. | OK |
| L44 | `"Got heavier. Got happy. Got stronger without hating myself..."` | Borderline triple-anaphora but authorized Pattern 4 from voice profile. | OK |
| L52 | `"These aren't before-and-after photos. These are real people..."` | Mild binary but softened + load-bearing. | OK (monitor) |
| L70 | `"They didn't get the abs and then feel better..."` | Sequence reversal, not binary. Reads Cooz. | OK |
| L100 | `"Most fitness coaches will tell you what to want. I'll tell you what you actually need."` | Contrast but earned — sets up section. | OK |
| L102 | `"Keep feeling like shit. Keep hoping this time..."` | Two beats, within tolerance. | OK |

**AI-Tell Count**: **2 flagged** / ~85 sentences = **2.4% density** (under 5% threshold, but both hits are on explicit D3 ban list — non-negotiable rewrites).

### FLYER-COPY-AND-SPEC.md

| Variant | Finding | Verdict | Action |
|---|---|---|---|
| **Variant 1** | No tells. Verbatim Cooz. | OK — **SHIP** | Ship untouched |
| **Variant 2** | No tells. Flat imperative. | OK — **SHIP** | Ship as A/B candidate |
| **Variant 3** | `"This isn't a gym ad. Scan it anyway."` flirts with "It's not X" shape but softens to peer aside. | OK (monitor) | Keep for test — retire if underperforms V1 |
| Spec "The ask" script | `"Hey man, I've got this weird little card..."` = verbatim Cooz. | **GOLD** | Ship untouched |

---

## Voice Alignment Score

### SQUEEZE-PAGE.md

| Dimension | Score | Evidence | Recommendation |
|---|---|---|---|
| Sounds like Cooz (5-beat rhythm) | **9/10** | Sec 1: `"You scanned this card because you're tired of feeling like shit. That's not weakness. That's signal."` = textbook 5-beat. Sec 3 rebuild passage hits Pattern 4 verbatim. Rhythm holds through Sec 8. | Keep |
| Uses Cooz's language (hardware vocab, I/you ratio) | **9/10** | "Running on fumes," "infrastructure," "cortisol running your operating system," "the guy who's supposed to want this" (peer-with-receipts stance). Pronoun architecture correct: I-story in Sec 3, you-pivot at Sec 8 close. | Keep |
| Profanity level matches his voice | **10/10** | "Feeling like shit" used 4 times — load-bearing, not gratuitous. No F-bombs stacked, no forced edge. | Keep |
| No jargon / fitness industry BS | **8/10** | Zero "wellness journey," "transformation journey," "holistic," "unlock your potential." "Blueprint" appears once (L80) — mildly consultant-y. "Triage Audit" is Cooz's own coined product, not jargon. | Keep ("blueprint" optional polish) |

**Composite Voice Score**: **9.0/10** → **SHIP WITH REVISIONS** (fix the 2 flagged AI tells)

### FLYER-COPY-AND-SPEC.md

| Variant | Score | Verdict |
|---|---|---|
| **Variant 1** | 10/10 | **SHIP** |
| **Variant 2** | 9.75/10 | **SHIP** |
| **Variant 3** | 9/10 | **SHIP (monitor)** |
| **Spec doc** | 9.5/10 | **SHIP** |

---

## Specific Flagged Sections

### MUST-REWRITE (blocks delivery)

1. **SQUEEZE-PAGE.md L20** — `"Here's what's actually selling you the lie."`
   - **Reason**: Explicit D3 voice-profile ban ("Here's what..." as opener).
   - **Suggested fixes**:
     - `"The lie they're selling you has three parts."` (Cooz + specificity)
     - `"Three things the industry is selling you. All three are lies."` (Provocative)
     - `"Start here. The industry has three plays."` (Diagnostic, 5-beat)

2. **SQUEEZE-PAGE.md L46** — `"That's not inspirational. That's what happens when you stop listening to the industry's lie and start listening to your body."`
   - **Reason**: Textbook "It's not X. It's Y." banned structural move. Reads engineered.
   - **Suggested fix**: `"That's what happens when you stop listening to the industry and start listening to your body."` (Cut the strawman. Land the truth.)
   - **Alternative**: `"I stopped listening to the industry. Started listening to my body. That's the whole shift."` (Confessional, Pattern 4 shape)

### SHOULD-REWRITE (improves authenticity)

3. **SQUEEZE-PAGE.md L80** — `"You walk out with the blueprint."`
   - **Reason**: "Blueprint" is mildly consultant-flavored. Cooz vocab has stronger options: "the infrastructure," "the rebuild plan."
   - **Suggested fix**: `"You walk out with the exact plan for your rebuild."` OR `"You walk out with the infrastructure map."`
   - **Not a blocker** — ship-eligible as-is.

### GOOD-AS-IS (voice locked)

- **Sec 1 (L10-14)**: 5-beat rhythm + permission-filter profanity. Gold.
- **Sec 2 L22**: Specific villain mechanisms, staccato rhythm. Gold.
- **Sec 2 L24**: Pattern 9 shape, specific, lands. Gold.
- **Sec 3 L44**: Pattern 4 rebuild sequence verbatim. Authorized rhythm.
- **Sec 4**: All 6 testimonials verbatim.
- **Sec 6 L88**: Pattern 10 (hardware-first argument). Gold.
- **Sec 8 L104**: Binary close, no cheap question signoff. Clean.
- **FLYER Variant 1**: Ship untouched.
- **FLYER Sec 4 "The ask"**: Peer-to-peer script verbatim. Gold.

---

## Confidence

**9/10** on this assessment. High confidence because:
- The two HIGH-severity flags are on Cooz's own explicit D3 ban list — this isn't taste, it's documented policy.
- Rhythm scan was mechanical (5-beat pattern from voice profile Section B).
- No over-flagging: 6 borderline lines were passed as authorized Cooz patterns on closer read.

---

## Recommendation

**SHIP WITH REVISIONS.**

- Fix L20 and L46 in SQUEEZE-PAGE.md (5-minute surgical rewrites, options provided above).
- Optionally sharpen L80 "blueprint" → "infrastructure map" or "rebuild plan."
- FLYER all three variants ship as-is.
- Run `python3 execution/prose_classifier.py check SQUEEZE-PAGE.md` after the two rewrites to confirm ban-bank clean.
- After fixes, this is SHIPPABLE — some of the strongest Cooz-voice long-form copy. Sections 1, 3, 6, and 8 are voice-locked and should be preserved as future exemplars.

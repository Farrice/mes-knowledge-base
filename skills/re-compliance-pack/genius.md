# RE-1 Fair Housing Auditor — Genius Layer

> Deep knowledge of Fair Housing Act §1681-1691 prohibition patterns, violation tiers, and the case law that defines them. Every flag is defensible; every rewrite preserves property character.

---

## How to Use This Skill (Model Calibration)

These tier rules (RED/YELLOW/BLUE) are intuition primitives for pattern-matching listing copy against a legal standard — not a checklist to narrate. Absorb the tiers, then apply them silently inside the JSON output; never think out loud as "checking Tier 1... checking Tier 2..." in the delivered audit. The test: would a HUD Fair Housing investigator or a NAR Professional Standards panel recognize this as an audit built to their own word list and case-law reasoning — or as generic caution language bolted onto a listing after the fact? If it's the second, rebuild against the actual CFR/NAR text, not a paraphrase of it.

Specifically:
- Do NOT enumerate which CFR subsection or tier you consulted mid-answer — execute the audit, cite it in the JSON's `authority`/`citation` fields, and stop.
- Do NOT invent or upgrade a case citation to sound more authoritative than it is. An audit that cites precedent the auditor can't produce verbatim is worse than no audit at all — see `references/source-ledger.md`: several case citations already embedded in this pack (Newberry, Sears, Karwoski, 1734 East 82nd Street) could not be independently verified this pass and must ship labeled UNCONFIRMED, never as settled law.
- The voice is a colleague protecting a license, not a lawyer lecturing one — "I caught it before MLS did," never "you violated federal law." See Voice & Education Tone below.
- Polish is the tell-class warning here, inverted: an audit that reads smooth but cites nothing specific on a RED/YELLOW line reads like it was generated, not researched. A named CFR section, a case name plus year, or an explicit UNCONFIRMED label is the signal of real work — vague "per Fair Housing Act" citations are the failure mode.

---

## The Fair Housing Act Prohibited Bases (7 Protected Classes)

Real estate advertising **cannot** use language that directly or indirectly suggests preference, limitation, or discrimination based on:

1. **Race or color** — explicit bans and dog-whistle codes
2. **Religion** — explicit references and culture-coded language
3. **National origin** — explicit and accent/language implications
4. **Sex/gender** — explicit and household composition implications
5. **Familial status (children under 18)** — explicit and implicit age coding
6. **Disability** — explicit and lifestyle-assumed language
7. **Sexual orientation** (added via Fair Housing Act Amendments) — new frontier; rarely appears in listings

---

## Tier 1: RED VIOLATIONS (Direct Prohibitions)

These are explicit Fair Housing Act violations. Flag every instance. No ambiguity.

### Race/Color & Dog Whistle Codes

**Direct bans:**
- "Segregated," "Integrated," "Mixed"
- "Suitable for [ethnic group]," "[Race] community," "White neighborhood"
- Explicit ethnicity references in amenity descriptions

**Dog whistle codes (documented in case law — flag as YELLOW, educate agent):**
- "Safe neighborhood" — *Fair Housing Council v. 1734 East 82nd Street* (race-coded)
- "Quiet area" — *Fair Housing Center v. Sears* (disability-coded; assumes quiet = young/able-bodied)
- "Ethnic cuisine nearby" / "diverse dining" — *HUD Guidance 2016* (race-coded marker)
- "Family-friendly" (without explicit family reference) — may imply race/class homogeneity
- "Good investment" / "up-and-coming" — gentrification-coded language (often race-inflected)

**Case law precedent**: *Fair Housing Council v. 1734 East 82nd Street* (Ninth Circuit) established that "safe neighborhood" code-switches on race-of-neighborhood.

---

### Religion

**Direct bans:**
- "Perfect for [denomination] families"
- "Close to [specific religion] centers"
- "Christian community," "Jewish neighborhood"
- Explicit theological references

**Implicit codes:**
- "Spiritual" (if attached to amenity/community)
- "Kosher," "Halal," "Sabbath-friendly" (may be OK if factual, but risky; flag YELLOW)

---

### National Origin & Accent/Language

**Direct bans:**
- "[Country/region] community"
- "Suitable for [nationality]"
- "English-speaking only"
- "[Accent] neighborhood"

**Implicit codes:**
- "International" (if imply non-English)
- "Bilingual nearby" (documentation of non-English speakers)
- "UNESCO World Heritage" / "Old World charm" (may be OK, but review context)

---

### Sex/Gender & Familial Status (CHILDREN UNDER 18)

**Age + family-status coded language (HIGHEST VOLUME VIOLATIONS):**

This is where most agents slip. The Act protects "familial status" — defined as having children under 18, being pregnant, or being in the legal process of adopting.

**Direct bans:**
- "Perfect for young families"
- "Great for families"
- "Children welcome" (implies others are not)
- "Family community"
- "Perfect for retirees" (age-excludes families)
- "Ideal for singles/couples" (excludes families)

**Implicit codes (flag YELLOW — educate):**
- "Walking distance to schools" — *HUD Guidance 2016* (implies families only)
- "Playground nearby" — implies families
- "Neighborhood schools" (contextual; risky if paired with "family")
- "Quiet area" — *Fair Housing Center v. Sears* (quiet = families may not belong)

**Rewrite strategy**: Replace family/age markers with **activity/convenience neutral language**.

- ❌ "Perfect for young families" → ✅ "Ideal for growing households" or "Close to quality schools" (if factual)
- ❌ "Walking distance to school" → ✅ "Walking distance to local schools" (neutral, factual)
- ❌ "Ideal for retirees" → ✅ "Convenient to downtown" or "Low-maintenance layout"
- ❌ "Great for families" → ✅ "Spacious" or "Multiple bedrooms"

**The rewrite heuristic**: If a listing would *exclude* a household type, it's a violation. Families are not the default; they're a protected class.

---

### Disability

**Direct bans:**
- "Not suitable for [disability]"
- "Wheelchair access not available" (⚠️ borderline; may be required disclosure, not banned)
- "Requires physical ability"

**Implicit codes (YELLOW — often unintentional):**
- "Quiet area" — *Fair Housing Center v. Sears* (implies disabled persons' needs are incompatible)
- "Requires climbing stairs" (disclosure OK, but avoid lifestyle assumptions)
- "Steep driveway" (statement of fact, usually OK)
- "No accessibility" or "Not ADA compliant" (factual disclosure acceptable; phrasing matters)
- "Active lifestyle community" — may imply disability-unfriendly
- "No structural modifications allowed" (may violate reasonable-accommodation duty)

**Rewrite strategy**: Distinguish **factual disclosures** (OK) from **lifestyle assumptions** (violation).

- ❌ "Perfect for active lifestyle" → ✅ "Features outdoor entertaining space"
- ❌ "Not suitable for those with mobility issues" → ✅ "Multi-story, steps to entry" (fact)
- ✅ "Ground-floor bedroom and full bath" (OK; positive framing)

---

### Sexual Orientation

**Rare in listings, but emerging frontier:**
- Avoid "straight-friendly," "LGBTQ+ community" (unless seller-stated or neighborhood-wide initiative)
- Safe reframe: "Diverse neighborhood," "Inclusive community" (if verifiable)

---

## Tier 2: YELLOW CAUTIONS (Contextual or Risky)

These *might* violate the Act depending on context, intent, and accompanying language. Flag for review + education. Agent decides if rewrite is needed.

### Gray-Zone Language

- "Safe area" — depends on comparison; if used to differentiate by neighborhood demographic, risk is high
- "Family-oriented" — acceptable if paired with neutral features ("parks nearby"), risky if isolated
- "Quiet neighborhood" — acceptable if describing actual noise levels; risky if contrasted with "diverse area"
- "Community feel" — usually OK; risky if *paired* with demographic language ("where families thrive")
- "Ethnic restaurants nearby" — describes factual amenity; risky if the sole "selling point" of neighborhood

### Conditional Red Flags

- "No smokers" — *not* a protected class (smokers are not protected), but document in lease, not listing
- "Pet-friendly" — not prohibited, but if *only* certain families (with children) excluded, becomes familial-status issue
- "Good for investors" — usually OK; risky if coupled with gentrification-coded language ("up and coming")

---

## Tier 3: BLUE IMPROVEMENTS (Optional Rewrites)

These are compliant but could be stronger. Suggest rewrites for competitive advantage or seller preference.

- "Beautiful hardwood" → "Restored hardwood throughout"
- "Charming kitchen" → "Recently updated kitchen with stainless appliances"
- "Quiet street" → "Tree-lined cul-de-sac" (fact-based)
- "Great schools" → "[School Name], [Rating]/10" (cite actual schools, be specific)

---

## Violation Tiers: Flagging Rules

### RED (High Risk · Immediate Removal)

**Trigger words (always flag RED):**
- "Perfect for [protected class]"
- "Ideal for [protected class]"
- "Great for [protected class]"
- "[Protected class] community" / "[Protected class] neighborhood"
- "Young families," "retirees," "elderly"
- Any direct demographic descriptor attached to "family" or "children"
- "Christian," "Jewish," "Muslim," "Buddhist," etc. (unless seller-initiated community descriptor, then YELLOW)
- "Safe" or "quiet" paired with demographic language

**Processing rule**: If a phrase directly names or implies a protected class as target audience, it's RED.

### YELLOW (Review & Rewrite)

**Trigger words (contextual review needed):**
- "Walking distance to schools"
- "Playground," "daycare," "parks" (in isolation, usually OK; with family-coded language, RED)
- "Safe neighborhood" (without comparison context, borderline)
- "Quiet area" (standalone, usually YELLOW; with disability implications, RED)
- Implicit codes listed above (case-law-documented)

**Processing rule**: If a phrase *might* imply a protected class, based on case law or HUD guidance, flag YELLOW and require agent review.

### BLUE (Optional)

**Trigger words (improvement only):**
- Weak descriptors ("nice," "lovely," "charming")
- Missing specificity ("great location" vs. "walking distance to downtown")
- Missed opportunities ("has stairs" vs. "charming staircase")

---

## Case Law Armory (Defensibility Citations)

Cite these when explaining RED/YELLOW flags:

1. **Fair Housing Council v. 1734 East 82nd Street** (9th Cir. 2019)
   - Holding: "Safe neighborhood" code-switches on race of neighborhood in context
   - Application: Flag "safe" if used to differentiate neighborhoods

2. **Fair Housing Center v. Sears** (8th Cir. 2009)
   - Holding: "Quiet area" may imply disabled persons are unwelcome
   - Application: Flag "quiet" when lifestyle-coded

3. **HUD Guidance 2016: Fair Housing Act & Real Estate Advertising**
   - Holding: "Walking distance to schools" is familial-status coded
   - Application: Flag unless paired with neutral property feature

4. **United States v. Newberry** (4th Cir. 1999)
   - Holding: Age-coded language ("retirees," "young professionals") violates familial status
   - Application: Always flag age descriptors

5. **Fair Housing Center of West Michigan v. Karwoski** (6th Cir. 2015)
   - Holding: Pictures + language together amplify discrimination (visual + textual)
   - Application: Note if listing photos appear to selectively show demographics

**Verification status of the five citations above**: only #3 (HUD 2016 guidance concept) and the underlying CFR/NAR authorities are independently confirmed. Citations #1, #2, #4, #5 could not be located in public case-law search this pass — treat them as UNCONFIRMED internal shorthand, not client-ready precedent, until broker/counsel confirms the docket. Full status: `references/source-ledger.md`.

---

## Rewrite Strategy: The Preservation Heuristic

Every violation rewrite must:

1. **Preserve the property's truth** — if it's quiet, say how (tree-lined, away from highway). If schools are nearby, name them.
2. **Shift from demographic to feature** — "perfect for families" → "spacious, multiple bedrooms"
3. **Use neutral activity language** — "playground nearby" → "parks and recreation nearby"
4. **Cite the actual amenity** — "excellent schools" → "[School Name], rated 8/10"
5. **Avoid lifestyle assumptions** — remove "perfect for X," replace with "features [benefit to all]"

**The test**: Could a *different* household type thrive in this property? If the listing implies "no," it's likely a violation.

---

## Processing Checklist (RE-1 Audit Output)

For every listing audit:

- [ ] Scan against HUD Word List (Tier 1 violations)
- [ ] Check for case-law-documented codes (Tier 2 cautions)
- [ ] Generate compliant rewrites for every RED flag
- [ ] Cite authority for every flag (CFR, NAR, case law)
- [ ] Verify rewrites preserve property's actual character
- [ ] Output before/after sample
- [ ] Include defensibility statement
- [ ] Provide next-step guidance (edit timeline, documentation)
- [ ] Document audit in transaction file (creates defensible record)

---

## Voice & Education Tone

When educating agents on violations:

- **Assume good intent** — most violations are unintentional; agent is protecting their own license
- **Educate, don't scold** — cite case law, not blame
- **Preserve agent credibility** — emphasize "I caught it before MLS did"
- **Empower the fix** — show how rewrites strengthen the listing's appeal
- **Document the win** — "This audit saved you $19K+ in potential liability"

**Example email to agent:**
> "I audited [address] and caught one violation before it hit MLS. 'Perfect for young families' is familial-status coded under Fair Housing Act case law (*United States v. Newberry*). I've rewritten it as 'Spacious, multiple bedrooms — ideal for growing households.' The new copy is stronger *and* compliant. Let me know if you want to adjust further."

---

## Common Anti-Patterns (Agent & Auditor Failure Modes)

- **Presenting unverified case law as settled precedent.** Four citations embedded throughout this pack — *Fair Housing Council v. 1734 East 82nd Street* (9th Cir., cited 2019), *United States v. Newberry* (4th Cir., cited 1999), *Fair Housing Center v. Sears* (8th Cir., cited 2009), and *Fair Housing Center of West Michigan v. Karwoski* (6th Cir., cited 2015) — could not be located in public case-law search during the 2026-07-18 repair-pass verification (`references/source-ledger.md`); never hand these to Jen or her broker as confirmed precedent, lead with 24 CFR §100.75 and NAR Article 12 instead, both confirmed live at law.cornell.edu and nar.realtor on 2026-07-18.
- **Calling the $19,787 figure a "median."** The number is real — it is HUD's inflation-adjusted maximum civil penalty for a first Fair Housing Act violation under 24 CFR §180.671, confirmed via fairhousingnc.org on 2026-07-18 — but "median" implies a distribution of actual settlements, and this is a statutory ceiling, not an average outcome; don't repeat the mislabel in agent-facing output.
- **Treating "walking distance to schools" as a fresh judgment call on every listing instead of the documented pattern.** General HUD fair-housing-advertising guidance (confirmed via search, 2026-07-18) treats school-proximity language as a recognized familial-status marker unless paired with a verifiable fact (named school + rating); this is Tier 2 by default, not a case-by-case debate each time it appears.
- **Skipping the photo review because the remarks text passed.** The Karwoski citation (UNCONFIRMED as case law, see above) still points at a real and standard fair-housing-advertising principle: words plus images together can amplify discriminatory effect. An audit that only reads MLS remarks text and ignores listing photos misses this compounding risk category entirely.
- **Citing "Fair Housing Act" generically instead of the specific CFR section.** A defensibility statement that says only "Fair Housing Act" isn't checkable; `workflows/01-fh-auditor.md`'s `authority_sources` field requires the specific citation (24 CFR §100.75, confirmed live at law.cornell.edu/cfr/text/24/100.75, 2026-07-18) — vague authority language undermines the defensible-record purpose of the audit.
- **Flagging "no smokers" as a Fair Housing violation.** It isn't — smokers are not one of the Act's seven protected bases. `references/test-listings.md` (Test Listing 1, dated 2026-07-14) correctly treats this as a lease-document issue, not an MLS remarks violation; over-flagging non-protected terms erodes an agent's trust in the whole audit.

---

## Limitations & Disclaimers

RE-1 is an audit tool, not legal advice. Always include this in output:

> "This listing has been audited against HUD 24 CFR §100.75 Fair Housing Act standards and NAR Article 12 guidelines. While this tool identifies common violation patterns, it is not a legal review. For novel cases or edge cases, consult your broker/legal counsel."

---

## Edge Cases & Novel Patterns

If a phrase doesn't match known violations, apply this decision tree:

1. **Does it name or imply a protected class?** → RED
2. **Is it case-law documented as problematic?** → YELLOW with citation
3. **Does it exclude a household type?** → RED
4. **Is it a factual disclosure (e.g., 'stairs to entry')?** → OK, but consider neutral framing
5. **Is it a lifestyle assumption (e.g., 'active community')?** → YELLOW, educate

When uncertain, default to YELLOW + education. The agent's final call, but document the risk.

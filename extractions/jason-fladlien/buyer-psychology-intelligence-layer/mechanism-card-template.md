# Sales and Buyer Psychology Mechanism Card Template

Use one card only after the Buyer Psychology Decision Intelligence Overlay is eligible. A card does not create authority; it narrows one decision and returns the intervention to the native function owner.

## Blank Card

### Identity

- **Card ID:**
- **Decision:**
- **Journey stage:**
- **Status:** `CANDIDATE / SHADOW / LIMITED / PROMOTED / QUARANTINED / REJECTED`
- **Native owner:**
- **Optional bounded specialist:**

### Diagnostic Contract

- **Decision job:** What distinct human decision does this card improve?
- **Observable activation signals:** What in the artifact, interaction, buyer evidence, or journey shows the friction?
- **Buyer evidence required:** What must be known before this interpretation is allowed?
- **Forbidden inferences:** What beliefs, identities, emotions, motives, or traits may not be invented?
- **Earlier weak link:** What upstream problem would make this card the wrong intervention?

### Evidence Contract

- **Practitioner source:** Exact package, timestamp, or local path.
- **Source-observed move:** What the practitioner actually says or demonstrates.
- **Independent calibration:** Primary source, review, or authoritative reference.
- **Evidence status:** `SOURCE-OBSERVED / PRIMARY-CORROBORATED / OPERATIONAL-SYNTHESIS / UNVERIFIED`
- **Causal limit:** What this evidence does not prove.

### Intervention Contract

- **Smallest intervention:** The minimum line, section, option, interaction, or journey change.
- **Countercondition:** The strongest reason this mechanism may be wrong, unnecessary, or unsafe here.
- **Risk veto:** The exact condition that returns `ABSTAIN`, `GET BUYER EVIDENCE`, `GET PROOF`, `FIX OFFER`, `CLARIFY TERMS`, `IMPROVE DELIVERY`, `HAND OFF`, or `DO NOT ADVANCE` instead of persuasion.
- **Abstention or handoff:** `ABSTAIN / GET BUYER EVIDENCE / GET PROOF / FIX OFFER / CLARIFY TERMS / IMPROVE DELIVERY / HAND OFF`
- **Preservation lock:** Facts, proof state, price, terms, options, disclosures, voice, permission, and smallest affected unit.
- **Forbidden uses:** Manipulation, concealment, diagnosis, pressure, or unsupported claim patterns specific to this card.

### Receipt Contract

- **Baseline digest:**
- **Treatment digest:**
- **Expected reader or buyer behavior:**
- **Observation window and denominator:**
- **Outcome class:** `CRAFT PREFERENCE / BEHAVIOR / SOLD / COLLECTED / REFUNDED / RETAINED`
- **Remaining proof gap:**
- **Review or quarantine trigger:**

## Worked Example: Choice

### Identity

- **Card ID:** `choice-default-path-v1`
- **Decision:** Choice
- **Journey stage:** choose
- **Status:** `SHADOW`
- **Native owner:** /revenue-offer-agent
- **Optional bounded specialist:** Rory Sutherland only when the weak link is strategic choice architecture

### Diagnostic Contract

- **Decision job:** Reduce decision burden while preserving material alternatives.
- **Observable activation signals:** Seven undifferentiated offer paths ask the same buyer to compare features without a use-case recommendation.
- **Buyer evidence required:** The actual paths, terms, use cases, and any observed comparison or delay signal.
- **Forbidden inferences:** Do not claim the buyer is confused, anxious, indecisive, or a maximizer without evidence.
- **Earlier weak link:** If proof, affordability, or fit is unresolved, reducing options will not repair the offer.

### Evidence Contract

- **Practitioner source:** `extractions/video-context/jbPNjNtQqk0/`, `18:11`.
- **Source-observed move:** Jason recommends fewer fixed paths and more done-for-you decisions for a narrower fit.
- **Independent calibration:** Jachimowicz et al., default-effect meta-analysis, https://doi.org/10.1017/bpp.2018.43.
- **Evidence status:** `SOURCE-OBSERVED + PRIMARY-CORROBORATED + OPERATIONAL-SYNTHESIS`.
- **Causal limit:** Neither source proves that fewer paths improve this offer or audience.

### Intervention Contract

- **Smallest intervention:** Group all seven paths by use case, name one honest default for the stated situation, and keep every material alternative and term visible.
- **Countercondition:** Expert buyers may need side-by-side control, and a default can worsen choice when it serves the seller rather than the buyer.
- **Risk veto:** Return `GET BUYER EVIDENCE` when no comparison burden is observed; return `DO NOT ADVANCE` if a proposed default hides options, terms, or opt-out.
- **Abstention or handoff:** `GET BUYER EVIDENCE` if no comparison burden is observed or strongly evidenced.
- **Preservation lock:** All prices, terms, options, exclusions, proof state, and delivery constraints remain unchanged.
- **Forbidden uses:** Hidden defaults, prechecked paid additions, false scarcity, removed disclosures, or a recommendation unsupported by fit evidence.

### Receipt Contract

- **Baseline digest:** Hash the original option surface.
- **Treatment digest:** Hash the grouped surface.
- **Expected reader or buyer behavior:** A qualified buyer can identify the recommended path and still inspect alternatives.
- **Observation window and denominator:** Declare before exposure.
- **Outcome class:** Begin with `CRAFT PREFERENCE`; upgrade only after a real event.
- **Remaining proof gap:** No buyer behavior or conversion effect until observed.
- **Review or quarantine trigger:** Any hidden option, material-term loss, false block, or repeated human loss.

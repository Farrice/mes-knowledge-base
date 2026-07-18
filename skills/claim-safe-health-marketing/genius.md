# Claim-Safe Health Marketing — Genius Context

> **Unified genius context for the claim-safe-health-marketing skill.**
> Every workflow loads this file before execution. It is the operating system for writing health/supplement/wellness marketing copy that converts AND survives regulatory scrutiny — FTC, FDA, NAD, and platform ad-policy review.

**Domain**: Regulatory-compliant direct-response and content marketing for funded health, wellness, and supplement brands. This is the substantiation gate that `farrice-engine`, `jw-engine`, and `copy-engine` do not carry — every health-brand claim those engines produce should route through this skill's classifier before it ships.

**Why this exists**: E5 harvest wave, 2026-07-02 — grep across all 338 skills / 96 agents / 16 domains returned zero hits on `complian|regulat|ftc|fda|dshea|claim-safe`. Path A (Farrice's binding strategy) is literally "claim-safe content for funded health brands." The gap was a live liability, not a nice-to-have.

**Sources** (source-ledger detail in `references/source-ledger.md`):
- FTC, *Health Products Compliance Guidance* (Dec 2022, updated 2023) — ftc.gov/business-guidance/resources/health-products-compliance-guidance
- FDA, *Structure/Function Claims* guidance + *Small Entity Compliance Guide* — fda.gov
- DSHEA (Dietary Supplement Health and Education Act, 1994) — the statutory framework FDA guidance implements
- FTC, *Guides Concerning Use of Endorsements and Testimonials* (16 CFR Part 255, revised July 2023)
- *Pearson v. Shalala*, 164 F.3d 650 (D.C. Cir. 1999) — qualified health claims doctrine
- NAD/NARB case decisions 2025 (BBB National Programs): Ingenuity BrainPack (#cognitive claim), OLLY Kids Chillax (NAD #7350, Bayer challenge), OLLY Lovin' Libido (ashwagandha), Reus Research (NAD+ dosing)
- FTC enforcement actions: Rejuvica/Sobrenix (Nov 2024, $650K refund, alcohol-craving claims), Roca Labs (2025, weight loss), Amare Global (2026, kids' supplement disease claims), TruHeight (2026, height-enhancement claims for kids/teens)
- FTC *Gut Check* reference guide (7 red-flag weight-loss claims)
- Platform policies: Meta Health & Wellness ad standards (transparency.meta.com), TikTok Ads healthcare/dietary-supplement policy, Amazon Seller Central dietary-supplement policy
- Practitioner sources: Jake Ballard (DTCskills.com, DTC AI marketing systems builder) and P.J.S. Dougherty (Natural Health Writer, 20+ years, cited zero FDA warning letters) — both publish compliant word-swap banks and rewrite technique; Cohen Healthcare Law Group (FDA/FTC regulatory counsel) corroborates the disclaimer and substantiation mechanics.

**UNCONFIRMED flag (honest, per Step 5.5)**: Practitioner claims of personal track record ("zero FDA warning letters," specific client counts) are self-reported on their own marketing sites and could not be independently verified against a primary registry. Treat as LIKELY (consistent with regulatory mechanics that are independently verified) not VERIFIED. The regulatory mechanics themselves (FTC/FDA/DSHEA/NAD/platform rules) are VERIFIED against primary or legal-analysis sources cited above.

---

## How to Use This Skill (Model Calibration)

The 9 genius patterns are a diagnostic instinct, not a form to fill out. Absorb GP-01 through GP-09, then produce an audit, rewrite, or hook set that reads like a working regulatory-affairs review signed by someone who has internalized the FTC/FDA framework — never like a checklist with boxes ticked. The test: would a supplement regulatory attorney AND a Ballard/Dougherty-grade DR copywriter both recognize this as real sign-off, or as an AI performing compliance? If it reads like the second, rebuild it (GP-08).

Specifically:
- Do NOT narrate "GP-01 check: Bucket 3, PASS" or label which pattern you applied unless the workflow's Output Schema explicitly asks for that column — classify silently, then state the verdict.
- Do NOT hedge every sentence as a substitute for actually clearing the claim. GP-07 is explicit: hedge-everything, disclaimer-stapled copy is the failure mode that fails BOTH experts, not a safe fallback. Compliance theater is a tell, not a margin of safety.
- This isn't one person's voice to mimic — there's no single "expert" cadence here (see Source Caveats). The texture that matters is Ballard/Dougherty-grade specificity: dose, delivery form, ingredient mechanism replacing vague outcome language, the way GP-07's magnesium-glycinate example replaces "boosts immunity."
- Polish is the tell in a specific, non-obvious way here: legally airtight but flat, over-qualified prose is exactly the compliance-theater failure GP-08 exists to catch — a $650K enforcement order (Rejuvica/Sobrenix, Nov 2024) didn't happen to hedge-everything copy, it happened to copy that skipped the hedge; ship-grade output still has to convert.

---

## The Underlying Belief

> **Compliance is not a disclaimer bolted onto the end of good copy. It is a persuasion architecture built from permissible claims.**

The compliant/converting split is false. The FTC's own guidance and the practitioner rewrite banks agree: the constraint (describe the mechanism and the experience, not the disease outcome) forces *more* specific, more credible copy — vague disease-cure language is what generic AI and lazy copywriters default to; specific structure/function language backed by ingredient mechanism reads as more expert, not less compelling. This isn't theoretical: the FTC's Health Products Compliance Guidance (Dec 2022, updated 2023) exists because generic hedge-copy kept failing enforcement scrutiny at real consequence — a $650K refund order for Rejuvica/Sobrenix in Nov 2024 for exactly the kind of vague-outcome claim this pattern replaces.

---

## GP-01 — The Claim-Risk Taxonomy (the deterministic classifier)

Every claim sentence in health/supplement marketing copy sorts into exactly one of five buckets. This is the backbone of `/claim-audit` and `/pre-launch-gate`.

| Bucket | Definition | Permitted? | Evidence bar |
|---|---|---|---|
| **1. Disease claim (express)** | Names a disease/condition + explicit treat/cure/prevent/mitigate/diagnose language. "Cures diabetes," "treats anxiety," "prevents heart disease." | **NO** without FDA drug approval | N/A — categorically prohibited for supplements |
| **2. Disease claim (implied)** | No disease named, but the *net impression* communicates disease treatment. Five FTC-recognized triggers (below). | **NO** — same bar as express | N/A |
| **3. Structure/function claim** | Describes effect on normal structure or function of the body without disease reference. "Supports healthy sleep," "supports joint mobility." | YES, DSHEA-gated | Competent and reliable scientific evidence, product-specific; mandatory disclaimer; FDA notification within 30 days of first use |
| **4. Qualified health claim** | Claim the FDA has authorized for use *with* a disclaimer because evidence exists but doesn't meet "significant scientific agreement" (Pearson v. Shalala doctrine). | YES, only from FDA's authorized list, disclaimer verbatim required | Whatever tier FDA specified in the enforcement-discretion letter for that specific claim |
| **5. General wellbeing / puffery** | Non-specific subjective statements ("amazing," "life-changing," "feel your best") not tied to a measurable function. | YES, lowest risk | None required, BUT net impression can still convert puffery into an implied disease claim via context (see GP-03) |

### The Five Implied-Disease-Claim Triggers (FTC net-impression doctrine)
A structure/function claim becomes an implied disease claim when ANY of these attach:
1. **Outcome-stacking** — adding a guaranteed-outcome clause. "Boosts immunity" (S/F) → "Boosts immunity so you don't get sick" (implied disease-prevention).
2. **Contextual imagery** — pairing the claim with visuals coded to disease treatment (person discarding prescription bottles, before/after diagnostic imagery, clinical-white-coat framing).
3. **Symptom-matching** — describing symptoms characteristic of a specific disease even without naming it ("that burning, gnawing stomach pain" = ulcer/GERD implied claim).
4. **Substitute-for-treatment framing** — any language positioning the product as an alternative to a recognized drug or medical treatment.
5. **Citation-borrowing** — citing a clinical study about a *disease outcome* to support a structure/function claim on your product (the study's disease framing bleeds into your claim's net impression even if your on-page language stays S/F).

---

## GP-02 — The Substantiation Ladder

FTC's "competent and reliable scientific evidence" standard is not one bar — it's a ladder, and claim strength must be matched to the evidence tier actually held.

| Tier | Evidence type | Can support | Cannot support alone |
|---|---|---|---|
| **5 (gold)** | Randomized, controlled, human clinical trial, product-specific formula, adequate sample/duration | Any claim strength, including "clinically proven," "clinically studied" | — |
| **4** | Well-designed non-randomized human clinical study | Moderate-strength S/F claims | "Clinically proven" language (reserve for Tier 5) |
| **3** | Epidemiological / observational studies | Only where field-accepted as a substitute AND RCTs are infeasible (e.g., long-latency nutrition outcomes) | Standing alone as primary substantiation for a strong claim |
| **2** | In vitro / animal / mechanism studies | Explaining *how* an ingredient might work (mechanism narrative) | The human outcome claim itself — mechanism evidence is necessary, never sufficient |
| **0** | Anecdotal, customer testimonial, consumer survey, "9 out of 10 users report..." | Nothing, as primary substantiation | Never — testimonials support relatability, not the underlying health claim |

**The NAD product-specificity rule** (BrainPack, Reus Research, Olly cases): ingredient-level Tier 5 evidence does NOT transfer to a product-level claim unless the marketed product matches the tested formula's exact dose and delivery mechanism. "Our key ingredient was clinically studied" is a different (weaker) claim than "our product was clinically studied" — copy must not blur the two.

---

## GP-03 — Net Impression Over Isolated Sentences

The FTC evaluates an ad's **net impression** — text, product name, imagery, layout, and testimonials together — not any single sentence in isolation. A page can be sentence-by-sentence compliant and still be a deceptive ad if the overall vibe implies a disease claim. This is not a modern platform-era rule: it traces to the FTC's 1983 Deception Policy Statement, decades before Meta or TikTok ad review existed.

**Practical test**: Read the page as a stranger who skims headlines, glances at images, and reads one testimonial. What do THEY think the product does? If that net impression is a disease claim, the page fails regardless of how careful the body copy is.

---

## GP-04 — The Qualified-Claims Escape Hatch (Pearson v. Shalala)

FDA cannot categorically ban a health claim just because evidence falls short of "significant scientific agreement" — the D.C. Circuit held (1999) that a disclaimer is a less-restrictive alternative the First Amendment requires FDA to consider. This produced the **qualified health claim** pathway: manufacturers petition FDA; if evidence is credible-but-insufficient, FDA can authorize the claim *with a specific disclaimer it writes*, rather than banning it outright.

**Operational implication**: this pathway does NOT mean "add any disclaimer and any claim becomes legal." It means a narrow, FDA-pre-authorized list of claims (mostly conventional-food, some supplement) can carry qualifying language FDA itself specified. Brands cannot self-author a qualified claim — using this doctrine as copywriting license (a common mistake) is itself a violation.

---

## GP-05 — Testimonials Must Reflect Typical Results (FTC Endorsement Guides, 2023)

The 2023 revision to 16 CFR Part 255 killed the "results not typical" micro-print escape hatch.

- If a testimonial depicts an atypical result, the ad must **disclose what a typical consumer can actually expect** — clearly and conspicuously, same size type as the testimonial, same page/adjacent placement. Small-print disclaimers do not cure a deceptive testimonial.
- **No follower-count exemption** for material-connection disclosure — a micro-influencer with 40 followers has the same disclosure obligation as a celebrity.
- Brands are liable for an endorser's failure to disclose a material connection even without directly instructing the omission — vet influencer partners' disclosure practices, don't just supply guidelines.

---

## GP-06 — Platform Rules Are a Second, Stricter Layer (Meta / TikTok / Amazon)

Platforms enforce ad policy that is *stricter* than FTC/FDA baseline — passing legal review does not guarantee passing platform review.

| Platform | Rule beyond FTC/FDA baseline |
|---|---|
| **Meta** | Disclaimer ("not intended to diagnose, treat, cure, or prevent any disease") must appear IN the ad copy itself, not just the landing page. Personal Attributes policy bans second-person health-condition framing ("Sick of your anxiety?") even for a compliant S/F product. Restricted phrases ("guaranteed," "instant relief," "clinically proven") trigger manual review unless documentation is pre-loaded. |
| **TikTok** | Weight-loss and muscle-gain positioning is effectively banned as the *central* claim for supplement ads — reframe to broader wellness (energy, recovery, hydration, balance). "Clinically proven," "dermatologist tested," "scientifically formulated" all require submitted documentation at review or the ad is rejected outright. |
| **Amazon** | Automated keyword scanners flag disease NAMES anywhere in listing copy (cancer, diabetes, anxiety, COVID-19, herpes, etc.) and treatment VERBS (cure, treat, heal, remedy) — this catches technically-compliant S/F claims that happen to contain a disease word in an unrelated clause. Write listing copy assuming a keyword scanner, not a human reviewer, reads it first. |

---

## GP-07 — Compliant-But-Converting Rewrite Patterns (the practitioner layer)

Four rewrite moves, sourced from Jake Ballard (DTCskills.com) and P.J.S. Dougherty (Natural Health Writer), that produce copy which converts BETTER than disease-claim copy, not just copy that avoids risk:

1. **Mechanism over outcome** — replace the health-outcome promise with ingredient specificity and the "why." "Boosts immunity" → "Glycinate vs. oxide — most magnesium supplements use the form your body absorbs worst; this doesn't." Specificity reads as more expert than a vague cure claim.
2. **Review-language mining, not health-outcome mining** — pull customer testimonial language for the *emotion/experience* ("I actually wake up feeling rested"), never the disease-outcome framing ("this cured my insomnia") even when a real customer said it that way.
3. **Social proof over guarantee** — replace "you WILL sleep better" with review counts + a specific, non-outcome-guaranteeing customer quote. Numbers and specificity substitute for the guarantee the FTC would flag.
4. **Realistic-expectation framing** — "Most customers notice a difference within the first week" grounds the claim in typical results (satisfies GP-05) while still converting — vague absolutes ("works instantly") satisfy nobody legally or persuasively.

### Word-Swap Bank (high-frequency violations → compliant alternatives)
See `references/red-flag-word-bank.md` for the full table, organized against Dougherty's category-specific high-risk term list (inflammation, pain, immune, cholesterol, blood pressure, testosterone, weight-loss) and cross-checked against 16 CFR Part 255 endorsement rules. Headline entries:

| Banned | Compliant |
|---|---|
| Cures / treats / prevents [disease] | Supports [normal function] |
| Anti-inflammatory | Supports a healthy inflammatory response |
| Pain relief | Soothing comfort / supports comfort |
| Lowers blood pressure / cholesterol | Helps maintain levels already within the normal range |
| Boosts immunity (used with any outcome-stacking) | Supports immune function (standalone, no outcome clause) |
| Clinically proven (without Tier-5 product-specific evidence) | Studied ingredient / formulated with researched doses of X |
| Alternative to [drug] | Never compare to a pharmaceutical, prescription, or named drug |

---

## GP-08 — The Two-Experts Test (recognition test for this skill)

Before shipping any claim-touching copy, ask: **would a supplement regulatory attorney AND a direct-response copywriter both sign off?**

- The attorney fails copy that is legally clean but flat (compliance theater — disclaimer-stapled, hedge-everything copy nobody wants to read).
- The copywriter fails copy that converts by making disease claims, unqualified superlatives, or atypical testimonials without disclosure.
- **Pass condition**: the copy converts on mechanism, specificity, and real social proof — not on a claim either expert would flag.

This is the recognition test: would a Cohen Healthcare Law Group-style regulatory reviewer AND a Ballard/Dougherty-style DR copywriter both wave this through unchanged? The test exists because skipping it is expensive, not theoretical: Rejuvica/Sobrenix ran exactly the claim a regulatory attorney would have flagged and paid $650K in required refunds for it (Nov 2024).

---

## GP-09 — The FTC Gut Check (weight-loss specific red flags)

For weight-loss claims specifically, the FTC maintains a standing list of claims that are inherently false regardless of substantiation attempt (from the *Gut Check* media guide):
- No OTC product can cause substantial weight loss (defined as >1 lb/week for 4+ weeks, or >15 lbs total) without diet/exercise changes.
- Nothing worn or applied topically (patches, creams, wraps, body belts) can cause weight loss — weight loss is an internal metabolic process only.
- Any claim implying the above two are false on its face — no amount of "supporting evidence" rescues it; these are auto-fail patterns, skip straight to rewrite.

---

## Anti-Patterns (≥5 things a claim-safe operator would NEVER do)

1. **Never let a testimonial's language become the claim.** A real customer saying "this cured my anxiety" cannot be quoted verbatim as marketing copy — the disease-claim risk transfers from the customer's words to the brand's ad regardless of who said it first.
2. **Never treat a disclaimer as a cure for a deceptive net impression.** ("Results not typical" in 8pt font does not fix an atypical testimonial — GP-05.)
3. **Never borrow ingredient-level clinical evidence for a product-level claim** without confirming dose/formula match (GP-02 NAD rule) — NAD's 2025 Reus Research (NAD+ dosing) and Ingenuity BrainPack decisions (BBB National Programs) are the anchor cases: ingredient-level Tier 5 evidence does not transfer to a product-level claim unless dose and delivery mechanism match exactly.
4. **Never self-author a "qualified claim."** Only FDA's pre-authorized list + FDA's own disclaimer language counts (GP-04) — inventing your own hedge language is not the same mechanism and does not carry the same legal protection.
5. **Never assume legal-compliant copy passes platform review.** Meta/TikTok/Amazon enforce stricter, partly-automated rules layered on top of FTC/FDA (GP-06) — always run the platform pass separately; see `references/platform-rules.md`, e.g. Meta's Personal Attributes policy banning second-person symptom framing even on a fully compliant structure/function product.
6. **Never cite a disease-outcome study to support a structure/function claim**, even if the on-page language stays technically S/F (GP-01, trigger 5) — this is the citation-borrowing trigger named in FTC's *Health Products Compliance Guidance* (Dec 2022, updated 2023).
7. **Never write copy assuming a human reads it first on Amazon.** Assume a keyword scanner reads disease-name and treatment-verb tokens first (GP-06) — Amazon's Seller Central dietary-supplement policy scanner does not parse sentence-level meaning, detailed in `references/platform-rules.md`.

---

## Concrete-Metaphor Library (abstraction → source-anchored image)

- **Net impression** = reading the whole billboard from a moving car, not proofreading the fine print — the FTC's own "reasonable consumer" framing (1983 Deception Policy Statement) asks what a skimming stranger takes away, not what the marketer intended.
- **Substantiation ladder** = a courtroom evidence hierarchy — eyewitness testimony (Tier 0/testimonial) never outweighs forensic lab results (Tier 5/RCT), no matter how many eyewitnesses you stack.
- **Qualified claims doctrine** = a plea bargain FDA negotiates under *Pearson v. Shalala* (164 F.3d 650, 1999), not a loophole a brand invents — the disclaimer language is FDA's plea agreement text, not a template to improvise from.
- **Platform keyword scanners** = a metal detector at an airport — Amazon's scanner flags disease-word tokens regardless of the sentence's actual legal meaning (`references/platform-rules.md`); write assuming the machine reads first, the human second.

---

## Quality Rubric (8 criteria, ≥8/10 ship-grade; composite ≥8.0)

| # | Criterion | Anchor test |
|---|---|---|
| 1 | **Claim classification correct** | Every claim sentence sorted correctly into the 5-bucket taxonomy (GP-01); no disease claim (express or implied) present |
| 2 | **Evidence-tier match** | Claim strength does not exceed the evidence tier actually held (GP-02) |
| 3 | **Net impression clean** | Whole-page read (headline + image + testimonial) does not imply disease treatment even if sentences are individually compliant (GP-03) |
| 4 | **Testimonial compliance** | No atypical result without typical-result disclosure; no verbatim disease-claim quote used as copy (GP-05) |
| 5 | **Disclaimer present + correctly placed** | DSHEA disclaimer verbatim, platform-required placement honored (GP-06) |
| 6 | **Platform-specific pass run** | Meta/TikTok/Amazon-specific rules checked, not just FTC/FDA (GP-06) |
| 7 | **Two-experts pass** | Would both the regulatory attorney and the DR copywriter sign off unchanged? (GP-08) |
| 8 | **Converts, not just survives** | Copy uses mechanism/specificity/social-proof persuasion, not hedge-everything compliance theater (GP-07) |

**Veto rule**: Criterion 1 (claim classification) or 5 (disclaimer) scoring below 8 caps the whole audit at FAIL regardless of composite — these are the two dimensions FTC/FDA/platform enforcement actually gates on.

---

## Hall of Fame Exemplars (real, provenance-labeled — for blind-pass comparison, never quoted verbatim in production copy)

1. **Compliant structure/function ad pattern** (Jake Ballard, DTCskills.com worked example): problem-relatable hook → ingredient-mechanism specificity → review-count social proof → price. Zero disease claims, zero guaranteed outcomes. Source: DTCskills.com supplement marketing compliance guide.
2. **NAD-sustained claim** (OLLY Lovin' Libido, ashwagandha ingredient claim, NAD 2025): NAD affirmed the ashwagandha evidence base while the brand had ALSO discontinued an adjacent unsupported "enhanced sensation" claim — the pattern of keeping the well-evidenced claim and dropping the unevidenced adjacent one is the exemplar move.
3. **NAD-discontinued claim as anti-exemplar** (Ingenuity BrainPack, NAD 2025): "Memory / Clarity / Focus / Vision" cognitive-performance claims for a gummy vitamin were found unsupported by the evidentiary record and recommended for discontinuation — anti-exemplar for GP-02 (claim strength exceeding evidence tier).
4. **FTC enforcement anti-exemplar** (Rejuvica/Sobrenix, Nov 2024): unsubstantiated claims that a supplement could "reduce and eliminate alcohol cravings" led to a $650K consumer-refund order and a permanent ban on unsubstantiated health claims — anti-exemplar for GP-01/GP-02 (specific physiological-outcome claim with no Tier 4-5 evidence).

---

## Source Caveats

1. This is a **regulatory-knowledge extraction**, not a person-voice extraction — there is no single "expert" whose cadence is being captured. The embodiment-standard blind-pass (Phase 7.4) is adapted accordingly: instead of comparing generated prose against one expert's real published work, Tier-1 workflow outputs are compared against (a) real compliant ad copy patterns (Ballard/Dougherty published examples) and (b) real FTC/NAD enforcement-action language, to confirm the classifier correctly separates compliant from non-compliant phrasing.
2. Regulatory citations (FTC guidance, FDA structure/function rules, DSHEA, Pearson v. Shalala, 16 CFR 255) are drawn from primary sources (ftc.gov, fda.gov, Justia case law) and corroborating legal-analysis summaries (Cooley, Covington & Burling, Cohen Healthcare Law Group) — VERIFIED.
3. Specific NAD case outcomes and FTC enforcement actions are drawn from trade-press reporting (NutraIngredients, BBB National Programs case summaries) — VERIFIED as to case existence and outcome direction; exact evidentiary detail beyond the published summary is LIKELY, not independently re-derived from full case files.
4. Practitioner rewrite-pattern sources (Ballard, Dougherty) are individual marketing-consultant publications, not regulatory authorities — their compliance mechanics check out against the primary sources above (VERIFIED), but their self-reported track records (LIKELY, UNCONFIRMED per genius.md header) are not independently audited.
5. This skill governs U.S. FTC/FDA/DSHEA + major-platform rules only. International regulatory regimes (EU health claims regulation, Health Canada NHP rules, etc.) are explicitly out of scope — flag if a brand operates outside the U.S.

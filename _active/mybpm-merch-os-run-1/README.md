# MyBPM Merch OS — Run 1 (Complete)

**Execution Date**: June 10, 2026  
**Orchestrator**: `/merch-os`  
**Expert**: Meg Heckman (Buyer-Trigger Psychology + POD Operating System)  
**Brand**: MyBPM (EDM Streetwear, PLUR Culture)  
**Status**: Ready for Implementation  

---

## Deliverables Summary

### Phase 0 — GROUND (01-ground.md)
**Sub-Identity**: The Raver as Identity Keeper — person who wears PLUR as a year-round identity, treasures friendships from raves, attends 2–5 events/year as pilgrimages.

**Key insight**: Existing merch brands miss this person; they focus on party aesthetics instead of emotional ownership and behavioral commitment.

**Gate Status**: ✓ PASS — behavioral-moment person is specific, pictureable, grounded in real rave culture.

---

### Phase 1 — CONCEPT (02-concepts.md)
**12 mirror-only concepts**, all scoring ≥3.8 composite (10-criterion rubric):

**Tier 1 Leads** (5.0):
1. The Kandi Keeper — "I still have your kandi"
5. Stranger-to-Friend — "Met strangers, found family"

**Tier 1A Leads** (4.8):
4. Sunrise Survivor — "I walked out changed"
7. Flow Arts Soul — "I spin to find myself"
11. Raver Parent — "Next generation: PLUR"
12. Raver's Commitment — "This is my table"
2. Genre Knowing — "Hardstyle: Where I Found My People"

**Tier 2 Leads** (4.2–4.8):
3. Kandi Code — "Raver's language"
+ 4 Revised concepts (PLUR Liver, Genre-Home, Set-Changer, Alive Between)

**Gate Status**: ✓ PASS — 12 concepts, zero posters, varied triggers, strong self-deprecating identity subset.

---

### Phase 2 — SCORE (03-scorecard.md)
**10-criterion trigger audit**:
- **8 LEAD concepts** (≥4.0, no criterion <3) ready for design/listing
- **4 REVISE concepts** (one weak trigger each, revision directive named)
- **0 KILL concepts** (all viable)

**Highest-confidence leads**: The Kandi Keeper, Stranger-to-Friend (both 5.0)

**Gate Status**: ✓ PASS — ≥3 LEAD verdicts. Ready for Phase 3.

---

### Phase 3 — LISTING & DESIGN HANDOFF (04-listings.md, 05-prompt-pack.md)

**5 LEAD designs detailed**:
1. The Kandi Keeper (Satori Graphics — vector kandi focal point)
2. Stranger-to-Friend (Kittl — silhouette/connection composition)
3. Sunrise Survivor (Kittl — dawn moment, transformation framing)
4. Flow Arts Soul (Satori — motion-arc centered, meditation framing)
5. Raver's Commitment (Satori — table/symbol, bold declaration)

**Each design includes**:
- Recognition lead (50ms moment)
- Identity statement (first-person)
- Social moment (the future where this works)
- Buyer scene (behavioral moment, not demographic)
- Graphic system (focal point, color, style, composition)
- Identity micro-text (main text + placement)
- Niche-specific avoid-list (10 things that would kill it)
- Typography/composition brief

**Routing**: Per `creative_router.py` pre-flight
- Satori Graphics: Concepts 1, 4, 5 (composition-forward, illustration)
- Kittl: Concepts 2, 3 (typography + silhouette)

**Gate Status**: ✓ PASS — 5 designs ready for execution (cost-gated per CLAUDE.md)

---

### Phase 4 — LAUNCH (06-launch-plan.md)

**Test strategy**: Smallest honest test first (Josh V1 doctrine)
- **3-design slate**: Kandi Keeper, Stranger-to-Friend, Sunrise Survivor
- **Duration**: 14 days (July 1–14, 2026)
- **Platform**: Shopify (existing mybpm.store)
- **Budget floor**: $200 Meta Ads
- **Collection**: "PLUR Soul" (new, cohesive portfolio)

**Email sequence**:
1. Day 1: "We made three shirts just for you"
2. Day 4: Single-design deep-dive (The Kandi Keeper focus)
3. Day 12: End-of-window urgency

**Success criteria**:
- ≥1 design ROAS 2.5+ (scale trigger)
- ≥1 design ATC 7%+ (product resonance)
- ≥3 total sales across slate

**Kill criteria**:
- ROAS <2.0 across all three (market doesn't care)
- Zero multi-buys (portfolio doesn't cohere)
- ATC <5% across slate (execution problem)

**Founder approval checklist**: Mockup quality, copy tone, design integrity, launch logistics, price/margins, ad account readiness.

**48-hour read protocol**: Daily metric monitoring (CPC, ATC, ROAS, email opens) for first 2 days. Debug sequence if metrics weak.

**Gate Status**: ✓ PASS — smallest honest test named. Ready to run.

---

### Phase 5 — DIAGNOSTICS (07-diagnostics.md)

**6-metric weekly dashboard**:
- CPC ($0.55–$0.75 healthy)
- ROAS (2.5+ = scale; 2.0 = floor)
- ATC (7–8% = good; <5% = problem)
- IC (5–6% = healthy)
- CVR (3–4% = healthy)
- AOV ($45+ = profit floor)

**Weekly review cadence**: Monday, 9 AM (30 min)
**Ownership**: Farrice (decision-maker on kill/scale)

**Pre-committed kill/scale rules** (non-negotiable):
- **SCALE**: ROAS ≥2.5 + ATC ≥7% + CVR ≥3% → increase daily budget
- **REVISE**: ROAS 2.0–2.5 → mockup swap or email refresh (one test cycle)
- **KILL**: ROAS <2.0 after $100 spend; zero ATC; IC <4% post-fixes; CPC >$1.50 post-audience-refinement

**Factory loop** (if winning design found):
1. Keep LEAD design live
2. Scale ad spend to $500/week
3. Run Phase 1 again (new 12 concepts)
4. Score Phase 2
5. Launch Phase 3–4 (test 3 new designs)
6. Continue Phase 5 weekly cadence
7. Repeat

**Gate Status**: ✓ PASS — instruments installed before needed. Rules pre-committed. Taste cannot veto data.

---

## Ready for Production

### Next Steps (Immediate)

1. **Farrice approval**: Review all 7 deliverable files (01-ground through 07-diagnostics). Sign off or request revisions.

2. **Design execution** (cost-gated): 
   - Commission 5 designs from Satori Graphics / Kittl (per prompts in 05-prompt-pack.md)
   - Mockup on t-shirt before ad spend
   - Approval checkpoint before render

3. **Shopify setup**:
   - Create "PLUR Soul" collection
   - Add 3 product PDPs (Kandi Keeper, Stranger-to-Friend, Sunrise Survivor)
   - Update collection page copy (per Phase 4)
   - Add images (flat-lay clean, lifestyle, close-up text)
   - Configure Shopify Pixel + Meta integration

4. **Email setup**:
   - Load Email 1, 2, 3 sequences into email platform (Klaviyo, ConvertKit, etc.)
   - Schedule sends: Day 1, Day 4, Day 12 of test window
   - Pre-test email rendering (mobile, dark mode)

5. **Ad account readiness**:
   - Create Meta Ads campaign for PLUR Soul collection
   - Set budget to $20/day (total $140 over 7 days first half)
   - Configure conversion tracking (Add to Cart, Purchase)
   - Build lookalike audience from existing customer list (if <1K subscribers, use all)

6. **Week 1 cadence starts**:
   - Run ads (Day 1, 9 AM)
   - Send Email 1 (Day 1, 9 AM)
   - Monitor 48h metrics (first check: Day 1, 5 PM)
   - Weekly diagnostic (Day 8, 9 AM)

---

## Key Files (Archive)

| File | Purpose |
|---|---|
| `00-run-config.md` | Run parameters, grounding rule, phase overview |
| `01-ground.md` | Sub-identity person (behavioral moments), saturation proof, constraints |
| `02-concepts.md` | 12 mirror-only concepts (all 8 fields each) |
| `03-scorecard.md` | 10-criterion audit + revision directives + final LEAD verdicts |
| `04-listings.md` | Listing copy for 5 LEAD designs (recognition → identity → social → logic) |
| `05-prompt-pack.md` | Design handoff with buyer scene, graphic system, avoid-list, typography brief |
| `06-launch-plan.md` | 14-day test strategy, 3-design slate, email sequence, approval checklist, 48h protocol |
| `07-diagnostics.md` | 6-metric weekly dashboard, pre-committed kill/scale rules, factory loop |

---

## Pair With

- `/meg-trigger-audit` — weekly scorecard updates (if adding new concepts mid-run)
- `/meg-factory-loop` — if test succeeds and moving to full scale
- `/meg-store-stack` — if graduating from collection test to full Shopify architecture
- `/build-bos` — if test succeeds and brand expands beyond t-shirts

---

## Extraction Grounding

This run is grounded in the **Meg Heckman Buyer-Trigger OS** extraction (Phase 1–6 complete, Phase 7 deployed here, Phase 8 pending finalize):

- **Source**: 6 YouTube videos, 13,339 words, 240 frames
- **Genius patterns**: 16 documented
- **Hidden knowledge**: 12 items
- **Exemplars**: 4 (Sloth Hiking Club, "Out of Breath", kandi mechanics, mockup swap)
- **Signature moves**: 7
- **Quality rubric**: 10 criteria
- **Vocabulary contract**: 6 triggers (frozen per Josh production)
- **Confidence**: All claims labeled VERIFIED/LIKELY/UNCONFIRMED per source quotes

---

## Finalize Status

**Pending**: Chain Step 6 finalization (Phase 8)
- Extraction (Meg Heckman forge): Type=Extraction
- MyBPM Run (first deployment): Type=Creative

Both require:
```bash
python3 execution/chain_runner.py finalize "[description]" \
    --expert meg-heckman --skill meg-heckman-buyer-trigger-os \
    --type [Extraction|Creative] --intent [1-10] --expert-score [1-10] \
    --adversarial [1-10] --sub-agents [measured] \
    --notes "[working/didn't] | Factual Grounding: [1-10] | Verification: [PASS/FAIL/PARTIAL/N/A]"
```

---


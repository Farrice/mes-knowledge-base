---
description: The master diagnostic — map all 6 blocks, flag what's missing, strengthen each via CRAVES, tune velocity. How Luke reviews $2,500/mo client copy.
---

# Copy Block Audit — The Two-Move Diagnostic

This is the flagship diagnostic: exactly how Luke Iha reviews copy on the A-list feedback calls. Two moves: **(1) Does it have all 6 blocks? Add the missing ones. (2) Look at the blocks it has — which is weakest? Strengthen it via CRAVES.** Plus a velocity pass for rhythm. Produces a block map, gap analysis, CRAVES strengthening, velocity chart, and rewrites — every weakness paired with a rewritten line (never naked critique).

> **🔒 Pre-Flight Gate**: Run the **Decision Framework** in `genius.md`. Confirm you know the market's Core Wound, the dominant pain dimension (psychological/physiological), and the top identity/value constraints to work around.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If the audited copy targets an already-grounded market, read cached intelligence to judge it against *real* market psychology, not assumptions:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — audit proceeds on the copy alone; for market-grounded critique run /copy-engine for this market first."
```
Use `core_wound`, `dominant_emotion`, `pain_to_promise_gap`, `market_beliefs`, `top_voc_soundbites` to check whether the copy's blocks actually match the market. (Optional — the audit also works standalone on structure alone.)

## PHASE 1: SKILL ACQUISITION (Do this FIRST)

Read in order:
1. `skills/luke-iha-copy-blocks/genius.md`
2. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md`
3. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md`

## PHASE 2: INPUT REQUIREMENTS
- **The copy to audit** (ad, VSL, email, landing page, headline — any persuasive text)
- **Context** (optional): target audience, product, awareness level, performance data

## PHASE 3: BLOCK MAPPING
Tag every sentence with its primary block:
- **[P]** Pain · **[PR]** Promise · **[PF]** Proof · **[CN]** Constraints · **[CU]** Curiosity · **[CO]** Conditions

Output as a numbered list with tags. (Note where a single line carries two blocks — e.g. proof-as-promise.)

## PHASE 4: MOVE 1 — GAP ANALYSIS (missing/underweight blocks)
For each absent or thin block, name the reader reaction it causes — then (Phase 6) write the fix:
- **No Pain** → "so what?" · **No Promise** → "why care?" · **No Proof** → "I don't believe you" · **No Constraints** → "I'll do it later" · **No Curiosity** → no reason to keep reading · **No Conditions** → "is this for me / why now?"

## PHASE 5: MOVE 2 — CRAVES STRENGTHENING (the blocks it HAS)
Score each present block against CRAVES (Clear · Relevant · Accurate · Visual · Expressive · Specific). Flag the **weakest dimension per block**. Priority order of attack: the **Curiosity** block first (usually weakest — generic mechanism names), then Proof balance, then Visual/Specific gaps in Pain/Promise.
- Generic-mechanism test: could the curiosity name drop unchanged into an unrelated market? If yes → not Specific, rewrite (see `curiosity-engine.md` Evocative Naming).

## PHASE 6: VELOCITY ANALYSIS
1. **Block sequence** in order (e.g. P-CU-PR-P-PF-CU-CN-PR).
2. **Consecutive runs** — flag any block dominating 4+ sentences (velocity drop).
3. **Opening velocity** — # distinct blocks in first ~5 sentences (target 3+).
4. **Pre-CTA** — does rhythm slow deliberately before the close? (intentional = good).
5. **Density** — any padded passages that could compress (informal CVS feel, not a reported number).

## PHASE 7: REWRITE RECOMMENDATIONS (copy-feedback-as-copy)
**Every flagged issue MUST ship with a rewritten line.** "Add curiosity" is bozo feedback — show the line.
1. Missing blocks → 2–3 example sentences adding the block with a fresh angle.
2. Weak curiosity → an Evocative-Named alternative (+ what associations it triggers).
3. CRAVES weaknesses → the before/after line.
4. Velocity drops → the compressed/interleaved rewrite.

## OUTPUT FORMAT
```
## Copy Block Audit

### Block Map
[Numbered sentence-by-sentence tags]

### Move 1 — Missing Blocks
[Block] missing → reader reaction → FIX: "[rewritten line]"

### Move 2 — Strengthen What's There (CRAVES)
[Block]: weakest = [dimension]. Before: "…" → After: "…"

### Velocity
Opening: X/5 blocks · Longest run: [Block]×N (sent. A–B) · Distribution: P:_ PR:_ PF:_ CN:_ CU:_ CO:_
Pre-CTA slowdown: [yes/no]

### Diagnosis
[2–3 sentences: structural health + the single highest-leverage fix]

### Prioritized Rewrites
1. [issue → rewritten copy]
```

---
## Quality Gate
> **🛡️ Anti-Pattern Check**: Review against `genius.md` § Anti-Patterns. No naked critique (every flag has a rewrite). No visible block labels in the rewritten *customer-facing* lines. Clarity never sacrificed for density.

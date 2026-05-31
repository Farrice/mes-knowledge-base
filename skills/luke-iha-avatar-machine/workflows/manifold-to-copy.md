---
description: Turn a completed Avatar Manifold into FINISHED converting copy by dispatching the Luke copy stack with manifold sections injected — a real invoker, not a routing brief
tier: 3
wired: true
stacks_with: luke-iha-vsl-leads, luke-iha-copy-blocks, luke-iha-vicious-hooks, luke-iha-proof-ladder, luke-iha-million-dollar-mechanisms, luke-iha-unaware-ads
---

# Manifold → Copy Bridge (WIRED — real invoker)

The connective tissue that makes the keystone feed the whole system. Takes a completed Avatar Manifold + an **objective/asset type** and produces **finished copy** by actually dispatching the right downstream Luke skills with the manifold's sections injected as context.

> **This workflow returns finished copy, not a routing brief.** Returning only a routing table is an auto-fail. The routing table is an *internal intermediate* (step 2), not the deliverable.

## Pre-Flight Gate
- A completed (or substantial) Avatar Manifold in hand (anchor it via `anchor_memory` if part of an orchestrated run). If not, run `/avatar-manifold` first.
- **`--objective` / asset type named** (VSL for $X offer · cold FB ad · N-email sequence · sales page · funnel). If missing, ask once — it selects the skill chain.
- This workflow ROUTES + INVOKES; it does NOT re-research. The manifold is already grounded.

## Skill Acquisition
Load genius.md "5-Part Sales Formula" + "Canonical Assembly Order." Have the target Manifold (or its `anchor_memory` anchors) open.

## Execution

### 1 — Resolve objective → skill chain (the asset→chain map)
| `--objective` | Skill chain (dispatch in order) |
|---|---|
| **VSL** ($X offer) | vsl-leads → million-dollar-mechanisms → proof-ladder → copy-blocks → vicious-hooks (hook pass) |
| **Cold FB/IG ad** | vicious-hooks → unaware-ads → copy-blocks (CASH) |
| **Sales page** | proof-ladder → copy-blocks → dissolution-forge (objection section) |
| **Email sequence** (N) | copy-blocks ("What The Hell" template) → vsl-leads (micro-lead per email) |
| **Funnel** (ad→page) | vicious-hooks → unaware-ads → vsl-leads → proof-ladder → copy-blocks |

### 2 — Build shared boundaries (once)
- **Do-not-say list** = the manifold's Ejection Triggers (hard boundary passed to every downstream agent).
- **Awareness level** = from consciousness level + Resonance Hierarchy → routes hook density/CTA via `luke-iha-unaware-ads`.

### 3 — Dispatch each downstream skill as a SkillExecutor sub-agent (real invocation)
For each skill in the chain, spawn one Agent (4-field envelope per `directives/sub_agent_protocol.md`). The **5-part mapping table** below dictates which manifold sections inject into each:

| Sales part → skill | Manifold sections injected (the ANCHORS field) |
|---|---|
| LEAD → vsl-leads + vicious-hooks | Epiphany Threshold (Goldilocks set) · Pick-Up Lines · archetype tone · landmines (do-not-say) |
| BACKGROUND → vsl-leads (body) + copy-blocks (Pain) | Anti-Hero Pt 1 · Core Wound · Pain Matrix |
| MECHANISM → million-dollar-mechanisms | Epiphany (Goldilocks synthesis) · Interoceptive Mechanism · Causal Clarity |
| PRODUCT → copy-blocks (Promise/Proof) + proof-ladder | Anti-Hero Pt 2 · Benefit Matrix · Daisy-Chain |
| CLOSE → proof-ladder + proof-mechanisms | RH Constraints · Dissolution Frameworks · landmines |

```
Agent(subagent_type="general-purpose", description="copy: <part> via <skill>", prompt="""
═══ OBJECTIVE ═══ Produce the <part> for a <asset> to expert standard, in the market's grounded voice.
═══ SKILL ACQUISITION ═══ Read skills/<skill>/SKILL.md → genius.md → workflows/<writer>.md
═══ ANCHORS (read-only) ═══ <inject the manifold sections from the table above, verbatim>
═══ BOUNDARIES ═══ Honor the do-not-say list (ejection triggers) absolutely; awareness level = <level>; use the supplied VOC soundbites, do not invent language; later parts load earlier parts' artifacts.
═══ OUTPUT FORMAT ═══ Write to .tmp/copy-engine/<slug>/<asset>-<part>.md; return ≤500-token summary + self-score.
""")
```
Dispatch in dependency order (lead → body → mechanism → product → close); later agents read earlier artifacts as additional anchors. The router fires only the parts the asset needs (a cold FB ad = LEAD + compressed MECHANISM + CLOSE).

### 4 — Quality-gate each artifact (Gate B)
Before assembly, each artifact passes `/adversarial-review`; hook/lead artifacts also `/writers-room` (the heartbeat pass). Composite <7 → one targeted rewrite. Verify the do-not-say list is absent from each artifact.

### 5 — Assemble + finalize
Assemble the artifacts into the finished asset (VSL script / ad / sequence) in canonical order. Then **Gate C** — per-artifact `chain_runner.py finalize` (never batch):
```bash
// turbo
python3 execution/chain_runner.py finalize "<artifact summary>" \
  --expert luke-iha --skill luke-iha-<downstream> --workflow manifold-to-copy --type Copy \
  --intent <1-10> --expert-score <1-10> --adversarial <1-10> --sub-agents <N> --anchor-named \
  --notes "Asset=<asset>. Manifold sections: <list>. Do-not-say honored."
```

## Content Type Adaptations
See the asset→chain map (step 1). A VSL fires all 5 parts; a cold FB ad fires LEAD + compressed MECHANISM + CLOSE; an email sequence runs one micro-lead + block per email.

## Output Requirements
- **Finished copy artifact(s)** in canonical order (the deliverable) — NOT a routing brief.
- A per-artifact quality-score table (each `chain_runner.finalize` composite ≥7).
- Confirmation the do-not-say list is absent from every artifact.

## Quality Gate
Rubric criterion 8 (Deployability) ≥8: finished copy produced, every artifact `finalize` composite ≥7, ejection triggers absent. **Auto-fail**: returning a routing brief instead of finished copy; generic copy not tied to this manifold's grounded sections; inventing language instead of using the supplied VOC; skipping the per-artifact finalize.

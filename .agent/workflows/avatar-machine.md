---
description: Cold-start → finished converting copy. The Avatar Machine end-to-end orchestrator — real research, dependency-batched manifold build, audit, downstream copy production, per-artifact finalize.
tier: system
wired: true
---

# /avatar-machine — Cold-Start → Converting Copy

The full pipeline. Type a market + product + objective; get a grounded Avatar Manifold AND the finished asset (VSL / ad / sequence), with real (not modeled) VOC and per-artifact quality scores. This is the orchestrated front door of the entire Luke Iha stack.

```
/avatar-machine "[market]" "[product]" --objective "VSL for $2k offer" [--voc-file <path>] [--no-ground]
```
`--objective` ∈ {`VSL for $X offer`, `cold FB ad`, `N-email sequence`, `sales page`, `funnel`}. Omit → build manifold + audit only, then ask.

> Routing: enforced by `routing_enforcer.py` binding `avatar_manifold_coldstart`. Phase 0 GROUND is the deterministic backstop — never skip it on a cold start unless `--no-ground` (+ `--voc-file`). Reuses the `supercomputer` Phase 0–5 orchestration shape; quality moat stays in `chain_runner.finalize`.

Skill: `skills/luke-iha-avatar-machine/`. Read `SKILL.md` → `genius.md` → `references/research-spine.md` first.

---

## PHASE 0 — PROJECT STATE
Derive a kebab `<slug>` from the product/market. Init anchor memory (state lives at `projects/<slug>/state.yaml`):
```bash
// turbo
python3 execution/anchor_memory.py init <slug> --audience "<market>" 2>/dev/null || python3 execution/anchor_memory.py load <slug>
```
State the slug to the user.

## PHASE 1 — GROUND (cold-start research — AUTO-FIRES, deterministic backstop)
Fire the runner. It writes the canonical dossier (`.tmp/copy-engine/deep-research.md` + `voc-pack.md`) BEFORE any plotting, so the manifold cannot be built on contextual guessing.
```bash
// turbo
python3 execution/cost_gate.py status 2>/dev/null || true   # G2 awareness ($5 session soft cap)
python3 execution/avatar_manifold_runner.py ground \
  --market "<market>" --product "<product>" --slug <slug> \
  --mode max --depth heavy $( [ -n "<voc-file>" ] && echo "--voc-file <voc-file> --no-ground" )
cat .tmp/copy-engine/ground-status.json
```
- **MCP enrichment (model-side, additive):** after the runner, fire `mcp__playwright__browser_navigate`→`facebook.com/ads/library`→`browser_snapshot` for live hooks, and `mcp__recall__search` (focused, 2 queries) for expert grounding; append both to `voc-pack.md`.
- **Floor check** (must pass or proceed knowing language is modeled):
```bash
// turbo
python3 - <<'PY' || echo "GROUND GATE: thin/unsourced — re-mine via /buyer-sourcer before plotting"
import re,glob,sys
f=glob.glob(".tmp/copy-engine/voc-pack.md")
t=open(f[0]).read() if f else ""
u=len(re.findall(r'https?://',t)); m=t.upper().count("[MODELED]")
print(f"VOC: {u} sources, {m} [MODELED]"); sys.exit(0 if u>=15 and m==0 else 1)
PY
```
GROUND STATUS `DEGRADED` → continue, but every specific-language item ships `[MODELED]` and the final summary flags it.

## PHASE 2 — BUILD MANIFOLD (dependency-batched Agent fan-out)
Run the 14 stages in 6 dependency batches. Each stage = one SkillExecutor sub-agent (4-field envelope, `directives/sub_agent_protocol.md`) that loads `skills/luke-iha-avatar-machine/SKILL.md → genius.md → workflows/<stage>.md` + the GROUND dossier + prior-batch anchors, and writes its section to `.tmp/copy-engine/<slug>/<stage>.md`. After each batch, register anchors:
```bash
// turbo
python3 execution/anchor_memory.py anchor <slug> --type manifold_section --path .tmp/copy-engine/<slug>/<stage>.md --desc "<stage>" --ref-for "<downstream batches>"
```

| Batch | Stages (run concurrently) | Consumes |
|---|---|---|
| **B0** | build-a-buyer | GROUND dossier (`deep-research.md`) |
| **B1** | pain-matrix · specific-language | B0 (specific-language reads `voc-pack.md`) |
| **B2** | core-wound · benefit-matrix | B1 |
| **B3** | resonance-hierarchy · daisy-chain · anti-hero · suffering-archetype | B2 |
| **B4** | rh-constraints · epiphany-threshold · landmines | B3 |
| **B5** | dissolution · market-pickup-lines | B4 |
| **B6** | concatenate + 5-Part Sales Formula Map | B0–B5 |

**Heartbeat guard:** prose stages (core-wound, anti-hero, resonance-hierarchy, specific-language) run via the Agent tool (Claude), never `parallel_swarm` Gemini workers. Analytic/table stages may use `parallel_swarm.py` only if cost/speed demands — and still pass Gate A.

**Gate A (per stage, inline):** score each section against the genius.md 8-criterion rubric. Auto-fails (single-adjective, scores-without-consequences, invented-VOC-unflagged, summarized-beats) → re-spawn that one stage once via the Agent tool.

Concatenate B6 → `# AVATAR MANIFOLD — [Market]`, anchor it (`--type avatar_manifold`).

## PHASE 3 — AUDIT (pre-handoff QA)
Run `/manifold-audit` on the assembled manifold (coverage table + 8 rubric scores + gap list). Gaps in the leverage components (dimensionality, core-wound, identity, specific-language) → re-run those stages once. Target: dimensionality ≥8 and core-wound ≥8.

## PHASE 4 — PRODUCE COPY (if `--objective` given)
Invoke `/manifold-to-copy --objective "<objective>"` (the real invoker). It resolves the asset→skill chain, injects the manifold's grounded sections into each downstream Luke skill via the 5-part map, runs Gate B (`/adversarial-review` + `/writers-room` on hooks/leads) per artifact, and assembles the finished asset.

## PHASE 5 — FINALIZE (Gate C, per artifact — never batch)
```bash
// turbo
python3 execution/chain_runner.py finalize "Avatar Manifold — <market> (cold-start)" \
  --expert luke-iha --skill luke-iha-avatar-machine --workflow avatar-machine --type System \
  --intent <1-10> --expert-score <1-10> --adversarial <1-10> --factual <1-10> \
  --sub-agents <N> --critical-path 6 --anchor-named \
  --anchor-type avatar_manifold --anchor-path .tmp/copy-engine/<slug>/manifold.md \
  --notes "GROUND=<status>. Stages=14/6 batches. Objective=<objective>." \
  --source-request "<original user request>"
# + a separate finalize per finished copy artifact (Asset=...)
```
Verify anchor propagation (each downstream stage references its upstream anchor's key terms). Present a one-block mission summary: slug + `projects/<slug>/state.yaml`, files produced, per-artifact composite scores, the finished converting copy, GROUND status, suggested next move.

---

## Cost
~$1–2 per cold-start run (Gemini $0.5–1.5 + Apify ~$0.10). Gemini + Apify self-gate; G2 = `cost_gate.py status` ($5 session soft cap). `--mode standard` halves the Gemini cost.

## Full list of stage workflows
`build-a-buyer`(in avatar-manifold) · `pain-matrix` · `core-wound` · `resonance-hierarchy` · `epiphany-threshold` · `market-pickup-lines` · `dissolution-forge` · `anti-hero-journey` · `suffering-archetype` · `buyer-sourcer`(specific-language) · `manifold-audit` · `manifold-to-copy`. All wired with PHASE 0 GROUND; see `references/research-spine.md`.

---
description: Execute the compiled prompts across models behind the cost gate — draft cheap, promote only the winners, log every dollar into a spend ledger; the ONE Studio stage that spends money.
---

# 06 — Generate Run (/fantastic-generate-run)

> The only stage where money moves. Everything upstream was free thinking; here the compiled prompts become pixels — but never in one greedy pass. Draft at the cheapest tier, let the critique loop cull, and promote only survivors. Satori decides, the router picks the instrument, the studio critiques its own work — and the wallet stays disciplined the whole way.

## Pre-Flight Gate

**Use this when**:
- WF-05 has produced a COMPILED PROMPTS block (per-direction, model-specific) and WF-04 has assigned each direction an instrument. You are ready to render.
- You have a single locked direction and just need it generated and promoted to a final.
- You are re-rolling a direction the critique loop (WF-07) sent back — the mask edit or regenerate still runs through this gated sequence.

**Do NOT use this when**:
- The prompts are not compiled yet — run WF-05 first. A vague prompt burns money on a bad render.
- No instrument is assigned — run WF-04 (`creative_router.py`) first, or this stage guesses and pays for the guess.
- You only want to *judge* an existing render — that is WF-07 (critique + refine), which is free until it prescribes a new paid call.
- You are format-packing a finished concept into feed/story/hero variants — that is WF-08.
- The concept itself is unproven — do not spend to discover the concept is wrong; that is a WF-01→05 failure, not a generation problem.

**Hard rule this stage enforces**: nothing auto-fires. Even here — the one paid stage — every call runs `check → (approve on needs-approval) → run → log` with a human in the loop. `seedance-1080p` is HARD-BLOCKED. A denial is surfaced and stops the run; it is never retried or worked around.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md          ← the studio brain
  ├─ Cost Discipline (non-negotiable — physical gate) ... the whole doctrine of this stage
  ├─ The Capability Map ............................ which lever/flag each instrument exposes
  ├─ Model-Routing Decision Tree (WF-04) ........... draft-first: low / Nano → promote the survivor
  └─ Anti-Patterns 8 (auto-firing) · 6 (under-used hands)

Compose (free judgment gates — run on drafts BEFORE any promotion spends more):
  /satori-flip-test                                → 90-sec structural cull on each draft (free)
  skills/satori-graphics/workflows/01-lift-audit.md → /satori-lift-audit  (leverage/eye/friction/transfer on a survivor)
  workflows/07-critique-refine.md                  → /fantastic-critique   (the full SHIP · REFINE · REGENERATE call)

Drives (real code — this stage FIRES these behind the gate):
  execution/cost_gate.py            — unified pre-flight (check / approve / log)
  execution/fal_budget_guard.py     — Fal wallet guard (cost_gate delegates here; carries the $ accounting for Fal)
  execution/higgsfield_budget_guard.py — Higgsfield credit guard (separate credit wallet)
  skills/fantastic-posters/generate.js — Fal GPT Image 2 generator (run from repo root, FAL_KEY in env)
  execution/fal_video_kling.py / fal_video_seedance.py — video wrappers (handle FAL_KEY, upload, MP4 download)
  Higgsfield MCP (via ToolSearch): generate_image · generate_video · models_explore(action:'recommend')
```

## Execution

Five moves, run in order. Moves 1–2 are free planning; move 3 is the gated firing loop; move 4 promotes only survivors; move 5 closes the books. Do not skip the draft pass to "save time" — a $0.011 draft that fails saves you a $0.17 mistake.

### 1 — INGEST the run manifest (WF-05 prompts + WF-04 routes)

**Decision forced**: which directions enter the draft pass, and what instrument does each one fire?

- Pull the **COMPILED PROMPTS** block (WF-05): for each direction, the exact model-specific prompt or the path to its Fal `--brief=<dir>.json`, plus any compiled flags (`--style` / `--input` / `--mask` / `--refs` / `--logo` / `--template` / `--size` / `--palette` / `--rembg`).
- Pull the **MODEL ROUTE** block (WF-04): direction → service. If any direction is unrouted or you want to confirm the instrument, run the router (free, read-only):

```bash
python3 execution/creative_router.py route --task "<direction one-liner + surface>" --json
```

- Tag every direction **DRAFT**. Nothing enters at medium or high. Distinct directions from WF-03 stay **separate calls** (one `--brief` each) — never collapse them into `generate.js --n=4`; `--n` is a diversity nudge on one idea, not the divergence engine.

### 2 — SET the budget ladder (draft cheap → promote the winner)

**Decision forced**: what is the cheapest tier that still tells me whether this direction works?

| Instrument | Draft tier (cheapest useful) | Est / call | Promote to |
|---|---|---|---|
| Fal poster / edit (`fal-poster` / `fal-edit`) | `--quality=low` | **$0.011** | medium ($0.04) → high ($0.17), finals only |
| Higgsfield Nano (`higgsfield-nano`) | Nano Banana Pro, 1 image | **~$0.05** | escalate to Soul only if photoreal fidelity needed |
| Higgsfield Soul (`higgsfield-soul`) | 1 image | **~$0.10** | more takes / larger only on the survivor |
| Video (`fal-kling` / `fal-seedance-720p` / `higgsfield-cinema`) | **do not draft video** | — | animate ONLY the winning still |

Rule: **draft = 1 image per direction.** Cheap siblings (`--variants=2..4`, one API call) and quality bumps come *after* the cull in move 4, not before.

### 3 — DRAFT PASS — the gated firing sequence (run once per direction)

For **every** paid call, run these four steps — never skipped, never reordered:

- **(a) CHECK** — `cost_gate.py check`. Reads the verdict: `AUTO-APPROVED` (<$0.20) · `USER APPROVAL NEEDED` (≥$0.20) · `DENIED` (cap/hard-block).
- **(b) APPROVE** — only if the check said *needs approval*. **STOP. Surface the estimate to Farrice** ("Approve ~$X for [thing]? y/n"). Only after an explicit yes run `cost_gate.py approve` (token lasts ~15 min). If DENIED: surface and stop — do not retry.
- **(c) RUN** — fire the compiled command for the instrument.
- **(d) LOG** — record the actual spend so the ledger and guards stay honest.

**Fal poster / edit** (`fal-poster` / `fal-edit`) — `cost_gate` delegates the check to `fal_budget_guard`, so **pass `--quality` and `--n`** (the delegate needs them) and record the dollar accounting with `fal_budget_guard log`:

```bash
# (a) check — delegates to fal_budget_guard mode=poster; low + n=1 → est $0.011
python3 execution/cost_gate.py check --service fal-poster --request "<direction one-liner>" --quality low --n 1

# (c) run — FAL_KEY in env (or .env at repo root); run from repo root
node skills/fantastic-posters/generate.js --brief=.tmp/studio/dir-01.json --quality=low
#   (or the exact flags WF-05 compiled: --style=<id> / --input=<path> --mask=<path> / --refs=hero.jpg,brand.pdf,logo.png
#    / --logo=<path> / --template=<png> / --size=portrait|square|poster-xl|WxH / --palette="#hex,#hex" / --rembg)

# (d) log — Fal accounting lives in fal_budget_guard; cost_gate log for a Fal service is only a cross-reference
python3 execution/fal_budget_guard.py log --mode=poster --quality=low --n=1 --status=success --actual-cost=0.011 --style=<id> --output-path=skills/fantastic-posters/out/<file>.png
```

Transparency cutouts add one chained call: append `--rembg` to the run (writes `*_alpha.png`, +~$0.005) — no separate service.

**Higgsfield Nano / Soul** (`higgsfield-nano` ~$0.05 · `higgsfield-soul` ~$0.10 — both auto-approve under $0.20) — Higgsfield has its OWN credit wallet, so it gets a second guard, and the render fires through the MCP tool:

```bash
# (a) unified pre-flight
python3 execution/cost_gate.py check --service higgsfield-nano --request "<direction one-liner>"
# Higgsfield credit guard (its own wallet — prompt-only ideation is free; generation is gated)
python3 execution/higgsfield_budget_guard.py check --operation image_preview --count 1

# (c) run — load the MCP tool schema first, then call it
#     ToolSearch query: select:mcp__claude_ai_Higgsfield__generate_image
#     (unsure which Higgsfield model fits? ToolSearch → mcp__claude_ai_Higgsfield__models_explore, action:'recommend')
#     then invoke mcp__claude_ai_Higgsfield__generate_image with the WF-05 prompt (+ character ref for Soul face consistency)

# (d) log — both ledgers
python3 execution/higgsfield_budget_guard.py log --operation image_preview --status success --estimated-credits <e> --actual-credits <a> --job-id <id>
python3 execution/cost_gate.py log --service higgsfield-nano --status success --actual-cost 0.05
```

### 4 — JUDGE + PROMOTE (only survivors cost more)

**Decision forced**: which drafts earned a medium pass, and which single winner earns high?

1. **Cull for free.** Run each draft through `/satori-flip-test` (90 sec) and the WF-07 critique (Virgil × LIFT × type × anti-slop → SHIP · REFINE · REGENERATE). Judgment is free; killing a direction here costs $0.
2. **Promote survivors to medium** ($0.04). For a chosen direction's cheap siblings, use one batched call rather than N separate calls:

```bash
python3 execution/cost_gate.py check --service fal-poster --request "<survivor> — sibling spread" --quality medium --n 1
node skills/fantastic-posters/generate.js --brief=.tmp/studio/dir-01.json --quality=medium --variants=4   # 4 images, ONE API call
python3 execution/fal_budget_guard.py log --mode=poster --quality=medium --n=4 --status=success --actual-cost=0.16 --output-path=skills/fantastic-posters/out/
```

3. **One winner → high** ($0.17), finals only. Re-run the full four-step sequence at the new tier — **a promotion is a brand-new paid call**, gated like any other. `generate.js` self-prompts for confirmation on `--quality=high` (and on ≥5 images), so never pass `--yes` on a final.
4. **Video is a promotion, never a draft.** Animate only the winning still. Video needs the Fal budget guard's mode check *and* the wrapper. Above-threshold routes (`higgsfield-cinema` est $1.50) trip the needs-approval branch — STOP and surface:

```bash
# Fal Kling (multi-shot / cheaper) — winning still as the opening frame
python3 execution/fal_budget_guard.py check --mode=kling --duration=5 --audio=on          # est ~$0.84 (≤ $2 ceiling)
python3 execution/fal_video_kling.py --prompt "<motion beat>" --start-image "skills/fantastic-posters/out/<winner>.png" --duration 5 --audio on
python3 execution/fal_budget_guard.py log --mode=kling --duration=5 --audio=on --status=success --actual-cost=0.84 --brief="<direction> reveal"

# Fal Seedance 720p (single-shot cinematic) — 1080p is HARD-BLOCKED, never attempt it
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=6           # est ~$1.81 (≤ $3 ceiling)
python3 execution/fal_video_seedance.py --prompt "<motion beat>" --image "skills/fantastic-posters/out/<winner>.png" --duration 6 --resolution 720p --aspect 9:16 --audio on
python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=6 --status=success --actual-cost=1.81 --brief="<direction> reveal"

# Higgsfield Cinema (needs-approval — est $1.50 > $0.20)
python3 execution/cost_gate.py check --service higgsfield-cinema --request "6s cinematic hero"    # → USER APPROVAL NEEDED
# STOP → ask Farrice: "Approve ~$1.50 for the 6s cinematic hero? (y/n)". ONLY after explicit yes:
python3 execution/cost_gate.py approve --service higgsfield-cinema                                # token ~15 min
python3 execution/higgsfield_budget_guard.py check --operation marketing_studio_video --estimated-credits <e> --approved
#   run: ToolSearch → mcp__claude_ai_Higgsfield__generate_video, then invoke it
python3 execution/cost_gate.py log --service higgsfield-cinema --status success --actual-cost 1.50
```

### 5 — LEDGER + RECONCILE

**Decision forced**: does the recorded spend match the guards, and is the run within cap?

Fill one ledger row per fired call (template in Output Requirements). Then reconcile against the source-of-truth trackers — if a row is missing, a `log` was skipped:

```bash
python3 execution/cost_gate.py status              # session + daily $ + quota pools
python3 execution/fal_budget_guard.py status       # Fal wallet, cycle/day spend by mode, last 5 calls
python3 execution/higgsfield_budget_guard.py status # Higgsfield credit balance
```

## Content-Type Adaptations

| Content type | Draft tier / instrument | Promote path | Gate command spine |
|---|---|---|---|
| **Poster / print** | `fal-poster --quality=low` ($0.011), 1 image | medium spread via `--variants`; **one** winner → high; `--size=poster-xl` for print | `cost_gate check --service fal-poster --quality low --n 1` → run → `fal_budget_guard log --mode=poster` |
| **Logo / identity** | `fal-poster --quality=low` + `--logo=<path>` (exact wordmark) | winner → high + `--rembg` for transparent `*_alpha.png` | same Fal spine; add `--service fal-rembg` only if cutout is a separate pass |
| **Social / feed** | `fal-poster --quality=low --size=square\|portrait` | survivor → `--variants=2..4` at medium for sibling formats | Fal spine; WF-08 handles the full format pack |
| **Product / photoreal** | `higgsfield-soul` draft (~$0.10), attach character/product ref | more takes on the survivor; Nano fallback if Soul over-stylizes | `cost_gate check --service higgsfield-soul` → `higgsfield_budget_guard check --operation image_preview --count 1` → MCP `generate_image` → both logs |
| **Packaging** | `fal-poster --quality=low --style=packaging-mockup`, `--refs=` for brand book | winner → high; material/finish tuning via WF-07 mask edits | Fal spine |
| **Video / motion** | **no draft** — lock the winning still first | Kling (multi-shot, ≤$2) · Seedance-720p (single, ≤$3) · Cinema (needs-approval) | `fal_budget_guard check --mode=<kling\|seedance-720p>` → wrapper → `fal_budget_guard log`; Cinema via `cost_gate approve` |

## Output Requirements

This stage writes ONE named block — the **GENERATION RUN** — into the accumulating Studio Job. WF-07 (critique) consumes the rendered file paths; WF-08 (format pack) consumes the promoted winner.

```markdown
## GENERATION RUN — [design name / surface]

### Runbook (ordered, as executed — draft → promote)
1. DRAFT · dir-01 (fal-poster, low) — check ✓ auto → node generate.js --brief=dir-01.json --quality=low → out/…_v1.png → logged ✓
2. DRAFT · dir-02 (higgsfield-nano) — check ✓ auto → MCP generate_image → job <id> → logged ✓
   … one line per fired call …
N. PROMOTE · dir-01 winner (fal-poster, high) — check ✓ (self-confirm) → run → out/…final.png → logged ✓

### Spend Ledger
| # | Direction | Service | Pass | Tier (q / dur) | Est $ | Gate verdict | Actual $ | Output file | Logged |
|---|---|---|---|---|---|---|---|---|---|
| 1 | dir-01 | fal-poster | draft | low | 0.011 | auto | 0.011 | out/…_v1.png | ✓ |
| 2 | dir-02 | higgsfield-nano | draft | — | 0.05 | auto | 0.05 | job <id> | ✓ |
| 3 | dir-01 | fal-poster | promote | medium ×4 | 0.16 | auto | 0.16 | out/…_v1..4.png | ✓ |
| 4 | dir-01 | fal-poster | final | high | 0.17 | self-confirm | 0.17 | out/…final.png | ✓ |
|   |          |            |       | **TOTAL** |  |  | **$0.39** |  |  |

### Reconciliation
- cost_gate status: session $__ / daily $__ ·  fal_budget_guard: cycle $__ / wallet $__ · higgsfield: __ credits
- Winner(s) handed to WF-07 (critique) → WF-08 (format pack): [file paths]
```

The block is complete only when: every fired call has both a runbook line and a ledger row, every row's `Logged` is ✓, the TOTAL reconciles against `cost_gate status` + `fal_budget_guard status`, and no direction was promoted before it survived the free WF-07/flip-test cull. A run that "produced lots of images" but skipped the draft-first ladder is a cost-discipline failure regardless of output count.

## Cost & Safety

This is the trigger stage — and even here the rule holds: **nothing auto-fires.** Every paid call is a human-in-the-loop `check → approve(if needed) → run → log`.

```bash
# canonical spine for ANY paid call
python3 execution/cost_gate.py check --service <fal-poster|fal-edit|fal-rembg|higgsfield-soul|higgsfield-nano|higgsfield-cinema|fal-kling|fal-seedance-720p> --request "<task>"
# on USER APPROVAL NEEDED: surface to Farrice, and ONLY after explicit yes →
python3 execution/cost_gate.py approve --service <id>            # token ~15 min
# … run …
python3 execution/cost_gate.py log --service <id> --status success --actual-cost <n>

# Fal services: the check delegates to fal_budget_guard (pass --quality/--n), and the $ accounting is recorded there:
python3 execution/fal_budget_guard.py check --mode=<poster|edit|rembg|kling|seedance-720p> [--quality=<..> --n=<..>] [--duration=<N> --audio=<off|on>]
python3 execution/fal_budget_guard.py log   --mode=<..> [flags] --status=success --actual-cost=<n>
```

Hard rules (from genius.md § Cost Discipline):
- **Never auto-fire.** No paid render without the gate + a human yes.
- **`seedance-1080p` is HARD-BLOCKED** at the script level (~$10/call). Do not attempt it; use `seedance-720p`.
- **DENIED = surface + stop.** Report the denial to Farrice; do not retry or route around a cap.
- **An approve token lasts ~15 min** — if it expires, re-approve; do not stockpile tokens.
- **Draft cheap, promote the winner.** low/Nano to scout · `--variants` for siblings · medium for review · high for finals only (then upscale externally — Topaz/Real-ESRGAN, not in this skill).

## Related Workflows

**Studio stages** (this is WF-06 — the money stage):
- WF-04 — model route (`creative_router.py`) → the MODEL ROUTE block this consumes (upstream)
- WF-05 — prompt compile → the COMPILED PROMPTS block this fires (upstream)
- WF-07 — `/fantastic-critique` → judges each render, prescribes mask-edit REFINE or REGENERATE (downstream; its paid re-rolls loop back through this stage)
- WF-08 — format pack → takes the promoted winner into feed/story/hero/print/cutout/motion
- WF-00 — `/fantastic-studio` (front door orchestrating 01→08)

**Composed judgment (free, gates promotion)**: `/satori-flip-test` · `/satori-lift-audit` (`skills/satori-graphics/workflows/01-lift-audit.md`).

**Instruments & guards (the real code this stage drives)**: `generate.js` · `fal_video_kling.py` / `fal_video_seedance.py` · Higgsfield MCP (`generate_image` / `generate_video` / `models_explore`) · `cost_gate.py` · `fal_budget_guard.py` · `higgsfield_budget_guard.py` · `creative_router.py`.

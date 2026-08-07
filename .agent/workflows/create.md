---
name: create
description: "Universal Content Conductor — thin front door for ANY content deliverable (education, value, aha, personal-brand, client, campaign). Composes existing engines (farrice-engine, jw-engine, aha-engine, oe-teach-to-sell-engine, novelty-forge, writers-room) rather than rebuilding them. Guarantees contextual richness, live zeitgeist grounding, and at least two engineered outcomes per piece."
routing: core
---

# /create — The Universal Content Conductor

A THIN CONDUCTOR, not a new engine. It never writes copy itself — it gates the outcome contract, loads real context, forces live zeitgeist research, routes to the right existing expert stack, then hands off. Never rebuild what a named engine below already does well.

## Invocation

```
/create <topic or request>
/create education "<topic>" --audience <who>
/create client "<topic>" --project <slug>
```

If purpose class is ambiguous, Stage 0 asks one question round — never guesses silently on client or campaign work.

---

## Stage 0 — OUTCOME CONTRACT (gate, always runs)

Declare, in order:
1. **Purpose class**: `education | value | aha | personal-brand | client | campaign`
2. **Audience**: default = Deep ICP "Invisible Expert" (`_active/linkedin/01-research/deep-icp-profile-invisible-expert.md`) for personal work; for client work, the client's own CLAUDE.md ICP (see Stage 3 table).
3. **Minimum TWO engineered outcomes**, written as testable statements — not vibes. Example: "positions Farrice as the only voice naming X to Y" + "drives N replies/booked calls this week."

No contract from the request → sharpen with one question round (Chain Step 2 rules apply), then proceed. Do not skip this stage for "just a quick post" — Score/DICE logic from CLAUDE.md Step 1 still applies underneath it.

---

## Stage 1 — CONTEXT RICHNESS (deterministic, always runs)

Run in order, inject results as context for every later stage:

```bash
python3 execution/memory_facade.py "<topic + purpose>" --top 10
python3 execution/thought_bank.py list --days 14
```

Then read:
- `.agent/cos/goals.json` + the latest entry in `.agent/cos/briefs/` (current goals/commitments — pick the newest date)
- `FARRICE.md` for personal-brand/education/value/aha work; for client work, `cd` into the client's project and read its own `CLAUDE.md` instead (see table: `_active/clients/andrea-dj/CLAUDE.md`, `_active/clients/jen-listings/CLAUDE.md`, `_active/farrice-brand/CLAUDE.md`)

---

## Stage 2 — ZEITGEIST (live, never optional, never from training memory)

0. **Today's zeitgeist brief first (free)** — check `deliverables/research-briefs/zeitgeist-*/` for a brief ≤48h old matching the topic's lane (the 06:20 engine already paid for it). Fresh brief → its evidence rows + decision layer ARE your live signals; skip step 0b. Stale/missing/off-lane → **0b: one cheap live pull** (`python3 execution/apify_client.py twitter "<topic>" --limit 30 --pulse-mode` or `threads-search`, ~$0.02) — budget-gated, and `fallback: true` means skip silently and continue with steps 1-3 (never block on it). Full protocol: `directives/live-data-grounding-protocol.md`; suppress with `--no-live`.
1. `mcp__recall__search` on the topic — grounding cards, cite don't fabricate.
2. `mcp__perplexity-ask__perplexity_search` with a recency filter — what's live THIS WEEK in the niche.
3. For deeper/strategic pieces: `python3 execution/research.py "<question>"` (Gemini-primary, receipt-carrying — never Perplexity-first per `feedback_research-priority-gemini-primary`).

**Output a zeitgeist brief before drafting**: 3-5 live signals, each with source + date + VERIFIED/LIKELY label, plus 1-2 tension points (what people are getting wrong right now — this is the curiosity fuel for Stage 4's open loops). Signals from step 0/0b carry their actor receipts (source URL + engagement numbers), not paraphrase.

Optional novelty lens if the topic is old/saturated: `skills/kallaway-illusion-of-novelty` (front door `/novelty-forge`) or Kallaway jackpost mechanics (`skills/kallaway-content-psychology`).

---

## Stage 3 — ROUTE (compose, don't inline)

One author writes the body. Diandra (`skills/diandra-*`) is hooks à la carte only — never wired into body copy or a multi-expert sandwich (`feedback_diandra-hooks-only-separation`).

| Purpose class | Engine / expert stack | Real asset |
|---|---|---|
| `aha` | Kobi Brown universal aha engine | `.agent/workflows/aha-engine.md` → `skills/kobi-brown-educational-virality/` |
| `education` / teach | Omar Eltakrori teach-to-sell + How-I-Write altitude stack | `.agent/workflows/oe-teach-to-sell-engine.md` → `skills/omar-eltakrori/` + `.agent/workflows/how-i-write.md` (alias `how-i-write-os.md`) |
| `value` / authority | Kallaway content psychology + Justin Welsh / Lara Acosta lanes | `skills/kallaway-content-psychology/`, `skills/justin-welsh-solopreneur/`, `skills/lara-acosta-content-system/` (or `lara-acosta-linkedin-growth/` for growth-specific asks) |
| `personal-brand` (Farrice) | Farrice's own master OS — specialist lane, not reinvented here | `.agent/workflows/farrice-engine.md` |
| `client` | Client CLAUDE.md constraints + production-sheet format (per-asset cards: Hook/caption/on-screen/shot — never a prose blob, per the client-content-production-format memory rule) | Client project folder + its `CLAUDE.md` |
| `campaign` / persuasion | John Whiting propaganda engine — any objective, ethics-gated | `.agent/workflows/jw-engine.md` → `skills/john-whiting-propaganda-machine/` |
| refinement of an existing draft (any class) | Writers' room — never production-from-scratch | `.agent/workflows/writers-room.md` |

Narrative/story pieces may also pull the story-stack (Runia → Hawley → Stanton) available inside the How-I-Write OS — do not hand-wire it here; let the composed engine pull it if it needs it.

---

## Stage 4 — PRODUCE

Follow the proven recipe: **scaffold × parallel-depth × expert-lens × voice-rules × dual-QA**. Required benchmark read before drafting: `_active/linkedin/04-deliverables/content-os/ai-boom-content-package.md`.

Voice rules (house standard, already in memory): Show > Tell, reader-as-protagonist, no forced jargon, 3-variant process (content-voice-calibration memory note).

Curiosity-driven structure: open the piece on one of Stage 2's tension points as an open loop; resolve it using the engine composed in Stage 3, not generic structure.

---

## Stage 5 — GATE

1. `python3 execution/prose_classifier.py check <file>` — AI-slop ban bank enforcement.
2. Claim-risk check fires automatically inside finalize for health/medical/technical-fact content (Chain Step 5.5).
3. **Outcome Contract Check** — re-read the two outcomes declared in Stage 0. Name explicitly how the piece serves BOTH. If it only serves one, run one surgical revision pass (not a rewrite) before finalizing.
4. Chain finalize:

```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [expert-name] --skill [skill-dir] --workflow create \
    --type Content --intent [1-10] --expert-score [1-10] --adversarial [1-10] --sub-agents [measured count] \
    --notes "[what worked/didn't] | Outcome Contract: [both outcomes named] | Factual Grounding: [1-10] | Verification: [PASS/FAIL/PARTIAL/N/A]"
```

---

## Anti-Patterns

- Do not draft before Stage 2's zeitgeist brief exists — "true ear to the ground" is the whole point of this conductor.
- Do not invent a routing lane not in the Stage 3 table — if the purpose class doesn't fit, ask Farrice rather than freelancing a new stack.
- Do not let `/create` grow craft of its own. If a gap appears repeatedly, extend the relevant composed engine, not this file.

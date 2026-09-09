---
name: "gb-intake"
description: "Client intake → free personalized mini-report inside the 48h promise: reads the frozen-shape intake-pack, seeds the radar from their own answers, bakes the mini, stages a Gmail DRAFT (never sends). Paid chain fires only on Farrice's explicit call."
expert: "Growth Blueprint OS"
produces: "growth-lab/<client-slug>/exports/mini-report.html (+ PDF, Drive link, Gmail DRAFT)"
---

# Growth Blueprint OS — Intake → Free Mini (manual fire)

The delivery arm of the intake engine (`growth-lab/intake/INTAKE-ENGINE.md`). A submission
became `growth-lab/<slug>/intake-pack.md` via `intake_bridge.py pull`; this workflow turns
it into the promised deliverable. **Nothing here sends, publishes, or charges.** The
terminal artifact is always a DRAFT Farrice reviews and sends himself.

## Pre-Flight Gate

- **Intake-pack exists?** Read `growth-lab/<slug>/intake-pack.md` fully. No pack → stop;
  run `intake_bridge.py pull` first (the pack, not the raw Sheet row, is the input contract).
- **48h clock.** The pack's provenance header carries the elapsed/remaining time. Past or
  near the promise → say so in one line and prioritize shipping the mini over enriching it.
  The promise is the turnaround, not the data tier.
- **Confidential-input boundary (binding).** This tier collects business answers only —
  NO client file uploads, analytics exports, or internal documents. If the client attached
  or offered files anyway: do not open them; note it for Farrice. Owned-metrics intake
  (IG/TikTok/YouTube exports per gb-interview's client adaptation) is a PAID-engagement
  kickoff step, after conversion, behind the manual READY/HOLD gate.
- **Tier?** Default is FREE MINI. The paid chain runs only when Farrice explicitly says
  this client paid (or approved paid scope). Never infer it from enthusiasm.

## Skill Acquisition

Load `genius.md` (honesty tiers, receipts discipline). The mini itself is deterministic —
`build_lead_magnet.py` owns the bake; this workflow's craft surface is the draft email and
the label honesty. Brief any dispatched subagent negatively: no Chain, no finalize, no
Notion, no Next Moves, return only the artifact.

## Execution — FREE MINI (default)

1. **Seed the radar from their own answer.** The pack's §Known competitors/creators
   section lists parsed seeds. Verify each handle exists before adding (a typo'd handle
   poisons the pack):
   `.venv/bin/python3 execution/outlier_radar.py add-channels --niche <slug> @h1 @h2 ...`
   then `.venv/bin/python3 execution/outlier_radar.py refresh --niche <slug>`.
   No parseable seeds → seed from the niche named in Q1/Q2 using known channel lookups,
   and say so in the operator note (their seeds beat ours; ask in the delivery email).
2. **Bake the personalized mini.** Niche label in THEIR words (Q2/Q7 language, not ours);
   CTA = `payment_url` from `growth-lab/intake/faces-config.json`, or the documented
   mailto fallback while unset:
   `.venv/bin/python3 execution/build_lead_magnet.py --pack .agent/outlier-radar/packs/<slug>/latest.json --niche-label "<label>" --cta-url "<url>" --out growth-lab/<slug>/exports/mini-report.html`
   A degraded/thin pack bakes the interview-only variant — ship it anyway, inside the
   promise, with its honest "data refresh pending" line intact.
3. **PDF of record.**
   `.venv/bin/python3 execution/export_growth_package.py pdf growth-lab/<slug>/exports/mini-report.html`
4. **Delivery surfaces.** Upload the PDF (and/or HTML) to Drive via the gws CLI; capture
   the share link. Then stage a **Gmail DRAFT** to the client's email (from the pack
   header) — never send, never schedule.
5. **Draft email shape** (reader-pure; adapt, don't template-stamp):
   - Subject: their niche + "your mini-read" — no hype words.
   - Body: one line naming what was measured (channels/window, from the pack receipts) ·
     the Doc/PDF link · one genuine observation from THEIR data (quote the number) ·
     the upsell slot: one sentence offering the full artifact they selected on the form,
     with `payment_url` when set, else "reply and I'll set it up" · sign-off. No sequence
     language, no scarcity, no "just checking in" scaffolding.
6. **Mark handled.** Tell Farrice the draft is staged; after he sends, he writes the
   `Status` cell in the Sheet (that clears the pending count deterministically).

## Execution — PAID CHAIN (only on Farrice's explicit call)

Fire the routed chain from the pack's Engagement-routing block (table:
`INTAKE-ENGINE.md` §Routing): e.g. Growth Blueprint = `/gb-interview` →
`/gb-whitespace` → `/gb-bullseye` → `/gb-topic-scan` → `/gb-format-find` →
`/growth-blueprint`. The intake-pack pre-loads the interview: fold its [V] answers into
reflect-backs and interview only the gaps + the two interview-fallback sections (Target
Authority Statement, Delivery style). Owned-metrics request goes out at THIS kickoff,
not before.

## Output Contract

- `growth-lab/<slug>/exports/mini-report.html` + `exports/pdf/` PDF — the deliverable.
- Drive link + **Gmail DRAFT staged, never sent** — the delivery. Auto-send is a
  contract violation, not a shortcut.
- Manifest untouched by this workflow except what `intake_bridge.py` already wrote;
  paid-chain artifacts update it via their own workflows.
- One-line close to Farrice: client · elapsed vs 48h · mini mode (full/interview) ·
  draft staged where · what the upsell sentence offers.

## Quality Gate

- **Reader purity:** the mini and the draft email carry zero operator language, zero repo
  paths, zero tool names — `execution/client_package_lint.py` standard applies to
  anything the client will see.
- **Honest labels:** every number in the draft comes from the pack or the bake receipts;
  degraded bake = degraded language ("data refresh pending"), never borrowed confidence.
- **Verbatim respect:** where the email mirrors their situation, use their words from the
  intake-pack [V] lines — never an elevated paraphrase.
- **The two hard checks:** DRAFT not sent · no client files opened at this tier.

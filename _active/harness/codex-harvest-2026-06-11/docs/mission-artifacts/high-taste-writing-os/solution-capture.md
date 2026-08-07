# Solution Capture: High-Taste Writing OS

Created: 2026-05-10
Mission: high-taste-writing-os

Use this while context is fresh. If the learning is generalizable, copy or convert it into `docs/solutions/`.

## Track
- Type: workflow / architecture

## Symptoms Or Context
- The system had strong writing, copy, taste, and retention experts, but outputs still read as structurally sound and low-taste because the experts were applied as labels or broad passes rather than a composed sequence.

## What Did Not Work
- More expert names did not improve prose by itself.
- Copy Gate scoring improved confidence control, but it did not solve flow, taste, interweaving, or sentence craft.
- A single anti-slop check catches some generic patterns but cannot compose a compelling piece.

## Working Solution Or Durable Guidance
- Use a companion OS: one composer owns the piece; specialists provide narrow line-level passes; final output includes a Taste Evidence Ledger.
- Run the OS before Publishable Copy Gate when the issue is composition quality, not conversion mechanics.
- Treat material quality as the bottleneck: reader private sentence, concrete artifact, proof/demo moment, refusal, worldview sentence, and market tension.

## Why This Works
- It turns expert stacking into handoff architecture. The OS forces input quality, architecture, and sentence craft before scoring. That makes "taste" operational instead of aspirational.

## Prevention Or Reuse
- `/high-taste-writing-os` is wired into Writing Agent, Copywriting Agent, Publishable Copy Gate, Autopilot, and Orchestrate.
- `execution/verify_high_taste_writing_os.py` protects bridge and route discoverability.

## Generalization Decision
- Keep mission-local: no.
- Promote to `docs/solutions/`: yes, `docs/solutions/high-taste-writing-os.md`.

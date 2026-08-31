# Matt Haig Reader Bridge — Human A-Tier Verdict

## Verdict

**PASS — A-TIER PROMOTION EARNED THROUGH THE PREFERRED PATH.**

Farrice judged the full repair and the published-corpus spot-check without being shown the mappings. The system passage was detectable as patterned, but it was preferred alongside one real passage and over another real passage. The forge standard permits `indistinguishable or preferred`; this result passes through preference, not imitation.

## Test 1 — Full-Scene Repair

| Blind label | Hidden mapping |
|---|---|
| A | `proof/fixture-01-output.md` — initial model output |
| B | `proof/fixture-01-output-round2.md` — bounded repair |

Farrice's judgment:

- B was easier to read.
- A jumped around and its ending was too vague to make the literal event clear.
- A sometimes painted a stronger picture.
- B had the better ending overall.

**Interpretation:** the repair improved reader access and causal legibility. The retained caution is to preserve A's stronger images when they do not obscure the event.

## Test 2 — Published-Corpus Spot-Check

| Blind label | Hidden mapping | Provenance class |
|---|---|---|
| X | Official Penguin Random House Matt Haig sampler | Real published work |
| Y | Reader Bridge fixture 01, round 2 | Skill-generated |
| Z | Matt Haig's Guardian Christmas essay | Real published work |

Farrice's judgment:

- X and Y both felt system-patterned.
- Z felt disjointed, repetitive, and almost imitative.
- He wanted to continue reading X and Y.

**Interpretation:** Y was not indistinguishable, but it was preferred. That satisfies the explicit A-tier pass rule without authorizing Haig voice imitation.

## Promotion Basis

| Requirement | Result |
|---|---|
| Structural verifier | PASS |
| Heartbeat | 7/7 PASS |
| Provenance corpus | Four pieces; two used in the human spot-check |
| Model blind repair | EVAL-064 FAIL → EVAL-065 PASS |
| Farrice human judgment | EVAL-066 PASS |
| Generated work indistinguishable or preferred | PREFERRED |
| Voice imitation | NOT USED |
| Reader or market outcome | NO EVENT |
| Chain closeout | PASS — 8.67/10, trace `trace_20260828_192010_matt-haig-reader-bridge.json` |

## Locked Learning

Use plain causal legibility before conspicuous metaphor. Preserve specific images, but remove imagery that makes the reader stop to decode the literal event. A real source passage can be less compelling than generated work; provenance is calibration, not automatic superiority.

## Evidence Boundary

A-tier means human-calibrated source-mechanic embodiment inside this skill system. It does not establish Matt Haig endorsement, voice equivalence, publication quality across every format, reader response, sales, or market performance.

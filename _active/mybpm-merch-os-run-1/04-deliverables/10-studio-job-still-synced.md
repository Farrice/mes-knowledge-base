# Studio Job — MY.BPM Week-1 "Still Synced" (live /fantastic-studio run)

> First real run of the **Fantastic Studio** pipeline (fantastic-posters v2). Ingested the satori Production Brief in [09-week1-drop-hero-brief.md](09-week1-drop-hero-brief.md), diverged into 3 orthogonally-distinct directions, routed each to the right model, and generated real images — cost-gated, $0.15 total.
>
> **Satori decided. The router picked the instrument. The studio critiqued its own work.**

---

## Stage 0-2 — Frame + Art-Direct (ingested from satori)

- **Surface**: launch hero / ad creative (Meta + IG + Shopify + Email-1).
- **Hidden truth** (satori): *the real thing isn't the night you went out — your body never fully came back; your resting heart rate is still running the set's BPM.*
- **Color tokens**: `#E9E2D2` cotton · `#16181D` ink · `#007FFF` electric blue (accent, one zone) · `#5A5F66` graphite.
- **Strategic bet**: STAND OUT from the neon-rave monopoly via premium restraint.

## Stage 3 — Divergence Spread (the anti-redundancy proof)

Three directions varying on ≥3 orthogonal axes — **strangers, not tints**:

| Dir | Concept angle (A1) | Lineage (A2) | Composition (A3) | Register (A6) | Model (A5) |
|---|---|---|---|---|---|
| **A · Flatline Ignition** | emotion-over-info: flat line → alive | Swiss / medical-precision | negative-space, single hero line | premium-restrained | GPT Image 2 |
| **B · Body Still Running It** | hidden-truth via a *person* | editorial documentary portrait | image-dominant, soft daylight | quiet / eerie recognition | **Higgsfield Soul** |
| **C · Riso Flyer** | one-big-idea, insider | risograph / DIY rave zine | full-bleed collage, huge type | loud / in-group | GPT Image 2 |

Diversity self-check: **PASS** — no two collapse into one concept sentence; each would live on a different surface (A=Shopify hero, B=lifestyle/IG, C=flyer/story).

## Stage 4 — Model Route (multi-model proof)

`creative_router.py` resolved each direction live:
- A "swiss minimal typographic poster…" → **fal-poster** ✓
- B "photoreal portrait of a person… blue pulse…" → **higgsfield-soul** ✓ (the people-routing added this session)
- C "risograph DIY rave flyer…" → **fal-poster** ✓

## Stage 5-6 — Compile + Generate (cost-gated, real)

Compiled to `briefs/mybpm-A-flatline.json` and `briefs/mybpm-C-riso.json` (Fal `--brief`), and a Soul prose prompt (B).

| Dir | Model | Cmd | Quality | Cost | Output |
|---|---|---|---|---|---|
| A | Fal GPT Image 2 | `generate.js --brief=mybpm-A-flatline.json` | medium | $0.040 | `out/swiss-minimal-typo_1783181469003_v1.png` |
| C | Fal GPT Image 2 | `generate.js --brief=mybpm-C-riso.json` | low | $0.011 | `out/indie-gig-riso_1783181507117_v1.png` |
| B | Higgsfield Soul (`text2image_soul_v2`) | MCP `generate_image` | 1080p/2k | $0.100 | `out/mybpm-B-soul_still-synced.png` |

**Total: $0.151** (cost_gate: check → approve → run → log for each; wallet unaffected materially).

## Stage 7 — Critique + Refine (the loop)

| Dir | Virgil | LIFT | Type/legibility | Anti-slop | Verdict |
|---|---|---|---|---|---|
| **A** | ✅ clear POV, tension (flat→alive), Swiss anchor | ✅ blue ignition wins in <2s | ✅ full 8-word headline clean, EKG morphology (not equalizer) | ✅ hand tremor, uneven peaks | **SHIP-grade** — the perception-gap fix (EKG not equalizer) held |
| **B** | ✅ cinematic, "morning after" tension | ✅ pulse is the one saturated leverage | n/a (headline goes in the negative space above) | ✅ 35mm grain, natural imperfection | **SHIP-grade** — Soul delivered a photoreal portrait GPT Image 2 can't |
| **C** | ✅ insider energy | ✅ type-dominant | ⚠️ "strangers" slightly garbled; invented date "05.24.24" | ✅ authentic riso off-register | **REFINE** — masked re-render of the subtitle + drop the date (`--input` + `--mask`) |

The C findings are the loop working: a targeted `--mask` edit fixes the text region without re-rolling the whole image.

## Stage 8 — Format Pack (plan)

Winner (A) → deployment set, cheap→final: feed 4:5 (`--size=1024x1280`), story 9:16 (`--size=1024x1792`), Shopify hero (`--size=hero-2to1`), print (`--size=poster-xl` @ high), transparent wordmark (`--rembg`), motion (poster-to-video, cost-gated). B → the lifestyle/IG cut. C → the story/flyer cut (post-refine).

---

### What this run proved
1. **Concept-first, not template**: A carries the satori hidden truth, not a filled-in style. 2. **Divergence, not tints**: A/B/C are strangers. 3. **Multi-model**: the person direction routed to and rendered on Higgsfield Soul; posters on Fal. 4. **Self-critique**: C caught its own text flaw with a concrete refine command. 5. **Cost-safe**: every generation gated + logged; $0.15 total.

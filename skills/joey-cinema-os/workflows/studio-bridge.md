---
description: "/jcin-studio-bridge — integration run: fantastic-studio stages 04 (model route) / 05 (prompt compile) hand photoreal-people and Seedance work into the Joey pipeline and get assets back; the Higgsfield MCP paste-and-attach loop (generate_image / generate_video / show_characters / show_reference_elements); Fal-surface fallback (strip @tags to prose); explicit when-NOT-to-bridge boundaries"
---

# Studio Bridge (Joey Cinema OS)

The system already has an image factory: fantastic-studio's eight stages art-direct, diverge, route, compile, generate, critique. What it never had is a consistency layer — stage 04 can route a direction to "Higgsfield Soul, people/faces" and stage 05 can compile a gorgeous one-off prompt, but the same face won't survive the second generation. This workflow is the interchange: when a studio session's routing lands on **photoreal people** or **Seedance video**, the compile step can hand off to the Joey pipeline (locked references + banana-pro/worldbuilder grammar) and receive identity-stable assets back into the studio's critique and format-pack stages. It also documents the two execution surfaces — the Higgsfield MCP paste-and-attach loop where `@tags` are native, and the Fal fallback where they must be stripped to prose. Per the no-forced-wiring rule: everything here is an OPTION the conductor offers with a reason. No studio session is ever required to bridge, and no Joey session is ever required to start in the studio.

## Pre-Flight

Read before executing:
1. `skills/joey-cinema-os/SKILL.md` (§ Surfaces & Gates, § Stacking Guide — the fantastic-studio row) and `genius.md` (§ System Fit — division of lanes + the GPT-2 disambiguation)
2. `.agent/workflows/fantastic-model-route.md` and `.agent/workflows/fantastic-prompt-compile.md` (stage front doors; full specs at `skills/fantastic-posters/workflows/04-model-route.md` and `05-prompt-compile.md`)
3. `skills/higgsfield-creative-studio/SKILL.md` (§ Credit Guard, § Tool Routing — the MCP/CLI bridge discipline this run inherits)
4. `directives/higgsfield-usage-policy.md` + `python3 execution/higgsfield_budget_guard.py check` before ANY real MCP generation

> 🔒 **Pre-Flight Gate** — route before you bridge:
> 1. **Is this even the right lane?** Run the when-NOT-to-bridge table (Step 5) first. Stylized/typographic posters and layout/text-dense work have owners already; bridging them here produces worse output at higher cost.
> 2. **Disambiguation check.** Joey's "GPT-2" = **Higgsfield GPT-2** (face-fidelity king, credit-heavy). The system's `gpt-image-2-director` = **OpenAI GPT Image 2** (layout/typography king, weak faces). Opposite verdicts — a routing note that says "GPT-2" without a surface name is a bug; resolve it before compiling.
> 3. **Identity inventory.** Bridging photoreal people with no locked reference means the first bridge deliverable is a lock build (`/jcin-character-lock`), not a render. Say so up front — it changes the cost estimate.

## Input Required

- The incoming work: a fantastic-studio direction (stage 03/04 output), a bare brief, or a Joey-pipeline asset wanting studio polish (the reverse bridge)
- Routing verdict if one exists — `creative_router.py` output or the stage 04 note naming the surface
- Identity inventory: locked references that already exist for the subjects in play (paths + tag names), or "none"
- Surface availability: Higgsfield MCP session live, or Fal-only run
- Budget state: `python3 execution/higgsfield_budget_guard.py check` output, so the bridge offer carries an honest cost line

## Skill Acquisition

Load the production skill for whichever layer the bridged work enters: `skills/banana-pro-director/SKILL.md` for stills, `skills/cinema-worldbuilder-pro/SKILL.md` for video — their blocks are LOCKED verbatim grammar; compile through them, never paraphrase them. `execution/creative_router.py route --task "<task>"` is the deterministic dispatcher underneath stage 04 — its output names the surface and prints the cost-gate pre-flight; trust it over vibes.

## Execution

### Step 1: Catch the handoff (studio → pipeline)
A fantastic-studio session bridges when stage 04's routing verdict for a direction is **photoreal people/faces** (routed toward Higgsfield Soul / GPT-2-class face fidelity) or **Seedance video**. At that point, offer the bridge in one line: *"This direction is identity-bearing — compile it through the Joey pipeline so the face/product holds across variants? (Option, not required — a one-off can stay in the studio.)"* One-off hero image with no reuse intent → no bridge; the studio's own compile is cheaper. Accepted bridge → the direction's art-direction spec (stage 03 output) travels with it.

### Step 2: Compile through the pipeline grammar (replaces stage 05 for this direction)
- **Stills:** the art-direction spec compiles through banana-pro grammar — existence question, face lock / product lock first if missing, then the scene plate or sheet prompt. The studio spec's mood/palette language survives as scene-level direction; identity language is REPLACED by references (the spec's "confident woman, 30s, warm smile" becomes an attached `@founder_ref` — names/ages never enter the prompt).
- **Video:** the spec compiles through worldbuilder block order, mode-matched, FOV from the degree ladder, costed runtime declared. Multi-beat → `/jcin-shot-plan` first.
- Either way the studio's remaining stages stay upstream/downstream owners: concept/divergence before the bridge, critique-refine and format-pack after it. The bridge swaps the ENGINE, not the studio.

### Step 3: Execute on the native surface — the Higgsfield MCP paste-and-attach loop
The MCP surface is Joey's home turf; the loop that makes it compound:
1. **Generate** the identity asset: `generate_image` (guarded) from the banana-pro prompt.
2. **Bank it:** confirmed outputs become reference elements — `show_reference_elements` lists the element library, `show_characters` lists character slots; a kept face lock gets saved as a character/element, not left as a loose generation (`show_generations` finds strays).
3. **Attach and tag:** in the next prompt, worldbuilder `@tags` map one-to-one onto attached elements — upload/attach the reference under the tag name the prompt uses (`@sol_ref` in the prompt = the sol reference element attached). The prompt is pasted as one code block; Seedance reads each `@tag` at its anchor point.
4. **Iterate one variable at a time**, re-attaching the SAME elements — that's the consistency mechanism, not prompt willpower.
5. Every generation: `higgsfield_budget_guard.py check` before, `log` after. No exceptions; the skill's job ends at the code block and the human triggers spend.

### Step 4: Fal-surface fallback (when MCP isn't the runway)
Fal wrappers (`execution/` fal scripts via `creative_router.py`) have **no element/@tag system**. To run a pipeline prompt on Fal: strip every `@tag` and replace it with the reference's prose descriptor from its lock (the 3-panel sheet's identity language IS that descriptor — this is why locks are written as prompt-ready payloads). Pass reference images through the wrapper's own `--reference`-style flags where they exist. Expect weaker identity hold; budget an extra take. **seedance-1080p on Fal is HARD-BLOCKED by the budget guard** — video fallback means a different model or back to the MCP surface, never a bypass.

### Step 5: Hand assets BACK (pipeline → studio)
Bridged outputs return to the studio flow as first-class citizens: into `/fantastic-critique-refine` for the self-critique pass (its verdicts feed prompt iteration — remembering the bell curve: 3 failed iterations → reset, don't patch), then `/fantastic-format-pack` for crops/formats. New locks built during the bridge get REGISTERED (project folder + tag name + surface location) so the next studio session's stage 04 knows the identity already exists — the bridge's compounding payoff.

### When NOT to bridge (boundaries are the feature)

| Work | Stays with | Why |
|---|---|---|
| Stylized / typographic / illustrated posters | `fantastic-posters` (Fal / GPT-Image-2, 38 styles) | Style-first work has no persistent identity to protect; the poster lane is cheaper and better at it |
| Layout-heavy, text-dense, UI mockups, infographics | `gpt-image-2-director` (OpenAI GPT Image 2) | Layout/typography king; Higgsfield-lane models render weak text |
| One-off hero image, no reuse intent | fantastic-studio stages 05–06 as-is | Lock-building overhead buys nothing a single render needs |
| Marketing Studio preset video ads (UGC/Unboxing/TV Spot) | `skills/higgsfield-creative-studio/SKILL.md` router → `marketing-studio-director` | Preset paragraph format ≠ worldbuilder block grammar; don't force one into the other |
| Real-footage edits (≤10s, "keep me the same, change X") | Higgsfield Omni, plain imperative prompts | The register flip: edit prompts are simple; cinema grammar actively hurts here |

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| **Studio session, photoreal-people direction** | The canonical Step 1–5 run: bridge offered at stage 04, compile via banana-pro, return via critique-refine. |
| **Studio session, Seedance direction** | Bridge at stage 05: art direction → `/jcin-scene-shot` or `/jcin-story-15s`; runtime + credits declared before the studio sees a prompt; 4K-native vs 1080p decided at generation. |
| **Standing brand world exists (`/jcin-ad-world` built)** | The bridge gets cheap: stage 04 routes, Step 2 skips straight to attach-and-compile against the registered library — inventory before building anything. |
| **Pipeline-first session needing studio polish** | Reverse bridge: Joey outputs into `/fantastic-critique-refine` + `/fantastic-format-pack` only — divergence/art-direct stages add nothing to an already-locked identity. |

## Output Requirements

1. **Bridge decision line** — bridged or not, with the reason (identity-bearing? reuse intent? lane owner?), always phrased as an offer that was taken or declined.
2. **Surface call** — Higgsfield MCP (native, @tags live) or Fal fallback (tags stripped to prose), with the disambiguation resolved by name.
3. **The compiled prompt(s)** in the owning grammar's exact delivery format (banana-pro / worldbuilder code blocks, title + runtime for video).
4. **Attach map** — each `@tag` → which reference element/character slot it maps to on the surface (or the prose descriptor that replaced it on Fal).
5. **Guard trail** — pre-flight command shown before spend, log command after; costs stated per take.
6. **Registration note** — any new lock's path + tag + surface location, so future sessions inventory instead of rebuild.

Execution prompt: references/prompts-v2/seedance-shot.md — honor its Output Contract.

```
STUDIO BRIDGE — [direction / task]

BRIDGE DECISION: [taken / declined] — because [identity-bearing? reuse intent? lane owner?]
LANE CHECK:      [passed — not stylized/typographic, not layout/text-dense]
SURFACE:         [Higgsfield MCP (@tags native) / Fal fallback (tags stripped)]
                 GPT-2 disambiguation: [Higgsfield GPT-2 / OpenAI GPT Image 2 / n.a.]

IDENTITY:        [existing locks reused: @tag → path] · [locks built this run: ...]

COMPILED PROMPT(S):
  [banana-pro / worldbuilder code block(s), exact source-skill delivery format]

ATTACH MAP:
  @______ → [reference element / character slot / Fal prose descriptor]
  @______ → [...]

GUARD TRAIL:     check → [output] · generation [human-triggered] · log → [pending]
RETURN PATH:     [→ /fantastic-critique-refine → /fantastic-format-pack / none]
REGISTERED:      [new lock path + tag + surface location, or "no new locks"]
```

## Quality Gate

> 🛡️ Anchor against `genius.md § Quality Rubric` (**Reference discipline** row) and § Anti-Patterns before delivering.

- **The bridge was an option, audibly** — the offer/decline is in the record; a bridge imposed as a pipeline step violates the no-forced-wiring binding.
- **Right lane confirmed** — nothing stylized/typographic or layout/text-dense crossed the bridge; the when-NOT table was actually consulted.
- **GPT-2 disambiguated by full surface name** everywhere it appears — "Higgsfield GPT-2" or "OpenAI GPT Image 2," never bare "GPT-2."
- **@tags resolve** — every tag in a delivered prompt has an attach-map entry; on Fal, zero @tags survive in the prompt body and each replacement descriptor came from the lock, not improvisation.
- **No layer did another layer's job** — the studio kept concept/critique/format; the pipeline kept identity/grammar; unbuilt identity kicked to `/jcin-character-lock` rather than being faked inline.
- **Every generation guarded and logged** — check before, log after, seedance-1080p never touched on Fal; a render without its guard trail is a violation, not a shortcut.
- **Locks registered** — a bridge that builds identity and doesn't register it forces the next session to rebuild; that's unfinished work.

## Common Pitfalls

- **Bridging everything because the bridge exists.** A one-off stylized poster gains nothing from identity locks and loses the poster lane's strengths. The when-NOT table is a gate, not garnish — most studio sessions never bridge, and that's correct.
- **Letting "@tags" leak onto Fal.** A Fal wrapper reads `@sol_ref` as three literal characters. Strip every tag to the lock's prose descriptor; if the descriptor isn't prompt-ready, the LOCK was written wrong (bible payloads must paste verbatim into their downstream slot) — fix upstream.
- **Conflating the two GPT-2s.** Face work sent to OpenAI GPT Image 2 renders weak faces; typography sent to Higgsfield GPT-2 burns face-fidelity credits on text it renders badly. Opposite kings, opposite verdicts — full surface name every time.
- **Re-describing the attached reference in the compiled prompt.** The studio's art-direction spec arrives full of identity language; compiling means REPLACING it with the tag, not stacking both. A sentence that repeats what the reference shows gets cut unless it's load-bearing for composition.
- **Loose generations.** A kept output that never becomes a reference element (`show_reference_elements` / character slot) is a consistency asset thrown away — the paste-and-attach loop compounds only if step 2 (bank it) actually runs.
- **Using cinema grammar on an Omni edit.** Real-footage video-to-video wants ≤10s of source and a plain imperative ("keep me exactly the same, change the glasses"). The register flip is the rule: generation prompts are dense, edit prompts are simple.

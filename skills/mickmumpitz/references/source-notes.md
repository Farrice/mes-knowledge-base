# Mickmumpitz — Source Notes & Fidelity Ledger

Extraction date: **2026-08-02**. Method: **watched**, not transcript-skimmed — full captions pulled for
all five sources, then frames extracted and read at every moment a workflow, dataset, layout or result
was shown on screen (37 frames across four videos). Frames are what verified the model-sheet shape, the
Blender blocking, the driving-plate composite, the bounding-box control and the CCC version number.

Doctrine applied: **weight 2025–2026 sources; the core must be craft that transcends model/tool
selection.** Tool names, model names, node graphs and version-specific settings are quarantined in
`era-bound-mechanics.md` and appear nowhere in SKILL.md, genius.md, the workflows or the execution
prompts.

---

## Sources (all watched in full)

| # | Date | Title | Length | Views at extraction | URL |
|---|---|---|---|---|---|
| S1 | **2026-07-17** | Create HYPERREALISTIC AI Characters That INTERACT \| FREE & LOCAL | 34:28 | 39,008 | `youtube.com/watch?v=ghFYDG0DF1w` |
| S2 | **2026-03-30** | I Built a FREE VFX Pipeline with Local AI [2026 Masterclass] | 19:12 | 177,109 | `youtube.com/watch?v=_n0ir5V5tX4` |
| S3 | **2025-10-07** | Create HYPERREALISTIC Consistent AI Characters — FREE & LOCAL! [Full ComfyUI Masterclass 2025] | 24:23 | 617,739 | `youtube.com/watch?v=PhiPASFYBmk` |
| S4 | **2025-07-17** | Create CONTROLLABLE AI CHARACTERS for your MOVIES | 17:16 | 118,096 | `youtube.com/watch?v=OhKoh0CsVFo` |
| S5 | **2025-03-07** | Control MULTIPLE CONSISTENT CHARACTERS + CAMERA with this FREE AI Workflow [Blender + ComfyUI] | 26:31 | 204,216 | `youtube.com/watch?v=PZVs4lqG6LA` |

**Recency weighting applied:** S1 and S2 (both 2026) carry the core. S1 supplies the five dataset
rules, the detail-anchor loop, multi-character separateness and checkpoint sampling. S2 supplies the
one-line thesis, the Four Building Blocks, the mask trade-off and the driving-video-as-animation move.
S3–S5 (2025) are mined for durable principles only — blocking, decaying structure, the preview shop,
control-representation choice — and their tool specifics were the first thing to churn.

Video descriptions were pulled alongside the captions and used to **correct caption mis-transcriptions
of proper nouns** (auto-captions rendered Krea 2 as "Crea/Korea 2", Wan 2.2 as "one 2.2/12.2", Qwen as
"Gwen", Ostris as "Austris/ostress", LoRA as "Laura/Allora/Aura"). Corrected names appear only in the
era-bound appendix.

Two additional 2026 uploads exist on-channel and were **not** extracted (out of lane, no gap left):
*We Built a FREE AI Render Engine for CG & Facial Animation* and *Generate ENTIRE AI MOVIES with this
NEW METHOD*.

---

## Verified (in-source, timestamped)

| Claim | Evidence |
|---|---|
| Channel ~182,000 subscribers, handle `@mickmumpitz`, site `mickmumpitz.ai`, Patreon-funded | channel metadata + video descriptions, all five sources, checked 2026-08-02 |
| Free ComfyUI + Blender workflows, actively shipping through Jul 2026 | S1 published 2026-07-17; free-workflow links in every description |
| One reference image → full character dataset (turnaround, poses, emotions, lighting, environments) | **seen on screen** S3 07:07 (5-view turnaround + portrait), S3 08:58 (T-pose, laying, side), S1 05:39–05:48 |
| The dataset is model-agnostic — same folder trained into an image model, a bounding-box model and a video model | S1 02:43–02:45, 30:29–31:57 |
| Five LoRA dataset rules, stated as a numbered list | S1 01:03–02:28, verbatim |
| Caption grammar must match the target model's prompt grammar ("a caption is a reverse prompt") | S1 02:18–02:35 |
| Detail-anchor loop (necklace drifted → targeted close-ups + snipped reference) | S1 06:59–08:19; **seen on screen** at 07:16 (necklace reference node) and 07:56 (`Set_necklace` feeding the graph) |
| T-pose + full-face as the standard reference pair | S1 06:38; **seen on screen** 07:16 (`Get_T-POSE` + `Get_INPUT_FACE` into the edit node) |
| Multi-character separateness taught by including group shots in the dataset | S1 17:29–18:57; **verbatim group-shot prompt read off screen** at 18:05 |
| Bounding-box placement controls composition per character and per object | **seen on screen** S1 29:35 — six drawn boxes: three characters, squirrel, bluebird, mantis, walnut |
| Last checkpoint ≠ best; sample the curve | S1 15:41, 27:22 |
| Camera blocking in 3D before generation, then lighting the layout for mood | S5 09:08–09:32; **seen on screen** 09:05 (layout + camera frustum + posed characters), 09:25 (same frame lit evening) |
| "Good enough" issued deliberately on geometry-only layers | S5 07:29, 07:34 |
| Structure early / freedom late (decaying structural guidance) | S5 12:12 |
| Two-step preview shop (low-step seed selection, then finish) | S4 12:42; live-preview companion S2 11:41 |
| Four Building Blocks (mask · driving plate + ControlNet · references · prompt) | S2 04:04, verbatim |
| Driving plate = subject preserved in colour, composited over structural guidance | **seen on screen** S2 02:45 |
| Mask boundary as the identity/integration trade-off dial, and it can be feathered | S2 12:03–12:31; deliberate inverse at 17:05 |
| Every reference is a vote — ball-shaped reference + ball-shaped mask → literal ball | S2 16:29–16:57 |
| Driving video hand-authored as animation (progressive black-out + drawn white lines) | S2 17:30–17:58; **seen on screen** 17:35 (AE, arm masked black with pose skeleton) |
| Derivation buys compositing — original mask re-blends generated footage frame-accurately | S2 16:09 |
| Don't stack every control; over-constraining kills motion | S4 06:26 |
| Trajectory chosen over pose skeleton for domain width | S4 02:07 |
| Two-pose interpolation as the animation unit | S5 23:05 |
| Prompt-format propagation via LLM ("this is the format, adapt it") | S1 32:53; S2 11:13 |
| The honest-folder standard ("no cherry-picking… these are all the images") | S1 21:21, with the failures scrolled |
| Method works across styles — photoreal, 3D-animated, anime | S1 09:00–09:45 (stylized run); anime result **seen on screen** S1 00:18 |
| Ships a finished short film with major pipeline releases | *Paper Jam* S5 24:33; *The Crystal Cat* S4 16:30 |

---

## UNCONFIRMED — flagged, never used in a prompt's Role & Activation

| Claim | Origin | Status |
|---|---|---|
| **"Consistent Character Creator v4"** | master-hunt dossier entry 4 | **CONTRADICTED by source.** The ComfyUI tab in S3 (2025-10-07) reads `250929_MICKMUMPITZ_CCC_3-0` — **version 3.0**. In S1 (2026-07-17) he calls the successor only *"the new consistent character… the simple version"* and outputs to `ComfyUI/output/CCC/`. No "v4" appears in any source, description or on-screen artifact. **Do not cite a version number.** |
| His real name, nationality, professional background, studio history, client list, education | — | **Absent from all five sources.** Speech is German-accented English and the channel name is a German idiom; that is an observation, not a biography. Assert nothing. |
| Any professional VFX/film credit outside his own channel shorts | — | **Absent.** The only credits observable are his own films: *Paper Jam*, *The Crystal Cat*, plus a third in progress (S4 16:03). |
| Patreon subscriber count, revenue, team size | — | **Absent.** He says "we" throughout and thanks "our Patreon supporters," implying a small team, but no size is stated. |
| Adoption by studios or named clients | — | **Absent.** Views and subscriber count are the only reach evidence. |

---

## Fidelity assessment

**HIGH.** Five long-form sources, 121 minutes total, all watched with frames read at the demonstration
moments. The corpus is unusually well-suited to extraction because it is *demonstrative*: he shows the
input, the failure, the diagnosis and the fix on screen, so the claims verify visually rather than
rhetorically.

Where the corpus is thin, and how that is handled:

- **He never generalises his own method.** The Control Ladder is *this extraction's* synthesis of
  behaviour that is consistent and explicit across all five sources — he names every rung, but never
  arranges them. It is labelled as a house frame in the workflows, not put in his mouth. The Four
  Building Blocks, by contrast, are his own words, verbatim.
- **No taste vocabulary.** He does not teach composition, palette, lighting design or meaning, and
  none has been invented for him. Routing sends taste work to Dave Clark / Nick St. Pierre / Rory Flynn.
- **No stated numbers beyond the era-bound table.** Every threshold he gives is hedged
  (*"at least in my experience"*, *"I think"*) and is quarantined with its date. No workflow or prompt
  in this skill depends on one.
- **Four execution prompts, not ten.** One per deliverable the corpus can honestly carry:
  dataset spec, drift diagnostic, controlled-shot spec, previs/blocking plan. A fifth was considered
  (LoRA training config) and dropped — that deliverable is entirely era-bound settings, which belong in
  the appendix, not in a prompt.

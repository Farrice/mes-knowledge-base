# Era-Bound Mechanics — VERIFY BEFORE USE

**Everything on this page is dated and perishable.** It is recorded so that source quotes stay
traceable, not so it can be executed. No workflow and no execution prompt in `skills/bilawal-sidhu/`
depends on a single line of this file. If a named tool below has been renamed, superseded, or
repositioned, the method in `genius.md` is unaffected — it was never about the tool.

**Last verified: 2026-08-02.** Anything here older than ~90 days should be re-checked before use.

---

## A. The greybox→reskin stack as posted (2025-01-06) [S1]

| Stage | What he used then | The durable requirement |
|---|---|---|
| Build the scene | kitbashed 3D models (application unnamed in the post) | any DCC that can assemble existing parts fast |
| Render | greybox animation | untextured render carrying geometry, motion, camera, timing |
| Reskin | Runway Gen-3 | any video-to-video / video-conditioned model that respects input structure |

His stated observations about that generation of models, **as of January 2025**:
- Gen-3 and Sora handled volumetric fog and lighting effects well — aurora, ground fog, light interaction.
- Materials and lighting were promptable, including environment skybox and key light direction.

Both observations are now three-plus model generations old. The *shape* of the observation — that the
reskin pass buys volumetrics and light, and takes lighting-department direction — is what carries.

---

## B. Named tools across the 2026 corpus (mentions only; none endorsed as a stack)

**Video / world models discussed:** Runway Gen-3 [S1] · Sora [S1] · Google "Omni" multimodal video model
[S4] · Seedance [S4] · Veo / Veo 3.1 [S4, S6] · Google DeepMind Genie 2 and Genie 3 / Project Genie
[S3, S5, S6] · Nano Banana and Nano Banana Pro (image; Genie's image front-end) [S4, S5] · Motion
Stream (direct object manipulation in generation) [S2] · Cat4D (single video → dynamic 3D, Google
DeepMind) [S4] · World Labs, incl. RTFM (environment generation, spatial memory research) [S2, S3, S5].

**3D-first / scene-graph tools he names as building the direction he wants:** Intangible AI (text →
manipulable 3D scene, then generative finish) [S2, S3] · ArtCraft (3D scene block-out for multi-shot
continuity) [S2] · Cascadeur (AI in-betweening / text-to-motion on rigged characters) [S3] · Berkeley's
"Vega" paper (VLM composing a 3D scene from concept art) [S3] · Unreal Engine and Unity as the existing
proof that viewport + timeline + nodes can coexist [S2, S3].

**Node-based tools named in the critique** (as things he respects but considers the wrong abstraction for
composition): ComfyUI · Krea · Weave · Runway · Adobe · Houdini · Nuke · Blender [S2 00:01–02:24].

**Referenced-not-endorsed:** Higgsfield, named as the template approach — good for memes and short form,
exhausting past 3–5 minutes [S2 06:21]. (Note: Higgsfield is a house tool. His critique is of
*templates as a long-form production strategy*, not of the product.)

**Not found anywhere in the corpus:** **SpAItial.** The extraction brief listed it alongside World Labs;
no mention of it appears in any source examined on 2026-08-02. Do not attribute it to him.

---

## C. Reality-capture stack as taught 2026-01-23 [S7]

| Tier | Named then | Why he picked it |
|---|---|---|
| Phone, on-device | Scaniverse (Niantic) | real-time coverage feedback; processes and saves locally without cloud; quality ceiling limits it to rooms / small outdoor sections |
| Phone/camera, cloud | Varjo Teleport · Polycam | 15 min – few hours processing; much higher quality; larger spaces; built-in viewer, annotation, measurement; `.ply` export |
| Mirrorless / DSLR | any body + widest available lens; **14–18 mm called the sweet spot**, 8 mm fisheye possible; external shutter trigger, burst mode; stopped to ~f5–f7, shutter cranked to kill motion blur; 4K video capture also viable | full-frame sensor, low-light headroom for dim interiors |
| Desktop training | Postshot (Windows/NVIDIA) · Brush (Apple Silicon) | local training; Postshot also renders camera views and exports formats |
| Pose / registration | RealityCapture (Epic) or Agisoft Metashape → export poses → Postshot to train | registration is faster and more reliable in a dedicated photogrammetry tool than in the trainer |
| 360 cameras | Insta360 / DJI / GoPro → "360 toolkit" utility to stamp rectilinear views out of stitched 360s → register → train | most trainers need rectilinear, not fisheye; mount overhead to stitch yourself out |
| LiDAR + 360 rigs | XGrids Lixel K1 (~$5k, incl. RTK GPS module) · XGrids PortalCam (~$15k) | LiDAR SLAM gives real-time capture guidance and geometry through foliage; RTK auto-fuses multiple collects without manual tie points |

Prices, tiers and free-plan terms cited above are as stated in January 2026 and will have moved.

---

## D. Model-behaviour claims with a short shelf life

- Real-time/interactive video models run *"roughly a version or two behind the offline video models"*
  [S6 06:24, 2026-05].
- Genie 3 sessions capped at ~60 seconds, described by its own team as *"somewhat artificial… not a
  fundamental limitation"*, downloadable as a 60-second clip [S5, 2026-01].
- Grounding by Street View panorama retrieval was live in Genie 3 via a "choose location from Google
  Maps" control; aerial/oblique imagery was *not yet* fed in as of 2026-05 [S6].
- One multimodal model being weak at text-to-video while strong at VFX-style editing [S4, 2026-06] is a
  statement about one checkpoint, not a law.

Use these as evidence that **the previz-cheap / finish-expensive split existed**, not as current specs.

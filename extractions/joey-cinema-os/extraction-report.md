# JOEY (Noisy Group / Control World) — Mastery Extraction (Forge, Deep Tier)

## Content Assessment

- **Source:** 3 YouTube videos (10:30 + 09:10 + 13:55, transcripts + full frame harvests), 1 Notion release doc, 3 production Claude skills (v3.0, ~184KB of locked prompt grammar)
- **Expert:** Joey — professional filmmaker (brand/ad work) building "Control (CTRL)," a fully AI-generated K-pop group with published music videos; channel grew 40 → ~25k subs in months, unmonetized, anti-gatekeeping. Collaborator KY — formally trained fashion designer, CTRL World Fashion Design Director.
- **Domain:** Cinema-grade AI image/video production — character/world consistency systems, Higgsfield (Banana Pro / Soul Cinema / GPT-2 / Seedance 2.0), prompt-as-production-document discipline
- **Depth Tier:** Deep (forced — forge) — multi-source, dense locked methodology, verbatim production artifacts
- **Genius Patterns:** 24 identified (20 from skill files — see `extractions/joey-cinema/skill-files-analysis.md` §3 — + 4 video-only, below)
- **Hidden Knowledge:** 8 tacit insights
- **Existing Overlap:** Tao Prompts (video pipeline), PJ Accetturo (production-grade video), fantastic-studio/posters (stylized image lane), gpt-image-2-director (layout/text lane) — none do consistency infrastructure

## Executive Summary

- **Core Genius:** Consistency in AI video is not a model feature — it's an *asset discipline*. Joey moves every load-bearing decision OUT of the prompt and INTO locked upstream artifacts (bibles, face locks, flat reference plates, canonical sheets), so each generation is a cheap, disposable read of expensive, permanent context. "The pipeline is the actual product. The video is just a demo."
- **What Makes Him Different:** He engineers references *for the model's failure modes*, not for human eyes — gray-not-white for edge stability, headless panels so garments get a panel with zero facial data competing for attention, faces large because face size controls drift, zero baked lighting because references get "inherited and amplified." Nobody else in the roster (or, per his own market scan, on YouTube) works at this layer.
- **Deployable Skills:** Full character/world/product consistency pipeline: story bible → face lock → outfit base → 3-panel sheet → scene plates → block-structured Seedance prompts, with credit-costed shot plans and drift-repair rituals.
- **Hidden Knowledge Captured:** Prompt density bell curve; degrees-vs-millimeters snap behavior; position-in-prompt-is-instruction; the "never" clause; contrast-stated-three-ways; technical flats as anti-slop inputs; ~50-generation expectation for hard garments; 8-10 takes → 2-3 takes as the honest win condition ("drift never fully solved, hit rate scales with prep").

## Genius Patterns (video-sourced additions — the 20 skill-file patterns live in skill-files-analysis.md §3 and genius.md)

### 21. The Prompt Bell Curve
- **What He Does Unconsciously:** Treats prompt length as a tuned dial, not a maximization: "more is more and less is more... It's all about finding that sweet spot."
- **Executable Behavior:** When a prompt has accreted 10+ iterations of patches, don't add — tell the LLM to "cut it, reset it, let the prompt breathe," then re-add only what's necessary.
- **Deployment Context:** Any generation loop past ~3 failed iterations.
- **Success Metric:** Post-reset prompt is shorter than the bloated one AND hits in ≤3 takes.

### 22. Face Size Controls Drift
- **What He Does Unconsciously:** Evaluates every reference image by how many pixels the FACE gets — moved 6-panel → 3-panel, removed the mascot from frame, deleted heads from body panels.
- **Executable Behavior:** In any identity reference: exactly ONE face, as large as the format allows; delete every competing face; give garments/silhouette their own face-free panel.
- **Deployment Context:** Character sheets, brand-mascot refs, product-with-model refs.
- **Success Metric:** Character holds identity across 10+ downstream generations without re-prompting the face.

### 23. Timestamped Beats Inside One Generation
- **What He Does Unconsciously:** Choreographs multi-beat action inside a single video generation with absolute timestamps ("heels hit the ledge at 7.0s... again at 11.0s") plus per-beat camera physics (shutter, slow-motion intervals).
- **Executable Behavior:** For any 10-15s shot with 2+ beats: name each beat's time, action, and speed treatment explicitly; put a hard cut at every speed change.
- **Deployment Context:** Single-prompt story shots, contest-format 15s narratives, ad beats.
- **Success Metric:** The model renders beats AT the named marks; no unplanned cuts.

### 24. Real Documentation Beats Vibe Prompts (the KY pattern)
- **What He Does Unconsciously:** Imports actual industry documentation as model inputs — fashion spec sheets, Adobe technical flats, measurements, front/side/back/three-quarter views — instead of describing garments impressionistically.
- **Executable Behavior:** For any real product/garment: feed construction documentation + all angles; expect ~50 generations for the hardest pieces; per-character/product color palette sheets WITH a colors-to-avoid row.
- **Deployment Context:** Client product work (apparel, packaging, listings), brand worlds.
- **Success Metric:** A designer recognizes their own garment construction in the output.

## Hidden Knowledge

- **The 3-shot/15-second story test:** grab attention → emotional payoff → leave unresolved questions. Joey's judging criterion is question count: the winner made him ask four "why"s. Unresolved tension is the win condition, not resolution.
- **Voice consistency is a context problem:** "not a fully recognized thing yet" at the model level — he gets it by feeding voice timbre/cadence descriptors from the bible into every prompt. Consistency features arrive late; context discipline works today.
- **Native resolution beats upscale:** "Seedance 4K native... is much different than 720p upscaled to 4K" — resolution decisions happen at generation, not post.
- **Omni/video-to-video register flip:** for edit-style operations on real footage (≤10s), prompts go SIMPLE and imperative ("keep me exactly the same, change X") — the opposite register from generation prompts. Match prompt complexity to operation type.
- **The honest economics:** 200-300 credits per studio piece, 5,000-6,000 per music video, ~117 credits per 13s 1080p Seedance gen; skills exist to eliminate trial-and-error, not to guarantee first-take success (8-10 takes → 2-3).
- **Fake-BTS worldbuilding:** behind-the-scenes-that-never-happened (blue screens, film crews, camcorder-era emulation, domestic slice-of-life) makes a synthetic world read real — realism through *context*, not just fidelity.
- **Collaboration surface:** teams work inside Higgsfield Cinema Studio (shared world assets, in-platform iteration) — no screenshot ping-pong.
- **Ship-then-raise-the-bar:** "I'm going to say this is not great... I liked it enough to post it." Perfectionism budgeted, not indulged.

## Hall of Fame Exemplars (reference-corpus/, real published artifacts)

### Exemplar 1: The amber-PVC-raincoat 3-panel sheet prompt (Notion doc, complete, ~5,150 chars)
- **Context:** The sample prompt Joey shipped with the v3.0 release, rendered output shown.
- **The Example:** `reference-corpus/joey-3panel-sheet-amber-pvc-raincoat.md`
- **What makes this excellent:** Every v3 technique in one artifact — identical-figure lock across panels, headless front with ghost-mannequin hollow + full suppression stack, rear-with-head, chest-up identity panel, uniform mid-gray with skin-tone consistency clause ("identical in value and hue across the face, midriff, legs, and hands in every panel"), material-true sheen exceptions (PVC/leather keep specular while skin stays matte), "Photographed not generated" close.

### Exemplar 2: The '33' jersey character prompt (video 2, t=05:46)
- **Context:** Live output of his skill in Claude, Copy button visible.
- **The Example:** `reference-corpus/joey-character-prompt-and-seedance-prompt.md` §1
- **What makes this excellent:** Costume-designer breakdown language — hair geometry, skin finish, garment construction, drape behavior, brand-neutral "three-stripe" — zero AI-art keywords. This is what "their thinking, not their terminology" looks like in image prompting.

### Exemplar 3: The rooftop-runner timestamped Seedance prompt (video 1, t=09:17, 330 credits, production UI)
- **Context:** Real generation loaded in Higgsfield Create Video.
- **The Example:** `reference-corpus/joey-character-prompt-and-seedance-prompt.md` §3
- **What makes this excellent:** Restricted warm accents against a cool grade ("the ONLY warm"), 24fps/180° shutter physics, absolute-timestamp beats with per-beat slow-motion — choreography, not description.

### Anti-Exemplar: The keyword-slop prompt
- **What mediocre looks like:** "8k, masterpiece, hyperrealistic, cinematic lighting, trending on artstation" + a character name + a brand name + "beautiful girl, age 22" + style header at the top + 5,000 characters re-describing what the attached reference already shows.
- **Why it fails:** Violates every lock at once — names drift, ages are banned, style prefixes scatter attention, re-description double-weights identity, quality words produce no visible pixels, and there's no reference discipline underneath so every generation re-rolls identity.

## Signature Moves

- **The Reset Ritual:** prompt past ~3 failed iterations → cut it, let it breathe, re-add only what's necessary → **Deploy when:** iteration bloat detected.
- **References First, Always:** every pre-prompt confirmation lists attached references before anything else — a missing ref is caught before the prompt ships → **Deploy when:** any multi-reference composition.
- **Ask the Existence Question:** first move on any character work: "does this character already exist, or are we developing them?" — routes to lock vs. build → **Deploy when:** session start, new subject.
- **Cost Before Generate:** every video prompt carries a declared duration; every shot plan carries a credit estimate before anything runs → **Deploy when:** any paid generation.
- **One Variable Per Shot:** building reference series, vary exactly one parameter (pose/framing/expression/light direction); identity stays locked → **Deploy when:** building asset libraries.
- **Kick to the Right Layer:** worldbuilder refuses unbuilt characters (kicks to Banana Pro); Banana Pro refuses to bake lighting (kicks to the scene); the bible refuses cinematography — nothing does another layer's job → **Deploy when:** any cross-layer temptation.

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|---|---|---|---|
| Identity persistence | Character recognizable across 3 shots | Holds across a full scene without re-rolls | Holds across a full music video incl. wardrobe changes, action, era shifts |
| Reference discipline | References attached | References carry identity; prompt carries only framing | Zero re-description; plates flat-graded; canonical-over-plate everywhere |
| Anti-AI-render physics | No obvious plastic skin | Matte skin + grain + rolled highlights | Full stack: SSS biology, atmospheric planes, flattering ceiling, "photographed not generated" |
| Write-the-visible | Some measurables | km/h, %, meters, muscle-level emotion throughout | Every word produces a visible pixel; resolution-aware detail only |
| Prompt economy | Under model limits | Bell-curve tuned; front-loaded composition | 2,500-char prompt + strong refs beating 5,000-char; reset ritual reflexive |
| Credit economy | Costs tracked | Duration declared per prompt; shot plan costed pre-run | 8-10 takes → 2-3; hardest asset budgeted (~50 gens) knowingly |
| Story grip (motion work) | Coherent action | Clear beat structure with timestamps | 15s/3-shot: grab → payoff → unresolved questions (viewer asks "why?" ≥2×) |
| World believability | Consistent look | Era/palette locks per bible | Fake-BTS/domestic/mundane texture makes the synthetic world read documentary-real |

## Applied Intelligence

### Capability Unlocks
- **Product-grade identity lock for client work:** the character pipeline transfers directly to products (bottles, garments, vehicles) — face lock ≈ hero-angle lock; 3-panel sheet ≈ turnaround; the KY method (technical flats + measurements + colors-to-avoid) is the client-brand version of the bible.
- **Branded-world ad systems:** locked characters + locked products + scene plates = campaign-scale consistency (Dara/Omar static+video stacks with identity that holds).
- **Voice-consistent character content:** bible Speech/Movement/Stillness descriptors → Sound Bed/Subject Lock = repeatable character performances.

### System Enhancements
- The reference-plate doctrine (zero baked lighting, gray-flat) should become the standing rule for ANY image in this system that seeds downstream video — fantastic-posters' poster-to-video bridge included.
- "Position in prompt is instruction" and "discrete anchors beat continuous suggestions" generalize to all prompt engineering in the system.

### Market Signals
- "Nobody is showing you the system" — the systematic middle layer (between one-cool-image posts and $500 courses) is an open lane; Joey took it with free skills and 40→25k in months. Same lane exists for product-grade brand work.

## Implementation Pathway
- **24-Hour:** Run `/jcin-character-lock` on a Control-style test character end-to-end (face lock → sheet) on Higgsfield MCP; run the flat-grade plate rule on one MyBPM product.
- **7-Day:** Build a client bible (Jen listings world or MyBPM brand world); produce one 15s 3-shot branded story via the full pipeline.
- **30-Day:** Campaign-scale: locked product + locked avatar characters + scene-plate library feeding both static (Dara) and video (worldbuilder) ad production.

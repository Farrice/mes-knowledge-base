# StoryBrand Message Clarity System Contract

| Field | Required Output |
|---|---|
| Source evidence | `extractions/video-context/d4Pmq27udNc/`, `extractions/video-context/5OJT1ph-yL4/`, `extractions/video-context/SzugliCQ3XY/`, and this extraction package. Earlier packages are transcript-only; `SzugliCQ3XY` has spoken rows and sampled frame files, with OCR unavailable. |
| Objective | Turn StoryBrand message clarity and soundbite strategy into one replayable command that produces a deployable Message Clarity Pack. |
| Components | `donald-miller-cognitive-load`, `donald-miller-storybrand`, `agents/donald-miller`, `/message-audit`, `/storybrand`, `/one-liner`, `/storybrand-copy`, `/low-cognitive-load-message-gate`, and `/storybrand-message-clarity-system`. |
| Step order | source grounding -> runtime input gate -> low-cognitive-load gate -> one-hole lock -> cognitive-load autopsy -> PEACE sound bites -> StoryBrand one-liner -> BrandScript alignment -> deployment matrix -> consistency audit -> quality gate. |
| Inputs | Business name, offer, target customer, primary customer problem, optional existing copy or URL, optional active channels. |
| Outputs | Message Clarity Pack with one-hole problem, load diagnosis, five locked PEACE sound bites, one-liner, BrandScript alignment notes, deployment matrix, and monthly audit. |
| Handoff summary | Each component passes a compact output into the next step: problem lock -> scored language -> locked sound bites -> story alignment -> deployment. |
| Composition rule | Donald Miller is the expertise owner; `/low-cognitive-load-message-gate` owns the clarity stop condition; cognitive-load workflow owns language weight; StoryBrand workflow owns narrative structure; the orchestrator owns order and integration. |
| Human checkpoint | Ask only when the primary customer, offer, or one specific problem cannot be derived from the provided context. Skip for local reversible Codex Antigravity file edits already approved. |
| Validation | Validate both Donald Miller skills, validate the new source-command wrapper, verify command/router discoverability, and run harness contract checks. |
| Result surface | Render the Message Clarity Pack directly in conversation; local docs are persistence and routing surfaces. |
| Context policy | Keep `/storybrand-message-clarity-system` hot as the orchestrator; keep detailed component workflow files cold until each phase needs them. |
| Reuse hook | Use this route for business messaging, offer clarity, homepage clarity, pitch simplification, and soundbite deployment work before downstream copywriting. |

## Boundary Handoffs

### Input Gate -> One-Hole Lock
- **Source evidence**: user business context plus source-map anchors.
- **Component used**: `/storybrand-message-clarity-system`.
- **Output produced**: one primary customer, one offer, one problem.
- **Next input**: specific problem statement for cognitive-load and soundbite work.
- **Validation**: no commas or multi-problem bundles in the problem lock.
- **Open risk**: if context is too thin, ask for missing business, customer, or problem.

### Input Gate -> Low-Cognitive-Load Message Gate
- **Source evidence**: supplied message/copy plus `source-map.md` and `semantic_libraries/antigravity/primitives/low-cognitive-load-message-gate.md`.
- **Component used**: `/low-cognitive-load-message-gate`.
- **Output produced**: gate verdict, scored heavy phrases, repeatability lock, and required fixes.
- **Next input**: locked problem and zero-load rewrite directions.
- **Validation**: supplied phrases are scored; PASS/REVISE/REWORK is explicit.
- **Open risk**: if no copy is supplied, score candidate problem, answer, and repeatability phrases only.

### One-Hole Lock -> Cognitive-Load Autopsy
- **Source evidence**: supplied copy or inferred current message from user context.
- **Component used**: `donald-miller-cognitive-load/workflows/01-cognitive-load-autopsy.md`.
- **Output produced**: load diagnosis and zero-load rewrite targets.
- **Next input**: simplified phrase candidates.
- **Validation**: every high-load phrase has a plain-language replacement.
- **Open risk**: if no copy is supplied, diagnose proposed language only.

### Cognitive-Load Autopsy -> PEACE Sound Bites
- **Source evidence**: selected problem and zero-load phrase candidates.
- **Component used**: `donald-miller-cognitive-load/workflows/02-peace-soundbite-generator.md`.
- **Output produced**: locked Problem, Empathy, Answer, Change, and End Result sound bites.
- **Next input**: sound bites for StoryBrand alignment.
- **Validation**: problem and end result bookend; answer is simple; phrases are repeatable.
- **Open risk**: over-polished phrases can become heavier than plain ones.

### PEACE Sound Bites -> StoryBrand Alignment
- **Source evidence**: locked sound bites plus business context.
- **Component used**: `donald-miller-storybrand/workflows/04-one-liner-generator.md` and BrandScript alignment rules.
- **Output produced**: one-liner and BrandScript notes.
- **Next input**: deployable message language.
- **Validation**: customer is hero; product appears after problem; CTA resolves a decision.
- **Open risk**: BrandScript expansion can dilute the locked phrases if not constrained.

### StoryBrand Alignment -> Deployment Matrix
- **Source evidence**: locked sound bites, one-liner, active channels.
- **Component used**: `donald-miller-cognitive-load/workflows/05-soundbite-deployment-matrix.md`.
- **Output produced**: channel map and monthly consistency audit.
- **Next input**: final user-facing Message Clarity Pack.
- **Validation**: sound bites appear verbatim across channels.
- **Open risk**: missing active-channel data requires a default channel set.

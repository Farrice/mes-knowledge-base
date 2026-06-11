# Sam Parr Copywriting Extraction Brief

## Source

| Field | Value |
|---|---|
| Video | The $2 Billion Copywriting Secret Behind The Most Successful Ad Ever w/ Sam Parr |
| Channel | Sweat Equity |
| URL | `https://www.youtube.com/watch?v=uf4fR3qcDkU&t=151s` |
| Local package | `extractions/video-context/uf4fR3qcDkU/` |
| Transcript | `extractions/video-context/uf4fR3qcDkU/transcript.txt` |
| Ledger | `extractions/video-context/uf4fR3qcDkU/video-context-ledger.md` |
| Uncertainty | `extractions/video-context/uf4fR3qcDkU/uncertainty-report.md` |

The package contains 3,988 spoken-evidence rows. Visual and OCR evidence are unavailable because the run used transcript mode.

## Build Decision

This source should become a Companion OS plus deployable command, not a replacement for the Copywriting Agent.

Reason:

- The workspace already has `copywriting-agent`, `high-taste-writing-os`, `publishable-copy-gate`, `proof-copy-engine`, and `farrice-content-os`.
- The existing Sam Parr skill owns taste acquisition. This source adds copy mechanics, not a new all-purpose Sam persona.
- The useful leverage is a narrow set of copy moves: headline gravity, curiosity gaps, proof, visual proof, copywork, rhythm, story, objections, and humor fit.
- The repaired build must prove behavior change on weak copy before it is considered complete.

## Skill System Contract

| Field | Decision |
|---|---|
| Source evidence | Transcript-backed package at `extractions/video-context/uf4fR3qcDkU/`. |
| Objective | Improve Antigravity copywriting outputs with Sam Parr's direct-response mechanics. |
| Components | `_active/sam-parr-copywriting-os/`, `skills/sam-parr-copywriting-mechanics/`, `.agent/workflows/sam-parr-copywriting-mechanics.md`, hot/cold command wrappers, `copywriting-agent`, `high-taste-writing-os`, `publishable-copy-gate`, `farrice-content-os`. |
| Step order | Source capture -> mechanics extraction -> Companion OS -> deployable skill -> command bridge -> expert integrations -> behavior proof -> validation. |
| Inputs | Draft copy, offer, audience, proof assets, desired action, platform, and source evidence path. |
| Outputs | Mechanics pass, rewritten copy, copywork plan, proof/story/objection improvements, behavior delta, quality checklist. |
| Handoff summary | Pass only the relevant mechanic, evidence timestamp, and changed copy section to downstream gates. |
| Composition rule | `source-to-skill-system` owns the system, Sam Parr supplies the differentiator, copy gates own publishability. |
| Human checkpoint | Required before global skill edits, publishing, external writes, or visual-evidence claims. Hot wrapper promotion is approved only if proof and validators pass. |
| Validation | Skill validation, registry sync, command/workflow search, context retrieval, and artifact guards. |
| Behavior-changing proof | `_active/sam-parr-copywriting-os/06-before-after-proof-lab.md` proves the source can transform weak copy with diagnosis, rewrite, and behavior delta. |
| Result surface | Rendered conversation closeout plus local readable Markdown source files. |
| Context policy | Keep the Companion OS loaded on demand; allow the bounded command hot only for direct-response mechanics. |
| Reuse hook | Load for headline rewrites, ad diagnostics, script hooks, direct-response story copy, and copywork training. |

## Extracted Mechanics

| Mechanic | Timestamp Evidence | What It Adds |
|---|---|---|
| AIDA as behavior sequence | `00:01:19`, `00:35:17` | Forces copy to move from attention to action instead of sounding good in place. |
| Familiar energy | `00:02:27` | Makes copy feel like it already belongs in the reader's world. |
| Headline gravity | `00:03:01`, `00:04:24` | Treats the headline as the highest-leverage work, not a last-minute label. |
| Curiosity gap | `00:05:03`, `00:06:08`, `00:07:16`, `00:10:13` | Creates unresolved tension that pulls the reader through the next line. |
| Long is not the problem | `00:08:00`, `00:24:35` | Judges length by interest, story, and reader movement. |
| Phrase twist | `00:14:21`, `00:15:37`, `00:16:11` | Reuses known language patterns with a new turn. |
| Rhythm | `00:20:21`, `00:21:08` | Uses sentence-length variation and transition words to make copy move. |
| Simple language | `00:21:31` | Explains complex ideas in clean, plain sentences. |
| Story-first desire | `00:24:28`, `00:25:04`, `00:37:08` | Lets story carry desire before the product appears. |
| Copywork | `00:27:56`, `00:29:10`, `00:31:20`, `00:45:23`, `00:46:02` | Builds writing taste through exact reproduction and rule extraction. |
| Proof-first ads | `00:34:17`, `00:34:46` | Starts with evidence, comparison, quote, or before/after instead of claims. |
| Visual proof translation | `00:38:29`, `00:40:34` | Turns abstract facts into concrete images the reader can feel. |
| Objection by anecdote | `00:40:34`, `00:42:15` | Handles doubt through story and lived proof, not only FAQ rebuttals. |
| Humor/personality | `00:43:58`, `00:44:05`, `00:45:17` | Uses humor only when it fits the brand and improves trust or attention. |

## Integration Notes

- `copywriting-agent` should route into this layer when a draft has weak headlines, weak proof, no curiosity gap, dead rhythm, or no copywork benchmark.
- `high-taste-writing-os` should use it as a scalpel pass for reader pull and rhythm, not as a whole-draft rewrite.
- `publishable-copy-gate` should add a Sam check for public copy when the main risk is attention, proof, or direct-response momentum.
- `farrice-content-os` should use it in Hook Room and conversion content, especially for brandjack-to-proof assets.
- Future source-to-copywriting extractions should fail if they do not include a before/after proof lab or comparable behavior proof artifact.

## Risks

- Auto captions may contain wording errors. Use timestamps for evidence but avoid treating exact phrasing as final quote authority.
- Visual claims are unavailable until a full frame/OCR pass exists.
- Sam's direct-response instincts can make copy punchier, but the final voice must still be Farrice/client-specific.

# Niche Bending System Contract

| Field | Required Output |
|---|---|
| Source evidence | `extractions/video-context/fLDrB_wmbNE/` plus this extraction package. Transcript and frame samples exist; OCR is unavailable. |
| Objective | Turn niche bending into one replayable command that takes any credible expertise/domain and produces differentiated, production-ready content angles. |
| Components | `/source-to-skill-system`, `/extraction-governor-agent`, `/niche-bending-system`, `tim-danilov-niche-bending`, Tim Danilov component workflows, command/menu routers, and validation scripts. |
| Step order | source grounding -> input gate -> expertise constraint -> demand/staleness scan -> outlier scout -> empty square grid -> borrowed fluency -> visual language -> 3 production-ready bends -> validation verdict. |
| Inputs | Core expertise/niche, target audience/market, primary platform, desired outcome, optional current content, competitors, scout markets, proof, and constraints. |
| Outputs | Niche Bending Pack with diagnosis, scout notes, grid, fluency map, visual notes, three bend concepts, validation verdict, and first experiment. |
| Handoff summary | Each phase passes a compact decision, evidence anchor, selected object, and open risk into the next phase. |
| Composition rule | `/niche-bending-system` owns orchestration. Tim Danilov owns method. `/extraction-governor-agent` owns source-to-capability governance. `/source-to-skill-system` owns system contract and validation shape. |
| Human checkpoint | Ask only when core expertise, target market, platform, or outcome is missing and cannot be inferred. Ask before paid/quota-heavy or external research. |
| Validation | Validate Tim Danilov skill, validate the source-command wrapper, run routing/search proof, run live-surface audit, and preserve source uncertainty. |
| Result surface | Render the Niche Bending Pack directly in conversation. Local files are the persistent command and source surfaces. |
| Context policy | Keep the command workflow concise; load source map, command contract, and one downstream Tim Danilov workflow at a time. |
| Reuse hook | Use this route whenever the user wants differentiated content formats, category-creating angles, market-format transplants, or domain expertise turned into remarkable content series. |

## Boundary Handoffs

### Input Gate -> Expertise Constraint
- **Source evidence**: user context plus `source-map.md`.
- **Component used**: `/niche-bending-system`.
- **Output produced**: expertise, market, platform, and outcome lock.
- **Next input**: credibility boundary for format selection.
- **Validation**: no bend is proposed until expertise fit is clear.
- **Open risk**: if the expertise is too broad, ask for the specific proof-backed domain.

### Expertise Constraint -> Demand And Staleness Scan
- **Source evidence**: selected market and user's credible payload.
- **Component used**: `blue-ocean-market-identification.md`.
- **Output produced**: market demand/staleness notes.
- **Next input**: market rows for the empty square grid.
- **Validation**: saturated markets are allowed when demand is visible.
- **Open risk**: demand may require live research if not supplied.

### Demand Scan -> Outlier Format Scout
- **Source evidence**: target platform and candidate scout markets.
- **Component used**: `viral-format-engineering.md`.
- **Output produced**: candidate formats and performance rationale.
- **Next input**: format columns for the grid.
- **Validation**: prefer smaller-channel outliers over large-channel defaults.
- **Open risk**: current outlier data may require external search.

### Outlier Scout -> Empty Square Grid
- **Source evidence**: proven formats plus target/adjacent markets.
- **Component used**: `format-market-grid-builder` prompt logic and command contract.
- **Output produced**: occupied, emerging, empty, and incompatible cells.
- **Next input**: top cells for fluency mapping.
- **Validation**: empty square means proven format plus proven market, not random novelty.
- **Open risk**: competitor visibility may be incomplete without research.

### Empty Square Grid -> Production-Ready Bends
- **Source evidence**: selected empty cells and source-format language.
- **Component used**: `high-conversion-content-design.md`.
- **Output produced**: three bend concepts with title, hook, skeleton, payload, visual notes, and verdict.
- **Next input**: final Niche Bending Pack.
- **Validation**: each concept has a first experiment and quality verdict.
- **Open risk**: visual language may need designer review for final production.

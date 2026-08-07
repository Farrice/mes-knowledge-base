# Source Coverage Matrix — Oren Archetype Video Forge

| Source | Package | Capture Mode | Observed Spoken | Observed Visual | Onscreen Text | Limitation | Primary Use |
|---|---|---:|---:|---:|---:|---|---|
| `tcqf6sgw_Ho` | `extractions/video-context/tcqf6sgw_Ho` | full ledger + frames | yes | yes | no | OCR unavailable | Archetype spine |
| `l3inbx2jeZU` | `extractions/video-context/l3inbx2jeZU` | transcript metadata | yes | skipped | skipped | visual examples not harvested | Pricing psychology |
| `IdmtqdoZTBA` | `extractions/video-context/IdmtqdoZTBA` | transcript metadata | yes | skipped | skipped | visual examples not harvested | Content-team ops |
| `1YVi3iFk3V0` | `extractions/video-context/1YVi3iFk3V0` | transcript metadata | yes | skipped | skipped | visual examples not harvested | Marketing planning |
| `8gvCc5jvcH0` | `extractions/video-context/8gvCc5jvcH0` | transcript metadata | yes | skipped | skipped | visual examples not harvested | Short-form monetization |
| `QHPmOgnc96E` | `extractions/video-context/QHPmOgnc96E` | transcript metadata | yes | skipped | skipped | visual examples not harvested | Creative systems |

## Evidence Separation Rule
- `observed_spoken`: Mechanics explicitly present in cleaned transcript.
- `observed_visual`: Captured frame context from the full archetype ledger only.
- `observed_onscreen_text`: Empty because OCR was unavailable.
- `inferred_context`: Used only for synthesis and workflow design, not recorded as observed evidence.
- `uncertain_or_unavailable`: OCR failure and skipped support-source frames are preserved as limitations.

## Build Decision
- Create `oren-archetype-social-strategy` as a companion module.
- Preserve `oren-content-team-architecture`, `oren-luxury-psychology`, and `oren-operational-systems` as canonical packages for their stronger existing domains.
- Cross-link rather than duplicate where support videos overlap existing Oren systems.

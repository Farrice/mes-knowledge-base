# Provenance — Anchors Introduced in This Repair Pass

Anchor → source file + exact location, for the adversarial verifier. All anchors below were opened and quote-checked this pass (2026-07-18), not carried over from a prior pass.

| Anchor ID | Used In | Source File | Location | Verbatim Text Checked |
|---|---|---|---|---|
| S-P1 | genius.md → "How to Use This Skill" quote; all 5 core Anti-Patterns | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/projects/0198ed9a-7175-769c-9230-b32b41f7e64f.md` (35,068 bytes) | §"For Any Platform" (near end of file); §"Platform-Specific Deployment → ChatGPT Custom GPT → Instructions Format" ("Never:" list) | "feel like Jason Fladlien himself is mentoring the user - vulnerable yet authoritative, direct yet compassionate, practical yet profound." / "Never: Promise instant results / Ignore crisis signs / Enable victimhood / Suggest perfection / Forget compassion" |
| S-P2 | genius.md → 2 excess-marker Anti-Patterns | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/projects/0199139f-4327-7717-88fc-154a86b034ba.md` (26,439 bytes) | JSON key path `prosperity_algorithm_system.prosperity_factors.4_tenacious_persistence.diagnostic_markers.excess`; `...1_prosperous_purpose.diagnostic_markers.excess` | `["Grinding to exhaustion", "Persistence without compassion", "Brittle tenacity"]` / `["Purpose without joy", "Burning out from mission", "Rigid purpose adherence"]` |

## How S-P1 / S-P2 were extracted

Both files live inside `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 7,728 members). They are not on disk elsewhere. Extraction method, reproducible:

```python
import tarfile
tf = tarfile.open("_archive/claude-export-2026-07-01.tar.gz", "r:gz")
m = tf.getmember("claude-export/normalized/projects/0198ed9a-7175-769c-9230-b32b41f7e64f.md")
data = tf.extractfile(m).read()  # 35,068 bytes, confirmed non-empty
```

Discovery: a full-archive `tarfile` scan of all 7,708 `.md` members for the case-insensitive phrase "prosperity algorithm" returned 9 hits; the 2 hits under `.../normalized/projects/` were opened first because they match SKILL.md's own front-matter (`source: "claude.ai project export (2026-07-01)"`) and confirmed to contain the coaching system this skill is built from, almost line-for-line.

## Ruled-out sources (checked, not used)

| Path | Size | Why ruled out |
|---|---|---|
| `extractions/Jason Fladlien/transcript.txt` | 89,775 bytes | Full-text regex scan for "prosperity" (case-insensitive): 1 hit, unrelated context ("...this is how I think about it from the that view of prosperity..." — a Hindu-religion tangent, not the 10-factor system). |
| `extractions/jason-fladlien/transcript.txt` | 91,971 bytes | Full-text regex scan for "prosperity": 0 hits. |

Both files were opened and read (not assumed absent/irrelevant) before being excluded — per the envelope's rule that a claim of source absence is itself a provenance claim requiring verification.

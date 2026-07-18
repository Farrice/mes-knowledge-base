# Provenance — expert-assembly-os repair

Anchor → source file + location. All sizes via `wc -c` on 2026-07-17.

| Anchor (in genius.md / workflows) | Source file | Location | Size (bytes) | Verified how |
|---|---|---|---|---|
| "Composite label explicit; authority from specificity, not numbers." | `skills/expert-assembly-os/SKILL.md` | line 39, "Composite Personas" bullet | 5,154 | Direct Read, exact string match |
| "Floor fails after retry → seat with `[MASTERY FLAG: <reason>]`..." | `skills/expert-assembly-os/references/persona-synthesis-prompt.md` | line 173, Step G4 | 7,365 | Direct Read, exact string match |
| "All synthetic panelists explicitly marked `[Bespoke Composite]`..." | `skills/expert-assembly-os/references/roadmap-schema.md` | line 24, Labeling Rule | 5,527 | Direct Read, exact string match |
| "'Improve X' became 'X reaches Y by DATE.'" | `skills/expert-assembly-os/references/lineage.md` | line 36, Requirement 3 | 8,153 | Direct Read, exact string match |
| "No fake stats... authority from specificity not numbers" (Key Decision #2) | `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md` | line 57 | 7,500 | Direct Read |
| "Never pin Opus: Conductor = strongest available model; Sonnet executes" (Key Decision #5) | `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md` | line 60 | 7,500 | Direct Read |
| Commit `26adc893f`, 2026-07-15, "Expert Assembly OS Phase 0–3..." | `git show 26adc893f294e1097ff9c4b23133d9dc2fcf9573` | commit header + body | n/a (git object) | `git show --stat` |
| Commit `9c8c4d098`, 2026-07-15, "Grounded Forge + Mastery Floor..." | `git show 9c8c4d098ccecf5c0d97f78d59f60812a62dcee5` | commit header + body | n/a (git object) | `git show --stat` |
| "Latent-only personas are no longer acceptable for bespoke seats." | `project_expert-assembly-os.md` (user memory, `~/.claude/projects/.../memory/`) | line 15 | 3,267 | Direct Read; labeled LIKELY in source-ledger.md per the file's own staleness caveat |
| "Extend, never rebuild. Known open edges: keyword coverage scoring is crude..." | `project_expert-assembly-os.md` | line 20 | 3,267 | Direct Read; LIKELY (same caveat) |
| 227-card roster, STRONG ≥2 hits +≥50% ratio / THIN / ABSENT thresholds | `skills/expert-assembly-os/SKILL.md` | lines 30–35 | 5,154 | Direct Read, exact string/number match |
| 8-phase workflow names (Scope→Cast→Forge→Ground→Diverge→Deliberate→Synthesize→Close) | `.agent/workflows/assemble.md` | "What it does (phases)" section | 8,162 | Direct Read |
| "How to Use This Skill" structural model (never-announce-the-machinery, recognition-test framing, polish-is-the-tell) | `skills/ben-watkins-storytelling/genius.md` | lines 7–16 | 31,629 | Direct Read; structure only, no content copied |
| "Output Contract" / "Quality Gate" heading + "The X Test" numbered format | `skills/adam-enfroy-affiliate-marketing/workflows/platform-niche-matchmaker.md` | lines 66–81 | 6,697 | Direct Read; house-style model only, no content copied |

## Explicit non-claim

No source in this repair was declared "absent" without a direct file read confirming
it (per Envelope rule #2). The `extractions/` check was run as a live grep, not
assumed: `ls extractions/ | grep -i assembl` returned zero matches, confirmed
2026-07-17, no extraction folder exists for this skill.

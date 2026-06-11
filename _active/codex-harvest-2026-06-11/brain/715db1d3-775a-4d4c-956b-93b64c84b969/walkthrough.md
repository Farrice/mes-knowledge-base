# Walkthrough: MetaHarness → Self-Evolving Antigravity System

## What Was Built

Extracted the MetaHarness paper (arXiv:2603.28052v1) and Karpathy's autoresearch into a complete self-evolution capability for Antigravity. The system can now automatically propose, evaluate, and iterate on its own workflows, skills, and prompts.

## Files Created/Modified

### Extraction (1 file)
| File | Purpose |
|------|---------|
| [extraction_report.md](file:///Users/farricecain/Google%20Antigravity/extractions/matthew-berman/extraction_report.md) | Full extraction: frameworks, genius patterns, key results, practical tips |

### Skill (2 files)
| File | Purpose |
|------|---------|
| [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/self-evolving-systems/SKILL.md) | Core capability, principles, stacking, load order |
| [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/self-evolving-systems/genius.md) | 8 genius patterns, 5 hidden knowledge items, decision framework, anti-patterns |

### Workflows (8 files)
| Command | File | Purpose |
|---------|------|---------|
| `/self-evolve` | [self-evolve.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/self-evolve.md) | Master MetaHarness evolution loop |
| `/harness-evolve` | [harness-evolve.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/harness-evolve.md) | Focused single-workflow evolution |
| `/auto-experiment` | [auto-experiment.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/auto-experiment.md) | Karpathy-style experiment runner |
| `/evolution-audit` | [evolution-audit.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/evolution-audit.md) | History inspection + regression detection |
| `/skill-anneal` | [skill-anneal.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/skill-anneal.md) | Self-annealing via past quality gate failures |
| `/proposer-sprint` | [proposer-sprint.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/proposer-sprint.md) | Time-boxed improvement sprint |
| `/evolution-status` | [evolution-status.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/evolution-status.md) | Dashboard of all evolution loops |
| `/bitter-lesson-check` | [bitter-lesson-check.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/bitter-lesson-check.md) | Audit hand-coded heuristics for evolution potential |

### Directive Update (1 file)
| File | Change |
|------|--------|
| [deep_self_annealing.md](file:///Users/farricecain/Google%20Antigravity/directives/deep_self_annealing.md) | Added Tier 4 (Self-Evolution) with triggers, rules, and cross-references |

## Key Design Decisions

1. **Methodology extraction, not infrastructure build** — We extracted the *how to think about it* from MetaHarness, not a Python eval loop. The workflows are human-supervised evolution sprints, not overnight autonomous runs.

2. **8 commands at different granularities** — `/self-evolve` is the full loop, `/proposer-sprint` is a 15-minute quick hit, `/bitter-lesson-check` is just an audit. Different tools for different situations.

3. **Tier 4 integration** — The deep_self_annealing directive now has a natural escalation path: fix → diagnose → escalate → **evolve**. Tier 4 fires when the same error class recurs 3+ times.

## How to Start Using It

- **Quick win**: Run `/bitter-lesson-check` with target "all" to see which Antigravity components have the highest evolution potential
- **First evolution**: Pick a high-scoring component from the audit and run `/proposer-sprint` with 5 iterations
- **Full loop**: Once comfortable, run `/self-evolve` on a key workflow with 10-20 iterations

## Verification

- ✅ All 8 workflow files exist in `.agent/workflows/`
- ✅ Skill directory has `SKILL.md` + `genius.md`
- ✅ Extraction report complete with frameworks, results, and references
- ✅ `deep_self_annealing.md` updated with Tier 4 + cross-references
- ✅ Quick reference decision tree includes Tier 4 path

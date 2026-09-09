# Global Mirror Proposal

Status: `APPLIED / MIRROR VERIFIED / BRIDGE MAINTENANCE DEBT NOTED`

The exact proposed patch is `global-mirror-proposal.patch`. It changes only:

- `/Users/farricecain/.codex/AGENTS.md`
- `/Users/farricecain/.codex/skills/autopilot/SKILL.md`

Read-only precondition hashes captured 2026-09-03:

| Target | SHA-256 |
|---|---|
| `/Users/farricecain/.codex/AGENTS.md` | `35555c0b8a207722bfe14e811a123f1ea6bdaa2ff7d7d916f99e636f536ab87e` |
| `/Users/farricecain/.codex/skills/autopilot/SKILL.md` | `557f53ee8e6391c988609f32235f785f7a796d6522312846424049ab52c8a71e` |

Both precondition hashes were re-checked and matched before application on
2026-09-03. The prepared patch then applied cleanly without modification.

Post-application hashes:

| Target | SHA-256 |
|---|---|
| `/Users/farricecain/.codex/AGENTS.md` | `7e0b399a0edc45990392d77206f1c2724082e73b1e31cd2a8bbbe463adc4efc6` |
| `/Users/farricecain/.codex/skills/autopilot/SKILL.md` | `54363c94c6fdab2d559497475aeecd49e19061210e1b497f92d3c1a37b54a4d5` |

Verification:

- Global policy and Autopilot wrapper contain the intended launchpad v3 text.
- Outside-workspace smoke tests emitted the expected `Mode: Probe` and
  `Mode: Analyze` material-fork signals.
- Google Operator Core verification passed, including the global adaptive
  judgment floor.
- Autopilot runtime verification passed all adaptive inquiry, routing,
  anti-shackle, and blind-comparison cases.

The broader global bridge verifier remains partial because the separately
configured Codex mutation worktree is stale and contains one untracked runtime
path. This pre-existing maintenance debt does not change the read-only global
policy or canonical preflight behavior, and it was not modified under this
two-file approval.

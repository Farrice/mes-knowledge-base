# Triage Labels

> Wired by `/setup-matt-pocock-skills` on 2026-06-15. Tracker = local markdown, so "labels" are recorded as a `Status:` line near the top of each issue file (not GitHub labels). Defaults kept (role name == status string).

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual status strings used in this repo's local-markdown tracker.

| Role in mattpocock/skills | `Status:` value in our tracker | Meaning                                  |
| ------------------------- | ------------------------------ | ---------------------------------------- |
| `needs-triage`            | `needs-triage`                 | Maintainer needs to evaluate this issue  |
| `needs-info`              | `needs-info`                   | Waiting on reporter for more information |
| `ready-for-agent`         | `ready-for-agent`              | Fully specified, ready for an AFK agent  |
| `ready-for-human`         | `ready-for-human`              | Requires human implementation            |
| `wontfix`                 | `wontfix`                      | Will not be actioned                     |

Plus two category roles, recorded the same way: `bug` (something is broken) and `enhancement` (new feature/improvement). Every triaged issue carries exactly one category + one state.

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), set the issue file's `Status:` line to the corresponding value above. Edit the right-hand column if you adopt a different vocabulary.

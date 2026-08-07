# Shared Integration And Permission Design

## Integration Manifest

Every integration needs:

- Name
- Owner
- Credential holder
- Scope: personal, project, team, company, client, public
- Allowed read actions
- Allowed write actions
- Approval gate
- Audit trail
- Revocation path
- Fallback if unavailable

## Personal Versus Team

| Type | Use When | Guard |
|---|---|---|
| Personal integration | The data belongs to one person or private workspace. | Use only for that owner and surface. |
| Project integration | The data belongs to a specific project. | Keep outputs inside project scope. |
| Team integration | The data is intentionally shared with a team. | Limit by role and team membership. |
| Company integration | The data is broadly company-operational. | Require stronger audit and admin review. |

## Approval Ladder

1. Read public/local reference.
2. Read scoped shared data.
3. Draft from private data for owner review.
4. Perform reversible internal action with approval.
5. Perform external or irreversible action only with explicit approval.

## Anti-Patterns

- "One person connected it, so everyone can use it."
- "The agent can see it, so it can cite it."
- "The connector exists, so it should act."
- "A team integration can safely include personal data."

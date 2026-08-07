# Context And Memory Isolation

## Purpose

Prevent the employee from using the wrong context, leaking private context, or letting memory bloat degrade output.

## Required Partitions

| Partition | Examples | Default Rule |
|---|---|---|
| Personal/private | Personal email, private DMs, personal notes | Never shared without explicit owner approval. |
| Project | Repo files, project notes, task plans | Usable only inside the named project. |
| Team/company | Shared docs, team channels, operating metrics | Usable by role if owner permits. |
| Client | Client docs, strategy, account materials | Scoped to client and never mixed across clients. |
| Public/reference | Public sources, docs, videos, web pages | Usable with citation and source limits. |

## Leakage Tests

- Can the employee answer using growth-channel context in engineering? It should not unless policy allows it.
- Can a private integration be used in public/team output? It should not unless owner explicitly shared it.
- Can one client output include another client's facts? It should fail validation.
- Can old memory override current user instruction? It should yield to current scope and authority.

## Memory Rules

- Keep raw evidence in source packages or logs.
- Pass compact handoffs between steps.
- Summarize older context before reuse.
- Prefer named paths over hidden chat memory.
- Define deletion and revocation paths for sensitive context.

---
description: "Global artifact organization router for project-first placement, domain-first retrieval, staged cleanup, and placement enforcement"
---

# /artifact-router - Global Artifact Organization Router

Use this workflow when files, documents, artifacts, outputs, projects, session folders, or deliverables need to be placed, found, cleaned up, migrated, or enforced across the Codex system roots.

## Scope

Owned roots:

- `/Users/farricecain/Codex Antigravity`
- `/Users/farricecain/Documents/Codex`

Never modify `/Users/farricecain/Google Antigravity` from this workflow.

## Operating Rule

The physical hierarchy is project-first:

```text
_active/<project-slug>/
  INDEX.md
  00-start-here/
  01-source/
  02-research/
  03-working-drafts/
  04-deliverables/
  05-assets/
  06-system/
  90-exports/
  99-archive/
```

The retrieval layer is domain-first:

```text
System, Creative, Extraction, Revenue, Client, Research, Content, Ops, Personal
```

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the router inbox instead of being moved automatically.

## Commands

Build or refresh the inventory:

```bash
python3 execution/artifact_router.py inventory
```

Classify a specific path:

```bash
python3 execution/artifact_router.py classify "<path>"
```

Generate a staged move plan:

```bash
python3 execution/artifact_router.py plan
```

Apply only safe moves from a reviewed plan:

```bash
python3 execution/artifact_router.py apply --plan "<plan-json>"
```

Enforce placement for new artifacts before closeout:

```bash
python3 execution/artifact_router.py enforce "<path>" ["<path-2>"]
python3 execution/artifact_frontmatter_guard.py "<path>" ["<path-2>"]
```

## Protocol

1. Run `inventory` before broad cleanup, closeout, or router debugging.
2. Use `classify` before saving or moving a single artifact.
3. Use `plan` for backlog cleanup. Review safe, ambiguous, blocked, and skipped buckets.
4. Use `apply` only for the `safe` bucket. Do not manually move ambiguous files.
5. Use `enforce` and the Markdown readability guard on newly created artifacts before finalizing written, client-facing, or system-changing work.

## Handoff

Every meaningful artifact-producing session should mention:

- canonical project route
- domain metadata
- whether enforcement passed
- any inbox items requiring review

## Verification

After changing this workflow or router behavior, run:

```bash
python3 execution/verify_artifact_router.py
python3 execution/command_menu.py show artifact-router
python3 execution/command_menu.py search "organize files artifacts projects router"
python3 execution/workflow_router.py search "organize files artifacts projects router"
```

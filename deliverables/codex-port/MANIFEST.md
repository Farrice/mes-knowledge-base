# Antigravity To Codex Port Manifest

Imported on: 2026-04-29

## Installed Locations
- Native Codex skills: `/Users/farricecain/.codex/skills`
- Antigravity wrapper skill: `/Users/farricecain/.codex/skills/antigravity-harness`
- Antigravity vendor import: `/Users/farricecain/.codex/vendor_imports/antigravity-system`
- Live source repo: `/Users/farricecain/Google Antigravity`

## Import Notes
- Antigravity `skills/` folders were copied into Codex's native skill directory.
- Existing Codex skill `pdf` was preserved.
- Antigravity's `skills/pdf` was imported as `antigravity-pdf`.
- `.env`, `.git`, `.DS_Store`, and `node_modules/` were excluded from the vendor import.
- The vendor import keeps agents, workflows, directives, execution scripts, registries, knowledge files, and local docs available to Codex outside the live repo.

## Refresh
Run this from the Antigravity repo:

```bash
./deliverables/codex-port/sync-antigravity-to-codex.sh
```


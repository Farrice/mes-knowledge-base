---
status: done
---

# Notion Intellectual Library

> **STATUS 2026-07-06**: historical deploy documentation. The live pipeline is `mirror_notion.py` → `.memory/sovereign.db` (`notion_mirror`), nightly launchd `com.antigravity.mirror-nightly`; write path = `chain_runner` finalize → Notion. This folder is not a live mirror.

## Purpose
Canonical project home managed by the global artifact router.

## Router
Use `python3 execution/artifact_router.py classify <path>` to place new artifacts.

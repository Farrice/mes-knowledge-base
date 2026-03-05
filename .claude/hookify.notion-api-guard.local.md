---
name: notion-api-guard
enabled: true
event: bash
pattern: notion.*client|@notionhq|npm.*notion
action: block
---

**Notion API Guard**: Do not use `@notionhq/client` or npm notion packages. The JS client uses a newer API version that silently fails. Use `python execution/notion_api.py` instead (pins to `Notion-Version: 2022-06-28`). See `directives/notion-databases.md` for database IDs and schemas.

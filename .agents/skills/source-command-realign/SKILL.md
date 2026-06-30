---
name: "source-command-realign"
description: "Load a past work-thread as BACKGROUND context for NEW work (not bound to its old plan). Sibling of /resume, same engine."
---

# source-command-realign

Use this skill when the user asks to run the migrated source command `realign`.

## Command Template

Read and execute the workflow at `.agent/workflows/resume.md` in **/realign mode** — load the selected thread as background context for new work, NOT as a plan to resume. ARGUMENTS = thread selector (number, name, or keyword). If no argument, show the menu (Step 1) first.

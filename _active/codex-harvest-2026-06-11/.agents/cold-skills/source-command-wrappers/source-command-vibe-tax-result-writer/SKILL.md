---
name: "source-command-vibe-tax-result-writer"
description: "Native Codex writer for Vibe Tax Diagnostic results from pasted rows, Notion Codex Input blocks, rough drafts, or approved tracker scans"
---

# source-command-vibe-tax-result-writer

Use this skill when the user invokes `/vibe-tax-result-writer`, asks for the Vibe Tax Result Writer, pastes a diagnostic response, pastes a Notion `Codex Input` block, asks to scan the Vibe Tax tracker for new responses, or asks to turn a rough diagnostic result into a sendable Vibe Tax Read.

This is a draft-only result-writing surface. It may read or parse user-provided rows and approved trackers, but it must not publish, email, DM, update databases, create external docs, or change sharing without explicit approval.

## Command Template

Read and execute the workflow at `.agent/workflows/vibe-tax-result-writer.md` - Generate native Codex Vibe Tax Reads from pasted diagnostic rows, Notion Codex Input blocks, rough drafts, or approved response-tracker scans.

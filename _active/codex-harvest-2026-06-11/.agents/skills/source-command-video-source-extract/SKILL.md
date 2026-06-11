---
name: "source-command-video-source-extract"
description: "Prepare a YouTube video context package for /extract, /extract-forge, source-to-skill-system, or claim-grounded creative work."
---

# source-command-video-source-extract

Use this skill when Farrice invokes `/video-source-extract`, provides a YouTube URL for extraction, or asks for a source package before forge/source-to-skill work.

## Command Template

Read and execute the workflow at `.agent/workflows/video-source-extract.md`.

## Source Truth Requirement

The output package must preserve raw VTT, clean transcript, transcript segments, metadata, ledger, frame/OCR notes, and uncertainty. Visual claims remain blocked unless frame/OCR evidence is reviewed.

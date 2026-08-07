---
name: "source-command-buyer-trigger-os"
description: "Run the source-traced and research-backed Meg Heckman Buyer-Trigger OS for apparel, POD, offers, product ideas, landing pages, and client creative. Modes: research, audit, generate, score, transfer."
---

# source-command-buyer-trigger-os

Use this skill when Farrice invokes `/buyer-trigger-os`, asks for the Meg Heckman buyer-trigger OS, asks to score purchase intent, wants source-traced buyer psychology for apparel, POD, offers, landing pages, product ideas, or client creative, or asks for current buyer insights, trend-backed concepts, purchase intent research, social listening, or research-backed trigger audits.

This is a thin hot launcher. It is not a cheap version and it must not reimplement or summarize the cold skill. It loads the full OS at `skills/meg-heckman-buyer-trigger-os/SKILL.md` and follows `.agent/workflows/buyer-trigger-os.md`.

## Command Template

Read and execute the workflow at `.agent/workflows/buyer-trigger-os.md`.

For current-world evidence, use the workflow's Research-Trace Default and the guarded runner `execution/buyer_trigger_research.py`. Do not invent trends, quotes, buyer language, competitor claims, marketplace claims, or social-listening claims without source URLs.

## Required Source Boundary

Every meaningful output must:

- load the Meg source ledger and genius patterns;
- name source timestamp anchors used;
- separate `Source Mechanics` from `Domain Extrapolation`;
- keep Josh and MyBPM as explicit examples only, not default templates;
- mark revenue/margin as source claims only;
- avoid visual claims unless frame/OCR evidence has actually been reviewed.

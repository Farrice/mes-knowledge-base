---
name: imagegen-static-placement-correction
problem_signature: "image generation returned a taller portrait after an explicit 4:5 request, so downstream static variants risked inheriting the wrong placement"
domain: system
tags: [image-generation, static-ads, aspect-ratio, verification]
date: 2026-08-01
status: active
session: "019fbd9c-8730-7271-9e48-fe232ba41683"
---

## Problem

An ads-marketing image prompt asked for a 4:5 feed asset, but the rendered file measured 1003 × 1568. Building edit variants from that parent would have preserved the wrong placement while making the batch look finished.

## Root Cause

Aspect ratio in a natural-language image prompt is a creative instruction, not a reliable file-level guarantee. The first production check inspected the picture but had not yet treated pixel dimensions as a separate trafficking gate.

## Approach That Worked

1. Read the rendered dimensions before promoting the control. When they missed 4:5, edit the control with a narrow reframe request that named an exact 4:5 canvas and prohibited redesign.
2. Verify the corrected file dimensions, then build every challenger from that corrected parent. Recheck all final files and keep the original generated copies for traceability.

## Dead Ends

Repeating “4:5” inside the initial creative brief was not enough. Accepting the visible portrait shape would also have failed because the wrong ratio was not obvious at a glance.

## Verification

The corrected control and both derived challengers measured 1122 × 1402, the generator's rounded 4:5 output. Visual review confirmed that copy, hierarchy, and the isolated test variables survived the reframe.

## Weaker-Model Trap

A weaker run calls a portrait image “4:5” because it looks vertical, then produces every variant from the bad parent. The correct move separates creative approval from file-spec approval and verifies both.

## Pointers

- `extractions/alex-copper-static-ads/production/morrow-sleep-concept-a/PRODUCTION-AND-AUDIT.md`
- `extractions/alex-copper-static-ads/production/morrow-sleep-concept-a/01-control-ordinary-product.png`
- `/Users/farricecain/.codex/skills/.system/imagegen/SKILL.md`

---
name: mybpm-horizon-premium-relaunch
problem_signature: "Build a credible premium Shopify relaunch without live store write access while separating verified product proof from sample-gated merchandising"
domain: client-work
tags: [shopify, horizon, streetwear, merchandising, staging]
date: 2026-08-29
status: active
session: "Client: MyBPM Shopify - Premium Relaunch Build"
---

## Problem

MyBPM needed a premium fashion-store relaunch, but the live catalog mixed current on-body product proof with old mockups, duplicate concepts, long descriptions, and broken supplier/swatch assets. The task had no authenticated Shopify write surface and could not safely publish.

## Root Cause

The visible website problem was downstream of an uncurated merchandising system: no shared product admission bar, no campaign-level data contract, and no boundary between verified claims and aspirational premium copy.

## Approach That Worked

1. Audit the live store and select one evidence-backed visual lead, then mark every supporting product as sample-gated instead of upgrading it through language.
2. Build an unpublished Horizon-based theme and static visual preview around a reusable drop system: editorial sections, structured product metafields, capsule status, photography rules, launch QA, and explicit publish approval.

## Dead Ends

Running Shopify CLI through the restricted network hung with no output; rerunning the same scoped command with approved network access completed. A guessed storefront image suffix returned 404 and was replaced only after browser HEAD verification.

## Verification

Shopify Theme Check 4.7.0 passed 363 files with no offenses. The local verifier passed 75 JSON files, 141 Liquid schema objects, wiring, placeholders, local links, anchors, and alt text. Browser checks at 1440 and 390 pixels showed no overflow, broken images, or console errors.

## Weaker-Model Trap

Treating the task as a color-and-layout makeover would make every weak catalog item look more prominently weak. The premium claim must be constrained by physical sample, product data, fulfillment truth, and current photography.

## Pointers

- `_active/mybpm/premium-shopify-relaunch/README.md`
- `_active/mybpm/premium-shopify-relaunch/03-capsule-selection.md`
- `_active/mybpm/premium-shopify-relaunch/07-build-receipt.md`
- `_active/mybpm/premium-shopify-relaunch/theme/`

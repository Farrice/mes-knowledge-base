---
name: health-performance-paid-pilot-readiness
problem_signature: "A current paid health-marketing offer was package-ready but not client-delivery-ready because no named brand had supplied account evidence, approved claims, or human owners"
domain: revenue
tags: [marketing-engineering, health-performance, paid-pilot, readiness, proof-boundary]
date: 2026-08-31
status: active
session: "Revenue: Health Marketing Engineering Pilot - Readiness and Offer"
---

## Problem

The Control-Beater had a current buyer, price, scope, turnaround, and claim-safe promise, but the Marketing Engineering readiness contract also required real client data, a baseline, permissions, and human approval owners. Treating the existing offer package as full client readiness would have invented the evidence-to-outcome loop the service is supposed to prove.

## Root Cause

Two readiness questions had been collapsed: whether the exact offer was ready for a payment decision, and whether a named client had supplied enough evidence and authority for production. The first was ready; the second had no event and no approved client source set.

## Approach That Worked

1. Preserve the newest committed commercial owner and exact offer instead of reviving an older strategy offer or promoting the broader 15-Ad Pack.
2. Issue one `DISCOVER FIRST` verdict, select `creative_testing`, use cleared $500 pilot revenue as the primary business event, and require a client fit/input gate before any `BUILD` run.
3. Freeze a local pilot contract, machine-readable hypothesis, zero-event ledger, and reusable fit packet with external actions empty.
4. Separate payment, delivery, launch, and outcome proof so one cleared purchase cannot be relabeled as performance or repeatability.

## Dead Ends

- Calling the infrastructure `BUILD`-ready because category research and spec creative already existed.
- Replacing the current $500 Control-Beater with the $1,000 15-Ad Creative Test Pack before a paid event.
- Using creative volume, replies, calls, or verbal acceptance as the primary success metric.
- Promising control-beating, legal clearance, platform acceptance, or account performance without client-authorized evidence.

## Verification

- The exact Control-Beater preservation source resolves at commit `2a99eb327`.
- The contract contains one wedge: `creative_testing`.
- The primary metric is one cleared $500 payment; activity counts are secondary diagnostics.
- `external_actions` is empty and the demand test is explicitly unauthorized.
- The ledger baseline is `NO EVENT / $0`.
- The claim boundary requires product-specific sources, a qualified client reviewer, and a client launch owner.

## Weaker-Model Trap

A weaker model will confuse a complete offer page with a ready client system, or will “improve” the work by introducing a second offer, higher price, performance guarantee, dashboard, or software layer. The correct move is to preserve the current commercial owner, separate offer validation from delivery readiness, and stop at the nearest missing evidence.

## Pointers

- `deliverables/marketing-engineering/health-performance-control-beater/readiness-and-paid-pilot.md`
- `deliverables/marketing-engineering/health-performance-control-beater/pilot-hypothesis.json`
- `deliverables/marketing-engineering/health-performance-control-beater/control-beater-fit-and-input-packet.md`
- `deliverables/marketing-engineering/health-performance-control-beater/demand-ledger.csv`
- `skills/marketing-engineering-service-system/`

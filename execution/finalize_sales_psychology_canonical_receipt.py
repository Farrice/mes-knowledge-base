#!/usr/bin/env python3
"""Regenerate the canonical buyer-psychology file manifest.

This helper deliberately does not edit the verifier's frozen receipt hash. That
manual one-line update keeps receipt generation separate from trust admission.
"""

from __future__ import annotations

import argparse
import json

from jason_buyer_psychology_runtime_surface import runtime_policy_attestation
from verify_sales_psychology_mastery_layer import (
    ROOT,
    RUN_RECEIPT,
    jason_context_index_attestation,
    sha256,
    trust_paths,
)


def expected_manifest() -> dict[str, str]:
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in trust_paths()
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    receipt = json.loads(RUN_RECEIPT.read_text(encoding="utf-8"))
    expected = expected_manifest()
    expected_runtime = runtime_policy_attestation(ROOT)
    expected_context_index = jason_context_index_attestation()
    if expected_context_index.get("matchesLiveSkill") is not True:
        print("FAIL: cached Jason context index does not match live skill chunking")
        return 1
    if args.check:
        if receipt.get("manifest_sha256") != expected:
            print("FAIL: canonical verification receipt manifest drift")
            return 1
        actual_runtime = receipt.get("activeRuntimeSurface", {})
        policy_fields = ("scannedFileCount", "fullSurfaceSha256", "policyAggregateSha256", "overlayPointers", "pointerParagraphSha256", "coldMarkerViolations", "promotionViolations")
        if any(actual_runtime.get(field) != expected_runtime.get(field) for field in policy_fields):
            print("FAIL: canonical verification receipt runtime-surface drift")
            return 1
        if receipt.get("jasonContextIndex") != expected_context_index:
            print("FAIL: canonical verification receipt Jason context-index drift")
            return 1
        print("PASS: canonical verification receipt manifest")
        print(f"- files: {len(expected)}")
        print(f"- active runtime files scanned now: {expected_runtime['scannedFileCount']}")
        print(f"- receipt sha256: {sha256(RUN_RECEIPT)}")
        return 0
    receipt["manifest_sha256"] = expected
    receipt["activeRuntimeSurface"] = expected_runtime
    receipt["jasonContextIndex"] = expected_context_index
    RUN_RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"WROTE {RUN_RECEIPT}")
    print(f"- files: {len(expected)}")
    print(f"- active runtime files scanned: {expected_runtime['scannedFileCount']}")
    print(f"- receipt sha256: {sha256(RUN_RECEIPT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

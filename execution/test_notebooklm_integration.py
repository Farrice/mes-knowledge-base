#!/usr/bin/env python3
"""
NotebookLM Integration Tests

Usage:
    python execution/test_notebooklm_integration.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from execution.notebooklm_client import NotebookLMClient, load_env


def test_client():
    """Test client initialization."""
    print("Test 1: Client initialization...")

    load_env()
    client = NotebookLMClient()

    notebooks = client.list_notebooks()

    if len(notebooks) >= 3:
        print(f"  ✓ Found {len(notebooks)} registered notebooks")
        return True
    else:
        print(f"  ✗ Expected 3+ notebooks, found {len(notebooks)}")
        return False


def test_budget():
    """Test budget tracking."""
    print("\nTest 2: Budget tracking...")

    load_env()
    client = NotebookLMClient()

    queries_used, queries_remaining = client.check_budget()

    print(f"  ✓ Used: {queries_used}/100")
    print(f"  ✓ Remaining: {queries_remaining}")

    return queries_remaining >= 0


def run_tests():
    """Run all tests."""
    print("=" * 60)
    print("NotebookLM Integration Tests")
    print("=" * 60)

    tests = [
        ("Client initialization", test_client),
        ("Budget tracking", test_budget),
    ]

    results = []

    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"\n  ✗ Test failed: {e}")
            results.append((name, False))

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)

    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status:10} {name}")

    print(f"\nTotal: {passed_count}/{total_count} passed")

    if passed_count == total_count:
        print("\n🎉 All tests passed!")
        return 0
    else:
        return 1


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)

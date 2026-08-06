#!/usr/bin/env python3
"""Fail closed when a smoke record lacks branch-required browser capabilities."""

import argparse
import json
import sys
from pathlib import Path


def capability_value(capabilities, name):
    value = capabilities.get(name)
    if isinstance(value, dict):
        return bool(value.get("verified"))
    return value is True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--adapter", required=True)
    parser.add_argument("--require", action="append", default=[])
    args = parser.parse_args()

    payload = json.loads(args.record.read_text())
    matches = [item for item in payload.get("results", []) if item.get("adapter") == args.adapter]
    record = matches[-1] if matches else {}
    nested = record.get("details") or {}
    details = nested.get("details") or nested
    capabilities = details.get("capabilities") or {}
    checks = {name: capability_value(capabilities, name) for name in args.require}
    passed = record.get("status") == "pass" and all(checks.values())
    result = {
        "gate": "PASS" if passed else "FAIL",
        "adapter": args.adapter,
        "skill_version": payload.get("skill_version"),
        "tested_at": payload.get("tested_at"),
        "required": checks,
        "missing_or_failed": [name for name, ok in checks.items() if not ok],
        "note": "Target-service disposable write/readback/clear is still required before a real prompt.",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

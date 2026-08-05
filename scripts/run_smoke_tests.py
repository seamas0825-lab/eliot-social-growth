#!/usr/bin/env python3
"""Run one or more adapter smoke tests and save reproducible JSON evidence."""

import argparse
import datetime as dt
import json
import os
import platform
import re
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command, timeout=180):
    started = time.monotonic()
    result = subprocess.run(command, text=True, capture_output=True, timeout=timeout, check=False)
    return result, round(time.monotonic() - started, 3)


def clean(text):
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[redacted-email]", text or "")
    return text[-4000:]


def version(command, fallback="unknown"):
    try:
        result = subprocess.run(command, text=True, capture_output=True, timeout=15, check=False)
        value = (result.stdout or result.stderr).strip().splitlines()
        return value[0] if value else fallback
    except Exception:
        return fallback


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--adapter", action="append", choices=["ego", "browser-use", "web-access"], required=True)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--task-space", default="social-media-skill-smoke")
    parser.add_argument("--browser-executable")
    parser.add_argument("--web-access-dir")
    parser.add_argument("--chrome-path")
    parser.add_argument("--launch-chrome", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()

    records = []
    for adapter in args.adapter:
        if adapter == "ego":
            command = [sys.executable, str(ROOT / "scripts/smoke_ego.py"), "--task-space", args.task_space]
            tool_version = version(["ego-browser", "--version"])
        elif adapter == "browser-use":
            command = [args.python, str(ROOT / "scripts/smoke_browser_use.py")]
            if args.browser_executable:
                command += ["--executable-path", args.browser_executable]
            tool_version = version([args.python, "-c", "import importlib.metadata; print(importlib.metadata.version('browser-use'))"])
        else:
            if not args.web_access_dir:
                parser.error("--web-access-dir is required for web-access")
            command = ["node", str(ROOT / "scripts/smoke_web_access.mjs"), "--web-access-dir", args.web_access_dir]
            if args.chrome_path:
                command += ["--chrome-path", args.chrome_path]
            if args.launch_chrome:
                command.append("--launch-chrome")
            commit = version(["git", "-C", args.web_access_dir, "rev-parse", "--short", "HEAD"])
            tool_version = f"web-access commit {commit}; {version(['node', '--version'])}"

        try:
            result, duration = run(command)
            stdout, stderr = clean(result.stdout), clean(result.stderr)
            records.append({
                "adapter": adapter,
                "tool_version": tool_version,
                "status": "pass" if result.returncode == 0 else "fail",
                "exit_code": result.returncode,
                "duration_seconds": duration,
                "stdout": stdout,
                "stderr": stderr,
            })
        except Exception as exc:
            records.append({"adapter": adapter, "tool_version": tool_version, "status": "error", "error": str(exc)})

    now = dt.datetime.now(dt.timezone.utc)
    payload = {
        "schema_version": 1,
        "skill_version": (ROOT / "VERSION").read_text().strip(),
        "tested_at": now.isoformat(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "results": records,
        "passed": all(item["status"] == "pass" for item in records),
        "scope": "Public-page startup, navigation, readback, and cleanup only; authenticated reliability is not implied.",
    }
    output = Path(args.output) if args.output else ROOT / "test-results" / f"smoke-{now.date().isoformat()}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

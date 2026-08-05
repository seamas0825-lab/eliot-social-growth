#!/usr/bin/env python3
"""Harmless EGO navigation/readback smoke test with dedicated cleanup."""

import argparse
import json
import subprocess
import sys


def run_ego(script):
    return subprocess.run(
        ["ego-browser", "nodejs"],
        input=script,
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-space", default="social-media-skill-smoke")
    args = parser.parse_args()
    target = int(args.task_space) if args.task_space.isdigit() else args.task_space
    target_js = json.dumps(target)

    test_script = f"""
const task = await useOrCreateTaskSpace({target_js})
await openOrReuseTab('https://example.com', {{ wait: true, timeout: 20 }})
const info = await pageInfo()
const text = await snapshotText()
const ok = info.url.startsWith('https://example.com') && text.includes('Example Domain')
cliLog(JSON.stringify({{ok, taskSpaceId: task.id, url: info.url, title: info.title, marker: text.includes('Example Domain')}}))
"""
    test = run_ego(test_script)
    cleanup_script = f"""
const result = await completeTaskSpace({target_js}, {{ keep: false }})
cliLog(JSON.stringify(result))
"""
    cleanup = run_ego(cleanup_script)

    test_stream = (test.stdout or "") + (test.stderr or "")
    cleanup_stream = (cleanup.stdout or "") + (cleanup.stderr or "")
    payload = {
        "ok": test.returncode == 0 and '"ok":true' in test_stream and cleanup.returncode == 0 and '"done":true' in cleanup_stream,
        "adapter": "ego",
        "test_output": test.stdout.strip(),
        "test_error": test.stderr.strip(),
        "cleanup_output": cleanup.stdout.strip(),
        "cleanup_error": cleanup.stderr.strip(),
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

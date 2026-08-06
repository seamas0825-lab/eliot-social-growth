#!/usr/bin/env python3
"""Harmless EGO runtime capability smoke test with dedicated cleanup."""

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


def extract_json(text):
    for line in reversed((text or "").splitlines()):
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-space", default="social-media-skill-smoke")
    args = parser.parse_args()
    target = int(args.task_space) if args.task_space.isdigit() else args.task_space
    target_js = json.dumps(target)

    test_script = """
const task = await useOrCreateTaskSpace(__TARGET__)
await openOrReuseTab('https://example.com', { wait: true, timeout: 20 })
const info = await pageInfo()
const text = await snapshotText()
const helperTypes = {
  snapshotText: typeof snapshotText,
  captureScreenshot: typeof captureScreenshot,
  fillInput: typeof fillInput,
  js: typeof js,
}
const diagnostic = typeof help === 'function' ? await help('captureScreenshot') : 'help unavailable'
const domSetup = await js(String.raw`(() => {
  document.querySelector('#ego-smoke-fixture')?.remove()
  const root = document.createElement('div')
  root.id = 'ego-smoke-fixture'
  const ta = document.createElement('textarea')
  ta.id = 'ego-smoke-ta'
  const ce = document.createElement('div')
  ce.id = 'ego-smoke-ce'
  ce.contentEditable = 'true'
  root.append(ta, ce)
  document.body.append(root)
  return true
})()`)
let textareaInput = false
let contenteditableInput = false
if (typeof fillInput === 'function') {
  await fillInput('#ego-smoke-ta', 'ego-textarea-probe')
  textareaInput = await js(String.raw`document.querySelector('#ego-smoke-ta')?.value === 'ego-textarea-probe'`)
  await fillInput('#ego-smoke-ta', '')
  await fillInput('#ego-smoke-ce', 'ego-contenteditable-probe')
  contenteditableInput = await js(String.raw`document.querySelector('#ego-smoke-ce')?.textContent === 'ego-contenteditable-probe'`)
  await fillInput('#ego-smoke-ce', '')
}
let visualCapture = {available: typeof captureScreenshot === 'function', verified: false, error: ''}
if (visualCapture.available) {
  try {
    const result = await Promise.race([
      captureScreenshot().then(value => ({state: 'resolved', value})).catch(error => ({state: 'rejected', error: String(error)})),
      new Promise(resolve => setTimeout(() => resolve({state: 'timeout'}), 10000)),
    ])
    visualCapture.state = result.state
    visualCapture.verified = result.state === 'resolved' && Boolean(result.value)
    visualCapture.returnType = result.state === 'resolved' ? typeof result.value : undefined
    visualCapture.error = result.error || ''
  } catch (error) {
    visualCapture.error = String(error)
  }
}
await js(String.raw`document.querySelector('#ego-smoke-fixture')?.remove()`)
const capabilities = {
  navigation: info.url.startsWith('https://example.com'),
  semantic_snapshot: text.includes('Example Domain'),
  dom_evaluation: domSetup === true,
  visual_capture: visualCapture,
  textarea_input: textareaInput === true,
  contenteditable_input: contenteditableInput === true,
}
const coreOk = capabilities.navigation && capabilities.semantic_snapshot && capabilities.dom_evaluation && capabilities.textarea_input && capabilities.contenteditable_input
cliLog(JSON.stringify({ok: coreOk, taskSpaceId: task.id, url: info.url, title: info.title, helperTypes, diagnostic, capabilities}))
""".replace("__TARGET__", target_js)
    test = run_ego(test_script)
    cleanup_script = f"""
const result = await completeTaskSpace({target_js}, {{ keep: false }})
cliLog(JSON.stringify(result))
"""
    cleanup = run_ego(cleanup_script)

    test_stream = (test.stdout or "") + "\n" + (test.stderr or "")
    cleanup_stream = (cleanup.stdout or "") + (cleanup.stderr or "")
    details = extract_json(test_stream)
    cleanup_details = extract_json(cleanup_stream)
    payload = {
        "ok": test.returncode == 0 and bool(details and details.get("ok")) and cleanup.returncode == 0 and bool(cleanup_details and cleanup_details.get("done")),
        "adapter": "ego",
        "details": details,
        "cleanup": cleanup_details,
        "test_output": test.stdout.strip(),
        "test_error": test.stderr.strip(),
        "cleanup_output": cleanup.stdout.strip(),
        "cleanup_error": cleanup.stderr.strip(),
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

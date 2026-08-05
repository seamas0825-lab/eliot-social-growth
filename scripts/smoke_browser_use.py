#!/usr/bin/env python3
"""Browser Use public-page navigation/readback smoke test; no LLM required."""

import argparse
import asyncio
import importlib.metadata
import json
import sys


async def smoke(executable_path):
    from browser_use import BrowserProfile, BrowserSession

    profile_args = {
        "headless": True,
        "user_data_dir": None,
        "keep_alive": False,
    }
    if executable_path:
        profile_args["executable_path"] = executable_path
    session = BrowserSession(browser_profile=BrowserProfile(**profile_args))
    try:
        await session.start()
        page = await session.new_page("https://example.com")
        title, url = "", ""
        for _ in range(40):
            title = await page.get_title()
            url = await page.get_url()
            if title == "Example Domain" and url.startswith("https://example.com"):
                break
            await asyncio.sleep(0.25)
        ok = url.startswith("https://example.com") and title == "Example Domain"
        return {"ok": ok, "adapter": "browser-use", "url": url, "title": title}
    finally:
        await session.kill()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable-path")
    args = parser.parse_args()
    try:
        result = asyncio.run(smoke(args.executable_path))
        result["version"] = importlib.metadata.version("browser-use")
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result["ok"] else 1
    except Exception as exc:
        print(json.dumps({"ok": False, "adapter": "browser-use", "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())

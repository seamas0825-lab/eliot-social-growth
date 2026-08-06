#!/usr/bin/env python3
"""Dependency-free package, link, naming, and privacy validation."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def main():
    failures = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    if not skill.startswith("---\nname: eliot-social-growth\n"):
        failures.append("SKILL.md frontmatter name is not eliot-social-growth")
    if skill.count("\n") + 1 > 500:
        failures.append("SKILL.md exceeds 500 lines")
    if f"version-{version}-blue" not in readme or f"Current version: **{version}**" not in readme:
        failures.append("README version does not match VERSION")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            clean = target.strip().strip("<>").split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                failures.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in EMAIL.findall(text):
            failures.append(f"possible committed account identifier: {path.relative_to(ROOT)} -> {match}")

    result = {
        "skill": "eliot-social-growth",
        "version": version,
        "markdown_files": len(list(ROOT.rglob("*.md"))),
        "failures": sorted(set(failures)),
        "passed": not failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate SKILL.md files in this repository.

Checks the front matter rules Bionic uses, plus that locally referenced
files actually exist. Exits non-zero if anything is wrong.

Usage:
    python3 scripts/validate_skills.py [skills-root]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REF_RE = re.compile(r"`((?:\.\./)?[A-Za-z0-9._/-]+\.md)`")

MAX_NAME = 63
SOFT_DESC = 150
HARD_DESC = 300


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    block, body = parts[1], parts[2]
    data: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def check_skill(skill_dir: Path) -> list[str]:
    problems: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    meta, _ = parse_front_matter(text)
    name = meta.get("name", "")
    desc = meta.get("description", "")

    if not name:
        problems.append(f"{skill_dir.name}: front matter has no `name`")
    else:
        if name != skill_dir.name:
            problems.append(
                f"{skill_dir.name}: `name: {name}` does not match the folder name"
            )
        if len(name) > MAX_NAME:
            problems.append(f"{skill_dir.name}: name is longer than {MAX_NAME} chars")
        if not NAME_RE.match(name):
            problems.append(
                f"{skill_dir.name}: name must be kebab-case (a-z, 0-9, single hyphens)"
            )

    if not meta.get("display-name"):
        problems.append(f"{skill_dir.name}: no `display-name`")

    if not desc:
        problems.append(f"{skill_dir.name}: front matter has no `description`")
    elif len(desc) > HARD_DESC:
        problems.append(
            f"{skill_dir.name}: description is {len(desc)} chars (limit {HARD_DESC})"
        )
    elif len(desc) > SOFT_DESC:
        problems.append(
            f"{skill_dir.name}: description is {len(desc)} chars, aim for under {SOFT_DESC}"
        )

    for ref in sorted(set(REF_RE.findall(text))):
        if ref.startswith(("http://", "https://")):
            continue
        target = (skill_dir / ref).resolve()
        if not target.is_file():
            problems.append(f"{skill_dir.name}: referenced file not found: {ref}")

    return problems


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".agents/skills")
    if not root.is_dir():
        print(f"error: {root} is not a directory")
        return 2

    skill_dirs = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not skill_dirs:
        print(f"error: no skills found in {root}")
        return 2

    problems: list[str] = []
    seen: dict[str, Path] = {}
    for skill_dir in skill_dirs:
        problems.extend(check_skill(skill_dir))
        meta, _ = parse_front_matter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
        name = meta.get("name", "")
        if name in seen:
            problems.append(f"duplicate skill name `{name}`: {seen[name]} and {skill_dir}")
        seen[name] = skill_dir

    for skill_dir in skill_dirs:
        meta, body = parse_front_matter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
        print(
            f"  {meta.get('name', skill_dir.name):28s} "
            f"desc {len(meta.get('description', '')):3d} chars  "
            f"body {len(body.splitlines()):4d} lines"
        )

    if problems:
        print("\nproblems:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print(f"\nok: {len(skill_dirs)} skills valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

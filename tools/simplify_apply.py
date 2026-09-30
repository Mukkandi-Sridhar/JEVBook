"""Apply a batch of wording changes and log them: python3 tools/simplify_apply.py "Chapter 5" edits.py

edits.py defines EDITS = [(file, before, after), ...]. Each `before` must occur exactly once in its file (the
script stops before changing anything if one doesn't). The pairs are appended to SIMPLIFY.md under the heading given,
so every change made in the language pass is on record.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "SIMPLIFY.md"


def main(label: str, edits_file: str):
    edits = [e for e in runpy.run_path(edits_file)["EDITS"] if e[1] != e[2]]   # ignore no-op pairs
    texts: dict[str, str] = {}
    for f, before, after in edits:
        texts.setdefault(f, (ROOT / f).read_text())
    problems = []
    for f, before, after in edits:
        n = texts[f].count(before)
        if n != 1:
            problems.append(f"{f}: found {n} times: {before[:70]!r}")
    if problems:
        sys.exit("not applied:\n" + "\n".join(problems))
    for f, before, after in edits:
        texts[f] = texts[f].replace(before, after, 1)
    for f, t in texts.items():
        (ROOT / f).write_text(t)
    log = [f"\n## {label}\n", f"{len(edits)} changes.\n"]
    for f, before, after in edits:
        log.append(f"- `{f}`\n  - Before: {before.strip()}\n  - After: {after.strip() or '(removed)'}")
    with LOG.open("a") as fh:
        fh.write("\n".join(log) + "\n")
    print(f"{label}: {len(edits)} changes applied")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

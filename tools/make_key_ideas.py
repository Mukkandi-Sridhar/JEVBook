"""Write the Key ideas appendix from the chapters: python3 tools/make_key_ideas.py [--check]

Every ::: {.keyidea} box in chapters/chNN.qmd, in order, becomes one line of back/key-ideas.qmd, grouped by chapter.
Each line ends with [ ]{.kref ref="key-chNN-K"}: filters/book.lua gives the box that id (K counts the chapter's key
ideas in order) and turns the span into the page number in print and a link in the ebook. --check exits 1 if the
file is out of date.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "back" / "key-ideas.qmd"

HEAD = """# Key ideas {.unnumbered #sec-key-ideas}

<!-- Made by tools/make_key_ideas.py from the key idea boxes in the chapters. Don't edit by hand. -->

These are the book's key ideas, chapter by chapter, with the page where each one is explained. Use them to revise.
If a line no longer makes sense to you, go back to its page and read that part again.

::: {.keyideaslist}
"""


def key_ideas() -> list[tuple[int, str, list[str]]]:
    out = []
    for f in sorted((ROOT / "chapters").glob("ch[0-9][0-9].qmd")):
        text = f.read_text()
        n = int(f.stem[2:])
        title = re.search(r"^# (.*?)\s*\{#sec-ch\d+\}", text, re.M).group(1)
        keys = [re.sub(r"\s+", " ", k.strip()) for k in re.findall(r"^::: \{\.keyidea\}\n(.*?)\n:::", text, re.S | re.M)]
        out.append((n, title, keys))
    return out


def render() -> str:
    lines = [HEAD]
    for n, title, keys in key_ideas():
        if not keys:
            continue
        lines.append(f"`\\keychapter{{`{{=latex}}**Chapter {n}. {title}**`}}`{{=latex}}\n")
        for k, key in enumerate(keys, 1):
            plain = key.replace("**", "")
            lines.append(f"- {plain} [ ]{{.kref ref=\"key-ch{n:02d}-{k}\"}}")
        lines.append("")
    lines.append(":::\n")
    return "\n".join(lines)


if __name__ == "__main__":
    new = render()
    if "--check" in sys.argv:
        sys.exit(0 if OUT.exists() and OUT.read_text() == new else "back/key-ideas.qmd is out of date: run tools/make_key_ideas.py")
    OUT.write_text(new)
    print(f"{OUT.relative_to(ROOT)}: {sum(len(k) for _, _, k in key_ideas())} key ideas")

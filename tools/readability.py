"""Readability of the book's prose: python3 tools/readability.py [files...] [--long N] [--json out.json]

For each file: US grade level (Flesch-Kincaid), average sentence length, and the share of sentences over 25 words.
Only prose counts: code blocks, figures, tables, maths, citations, div fences and headings are removed first, and
number shortcodes read as a number. --long N also prints every sentence longer than N words.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import textstat

ROOT = Path(__file__).resolve().parent.parent


def prose(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)                  # YAML header
    text = re.sub(r"^```.*?^```\s*$", " ", text, flags=re.S | re.M)           # code blocks
    text = re.sub(r"\{\{<\s*num[^>]*>\}\}", "12", text)                       # numbers from results/
    text = re.sub(r"\{\{<[^>]*>\}\}", "", text)
    out = []
    for line in text.splitlines():
        s = line.strip()
        if (not s or s.startswith(("#", ":::", "|", "![", "<", "```", "\\")) or re.match(r"^[-*]{3,}$", s)):
            out.append("")
            continue
        out.append(line)
    text = "\n".join(out)
    text = text.replace("\\$", "USD ")                                         # escaped dollar signs are money
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$", "x", text)                                  # inline maths reads as one word
    text = re.sub(r"\s*\[-?@[^\]]*\]", "", text)                              # citations
    text = re.sub(r"@(fig|tbl|sec)-[\w-]+", "Figure 1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)                      # links
    text = re.sub(r"\{[^}]*\}", "", text)                                     # attributes
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[*_]{1,2}([^*_]+)[*_]{1,2}", r"\1", text)
    text = re.sub(r"^\s*(\d+\.|[-*])\s+", "", text, flags=re.M)               # list markers
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text)]
    return "\n\n".join(p for p in paras if p)


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])[\"”’)]*\s+(?=[\"“‘(]*[A-Z0-9])", text.replace("\n\n", " \n\n "))
    return [s.strip() for s in parts if len(s.split()) >= 3]


def stats(path: Path) -> dict:
    t = prose(path.read_text())
    sents = sentences(t)
    lens = [len(s.split()) for s in sents]
    return dict(file=str(path.relative_to(ROOT)), words=sum(lens), grade=round(textstat.flesch_kincaid_grade(t), 1),
                avg_sentence=round(sum(lens) / max(1, len(lens)), 1),
                over25=round(100 * sum(l > 25 for l in lens) / max(1, len(lens)), 1),
                over30=sum(l > 30 for l in lens))


def main(argv):
    long_n = None
    out_json = None
    files = []
    it = iter(argv)
    for a in it:
        if a == "--long":
            long_n = int(next(it))
        elif a == "--json":
            out_json = next(it)
        else:
            files.append(ROOT / a)
    if not files:
        files = [ROOT / "index.qmd", *sorted((ROOT / "front").glob("*.qmd")), *sorted((ROOT / "parts").glob("*.qmd")),
                 *sorted((ROOT / "chapters").glob("*.qmd")), *sorted((ROOT / "back").glob("*.qmd"))]
    rows = [stats(f) for f in files]
    print(f"{'file':32} {'words':>6} {'grade':>6} {'avg':>5} {'>25%':>5} {'>30':>4}")
    for r in rows:
        print(f"{r['file']:32} {r['words']:6} {r['grade']:6} {r['avg_sentence']:5} {r['over25']:5} {r['over30']:4}")
    all_text = "\n\n".join(prose(f.read_text()) for f in files)
    print(f"{'ALL':32} {sum(r['words'] for r in rows):6} {textstat.flesch_kincaid_grade(all_text):6.1f}")
    if long_n:
        for f in files:
            for s in sentences(prose(f.read_text())):
                if len(s.split()) > long_n:
                    print(f"\n[{f.name} {len(s.split())}] {s}")
    if out_json:
        Path(out_json).write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])

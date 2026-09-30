"""Code lines that wrap in the PDF: python3 tools/check_code_wrap.py [book.pdf] [book.tex]

Reads every code listing and cell output from the kept LaTeX file, and the monospace lines from the PDF (via
`mutool draw -F stext`). A listing line that doesn't appear whole on one PDF line has wrapped. Exits 1 if any code
line wraps; long output lines (data, one record per line) are listed but allowed.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ESCAPES = [(r"\textgreater{}", ">"), (r"\textless{}", "<"), (r"\textquotesingle{}", "'"), (r"\textbar{}", "|"),
           (r"\textasciitilde{}", "~"), (r"\ldots{}", "…"), (r"\textbackslash{}", "\\")]


def norm(s: str) -> str:
    s = re.sub(r"\s+", "", s)
    return s.translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'}))


def detok(line: str) -> str:
    """Visible text of one Highlighting line: drop the \\XxxTok{...} wrappers and unescape."""
    for a, b in ESCAPES:
        line = line.replace(a, b)
    out, i = [], 0
    while i < len(line):
        c = line[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)\{", line[i:])
            if m:
                i += len(m.group(0))
                continue
            if i + 1 < len(line):
                out.append(line[i + 1])
                i += 2
                continue
        if c not in "{}":
            out.append(c)
        i += 1
    return "".join(out)


def pdf_mono_lines(pdf: Path) -> list[str]:
    with tempfile.TemporaryDirectory() as d:
        stext = Path(d) / "book.stext"
        subprocess.run(["mutool", "draw", "-q", "-F", "stext", "-o", str(stext), str(pdf)], check=True,
                       stderr=subprocess.DEVNULL)
        rows = []
        for _, el in ET.iterparse(stext, events=("end",)):
            if el.tag != "page":
                continue
            by_y: dict[float, list] = {}
            for font in el.iter("font"):
                if "JetBrains" in font.get("name"):
                    for ch in font.iter("char"):
                        by_y.setdefault(round(float(ch.get("y")), 1), []).append((float(ch.get("x")), ch.get("c")))
            rows += [norm("".join(c for _, c in sorted(chs))) for chs in by_y.values()]
            el.clear()
    return rows


def main(pdf: Path, tex: Path) -> int:
    t = tex.read_text()
    blocks = [("code", [detok(l) for l in m.group(1).splitlines()])
              for m in re.finditer(r"\\begin\{Highlighting\}[^\n]*\n(.*?)\\end\{Highlighting\}", t, re.S)]
    blocks += [("output", m.group(1).splitlines())
               for m in re.finditer(r"\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}", t, re.S)]
    rows = pdf_mono_lines(pdf)
    wrapped = [(kind, l.rstrip()) for kind, lines in blocks for l in lines
               if norm(l) and not any(norm(l) in r for r in rows)]
    print(f"{len(blocks)} listings and outputs checked")
    for kind, l in wrapped:
        print(f"{kind:6} {len(l):3}  {l}")
    code = sum(k == "code" for k, _ in wrapped)
    print(f"wrapped code lines: {code}; wrapped output lines (allowed): {len(wrapped) - code}")
    return 1 if code else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.exit(main(Path(a[0]) if a else ROOT / "_book" / "Decide,-Don-t-Generate.pdf",
                  Path(a[1]) if len(a) > 1 else ROOT / "Decide,-Don-t-Generate.tex"))

"""Regenerate the chapter table in PROGRESS.md from the repository itself.

usage: python tools/progress.py [--pdf _book/*.pdf]

Words and voice come from tools/voice_check.py; figures from figures/chNN/*.pdf (minus the map and QR);
labs from whether labs/chNN.py exists (CI runs them); open [[VERIFY]] marks are counted in the chapter source;
pages are read from the rendered PDF when one is given.
"""
import contextlib
import io
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from jevkit.figs.bookmap import PARTS  # noqa: E402
import voice_check  # noqa: E402


def chapter_pages(pdf: str) -> dict:
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout)[1])
    starts = {}
    for i in range(1, n + 1):
        head = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), pdf, "-"], capture_output=True,
                              text=True).stdout[:80]
        m = re.match(r"\s*CHAPTER (\d+)\s*\n", head)
        if m and int(m[1]) not in starts:
            starts[int(m[1])] = i
    out = {}
    ks = sorted(starts)
    for a, b in zip(ks, ks[1:] + [None]):
        end = starts[b] if b else n
        out[a] = end - starts[a]
    return out


def row(num, ch, title, pages):
    q = ROOT / "chapters" / f"{ch}.qmd"
    text = q.read_text()
    if "Draft in progress" in text:
        return f"| {num} | {title} | – | – | – | – | – | – |"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        issues = voice_check.check(q)
    words = re.search(r"(\d+) words", buf.getvalue())
    figs = [p for p in (ROOT / "figures" / ch).glob("*.pdf") if p.stem not in ("map", "qr")]
    nfig = len([p for p in figs if p.stem != "summary"])
    summ = " + summary" if any(p.stem == "summary" for p in figs) else ""
    lab = "ok" if (ROOT / "labs" / f"{ch}.py").exists() else "–"
    verify = text.count("[[VERIFY]]")
    pg = pages.get(num, "–")
    return (f"| {num} | {title} | {int(words[1]):,} | {pg} | {nfig}{summ} | {lab} | "
            f"{'pass' if issues == 0 else f'{issues} issue(s)'} | {verify} |")


def main():
    pdf = sys.argv[sys.argv.index("--pdf") + 1] if "--pdf" in sys.argv else None
    pages = chapter_pages(pdf) if pdf else {}
    rows = ["| Ch | Title | Words | Pages | Figures | Lab | Voice | Open [[VERIFY]] |", "|---|---|---|---|---|---|---|---|"]
    for _, _, chs in PARTS:
        for num, ch, title in chs:
            rows.append(row(num, ch, title, pages))
    p = ROOT / "PROGRESS.md"
    s = p.read_text()
    start = s.index("| Ch | Title |")
    end = s.index("\n\n", start)
    p.write_text(s[:start] + "\n".join(rows) + s[end:])
    print("\n".join(rows))


if __name__ == "__main__":
    main()

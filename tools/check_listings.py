"""Run every executable listing (```{python} cells) in every chapter, in order, one process per chapter.

This is what makes the promise "every code listing in the book runs" checkable in CI
without rendering the whole book.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CELL = re.compile(r"^```\{python[^}]*\}\s*\n(.*?)^```", re.S | re.M)


def cells(qmd: Path) -> list[str]:
    out = []
    for m in CELL.finditer(qmd.read_text()):
        body = "\n".join(l for l in m.group(1).splitlines() if not l.startswith("#|"))
        out.append(body)
    return out


def main(names):
    files = (sorted((ROOT / "chapters").glob("ch*.qmd")) + sorted((ROOT / "front").glob("*.qmd"))
             + sorted((ROOT / "back").glob("*.qmd")))
    if names:
        files = [f for f in files if f.stem in names]
    bad = 0
    for f in files:
        cs = cells(f)
        if not cs:
            continue
        src = "import matplotlib\nmatplotlib.use('Agg')\n" + "\n\n".join(cs)
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
            fh.write(src)
        r = subprocess.run([sys.executable, fh.name], cwd=ROOT, capture_output=True, text=True,
                           env={"PYTHONPATH": str(ROOT), "PATH": "/usr/bin:/bin:/usr/local/bin", "HOME": str(Path.home())})
        if r.returncode:
            bad += 1
            print(f"FAIL {f.name}\n{r.stderr[-1500:]}")
        else:
            print(f"ok   {f.name} ({len(cs)} listings)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])

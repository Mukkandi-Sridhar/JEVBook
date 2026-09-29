"""Build every figure for one or more chapters: python tools/build_figures.py ch01 ch21 (or 'all')."""

import importlib.util
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from jevkit import figs  # noqa: E402
from jevkit.figs.bookmap import CHAPTERS  # noqa: E402


def build(ch: str, only: set[str] | None = None) -> int:
    src = ROOT / "figures" / "src" / f"{ch}.py"
    if not src.exists():
        print(f"[skip] {ch}: no figure source")
        return 0
    spec = importlib.util.spec_from_file_location(f"figsrc_{ch}", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    n = 0
    figs.save(figs.you_are_here(ch), ch, "map")
    figs.qr(ch)
    for name, fn in figs.registered(ch):
        if only and name not in only:
            continue
        t = time.time()
        f = fn()
        figs.save(f, ch, name)
        n += 1
        print(f"  {ch}/{name}  ({time.time() - t:.1f}s)")
    return n


if __name__ == "__main__":
    args = sys.argv[1:] or ["all"]
    only = None
    if "--only" in args:
        i = args.index("--only")
        only = set(args[i + 1:])
        args = args[:i]
    chs = sorted(CHAPTERS) if args == ["all"] else args
    total = sum(build(c, only) for c in chs)
    print(f"built {total} figures")

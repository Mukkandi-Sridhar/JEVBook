"""Build the figures of one or more chapters: python3 tools/build_figures.py c01 c02 (or 'all').

Each figures/src/cNN.py defines functions whose names start with fig_; each returns a Matplotlib figure, saved as
figures/cNN/<name>.pdf."""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import figstyle  # noqa: E402


def build(ch):
    src = ROOT / "figures" / "src" / f"{ch}.py"
    spec = importlib.util.spec_from_file_location(f"fig_{ch}", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for name in dir(mod):
        if name.startswith("fig_"):
            figstyle.save(getattr(mod, name)(), ch, name[4:].replace("_", "-"))
            print(f"  {ch}/{name[4:].replace('_', '-')}")


if __name__ == "__main__":
    args = sys.argv[1:]
    chs = sorted(p.stem for p in (ROOT / "figures" / "src").glob("c*.py")) if args == ["all"] else args
    for ch in chs:
        build(ch)

"""Run every Python block in the book's chapters, in order, module by module (python3 tools/check_code.py [m05 ...]).

Blocks run in one namespace per module, like cells of a notebook, with code/ on the path and as the working
directory, and with TARKIKA_FAKE=1 so the scripted stand-in model answers. Directives are HTML comments placed
just before a block (they do not appear in the printed book):

  <!-- check: skip -->            do not run (needs a live service, e.g. embeddings or a hosted reranker)
  <!-- check: replies [ ... ] --> queue replies for the stand-in model (a Python list literal)
  <!-- check: expect -->          the block's printed output must equal the ```text block that follows it
"""
import ast, contextlib, io, os, re, sys, traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
os.environ["TARKIKA_FAKE"] = "1"
sys.path.insert(0, str(CODE))
os.chdir(CODE)
BLOCK = re.compile(r"((?:<!-- check:[^>]*-->\s*)*)```(\w+)\n(.*?)```", re.S)


def run(chapter: Path) -> int:
    import fake_model
    txt = chapter.read_text()
    blocks = list(BLOCK.finditer(txt))
    ns, fails, n = {"__name__": f"book_{chapter.stem}"}, 0, 0
    for i, m in enumerate(blocks):
        directives, lang, code = m.group(1), m.group(2), m.group(3)
        if lang != "python" or "check: skip" in directives:
            continue
        n += 1
        rep = re.search(r"check: replies (\[.*?\])\s*-->", directives, re.S)
        fake_model.REPLIES[:] = ast.literal_eval(rep.group(1)) if rep else []
        out = io.StringIO()
        line = txt[:m.start(2)].count("\n") + 1
        try:
            with contextlib.redirect_stdout(out):
                exec(compile(code, f"{chapter.name}:{line}", "exec"), ns)
        except Exception:
            fails += 1
            print(f"FAIL {chapter.name} line {line}\n{traceback.format_exc(limit=3)}")
            continue
        if "check: expect" in directives:
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            want = nxt.group(3).strip() if nxt and nxt.group(2) == "text" else None
            if out.getvalue().strip() != want:
                fails += 1
                print(f"OUTPUT MISMATCH {chapter.name} line {line}\n--- printed:\n{out.getvalue()}--- book:\n{want}")
    for name, fn in list(ns.items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
            except Exception:
                fails += 1
                print(f"TEST FAILED {chapter.name}: {name}\n{traceback.format_exc(limit=2)}")
    print(f"{chapter.stem}: {n} blocks run, {fails} problems")
    return fails


if __name__ == "__main__":
    names = sys.argv[1:] or sorted(p.stem for p in (ROOT / "chapters").glob("m*.qmd"))
    sys.exit(1 if sum(run(ROOT / "chapters" / f"{n}.qmd") for n in names) else 0)

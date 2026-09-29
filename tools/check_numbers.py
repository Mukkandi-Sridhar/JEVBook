"""Check that every {{< num chNN key fmt >}} shortcode in the book resolves to a value in results/chNN.json."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = re.compile(r"\{\{<\s*num\s+(\S+)\s+(\S+)")


def lookup(d, key):
    for part in key.split("."):
        if isinstance(d, list) and part.isdigit():
            d = d[int(part)]
        elif isinstance(d, dict) and part in d:
            d = d[part]
        else:
            return None
    return d


bad = 0
for q in sorted(ROOT.glob("**/*.qmd")):
    if "_book" in q.parts or ".quarto" in q.parts:
        continue
    for ch, key in SHORT.findall(q.read_text()):
        f = ROOT / "results" / f"{ch}.json"
        if not f.exists() or lookup(json.loads(f.read_text()), key) is None:
            bad += 1
            print(f"MISSING {q.relative_to(ROOT)}: {ch} {key}")
print(f"{bad} missing")
sys.exit(1 if bad else 0)

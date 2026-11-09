"""Tokens in each part of Tarkika's skills (Module 13): the menu entry (name and description), the whole SKILL.md,
and the reference files. Needs Node with gpt-tokenizer (npm install gpt-tokenizer; set NODE_PATH to its folder)."""
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parts = []
for skill in sorted((ROOT / "code" / "skills").iterdir()):
    text = (skill / "SKILL.md").read_text()
    parts.append((skill.name, "menu", text.split("---")[1].strip()))
    parts.append((skill.name, "skill", text))
    for ref in sorted((skill / "reference").glob("*.md")) if (skill / "reference").exists() else []:
        parts.append((skill.name, "reference", ref.read_text()))
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
    json.dump([p[2] for p in parts], f)
out = subprocess.run(["node", str(ROOT / "tools" / "count_tokens.cjs"), f.name], capture_output=True, text=True,
                     check=True).stdout
counts = [int(line.split()[1]) for line in out.splitlines() if line.startswith("o200k")]
res = [{"skill": s, "part": k, "tokens": n} for (s, k, _), n in zip(parts, counts)]
(ROOT / "research" / "m13-skills.json").write_text(json.dumps(res, indent=1))
for r in res:
    print(r)

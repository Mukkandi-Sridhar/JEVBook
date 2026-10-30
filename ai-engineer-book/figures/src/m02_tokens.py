"""Token 'playground' figures, typeset with LuaLaTeX so Indian scripts are shaped correctly.

Data: research/m02-tokens.json (measured with tools/count_tokens.cjs). Run: python3 figures/src/m02_tokens.py
"""
import json, subprocess, tempfile, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "research" / "m02-tokens.json").read_text())
OUT = ROOT / "figures" / "m02"
FILLS = ["chipA", "chipB", "chipC", "chipD"]

PRE = r"""\documentclass[border=2pt]{standalone}
\usepackage{fontspec,tikz,xcolor}
\directlua{luaotfload.add_fallback("indic",{"NotoSansDevanagari:mode=harf;script=dev2;","NotoSansKannada:mode=harf;script=knd2;","NotoSansTelugu:mode=harf;script=tel2;"})}
\setmainfont{Noto Sans}[RawFeature={fallback=indic;mode=harf}]
\definecolor{chipA}{HTML}{DCE0F3}\definecolor{chipB}{HTML}{F8E3C6}\definecolor{chipC}{HTML}{E2E4E9}\definecolor{chipD}{HTML}{EDD5E6}
\definecolor{ink}{HTML}{14161A}\definecolor{soft}{HTML}{4A5160}\definecolor{saffron}{HTML}{D97706}
\begin{document}\fontsize{8}{10}\selectfont
"""


def esc(s):
    return s.replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")


def chip(t, i):
    shown = esc(t.replace(" ", "·", 1) if t.startswith(" ") else t)
    return (r"\tikz[baseline=(c.base)]\node[fill=" + FILLS[i % 4] + r",rounded corners=1.5pt,inner xsep=2.2pt,"
            r"inner ysep=2.5pt,text height=1.6ex,text depth=.45ex](c){" + shown + "};")


def tokens_fig():
    rows = []
    for lang, d in DATA["sentences"].items():
        chips = r"\hspace{1.2pt}".join(chip(t, i) for i, t in enumerate(d["o200k"]))
        rows.append(r"\parbox[c]{14mm}{\textcolor{soft}{" + lang + r"}}\parbox[c]{103mm}{\raggedright " + chips +
                    r"}\parbox[c]{12mm}{\raggedleft\textbf{" + str(len(d["o200k"])) + r"}\,\textcolor{soft}{tok.}}")
    body = r"\begin{minipage}{131mm}" + r"\\[5pt]".join(rows) + r"\end{minipage}"
    return body


def words_fig():
    rows = []
    for w, pieces in DATA["words"].items():
        chips = r"\hspace{1.2pt}".join(chip(t, i) for i, t in enumerate(pieces))
        rows.append(r"\parbox[c]{20mm}{\textcolor{soft}{" + w + r"}}" + chips)
    return r"\begin{minipage}{60mm}" + r"\\[4pt]".join(rows) + r"\end{minipage}"


def build(name, body):
    with tempfile.TemporaryDirectory() as tmp:
        tex = Path(tmp) / f"{name}.tex"
        tex.write_text(PRE + body + "\n\\end{document}\n", encoding="utf-8")
        subprocess.run(["lualatex", "-interaction=nonstopmode", tex.name], cwd=tmp, check=True,
                       stdout=subprocess.DEVNULL)
        OUT.mkdir(parents=True, exist_ok=True)
        shutil.copy(Path(tmp) / f"{name}.pdf", OUT / f"{name}.pdf")
        print(" ", f"m02/{name}")


if __name__ == "__main__":
    build("tokens-playground", tokens_fig())
    build("tokens-words", words_fig())

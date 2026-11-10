"""The complete colour book as one PDF: front cover (design 4, paper), the interior, and the back cover.

Run after `quarto render --to pdf`:  python3 cover/final_book.py
Writes cover/final/front.pdf, cover/final/back.pdf and drafts/Ship-Real-AI-complete-colour.pdf.
"""
import json
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cover"))
import covers3 as c3  # noqa: E402

OUT = ROOT / "cover" / "final"
OUT.mkdir(exist_ok=True)
TW, TH = 176, 250            # trim in mm

# Front: design 4, cropped from the bleed canvas (3 mm bleed at top, bottom and right) to the trim.
front = c3.neural_ship(c3.PAPER).replace(
    f'width="{c3.W}mm" height="{c3.H}mm" viewBox="0 0 {c3.W} {c3.H}"',
    f'width="{TW}mm" height="{TH}mm" viewBox="0 3 {TW} {TH}"')
(OUT / "front.html").write_text(front)

INK, SOFT, SAFF, INDIGO = "#10163A", "#454C6E", "#E8780A", "#2A3789"
POINTS = [
    "Build one real system, a support assistant for an Indian marketplace, from its first API call to a service in production.",
    "Learn how LLMs read, write and cost, in tokens and in rupees, including what Hindi and Hinglish do to the bill.",
    "Master context, memory, tools, structured output, search, RAG and the evals that prove each change helped.",
    "Design agents that act safely: guardrails, private data, prompt injection, approvals people actually read.",
    "Connect everything with MCP, skills and agent protocols, and run long jobs that survive crashes.",
    "Ship it: caching, concurrency, cost per correct answer, traces, safe releases, fine-tuning and open models.",
    "Finish with system design and interview questions worked as reasoning chains.",
]
lis = "".join(f"<li>{p}</li>" for p in POINTS)
fonts = "".join(
    f"@font-face{{font-family:'{fam}';src:url('file://{ROOT / 'assets' / 'fonts' / f}');font-weight:{wt};font-style:{st};}}"
    for fam, f, wt, st in [("Work Sans", "WorkSans-Regular.ttf", 400, "normal"), ("Work Sans", "WorkSans-Bold.ttf", 700, "normal"),
                           ("Plex Serif", "IBMPlexSerif-Regular.ttf", 400, "normal"),
                           ("Plex Serif", "IBMPlexSerif-Italic.ttf", 400, "italic"),
                           ("Plex Serif", "IBMPlexSerif-Bold.ttf", 700, "normal")])
back = f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
@page {{ size: {TW}mm {TH}mm; margin: 0 }}
html,body{{margin:0;padding:0}}
.page{{width:{TW}mm;height:{TH}mm;box-sizing:border-box;padding:16mm 16mm 14mm;position:relative;
  background:linear-gradient(#FBF8F0,#F1EADA);font-family:'Work Sans';color:{INK}}}
h1{{font-family:'Plex Serif';font-weight:700;font-size:17pt;line-height:1.22;margin:0 0 5mm}}
h1 span{{color:{SAFF}}}
p{{font-family:'Plex Serif';font-size:9.6pt;line-height:1.5;margin:0 0 4mm;color:{SOFT}}}
ul{{margin:2mm 0 5mm;padding:0;list-style:none}}
li{{font-size:8.9pt;line-height:1.42;margin:0 0 2.4mm;padding-left:6mm;position:relative}}
li:before{{content:'';position:absolute;left:0;top:1.6mm;width:2.4mm;height:2.4mm;border-radius:50%;background:{SAFF}}}
.rule{{height:0.4mm;background:{INDIGO};opacity:.25;margin:5mm 0}}
.author{{display:flex;gap:5mm;align-items:flex-start}}
.author b{{font-size:9pt;letter-spacing:.12em}}
.author p{{font-size:8.6pt;margin-top:1.5mm}}
.foot{{position:absolute;left:16mm;right:16mm;bottom:14mm;display:flex;justify-content:space-between;align-items:flex-end}}
.cat{{font-size:7.5pt;letter-spacing:.14em;color:{SOFT}}}
.isbn{{width:46mm;height:26mm;background:#fff;border:0.3mm solid #D9D2C2;display:flex;align-items:center;
  justify-content:center;font-size:6.5pt;color:#9A9384}}
</style></head><body><div class="page">
<h1>Anyone can build the demo.<br><span>This book is about what comes after.</span></h1>
<p>A weekend chatbot answers "Can I return opened earbuds?" with a confident yes. The bill arrives at five times the
estimate. Nobody can say whether last week's prompt change helped. <i>Ship Real AI</i> is the complete path from first
principles to production, built around one system you grow module by module, with every number measured and every line
of code run before it was printed.</p>
<ul>{lis}</ul>
<div class="rule"></div>
<div class="author"><div><b>SRIDHAR MUKKANDI</b>
<p>is an applied AI engineer who builds AI agents and the decision systems behind them. He writes for engineers who want
AI systems they can trust in production.</p></div></div>
<div class="foot"><div class="cat">AI ENGINEERING · LLMs · RAG · AGENTS · EVALS</div><div class="isbn">ISBN barcode</div></div>
</div></body></html>"""
(OUT / "back.html").write_text(back)

jobs = [{"src": str(OUT / "front.html"), "out": str(OUT / "front.pdf"), "type": "pdf", "width": f"{TW}mm", "height": f"{TH}mm"},
        {"src": str(OUT / "back.html"), "out": str(OUT / "back.pdf"), "type": "pdf", "width": f"{TW}mm", "height": f"{TH}mm"}]
(OUT / "jobs.json").write_text(json.dumps(jobs))
subprocess.run(["node", str(ROOT / "cover" / "render.mjs"), str(OUT / "jobs.json")], check=True, stdout=subprocess.DEVNULL)
(OUT / "jobs.json").unlink()

w = PdfWriter()
for part in [OUT / "front.pdf", ROOT / "_book" / "Ship-Real-AI.pdf", OUT / "back.pdf"]:
    for pg in PdfReader(part).pages:
        w.add_page(pg)
w.add_metadata({"/Title": "Ship Real AI", "/Author": "Sridhar Mukkandi",
                "/Subject": "The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals"})
dest = ROOT / "drafts" / "Ship-Real-AI-complete-colour.pdf"
with open(dest, "wb") as f:
    w.write(f)
print(dest, len(w.pages), "pages")

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

# The ISBN. Leave it as None until RRRNA allots it; then write it here, e.g. "978-93-xxxxx-xx-x", and rerun.
# With None the back cover shows a clean, labelled box of the right size; with a number it prints the EAN-13 barcode.
ISBN = None

L = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
G = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
R = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
PARITY = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]


def check_digit(d12):
    return (10 - sum(int(c) * (3 if i % 2 else 1) for i, c in enumerate(d12)) % 10) % 10


def ean13_svg(isbn):
    """A scannable EAN-13 barcode at 100% size (0.33 mm modules), with the ISBN above and digits below, as SVG in mm."""
    d = isbn.replace("-", "")
    assert len(d) == 13 and check_digit(d[:12]) == int(d[12]), "bad ISBN check digit"
    bits = "101" + "".join((L if p == "L" else G)[int(c)] for p, c in zip(PARITY[int(d[0])], d[1:7])) + "01010" \
        + "".join(R[int(c)] for c in d[7:]) + "101"
    m, x0, top, h = 0.33, 7.0, 6.0, 18.0
    guard = {0, 1, 2, 45, 46, 47, 48, 49, 92, 93, 94}
    bars = "".join(f'<rect x="{x0 + i * m:.3f}" y="{top}" width="{m:.3f}" height="{h + (1.6 if i in guard else 0)}"/>'
                   for i, b in enumerate(bits) if b == "1")
    nums = (f'<text x="{x0 - 2.2}" y="{top + h + 3.4}" font-size="3.2">{d[0]}</text>'
            f'<text x="{x0 + 3 * m + 21 * m}" y="{top + h + 3.4}" font-size="3.2" text-anchor="middle" letter-spacing="0.55">{d[1:7]}</text>'
            f'<text x="{x0 + 50 * m + 21 * m}" y="{top + h + 3.4}" font-size="3.2" text-anchor="middle" letter-spacing="0.55">{d[7:]}</text>')
    return (f'<svg viewBox="0 0 46 30" width="46mm" height="30mm" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Work Sans" fill="#000"><rect width="46" height="30" fill="#fff"/>'
            f'<text x="23" y="4.4" font-size="3.0" text-anchor="middle" letter-spacing="0.25">ISBN {isbn}</text>'
            f'{bars}{nums}</svg>')


def isbn_box():
    if ISBN:
        return f'<div class="isbn">{ean13_svg(ISBN)}</div>'
    return ('<div class="isbn empty"><div class="lbl">ISBN</div><div class="ph">978-93-XXXXX-XX-X</div>'
            '<div class="bars"></div><div class="note">barcode area · 46 × 30 mm</div></div>')


# Back-cover copy. BACK picks the version: "A" (problem first) or "B" (outcome first).
BACK = "C"
COPY = {
 "A": dict(
  kick="THE AI ENGINEER BOOTCAMP",
  h1="Your AI demo works.<br><span>Production is a different job.</span>",
  lead="The chatbot invents a refund policy. The bill comes in at five times the estimate. A prompt change ships "
       "and nobody can say if it helped. <i>Ship Real AI</i> teaches the engineering that fixes this, by building one "
       "real system, step by step, from the first model call to a service running in production.",
  head="YOU WILL LEARN TO",
  points=["Control what the model sees: prompts, context, memory and caching",
          "Build retrieval that finds the right answer: hybrid search, reranking, RAG",
          "Prove every change with evals, golden sets and LLM judges",
          "Design agents that act safely, with guardrails and human approval",
          "Connect tools with MCP, and run long jobs that survive failure",
          "Cut cost and latency, release safely, and know when to fine-tune",
          "Answer AI system-design questions in interviews"]),
 "B": dict(
  kick="FROM FIRST PRINCIPLES TO PRODUCTION",
  h1="Stop building demos.<br><span>Start shipping AI systems.</span>",
  lead="Most AI tutorials end where the real work begins. This book starts there. Across 17 modules you build one "
       "complete AI assistant and learn the engineering every production system needs: retrieval that is right, "
       "agents that are safe, costs you can predict, and quality you can measure.",
  head="INSIDE",
  points=["How LLMs work, explained for engineers",
          "Prompts, context engineering and memory",
          "Tools, structured output, search and RAG",
          "Evals, LLM-as-judge and calibrated decisions",
          "Agents, guardrails, MCP and agent protocols",
          "Caching, scale, cost, tracing and safe releases",
          "System design and interview preparation"]),
}
C = COPY.get(BACK, COPY["A"])
lis = "".join(f"<li>{t}</li>" for t in C["points"])
fonts = "".join(
    f"@font-face{{font-family:'{fam}';src:url('file://{ROOT / 'assets' / 'fonts' / f}');font-weight:{wt};font-style:{st};}}"
    for fam, f, wt, st in [("Work Sans", "WorkSans-Regular.ttf", 400, "normal"), ("Work Sans", "WorkSans-Bold.ttf", 700, "normal"),
                           ("Plex Serif", "IBMPlexSerif-Regular.ttf", 400, "normal"),
                           ("Plex Serif", "IBMPlexSerif-Italic.ttf", 400, "italic"),
                           ("Plex Serif", "IBMPlexSerif-Bold.ttf", 700, "normal"),
                           ("Plex Mono", "IBMPlexMono-Regular.ttf", 400, "normal")])
words = ("tokens · attention · embeddings · KV cache · structured output · tool calls · hybrid search · reranker · RAG · "
         "golden set · LLM-as-judge · guardrails · MCP · skills · durable execution · semantic cache · LoRA · traces · ")
back = f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
@page {{ size: {TW}mm {TH}mm; margin: 0 }}
html,body{{margin:0;padding:0}}
.page{{width:{TW}mm;height:{TH}mm;box-sizing:border-box;padding:15mm 15mm 0;position:relative;overflow:hidden;
  background:radial-gradient(120mm 90mm at 100% 0%,#FBE2BD 0%,rgba(251,226,189,0) 70%),linear-gradient(#FBF8F0,#EFE7D5);
  font-family:'Work Sans';color:{INK}}}
.kick{{font-size:7.4pt;letter-spacing:.22em;color:{SAFF};font-weight:700;margin-bottom:3mm}}
h1{{font-family:'Plex Serif';font-weight:700;font-size:22pt;line-height:1.16;margin:0 0 6mm}}
h1 span{{color:{SAFF}}}
p.lead{{font-family:'Plex Serif';font-size:10.6pt;line-height:1.55;margin:0 0 7mm;color:{SOFT}}}
ul{{margin:0 0 5mm;padding:0;list-style:none}}
li{{font-size:10pt;line-height:1.38;margin:0 0 3mm;padding-left:6.5mm;position:relative;color:#2B3157}}
.head{{font-size:7.2pt;letter-spacing:.2em;font-weight:700;color:{INDIGO};margin:0 0 3.4mm}}
li:before{{content:'';position:absolute;left:0;top:1.4mm;width:2.3mm;height:2.3mm;border-radius:50%;
  background:{SAFF};box-shadow:0 0 0 1.1mm rgba(232,120,10,.16)}}
.facts{{display:flex;gap:4mm;margin:6mm 0 7mm}}
.fact{{flex:1;border:0.3mm solid rgba(42,55,137,.18);border-radius:2mm;padding:2.4mm 3mm;background:rgba(255,255,255,.45)}}
.fact b{{display:block;font-size:13pt;color:{INDIGO}}}
.fact span{{font-size:6.8pt;letter-spacing:.06em;color:{SOFT}}}
.author{{border-top:0.35mm solid rgba(42,55,137,.2);padding-top:4mm;font-family:'Plex Serif';font-size:8.6pt;
  line-height:1.5;color:{SOFT}}}
.author b{{font-family:'Work Sans';letter-spacing:.14em;color:{INK};font-size:8.4pt;margin-right:1.5mm}}
.sea{{position:absolute;left:-10mm;right:-10mm;bottom:2.5mm;font-family:'Plex Mono';font-size:6.4pt;color:{INDIGO};
  opacity:.16;line-height:1.9;white-space:nowrap}}
.foot{{position:absolute;left:15mm;right:15mm;bottom:14mm;display:flex;justify-content:space-between;align-items:flex-end}}
.cat{{font-size:6.8pt;letter-spacing:.16em;color:{SOFT};line-height:1.7}}
.cat b{{color:{INK}}}
.isbn{{width:46mm;height:30mm;background:#fff;border-radius:1mm;box-shadow:0 0.6mm 2mm rgba(16,22,58,.12)}}
.isbn.empty{{box-sizing:border-box;border:0.35mm dashed #B9B2A2;padding:2.6mm 3mm;font-family:'Work Sans';color:#8C8576}}
.isbn .lbl{{font-size:6.4pt;letter-spacing:.2em;font-weight:700}}
.isbn .ph{{font-size:8pt;margin:1mm 0 1.6mm;letter-spacing:.06em}}
.isbn .bars{{height:12mm;background:repeating-linear-gradient(90deg,#E4DFD3 0 .5mm,transparent .5mm 1.3mm)}}
.isbn .note{{font-size:5.4pt;margin-top:1.2mm;letter-spacing:.06em}}
</style></head><body><div class="page">
<div class="kick">{C["kick"]}</div>
<h1>{C["h1"]}</h1>
<p class="lead">{C["lead"]}</p>
<div class="head">{C["head"]}</div>
<ul>{lis}</ul>
<div class="facts"><div class="fact"><b>17</b><span>MODULES</span></div><div class="fact"><b>80+</b><span>FIGURES</span></div>
<div class="fact"><b>193</b><span>COLOUR PAGES</span></div><div class="fact"><b>₹</b><span>COSTS IN RUPEES</span></div></div>
<div class="author"><b>SRIDHAR MUKKANDI</b> is an applied AI engineer who builds AI agents and the decision systems
behind them. He writes for engineers who want AI systems they can trust in production.</div>
<div class="sea">{words * 3}<br>&nbsp;&nbsp;&nbsp;&nbsp;{words * 3}</div>
<div class="foot"><div class="cat"><b>AI ENGINEERING</b><br>LLMs · RAG · AGENTS · MCP · EVALS</div>{isbn_box()}</div>
</div></body></html>"""

# ---------------------------------------------------------------- back cover C: two answers and a route map
STOPS = ["The job", "How LLMs|work", "Prompts &amp;|context", "Memory", "Tools", "Search",
         "RAG", "Advanced|RAG", "Evals", "Decisions", "Agent|loop", "Guardrails",
         "MCP &amp;|skills", "Long|tasks", "Scale &amp;|cost", "Production", "System|design"]
PART_OF = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4]
PART_COL = ["#3B4BA8", "#E8780A", "#8E3B7A", "#1F7A63", "#10163A"]
PART_NAME = ["The model", "Memory, tools, knowledge", "Measuring", "Agents", "Production"]


def route_svg():
    w, rows, x0, x1 = 146.0, [(0, 6), (6, 12), (12, 17)], 12.0, 134.0
    ys = [10.0, 38.0, 66.0]
    pts = []
    for r, (a, b) in enumerate(rows):
        n = b - a
        xs = [x0 + (x1 - x0) * i / 5 for i in range(n)]
        if r == 1:
            xs = xs[::-1]
        pts += [(x, ys[r]) for x in xs]
    out = []
    for i in range(16):                                   # the line, coloured by part, with rounded turns
        (xa, ya), (xb, yb) = pts[i], pts[i + 1]
        col = PART_COL[PART_OF[i + 1]]
        if ya == yb:
            out.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="{col}" stroke-width="2.2" stroke-linecap="round"/>')
        else:
            side = 1 if xa > 70 else -1
            cx = xa + side * 9
            out.append(f'<path d="M{xa},{ya} C{cx},{ya} {cx},{yb} {xb},{yb}" fill="none" stroke="{col}" '
                       f'stroke-width="2.2" stroke-linecap="round"/>')
    for i, (x, y) in enumerate(pts):
        col = PART_COL[PART_OF[i]]
        big = i in (0, 16)
        out.append(f'<circle cx="{x}" cy="{y}" r="{2.6 if big else 1.9}" fill="#FFFFFF" stroke="{col}" stroke-width="{1.1 if big else 0.9}"/>')
        out.append(f'<text x="{x}" y="{y + 1.15}" text-anchor="middle" font-size="2.3" font-weight="700" fill="{col}">{i + 1}</text>')
        for k, line in enumerate(STOPS[i].split("|")):
            anc, lx = ("end", x + 1.5) if i == 5 else ("start", x - 1.5) if i == 11 else ("middle", x)
            out.append(f'<text x="{lx}" y="{y + 7.0 + k * 3.7}" text-anchor="{anc}" font-size="3.2" fill="#2B3157">{line}</text>')
    out.append(f'<text x="{pts[0][0] - 4}" y="{pts[0][1] - 4.6}" font-size="2.9" letter-spacing="0.35" fill="#8C8576">FIRST API CALL</text>')
    out.append(f'<text x="{pts[16][0] + 4}" y="{pts[16][1] - 4.6}" text-anchor="end" font-size="2.9" letter-spacing="0.35" '
               f'fill="#E8780A" font-weight="700">IN PRODUCTION</text>')
    lx, leg = 4.0, ""
    for c, n in zip(PART_COL, PART_NAME):
        leg += f'<circle cx="{lx}" cy="88" r="1.3" fill="{c}"/><text x="{lx + 2.4}" y="89.1" font-size="2.9" fill="#454C6E">{n}</text>'
        lx += 2.4 + len(n) * 1.55 + 6
    return (f'<svg viewBox="0 0 {w} 92" width="{w}mm" height="92mm" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Work Sans">{"".join(out)}{leg}</svg>')


if BACK == "C":
    back = f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
@page {{ size: {TW}mm {TH}mm; margin: 0 }}
html,body{{margin:0;padding:0}}
.page{{width:{TW}mm;height:{TH}mm;box-sizing:border-box;padding:14mm 15mm 0;position:relative;overflow:hidden;
  background:radial-gradient(120mm 90mm at 100% 0%,#FBE2BD 0%,rgba(251,226,189,0) 70%),linear-gradient(#FBF8F0,#EFE7D5);
  font-family:'Work Sans';color:{INK}}}
.kick{{font-size:7.2pt;letter-spacing:.22em;color:{SAFF};font-weight:700;margin-bottom:2.5mm}}
h1{{font-family:'Plex Serif';font-weight:700;font-size:21pt;line-height:1.12;margin:0 0 5mm}}
.q{{font-family:'Plex Mono';font-size:8.2pt;color:{SOFT};margin:0 0 2.4mm}}
.q b{{color:{INK}}}
.ans{{display:flex;gap:4mm;margin-bottom:4mm}}
.card{{flex:1;border-radius:2.4mm;padding:3mm 3.4mm;box-sizing:border-box}}
.demo{{background:#FFFFFF;border:0.35mm solid #E7D9D6}}
.prod{{background:{INK};color:#fff}}
.tag{{font-size:6.4pt;letter-spacing:.2em;font-weight:700;margin-bottom:1.6mm}}
.demo .tag{{color:#B42318}} .prod .tag{{color:#FFB84D}}
.say{{font-family:'Plex Serif';font-size:9.6pt;line-height:1.35;margin-bottom:2mm}}
.demo .say{{color:#5A1A14}}
.meta{{font-family:'Plex Mono';font-size:6.4pt;line-height:1.5}}
.demo .meta{{color:#B42318}} .prod .meta{{color:#9FE3BE}}
.diff{{font-family:'Plex Serif';font-size:10.2pt;line-height:1.45;color:{SOFT};margin:0 0 1mm}}
.diff b{{color:{INK}}}
.route{{margin:0 -1mm}}
.foot{{position:absolute;left:15mm;right:15mm;bottom:12mm;display:flex;justify-content:space-between;align-items:flex-end}}
.who{{font-family:'Plex Serif';font-size:8.4pt;line-height:1.45;color:{SOFT};max-width:88mm}}
.who b{{font-family:'Work Sans';letter-spacing:.14em;color:{INK};font-size:8.2pt;display:block;margin-bottom:1mm}}
.isbn{{width:46mm;height:30mm;background:#fff;border-radius:1mm;box-shadow:0 0.6mm 2mm rgba(16,22,58,.12)}}
.isbn.empty{{box-sizing:border-box;border:0.35mm dashed #B9B2A2;padding:2.6mm 3mm;font-family:'Work Sans';color:#8C8576}}
.isbn .lbl{{font-size:6.4pt;letter-spacing:.2em;font-weight:700}}
.isbn .ph{{font-size:8pt;margin:1mm 0 1.6mm;letter-spacing:.06em}}
.isbn .bars{{height:12mm;background:repeating-linear-gradient(90deg,#E4DFD3 0 .5mm,transparent .5mm 1.3mm)}}
.isbn .note{{font-size:5.4pt;margin-top:1.2mm;letter-spacing:.06em}}
</style></head><body><div class="page">
<div class="kick">SAME QUESTION · TWO SYSTEMS</div>
<h1>Anyone can build the demo.<br><span style="color:{SAFF}">This book is about what comes after.</span></h1>
<div class="q">customer › <b>Can I return opened earbuds?</b></div>
<div class="ans">
 <div class="card demo"><div class="tag">THE DEMO</div>
  <div class="say">"Yes! Returns are accepted within 10 days."</div>
  <div class="meta">✗ wrong: opened in-ear audio is non-returnable<br>✗ no source · cost unknown · never tested</div></div>
 <div class="card prod"><div class="tag">THE REAL SYSTEM</div>
  <div class="say">"Only if they are faulty. Opened in-ear audio can't be returned otherwise."</div>
  <div class="meta">✓ sources: policy §3, §4 · 1.2 s · ₹1.17<br>✓ golden set 92% · guardrails passed</div></div>
</div>
<p class="diff">The difference is engineering. <b>Ship Real AI</b> builds it with you, one system and seventeen modules,
from the first API call to production.</p>
<div class="route">{route_svg()}</div>
<div class="foot"><div class="who"><b>SRIDHAR MUKKANDI</b>Applied AI engineer. Builds AI agents and the decision
systems behind them, and writes for engineers who want AI they can trust in production.</div>{isbn_box()}</div>
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

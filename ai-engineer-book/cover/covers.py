"""Five front-cover concepts for Ship Real AI, rendered at print size with Chromium.

Each concept is an HTML page holding one inline SVG drawn at the B5 trim (176 x 250 mm) plus 3 mm bleed on the
three outer edges, in the book's own fonts. Run:  python3 cover/covers.py
Outputs go to cover/concepts/: full size PNG (300 dpi), a 160 px thumbnail and a greyscale copy of each, and a
comparison sheet.
"""
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "cover" / "concepts"
FONTS = ROOT / "assets" / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = ("SHIP", "REAL AI")
SUB = "The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals, from First Principles to Production and Interviews"
AUTHOR = "SRIDHAR MUKKANDI"
STRAP = "17 modules  ·  80+ figures  ·  every line of code runs"

# Canvas in mm: trim 176 x 250 plus 3 mm bleed on top, bottom and the outer (right) edge.
W, H, B = 179, 256, 3

NAVY, NIGHT, INK = "#14203A", "#0B1222", "#14161A"
INDIGO, INDIGO_L, INDIGO_T = "#3B4BA8", "#7F8CF0", "#DCE0F3"
SAFFRON, SAFFRON_L, SAFFRON_T = "#E8860C", "#FFB54A", "#F8E3C6"
PAPER, WHITE, SOFT = "#F4F1EA", "#FFFFFF", "#AEB6C8"


def page(svg_body, bg):
    fonts = "".join(
        f"@font-face{{font-family:'{fam}';src:url('file://{FONTS / f}');font-weight:{wt};}}"
        for fam, f, wt in [("Work Sans", "WorkSans-Regular.ttf", 400), ("Work Sans", "WorkSans-Bold.ttf", 700),
                           ("Plex Serif", "IBMPlexSerif-Bold.ttf", 700), ("Plex Serif", "IBMPlexSerif-Regular.ttf", 400),
                           ("Plex Mono", "IBMPlexMono-Regular.ttf", 400), ("Plex Mono", "IBMPlexMono-Bold.ttf", 700)])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
html,body{{margin:0;padding:0;background:{bg}}} svg{{display:block}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">{svg_body}</svg>
</body></html>"""


def wrap_lines(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    return lines + [cur]


def subtitle(x, y, colour, size=4.3, width=46, lead=6.0, weight=400):
    return "".join(f'<text x="{x}" y="{y + i * lead}" font-family="Work Sans" font-weight="{weight}" '
                   f'font-size="{size}" fill="{colour}">{t}</text>' for i, t in enumerate(wrap_lines(SUB, width)))


def chips(x, y, fg, bg, items=("LLMs", "RAG", "MCP", "AGENTS", "EVALS"), size=3.6):
    out, cx = [], x
    for t in items:
        w = len(t) * size * 0.68 + 5
        out.append(f'<rect x="{cx}" y="{y}" width="{w}" height="{size + 3.6}" rx="1.2" fill="{bg}"/>'
                   f'<text x="{cx + w / 2}" y="{y + size + 1.1}" text-anchor="middle" font-family="Work Sans" '
                   f'font-weight="700" font-size="{size}" letter-spacing="0.4" fill="{fg}">{t}</text>')
        cx += w + 2.2
    return "".join(out)


def title2(x, y1, y2, size, c1, c2, c3=None):
    """SHIP on one line, REAL AI on the next; c3 colours AI if given."""
    ai = f'<tspan fill="{c3}">AI</tspan>' if c3 else "AI"
    f = f'font-family="Work Sans" font-weight="700" font-size="{size}" letter-spacing="{-size * 0.035}"'
    return (f'<text x="{x}" y="{y1}" {f} fill="{c1}">SHIP</text>'
            f'<text x="{x}" y="{y2}" {f} fill="{c2}">REAL {ai}</text>')


def foot(colour, soft, y=238):
    return (f'<text x="14" y="{y}" font-family="Work Sans" font-size="3.4" fill="{soft}">{STRAP}</text>'
            f'<text x="14" y="{y + 9}" font-family="Work Sans" font-weight="700" font-size="5.2" '
            f'letter-spacing="1.3" fill="{colour}">{AUTHOR}</text>')


# ------------------------------------------------------------------ concept A: the harness
def harness():
    cx, cy = 88, 160
    parts = ["Prompts", "Memory", "Tools", "Search", "RAG", "Evals", "Decisions", "Agent loop",
             "Guardrails", "MCP", "Skills", "Long jobs", "Caching", "Cost", "Traces", "Releases"]
    s = [f'<rect width="{W}" height="{H}" fill="{NIGHT}"/>']
    for r, op in [(56, "#1B2746"), (44, "#1E2C52"), (30, "#22325F")]:
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{op}" stroke-width="0.5"/>')
    for i, p in enumerate(parts):
        a = 2 * math.pi * i / len(parts) - math.pi / 2
        r = 44 if i % 2 == 0 else 56
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        s.append(f'<line x1="{cx + 11 * math.cos(a)}" y1="{cy + 11 * math.sin(a)}" x2="{x}" y2="{y}" '
                 f'stroke="{INDIGO}" stroke-width="0.35"/>')
        w = len(p) * 2.15 + 6
        s.append(f'<rect x="{x - w / 2}" y="{y - 3.6}" width="{w}" height="7.2" rx="3.6" fill="{NAVY}" '
                 f'stroke="{INDIGO_L}" stroke-width="0.4"/>'
                 f'<text x="{x}" y="{y + 1.25}" text-anchor="middle" font-family="Work Sans" font-size="3.3" '
                 f'fill="{INDIGO_T}">{p}</text>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="{SAFFRON}" opacity="0.18"/>'
             f'<rect x="{cx - 11}" y="{cy - 6}" width="22" height="12" rx="2" fill="{SAFFRON}"/>'
             f'<text x="{cx}" y="{cy + 1.6}" text-anchor="middle" font-family="Work Sans" font-weight="700" '
             f'font-size="4.6" letter-spacing="0.6" fill="{NIGHT}">MODEL</text>')
    s.append(title2(14, 44, 80, 40, WHITE, WHITE, SAFFRON))
    s.append(subtitle(14, 92, SOFT, size=4.2, width=58, lead=5.4))
    s.append(f'<text x="14" y="229" font-family="Plex Serif" font-size="5.2" fill="{WHITE}">The model is one box.'
             f'</text><text x="14" y="236" font-family="Plex Serif" font-size="5.2" fill="{SAFFRON_L}">'
             f'This book is everything you build around it.</text>')
    s.append(foot(WHITE, SOFT, y=243 - 9 + 9 - 2))
    return page("".join(s), NIGHT)


# ------------------------------------------------------------------ concept B: the trace
def trace():
    rows = [("chain", "support_agent", "", 0), ("guard", "mask_aadhaar", "****2346", 1),
            ("llm", "route", "refund · p=0.94", 1), ("chain", "agent_loop", "", 1),
            ("tool", "check_order_status", "Delivered on 20 Oct.", 2), ("tool", "search_policy", "§4 faulty items", 2),
            ("llm", "draft_reply", "1,412 tokens in", 2), ("guard", "check_reply", "0 problems", 1),
            ("eval", "golden_set", "92% pass", 1), ("cost", "per_chat", "₹1.17", 1)]
    col = {"chain": SOFT, "guard": "#F2667A", "llm": SAFFRON_L, "tool": INDIGO_L, "eval": "#5FD39A", "cost": "#5FD39A"}
    s = [f'<rect width="{W}" height="{H}" fill="#0A0D14"/>']
    for i in range(0, 260, 6):
        s.append(f'<line x1="0" y1="{i}" x2="{W}" y2="{i}" stroke="#10151F" stroke-width="0.3"/>')
    y0 = 138
    for i, (k, n, v, d) in enumerate(rows):
        y = y0 + i * 8.0
        x = 16 + d * 9
        if d:
            s.append(f'<path d="M{x - 6} {y - 7} V{y - 1.4} H{x - 1.5}" fill="none" stroke="#2A3346" stroke-width="0.4"/>')
        s.append(f'<text x="{x}" y="{y}" font-family="Plex Mono" font-size="3.7" fill="{col[k]}">{k:<5}</text>'
                 f'<text x="{x + 14}" y="{y}" font-family="Plex Mono" font-weight="700" font-size="3.7" '
                 f'fill="{WHITE}">{n}</text>')
        if v:
            s.append(f'<text x="163" y="{y}" text-anchor="end" font-family="Plex Mono" font-size="3.5" '
                     f'fill="{col[k]}">{v}</text>')
    s.append(f'<rect x="14" y="16" width="3" height="70" fill="{SAFFRON}"/>')
    s.append(title2(22, 46, 82, 40, WHITE, WHITE, SAFFRON_L))
    s.append(subtitle(22, 96, SOFT, size=4.2, width=54, lead=5.4))
    s.append(f'<text x="16" y="124" font-family="Plex Mono" font-size="3.5" fill="#5FD39A">$ python3 run.py  '
             f'# one customer message, every step traced</text>')
    s.append(chips(16, 218, "#0A0D14", SAFFRON_L))
    s.append(foot(WHITE, SOFT))
    return page("".join(s), "#0A0D14")


# ------------------------------------------------------------------ concept C: the loop
def loop():
    cx, cy, r = 92, 168, 41
    s = [f'<rect width="{W}" height="{H}" fill="{SAFFRON}"/>']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{NAVY}" stroke-width="13"/>')
    for i, (lab, a) in enumerate([("DECIDE", -90), ("ACT", 30), ("CHECK", 150)]):
        t = math.radians(a)
        x, y = cx + r * math.cos(t), cy + r * math.sin(t)
        s.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{PAPER}" stroke="{NAVY}" stroke-width="2.2"/>'
                 f'<text x="{x}" y="{y + 1.6}" text-anchor="middle" font-family="Work Sans" font-weight="700" '
                 f'font-size="4.4" fill="{NAVY}">{lab}</text>')
        t2 = math.radians(a + 60)
        ax, ay = cx + r * math.cos(t2), cy + r * math.sin(t2)
        rot = a + 60 + 90
        s.append(f'<polygon points="-5,-6 6,0 -5,6" transform="translate({ax},{ay}) rotate({rot})" fill="{PAPER}"/>')
    s.append(f'<text x="{cx}" y="{cy - 2}" text-anchor="middle" font-family="Plex Serif" font-weight="700" '
             f'font-size="7" fill="{NAVY}">one agent,</text><text x="{cx}" y="{cy + 7}" text-anchor="middle" '
             f'font-family="Plex Serif" font-weight="700" font-size="7" fill="{NAVY}">every guardrail</text>')
    s.append(title2(14, 46, 84, 42, NAVY, NAVY, WHITE))
    s.append(subtitle(14, 97, NAVY, size=4.2, width=58, lead=5.4, weight=700))
    s.append(chips(14, 214, SAFFRON, NAVY))
    s.append(foot(NAVY, NAVY))
    return page("".join(s), SAFFRON)


# ------------------------------------------------------------------ concept D: the stack
def stack():
    layers = ["Production", "Agents & MCP", "Guardrails", "Evals", "RAG & search", "Tools & memory", "Prompts"]
    s = [f'<rect width="{W}" height="{H}" fill="{NAVY}"/>']
    cx, top, dx, dy, gap = 86, 144, 46, 13, 11.5
    shades = ["#2E3A8C", "#34429A", "#3B4BA8", "#4A5AB8", "#5B6AC6", "#6E7CD2", "#8390DD"]
    for i, lab in enumerate(layers):
        y = top + i * gap
        sh = shades[i]
        s.append(f'<polygon points="{cx},{y} {cx + dx},{y + dy / 2} {cx},{y + dy} {cx - dx},{y + dy / 2}" '
                 f'fill="{sh}" stroke="{NAVY}" stroke-width="0.6"/>'
                 f'<polygon points="{cx - dx},{y + dy / 2} {cx},{y + dy} {cx},{y + dy + 3} {cx - dx},{y + dy / 2 + 3}" fill="#1E275E"/>'
                 f'<polygon points="{cx + dx},{y + dy / 2} {cx},{y + dy} {cx},{y + dy + 3} {cx + dx},{y + dy / 2 + 3}" fill="#18204F"/>'
                 f'<text x="{cx + dx + 4}" y="{y + dy / 2 + 1.4}" font-family="Work Sans" font-weight="700" '
                 f'font-size="3.6" fill="{INDIGO_T}">{lab}</text>')
    y = top - 16
    s.append(f'<polygon points="{cx},{y} {cx + 20},{y + 6} {cx},{y + 12} {cx - 20},{y + 6}" fill="{SAFFRON}"/>'
             f'<polygon points="{cx - 20},{y + 6} {cx},{y + 12} {cx},{y + 16} {cx - 20},{y + 10}" fill="#B9660A"/>'
             f'<polygon points="{cx + 20},{y + 6} {cx},{y + 12} {cx},{y + 16} {cx + 20},{y + 10}" fill="#9A5508"/>'
             f'<text x="{cx}" y="{y + 7.6}" text-anchor="middle" font-family="Work Sans" font-weight="700" '
             f'font-size="3.6" fill="{NAVY}">MODEL</text>'
             f'<line x1="{cx}" y1="{y + 16}" x2="{cx}" y2="{top}" stroke="{SAFFRON}" stroke-width="0.5" stroke-dasharray="1 1"/>')
    s.append(title2(14, 44, 80, 40, WHITE, WHITE, SAFFRON))
    s.append(subtitle(14, 93, INDIGO_T, size=4.2, width=58, lead=5.4))
    s.append(f'<text x="14" y="116" font-family="Plex Serif" font-size="4.8" fill="{SAFFRON_L}">One real system, '
             f'built layer by layer and measured at every step.</text>')
    s.append(foot(WHITE, SOFT))
    return page("".join(s), NAVY)


# ------------------------------------------------------------------ concept E: typographic, demo vs production
def demo_vs_prod():
    s = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>', f'<rect y="150" width="{W}" height="{H - 150}" fill="{INK}"/>']
    s.append(f'<text x="14" y="30" font-family="Plex Mono" font-size="4" fill="#8A8F99">demo.py</text>'
             f'<text x="14" y="40" font-family="Plex Mono" font-size="4.2" fill="#555B66">&gt; Can I return opened earbuds?</text>'
             f'<text x="14" y="49" font-family="Plex Mono" font-size="4.2" fill="#B42318">&lt; Yes! Returns are accepted within 10 days.</text>'
             f'<line x1="14" y1="52" x2="128" y2="52" stroke="#B42318" stroke-width="0.6"/>')
    s.append(f'<text x="12" y="104" font-family="Work Sans" font-weight="700" font-size="44" letter-spacing="-1.8" '
             f'fill="{INK}">SHIP</text><text x="12" y="141" font-family="Work Sans" font-weight="700" font-size="44" '
             f'letter-spacing="-1.8" fill="{SAFFRON}">REAL AI</text>')
    s.append(f'<text x="14" y="164" font-family="Plex Mono" font-size="4" fill="#8A8F99">production</text>'
             f'<text x="14" y="174" font-family="Plex Mono" font-size="4.2" fill="#C9CED6">&gt; Can I return opened earbuds?</text>'
             f'<text x="14" y="183" font-family="Plex Mono" font-size="4.2" fill="#5FD39A">&lt; Only if they are faulty (policy §3, §4).</text>'
             f'<text x="14" y="190" font-family="Plex Mono" font-size="3.4" fill="#8A8F99">  sources checked · 1.2 s · ₹1.17 · golden set 92%</text>')
    s.append(subtitle(14, 204, WHITE, size=4.3, width=56, lead=5.6))
    s.append(chips(14, 222, INK, SAFFRON))
    s.append(foot(WHITE, '#AEB6C8', y=240))
    return page("".join(s), PAPER)


CONCEPTS = {"a-harness": harness, "b-trace": trace, "c-loop": loop, "d-stack": stack, "e-demo-vs-production": demo_vs_prod}

if __name__ == "__main__":
    px_w = round(W / 25.4 * 300)
    px_h = round(H / 25.4 * 300)
    css_w, css_h = round(W / 25.4 * 96), round(H / 25.4 * 96)
    jobs = []
    for name, fn in CONCEPTS.items():
        (OUT / f"{name}.html").write_text(fn())
        jobs.append({"src": str(OUT / f"{name}.html"), "out": str(OUT / f"{name}.png"), "type": "png",
                     "width": css_w, "height": css_h, "scale": px_w / css_w})
    (OUT / "jobs.json").write_text(json.dumps(jobs))
    subprocess.run(["node", str(ROOT / "cover" / "render.mjs"), str(OUT / "jobs.json")], check=True)
    thumbs = []
    for name in CONCEPTS:
        im = Image.open(OUT / f"{name}.png").convert("RGB")
        ImageOps.grayscale(im).save(OUT / f"{name}-grey.png")
        t = im.resize((160, round(160 * im.height / im.width)), Image.LANCZOS)
        t.save(OUT / f"{name}-thumb160.png")
        thumbs.append(im.resize((600, round(600 * im.height / im.width)), Image.LANCZOS))
    sheet = Image.new("RGB", (len(thumbs) * 620 + 20, thumbs[0].height + 40), "#DDDDDD")
    for i, t in enumerate(thumbs):
        sheet.paste(t, (20 + i * 620, 20))
    sheet.save(OUT / "compare.png")
    print("sheet", sheet.size)

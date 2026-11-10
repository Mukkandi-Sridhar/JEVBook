"""Third round of front covers for Ship Real AI: the ship is made of AI. Run: python3 cover/covers3.py

The ship's sails are the layers of a neural network, its hull is a mesh of nodes, and the sea it sails on is made
of customer messages. B5 trim (176 x 250 mm) plus 3 mm bleed; SVG in millimetres, rendered by Chromium at 300 dpi
to cover/round3/.
"""
import json
import random
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "cover" / "round3"
FONTS = ROOT / "assets" / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 179, 256
SUB1 = "The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals,"
SUB2 = "from First Principles to Production and Interviews"
AUTHOR = "SRIDHAR MUKKANDI"
WS, SERIF, MONO = "Work Sans", "Plex Serif", "Plex Mono"

# The sea: the concepts the book teaches.
SEA = ["tokens", "attention", "embeddings", "KV cache", "context window", "system prompt", "structured output",
       "tool calls", "BM25", "HNSW", "hybrid search", "reranker", "RAG", "chunking", "golden set", "LLM-as-judge",
       "calibration", "agent loop", "ReAct", "guardrails", "prompt injection", "MCP", "skills", "A2A", "durable execution",
       "semantic cache", "prompt caching", "rate limits", "traces", "canary release", "LoRA", "distillation", "evals",
       "least privilege", "idempotency", "mixture of experts", "transformer", "latency budget"]


def page(body, bg, defs=""):
    fonts = "".join(
        f"@font-face{{font-family:'{fam}';src:url('file://{FONTS / f}');font-weight:{wt};font-style:{st};}}"
        for fam, f, wt, st in [(WS, "WorkSans-Regular.ttf", 400, "normal"), (WS, "WorkSans-Bold.ttf", 700, "normal"),
                               (SERIF, "IBMPlexSerif-Italic.ttf", 400, "italic"),
                               (SERIF, "IBMPlexSerif-Bold.ttf", 700, "normal"),
                               (MONO, "IBMPlexMono-Regular.ttf", 400, "normal"),
                               (MONO, "IBMPlexMono-Bold.ttf", 700, "normal")])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
html,body{{margin:0;background:{bg}}} svg{{display:block}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}"><defs>{defs}</defs>
{body}</svg></body></html>"""


def t(x, y, s, size, fill, fam=WS, wt=700, anchor="start", ls=0, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{wt}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{s}</text>')


# ---------------------------------------------------------------- the ship
def sail(x0, top, bottom, width, cols, direction, spacing, belly):
    """A sail whose cloth is a neural network: columns of nodes (layers), tallest at the mast, one at the clew.

    belly > 1 bows the outer edge outwards, as wind does. Returns (columns of nodes, outline path)."""
    def ytop(f):
        return top + (bottom - top) * f ** belly
    columns = []
    for k in range(cols):
        f = k / (cols - 1)
        x, h = x0 + direction * width * f, bottom - ytop(f)
        n = max(1, round(h / spacing) + 1)
        columns.append([(x, bottom - h * j / (n - 1)) for j in range(n)] if n > 1 else [(x, bottom)])
    pts = [(x0, bottom), (x0, top)] + [(x0 + direction * width * i / 30, ytop(i / 30)) for i in range(1, 31)]
    return columns, "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"


def ship(cx, base, p, scale=1.0, pitch=-4.0):
    """The neural ship. cx: the mast; base: the y of the deck. Returns SVG."""
    s = scale
    top_y = base - 90 * s
    main, main_d = sail(cx - 1.5 * s, base - 84 * s, base - 7 * s, 54 * s, 6, -1, 10.4 * s, 1.55)
    jib, jib_d = sail(cx + 1.5 * s, base - 72 * s, base - 7 * s, 40 * s, 5, +1, 10.4 * s, 1.45)
    edges, nodes = [], []
    for cols in (main, jib):
        for u_col, v_col in zip(cols, cols[1:]):
            edges += [(u, v) for u in u_col for v in v_col]
        nodes += [n for col in cols for n in col]
    lines = "".join(f'<line x1="{u[0]:.2f}" y1="{u[1]:.2f}" x2="{v[0]:.2f}" y2="{v[1]:.2f}"/>' for u, v in edges)
    out = [f'<path d="{main_d}" fill="{p["sailfill"]}"/><path d="{jib_d}" fill="{p["sailfill"]}"/>',
           f'<g stroke="url(#sail)" stroke-width="{0.2 * s}" opacity="{p["web"]}" fill="none">{lines}</g>',
           f'<path d="{main_d}" fill="none" stroke="url(#sail)" stroke-width="{0.5 * s}" stroke-linejoin="round"/>'
           f'<path d="{jib_d}" fill="none" stroke="url(#sail)" stroke-width="{0.5 * s}" stroke-linejoin="round"/>']
    # hull: deck rising to the bow, a bowsprit, and a mesh of nodes over a solid body
    stern, bow = (cx - 50 * s, base + 1.5 * s), (cx + 66 * s, base - 4 * s)
    sprit = (cx + 80 * s, base - 8.5 * s)
    deck = [(stern[0] + (bow[0] - stern[0]) * i / 9, stern[1] + (bow[1] - stern[1]) * i / 9) for i in range(10)]
    keel = [(cx - 36 * s + i * 66 * s / 6, base + 19.5 * s + 1.2 * s * abs(i - 3) / 3 * -1) for i in range(7)]
    d = (f'M{stern[0]},{stern[1]} L{bow[0]},{bow[1]} Q{cx + 50 * s},{base + 15 * s} {keel[-1][0]},{keel[-1][1]} '
         f'Q{cx - 3 * s},{base + 22.5 * s} {keel[0][0]},{keel[0][1]} Q{cx - 47 * s},{base + 15 * s} {stern[0]},{stern[1]} Z')
    out.append(f'<line x1="{cx}" y1="{top_y}" x2="{sprit[0]}" y2="{sprit[1]}" stroke="{p["mast"]}" stroke-width="{0.22 * s}" opacity="0.7"/>'
               f'<line x1="{cx}" y1="{top_y}" x2="{stern[0] + 2 * s}" y2="{stern[1]}" stroke="{p["mast"]}" stroke-width="{0.22 * s}" opacity="0.7"/>'
               f'<line x1="{bow[0] - 2 * s}" y1="{bow[1] + 0.6 * s}" x2="{sprit[0]}" y2="{sprit[1]}" stroke="{p["mast"]}" '
               f'stroke-width="{0.7 * s}" stroke-linecap="round"/>'
               f'<line x1="{cx}" y1="{top_y}" x2="{cx}" y2="{base + 1 * s}" stroke="{p["mast"]}" stroke-width="{0.75 * s}" '
               f'stroke-linecap="round"/>')
    out.append(f'<path d="{d}" fill="url(#hull)"/>')
    hl = list(zip(keel, keel[1:]))
    for j, k in enumerate(keel):
        hl += [(k, deck[j + i]) for i in (1, 2)]
    out.append(f'<g stroke="{p["hullweb"]}" stroke-width="{0.3 * s}" opacity="{p["hullwebop"]}">'
               + "".join(f'<line x1="{u[0]:.2f}" y1="{u[1]:.2f}" x2="{v[0]:.2f}" y2="{v[1]:.2f}"/>' for u, v in hl) + "</g>")
    out.append(f'<path d="M{stern[0]},{stern[1]} L{bow[0]},{bow[1]}" stroke="{p["rail"]}" stroke-width="{0.7 * s}" stroke-linecap="round"/>')
    out.append("".join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{0.8 * s}" fill="{p["hullnode"]}"/>' for x, y in deck[1:-1]))
    halo = "".join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{2.6 * s}"/>' for x, y in nodes)
    out.append(f'<g fill="{p["halo"]}" opacity="{p["haloop"]}" filter="url(#soft)">{halo}</g>')
    out.append("".join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{0.95 * s}" fill="{p["node"]}"/>' for x, y in nodes))
    out.append(f'<circle cx="{cx}" cy="{top_y}" r="{5 * s}" fill="{p["halo"]}" opacity="0.6" filter="url(#soft)"/>'
               f'<circle cx="{cx}" cy="{top_y}" r="{1.8 * s}" fill="{p["top"]}"/>')
    return f'<g transform="rotate({pitch} {cx} {base + 12 * s})">' + "".join(out) + "</g>"


# ---------------------------------------------------------------- the sea of messages
def sea(y0, p, seed=3, rows=6):
    """Rows of text on wave paths, small and tight at the horizon, larger towards the reader."""
    rnd = random.Random(seed)
    defs, rows_out = [], []
    for i in range(rows):
        y = y0 + 3.3 * i + 0.6 * i * i
        amp, wl, size = 0.9 + 0.3 * i, 15 + 2.4 * i, 2.0 + 0.3 * i
        d = f"M{-20 - rnd.random() * wl} {y:.2f}" + "".join(f" q {wl / 4:.2f} {-amp:.2f} {wl / 2:.2f} 0 t {wl / 2:.2f} 0"
                                                           for _ in range(int(240 / wl) + 2))
        defs.append(f'<path id="w{seed}_{i}" d="{d}"/>')
        words = SEA[:]
        rnd.shuffle(words)
        op = p["sea_op"] * (1 - i / (rows + 1.5)) ** 1.25
        rows_out.append((size, op, f'<textPath href="#w{seed}_{i}">{"   ·   ".join(words)}</textPath>'))

    def layer(fill, k=1.0):
        return "".join(f'<text font-family="{MONO}" font-size="{sz:.2f}" fill="{fill}" opacity="{min(1, op * k):.2f}" '
                       f'letter-spacing="0.2">{tp}</text>' for sz, op, tp in rows_out)
    return "".join(defs), layer


def stars(p, n=85, ymax=150, seed=5):
    rnd = random.Random(seed)
    pts = [(rnd.uniform(4, W - 4), rnd.uniform(6, ymax)) for _ in range(n)]
    out = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.choice([0.22, 0.22, 0.3, 0.42]):.2f}" fill="{p["star"]}" '
                  f'opacity="{rnd.uniform(0.25, 0.9) * (1 - y / (ymax * 1.25)):.2f}"/>' for x, y in pts)
    return out


def common_defs(p):
    return f"""
<filter id="soft" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="1.5"/></filter>
<filter id="big" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="3.2"
 numOctaves="2" seed="4"/><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 {p['grain']} 0"/></filter>
<linearGradient id="sail" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['sail0']}"/>
<stop offset="1" stop-color="{p['sail1']}"/></linearGradient>
<linearGradient id="hull" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p['hull0']}"/>
<stop offset="1" stop-color="{p['hull1']}"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">{''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in p['sky'])}
</linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['water']}" stop-opacity="0"/>
<stop offset="0.25" stop-color="{p['water']}" stop-opacity="0.35"/><stop offset="0.5" stop-color="{p['water']}" stop-opacity="0.9"/><stop offset="1" stop-color="{p['water']}" stop-opacity="1"/></linearGradient>"""


def neural_ship(p, tag1="A demo floats.", tag2="A real system sails."):
    cx, base = 88, 170
    horizon = base + 16
    sdefs, sea_layer = sea(horizon + 7.5, p)
    s = [f'<rect width="{W}" height="{H}" fill="url(#sky)"/>', stars(p, ymax=horizon - 14)]
    if p.get("sun"):                                             # a rising sun behind the sails
        s.append(f'<circle cx="{cx + 6}" cy="{horizon - 30}" r="74" fill="{p["sun"][1]}" opacity="0.5" filter="url(#big)"/>'
                 f'<g clip-path="url(#above)"><circle cx="{cx + 6}" cy="{horizon - 30}" r="57" fill="url(#sun)"/>'
                 + "".join(f'<circle cx="{cx + 6}" cy="{horizon - 30}" r="{r}" fill="none" stroke="{p["ring"]}" '
                           f'stroke-width="0.25" opacity="{o}"/>' for r, o in [(64, 0.34), (73, 0.22), (84, 0.13)]) + "</g>")
    else:
        s.append(f'<ellipse cx="{cx}" cy="{base - 42}" rx="62" ry="58" fill="{p["aura"]}" opacity="{p["auraop"]}" filter="url(#big)"/>')
    s.append(f'<rect y="{horizon}" width="{W}" height="{H - horizon}" fill="url(#water)"/>')
    s.append(f'<ellipse cx="{W / 2}" cy="{horizon}" rx="130" ry="2.6" fill="{p["dawn"]}" opacity="{p["dawnop"]}" filter="url(#soft)"/>')
    s.append(f'<ellipse cx="{cx + 6}" cy="{horizon + 6}" rx="70" ry="9" fill="{p["glow"]}" opacity="{p["glowop"]}" filter="url(#big)"/>')
    s.append(ship(cx, base, p))
    s.append(f'<rect y="{horizon + 0.6}" width="{W}" height="14" fill="url(#lap)"/>')      # water over the keel
    s.append(sea_layer(p["sea"]))
    s.append(f'<g mask="url(#refl)">{sea_layer(p["searefl"], 1.9)}</g>')
    s.append(f'<rect y="200" width="{W}" height="56" fill="url(#fade)"/>')
    s.append(t(14, 50, f'SHIP REAL <tspan fill="{p["ai"]}">AI</tspan>', 26.5, p["title"],
               extra='textLength="151" lengthAdjust="spacingAndGlyphs"'))
    s.append(t(14.5, 61.5, SUB1, 4.25, p["sub"], wt=400) + t(14.5, 67.3, SUB2, 4.25, p["sub"], wt=400))
    s.append(t(W / 2, 234, f'{tag1} <tspan fill="{p["accent"]}">{tag2}</tspan>', 6.8, p["title"], SERIF, 400, "middle",
               extra='font-style="italic"'))
    s.append(t(W / 2, 247.5, AUTHOR, 5.4, p["title"], anchor="middle", ls=1.6))
    s.append(f'<rect width="{W}" height="{H}" filter="url(#grain)"/>')
    sun = p.get("sun")
    extra = f"""
<clipPath id="above"><rect width="{W}" height="{horizon}"/></clipPath>

<linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['water0']}"/>
<stop offset="0.5" stop-color="{p['water']}"/><stop offset="1" stop-color="{p['water']}"/></linearGradient>
<linearGradient id="lap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['water0']}" stop-opacity="0.0"/>
<stop offset="0.5" stop-color="{p['water0']}" stop-opacity="0.85"/><stop offset="1" stop-color="{p['water0']}" stop-opacity="0"/></linearGradient>
<mask id="refl"><ellipse cx="{cx + 6}" cy="{horizon + 30}" rx="26" ry="44" fill="white" filter="url(#big)"/></mask>"""
    if sun:
        extra += (f'<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1">'
                  + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in zip((0, 0.5, 1), sun)) + "</linearGradient>")
    return page("".join(s), p["bg"], common_defs(p) + extra + sdefs)


NIGHT = dict(bg="#050716", sky=[(0, "#04061A"), (0.42, "#0B1040"), (0.727, "#27218A"), (1, "#27218A")],
             water0="#141055", water="#050720", aura="#5B4BFF", auraop=0.6, glow="#FF9A2E", glowop=0.55,
             dawn="#FF8A3D", dawnop=0.55, sail0="#FFFFFF", sail1="#FFC873", sailfill="rgba(255,255,255,0.05)", web=0.5,
             mast="#FFFFFF", hull0="#FFC857", hull1="#EA6208", hullweb="#FFF1D0", hullwebop=0.5, rail="#FFF4DC",
             hullnode="#FFFFFF", node="#FFFFFF", halo="#FFB23E", haloop=0.75, top="#FFD27F", star="#C9D2FF",
             sea="#9AA6F5", searefl="#FFC873", sea_op=0.9, title="#FFFFFF", ai="#FFB23E", sub="#BBC4EE",
             accent="#FFB84D", grain=0.05, ring="#FFFFFF")

# The hero: a sun rising behind the sails.
DAWN = dict(NIGHT, sky=[(0, "#05061C"), (0.4, "#101146"), (0.727, "#3A2796"), (1, "#3A2796")],
            sun=("#6F52FF", "#D9409F", "#FF6F61"), sailfill="rgba(10,10,48,0.62)", web=0.62, water0="#1A1160",
            dawn="#FFB061", dawnop=0.85, glow="#FF7A3D", glowop=0.6, searefl="#FFD08A")

# Saffron day: dark ship on orange, for a shelf of dark AI books.
SAFFRON = dict(bg="#F7860F", sky=[(0, "#FFA233"), (0.727, "#F7860F"), (1, "#F7860F")], sun=("#FFF6DF", "#FFE9BD", "#FFD896"),
               water0="#E06C06", water="#D96505", aura="#FFFFFF", auraop=0, glow="#FFF3D6", glowop=0.45,
               dawn="#FFF3D6", dawnop=0.8, sail0="#10163A", sail1="#10163A", sailfill="rgba(16,22,58,0.10)", web=0.5,
               mast="#10163A", hull0="#1E2866", hull1="#0A0E2C", hullweb="#FFC873", hullwebop=0.55, rail="#FFE2AE",
               hullnode="#FFE2AE", node="#10163A", halo="#FFF3D6", haloop=0.85, top="#FFFFFF", star="#FFE9BD",
               sea="#1A1F55", searefl="#FFF6DF", sea_op=0.8, title="#10163A", ai="#10163A", sub="#232A63",
               accent="#FFFFFF", grain=0.04, ring="#FFFFFF")

# Paper: indigo ship and a saffron sun on cream.
PAPER = dict(bg="#F4EFE3", sky=[(0, "#FBF8F0"), (0.727, "#F1EADA"), (1, "#F1EADA")], sun=("#FFC65A", "#FF9E2E", "#F27C12"),
             water0="#D5D9F0", water="#EDE7D8", aura="#FFFFFF", auraop=0, glow="#FF9E2E", glowop=0.35,
             dawn="#F27C12", dawnop=0.5, sail0="#1B2566", sail1="#1B2566", sailfill="rgba(244,239,227,0.30)", web=0.5,
             mast="#1B2566", hull0="#3B4BA8", hull1="#151D57", hullweb="#DCE0F3", hullwebop=0.6, rail="#DCE0F3",
             hullnode="#FFFFFF", node="#1B2566", halo="#FFB23E", haloop=0.7, top="#F27C12", star="#B8BEDD",
             sea="#2A3789", searefl="#C85E00", sea_op=0.75, title="#10163A", ai="#E8780A", sub="#454C6E",
             accent="#C85E00", grain=0.0, ring="#E8780A")

VARIANTS = {"1-neural-ship-dawn": lambda: neural_ship(DAWN), "2-neural-ship-night": lambda: neural_ship(NIGHT),
            "3-neural-ship-saffron": lambda: neural_ship(SAFFRON), "4-neural-ship-paper": lambda: neural_ship(PAPER)}

if __name__ == "__main__":
    only = sys.argv[1:]
    names = [n for n in VARIANTS if not only or any(o in n for o in only)]
    css_w, css_h = round(W / 25.4 * 96), round(H / 25.4 * 96)
    scale = round(W / 25.4 * 300) / css_w
    jobs = []
    for name in names:
        (OUT / f"{name}.html").write_text(VARIANTS[name]())
        jobs.append({"src": str(OUT / f"{name}.html"), "out": str(OUT / f"{name}.png"), "type": "png",
                     "width": css_w, "height": css_h, "scale": scale})
    (OUT / "jobs.json").write_text(json.dumps(jobs))
    subprocess.run(["node", str(ROOT / "cover" / "render.mjs"), str(OUT / "jobs.json")], check=True,
                   stdout=subprocess.DEVNULL)
    (OUT / "jobs.json").unlink()
    ims = [Image.open(OUT / f"{n}.png").convert("RGB") for n in VARIANTS if (OUT / f"{n}.png").exists()]
    big = [im.resize((700, round(700 * im.height / im.width)), Image.LANCZOS) for im in ims]
    sheet = Image.new("RGB", (len(big) * 720 + 20, big[0].height + 40), "#D9D9D9")
    for i, b in enumerate(big):
        sheet.paste(b, (20 + i * 720, 20))
    sheet.save(OUT / "compare.png")
    th = [im.resize((160, 229), Image.LANCZOS) for im in ims]
    sheet = Image.new("RGB", (len(th) * 175 + 15, 2 * 240 + 20), "white")
    for i, x in enumerate(th):
        sheet.paste(x, (15 + i * 175, 10))
        sheet.paste(ImageOps.grayscale(x).convert("RGB"), (15 + i * 175, 250))
    sheet.save(OUT / "thumbs.png")
    print("rendered", names)

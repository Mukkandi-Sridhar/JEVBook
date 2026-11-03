import json
import numpy as np
import figstyle as fs
from figstyle import C

R = fs.ROOT / "research"
BM = json.loads((R / "m06-bm25.json").read_text())
ANN = json.loads((R / "m06-ann.json").read_text())
LABEL = {"P1": "P1 general returns", "P2": "P2 hygiene (the answer)", "P3": "P3 earbuds guide",
         "P4": "P4 FAQ: unopened earbuds", "P5": "P5 faulty items", "P6": "P6 refund timing",
         "P7": "P7 phones", "P8": "P8 AX-7781 sale"}


def fig_keyword_scores():
    f, axes = fs.subplots(1, 2, height=2.1, sharey=True)
    order = list(LABEL)
    for ax, q, title in [(axes[0], "can I return opened earbuds", "Query 1:\n\"can I return opened earbuds\""),
                         (axes[1], "can I send back earphones I already used",
                          "Query 2:\n\"can I send back earphones I already used\"")]:
        sc = BM[q]["scores"]
        ys = np.arange(len(order))[::-1]
        cols = [C["saffron"] if p == "P2" else C["indigo"] for p in order]
        ax.barh(ys, [sc[p] for p in order], color=cols, height=0.6)
        for y, p in zip(ys, order):
            ax.text(sc[p] + 0.04, y, f"{sc[p]:.2f}", va="center", fontsize=6.0, color=C["ink2"])
        ax.set_title(title, fontsize=6.3, color=C["ink"], pad=4, linespacing=1.2)
        ax.set_xlim(0, 2.3)
        ax.grid(axis="y", visible=False)
        ax.set_xlabel("BM25 score")
    axes[0].set_yticks(np.arange(len(order))[::-1], [LABEL[p] for p in order], fontsize=6.4)
    axes[1].text(1.15, 3.5, "no shared words:\nevery score is 0", ha="center", fontsize=6.6, color=C["crimson"])
    f.tight_layout()
    return f


def fig_inverted_index():
    f, ax = fs.canvas(5.2, 1.9)
    ax.text(0.0, 1.8, "WORD", fontsize=6.4, fontweight="bold", color=C["ink2"])
    ax.text(1.05, 1.8, "PARAGRAPHS THAT CONTAIN IT", fontsize=6.4, fontweight="bold", color=C["ink2"])
    rows = [("return", BM["index_sample"]["return"]), ("open", BM["index_sample"]["open"]),
            ("earbud", BM["index_sample"]["earbud"]), ("ax-7781", BM["index_sample"]["ax-7781"])]
    for i, (w, ps) in enumerate(rows):
        y = 1.42 - i * 0.36
        fs.box(ax, 0.0, y, 0.85, 0.27, w, size=6.6, fc=C["indigo_t"], ec=C["indigo"])
        fs.arrow(ax, 0.87, y + 0.135, 1.03, y + 0.135, lw=0.8)
        for j, p in enumerate(ps):
            fs.box(ax, 1.05 + j * 0.42, y, 0.36, 0.27, p, size=6.2,
                   fc=C["saffron_t"] if p == "P2" else "white", ec=C["saffron"] if p == "P2" else None)
    ax.text(3.75, 1.0, "A query for \"opened\"\nreads one short list,\nnot every paragraph.",
            fontsize=6.4, va="center", color=C["ink2"])
    return f


def fig_bm25_parts():
    f, axes = fs.subplots(1, 3, height=1.75)
    tf = np.arange(0, 11)
    k1 = 1.5
    axes[0].plot(tf, tf * (k1 + 1) / (tf + k1), color=C["indigo"], marker="o", ms=3)
    axes[0].set_title("1  How often", fontsize=6.8, color=C["ink"])
    axes[0].set_xlabel("times the word appears")
    axes[0].set_ylabel("weight")
    axes[0].set_ylim(0, 2.6)
    idf = BM["idf"]
    axes[1].bar(["return\n6 of 8", "earbud\n3 of 8", "open\n1 of 8"], [idf["return"], idf["earbud"], idf["open"]],
                color=[C["slate"], C["slate"], C["saffron"]], width=0.55)
    for x, v in enumerate([idf["return"], idf["earbud"], idf["open"]]):
        axes[1].text(x, v + 0.05, f"{v:.2f}", ha="center", fontsize=6.0)
    axes[1].set_title("2  How rare", fontsize=6.8, color=C["ink"])
    axes[1].set_ylim(0, 2.0)
    axes[1].tick_params(axis="x", labelsize=6.0)
    axes[1].grid(axis="x", visible=False)
    L = np.linspace(5, 40, 50)
    b, avg = 0.75, 13
    axes[2].plot(L, (k1 + 1) / (1 + k1 * (1 - b + b * L / avg)), color=C["indigo"])
    axes[2].axvline(avg, color=C["rule"], ls=(0, (3, 2)), lw=0.8)
    axes[2].text(avg + 1, 1.45, "average\nlength", fontsize=5.8, color=C["ink2"])
    axes[2].set_title("3  How long", fontsize=6.8, color=C["ink"])
    axes[2].set_xlabel("paragraph length (words)")
    axes[2].set_ylim(0, 1.9)
    f.tight_layout(w_pad=1.2)
    return f


def fig_hnsw():
    f, ax = fs.canvas(5.2, 2.75)
    rng = np.random.default_rng(3)
    layers = [(2.0, 4), (1.15, 10), (0.25, 26)]
    pts = rng.uniform([0.4, 0], [4.4, 0.45], size=(26, 2))
    target = np.array([3.85, 0.2])
    pts[5] = target + [0.05, 0.02]
    chosen = {0: [0, 1, 2, 3], 1: list(range(10)), 2: list(range(26))}
    path = [[0, 1], [1, 4, 7], [7, 9, 5]]
    for li, (y0, n) in enumerate(layers):
        fs.box(ax, 0.3, y0 - 0.05, 4.25, 0.6, "", fc=C["paper"] if li < 2 else "white", ec=C["rule"], lw=0.6)
        ax.text(0.22, y0 + 0.25, ["top layer:\nfew points,\nlong links", "middle", "bottom layer:\nevery point"][li],
                ha="right", va="center", fontsize=5.8, color=C["ink2"])
        idx = chosen[li]
        P = pts[idx] + [0, y0]
        for a in range(len(idx)):
            d = np.linalg.norm(P - P[a], axis=1)
            for b in np.argsort(d)[1:3]:
                ax.plot([P[a, 0], P[b, 0]], [P[a, 1], P[b, 1]], color=C["rule"], lw=0.5, zorder=1)
        ax.scatter(P[:, 0], P[:, 1], s=9, color=C["slate"], zorder=2)
        hop = [pts[i] + [0, y0] for i in path[li]]
        for a, b in zip(hop, hop[1:]):
            ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=C["saffron"], lw=1.4))
    for (ya, yb, i) in [(2.0, 1.15, 1), (1.15, 0.25, 7)]:
        x, yy = pts[i]
        ax.plot([x, x], [ya + yy, yb + yy], color=C["saffron"], lw=1.0, ls=(0, (2, 2)))
    tq = target + [0, 0.25]
    ax.scatter([tq[0]], [tq[1]], marker="*", s=70, color=C["crimson"], zorder=3)
    ax.text(tq[0] + 0.1, tq[1] + 0.12, "query", fontsize=6.2, color=C["crimson"])
    ax.text(2.45, 2.7, "Start at the top, jump close fast, then step down and search finely", ha="center",
            fontsize=6.2, color=C["ink2"])
    return f


def fig_ann_tradeoff():
    f, ax = fs.subplots(height=1.95)
    h = ANN["hnsw"]
    ax.plot([x["ms_per_query"] for x in h], [x["recall_at_10"] for x in h], color=C["indigo"], marker="o")
    for x in h:
        ax.text(x["ms_per_query"] * 1.12, x["recall_at_10"] - 0.03, f"ef={x['ef']}", fontsize=5.8, color=C["ink2"])
    ax.plot([ANN["flat_ms_per_query"]], [1.0], marker="s", color=C["saffron"])
    ax.text(ANN["flat_ms_per_query"] * 0.92, 0.955, f"check every vector\n{ANN['flat_ms_per_query']:.0f} ms",
            fontsize=6.0, ha="right", va="top", color=C["saffron"])
    ax.text(0.33, 0.9, "HNSW", fontsize=6.6, color=C["indigo"], fontweight="bold")
    ax.set_xscale("log")
    ax.set_xticks([0.3, 1, 3, 10, 30, 60], ["0.3", "1", "3", "10", "30", "60"])
    ax.set_xlabel("milliseconds per query (log scale)")
    ax.set_ylabel("true top 10 found")
    ax.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0], ["50%", "60%", "70%", "80%", "90%", "100%"])
    ax.set_ylim(0.45, 1.05)
    return f


def fig_hybrid():
    f, ax = fs.canvas(5.2, 2.05)
    kw = ["P2", "P4", "P8", "P3", "P1"]
    vec = ["P4", "P3", "P8", "P2", "P1"]
    rrf = {}
    for lst in (kw, vec):
        for r, p in enumerate(lst, 1):
            rrf[p] = rrf.get(p, 0) + 1 / (60 + r)
    fused = sorted(rrf, key=lambda p: -rrf[p])
    cols = [(0.0, "KEYWORD (BM25)", kw, None), (1.75, "MEANING (vectors)", vec, None),
            (3.5, "COMBINED (RRF)", fused, rrf)]
    for x, title, lst, sc in cols:
        ax.text(x + 0.7, 1.95, title, ha="center", fontsize=6.4, fontweight="bold", color=C["ink2"])
        for r, p in enumerate(lst):
            y = 1.55 - r * 0.33
            ans = p == "P2"
            txt = f"{r + 1}  {LABEL[p][3:]}" if sc is None else f"{r + 1}  {LABEL[p][3:]}  {sc[p] * 1000:.1f}"
            fs.box(ax, x, y, 1.5, 0.26, txt, size=5.6, ha="left", fc=C["saffron_t"] if ans else "white",
                   ec=C["saffron"] if ans else None)
    fs.arrow(ax, 1.55, 0.95, 1.72, 0.95, lw=0.8)
    ax.text(1.635, 1.05, "+", ha="center", fontsize=8)
    fs.arrow(ax, 3.3, 0.95, 3.47, 0.95, lw=0.8)
    return f

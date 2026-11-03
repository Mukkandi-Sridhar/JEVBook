import figstyle as fs
from figstyle import C


def fig_four_questions():
    f, ax = fs.canvas(5.2, 2.5)
    cols = [("Where is the\nknowledge?", ["Meaning: vector RAG", "Exact words: BM25", "Both: hybrid RAG",
                                         "Tables: text-to-SQL", "Relationships: graph RAG", "Page images",
                                         "The live web"]),
            ("How good is\nthe question?", ["Rewrite it", "Split it", "Write a guess\nanswer (HyDE)"]),
            ("How do you check\nwhat was found?", ["Grade the chunks\n(corrective RAG)",
                                                 "Model critiques\nitself (self-RAG)"]),
            ("Who decides\nwhere to look?", ["Fixed pipeline", "A router picks\n(adaptive RAG)",
                                             "The model, in a\nloop (agentic RAG)"])]
    w, gap = 1.2, 0.133
    for i, (q, opts) in enumerate(cols):
        x = i * (w + gap)
        fs.box(ax, x, 1.92, w, 0.48, q, size=6.4, weight="bold", fc=C["navy"], ec=C["navy"], color="white")
        y = 1.78
        for o in opts:
            h = 0.32 if "\n" in o else 0.21
            fs.box(ax, x, y - h, w, h, o, size=5.8, fc=C["indigo_t"] if i == 0 else "white",
                   ec=C["indigo"] if i == 0 else C["rule"], radius=0.03)
            y -= h + 0.045
    return f


def fig_query_rewrite():
    f, ax = fs.canvas(5.2, 2.05)
    ax.text(0.0, 1.95, "REWRITE: make it stand alone", fontsize=6.6, fontweight="bold", color=C["indigo"])
    fs.box(ax, 0.0, 1.25, 2.3, 0.55, "Earlier: \"Can I return opened earbuds?\"\nNow: \"and for phones?\"",
           size=6.0, ha="left")
    fs.arrow(ax, 2.35, 1.52, 2.7, 1.52, lw=1.0)
    fs.box(ax, 2.75, 1.3, 2.45, 0.45, "\"What is the return policy for phones?\"", size=6.0, fc=C["indigo_t"],
           ec=C["indigo"])
    ax.text(0.0, 0.98, "SPLIT: one search per part", fontsize=6.6, fontweight="bold", color=C["indigo"])
    fs.box(ax, 0.0, 0.05, 2.3, 0.75, "\"Can I return the earbuds and\nthe phone case together, and\nwhen "
           "will I get my money?\"", size=6.0, ha="left")
    for i, t in enumerate(["return rules for earbuds", "return rules for phone cases", "refund timing"]):
        y = 0.6 - i * 0.27
        fs.arrow(ax, 2.35, 0.42, 2.7, y + 0.1, lw=0.8)
        fs.box(ax, 2.75, y, 2.45, 0.21, t, size=6.0, fc=C["indigo_t"], ec=C["indigo"])
    return f


def fig_text_to_sql():
    f, ax = fs.canvas(5.2, 1.95)
    fs.box(ax, 0.0, 1.2, 1.25, 0.55, "\"How many refunds\nover ₹2,000 this year?\"", size=6.0)
    fs.arrow(ax, 1.27, 1.47, 1.5, 1.47, lw=1.0)
    fs.box(ax, 1.52, 1.2, 0.9, 0.55, "Model writes\nSQL", size=6.2, fc=C["saffron_t"], ec=C["saffron"])
    fs.arrow(ax, 2.44, 1.47, 2.67, 1.47, lw=1.0)
    fs.box(ax, 2.69, 0.95, 1.35, 1.05, "", fc=C["crimson_t"], ec=C["crimson"])
    ax.text(3.365, 1.88, "YOUR CHECKS", ha="center", fontsize=6.2, fontweight="bold", color=C["crimson"])
    ax.text(2.76, 1.42, "• read-only login\n• allowed tables only\n• this customer's rows\n• at most 100 rows",
            fontsize=5.8, va="center", linespacing=1.35)
    fs.arrow(ax, 4.06, 1.47, 4.29, 1.47, lw=1.0)
    fs.box(ax, 4.31, 1.2, 0.89, 0.55, "Database\nruns it", size=6.2)
    fs.box(ax, 0.0, 0.05, 5.2, 0.62, "", fc=C["paper"], ec=C["rule"])
    ax.text(0.1, 0.36, "SELECT COUNT(*) FROM refunds\nWHERE customer_id = :me AND amount > 2000 AND "
            "created_at >= '2026-01-01';", fontsize=5.8, family="monospace", va="center", linespacing=1.3)
    ax.text(5.1, 0.36, ":me comes from the\nlogin, not the model", fontsize=5.8, color=C["crimson"], ha="right",
            va="center")
    return f


def fig_graph():
    f, ax = fs.canvas(5.2, 2.1)
    nodes = {"cust": (0.45, 1.05, "Customer\n881", "white"), "phone": (1.75, 1.05, "Phone\nNova 12", C["indigo_t"]),
             "case": (3.25, 1.75, "Case\nCS-12", C["indigo_t"]), "charger": (3.25, 0.35, "Charger\n33 W", C["indigo_t"]),
             "s1": (4.7, 1.75, "Seller\nRaj Mobiles", C["saffron_t"]),
             "s2": (4.7, 0.35, "Seller\nGadgetHub", C["saffron_t"])}
    for k, (x, y, t, fc) in nodes.items():
        fs.box(ax, x - 0.45, y - 0.22, 0.9, 0.44, t, size=6.0, fc=fc)
    edges = [("cust", "phone", "bought"), ("case", "phone", "fits"), ("charger", "phone", "fits"),
             ("s1", "case", "stocks"), ("s2", "charger", "stocks")]
    for a, b, lab in edges:
        xa, ya = nodes[a][:2]
        xb, yb = nodes[b][:2]
        dx, dy = xb - xa, yb - ya
        fs.arrow(ax, xa + 0.47 * (1 if dx > 0 else -1) if abs(dx) > 0.1 else xa, ya,
                 xb - 0.47 * (1 if dx > 0 else -1) if abs(dx) > 0.1 else xb, yb, lw=0.9)
        ax.text((xa + xb) / 2, (ya + yb) / 2 + 0.07, lab, ha="center", fontsize=5.8, color=C["ink2"])
    return f


def fig_who_decides():
    f, ax = fs.canvas(5.2, 2.0)
    ax.text(1.2, 1.9, "HYBRID: always both, then merge", ha="center", fontsize=6.4, fontweight="bold",
            color=C["indigo"])
    fs.box(ax, 0.75, 1.4, 0.9, 0.3, "question", size=6.0)
    for x, t in [(0.0, "keyword"), (1.5, "meaning")]:
        fs.arrow(ax, 1.2, 1.4, x + 0.45, 1.06, lw=0.8)
        fs.box(ax, x, 0.76, 0.9, 0.3, t, size=6.0, fc=C["indigo_t"], ec=C["indigo"])
        fs.arrow(ax, x + 0.45, 0.76, 1.2, 0.44, lw=0.8)
    fs.box(ax, 0.75, 0.14, 0.9, 0.3, "merge (RRF)", size=6.0)
    ax.text(1.2, 0.02, "no model call to decide", ha="center", va="top", fontsize=5.8, color=C["ink2"])
    ax.text(3.95, 1.9, "AGENTIC: the model chooses, in a loop", ha="center", fontsize=6.4, fontweight="bold",
            color=C["saffron"])
    fs.box(ax, 3.45, 0.85, 1.0, 0.45, "Model", size=6.8, weight="bold", fc=C["saffron_t"], ec=C["saffron"])
    tools = [(2.85, 1.5, "search_policy"), (4.25, 1.5, "query_orders"), (2.85, 0.2, "grep_documents"),
             (4.25, 0.2, "web_search")]
    ends = [((3.45, 1.3), (3.3, 1.5)), ((4.45, 1.3), (4.7, 1.5)), ((3.45, 0.85), (3.3, 0.48)),
            ((4.45, 0.85), (4.7, 0.48))]
    for (x, y, t), (a, b) in zip(tools, ends):
        fs.box(ax, x, y, 0.95, 0.28, t, size=5.6)
        fs.arrow(ax, a[0], a[1], b[0], b[1], lw=0.7, style="<|-|>")
    ax.text(3.95, 0.02, "each choice is a model call", ha="center", va="top", fontsize=5.8, color=C["ink2"])
    return f

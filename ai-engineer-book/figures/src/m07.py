import json
import textwrap
import figstyle as fs
from figstyle import C

CH = json.loads((fs.ROOT / "research" / "m07-chunks.json").read_text())


def fig_rag_pipelines():
    f, ax = fs.canvas(5.2, 2.35)

    def row(y, title, steps, fc, ec, note):
        ax.text(0.0, y + 0.62, title, fontsize=6.6, fontweight="bold", color=ec)
        ax.text(5.2, y + 0.62, note, fontsize=6.0, color=C["ink2"], ha="right")
        n = len(steps)
        w, gap = (5.2 - 0.12 * (n - 1)) / n, 0.12
        for i, s in enumerate(steps):
            x = i * (w + gap)
            fs.box(ax, x, y, w, 0.48, s, size=6.0, fc=fc, ec=ec)
            if i < n - 1:
                fs.arrow(ax, x + w, y + 0.24, x + w + gap, y + 0.24, lw=0.9)

    row(1.45, "INGESTION: prepare the documents", ["Load\nPDFs, pages", "Clean\nheaders, tables", "Cut into\nchunks",
        "Add context\nto each", "Embed and\nindex", "Store"], C["slate_t"], C["slate"],
        "runs when documents change")
    row(0.2, "ANSWERING: for each question", ["Question", "Search\nboth ways", "Rerank\nkeep 5",
        "Build the\nrequest", "Model\nanswers", "Check\ncitations"], C["indigo_t"], C["indigo"],
        "runs for every message")
    fs.arrow(ax, 4.8, 1.45, 1.6, 0.7, lw=0.9, ls=(0, (3, 2)))
    ax.text(2.0, 1.22, "the store connects them", fontsize=5.8, color=C["ink2"], ha="center")
    return f


def _col(ax, x, w, title, chunks, highlight):
    ax.text(x + w / 2, 3.55, title, ha="center", fontsize=6.4, fontweight="bold", color=C["ink2"])
    y = 3.4
    for c in chunks:
        lines = textwrap.wrap(c.replace("\n", " "), 31)
        show = lines[:4] + (["…"] if len(lines) > 4 else [])
        h = 0.12 * len(show) + 0.08
        hit = any(k in c for k in highlight)
        fs.box(ax, x, y - h, w, h, "", fc=C["saffron_t"] if hit else "white",
               ec=C["saffron"] if hit else C["rule"], lw=0.7, radius=0.02)
        ax.text(x + 0.05, y - 0.05, "\n".join(show), fontsize=5.0, va="top", linespacing=1.15,
                family="monospace")
        y -= h + 0.04
    return y


def fig_chunking():
    f, ax = fs.canvas(5.2, 3.65)
    ax.set_ylim(0, 3.65)
    small = CH["fixed_120"]
    keep = [i for i, c in enumerate(small) if "3." in c or "In-ear" in c or "The rule" in c or "4." in c
            or "If an item" in c]
    sm = [small[i] for i in range(keep[0], keep[-1] + 1)]
    _col(ax, 0.0, 1.62, "TOO SMALL (120 characters)", sm, ["In-ear", "The rule"])
    big = CH["fixed_1000"]
    _col(ax, 1.78, 1.62, "TOO LARGE (1,000 characters)", big, ["In-ear"])
    heads = [d["text"] for d in CH["by_heading"]]
    heads = [("§" + d["meta"].get("section", "")[:2] + " " + d["text"]) for d in CH["by_heading"]]
    _col(ax, 3.56, 1.64, "BY HEADING (one section each)", heads, ["In-ear"])
    return f


def fig_contextual_results():
    f, ax = fs.subplots(height=1.8)
    labels = ["plain chunks\n(embeddings + BM25)", "with context\n(embeddings only)",
              "with context\n(embeddings + BM25)", "with context\n+ reranking"]
    vals = [5.7, 3.7, 2.9, 1.9]
    bars = ax.bar(labels, vals, color=[C["slate"], C["indigo"], C["indigo"], C["saffron"]], width=0.55)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.15, f"{v}%", ha="center", fontsize=6.6)
    ax.set_ylabel("right chunk not in top 20")
    ax.set_ylim(0, 7)
    ax.set_yticks([0, 2, 4, 6], ["0%", "2%", "4%", "6%"])
    ax.tick_params(axis="x", labelsize=6.0)
    ax.grid(axis="x", visible=False)
    return f


def fig_encoders():
    f, ax = fs.canvas(5.2, 2.15)
    ax.text(1.2, 2.05, "EMBEDDINGS: read separately", ha="center", fontsize=6.6, fontweight="bold",
            color=C["indigo"])
    fs.box(ax, 0.0, 1.45, 1.1, 0.36, "question", size=6.2)
    fs.box(ax, 1.3, 1.45, 1.1, 0.36, "paragraph", size=6.2)
    for x in (0.55, 1.85):
        fs.arrow(ax, x, 1.45, x, 1.2, lw=0.8)
        fs.box(ax, x - 0.5, 0.82, 1.0, 0.36, "embedding\nmodel", size=6.0, fc=C["indigo_t"], ec=C["indigo"])
        fs.arrow(ax, x, 0.82, x, 0.6, lw=0.8)
        fs.box(ax, x - 0.45, 0.3, 0.9, 0.28, "[0.12, …]", size=5.8)
    ax.text(1.2, 0.12, "compare the two lists: fast, paragraphs\nembedded once in advance", ha="center",
            va="top", fontsize=5.8, color=C["ink2"])
    ax.text(4.0, 2.05, "RERANKER: read together", ha="center", fontsize=6.6, fontweight="bold",
            color=C["saffron"])
    fs.box(ax, 2.95, 1.45, 2.1, 0.36, "question  +  paragraph", size=6.2)
    fs.arrow(ax, 4.0, 1.45, 4.0, 1.2, lw=0.8)
    fs.box(ax, 3.4, 0.82, 1.2, 0.36, "reranker\nmodel", size=6.0, fc=C["saffron_t"], ec=C["saffron"])
    fs.arrow(ax, 4.0, 0.82, 4.0, 0.6, lw=0.8)
    fs.box(ax, 3.4, 0.3, 1.2, 0.28, "does it answer? 0.94", size=5.8)
    ax.text(4.0, 0.12, "sees \"unopened\" against \"opened\": accurate,\nbut one model run per paragraph",
            ha="center", va="top", fontsize=5.8, color=C["ink2"])
    return f

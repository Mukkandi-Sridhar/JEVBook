import numpy as np
import figstyle as fs
from figstyle import C

# One support request in our example, in tokens (assumed sizes; they add up to Module 1's 3,000).
PARTS = [("Instructions", 700, "fixed"), ("Tool list", 600, "fixed"), ("Earlier\nmessages", 460, "changes"),
         ("Policy text", 1200, "changes"), ("Question", 40, "changes")]


def fig_request_anatomy():
    f, ax = fs.canvas(5.2, 1.75)
    total = sum(p[1] for p in PARTS)
    scale = 5.2 / total
    x = 0.0
    for name, n, kind in PARTS:
        w = n * scale
        fixed = kind == "fixed"
        fs.box(ax, x, 0.62, w - 0.03, 0.5, "", fc=C["indigo_t"] if fixed else C["saffron_t"],
               ec=C["indigo"] if fixed else C["saffron"], lw=0.9, radius=0.03)
        if n >= 400:
            ax.text(x + w / 2, 0.93, name, ha="center", va="center", fontsize=6.8 if "\n" not in name else 6.2,
                    fontweight="bold", linespacing=1.0)
            ax.text(x + w / 2, 0.71, f"{n:,} tokens", ha="center", fontsize=6.4, color=C["ink2"])
        x += w
    # the tiny question gets a pointer
    ax.annotate("Question: 40 tokens,\n1% of the request", xy=(5.2 - 0.03, 1.12), xytext=(4.55, 1.5),
                fontsize=6.4, ha="center", arrowprops=dict(arrowstyle="-", color=C["ink2"], lw=0.7))
    ax.plot([0, 1300 * scale - 0.03], [0.5, 0.5], color=C["indigo"], lw=1.2)
    ax.text(0, 0.36, "the same in every request: written once by you", fontsize=6.4, color=C["indigo"])
    ax.plot([1300 * scale, 5.2 - 0.03], [0.5, 0.5], color=C["saffron"], lw=1.2, ls=(0, (4, 2)))
    ax.text(5.17, 0.36, "different for every message", fontsize=6.4, color=C["saffron"], ha="right")
    ax.text(2.6, 0.06, "One request, 3,000 tokens in all (sizes assumed for illustration)", ha="center",
            fontsize=6.2, color=C["ink2"])
    return f


def fig_lost_middle():
    f, ax = fs.subplots(height=2.0)
    pos = np.array([1, 5, 10, 15, 20])
    acc = np.array([75, 57, 54, 56, 64])  # approximate shape, read off the published chart
    ax.plot(pos, acc, "o-", color=C["indigo"], lw=1.8)
    ax.axhline(56, color=C["crimson"], ls=(0, (4, 2)), lw=1.0)
    ax.text(20.3, 55.2, "with no documents: 56%", fontsize=6.4, color=C["crimson"], ha="right", va="top")
    ax.set_xticks([1, 5, 10, 15, 20], ["1st", "5th", "10th", "15th", "20th"])
    ax.set_xlabel("where the one useful document sits among 20")
    ax.set_ylabel("questions answered correctly")
    ax.set_yticks([50, 60, 70, 80], ["50%", "60%", "70%", "80%"])
    ax.set_ylim(48, 80)
    ax.set_xlim(0, 21)
    ax.text(1.4, 76.5, "start", fontsize=6.8, fontweight="bold")
    ax.text(10, 52.2, "middle", fontsize=6.8, fontweight="bold", ha="center")
    ax.text(19.6, 65.6, "end", fontsize=6.8, fontweight="bold", ha="right")
    return f


def fig_context_funnel():
    f, ax = fs.subplots(height=2.15)
    stages = [("Search returns", 40, 16000, "40 pieces of policy"),
              ("Prune", 28, 11200, "drop 9 repeats and 3 out-of-date pieces"),
              ("Select", 6, 2400, "keep the 6 most relevant"),
              ("Compress", 6, 1200, "cut each to the paragraphs that matter")]
    ys = np.arange(len(stages))[::-1]
    for y, (name, n, tok, note) in zip(ys, stages):
        ax.barh(y, tok, color=C["indigo"] if name != "Search returns" else C["slate"], height=0.56)
        ax.text(tok + 250, y + 0.08, f"{tok:,} tokens", va="center", fontsize=6.8, fontweight="bold")
        ax.text(tok + 250, y - 0.2, note, va="center", fontsize=6.2, color=C["ink2"])
    ax.set_yticks(ys, [s[0] for s in stages])
    ax.set_xlim(0, 24500)
    ax.set_xticks([0, 5000, 10000, 15000], ["0", "5,000", "10,000", "15,000"])
    ax.axvline(1200, color=C["saffron"], ls=(0, (4, 2)), lw=1.0)
    ax.text(1350, 3.55, "budget: 1,200", fontsize=6.2, color=C["saffron"])
    ax.set_ylim(-0.5, 3.75)
    ax.grid(axis="y", visible=False)
    return f


WIDTHS = {"Instructions": 0.95, "Tools": 0.75, "Policy": 0.9, "History": 0.7, "Question": 0.7,
          "Date, name": 0.62}


def _row(ax, y, names, label, cached=0, changed_first=False):
    ax.text(0.9, y + 0.16, label, ha="right", va="center", fontsize=6.6)
    x = 0.98
    for i, n in enumerate(names):
        w = WIDTHS[n]
        hit = i < cached
        red = changed_first and i == 0
        fs.box(ax, x, y, w - 0.05, 0.32, n, size=6.2, radius=0.03, lw=0.9,
               fc=C["indigo"] if hit else (C["crimson_t"] if red else "white"),
               ec=C["indigo"] if hit else (C["crimson"] if red else C["rule"]),
               color="white" if hit else C["ink"], weight="bold" if hit else "normal")
        x += w
    return x


def fig_cache_prefix():
    f, ax = fs.canvas(5.2, 2.5)
    good = ["Instructions", "Tools", "History", "Policy", "Question"]
    ax.text(0.0, 2.38, "FIXED TEXT FIRST", fontsize=6.8, fontweight="bold", color=C["indigo"])
    _row(ax, 1.86, good, "request 1")
    _row(ax, 1.42, good, "request 2", cached=2)
    ax.text(0.98 + 0.85, 1.32, "same text, same position: read from the cache", ha="center", va="top",
            fontsize=6.2, color=C["indigo"])
    ax.text(0.0, 0.94, "TODAY'S DATE AND THE CUSTOMER'S NAME FIRST", fontsize=6.8, fontweight="bold",
            color=C["crimson"])
    bad = ["Date, name", "Instructions", "Tools", "History", "Policy", "Question"]
    _row(ax, 0.42, bad, "request 1", changed_first=True)
    _row(ax, -0.02, bad, "request 2", changed_first=True)
    ax.text(0.98 + 0.29, -0.12, "differs at the first token, so nothing after it is reused", ha="left",
            va="top", fontsize=6.2, color=C["crimson"])
    return f


def fig_compaction():
    f, ax = fs.subplots(height=2.1)
    steps = np.arange(0, 41)
    plain = 4000 + 3000 * steps
    ax.plot(steps[plain <= 100000], plain[plain <= 100000], color=C["crimson"], ls=(0, (4, 2)), lw=1.4)
    stop = steps[plain <= 100000][-1]
    ax.plot(stop, 100000, "x", color=C["crimson"], ms=7, mew=1.6)
    ax.text(stop + 0.7, 96000, "without compaction:\nfull, the run stops", fontsize=6.4, color=C["crimson"],
            ha="left", va="top")
    comp, y = [], 4000
    for s in steps:
        comp.append(y)
        y += 3000
        if y > 80000:
            y = 12000
    ax.plot(steps, comp, color=C["indigo"], lw=1.6)
    ax.text(40.5, comp[-1] + 1500, "with compaction", fontsize=6.4, color=C["indigo"], ha="right", va="bottom")
    ax.axhline(100000, color=C["ink2"], lw=0.8)
    ax.text(0.3, 102000, "context window: 100,000 tokens", fontsize=6.2, color=C["ink2"], va="bottom")
    ax.axhline(80000, color=C["saffron"], lw=0.9, ls=(0, (1, 1.6)))
    ax.text(0.3, 76000, "compact at 80%", fontsize=6.2, color=C["saffron"], va="top")
    ax.set_xlabel("steps of the agent (each adds about 3,000 tokens of tool results)")
    ax.set_ylabel("tokens in the context")
    ax.set_yticks([0, 25000, 50000, 75000, 100000], ["0", "25k", "50k", "75k", "100k"])
    ax.set_ylim(0, 112000)
    ax.set_xlim(0, 41)
    return f

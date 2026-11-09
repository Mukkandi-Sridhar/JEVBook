import json
import figstyle as fs
from figstyle import C

CC = json.loads((fs.ROOT / "research" / "m15-concurrency.json").read_text())


def fig_debounce():
    f, ax = fs.canvas(5.2, 1.6)
    x0, w = 1.25, 3.85                       # 9:00 to 9:35 across the axis
    t = lambda m: x0 + m / 35 * w
    saves = [2, 3, 5, 6, 7, 20, 21]
    for y, label in [(1.15, "Re-index on every save"), (0.55, "Wait for 5 quiet minutes")]:
        ax.text(0, y, label, fontsize=6.2, fontweight="bold", va="center")
        ax.plot([x0, x0 + w], [y, y], color=C["rule"], lw=0.6)
        for s in saves:
            ax.plot([t(s)], [y], marker="|", ms=9, mew=1.4, color=C["ink2"])
    for s in saves:
        fs.box(ax, t(s) + 0.02, 1.25, 0.14, 0.14, "", fc=C["crimson_t"], ec=C["crimson"], radius=0.02, lw=0.6)
    ax.text(t(22) + 0.1, 1.32, "7 rebuilds, two of them\nrunning at the same time", fontsize=5.6, va="center",
            color=C["crimson"])
    for s in [12, 26]:
        fs.box(ax, t(s), 0.65, 0.16, 0.14, "", fc=C["indigo_t"], ec=C["indigo"], radius=0.02, lw=0.6)
    ax.annotate("", xy=(t(12), 0.47), xytext=(t(7), 0.47),
                arrowprops=dict(arrowstyle="<->", color=C["indigo"], lw=0.7))
    ax.text(t(9.5), 0.38, "5 quiet minutes", ha="center", va="top", fontsize=5.6, color=C["indigo"])
    ax.text(t(27) + 0.1, 0.72, "2 rebuilds", fontsize=5.6, va="center", color=C["indigo"])
    for m in [0, 10, 20, 30]:
        ax.text(t(m), 0.12, f"9:{m:02d}", ha="center", fontsize=5.6, color=C["ink2"])
    ax.text(x0, 1.55, "|  an editor saves the policy", fontsize=5.6, color=C["ink2"])
    return f


def fig_concurrency():
    f, ax = fs.subplots(height=1.95)
    x = [r["concurrency"] for r in CC]
    y = [r["minutes"] for r in CC]
    ax.plot(x, y, color=C["indigo"], marker="o", ms=4)
    ax.set_xscale("log", base=2)
    ax.set_xticks(x, [str(v) for v in x])
    ax.axhline(2000 / 120, color=C["ink2"], lw=0.7, ls=(0, (3, 2)))
    ax.text(1.05, 3, "floor: at 120 requests a minute, 2,000 take at least 17 minutes", fontsize=5.8,
            color=C["ink2"])
    for r in CC:
        lab = f"{r['minutes'] / 60:.1f} h" if r["minutes"] > 60 else f"{r['minutes']:.0f} min"
        if r["refused"]:
            lab += f"\n{r['refused']:,}\nrefused"
        big = r["concurrency"] >= 8
        ax.annotate(lab, (r["concurrency"], r["minutes"]), xytext=(0, 10) if big else (5, 5),
                    textcoords="offset points", fontsize=5.6, ha="center" if big else "left",
                    color=C["crimson"] if r["refused"] > 1000 else C["ink2"])
    ax.set_ylim(0, 225)
    ax.set_xlim(0.8, 110)
    ax.set_xlabel("checks running at the same time")
    ax.set_ylabel("minutes for 2,000 checks")
    return f


def fig_where_it_goes():
    f, axes = fs.subplots(2, 1, height=1.75)
    time_parts = [("checks", 0.05), ("search", 0.09), ("rerank", 0.15), ("first word", 0.7), ("writing 300 tokens", 3.0)]
    cost_parts = [("system message", 0.455), ("policy chunks", 0.42), ("chat so far", 0.175), ("reply, 300 tokens", 0.51),
                  ("reranker", 0.02)]
    fills = [C["slate_t"], C["indigo_t"], C["plum_t"], C["saffron_t"], C["indigo"]]
    hatches = [None, "////", None, "\\\\\\\\", None]
    for ax, parts, unit, title in [(axes[0], time_parts, "s", "time: about 4 seconds"),
                                   (axes[1], cost_parts, "₹", "cost: about ₹1.58")]:
        left = 0
        total = sum(v for _, v in parts)
        for i, (k, v) in enumerate(parts):
            ax.barh(0, v / total * 100, left=left, height=0.6, color=fills[i], edgecolor="white", lw=1.5,
                    hatch=hatches[i])
            if v / total > 0.09:
                val = f"{v:.2f} s" if unit == "s" else f"₹{v:.2f}"
                ax.text(left + v / total * 50, 0, f"{k}\n{val}", ha="center", va="center", fontsize=5.6,
                        color="white" if fills[i] == C["indigo"] else C["ink"])
            left += v / total * 100
        ax.set_xlim(0, 100)
        ax.set_yticks([])
        ax.set_title(title, fontsize=6.8, loc="left", fontweight="bold")
        ax.grid(False)
        ax.spines["left"].set_visible(False)
        ax.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    axes[0].text(100, 0.36, "unlabelled at left: input checks, search, reranker", ha="right", va="bottom",
                 fontsize=5.4, color=C["ink2"])
    f.tight_layout(h_pad=1.6)
    return f

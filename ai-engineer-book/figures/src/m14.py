import json
import numpy as np
import figstyle as fs
from figstyle import C

CR = json.loads((fs.ROOT / "research" / "m14-crash.json").read_text())


def fig_crash_timeline():
    f, ax = fs.canvas(5.2, 1.55)
    L, x0 = 3.9, 1.15            # bar length for 2,000 items, left edge

    def seg(y, a, b, fc, ec, hatch=None):
        fs.box(ax, x0 + a * L, y, (b - a) * L, 0.22, "", fc=fc, ec=ec, hatch=hatch, radius=0.02, lw=0.6)

    def crash(x, y):
        ax.plot([x0 + x * L], [y + 0.11], marker="X", ms=7, color=C["crimson"], mec="white", mew=0.7)

    ax.text(0, 1.2, "Nothing saved", fontsize=6.4, fontweight="bold", va="center")
    seg(1.09, 0, 0.62, C["slate_t"], C["slate"], "////")
    crash(0.62, 1.09)
    ax.text(x0 + 0.31 * L, 1.36, "items 1 to 1,240: lost", ha="center", fontsize=5.6, color=C["crimson"])
    seg(0.79, 0, 0.45, C["indigo_t"], C["indigo"])
    ax.text(x0 + 0.47 * L, 0.9, "start again from item 1 ...", fontsize=5.6, va="center", color=C["ink2"])

    ax.text(0, 0.42, "Each item saved", fontsize=6.4, fontweight="bold", va="center")
    seg(0.31, 0, 0.62, C["indigo_t"], C["indigo"])
    crash(0.62, 0.31)
    seg(0.31, 0.62, 1.0, C["indigo_t"], C["indigo"])
    ax.text(x0 + 0.81 * L, 0.42, "resume at item 1,241", ha="center", va="center", fontsize=5.6)
    ax.plot([x0, x0 + L], [0.12, 0.12], color=C["rule"], lw=0.6)
    for v in [0, 500, 1000, 1500, 2000]:
        ax.text(x0 + v / 2000 * L, 0.02, f"{v:,}", ha="center", va="top", fontsize=5.6, color=C["ink2"])
    ax.text(x0 + L / 2, -0.14, "items handled", ha="center", va="top", fontsize=6.0, color=C["ink2"])
    return f


def fig_restart_cost():
    f, ax = fs.subplots(height=1.95)
    n = np.array(CR["sizes"])
    ax.plot(n, CR["restart"], color=C["crimson"], ls=fs.LINESTYLES[1], marker="s", ms=3.5)
    ax.plot(n, CR["resume"], color=C["indigo"], marker="o", ms=3.5)
    ax.set_yscale("log")
    ax.set_ylim(40, 60000)
    ax.set_yticks([100, 1000, 10000], ["100", "1,000", "10,000"])
    ax.set_xlim(0, 2250)
    ax.set_xticks([0, 500, 1000, 1500, 2000], ["0", "500", "1,000", "1,500", "2,000"])
    ax.text(2030, CR["restart"][-1], f"start again:\n{CR['restart'][-1]:,.0f}", va="center", fontsize=6.2,
            color=C["crimson"])
    ax.text(2030, CR["resume"][-1], f"resume:\n{CR['resume'][-1]:,.0f}", va="center", fontsize=6.2,
            color=C["indigo"])
    ax.set_xlabel("items in the job")
    ax.set_ylabel("items handled, on average")
    return f


def fig_plan_waves():
    f, ax = fs.canvas(5.2, 1.75)
    pos = {"export": (0, 1.05), "rules": (0, 0.35), "check": (1.38, 0.7), "letters": (2.76, 1.05),
           "totals": (2.76, 0.35), "review": (4.14, 0.7)}
    text = {"export": "export\nthe 2,000 requests", "rules": "rules\npolicy as a checklist",
            "check": "check\na verdict for each", "letters": "letters\none per wrong refusal",
            "totals": "totals\nfor finance", "review": "review\na person approves"}
    needs = {"check": ["export", "rules"], "letters": ["check"], "totals": ["check"], "review": ["letters", "totals"]}
    for w in range(4):
        fs.box(ax, w * 1.38 - 0.06, 0.18, 1.12, 1.43, "", fc=C["paper"] if w % 2 == 0 else "white",
               ec=C["paper"], radius=0.04)
        ax.text(w * 1.38 + 0.5, 1.68, f"wave {w + 1}", ha="center", fontsize=6.2, fontweight="bold",
                color=C["ink2"])
    for k, (x, y) in pos.items():
        fs.box(ax, x, y, 1.0, 0.36, text[k], size=5.6,
               fc=C["saffron_t"] if k == "review" else C["indigo_t"],
               ec=C["saffron"] if k == "review" else C["indigo"], radius=0.04)
    for k, ds in needs.items():
        for d in ds:
            (x1, y1), (x2, y2) = pos[d], pos[k]
            fs.arrow(ax, x1 + 1.0, y1 + 0.18, x2, y2 + 0.18, lw=0.7)
    return f


def fig_many_agents():
    f, ax = fs.canvas(5.2, 1.9)
    fs.box(ax, 0, 0.7, 1.2, 0.6, "Lead agent\nplans, then writes\nthe letters", size=6.0, fc=C["saffron_t"],
           ec=C["saffron"])
    for i in range(4):
        y = 1.5 - i * 0.45
        fs.box(ax, 1.95, y, 1.25, 0.34, f"Subagent {i + 1}\nreads requests {i * 500 + 1:,}-{(i + 1) * 500:,}",
               size=5.6, fc=C["indigo_t"], ec=C["indigo"], radius=0.04)
        fs.arrow(ax, 1.2, 1.0, 1.95, y + 0.17, lw=0.6)
        fs.arrow(ax, 3.2, y + 0.17, 3.7, y + 0.17, lw=0.6, color=C["muted"])
        ax.text(3.75, y + 0.17, "a short summary back", va="center", fontsize=5.5, color=C["ink2"])
    ax.text(0, 0.35, "Each subagent has its own context,\nso the lead never reads 2,000 requests.",
            fontsize=5.7, color=C["ink2"], va="top")
    ax.text(5.2, 0.0, "Many readers, one writer.", fontsize=6.2, fontweight="bold", ha="right")
    return f

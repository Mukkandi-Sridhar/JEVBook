import json
import numpy as np
import figstyle as fs
from figstyle import C

RS = json.loads((fs.ROOT / "research" / "m11-retry.json").read_text())


def _mini(ax, x, y, title, sub, draw):
    fs.box(ax, x, y, 1.62, 1.05, "", fc="white", ec=C["rule"], lw=0.7)
    ax.text(x + 0.08, y + 0.92, title, fontsize=6.4, fontweight="bold")
    ax.text(x + 0.08, y + 0.08, sub, fontsize=5.5, color=C["ink2"], va="bottom")
    draw(x, y)


def _node(ax, x, y, t, fc="white", ec=None, w=0.36):
    fs.box(ax, x, y, w, 0.2, t, size=5.4, fc=fc, ec=ec, radius=0.03)


def fig_workflows():
    f, ax = fs.canvas(5.2, 2.35)
    L = C["indigo_t"]

    def chain(x, y):
        for i in range(3):
            _node(ax, x + 0.1 + i * 0.5, y + 0.5, f"step {i + 1}", L, C["indigo"])
            if i < 2:
                fs.arrow(ax, x + 0.46 + i * 0.5, y + 0.6, x + 0.6 + i * 0.5, y + 0.6, lw=0.6)

    def route(x, y):
        _node(ax, x + 0.1, y + 0.5, "router", C["saffron_t"], C["saffron"])
        for j, t in enumerate(["refund", "delivery", "other"]):
            _node(ax, x + 0.85, y + 0.72 - j * 0.24, t, L, C["indigo"], w=0.5)
            fs.arrow(ax, x + 0.46, y + 0.6, x + 0.85, y + 0.82 - j * 0.24, lw=0.5)

    def parallel(x, y):
        _node(ax, x + 0.08, y + 0.5, "split", w=0.3)
        for j in range(3):
            _node(ax, x + 0.62, y + 0.72 - j * 0.24, f"part {j + 1}", L, C["indigo"])
            fs.arrow(ax, x + 0.38, y + 0.6, x + 0.62, y + 0.82 - j * 0.24, lw=0.5)
            fs.arrow(ax, x + 0.98, y + 0.82 - j * 0.24, x + 1.2, y + 0.6, lw=0.5)
        _node(ax, x + 1.2, y + 0.5, "join", w=0.3)

    def orch(x, y):
        _node(ax, x + 0.1, y + 0.5, "lead", C["saffron_t"], C["saffron"])
        for j in range(3):
            _node(ax, x + 0.85, y + 0.72 - j * 0.24, f"worker {j + 1}", L, C["indigo"], w=0.5)
            fs.arrow(ax, x + 0.46, y + 0.6, x + 0.85, y + 0.82 - j * 0.24, lw=0.5, style="<|-|>")

    def evalopt(x, y):
        _node(ax, x + 0.15, y + 0.5, "writer", L, C["indigo"], w=0.45)
        _node(ax, x + 0.95, y + 0.5, "checker", C["saffron_t"], C["saffron"], w=0.5)
        fs.arrow(ax, x + 0.6, y + 0.63, x + 0.95, y + 0.63, lw=0.6)
        fs.arrow(ax, x + 0.95, y + 0.55, x + 0.6, y + 0.55, lw=0.6)

    def agent(x, y):
        _node(ax, x + 0.55, y + 0.62, "model", C["saffron_t"], C["saffron"], w=0.5)
        _node(ax, x + 0.55, y + 0.3, "tools", L, C["indigo"], w=0.5)
        fs.arrow(ax, x + 0.6, y + 0.62, x + 0.6, y + 0.5, lw=0.6)
        fs.arrow(ax, x + 1.0, y + 0.5, x + 1.0, y + 0.62, lw=0.6)

    items = [("1  Chain", "fixed steps in order", chain), ("2  Route", "classify, then one path", route),
             ("3  Parallel", "independent parts at once", parallel),
             ("4  Orchestrator-workers", "a lead splits work", orch),
             ("5  Evaluator-optimiser", "write, check, rewrite", evalopt),
             ("Agent", "model picks every next step", agent)]
    for i, (t, s, d) in enumerate(items):
        x, y = (i % 3) * 1.79, 1.25 - (i // 3) * 1.2
        _mini(ax, x, y, t, s, d)
    return f


def fig_react_trace():
    f, ax = fs.canvas(5.2, 2.45)
    rows = [("Customer", "\"Can I return my earbuds from TK-5521? I opened them.\"", "white", C["rule"]),
            ("Decide", "I need the order first.  → check_order_status(\"TK-5521\")", C["saffron_t"], C["saffron"]),
            ("Look", "\"Delivered on 20 Oct.\"", C["indigo_t"], C["indigo"]),
            ("Decide", "Opened earbuds: check the policy.  → search_policy(\"return opened earbuds\")",
             C["saffron_t"], C["saffron"]),
            ("Look", "\"Hygiene products cannot be returned once opened, unless faulty.\"", C["indigo_t"],
             C["indigo"]),
            ("Decide", "Enough to answer. No tool.", C["saffron_t"], C["saffron"]),
            ("Reply", "\"Opened earbuds can be returned only if they are faulty. Are they?\"", "white", C["ink2"])]
    for i, (k, t, fc, ec) in enumerate(rows):
        y = 2.12 - i * 0.33
        ax.text(0.78, y + 0.12, k, ha="right", va="center", fontsize=6.4, fontweight="bold", color=ec)
        fs.box(ax, 0.86, y, 4.34, 0.25, t, size=5.9, ha="left", fc=fc, ec=ec, radius=0.03)
    return f


def fig_compound():
    f, ax = fs.subplots(height=1.95)
    n = np.arange(1, 21)
    for i, p in enumerate([0.99, 0.95, 0.9]):
        st = fs.SERIES[i]
        ax.plot(n, p ** n * 100, color=st["color"], ls=st["ls"], marker=st["marker"], ms=3, markevery=2)
        ax.text(20.4, p ** 20 * 100, f"{p:.0%} per step", va="center", fontsize=6.2, color=st["color"])
    ax.plot([10], [0.95 ** 10 * 100], "o", color=C["saffron"], ms=6, mfc="none", mew=1.4)
    ax.annotate("10 steps at 95%:\n60% of runs fully right", xy=(10, 59.9), xytext=(3.3, 22), fontsize=6.2,
                arrowprops=dict(arrowstyle="-", color=C["ink2"], lw=0.6))
    ax.set_xlim(0.5, 24.5)
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_ylim(0, 105)
    ax.set_yticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel("steps in the run")
    ax.set_ylabel("runs with every step right")
    return f


def fig_retry_storm():
    f, axes = fs.subplots(2, 1, height=2.4, sharex=True)
    t = np.arange(len(RS["fixed"]["load"])) / 10
    for ax, key, col, title in [(axes[0], "fixed", C["crimson"], "retry after exactly 1 second"),
                                (axes[1], "jitter", C["indigo"], "retry after a random wait that grows each time")]:
        r = RS[key]
        ax.bar(t, r["load"], width=0.1, color=col, align="edge")
        ax.axhline(50, color=C["ink2"], lw=0.8, ls=(0, (3, 2)))
        ax.set_ylim(0, 520)
        ax.set_yticks([0, 250, 500])
        ax.text(10.4, 470, f"{title}: {r['calls']:,} calls, all served by {r['last_done_s']:.1f} s",
                ha="right", va="top", fontsize=6.2, color=col)
        ax.grid(axis="x", visible=False)
    axes[0].text(10.4, 75, "the service handles 50 per 0.1 s", ha="right", fontsize=5.8, color=C["ink2"])
    axes[1].set_xlim(-0.2, 10.5)
    axes[1].set_xlabel("seconds after 500 requests arrive at once")
    f.text(0.0, 0.55, "requests arriving", rotation=90, va="center", fontsize=7, color=C["ink2"])
    f.tight_layout()
    return f


def fig_harness():
    f, ax = fs.canvas(5.2, 2.3)
    fs.box(ax, 2.05, 0.85, 1.1, 0.55, "The model", size=7.4, weight="bold", fc=C["saffron_t"], ec=C["saffron"])
    parts = [("System message", 3), ("Tools and their\ndescriptions", 5), ("Memory", 4), ("Context: what\nto send", 3),
             ("Step limits,\ntimeouts", 11), ("Retries and\nfallbacks", 11), ("Approvals", 12), ("Safety checks", 12),
             ("Traces and\ncosts", 16), ("Evals", 9)]
    cx, cy = 2.6, 1.12
    for i, (t, m) in enumerate(parts):
        a = 2 * np.pi * i / len(parts) + np.pi / 2
        x, y = cx + 2.1 * np.cos(a), cy + 0.92 * np.sin(a)
        fs.box(ax, x - 0.48, y - 0.17, 0.96, 0.34, t, size=5.6, fc=C["indigo_t"], ec=C["indigo"], radius=0.04)
        ax.text(x, y - 0.24, f"Module {m}", ha="center", va="top", fontsize=5.0, color=C["ink2"])
    return f

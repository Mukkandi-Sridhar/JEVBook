import json
import figstyle as fs
from figstyle import C

SK = json.loads((fs.ROOT / "research" / "m13-skills.json").read_text())
APPS = ["Support agent", "Staff assistant", "Seller agent"]
SYSTEMS = ["Orders", "Payments", "Couriers", "Policy docs"]


def _panel(ax, x0, title, sub):
    ax.text(x0, 2.25, title, fontsize=6.8, fontweight="bold", va="top")
    ax.text(x0, 2.07, sub, fontsize=5.8, color=C["ink2"], va="top")


def fig_n_by_m():
    f, ax = fs.canvas(5.2, 2.3)
    ya = [1.45, 0.95, 0.45]
    ys = [1.6, 1.15, 0.7, 0.25]
    _panel(ax, 0, "Without a standard", "every app wires every system itself: 3 × 4 = 12 connectors")
    for y in ya:
        fs.box(ax, 0, y - 0.13, 0.82, 0.26, APPS[ya.index(y)], size=5.6, fc=C["saffron_t"], ec=C["saffron"])
    for y in ys:
        fs.box(ax, 1.62, y - 0.12, 0.8, 0.24, SYSTEMS[ys.index(y)], size=5.6, fc=C["indigo_t"], ec=C["indigo"])
    for a in ya:
        for s in ys:
            ax.plot([0.82, 1.62], [a, s], color=C["crimson"], lw=0.6)
    x0 = 2.75
    _panel(ax, x0, "With MCP", "each app speaks MCP once, each system is wrapped once: 3 + 4 = 7")
    for y in ya:
        fs.box(ax, x0, y - 0.13, 0.82, 0.26, APPS[ya.index(y)], size=5.6, fc=C["saffron_t"], ec=C["saffron"])
        ax.plot([x0 + 0.82, x0 + 1.12], [y, y], color=C["indigo"], lw=0.8)
    fs.box(ax, x0 + 1.12, 0.2, 0.2, 1.52, "", fc=C["slate_t"], ec=C["slate"], radius=0.03)
    ax.text(x0 + 1.22, 0.96, "MCP", rotation=90, ha="center", va="center", fontsize=6.2, fontweight="bold")
    for y in ys:
        ax.plot([x0 + 1.32, x0 + 1.5], [y, y], color=C["indigo"], lw=0.8)
        fs.box(ax, x0 + 1.5, y - 0.12, 0.95, 0.24, SYSTEMS[ys.index(y)] + " server", size=5.4,
               fc=C["indigo_t"], ec=C["indigo"])
    return f


def fig_mcp_parts():
    f, ax = fs.canvas(5.2, 2.45)
    fs.box(ax, 0, 0.15, 1.95, 2.2, "", fc="white", ec=C["ink2"], radius=0.05)
    ax.text(0.1, 2.25, "Host: Tarkika's support app", fontsize=6.4, fontweight="bold", va="top")
    fs.box(ax, 0.15, 1.35, 0.7, 0.5, "Model", size=6.4, weight="bold", fc=C["saffron_t"], ec=C["saffron"])
    fs.box(ax, 1.05, 1.45, 0.78, 0.36, "MCP client 1", size=5.8, fc=C["indigo_t"], ec=C["indigo"])
    fs.box(ax, 1.05, 0.55, 0.78, 0.36, "MCP client 2", size=5.8, fc=C["indigo_t"], ec=C["indigo"])
    fs.arrow(ax, 0.85, 1.6, 1.05, 1.62, lw=0.6, style="<|-|>")
    fs.arrow(ax, 0.6, 1.35, 1.05, 0.75, lw=0.6, style="<|-|>")
    ax.text(0.1, 0.32, "one client for each server", fontsize=5.5, color=C["ink2"])

    def server(y, title, how, rows):
        fs.box(ax, 2.75, y, 2.42, 0.98, "", fc=C["slate_t"], ec=C["slate"], radius=0.04)
        ax.text(2.85, y + 0.9, title, fontsize=6.2, fontweight="bold", va="top")
        ax.text(2.85, y + 0.73, how, fontsize=5.4, color=C["ink2"], va="top")
        for i, (k, v) in enumerate(rows):
            ax.text(2.85, y + 0.5 - i * 0.15, k, fontsize=5.5, fontweight="bold", va="top")
            ax.text(3.55, y + 0.5 - i * 0.15, v, fontsize=5.5, va="top", family="IBM Plex Mono")

    server(1.37, "Server: tarkika-orders", "local: started by the host, talks over stdin and stdout",
           [("Tools", "check_order_status"), ("Resources", "policy://returns"), ("Prompts", "none")])
    server(0.15, "Server: payments", "remote: over HTTP, after the person signs in",
           [("Tools", "refund_status"), ("Resources", "none"), ("Prompts", "explain-refund")])
    fs.arrow(ax, 1.83, 1.63, 2.75, 1.86, lw=0.8, style="<|-|>")
    fs.arrow(ax, 1.83, 0.73, 2.75, 0.64, lw=0.8, style="<|-|>")
    ax.text(2.3, 1.84, "JSON-RPC", fontsize=5.3, color=C["ink2"], ha="center", rotation=14)
    ax.text(0, 0.02, "Who decides when each is used: the model picks tools, the app picks resources, and the person picks prompts.",
            fontsize=5.6, color=C["ink2"], va="top")
    return f


def fig_skill_levels():
    f, ax = fs.subplots(height=1.55)
    d = {r["part"]: r["tokens"] for r in SK if r["skill"] == "damaged-item-claim"}
    rows = [("menu", "1. Always in the request:\nname and description"),
            ("skill", "2. When a chat needs it:\nthe whole SKILL.md"),
            ("reference", "3. When a step needs it:\na reference file")]
    for i, (k, label) in enumerate(rows[::-1]):
        n = d[k]
        ax.barh(i, n, height=0.55, color=[C["indigo"], C["indigo_t"], C["slate_t"]][2 - i],
                edgecolor=C["indigo"], lw=0.6, hatch=None if k == "menu" else ("////" if k == "reference" else None))
        ax.text(n + 5, i, f"{n} tokens", va="center", fontsize=6.4, color=C["ink2"])
    ax.set_yticks(range(3), [r[1] for r in rows[::-1]], fontsize=6.4)
    ax.set_xlim(0, 330)
    ax.set_xlabel("tokens for the damaged-item skill (GPT-4o tokenizer)")
    ax.grid(axis="y", visible=False)
    return f

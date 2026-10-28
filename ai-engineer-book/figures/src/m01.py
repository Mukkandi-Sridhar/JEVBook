import figstyle as fs
from figstyle import C


def fig_two_halves():
    f, ax = fs.canvas(4.7, 2.25)
    # Model
    fs.box(ax, 0.0, 1.25, 1.55, 0.85, "", fc=C["saffron_t"], ec=C["saffron"])
    ax.text(0.77, 1.93, "THE MODEL", ha="center", fontsize=6.6, fontweight="bold", color=C["ink"])
    ax.text(0.1, 1.62, "can: understand language", fontsize=6.2, color=C["ink"])
    ax.text(0.1, 1.40, "cannot: act", fontsize=6.2, color=C["crimson"])
    # Tool
    fs.box(ax, 0.0, 0.15, 1.55, 0.85, "", fc=C["indigo_t"], ec=C["indigo"])
    ax.text(0.77, 0.83, "A TOOL (a function)", ha="center", fontsize=6.6, fontweight="bold", color=C["ink"])
    ax.text(0.1, 0.52, "can: act", fontsize=6.2, color=C["ink"])
    ax.text(0.1, 0.30, "cannot: understand language", fontsize=6.2, color=C["crimson"])
    ax.text(1.7, 1.15, "+", fontsize=16, ha="center", va="center", color=C["ink2"])
    fs.arrow(ax, 1.86, 1.15, 2.08, 1.15, lw=1.2)
    # Agent loop
    steps = [(2.15, 1.62, "1  Message:\n\"mera parcel kab aayega\""),
             (3.45, 1.62, "2  Model chooses a tool:\ncheck_order_status"),
             (3.45, 0.52, "3  Your program runs it\nfor TK-48213: \"out for delivery\""),
             (2.15, 0.52, "4  Model writes the reply")]
    for x, y, t in steps:
        fs.box(ax, x, y, 1.22, 0.48, t, size=5.6, ha="left")
    fs.arrow(ax, 3.37, 1.86, 3.45, 1.86)
    fs.arrow(ax, 4.06, 1.62, 4.06, 1.0)
    fs.arrow(ax, 3.45, 0.76, 3.37, 0.76)
    ax.text(3.41, 1.28, "AN AGENT", ha="center", va="center", fontsize=6.8, fontweight="bold", color=C["navy"])
    return f


def fig_system_map():
    f, ax = fs.canvas(4.7, 2.9)
    y0 = 1.55
    fs.box(ax, 0.0, y0, 0.55, 0.5, "Customer\nmessage", size=5.9)
    fs.box(ax, 0.68, y0, 0.62, 0.5, "Front door\n(16)", size=5.9)
    fs.box(ax, 1.43, y0, 0.62, 0.5, "Safety in\n(12)", fc=C["crimson_t"], ec=C["crimson"], size=5.9)
    fs.box(ax, 2.18, y0 - 0.05, 0.82, 0.6, "Control\nworkflow, agent,\nplan (11, 14)", fc=C["slate_t"],
           ec=C["slate"], size=5.7, weight="bold")
    fs.box(ax, 3.13, y0, 0.62, 0.5, "Safety out\n(12)", fc=C["crimson_t"], ec=C["crimson"], size=5.9)
    fs.box(ax, 3.88, y0, 0.62, 0.5, "Reply or\naction", size=5.9)
    for x1, x2 in [(0.55, 0.68), (1.30, 1.43), (2.05, 2.18), (3.0, 3.13), (3.75, 3.88)]:
        fs.arrow(ax, x1, y0 + 0.25, x2, y0 + 0.25)
    # Around control
    fs.box(ax, 1.25, 2.38, 0.8, 0.42, "Context\n(3, 4, 6–8)", fc=C["indigo_t"], ec=C["indigo"], size=5.9)
    fs.box(ax, 2.18, 2.38, 0.82, 0.42, "The model\n(2, 10)", fc=C["saffron_t"], ec=C["saffron"], size=6.2,
           weight="bold")
    fs.box(ax, 3.13, 2.38, 0.8, 0.42, "Tools, MCP\n(5, 13)", fc=C["indigo_t"], ec=C["indigo"], size=5.9)
    fs.arrow(ax, 2.59, 2.1, 2.59, 2.38, style="<|-|>")
    fs.arrow(ax, 2.3, 2.1, 1.75, 2.38, style="<|-|>")
    fs.arrow(ax, 2.88, 2.1, 3.43, 2.38, style="<|-|>")
    # Watching band
    fs.box(ax, 0.0, 0.55, 4.5, 0.62, "", fc=C["paper"], ec=C["ink2"])
    ax.text(2.25, 1.03, "WATCHING EVERYTHING", ha="center", fontsize=6.0, fontweight="bold", color=C["ink2"])
    items = ["Tests and evals (9)", "Traces (16)", "Cost and caching (15)", "Versions and releases (16)"]
    for i, t in enumerate(items):
        ax.text(0.56 + i * 1.12, 0.74, t, fontsize=5.6, color=C["ink"], ha="center")
    fs.arrow(ax, 2.25, 1.17, 2.25, 1.5, style="-", ls=(0, (2, 2)), color=C["rule"])
    return f

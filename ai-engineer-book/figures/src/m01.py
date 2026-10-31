import figstyle as fs
from figstyle import C
from matplotlib.patches import Circle


def _card(ax, x, y, w, h, title, can, cannot, fc, ec):
    fs.box(ax, x, y, w, h, "", fc=fc, ec=ec, lw=1.1)
    ax.text(x + w / 2, y + h - 0.17, title, ha="center", va="center", fontsize=7.6, fontweight="bold",
            color=C["ink"])
    ax.text(x + 0.14, y + h - 0.45, "can:  " + can, fontsize=7.0, va="center", color=C["ink"])
    ax.text(x + 0.14, y + h - 0.7, "cannot:  " + cannot, fontsize=7.0, va="center", color=C["crimson"],
            fontweight="bold")


def fig_two_halves():
    f, ax = fs.canvas(5.4, 2.5)
    _card(ax, 0.0, 1.35, 1.75, 0.95, "THE MODEL", "understand language", "act", C["saffron_t"], C["saffron"])
    _card(ax, 0.0, 0.15, 1.75, 0.95, "A TOOL (a function)", "act", "understand language", C["indigo_t"],
          C["indigo"])
    ax.text(1.98, 1.22, "+", fontsize=20, ha="center", va="center", color=C["ink2"])
    fs.arrow(ax, 2.13, 1.22, 2.4, 1.22, lw=1.6)
    # The agent loop: four steps around a centre
    ax.add_patch(Circle((3.9, 1.22), 0.34, fc=C["navy"], ec="none"))
    ax.text(3.9, 1.22, "AGENT", ha="center", va="center", fontsize=7.4, fontweight="bold", color="white")
    steps = [(2.45, 1.72, "1  Customer writes\n\"mera parcel kab aayega?\""),
             (4.05, 1.72, "2  Model picks a tool:\ncheck_order_status"),
             (4.05, 0.22, "3  Your program runs it:\n\"out for delivery\""),
             (2.45, 0.22, "4  Model writes the reply:\n\"Your parcel arrives today\"")]
    for x, y, t in steps:
        fs.box(ax, x, y, 1.35, 0.55, t, size=6.4, ha="left", fc="white")
    fs.arrow(ax, 3.8, 2.0, 4.05, 2.0, lw=1.1)
    fs.arrow(ax, 4.72, 1.72, 4.72, 0.77, lw=1.1)
    fs.arrow(ax, 4.05, 0.5, 3.8, 0.5, lw=1.1)
    fs.arrow(ax, 3.12, 0.77, 3.12, 1.72, lw=1.1, ls=(0, (3, 2)))
    ax.text(3.06, 1.22, "next\nmessage", ha="right", va="center", fontsize=5.8, color=C["ink2"])
    return f


def fig_system_map():
    f, ax = fs.canvas(5.2, 3.15)
    w, h, gap, y0 = 0.74, 0.58, 0.155, 1.5
    row = [("Customer\nmessage", "white", None, ""),
           ("Front door", "white", None, "16"),
           ("Safety in", C["crimson_t"], C["crimson"], "12"),
           ("Control", C["slate_t"], C["slate"], "11, 14"),
           ("Safety out", C["crimson_t"], C["crimson"], "12"),
           ("Reply or\naction", "white", None, "")]
    xs = []
    for i, (t, fc, ec, mod) in enumerate(row):
        x = i * (w + gap)
        xs.append(x)
        fs.box(ax, x, y0, w, h, t, fc=fc, ec=ec, size=7.0, weight="bold" if t == "Control" else "normal",
               lw=1.0)
        if mod:
            ax.text(x + w / 2, y0 - 0.12, "Module " + mod, ha="center", fontsize=6.0, color=C["ink2"])
        if i < len(row) - 1:
            fs.arrow(ax, x + w, y0 + h / 2, x + w + gap, y0 + h / 2, lw=1.0)
    cx = xs[3] + w / 2
    top = [("Context", C["indigo_t"], C["indigo"], "3, 4, 6–8", cx - 1.42),
           ("The model", C["saffron_t"], C["saffron"], "2, 10", cx - 0.42),
           ("Tools, MCP", C["indigo_t"], C["indigo"], "5, 13", cx + 0.58)]
    for t, fc, ec, mod, x in top:
        fs.box(ax, x, 2.45, 0.84 if t != "The model" else 0.84, 0.5, t, fc=fc, ec=ec, size=7.0,
               weight="bold" if t == "The model" else "normal", lw=1.0)
        ax.text(x + 0.42, 3.05, "Module " + mod, ha="center", fontsize=6.0, color=C["ink2"])
        fs.arrow(ax, x + 0.42, 2.45, cx + (x + 0.42 - cx) * 0.25, y0 + h, style="<|-|>", lw=0.9)
    fs.box(ax, 0.0, 0.18, 5.2, 0.85, "", fc=C["paper"], ec=C["ink2"], lw=0.9)
    ax.text(2.6, 0.86, "WATCHING EVERYTHING", ha="center", fontsize=6.8, fontweight="bold", color=C["ink2"])
    items = [("Tests and evals", "9"), ("Traces", "16"), ("Cost and caching", "15"), ("Versions, releases", "16")]
    for i, (t, m) in enumerate(items):
        x = 0.65 + i * 1.3
        ax.text(x, 0.55, t, ha="center", fontsize=7.0, color=C["ink"])
        ax.text(x, 0.33, "Module " + m, ha="center", fontsize=6.0, color=C["ink2"])
    return f

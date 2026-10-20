import figstyle as fs
from figstyle import C


def fig_system():
    f, ax = fs.canvas(4.7, 2.75)
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((0.62, 0.12), 3.46, 2.45, boxstyle="round,pad=0,rounding_size=0.08", fc="none",
                                ec=C["teal"], lw=1.0, ls=(0, (4, 2))))
    ax.text(0.72, 2.45, "THE AI SYSTEM: WHAT THE AI ENGINEER BUILDS", fontsize=6.2, fontweight="bold", color=C["teal"],
            va="center")
    top = ["Instructions\nand context", "Knowledge\n(policies, orders)", "Tools\n(look up, refund)"]
    bot = ["Tests\n(is it right?)", "Guardrails\n(what it must not do)", "Cost and speed\n(the bill, the wait)"]
    for i, t in enumerate(top):
        fs.box(ax, 0.8 + i * 1.07, 1.72, 0.98, 0.52, t, fc=C["blue_t"], ec=C["blue"], size=6.6)
    for i, t in enumerate(bot):
        fs.box(ax, 0.8 + i * 1.07, 0.3, 0.98, 0.52, t, fc=C["grey_t"], ec=C["ink2"], size=6.6)
    fs.box(ax, 1.55, 1.04, 1.6, 0.46, "The model (LLM)", fc=C["orange_t"], ec=C["orange"], size=7.6, weight="bold")
    fs.box(ax, 0.0, 1.04, 0.5, 0.46, "Customer\nmessage", fc="white", size=6.2)
    fs.box(ax, 4.2, 1.04, 0.5, 0.46, "Reply or\naction", fc="white", size=6.2)
    fs.arrow(ax, 0.5, 1.27, 1.55, 1.27)
    fs.arrow(ax, 3.15, 1.27, 4.2, 1.27)
    for i in range(3):
        x = 0.8 + i * 1.07 + 0.49
        fs.arrow(ax, x, 1.72, min(max(x, 1.7), 3.0), 1.5, style="-", color=C["rule"], lw=0.7)
        fs.arrow(ax, x, 0.82, min(max(x, 1.7), 3.0), 1.04, style="-", color=C["rule"], lw=0.7)
    return f


def fig_project():
    f, ax = fs.canvas(4.7, 2.9)
    fs.box(ax, 0.0, 1.55, 0.72, 0.62, "Customer\nmessage\n(English, Hindi,\nHinglish)", size=5.9)
    fs.box(ax, 0.92, 1.6, 0.72, 0.52, "Sort it\n(type, language,\nurgency)", fc=C["teal_t"], ec=C["teal"], size=5.9)
    fs.arrow(ax, 0.72, 1.86, 0.92, 1.86)
    rows = [(2.38, "Answer from policy\ndocuments", C["blue_t"], C["blue"]),
            (1.6, "Look up the order\n(tool)", C["blue_t"], C["blue"]),
            (0.82, "Prepare a refund\n(tool)", C["blue_t"], C["blue"])]
    for y, t, fc, ec in rows:
        fs.box(ax, 1.86, y, 0.92, 0.5, t, fc=fc, ec=ec, size=5.9)
        fs.arrow(ax, 1.64, 1.86, 1.86, y + 0.25)
    fs.box(ax, 2.98, 0.82, 0.66, 0.5, "Above\n₹2,000?", fc=C["purple_t"], ec=C["purple"], size=5.9)
    fs.arrow(ax, 2.78, 1.07, 2.98, 1.07)
    fs.box(ax, 2.98, 0.2, 0.66, 0.44, "", fc=C["purple_t"], ec=C["purple"], hatch="////")
    ax.text(3.31, 0.42, "A person\napproves", ha="center", va="center", fontsize=5.9, bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))
    fs.arrow(ax, 3.31, 0.82, 3.31, 0.64)
    ax.text(3.36, 0.73, "yes", fontsize=5.6, color=C["ink2"])
    fs.box(ax, 3.92, 1.55, 0.78, 0.62, "Reply to\nthe customer", fc="white", size=6.2, weight="bold")
    fs.arrow(ax, 2.78, 2.63, 3.92, 1.98)
    fs.arrow(ax, 2.78, 1.85, 3.92, 1.86)
    fs.arrow(ax, 3.64, 1.07, 3.92, 1.7)
    ax.text(3.82, 1.28, "no", fontsize=5.6, color=C["ink2"])
    fs.arrow(ax, 3.64, 0.42, 4.3, 0.42, style="-")
    fs.arrow(ax, 4.3, 0.42, 4.3, 1.55)
    fs.box(ax, 0.0, -0.22, 4.7, 0.3, "Watching everything: guardrails  ·  tests  ·  logs  ·  cost and speed tracking",
           fc=C["grey_t"], ec=C["ink2"], size=6.2)
    return f

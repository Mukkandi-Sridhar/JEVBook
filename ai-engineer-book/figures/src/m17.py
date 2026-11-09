import figstyle as fs
from figstyle import C


def _stage(ax, x, y, w, h, title, detail, mod, fc, ec, bold=False):
    fs.box(ax, x, y, w, h, "", fc=fc, ec=ec, lw=0.9, radius=0.04)
    ax.text(x + w / 2, y + h - 0.07, title, ha="center", va="top", fontsize=6.4, fontweight="bold")
    ax.text(x + w / 2, y + h - 0.24, detail, ha="center", va="top", fontsize=5.2, color=C["ink2"], linespacing=1.2)
    ax.text(x + w / 2, y - 0.05, mod, ha="center", va="top", fontsize=5.3, color=C["ink2"])


def fig_system_design():
    f, ax = fs.canvas(5.2, 3.55)
    w, h, gap, y0 = 0.96, 0.82, 0.1, 1.42
    row = [("Front door", "sign-in, 20 messages\na minute, size limit", "Module 16", "white", C["ink2"]),
           ("Safety in", "Aadhaar and card\ndetectors: mask\nor block", "Module 12", C["crimson_t"], C["crimson"]),
           ("Control", "router: tracking goes\nto a workflow, the\nrest to the agent", "Modules 10, 11", C["slate_t"],
            C["slate"]),
           ("Safety out", "promises, other\ncustomers' orders,\nsources checked", "Module 12", C["crimson_t"],
            C["crimson"]),
           ("Reply", "streamed; or a\nhandover with a\nsummary", "", "white", C["ink2"])]
    xs = []
    for i, (t, d, m, fc, ec) in enumerate(row):
        x = i * (w + gap) + 0.07
        xs.append(x)
        _stage(ax, x, y0, w, h, t, d, m, fc, ec)
        if i < len(row) - 1:
            fs.arrow(ax, x + w, y0 + h / 2, x + w + gap, y0 + h / 2, lw=0.9)
    cx = xs[2] + w / 2
    top = [("Context", "system message v7,\nthread memory, hybrid\nsearch and reranker", "Modules 3, 4, 6-8",
            C["indigo_t"], C["indigo"], cx - 1.72),
           ("The model", "a mid-size model;\na small one for\nconfident easy cases", "Modules 2, 10", C["saffron_t"],
            C["saffron"], cx - 0.525),
           ("Tools", "orders server (MCP);\nrefunds checked in code,\nover ₹2,000 to a person", "Modules 5, 12, 13",
            C["indigo_t"], C["indigo"], cx + 0.67)]
    for t, d, m, fc, ec, x in top:
        _stage(ax, x, 2.5, 1.05, 0.82, t, d, "", fc, ec)
        ax.text(x + 0.525, 3.42, m, ha="center", fontsize=5.3, color=C["ink2"])
        fs.arrow(ax, x + 0.525, 2.5, cx + (x + 0.525 - cx) * 0.3, y0 + h, style="<|-|>", lw=0.8)
    fs.box(ax, 0.07, 0.08, 5.2 - 0.07, 0.95, "", fc=C["paper"], ec=C["ink2"], lw=0.8)
    ax.text(2.63, 0.93, "WATCHING EVERYTHING", ha="center", va="top", fontsize=6.2, fontweight="bold",
            color=C["ink2"])
    items = [("Evals", "120 golden questions,\n60 attacks, every release", "9, 12"),
             ("Traces", "version record\non every reply", "16"),
             ("Cost", "cache, batch,\ncost per resolved chat", "15"),
             ("Releases", "shadow, canary,\none-switch rollback", "16")]
    for i, (t, d, m) in enumerate(items):
        x = 0.72 + i * 1.3
        ax.text(x, 0.7, t, ha="center", fontsize=6.2, fontweight="bold")
        ax.text(x, 0.55, d, ha="center", va="top", fontsize=5.2, color=C["ink2"], linespacing=1.2)
        ax.text(x, 0.22, "Module " + m, ha="center", va="top", fontsize=5.0, color=C["muted"])
    return f


def fig_voice_budget():
    f, ax = fs.subplots(height=1.7)
    stages = [("caller stops; turn detected", 250), ("speech to text: last words", 150),
              ("model: first words of the reply", 400), ("text to speech: first sound", 150),
              ("network, both ways", 100)]
    left = 0
    cols = [C["slate_t"], C["indigo_t"], C["saffron_t"], C["indigo_t"], C["slate_t"]]
    for i, (k, ms) in enumerate(stages):
        y = len(stages) - 1 - i
        ax.barh(y, ms, left=left, height=0.6, color=cols[i], edgecolor=C["ink2"], lw=0.5,
                hatch="////" if i in (0, 4) else None)
        ax.text(left + ms + 15, y, f"{ms} ms", va="center", fontsize=6.0, color=C["ink2"])
        left += ms
    ax.axvline(left, color=C["crimson"], lw=0.8, ls=(0, (3, 2)))
    ax.text(left + 15, 4.35, f"total: {left:,} ms", fontsize=6.2, color=C["crimson"], fontweight="bold")
    ax.set_yticks(range(len(stages)), [s[0] for s in stages][::-1], fontsize=6.2)
    ax.set_xlim(0, 1300)
    ax.set_xticks([0, 250, 500, 750, 1000, 1250], ["0", "250", "500", "750", "1,000", "1,250"])
    ax.set_xlabel("milliseconds after the caller stops speaking (a budget, not a measurement)")
    ax.grid(axis="y", visible=False)
    return f

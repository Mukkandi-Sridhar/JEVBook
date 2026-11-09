import json
import figstyle as fs
from figstyle import C

N = json.loads((fs.ROOT / "research" / "m16-numbers.json").read_text())


def fig_service_layout():
    f, ax = fs.canvas(5.2, 2.5)
    I, IT, S, ST = C["indigo"], C["indigo_t"], C["saffron"], C["saffron_t"]
    fs.box(ax, 0, 1.05, 0.62, 0.5, "Customer's\napp", size=5.8)
    fs.box(ax, 0.82, 0.95, 0.9, 0.7, "Front door\nsign-in, rate limits,\nsize limits", size=5.6, fc=C["slate_t"],
           ec=C["slate"])
    fs.box(ax, 1.95, 0.95, 1.0, 0.7, "Chat service\nmany identical copies,\nno state of their own", size=5.6,
           fc=IT, ec=I)
    fs.box(ax, 3.25, 1.6, 0.95, 0.55, "Model gateway\nkeys, retries,\nfallbacks, costs", size=5.6, fc=ST, ec=S)
    fs.box(ax, 4.45, 1.85, 0.75, 0.3, "Provider A", size=5.6)
    fs.box(ax, 4.45, 1.45, 0.75, 0.3, "Provider B", size=5.6)
    fs.box(ax, 3.25, 0.85, 0.95, 0.5, "Tools and\nsearch (MCP)", size=5.6, fc=IT, ec=I)
    fs.box(ax, 1.95, 0.1, 1.0, 0.5, "Queue\nfor long jobs", size=5.6, fc=C["slate_t"], ec=C["slate"])
    fs.box(ax, 3.25, 0.1, 0.95, 0.5, "Workers\n(Module 14)", size=5.6, fc=IT, ec=I)
    fs.box(ax, 0, 0.1, 1.72, 0.5, "Threads, task store,\ntraces, version records", size=5.6, fc="white",
           ec=C["rule"])
    for a in [((0.62, 1.3), (0.82, 1.3)), ((1.72, 1.3), (1.95, 1.3)), ((2.95, 1.5), (3.25, 1.85)),
              ((2.95, 1.15), (3.25, 1.1)), ((2.45, 0.95), (2.45, 0.6)), ((2.95, 0.35), (3.25, 0.35)),
              ((4.2, 1.95), (4.45, 2.0)), ((4.2, 1.75), (4.45, 1.6))]:
        fs.arrow(ax, *a[0], *a[1], lw=0.7)
    fs.arrow(ax, 1.95, 1.05, 1.72, 0.55, lw=0.6, color=C["muted"], ls=(0, (2, 2)))
    ax.text(0.68, 1.75, "replies stream back word by word", fontsize=5.5, color=C["ink2"])
    ax.text(5.2, 2.42, "every arrow has a timeout", fontsize=5.6, color=C["ink2"], ha="right", va="top",
            style="italic")
    return f


def fig_release_ladder():
    f, ax = fs.canvas(5.2, 1.45)
    steps = [("Offline evals", "golden set and\nattack set pass"), ("Shadow", "runs on real traffic;\nanswers not shown"),
             ("Canary 5%", "real customers;\nwatch the numbers"), ("25%", "still watching"), ("100%", "old version\nkept ready")]
    w, gap = 0.9, 0.17
    for i, (t, s) in enumerate(steps):
        x = i * (w + gap)
        fs.box(ax, x, 0.62, w, 0.5, "", fc=C["indigo_t"] if i else C["slate_t"], ec=C["indigo"] if i else C["slate"],
               radius=0.04)
        ax.text(x + w / 2, 1.02, t, ha="center", va="top", fontsize=6.0, fontweight="bold")
        ax.text(x + w / 2, 0.84, s, ha="center", va="top", fontsize=5.3, color=C["ink2"], linespacing=1.2)
        if i < len(steps) - 1:
            fs.arrow(ax, x + w, 0.87, x + w + gap, 0.87, lw=0.8)
    ax.annotate("", xy=(0.45, 0.6), xytext=(4.75, 0.6),
                arrowprops=dict(arrowstyle="-|>", color=C["crimson"], lw=0.8, ls=(0, (3, 2)),
                                connectionstyle="arc3,rad=-0.12"))
    ax.text(2.6, 0.1, "any number worse than its limit: one switch back to the old version", ha="center",
            fontsize=5.8, color=C["crimson"])
    return f


def fig_finetune_memory():
    f, ax = fs.subplots(height=1.55)
    m = N["memory"]
    rows = [("QLoRA: 4-bit model, train adapters", m["qlora"]), ("LoRA: frozen model, train adapters", m["lora"]),
            ("Full fine-tuning", m["full"])]
    for i, (k, v) in enumerate(rows):
        ax.barh(i, v, height=0.55, color=[C["indigo"], C["indigo_t"], C["crimson_t"]][i],
                edgecolor=[C["indigo"], C["indigo"], C["crimson"]][i], lw=0.6, hatch="////" if i == 2 else None)
        ax.text(v + 2, i, f"{v:.0f} GB", va="center", fontsize=6.4, color=C["ink2"])
    for g in [24, 80]:
        ax.axvline(g, color=C["ink2"], lw=0.7, ls=(0, (3, 2)))
        ax.text(g + 1, 2.45, f"one {g} GB GPU", fontsize=5.6, color=C["ink2"])
    ax.set_yticks(range(3), [r[0] for r in rows], fontsize=6.3)
    ax.set_xlim(0, 150)
    ax.set_ylim(-0.5, 2.7)
    ax.set_xlabel("memory for an 8-billion-parameter model, before working memory (GB)")
    ax.grid(axis="y", visible=False)
    return f


def fig_crossover():
    f, ax = fs.subplots(height=1.9)
    c = N["cost"]
    x = [d / 1000 for d in c["per_day"]]
    ax.plot(x, [v / 1e5 for v in c["api"]], color=C["saffron"], lw=1.6)
    ax.plot(x, [v / 1e5 for v in c["own"]], color=C["indigo"], lw=1.6, ls=fs.LINESTYLES[1], drawstyle="steps-post")
    ax.text(41, 15.2, "API", color=C["saffron"], fontsize=6.4, fontweight="bold")
    ax.text(41, 5.6, "own GPUs", color=C["indigo"], fontsize=6.4, fontweight="bold")
    cr = N["crossover"] / 1000
    ax.axvline(cr, color=C["ink2"], lw=0.6, ls=(0, (2, 2)))
    ax.text(cr + 0.6, 16.4, f"equal near {N['crossover']:,} a day", fontsize=6.0, color=C["ink2"])
    for d, lab in [(4, "a normal day"), (40, "festival week")]:
        ax.axvline(d, color=C["muted"], lw=0.5, ls=(0, (1, 2)))
        ax.text(d, 18.2, lab, fontsize=5.8, ha="center", color=C["ink2"])
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 19)
    ax.set_xlabel("messages a day (thousands)")
    ax.set_ylabel("cost a month (₹ lakh)")
    return f

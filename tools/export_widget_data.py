"""Write site/data.js: the synthetic data the companion-site widgets use.

    python tools/export_widget_data.py

Everything exported is synthetic (Kestrel's generated alerts, mock-Jev probabilities, the book's bake-off results).
"""
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

import sys  # noqa: E402
sys.path.insert(0, str(ROOT))
from jevkit import soc, calibration as cal, econ  # noqa: E402
from jevkit.batch import score_alerts  # noqa: E402


def main():
    A = soc.load()
    A["p"] = score_alerts(A)
    H, L = soc.history_and_live(A)
    platt = cal.Platt().fit(H.p.to_numpy(), H.malicious.to_numpy())
    live = dict(p_raw=np.round(L.p.to_numpy(), 5).tolist(), p=np.round(platt(L.p.to_numpy()), 5).tolist(),
                y=L.malicious.astype(int).tolist(), days=7)
    # Harbor Pharma (Chapter 18): the same mock at a company with a lower base rate
    Hb = soc.to_frame(soc.generate(n=4000, seed=21, logit_shift={r: -1.3 for r in soc.RULES}))
    harbor = dict(p=np.round(score_alerts(Hb), 5).tolist(), y=Hb.malicious.astype(int).tolist())
    ch20 = json.loads((ROOT / "results" / "ch20.json").read_text())
    methods = ["rules", "logistic", "text_clf", "llm_json", "llm_judge", "jev"]
    bake = {m: {k: ch20.get(f"{m}_{k}") for k in ("auc", "ece", "brier", "caught")} for m in methods}
    bake["_cost_m"] = dict(rules=0.3, logistic=0.5, text_clf=1.0, llm_json=ch20["llm_json_cost_m"],
                           llm_judge=ch20["llm_judge_cost_m"], jev=ch20["jev_cost_m"])
    bake["_latency_s"] = dict(rules=1e-6, logistic=1e-5, text_clf=1e-4, llm_json=ch20["llm_json_latency"],
                              llm_judge=ch20["llm_judge_latency"], jev=(econ.JEV_LATENCY[0] * econ.JEV_LATENCY[1]) ** 0.5)
    prices = dict(jev_in_per_m=econ.JEV_PRICE_IN_PER_M, llm_in_per_m=1.0, llm_out_per_m=4.0,
                  jev_latency=list(econ.JEV_LATENCY), llm_latency=econ.LLM_LATENCY)
    data = dict(live=live, harbor=harbor, bakeoff=bake, prices=prices,
                note="Synthetic: generated alerts and jev-mock-synthetic probabilities. Not measured on real Jev.")
    out = ROOT / "site" / "data.js"
    out.parent.mkdir(exist_ok=True)
    out.write_text("window.BOOK_DATA = " + json.dumps(data, separators=(",", ":")) + ";\n")
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()

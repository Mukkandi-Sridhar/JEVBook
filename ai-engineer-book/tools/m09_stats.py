"""Numbers for Module 9: score spread at n=50, a paired comparison, retrieval metrics, pass^k."""
import json, math
from pathlib import Path
import numpy as np

rng = np.random.default_rng(7)
res = {}
# 1. Same system (true accuracy 80%), scored on 50 random questions, 10,000 times
sims = rng.binomial(50, 0.8, size=10000) / 50
vals, counts = np.unique(sims, return_counts=True)
res["spread"] = {"values": vals.round(2).tolist(), "counts": counts.tolist(),
                 "p05": float(np.percentile(sims, 5)), "p95": float(np.percentile(sims, 95)),
                 "share_at_or_below_74": float((sims <= 0.74).mean()), "share_at_or_above_86": float((sims >= 0.86).mean())}
for n in [50, 200, 1000]:
    s = rng.binomial(n, 0.8, size=10000) / n
    res[f"range90_n{n}"] = [float(np.percentile(s, 5)), float(np.percentile(s, 95))]
# 2. Paired comparison: v2 fixes 5, breaks 2. Two-sided sign test on the 7 flips.
k, n = 2, 7
p = 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
res["sign_test_5_vs_2"] = round(p, 3)
k, n = 3, 17   # fixes 14, breaks 3
res["sign_test_14_vs_3"] = round(2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n, 4)
# 3. Retrieval metrics on three questions
qs = [({"s3"}, ["s3", "s1", "s4", "s2", "s5"]), ({"s3", "s4"}, ["s1", "s4", "s2", "s3", "s5"]),
      ({"s5"}, ["s1", "s2", "s4", "s3", "s6"])]
hits, rr = [], []
for rel, ranked in qs:
    first = next((i + 1 for i, d in enumerate(ranked) if d in rel), None)
    hits.append(1 if first else 0)
    rr.append(1 / first if first else 0)
rel, ranked = qs[1]
dcg = sum(1 / math.log2(i + 2) for i, d in enumerate(ranked) if d in rel)
idcg = sum(1 / math.log2(i + 2) for i in range(len(rel)))
res["retrieval"] = {"hit_rate": sum(hits) / 3, "rr": rr, "mrr": sum(rr) / 3,
                    "q2_precision_at_5": 2 / 5, "q2_recall_at_3": 1 / 2, "q2_recall_at_5": 1.0,
                    "q2_dcg": round(dcg, 3), "q2_idcg": round(idcg, 3), "q2_ndcg": round(dcg / idcg, 3)}
# 4. pass^k
res["pass_k"] = {str(p): [round(p ** k, 3) for k in range(1, 11)] for p in [0.95, 0.9, 0.8]}
Path(__file__).resolve().parents[1].joinpath("research/m09-stats.json").write_text(json.dumps(res, indent=1))
print(json.dumps({k: v for k, v in res.items() if k != "spread"}, indent=1))
print({k: v for k, v in res["spread"].items() if k not in ("values", "counts")})

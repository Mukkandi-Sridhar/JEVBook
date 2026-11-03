"""Time brute-force vs HNSW search on 1,000,000 synthetic 384-number vectors (Module 6)."""
import json, time
from pathlib import Path
import numpy as np, hnswlib

rng = np.random.default_rng(0)
N, D, Q, K = 1_000_000, 384, 200, 10
latent = rng.standard_normal((N, 48)).astype(np.float32)
proj = rng.standard_normal((48, D)).astype(np.float32)
X = latent @ proj + 0.3 * rng.standard_normal((N, D)).astype(np.float32)
X /= np.linalg.norm(X, axis=1, keepdims=True)
qs = X[rng.choice(N, Q, replace=False)] + 0.05 * rng.standard_normal((Q, D)).astype(np.float32)
qs /= np.linalg.norm(qs, axis=1, keepdims=True)

t = time.perf_counter(); truth = []
for q in qs:
    s = X @ q
    truth.append(set(np.argpartition(-s, K)[:K]))
flat_ms = (time.perf_counter() - t) / Q * 1000

idx = hnswlib.Index(space="cosine", dim=D)
t = time.perf_counter()
idx.init_index(max_elements=N, M=16, ef_construction=100)
idx.add_items(X, num_threads=4)
build_s = time.perf_counter() - t
res = {"N": N, "D": D, "flat_ms_per_query": round(flat_ms, 1), "hnsw_build_seconds": round(build_s), "hnsw": []}
idx.set_num_threads(1)
for ef in [20, 50, 100, 200]:
    idx.set_ef(ef)
    t = time.perf_counter()
    labels, _ = idx.knn_query(qs, k=K)
    ms = (time.perf_counter() - t) / Q * 1000
    rec = np.mean([len(set(l) & tr) / K for l, tr in zip(labels, truth)])
    res["hnsw"].append({"ef": ef, "ms_per_query": round(ms, 3), "recall_at_10": round(float(rec), 3)})
print(json.dumps(res, indent=1))
Path(__file__).resolve().parents[1].joinpath("research/m06-ann.json").write_text(json.dumps(res, indent=1))

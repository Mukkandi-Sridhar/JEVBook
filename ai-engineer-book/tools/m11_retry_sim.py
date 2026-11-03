"""Retry storm: 500 requests hit a service that can handle 50 per 100 ms (Module 11)."""
import json
from pathlib import Path
import numpy as np

CAP, N, SLOTS = 50, 500, 400   # capacity per 100-ms slot, requests, 40 seconds

def simulate(strategy, seed=1):
    rng = np.random.default_rng(seed)
    pending = {0: list(range(N))}          # slot -> request ids arriving
    attempts = np.zeros(N, int)
    done_at = np.full(N, -1)
    load = np.zeros(SLOTS, int)
    for t in range(SLOTS):
        arr = pending.pop(t, [])
        load[t] = len(arr)
        rng.shuffle(arr)
        ok, fail = arr[:CAP], arr[CAP:]
        for r in ok:
            done_at[r] = t
        for r in fail:
            attempts[r] += 1
            if strategy == "fixed":
                wait = 10                                   # always 1 s
            else:
                wait = int(rng.integers(1, 10 * 2 ** min(attempts[r] - 1, 4) + 1))   # full jitter, cap 16 s
            if t + wait < SLOTS:
                pending.setdefault(t + wait, []).append(r)
    return {"load": load.tolist(), "finished": int((done_at >= 0).sum()),
            "last_done_s": float(done_at.max() / 10), "calls": int(load.sum()),
            "p50_done_s": float(np.median(done_at[done_at >= 0]) / 10)}

res = {s: simulate(s) for s in ["fixed", "jitter"]}
Path(__file__).resolve().parents[1].joinpath("research/m11-retry.json").write_text(json.dumps(res))
for s, r in res.items():
    print(s, {k: v for k, v in r.items() if k != "load"}, "max load", max(r["load"]))

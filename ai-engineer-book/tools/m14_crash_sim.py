"""How much work does a crash cost a long run? (Module 14)

A job handles N items one after another. Each item has the same small chance p of the run crashing while it is
handled (a deploy, a timeout, a lost machine). Two ways to recover:
  restart: start again from item 1 after every crash (nothing was saved);
  resume:  start again from the item that crashed (each finished item was saved).
We compute the expected number of items handled before the job is complete, by formula and by simulation.
"""
import json
from pathlib import Path

import numpy as np

P = 1 / 500                       # assumed: one crash in every 500 items
SIZES = [50, 100, 200, 300, 500, 750, 1000, 1250, 1500, 1750, 2000]
rng = np.random.default_rng(14)


def restart_formula(n, p=P):
    return ((1 - p) ** -n - 1) / p          # expected attempts until n successes in a row


def resume_formula(n, p=P):
    return n / (1 - p)                      # every item retried until it passes


def simulate(n, resume, runs=2000):
    total = 0
    for _ in range(runs):
        done = handled = 0
        while done < n:
            handled += 1
            if rng.random() < P:              # crash while handling this item
                done = done if resume else 0
            else:
                done += 1
        total += handled
    return total / runs


res = {"p": P, "sizes": SIZES,
       "restart": [restart_formula(n) for n in SIZES], "resume": [resume_formula(n) for n in SIZES],
       "restart_sim_2000": simulate(2000, False, runs=400), "resume_sim_2000": simulate(2000, True),
       "clean_run_2000": (1 - P) ** 2000}
Path(__file__).resolve().parents[1].joinpath("research/m14-crash.json").write_text(json.dumps(res, indent=1))
print(f"2,000 items: restart {res['restart'][-1]:,.0f} (sim {res['restart_sim_2000']:,.0f}), "
      f"resume {res['resume'][-1]:,.0f} (sim {res['resume_sim_2000']:,.0f}), "
      f"chance of no crash {res['clean_run_2000']:.1%}")

# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 13 · Agents: Observe, Decide, Act
#
# *Decide, Don't Generate*, Chapter 13. The agent, the LLM and Jev are all synthetic stand-ins.
#
# 1. Run the book's SOC agent on one alert and read its trace.
# 2. Count what kinds of steps it takes over many alerts.
# 3. See how errors and latency compound over steps.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2", "autograd",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
from collections import Counter
from jevkit import soc
from jevkit.agent import SOCAgent

alerts = soc.load()
agent = SOCAgent()
trace = agent.run(next(alerts.iloc[[3]].itertuples()))
for s in trace.steps:
    print(f"{s.kind:>8}  {s.name:<18} {s.detail}")
print("door:", trace.action)

# %%
traces = [agent.run(row) for row in alerts.head(300).itertuples()]
kinds = Counter(s.kind for t in traces for s in t.steps)
print({k: round(v / len(traces), 2) for k, v in kinds.items()})
print(Counter(t.action for t in traces))

# %% [markdown]
# ## Compounding

# %%
for per_step in (0.99, 0.95, 0.90):
    print(per_step, [round(per_step ** n, 2) for n in (5, 10, 20)])

# %% [markdown]
# **Try:** set `SOCAgent(max_evidence=1)` and rerun. How do the step counts and the doors change?

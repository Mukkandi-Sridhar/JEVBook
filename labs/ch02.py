# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 2 · Probability is the language of decisions
#
# *Decide, Don't Generate*, Chapter 2. Synthetic data throughout.
#
# 1. Conditional probability: "among alerts like this one".
# 2. The base-rate trap, with natural frequencies.
# 3. Bayes' rule as "multiply the odds".
# 4. Precision, recall, and why accuracy lies.
# 5. How much a small sample can wobble.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import numpy as np
from jevkit import soc

alerts = soc.load()
y = alerts.malicious
print(f"P(attack)                        = {y.mean():.3f}")
bad = alerts.ioc_score >= 0.7
print(f"P(attack | threat-intel >= 0.7)  = {y[bad].mean():.3f}")
print(f"P(threat-intel >= 0.7 | attack)  = {bad[y == 1].mean():.3f}")

# %% [markdown]
# Notice the last two lines are *different questions* with different answers.

# %% [markdown]
# ## The base-rate trap

# %%
def p_real_given_alert(base_rate, hit_rate, false_alarm_rate):
    real = base_rate * hit_rate
    false = (1 - base_rate) * false_alarm_rate
    return real / (real + false)

for base in (0.001, 0.01, 0.076, 0.3):
    print(f"base rate {base:>6.1%}: P(real | alert) = {p_real_given_alert(base, 0.99, 0.05):.1%}")

# %% [markdown]
# ## Bayes' rule: multiply the odds

# %%
def likelihood_ratio(mask):
    return mask[y == 1].mean() / mask[y == 0].mean()

odds = y.mean() / (1 - y.mean())
for name, mask in [("bad threat intel", alerts.ioc_score >= 0.7),
                   ("after hours", alerts.after_hours),
                   ("new country", alerts.new_geo)]:
    lr = likelihood_ratio(mask)
    odds *= lr
    print(f"{name:>17}: x{lr:4.1f}  ->  P = {odds / (1 + odds):.0%}")

both = (alerts.ioc_score >= 0.7) & alerts.after_hours
print(f"\nreality for the first two clues together: {y[both].mean():.0%} (n={both.sum()})")

# %% [markdown]
# ## Precision, recall, accuracy

# %%
flag = alerts.ioc_score >= 0.5
tp = (flag & (y == 1)).sum(); fp = (flag & (y == 0)).sum()
fn = (~flag & (y == 1)).sum(); tn = (~flag & (y == 0)).sum()
print(f"precision {tp / (tp + fp):.0%}  recall {tp / (tp + fn):.0%}  accuracy {(tp + tn) / len(y):.0%}")
print(f"'never alert' accuracy: {1 - y.mean():.0%}")

# %% [markdown]
# ## Small samples wobble

# %%
rng = np.random.default_rng(0)
for n in (20, 100, 1000):
    draws = [y.sample(n, random_state=int(s)).mean() for s in rng.integers(0, 10**6, 5)]
    print(n, [f"{d:.0%}" for d in draws])

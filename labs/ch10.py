# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 10 · How an LLM writes, one token at a time
#
# *Decide, Don't Generate*, Chapter 10. Toy models only; `llm-mock-synthetic` is not a real LLM.
#
# 1. Train a tiny tokenizer (byte-pair encoding) and see how text gets chopped.
# 2. Generate text one token at a time from a trigram model, at different temperatures.
# 3. Ask a mock LLM the same question 20 times and count the disagreements.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2", "autograd",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
from jevkit import llm, text

notes = [" ".join(n) for n in text.notes_corpus(5000)]
tok = llm.BPE().fit(notes, merges=150)
for s in ["the ransomware was quarantined", "passw0rd reset", "2026-09-14"]:
    t = tok.tokenize(s)
    print(f"{len(t):2d} tokens  {t}")

# %% [markdown]
# ## The generation loop

# %%
lm = llm.TrigramLM().fit(text.notes_corpus(30000))
dist = lm.next_distribution("the", "phishing")
print(sorted(dist.items(), key=lambda kv: -kv[1])[:5])

for T in (0, 0.7, 1.5):
    for seed in range(2):
        words = [w for w, p in lm.generate(["the", "phishing"], temperature=T, seed=seed)]
        print(f"T={T:<3}  the phishing {' '.join(words)}")

# %% [markdown]
# ## Same question, twenty times

# %%
from jevkit import soc
alert = soc.load().description[118]
mock = llm.MockLLM(temperature=0.7)
answers = [mock.classify(alert)["label"] for _ in range(20)]
print(alert[:100], "...")
print({a: answers.count(a) for a in set(answers)})

# %% [markdown]
# **Try:** set `temperature=0` and repeat. Then try other alerts. Which ones flip the most?

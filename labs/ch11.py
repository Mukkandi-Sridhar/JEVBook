# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 11 · Structured outputs and JSON mode
#
# *Decide, Don't Generate*, Chapter 11. `llm-mock-synthetic` and `jev-mock-synthetic` are synthetic.
#
# 1. Ask a (mock) LLM for JSON and count what comes back.
# 2. Validate strictly with pydantic; retry; fail safe.
# 3. Compare three "confidences" on the same alerts.
# 4. Ask the same thing as a typed question through the TypeSafe SDK.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2", "autograd",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import json
from typing import Literal
from pydantic import BaseModel, ConfigDict, ValidationError
from jevkit import soc, llm

class Verdict(BaseModel):
    model_config = ConfigDict(extra="forbid")          # unknown fields are an error
    verdict: Literal["malicious", "benign"]
    confidence: float
    rule: str
    threat_intel_score: float
    after_hours: bool
    related_alerts: int

def parse(raw: str) -> Verdict | None:
    try:
        return Verdict.model_validate_json(raw)
    except ValidationError:
        return None

alerts = soc.load()
train, calib, test = soc.split(alerts)
mock = llm.MockLLM()
results = [parse(mock.structured(t)) for t in test.description]
print(f"valid: {sum(r is not None for r in results):,} of {len(results):,}")

# %%
def ask_with_retry(text, tries=2):
    for attempt in range(tries):
        v = parse(llm.MockLLM(json_mode=attempt > 0).structured(text))
        if v is not None:
            return v
    return None                                        # caller must fail safe (send to review)

bad = [t for t, r in zip(test.description, results) if r is None][:3]
for t in bad:
    print(ask_with_retry(t))

# %% [markdown]
# ## Three confidences

# %%
import numpy as np
from jevkit import calibration as cal
from jevkit.batch import score_alerts

y = test.malicious.to_numpy()
verbal = []
for t in test.description:
    r = mock.classify(t)
    verbal.append(r["confidence"] if r["label"] == "malicious" else 1 - r["confidence"])
token = [mock.label_token_prob(t) for t in test.description]
alerts["p_text"] = score_alerts(alerts, "text")
jev = soc.split(alerts)[2].p_text          # same test alerts, same raw text

for name, p in (("stated in JSON", verbal), ("first-token prob", token), ("decision model", jev)):
    s = cal.summary(np.asarray(p), y)
    print(f"{name:>16}: AUC {s['auc']:.3f}  ECE {s['ece']:.3f}")

# %% [markdown]
# ## The typed version

# %%
from typesafe_sdk import Choice, Noul, TypeSafeClient
from jevkit import MockJevTransport

client = TypeSafeClient(api_key="mock", transport=MockJevTransport())
r = client.system_one(state=test.description.iloc[0], questions={
    "attack": Noul(instructions="Is this alert a real attack?"),
    "kind": Choice(criteria={c: None for c in soc.CATEGORIES}),
})
print(r.nouls["attack"].noul, r.choices["kind"].choice, r.choices["kind"].probabilities)

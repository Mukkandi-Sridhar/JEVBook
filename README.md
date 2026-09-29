# Decide, Don't Generate

*Jev, System One Models, and the Decision Layer of Agentic AI*: the source of the book, its labs and `jevkit`.

- `chapters/`, `parts/`, `front/`, `back/`: the book, in Quarto markdown
- `jevkit/`: the companion toolkit
  - `MockJevTransport`: a deterministic, **synthetic** stand-in for the Jev API that plugs into the official
    `typesafe_sdk.TypeSafeClient(transport=...)`. The model answers as `jev-mock-synthetic`.
  - `soc`: the synthetic Kestrel Logistics SOC alert generator (known true probabilities)
  - `calibration`, `policy`: reliability diagrams, ECE/Brier, Platt/temperature/isotonic, act/review/escalate
  - `figs`: the book's figure system
- `labs/`: one notebook per chapter (`chNN.py` source, `chNN.ipynb` for Colab)
- `figures/src/`: the code behind every figure; `figures/chNN/` the generated PDF + SVG
- `site/`: companion widgets (calibration playground, threshold simulator, bake-off explorer, cost calculator)

```python
from typesafe_sdk import Choice, TypeSafeClient
from jevkit import MockJevTransport

client = TypeSafeClient(api_key="mock", transport=MockJevTransport())
r = client.system_one(
    state="I was charged twice. Please fix this ASAP.",
    questions={"category": Choice(criteria={"billing": None, "technical": None, "other": None})},
)
print(r.choices["category"])
```

**Every Jev number in this repository is synthetic: not measured on real Jev.** See `DECISIONS.md`.

## Build

```bash
pip install -r requirements.txt && pip install -e .
make fonts      # install the book fonts (OFL)
make test       # jevkit tests
make figures    # rebuild every figure from code
make labs       # execute every notebook in mock mode
make pdf        # 7x10in print PDF (needs LuaLaTeX)
make html       # web edition
```

Progress and resume notes: `PROGRESS.md`. Every judgement call: `DECISIONS.md`.

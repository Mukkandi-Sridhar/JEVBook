"""Two calculations for Module 16, saved to research/m16-numbers.json.

1. Memory to fine-tune an 8-billion-parameter model (shapes of Llama 3 8B: 32 layers, width 4096, MLP width 14336,
   keys and values 1024 wide), not counting activations, which grow with sequence length and batch size.
   Full fine-tuning with Adam in mixed precision: 16 bytes per parameter (weights 2, gradients 2, fp32 master
   weights 4, two Adam moments 8). LoRA: frozen weights at 2 bytes, plus 16 bytes per adapter parameter.
   QLoRA: frozen weights in 4 bits (0.5 bytes, plus about 0.03 bytes of scaling constants), plus the adapters.
2. Monthly cost of an API against renting GPUs, by messages a day. All prices are assumptions, stated below.
"""
import json
from pathlib import Path

P = 8.03e9
LAYERS, D, MLP, KV, R = 32, 4096, 14336, 1024, 16
adapter = LAYERS * R * ((D + D) + (D + KV) * 2 + (D + D) + (D + MLP) * 2 + (MLP + D))   # q,k,v,o,gate,up,down
GB = 1e9
memory = {"full": P * 16 / GB, "lora": (P * 2 + adapter * 16) / GB, "qlora": (P * 0.53 + adapter * 16) / GB,
          "adapter_params": adapter, "adapter_share": adapter / P}

API_PER_MESSAGE = 1.17            # rupees, the cached reply of Section 15.8
GPU_HOUR = 250                    # rupees per GPU-hour, assumed
PER_GPU = 15_000                  # messages a day one GPU serves at the needed speed, assumed
PEOPLE = 1_50_000                 # rupees a month: half an engineer's time to run it, assumed
OTHER = 20_000                    # monitoring, storage, network, assumed


def self_hosted(per_day):
    gpus = max(2, -(-per_day // PER_GPU))         # never fewer than two, so one can fail
    return gpus * GPU_HOUR * 24 * 30 + PEOPLE + OTHER


days = list(range(0, 50_001, 1000))
cost = {"per_day": days, "api": [API_PER_MESSAGE * d * 30 for d in days], "own": [self_hosted(d) for d in days]}
cross = next(d for d, a, o in zip(days, cost["api"], cost["own"]) if a > o)
Path(__file__).resolve().parents[1].joinpath("research/m16-numbers.json").write_text(
    json.dumps({"memory": memory, "cost": cost, "crossover": cross,
                "assumptions": {"api_per_message": API_PER_MESSAGE, "gpu_hour": GPU_HOUR, "per_gpu": PER_GPU,
                                "people": PEOPLE, "other": OTHER}}, indent=1))
print({k: round(v, 3) if isinstance(v, float) else v for k, v in memory.items()})
print("crossover near", cross, "messages a day;", "at 4,000:", round(cost["api"][4]), "vs", self_hosted(4000),
      "; at 40,000:", round(cost["api"][40]), "vs", self_hosted(40000))

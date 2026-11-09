"""Why the batch takes three hours: 2,000 checks, one at a time or many at once (Module 15).

A stand-in service answers each check after a random delay (median 5 s, as for a short agent run) and allows at
most 120 requests a minute; above that it refuses with 429 "too many requests". The client runs up to C checks at
once with an asyncio.Semaphore and retries a 429 after a random wait. Real asyncio code runs against the
stand-in, with every delay shrunk 400 times, so the measurement takes about a minute; times are reported at full
scale.
"""
import asyncio
import json
import random
import time
from pathlib import Path

N, SCALE = 2000, 1 / 400
RATE = 120 / 60                  # requests allowed per second
rng = random.Random(15)


class Service:
    def __init__(self):
        self.tokens, self.last = 2.0, time.monotonic()
        self.refused = 0

    async def check(self):
        now = time.monotonic()
        self.tokens = min(2.0, self.tokens + (now - self.last) / SCALE * RATE)   # token bucket, burst of 2
        self.last = now
        if self.tokens < 1:
            self.refused += 1
            return 429
        self.tokens -= 1
        await asyncio.sleep(rng.lognormvariate(1.609, 0.4) * SCALE)            # median 5 s
        return 200


async def run(concurrency):
    service, limit = Service(), asyncio.Semaphore(concurrency)

    async def one():
        async with limit:
            attempt = 0
            while await service.check() == 429:
                attempt += 1
                await asyncio.sleep(rng.uniform(0, min(30, 2 ** attempt)) * SCALE)

    start = time.monotonic()
    await asyncio.gather(*(one() for _ in range(N)))
    return {"concurrency": concurrency, "minutes": (time.monotonic() - start) / SCALE / 60,
            "refused": service.refused}


res = [asyncio.run(run(c)) for c in [1, 2, 4, 8, 16, 32, 64]]
Path(__file__).resolve().parents[1].joinpath("research/m15-concurrency.json").write_text(json.dumps(res, indent=1))
for r in res:
    print(f"{r['concurrency']:3d} at once: {r['minutes']:6.1f} minutes, {r['refused']:5d} refused")

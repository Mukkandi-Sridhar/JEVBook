import asyncio, sys, time

DELAY = float(sys.argv[1]) if len(sys.argv) > 1 else 3

async def ask_model(message):          # stand-in for a real model call
    await asyncio.sleep(DELAY)         # the time spent waiting for the reply
    return "refund"

async def classify_all(messages, limit=20):
    gate = asyncio.Semaphore(limit)
    async def one(m):
        async with gate:
            return await ask_model(m)
    return await asyncio.gather(*(one(m) for m in messages))

t = time.time()
results = asyncio.run(classify_all(["paisa wapas karo"] * 100))
print(len(results), round(time.time() - t, 2))

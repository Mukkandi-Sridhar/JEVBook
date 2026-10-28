import random, time

RETRYABLE = {429, 500, 503, 529}

def call_with_retry(send, max_attempts=5):
    for attempt in range(max_attempts):
        if attempt > 0:
            time.sleep(random.uniform(0, 2 ** (attempt - 1)))   # full jitter
        status, body = send()
        if status == 200:
            return body
        if status not in RETRYABLE:
            raise RuntimeError(f"Not retryable: {status}")
    raise RuntimeError("Gave up after retries")

if __name__ == "__main__":
    replies = iter([(429, None), (529, None), (200, "refund")])
    print(call_with_retry(lambda: next(replies)))
    try:
        call_with_retry(lambda: (401, None))
    except RuntimeError as e:
        print(e)

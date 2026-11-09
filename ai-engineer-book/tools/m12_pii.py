"""How well does a checksum separate Aadhaar numbers from other 12-digit numbers? (Module 12)

Three kinds of input, 100,000 of each, all random and none belonging to anyone:
  1. numbers in the Aadhaar format: 12 digits, first digit 2-9, last digit the Verhoeff check digit;
  2. the same numbers with one digit mistyped, or two neighbouring digits swapped;
  3. other 12-digit numbers starting 2-9, standing in for UPI reference numbers and phone numbers written with 91.
Two detectors: the pattern alone (12 digits, first digit 2-9), and the pattern plus python-stdnum's Aadhaar check.
Only counts are saved; no generated number is written anywhere.
"""
import json
import random
from pathlib import Path

from stdnum import verhoeff
from stdnum.in_ import aadhaar

N = 100_000
rng = random.Random(12)


def aadhaar_format():
    body = str(rng.randint(2, 9)) + "".join(str(rng.randint(0, 9)) for _ in range(10))
    return body + verhoeff.calc_check_digit(body)


def mistyped(n):
    d = list(n)
    if rng.random() < 0.5:                       # one digit typed wrong
        i = rng.randrange(1, 12)                 # keep the first digit, so the pattern still matches
        d[i] = rng.choice([c for c in "0123456789" if c != d[i]])
    else:                                        # two neighbouring digits swapped
        i = rng.randrange(1, 11)
        while d[i] == d[i + 1]:
            i = rng.randrange(1, 11)
        d[i], d[i + 1] = d[i + 1], d[i]
    return "".join(d)


def other_number():
    return str(rng.randint(2, 9)) + "".join(str(rng.randint(0, 9)) for _ in range(11))


def pattern(n):
    return len(n) == 12 and n.isdigit() and n[0] not in "01"


kinds = {"aadhaar": [aadhaar_format() for _ in range(N)]}
kinds["mistyped"] = [mistyped(n) for n in kinds["aadhaar"]]
kinds["other"] = [other_number() for _ in range(N)]

res = {k: {"n": N, "pattern": sum(map(pattern, v)) / N,
           "checksum": sum(pattern(n) and aadhaar.is_valid(n) for n in v) / N}
       for k, v in kinds.items()}
Path(__file__).resolve().parents[1].joinpath("research/m12-pii.json").write_text(json.dumps(res, indent=1))
for k, r in res.items():
    print(f"{k:9s} pattern {r['pattern']:.1%}  pattern+checksum {r['checksum']:.2%}")

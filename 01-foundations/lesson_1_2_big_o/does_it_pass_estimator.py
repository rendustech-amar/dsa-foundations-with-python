"""Lesson 1.2 - Practice: will my solution pass or time out?

Rule of thumb from the lesson: Python does about 10^7 simple operations per
second. Change TIME_LIMIT_SECONDS to match the platform you practise on.
"""

import math

OPS_PER_SECOND = 10**7
TIME_LIMIT_SECONDS = 3

COMPLEXITIES = {
    "O(log n)": lambda n: math.log2(n),
    "O(n)": lambda n: n,
    "O(n log n)": lambda n: n * math.log2(n),
    "O(n^2)": lambda n: n**2,
    "O(n^3)": lambda n: n**3,
}


def estimate(complexity, n):
    """Return (steps, seconds, passes) for a complexity at input size n."""
    steps = COMPLEXITIES[complexity](n)
    seconds = steps / OPS_PER_SECOND
    return steps, seconds, seconds <= TIME_LIMIT_SECONDS


def show(n_values):
    print(f"Limit: {TIME_LIMIT_SECONDS}s at {OPS_PER_SECOND:.0e} ops/second\n")
    for n in n_values:
        print(f"n = {n:,}")
        for name in COMPLEXITIES:
            steps, seconds, ok = estimate(name, n)
            verdict = "PASS" if ok else "TIMEOUT"
            print(f"  {name:<11} ~{steps:>10.2e} steps  ~{seconds:>12.4f} s  {verdict}")
        print()


if __name__ == "__main__":
    # The three sizes from the lesson practice: 10^4, 10^5 and 10^6
    show([10**4, 10**5, 10**6])

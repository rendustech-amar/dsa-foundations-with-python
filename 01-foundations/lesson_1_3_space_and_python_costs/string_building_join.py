"""Lesson 1.3 - Building strings: `s += c` in a loop versus collect and join.

Strings are immutable, so `+=` may copy the whole string on every step
(up to O(n^2) total). Collecting pieces in a list and calling "".join once
is O(n) overall.

Note: CPython sometimes optimises `s += c`, so the gap can look small on your
machine. Do not rely on that optimisation, and it does not exist in many
other Python implementations or when the string is referenced elsewhere.
"""

import time

N = 200_000


def build_with_plus(n):
    result = ""
    for _ in range(n):
        result += "a"
    return result


def build_with_join(n):
    parts = []
    for _ in range(n):
        parts.append("a")
    return "".join(parts)


def timed(func, n):
    start = time.perf_counter()
    out = func(n)
    return time.perf_counter() - start, out


if __name__ == "__main__":
    t_plus, a = timed(build_with_plus, N)
    t_join, b = timed(build_with_join, N)
    assert a == b
    print(f"Building a string of {N:,} characters")
    print(f"  s += c      : {t_plus:.4f} s")
    print(f"  list + join : {t_join:.4f} s")

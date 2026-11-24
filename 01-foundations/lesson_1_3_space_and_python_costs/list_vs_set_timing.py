"""Lesson 1.3 - Speed demonstration: `x in list` versus `x in set`.

The lesson idea: check membership many times in 100,000 numbers.
A full 100,000 checks on the list takes minutes, so CHECKS defaults to a
smaller number. Both sides use the same number of checks, so the comparison
is fair. Raise CHECKS if you want to wait for the full demo.
"""

import random
import time

N = 100_000        # size of the data
CHECKS = 2_000     # how many membership checks to run (try 100_000 for the full demo)


def time_checks(container, queries):
    start = time.perf_counter()
    found = 0
    for q in queries:
        if q in container:
            found += 1
    return time.perf_counter() - start, found


if __name__ == "__main__":
    random.seed(1)
    data_list = list(range(N))
    data_set = set(data_list)
    # Worst case for the list: values near the end, or missing (full scan)
    queries = [random.randint(0, 2 * N) for _ in range(CHECKS)]

    t_list, found_list = time_checks(data_list, queries)
    t_set, found_set = time_checks(data_set, queries)
    assert found_list == found_set

    print(f"{CHECKS:,} membership checks in {N:,} numbers")
    print(f"  list : {t_list:.4f} s   (O(n) per check)")
    print(f"  set  : {t_set:.6f} s   (O(1) average per check)")
    print(f"  set is about {t_list / t_set:,.0f}x faster")

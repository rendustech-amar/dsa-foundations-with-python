"""Lesson 1.3 - Practice: replace a slow pop(0) loop with deque.popleft()."""

import time
from collections import deque

N = 100_000


def drain_with_list(n):
    """list.pop(0) shifts every remaining element: O(n) each, O(n^2) total."""
    queue = list(range(n))
    while queue:
        queue.pop(0)


def drain_with_deque(n):
    """deque.popleft() is O(1) each, O(n) total."""
    queue = deque(range(n))
    while queue:
        queue.popleft()


def timed(func, n):
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start


if __name__ == "__main__":
    t_list = timed(drain_with_list, N)
    t_deque = timed(drain_with_deque, N)
    print(f"Removing {N:,} items from the front")
    print(f"  list.pop(0)      : {t_list:.4f} s")
    print(f"  deque.popleft()  : {t_deque:.4f} s")
    print(f"  deque is about {t_list / t_deque:,.0f}x faster")

"""Lesson 1.3 - Practice: time and space complexity of 5 short functions.

Space means AUXILIARY space: extra memory beyond the input itself.
"""

import sys


def sum_list(nums):
    """Time O(n), space O(1): a single running total."""
    total = 0
    for x in nums:
        total += x
    return total


def doubled(nums):
    """Time O(n), space O(n): builds a brand new list of n items."""
    return [x * 2 for x in nums]


def make_grid(n):
    """Time O(n^2), space O(n^2): an n x n grid."""
    return [[0] * n for _ in range(n)]


def factorial(n):
    """Time O(n), space O(n): n calls wait on the call stack."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def reverse_in_place(nums):
    """Time O(n), space O(1): swaps inside the input, no new list."""
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


if __name__ == "__main__":
    print("sum_list([1,2,3])        =", sum_list([1, 2, 3]))
    print("doubled([1,2,3])         =", doubled([1, 2, 3]))
    print("make_grid(3)             =", make_grid(3))
    print("factorial(5)             =", factorial(5))
    print("reverse_in_place([1,2,3])=", reverse_in_place([1, 2, 3]))

    print("\nRecursion depth is space. Default limit:", sys.getrecursionlimit())
    try:
        factorial(5000)
    except RecursionError:
        print("factorial(5000) -> RecursionError (stack too deep)")

    print("""
Summary
  function          time     space
  sum_list          O(n)     O(1)
  doubled           O(n)     O(n)
  make_grid         O(n^2)   O(n^2)
  factorial         O(n)     O(n)   (call stack)
  reverse_in_place  O(n)     O(1)""")

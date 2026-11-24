"""Lesson 1.1 - Practice: find the largest and second largest in a list.

"Second largest" here means the next smaller DISTINCT value.
If there is no such value (single element, all equal), it is None.
"""


def largest_and_second_largest_brute_force(nums):
    """Sort the distinct values. Time O(n log n), space O(n)."""
    if not nums:
        raise ValueError("list is empty")
    unique = sorted(set(nums), reverse=True)
    second = unique[1] if len(unique) > 1 else None
    return unique[0], second


def largest_and_second_largest(nums):
    """One pass, two variables. Time O(n), space O(1)."""
    if not nums:
        raise ValueError("list is empty")
    largest = float("-inf")
    second = float("-inf")
    for x in nums:
        if x > largest:
            second = largest
            largest = x
        elif largest > x > second:
            second = x
    if second == float("-inf"):
        second = None
    return largest, second


if __name__ == "__main__":
    tests = [
        [3, 9, 2, 7],      # normal
        [-5, -1, -8],      # negatives
        [4, 4, 4],         # all equal -> no second largest
        [9],               # single element
        [1, 2, 3, 4, 5],   # sorted
        [5, 4, 3, 2, 1],   # reverse sorted
        [8, 8, 5, 5],      # duplicates
    ]
    for nums in tests:
        fast = largest_and_second_largest(nums)
        slow = largest_and_second_largest_brute_force(nums)
        assert fast == slow, (nums, fast, slow)
        print(nums, "->", fast)

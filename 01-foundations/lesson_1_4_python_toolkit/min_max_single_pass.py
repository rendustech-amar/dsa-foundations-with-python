"""Lesson 1.4 - Warm-up 5: minimum and maximum in a single pass."""


def min_max(nums):
    """One loop, two variables. Time O(n), space O(1).

    Starts from float("inf") and float("-inf") so any real number beats them.
    Raises ValueError for an empty list.
    """
    if not nums:
        raise ValueError("list is empty")
    smallest = float("inf")
    biggest = float("-inf")
    for x in nums:
        if x < smallest:
            smallest = x
        if x > biggest:
            biggest = x
    return smallest, biggest


if __name__ == "__main__":
    tests = [[3, 9, 2], [-5, -1, -8], [7], [4, 4, 4], [1, 2, 3, 4, 5]]
    for nums in tests:
        assert min_max(nums) == (min(nums), max(nums))
        print(nums, "->", min_max(nums))
    try:
        min_max([])
    except ValueError as err:
        print("[] ->", err)

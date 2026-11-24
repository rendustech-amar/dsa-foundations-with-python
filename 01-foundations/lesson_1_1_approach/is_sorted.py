"""Lesson 1.1 - Example B: check whether a list is sorted (ascending)."""


def is_sorted_brute_force(nums):
    """Sort a copy and compare.

    Time O(n log n), extra space O(n).
    """
    return nums == sorted(nums)


def is_sorted(nums):
    """Scan once and stop at the first violation.

    Time O(n), space O(1).
    """
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], True),
        ([1, 3, 2, 4], False),
        ([], True),             # empty
        ([5], True),            # single element
        ([2, 2, 2], True),      # all equal
        ([5, 4, 3], False),     # reverse sorted
        ([-3, -1, 0, 2], True), # negatives and zero
    ]
    for nums, expected in tests:
        assert is_sorted(nums) == is_sorted_brute_force(nums) == expected
        print(nums, "->", is_sorted(nums))
